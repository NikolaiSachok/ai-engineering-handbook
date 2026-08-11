#!/usr/bin/env python3
"""Russian canon gate — assert four rulings the corpus broke silently, three of them twice.

usage:  python3 scripts/ru-canon-check.py [root ...]     # default: i18n/ru
        python3 scripts/ru-canon-check.py --self-test

WHY THIS FILE EXISTS. Every rule below was already written into `editorial/canon/ru/`, and
every one of them was violated in SHIPPED, DEPLOYED prose. The sibling `sk-canon-check.py`
says it best and it governs here too: writing a rule into the canon does not enforce it; only
a gate does. Russian earned its own gate the same way Slovak did — by drifting back after
being fixed.

The sharper lesson, which is why this file checks four rules and not one. Twice, a rule
survived only as an ILLUSTRATION, and the illustration taught the losing form:

  * `_language.md` stated the decimal-comma rule and demonstrated it with a SPACED «34,85 %»,
    while 175 corpus instances were tight. The spaced form then survived a full page rebuild,
    because the writer had the canon example in front of it and copied it (#544).
  * The `gate` collocation card offered «эти контроли»/«оба контроля» as a licensed back-
    reference for three weeks after the owner ruled that plural out (#546).

A rule that exists only as an example teaches the example. So each rule below is now stated
with its count and its reasoning in the canon, AND asserted here.

WHAT IS CHECKED

  1. `AI` IS LATIN, «ИИ» IS BANNED. Canon `_language.md`: "латиницей во всех позициях, никогда
     «ИИ»". The corpus carried 52 violations (#539); the page-rebuild wave cleared 50 of them
     and the last two sat in the AI-SDLC glossary, in definitions — the highest-traffic prose
     on the site.

  2. PERCENT SIGN IS TIGHT. Canon `_language.md`: «20%», never «20 %». The printers' norm for
     Russian typesetting wants a space; the corpus decided otherwise and decided it decisively
     — 175 tight against 45 spaced, with all 45 sitting in two files of one course, one of
     which disagreed with itself on the same page. Adjacent lessons disagreeing about the same
     numeral costs a reader more than the deviation does (#544).

  3. «КОНТРОЛИ» PLURAL IS BANNED. Owner ruling 2026-08-10 (issue #269): the plural is not
     Russian. A countable set of controls takes the head noun — «средства контроля»,
     «механизмы контроля» — never a pluralised «контроль».

  4. «ГЕЙТ» IS BANNED. Owner ruling 2026-08-10, and the reasoning is worth keeping: the
     transliteration looked well attested, and EVERY attesting source was from 2026. Post-2023
     Russian tech writing is substantially model-generated, so "I searched and it's attested"
     collapses into "models like this word". Four human-written pre-2023 articles on the
     identical topic contain the Cyrillic form zero times and all keep `Quality Gate` in Latin.

NO IGNORE LIST, BY POLICY — the reason `locale-parity-check.sh` gives governs here: a gate with
an ignore list is a gate nobody reads. The corpus was corrected first so this ships green.

WHAT THIS DELIBERATELY DOES NOT DO, stated because a silent limit reads as coverage.

  * It does not check terminology that requires reading meaning — whether `gate` in a given
    sentence is a countable point («проверка») or a mass process («контроль») is a judgement
    the sense card makes and a regex cannot. That stays with the per-page critics.
  * Rule 1 matches «ИИ» only as a standalone word. A Cyrillic «ИИ» inside a longer token is not
     flagged, because the real-world instances are all standalone and a substring match would
     fire on unrelated capitalised text.
  * Rule 2 accepts a space between a numeral and `%` inside fenced code blocks and inline code,
    where the string may be a literal being quoted rather than prose being typeset.
"""
import re
import sys
from pathlib import Path

DEFAULT_ROOTS = ["i18n/ru"]

# «ИИ» as a standalone word — Cyrillic И twice, not part of a longer Cyrillic run.
RE_II = re.compile(r"(?<![А-Яа-яЁё])ИИ(?![А-Яа-яЁё])")
# digit, then a space (plain, NBSP or narrow NBSP), then the percent sign
RE_SPACED_PCT = re.compile(r"\d[   ]%")
# «контроли» / «контролей» / «контролям» … — the pluralised noun, not the verb «контролируешь»
RE_KONTROLI = re.compile(r"(?<![А-Яа-яЁё])контрол(?:и|ей|ям|ями|ях)(?![А-Яа-яЁё])", re.IGNORECASE)
RE_GEYT = re.compile(r"(?<![А-Яа-яЁё])гейт[а-яё]*(?![А-Яа-яЁё])", re.IGNORECASE)

