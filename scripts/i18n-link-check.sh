#!/usr/bin/env bash
#
# i18n link + anchor gate for the unreleased-inclusive build.
#
# Context. `onBrokenLinks` and `onBrokenAnchors` throw for released (deployed) builds but
# only warn when HANDBOOK_INCLUDE_UNRELEASED=1 (see docusaurus.config.ts). The reason is
# one class of link that gated partial translation makes unavoidable and that never ships:
# an untranslated fallback lesson (served from `docs/` in the unreleased locale) links to
# the glossary via a relative `.md` path; once the glossary alone is translated,
# Docusaurus cannot path-match that link across the `docs/` (fallback) and
# `i18n/<locale>/` (translated) trees — and the localized slug wouldn't match the EN
# one anyway — until the lesson itself is translated. Those links resolve correctly in
# every deployed build.
#
# This gate keeps CI strict everywhere else. It runs the unreleased-inclusive build and
# FAILS on any broken link OR broken anchor whose source page is NOT such a tolerable
# fallback, i.e.:
#   - any broken link/anchor in a released locale — real, shipping breakage; and
#   - any broken link/anchor on a page that IS translated in an unreleased locale — a
#     real defect in authored content (e.g. a freshly translated lesson whose
#     terms-footer points at a wrong glossary slug).
# It is tolerated ONLY when the source is an unreleased-locale page that has no
# translation file yet (a pure EN fallback). The gate self-maintains as locales fill
# in: the day a lesson is translated, its links must resolve or this gate fails.
#
# Usage:
#   scripts/i18n-link-check.sh              # from repo root; runs the build itself
#   scripts/i18n-link-check.sh --self-test  # exercise the classifier only, no build

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Unreleased locales that may legitimately carry EN-fallback pages. Keep in sync with
# UNRELEASED_LOCALES in docusaurus.config.ts (single source of truth would be nicer,
# but the config is TS; this list is small and changes once per locale launch).
UNRELEASED_LOCALES=(de)  # sk launched 2026-07-15; de scaffolded 2026-07-28 (translation in progress)

I18N_DOCS_ROOT="${I18N_DOCS_ROOT:-i18n}" # i18n/<locale>/<plugin-dir>/current/<docpath>

# --- URL → translation-file mapping, DERIVED (never restated) ---------------------------
#
# A doc URL is `<baseUrl><locale>/<routeBasePath>/<docpath>` while its translation file is
# `i18n/<locale>/<plugin-dir>/current/<docpath>`. The two differ by the course's routeBasePath,
# which exists in the ROUTES and nowhere in the file tree — and each routeBasePath belongs to a
# DIFFERENT plugin dir. Getting that mapping from `scripts/courses.py`, which reads the COURSES
# array in docusaurus.config.ts, is the whole point: hard-coding it is what broke this gate
# (#307 — the prefix was never stripped and only the first course's dir was ever consulted, so
# every unreleased-locale page classified as an untranslated fallback and the gate was a no-op
# exactly where it was supposed to bite). A third course must not need an edit here.
#
# The table's fourth column is the course's declared locales. This gate deliberately does
# NOT scope itself by it, and the reason is worth stating because the parity gate does the
# opposite. Parity asks "should a translation exist here?" — a question only the course can
# answer. This gate asks "does this link resolve for a reader?" — and a reader of an
# English-only course under /ru/ is being served real, shipping content. A broken link on
# that page is broken for them. Tolerating it because the course is not translated would
# weaken the gate to buy nothing: the pages are uniform EN in every locale, so they cannot
# produce the split-tree fallback breakage the tolerance above exists for. The column is
# read only so the field split stays correct as columns are added.
COURSE_BASES=()
COURSE_I18N_DIRS=()
while IFS=$'\t' read -r _base _docs _i18n _locales; do
  [ -n "$_base" ] && COURSE_BASES+=("$_base") && COURSE_I18N_DIRS+=("$_i18n")
done < <(python3 scripts/courses.py)
if [ "${#COURSE_BASES[@]}" -eq 0 ]; then
  echo "i18n-link-check: FAIL — could not derive the course table from docusaurus.config.ts."
  echo "Refusing to run: with no course table every page would classify as a tolerable fallback."
  exit 1
fi

