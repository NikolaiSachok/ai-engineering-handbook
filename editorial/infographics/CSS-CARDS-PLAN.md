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

## The open tension: generated rasters vs theme adaptation

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

## Sequence

1. Generate and slice the two icon sheets; ship as `static/img/infographics/icons/<concept>.webp`.
2. Build `Card` / `Lane` / `Node` / `Flow` / `Brace` + `icons.ts`, with the `rank` ordering channel.
3. **Port card 06 (the drift ladder) first** — it is the card whose encoding is currently wrong, so the port
   demonstrates the win rather than merely reproducing a raster.
4. Compare side by side at article width and 360px; decide whether the composed register is good enough to
   replace the whole set.
5. If yes: port the remaining eight, drop the rasters, and translate the labels — the RU/SK pages then carry
   real localised diagrams. Keep `hero.webp` as a raster; a hero is an illustration, not a labelled-node
   diagram, and it is the one image where generation genuinely wins.
6. Update the `create-infographic` skill: composed cards become the default for labelled-node content, and
   generation is reserved for heroes and scenes.

## What does NOT change

The labelled-node discipline, the label budget (a phone is still 360px wide), the demo/production lane
grammar, the flow-mark vocabulary, and the rule that the prose must still teach the lesson. Composition changes
the substrate, not the method.
