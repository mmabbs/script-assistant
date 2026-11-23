#!/usr/bin/env bash
set -euo pipefail

# Case 12, V8: a copy from an earlier run sits below the writer's new tag.
# The project as it stands after the migrator's pass of batch b1, before any
# pointer.
#
# The earlier run, run-2026-10-02-1830-migration, migrated two provisional
# lines from ### 2026-10-02 to idea-mara-habits, tag and all, and wrote their
# pointers. Since then the writer changed one of them, the wreck-buoy line,
# from #status/provisional to #status/committed.
#
# How the scan reads that line (CONTRACT.md 5.2 items 6 to 8): its text no
# longer matches its handled entry; it carries a pointer; exactly one handled
# entry in brain-dump.md has the same destinations and text that is gone from
# the note; the tags differ, so the line is new work in this run. It is in
# batch b1, alone in the ### 2026-10-02 piece. The barometer line still matches
# its handled entry, so it isn't.
#
# u1 is correct: the migrator graduated the re-tagged line to char-mara as a
# plain statement. The earlier run's copy in idea-mara-habits still carries
# #status/provisional, below the writer's new tag. It wasn't written in this
# run, and the migrator leaves a line alone where its pointer already names the
# note (spec-migrator.md 07 item 5). It is neither a status fix nor missed
# (spec-migration-verifier.md 04.2 item 3).
#
# u2 is planted: a copy written in this run that drops the writer's
# #status/provisional, a status fix (spec-migration-verifier.md 04.1 item 4).

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

- Mara keeps her father's barometer notes in a biscuit tin. #status/provisional [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]
- Mara rows out to the wreck buoy every Sunday to leave flowers for Tobias. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]

### 2026-10-09

- Mara has stopped answering letters from the mainland. #status/provisional
%% Agent, idea-mara-habits. %%
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
- Every Sunday, Mara rows out to the wreck buoy to leave flowers for Tobias.

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
- Mara keeps her father's barometer notes in a biscuit tin. #status/provisional
- Mara rows out to the wreck buoy every Sunday to leave flowers for Tobias. #status/provisional
- Mara has stopped answering letters from the mainland.

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
          "line": 11,
          "text": "- Mara rows out to the wreck buoy every Sunday to leave flowers for Tobias. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Every Sunday, Mara rows out to the wreck buoy to leave flowers for Tobias."]
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
          "line": 15,
          "text": "- Mara has stopped answering letters from the mainland. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-habits.md",
          "under": "# Idea - Mara Habits",
          "lines": ["- Mara has stopped answering letters from the mainland."]
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
              "text": "- Mara rows out to the wreck buoy every Sunday to leave flowers for Tobias. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"
            }
          ]
        },
        {
          "note": "brain-dump.md",
          "heading": "### 2026-10-09",
          "lines": [
            {
              "line": 15,
              "text": "- Mara has stopped answering letters from the mainland. #status/provisional"
            },
            {
              "line": 16,
              "text": "%% Agent, idea-mara-habits. %%"
            }
          ]
        }
      ]
    }
  ],
  "skipped": []
}
JSON_EOF
