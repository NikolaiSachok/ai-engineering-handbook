#!/usr/bin/env python3
"""Diff any text against a locale's OWN ban list.

WHY THIS EXISTS, precisely: reconciliation compares sheets to EACH OTHER, and that comparison
cannot by construction catch a defect that BOTH runs share. Both blind runs of one slice
independently wrote the same banned German collocation into their own sheets. Two runs
converging on a banned string is not confirmation; it is one English collocation surviving
twice.

And the POSITION matters. A banned string sitting in a ledger's WORKED SENTENCE is the worst
place for it, because copying the worked sentence is exactly what a worked sentence is for. So
this runs over ledgers BEFORE they bind, and over rendered prose AFTER.

TWO PROPERTIES OF A GOOD BAN, both bought with defects:

  * AN OVER-BROAD BAN IS A DEFECT, not a safe default. Two rules in this list were written
    wide enough to fire on correct forms — 19 false positives between them — and the cost is
    not the reading time. It is that the author learns to skip the scanner, after which a real
    hit goes past too. Two rules were therefore NARROWED rather than kept "just in case": one
    released for the host-platform referent, one restricted to a single sense.
  * A BAN IS NOT ALWAYS ONE REPAIR. Where a banned string spans two senses, the row must
    spell the repair out PER SENSE; a single replacement instruction applied across senses is
    how a correct measurement gets applied to the wrong word.

usage: banscan.py <file|dir> [...] [--banlist=PATH] [--skip-group=NAME]
       banscan.py --self-test
"""

from __future__ import annotations

import collections
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
DEFAULT_BANLIST = HERE / "banlist.de.json"

# The typography rules govern SHIPPING PROSE. Ledgers, briefs and canon are METAPROSE and
# legitimately carry em dashes, quoted bans and English sentences — 700 em-dash "hits" across
# seven ledgers is not a finding, it is the wrong scope, and an assertion nobody can act on is
# one nobody reads. Hence --skip-group.
SKIPPABLE_HINT = "e.g. --skip-group=typography when scanning ledgers rather than shipped prose"

# A ban list is a list of things NOT to WRITE. A line that QUOTES the ban in order to state it
# is not a violation — otherwise the ban list flags itself, and so does every ledger that
# dutifully records its own rejections. This is a heuristic and is labelled as one.
REJECTION_MARKERS = ("⛔", "NICHT", "nicht schreiben", "verboten", "rejected", "banned", "instead")


def load_rules(banlist_path: pathlib.Path, skip_groups: set[str]):
    """Compile the ban list. Fails closed: a malformed regex or a missing `re` key raises here
    rather than silently dropping a rule, because a silently dropped rule is a gate that
    reports a clean run on text it never checked."""
    data = json.loads(banlist_path.read_text(encoding="utf-8"))
    rules = []
    for group, entries in data.items():
        if group.startswith("_") or group in skip_groups:
            continue
        if not isinstance(entries, dict):
            raise ValueError(f"group {group!r} is not an object")
        for name, spec in entries.items():
            if "re" not in spec:
                raise ValueError(f"rule {group}/{name} has no 're' key")
            rules.append((group, name, re.compile(spec["re"]), spec))
    return rules


def own_voice(line: str) -> str:
    """Drop German-quoted spans („…“), for rules whose `scope` is `own_voice`.

    A rule about how the BOOK addresses its reader must not fire on text the book QUOTES. The
    Anrede rule fired on „Nenne deine Quellen“ and „Fasse dich kurz“ — prompt examples addressed
    to a model, where German idiomatically takes `du`. Both were correct shipped prose.

    A rule declares this itself, in the ban list, with its reason. That is deliberate: the
    alternative is an ignore list, and a gate with an ignore list is a gate nobody reads.
    """
    return re.sub(r"„[^“]*“", " ", line)


