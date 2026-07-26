# Infographic canon — this handbook's card language

**The method lives in the `create-infographic` skill** (`Career/skills/create-infographic/`, symlinked into
`~/.claude/skills/`): the go/no-go test, the labelled-node discipline, the label budget, the prompt structure,
the model failure modes, and the verification gate. Read it first. It was derived by dissecting the
ByteByteGo poster this set's register is based on.

**This file owns only what is specific to this repo** — palette, dimensions, naming, embedding, the archive,
and the decisions taken for the first set. Where the two disagree, the skill wins on *method* and this file
wins on *palette, dimensions, naming and embedding*. Nothing here restates the method; if you find yourself
duplicating a rule from the skill, delete it here instead.

---

## 1 · Palette

**Two card substrates now exist, and the palette below is the generated one.** A *generated* card is a
baked raster and is light-ground in both themes (§4 frames it). A *composed* card
(`src/components/InfoCard/`) carries the same palette **as roles, not as literal hexes**: the values
live in CSS custom properties on `.plate` and are overridden under `html[data-theme='dark']`, so a
composed card is a dark card on the dark theme. Composed cards add one property the generated set
cannot have — `rank`, an ordering ramp that tints the **icon as well as its label**. Canon for the
composed substrate: `CSS-CARDS-PLAN.md` §"Built 2026-07-26"; icon provenance:
`src/components/InfoCard/icons/NOTICE.md`.

Generated cards are **light-ground**, chosen deliberately: it is the register of the reference poster, it gives the
best label contrast, and the illustration reads as an explainer rather than a neon dashboard. The site's own
brand assets (`static/img/logo.svg`, `static/img/og-card.jpg`) are dark — the cards do not have to match them,
because `src/components/Infographic` frames them for both themes (§4).

Write colours into prompts as **RGB triplets, never hex** — if `#` never enters the prompt it cannot leak onto
the card as literal text (a real, observed failure).

| Role | Value | Applies to |
|---|---|---|
| Card ground | `234 238 246` | the whole card, plain — no tint bands |
| Lane panel | `255 255 255` | the demo and production lanes, 2px outline, radius 14 |
| Primary ink | `26 34 48` | title and every node label |
| Failure hue | `239 68 68` | demo-lane outline, its `DEMO` pill, its arrows, fault text — nothing else |
| Correct hue | `20 184 166` | production-lane outline, its `PRODUCTION` pill, its arrows, accepted-result ticks |
| Icon fill | `59 130 246` | **every** icon, uniformly — icon colour carries no meaning |
| Coin / value fill | `240 180 41` | the one exception, on the cost card only — and, on composed cards, on the `coins` icon always: it is what stops a stack of coins reading as a second database |
| Muted / caption | `110 122 138` | the single caption line |

## 2 · Set grammar (decisions taken for `production-failures`)

- **Two stacked lanes**, demo above production, with a small rounded **pill badge** overlapping each lane's
  left edge reading `DEMO` / `PRODUCTION`. This is the set's spine — eight of the ten cards use it. A card
  whose content isn't a demo-vs-production contrast (the cost comparison, the four-quadrant card, the hero)
  may drop the lanes, but nothing else changes.
- **No index badges.** The skill offers a numbered circle; this set omits it, because the page's numbered
  headings already carry the ordinal and a badge-less card stays reusable on a page that isn't numbered.
- **Icons confined to the upper two thirds of a lane**, so labels sit *inside* the panel border. Without this
  the model pushes labels below the border.
- **Monospace labels, bold geometric sans titles**, sentence case, one line.

## 3 · Dimensions and shipping

| | Ratio | Generate | Ship |
|---|---|---|---|
| Card | `4:3` | `--res 2K` PNG | WebP, **1400px**, `-q 82` |
| Hero | `16:9` | `--res 2K` PNG | WebP, **1600px**, `-q 82` |

