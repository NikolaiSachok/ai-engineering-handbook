# Composed cards — migrating from generated rasters to CSS + an icon set

**Status: MIGRATED (EN), 2026-07-27; owner rulings applied the same day.** The English `production-failures`
page ships **eight composed cards and one raster** (`05-cost`), and no hero. The nine `.webp` files stay in
git, unreferenced by EN, until the RU/SK pages are migrated too. The record below is chronological: the plan,
four review rounds, the migration, and **the owner's rulings in the final section** — which is where the four
open questions (card 05's substrate, card 09's existence, fork arrowheads, card titles) are closed.

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

> **Superseded in practice, 2026-07-27 — not refuted.** The reasoning still holds: a hero *is* an
> illustration, and generation genuinely wins there. But the page's hero was removed, because a hero has
> **no canon** — no grammar, palette, icon register, sizing rule or verification gate, unlike a card — and
> an unregulated one-off is how a style system drifts. **No heroes until a hero guide exists**
> (STYLE.md §2). When someone writes that guide, this paragraph is where it starts.

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
   the page's author can settle it. **Resolved 2026-07-27 — see the owner-rulings section at the end.**
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

---

## Owner review round 3 — centred scheme, symmetric fork, raster proportions

### 1 · Centred, and the blind read says the risk did not materialise

Reverted the edge-to-edge fill: connectors are capped again (`max-width: 3.5rem`) and `.laneBody` is
`justify-content: center`, so a short lane sits centred with equal spare space either side.

This reintroduced the exact risk an earlier reader had raised — centred lanes read as *"two unrelated
diagrams"* because the two lanes' first icons no longer share an x origin. **Re-tested on that axis,
and the reading did not return.** A fresh label-stripped reader answered plainly: *"Both cards read
as ONE system, two maturity levels."* What carries it is not the left edge at all — it is the
**repeated object**: on card 06 the chip is the demo's only destination and the production ladder's
last rung, and on card 02 the answer bubble is the shared terminal in both lanes. *"Same endpoint,
different route… I read that before I read the headline."*

So the trade is recorded and settled: **a contrast card is held together by a recurring icon, not by
a shared left margin.** That is a more robust coupling than alignment, because it survives the two
lanes having different numbers of nodes.

The same reader did find a **missed opportunity**, and it is worth writing down for whoever decides
the final layout: centring the short lane leaves the *repeated* icon unaligned between lanes — card
06's demo chip sits above production's `prompt` rather than above production's chip, which *"actively
suggests a false pairing"*. Aligning the two chips would make the card's argument land with no words
at all. It cannot be had together with "centre a short lane": with different node counts, centring
and endpoint-alignment are mutually exclusive. The owner has chosen centring; a future option is to
right-align lanes instead, which aligns endpoints rather than origins.

### 2 · The disabled chip, fixed at the right level

Badge grammar now carries the meaning: `retrain the model` is `chip` + `refresh` (a repeat mark on a
chip *is* retraining), and `weights last` is a bare chip drawn at full confidence.

The deeper fix was in the ramp. Dropping the opacity fade was not enough — the reader still called
the last chip *"switched off… the exact rendering convention for a disabled UI control"*, because
`rank` was applied to the node's `color`, which the icon's **stroke** inherits. Desaturated fills plus
a desaturated outline is what "disabled" looks like. **The ramp now reaches the icon through its
fills only; the outline stays `--ic-ink` at every rank.** Codified in STYLE.md §10.

### 3 · Symmetric fork — and yes, it deleted the fork lead

The fork is now symmetric about the incoming connector's axis: with two outcomes one sits above the
line and one below. Two things fell out of one change:

- **The fork lead is gone.** It existed only to stop the first outcome being collinear with the
  incoming arrow. Symmetry removes the collinearity by construction, so the compensating hack
  deleted itself — the second time in this component that fixing the geometry properly removed a
  workaround rather than adding one.
- **The lane's dead region went with it.** The scheme now straddles the axis instead of hanging
  below it, so the lane is no taller than the fork needs.

