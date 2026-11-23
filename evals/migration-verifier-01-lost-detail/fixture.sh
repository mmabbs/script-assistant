#!/usr/bin/env bash
set -euo pipefail

# Case 1, V1: lost detail. The project as it stands after the migrator's pass
# of batch b1, before any pointer. Planted: u1's idea-tobias copy loses "nine";
# u2's copy drops "Maybe". u3 is a correct reword.

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

- Mara's brother Tobias drowned off the north jetty when she was nine. She still sets a place for him at dinner.
%% Agent, the drowning goes in idea-tobias, the dinner habit in idea-mara-habits. %%

- Maybe her father hid the old keeper's logbook somewhere in the tower before he died.
%% Agent, this goes in idea-mara-lighthouse. %%

- The lamp room smells of paraffin even though the light went electric in 1962.
%% Agent, idea-mara-lighthouse. %%
BD_EOF

cat > project/Ideas/idea-tobias.md << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias worked summers on the ferry to the mainland.
- He kept a rowing boat tied up under the pier.
- Mara's brother Tobias drowned off the north jetty when she was a child.

## Rejected
IDEA_EOF

cat > project/Ideas/idea-mara-habits.md << 'IDEA_EOF'
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits

- Mara walks the gallery every evening at dusk.
- She drinks her tea black, from her father's enamel mug.
- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine.

## Rejected
IDEA_EOF

cat > project/Ideas/idea-mara-lighthouse.md << 'IDEA_EOF'
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

- The Harrow Point light stands on a rock at the end of the headland.
- Mara lives alone in the keeper's cottage at the foot of the tower.
- Mara's father hid the old keeper's logbook somewhere in the tower before he died.
- The lamp room still smells of paraffin, though the light went electric in 1962.

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
          "text": "- Mara's brother Tobias drowned off the north jetty when she was nine. She still sets a place for him at dinner."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Mara's brother Tobias drowned off the north jetty when she was a child."]
        },
        {
          "note": "Ideas/idea-mara-habits.md",
          "under": "# Idea - Mara Habits",
          "lines": ["- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine."]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u2",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- Maybe her father hid the old keeper's logbook somewhere in the tower before he died."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Mara's father hid the old keeper's logbook somewhere in the tower before he died."]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u3",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 16,
          "text": "- The lamp room smells of paraffin even though the light went electric in 1962."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- The lamp room still smells of paraffin, though the light went electric in 1962."]
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
              "text": "%% Agent, the drowning goes in idea-tobias, the dinner habit in idea-mara-habits. %%"
            },
            {
              "line": 14,
              "text": "%% Agent, this goes in idea-mara-lighthouse. %%"
            },
            {
              "line": 17,
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
