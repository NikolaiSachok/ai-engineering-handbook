#!/usr/bin/env python3
"""Analyser behind scripts/locale-parity-check.sh — see that file for the WHY.

This module holds the extraction and comparison logic only. It is Python rather than more shell
because every check here turns on Unicode-aware text normalisation (non-breaking and thin spaces
as digit-group separators, decimal commas, Cyrillic word boundaries) and on set/multiset algebra.
The gate itself stays a shell script beside the other gates; this is the part that would have been
fragile in sed.

Prints findings to stdout; exits 0 when every locale is in parity, 1 otherwise.
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter

# The English source dir -> the i18n plugin dir that translates it. The FIRST course is the preset
# docs instance, whose i18n dir is UN-suffixed; every other course is a plugin instance with an
# `-<id>` suffix (see the COURSES block in docusaurus.config.ts). Adding a course = a pair here.
COURSE_PAIRS = [
    ("docs", "docusaurus-plugin-content-docs"),
    ("docs-ai-sdlc", "docusaurus-plugin-content-docs-ai-sdlc"),
]

# The MDX components whose silent loss is invisible in prose. `<Node` is counted bare rather than as
# `<Node label=`: every node in this corpus writes `icon` before `label`, so matching the literal
# `<Node label=` would count zero everywhere and quietly assert nothing.
COMPONENTS = ["<InfoCard", "<Node", "<YouTube"]

# Fence languages a locale may legitimately drop entirely, because their content is prose in a
# monospace box and a locale may inline it instead (RU renders two English ```text formula blocks as
# inline code inside a numbered list). Every other language must appear the same number of times:
# a dropped ```mermaid is a lost diagram and a dropped ```bash is a lost copyable command.
COUNT_EXEMPT_FENCES = {"text", "(none)"}

# Digit-group separators seen in this corpus: plain space, NBSP, narrow NBSP, thin space, figure space.
SEP = "[     ]"


# --------------------------------------------------------------------------- extraction

def read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def strip_frontmatter(text: str) -> str:
    """Drop the YAML block. Its titles/descriptions are translated by design, and the fields that
    must match (id, sidebar_position) are already enforced by the build's sidebar assembly."""
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)


def headings(text: str, max_level: int = 2) -> list[int]:
    """The heading LEVEL sequence — text is translated, that is the point of a translation.

    Only H1 and H2 count. See the .sh header for the measurement behind that cut-off: at full depth
    the natively-authored locales diverge on `###` subdivision in a way that is editorial, not
    defective; H2 is the page's section contract (sidebar, right-hand TOC, the canon's book units).
    """
    out, fence = [], False
    for line in strip_frontmatter(text).splitlines():
        if re.match(r"^ *(```|~~~)", line):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r"^(#{1,6}) ", line)
        if m and len(m.group(1)) <= max_level:
            out.append(len(m.group(1)))
    return out


def components(text: str) -> dict[str, int]:
    return {tag: text.count(tag) for tag in COMPONENTS}


def fences(text: str) -> list[tuple[str, str]]:
    """Every fenced block as (language, body). Unlabelled fences report as '(none)'."""
    out, lang, buf = [], None, []
    for line in text.splitlines(keepends=True):
        m = re.match(r"^ *(?:```|~~~)(.*)$", line)
        if m:
            if lang is None:
                lang = m.group(1).strip() or "(none)"
                buf = []
            else:
                out.append((lang, "".join(buf)))
                lang = None
            continue
        if lang is not None:
            buf.append(line)
    return out


