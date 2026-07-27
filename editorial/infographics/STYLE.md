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

**Two card substrates now exist, and the palette below is the generated one.** Which one a card gets is the
skill's call, not this file's: **composed is the default and generation is the documented escape hatch**
(`create-infographic` §1a) — taken only when a thought needs a channel the composed grammar does not have,
because a composed card that drops an encoding its argument depends on is a *weaker* drawing, not a
different one. This set uses the hatch exactly once, on `05-cost` (§7), and pays the declared cost: one
light plate among eight theme-adaptive cards.

A *generated* card is a baked raster and is light-ground in both themes (§4 frames it). A *composed* card
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
  left edge reading `DEMO` / `PRODUCTION`. This is the set's spine — seven of the nine cards use it. A card
  whose content isn't a demo-vs-production contrast (the cost comparison, the four-peer card) may drop the
  lanes, but nothing else changes: the four-peer card uses `Grid` (§17) and keeps every other rule.
- **No hero, and this is a rule rather than an omission.** The page had a `16:9` generated hero; it was
  removed on 2026-07-27. Two reasons, and the second is the durable one: no other page in the handbook has a
  hero, and there is **no canon for making one** — cards have a grammar, a palette, an icon register, a
  sizing rule and a verification gate, and a hero has none of that. An unregulated one-off is how a style
  system starts drifting. **So: no heroes until a hero guide exists.** `hero.webp` stays in git, unused,
  and `CSS-CARDS-PLAN.md`'s "a hero is an illustration where generation genuinely wins" still holds for
  whoever writes that guide — it is deferred, not refuted.
- **No index badges.** The skill offers a numbered circle; this set omits it, because the page's numbered
  headings already carry the ordinal and a badge-less card stays reusable on a page that isn't numbered.
- **Every card keeps its own title inside the frame, even under an `##` that says nearly the same words.**
  Settled by the owner on 2026-07-27, and the reasoning is the rule: with a title in the frame the reader
  stays focused *within* the diagram and is reminded what it argues; without one they must look outside it
  to a heading that "has a different layout and looks like it belongs to the section, not the diagram".
  The repetition is real — it was invisible while the title was baked into a raster — and it is answered by
  **shortening the title, never the heading**: the heading carries the full claim, the card title the short
  form, on the model of an article title against its table-of-contents entry (`create-infographic` §3).
  Where a heading is already the minimal form of its claim, an identical card title is the right outcome;
  a title that decays into a topic label ("Drift") is worse than a duplicate, because a duplicate still
  argues something. Applied to this set: `## 3 · One eval set is not enough` → card **"Two eval sets, not
  one"**, and `## 6 · Re-index before you retrain` → card **"Retrain last"**. Cards 01 (`The corpus is the
  product`), 04 (`Green is not correct`) and 07 (`Prompt and corpus are releases`) were left alone —
  the first is already its own short form and the other two already are the compressed heading.
- **Icons confined to the upper two thirds of a lane**, so labels sit *inside* the panel border. Without this
  the model pushes labels below the border.
- **Monospace labels, bold geometric sans titles**, sentence case, one line.

## 3 · Dimensions and shipping

| | Ratio | Generate | Ship |
|---|---|---|---|
| Card | `4:3` | `--res 2K` PNG | WebP, **1400px**, `-q 82` |
| ~~Hero~~ | ~~`16:9`~~ | ~~`--res 2K` PNG~~ | ~~WebP, **1600px**, `-q 82`~~ — **suspended, §2: no heroes until a hero guide exists** |

```bash
cwebp -q 82 -resize 1400 0 raw/02-retrieval.png -o static/img/infographics/production-failures/02-retrieval.webp
```

Budget ≤ 200 KB per card; the first set runs **42–54 KB each, 500 KB for ten**. Raw PNGs never enter git —
they live in the session scratchpad and are reproducible from the archived batch (§5).

**Naming:** `static/img/infographics/<page-slug>/NN-<slug>.webp`, `NN` = reading order on the page. The
directory always matches the page slug, so a card is traceable to its page.

## 4 · Embedding

Use the globally-registered component — no import needed in any `.md`, in any locale:

```mdx
<Infographic
  src="/img/infographics/production-failures/05-cost.webp"
  alt="Tri lacné pokusy proti jednému drahému, s vyznačenou daňou za opakovanie"
  caption="Lacnejší model vyhrá len vtedy, ak jeho úspešnosť prekoná drahší viac než rozdiel v cene."
