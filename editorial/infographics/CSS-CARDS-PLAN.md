# Composed cards — migrating from generated rasters to CSS + an icon set

**Status: design agreed, not built.** The ten `production-failures` cards ship as whole generated images; this
document is the plan to replace that with cards composed in the browser from a fixed icon set. Written before
a second card set exists, deliberately: migrating two sets costs twice as much as migrating one.

## Why

Icon consistency is the trigger, and the smaller half of the prize. The demonstrated defect: `the model`
appears on card 06 as a chip with thick pins and internal circuit traces, and on card 07 as a chip with fine
comb pins and a plain core. Nothing in a per-card generation pipeline prevents that — `--ref` anchors *style*,
not *identity*, because the model redraws a reference rather than placing it.

What composition actually buys, in order of value:

1. **Labels become HTML text, so they localise.** This deletes the constraint that currently shapes the whole
   system (English-only in-image text). RU and SK readers get their own labels; a typo costs an edit, not a
   generation; screen readers read the diagram.
2. **Icon identity is guaranteed** — one asset per concept, referenced, never redrawn.
3. **Encoding becomes cheap.** Colour-as-ordering, size-as-cost, emphasis-as-priority become a class name.
   Today, changing one node's colour means regenerating a card and re-verifying nine labels.
4. **Reviewable** — a card is a diff, not a binary blob.
5. **Card eleven costs markup**, not a generation, a verification pass and a WebP conversion.

## Purpose before pixels (the rule this system exists to serve)

A card is not an illustration of a paragraph; it is an argument compressed into a spatial structure. So before
any markup:

1. **State the one thought** the card must deliver, in a sentence.
2. **Classify the structure** — a *contrast* (demo vs production), a *sequence* (pipeline), an *ordering/scale*
   (cheapest → dearest, first resort → last), a set of *peers* (four unrelated failures), or a *branch*.
3. **Allocate the channels to that structure** — position, spacing, size, icon form, colour, weight, label —
   and say which channels are deliberately left neutral, and why.

The failure to avoid is the one the first set committed: a channel spent on nothing. Icons were uniformly azure
across all ten cards, which is right where nodes are peers and the lane carries the contrast, and wrong on the
two cards whose whole point is an **ordering** — the drift ladder (first resort → last resort) and the gate
chain (cheapest → dearest). There, colour and size should carry the gradient so the reader sees the argument
before reading a single label.

## Architecture

```text
src/components/Infographic/
  Card.tsx        <InfoCard title=… caption=…>            the frame: title, optional caption, ratio box
  Lane.tsx        <Lane kind="demo|production" label=…>   the pill badge + the outlined panel
  Node.tsx        <Node icon="database" label=…           an icon + its label; the labelled-node primitive
                        badge="refresh" rank="last">      overlay badge; rank drives the ordering encoding
  Flow.tsx        <Flow kind="dashed|solid|fail">         a connector between nodes
  Brace.tsx       <Brace>                                 1→N branch or N→1 merge
  icons.ts        the lexicon: concept -> asset + alt fragment
```

Authoring stays in Markdown, so a translator edits only text:

```mdx
<InfoCard title="Re-index before you retrain" caption="Weights are the last rung, not the first.">
  <Lane kind="demo" label="DEMO">
    <Node icon="drift" label="drift detected" />
    <Flow kind="fail" />
    <Node icon="chip" label="retrain the model" />
  </Lane>
  <Lane kind="production" label="PRODUCTION">
    <Node icon="database" badge="refresh" label="re-index"     rank="1" />
    <Node icon="sliders"                  label="retrieval mix" rank="2" />
    <Node icon="promptFile"               label="prompt"        rank="3" />
    <Node icon="chip"                     label="weights last"  rank="last" />
  </Lane>
</InfoCard>
```

`rank` is the ordering channel made explicit: the component maps it to the colour ramp and de-emphasis, so the
gradient is a property of the data rather than a decision re-made per card.

## The icon lexicon — base objects × badge overlays

Naively the ten cards need ~36 distinct icons, because concepts recur with modifiers (a database; a database
being refreshed; a database tagged as a snapshot). Composition removes that multiplication: **a base object
plus a small overlay badge**, positioned by CSS.