def numeric_tokens(text: str) -> set[str]:
    """Percentages and decimal figures, normalised across locale number punctuation.

    Scope and normalisation are both deliberate; the .sh header carries the measurements. Excluded
    before extraction because they are not prose figures: fenced code (compared separately), URLs and
    link targets, arXiv ids, explicit heading anchors, and years/decades (locales write dates their
    own way). Bare integers are excluded too — in this corpus they are overwhelmingly cross-reference
    ordinals ("Part 2", "hop 3"), HTTP status codes and counts that each locale words differently.
    """
    t = strip_frontmatter(text)
    t = re.sub(r"(?ms)^ *(```|~~~).*?^ *(```|~~~) *$", "", t)   # fenced code
    t = re.sub(r'https?://[^ )"]*', "", t)                       # URLs
    t = re.sub(r"\]\([^)]*\)", "]()", t)                         # link targets
    t = re.sub(r"\{#[^}]*\}", "", t)                             # explicit heading anchors
    t = re.sub(r"\d{4}\.\d{4,5}", "", t)                         # arXiv ids
    t = re.sub(r"\b(19|20)\d{2}s?(?!\d)", "", t)                 # years and decades
    t = re.sub(r"(\d)" + SEP + r"(\d{3})(?!\d)", r"\1\2", t)      # 10 000 -> 10000
    t = re.sub(r"([1-9]\d{0,2}),(\d{3})(?!\d)", r"\1\2", t)       # 10,000 -> 10000
    t = re.sub(r"(\d),(\d)", r"\1.\2", t)                         # 0,95   -> 0.95

    out = set()
    for m in re.finditer(r"(\d+(?:\.\d+)?)" + SEP + r"?(%)?", t):
        num, unit = m.group(1), m.group(2)
        if unit == "%":
            out.add(num + "%")
        elif "." in num:
            out.add(num)
    return out


def unit_class(token: str) -> str:
    return "%" if token.endswith("%") else "decimal"


# --------------------------------------------------------------------------- comparison

class Report:
    def __init__(self) -> None:
        self.failures = 0
        self.checked = 0
        self.categories = 0  # sidebar category labels, counted apart from files
        self.tolerated = 0

    def fail(self, message: str) -> None:
        self.failures += 1
        print()
        print(f"locale-parity-check: FAIL — {message}")


def md_files(root: str) -> set[str]:
    out = set()
    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            if name.endswith(".md"):
                out.add(os.path.relpath(os.path.join(dirpath, name), root))
    return out


def compare_pair(locale: str, src: str, tgt: str, rep: Report) -> None:
    if not os.path.isdir(tgt):
        print(f"  - {src}: no {tgt} — locale does not translate this course")
        return

    en_files, loc_files = md_files(src), md_files(tgt)

    # 1. file set
    if en_files - loc_files:
        rep.fail(f"{locale}/{src} — page(s) present in English, missing in {locale}:")
        for p in sorted(en_files - loc_files):
            print(f"    - {p}")
    if loc_files - en_files:
        rep.fail(f"{locale}/{src} — page(s) present in {locale} with no English source:")
        for p in sorted(loc_files - en_files):
            print(f"    - {p}")

    for rel in sorted(en_files & loc_files):
        rep.checked += 1
        en, loc = read(os.path.join(src, rel)), read(os.path.join(tgt, rel))
        where = f"{locale}/{src}/{rel}"

        # 2. heading shape
        a, b = headings(en), headings(loc)
        if a != b:
            if len(a) != len(b):
                rep.fail(f"{where} — H1/H2 count differs: en={len(a)} {locale}={len(b)}")
            else:
                rep.fail(f"{where} — H1/H2 level sequence differs (same count, different nesting):")
                print(f"    en:     {a}")
                print(f"    {locale}: {b}")

        # 3. component counts
        ca, cb = components(en), components(loc)
        if ca != cb:
            rep.fail(f"{where} — MDX component counts differ:")
            for tag in COMPONENTS:
                if ca[tag] != cb[tag]:
                    print(f"    {tag}: en={ca[tag]} {locale}={cb[tag]}")

        # 4. fenced blocks — count per language; content is the locale's own (see the .sh header)
        fa, fb = fences(en), fences(loc)
        count_a = Counter(l for l, _ in fa if l not in COUNT_EXEMPT_FENCES)
        count_b = Counter(l for l, _ in fb if l not in COUNT_EXEMPT_FENCES)
        if count_a != count_b:
            rep.fail(f"{where} — fenced block counts differ by language:")
            for lang in sorted(set(count_a) | set(count_b)):
                if count_a[lang] != count_b[lang]:
                    print(f"    ```{lang}: en={count_a[lang]} {locale}={count_b[lang]}")
        rep.tolerated += sum(
            1 for (_, ba), (_, bb) in zip(fa, fb) if ba != bb
        )

        # 5. numeric drift
        na, nb = numeric_tokens(en), numeric_tokens(loc)
        only_en, only_loc = na - nb, nb - na
        classes = {unit_class(t) for t in only_en} & {unit_class(t) for t in only_loc}
        if classes:
            rep.fail(f"{where} — a figure DRIFTED (same kind of quantity, different value):")
            print(f"    only in en:     {sorted(only_en)}")
            print(f"    only in {locale}: {sorted(only_loc)}")
        else:
            rep.tolerated += len(only_en) + len(only_loc)


