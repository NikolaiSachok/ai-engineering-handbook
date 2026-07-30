#!/usr/bin/env python3
"""Concordance for a term slice over a source tree — every occurrence, nothing truncated.

Built against the input-side defects the German waves have hit. Each rule below is a defect,
not a preference:

  * a TRUNCATING extractor -> fabricated verdicts. So: nothing is ever cut. If a term has 183
    sentences, all 183 print, and the header says 183.
  * a NARROWING regex -> fabricated ABSENCES. A trailing `(?![a-z])` guard excluded every
    inflected form by construction, and the measured damage was large: `primitive` showed 3
    sentences where the tree had 22, and NONE of the three carried the sense the row hung on.
  * a gate that refused every page containing a table. So: tables are prose here.
  * a shared scratch path served one renderer another lesson's prompt. So: the output path is
    owner-scoped and carries the slice id, and every file stamps its own slice id and file
    list in the header.

THE TRAILING-CONTEXT DEFECT IS SUBTLER THAN "DROP THE GUARD", which is why this file now
builds an explicit union of SURFACE FORMS instead of bolting an optional suffix group onto the
stem. Measured, with the suffix-group version still in place:

    residency -> "data residencies"  MISS      policy -> "policies"  MISS
    query     -> "queries"           MISS      cache  -> "cached"    MISS
    run       -> "running"           MISS

Every one of those is an orthographic change at the stem boundary (y->ies, silent-e drop,
consonant doubling) that no amount of trailing-guard tuning reaches. `residency` matters
specifically: it is the head term of a load-bearing section with ~30 occurrences, and a
missed plural understates exactly the row that carries the most weight.

The forms are ENUMERATED rather than inferred, and every form actually matched is printed in
the header of its section, so the reader can see what was counted. A count whose surface forms
are invisible is a count nobody can check.

Usage:
    concord.py <slice-id> <termfile> <path> [<path> ...]   > <owner-scoped-out>
    concord.py --self-test

`<path>` is any file or directory; directories are walked for `*.md`. There is no built-in
file list: the earlier version hardcoded one course's ten Part III pages, which made the tool
unusable for any other course or locale — and the RU/SK re-gate needs exactly this tool.
"""

from __future__ import annotations

import collections
import pathlib
import re
import sys


# --------------------------------------------------------------------------- source reading

def load(path: pathlib.Path) -> str:
    """Read a page down to the text a translator actually translates.

    Frontmatter strings ARE translatable and stay. Real code fences are excluded: identifiers
    are class 1. MERMAID IS NOT CODE — its node labels, edge labels and captions are a
    translatable surface, and the first build of this tool hid them, which is the
    narrowing defect again, caught before it reached a slice.
    """
    lines = path.read_text(encoding="utf-8").split("\n")
    out, i = [], 0
    if lines and lines[0].strip() == "---":
        i = 1
        while i < len(lines) and lines[i].strip() != "---":
            out.append(lines[i])
            i += 1
        i += 1
    infence, fence_lang = False, None
    for ln in lines[i:]:
        s = ln.strip()
        if s.startswith("```"):
            if not infence:
                infence, fence_lang = True, s[3:].strip().lower()
            else:
                infence, fence_lang = False, None
            continue
        if infence:
            if fence_lang == "mermaid":
                out.append("[mermaid] " + s)
            continue
        out.append(ln)  # table rows kept verbatim
    return "\n".join(out)


def sentences(text: str) -> list[str]:
    """Split into units. A markdown table row, a list item and a heading are each ONE unit —
    splitting them on '.' is what produced a wave's spurious sentence-fragment verdicts."""
    units = []
    for block in text.split("\n"):
        b = block.strip()
        if not b:
            continue
        if b.startswith(("|", "#", "-", "*", ":::", "<")):
            units.append(b)
            continue
        units += [p.strip() for p in re.split(r"(?<=[.!?])\s+(?=[A-Z\"'`*\[(])", b) if p.strip()]
    return units


