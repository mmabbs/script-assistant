#!/usr/bin/env bash
set -euo pipefail

# Case 4: the standalone check. The project as it stands after the migrator's
# pass of batch b1, before any pointer. Planted: u1's char-mara line reads only
# with its source beside it ("what happened that winter"). u2 is correct: its
# Rationale line is the writer's own words, kept as written.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/_fixtures/rules"
if [ ! -d "$FIXTURES_DIR" ]; then
  echo "Cannot find _fixtures/rules" >&2
  exit 1
fi

mkdir -p rules
cp "$FIXTURES_DIR/migrator-rules.md" rules/migrator-rules.md

mkdir -p project/.runs/run-2026-10-09-2100-migration

cat > project/brain-dump.md << 'BD_EOF'
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-09

- Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. Mara has never forgiven her. #status/committed
%% Agent, char-mara. %%

- Mara swims in the harbour every morning at six, even in January. #status/committed
    - I like that her discipline looks like penance.
%% Agent, char-mara. %%
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

- Mara has kept the lighthouse for eleven years.
- Mara has never forgiven her mother for what happened that winter.
- Mara swims in the harbour every morning at six, even in January.

# Psychology

## Values, Beliefs, etc.

# Rationale

- I like that her discipline looks like penance.

# Rejected
CHAR_EOF

cat > project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json << 'JSON_EOF'
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. Mara has never forgiven her. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara has never forgiven her mother for what happened that winter."]
        }
      ],
      "edits": [],
      "status": "committed"
    },
    {
      "id": "u2",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- Mara swims in the harbour every morning at six, even in January. #status/committed"
        },
        {
          "note": "brain-dump.md",
          "line": 14,
          "text": "    - I like that her discipline looks like penance."
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara swims in the harbour every morning at six, even in January."]
        },
        {
          "note": "char-mara.md",
          "under": "# Rationale",
          "lines": ["- I like that her discipline looks like penance."]
        }
      ],
      "edits": [],
      "status": "committed"
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
JSON_EOF

# The batch as runmanager start wrote it (CONTRACT.md 5.2), as the notes stood
# when the run started.
cat > project/.runs/run-2026-10-09-2100-migration/batches.json << 'JSON_EOF'
{
  "batches": [
    {
      "batch": "b1",
      "pieces": [
        {
          "note": "brain-dump.md",
          "heading": "### 2026-10-09",
          "lines": [
            {
              "line": 10,
              "text": "- Mara's mother sold the family's fishing licence to the cannery the winter Tobias died. Mara has never forgiven her. #status/committed"
            },
            {
              "line": 11,
              "text": "%% Agent, char-mara. %%"
            },
            {
              "line": 13,
              "text": "- Mara swims in the harbour every morning at six, even in January. #status/committed"
            },
            {
              "line": 15,
              "text": "%% Agent, char-mara. %%"
            }
          ]
        }
      ]
    }
  ],
  "skipped": []
}
JSON_EOF