**Base objects (16)** — `document`, `documentStack`, `spreadsheet`, `browserPage`, `database`, `clipboard`,
`calendar`, `dashboard`, `speechBubble`, `speechBubbleGroup`, `magnifier`, `sortedList`, `gauge`, `gate`,
`chip`, `sliders`, plus `coins`, `globe`, `plug`, `timeline`, `scales`, `cloud`, `promptFile`, `branchSplit`
as the second row.

**Badge overlays (8)** — `tick`, `cross`, `bang`, `padlock`, `pin`, `tag`, `refresh`, `crack`. Rendered at ~40%
of the base icon, bottom-right or top-right, in the semantic hue (`tick` correct, `cross`/`bang`/`crack`
failure, the rest neutral).

That is 24 + 8 = 32 assets covering every combination the first set needed and most of what a second set will.

**Generation:** one sheet per group, in a **single image** — icons drawn together in one pass are inherently
consistent in weight, perspective and detail, which is precisely what per-card generation cannot achieve. Then
slice into individual files. A 4×6 sheet at 2K gives ~340px per cell, ample for a ~64px render.

## Resolved 2026-07-26: icons are SVG, and no image generation is involved

Measured, not assumed. Two icons hand-authored as SVG and rendered in Chromium at 2× beside the
shipped WebP equivalents:

| | Generated WebP | Hand-authored SVG |
|---|---|---|
| One icon (`database`) | **7052 B** | **547 B** raw · **257 B** gzipped |
| 24-icon set | ~156 KB | ~13 KB raw · ~6 KB gzipped |
| Theme adaptation | none — card is a light plate | **works**: one file, recoloured by CSS, verified on near-black |
| Per-node recolouring | impossible | **works**: the same file rendered in the failure hue |
| `rank` encoding | label colour only | label **and** icon — a stronger channel |
| Badge overlay | second raster + `mix-blend-mode` hack | native `<svg>`, positioned exactly, recolourable |
| Retina | fixed raster | crisp at any size |
| Text mangling / slicing bugs | two hit us (labels, badge pitch) | structurally impossible |
| Domain metaphors | anything generable | anything drawable |

So **SVG wins decisively**, the whole generation-plus-slicing pipeline disappears for icons, and the
light-plate compromise disappears with it. Generation stays for heroes and scenes, which is what it is
actually good at.

**But drawing quality moves onto us, and the probe proves the risk.** `driftCurves` came out well —
two offset curves with the overlap shaded, legible at 34 px, ~450 bytes, and no icon set ships it. The
`database` did not: three stacked discs were specified and it rendered as a single cylinder with a lid,
because each later path's fill painted over the separations above it. Recognisable, but not what was
asked for. Deterministic *files* are not the same thing as competent *geometry*.

**Therefore: a hybrid, and this is the decision.**

- **Generic objects** — document, documentStack, spreadsheet, browserPage, database, clipboard,
  calendar, dashboard, speechBubble(s), magnifier, sliders, globe, plug, keyLock, coins, cloud,
  codeFile, timeline: take from an established open set (Phosphor duotone, Tabler or Lucide — MIT/ISC,
  so vendor the specific files into `src/components/InfoCard/icons/` with attribution rather than
  adding a dependency). Professional geometry, zero authoring risk.
- **Domain metaphors no set ships** — `driftCurves`, a gauge with a marked threshold notch, a gate
  beside a funnel, `branchSplit` with a return arrow, `chainSteps`: hand-author these. They are few,
  they are the ones that carry the argument, and the probe shows they are within reach.
- Normalise everything to one 48×48 grid, one stroke width, `currentColor` for the outline and
  `--ic-fill` / `--ic-tint` custom properties for the two fills, so a vendored icon and a
  hand-authored one are indistinguishable in use.

One caveat worth writing down: ImageMagick cannot resolve `var()`, so any non-browser rasteriser
(og-image generation, PDF export) will not render these. Give every custom property a literal
fallback — `fill="var(--ic-fill, #3b82f6)"` — and treat the browser as the only supported renderer.

