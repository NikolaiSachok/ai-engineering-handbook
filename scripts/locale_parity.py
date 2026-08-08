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
COMPONENTS = ["<InfoCard", "<Node", "<YouTube", "<Verdict"]

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


def strip_mermaid_labels(body: str) -> str:
    """Remove every label body from a mermaid fence, leaving only ids, arrows and keywords.

    Necessary before reading ids, because label prose is full of words that look like ids:
    `LD["Ranked list (dense)"]` yields a phantom node `list`, and the sequence message
    `S->>M: Generate (stream: true)` yields a phantom `Generate`. Both are translated text and
    would make this check fire on every correct translation.

    Order matters. Quoted labels go first because they may themselves contain brackets. Then the
    three UNQUOTED edge-label forms mermaid accepts — `-->|yes, it's X|`, `-. prune .->`,
    `-- reads body -->` — each of which otherwise leaks its words. Then message and note text
    after a colon. Bracket pairs are peeled innermost-out so `[("...")]` and `(["..."])` collapse.
    """
    b = re.sub(r'"[^"]*"', "", body)
    b = re.sub(r"\|[^|]*\|", "|", b)
    b = re.sub(r"-\.[^.\n]*\.->", "-.->", b)
    b = re.sub(r"--\s+[^->\n]+\s+-->", "-->", b)
    b = re.sub(r"==\s+[^=>\n]+\s+==>", "==>", b)
    b = re.sub(r"(?m):.*$", "", b)
    for _ in range(4):
        new = re.sub(r"\[[^\[\]]*\]|\{[^{}]*\}|\([^()]*\)", "", b)
        if new == b:
            break
        b = new
    return b


MERMAID_KEYWORDS = {
    "flowchart", "graph", "sequenceDiagram", "subgraph", "direction", "end", "participant",
    "Note", "over", "as", "loop", "alt", "opt", "par", "rect", "activate", "deactivate",
    "LR", "RL", "TB", "TD", "BT",
}


def mermaid_shape(body: str) -> tuple[str | None, frozenset[str], int]:
    """A diagram's SHAPE: layout direction, the set of node ids, and the edge count.

    Label text is excluded on purpose — translating a label is the entire point of a locale. What
    must not differ is the graph: same nodes, same wiring, same axis. Ids are not content, they are
    the diagram's code, and holding them equal across locales is what makes four files diffable.

    Why this check exists at all: measured 2026-08-03, 27 of the Russian renders had drifted into
    genuinely different diagrams — one was 2 062px where its English counterpart was 635px because
    two English diagrams had been merged into one; another put the local MCP server OUTSIDE the
    trust boundary that English puts it inside, and carried a caption asserting the opposite of
    what English teaches. Every one of those shipped. The heading, anchor and fence-count checks
    above all passed, because none of them looks INSIDE a fence.
    """
    direction = None
    m = re.search(r"^\s*(?:flowchart|graph)\s+(\w+)", body, re.M)
    if m:
        # TD and TB are the same axis in mermaid; normalise so a locale writing the other spelling
        # is not reported as a defect.
        direction = "TB" if m.group(1) in ("TB", "TD") else m.group(1)
    elif re.search(r"^\s*sequenceDiagram", body, re.M):
        direction = "sequence"

    ids = set(re.findall(r"^\s*participant\s+(\w+)", body, re.M))
    ids |= set(re.findall(r"subgraph\s+([A-Za-z_][\w-]*)", body))
    stripped = strip_mermaid_labels(body)
    if direction == "sequence":
        for a, b in re.findall(r"(\w+)\s*(?:-|--)?(?:->>|-->>|->|-->|<<-|x|\))\s*(\w+)", stripped):
            ids |= {a, b}
    else:
        for line in stripped.splitlines():
            line = re.sub(r"^\s*(subgraph|direction|end)\b.*", "", line)
            ids |= set(re.findall(r"\b([A-Za-z_][\w-]*)\b", line))
    edges = len(re.findall(r"(-\.->|-->>|<-->|-->|---|==>|->>|<--)", stripped))
    return direction, frozenset(ids - MERMAID_KEYWORDS), edges


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
        self.scoped_out = 0  # course/locale pairs the course does not claim

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
            f"{locale}/{src} — released locale has no {path}. This course CLAIMS {locale} "
            f"(its `locales` in docusaurus.config.ts), and a claimed locale that ships must be "
            f"translated; absence here means the whole course renders in English. If the course "
            f"is genuinely not translated here, drop {locale} from its declared locales — that "
            f"is a decision, and it belongs in the config where readers of the card can see it."
        )
    else:
        print(f"  - {src}: no {path} — not yet translated ({locale} is gated/unreleased)")


