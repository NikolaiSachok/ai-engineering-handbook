#!/usr/bin/env python3
"""Typography census for a translated locale — MEASURED ON ADDED LINES ONLY.

Why added lines only: the canon files carry a large pre-existing metaprose debt of em dashes
(#318, several hundred). A whole-file count drowns the signal from the lines a wave actually
wrote, and a drowned assertion is one nobody acts on.

Why every rule is expressed as the thing it FORBIDS and, for a pair, as a BALANCE: one wave's
first write shipped seven ASCII closing quotes where German needs the low-9 opener's partner.
That is invisible to reading and invisible to any grep for the opener. Only the balance
assertion sees it.

WHY THIS FILE HAS A LINE CLASSIFIER INSTEAD OF A LINE FILTER — the defect that forced it.
The original `prose()` was a per-line regex chain. It stripped inline code and single-line
JSX tags, and it could not see anything spanning more than one line. So it counted MARKUP as
German prose, twice over:

  * a ```python fence contributed 12 ASCII quotes, and
  * multi-line JSX attributes (`<InfoCard` ... `title="..."` on its own line ... `/>`)
    contributed 38 more,

to a GATED assertion — 50 false positives in one run, every one of them markup. An assertion
with 50 known-false hits is an assertion nobody reads, which is the same failure mode as an
over-broad ban: it trains the author to ignore the scanner.

A per-line regex cannot fix this, because "am I inside a fence?" is not a property of a line.
So the fence and open-tag state is computed by scanning the WHOLE FILE from the top, and each
added line is looked up by its NEW-FILE LINE NUMBER (parsed from the hunk headers), not
guessed from its content.

FAIL CLOSED. If an added line's text does not match the file's line at that number, the
working tree moved since the diff was taken; the run reports that and exits non-zero rather
than classify the wrong line. A census that silently measures stale text is worse than none.

Usage:  census.py <git-rev> [--locale=de]     e.g.  census.py origin/main --locale=de
        census.py --self-test
"""

from __future__ import annotations

import collections
import pathlib
import re
import subprocess
import sys

# --------------------------------------------------------------------------- classification

FENCE_RE = re.compile(r"^\s*(?:```|~~~)")

PROSE, FENCE, JSX = "prose", "fence", "jsx"


def classify(text: str) -> list[str]:
    """Classify every line of a file as PROSE, FENCE or JSX.

    FENCE covers the fence markers themselves and everything between them: a code block is
    class-1 identifiers, and the typography rules do not govern it.

    JSX covers the continuation lines of a tag whose attribute list spans several lines. Those
    lines are attribute markup (`title="..."`), and their ASCII quotes are delimiters. The
    line that OPENS the tag stays PROSE, because on this corpus it routinely carries prose
    after the tag on the same line; the inline stripping in `strip_markup` handles that line.

    Returns a list of length len(lines); index 0 is line 1.
    """
    out: list[str] = []
    in_fence = False
    depth = 0  # unclosed `<` of an opening tag, i.e. we are inside an attribute list
    for raw in text.split("\n"):
        if FENCE_RE.match(raw):
            # The marker line belongs to the fence in both directions.
            out.append(FENCE)
            in_fence = not in_fence
            continue
        if in_fence:
            out.append(FENCE)
            continue
        out.append(JSX if depth > 0 else PROSE)
        # Update the open-tag depth AFTER classifying, so the opening line reads as prose.
        for m in re.finditer(r"<[A-Za-z][A-Za-z0-9]*\b|/?>", raw):
            if m.group(0).startswith("<"):
                depth += 1
            elif depth > 0:
                depth -= 1
    return out


def strip_markup(line: str) -> str:
    """Strip the parts of a PROSE line that are still not German prose. Every reason measured:

      * `<YouTube title="What are Word Embeddings? — IBM Technology">` — an English video
        title, a quoted proper name. It legitimately carries U+2014 and ASCII quotes, and
        most of the shipped German files contain one. Asserting over it makes the em-dash
        rule fire on nearly every page, and the assertion stops being read.
      * JSX attributes generally (`label="…"`, `icon="…"`) use ASCII quotes as MARKUP.
      * inline code and code spans are class-1 identifiers.
      * YAML scalar quotes (`title: "…"`) and Mermaid label delimiters (`A["…"]`, `-->|"…"|`)
        are markup that happens to be an ASCII quote. The INNER text stays — it is translated
        prose, and the dash and percent rules do govern it.
    """
    line = re.sub(r"<[A-Za-z][^>]*>", " ", line)          # JSX/HTML tags incl. their attrs
    line = re.sub(r"`[^`]*`", " ", line)                  # inline code
    line = re.sub(r"\]\([^)]*\)", "] ", line)             # link targets
    line = re.sub(r"https?://\S+", " ", line)             # bare URLs
    line = re.sub(r'^(\s*[A-Za-z_][\w.-]*:\s*)"(.*)"\s*$', r"\1\2", line)
    line = line.replace('["', "[").replace('"]', "]")
    line = line.replace('|"', "|").replace('"|', "|")
    line = line.replace('{"', "{").replace('"}', "}")     # mermaid diamond nodes
    line = re.sub(r'--\s*"([^"]*)"\s*-->', r"-- \1 -->", line)  # mermaid edge labels
    return line


