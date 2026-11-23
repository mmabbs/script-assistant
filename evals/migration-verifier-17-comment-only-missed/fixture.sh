#!/usr/bin/env bash
set -euo pipefail

# Case 17, V7: an untagged line only a comment triggered, which the migrator
# ignored. The project as it stands after the migrator's pass of batch b1,
# before any pointer. Two lines under ### 2026-10-09, each untagged, each with a
# comment below it that names a note:
#   A (line 10): "Agent, idea-tobias." Nothing in the record names the line or
#     its comment: no unit, no left_in_place, no questions, no could_not.
#     Planted: it belongs in `missed`.
#   B (line 13): "Agent, idea-mara-lighthouse." u1 copies it. Correct.
#
# Only the comments are batch lines (CONTRACT.md 5.2 items 2 and 3): an
# untagged bullet is not a trigger line. Code can't see the plant: close.py's
# nothing_done_lines skips comment lines, and spec-run-manager.md 07.1 item 8
# covers tagged lines only. At close, the comment goes on the handled list as
# `comment` (CONTRACT.md 5.6 item 3), so the line is dropped for good unless
# the migration-verifier calls it missed. No could_not entry names
# brain-dump.md, so close.py's could_not note-skip masks nothing here.

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

- Tobias tied a red ribbon to the jetty post whenever he took the boat out alone.
%% Agent, idea-tobias. %%

- Mara leaves the lamp-room door open so she can hear the foghorn from the kitchen.
%% Agent, idea-mara-lighthouse. %%
BD_EOF

cat > project/Ideas/idea-tobias.md << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias was afraid of the dark until he was ten.

## Rejected
IDEA_EOF

cat > project/Ideas/idea-mara-lighthouse.md << 'IDEA_EOF'
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

- The lamp room smells of paraffin even though the light went electric in 1962.
- Mara leaves the lamp-room door open so she can hear the foghorn from the kitchen.

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
          "line": 13,
          "text": "- Mara leaves the lamp-room door open so she can hear the foghorn from the kitchen."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Mara leaves the lamp-room door open so she can hear the foghorn from the kitchen."]
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
              "text": "%% Agent, idea-tobias. %%"
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