def compare_pair(locale: str, released: bool, src: str, tgt: str, rep: Report) -> None:
    if not os.path.isdir(tgt):
        missing_translation(locale, released, src, tgt, rep)
        return

    en_files, loc_files = md_files(src), md_files(tgt)

    # 1. file set
    #
    # An absent page is a DEFECT in a released locale and the EXPECTED state in an unreleased one —
    # the same asymmetry missing_translation() already applies to a whole absent course, applied one
    # level down. Without it a locale is all-or-nothing: the first pilot lesson creates `current/`,
    # every other page of the course reads as "missing", and the gate fails on a tree that is
    # correct for its stage. That is not a tolerance the gate can do without, because a locale
    # cannot be translated in one commit — it is the ordinary mid-programme state.
    #
    # The reverse direction stays a hard failure in EVERY locale: a page with no English source is
    # never expected, at any stage, and is the one half of this check that cannot fail open.
    if en_files - loc_files:
        if released:
            rep.fail(f"{locale}/{src} — page(s) present in English, missing in {locale}:")
            for p in sorted(en_files - loc_files):
                print(f"    - {p}")
        else:
            print(f"  - {src}: {len(en_files - loc_files)} of {len(en_files)} page(s) not yet "
                  f"translated ({locale} is gated/unreleased) — EN fallback")
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

        # 5b. mermaid diagram SHAPE — inside the fence the count check above only weighs
        #
        # A diagram is four files, and until 2026-08-03 nothing compared them. Only run when the
        # counts already agree; otherwise the count failure above is the finding and this would
        # just repeat it against mismatched pairs.
        ma = [b for lang, b in fa if lang == "mermaid"]
        mb = [b for lang, b in fb if lang == "mermaid"]
        if len(ma) == len(mb):
            for n, (ba, bb) in enumerate(zip(ma, mb), start=1):
                da, ia, ea = mermaid_shape(ba)
                db, ib, eb = mermaid_shape(bb)
                if (da, ia, ea) == (db, ib, eb):
                    continue
                rep.fail(f"{where} — mermaid diagram #{n} differs in SHAPE, not just wording:")
                if da != db:
                    print(f"    layout direction: en={da} {locale}={db}")
                if ia != ib:
                    if sorted(ia - ib):
                        print(f"    node id(s) missing in {locale}: {sorted(ia - ib)}")
                    if sorted(ib - ia):
                        print(f"    node id(s) only in {locale}:    {sorted(ib - ia)}")
                if ea != eb:
                    print(f"    edge count: en={ea} {locale}={eb}")

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


