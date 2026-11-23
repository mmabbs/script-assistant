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
mkdir -p project

cat > project/brain-dump.md << 'BD_EOF'
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- Mara took over the lighthouse at nineteen, the winter after her father's stroke, and she has never once let the lamp go dark, not even on the night of Tobias's funeral. I really want to keep this. She keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it. The coat works better than a photograph because she has to walk past it every day. #status/committed

%% Agent, this belongs in char-mara. %%
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

# Core

## Motivation and Intention

# Bio

## General

- Mara has kept the lighthouse for eleven years.
- Mara's younger brother Tobias drowned six years ago.

# Psychology

## Values, Beliefs, etc.

# Rationale

- A lighthouse keeper who is afraid of the sea is the whole joke of her.

# Rejected
CHAR_EOF