# Is the source page an unreleased-locale page with no translation file (a fallback)?
#
# Fails CLOSED throughout: a URL under an unreleased locale that matches no course prefix (the
# landing hub, the EN-only blog, a course added to the routes but not to COURSES) is reported,
# never exempted. An unmapped route becoming a blanket exemption is the failure mode this
# function exists to avoid.
is_tolerable_fallback() {
  local src="$1" loc rest base i18n_dir docpath f ext i
  for loc in "${UNRELEASED_LOCALES[@]}"; do
    # Match ".../<loc>/<rest>" anywhere in the source URL (baseUrl-agnostic).
    [[ "$src" == *"/$loc/"* ]] || continue
    rest="${src##*/$loc/}"   # `<routeBasePath>/<docpath>` — still carrying the course prefix
    rest="${rest%/}"         # trim trailing slash
    for i in "${!COURSE_BASES[@]}"; do
      base="${COURSE_BASES[$i]}"
      i18n_dir="${COURSE_I18N_DIRS[$i]}"
      if [ "$rest" = "$base" ]; then
        docpath="intro"                 # the course root: its intro page carries `slug: /`
      elif [[ "$rest" == "$base/"* ]]; then
        docpath="${rest#"$base"/}"
      else
        continue
      fi
      f="$I18N_DOCS_ROOT/$loc/$i18n_dir/current/$docpath"
      # Translated iff a matching file exists → NOT a tolerable fallback.
      for ext in ".md" ".mdx" "/index.md" "/index.mdx"; do
        [ -f "$f$ext" ] && return 1
      done
      return 0
    done
    return 1 # unreleased locale, but no course owns this route → fail closed
  done
  return 1 # not an unreleased-locale page → never tolerable (released content)
}

# Is this URL under an unreleased locale at all? (Cheap guard so the target-side tolerance
# below can never touch a released locale's links.)
is_unreleased_page() {
  local src="$1" loc
  for loc in "${UNRELEASED_LOCALES[@]}"; do
    [[ "$src" == *"/$loc/"* ]] && return 0
  done
  return 1
}

# Normalise a `resolved as:` target to the shape is_tolerable_fallback() expects: drop the
# anchor and the `.md`/`.mdx` suffix, leaving `<baseUrl><locale>/<routeBasePath>/<docpath>`.
normalise_target() {
  local t="${1%%#*}"
  t="${t%.md}"; t="${t%.mdx}"
  printf '%s' "$t"
}

# Is this broken link tolerable — judged on the PAIR, not on the source alone?
#
# The source-only rule (is_tolerable_fallback) covers an untranslated page linking anywhere. It
# does NOT cover the case that every locale must pass through exactly once: the FIRST translated
# lesson, whose in-body links point at siblings and a glossary that are still untranslated. Those
# links cannot resolve — Docusaurus path-matches across the `docs/` fallback and `i18n/<locale>/`
# trees, and the target simply has no file yet — so the gate would fail on the first correct page
# of every locale and stay failing until the whole course landed in one commit. The gate's own
# header promises it "self-maintains as locales fill in"; without this it self-maintains only at
# 0 % and 100 %.
#
# The tolerance is deliberately narrow and does NOT reopen #307's fail-open. It requires BOTH:
#   - the source page is in an unreleased locale, AND
#   - the TARGET is itself an untranslated page of that same unreleased locale.
# So the moment the target IS translated, a link into it must resolve or this fails — which is
# exactly the class the gate was written to catch (a freshly translated lesson pointing at a wrong
# glossary slug still fails, because the glossary file exists). A target in a released locale, an
# unmapped route, or an external path is never tolerable: is_tolerable_fallback fails closed on all
# three.
is_tolerable_pair() {
  local src="$1" target="$2"
  is_tolerable_fallback "$src" && return 0          # untranslated source — the original rule
  is_unreleased_page "$src" || return 1             # released locale — never tolerable
  [ -n "$target" ] || return 1                      # no target parsed — fail closed
  is_tolerable_fallback "$(normalise_target "$target")"
}