```bash
cwebp -q 82 -resize 1400 0 raw/02-retrieval.png -o static/img/infographics/production-failures/02-retrieval.webp
```

Budget ≤ 200 KB per card; the first set runs **42–54 KB each, 500 KB for ten**. Raw PNGs never enter git —
they live in the session scratchpad and are reproducible from the archived batch (§5).

**Naming:** `static/img/infographics/<page-slug>/NN-<slug>.webp`, `NN` = reading order on the page, plus
`hero.webp`. The directory always matches the page slug, so a card is traceable to its page.

## 4 · Embedding

Use the globally-registered component — no import needed in any `.md`, in any locale:

```mdx
<Infographic
  src="/img/infographics/production-failures/02-retrieval.webp"
  alt="Ako vyzerá vyhľadávanie, ktoré smie odmietnuť odpoveď"
  caption="Prah relevancie sa uplatňuje po reranku — nie na fúzované skóre."
/>
```

`src` is identical in every locale; **`alt` and `caption` are translated** (in-image labels are English-only —
the skill explains why, and requires the prose to restate every label). `alt` must describe what the card
actually shows: if a card is regenerated with a different composition, its `alt` is now wrong.

`src/components/Infographic/` handles the responsive frame, lazy loading, the caption, and — because the cards
are light-ground — a border plus a slight brightness reduction on the dark theme so a card reads as a
deliberate plate rather than a white flash.

**Composed cards embed as markup, not as `src`.** `InfoCard` / `Lane` / `Node` / `Flow` / `Branch` are
registered globally in `src/theme/MDXComponents.tsx`, so any `.md` in any locale can use them with no
import — and because every label is HTML text, a translator edits the Markdown rather than asking for a
regenerated image. The connector vocabulary is `kind="dashed"` (normal flow), `"solid"` (tight
adjacency) and `"fail"` (the consequence of the fault, and nothing else).

## 5 · Archive

```text
editorial/infographics/
  STYLE.md                              ← this file (canon)
  prompts/<page-slug>/README.md         ← the set: cards, string counts, iteration record, status
  prompts/<page-slug>/batch-*.json      ← the batch actually executed, verbatim
```

**This project archives the executed batch JSON rather than a retyped per-card markdown file.** The skill's
default is one `.md` per card; the JSON is preferred here because it is exactly what the generator received —
prompt, `model`, `ratio`, `res`, `ref`, output path — with no transcription step that can drift from the image
it claims to reproduce. The `README.md` carries the per-card metadata, status and iteration history that the
skill's format would have held.

## 6 · Reviewing a set

```bash
python3 scripts/infographic-review.py <page-slug> --open     # or any directory of candidates
```

Renders every card at article width and at 360px, on both the light and the dark page ground, and flags
anything over 200 KB. The 360px column is the phone test, which is the check that actually fails — mechanise
it, don't eyeball it.

The page is written to the **system temp dir, never into the repo**. It embeds absolute `file://` paths, and
`scripts/leak-scan.sh` greps the whole working tree rather than the git index — so a review page in the repo
root fails the leak gate even while gitignored. (It did, on the first commit attempt. The gate was right.)

## 7 · Sets in this repo

| Set | Page | Cards | Status |
|---|---|---|---|
| `production-failures` | [Why AI systems fail in production](../../docs/part-3-production/production-failures.md) | 9 + hero | pending owner approval |

---

# The visual system, codified

Everything below is **canon for this repo**: enumerable rules with the values that actually ship, so
the `create-infographic` skill has a reference to point at instead of re-deriving them per set. The
skill still owns the *method*; this owns the *values*. Provenance and licensing for the icon files
are **not** repeated here — they live in `src/components/InfoCard/icons/NOTICE.md`.

Values are read from `src/components/InfoCard/styles.module.css` and `icons/index.ts`. **If the code
and this file disagree, the code is right and this file is a bug** — a canon that drifts is worse
than none.

## 8 · Badge lexicon

