---
id: css-card-pilot
title: "Pilot — composed cards vs generated images"
sidebar_label: "Pilot (internal)"
sidebar_position: 99
unlisted: true
---

# Composed cards vs generated images

A temporary comparison page, not part of the course. Each pair below shows the **generated raster
card** that ships today and the same card **composed from HTML and an inline-SVG icon lexicon**.
Delete this page once the approach is decided.

What to judge: whether the composed version reads as well as the raster at desktop and phone width,
whether the icon set carries enough character, whether the connectors and the brace now read as
deliberate drawing rather than CSS approximations, and whether the ordering ramp on card 06 makes
the argument land faster than the flat version does. Toggle the site theme as well — the composed
cards adapt, the rasters cannot.

## Card 06 — the drift ladder

The card whose encoding is *wrong* in the raster set, which is why it goes first: it is an
**ordering** — first resort to last — and the raster renders the four rungs as identical peers, so
the reader has to reconstruct the order from four labels. The composed version encodes rank in
colour and emphasis, and because the icons are `currentColor`-driven the ramp tints **the icon as
well as the label**, so it is visible before a single word is read.

### Generated (ships today)

<Infographic
  src="/img/infographics/production-failures/06-drift.webp"
  alt="A demo lane going straight from detected drift to retraining the model, and a production lane stepping through re-index, retrieval mix and prompt before reaching a greyed-out chip labelled 'weights last'"
  caption="Three drifts, one ladder — and weights are the last rung, not the first."
/>

### Composed

<InfoCard
  title="Re-index before you retrain"
  caption="Three drifts, one ladder — and weights are the last rung, not the first.">
  <Lane kind="demo" label="DEMO">
    <Node icon="driftCurves" label="drift detected" />
    <Flow kind="fail" />
    <Node icon="chip" label="retrain the model" />
  </Lane>
  <Lane kind="production" label="PRODUCTION">
    <Node icon="database" badge="refresh" label="re-index" rank="1" />
    <Flow />
    <Node icon="sliders" label="retrieval mix" rank="2" />
    <Flow />
    <Node icon="codeFile" label="prompt" rank="3" />
    <Flow />
    <Node icon="chip" label="weights last" rank="last" />
  </Lane>
</InfoCard>

## Card 02 — retrieval and the refusal path

Tests the other half of the grammar: a **branch**. One input, two legitimate fates — an answer or an
honest refusal — drawn with a brace that spans both outcomes, stacked, with the incoming arrow aimed
at the brace's midpoint.

### Generated (ships today)

<Infographic
  src="/img/infographics/production-failures/02-retrieval.webp"
  alt="A demo pipeline that always returns top-k, against a production pipeline where a score floor after reranking permits an empty result"
  caption="A relevance floor applied after reranking, and a generator allowed to answer 'no context'."
/>

### Composed

<InfoCard
  title="Retrieval must be allowed to refuse"
  caption="A relevance floor applied after reranking, and a generator allowed to answer 'no context'.">
  <Lane kind="demo" label="DEMO">
    <Node icon="documentStack" badge="cross" label="top-k, always" />
    <Flow kind="fail" />
    <Node icon="speechBubble" badge="bang" label="confident wrong answer" />
  </Lane>
  <Lane kind="production" label="PRODUCTION">
    <Node icon="sortedList" label="rerank" />
    <Flow />
    <Node icon="gauge" label="score floor" />
    <Flow />
    <Branch>
      <Node icon="speechBubble" badge="tick" label="grounded answer" />
      <Node icon="speechBubbleEmpty" badge="tick" label="or “no context”" />
    </Branch>
  </Lane>
</InfoCard>

## The icon lexicon

Thirty-seven inline SVGs — twenty-nine base objects and eight overlay badges. Generic objects are
vendored from Tabler (MIT) and normalised onto one 48-unit grid; the domain metaphors no icon set
ships are hand-authored on the same grid, so a vendored icon and a hand-authored one are
indistinguishable in use. Provenance, the convention each hand-authored icon draws, and the licence
are in `src/components/InfoCard/icons/NOTICE.md`.

