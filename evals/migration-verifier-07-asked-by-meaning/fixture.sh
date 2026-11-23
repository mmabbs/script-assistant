#!/usr/bin/env bash
set -euo pipefail

# Case 7, V3 at the batch check: asked for, judged by meaning. The project as
# it stands after the migrator's pass of batch b1, before any pointer. Every
# unit is correct. u1's spelling fix also turns a comma splice into two
# sentences; u2's grammar fix adds a capital and a full stop.
#
# Edit and source line numbers are as the notes stood when the run started.
# Nothing above the edited lines moved, so they are the same now.

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

- Mara counts the steps on the way up: 114.
%% Agent, idea-mara-lighthouse. %%
BD_EOF

cat > project/Ideas/idea-mara-lighthouse.md << 'IDEA_EOF'
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

- The Harrow Point light stands on a rock at the end of the headland.
- Mara lives alone in the keeper's cottage at the foot of the tower.

- Mara repaints the gallery railing every spring. It's the only job she enjoys.
%% Agent, please correct the spelling in that line. %%

- The keeper before Mara was a drunk named Ollie Venn.
%% Agent, tidy the grammar here. %%

- Mara counts the steps on the way up: 114.

## Rejected
IDEA_EOF

cat > project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json << 'JSON_EOF'
{
  "units": [
    {
      "id": "u1",
      "action": "edit",
      "sources": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 11,
          "text": "- Mara repaints the gallery railing evrey spring, its the only job she enjoys."
        }
      ],
      "copies": [],
      "edits": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 11,
          "before": "- Mara repaints the gallery railing evrey spring, its the only job she enjoys.",
          "after": "- Mara repaints the gallery railing every spring. It's the only job she enjoys."
        }
      ],
      "status": "tentative"
    },
    {
      "id": "u2",
      "action": "edit",
      "sources": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 14,
          "text": "- the keeper before Mara were a drunk named Ollie Venn"
        }
      ],
      "copies": [],
      "edits": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 14,
          "before": "- the keeper before Mara were a drunk named Ollie Venn",
          "after": "- The keeper before Mara was a drunk named Ollie Venn."
        }
      ],
      "status": "tentative"
    },
    {
      "id": "u3",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara counts the steps on the way up: 114."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Mara counts the steps on the way up: 114."]
        }
      ],
      "edits": [],
      "status": "tentative"
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
              "line": 11,
              "text": "%% Agent, idea-mara-lighthouse. %%"
            }
          ]
        },
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "heading": null,
          "lines": [
            {
              "line": 12,
              "text": "%% Agent, please correct the spelling in that line. %%"
            },
            {
              "line": 15,
              "text": "%% Agent, tidy the grammar here. %%"
            }
          ]
        }
      ]
    }
  ],
  "skipped": []
}
JSON_EOF
