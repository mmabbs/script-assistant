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

%% Agent, in idea-mara-backstory: Mara being afraid of the sea is out. It makes her too passive. Keep the seasickness, that's physical, not fear. %%
BD_EOF

cat > project/Ideas/idea-mara-backstory.md << 'IDEA_EOF'
---
title: Idea - Mara Backstory
type: [idea-note]
---

# Idea - Mara Backstory

## Mara and the sea

- Mara is afraid of the sea.
- She gets seasick even on the ferry.
- Tobias was afraid of the sea too, which is why he took the skiff out, to prove something.
- The whole town has a superstition about saying "drown" out loud.
IDEA_EOF
