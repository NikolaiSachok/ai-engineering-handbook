# Card set — `production-failures`

Ten cards for [Why AI systems fail in production](../../../docs/part-3-production/production-failures.md),
the opener of Part III. Light ground, `4:3` cards + one `16:9` hero, generated with Gemini Pro through the
`create-infographic` skill.

**Status: all ten pending owner approval** (generated 2026-07-26).

## Archive format — the exact batch, not a retyped prompt

The skill asks for one `NN-slug.md` per card. This set archives the **batch JSON that was actually executed**
instead, because it is verbatim: prompt text, `model`, `ratio`, `res`, `ref` and output path in the exact form
the generator received, with no transcription step that could silently drift from what produced the image.

| File | What it produced |
|---|---|
| `prompt-01-corpus.txt` | card 01, the style anchor (third generation; the first two failed the phone test) |
| `batch-01-set.json` | cards 02–09 and the hero, first pass — 9 items, one command |
| `batch-02-fixes.json` | the two regenerations: `05-cost` and `hero` |

To reproduce any card, feed its item back through
`~/.claude/skills/generate-image/references/generate.sh --batch <file>`. Every item in the batches carries
`01-corpus.webp` as its `--ref` — the style anchor for the set — except the two fixes, which anchor on
`06-drift` and `09-four-missed` respectively (chosen for crisp icon linework).

## The cards

| # | File | Node/edge content | Strings |
|---|---|---|---|
| 01 | `01-corpus.webp` | demo: `clean uniform docs` → `index`; the drop: `silently dropped`; prod: `mixed sources` → `layout-aware chunking` → `ingestion manifest` | 9 |
| 02 | `02-retrieval.webp` | demo: `top-k, always` → `confident wrong answer`; prod: `rerank` → `score floor` → brace → `grounded answer` / `or "no context"` | 9 |
| 03 | `03-eval-sets.webp` | demo: `day-one test set` → `false confidence`; prod: `frozen set` + `live sample` → `honest scoreboard` | 8 |
| 04 | `04-green-not-correct.webp` | demo: `200 OK` → `wrong answer`; prod: `pipeline trace` → `judge on sample` → `quality alert` | 8 |
| 05 | `05-cost.webp` | `cheap model` / `3 attempts` vs `expensive model` / `1 attempt`, arrow → `the retry tax`; caption | 7 |
| 06 | `06-drift.webp` | demo: `drift detected` → `retrain the model`; prod ladder: `re-index` → `retrieval mix` → `prompt` → `weights last` | 9 |
| 07 | `07-releases.webp` | demo: `prompt in code` → `every edit ships`; prod: `prompt config` + `pinned model` + `corpus snapshot` → `canary, rollback` | 9 |
| 08 | `08-gates.webp` | demo: `no checks` → `first error spreads`; prod: `schema` → `citations` → `judge`, annotated `cheapest first` | 9 |
| 09 | `09-four-missed.webp` | quadrants: `unscoped access` · `poisoned documents` · `one language only` · `flaky tools`; caption | 6 |
| — | `hero.webp` | `demo` platform, broken span, larger `production` platform; caption | 4 |

Every card is at or under the 9-string budget. Cards 02, 06, 07 and 08 sit exactly at it — do not add a label
to those without removing one.

## Iteration record

- **Card 01** took three generations. Only the **phone test** failed the first two: labels rendered at ~6–9 CSS
  px against the 11px floor, and lane labels fell outside their panel border. Fixed by sizing type
  *relatively* ("one third the height of the title's letters") rather than with adjectives, and by confining
  icons to the upper two thirds of each lane. Two content points were also cut to fit the budget — parsing
  merged into `layout-aware chunking`, and the manifest's three fields moved into the prose.
- **Cards 02–04, 06–09** were accepted on the first generation: every label correct, no hex leak, no invented
  text, and all legible at 360px.
- **Card 05** was regenerated once: the coin icons came back sketchy and hand-drawn while every other card is
  crisp flat vector, and the caption was too small. Fixed with an explicit `CRITICAL ICON STYLE` clause and a
  crisp-linework card as the `--ref`.
- **Hero** was regenerated once for the dead-bottom-band failure — the scene sat in the upper two thirds with
  roughly a quarter of the frame empty beneath it.

Two earlier dark-ground candidates for cards 02 and 05 were **rejected** when the owner chose the light
register; their prompt files were deleted per the skill's rule rather than left to rot.