A badge is a small overlay glyph composed onto a base object. It is what keeps the lexicon
economical: `database` + `refresh` is *re-index*, `chip` + `refresh` is *retraining*, and neither
needs its own asset.

**The constraint that makes it work: a badge modifies the object's state or action, it never renames
the object.** A chip with a `refresh` is still a chip. If the badge would change *what the thing is*,
the lexicon needs a new base object, not an overlay.

| Badge | Means | Use it when | Colour role | Position |
|---|---|---|---|---|
| `tick` | accepted, correct outcome | an outcome the system is *supposed* to produce — including a refusal | correct hue | bottom-right |
| `cross` | rejected, does not happen | a step that is skipped, dropped or refused | failure hue | bottom-right |
| `bang` | fault, warning | the thing that goes wrong; at most twice per card | failure hue | bottom-right |
| `crack` | broken, degraded | a component that has failed rather than one that misbehaves | failure hue | bottom-right |
| `padlock` | scoped, restricted | access control, secrets, redaction | neutral | bottom-right |
| `pin` | fixed, pinned | a version, a snapshot, a chosen anchor | neutral | bottom-right |
| `tag` | labelled, versioned | metadata, an ingestion tag, a release | neutral | bottom-right |
| `refresh` | repeated, re-run | re-indexing, retraining, retrying, any repeat of the base action | neutral | bottom-right |

Colour roles resolve to `--ic-ok`, `--ic-fail` and `--ic-neutral` (§9). The glyph inside is
`--ic-badge-ink` (`#ffffff` in both themes).

**`BADGE_TOP_RIGHT` — the declared exception.** Badges sit bottom-right by default. Icons whose own
drawing occupies that corner move theirs to the top-right, or the overlay covers the part of the icon
that carries the meaning — `driftCurves` (the shift arrow), `sortedList` (the descending arrow),
`traceSpans` (the last span and the axis), `gate` (the base plate), `branchSplit` (the return arm),
`speechBubble` and `speechBubbleEmpty` (the tail). The list lives in `icons/index.ts`; adding an icon
whose bottom-right is busy means adding it there too.

## 9 · Colour semantics, as roles

Generated cards bake the literal values from §1. Composed cards carry the **same roles** as custom
properties on `.plate`, with a dark-theme override — which is why a composed card is a dark card on
the dark theme and a generated one stays a light plate.

| Role | Property | Light | Dark |
|---|---|---|---|
| Card ground | `--ic-ground` | `#eaeef6` | `#15181e` |
| Lane panel | `--ic-panel` | `#ffffff` | `#1f2530` |
| Card hairline | `--ic-hairline` | `#cfd7e6` | `#2c333f` |
| Primary ink | `--ic-ink` | `#1a2230` | `#e8ecf3` |
| Muted | `--ic-muted` | `#6e7a8a` | `#94a3b8` |
| Failure hue | `--ic-fail` | `#ef4444` | `#f87171` |
| Correct hue | `--ic-ok` | `#14b8a6` | `#2dd4bf` |
| Neutral badge | `--ic-neutral` | `#64748b` | `#94a3b8` |
| Icon fill (accent) | `--ic-fill` | `#3b82f6` | `#60a5fa` |
| Icon tint (body) | `--ic-tint` | `#bfdbfe` | `#2f4a70` |
| Value / cost | `--ic-coin` · `--ic-coin-tint` | `#f0b429` · `#fde68a` | `#f5c451` · `#5c4517` |

Three rules:

1. **Icon fill is not semantic.** Every icon is azure by default and that carries no meaning. Meaning
   lives in the **panel tint** (which lane), the **connector colour** (§11) and the **text colour**
   (§10). Do not recolour an icon to say something; recolour the panel, the arrow or the label.
2. **One codified exception: `coins` is always amber.** Not decoration — three discs seen edge-on is
   literally the `database` convention, and colour is what separates the two at a glance. Any future
   icon that collides with an existing convention may take a colour exception only by being recorded
   here.