## Superseded (twice — kept as the record of why the card is no longer a light plate)

A CSS card adapts to the dark theme for free — ground, panels, text and connectors are all CSS. **The icons do
not.** A raster icon has a baked fill and outline: a dark outline vanishes on a dark card, a light one vanishes
on a light card. Three ways out, with the trade stated honestly:

| Option | Icons | Theme | Look |
|---|---|---|---|
| **A — chosen for v1** | generated raster on white | card renders as a light plate in **both** themes, framed by the component (what the current cards already do) | keeps the approved sticker register exactly |
| B | an open SVG set (Phosphor duotone, Tabler — MIT/ISC) | fully theme-adaptive via `currentColor` | stroke-style; loses the blue-fill sticker character |
| C | hand-authored SVG in our style, fill and outline as separate `currentColor` paths | fully theme-adaptive | best of both, and much the most work — 32 icons drawn by hand |

**A** ships the two things asked for — consistent icons, localised labels — without renegotiating the visual
register, and leaves B/C open. If theme-adaptive icons later outweigh the sticker look, only `icons.ts` and the
assets change; no card markup moves. Note the consequence plainly: on the dark theme a composed card is a light
plate, not a dark card.

## Pilot review — 2026-07-26: not yet good enough, two structural defects

Verdict on the first pilot (cards 06 and 02 on the unlisted pilot page): **the rasters still read
better; do not migrate yet.** The ordering ramp on card 06 works and is a genuine improvement over the
raster's four identical peers. Two things fail, and the second is not cosmetic.

**1 · Connectors are wrong.** Built as a `border-top` dash with an arrowhead faked from `border` on a
`::after`. Symptoms: the head is undersized and reads as detached from the dash, it sits slightly off
the dash's axis, and the length is a fixed `2rem` regardless of the gap it spans, so it looks like a
stub next to the raster's long, confidently aimed arrows.

*Fix:* draw connectors as **inline SVG** with a real `marker-end`, and let them size to their
container (`width: 100%` inside a flex-grow slot) so the arrow spans the actual gap. Vertical centring
should align to the **icon box**, not to the node including its label — the current
`margin-bottom: 1.4rem` hack approximates that and drifts whenever a label wraps to two lines.

**2 · The branch does not express a branch.** On card 02 the meaning is *one input, two legitimate
fates* — `grounded answer` **or** `"no context"`. The raster draws a brace opening into two **stacked**
outcomes. The composed version puts both outcome nodes in the same flex row, so they sit side by side,
their two labels run together and read as a single line, and the brace is a small bracket attached to
nothing. The card has stopped saying what it means, which by §8 of the skill is a failed card no matter
how correct every label is.

*Fix:* a real `<Branch>` component — a column of two (or N) nodes with a brace that **spans their full
height**, and the incoming connector aimed at the brace's vertical midpoint. `Brace` as a standalone
sibling in a row cannot work; the brace has to own its branches as children so it can size to them:

```mdx
<Node icon="gauge" label="score floor" />
<Flow />
<Branch>
  <Node icon="document" badge="tick" label="grounded answer" />
  <Node icon="speechBubble" label="or “no context”" />
</Branch>
```

Also worth fixing while in there: node labels should not be allowed to visually merge with a
neighbour's — give each node a minimum horizontal gutter, and never let two labels share a text line.

**3 · The lexicon is too generic, and the substitution was made silently.** Card 06's concept is
*drift*. The raster draws **two offset distribution curves** — the reader sees "the distribution
moved" before reading the label, which is the icon doing real work. The composed version used
`dashboard` + a `bang` badge, a monitor with bars, which says only "something is wrong with a chart".
The lexicon had no drift icon, so a generic object was substituted and the card lost meaning.

That is a **compromise report failure**, not merely a missing asset: the skill requires any content
concession to go back to the page's author, and this one was made quietly. New rule, worth carrying
into the skill: *where a concept has a recognisable visual metaphor, a generic stand-in is a defect.*
An icon set built only from office objects will quietly flatten every domain idea it meets.

