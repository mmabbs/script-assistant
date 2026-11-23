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

# Create project files. The plan and findings come from the shared penny-farthings fixture.
# The note is not copied: the research-writer writes it.
FINDINGS=project/llm-files/research-findings/run-2026-10-12-1400-research/penny-farthings
mkdir -p project/Research project/llm-files/research-plans "$FINDINGS" project/Ideas
cp "$FIXTURES_DIR/penny-farthings/research-plan-penny-farthings.md" project/llm-files/research-plans/
cp "$FIXTURES_DIR/penny-farthings/topic-1.md" "$FIXTURES_DIR/penny-farthings/topic-2.md" "$FINDINGS/"

cat > project/Ideas/idea-market-day.md << 'NOTE_EOF'
---
title: Idea - Market Day
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
---

# Idea - Market Day

- Opening image: the high street on market day, the townsfolk riding to work on penny-farthings.
- [r] How did people ride penny-farthings to work in English towns, and who rode them? How did a rider get on and off one, and what were the dangers? #research/run-6
    %% England, 1905 to 1914. %%
NOTE_EOF
