#!/usr/bin/env bash
set -euo pipefail

# Locate _fixtures/research relative to this script, fall back to absolute path
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/_fixtures/research"
if [ ! -d "$FIXTURES_DIR" ]; then
  echo "Cannot find _fixtures/research" >&2
  exit 1
fi

# Copy the note template
mkdir -p templates
cp "$FIXTURES_DIR/research-template.md" templates/research-template.md
# The project's own template copy carries the hub link (spec 07 item 1)
sed -i.bak 's#^project:.*#project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"#' templates/research-template.md && rm templates/research-template.md.bak

# Create project files from the shared stained-glass fixture. No draft-1.md: the research-writer writes it.
FINDINGS=project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows
mkdir -p project/Research project/llm-files/research-plans "$FINDINGS"
cp "$FIXTURES_DIR/stained-glass/research-plan-stained-glass-windows.md" project/llm-files/research-plans/
cp "$FIXTURES_DIR/stained-glass/topic-1.md" "$FIXTURES_DIR/stained-glass/topic-2.md" "$FINDINGS/"
cp "$FIXTURES_DIR/stained-glass/research-stained-glass-windows.md" project/Research/

# The note as handed to the fix round: E6's three planted errors, which the prompt lists as the
# research-evaluator's problems. Fail if any edit doesn't land.
# (a) Disagreement / Uncertainty: the piece count changed from about 800 to about 600
# (b) Building the window: a which-clause adds a conclusion the findings don't hold
# (c) Making the coloured glass: the answer to plan question 2 (how the pieces were cut) removed, with its
#     clause in the Summary and its footnote; later footnotes renumbered so none is left unused
perl -0pi -e '
  $n = 0;
  $n += s/piece count of about 800/piece count of about 600/;
  $n += s/carried the weight of the leaded panels\.\[\^5\]/carried the weight of the leaded panels, which let the builders make the window openings far larger than before.[^5]/;
  $n += s/molten, using metal oxides, and cut it with a hot iron before trimming the edges with a grozing iron\.\[\^1\]\[\^3\]/molten, using metal oxides.[^1]/;
  $n += s/\nTo cut a piece, the glazier drew.*?Diamond cutters came much later\.\[\^3\]\n//s;
  $n += s/\n\[\^3\]: [^\n]*//;
  s/\[\^([4-7])\]/"[^" . ($1 - 1) . "]"/ge;
  die "fixture.sh: $n of 5 plant edits landed\n" unless $n == 5;
' project/Research/research-stained-glass-windows.md
