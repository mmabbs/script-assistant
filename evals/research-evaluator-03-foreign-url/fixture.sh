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

# Plant this case's error in the note
perl -pi -e 's#^\[\^6\]: .*#[^6]: https://www.glass-history-blog.example/2022/lancet-windows#' project/Research/research-stained-glass-windows.md