# --------------------------------------------------------------------------- term matching

PLAIN_SUFFIXES = ("s", "es", "ed", "ing", "er", "ers", "'s", "'")
DOUBLING_TAIL = re.compile(r"^[a-z]*[aeiou][bcdfgklmnprstvz]$")


def surface_forms(term: str) -> list[str]:
    """Every surface form of a term this corpus can plausibly write, ENUMERATED.

    Enumerated rather than inferred by a suffix group, because the misses are orthographic
    changes at the stem boundary, which a suffix group cannot express:
      y -> ies/ied/ier/iest   (policy -> policies)
      silent e dropped        (cache -> cached, caching)
      consonant doubled       (run -> running)
    For a multi-word term only the LAST word inflects: `attack success rate` ->
    `attack success rates`.
    """
    words = term.split()
    head, base = words[:-1], words[-1].lower()
    forms = {base}
    forms |= {base + s for s in PLAIN_SUFFIXES}
    if base.endswith("y") and len(base) > 1 and base[-2] not in "aeiou":
        stem = base[:-1]
        forms |= {stem + s for s in ("ies", "ied", "ier", "iest")}
    if base.endswith("e"):
        stem = base[:-1]
        forms |= {base + "d", base + "r", stem + "ed", stem + "ing", stem + "er"}
    if DOUBLING_TAIL.match(base):
        forms |= {base + base[-1] + s for s in ("ing", "ed", "er")}
    joined = [" ".join(head + [f]) if head else f for f in forms]
    # Longest first, so the pattern prefers `residencies` over `residency` and the printed
    # surface-form tally is not silently split across a shorter prefix match.
    return sorted(joined, key=len, reverse=True)


def pat(term: str) -> re.Pattern:
    alts = [r"[-\s]+".join(re.escape(w) for w in f.split()) for f in surface_forms(term)]
    return re.compile(r"(?<![A-Za-z])(" + "|".join(alts) + r")(?![A-Za-z])", re.I)


# --------------------------------------------------------------------------- driver

def resolve(args: list[str]) -> tuple[list[pathlib.Path], list[str]]:
    files, missing = [], []
    for a in args:
        p = pathlib.Path(a)
        if p.is_dir():
            files += sorted(p.rglob("*.md"))
        elif p.is_file():
            files.append(p)
        else:
            missing.append(a)
    return files, missing


def main(argv: list[str]) -> int:
    if len(argv) < 4:
        print(__doc__)
        return 2
    slice_id, termfile = argv[1], pathlib.Path(argv[2])
    files, missing = resolve(argv[3:])
    if missing:
        print("FAIL: these source paths do not exist — a mistyped path is a tool failure, not")
        print("      a concordance over zero files (that would fabricate absences for every term):")
        for m in missing:
            print(f"        {m}")
        return 2
    if not files:
        print("FAIL: the paths given match no files. A concordance over zero files reports every")
        print("      term as absent, which is the fabricated-absence defect with extra steps.")
        return 2

    terms = [t.strip() for t in termfile.read_text(encoding="utf-8").split("\n")
             if t.strip() and not t.startswith("#")]
    if not terms:
        print(f"FAIL: no terms in {termfile}")
        return 2

    corpus = {p: sentences(load(p)) for p in files}
    total_units = sum(len(v) for v in corpus.values())

    print(f"# CONCORDANCE — slice {slice_id}")
    print(f"# source: {len(files)} file(s), {total_units} text units")
    for p in files:
        print(f"#   {p}")
    print(f"# terms: {len(terms)}")
    print("# NOTHING IN THIS FILE IS TRUNCATED. Every occurrence of every term is printed.")
    print("# If a term shows 0 occurrences that is a real zero in THIS file set, not a tool")
    print("# artefact — but a zero on a LOAN is not a zero on the REFERENT. Check the referent")
    print("# with your own grep before recording any null finding.\n")

    for t in terms:
        p = pat(t)
        hits, forms = [], collections.Counter()
        for f, units in corpus.items():
            for u in units:
                for m in p.findall(u):
                    forms[m.lower()] += 1
                if p.search(u):
                    hits.append((f"{f.parent.name}/{f.name}", u))
        print(f"\n{'=' * 100}\n## `{t}` — {sum(forms.values())} occurrence(s) in {len(hits)} unit(s)")
        print(f"   surface forms COUNTED: {dict(forms) if forms else 'NONE'}")
        print(f"   surface forms SOUGHT:  {', '.join(surface_forms(t))}")
        if not hits:
            print("   (zero units — read the header note before recording this as a null finding)")
        for f, u in hits:
            print(f"   [{f}] {u}")
        print(f"   -- end of `{t}`: {len(hits)} unit(s) listed, {len(hits)} printed (complete)")
    return 0


