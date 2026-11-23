#!/usr/bin/env bash
set -euo pipefail

# Case 23: a provisional line the writer left in an Area Note.
#
# char-mara holds "- Mara is wary of the mainland doctor. #status/provisional"
# among plain lines. The migrator leaves it exactly as it is, copies it nowhere,
# and asks about it once in questions. The bell-buoy line in the Brain Dump is
# the control: the writer tagged it and its comment names idea-mara-habits, so
# it migrates there, provisional.

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

### 2026-10-14

- Mara rows out to the bell buoy every Sunday to scrape the gull droppings off it. #status/provisional
%% Agent, this goes in idea-mara-habits. %%
BD_EOF

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

- Mara was born on Harrow Point and has never spent a night off it.

# Psychology

## Values, Beliefs, etc.

- Mara trusts the tide tables more than any forecast.
- Mara is wary of the mainland doctor. #status/provisional
- Mara thinks asking for help puts her in someone's debt.

# Rationale

# Rejected
CHAR_EOF

cat > project/Ideas/idea-mara-habits.md << 'IDEA_EOF'
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits

- Mara drinks her tea standing at the kitchen window, never sitting.
IDEA_EOF

cat > project/Ideas/idea-harrow-point.md << 'IDEA_EOF'
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## Getting to the mainland

- The clinic boat leaves at six in the morning and comes back at four.
IDEA_EOF
