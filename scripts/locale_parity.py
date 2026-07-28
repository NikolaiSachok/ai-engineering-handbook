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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from courses import courses  # noqa: E402  (path set above so the gate runs from the repo root)

# The MDX components whose silent loss is invisible in prose. `<Node` is counted bare rather than as
# `<Node label=`: every node in this corpus writes `icon` before `label`, so matching the literal
# `<Node label=` would count zero everywhere and quietly assert nothing.
COMPONENTS = ["<InfoCard", "<Node", "<YouTube"]

# Fence languages a locale may legitimately drop entirely, because their content is prose in a
# monospace box and a locale may inline it instead (RU renders two English ```text formula blocks as
# inline code inside a numbered list). Every other language must appear the same number of times:
# a dropped ```mermaid is a lost diagram and a dropped ```bash is a lost copyable command.
COUNT_EXEMPT_FENCES = {"text", "(none)"}

# The sub-fields a sidebar category key may legitimately carry beyond its label, i.e. the keys of
# the form `sidebar.<id>.category.<label>.<subfield>`. Docusaurus emits exactly these for a
# category with a generated-index link. Matched as a CLOSED SET rather than "anything after a
# known label", so that a typo'd or stale sub-field is reported instead of silently accepted.
CATEGORY_SUBFIELDS = {"link.generated-index.title", "link.generated-index.description"}

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


def heading_anchors(text: str) -> list[str]:
    """The ORDERED sequence of explicit heading ids — `## Some term \\{#some-id}`.

    An explicit id is a cross-locale CONTRACT, not decoration. A lesson's terms footer links to
    `../glossary.md#some-id` and that one link is shared by every locale, so the id has to name
    the same entry in all of them; an auto-slug cannot hold it, because a translated heading
    slugifies to something else entirely (#300, #306).

    ORDER, not just the set, because #306 applied 123 ids across six glossary files BY HEADING
    INDEX. That is correct exactly once. Insert a new entry mid-file in one locale only and every
    id below it shifts by one: each id still exists, the counts still match, the set is still
    equal — and every inbound link into that locale now lands on the neighbouring entry. The
    reader gets a plausible wrong definition, which is the failure mode nobody reports. A sequence
    comparison catches both the insert and the straight swap; a set comparison catches neither.

    The brace is backslash-escaped in source (`\\{#id}`) because `future.v4: true` turns off the
    MDX1 heading-id compat preprocessor and a bare `{` parses as a JSX expression, hard-failing the
    build. The escape is therefore the form on disk — but it is markup, not part of the id, so it
    is matched optionally and stripped: a bare `{#id}` must compare equal to `\\{#id}`, or this
    gate would report a mismatch for two headings that name the same anchor.
    """
    out, fence = [], False
    for line in strip_frontmatter(text).splitlines():
        if re.match(r"^ *(```|~~~)", line):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r"^#{1,6} .*?\\?\{#([^}\s]+)\}\s*$", line)
        if m:
            out.append(m.group(1))
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


def released_locales() -> set[str]:
    """The locales that ship publicly, read from the same constant the build uses.

    A missing translation is a defect for a RELEASED locale and expected for one still being
    scaffolded, so the gate has to know which is which — and the only honest source is
    `RELEASED_LOCALES` in docusaurus.config.ts. Parsing is deliberately strict: if the constant
    ever moves or changes shape this ABORTS rather than falling back to a permissive default,
    because the permissive default is exactly the fail-open this function exists to close.
    """
    config = "docusaurus.config.ts"
    m = re.search(r"const\s+RELEASED_LOCALES\s*=\s*\[(.*?)\]", read(config), re.S)
    if not m:
        sys.exit(
            f"locale-parity-check: ERROR — could not read RELEASED_LOCALES from {config}. "
            "The gate cannot tell a released locale from a scaffolded one, so it refuses to "
            "run rather than pass silently. Fix the parse in released_locales()."
        )
    found = set(re.findall(r"['\"]([\w-]+)['\"]", m.group(1)))
    if not found:
        sys.exit(f"locale-parity-check: ERROR — RELEASED_LOCALES in {config} parsed as empty.")
    return found