def scan(targets, rules):
    """Return {(group, name): [(path, lineno, line, matched), ...]}."""
    hits = collections.defaultdict(list)
    for f in targets:
        for i, line in enumerate(f.read_text(encoding="utf-8").split("\n"), 1):
            if any(m in line for m in REJECTION_MARKERS):
                continue
            for group, name, rx, spec in rules:
                subject = own_voice(line) if spec.get("scope") == "own_voice" else line
                for m in rx.finditer(subject):
                    hits[(group, name)].append((str(f), i, line.strip()[:170], m.group(0)))
    return hits


def resolve(args):
    """Expand paths to files. Returns (targets, missing).

    A path that does not exist is returned as MISSING rather than passed through as a target.
    The earlier version appended it blindly, and the scan then died with a FileNotFoundError
    traceback — which is a crash where the convention is a named failure. A mistyped path must
    be reported as a tool failure, never mistaken for a clean run over zero files."""
    targets, missing = [], []
    for a in args:
        p = pathlib.Path(a)
        if p.is_dir():
            targets += sorted(p.rglob("*.md"))
        elif p.is_file():
            targets.append(p)
        else:
            missing.append(a)
    return targets, missing


def main(argv):
    args = argv[1:]
    banlist = DEFAULT_BANLIST
    skip_groups = set()
    paths = []
    for a in args:
        if a.startswith("--banlist="):
            banlist = pathlib.Path(a.split("=", 1)[1])
        elif a.startswith("--skip-group="):
            skip_groups.add(a.split("=", 1)[1])
        elif not a.startswith("--"):
            paths.append(a)

    if not paths:
        print(__doc__)
        return 2
    if not banlist.is_file():
        print(f"FAIL: no ban list at {banlist}")
        return 2

    rules = load_rules(banlist, skip_groups)
    targets, missing = resolve(paths)
    if missing:
        print("FAIL: these paths do not exist — a mistyped path is a tool failure, not a")
        print("      clean run over zero files:")
        for m in missing:
            print(f"        {m}")
        return 2
    if not targets:
        print("FAIL: the paths given match no files — that is a tool failure, not a clean run.")
        return 2

    hits = scan(targets, rules)

    print("# BAN SCAN — a locale's own ban list, applied to its own artefacts")
    print(f"# ban list: {banlist}")
    print(f"# {len(targets)} file(s) · {len(rules)} rule(s)"
          + (f" · skipped group(s): {', '.join(sorted(skip_groups))}" if skip_groups else ""))
    print(f"# ({SKIPPABLE_HINT})\n")
    if not hits:
        print("ok — no banned string found.")
        return 0

    by_key = {(g, n): spec for g, n, _, spec in rules}
    worst = 0
    for key, occurrences in sorted(hits.items(), key=lambda kv: -len(kv[1])):
        group, name = key
        spec = by_key[key]
        print(f"## [{group}] {name} — {len(occurrences)} hit(s)")
        if spec.get("why"):
            print(f"   WHY BANNED: {spec['why']}")
        print(f"   INSTEAD: {spec.get('instead', '(see the sheet)')}")
        if spec.get("do_not_confuse_with"):
            print(f"   ! DO NOT CONFUSE WITH: {spec['do_not_confuse_with']}")
        for f, i, line, matched in occurrences[:12]:
            print(f"     {f}:{i}  «{matched}»  {line}")
        if len(occurrences) > 12:
            print(f"     … and {len(occurrences) - 12} more")
        print()
        worst += len(occurrences)

    print(f"TOTAL: {worst} hit(s). Each is either a real defect or a line the skip-heuristic")
    print("should have skipped — READ THEM. A ban list obeyed without being read is how a")
    print("correct measurement gets applied to the wrong word. And a rule that keeps producing")
    print("false positives is itself the defect: NARROW IT, do not learn to ignore it.")
    return 1


# --------------------------------------------------------------------------- self-test

