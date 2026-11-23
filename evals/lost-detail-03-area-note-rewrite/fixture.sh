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

- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job. I really like this. Tobias as the reason feels more honest than duty. #status/committed

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

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
CHAR_EOF