**Lexicon gap — the domain sheet that has to exist.** The first sheet is generic containers and
controls. These concepts, all needed by the existing ten cards, have no honest representation in it:

| Needed | Metaphor |
|---|---|
| `driftCurves` | two offset bell curves, one shifted right, overlap shaded |
| `coins` | a stack of coins (cost) |
| `globe` | a globe with a speech bubble (language coverage) |
| `plug` | a plug pulled from its socket (tool failure) |
| `keyLock` | a key beside an open padlock (unscoped access) |
| `scales` | a balance (an honest scoreboard) |
| `timeline` | three connected spans (a trace) |
| `branchSplit` | a path splitting, with a return arrow (canary / rollback) |
| `cloudBreak` | an upload cloud with a crack (deploy failure) |
| `codeFile` | a file with angle brackets (prompt in code) |
| `funnel` | a funnel alone, without the barrier |
| `chainSteps` | four linked squares (an unguarded pipeline) |

Generate these as a **second sheet** in one pass, in the same style, and slice with the same
gutter-detection slicer. Until they exist, a composed card that needs one of them must not be
authored with a substitute.

**Kept from the pilot:** the 24 generic assets (consistent, verified), the `rank` ordering ramp,
the lane/pill grammar, the light-plate decision, and the width cap. The defects are the connector
primitive, the branch primitive, and the lexicon's coverage.

## What does NOT change

The labelled-node discipline, the label budget (a phone is still 360px wide), the demo/production lane
grammar, the flow-mark vocabulary, and the rule that the prose must still teach the lesson. Composition changes
the substrate, not the method.


---

## Built 2026-07-26 — the rebuild that answers the pilot review

All three named defects are fixed and the pilot page carries the comparison. Code:
`src/components/InfoCard/` (`index.tsx`, `styles.module.css`, `icons/` + `icons/NOTICE.md`).

### 1 · Connectors — fixed, as designed

`Flow` is now an inline `<svg>` with a real `marker-end`. Two details make it work:

- **No `viewBox`**, so user units are CSS pixels and the line can be written `x1="0" x2="100%"`. The
  arrow therefore spans whatever slot flex gives it — the connector *is* the gap.
  `markerUnits="strokeWidth"` keeps the head proportional to the line, so it can never detach.
- **Vertical position is `calc(var(--ic-box) / 2 - 5px)` from the top of a top-aligned row.** The
  offset is derived from the icon box, never from the node, so a two-line label cannot drag the
  arrow off the icons' centre line. Verified: on card 06 `retrain the model` wraps and the arrow
  does not move.
- Later addition, from a label-stripped read: `max-width: 7rem`. Uncapped, a two-node lane stretched
  one arrow to four times the length of the arrows in a four-node lane, and the disparity read as a
  claim about distance.

### 2 · The branch — fixed, but not the way the review specified

`Branch` owns its children, as required. The part that changed: the review said *aim the incoming
connector at the brace's vertical midpoint*. Built that way first, and a blind label-stripped reader
called it **"the worst mechanical error on either card"** — a symmetric brace's midpoint sits a
label's height below the node the arrow leaves, so the arrow appeared to start in mid-air.

The fix inverts it: **the brace moves to the arrow.** It is drawn as *two independently stretched
halves* (`viewBox="0 0 14 50"`, `preserveAspectRatio="none"`, `vector-effect="non-scaling-stroke"`),
split at `calc(var(--ic-box) / 2)` — so the nub lands exactly on the icon centre line, the same line
every other connector sits on. **One alignment rule now governs the whole grammar**, and the special
case in `Lane` disappeared.

Two more things a stripped read forced:

- A **junction dot** at the nub. Without it the brace floats: the arrow looks like it points at the
  first branch rather than at the fork, and the reader called the brace "structurally unanchored".
- `Lane` wraps a `Flow`+`Branch` pair into one flex item. They are authored as siblings, and at phone
  width the lane wrapped between them, leaving the arrow pointing off the end of the row at nothing.

Node gutters: `min-width: 5.5rem` plus horizontal padding, so two labels can never share a text line.

### 3 · The icon lexicon — SVG, hybrid, and a blind gate that actually failed things

