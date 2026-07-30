#!/usr/bin/env python3
"""Assert invisible codepoints in a file — BY READING BYTES, never through a shell string.

WHY THIS FILE EXISTS AT ALL, and why it is not a one-liner in a brief.

The German typography rules turn on characters a reader cannot see and a terminal does not
show: U+202F NARROW NO-BREAK SPACE (the thousands separator and the space before `%`),
U+00A0 NO-BREAK SPACE (the tolerated fallback, which is a defect where U+202F is the form),
U+2009 THIN SPACE, and the zero-width family. Whether the shipped page carries the right one
is a gated assertion.

THE FAILURE THIS REPLACES. A run verified that assertion with

    python3 -c "print(open('page.md').read().count('<the character, pasted inline>'))"

inside DOUBLE QUOTES, and it printed `U+202F: 0` for a file that demonstrably contained
U+202F. The character never reached Python: it was consumed somewhere in the shell's own
handling of the argument. The probe was confident, well-formed, and measured a string that no
longer existed — the same shape as every other input failure this project has hit, and the
eighth of them.

THE RULE, therefore, and it is not "be careful with quoting":
  * a codepoint assertion NEVER travels through a shell argument, a shell variable, or an
    interpolated string. It is named by its NUMBER (`U+202F`) in source, and the character is
    constructed from that number inside Python;
  * the file is opened and read as BYTES, then decoded explicitly, so a mis-declared encoding
    surfaces as an error instead of as a silent zero;
  * a zero is only believed when the run also proves it can see the character at all. Every
    invocation carries a POSITIVE CONTROL: a fixture string built from the codepoint numbers,
    counted by the same code path. If the control does not register, the run fails and no
    count is reported.

Usage:
    codepoints.py <file> [<file> ...]           # census of the invisible codepoints
    codepoints.py --assert-percent <file> ...   # gate: every `%` takes U+202F, nothing else
    codepoints.py --self-test
"""

from __future__ import annotations

import pathlib
import re
import sys
import unicodedata

# Named by NUMBER, never pasted as a literal. This is the whole point of the file: nothing
# below can be destroyed by a quoting layer, because there is no character to destroy until
# Python builds one.
WATCHED: dict[str, str] = {
    "U+00A0": "NO-BREAK SPACE — the tolerated fallback; a defect where U+202F is the form",
    "U+2009": "THIN SPACE — not the norm's separator",
    "U+202F": "NARROW NO-BREAK SPACE — the German thousands separator and the space before %",
    "U+2007": "FIGURE SPACE",
    "U+200B": "ZERO WIDTH SPACE — invisible, and a word-boundary bug in any grep",
    "U+200E": "LEFT-TO-RIGHT MARK",
    "U+FEFF": "ZERO WIDTH NO-BREAK SPACE / BOM",
    "U+00AD": "SOFT HYPHEN — invisible, and it breaks a compound at an arbitrary point",
    "U+2011": "NON-BREAKING HYPHEN",
    "U+2013": "EN DASH — the Gedankenstrich, correct when spaced",
    "U+2014": "EM DASH — forbidden in this corpus",
}


def ch(name: str) -> str:
    """`U+202F` -> the character. The only place a watched character is ever constructed."""
    if not re.fullmatch(r"U\+[0-9A-Fa-f]{4,6}", name):
        raise ValueError(f"not a codepoint name: {name!r}")
    return chr(int(name[2:], 16))


def read_text(path: pathlib.Path) -> str:
    """Read as BYTES and decode explicitly, so a bad encoding raises instead of returning a
    plausible string. `errors='strict'` is the assertion."""
    return path.read_bytes().decode("utf-8", errors="strict")


def positive_control() -> tuple[bool, list[str]]:
    """Prove this code path can see every watched codepoint before any count is believed.

    Builds a fixture containing each character exactly once, from the codepoint numbers, and
    counts it with the same function the real files go through. A zero here means the run
    cannot see the character, and therefore that a zero on a real file means nothing.
    """
    missed = []
    for name in WATCHED:
        c = ch(name)
        fixture = f"a{c}b"
        if fixture.count(c) != 1:
            missed.append(name)
    return (not missed), missed


def census(paths: list[pathlib.Path]) -> int:
    ok, missed = positive_control()
    print("# POSITIVE CONTROL — read this before any number below")
    if not ok:
        print(f"  FAIL the run cannot see: {', '.join(missed)}. Every count below is worthless.")
        return 2
    print(f"  ok all {len(WATCHED)} watched codepoints are visible to this code path;")
    print("     a zero below is therefore a real zero and not a destroyed character.\n")

    rc = 0
    for p in paths:
        if not p.is_file():
            print(f"FAIL: not a file: {p}")
            rc = 2
            continue
        text = read_text(p)
        print(f"## {p}  ({len(text)} chars, {len(p.read_bytes())} bytes)")
        for name, why in WATCHED.items():
            n = text.count(ch(name))
            mark = "   " if n == 0 else " * "
            print(f"  {mark}{name}  {n:>5}   {unicodedata.name(ch(name), '?')} — {why}")
        print()
    return rc


