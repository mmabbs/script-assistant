#!/usr/bin/env bash
set -euo pipefail

# Locate _fixtures/rules relative to this script, fall back to absolute path
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/_fixtures/rules"
if [ ! -d "$FIXTURES_DIR" ]; then
  echo "Cannot find _fixtures/rules" >&2
  exit 1
fi

# Copy rules files
mkdir -p rules
cp "$FIXTURES_DIR/migrator-rules.md" rules/migrator-rules.md

# Create project files
mkdir -p project/Ideas

cat > project/brain-dump.md << 'BD_EOF'
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- The lamp turns counterclockwise, which is wrong for this coast.
- Mara's lamp rotates the wrong way round. Every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911.
- It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose.

%% Agent, these three are the same idea said three ways. Merge them into one unit in idea-mara-lighthouse. %%
BD_EOF

cat > project/Ideas/idea-mara-lighthouse.md << 'IDEA_EOF'
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
IDEA_EOF