# --- self-test ---------------------------------------------------------------------------
#
# A gate that has only ever been seen to PASS proves nothing. #307 survived because the
# corpus it guards happened to contain no case that would expose it: the mapping was broken
# for EVERY unreleased-locale page, and with no such page yet translated the output was
# indistinguishable from a working gate. This asserts the classifier's verdicts against a
# synthetic i18n tree, so the mapping is exercised without a five-minute site build — the
# translated-page cases below are precisely the ones the old code got wrong.
self_test() {
  if [ "${#UNRELEASED_LOCALES[@]}" -eq 0 ]; then
    echo "i18n-link-check --self-test: SKIP — no unreleased locales; the classifier is inert."
    return 0
  fi
  local loc="${UNRELEASED_LOCALES[0]}" rel="" cand
  for cand in en ru sk; do
    if ! printf '%s\n' "${UNRELEASED_LOCALES[@]}" | grep -qx "$cand"; then rel="$cand"; break; fi
  done
  [ -n "$rel" ] || { echo "i18n-link-check --self-test: SKIP — no released locale to sample."; return 0; }

  local root base_a base_b dir_a dir_b second=0
  root="$(mktemp -d)"
  # The second course is the case #307 missed entirely; fall back to the first if a future
  # config ever declares only one, so the self-test degrades rather than lying.
  [ "${#COURSE_BASES[@]}" -gt 1 ] && second=1
  base_a="${COURSE_BASES[0]}";      dir_a="${COURSE_I18N_DIRS[0]}"
  base_b="${COURSE_BASES[$second]}"; dir_b="${COURSE_I18N_DIRS[$second]}"

  mkdir -p "$root/$loc/$dir_a/current/part-x/lesson" "$root/$loc/$dir_b/current/part-y"
  : > "$root/$loc/$dir_a/current/translated.md"
  : > "$root/$loc/$dir_a/current/part-x/lesson/index.md"
  : > "$root/$loc/$dir_b/current/part-y/translated.md"

  # `<source page url>|<expected verdict>` — verdict is `tolerable` or `reported`.
  local cases=(
    "/hb/$loc/$base_a/translated|reported"          # translated, course 1 — #307's blind spot
    "/hb/$loc/$base_b/part-y/translated|reported"   # translated, course 2 — never even looked at
    "/hb/$loc/$base_a/part-x/lesson/|reported"      # translated as <dir>/index.md
    "/hb/$loc/$base_a/part-x/absent|tolerable"      # untranslated → EN fallback
    "/hb/$loc/$base_b/part-y/absent|tolerable"      # untranslated, course 2
    "/hb/$loc/$base_a/|tolerable"                   # course root, intro not translated
    "/hb/$loc/blog/some-post|reported"              # no course owns it → fail closed
    "/hb/$loc/|reported"                            # the landing hub, not a doc
    "/hb/$rel/$base_a/part-x/absent|reported"       # released locale → never tolerable
  )

  # `<source url>::<resolved target>|<expected verdict>` for the PAIR classifier. These are the
  # cases the source-only rule cannot express: a translated page is always "reported" on its own,
  # so whether its link is tolerable turns entirely on the target.
  local pair_cases=(
    # first translated lesson → untranslated sibling / glossary: the case every locale hits once
    "/hb/$loc/$base_a/part-x/lesson/::/hb/$loc/$base_a/glossary.md|tolerable"
    "/hb/$loc/$base_a/part-x/lesson/::/hb/$loc/$base_a/part-x/absent/index.md|tolerable"
    "/hb/$loc/$base_a/part-x/lesson/::/hb/$loc/$base_a/glossary.md#some-anchor|tolerable"
    # target IS translated → a wrong slug/anchor, the defect this gate exists for
    "/hb/$loc/$base_a/part-x/lesson/::/hb/$loc/$base_a/translated.md#wrong|reported"
    "/hb/$loc/$base_a/part-x/lesson/::/hb/$loc/$base_a/part-x/lesson/index.md|reported"
    # cross-course target, untranslated → still tolerable (course 2 must be mapped too)
    "/hb/$loc/$base_a/part-x/lesson/::/hb/$loc/$base_b/part-y/absent.md|tolerable"
    # released-locale source → never tolerable, whatever the target
    "/hb/$rel/$base_a/part-x/lesson/::/hb/$rel/$base_a/glossary.md|reported"
    # target outside any unreleased locale, or unparseable → fail closed
    "/hb/$loc/$base_a/part-x/lesson/::/hb/$rel/$base_a/glossary.md|reported"
    "/hb/$loc/$base_a/part-x/lesson/::|reported"
    # untranslated source stays tolerable regardless of target (the original rule still applies)
    "/hb/$loc/$base_a/part-x/absent::/hb/$loc/$base_a/translated.md|tolerable"
  )

  local url want got failures=0 line total=0
  local saved_root="$I18N_DOCS_ROOT"
  I18N_DOCS_ROOT="$root"
  for line in "${cases[@]}"; do
    url="${line%%|*}"; want="${line##*|}"
    if is_tolerable_fallback "$url"; then got="tolerable"; else got="reported"; fi
    if [ "$got" = "$want" ]; then
      printf '  ok    %-46s %s\n' "$url" "$got"
    else
      printf '  FAIL  %-46s want=%s got=%s\n' "$url" "$want" "$got"
      failures=$((failures + 1))
    fi
    total=$((total + 1))
  done
  local pair src_url tgt_url
  for line in "${pair_cases[@]}"; do
    pair="${line%|*}"; want="${line##*|}"
    src_url="${pair%%::*}"; tgt_url="${pair#*::}"
    if is_tolerable_pair "$src_url" "$tgt_url"; then got="tolerable"; else got="reported"; fi
    if [ "$got" = "$want" ]; then
      printf '  ok    %-46s -> %-42s %s\n' "$src_url" "${tgt_url:-<none>}" "$got"
    else
      printf '  FAIL  %-46s -> %-42s want=%s got=%s\n' "$src_url" "${tgt_url:-<none>}" "$want" "$got"
      failures=$((failures + 1))
    fi
    total=$((total + 1))
  done
  I18N_DOCS_ROOT="$saved_root"
  rm -rf "$root"

  echo ""
  if [ "$failures" -eq 0 ]; then
    echo "i18n-link-check --self-test: PASS — $total classifier case(s)."
    return 0
  fi
  echo "i18n-link-check --self-test: FAIL — $failures of $total classifier case(s)."
  return 1
}