def category_labels(src: str) -> list[tuple[str, str]]:
    """Every sidebar category label the English tree declares, as (label, source file)."""
    out = []
    for dirpath, _, filenames in os.walk(src):
        if "_category_.json" in filenames:
            path = os.path.join(dirpath, "_category_.json")
            out.append((json.load(open(path, encoding="utf-8"))["label"], path))
    return sorted(out)


def compare_category_keys(locale: str, src: str, current_json: str, rep: Report) -> None:
    """Every sidebar category must have a translation key, and every key a category.

    This is shape, not wording: a category label lives in `current.json` under
    `sidebar.<sidebarId>.category.<English label>`, and a MISSING key does not fail the build
    or the link check — Docusaurus silently serves the English source string. That is how four
    AI-SDLC deep-dive categories shipped untranslated in two released locales.

    The `_category_.json` under `i18n/` is NOT consulted, because it never renders (it is
    overridden by `current.json`); asserting against it would be asserting against a decoy.

    Sidebar id is read off the key rather than configured, so this needs no third column in
    COURSE_PAIRS to keep in sync. A key may also carry sub-fields of a category — e.g.
    `...category.Cross-cutting.link.generated-index.description` — so a key is orphaned only
    when its remainder is neither a label nor a sub-field of one.
    """
    if not os.path.isfile(current_json):
        print(f"  - {src}: no {current_json} — locale does not translate this course")
        return

    labels = category_labels(src)
    known = {label for label, _ in labels}
    data = json.load(open(current_json, encoding="utf-8"))
    translated = {
        m.group(1) for m in (re.match(r"sidebar\.[^.]+\.category\.(.+)", k) for k in data) if m
    }

    missing = [(label, path) for label, path in labels if label not in translated]
    orphans = sorted(
        r for r in translated
        if r not in known and not any(r.startswith(f"{label}.") for label in known)
    )

    if missing:
        rep.fail(f"{locale}/{src} — sidebar category with no translation key "
                 f"(renders in English, silently):")
        for label, path in missing:
            print(f"    {label!r}  declared in {path}")
    if orphans:
        rep.fail(f"{locale}/{src} — translation key for a category that no longer exists "
                 f"(a rename left the new label untranslated):")
        for r in orphans:
            print(f"    {r!r}  in {current_json}")

    rep.categories += len(labels)


def main(argv: list[str]) -> int:
    locales = argv[1:] or sorted(
        d for d in os.listdir("i18n") if os.path.isdir(os.path.join("i18n", d))
    )
    rep = Report()
    for locale in locales:
        if locale == "en":
            continue
        print(f">> {locale}")
        for src, plugin in COURSE_PAIRS:
            compare_pair(locale, src, f"i18n/{locale}/{plugin}/current", rep)
            compare_category_keys(locale, src, f"i18n/{locale}/{plugin}/current.json", rep)

    print()
    if rep.failures == 0:
        print(
            f"locale-parity-check: PASS — {rep.checked} file(s) in structural parity; "
            f"{rep.categories} sidebar category label(s) translated; "
            f"{rep.tolerated} tolerated wording difference(s)."
        )
        return 0

    print(
        f"locale-parity-check: FAIL — {rep.failures} parity defect(s) across "
        f"{rep.checked} file(s) and {rep.categories} category label(s) checked."
    )
    print()
    print("This gate asserts SHAPE, never wording. If a finding is a legitimate translation")
    print("decision rather than a defect, relax that specific check and say why in its comment —")
    print("do not add an ignore list. A gate with an ignore list is a gate nobody reads.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
