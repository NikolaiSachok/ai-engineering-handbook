# Icon lexicon — provenance and licence

Thirty-seven assets: twenty-nine base objects and eight overlay badges. Sourcing is **hybrid** —
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
| `speechBubbleEmpty` | `message-2`, interior text lines replaced by a single dash — an answer with nothing in it |
| `speechBubbleGroup` | `messages` |
| `globe` | `world` |
| `plug` | `plug` |
| `chip` | `cpu` |
| `cloud` | `cloud` |
| `coins` | `coins`, painted in `var(--ic-coin, #f0b429)` |
| `lockOpen` | `lock-open` |

Three of these were re-sourced *because the blind-naming gate caught them*, which is the whole point
of running it: `spreadsheet` drawn as Tabler `table` was named "table / grid layout" and confused with
`browserPage`; `coins` was named as a possible second `database`, both being stacked ellipses, and was
fixed with colour rather than geometry — value/cost amber is the one palette exception STYLE.md
already allowed.

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
| `gauge` | a semicircular dial with a hub and needle, and a **radial notch crossing the arc** in the accent hue: the marked threshold |
| `funnel` | the plain filter funnel — kept separate from `gate` on purpose |
| `gate` | a boom barrier: post, base, and a striped arm. The plan asked for one *gate-beside-a-funnel* asset; two objects in one 48 grid failed the phone test, so it is two assets, and `funnel` was on the lexicon's own gap list anyway |
| `branchSplit` | a flow that splits: one path continues right, the other drops, routes back left and re-enters with an upward arrowhead — canary out, rollback home |
| `chainSteps` | linked rounded squares, links in the accent hue. **Three, not the four the plan asked for** — four squares inside 48 px at stroke 3 leaves 5 px of interior each and reads as noise |
| `sortedList` | rows of decreasing length with a descending arrow, the top row in the accent hue: the ranked list |
| `traceSpans` | three spans staggered left-to-right over a ticked time axis: the trace waterfall. **This icon cost three rounds of the blind gate.** As nested spans on a shared centre it read as "cascading pills… a lamp"; redrawn as dots on a line it read as "three pins… tuning knobs"; the staggered-spans version reads as "waterfall", which is the observability convention for a trace — so the *concept* was renamed from `timeline` to match what the drawing actually says |
| `speechBubbleEmpty` | the message bubble with a single dash where its text lines would be: an answer containing nothing. Pair it with a tick badge when the empty answer is the *correct* outcome, or the dash reads as "muted" |

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