def self_test():
    import tempfile

    fails = []

    def check(label, got, want):
        if got == want:
            print(f"  ok   {label} -> {got!r}")
        else:
            print(f"  FAIL {label} -> got {got!r}, want {want!r}")
            fails.append(label)

    print("banscan --self-test")
    print(f"  -- the shipped ban list must load and compile: {DEFAULT_BANLIST.name}")
    rules = load_rules(DEFAULT_BANLIST, set())
    check("every rule compiles", len(rules) > 0, True)
    print(f"  info {len(rules)} rule(s) across "
          f"{len({g for g, _, _, _ in rules})} group(s)")

    groups = {g for g, _, _, _ in rules}
    skipped = load_rules(DEFAULT_BANLIST, {"typography"})
    check("--skip-group drops exactly that group",
          {g for g, _, _, _ in skipped}, groups - {"typography"})

    with tempfile.TemporaryDirectory() as d:
        dd = pathlib.Path(d)

        # A rule must NOT fire on a line that quotes the ban in order to state it. That is the
        # property the whole skip-heuristic exists for.
        (dd / "quoting.md").write_text("⛔ irgendein verbotener String steht hier\n", encoding="utf-8")
        check("a line carrying a rejection marker is skipped",
              scan([dd / "quoting.md"], rules), {})

        (dd / "clean.md").write_text("Ein unauffaelliger deutscher Satz ohne Befund.\n",
                                     encoding="utf-8")
        check("a clean line produces no hit", scan([dd / "clean.md"], rules), {})

        # An `own_voice` rule must hold in the narration and exempt a quoted prompt example.
        anrede = [r for r in rules if r[1] == "du-Anrede"]
        check("the du-Anrede rule declares scope own_voice",
              bool(anrede) and anrede[0][3].get("scope"), "own_voice")
        if anrede:
            (dd / "voice.md").write_text("Wenn du das liest, ist es ein Befund.\n", encoding="utf-8")
            check("a `du` in the book's own voice is still a hit",
                  len(scan([dd / "voice.md"], anrede)), 1)
            (dd / "quoted.md").write_text(
                "Ein Prompt, der „Nenne deine Quellen“ sagt, ist korrekte Prosa.\n",
                encoding="utf-8")
            check("a `du` inside a quoted prompt example is NOT a hit",
                  len(scan([dd / "quoted.md"], anrede)), 0)
            # The exemption must not disable the rule for unscoped rules on the same line.
            unscoped = [(g, n, rx, {k: v for k, v in s.items() if k != "scope"})
                        for g, n, rx, s in anrede]
            check("without the scope declaration the same line WOULD be a hit "
                  "(this is the false positive that forced the narrowing)",
                  len(scan([dd / "quoted.md"], unscoped)), 1)

        # Fail closed on a malformed list rather than silently drop the rule.
        bad = dd / "bad.json"
        bad.write_text('{"g": {"r": {"instead": "x"}}}', encoding="utf-8")
        try:
            load_rules(bad, set())
            print("  FAIL a rule with no 're' key was accepted")
            fails.append("missing 're' key")
        except ValueError:
            print("  ok   a rule with no 're' key raises instead of being dropped")

        bad2 = dd / "bad2.json"
        bad2.write_text('{"g": {"r": {"re": "([unclosed"}}}', encoding="utf-8")
        try:
            load_rules(bad2, set())
            print("  FAIL an uncompilable regex was accepted")
            fails.append("uncompilable regex")
        except re.error:
            print("  ok   an uncompilable regex raises instead of being dropped")

        # A mistyped path must be a named tool failure, never a crash and never a clean run.
        # The earlier version raised FileNotFoundError here; this self-test is what found it.
        t, missing = resolve([str(dd / "does-not-exist")])
        check("a nonexistent path is reported MISSING, not passed through", (t, len(missing)), ([], 1))
        check("a mistyped path exits 2 rather than crashing",
              main(["banscan.py", str(dd / "does-not-exist")]), 2)
        check("an existing dir with no .md is a tool failure, not a pass",
              main(["banscan.py", str(dd / "empty-dir")]) if (dd / "empty-dir").mkdir() is None else None, 2)

    print()
    if fails:
        print(f"banscan --self-test: FAIL ({len(fails)}): {'; '.join(fails)}")
        return 1
    print("banscan --self-test: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else main(sys.argv))
