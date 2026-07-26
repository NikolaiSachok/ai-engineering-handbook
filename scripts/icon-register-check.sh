#!/usr/bin/env bash
#
# Drift check: the icon assets and the canon's icon register must agree, both ways.
#
# The icons live in src/components/InfoCard/icons/ because they have to: theme adaptation and the
# `rank` ramp need the SVG inline in the DOM so it inherits `currentColor`, which means an importable
# module under src/. The canon (editorial/infographics/STYLE.md §12) holds the rules and the
# per-icon convention. That split is deliberate — but it means the two can drift, so this asserts
# they do not: every asset has a register row, every register row has an asset.
#
# Deliberately dumb: a name-set diff, not a parser. It runs in CI beside the other gates.
#
# Exit code: 0 if they agree, 1 otherwise.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

ICON_DIR="src/components/InfoCard/icons"
CANON="editorial/infographics/STYLE.md"

assets="$(mktemp)"
register="$(mktemp)"
trap 'rm -f "$assets" "$register"' EXIT

# Base objects only. Badges have their own table and their own directory.
find "$ICON_DIR" -maxdepth 1 -name '*.svg' -exec basename {} .svg \; | sort >"$assets"

# Only the base-object table in §12 counts: badges have their own table and their own directory,
# and the rank table also uses backticked first cells. Take rows between the §12 heading and the
# next sub-heading, then the first cell of each.
awk '/^## 12 /{inside=1; next} inside && /^#/{exit} inside' "$CANON" \
  | grep -oE '^\| `[a-zA-Z]+` \|' | tr -d '|` ' | sort -u >"$register"

missing_row="$(comm -23 "$assets" "$register")"
missing_file="$(comm -13 "$assets" "$register")"

status=0

if [ -n "$missing_row" ]; then
  echo "icon-register-check: FAIL — asset with no row in $CANON §12:"
  echo "$missing_row" | sed 's/^/  - /'
  echo "  Add its row, including the convention it draws and its blind-naming verdict."
  status=1
fi

if [ -n "$missing_file" ]; then
  echo "icon-register-check: FAIL — register row with no asset in $ICON_DIR:"
  echo "$missing_file" | sed 's/^/  - /'
  echo "  Either the icon was deleted and the row is stale, or the row names it wrongly."
  status=1
fi

if [ "$status" -eq 0 ]; then
  echo "icon-register-check: PASS — $(wc -l <"$assets" | tr -d ' ') icons, all registered."
fi

exit "$status"
