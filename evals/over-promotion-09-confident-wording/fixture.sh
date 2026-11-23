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

- This is locked: Mara never learned to swim.
- 100% canon, Tobias was the better sailor of the two.
- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her.
- The lighthouse stays in the family, that's decided. #status/provisional
- Mara gets seasick, badly. #status/provisional
    - It happens even on the ferry, on a flat day.
    - [?] Does the town know, or does she hide it?

%% migrate all the bullets between "- This is locked" to "Mara gets seasick" %%

%% Agent, these go in idea-mara-backstory. %%
BD_EOF

cat > project/Ideas/idea-mara-backstory.md << 'IDEA_EOF'
---
title: Idea - Mara Backstory
type: [idea-note]
---

# Idea - Mara Backstory
IDEA_EOF

cat > project/char-mara.md << 'CHAR_EOF'
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Bio

## General

- Mara has kept the lighthouse for eleven years.

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
CHAR_EOF
