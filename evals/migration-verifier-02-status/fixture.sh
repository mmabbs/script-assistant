#!/usr/bin/env bash
set -euo pipefail

# Case 2, V2: status. The project as it stands after the migrator's pass of
# batch b1, before any pointer. Planted: u1 puts provisional material in an
# Area Note (its comment names no destination on purpose); u2's copy carries
# provisional, below the writer's committed tag. u3 is correct.

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

- Mara learned to read the weather from her father's barometer notes. #status/provisional
%% Agent, migrate this. %%

- Mara has never once left Harrow Point overnight. #status/committed
%% Agent, this goes in char-mara. %%

- Mara keeps the light by hand when the power fails, winding the old clockwork. #status/committed
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
- Mara learned to read the weather from her father's barometer notes.
- Mara keeps the light by hand when the power fails, winding the old clockwork mechanism.

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
- Mara has never once left Harrow Point overnight. #status/provisional

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
          "text": "- Mara learned to read the weather from her father's barometer notes. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara learned to read the weather from her father's barometer notes."]
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
          "text": "- Mara has never once left Harrow Point overnight. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Mara has never once left Harrow Point overnight. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional"
    },
    {
      "id": "u3",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 16,
          "text": "- Mara keeps the light by hand when the power fails, winding the old clockwork. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara keeps the light by hand when the power fails, winding the old clockwork mechanism."]
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
              "text": "- Mara learned to read the weather from her father's barometer notes. #status/provisional"
            },
            {
              "line": 11,
              "text": "%% Agent, migrate this. %%"
            },
            {
              "line": 13,
              "text": "- Mara has never once left Harrow Point overnight. #status/committed"
            },
            {
              "line": 14,
              "text": "%% Agent, this goes in char-mara. %%"
            },
            {
              "line": 16,
              "text": "- Mara keeps the light by hand when the power fails, winding the old clockwork. #status/committed"
            },
            {
              "line": 17,
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
