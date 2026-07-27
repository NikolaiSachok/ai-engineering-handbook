# Card set — `production-failures`

Ten cards for [Why AI systems fail in production](../../../docs/part-3-production/production-failures.md),
the opener of Part III. Light ground, `4:3` cards + one `16:9` hero, generated with Gemini Pro through the
`create-infographic` skill.

**Status: superseded and deleted, 2026-07-27 — this archive is all that survives of nine of them.** Eight of
the nine cards are now **composed** markup (`src/components/InfoCard/`) on all three locales' pages, reusing
these labels; the **hero was removed** (no heroes until a hero guide exists — STYLE.md §2); and once the
pilot comparison page was retired, the nine superseded `.webp` files were deleted from the repo.
**`05-cost.webp` is the one image still shipping** — the documented escape hatch (STYLE.md §7), embedded in
EN, RU and SK.

So this directory is now the **only** record of those nine images. It stays for two reasons: it is how each
card's node/edge structure and exact label strings were recovered for the port, and it is what would be
needed to reproduce `05-cost` or, one day, the hero. **Do not delete it** — the rasters were disposable
because the recipes are not.

**Five strings have since diverged from these rasters**, under the owner rulings of 2026-07-27 and the
label corrections that closed the migration (`CSS-CARDS-PLAN.md`, final sections) — so the table below is
the record of what the *images* said, not of what the pages now say:

| | Raster | Composed EN |
|---|---|---|
| 02 label | `top-k, always` | `top-K, always` (the handbook's token everywhere else; RU/SK shipped `top-K` first) |
| 03 title | `One eval set is not enough` | `Two eval sets, not one` |
| 03 label | `day-one test set` | `week-one set` (the prose said "week one"; "test" says nothing its peers do not) |
| 06 title | `Re-index before you retrain` | `Retrain last` |
| 06 caption | "Three drifts, one ladder…" | "Drift usually lives in the corpus or the query, not in the weights." — the card only ever drew one drift |

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

**The `ref` paths in the JSON are dead, and always were**: they point into a session scratchpad, and the
anchor images themselves were deleted with the rest of the rasters. Reproduction is therefore two steps —
regenerate `01-corpus` from `prompt-01-corpus.txt` first, ship it, then point the item's `--ref` at it. Only
`05-cost.webp` is still in the repo and can serve as its own anchor. This is the honest cost of deleting
rasters: the *prompts* are lossless, the *style anchoring* is not, so a regenerated card is a close
relative of the original rather than the same image. Anything regenerated goes through the blind-naming and
label-stripped gates again, exactly as a new card would.

## The cards

The `File` column names what each item *produced*; only `05-cost.webp` is still in
`static/img/infographics/production-failures/` — the other nine were deleted on 2026-07-27.

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
