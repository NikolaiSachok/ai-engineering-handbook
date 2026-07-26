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

Cards are **light-ground**, chosen deliberately: it is the register of the reference poster, it gives the
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
| Coin / value fill | `240 180 41` | the one exception, on the cost card only |
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