The mechanism is `Lane` computing a `--fork-offset` from the branch's outcome count and pushing
everything else in the row down by it, while the branch stays at the top. Outcome `i`'s centre line
is `i × pitch + half the icon box` and the axis is the midpoint of the first and last — arithmetic,
not guesswork, and it only works because the branch rows have a **fixed** pitch (`--branch-row`).

Card width dropped to `560px`, the same cap the generated cards use, so both substrates now sit at
identical proportions when the pilot page shows them side by side.

### Residual findings from the same read, not acted on

1. **The empty bubble reads as unfinished when stripped of its label.** *"Indistinguishable from a
   rendering failure."* This is in direct tension with the blind-*naming* result that chose it
   ("empty… nothing is in there") and with the owner's explicit instruction that emptiness is the
   meaning. Both tests are right about different things: named in isolation it reads as empty; seen
   as one of two peers it reads as the unfinished one. The canon records the constraint that falls
   out — `speechBubble` and `speechBubbleEmpty` must never appear as **unlabelled** peers.
2. **Panels are top-weighted with spare space pooled at the bottom.** Mostly an artefact of the
   stripped test — the hidden labels reserve their space and read as emptiness — but not entirely:
   `--branch-row` is a fixed 6.2rem, so a two-line label leaves real slack in the last outcome's row.

---

## Owner review round 4 — scale like an image, un-mark the input, and a real `retrieval` icon

### 1 · The diagram now scales instead of re-flowing (canon: STYLE.md §16)

Every length in the card became a multiple of one unit, `--ic-u`, which is 1% of the card's width
(`container-type: inline-size` on `.card`). The card has exactly one breakpoint left — the 560px
desktop cap it shares with the raster component — and the diagram inside has none.

**The tension was named before building, because it cuts against the label budget**, and all three
candidates were built and measured rather than argued:

| | Shape across 1440 → 360 | Node label on a 390px phone | |
|---|---|---|---|
| Pure `1cqw` | aspect ratio **exactly constant** (1.50 / 1.10) | **8.4px** | fails the 11px floor |
| Lock geometry, floor the type | horizontally constant | 11px but **words break mid-token** (`confiden/t`, `retriev/al`) | fails |
| Floor the unit | constant above the floor, old re-flow below | 11px | **shipped** |

The deciding evidence was a fresh phone-width reader on the pure-lock render. It transcribed every
label correctly at 1:1 — but measured the tiers and called node labels *"below the 11px line,
marginal"* and the 7px lane pills *"shape-recognition, not reading"*. So the full lock fails the
floor, and the hybrid ships: `--ic-u: max(4.695px, 1cqw)`, the floor derived as `11px ÷ 2.343`.

What that costs, recorded rather than buried: **a phone still re-flows.** The crossover is a 458px
card (≈490px viewport). At a 358px card an 11px label and an unwrapped four-node lane are
arithmetically exclusive. STYLE.md §16 records the lever that would move it — the connector reserves
a full-height flex column although it only occupies the icon centre line, which caps the label at the
node pitch; the raster has no such cap, which is exactly why its labels are ~28% larger.

Three things fell out of the conversion that are worth knowing:

- **The badge was silently wrong.** Canon said "44% of the icon box"; the code had a fixed `1.5rem`,
  which was 44% on the desktop card and **52%** of the smaller phone icon. In the unit it is 44%
  everywhere. A ratio expressed as an absolute length is a ratio that will drift.
- **The connector had to stop lying about its size.** Its `<svg>` carried `height="10"` and a line at
  `y="5"`; the drawing now takes `--flow-h` from CSS and the line rides `y="50%"`, so stroke weight,
  dash rhythm and arrowhead scale too instead of surviving as a hairline.
- **A blind reader found a canon/code disagreement nobody had noticed.** It measured the dark-theme
  `weights last` chip outline at **2.2:1** against the panel — "I registered it as an empty slot".
  Cause: `.ranklast` set `color` on the *node*, which the icon's stroke inherits, while §10 rule 2
  says the ramp reaches the icon through its fills only and every other rung obeys that. The rule was
  right and the code was wrong for three review rounds. Fixed to `.ranklast .nodeLabel`.

### 2 · The `cross` on `top-k, always` is gone, and the rule behind it is now canon

