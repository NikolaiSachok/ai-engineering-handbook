#!/usr/bin/env python3
"""Build a local review page for one infographic card set.

Usage:  python3 scripts/infographic-review.py <page-slug> [--open]

Reads every image in `static/img/infographics/<page-slug>/`, and writes a throwaway
`infographic-review-<page-slug>.html` into the system temp dir — never into the repo, because the
page embeds absolute `file://` paths and `scripts/leak-scan.sh` scans the whole tree. It shows each card:

  * at article width, on the LIGHT page ground and on the DARK page ground — cards are
    deep-slate by design (see editorial/infographics/STYLE.md §2), so both grounds must be checked;
  * at 360 CSS px, the phone width the label budget in STYLE.md §3 is derived from.

This mechanises the "phone test" in the STYLE.md §7 verification checklist. It is a review
tool only — nothing here ships.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
EXTS = {".webp", ".png", ".jpg", ".jpeg", ".avif"}


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if not args:
        sets = sorted(p.name for p in (REPO / "static/img/infographics").glob("*") if p.is_dir())
        print(f"usage: {sys.argv[0]} <page-slug> [--open]\nknown sets: {', '.join(sets) or '(none)'}")
        return 2

    slug = args[0]
    # Either a card-set slug under static/img/infographics/, or any directory path —
    # the latter lets you review candidate variants straight out of a scratch dir.
    card_dir = Path(slug).expanduser() if "/" in slug else REPO / "static/img/infographics" / slug
    if not card_dir.is_dir():
        print(f"no such card set: {card_dir}")
        return 1
    slug = card_dir.name

    cards = sorted(p for p in card_dir.iterdir() if p.suffix.lower() in EXTS)
    if not cards:
        print(f"no images in {card_dir}")
        return 1

    blocks = []
    for card in cards:
        # Absolute src so the page works whether the cards live in the repo or a scratch dir.
        rel = card.resolve().as_uri()
        kb = card.stat().st_size / 1024
        over = ' <b class="warn">over 200 KB</b>' if kb > 200 else ""
        blocks.append(f"""
    <section>
      <h2>{card.name} <span class="meta">{kb:.0f} KB{over}</span></h2>
      <div class="row">
        <figure class="ground-light">
          <figcaption>light page ground &middot; article width</figcaption>
          <img src="{rel}" alt="{card.stem} on a light ground">
        </figure>
        <figure class="ground-dark">
          <figcaption>dark page ground &middot; article width</figcaption>
          <img src="{rel}" alt="{card.stem} on a dark ground">
        </figure>
      </div>
      <div class="row">
        <figure class="ground-light phone">
          <figcaption>360px &mdash; phone test</figcaption>
          <img src="{rel}" alt="{card.stem} at phone width">
        </figure>
        <figure class="ground-dark phone">
          <figcaption>360px &mdash; phone test</figcaption>
          <img src="{rel}" alt="{card.stem} at phone width">
        </figure>
      </div>
    </section>""")

    html = f"""<!doctype html>
<meta charset="utf-8">
<title>Infographic review — {slug}</title>
<style>
  :root {{ color-scheme: light dark; --ink:#1a2230; --muted:#5d6b7d; }}
  body {{ margin:0; padding:2rem clamp(1rem,4vw,3rem); background:#e9edf2; color:var(--ink);
         font:16px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif; }}
  header {{ max-width:70ch; margin:0 auto 2.5rem; }}
  h1 {{ font-size:1.5rem; margin:0 0 .4rem; }}
  header p {{ color:var(--muted); margin:0; }}
  code {{ background:#dfe4ea; padding:.1em .35em; border-radius:3px; font-size:.9em; }}
  section {{ max-width:1400px; margin:0 auto 3rem; }}
  h2 {{ font-size:1rem; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-weight:600;
        border-bottom:1px solid #cfd6de; padding-bottom:.5rem; margin:0 0 1rem; }}
  .meta {{ font-weight:400; color:var(--muted); }}
  .warn {{ color:#b42318; }}
  .row {{ display:flex; flex-wrap:wrap; gap:1.25rem; margin-bottom:1.25rem; align-items:flex-start; }}
  figure {{ margin:0; flex:1 1 380px; border-radius:10px; padding:1.25rem; border:1px solid #cfd6de; }}
  figure.phone {{ flex:0 0 auto; }}
  figure.phone img {{ width:360px; }}
  .ground-light {{ background:#fff; }}
  .ground-dark  {{ background:#1b1b1d; border-color:#33353a; }}
  .ground-dark figcaption {{ color:#9aa4b2; }}
  figcaption {{ font-size:.78rem; letter-spacing:.03em; text-transform:uppercase; color:var(--muted);
                margin-bottom:.75rem; }}
  img {{ display:block; width:100%; height:auto; border-radius:8px; }}
</style>
<header>
  <h1>Infographic review — {slug}</h1>
  <p>{len(cards)} card(s). Check each against the checklist in
     <code>editorial/infographics/STYLE.md</code> §7: every label letter by letter, no invented text,
     nothing clipped, palette compliance, and readable at 360px.</p>
</header>
{"".join(blocks)}
"""

    # Written OUTSIDE the repo, deliberately. The page embeds absolute file:// paths, and
    # scripts/leak-scan.sh greps the entire working tree (not the git index), so a review page
    # sitting in the repo root trips the local-path rule even while gitignored.
    out = Path(tempfile.gettempdir()) / f"infographic-review-{slug}.html"
    out.write_text(html, encoding="utf-8")
    print(out)
    if "--open" in sys.argv[1:]:
        subprocess.run(["open", str(out)], check=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