The whole set is **13 KB raw, under 6 KB gzipped**, against 156 KB for the raster equivalent — and
unlike the rasters it recolours, adapts to the theme, and stays crisp at any size.

These three cards are a reference sheet rather than teaching cards, so they deliberately ignore the
nine-string label budget.

<InfoCard title="Containers, records, instruments">
  <Lane kind="production" label="OBJECTS">
    <Node icon="document" label="document" />
    <Node icon="documentStack" label="documentStack" />
    <Node icon="spreadsheet" label="spreadsheet" />
    <Node icon="browserPage" label="browserPage" />
    <Node icon="database" label="database" />
    <Node icon="clipboard" label="clipboard" />
    <Node icon="calendar" label="calendar" />
    <Node icon="codeFile" label="codeFile" />
    <Node icon="dashboard" label="dashboard" />
    <Node icon="gauge" label="gauge" />
    <Node icon="sliders" label="sliders" />
    <Node icon="magnifier" label="magnifier" />
    <Node icon="sortedList" label="sortedList" />
    <Node icon="funnel" label="funnel" />
    <Node icon="gate" label="gate" />
    <Node icon="scales" label="scales" />
  </Lane>
</InfoCard>

<InfoCard
  title="Reach, plumbing, and the domain metaphors"
  caption="The last four are hand-authored: no open set ships them, and a generic stand-in flattens the idea.">
  <Lane kind="production" label="OBJECTS">
    <Node icon="speechBubble" label="speechBubble" />
    <Node icon="speechBubbleEmpty" label="speechBubbleEmpty" />
    <Node icon="speechBubbleGroup" label="speechBubbleGroup" />
    <Node icon="globe" label="globe" />
    <Node icon="plug" label="plug" />
    <Node icon="chip" label="chip" />
    <Node icon="cloud" label="cloud" />
    <Node icon="coins" label="coins" />
    <Node icon="lockOpen" label="lockOpen" />
    <Node icon="driftCurves" label="driftCurves" />
    <Node icon="branchSplit" label="branchSplit" />
    <Node icon="chainSteps" label="chainSteps" />
    <Node icon="traceSpans" label="traceSpans" />
  </Lane>
</InfoCard>

<InfoCard title="Badge overlays" caption="Composed onto a base object, so the set covers far more concepts than it holds assets.">
  <Lane kind="demo" label="BADGES">
    <Node icon="document" badge="tick" label="tick" />
    <Node icon="document" badge="cross" label="cross" />
    <Node icon="document" badge="bang" label="bang" />
    <Node icon="document" badge="padlock" label="padlock" />
    <Node icon="document" badge="pin" label="pin" />
    <Node icon="document" badge="tag" label="tag" />
    <Node icon="document" badge="refresh" label="refresh" />
    <Node icon="document" badge="crack" label="crack" />
  </Lane>
</InfoCard>

## The connector vocabulary

Three kinds, and the third is reserved. Each is one SVG line with a real `marker-end`, sized to the
slot it is given, so the arrow spans the actual gap and its head is part of the same path.

<InfoCard title="Flow marks" caption="The failure hue is only ever the consequence of the fault.">
  <Lane kind="production" label="DASHED — NORMAL FLOW">
    <Node icon="database" label="retrieve" />
    <Flow />
    <Node icon="sortedList" label="rerank" />
    <Flow />
    <Node icon="speechBubble" label="answer" />
  </Lane>
  <Lane kind="production" label="SOLID — TIGHT ADJACENCY">
    <Node icon="gate" label="gate" />
    <Flow kind="solid" />
    <Node icon="scales" label="scoreboard" />
  </Lane>
  <Lane kind="demo" label="FAIL — THE CONSEQUENCE">
    <Node icon="chainSteps" badge="crack" label="unguarded chain" />
    <Flow kind="fail" />
    <Node icon="lockOpen" badge="bang" label="unscoped access" />
  </Lane>
</InfoCard>