The badge read as *"retrieval is broken"*. The card's claim is the opposite and sharper: **the
retrieval mechanism works correctly; always returning top-k is what produces the confident wrong
answer.** The fault is in the policy, not the machinery — and the red lane, the failure-hue connector
and the `bang` on the outcome already carry the failure, at the point where it actually happens.

New canon (§8): **a failure badge marks the thing that is broken, never the thing that is being
misused**, plus the corollary that the *input* node of a failure is usually unmarked. Auditing the
other nodes on both cards under that rule found one more instance: `chainSteps` + `crack` on
`unguarded chain` (flow-marks card) — a chain run without a gate is not a broken chain. Removed. The
neutral badges (`chip`+`refresh` = retraining, `database`+`refresh` = re-index) name an *action* and
survive; `bang` on `confident wrong answer` and the two `tick`s on the branch outcomes all mark
outcomes, which is what they are for.

### 3 · `retrieval` — a new base object, not a badge and not a swap

A magnifier is not a state, so it cannot be a badge (§8's constraint). A bare document stack says
*documents*; the node is about **retrieval as a process**, which the generated raster drew as a stack
*plus a magnifier* deliberately. So the lexicon gained an asset.

Three drafts. The first put a featureless near-square block under a small magnifier and read as "a
blue box"; the second, at proper page proportions, ended in a bare diagonal fill edge that read as a
**torn** page. The third solves the occlusion the way the paint-order rule demands: since an opaque
lens painted after the pages' outlines is forbidden, **the hole is baked into the path** — the front
page's fill arcs around a circle concentric with the lens, and its outline stops short of that arc.
No mask, no clip, no z-order trick. (An `evenodd` knockout was tried first and is wrong: a point
inside the circle but outside the page has an odd crossing count, so it fills — the bug shipped a
blue blob beside the magnifier until it was caught in the render.)

Blind naming (fresh agent, `documentStack` and `magnifier` as the nearest neighbours, plus controls):
**pass** — *"stack of documents with a magnifier — searching files"*, and it fused into one idea
rather than two objects side by side. At 40px the same reader saw *"something plus a magnifier"*: the
stack degrades, the magnifier survives. Recorded as a residual with the general lesson — **a
two-object icon buys meaning at reading size and spends legibility at phone size, because each object
gets half the detail budget.** Take that trade only when the second object *is* the concept.

The usage split is now canon rather than taste (§12): **`documentStack` is a noun** (a corpus, a set
of documents) and **`retrieval` is a verb** (the search over them). The test: a node that could be
labelled "documents" takes the stack; one that could be labelled "find" takes `retrieval`.

---

## Migrated 2026-07-27 — EN ships composed cards

The owner approved the approach; the English page now carries **eight composed cards, one raster and no
hero**. What follows is what the migration actually cost and what it found, because most of it was not
visible from the pilot.

### What ported, and the two that did not

| Card | Substrate | Why |
|---|---|---|
| 01 corpus · 02 retrieval · 03 eval sets · 04 green ≠ correct · 06 drift · 07 releases · 08 gates | **composed** | two-lane contrasts; the grammar already covered them once `Merge` existed |
| 09 four missed | **composed**, via a new `Grid` | peers, not a flow — the shape had to exist, but it is the cheapest shape in the system |
| **05 cost** | **stays a raster** | see below |
| hero | **removed** | no canon for heroes (STYLE.md §2) |

**Card 05 is the honest limit of this grammar, and the argument is worth keeping.** Its claim rides on
three channels the composed system does not have and should not gain casually:

1. **quantity by repetition** — three coin stacks against one, which is what "3 attempts" *means*;
2. **magnitude by size** — the single stack is *taller*, which is what "expensive" means;
3. **a curved arrow sweeping across a divider** — the retry tax climbing from one column to the other.

A `Compare` shape could hold the two columns. It could not hold the other two channels without adding a
size encoding and a curved connector, each of which is a **new encoding needing its own blind read** —
and a composed 05 without them is a *weaker* drawing than the raster, not merely a different one. The
test the decision was made on was not "can it be built" but **"does the composed version teach better"**,
and here it does not. Recorded cost, since it is real: on the dark theme card 05 is the one light plate
among eight dark cards, and it reads as a flash. The owner has three options — accept the seam, drop the
card (the prose already carries the sharpest form of its argument, an explicit `cost ≈ attempt_cost / p`
block), or commission the two encodings properly. **Not** "port it anyway".

### Two new shapes, both completing the design rather than extending it

**`Merge` (N→1)** was in the original architecture sketch — `<Brace>`: "1→N branch **or N→1 merge**" —
and was simply never built, because the pilot only needed a branch. Two shipping cards need it: two eval
sets feeding one scoreboard, three versioned artefacts feeding one canary. It is `Branch` mirrored: same
fixed row pitch, same `i × pitch + half the icon box` arithmetic, same `forkOffset`. Canon: STYLE.md §11.

**`Grid` (peers)** is the shape for content with no flow. The reasoning is in STYLE.md §17; the part
worth repeating is that **two columns is an argument, not a layout preference** — a row of four is read
left to right and reads as a sequence even with no arrows in it. A stripped reader confirmed the shape
does its job: *"unordered set of peers, unambiguously"*, citing the grid (no single reading path), the
absence of connectors, and the four cells being identical in size and border.

### The gates earned their keep again — five defects, three of them pre-existing

The blind-naming round and the label-stripped read between them found:

1. **`documentStack` was filling an open path**, so a straight closing chord painted half the front
   sheet in the back sheet's tint. Read as "the back sheet bleeding through — a z-order bug". Fixed by
   closing the fill path explicitly. **Pre-existing; shipped through four review rounds unnoticed.**
2. **`gauge`'s threshold notch read as a second needle**, and at 40 px as an "AI sparkle"; its
   full-circle hub bulged below the base line so the dial looked "knocked off its axis". Both flagged
   independently by two rounds. Redrawn: the threshold is now a **band on the rim** (concentric, so it
   cannot be mistaken for a pointer — the tachometer red-line convention, which is what a score floor
   *is*), and the hub is a half-disc sitting on the base. **Pre-existing, and CSS-CARDS-PLAN had already
   recorded "gauge wants another pass" — this is that pass.**
3. **Fork arms stopped inside the icon's transparent margin.** Measurably attached, visibly not: *"both
   branch ends terminate a few pixels before the glyphs, so the lines touch nothing."* An icon's drawing
   starts ~2 units of the card's width inside its viewBox, so the arm has to reach past the box edge, not
   to it. `-1.571` → `-2.6`. **Pre-existing — it was in the pilot too.**
4. **A merge's badges sat on its arms.** Three of them on card 07, so it read as systematic. New rule:
   **a badge never sits on the side a connector arrives from** — merge inputs flip theirs to the left.
5. **A fork group must not grow.** It used to (`flex: 1 1 auto`) and the surplus pooled at its trailing
   edge; harmless with a branch last in a lane, but a `Merge` is *followed* by the node it feeds, so it
   opened a gap between the arrowhead and its target. A drawing with a gap after the arrowhead says
   nothing arrives.

### Two content fixes a blind reader forced, both about badge *coverage*

- **Card 01's fork had one marked outcome and one bare one**, and the reader could not tell whether the
  fork meant "one branch works, one fails" or "the whole fork is the failure". The card means the first,
  so the surviving branch now carries a `tick`: some documents are indexed, some vanish. The asymmetry is
  the point here, unlike card 02, where both outcomes are equally correct and both take a `tick`.
- **Card 09 had badges on two of four peers**, and it manufactured a severity gradient out of nothing:
  *"the badged right column reads as worse and the bare globe reads as not actually a problem."* All four
  badges came off. The uniform channel is the red panel each cell already has; the icons name the
  subject and the labels name the fault. Cost, recorded: the raster's warning triangle on the poisoned
  document is gone, and the label carries it now.

The general rule that falls out, and it is the sharper cousin of §8's "one failure claim per fault":
**badge coverage across a card's peers must be all or none.** A partial pass reads as a ranking.

### Asked for a third time, and refused a third time: arrowheads on fork arms

Every stripped reader so far has wanted them. This one put it hardest — *"the only arrowhead in the red
panel points at the junction dot, not at either destination… direction is asserted for the first hop and
then silently dropped."* The grammar's answer is unchanged (STYLE.md §11: a fork draws topology, not
flow, and staying headless keeps it distinct from the dashed pipeline). But **three independent readers
raising the same objection is data, not noise**, and it is recorded here as an open question for the
owner rather than as a settled matter. **Closed 2026-07-27 — the arms stay headless, and the reasoning is
the owner's rather than the grammar's; see the owner-rulings section at the end.**

