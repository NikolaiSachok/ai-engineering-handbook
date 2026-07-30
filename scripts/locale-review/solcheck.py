#!/usr/bin/env python3
"""Validate a Sol verdict file against the page it claims to be about.

Discards, with the reason printed:
  * any verdict whose ZITAT is not VERBATIM in the page  -> fabricated citation;
  * any verdict with no BEFUND, or a BEFUND naming no linguistic phenomenon;
  * any verdict proposing a replacement (the prompt forbids it — if one appears, the prompt
    leaked, and that is itself a finding).

WHAT THE VERBATIM RULE BOUGHT, and the correction to the claim this file used to make.
The earlier docstring said a wave had run ~450 verdicts through this shape and found ZERO
fabricated citations, and concluded that "a non-zero means the gate's input or prompt drifted".

Re-counted over the 28 verdict files of the third wave: **334 blocks, 313 accepted, 21
discarded — 8 of them FABRICATED CITATIONS and 13 a BEFUND naming no phenomenon.** So the
zero was a property of one wave and not of the method, and the inference drawn from it was
wrong: a non-zero here does NOT imply drift. It is the ordinary behaviour of a stochastic
judge sampled more often, and this validator catching 8 of them is the mechanism WORKING.

The load-bearing claim is therefore the narrower one, and it is the true one: **across ~450
verdicts no fabricated citation was ever ACTED ON**, because every quote is checked against
the page before a verdict reaches a work list. Do not restore the stronger claim.

Usage: solcheck.py <page-path> <verdict-file>
       solcheck.py --self-test
"""

from __future__ import annotations

import collections
import pathlib
import re
import sys
import unicodedata

PHENOMENA = [
    "satzklammer", "verbzweit", "verbletzt", "verb-letzt", "rektion", "kasus", "genus",
    "nominalstil", "denglisch", "partizip", "von-genitiv", "genitiv", "wortstellung",
    "kollokation", "funktionsverb", "präposition", "tempus", "kongruenz", "register",
    "wendung", "idiom", "artikel", "plural", "komposit", "durchkopplung", "ellipse",
    "anrede", "imperativ", "passiv", "reflexiv", "adjektivendung", "wortbildung",
]

REPLACEMENT_RE = re.compile(r"(besser wäre|stattdessen|ersetzen durch|schlage vor|→)", re.I)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()


