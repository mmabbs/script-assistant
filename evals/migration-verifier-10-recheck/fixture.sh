#!/usr/bin/env bash
set -euo pipefail

# Case 10, V9: the re-check. Batch b1, round 1. The project as it stands after
# the migrator's fix round, before any pointer.
#
# Round 0 (findings-b1-r0.json): u1 was a fix, because its idea-tobias copy
# dropped "Maybe"; u2 was approved. The fix round put "Maybe" back, on the same
# line, and changed nothing else. The re-check is handed u1 only.
#
# Nothing is wrong now. Two things tempt a fresh reader, and both are off
# limits on a re-check (spec-migration-verifier.md 03.1 item 5; Decisions Log
# item 29):
#   - u2's approved copy, beside u1's copy in idea-tobias, says "when he was
#     twelve" where the source says "the summer he turned twelve".
#   - u1's idea-mara-lighthouse copy, which the fix didn't touch, says "The
#     morning after Tobias drowned" where the source says "the next morning".
#
# Line numbers in the records are as the notes stood when the run started.
# The copies were added at the end of each note's live part, so the lines
# above them didn't move.

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

- Maybe Tobias rowed out that night to meet someone. Mara found his oars still in the shed the next morning.
%% Agent, split this: the night row goes in idea-tobias, the oars in idea-mara-lighthouse. %%

- Tobias carved his initials into the gallery rail the summer he turned twelve.
%% Agent, idea-tobias. %%
BD_EOF

cat > project/Ideas/idea-tobias.md << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias worked summers on the ferry to the mainland.
- Tobias drowned off the north jetty in October.
- Maybe Tobias rowed out that night to meet someone.
- Tobias carved his initials into the gallery railing when he was twelve.

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
- The morning after Tobias drowned, Mara found his oars still in the shed.

## Rejected
IDEA_EOF

# Round 0's cut-down record, still in the run folder. Its u1 copy in
# idea-tobias is the one round 0 sent back.
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
          "text": "- Maybe Tobias rowed out that night to meet someone. Mara found his oars still in the shed the next morning."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Tobias rowed out that night to meet someone."]
        },
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- The morning after Tobias drowned, Mara found his oars still in the shed."]
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
          "text": "- Tobias carved his initials into the gallery rail the summer he turned twelve."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Tobias carved his initials into the gallery railing when he was twelve."]
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

# The migration-verifier's round-0 findings, as the session saved them.
cat > project/.runs/run-2026-10-09-2100-migration/findings-b1-r0.json << 'JSON_EOF'
{
  "batch": "b1",
  "round": 0,
  "units": [
    {
      "unit": "u1",
      "verdict": "fix",
      "problems": [
        {
          "check": "lost-detail",
          "note": "Ideas/idea-tobias.md",
          "line": 10,
          "what": "Your note says \"Maybe\" Tobias rowed out that night to meet someone. The copy in idea-tobias drops the \"Maybe\" and states it as fact."
        }
      ]
    },
    { "unit": "u2", "verdict": "approve", "problems": [] }
  ],
  "missed": []
}
JSON_EOF

# Round 1's cut-down record: the fixed unit only, and the three lists empty
# (CONTRACT.md 5.3 item 4).
cat > project/.runs/run-2026-10-09-2100-migration/verify-b1-r1.json << 'JSON_EOF'
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Maybe Tobias rowed out that night to meet someone. Mara found his oars still in the shed the next morning."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Maybe Tobias rowed out that night to meet someone."]
        },
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- The morning after Tobias drowned, Mara found his oars still in the shed."]
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
              "text": "%% Agent, split this: the night row goes in idea-tobias, the oars in idea-mara-lighthouse. %%"
            },
            {
              "line": 14,
              "text": "%% Agent, idea-tobias. %%"
            }
          ]
        }
      ]
    }
  ],
  "skipped": []
}
JSON_EOF