### Still open

1. **RU and SK are visually divergent** until their labels are translated: both pages still embed all
   nine rasters and the hero is gone from all three. The label list is small and the strings are short.
2. **The `.webp` files stay in git**, unreferenced by EN. They cannot go before the locales migrate.
3. **`pin`'s glyph is a map pin** — the convention for *place*, not for *pinned version*. Unused in the
   set for that reason (card 07's three artefacts all take `tag`, which is both correct and a stronger
   claim). Redraw it before anything uses it. STYLE.md §8 records this.
4. **Card titles restate their section headings** on five of the eight composed cards. Invisible while
   the title was baked into a raster; now it is HTML text 40 px under an `##` that says nearly the same
   words. Either is defensible — a card should be self-contained if it is ever reused — but it is now a
   visible repetition and only the page's author can settle it. **Resolved 2026-07-27: the titles stay,
   two were shortened — see the owner-rulings section at the end.**
5. **`branchSplit` is an icon made of arrows**, sitting at the end of an arrow. A reader called the
   arrow-on-arrow "the only node on any of the four cards that isn't clearly a *thing*".
6. **An odd fan puts one leg on the trunk.** Card 07's middle input is collinear with the outgoing
   connector — symmetry cannot help with an odd count. Rated "very slightly promotes the chip" by a
   stripped reader, so it ships; the mitigation is the visible vertical stem. STYLE.md §11 records it.

