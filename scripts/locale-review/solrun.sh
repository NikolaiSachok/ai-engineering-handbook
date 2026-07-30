#!/usr/bin/env bash
#
# Run the Sol (cross-model) naturalness gate on ONE translated page.
#
# WHY THE INPUT IS ASSERTED BEFORE THE OUTPUT IS BELIEVED. The gate's input has now failed
# eight distinct ways across three German waves, and every single failure returned a
# confident, well-formed, useless result. Six of the eight are assertable here and are:
#
#   truncating   -> the judge fabricates verdicts about text it never saw;
#   narrowing    -> the judge fabricates ABSENCES ("this page is clean");
#   colliding    -> a shared scratch path returns verdicts about a DIFFERENT lesson;
#   silence      -> the model returned nothing at all and the run looks like a clean page;
#   brevity      -> a real, short work list looks like silence (see the floor, below);
#   shell-eaten  -> an invisible codepoint destroyed by shell quoting (see codepoints.py;
#                   that is why nothing here interpolates page text into a shell string).
#
# The remaining two are properties of a matcher rather than of this driver, and live where
# they can be asserted: a trailing-context matcher that drops the occurrence that mattered
# (concord.py), and a node-ID heuristic that ate a Mermaid label (mermaid_gate.py).
#
# usage: solrun.sh <page-path> <slug> [prompt-builder]
#        solrun.sh --self-test
#
# The optional third argument selects the prompt builder, so the same driver runs the prose
# gate and the Mermaid-label gate:
#        solrun.sh page.md pf                     # prose  (solprompt.py)
#        solrun.sh page.md pf-mermaid mermaid     # labels (mermaid_gate.py solprompt)
set -uo pipefail

S="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ---------------------------------------------------------------------------------------
# THE FLOOR — the fix for the brevity false positive.
#
# The guard exists to catch SILENCE. It must not fire on BREVITY. The original guard was a
# flat `blocks >= 5`, and it was wrong twice on the same ~250-word page: the model returned
# only its non-NATIV findings — 2 blocks, then 3 — and the driver exited non-zero and hid a
# real work list both times.
#
# What actually distinguishes the two conditions is NOT the block count. It is whether the
# call produced an answer at all, and those signals are asserted separately and
# unconditionally below: a non-empty raw file, a `codex` answer marker, and a non-empty
# extracted answer. If all three hold, the model DID answer, and an answer with two blocks
# on a short page is a result — a short work list is the expected shape of a good page.
#
# So the count is only ever used LENGTH-SCALED, and only ever to WARN:
#   * ZERO blocks and no explicit all-clear -> FAIL (this is the silence mode);
#   * ZERO blocks WITH an explicit all-clear -> PASS, zero is a legitimate verdict;
#   * below the scaled floor -> WARN and keep going; the caller reads the work list.
# The floor is one block per WORDS_PER_BLOCK words, which reproduces the old threshold of
# 5 on the ~2000-word page it was tuned for and asks for 1 on a 250-word page.
WORDS_PER_BLOCK=400

# The string the prompt names as the legitimate all-clean answer. A page really can be
# clean; the prompt says so explicitly, so the driver has to be able to recognise it.
ALLCLEAN_RE='(durchgehend nativ|alle Beschriftungen sind nativ|keine Beanstandung)'

floor_for() {  # floor_for <word-count> -> minimum blocks expected, at least 1
  local f=$(( $1 / WORDS_PER_BLOCK ))
  [ "$f" -lt 1 ] && f=1
  echo "$f"
}