# --- self-test ---------------------------------------------------------------------------
#
# Per-course locale scope decides whether a course/locale pair is checked AT ALL, which makes it
# the one setting here that can turn the gate off. A wrong scope does not produce a wrong finding;
# it produces silence, and silence is what a passing gate looks like. The corpus cannot exercise
# it either — today every course claims every locale, so the scoping branch never runs against
# real content and would sit unproven until the first English-only course, which is exactly when
# a mistake would ship.
#
# So the verdicts are asserted against synthetic trees: a claimed locale is still checked and
# still fails when its translation is missing (the fail-closed the scope must not reopen), an
# unclaimed one is skipped, and a malformed declaration aborts rather than defaulting to
# "everything", which would be a blanket exemption wearing a green tick.
SELF_TEST_CASES = [
    # (name, courses declaration, tree to create, expected exit, expected substring)
    (
        "claimed + translated → checked",
        [("default", "/a", ["en", "ru"])],
        {
            "docs/x.md": "# T\n",
            "i18n/ru/docusaurus-plugin-content-docs/current/x.md": "# T\n",
            "i18n/ru/docusaurus-plugin-content-docs/current.json": "{}\n",
        },
        0,
        "1 file(s) in structural parity",
    ),
    (
        "claimed + MISSING translation, released locale → still fails",
        [("default", "/a", ["en", "ru"])],
        {"docs/x.md": "# T\n"},
        1,
        "released locale has no",
    ),
    (
        "NOT claimed → skipped, and the run passes",
        [("default", "/a", ["en"])],
        {"docs/x.md": "# T\n"},
        0,
        "not claimed by this course",
    ),
    (
        "not claimed → reported, never silent",
        [("default", "/a", ["en"])],
        {"docs/x.md": "# T\n"},
        0,
        "out of declared scope",
    ),
    (
        "claimed + unreleased locale, missing tree → tolerated",
        [("default", "/a", ["en", "de"])],
        {"docs/x.md": "# T\n"},
        0,
        "not yet translated",
    ),
    (
        "no `locales:` declared → aborts, does not default to all",
        [("default", "/a", None)],
        {"docs/x.md": "# T\n"},
        1,
        "declares no `locales:`",
    ),
    (
        "`locales:` without 'en' → aborts",
        [("default", "/a", ["ru"])],
        {"docs/x.md": "# T\n"},
        1,
        "does not claim 'en'",
    ),
    # --- mermaid diagram shape. Each case reproduces one of the 28 drifts found 2026-08-03, all
    # of which shipped past every other check in this file because none of them looks INSIDE a
    # fence. The last two are anti-false-positive controls: this check must stay silent on a
    # correct translation, or it trains the reader to ignore it.
    (
        "diagram: translated labels only → passes",
        [("default", "/a", ["en", "ru"])],
        {
            "docs/x.md": '# T\n\n```mermaid\nflowchart TB\n    A["Query"] --> B["Answer"]\n```\n',
            "i18n/ru/docusaurus-plugin-content-docs/current/x.md":
                '# T\n\n```mermaid\nflowchart TB\n    A["Запрос"] --> B["Ответ"]\n```\n',
            "i18n/ru/docusaurus-plugin-content-docs/current.json": "{}\n",
        },
        0,
        "1 file(s) in structural parity",
    ),
    (
        "diagram: renamed node id → FAILS",
        [("default", "/a", ["en", "ru"])],
        {
            "docs/x.md": '# T\n\n```mermaid\nflowchart TB\n    A["Query"] --> B["Answer"]\n```\n',
            "i18n/ru/docusaurus-plugin-content-docs/current/x.md":
                '# T\n\n```mermaid\nflowchart TB\n    Q["Запрос"] --> B["Ответ"]\n```\n',
            "i18n/ru/docusaurus-plugin-content-docs/current.json": "{}\n",
        },
        1,
        "differs in SHAPE",
    ),
    (
        "diagram: flipped layout direction → FAILS",
        [("default", "/a", ["en", "ru"])],
        {
            "docs/x.md": '# T\n\n```mermaid\nflowchart TB\n    A["Query"] --> B["Answer"]\n```\n',
            "i18n/ru/docusaurus-plugin-content-docs/current/x.md":
                '# T\n\n```mermaid\nflowchart LR\n    A["Запрос"] --> B["Ответ"]\n```\n',
            "i18n/ru/docusaurus-plugin-content-docs/current.json": "{}\n",
        },
        1,
        "layout direction",
    ),
    (
        "diagram: dropped edge → FAILS",
        [("default", "/a", ["en", "ru"])],
        {
            "docs/x.md":
                '# T\n\n```mermaid\nflowchart TB\n    A["Q"] --> B["A"]\n    A --> C["C"]\n```\n',
            "i18n/ru/docusaurus-plugin-content-docs/current/x.md":
                '# T\n\n```mermaid\nflowchart TB\n    A["З"] --> B["О"]\n    C["Ц"]\n```\n',
            "i18n/ru/docusaurus-plugin-content-docs/current.json": "{}\n",
        },
        1,
        "edge count",
    ),
    (
        "diagram: TD vs TB is the same axis → passes (anti-false-positive)",
        [("default", "/a", ["en", "ru"])],
        {
            "docs/x.md": '# T\n\n```mermaid\nflowchart TB\n    A["Query"] --> B["Answer"]\n```\n',
            "i18n/ru/docusaurus-plugin-content-docs/current/x.md":
                '# T\n\n```mermaid\nflowchart TD\n    A["Запрос"] --> B["Ответ"]\n```\n',
            "i18n/ru/docusaurus-plugin-content-docs/current.json": "{}\n",
        },
        0,
        "1 file(s) in structural parity",
    ),
    (
        "diagram: words inside labels and edge labels are not ids → passes",
        [("default", "/a", ["en", "ru"])],
        {
            "docs/x.md": (
                '# T\n\n```mermaid\nflowchart TB\n'
                '    A["Ranked list (dense)"] -->|"no, it is a skill"| B["Answer"]\n'
                '    B -. prune .-> C["End"]\n```\n'
            ),
            "i18n/ru/docusaurus-plugin-content-docs/current/x.md": (
                '# T\n\n```mermaid\nflowchart TB\n'
                '    A["Ранжированный список (плотный)"] -->|"нет, это навык"| B["Ответ"]\n'
                '    B -. отсекаем .-> C["Конец"]\n```\n'
            ),
            "i18n/ru/docusaurus-plugin-content-docs/current.json": "{}\n",
        },
        0,
        "1 file(s) in structural parity",
    ),
]


