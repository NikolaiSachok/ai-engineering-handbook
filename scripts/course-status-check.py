#!/usr/bin/env python3
"""Course status check: the 🚧 markers agree with each Part's published count, in every locale.

A Part overview states `Published: N of M ...`. When N == M the Part is complete, so:
  - the course intro's map row linking that overview carries no 🚧 (every locale's intro);
  - the overview itself carries no 🚧 (every locale).
When N < M the intro row must still carry 🚧.

Usage: course-status-check.py [--fix] [--self-test]
--fix removes the stale markers it can remove mechanically (intro rows, the overview's "🚧 marks planned" sentence)
and adds 🚧 to an intro row of an incomplete Part; it reports what is left for a hand edit.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COUNT = re.compile(r'^Published: (\d+) of (\d+)\b', re.M)
# The overview's legend sentence, per locale; dropped once the Part is complete.
LEGEND = [' Pages marked 🚧 are planned.', ' Знак 🚧 отмечает запланированные материалы.']


def row_re(part):
    return re.compile(r'^(\|\s*\[[^\]]+\]\(\./' + re.escape(part) + r'/overview\.md\))( 🚧)?(\s*\|)', re.M)


def check_text(intro, overviews, status, fix):
    """intro: text; overviews: {part: text}; status: {part: complete}. Returns (problems, intro, overviews)."""
    problems = []
    for part, complete in status.items():
        r = row_re(part)
        m = r.search(intro)
        if m and bool(m.group(2)) == complete:
            problems.append(f'intro row for {part}: {"remove" if complete else "add"} 🚧')
            if fix:
                intro = r.sub(lambda x: x.group(1) + ('' if complete else ' 🚧') + x.group(3), intro, count=1)
        text = overviews.get(part)
        if complete and text is not None and '🚧' in text:
            if fix:
                for s in LEGEND:
                    text = text.replace(s, '')
                overviews[part] = text
            if '🚧' in text:
                problems.append(f'{part}/overview.md: 🚧 left in a complete Part')
            elif not fix:
                problems.append(f'{part}/overview.md: drop the 🚧 legend sentence')
    return problems, intro, overviews


def course_dirs(course):
    """The EN docs dir followed by each locale's copy of the course."""
    name = os.path.basename(course)
    plugin = 'docusaurus-plugin-content-' + name
    return [course] + sorted(glob.glob(os.path.join(ROOT, 'i18n', '*', plugin, 'current')))


def main(fix):
    failures = 0
    for course in sorted(glob.glob(os.path.join(ROOT, 'docs*'))):
        status = {}
        for ov in sorted(glob.glob(os.path.join(course, 'part-*', 'overview.md'))):
            m = COUNT.search(open(ov, encoding='utf-8').read())
            if m:
                status[os.path.basename(os.path.dirname(ov))] = m.group(1) == m.group(2)
        if not status:
            continue
        for d in course_dirs(course):
            intro_path = os.path.join(d, 'intro.md')
            if not os.path.exists(intro_path):
                continue
            ov_paths = {p: os.path.join(d, p, 'overview.md') for p in status}
            ovs = {p: open(f, encoding='utf-8').read() for p, f in ov_paths.items() if os.path.exists(f)}
            intro = open(intro_path, encoding='utf-8').read()
            problems, new_intro, new_ovs = check_text(intro, dict(ovs), status, fix)
            if fix:
                if new_intro != intro:
                    open(intro_path, 'w', encoding='utf-8').write(new_intro)
                for p, t in new_ovs.items():
                    if t != ovs[p]:
                        open(ov_paths[p], 'w', encoding='utf-8').write(t)
                problems, _, _ = check_text(new_intro, new_ovs, status, False)
            for p in problems:
                print(f'{os.path.relpath(d, ROOT)}: {p}')
            failures += len(problems)
    print('course-status: ' + ('PASS' if not failures else f'FAIL ({failures})'))
    return 1 if failures else 0


def self_test():
    intro = '| [I — A](./part-1/overview.md) 🚧 | x |\n| [II — B](./part-2/overview.md) | y |\n'
    ovs = {'part-1': 'Published: 3 of 3 lessons. Pages marked 🚧 are planned.\n', 'part-2': 'Published: 1 of 4.\n'}
    status = {'part-1': True, 'part-2': False}
    problems, _, _ = check_text(intro, dict(ovs), status, False)
    assert len(problems) == 3, problems
    problems, fixed, fixed_ovs = check_text(intro, dict(ovs), status, True)
    assert '(./part-1/overview.md) |' in fixed and '(./part-2/overview.md) 🚧 |' in fixed, fixed
    assert '🚧' not in fixed_ovs['part-1'], fixed_ovs
    assert check_text(fixed, fixed_ovs, status, False)[0] == []
    print('course-status self-test: PASS')
    return 0


if __name__ == '__main__':
    sys.exit(self_test() if '--self-test' in sys.argv else main('--fix' in sys.argv))