def validate(page: str, raw: str):
    """Return (accepted, discarded). accepted: [(verdict, quote, befund)];
    discarded: [(reason, excerpt)]."""
    page_n = norm(page)
    ok, bad = [], []
    for b in re.split(r"\n(?=ZITAT:)", raw):
        if "ZITAT:" not in b:
            continue
        z = re.search(r"ZITAT:\s*(.*?)(?=\nURTEIL:|\Z)", b, re.S)
        u = re.search(r"URTEIL:\s*(\S+)", b)
        f = re.search(r"BEFUND:\s*(.*?)(?=\nZITAT:|\Z)", b, re.S)
        if not (z and u):
            bad.append(("malformed block", b[:160]))
            continue
        quote = norm(z.group(1)).strip("„\"'" + "“”")
        verdict = u.group(1).strip().upper()
        befund = norm(f.group(1)) if f else ""
        if quote and quote not in page_n:
            bad.append(("FABRICATED CITATION — quote is not verbatim in the page", quote[:160]))
            continue
        if verdict != "NATIV":
            if not befund:
                bad.append(("no BEFUND", quote[:100]))
                continue
            if not any(p in befund.lower() for p in PHENOMENA):
                bad.append(("BEFUND names no linguistic phenomenon", befund[:160]))
                continue
        if REPLACEMENT_RE.search(befund):
            bad.append(("PROPOSES A REPLACEMENT — the prompt forbids this; the prompt leaked",
                        befund[:160]))
            continue
        ok.append((verdict, quote, befund))
    return ok, bad


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2
    page_path, verdict_path = pathlib.Path(argv[1]), pathlib.Path(argv[2])
    for p in (page_path, verdict_path):
        if not p.is_file():
            print(f"FAIL: not a file: {p}")
            return 2
    ok, bad = validate(page_path.read_text(encoding="utf-8"),
                       verdict_path.read_text(encoding="utf-8"))

    print(f"# Sol verdicts for {page_path}")
    print(f"# accepted: {len(ok)}   discarded: {len(bad)}\n")
    print("## verdict distribution:", dict(collections.Counter(v for v, _, _ in ok)), "\n")
    print("## DISCARDED")
    for why, what in bad:
        print(f"   [{why}] {what}")
    if not bad:
        print("   (none)")
    print("\n## ACCEPTED, non-NATIV (the work list)")
    for v, q, f in ok:
        if v != "NATIV":
            print(f"\n   {v}\n     ZITAT:  {q}\n     BEFUND: {f}")
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

    print("solcheck --self-test")
    page = ("Der Dienst laeuft.\nEine Antwort ist keine Garantie und der\n"
            "Index haelt jedes Dokument.\nEin Anteil von 20 Prozent.\n")

    good = ("ZITAT: der Index haelt jedes Dokument\n"
            "URTEIL: ÜBERSETZT\n"
            "BEFUND: Kollokationsbruch; das Verb nimmt dieses Objekt im Deutschen nicht.\n")
    ok, bad = validate(page, good)
    check("a verbatim quote with a named phenomenon is accepted", (len(ok), len(bad)), (1, 0))
    check("the accepted verdict keeps its grade", ok[0][0], "ÜBERSETZT")

    # THE ASSERTION THAT MATTERS: a quote that is not in the page never reaches a work list.
    fabricated = ("ZITAT: dieser Satz steht nirgends auf der Seite\n"
                  "URTEIL: ÜBERSETZT\nBEFUND: Kollokationsbruch; frei erfunden.\n")
    ok, bad = validate(page, fabricated)
    check("a fabricated citation is discarded", (len(ok), len(bad)), (0, 1))
    check("and it is discarded FOR THAT REASON", "FABRICATED CITATION" in bad[0][0], True)

    # A quote that spans a line break in the page must still validate: the page is normalised
    # before comparison, or every multi-line quote would be a false fabrication.
    wrapped = ("ZITAT: Eine Antwort ist keine Garantie und der Index haelt jedes Dokument\n"
               "URTEIL: VERDÄCHTIG\nBEFUND: Wortstellung; folgt der englischen Reihenfolge.\n")
    ok, bad = validate(page, wrapped)
    check("a quote spanning a line break is NOT a false fabrication", (len(ok), len(bad)), (1, 0))

    vague = ("ZITAT: Der Dienst laeuft.\nURTEIL: ÜBERSETZT\n"
             "BEFUND: klingt holprig und unnatuerlich.\n")
    ok, bad = validate(page, vague)
    check("a BEFUND naming no phenomenon is discarded", (len(ok), len(bad)), (0, 1))
    check("and for that reason", "names no linguistic phenomenon" in bad[0][0], True)

    proposes = ("ZITAT: Der Dienst laeuft.\nURTEIL: ÜBERSETZT\n"
                "BEFUND: Kollokationsbruch; besser waere eine andere Fuegung. → so\n")
    ok, bad = validate(page, proposes)
    check("a replacement proposal is discarded (the prompt forbids it)", (len(ok), len(bad)), (0, 1))
    check("and it is reported as a PROMPT LEAK", "PROPOSES A REPLACEMENT" in bad[0][0], True)

    nativ = "ZITAT: Der Dienst laeuft.\nURTEIL: NATIV\nBEFUND: \n"
    ok, bad = validate(page, nativ)
    check("a NATIV verdict needs no BEFUND", (len(ok), len(bad)), (1, 0))

    check("an empty verdict file yields nothing rather than crashing", validate(page, ""), ([], []))

    print()
    if fails:
        print(f"solcheck --self-test: FAIL ({len(fails)}): {'; '.join(fails)}")
        return 1
    print("solcheck --self-test: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(self_test() if "--self-test" in sys.argv else main(sys.argv))