# ---------------------------------------------------------------------------------------
if [ "${1:-}" = "--self-test" ]; then
  fails=0
  check() { # check <label> <got> <want>
    if [ "$2" = "$3" ]; then echo "  ok   $1 -> $2"
    else echo "  FAIL $1 -> got $2, want $3"; fails=$((fails+1)); fi
  }
  echo "solrun --self-test: the floor must scale with length, not sit at a constant"
  check "2000 words (the length the old flat 5 was tuned for)" "$(floor_for 2000)" 5
  check "3000 words"                                           "$(floor_for 3000)" 7
  check "250 words (the page the flat guard failed on, twice)" "$(floor_for 250)"  1
  check "40 words"                                             "$(floor_for 40)"   1
  check "0 words"                                              "$(floor_for 0)"    1
  echo "  -- a 250-word page must never be asked for 5 blocks:"
  if [ "$(floor_for 250)" -lt 5 ]; then echo "  ok   floor_for 250 < 5"
  else echo "  FAIL floor_for 250 is still >= 5"; fails=$((fails+1)); fi
  echo "  -- the all-clean recogniser must match the prompt's own wording:"
  for s in "Diese Seite ist durchgehend nativ." "Alle Beschriftungen sind nativ"; do
    if printf '%s' "$s" | grep -qiE "$ALLCLEAN_RE"; then echo "  ok   recognised: $s"
    else echo "  FAIL not recognised: $s"; fails=$((fails+1)); fi
  done
  if printf '%s' "ZITAT: etwas" | grep -qiE "$ALLCLEAN_RE"; then
    echo "  FAIL a verdict block was misread as an all-clear"; fails=$((fails+1))
  else echo "  ok   a verdict block is not an all-clear"; fi
  echo
  [ "$fails" -eq 0 ] && { echo "solrun --self-test: PASS"; exit 0; }
  echo "solrun --self-test: FAIL ($fails)"; exit 1
fi

[ "$#" -ge 2 ] || { echo "usage: solrun.sh <page-path> <slug> [prompt-builder] | --self-test"; exit 2; }
PAGE="$1"; SLUG="$2"; BUILDER="${3:-prose}"

# Owner-scoped, page-named output directory. A shared /tmp path once overwrote one
# renderer's prompt with another's and returned 24 confident verdicts about a different
# lesson; the slug in the path is what makes that collision impossible rather than unlikely.
OUT="${SOL_OUT_DIR:-$S/.sol-out}"
mkdir -p "$OUT"
P="$OUT/PROMPT-$SLUG.txt"
R="$OUT/RAW-$SLUG.txt"
A="$OUT/ANSWER-$SLUG.txt"
V="$OUT/VERDICTS-$SLUG.txt"

[ -f "$PAGE" ] || { echo "FAIL: page does not exist: $PAGE"; exit 2; }

case "$BUILDER" in
  prose)   python3 "$S/solprompt.py" "$PAGE" "$SLUG" > "$P" ;;
  mermaid) python3 "$S/mermaid_gate.py" solprompt "$PAGE" "$SLUG" > "$P" ;;
  *) echo "FAIL: unknown prompt builder: $BUILDER (want 'prose' or 'mermaid')"; exit 2 ;;
esac

# ---- INPUT ASSERTIONS -----------------------------------------------------------------
# Everything here is done in Python over the FILES. Nothing interpolates page text into a
# shell string: that is the eighth input failure (a `python3 -c` inside double quotes
# reported `U+202F: 0` on a file that contained it, because the shell ate the character).
python3 - "$PAGE" "$P" "$SLUG" "$BUILDER" <<'PY'
import sys, pathlib
page = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
prompt = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8")
slug, builder = sys.argv[3], sys.argv[4]
fail = []
lines = [l for l in page.split("\n") if l.strip()]

# The Mermaid builder legitimately carries only the EXTRACTED labels, not the whole page,
# so the verbatim-containment assertions apply to the prose builder only. What both share
# is the slug assertion and a plausible size.
if builder == "prose":
    if page not in prompt:
        fail.append("TRUNCATED/ALTERED — the page text is not verbatim inside the prompt")
    for label, l in (("first", lines[0]), ("last", lines[-1])):
        if l not in prompt:
            fail.append(f"NARROWED — the {label} line of the page is missing from the prompt")
    if len(prompt) < len(page) + 2000:
        fail.append(f"IMPLAUSIBLE SIZE — prompt {len(prompt)} vs page {len(page)}; preamble appears lost")
