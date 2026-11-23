#!/usr/bin/env bash
set -euo pipefail

# Case 5, V7 and V8: missed line. The project as it stands after the migrator's
# pass of batch b1, before any pointer. Four lines under ### 2026-10-09:
#   A (line 10): committed, comment names char-mara, no unit. Planted miss.
#   B (line 13): three ideas; u1 graduates the first, a questions entry covers B.
#   C (line 15): a could_not entry; the named research note doesn't exist.
#   D (line 18): untagged, no comment. Not a trigger.

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

- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed
%% Agent, char-mara. %%

- Mara sleeps in the watch room in winter, the relief keeper might be a woman from Oban, and the light could be decommissioned by spring. #status/committed

- The old keepers logged every ship that passed.
%% Agent, add this to the paraffin section of research-light-lighthouse-lamps. %%

- What if the fog horn is broken all winter?
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
- Mara sleeps in the watch room in winter.

# Psychology

## Values, Beliefs, etc.

# Rationale

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
          "line": 13,
          "text": "- Mara sleeps in the watch room in winter, the relief keeper might be a woman from Oban, and the light could be decommissioned by spring. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara sleeps in the watch room in winter."]
        }
      ],
      "edits": [],
      "status": "committed"
    }
  ],
  "left_in_place": [],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- Mara sleeps in the watch room in winter, the relief keeper might be a woman from Oban, and the light could be decommissioned by spring. #status/committed"
      }
    }
  ],
  "could_not": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 15,
        "text": "- The old keepers logged every ship that passed."
      }
    }
  ]
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
              "text": "- Mara keeps Tobias's oilskin coat on the hook by the door. #status/committed"
            },
            {
              "line": 11,
              "text": "%% Agent, char-mara. %%"
            },
            {
              "line": 13,
              "text": "- Mara sleeps in the watch room in winter, the relief keeper might be a woman from Oban, and the light could be decommissioned by spring. #status/committed"
            },
            {
              "line": 16,
              "text": "%% Agent, add this to the paraffin section of research-light-lighthouse-lamps. %%"
            }
          ]
        }
      ]
    }
  ],
  "skipped": []
}
JSON_EOF