def outside_quotes(text: str) -> str:
    """Drop German-quoted spans („…“).

    Used by the Anrede check ONLY, and narrowly. The corpus addresses its reader as `Sie`, so a
    `du` in the book's own voice is a defect. But a QUOTED PROMPT EXAMPLE is text addressed to a
    model rather than to the reader — „Nenne deine Quellen“ is the string a reader would send to
    an LLM, and German prompt examples idiomatically take `du`. Asserting over it makes the rule
    fire on correct content.

    That distinction matters more than the one hit: an assertion with a known-false finding
    trains the author to skip the scanner, after which a real hit goes past too. So the rule is
    NARROWED here, with the reason recorded, rather than carrying an ignore list. It stays fully
    live in the book's own voice, which is what it was written to protect.

    Deliberately scoped to this one check: a quoted span is still governed by the dash, quote and
    percent rules, because those are about typography and apply to quoted German too.
    """
    return re.sub(r"„[^“]*“", " ", text)


# --------------------------------------------------------------------------- the rules

CHECKS = [
    ("U+2014 em dash",            lambda t: t.count("—"),                                 0,    "== 0 (the Gedankenstrich is the SPACED en dash)"),
    ("U+2013 en dash, UNSPACED",  lambda t: len(re.findall(r"\S–\S", t)),                 None, "ranges only (10–20); a parenthetical dash must be spaced"),
    ("U+2013 en dash, spaced",    lambda t: len(re.findall(r" – ", t)),                   None, "the Gedankenstrich"),
    ("„ opening quote",           lambda t: t.count("„"),                                 None, "must BALANCE the closing quote"),
    ("“ closing quote (U+201C)",  lambda t: t.count("“"),                                 None, "must BALANCE „"),
    ('ASCII " (U+0022)',          lambda t: t.count('"'),                                 0,    "== 0 outside JSX attributes/code/fences"),
    ("‚ single opening",          lambda t: t.count("‚"),                                 None, "nested"),
    ("‘ single closing",          lambda t: t.count("‘"),                                 None, "must balance ‚"),
    ("»…« guillemets",            lambda t: t.count("»") + t.count("«"),                  0,    "== 0, forbidden BY NAME"),
    ("percent TIGHT 20%",         lambda t: len(re.findall(r"\d%", t)),                    0,    "== 0; German takes 20 + U+202F + %"),
    ("percent + PLAIN space",     lambda t: len(re.findall(r"\d %", t)),                   0,    "== 0; a plain space is not the norm's space"),
    ("percent + U+00A0",          lambda t: len(re.findall("\\d\u00a0%", t)),              0,    "== 0; U+00A0 is the fallback, U+202F is the form"),
    ("percent + U+202F [TARGET]", lambda t: len(re.findall("\\d\u202f%", t)),              None, "the ONLY correct form"),
    ("thousands point 1.000",     lambda t: len(re.findall(r"\d\.\d{3}(?!\d)", t)),        None, "money amounts only; otherwise U+202F"),
    ("thousands + U+202F",        lambda t: len(re.findall("\\d\u202f\\d{3}", t)),         None, "the correct form"),
    ("thousands + PLAIN space",   lambda t: len(re.findall(r"\d \d{3}(?!\d)", t)),         0,    "== 0"),
    ("Swiss ss for ß",            lambda t: len(re.findall(r"\b(gross|heissen|Strasse|weiss)\b", t)), None, "manual read: Swiss variants"),
    ("bare { heading id",         lambda t: len(re.findall(r"(?<!\\)\{#", t)),             0,    "== 0; anchors need the BACKSLASH or the build hard-fails"),
    ("\\{#id} anchors",           lambda t: len(re.findall(r"\\\{#", t)),                  None, "the correct form"),
    ("du/dein Anrede",            lambda t: len(re.findall(r"\b(du|dich|dein|deine|deinem|deinen)\b", outside_quotes(t))), 0, "== 0 in the book's OWN voice; quoted prompt examples exempt (see outside_quotes)"),
]

BALANCES = [("„ opening quote", "“ closing quote (U+201C)"), ("‚ single opening", "‘ single closing")]


# --------------------------------------------------------------------------- diff parsing

HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")