37 inline SVGs (29 objects + 8 badges), imported through Docusaurus's built-in svgr. **20,478 B raw,
2,414 B gzipped**, against **110,908 B** for the 24 rasters they replace — 553 B per asset against
4,621 B. The `mix-blend-mode` hack and `static/img/infographics/icons/` are gone.

- **Vendored (20)** from **Tabler Icons (MIT)**, paths kept verbatim, wrapped in
  `<g transform="scale(2)" stroke-width="1.5">` to land on the 48 grid at the house weight.
- **Hand-authored (9)**: `driftCurves`, `gauge`, `funnel`, `gate`, `branchSplit`, `chainSteps`,
  `sortedList`, `traceSpans`, `speechBubbleEmpty`.
- **The fill-layering rule that came out of this** and is now in `icons/NOTICE.md`: every fill is
  painted in a `stroke="none"` group *before* any stroke. That structurally prevents the failure the
  probe hit — a later fill covering an earlier separation line, which turned a database into a drum.
- Every `var()` carries its literal fallback, so a non-browser rasteriser still gets a drawing.

**Deviations from the brief, each with its reason** (all recorded in `icons/NOTICE.md`):

| Asked for | Shipped | Why |
|---|---|---|
| `keyLock` — a key beside an open padlock | `lockOpen` | two objects in a 48 grid are illegible at the 34 px a card renders; the concept was renamed to match the drawing rather than the drawing bent to the name |
| one *gate beside a funnel* | `gate` **and** `funnel`, separately | same legibility reason, and `funnel` was on the lexicon's own gap list anyway |
| `chainSteps` — four linked squares | three | four squares at stroke 3 leave 5 units of interior each and read as noise |
| `timeline` | `traceSpans` | see below — it failed the blind gate twice under the old name |

### The blind-naming gate — it earned its keep

Three rounds, a fresh agent each time, no access to the intended names. What it caught:

- **`timeline` failed twice.** Nested spans on a shared centre read as *"cascading pills… a lamp"*;
  redrawn as dots on a line it read as *"three pins/nodes… tuning knobs"*. The third version —
  staggered spans over a ticked time axis — reads as *"bar chart, descending / waterfall"*, which is
  the observability convention for a trace, so the **concept was renamed `traceSpans` to match what
  the drawing actually says.** Two redraws and a rename: the honest cost of one icon.
- **`spreadsheet` drawn as Tabler `table`** read as *"table / grid layout"* and was confusable with
  `browserPage` — both a rectangle with an internal divider. Re-sourced to `file-spreadsheet`.
- **`coins` read as a possible second database** — both are stacked ellipses. Fixed with colour, not
  geometry: coins now use `var(--ic-coin, #f0b429)`, the value/cost amber STYLE.md already allowed as
  its one palette exception. Named *"coins / money"* on the next round.

Residual, documented rather than hidden: `traceSpans` and `chainSteps` both go mushy at 34 px, and
`speechBubble` vs `speechBubbleEmpty` differ only by an interior mark that is faint at that size.

### What the third stripped read changed (the layout rules that only a blind reader finds)

- **Lanes are left-aligned, not centred.** Centred rows put the demo lane's first node 170 px right
  of the production lane's, and the reader reported "two unrelated diagrams" rather than one lane at
  two maturity levels. A contrast card must share an x origin.
- **Connectors are capped at 5 rem.** Uncapped, arrow length tracked available gap rather than
  meaning, so the two-node demo lane's single arrow outweighed the production lane's four.
- **Branch nodes are left-aligned inside the branch.** Centring an icon in a box as wide as its label
  pushed the icon ~45 px away from the brace, and the brace then appeared to gather nothing.
- **Both branch outcomes carry the same badge mechanism.** A corner tick on one and an interior glyph
  on the other read as "two different kinds of thing"; the card's claim is that they are siblings.
  Both now take the teal tick, which is also the card's thesis — a refusal is a *correct* outcome.

One reported defect was **rejected on grounds of the project's own grammar**: the reader wanted
arrowheads leaving the brace. The skill's flow vocabulary specifies a brace *instead of* N arrows
from a point, so the brace stays and the junction dot carries the anchoring.