3. **The failure hue appears once or twice per card and never on a neutral label.** A lane outline,
   its pill, its connectors and the fault text — nothing else.

## 10 · The `rank` ordering ramp

`rank` is the ordering channel made explicit. It tints **the icon's fills and its label together**,
which is the encoding a raster set cannot do and the strongest single argument for composed cards.
**The icon's outline is never part of the ramp** — it stays `--ic-ink` at every rank (rule 2 below).

| Rank | Light: label · `--ic-fill` · `--ic-tint` | Dark: label · `--ic-fill` · `--ic-tint` |
|---|---|---|
| `1` | `#0f766e` · `#0d9488` · `#99f6e4` | `#5eead4` · `#2dd4bf` · `#134e4a` |
| `2` | `#0e7490` · `#0891b2` · `#a5f3fc` | `#67e8f9` · `#22d3ee` · `#164e63` |
| `3` | `#3c6076` · `#61829d` · `#cddbe6` | `#a8c0d4` · `#7e9cb6` · `#2a3947` |
| `4` | `#4a6980` · `#8397a9` · `#dde4ec` | `#8fa2b4` · `#68809a` · `#26313d` |
| `last` | `#55707f` · `#8fa8b6` · `#d5e2e8` | `#8b9ea8` · `#4c5c65` · `#232c31` |

Four rules, each paid for by a blind reader:

1. **Monotone desaturating, never a hue excursion.** An earlier ramp ran teal → cyan → **amber** →
   grey and read as *"the third rung is the important one"*. A warm step among cool ones reads as
   emphasis, not as position.
2. **The last rung keeps a confident outline.** No opacity fade, and the ramp colour is applied to
   `.nodeLabel` and the two fill properties — never to the node's `color`, which is what the icon's
   stroke inherits. A desaturated outline *plus* desaturated fills is the rendering convention for a
   disabled control: a blind reader called the last chip "switched off" rather than "last", and on a
   drift ladder that says "never retrain" instead of "retrain last".
3. **De-emphasis is hue, not weight.** If a node must look secondary, desaturate it; do not dim it.
4. **`rank` only where the content genuinely is an ordering.** Never on peers: a gradient across four
   unrelated failure modes asserts a ranking that does not exist.

## 11 · Connector vocabulary

| Mark | `kind` | Means |
|---|---|---|
| Dashed, correct or failure hue | `dashed` | the normal pipeline — flows to, across distance |
| Solid, primary ink | `solid` | tight adjacency — a step in a stack |
| Dashed, failure hue | `fail` | **the consequence of the fault, and nothing else** |
| Routed fork with a junction dot | `<Branch>` | 1→N — one input, N legitimate fates |

- Every connector is one SVG line with a real `marker-end`. Heads are never faked from CSS borders.
- **A 1→N split is a fork, not N arrows from a point.** The fork's arms carry no arrowheads: it draws
  topology, not flow, and staying headless keeps it distinct from the dashed pipeline.
- **The fork is symmetric about the incoming connector's axis** — with two outcomes, one above and
  one below. Hanging both below the axis makes the first outcome collinear with the incoming arrow,
  and it then reads as the main path with the other as a side note.
- **Alignment rule: a connector sits on the icon centre line, derived from the icon box, never from
  the node.** `margin-top: calc(var(--fork-offset, 0px) + var(--ic-box) / 2 - 5px)`. A node's height
  changes whenever a label wraps; the icon box does not.

## 12 · The icon register

Thirty-seven assets: twenty-nine base objects and eight badges. **The convention column is the
load-bearing one** — it is what stops the next person redrawing `database` as a plain cylinder.
Blind-naming rounds are recorded because a pass is evidence, not an opinion. Sourcing and licence:
`icons/NOTICE.md`.

