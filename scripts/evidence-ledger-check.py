#!/usr/bin/env python3
"""Evidence gate: grades live in the ledger and in the wording, never as tokens on the page.

Why this exists. The AI-SDLC course grades every claim MEASURED / REPORTED / ASSERTED. Until #800
the grade was printed inline as a code-styled token, `MEASURED`, and readers took it for what it
was: audit metadata surfaced in the reading layer — 110 tokens in English, 105 in Russian and 110
in Slovak, plus a fourth grade (`UNKNOWN`) that had crept in unannounced. The grade now has two
homes. The READER gets it from the wording ("a trial found", "she reports", "he argues"), exactly
as Lesson 2 prescribes. The AUDIT trail is a per-page ledger in editorial/evidence/<course>/,
outside the rendered site.

Two checks, both of which fail closed:

1. No token in the reading layer. A backticked grade token in any page of any course, in any
   locale the course claims, fails — except on the pages where the ladder is the subject
   (ALLOWED below). A token that returns is the old notation coming back one edit at a time.
2. Every ledger parses and points at real sources. Each row carries a grade from the closed set,
   and every URL in its Source column must appear verbatim in the English page it names. A row
   whose link has left the page is a claim whose evidence was deleted while the grade stayed.

What it deliberately does NOT assert: that every graded sentence has a ledger row, or that the
wording carries the right grade. Both are judgements; the editorial gate owns them.

Usage: evidence-ledger-check.py [--self-test]
"""

from __future__ import annotations

import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

GRADES = ("MEASURED", "REPORTED", "ASSERTED", "UNKNOWN")
TOKEN = re.compile(r"`(" + "|".join(GRADES) + r")`")
# Pages where the ladder itself is taught, so its names are content rather than markup.
ALLOWED = {("ai-sdlc", "part-1-foundation/reading-the-evidence.md"), ("ai-sdlc", "glossary.md")}
LEDGER_DIR = os.path.join("editorial", "evidence")
PAGE_LINE = re.compile(r"^Page: `([^`]+)`\s*$", re.M)
ROW = re.compile(r"^\|\s*(\d+)\s*\|(.*)\|\s*$")
URL = re.compile(r"https?://[^\s<|]+")


def token_findings(course_id: str, rel: str, text: str) -> list[str]:
    if (course_id, rel) in ALLOWED:
        return []
    out = []
    for n, line in enumerate(text.split("\n"), 1):
        for m in TOKEN.finditer(line):
            out.append(f"{rel}:{n}: grade token `{m.group(1)}` in the reading layer — phrase the grade instead")
    return out


def ledger_findings(name: str, ledger: str, page_text: str | None) -> list[str]:
    out = []
    if page_text is None:
        return [f"{name}: the page it names does not exist"]
    expected = 1
    for n, line in enumerate(ledger.split("\n"), 1):
        m = ROW.match(line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split("|")]
        if len(cells) != 4:
            out.append(f"{name}:{n}: row needs 5 columns (# | Claim | Grade | Qualifier | Source)")
            continue
        claim, grade, _qualifier, source = cells
        if int(m.group(1)) != expected:
            out.append(f"{name}:{n}: row numbered {m.group(1)}, expected {expected}")
        expected = int(m.group(1)) + 1
        if not claim:
            out.append(f"{name}:{n}: empty claim")
        if grade not in GRADES:
            out.append(f"{name}:{n}: grade '{grade}' is not one of {', '.join(GRADES)}")
        for url in URL.findall(source):
            if url not in page_text:
                out.append(f"{name}:{n}: source {url} no longer appears on the page")
    if expected == 1:
        out.append(f"{name}: no ledger rows")
    return out


def read(path: str) -> str | None:
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return None


def run() -> int:
    from courses import courses

    os.chdir(ROOT)
    problems: list[str] = []
    for c in courses():
        trees = [c.docs_dir] + [f"i18n/{loc}/{c.i18n_dir}/current" for loc in c.locales if loc != "en"]
        for tree in trees:
            for path in sorted(glob.glob(f"{tree}/**/*.md*", recursive=True)):
                rel = os.path.relpath(path, tree)
                problems += [f"{tree}/{f}" for f in token_findings(c.id, rel, read(path) or "")]
    for path in sorted(glob.glob(f"{LEDGER_DIR}/**/*.md", recursive=True)):
        if os.path.basename(path) == "README.md":
            continue
        text = read(path) or ""
        m = PAGE_LINE.search(text)
        if not m:
            problems.append(f"{path}: missing the `Page: \\`docs-…/…md\\`` line")
            continue
        problems += ledger_findings(path, text, read(m.group(1)))
    for p in problems:
        print(p)
    print(f"evidence-ledger-check: {'FAIL' if problems else 'OK'} ({len(problems)} finding(s))")
    return 1 if problems else 0


def self_test() -> int:
    page = "A trial [found it](https://example.org/a) and she [reports](https://example.org/b)."
    good = "| 1 | it holds | MEASURED | — | https://example.org/a |\n| 2 | she saw it | REPORTED | vendor | https://example.org/b |"
    cases = [
        (token_findings("ai-sdlc", "intro.md", "x (`MEASURED`) y"), 1),
        (token_findings("ai-sdlc", "part-1-foundation/reading-the-evidence.md", "`ASSERTED`"), 0),
        (token_findings("ai-sdlc", "intro.md", "MEASURED in caps, no backticks"), 0),
        (ledger_findings("L", good, page), 0),
        (ledger_findings("L", good, None), 1),
        (ledger_findings("L", good.replace("MEASURED", "PROVEN"), page), 1),
        (ledger_findings("L", good.replace("example.org/b", "example.org/gone"), page), 1),
        (ledger_findings("L", good.replace("| 2 |", "| 3 |"), page), 1),
        (ledger_findings("L", "no table here", page), 1),
    ]
    failed = [i for i, (got, want) in enumerate(cases) if len(got) != want]
    for i in failed:
        print(f"self-test case {i}: expected {cases[i][1]} finding(s), got {cases[i][0]}")
    print(f"evidence-ledger-check self-test: {'FAIL' if failed else 'OK'} ({len(cases)} cases)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv[1:] else run())