### Theme adaptation and the ordering ramp

The whole palette is CSS custom properties on `.plate`, overridden under `html[data-theme='dark']` —
ground, panels, ink, hairline, both icon fills, and the coin exception. The **light-plate decision is
dead**: a composed card is now a dark card on the dark theme.

`rank` drives **two monotone channels**: colour (a desaturating teal → slate ramp) applied to the
icon *and* its label, plus a descending icon opacity. Both were needed. A first attempt ran
teal → cyan → **amber** → grey; a stripped reader called the amber node "a palette outlier… it makes
the third rung look like the important one" — a hue excursion reads as emphasis, not as position.
And `ranklast` is tinted rather than dead grey, because flat grey reads as *disabled*, not *last
resort*.

### Verdict and what is still open

The composed cards now beat the rasters on encoding (the ramp tints the icon), on theme, on weight,
on localisation and on reviewability, and they match on register. **Not yet migrated** — the ten
rasters still ship. Open items for whoever takes the decision:

1. A branch leaves visible whitespace under the nodes preceding it. Inherent to a stacked branch in
   a flex row; the alternative (a slanted connector) needs geometry CSS cannot express.
2. Card 06's shipped caption says *"Three drifts"* and the card draws one. A stripped reader caught
   it in the raster's own wording — a **content** defect the composed port merely inherits, and only
   the page's author can settle it.
3. `gauge` reads as "a number on a scale", not as "a cutoff". The threshold notch is not enough; if
   the score-floor idea must be picture-legible, that icon wants another pass.
4. Three icons are weak at 34 px and are documented as such rather than quietly shipped:
   `traceSpans` and `chainSteps` both blur into "a row of rounded blobs", and `speechBubble` vs
   `speechBubbleEmpty` differ only by an interior mark. None is used on a card where the distinction
   is load-bearing without a label.


---

## Owner review 2026-07-26 — "looks better", four fixes before it can replace the rasters

### 1 · Short lanes stopped short of the right edge

**Fixed by deleting the connector cap, not by centring.** The connectors are `flex: 1 1 2rem` with no
`max-width`, so they absorb every spare pixel: a two-node lane now fills the panel edge to edge
exactly like a four-node lane, **and both lanes still start on the same x** — the property a blind
reader had already told us was worth protecting when it read centred lanes as "two unrelated
diagrams". Nothing was sacrificed; the whitespace moved from the right margin into the middle of the
lane, where a connector spans it instead of it sitting empty.

What that cost, honestly: card 06's demo lane is now two icons at the extremes with a long arrow
between them, and a stripped reader called that panel "under-populated". It is — the demo lane has
two nodes and the production lane has four, which *is* the card's argument (the demo path is short).
The lane was equally under-populated before; the fix only moved where the emptiness sits.

**One real bug the change exposed.** With the cap gone, card 02's branch dropped onto a second row.
Cause: a `<svg>` with no viewBox has an intrinsic width of **300 px**, so the connector's *intrinsic
contribution* was 300 px even though its flex-basis was 2 rem — enough to break the flex line. Fixed
by giving `.flow` a definite `width: 2rem` alongside the basis. Worth remembering: flex line-breaking
uses intrinsic contributions, and an inline SVG lies about its.

### 2 · The brace is gone; the fork is real geometry

The stretched `{` was a glyph scaled to a height it was never drawn for, and it read as "a thin
bracket floating away from the nodes it groups". Replaced with a **routed fork**: the junction dot on
the incoming connector's line, a stem dropping from it, one arm per outcome ending on **that
outcome's own icon centre line**.

The geometry is exact because `Branch` is now a **two-column grid** — arm cell, node cell, one row per
outcome. An arm cell is therefore always exactly as tall as the node beside it, so
`calc(var(--ic-box) / 2)` *inside that cell* is that node's icon centre line whatever its label does.
That is the trick worth keeping: **put the connector in the same grid row as the thing it points at,
and the alignment stops being a guess.** Arms are borders with a corner radius — straight lines and
real rounded corners, never a shape faked from border tricks.

