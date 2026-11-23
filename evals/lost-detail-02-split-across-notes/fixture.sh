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

- Mara's brother Tobias drowned when she was nine. She still sets a place for him at dinner.

%% Agent, migrate this. The drowning goes in idea-tobias, the dinner habit in idea-mara-habits. %%
BD_EOF

cat > project/Ideas/idea-tobias.md << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias
IDEA_EOF

cat > project/Ideas/idea-mara-habits.md << 'IDEA_EOF'
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits
IDEA_EOF
