#!/usr/bin/env bash
#
# Run every locale-review tool's own self-test.
#
# These tools are JUDGEMENT-BEARING instruments, not gates that pass or fail a build: they
# produce the work list a translator or reviewer then acts on. That makes their own correctness
# unusually load-bearing, because a broken instrument here does not fail — it returns a
# confident, well-formed, wrong result. Eight distinct input failures across three German waves
# did exactly that, and every self-test below is one of them, reproduced.
#
# So this runs in CI even though the tools themselves are run by hand: the fixtures are cheap,
# they need no build and no network, and the alternative is discovering the regression the way
# it was discovered the first time.
#
# usage: scripts/locale-review/self-test.sh
set -uo pipefail

S="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$S"

fails=0
run() { # run <label> <cmd...>
  local label="$1"; shift
  echo "=============================================================================="
  echo "== $label"
  echo "=============================================================================="
  if "$@"; then
    echo
  else
    echo ">> FAILED: $label"
    echo
    fails=$((fails + 1))
  fi
}

run "solrun.sh — the silence-vs-brevity floor"        bash    ./solrun.sh --self-test
run "census.py — fence and JSX classification"        python3 ./census.py --self-test
run "codepoints.py — invisible codepoints, from bytes" python3 ./codepoints.py --self-test
run "concord.py — inflected surface forms"            python3 ./concord.py --self-test
run "referents.py — case-marked forms, named"         python3 ./referents.py --self-test
run "mermaid_gate.py — label extraction"              python3 ./mermaid_gate.py --self-test
run "banscan.py — ban list integrity"                 python3 ./banscan.py --self-test
run "solcheck.py — verdict validation"                python3 ./solcheck.py --self-test

if command -v node >/dev/null 2>&1; then
  run "cardwidth.mjs — the baseUrl assertion"         node    ./cardwidth.mjs --self-test
else
  echo "SKIP cardwidth.mjs — node not available"
fi

echo "=============================================================================="
if [ "$fails" -eq 0 ]; then
  echo "locale-review self-tests: PASS"
  exit 0
fi
echo "locale-review self-tests: FAIL — $fails tool(s)"
exit 1