A blind read of that first fork confirmed the arrow *"terminates on the fork — the arrowhead's tip
touches the dot"* and that the drawing was *"deliberate, not decorative"* — and then demolished the
topology: with the junction **on** the first outcome's centre line, the incoming arrow, the junction
and the first outcome were **collinear**, so it read as *"flow continues into outcome A, with outcome
B bracketed underneath"*. The first outcome looked primary, which argues against the card's entire
claim that a refusal is an equally legitimate ending.

Fixed with a **fork lead**: the branch carries `padding-top: var(--fork-lead)`, so the junction sits
just above the first outcome's centre line and **both** legs leave the incoming axis and elbow out to
their node. Nothing is collinear with the arrow any more, and the junction is a real T rather than a
dot sitting on a through-line. The same read also caught both arms stopping in the column gutter, in
front of the icons' own transparent margin — so an outcome "was not actually attached to anything".
Arms now run `right: -0.55rem`, into the icon's margin.

Deliberately **not** done, though the reader asked for it: arrowheads on the fork's legs. The skill's
flow grammar specifies a brace-style fan for 1→N *instead of* N arrows from a point. The fork stays
headless and solid, which also keeps it visually distinct from the dashed pipeline — topology is not
flow.

### 5 · The uniform node pitch (not on the owner's list; the same read forced it)

Nodes had a *minimum* width and were sized by their own label, so each lane centred its first icon
somewhere different — the production row's first icon sat ~30 px left of the demo row's, on both
cards. A blind reader called it out twice, "consistently wrong". Nodes now share **one pitch**
(`flex: 0 1 6.2rem`), so every icon lands on the same grid and the two lanes' first icons align
exactly. Consequences worth knowing:

- Labels wrap earlier. That is fine — two-line wrap is normal per the skill — but it is a real trade.
- A long single token would overflow the fixed pitch and collide with its neighbour, which is the
  very defect the gutter exists to prevent, so `.nodeLabel` carries `overflow-wrap: anywhere`.
- Four nodes plus three connectors now fit one line by ~20 px. A fifth node wraps, which is correct:
  the label budget caps a lane well before that.

### 3 · `speechBubbleEmpty` is now genuinely empty

Both candidates went through blind naming. The **plain bubble** read as *"empty speech bubble… nothing
is in there… reads as empty / no content"*. The **`∅` variant** read as *"blocked / banned message"* —
a circle with a diagonal bar is the universal **prohibition** sign, not the empty set. Kept the plain
bubble and deleted the other.

The lesson generalises: **an absence beats a glyph that means absence.** A symbol for "nothing" is
still something, and readers decode the something first.

### 4 · Two icons redrawn to their conventions

- **`gate`** now draws the boom barrier's three defining features — base plate, vertical post, striped
  arm pivoting from the post's top on a visible hinge. Blind: *"barrier / boom gate (striped
  roadblock arm)"*. Mushy at 34 px, which is recorded rather than hidden.
- **`coins`** left the vendored set. Three stacked discs seen edge-on is *literally the database
  convention*, which is why a blind reader kept offering "database disks" — the drawing was not
  merely similar to `database`, it was the same convention. Redrawn as **two overlapping coins seen
  face-on with a currency mark**, keeping the amber exception. Blind: *"coins / money"*, no mention of
  discs or a database.

### Blind-naming diff, this round

| Intended | Blind read | Verdict |
|---|---|---|
| `gate` | "barrier / boom gate" | pass |
| `coins` | "coins / money (dollar coin)" | pass — the database collision is gone |
| `speechBubbleEmpty` (plain) | "empty speech bubble… nothing is in there" | pass — **kept** |
| `speechBubbleEmpty` (`∅`) | "blocked / banned message" | fail — **deleted** |
| controls: `database`, `magnifier`, `funnel`, `speechBubble` | all named correctly | — |

Residual, recorded: `speechBubble` and `speechBubbleEmpty` share a silhouette and differ only by
interior content, so at 34 px a fast scan reads both as "a comment". That is the *intended*
relationship — one object in two states — and on the card they are adjacent and labelled.
