#!/usr/bin/env bash
set -euo pipefail

# The live run's files (2026-10-12) are copied into this case folder under live-run/,
# because the test project they came from may be deleted. Fall back to the absolute path.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LIVE_DIR="${SCRIPT_DIR}/live-run"
if [ ! -d "$LIVE_DIR" ]; then
  echo "Cannot find live-run/" >&2
  exit 1
fi

# Create project files at the live run's paths
FINDINGS=llm-files/research-findings/run-2026-10-12-1649-research/lighthouse-fog-signals
mkdir -p project/Research project/llm-files/research-plans "project/$FINDINGS"
cp "$LIVE_DIR/llm-files/research-plans/research-plan-lighthouse-fog-signals.md" project/llm-files/research-plans/
cp "$LIVE_DIR/$FINDINGS/topic-1.md" "$LIVE_DIR/$FINDINGS/topic-2.md" "project/$FINDINGS/"
cp "$LIVE_DIR/Research/research-lighthouse-fog-signals.md" project/Research/

# The saved note is the fix-round version. Revert the one sentence the fix round changed,
# so the note is the first draft the live research-evaluator checked. Fail if the text isn't there.
perl -0pi -e '
  $n = s/\QThe same page says the building dates from 1871 and first used compressed-air horns, which were swapped for sirens in 1879 and for more powerful units in 1919.[^8]\E/The same page says the diaphones replaced more powerful units fitted in 1919.[^8]/;
  die "fixture.sh: the fix-round sentence was not found in the note\n" unless $n == 1;
' project/Research/research-lighthouse-fog-signals.md