/>
```

`Infographic` also takes `wide`, which opts out of the desktop width cap for a `16:9` image. **It
currently has no call site** — the only one was the hero (§2). The prop stays: it is part of the
component's documented API and the next set that ships a wide image will want it.

`src` is identical in every locale; **`alt` and `caption` are translated** (in-image labels are English-only —
the skill explains why, and requires the prose to restate every label). `alt` must describe what the card
actually shows: if a card is regenerated with a different composition, its `alt` is now wrong.

`src/components/Infographic/` handles the responsive frame, lazy loading, the caption, and — because the cards
are light-ground — a border plus a slight brightness reduction on the dark theme so a card reads as a
deliberate plate rather than a white flash.

**Composed cards embed as markup, not as `src`.** `InfoCard` / `Lane` / `Node` / `Flow` / `Branch` /
`Merge` / `Grid` are registered globally in `src/theme/MDXComponents.tsx`, so any `.md` in any locale can
use them with no import — and because every label is HTML text, a translator edits the Markdown rather
than asking for a regenerated image. The connector vocabulary is `kind="dashed"` (normal flow),
`"solid"` (tight adjacency) and `"fail"` (the consequence of the fault, and nothing else).

**Composed cards take no `alt`.** Their labels are real text in the DOM, so a screen reader already reads
the diagram; an `alt` would be a second, drift-prone description of something the markup already says.
`alt` belongs to `Infographic` alone.

**And the prose-restates-every-label rule changes weight with the substrate.** For a raster it is a hard
accessibility gate — unrestated in-image text is text no reader can reach. For a composed card the label
*is* text in the page, so what remains is a **coherence** preference: a card naming something the prose
never mentions reads as two authors. Add the anchor where it lands naturally; where it would only insert
the card's two words into a paragraph that already makes the point in sharper ones, leave the prose alone
and record the decision. (`create-infographic` §7.)

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
| `production-failures` | [Why AI systems fail in production](../../docs/part-3-production/production-failures.md) | 9 | **8 composed, 1 raster** (`05-cost`); hero removed (§2) — EN migrated 2026-07-27, RU/SK still on rasters until the labels are translated |

**`05-cost` is this set's one use of the escape hatch, and it is declared rather than tolerated** (§1). Its
argument needs quantity-by-repetition, magnitude-by-size and a curved connector crossing a divider; none is
expressible in the composed grammar, and each would be a new encoding owing its own blind read. The costs
are real and named: a light plate on the dark theme, labels that do not localise (so §4's restatement rule
applies in full to that card), and a card that cannot be diffed. Its icons happen not to collide with the
composed lexicon — `coins` appears on no composed card in this set — so the cross-substrate identity drift
`create-infographic` §1a warns about is **not** exercised here. Any *future* rasterised card must pass the
canon SVGs in as `--ref` images, per that section.

The nine `.webp` cards are **still in git and unreferenced by EN** — deliberately, until the owner confirms
the migrated page. Deleting the eight that composed cards replaced is one follow-up commit, and it cannot
happen before the RU and SK pages are migrated too, because those still embed them.

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
the lexicon needs a new base object, not an overlay. (A magnifier is not a state, which is why
*retrieval* is a base object — §12 — and not `documentStack` + a magnifier badge.)

**A failure badge marks the thing that is broken, never the thing that is being misused.** `cross`,
`bang` and `crack` are claims about a component. Put one on a component that works and the card
asserts something it does not mean.

> Card 02 carried a `cross` on its `top-k, always` node and it read as *"retrieval is broken"*. The
> card's claim is the opposite and sharper: **the retrieval mechanism works correctly; always
> returning top-k is what produces the confident wrong answer.** The fault is in the policy, not the
> machinery. The badge came off, and nothing was lost — the red lane, the failure-hue connector and
> the `bang` on the outcome already carry the failure, and they carry it *where it happens*.

Two rules fall out, and they are what to check before adding any failure badge:

1. **The input node of a failure is usually unmarked.** Mark the *consequence*, not the thing that
   was used badly. The same audit removed `crack` from `unguarded chain` on the flow-marks card: a
   chain run without a gate is not a broken chain.
2. **One failure claim per fault.** The lane outline, its pill, the `fail` connector and one badge
   are four channels saying the same thing; using all four on both ends of the arrow is
   over-marking, and over-marking blurs *which* thing failed.
3. **Across peers, badge coverage is all or none.** A partial pass reads as a *ranking*. Card 09 had
   badges on two of its four failure modes and a blind reader duly reported that *"the badged right
   column reads as worse and the bare globe reads as not actually a problem"* — a severity gradient
   manufactured out of nothing, on a card whose entire claim is that the four are peers. All four
   came off; the uniform channel is the red panel each cell already carries. This is rule 1's
   cousin: rule 1 says don't mark the wrong thing, rule 2 says don't mark one thing twice, and this
   says **don't mark some of a set**.
4. **A badge never sits on the side a connector arrives from.** A `Merge` gathers its inputs from the
   right, so a default bottom-right badge lands exactly on the arm; three of them on one card read as
   a systematic collision rather than an accident. Merge inputs flip theirs to the left. This is a
   *third* position rule alongside the default and `BADGE_TOP_RIGHT`, and it composes with them:
   first avoid the icon's own busy corner, then avoid the connector's side.

| Badge | Means | Use it when | Colour role | Position |
|---|---|---|---|---|
| `tick` | accepted, correct outcome | an outcome the system is *supposed* to produce — including a refusal | correct hue | bottom-right |
| `cross` | rejected, does not happen | a step that is skipped, dropped or refused | failure hue | bottom-right |
| `bang` | fault, warning | the thing that goes wrong; at most twice per card | failure hue | bottom-right |
| `crack` | broken, degraded | a component that has failed rather than one that misbehaves | failure hue | bottom-right |
| `padlock` | scoped, or sealed | access control, secrets, redaction — **and a thing deliberately held immutable**, e.g. a frozen regression set | neutral | bottom-right |
| `pin` | fixed, pinned | a version, a snapshot, a chosen anchor | neutral | bottom-right |
| `tag` | labelled, versioned | metadata, an ingestion tag, a release | neutral | bottom-right |
| `refresh` | repeated, re-run | re-indexing, retraining, retrying, any repeat of the base action | neutral | bottom-right |

Colour roles resolve to `--ic-ok`, `--ic-fail` and `--ic-neutral` (§9). The glyph inside is
`--ic-badge-ink` (`#ffffff` in both themes).

