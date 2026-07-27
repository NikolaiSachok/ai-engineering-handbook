# Icon lexicon — provenance and licence

Thirty-eight assets: thirty base objects and eight overlay badges. Sourcing is **hybrid** —
generic objects are vendored from an established set, the domain metaphors no set ships are
hand-authored. The rationale is in `editorial/infographics/CSS-CARDS-PLAN.md`; this file is the
attribution record and the redraw instructions.

## House grid (both kinds obey it, so a vendored icon and a hand-authored one match in use)

| | Value |
|---|---|
| viewBox | `0 0 48 48` |
| Stroke | effective width **3** in that grid, `stroke="currentColor"`, round cap and join |
| Fills | `var(--ic-fill, #3b82f6)` (accent) and `var(--ic-tint, #93c5fd)` (body wash) |
| Fill layering | **all fills are painted before any stroke.** A later fill must never cover an earlier separation line — that is exactly what turned a hand-drawn `database` into a plain drum |
| Fill paths | **a fill path must be closed on purpose.** Where a stroke stops at an occlusion boundary its path is open, and that is correct for the stroke — but reusing it as a *fill* makes SVG close it with a straight chord. On `documentStack` the chord ran corner to corner and painted half the front sheet in the back sheet's tint; a blind reader read it as *"the back sheet bleeding through the front one — a z-order bug"*. It shipped through four review rounds. Give the fill its own explicitly closed path, tracing the hidden edge |
| Literal fallback | mandatory in every `var()`. ImageMagick and other non-browser rasterisers cannot resolve custom properties |
| No `width`/`height` attributes | so svgo cannot drop the `viewBox` |

## Vendored — Tabler Icons

- Source: <https://github.com/tabler/tabler-icons>, `icons/outline/*.svg`
- Licence: **MIT** (© 2020–present Paweł Kuna). Permission notice below.
- Method: the upstream 24×24 stroke paths are kept **verbatim**, wrapped in
  `<g transform="scale(2)" stroke-width="1.5">` to land on the 48 grid at the house weight, and a
  fill layer is added underneath by duplicating selected paths as fill-only silhouettes. Nothing is
  redrawn, so an upstream fix can be re-applied mechanically.

| Concept | Tabler icon |
|---|---|
| `document` | `file-text` |
| `documentStack` | `files` |
| `spreadsheet` | `file-spreadsheet` |
| `browserPage` | `browser` |
| `database` | `database` |
| `clipboard` | `clipboard-text` |
| `calendar` | `calendar` |
| `codeFile` | `file-code` |
| `dashboard` | `device-desktop-analytics` |
| `sliders` | `adjustments-horizontal` |
| `magnifier` | `search` |
| `scales` | `scale` |
| `speechBubble` | `message-2` |
| `mixedSources` | two offset folded-corner pages whose **interiors differ** — four solid cells on the back sheet, text lines on the front — because *heterogeneity* is the concept and a stack of identical sheets says the opposite (`documentStack` already owns that). Deliberately shares `documentStack`'s silhouette: same object, one claim about its contents. Three things were paid for here. The cells were first an **outlined grid**, which at this page size lands within a stroke-width of the page's own outline — a blind reader read the table as *"an unclipped shape that escaped its container"*; solid blocks need no interior and fit in a third of the space. The two pages' folds must both clear the overlap, or one of them fills with the other page's tint. And the residual is structural: at 40 px the interiors go and the icon is named *"copies / multiple documents"*, i.e. as `documentStack` — never use the pair unlabelled |
| `chunkedPage` | one page whose interior is **four unequal blocks separated by wide gutters** — a header bar, a tall column, two stacked blocks — rather than the uniform text lines of `document` or the enclosed cell grid of `spreadsheet`. The gutters are as wide as the thinnest block is tall, on purpose: a tighter first version read as *"a bar chart in a document"*. Recorded residual, and it is honest rather than fixable at this size: the icon draws **layout**, not **the act of splitting** — a blind reader named it *"document layout / page structure / layout-aware parsing"* and then said plainly that it conveys *"a page that happens to have layout"*. The label supplies "chunking"; the icon supplies "layout-aware" |
| `speechBubbleEmpty` | `message-2` body, interior text lines removed |
| `speechBubbleGroup` | `messages` |
| `globe` | `world` |
| `plug` | `plug` |
| `chip` | `cpu` |
| `cloud` | `cloud` |
| `lockOpen` | `lock-open` |

Two of these were re-sourced *because the blind-naming gate caught them*, which is the whole point
of running it: `spreadsheet` drawn as Tabler `table` was named "table / grid layout" and confused with
`browserPage`, and was re-sourced to `file-spreadsheet`. `coins` left the vendored set entirely — see
below.