| Icon | Depicts | Convention drawn | Source | Blind verdict |
|---|---|---|---|---|
| `document` | a record | folded-corner page + text lines | Tabler | R1 pass |
| `documentStack` | many records | offset copies of the page | Tabler | R1 pass |
| `spreadsheet` | tabular data | page with a **cell grid** | Tabler | R1 fail as a bare grid, R2 pass |
| `browserPage` | a web page | window with a **chrome bar** | Tabler | R1 pass |
| `database` | a store | **stacked discs** — the separations are the meaning | Tabler | R1 pass |
| `clipboard` | a checklist | board with a clip | Tabler | R1 pass |
| `calendar` | a schedule | grid page with two hangers | Tabler | R1 pass |
| `codeFile` | code | page with angle brackets | Tabler | R1 pass |
| `dashboard` | monitoring | monitor + bar chart | Tabler | R1 pass |
| `sliders` | tuning | rails with knobs | Tabler | R1 pass |
| `magnifier` | search | lens + handle | Tabler | R1 pass |
| `scales` | a fair comparison | balance beam + two pans | Tabler | R1 pass |
| `speechBubble` | an answer | rounded bubble, tail, **text lines inside** | Tabler | R1 pass |
| `speechBubbleEmpty` | an empty answer | the same bubble with **nothing inside** | hand | R4 pass |
| `speechBubbleGroup` | a conversation | two overlapping bubbles | Tabler | R1 pass |
| `globe` | reach, language | sphere + meridians | Tabler | R1 pass |
| `plug` | an integration | plug body + prongs | Tabler | R1 pass |
| `chip` | the model | square die + pins | Tabler | R1 pass |
| `cloud` | deployment | lobed cloud outline | Tabler | R1 pass |
| `coins` | cost | **two overlapping coins face-on + currency mark**, amber | hand | R1/R2 fail, R4 pass |
| `lockOpen` | unscoped access | padlock, shackle open | Tabler | R1 pass |
| `driftCurves` | distribution shift | two bell curves on one baseline, offset, overlap shaded | hand | R1 pass |
| `gauge` | a threshold | semicircular dial, hub, needle, **radial notch across the arc** | hand | R1 pass |
| `funnel` | filtering | the filter funnel | hand | R1 pass |
| `gate` | a quality gate | boom barrier: **base plate, post, striped arm on a hinge** | hand | R1 pass, redrawn + R4 pass |
| `branchSplit` | canary / rollback | flow splits; one path returns with an up arrowhead | hand | R1 pass |
| `chainSteps` | an unguarded pipeline | linked rounded squares | hand | R1 pass |
| `sortedList` | a ranked list | rows of decreasing length + descending arrow | hand | R1 pass |
| `traceSpans` | a trace | **staggered spans over a ticked time axis** — the waterfall | hand | R1/R2 fail as `timeline`, R3 pass |

### Near-miss pairs — record what separates them before adding a neighbour

| Pair | What separates them |
|---|---|
| `coins` / `database` | **viewpoint plus colour**: coins are face-on and amber, the database is edge-on discs in azure. Three discs edge-on *is* the database convention — that collision is structural, not cosmetic |
| `speechBubble` / `speechBubbleEmpty` | interior content only. That is the intended relationship — one object in two states — so they must never appear as unlabelled peers |
| `spreadsheet` / `browserPage` | the page silhouette versus the window chrome bar; a bare rectangle with one divider reads as either |
| `chainSteps` / `traceSpans` | the stagger and the time axis. Equal blocks in a row read as a chain; offset blocks over an axis read as a trace |

### Residuals, recorded rather than hidden

`traceSpans`, `chainSteps`, `gate` and `branchSplit` all blur at the 34 px a phone renders. None is
used where the distinction is load-bearing without its label. Treat this as a budget: **do not add a
sixth detailed icon** to a card that already leans on one of these.

## 13 · Sizing and geometry — hard numbers

A set stays coherent because everything sits on one grid. These are *the* values, not suggestions.