# --------------------------------------------------------------------------- self-test

def self_test() -> int:
    fails: list[str] = []

    def check(label, got, want):
        if got == want:
            print(f"  ok   {label} -> {got!r}")
        else:
            print(f"  FAIL {label} -> got {got!r}, want {want!r}")
            fails.append(label)

    print("concord --self-test: the matcher must not fabricate absences")
    # THE MEASURED MISSES. Every one of these returned MISS with the suffix-group matcher.
    for term, text, want in [
        ("residency", "data residencies are required", "residencies"),
        ("policy", "two policies apply", "policies"),
        ("query", "many queries arrive", "queries"),
        ("cache", "cached results are returned", "cached"),
        ("run", "the running total", "running"),
        ("primitive", "three primitives exist", "primitives"),
        ("tier", "tiered pricing", "tiered"),
        ("checkpoint", "checkpointing the state", "checkpointing"),
        ("attack success rate", "two attack success rates", "attack success rates"),
        ("dry run", "a dry-run flag", "dry-run"),
    ]:
        got = pat(term).findall(text)
        check(f"`{term}` finds {want!r}", [g.lower() for g in got], [want])

    print("  -- and it must still not over-match")
    for term, text in [("run", "runtime configuration"), ("tier", "tierra del fuego"),
                       ("cache", "cachexia"), ("log", "logistics")]:
        check(f"`{term}` does NOT match in {text!r}", pat(term).findall(text), [])

    print("  -- the source reader")
    doc = ('---\ntitle: A Title\n---\n\n'
           '# A heading\n\n'
           'A sentence about residencies. Another sentence.\n\n'
           '| a | table row about queries |\n\n'
           '```python\nresidency = "not prose"\n```\n\n'
           '```mermaid\nflowchart TD\n  A["A node about policies"]\n```\n')
    body = load.__wrapped__ if hasattr(load, "__wrapped__") else load
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "page.md"
        p.write_text(doc, encoding="utf-8")
        text = body(p)
        check("frontmatter is kept (its strings are translatable)", "title: A Title" in text, True)
        check("a real code fence is excluded", 'residency = "not prose"' in text, False)
        check("a mermaid fence is KEPT (its labels are translatable)",
              "A node about policies" in text, True)
        units = sentences(text)
        check("a table row is ONE unit",
              sum(1 for u in units if u.startswith("|")), 1)
        check("a heading is one unit", sum(1 for u in units if u.startswith("#")), 1)
        check("two sentences split into two units",
              sum(1 for u in units if "sentence" in u), 2)

        # Fail closed rather than report every term absent.
        check("a mistyped source path exits 2, not a clean all-absent concordance",
              main(["concord.py", "T", str(p), str(pathlib.Path(d) / "nope")]), 2)

    print()
    if fails:
        print(f"concord --self-test: FAIL ({len(fails)}): {'; '.join(fails)}")
        return 1
    print("concord --self-test: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else main(sys.argv))
