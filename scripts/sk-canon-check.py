#!/usr/bin/env python3
"""Slovak canon gate — assert two rules that the corpus broke silently for months.

usage:  python3 scripts/sk-canon-check.py [root ...]     # default: i18n/sk
        python3 scripts/sk-canon-check.py --self-test

WHY THIS FILE EXISTS. Both rules it checks were already written down in
`editorial/canon/sk/_language.md`, and both were violated in SHIPPED, DEPLOYED prose. Writing
a rule into the canon does not enforce it; only a gate does. Each check below is here because
a real defect got past every existing gate and was live on the site:

  1. QUOTES. The canon says a Slovak quotation opens with U+201E and closes with U+201C, and
     explicitly rejects the ASCII straight quote. The AI-SDLC course shipped 20 quotations
     opened with U+201E and closed with an ASCII U+0022 (#431). The RAG course was clean, so
     nothing about the language made this inevitable -- one course simply drifted, and the
     only reason it survived is that no check looked. The build stays green either way: a
     wrong quotation mark is valid Markdown.

  2. `pipeline` GENDER. The canon now fixes this indeclinable loan as FEMININE, on the JULS
     rule that an indeclinable borrowing takes the gender of its nearest Slovak semantic
     equivalent (linka / retaz / postupnost). The corpus had it BOTH ways -- 18 masculine
     against 21 feminine across both courses, including an H2 heading contradicting a framing
     page (#432).

NO IGNORE LIST, BY POLICY. `scripts/locale-parity-check.sh` states the reason and it governs
here too: "a gate with an ignore list is a gate nobody reads." The corpus was corrected first
so this check could ship green against it.

WHAT CHECK 2 DELIBERATELY DOES NOT DO -- stated because a silent limit reads as coverage.
It flags only agreement it can attribute with CERTAINTY: an adjective or determiner standing
IMMEDIATELY beside `pipeline`. It does NOT chase agreement across a comma, because that is
exactly where attribution becomes ambiguous, and a false positive there would be a real
sentence a reviewer must defend. The live example: "podiel pipeline, ktory nemoze bezat
subezne" is CORRECT -- `ktory` agrees with `podiel`, not with `pipeline`. A gate that fired on
that would be arguing with the language. So distant agreement ("pipeline ... sa zacinal") is
NOT covered; it is caught by review, not here. Two of the eighteen 2026-08-08 fixes were of
that shape and this gate would not have found them.
"""
import re
import sys
from pathlib import Path

SK_OPEN = chr(0x201E)   # „
SK_CLOSE = chr(0x201C)  # “
ASCII_DQ = chr(0x0022)  # "

# Positive control: prove this process can distinguish the characters before believing a zero.
_ctl = SK_OPEN + ASCII_DQ + SK_CLOSE
assert len({_ctl[0], _ctl[1], _ctl[2]}) == 3, "positive control failed"

# Masculine adjective forms. Feminine is -a/-ej/-u/-ou, so none of these can be feminine.
#
# `-om` is DELIBERATELY ABSENT. It is the masculine-noun instrumental ending (krokom,
# problémom) far more often than an adjectival locative, and including it made the gate fire
# on "zlyhaním problémom pipeline"-shaped prose that is perfectly correct. Losing locative
# agreement ("v statickom pipeline") is the cheaper error: a missed defect costs one review,
# a false positive costs the gate its credibility.
MASC_ADJ = r"\w+(?:ý|ého|ému|ým)"
MASC_DET = r"(?:ten|tento|tamten|onen|svoj|tvoj|môj|náš|váš|každý|nejaký|žiadny)"

# Masculine nouns whose dative/locative is a homograph of an adjectival ending in -ému.
# Only stems ending in -ém collide, so the list is short and closed rather than open-ended.
NOUN_HOMOGRAPH = re.compile(r"(?:systému|problému)$", re.I)

# A noun adjunct may stand between the adjective and `pipeline` without breaking agreement --
# "statický RAG pipeline". Only an all-caps acronym qualifies; any ordinary word between them
# is a noun that the adjective is far likelier to agree with than `pipeline` is.
ADJUNCT = r"(?:[A-Z][A-Z0-9]+[-/]?\s+)?"


def prose(text: str) -> str:
    """Blank out regions where ASCII quotes and English words are CODE, keeping offsets."""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group())

    text = re.sub(r"\A---\n.*?\n---\n", blank, text, flags=re.S)   # YAML frontmatter
    text = re.sub(r"```.*?```", blank, text, flags=re.S)           # fenced code / mermaid
    text = re.sub(r"`[^`\n]*`", blank, text)                       # inline code
    text = re.sub(r"<[^<>\n]*>", blank, text)                      # JSX / HTML tags
    text = re.sub(r"\]\([^)]*\)", blank, text)                     # link targets
    return text


def check_quotes(text: str):
    """An ASCII double quote is a defect only while a U+201E quotation is OPEN.

    Paired, not blanket: a cited English work title (*"Don't Blame the Large Language
    Model"*) carries its own straight quotes in EN and RU too, so it is corpus convention.
    """
    out, depth = [], 0
    for lineno, line in enumerate(prose(text).split("\n"), 1):
        for ch in line:
            if ch == SK_OPEN:
                depth += 1
            elif ch == SK_CLOSE and depth:
                depth -= 1
            elif ch == ASCII_DQ and depth:
                out.append((lineno, "Slovak quotation closed with ASCII U+0022; use U+201C"))
                depth -= 1
    return out


