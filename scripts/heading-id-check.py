#!/usr/bin/env python3
"""Heading id check: every course H2-H4 carries an explicit, escaped `\\{#id}`, in every claimed locale.

A section link (`../part-2-loop/atomic-tasks.md#why-it-fails`) is written once in English and carried
into every translation. An auto-slug cannot hold it: Docusaurus slugs the heading TEXT, so the same
section is `#why-it-fails` in English and a Cyrillic or Slovak slug elsewhere, and the English slug
itself moves whenever the heading is reworded. An explicit id is the contract (#300 for the glossaries,
#813 for every course heading). This gate keeps every heading on it; locale_parity.py check 3 keeps the
ordered id sequence equal across locales.

Per heading it asserts:
  - an explicit id is present, as the last thing on the line;
  - the brace is backslash-escaped (`future.v4: true` parses a bare `{` as a JSX expression);
  - the id is lowercase ASCII (`[a-z0-9][a-z0-9_-]*`), so it reads the same in every locale's URL;
  - the id is unique on its page (Docusaurus does not de-duplicate explicit ids; a repeat sends the
    second link to the first heading).

Scope: every course in docusaurus.config.ts (scripts/courses.py), its English tree and each locale it
claims. Files and directories starting with `_` are not pages (Docusaurus excludes them) and are skipped.

Usage: heading-id-check.py [--self-test]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'scripts'))
from courses import courses  # noqa: E402

HEADING = re.compile(r'^(#{2,4}) (.*)$')
ID = re.compile(r'(\\?)\{#([^}]*)\}\s*$')
VALID = re.compile(r'[a-z0-9][a-z0-9_-]*')


def heading_lines(text):
    """(line number, line) for every H2-H4 outside the frontmatter and code fences."""
    fence = False
    m = re.match(r'\A---\n.*?\n---\n', text, re.S)
    skip = m.group(0).count('\n') if m else 0
    for n, line in enumerate(text.split('\n'), 1):
        if n <= skip:
            continue
        if re.match(r'^ *(```|~~~)', line):
            fence = not fence
        elif not fence and HEADING.match(line):
            yield n, line


def check_text(text):
    """Problems as (line number, message), one per offending heading."""
    problems, seen = [], {}
    for n, line in heading_lines(text):
        m = ID.search(line)
        if not m:
            problems.append((n, 'no explicit id — end the heading with `\\{#id}`: the English auto-slug, '
                                'the same id on this heading in every locale'))
            continue
        escaped, hid = m.groups()
        if not escaped:
            problems.append((n, f'`{{#{hid}}}` is unescaped — write `\\{{#{hid}}}` (a bare brace is JSX under future.v4)'))
        if not VALID.fullmatch(hid):
            problems.append((n, f'id `{hid}` is not lowercase ASCII `[a-z0-9_-]`'))
        if hid in seen:
            problems.append((n, f'id `{hid}` repeats line {seen[hid]} on this page'))
        seen.setdefault(hid, n)
    return problems


def pages(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith('_'))
        for f in sorted(filenames):
            if f.endswith('.md') and not f.startswith('_'):
                yield os.path.join(dirpath, f)


def main():
    os.chdir(ROOT)
    failures, headings = 0, 0
    for c in courses():
        for loc in c.locales:
            root = c.docs_dir if loc == 'en' else os.path.join('i18n', loc, c.i18n_dir, 'current')
            for page in pages(root):
                text = open(page, encoding='utf-8').read()
                headings += sum(1 for _ in heading_lines(text))
                for n, msg in check_text(text):
                    print(f'{page}:{n}: {msg}')
                    failures += 1
    print('heading-id-check: ' + (f'PASS — {headings} heading(s) checked' if not failures else f'FAIL ({failures})'))
    return 1 if failures else 0


def self_test():
    ok = '---\nid: x\n---\n\n# Title\n\n## A \\{#a}\n\n### B \\{#b}\n\n```md\n## not a heading\n```\n\n##### deep\n'
    assert check_text(ok) == [], check_text(ok)
    cases = {
        '## A\n': 'no explicit id',
        '#### A\n': 'no explicit id',
        '## A {#a}\n': 'unescaped',
        '## A \\{#Почему}\n': 'not lowercase ASCII',
        '## A \\{#a}\n\n### B \\{#a}\n': 'repeats line 1',
        '## A \\{#a} trailing\n': 'no explicit id',
    }
    for text, want in cases.items():
        got = check_text(text)
        assert len(got) == 1 and want in got[0][1], (text, got)
    print(f'heading-id-check self-test: PASS — {len(cases) + 1} case(s)')
    return 0


if __name__ == '__main__':
    sys.exit(self_test() if '--self-test' in sys.argv else main())
