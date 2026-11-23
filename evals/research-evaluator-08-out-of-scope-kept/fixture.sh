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