PERCENT_FORMS = [
    ("U+202F", 0, "THE FORM — a digit, U+202F, then %"),
    ("U+00A0", 1, "the fallback space; a defect where U+202F is the form"),
    ("U+2009", 1, "a thin space; not the norm's separator"),
]


def assert_percent(paths: list[pathlib.Path]) -> int:
    """Gate: in this corpus every `%` preceded by a digit takes U+202F and nothing else.

    Includes the tight form (`20%`) and the plain-ASCII-space form (`20 %`), both forbidden.
    """
    ok, missed = positive_control()
    if not ok:
        print(f"FAIL: positive control failed for {', '.join(missed)} — no count is reportable.")
        return 2

    # Prove the matcher itself fires, on a fixture built from the numbers.
    probe = "20" + ch("U+202F") + "%"
    if len(re.findall(r"\d" + ch("U+202F") + "%", probe)) != 1:
        print("FAIL: the U+202F percent matcher does not match its own fixture.")
        return 2

    rc = 0
    for p in paths:
        if not p.is_file():
            print(f"FAIL: not a file: {p}")
            rc = 2
            continue
        text = read_text(p)
        good = len(re.findall(r"\d" + ch("U+202F") + "%", text))
        tight = len(re.findall(r"\d%", text))
        plain = len(re.findall(r"\d %", text))
        bad = [(n, len(re.findall(r"\d" + ch(n) + "%", text))) for n, _, _ in PERCENT_FORMS[1:]]
        wrong = tight + plain + sum(c for _, c in bad)
        status = "ok  " if wrong == 0 else "FAIL"
        detail = f"U+202F={good} tight={tight} plain-space={plain} " + " ".join(
            f"{n}={c}" for n, c in bad
        )
        print(f"{status} {p}  {detail}")
        if wrong:
            rc = 1
    print()
    print("assert-percent: PASS" if rc == 0 else "assert-percent: FAIL")
    return rc


def self_test() -> int:
    fails: list[str] = []

    def check(label, got, want):
        if got == want:
            print(f"  ok   {label} -> {got!r}")
        else:
            print(f"  FAIL {label} -> got {got!r}, want {want!r}")
            fails.append(label)

    print("codepoints --self-test")
    check("ch('U+202F') is one character", len(ch("U+202F")), 1)
    check("ch('U+202F') is the narrow no-break space",
          unicodedata.name(ch("U+202F")), "NARROW NO-BREAK SPACE")
    check("ch rejects a non-codepoint", isinstance(_err(lambda: ch("202F")), ValueError), True)

    ok, missed = positive_control()
    check("the positive control passes", (ok, missed), (True, []))

    # The regression this file exists for, reproduced on a real temporary file: a count must
    # be non-zero on a file that contains the character.
    import tempfile

    with tempfile.TemporaryDirectory() as d:
        p = pathlib.Path(d) / "fixture.md"
        body = "Ein Anteil von 20" + ch("U+202F") + "% und 1" + ch("U+202F") + "000 Zeilen.\n"
        p.write_bytes(body.encode("utf-8"))
        text = read_text(p)
        check("U+202F is SEEN on a file that contains it (the defect: this returned 0)",
              text.count(ch("U+202F")), 2)
        check("the percent gate passes on the correct form", assert_percent([p]), 0)

        bad = pathlib.Path(d) / "bad.md"
        bad.write_bytes(("Ein Anteil von 20% und 30 % und 40" + ch("U+00A0") + "%.\n").encode())
        check("the percent gate FAILS on tight, plain and U+00A0 forms", assert_percent([bad]), 1)

        # Fail closed on a mis-encoded file rather than return a plausible string.
        latin = pathlib.Path(d) / "latin.md"
        latin.write_bytes("Grüße".encode("latin-1"))
        check("a non-UTF-8 file raises instead of decoding to something plausible",
              isinstance(_err(lambda: read_text(latin)), UnicodeDecodeError), True)

    print()
    if fails:
        print(f"codepoints --self-test: FAIL ({len(fails)}): {'; '.join(fails)}")
        return 1
    print("codepoints --self-test: PASS")
    return 0


def _err(fn):
    try:
        fn()
    except Exception as e:  # noqa: BLE001 — the self-test wants the exception object itself
        return e
    return None


def main(argv: list[str]) -> int:
    args = argv[1:]
    if not args or "--self-test" in args:
        return self_test() if "--self-test" in args else (print(__doc__) or 2)
    if args[0] == "--assert-percent":
        paths = [pathlib.Path(a) for a in args[1:]]
        return assert_percent(paths) if paths else (print("no files given") or 2)
    return census([pathlib.Path(a) for a in args])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