### The second stripped read — what the fixes bought, and the two charges that stand

Re-run after the fixes above, fresh agent, zoomed crops of every junction:

- **Card 01's fork now reads as intended** — *"one blessed, one rejected"*. The `tick` closed the
  ambiguity the first read found.
- **Card 03's merge reads as a merge**, and its two inputs read as **equals**: *"same size, symmetric
  bracket, the junction dot exactly midway, neither on the output axis."*
- **Card 07 is "the most consistent card"** — *"all three teal inputs carry the identical grey tag badge
  (an attribute, not a verdict)… nothing is singled out arbitrarily."* The decision to give all three
  artefacts the same version mark validated itself.
- **Card 09: "unordered set of peers, decisively"** — the one thing the shape had to achieve. Cited: no
  connectors, no numbering, four cells identical in size, border and radius, and a grid rather than a row.
- **Connectors touch, verified at 3× zoom. No badge sits on a connector.**

Two charges stand, and neither is a bug:

**1 · Card 09 might not deserve to be a card at all.** *"It strips down to four empty rectangles; it
would render identically as a plain bulleted list, which means the diagram is doing no work."* That is
the `create-infographic` skill's own go/no-go test pointed at a peer set — and the page's §9 prose is
already four bolded paragraphs with the same four names. The shape is correct; the question is whether
the content wants a picture. **Owner's call**, and worth taking seriously: keep it as a scannable visual
index, or drop it and let the prose carry four unrelated failures the way prose carries lists.
**Resolved 2026-07-27: the card stays, and the test itself was refined — see the owner-rulings section.**

**2 · Card 09's four glyphs are mixed in rhetorical register.** Two of them (an *open* padlock, a
disconnected plug) draw their own fault; two (a document, a globe) are neutral objects that only the red
panel accuses. There is no fully uniform option: badging all four double-marks the two that already say
it (§8 rule 2), and badging none leaves the glyph asymmetry. Bare is the lesser fault — a red badge is a
loud channel and a glyph's state is a quiet one — but it is recorded rather than resolved.

Smaller residuals from the same read, none acted on:

- **The arrowhead lands inside the junction dot** — *"two terminators stacked on the same point."* Moving
  either would re-open a defect the other was introduced to close (an unanchored fork, a dropped
  direction), so it stays.
