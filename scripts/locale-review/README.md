# `scripts/locale-review/` — instruments for reviewing a translated locale

These are the measuring instruments behind the German locale's gate stack
(`editorial/de-locale-playbook.md` §4). They were built across three translation waves, are
locale-parameterised, and are kept here because the Russian and Slovak re-gate needs exactly
these tools and there is no reason for the next locale to rediscover them.

**Most are review instruments; the German prose ban scan also gates CI.** `scripts/leak-scan.sh`, `scripts/i18n-link-check.sh` and
`scripts/locale-parity-check.sh` pass or fail CI. The instruments produce a **work list** that a
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
python3 scripts/locale-review/banscan.py editorial/ --skip-group=typography --metaprose
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

## Ban-scan scope and severity

`banscan.py` shares `census.py`'s shipping-prose extractor: fences, inline code, complete JSX/HTML
attribute lists, URLs and link destinations are excluded; headings, link labels and component children
remain prose. Explicit escaped heading IDs are route metadata, while malformed bare IDs remain checkable.
Line numbers still refer to the original file. `--metaprose` alone enables the rejection-marker heuristic
for ledgers quoting rejected forms; shipping prose never skips a whole line because it says `NICHT`.

Every German rule declares a severity. `absolute` findings fail the scan. `scoped` findings fail after
the declared `scope`, `exempt_re` and/or `path_re` have been applied. Exemptions remove only the matched
span, so a second violation on the same line remains visible. `advisory` word fields remain in the
work list but do not fail. Missing severity defaults to `absolute`; unknown severity/scope or malformed
regex is a tool error. The source-term bridges, proper model names, MCP SDK Tier labels, Grounding gloss
and model-internal safeguards have specific executable exemptions rather than file ignore lists.
`do_not_confuse_with` explains the Tool-Katalog referent; its protected form is also in `exempt_re`.

A ban governs a concept/sense, and a matching ban takes precedence over corpus precedent. A shipped
page can retain an older defect. It cannot license copying that defect. Word-field advisories still
require reading: `Leitung` for departmental leadership and `Redaktion` for editorial work are legitimate.

The existing `locale-review-tools` CI job runs the instrument self-tests and then
`python3 scripts/locale-review/banscan.py i18n/de/`. Only absolute/scoped findings fail; advisories
remain visible. The extractor deliberately excludes fenced diagrams and JSX attributes, so a clean
scan does not certify all visible translated text. RU and SK have their own narrower canon gates
(`ru-canon-check.py`, `sk-canon-check.py`), not a comprehensive machine-readable ban list. Those checks
cannot certify every retrospective lexical ruling in their prose canons either.