RULES = [
    ("AI-latin", RE_II, "«ИИ» — AI is written in Latin in every position"),
    ("percent-tight", RE_SPACED_PCT, "percent sign must be tight to the numeral: «20%», not «20 %»"),
    ("kontroli-plural", RE_KONTROLI,
     "«контроли» plural is banned — use «средства контроля» / «механизмы контроля»"),
    ("geyt", RE_GEYT, "«гейт» is banned — render the sense (проверка / контроль) or keep Latin"),
]

FENCE = re.compile(r"^\s*```")
INLINE_CODE = re.compile(r"`[^`]*`")


def strip_code(line: str) -> str:
    """Blank out inline code so a quoted literal is not read as prose typography."""
    return INLINE_CODE.sub(lambda m: " " * len(m.group(0)), line)


def scan(path: Path) -> list[tuple[int, str, str, str]]:
    out = []
    in_fence = False
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if FENCE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = strip_code(raw)
        for name, rx, why in RULES:
            for m in rx.finditer(line):
                out.append((n, name, m.group(0), why))
    return out


def run(roots: list[str]) -> int:
    files = sorted(p for r in roots for p in Path(r).rglob("*")
                   if p.is_file() and p.suffix in (".md", ".mdx", ".json"))
    findings = [(p, *f) for p in files for f in scan(p)]
    counts: dict[str, int] = {}
    for _, _, name, _, _ in findings:
        counts[name] = counts.get(name, 0) + 1

    for path, line, name, hit, why in findings:
        print(f"{path}:{line}: [{name}] {hit!r} — {why}")

    scanned = len(files)
    if findings:
        summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
        print(f"\nru-canon-check: FAIL — {len(findings)} violation(s) in {scanned} file(s) ({summary})")
        return 1
    print(f"ru-canon-check: PASS — {scanned} file(s), 0 violations across {len(RULES)} rules")
    return 0


def self_test() -> int:
    """Each rule must fire on a known-bad string and stay silent on a known-good one.

    A gate that cannot demonstrate it fires is indistinguishable from a gate that is broken —
    which is exactly how three unmeasured pages hid behind a green diagram gate for six days.
    """
    cases = [
        (RE_II, "как ИИ влияет на скорость", True),
        (RE_II, "как AI влияет на скорость", False),
        (RE_II, "ИИИ-подобная строка", False),
        (RE_SPACED_PCT, "выросла на 24 % за месяц", True),
        (RE_SPACED_PCT, "выросла на 24% за месяц", False),
        (RE_SPACED_PCT, "сложность 34,85 % — нет", True),
        (RE_KONTROLI, "эти контроли не сработали", True),
        (RE_KONTROLI, "эти средства контроля не сработали", False),
        (RE_KONTROLI, "ты контролируешь работу", False),
        (RE_GEYT, "блокирующий гейт в CI", True),
        (RE_GEYT, "блокирующая проверка в CI", False),
    ]
    bad = 0
    for rx, text, should_fire in cases:
        fired = bool(rx.search(text))
        if fired != should_fire:
            print(f"self-test FAIL: {text!r} expected fire={should_fire}, got {fired}")
            bad += 1
    # the inline-code carve-out must actually carve out
    if RE_SPACED_PCT.search(strip_code("литерал `20 %` в коде")):
        print("self-test FAIL: inline code was not stripped before the percent check")
        bad += 1
    if not RE_SPACED_PCT.search(strip_code("в прозе 20 % — дефект")):
        print("self-test FAIL: prose percent was stripped when it should not be")
        bad += 1
    if bad:
        print(f"ru-canon-check self-test: FAIL ({bad})")
        return 1
    print(f"ru-canon-check self-test: PASS ({len(cases) + 2} cases, {len(RULES)} rules)")
    return 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--self-test"]
    if "--self-test" in sys.argv[1:]:
        sys.exit(self_test())
    sys.exit(run(args or DEFAULT_ROOTS))
