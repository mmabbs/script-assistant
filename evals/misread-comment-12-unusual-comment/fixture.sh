#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/_fixtures/rules"
if [ ! -d "$FIXTURES_DIR" ]; then
  echo "Cannot find _fixtures/rules" >&2
  exit 1
fi

mkdir -p rules
cp "$FIXTURES_DIR/migrator-rules.md" rules/migrator-rules.md

mkdir -p project/Ideas

cat > project/brain-dump.md << 'BD_EOF'
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- The harbour wall was rebuilt in 1962 with stone from the old church.
- The stone is cursed, obviously.
- Pell's family paid for the rebuild and never let anyone forget it.

%% Agent, migrate the first and third bullets under this date to idea-harrow-point. The third one is provisional. Skip the second, I'm not sure about it. %%
BD_EOF

cat > project/Ideas/idea-harrow-point.md << 'IDEA_EOF'
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point
IDEA_EOF
