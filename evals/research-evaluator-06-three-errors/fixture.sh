#!/usr/bin/env bash
set -euo pipefail

# Locate _fixtures/research relative to this script, fall back to absolute path
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/_fixtures/research"
if [ ! -d "$FIXTURES_DIR" ]; then
  echo "Cannot find _fixtures/research" >&2
  exit 1
fi


# Create project files from the shared stained-glass fixture
mkdir -p project/Research project/llm-files/research-plans project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows
cp "$FIXTURES_DIR/stained-glass/research-plan-stained-glass-windows.md" project/llm-files/research-plans/research-plan-stained-glass-windows.md
cp "$FIXTURES_DIR/stained-glass/topic-1.md" project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows/topic-1.md
cp "$FIXTURES_DIR/stained-glass/topic-2.md" project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows/topic-2.md
cp "$FIXTURES_DIR/stained-glass/research-stained-glass-windows.md" project/Research/research-stained-glass-windows.md

# Plant this case's three errors in the note, each in a different section
# (a) Disagreement / Uncertainty: the piece count changed from about 800 to about 600
# (b) Building the window: a which-clause adds a conclusion the findings don't hold to the footnoted armatures sentence.
#     The writer kept the strict rule on 2026-10-12, with no reasoning steps allowed, so this fails "matches findings".
# (c) Making the coloured glass: the answer to plan question 2 (how the pieces were cut) is removed, with its clause in the Summary
#     and its footnote; the question is not listed under Open Research Questions. Later footnotes are renumbered so none is left unused.
perl -0pi -e '
  s/piece count of about 800/piece count of about 600/;
  s/carried the weight of the leaded panels\.\[\^5\]/carried the weight of the leaded panels, which let the builders make the window openings far larger than before.[^5]/;
  s/molten, using metal oxides, and cut it with a hot iron before trimming the edges with a grozing iron\.\[\^1\]\[\^3\]/molten, using metal oxides.[^1]/;
  s/\nTo cut a piece, the glazier drew.*?Diamond cutters came much later\.\[\^3\]\n//s;
  s/\n\[\^3\]: [^\n]*//;
  s/\[\^([4-7])\]/"[^" . ($1 - 1) . "]"/ge;
' project/Research/research-stained-glass-windows.md