def added_lines(rev: str) -> list[tuple[str, int, str]]:
    """Return (path, new_file_line_number, text) for every added line in the diff vs `rev`.

    The line NUMBER is what makes the classifier usable at all; the original tool kept only
    the text and therefore had nothing to look a classification up by.
    """
    diff = subprocess.run(
        ["git", "diff", rev, "--unified=0"], capture_output=True, text=True, check=False
    ).stdout
    out: list[tuple[str, int, str]] = []
    path, lineno = None, 0
    for ln in diff.split("\n"):
        if ln.startswith("+++ b/"):
            path, lineno = ln[6:], 0
        elif ln.startswith("@@"):
            m = HUNK_RE.match(ln)
            if m:
                lineno = int(m.group(1))
        elif ln.startswith("+") and not ln.startswith("+++"):
            if path:
                out.append((path, lineno, ln[1:]))
            lineno += 1
    return out


# --------------------------------------------------------------------------- reporting

def report(label: str, lines: list[str]) -> int:
    """Print one block; return the number of FAILED assertions."""
    t = "\n".join(lines)
    print(f"## {label}  ({len(lines)} prose line(s))")
    vals, failures = {}, 0
    for name, fn, expect, note in CHECKS:
        n = fn(t)
        vals[name] = n
        flag = ""
        if expect is not None:
            ok = n == expect
            flag = "  ok" if ok else "  FAIL"
            failures += 0 if ok else 1
        print(f"   {name:<28} {n:>5}{flag}   {note}")
    for opener, closer in BALANCES:
        o, c = vals[opener], vals[closer]
        ok = o == c
        failures += 0 if ok else 1
        label2 = f"BALANCE {opener[0]} vs {closer[0]}"
        print(f"   {label2:<28} {o} vs {c}   " + ("ok balanced" if ok else
              "FAIL — unbalanced; this is the check that caught the seven ASCII closers"))
    print()
    return failures


def main(argv: list[str]) -> int:
    rev, locale = "origin/main", "de"
    for a in argv[1:]:
        if a.startswith("--locale="):
            locale = a.split("=", 1)[1]
        elif not a.startswith("--"):
            rev = a
    shipping = f"i18n/{locale}/"

    rows = added_lines(rev)
    if not rows:
        print(f"census: no added lines vs {rev} — nothing to assert.")
        return 0

    kinds_of: dict[str, list[str] | None] = {}
    body_of: dict[str, list[str]] = {}
    prose_rows: list[tuple[str, str]] = []
    skipped: collections.Counter = collections.Counter()
    stale: list[str] = []

    for path, no, text in rows:
        if path not in kinds_of:
            p = pathlib.Path(path)
            if p.is_file():
                body = p.read_text(encoding="utf-8")
                body_of[path] = body.split("\n")
                kinds_of[path] = classify(body)
            else:
                kinds_of[path] = None
        kinds = kinds_of[path]
        if kinds is None:
            skipped["a file not present in the working tree"] += 1
            continue
        if not 1 <= no <= len(kinds):
            stale.append(f"{path}:{no} — beyond end of file ({len(kinds)} lines)")
            continue
        if body_of[path][no - 1] != text:
            stale.append(f"{path}:{no} — the diff's text is not the file's line at that number")
            continue
        if kinds[no - 1] == PROSE:
            prose_rows.append((path, strip_markup(text)))
        else:
            skipped[kinds[no - 1]] += 1

    print(f"# TYPOGRAPHY CENSUS — added lines only, vs {rev}, locale {locale}")
    print(f"# {len(rows)} added line(s); {len(prose_rows)} classified as PROSE")
    for k, v in sorted(skipped.items()):
        print(f"#   {v:>5} excluded as {k}")
    print("# Fenced blocks and multi-line JSX attribute lines are MARKUP, excluded by whole-file")
    print("# classification rather than a per-line regex. That distinction was bought with 50")
    print("# false positives: 12 from one Python fence, 38 from JSX attributes.")
    print()

    if stale:
        print("FAIL — THE WORKING TREE MOVED SINCE THE DIFF WAS TAKEN. Re-run; do not read the")
        print("numbers below. Classifying by line number requires file and diff to agree.")
        for s in stale[:20]:
            print(f"   {s}")
        if len(stale) > 20:
            print(f"   … and {len(stale) - 20} more")
        return 1

    ship = [l for f, l in prose_rows if f.startswith(shipping)]
    other = [l for f, l in prose_rows if not f.startswith(shipping)]
    by_file: dict[str, list[str]] = collections.defaultdict(list)
    for f, l in prose_rows:
        by_file[f].append(l)

    print("=" * 96)
    print(f"THE ASSERTION IS SCOPED TO SHIPPING PROSE ({shipping}**). The canon and editorial files")
    print("are METAPROSE: their pre-existing em-dash debt is #318, an open locale-wide editorial")
    print("question, and folding it in here would drown a wave's own signal in inherited dashes.")
    print("=" * 96 + "\n")

    failures = report(f"SHIPPING PROSE — {shipping}** (THE GATED ASSERTION)", ship)
    for f in sorted(by_file):
        if f.startswith(shipping):
            report(f, by_file[f])

    print("=" * 96)
    print("INFORMATIONAL ONLY — editorial/ and everything else. Not gated; see #318.")
    print("=" * 96 + "\n")
    report("NON-SHIPPING ADDED PROSE LINES", other)

    if failures:
        print(f"census: FAIL — {failures} gated assertion(s) failed on {shipping}**.")
        return 1
    print(f"census: PASS — every gated assertion holds on {shipping}**.")
    return 0


