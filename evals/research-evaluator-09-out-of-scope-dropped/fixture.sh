#!/usr/bin/env bash
set -euo pipefail

# Locate _fixtures/research relative to this script, fall back to absolute path
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/_fixtures/research"
if [ ! -d "$FIXTURES_DIR" ]; then
  echo "Cannot find _fixtures/research" >&2
  exit 1
fi

# Create project files from the shared penny-farthings fixture
FINDINGS=project/llm-files/research-findings/run-2026-10-12-1400-research/penny-farthings
mkdir -p project/Research project/llm-files/research-plans "$FINDINGS"
cp "$FIXTURES_DIR/penny-farthings/research-plan-penny-farthings.md" project/llm-files/research-plans/
cp "$FIXTURES_DIR/penny-farthings/topic-1.md" "$FIXTURES_DIR/penny-farthings/topic-2.md" "$FINDINGS/"
cp "$FIXTURES_DIR/penny-farthings/research-penny-farthings.md" project/Research/

# The shared note keeps the answer-changing passage (topic-1.md passage 3), labelled and footnoted [^6].
# Remove it in all three places: the Summary sentence, the topic 1 paragraph, and footnote 6.
# Fail if any text isn't found.
perl -0pi -e '
  $n = s/\Q One finding lies outside the 1905 to 1914 period asked about: penny-farthings were everyday transport on English roads only from about 1875 to 1885.[^6]\E\n/\n/;
  $n += s/\n\n\QOne finding lies outside the 1905 to 1914 period asked about: penny-farthings were everyday transport on English roads only from about 1875 to 1885.[^6] In the late 1880s the safety bicycle, with two wheels of the same size and a chain driving the back wheel, replaced them, and by 1892 no English maker still offered a high-wheeler in its catalogue.[^6]\E\n/\n/;
  $n += s/\Q[^6]: https:\/\/www.cycle-heritage-museum.example\/collections\/from-high-wheeler-to-safety\E\n//;
  die "fixture.sh: expected 3 edits to the note, made $n\n" unless $n == 3;
' project/Research/research-penny-farthings.md