def missing_translation(locale: str, released: bool, src: str, path: str, rep: Report) -> None:
    """Report an absent translation target according to the locale's release status.

    Absence used to be reported as "locale does not translate this course" and skipped. That is an
    INFERENCE from a missing file, and it is wrong the moment a locale ships: deleting a whole
    `current.json` (or a whole `current/` tree) for a released locale left every one of that
    course's categories rendering English with the gate still green — the same defect this gate
    was written for, one size up.
    """
    if released:
        rep.fail(
            f"{locale}/{src} — released locale has no {path}. Every course must be translated in "
            f"a locale that ships; absence here means the whole course renders in English."
        )
    else:
        print(f"  - {src}: no {path} — not yet translated ({locale} is gated/unreleased)")


def compare_pair(locale: str, released: bool, src: str, tgt: str, rep: Report) -> None:
    if not os.path.isdir(tgt):
        missing_translation(locale, released, src, tgt, rep)
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

        # 3. explicit heading anchors — the ordered id sequence (see heading_anchors())
        aa, ab = heading_anchors(en), heading_anchors(loc)
        if aa != ab:
            rep.fail(f"{where} — explicit heading id sequence differs (inbound "
                     f"`#anchor` links into {locale} would land on the wrong heading):")
            gone = [i for i in aa if i not in ab]
            extra = [i for i in ab if i not in aa]
            if gone:
                print(f"    missing in {locale}: {gone}")
            if extra:
                print(f"    only in {locale}:    {extra}")
            if not gone and not extra:
                print(f"    same ids, different ORDER — first divergence at index "
                      f"{next(i for i, (x, y) in enumerate(zip(aa, ab)) if x != y)}:")
                print(f"    en:     {aa}")
                print(f"    {locale}: {ab}")

        # 4. component counts
        ca, cb = components(en), components(loc)
        if ca != cb:
            rep.fail(f"{where} — MDX component counts differ:")
            for tag in COMPONENTS:
                if ca[tag] != cb[tag]:
                    print(f"    {tag}: en={ca[tag]} {locale}={cb[tag]}")

        # 5. fenced blocks — count per language; content is the locale's own (see the .sh header)
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

        # 6. numeric drift
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


def compare_category_keys(
    locale: str, released: bool, src: str, current_json: str, rep: Report
) -> None:
    """Every sidebar category must have a translation key, and every key a category.

    This is shape, not wording: a category label lives in `current.json` under
    `sidebar.<sidebarId>.category.<English label>`, and a MISSING key does not fail the build
    or the link check — Docusaurus silently serves the English source string. That is how four
    AI-SDLC deep-dive categories shipped untranslated in two released locales.

    The `_category_.json` under `i18n/` is NOT consulted, because it never renders (it is
    overridden by `current.json`); asserting against it would be asserting against a decoy.

    Sidebar id is read off the key rather than configured, so this needs no third column in
    the course table to keep in sync. A key may also carry sub-fields of a category — e.g.
    `...category.Cross-cutting.link.generated-index.description` — so a key is orphaned only
    when its remainder is neither a label nor a sub-field of one.
    """
    if not os.path.isfile(current_json):
        missing_translation(locale, released, src, current_json, rep)
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
        if r not in known
        and not any(r == f"{label}.{sub}" for label in known for sub in CATEGORY_SUBFIELDS)
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
    released = released_locales()
    course_table = courses()   # derived once; see scripts/courses.py
    rep = Report()
    for locale in locales:
        if locale == "en":
            continue
        is_released = locale in released
        print(f">> {locale}{'' if is_released else ' (gated/unreleased)'}")
        for course in course_table:
            src, plugin = course.docs_dir, course.i18n_dir
            compare_pair(locale, is_released, src, f"i18n/{locale}/{plugin}/current", rep)
            compare_category_keys(
                locale, is_released, src, f"i18n/{locale}/{plugin}/current.json", rep
            )

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
