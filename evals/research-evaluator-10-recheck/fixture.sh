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
FINDINGS=project/llm-files/research-findings/run-2026-10-08-1400-research/stained-glass-windows
NOTE=project/Research/research-stained-glass-windows.md
mkdir -p project/Research project/llm-files/research-plans "$FINDINGS"
cp "$FIXTURES_DIR/stained-glass/research-plan-stained-glass-windows.md" project/llm-files/research-plans/
cp "$FIXTURES_DIR/stained-glass/topic-1.md" "$FIXTURES_DIR/stained-glass/topic-2.md" "$FINDINGS/"
cp "$FIXTURES_DIR/stained-glass/research-stained-glass-windows.md" "$FINDINGS/draft-1.md"

# draft-1.md, the first draft the first check saw. Four errors in the clean note:
#   FP1  Disagreement / Uncertainty: piece count about 600 (findings: about 800). Listed as first problem 1.
#   FP2  Making the coloured glass: the glass scored "with a diamond" (findings: a red-hot iron). Listed as first problem 2.
#   FP3  Building the window: "a method copied from Byzantine mosaic workshops" added. Listed as first problem 3.
#   PL1  Making the coloured glass: grisaille made of "copper oxide" (findings: iron oxide). The first check missed it;
#        it is not in the first problems. Plant 1.
perl -0pi -e '
  $n = 0;
  $n += s/piece count of about 800/piece count of about 600/;
  $n += s/the glazier drew a red-hot iron along a line marked on the glass, and the glass cracked along it\./the glazier scored a line on the glass with a diamond, and the glass cracked along it./;
  $n += s/then cut the pieces and laid them out over the drawing\./then cut the pieces and laid them out over the drawing, a method copied from Byzantine mosaic workshops./;
  $n += s/ground glass and iron oxide/ground glass and copper oxide/;
  die "fixture.sh: $n of 4 first-draft edits landed\n" unless $n == 4;
' "$FINDINGS/draft-1.md"

# The note after the fix round:
#   Plant 2: FP1 left unfixed. The 600 stays.
#   Plant 3: FP2's sentence changed. The diamond is gone, but the new sentence adds "a method first recorded in 1240",
#            which the findings don't hold.
#   Plant 4: FP3's whole paragraph deleted, with its footnote [^7]. That paragraph was the note's only answer to plan
#            question 4, how glaziers planned the design (the whitewashed table), and the question is not listed as open.
#   Plant 1: unchanged, so the re-check must not report it.
cp "$FINDINGS/draft-1.md" "$NOTE"
perl -0pi -e '
  $n = 0;
  $n += s/the glazier scored a line on the glass with a diamond, and the glass cracked along it\./the glazier drew a red-hot iron along a line marked on the glass, and the glass cracked along it, a method first recorded in 1240./;
  $n += s/\nBefore any glass was cut, the glazier drew the whole design.*?washed and whitened again for the next design\.\[\^7\]\n//s;
  $n += s/\n\[\^7\]: [^\n]*//;
  die "fixture.sh: $n of 3 fix-round edits landed\n" unless $n == 3;
' "$NOTE"
