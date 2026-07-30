# `scripts/locale-review/` — instruments for reviewing a translated locale

These are the measuring instruments behind the German locale's gate stack
(`editorial/de-locale-playbook.md` §4). They were built across three translation waves, are
locale-parameterised, and are kept here because the Russian and Slovak re-gate needs exactly
these tools and there is no reason for the next locale to rediscover them.

**They are not build gates.** `scripts/leak-scan.sh`, `scripts/i18n-link-check.sh` and
`scripts/locale-parity-check.sh` pass or fail CI. These produce a **work list** that a
reviewer then acts on. That difference is the whole reason each one carries a self-test: a
broken build gate goes red, whereas a broken instrument returns a confident, well-formed,
**wrong** answer — which is what happened eight separate times.

## The eight input failures, and where each is now asserted

Every failure below returned a plausible result. None of them looked like a bug.

| # | Failure | Symptom | Asserted in |
|---|---|---|---|
| 1 | **truncating** the input | the judge fabricates verdicts about text it never saw | `solrun.sh` |
| 2 | **narrowing** the input | the judge fabricates ABSENCES — "this page is clean" | `solrun.sh` |
| 3 | a **shared scratch path** | verdicts about a *different* lesson, confidently reported | `solrun.sh` (slug-scoped paths) |
| 4 | a **silent zero** | the call returned nothing; the run looked like a clean page | `solrun.sh` |
| 5 | a **trailing-context matcher** | dropped the inflected occurrence that mattered | `concord.py`, `referents.py` |
| 6 | an **uppercase-node-ID heuristic** | ate a Mermaid label (`G[GPU]` — id `G`, label `GPU`) | `mermaid_gate.py` |
| 7 | a **fixed word-window scorer** | a working gate looked dead on a short page | `solrun.sh` (scaled floor) |
| 8 | a **quoted shell probe** | destroyed U+202F and reported `0` on a file containing it | `codepoints.py` |

Two further defects were in the *scope* of an assertion rather than its input, and are asserted
in `census.py` (fenced blocks and multi-line JSX counted as prose — 50 false positives) and in
`cardwidth.mjs` (an SPA-fallback server returning the wrong page — see below).

**Always carry a positive control.** Every count that can be zero is accompanied by proof the
run could see a non-zero. A zero with no positive control is not a null result; it is an
unfalsifiable one.

## The tools

| File | What it does |
|---|---|
| `solprompt.py` | builds the cross-model register-gate prompt for ONE page, from the shipped file |
| `mermaid_gate.py` | extracts every translatable Mermaid label; also builds the label-gate prompt |
| `solrun.sh` | drives one page through the gate, asserting the input before believing the output |
| `solcheck.py` | validates verdicts against the page: verbatim quote, named phenomenon, no replacement |
| `census.py` | typography census over *added* lines, classified by whole-file parse |
| `codepoints.py` | invisible-codepoint census and the percent gate, read from **bytes** |
| `concord.py` | full concordance of a term slice over a source tree — nothing truncated |
| `referents.py` | candidate "one referent, several names" collisions, with the matched surface form |
| `banscan.py` | scans any text against a locale's own ban list |
| `cardwidth.mjs` | measures card-label line counts at 360 px against the layout budget |
| `banlist.de.json`, `referent-groups.de.json` | the German data for the two scanners |

## Running them

```bash
scripts/locale-review/self-test.sh            # every tool's own regressions; no build, no network

python3 scripts/locale-review/census.py origin/main --locale=de
python3 scripts/locale-review/codepoints.py --assert-percent i18n/de/**/*.md
python3 scripts/locale-review/mermaid_gate.py labels i18n/de/…/part-3-production
python3 scripts/locale-review/banscan.py editorial/ --skip-group=typography
python3 scripts/locale-review/concord.py A slice-A.terms docs/part-3-production
python3 scripts/locale-review/referents.py scripts/locale-review/referent-groups.de.json i18n/de
bash    scripts/locale-review/solrun.sh <page.md> <slug> [prose|mermaid]
```

`cardwidth.mjs` needs the page served **under its real `baseUrl`**. This is a gate on the tool,
not a detail: a run once used `serve -s build`, whose SPA mode rewrites every unresolved path to
`index.html`, so the browser was handed the English landing page — `lang="en"`, no card markup —
and the metric measured it and reported a number. Serve it the way `e2e/` does:

```bash
npm run build && npm run serve -- --port 3210 --no-open &
node scripts/locale-review/cardwidth.mjs /de/part-3-production/production-failures de
```

The expected locale is an argument and is asserted against the served `<html lang>`; a mismatch
is now a hard failure rather than a line of INFO.

## Three things these tools cannot do

Worth stating, because each was learned by trusting an instrument past its range:

- **A count sees quantities, not referents.** `referents.py` never asserts a merge. It prints a
  sentence per occurrence, because deciding what an occurrence *refers to* is not a counting
  operation — and a count once *invented* a defect that reading immediately dispelled.
- **A count of a translated word is not a count of the English referent**, and a zero on a loan
  is not a zero on the referent (`Managed` 0 against `verwaltet` 9 — same referent, one word
  absent). An unrestricted corpus count measures the corpus's topic mix, not the word's register.
- **A width gate measures pixels, not meaning.** `cardwidth.mjs` will approve a shortened label
  that no longer says what the long one said. Shortening for a layout budget silently changed a
  claim at least once, and nothing in this directory can catch that. A human re-reads the
  shortened string against the claim it is making.