| | Value |
|---|---|
| Icon viewBox | `0 0 48 48`, no `width`/`height` attributes (so svgo cannot drop the viewBox) |
| Stroke | effective width **3** in that grid, `stroke="currentColor"`, round cap and join |
| Vendored normalisation | upstream 24×24 paths kept verbatim inside `<g transform="scale(2)" stroke-width="1.5">` |
| Fills | `var(--ic-fill, #3b82f6)` and `var(--ic-tint, #93c5fd)` — **always with the literal fallback**, because non-browser rasterisers cannot resolve `var()` |
| Icon box `--ic-box` | `3.4rem` desktop, `2.9rem` below 480px |
| Badge | `1.5rem` — **44% of the icon box** |
| Node pitch | `flex: 0 1 5.9rem`, `max-width` the same (`5.4rem` below 480px). A pitch, not a minimum: uniform node widths are also what stop two labels sharing a text line |
| Connector | `flex: 1 1 1.25rem`, `width: 1.25rem`, `min-width: 1.1rem`, `max-width: 3.5rem`. The definite `width` is required — an `<svg>` with no viewBox contributes **300px** to flex line-breaking otherwise |
| Connector offset | `calc(var(--fork-offset, 0px) + var(--ic-box) / 2 - 5px)` |
| Branch row pitch | `--branch-row: 6.2rem`, `--branch-gap: 0.55rem` — fixed, because every number in the fork derives from it |
| Card width | `560px` above 997px — the same cap as the generated cards, so both substrates sit at identical proportions |

**Paint order is a geometry rule, not a style one: all fills are painted in a `stroke="none"` group
before any stroke.** It structurally prevents the class of bug that turned a hand-drawn `database`
into a plain drum — a later path's fill covering an earlier path's separation lines. Ordering by
care fails; ordering by structure cannot.

## 14 · Where the artefacts live, and the check that keeps them honest

**The icon SVGs live in `src/components/InfoCard/icons/`, not under `editorial/`, and this is
technical rather than preference.** Theme adaptation and the `rank` ramp require the SVG to be
**inline in the DOM** so it inherits `currentColor`; an `<img>` pointing at an SVG file cannot be
recoloured that way. Inline means importable modules under `src/`. Keeping a copy in `editorial/` and
copying it in at build time would manufacture exactly the second source this canon exists to prevent,
plus a sync step that rots silently.

The general rule, so it is not relitigated per artefact: **artefacts live where they are compiled and
can fail a build; the canon holds the rules and points at them.** Provenance and licence sit with the
assets (`icons/NOTICE.md`); the rules, the conventions and the blind-naming verdicts sit here.

That split can drift, so it is asserted rather than trusted:

```bash
bash scripts/icon-register-check.sh      # or: npm run icon-register-check
```

It diffs the names in `src/components/InfoCard/icons/*.svg` against the rows of §12 **in both
directions** — an asset with no row fails, a row with no asset fails — and runs in CI beside the leak
scan. It is a name-set diff, not a parser, on purpose: a check that is cheap and dumb keeps running.

## 15 · Adding an icon

1. **Research the convention first.** How do established sets and common diagrams draw this term?
   Write that line down — it becomes the icon's row in §12 and it is what keeps the set extensible.
2. **Vendor it if a set ships it; hand-author only the domain metaphors none does.** Vendoring is
   professional geometry at zero authoring risk.
3. **Normalise to §13** — grid, stroke, fills, paint order — so a vendored icon and a hand-authored
   one are indistinguishable in use.
4. **Pass blind naming with a fresh reader.** Adding an icon *changes the lexicon*, so it triggers a
   round for **the new icon and its nearest neighbours** (§12's near-miss table names them) — not a
   full re-run. Named as something else is a fail, however good the drawing looks.
5. **Record the row in §12**, including the round it passed on and any residual. A pass you cannot
   cite is an opinion.