- **`branchSplit` and `scales` are optically light** next to the duotone icons, and both sit at the
  *conclusion* of their card — *"the terminal glyph is the weakest object on the card."* `branchSplit` is
  additionally an icon made of arrows, at the end of an arrow.
- **The two panels of a contrast card no longer share a left margin.** True, and it is the owner's
  explicit round-3 choice (centred lanes); the coupling that holds a contrast card together was measured
  to be the *recurring icon*, not the shared origin.
- **Panels look bottom-empty.** Largely an artefact of the test itself — hidden labels reserve their
  space — plus the known fixed `--branch-row` slack, which triples on a three-input merge.

---

## Owner rulings 2026-07-27 — four questions closed, and the content fixes they pulled in

Everything the migration left for the page's author. Three of the four had been raised repeatedly by
independent readers, and in two of those the **reader was right about the observation and wrong about the
remedy** — which is the pattern worth carrying forward: a stripped read reports what it sees, and only the
author knows what the card is for.

### 1 · Card 05 stays a raster — and the exception became a documented escape hatch

The migration argued card 05 as a one-off. It is now a **rule with a criterion**, written into
`create-infographic` §1a and cross-referenced from STYLE.md §1 and §7:

> **Substrate order is composed first, generation is the escape hatch.** Reach for it when a thought needs
> a channel the composed grammar does not have — because **a composed version that drops an encoding the
> argument depends on is a weaker drawing, not a different one.**

Card 05 is the worked example: quantity-by-repetition, magnitude-by-size and a curved connector crossing a
divider, none of them expressible, each a new encoding owing its own blind read. The costs are named rather
than discovered later — a light plate among theme-adaptive cards, labels that do not localise, a card that
cannot be diffed.

Three things the skill now says that this document did not:

- **The hatch is narrow.** It is for a missing *encoding* or a genuinely complex *composition* — never for
  "the markup would be fiddly" or "generation is faster". Those trade a permanent capability for a one-off
  convenience.
- **A rasterised card must pass the canon SVGs in as `--ref` images**, plus an approved composed card for
  palette and type, plus a sentence saying what each ref governs. Otherwise the hatch breaks the thing the
  lexicon exists for: **the substrate boundary is exactly where icon identity drifts, because nothing
  structurally prevents it there.** Stated with its limit — an image model *approximates* a reference, it
  does not place it — so the generated card's icons still go through blind naming and any drift is recorded
  as a residual on that card. This set does not exercise the risk (`coins` appears on no composed card),
  which is luck, not design.
- **Two honest exits, not three.** Build the missing encoding properly, or drop the card. A second card
  taking the hatch for the *same* missing channel is a gap in the grammar, and the fix belongs there.

### 2 · Card 09 keeps its card — and the go/no-go test needed refining, not applying

The charge was the skill's own test: *"it would render identically as a plain bulleted list, which means
the diagram is doing no work."* The ruling is that the test was too blunt, and it now reads
(`create-infographic` §1b):

> **"It would render identically as a list" is not sufficient grounds to reject a card when the card and
> the prose serve different reading modes.**

The card is the **glance**; the prose is the **detail**. A reader who skims and a reader who works through
are not the same reader, and a page may serve both. The test rejects a card that adds nothing *at a
glance* — not one whose content could also be written as a list, which is true of almost any diagram.
Card 09 is the skill's worked example precisely because it passed every other check (the two-column `Grid`
reads as *peers with no order*, confirmed by a stripped reader) and was nearly cut on this one.

### 3 · Fork arms stay headless — closed, with the owner's reasoning rather than the grammar's

Three independent readers asked for arrowheads. The grammar's defence ("a fork draws topology, not flow")
was never the point at issue; what settles it is how the drawing actually reads:

> An arm meeting an arrowhead reads as **"and this leads to the following results"** — the incoming
> connector's head, landing on the junction, already asserts direction for the whole fan, so the arms only
> have to say which destinations it reaches. **The topology is legible as drawn.**

Recorded in STYLE.md §11 as closed, with the condition for reopening: evidence that a reader misread a
fork's *direction*, not a further preference for heads. Written down because a question three readers have
raised will otherwise reopen itself by default.

### 4 · Embedded card titles stay — and the repetition is answered by shortening the title

