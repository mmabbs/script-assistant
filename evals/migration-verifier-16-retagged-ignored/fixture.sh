#!/usr/bin/env bash
set -euo pipefail

# Case 16, V7: a re-tagged line the migrator ignored. The project as it stands
# after the migrator's pass of batch b1, before any pointer.
#
# An earlier run, run-2026-10-02-1830-migration, copied two provisional lines
# from ### 2026-10-02 to idea-mara-habits, tag and all, and wrote their
# pointers. Since then the writer changed one of them, the notebook line, from
# #status/provisional to #status/committed. The nets line is unchanged.
#
# How the scan reads the notebook line (CONTRACT.md 5.2 item 8): its text no
# longer matches its handled entry; it carries a pointer; exactly one handled
# entry in brain-dump.md has the same destinations and text that is gone from
# the note; the tags differ, so the line is new work in this run
# (spec-run-manager.md 07.1 item 4). It is in batch b1, alone in the
# ### 2026-10-02 piece. The nets line still matches its handled entry, so it
# isn't in the batch.
#
# Planted: the migrator did nothing with the notebook line. The committed tag
# asks for it to graduate to an Area Note, and nothing did. Its only record
# entry is in left_in_place: the migrator read the pointer as "already
# migrated" (its full record's why: "Already migrated: its pointer names
# idea-mara-habits."), stretching spec-migrator.md 07 item 5, which covers only
# copying a line again into a note its pointer already names. The cut-down
# record keeps only the entry's source. Code can't see the plant: close.py's
# nothing_done_lines counts a line named by any left_in_place entry as handled.
# It is `missed` (spec-migration-verifier.md 04.2 items 1 and 3; 10 Decisions
# Log item 30).
#
# u1 is correct: a plain copy a comment asked for.
#
# The earlier run's copy of the notebook line in idea-mara-habits still carries
# #status/provisional. That is case 12's ground; nothing here turns on it.

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

### 2026-10-02

- Mara mends her own nets rather than buy new ones. #status/provisional [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]
- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]

### 2026-10-09

- Tobias once rowed to the mainland and back in a single night to win a bet.
%% Agent, idea-tobias. %%
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

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
CHAR_EOF

cat > project/Ideas/idea-mara-habits.md << 'IDEA_EOF'
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits

- Mara walks the gallery every evening at dusk.
- Mara mends her own nets rather than buy new ones. #status/provisional
- Mara writes down every ship she sees from the gallery in a notebook. #status/provisional

## Rejected
IDEA_EOF

cat > project/Ideas/idea-tobias.md << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias was afraid of the dark until he was ten.
- Tobias once rowed to the mainland and back in a single night to win a bet.

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
          "line": 15,
          "text": "- Tobias once rowed to the mainland and back in a single night to win a bet."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Tobias once rowed to the mainland and back in a single night to win a bet."]
        }
      ],
      "edits": [],
      "status": "tentative"
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 11,
        "text": "- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"
      }
    }
  ],
  "questions": [],
  "could_not": []
}
JSON_EOF

# The batch as runmanager start wrote it (CONTRACT.md 5.2), as the notes stood
# when the run started, with the earlier run's lines on the handled list.
cat > project/.runs/run-2026-10-09-2100-migration/batches.json << 'JSON_EOF'
{
  "batches": [
    {
      "batch": "b1",
      "pieces": [
        {
          "note": "brain-dump.md",
          "heading": "### 2026-10-02",
          "lines": [
            {
              "line": 11,
              "text": "- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"
            }
          ]
        },
        {
          "note": "brain-dump.md",
          "heading": "### 2026-10-09",
          "lines": [
            {
              "line": 16,
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