else:
    if len(prompt) < 2000:
        fail.append(f"IMPLAUSIBLE SIZE — prompt {len(prompt)}B; the preamble alone is longer than that")

if f"Seite: {slug}" not in prompt:
    fail.append(f"COLLISION — the prompt does not carry the slug {slug!r}")

words = len(page.split())
print(f"[input] page={len(page)}B words={words} prompt={len(prompt)}B lines={len(lines)} "
      f"slug={slug} builder={builder}")
if fail:
    for f in fail:
        print("  x", f)
    sys.exit(3)
print("  ok input assertions pass (not truncated, not narrowed, not collided, plausible size)")
PY
[ $? -eq 0 ] || exit 3

WORDS=$(python3 -c 'import sys,pathlib; print(len(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8").split()))' "$PAGE")
FLOOR=$(floor_for "$WORDS")

# ---- RUN ------------------------------------------------------------------------------
# On stdin, NEVER as an argument. As an argument it hangs.
codex exec -s read-only --skip-git-repo-check - < "$P" > "$R" 2>&1 || true

# ---- OUTPUT ASSERTIONS ----------------------------------------------------------------
# These are the real silence detectors, and they are unconditional. None of them is a
# count, so none of them can be fooled by a short page.
if [ ! -s "$R" ]; then
  echo "FAIL: the model returned an EMPTY file — silent failure, not a clean page"; exit 4
fi

# codex echoes the WHOLE prompt (which contains the page) and then prints the answer again
# after the token footer. Validating the raw file would match the ZITAT lines of the
# prompt's own format template and double-count every verdict. Extract just the answer:
# the block after the LAST `codex` marker, up to `tokens used`.
python3 - "$R" "$A" <<'PY'
import sys, pathlib
raw = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
lines = raw.split("\n")
starts = [i for i, l in enumerate(lines) if l.strip() == "codex"]
if not starts:
    print("FAIL: no `codex` answer marker in the raw output — the call did not produce an answer")
    sys.exit(7)
i = starts[-1] + 1
ends = [j for j, l in enumerate(lines) if j > i and l.strip() == "tokens used"]
j = ends[0] if ends else len(lines)
pathlib.Path(sys.argv[2]).write_text("\n".join(lines[i:j]).strip() + "\n", encoding="utf-8")
PY
[ $? -eq 0 ] || exit 7
[ -s "$A" ] || { echo "FAIL: the extracted answer is empty — silent failure, not a clean page"; exit 4; }

N=$(grep -c '^ZITAT:' "$A" || true)
echo "[output] raw $(wc -c < "$R")B -> answer $(wc -c < "$A")B, $N verdict block(s); floor for $WORDS words is $FLOOR"

if [ "$N" -eq 0 ]; then
  if grep -qiE "$ALLCLEAN_RE" "$A"; then
    echo "  ok zero verdicts WITH an explicit all-clear — a legitimate clean result."
  else
    echo "FAIL: zero verdict blocks and NO explicit all-clear. This is the SILENCE mode."
    echo "      Inspect $A and $R before believing anything."
    exit 5
  fi
elif [ "$N" -lt "$FLOOR" ]; then
  # WARN, never fail. This is the brevity fix: the model answered, so there is a work list;
  # a short one on a short page is the expected shape of a good page.
  echo "  WARN only $N block(s) against a scaled floor of $FLOOR. The call SUCCEEDED (answer"
  echo "       marker present, answer non-empty), so this is a short work list and not silence."
  echo "       Read it — and if the page really is long, sample again before trusting the low count."
else
  echo "  ok $N block(s) at or above the scaled floor of $FLOOR"
fi

python3 "$S/solcheck.py" "$PAGE" "$A" > "$V"
head -6 "$V"
echo "-> $V"