def check_pipeline_gender(text: str):
    """`pipeline` is feminine (canon _language.md §1.1). Adjacent agreement only -- see header."""
    out = []
    for lineno, line in enumerate(prose(text).split("\n"), 1):
        for pat, what in (
            (rf"\b((?:{MASC_ADJ}|{MASC_DET}))\s+{ADJUNCT}[Pp]ipeline\b", "before"),
            (rf"\b[Pp]ipeline\s+({MASC_ADJ})\b", "after"),
        ):
            for m in re.finditer(pat, line):
                if NOUN_HOMOGRAPH.search(m.group(1)):
                    continue
                out.append((lineno, f"masculine agreement {what} `pipeline` "
                                    f"(canon: feminine) -- «{m.group().strip()}»"))
    return out


CHECKS = (("quotes", check_quotes), ("pipeline-gender", check_pipeline_gender))


# ---------------------------------------------------------------------------------------
# SELF-TESTS. Half of them assert the gate stays SILENT: a check that cries wolf on correct
# prose gets ignored inside a week, which is the same outcome as having no check.
# ---------------------------------------------------------------------------------------
SELF_TESTS = [
    # (name, text, expected quote hits, expected gender hits)
    ("ascii close after sk open",
     f"Pravidlo znie {SK_OPEN}pokyn nie je kontrola{ASCII_DQ} a platí.", 1, 0),
    ("correct sk pair is silent",
     f"Pravidlo znie {SK_OPEN}pokyn nie je kontrola{SK_CLOSE} a platí.", 0, 0),
    ("english work title is NOT a defect",
     f'Pozri {ASCII_DQ}Don{chr(0x27)}t Blame the Model{ASCII_DQ} z júla 2026.', 0, 0),
    ("ascii inside a code fence is ignored",
     f"```\nlabel={ASCII_DQ}x{ASCII_DQ}\n```\n{SK_OPEN}veta{SK_CLOSE}", 0, 0),
    ("jsx attribute is ignored",
     f'<Node label={ASCII_DQ}statický režim{ASCII_DQ} />', 0, 0),
    ("masculine adjective before pipeline",
     "Časť I rozoberá statický pipeline: pevnú postupnosť.", 0, 1),
    ("masculine genitive before pipeline",
     "Ide to vedľa vektorového pipeline za routerom.", 0, 1),
    ("determiner before pipeline",
     "Preto je tento pipeline predvoľbou.", 0, 1),
    ("masculine participle after pipeline",
     "Nenahrádza pipeline postavený v lekciách.", 0, 1),
    ("feminine agreement is silent",
     "V Časti II táto statická pipeline ožíva a celá pipeline beží.", 0, 0),
    ("feminine oblique is silent",
     "Regresiu vieš lokalizovať namiesto hádania nad celou pipeline.", 0, 0),
    # THE false positive this gate must never produce -- `ktorý` agrees with `podiel`.
    ("relative pronoun across a comma is NOT attributed",
     "Podiel pipeline, ktorý nemôže bežať súbežne, rastie.", 0, 0),
    ("code identifier is ignored",
     "Jeho prepínač je `pipeline_parallel_size` a mení sa zriedka.", 0, 0),
    ("acronym adjunct does not break agreement",
     "Poskladali sme statický RAG pipeline a agentov nad ním.", 0, 1),
    # --------------------------------------------------------------------------------
    # The five false positives the FIRST draft of this gate produced against the real
    # corpus. Every one is grammatical Slovak in which the masculine adjective agrees with
    # an INTERVENING noun, not with `pipeline`. They are self-tests, not anecdotes: the
    # draft passed all thirteen of its own tests and was still wrong five times on real
    # prose, which is the argument for testing a gate against the corpus before shipping it.
    # --------------------------------------------------------------------------------
    ("intervening noun takes the agreement (locative)",
     "Dve techniky, každá v inom kroku pipeline, riešia tú stratu.", 0, 0),
    ("intervening noun takes the agreement (nominative)",
     "Žiadny neskorší krok pipeline to už nedokáže napraviť.", 0, 0),
    ("masculine adjective binds the noun, feminine binds pipeline",
     "Ten druhý krok pevná pipeline spraviť nevie.", 0, 0),
    ("feminine emphatic pronoun is not masculine",
     "Keď je časťou problému sama pipeline, vypnutie zlyhá.", 0, 0),
    ("noun instrumental in -om is not an adjective",
     "Ak je problémom pipeline, vráť sa o krok späť.", 0, 0),
]


def self_test() -> int:
    failed = 0
    for name, text, want_q, want_g in SELF_TESTS:
        got_q, got_g = len(check_quotes(text)), len(check_pipeline_gender(text))
        if (got_q, got_g) != (want_q, want_g):
            failed += 1
            print(f"  FAIL {name}: want quotes={want_q} gender={want_g}, "
                  f"got quotes={got_q} gender={got_g}")
        else:
            print(f"  ok   {name}")
    print(f"\n{len(SELF_TESTS) - failed}/{len(SELF_TESTS)} self-tests passed")
    return 1 if failed else 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    roots = [a for a in argv if not a.startswith("-")] or ["i18n/sk"]
    findings = 0
    for root in roots:
        for p in sorted(Path(root).rglob("*.md")):
            text = p.read_text(encoding="utf-8")
            for label, fn in CHECKS:
                for lineno, msg in fn(text):
                    print(f"{p}:{lineno}: [{label}] {msg}")
                    findings += 1
    if findings:
        print(f"\nsk-canon-check: {findings} finding(s). "
              f"Rules: editorial/canon/sk/_language.md §Typografia, §1.1")
        return 1
    print("sk-canon-check: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