# --------------------------------------------------------------------------- self-test

SELF_TEST_DOC = '''---
title: "Ein Titel"
---

Dies ist deutsche Prosa mit einem Anteil von 20\u202f% und einem \u201eZitat\u201c.

```python
d = {"key": "value", "other": "thing"}
print("a string with ASCII quotes")
```

<InfoCard
  title="An English card title \u2014 with an em dash"
  caption="Another attribute"
/>

Und hier noch ein Satz mit `inline_code = "x"` darin.

```mermaid
flowchart TD
  A["Ein Knoten"] --> B["Ein anderer"]
```
'''


def self_test() -> int:
    fails: list[str] = []

    def check(label, got, want):
        if got == want:
            print(f"  ok   {label} -> {got}")
        else:
            print(f"  FAIL {label} -> got {got!r}, want {want!r}")
            fails.append(label)

    print("census --self-test: the classifier must see fences and multi-line JSX")
    lines = SELF_TEST_DOC.split("\n")
    kinds = classify(SELF_TEST_DOC)
    check("classification length matches line count", len(kinds), len(lines))

    def kind_of(needle):
        for i, l in enumerate(lines):
            if needle in l:
                return kinds[i]
        return "NOT FOUND"

    check("a Python-fence body line is FENCE", kind_of('print("a string'), FENCE)
    check("the fence marker itself is FENCE", kind_of("```python"), FENCE)
    check("a Mermaid-fence body line is FENCE", kind_of('A["Ein Knoten"]'), FENCE)
    check("a JSX attribute continuation line is JSX", kind_of('title="An English card'), JSX)
    check("the second JSX attribute line is JSX", kind_of('caption="Another'), JSX)
    check("the tag-opening line stays PROSE", kind_of("<InfoCard"), PROSE)
    check("real German prose is PROSE", kind_of("Dies ist deutsche Prosa"), PROSE)
    check("a prose line carrying inline code is PROSE", kind_of("Und hier noch ein Satz"), PROSE)

    # The regression the classifier exists for: ASCII quotes must be zero over PROSE lines,
    # and non-zero if fences and JSX are wrongly counted as prose.
    prose_text = "\n".join(strip_markup(l) for i, l in enumerate(lines) if kinds[i] == PROSE)
    all_text = "\n".join(strip_markup(l) for l in lines)
    check("ASCII quotes over PROSE lines only", prose_text.count('"'), 0)
    print(f"  info ASCII quotes if fences/JSX counted as prose: {all_text.count(chr(34))}"
          "  <- the 50-false-positive defect, in miniature")
    if all_text.count('"') == 0:
        print("  FAIL the fixture no longer reproduces the defect — it must contain markup quotes")
        fails.append("fixture reproduces the defect")

    print("  -- the Anrede rule must hold in the book's voice and exempt a quoted prompt")
    check("a `du` in the book's own voice is still a finding",
          len(re.findall(r"\bdeine\b", outside_quotes("Nennen Sie deine Quellen."))), 1)
    check("a `du` inside a quoted prompt example is exempt",
          len(re.findall(r"\bdeine\b", outside_quotes("Ein Prompt, der \u201eNenne deine Quellen\u201c sagt."))), 0)
    check("the exemption does not swallow the whole line",
          "sagt" in outside_quotes("Ein Prompt, der \u201eNenne deine Quellen\u201c sagt."), True)

    check("U+202F percent seen on a prose line", len(re.findall("\\d\u202f%", prose_text)), 1)
    check("the em dash inside a JSX attribute is NOT counted", prose_text.count("\u2014"), 0)
    check("German quote pair balances over prose",
          (prose_text.count("\u201e"), prose_text.count("\u201c")), (1, 1))

    print("  -- hunk headers must yield NEW-file line numbers")
    m = HUNK_RE.match("@@ -1,0 +42,3 @@ context")
    check("multi-line hunk header", m.group(1) if m else None, "42")
    m2 = HUNK_RE.match("@@ -7 +7 @@")
    check("single-line hunk header", m2.group(1) if m2 else None, "7")

    print()
    if fails:
        print(f"census --self-test: FAIL ({len(fails)}): {'; '.join(fails)}")
        return 1
    print("census --self-test: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else main(sys.argv))