`lockOpen` is the concept the plan called `keyLock` ("a key beside an open padlock"). Two objects
inside a 48 grid are illegible at the 34 px a card actually renders, and an open padlock is the
stronger convention for *unscoped access*, so the concept was renamed to match the drawing rather
than the drawing bent to match the name.

## Hand-authored — the domain metaphors

No open set ships these, and a generic stand-in flattens the idea (the defect that made card 06's
drift node a monitor-with-bars). One line each on the convention being drawn, so the next person
extends the set consistently:

| Concept | Convention drawn |
|---|---|
| `driftCurves` | two bell curves on a shared baseline, the second offset right, the overlap shaded, plus a shift arrow — the reader must see *the distribution moved* before reading the label |
| `gauge` | a semicircular dial with a needle on a **half-disc hub sitting on the base rail's top edge**, and the threshold drawn as a short **band on the rim**, concentric with the arc, in the accent hue. **Redrawn 2026-07-27.** The original threshold was a *radial* notch crossing the arc, and two independent blind rounds read it the same way — *"a detached blue rod… the dial appears to have two needles"*, and at 40 px *"a sparkle"*. A mark that is meant to sit ON a line must be concentric with it and no heavier than it; radial says *pointer*. The hub was a full circle centred on the rail, so half of it hung below and the dial read as *"knocked off its axis"*; a half-disc on the rail's mid-line was then read as *"half-buried in the base bar"*, hence the top edge. Residual: at 40 px the rim band still reads as a highlight rather than a scale mark |
| `funnel` | the plain filter funnel — kept separate from `gate` on purpose |
| `gate` | a boom barrier drawn to the convention's three defining features: a **base plate**, a **vertical post**, and a **striped arm pivoting from the post's top** on a visible hinge. A first version had the arm but treated post and base as afterthoughts and read as "a slightly wrong parking barrier". The plan asked for one *gate-beside-a-funnel* asset; two objects in one 48 grid failed the phone test, so it is two assets, and `funnel` was on the lexicon's own gap list anyway |
| `coins` | **two overlapping coins seen face-on, with a currency mark**, in the value/cost amber. Vendored `coins` — three stacked discs seen edge-on — is *literally the database convention*, and a blind reader duly offered "database disks". Face-on plus a `$` removes the collision at the source: the next round named it "coins / money" |
| `branchSplit` | a flow that splits: one path continues right, the other drops, routes back left and re-enters with an upward arrowhead — canary out, rollback home |
| `chainSteps` | linked rounded squares, links in the accent hue. **Three, not the four the plan asked for** — four squares inside 48 px at stroke 3 leaves 5 px of interior each and reads as noise |
| `sortedList` | rows of decreasing length with a descending arrow, the top row in the accent hue: the ranked list |
| `traceSpans` | three spans staggered left-to-right over a ticked time axis: the trace waterfall. **This icon cost three rounds of the blind gate.** As nested spans on a shared centre it read as "cascading pills… a lamp"; redrawn as dots on a line it read as "three pins… tuning knobs"; the staggered-spans version reads as "waterfall", which is the observability convention for a trace — so the *concept* was renamed from `timeline` to match what the drawing actually says |
| `retrieval` | two offset pages **plus a magnifier over their lower-right** — the act of searching a corpus, not the corpus. `documentStack` is the noun, this is the verb (STYLE.md §12 holds the usage rule). The magnifier must read as being *in front of* the pages, and the fill-before-stroke rule forbids painting an opaque lens after the pages' outlines — so the occlusion is baked into the geometry instead: the front page's **fill path arcs around a circle of radius 12** concentric with the lens, and its outline stops short of that arc. No mask, no clip, no z-order trick; the hole is part of the path. Blind naming: *"stack of documents with a magnifier — searching files"* at reading size, *"something plus a magnifier"* at 40 px — recorded as a residual, never used unlabelled |
| `speechBubbleEmpty` | the message bubble with **nothing inside it at all** — emptiness is the meaning, so it is drawn as an absence rather than as a symbol for absence. Two candidates went through blind naming: this one read as *"empty speech bubble… nothing is in there"*; a variant carrying `∅` read as *"blocked / banned message"*, because a circle with a diagonal bar is the universal **prohibition** sign, not the empty set. An absence beats a glyph that means absence. Pair it with a tick badge when the empty answer is the *correct* outcome |

## Badges

Hand-authored. A filled disc in `currentColor` (so CSS sets the semantic hue) with a glyph in
`var(--ic-badge-ink, #ffffff)`: `tick` `cross` `padlock` `pin` `tag` `refresh` `crack`. `bang` is a
triangle rather than a disc, because the warning triangle is the convention. Semantics live in the
hue, set by `styles.module.css`: `tick` correct, `cross`/`bang`/`crack` failure, the rest neutral.

## MIT licence (Tabler Icons)

```text
MIT License

Copyright (c) 2020-2024 Paweł Kuna

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