def self_test() -> int:
    import shutil
    import subprocess
    import tempfile

    me = os.path.abspath(__file__)
    failures = 0
    for name, decls, tree, want_code, want_text in SELF_TEST_CASES:
        root = tempfile.mkdtemp(prefix="parity-selftest-")
        try:
            objs = []
            for cid, base, locs in decls:
                loc_line = "" if locs is None else f"    locales: {list(locs)!r},\n"
                objs.append(f"  {{\n    id: '{cid}',\n    basePath: '{base}',\n{loc_line}  }},")
            config = (
                "const RELEASED_LOCALES = ['en', 'ru', 'sk'];\n"
                "const UNRELEASED_LOCALES: string[] = ['de'];\n"
                "const COURSES: Course[] = [\n" + "\n".join(objs) + "\n];\n"
            )
            with open(os.path.join(root, "docusaurus.config.ts"), "w", encoding="utf-8") as fh:
                fh.write(config.replace("'", "'"))
            for rel, body in tree.items():
                path = os.path.join(root, rel)
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(body)
            # Every locale dir must exist or main() never iterates it.
            for loc in ("ru", "sk", "de"):
                os.makedirs(os.path.join(root, "i18n", loc), exist_ok=True)

            r = subprocess.run(
                [sys.executable, me], cwd=root, capture_output=True, text=True
            )
            out = r.stdout + r.stderr
            ok = r.returncode == want_code and want_text in out
            print(f"  {'ok  ' if ok else 'FAIL'}  {name}")
            if not ok:
                failures += 1
                print(f"        expected exit {want_code} and {want_text!r}")
                print(f"        got exit {r.returncode}; output:\n{out}")
        finally:
            shutil.rmtree(root, ignore_errors=True)

    print()
    if failures:
        print(f"locale-parity-check --self-test: FAIL — {failures} case(s).")
        return 1
    print(f"locale-parity-check --self-test: PASS — {len(SELF_TEST_CASES)} scope case(s).")
    return 0


def main(argv: list[str]) -> int:
    if "--self-test" in argv[1:]:
        return self_test()
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
            # Scope check, before anything is compared. A course that does not claim this
            # locale is not a defect and not a fallback — it is a declared boundary, and the
            # only honest thing to do with it is say so out loud. Reported, never silent:
            # an unexplained absence in the log is how "not translated here" and "translation
            # lost" become indistinguishable.
            if locale not in course.locales:
                print(
                    f"  - {course.docs_dir}: not claimed by this course "
                    f"(claims {', '.join(course.locales)}) — out of scope, EN throughout"
                )
                rep.scoped_out += 1
                continue
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
            f"{rep.tolerated} tolerated wording difference(s)"
            + (
                f"; {rep.scoped_out} course/locale pair(s) out of declared scope."
                if rep.scoped_out
                else "."
            )
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
