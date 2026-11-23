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

- Okay so the keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step? Maybe she logged every ship that didn't come back, 31 of them, going back to 1987. Does Mara find it, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out. What if the last entry is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.

%% Agent, migrate this to idea-mara-lighthouse. %%
BD_EOF

cat > project/Ideas/idea-mara-lighthouse.md << 'IDEA_EOF'
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
IDEA_EOF
