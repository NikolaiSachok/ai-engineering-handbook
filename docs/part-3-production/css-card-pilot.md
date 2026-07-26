---
id: css-card-pilot
title: "Pilot — composed cards vs generated images"
sidebar_label: "Pilot (internal)"
sidebar_position: 99
unlisted: true
---

# Composed cards vs generated images

A temporary comparison page, not part of the course. Each pair below shows the **generated raster
card** that ships today and the same card **composed from HTML and a fixed icon set**. Delete this
page once the approach is decided.

What to judge: whether the composed version reads as well as the raster at desktop and phone width,
whether the icon set carries enough character, and whether the ordering ramp on card 06 makes the
argument land faster than the flat version does.

## Card 06 — the drift ladder

The card whose encoding is *wrong* in the raster set, which is why it goes first: it is an
**ordering** — first resort to last — and the raster renders the four rungs as identical peers, so
the reader has to reconstruct the order from four labels. The composed version encodes rank in
colour and emphasis, so the ramp is visible before a single word is read.

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
    <Node icon="dashboard" badge="bang" label="drift detected" />
    <Flow kind="fail" />
    <Node icon="chip" label="retrain the model" />
  </Lane>
  <Lane kind="production" label="PRODUCTION">
    <Node icon="database" badge="refresh" label="re-index" rank="1" />
    <Flow />
    <Node icon="sliders" label="retrieval mix" rank="2" />
    <Flow />
    <Node icon="document" label="prompt" rank="3" />
    <Flow />
    <Node icon="chip" label="weights last" rank="last" />
  </Lane>
</InfoCard>

## Card 02 — retrieval and the refusal path

Tests the other half of the grammar: a **branch**. One input, two legitimate fates — an answer or an
honest refusal — drawn with a brace rather than two arrows.

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
    <Brace />
    <Node icon="document" badge="tick" label="grounded answer" />
    <Node icon="speechBubble" label="or “no context”" />
  </Lane>
</InfoCard>

## The icon lexicon

Twenty-four assets — sixteen base objects and eight overlay badges — generated as two single sheets
so they are consistent by construction rather than by luck, then sliced. A badge composed onto a
base object is what keeps the set at 24 assets instead of the ~36 the cards would otherwise need:
a database is one asset, and `re-index` is that database with a refresh badge.

<InfoCard title="Base objects">
  <Lane kind="production" label="OBJECTS">
    <Node icon="document" label="document" />
    <Node icon="documentStack" label="documentStack" />
    <Node icon="spreadsheet" label="spreadsheet" />
    <Node icon="browserPage" label="browserPage" />
    <Node icon="database" label="database" />
    <Node icon="clipboard" label="clipboard" />
    <Node icon="calendar" label="calendar" />
    <Node icon="dashboard" label="dashboard" />
    <Node icon="speechBubble" label="speechBubble" />
    <Node icon="speechBubbleGroup" label="speechBubbleGroup" />
    <Node icon="magnifier" label="magnifier" />
    <Node icon="sortedList" label="sortedList" />
    <Node icon="gauge" label="gauge" />
    <Node icon="gate" label="gate" />
    <Node icon="chip" label="chip" />
    <Node icon="sliders" label="sliders" />
  </Lane>
</InfoCard>

<InfoCard title="Badge overlays" caption="Composed onto a base object, so 24 assets cover ~36 concepts.">
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