if [ "${1:-}" = "--self-test" ]; then
  self_test
  exit $?
fi

LOG="$(mktemp)"
trap 'rm -f "$LOG"' EXIT

echo ">> Classifier self-test…"
self_test || exit 1

echo ">> Building with unreleased locales included (onBrokenLinks: warn)…"
HANDBOOK_INCLUDE_UNRELEASED=1 npm run build 2>&1 | tee "$LOG"
BUILD_STATUS="${PIPESTATUS[0]}"

if [ "$BUILD_STATUS" -ne 0 ]; then
  echo "i18n-link-check: FAIL — build errored (exit $BUILD_STATUS), not a broken-link warning."
  exit "$BUILD_STATUS"
fi

# Docusaurus reports one `Broken link/anchor on source page path = <src>:` header followed by one
# or more `-> linking to <raw> (resolved as: <target>)` lines. Judging the SOURCE alone cannot
# express the first-translated-lesson case (see is_tolerable_pair), so flatten the log into
# `<src>::<target>` PAIRS and judge each. A header with no parsable target yields an empty target,
# which is_tolerable_pair rejects — the parser fails closed if Docusaurus ever changes its format.
PAIRS=()
while IFS= read -r line; do
  [ -n "$line" ] && PAIRS+=("$line")
done < <(awk '
  /Broken (link|anchor) on source page path = / {
    src = $0
    sub(/^.*Broken (link|anchor) on source page path = /, "", src)
    sub(/:[[:space:]]*$/, "", src)
    seen = 0
    next
  }
  /-> linking to .*\(resolved as: / {
    if (src == "") next
    tgt = $0
    sub(/^.*\(resolved as: /, "", tgt)
    sub(/\).*$/, "", tgt)
    print src "::" tgt
    seen = 1
  }
' "$LOG")

REAL_BREAKS=()
TOLERATED=0
# `${PAIRS[@]+…}` guard, not a bare `"${PAIRS[@]}"`: under `set -u`, bash 3.2 (the macOS system
# bash) treats expanding an EMPTY array as an unbound variable and aborts. That is the
# zero-broken-links case, so the unguarded form made this gate fail exactly when it should pass —
# invisibly, because CI runs bash 5 where the bare form is fine.
for pair in ${PAIRS[@]+"${PAIRS[@]}"}; do
  src="${pair%%::*}"; tgt="${pair#*::}"
  if is_tolerable_pair "$src" "$tgt"; then
    TOLERATED=$((TOLERATED + 1))
  else
    REAL_BREAKS+=("$src -> $tgt")
  fi
done

# A header Docusaurus emitted but the parser produced no pair for is a parse failure, not a pass.
HEADERS="$(grep -cE 'Broken (link|anchor) on source page path = ' "$LOG" || true)"
if [ "$HEADERS" -gt 0 ] && [ "${#PAIRS[@]}" -eq 0 ]; then
  echo ""
  echo "i18n-link-check: FAIL — $HEADERS broken-link header(s) in the build log but 0 parsable"
  echo "targets. The log format changed; refusing to pass on an unread log."
  exit 1
fi

if [ "${#REAL_BREAKS[@]}" -gt 0 ]; then
  echo ""
  # One page can carry several broken items, so count the items and the pages separately —
  # "3 broken link(s)" over a list of 2 lines reads like the list lost something.
  PAGES="$(printf '%s\n' "${REAL_BREAKS[@]}" | sed 's/ -> .*//' | sort -u | wc -l | tr -d ' ')"
  echo "i18n-link-check: FAIL — ${#REAL_BREAKS[@]} broken link(s)/anchor(s) on $PAGES shipping / translated page(s):"
  printf '  - %s\n' "${REAL_BREAKS[@]}" | sort -u
  echo ""
  echo "Tolerated only when BOTH ends are an unreleased locale's untranslated content:"
  echo "an EN-fallback source page, or a translated page linking at a not-yet-translated target."
  exit 1
fi

echo ""
echo "i18n-link-check: PASS — build clean; $TOLERATED tolerated fallback link(s)/anchor(s) in unreleased locales, 0 real breaks."