The owner's reasoning is the durable part, so it is canon now (`create-infographic` §3, STYLE.md §2):

> With a title inside the frame the reader stays focused *within* the diagram and is reminded what it
> argues. Without one they must look outside it, to an `##` that "has a different layout and looks like it
> belongs to the section, not the diagram".

The repetition is real, and the fix runs one way only: **heading = the full claim, card title = the short
form**, on the model of an article title against its table-of-contents entry. **Never shorten the
heading** — it is the page's contract with a reader scanning the sidebar. And **a title that decays into a
topic label ("Drift") is worse than a duplicate**, because a duplicate still argues something.

Applied, with the reasoning per card, because "leave it" is a decision too:

| Card | Heading | Card title | |
|---|---|---|---|
| 03 | One eval set is not enough | **Two eval sets, not one** | shortened — the claim survives, and the positive form is sharper than the negative |
| 06 | Re-index before you retrain | **Retrain last** | shortened — an imperative with the ordering intact, and it is the compressed form of the heading rather than its topic |
| 01 | The corpus is the product | The corpus is the product | **left** — the heading is already the minimal form of its claim; "The corpus" would be a topic label |
| 04 | Green is not the same as correct | Green is not correct | **left** — already the compressed heading |
| 07 | The prompt and the corpus are releases | Prompt and corpus are releases | **left** — already the compressed heading; anything shorter ("Three releases") drops the subject |
| 02 · 08 · 09 | — | Retrieval must be allowed to refuse · Cheapest check first · Four the lists miss | already distinct |

Card 03's caption opened *"Two sets, two different questions…"*, which put **two** three times beside the
new title; it now opens *"Each answers a different question…"*.

### The content fixes the rulings pulled in

**"Three drifts" is gone.** Card 06's caption claimed a count the card never drew — tolerable baked into a
raster, not once it is HTML text a reader can hold against the diagram beside it. The number came from the
prose's pointer to LLMOps ("three flavours of drift"), which is a different lesson's content. Replaced with
the caveat the card actually argues: **"Drift usually lives in the corpus or the query, not in the
weights."** The dropped half ("weights are the last rung") is carried by the `weights last` node, the rank
ramp and the new title. The general rule: **a caption is a claim, and a claim about a quantity the drawing
does not show is false precision** — the same failure mode §6 of the skill records for generated cards,
arriving this time in hand-written text.

**`day-one test set` → `week-one test set`.** The card said one thing and the prose beneath it said
another ("Test cases written in week one"). Harmonised on the card, not the prose, deliberately: the card
label is an EN-only surface right now, so changing it leaves RU/SK untouched and the correction propagates
naturally when the labels are translated. The raster still says "day-one", which is the locales' existing
state and their translation pass's problem, not a new divergence.

**Prose anchors: three added, two refused.** Composed labels are DOM text, so the restatement rule is no
longer an accessibility gate — it is a coherence preference (STYLE.md §4). Added where it lands naturally:
`clean uniform docs` and `mixed sources` (§1's first sentence gained "clean, uniform, all of one kind" and
its list of PDFs and scans is now introduced as "a mix of sources"), and `grounded answer` (§2 described
only the refusal arm of the card's fork; it now describes both). Refused as padding, and recorded rather
than quietly skipped: `false confidence` and `honest scoreboard`, both on card 03 — §3's prose already
makes each claim in stronger words ("where a green dashboard starts lying", "Neither replaces the other"),
and inserting the card's two-word labels would be vocabulary matching, not teaching.

### Still open after this round

1. **RU and SK are unmigrated** and still embed all nine rasters; their card 06 caption still says
   *"Три вида дрейфа"* / three drifts, because the raster does. That is the translation pass's to fix
   together with the labels — this round deliberately did not touch `i18n/**`, since the labels it would
   translate had to be final first.
2. **`pin`'s glyph is a map pin.** Unchanged; redraw before anything uses it.
3. **`branchSplit` is an icon made of arrows at the end of an arrow**, and it and `scales` are optically
   light next to the duotone icons.
4. **An odd fan puts one leg on the trunk** (card 07). Ships, mitigated by the visible stem.
