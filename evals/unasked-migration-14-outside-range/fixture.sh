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

- The harbour has a tide bell that rings itself when the swell is over two metres.
- Nobody in town will say who installed it. Pell claims it predates the lighthouse.
- People set their clocks by it even though it's never on time.
- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too.

%% migrate all the bullets between "- The harbour has a tide bell" to "People set their clocks" %%

%% Agent, these go in idea-harrow-point. %%

### 2026-09-29

- Definitely keeping this: Mara hums the shipping forecast when she's nervous.
- Coyle waters down the whisky and everyone knows. #town
- The lifeboat station closed in 2009.
    - Its slipway is where the kids swim now.
BD_EOF

cat > project/Ideas/idea-harrow-point.md << 'IDEA_EOF'
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point
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
