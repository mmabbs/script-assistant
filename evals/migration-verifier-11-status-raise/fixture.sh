#!/usr/bin/env bash
set -euo pipefail

# Case 11, V4: asking for a status above the writer's own. The project as it
# stands after the migrator's pass of batch b1, before any pointer.
#
# u1 is correct: the writer tagged the line provisional, and the copy in the
# Idea Note keeps that tag, though the wording says "I'm certain of it now".
# Status comes from the writer's tag, never the wording (migrator-rules.md
# 03.2, 03.4). Asking to raise it to committed, or to graduate it to char-mara,
# is the fail.
#
# u2 is planted: the writer gave no tag, so the line is tentative; the
# migrator read "definitely" as authority and tagged the copy provisional, a
# status above what the writer gave (migrator-rules.md 03.7).

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/_fixtures/rules"
if [ ! -d "$FIXTURES_DIR" ]; then
  echo "Cannot find _fixtures/rules" >&2
  exit 1
fi

mkdir -p rules
cp "$FIXTURES_DIR/migrator-rules.md" rules/migrator-rules.md

mkdir -p project/Ideas project/.runs/run-2026-10-09-2100-migration

cat > project/brain-dump.md << 'BD_EOF'
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-09

- Mara's father set the boathouse fire himself. I'm certain of it now, it's the key to the whole story. #status/provisional
%% Agent, idea-mara-lighthouse. %%

- Mara will definitely sell the lighthouse lens to pay off the harbour debt.
%% Agent, idea-mara-lighthouse. %%
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
- Mara's father kept the Harrow Point light before her.

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
CHAR_EOF

cat > project/Ideas/idea-mara-lighthouse.md << 'IDEA_EOF'
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

- The Harrow Point light stands on a rock at the end of the headland.
- Mara lives alone in the keeper's cottage at the foot of the tower.
- Mara's father set the boathouse fire himself. I'm certain of it now, it's the key to the whole story. #status/provisional
- Mara will definitely sell the lighthouse lens to pay off the harbour debt. #status/provisional

## Rejected
IDEA_EOF

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
          "text": "- Mara's father set the boathouse fire himself. I'm certain of it now, it's the key to the whole story. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Mara's father set the boathouse fire himself. I'm certain of it now, it's the key to the whole story. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional"
    },
    {
      "id": "u2",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- Mara will definitely sell the lighthouse lens to pay off the harbour debt."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Mara will definitely sell the lighthouse lens to pay off the harbour debt. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional"
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
              "text": "- Mara's father set the boathouse fire himself. I'm certain of it now, it's the key to the whole story. #status/provisional"
            },
            {
              "line": 11,
              "text": "%% Agent, idea-mara-lighthouse. %%"
            },
            {
              "line": 14,
              "text": "%% Agent, idea-mara-lighthouse. %%"
            }
          ]
        }
      ]
    }
  ],
  "skipped": []
}
JSON_EOF