**Two rows earned their wording during the migration, and one is a known defect:**

- **`padlock` covers "sealed", not only "scoped".** The frozen regression set on card 03 is a thing held
  deliberately unchanging, and a padlock is the near-universal convention for exactly that. Extending the
  use-list to the case the glyph's own convention already carries is not lexicon creep; substituting a
  glyph that means something else would be.
- **`pin`'s drawing says the wrong thing, and it is unused for that reason.** The asset is a **map pin** —
  a teardrop marker with a hole — which is the convention for *place*, not for *pinned version*. The
  documented meaning ("a version, a snapshot, a chosen anchor") and the drawing disagree. No card in the
  shipping set uses it: the three versioned artefacts on card 07 all take `tag`, which is both correct and
  a stronger claim (one identical version mark across three different objects *is* that card's thesis).
  **Before `pin` is used, redraw it as a push-pin and blind-name it** — a badge whose glyph contradicts its
  row is worse than a missing badge.

**`BADGE_TOP_RIGHT` — the declared exception.** Badges sit bottom-right by default. Icons whose own
drawing occupies that corner move theirs to the top-right, or the overlay covers the part of the icon
that carries the meaning — `driftCurves` (the shift arrow), `sortedList` (the descending arrow),
`traceSpans` (the last span and the axis), `gate` (the base plate), `branchSplit` (the return arm),
`retrieval` (the magnifier — which is the whole meaning), `speechBubble` and `speechBubbleEmpty`
(the tail). The list lives in `icons/index.ts`; adding an icon whose bottom-right is busy means
adding it there too.

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
| The same fork, mirrored | `<Merge>` | N→1 — N peers, one destination |

- Every connector is one SVG line with a real `marker-end`. Heads are never faked from CSS borders.
- **A 1→N split is a fork, not N arrows from a point.** The fork's arms carry no arrowheads: it draws
  topology, not flow, and staying headless keeps it distinct from the dashed pipeline.
  **Closed by the owner on 2026-07-27 and not open by default** — three independent stripped readers had
  each asked for arrowheads on the arms, which is data rather than noise, so the objection was put to the
  owner rather than defended from the grammar. The ruling: an arm meeting an arrowhead reads as *"and this
  leads to the following results"* — the incoming connector's head, landing on the junction, already
  asserts the direction for the whole fan, and the arms then only have to say which destinations the fan
  reaches. **The topology is legible as drawn.** Reopen this only with evidence that a reader misread the
  *direction* of a fork, not with a further preference for heads.
- **The fork is symmetric about the incoming connector's axis** — with two outcomes, one above and
  one below. Hanging both below the axis makes the first outcome collinear with the incoming arrow,
  and it then reads as the main path with the other as a side note.
- **Alignment rule: a connector sits on the icon centre line, derived from the icon box, never from
  the node.** `margin-top: calc(var(--fork-offset, 0px) + var(--ic-box) / 2 - 5px)`. A node's height
  changes whenever a label wraps; the icon box does not.
- **`Merge` is `Branch` mirrored, not a second implementation.** Same fixed row pitch, same
  `i × pitch + half the icon box` arithmetic, same `forkOffset` pushing the rest of the lane onto the
  axis; only the handedness changes — fork column to the right of the nodes, stem on its right edge,
  arms running left into the nodes' own margin, node labels right-aligned so an icon never drifts away
  from the arm that gathers it.
- **A fork group does not grow.** The connector and the fork it meets live in one flex item so a wrapping
  lane cannot separate them, and that item is **content-sized**. It used to grow, and the growth had
  nowhere to go — the connector inside stops at its own cap, so the surplus pooled at the group's trailing
  edge. Harmless while a branch was the last thing in a lane; with a `Merge`, which is followed by the node
  it feeds, it opened a gap between the arrowhead and the thing the arrow points at. **A drawing with a gap
  after the arrowhead says nothing arrives.** The connector inside the group takes the cap (10 × the unit)
  as its *basis* instead of growing into it, so it matches a grown sibling arrow rather than rendering as
  the one short stub in the lane.
- **An odd fan puts one leg on the trunk, and nothing in CSS fixes that.** With three inputs the middle
  one is collinear with the outgoing connector, because the axis *is* its centre line — the same
  collinearity the symmetric `Branch` was built to remove, reappearing for the arithmetic reason symmetry
  cannot help with an odd count. What carries the reading instead is the stem: three arms off one visible
  vertical bus read as three taps, not as a through-line with two brackets. Prefer even fans where the
  content allows; where it does not, check it with a stripped read rather than assuming.

## 12 · The icon register

Thirty-eight assets: thirty base objects and eight badges. **The convention column is the
load-bearing one** — it is what stops the next person redrawing `database` as a plain cylinder.
Blind-naming rounds are recorded because a pass is evidence, not an opinion. Sourcing and licence:
`icons/NOTICE.md`.

| Icon | Depicts | Convention drawn | Source | Blind verdict |
|---|---|---|---|---|
| `document` | a record | folded-corner page + text lines | Tabler | R1 pass |
| `documentStack` | many records | offset copies of the page | Tabler | R1 pass |
| `spreadsheet` | tabular data | page with a **cell grid** | Tabler | R1 fail as a bare grid, R2 pass |
| `mixedSources` | **a heterogeneous corpus** — sources of different kinds, not many copies of one | two offset folded-corner pages whose **interiors differ**: four solid cells on the back sheet, text lines on the front. The difference between the sheets is the whole meaning, so both folds stay clear of the overlap | hand | R6 pass (*"two documents of different kinds… a mixed-format corpus"*), R7 pass after the cells were redrawn as solid blocks; mushy at 40 px — see the near-miss table |
| `chunkedPage` | **layout-aware chunking** | one page whose interior is **four unequal blocks with wide gutters** — a header bar, a tall column, two stacked blocks — instead of uniform text lines. Structure, not content, is what is drawn | hand | R6 first read *"a bar chart in a document"* → redrawn; R7 pass (*"document layout / page structure / layout-aware parsing"*) **with a recorded residual**: it draws *layout*, not *the act of splitting* |
| `browserPage` | a web page | window with a **chrome bar** | Tabler | R1 pass |
| `database` | a store | **stacked discs** — the separations are the meaning | Tabler | R1 pass |
| `clipboard` | a checklist | board with a clip | Tabler | R1 pass |
| `calendar` | a schedule | grid page with two hangers | Tabler | R1 pass |
| `codeFile` | code | page with angle brackets | Tabler | R1 pass |
| `dashboard` | monitoring | monitor + bar chart | Tabler | R1 pass |
| `sliders` | tuning | rails with knobs | Tabler | R1 pass |
| `magnifier` | search | lens + handle | Tabler | R1 pass |
| `retrieval` | **searching a corpus** — the act, not the corpus | offset pages **plus a magnifier over their lower-right**, the page fill cut back in a circle so the magnifier reads as being in front | hand | R5 pass ("stack of documents with a magnifier — searching files"); mushy at 40 px |
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
| `gauge` | a threshold | semicircular dial, **half-disc hub sitting on the base line**, needle, and the threshold as a short **band on the rim** — concentric with the arc, never radial | hand | R1 pass; **redrawn R7** after two rounds called the old radial notch "a detached blue rod… the dial appears to have two needles" and the full-circle hub "knocked off its axis" |
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
| `documentStack` / `retrieval` | **the magnifier, and it is the whole difference** — see the usage rule below. At 40 px the stack in `retrieval` blurs and only the magnifier survives, so the pair separates reliably only at reading size or with its label |
| `documentStack` / `mixedSources` | **whether the two sheets are the same kind of thing.** Identical silhouette by design — that is the point, one corpus drawn two ways — and the only differentiator is the interior: `documentStack`'s sheets are blank, `mixedSources` puts a block of cells on one and text lines on the other. Recorded honestly: at 40 px the interiors go and a blind reader named `mixedSources` "copies / multiple documents", i.e. as `documentStack`. The pair separates at reading size only |
| `spreadsheet` / `chunkedPage` | **enclosed cells versus free-standing blocks.** `spreadsheet` puts one outlined grid on the page, with a cross of dividers inside it; `chunkedPage` puts four solid unequal blocks with wide gutters and no enclosing frame. Both are "a page with blue geometry inside", so this is the pair to watch when either is redrawn |
| `retrieval` / `magnifier` | whether anything is being searched. `magnifier` is the bare instrument — a search box, a lookup; `retrieval` is the instrument **over a corpus** |

### `documentStack` or `retrieval` — the usage rule

They are not interchangeable, and picking by feel is how a lexicon flattens:

- **`documentStack` is a noun.** A corpus, a set of documents, the sources — the *things*. Use it for
  an ingested collection, a chunk set, the passages handed to a generator.
- **`retrieval` is a verb.** The search *over* those documents — the step that goes and finds them.
  Use it for a retrieve node, a top-k step, a search call.

The test: if the node could be labelled "documents" it is `documentStack`; if it could be labelled
"find" it is `retrieval`. Card 02's `top-k, always` is a retrieval *policy*, so it is `retrieval` —
drawn with `documentStack` it said "documents", which is not what the node does.

### Residuals, recorded rather than hidden

`traceSpans`, `chainSteps`, `gate`, `branchSplit`, `retrieval`, `mixedSources` and `chunkedPage` all
blur at the 34 px a phone renders. None is used where the distinction is load-bearing without its
label. Treat this as a budget: **do not add another detailed icon** to a card that already leans on
one of these.

**Card 08 spends that budget, and it is recorded rather than hidden.** It carries `chainSteps` plus
three `gate`s — four detail-heavy icons on one card, all four mushy at phone width. It is defensible
only because the three gates are *the same object three times*, so nothing depends on telling them
apart: the `rank` ramp and the labels carry the ordering, and the icon only has to say "a gate".

**A fill path must be closed on purpose.** `documentStack`'s front sheet was filled from an *open*
path — right for a stroke that stops where the occlusion starts, wrong for a fill, because SVG closes
an open fill path with a straight chord. The chord ran corner to corner and painted half the front
sheet in the back sheet's tint; a blind reader read it as "the back sheet bleeding through the front
one — a z-order bug", which is exactly what it looked like. This is a general trap for every
two-object icon in the lexicon, so it belongs beside the paint-order rule in §13.

`retrieval` is the newest and the clearest case of the underlying cost: **a two-object icon buys
meaning at large sizes and spends legibility at small ones.** Each object gets about half the grid,
so each is drawn at half the detail budget of a single-object icon. Blind naming confirmed both
halves of that: at 120 px it fused into one idea, *"search documents"*; at 40 px the reader saw
*"something plus a magnifier"* — the magnifier survives because a circle with a stick is almost
irreducible, the page stack does not. Accept the trade only where the second object **is** the
concept (here: without the magnifier the node says "documents", which is the wrong claim).

## 13 · Sizing and geometry — hard numbers

A set stays coherent because everything sits on one grid. These are *the* values, not suggestions.

**The card's own lengths are no longer in `rem`, they are multiples of one unit `--ic-u`** (§16). The
"× card width" column is the canonical number; the pixel column is only what it resolves to on the
560px desktop card, and is shown so the two can be checked against each other.

| | × card width | On a 560px card |
|---|---|---|
| Icon viewBox | — | `0 0 48 48`, no `width`/`height` attributes (so svgo cannot drop the viewBox) |
| Stroke | — | effective width **3** in that grid, `stroke="currentColor"`, round cap and join |
| Vendored normalisation | — | upstream 24×24 paths kept verbatim inside `<g transform="scale(2)" stroke-width="1.5">` |
| Fills | — | `var(--ic-fill, #3b82f6)` and `var(--ic-tint, #93c5fd)` — **always with the literal fallback**, because non-browser rasterisers cannot resolve `var()` |
| Icon box `--ic-box` | **9.714** | `54.4px` |
| Badge | **4.286** — 44% of the icon box, now at every width | `24px` |
| Node pitch | **16.857** (`flex-basis` and `max-width`) | `94.4px` |
| Node label | **2.343** | `13.1px` |
| Title | **3.857** | `21.6px` |
| Lane pill | **1.943** | `10.9px` |
| Connector | **3.571** basis and definite `width`, min **3.143**, max **10** | `20 / 17.6 / 56px` |
| Connector offset | `calc(var(--fork-offset, 0px) + var(--ic-box) / 2 - var(--flow-h) / 2)` | — |
| Connector drawing height `--flow-h` | **1.786**, line on its midpoint (`y="50%"`), stroke **0.357** | `10px`, stroke `2px` |
| Branch row pitch | `--branch-row` **17.714**, `--branch-gap` **1.571** — fixed, because every number in the fork derives from it | `99.2 / 8.8px` |
| Card width | — | `560px` above 997px — the same cap as the generated cards, so both substrates sit at identical proportions |

Two of these are load-bearing for reasons that are not obvious:

- The connector needs a **definite `width`**, not only a basis — an `<svg>` with no viewBox
  contributes **300px** to flex line-breaking otherwise, which once broke card 02's branch onto a
  second row.
- The node pitch is a pitch, **not a minimum**: uniform node widths are also what stop two labels
  sharing a text line.

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

## 16 · Composed cards scale, they do not re-flow — with a legibility floor

**The rule.** A composed card is a **query container** (`container-type: inline-size` on `.card`) and
every length inside the diagram — icon box, node pitch, connector slot and its cap, gaps, paddings,
badge, stroke widths, dash rhythm, and all four type sizes — is a multiple of one unit:

```css
--ic-u: max(4.695px, 1cqw);   /* 1cqw = 1% of the card's width */
```

There is **exactly one breakpoint left in the component** (the 560px desktop cap on `.card`, kept so
a composed card and a raster one sit at identical proportions). The diagram itself has none, and must
not gain one: a media query inside the card re-introduces the defect this rule exists to remove.

**Why: a diagram's shape is part of its argument.** With lengths in `rem`, the drawing was a fixed
island — the same 477px of diagram inside a 964px card on a tablet and a 291px lane on a phone — so
its *proportions* changed with the viewport and, past a threshold, its *topology* did: card 06's
four-rung ladder broke into 3 + 1 and card 02's fork dropped to a second row with its incoming arrow
starting at the panel edge, aimed at nothing. A reader who has seen the desktop card and then the
phone card has seen two different diagrams. Measured, pure `1cqw` holds card 06 at an aspect ratio of
**1.50** and card 02 at **1.10** at every viewport from 1440 down to 360; the `rem` version ran
0.83 → 1.54.

**The tension, stated because it cuts against §4's label budget.** Proportional scaling shrinks type,
and the budget's floor — rendered type below **~11px** is unreadable at phone width — is
evidence-derived. A card designed for four nodes across 560px puts its labels at **8.4px** when
scaled to a 358px card (a 390px phone). A pure lock therefore trades re-flow for illegibility. Three
options were built and measured:

| | Shape | Node label at a 390px phone | Verdict |
|---|---|---|---|
| Pure `1cqw` | exactly constant at every width | **8.4px** — a blind reader transcribed every label but called it *"below the 11px line, marginal"*, and the 7px lane pills *"shape-recognition, not reading"* | **fails the floor** |
| Lock geometry, floor the type at 11px | horizontally constant | 11px, but the label no longer fits its proportionally-shrunk column: measured mid-word breaks — `confiden/t`, `retriev/al`, `re-/index` | **fails — breaks words** |
| **Floor the unit** (shipped) | constant above the floor, re-flows below it | 11px | **shipped** |

So: **scale proportionally down to the legibility floor, and allow the old re-flow only below it.**
The floor is derived, not chosen — `11px ÷ 2.343` (the label's multiplier, §13) `= 4.695px`. Measured
consequences of that number: the lock holds exactly for a card **≥ 478px** (a viewport ≥ ~510px);
between 458 and 478px the unit is pinned but the lane still fits on one line; **below a 458px card
(a viewport below ~490px) the lane wraps**, as it did before. Invariant across the range that
matters, graceful past it.

**Recorded honestly: a phone still gets the re-flow, and this is why.** At a 358px card you can have
an 11px label *or* an unwrapped four-node lane, not both — the two are mutually exclusive at these
proportions, and the arithmetic says so: the lane needs 82.4 × the unit and the panel offers
85.2 × the card's percent, so the moment the unit is pinned above `1cqw` the lane no longer fits.

**The lever that would move the floor, for whoever takes it further.** The composed card's label
column is **14.86 × card width**; the generated cards' labels are ~**3.0 × card width** in size
against the composed card's 2.343, and they get away with it because a raster label may run *under*
the arrow — the arrow lives on the icon centre line and the label sits below it. In the composed
card the connector reserves a **full-height flex column**, so the label is capped at the node pitch
minus its padding. Letting labels extend under the connector slot would widen the column to
~20 × card width, admit a 3.0 label multiplier (raster parity, ~17px on the desktop card), and drop
the floor to roughly a 355px card — i.e. **a full lock that stays legible on a phone**. It is not
done here because it re-opens the "two labels sharing a text line" defect that the uniform pitch was
introduced to close, and that needs its own blind read.

## 17 · `Grid` — the shape for peers

A lane is a claim about **flow**. Some content has none: card 09's four failures are a *set* — no first,
no last, nothing leading to anything. Drawing them in a lane would have been the same category of error
as putting `rank` on peers (§10 rule 4), just committed with position instead of colour.

| Channel | On a `Grid` | Why |
|---|---|---|
| Connectors | **none** | nothing flows between peers |
| `rank` | **never** | a gradient asserts an order that does not exist |
| Columns | **two, at every width** | a row of four is read left to right and reads as a sequence *even with no arrows in it*. A 2×N block reads as a set. The column count is therefore part of the argument, not a layout preference, so it does not respond to the viewport (§16) |
| Panel | **one per peer**, `tone="fail"` or `"ok"` | a shared container is itself a claim — that these belong to one pipeline or one stage. Separate panels say "four independent things" |
| Node width | fills its cell | the uniform pitch (§13) exists to stop two labels in a row sharing a text line; inside a cell the panel border *is* the gutter, so a long label stays on one line instead of wrapping in a half-empty box |

**`tone` is a separate prop from `Lane`'s `kind`, deliberately.** A grid has no demo-vs-production
contrast to encode, so authoring these cells as `kind="demo"` would be false in the markup even though
it resolves to the same hue. Two vocabularies is the smaller cost.

Everything else is unchanged: the same unit, the same icon box, the same badge grammar, the same label
budget, one labelled node per cell.

**A `Grid` card will always look like a list, and that is not grounds to cut it.** Card 09 was charged with
exactly that — *"it would render identically as a plain bulleted list, so the diagram is doing no work"* —
and kept by the owner on 2026-07-27. The card and the prose serve **different reading modes**: the grid is
the glance, the four paragraphs underneath are the detail. `create-infographic` §1b carries the refined
test — *does it add anything **at a glance***, not *could its content also be written as a list* — and card
09 is its worked example.
