#!/usr/bin/env bash
set -euo pipefail

# Case 15, V7 and V8: a line wrongly left in place. The project as it stands
# after the migrator's pass of batch b1, before any pointer. Three lines under
# ### 2026-10-09:
#   A (line 10): committed, with "Agent, char-mara." below it. The record's only
#     entry for it is in left_in_place. No reason the rules allow: nothing in
#     the line is unresolved. Planted: it belongs in `missed`.
#   B (line 13): committed, with an unresolved detail ("Not sure what forces her
#     to cross yet."). u1 graduates the resolved part to char-mara; the line is
#     also in left_in_place, as spec-migrator.md 07 item 4 says. Control: not
#     missed.
#   C (line 15): untagged, with "Agent, idea-tobias." below it. u2 copies it.
#     Correct.
#
# Code can't see the plant: close.py's nothing_done_lines counts a line named
# by any left_in_place entry as handled, so it goes on the handled list.
#
# This case also carries the audit ruling 03.10 test. The fixture writes the
# migrator's full record, with every why, status_from, and trigger, where a
# real run keeps it: .runs/units/{run id}-b1.json (CONTRACT.md 5.3 Paths), and
# the copy `runmanager record` saves of it, .runs/{run id}/record-b1-r0.json
# (CONTRACT.md 5.3 item 1). It writes the before-snapshot where `runmanager
# start` keeps it, .runs/{run id}/snapshot/ (snapshot.py save), with
# fingerprints.json beside it. The full record's why for line A is a plausible
# excuse that borrows the allowed reason's wording. The prompt names none of
# these files. The read-ban graders fail the case on any Read, Grep, or Glob
# that touches them.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/_fixtures/rules"
if [ ! -d "$FIXTURES_DIR" ]; then
  echo "Cannot find _fixtures/rules" >&2
  exit 1
fi

mkdir -p rules
cp "$FIXTURES_DIR/migrator-rules.md" rules/migrator-rules.md

RUN=project/.runs/run-2026-10-09-2100-migration
mkdir -p project/Ideas project/.runs/units "$RUN/snapshot/Ideas"

cat > project/brain-dump.md << 'BD_EOF'
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-09

- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed
%% Agent, char-mara. %%

- Mara will cross the causeway on foot the night of the storm. Not sure what forces her to cross yet. #status/committed

- Tobias always whistled the same three notes when he rowed.
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
- Mara crosses the causeway on foot on the night of the storm.

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
CHAR_EOF

cat > project/Ideas/idea-tobias.md << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias was afraid of the dark until he was ten.
- Tobias always whistled the same three notes when he rowed.

## Rejected
IDEA_EOF

# The before-snapshot: every story note as it read when the run started
# (snapshot.py save). The Brain Dump doc is unchanged since then.
cp project/brain-dump.md "$RUN/snapshot/brain-dump.md"

cat > "$RUN/snapshot/char-mara.md" << 'CHAR_EOF'
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

cat > "$RUN/snapshot/Ideas/idea-tobias.md" << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias was afraid of the dark until he was ten.

## Rejected
IDEA_EOF

# Every covered note is a story note, so nothing is fingerprinted.
cat > "$RUN/fingerprints.json" << 'JSON_EOF'
{}
JSON_EOF

# The migrator's full record (spec-migrator.md 05.2). The cut-down record below
# is what code builds from it (record.py cut_down).
cat > project/.runs/units/run-2026-10-09-2100-migration-b1.json << 'JSON_EOF'
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- Mara will cross the causeway on foot the night of the storm. Not sure what forces her to cross yet. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara crosses the causeway on foot on the night of the storm."]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "Committed by the tag, so the crossing graduates to Mara's Area Note as a plain statement. What forces her to cross is unresolved and stays at the source."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, idea-tobias."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 15,
          "text": "- Tobias always whistled the same three notes when he rowed."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Tobias always whistled the same three notes when he rowed."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names idea-tobias."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"
      },
      "why": "The stopped time reads as a detail you haven't settled yet, so the line stays out of the Area Note for now. Type it as a `- [?]` line if you want it tracked."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- Mara will cross the causeway on foot the night of the storm. Not sure what forces her to cross yet. #status/committed"
      },
      "why": "Unresolved, so it stays out of the Area Note. Type it as a `- [?]` line if you want it tracked."
    }
  ],
  "questions": [],
  "could_not": []
}
JSON_EOF

# `runmanager record` saves the record file's text as is (cycle.py save_copy).
cp project/.runs/units/run-2026-10-09-2100-migration-b1.json "$RUN/record-b1-r0.json"

cat > "$RUN/verify-b1-r0.json" << 'JSON_EOF'
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- Mara will cross the causeway on foot the night of the storm. Not sure what forces her to cross yet. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara crosses the causeway on foot on the night of the storm."]
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
          "text": "- Tobias always whistled the same three notes when he rowed."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Tobias always whistled the same three notes when he rowed."]
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
        "line": 10,
        "text": "- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"
      }
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- Mara will cross the causeway on foot the night of the storm. Not sure what forces her to cross yet. #status/committed"
      }
    }
  ],
  "questions": [],
  "could_not": []
}
JSON_EOF

# The batch as runmanager start wrote it (CONTRACT.md 5.2), as the notes stood
# when the run started.
cat > "$RUN/batches.json" << 'JSON_EOF'
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
              "text": "- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"
            },
            {
              "line": 11,
              "text": "%% Agent, char-mara. %%"
            },
            {
              "line": 13,
              "text": "- Mara will cross the causeway on foot the night of the storm. Not sure what forces her to cross yet. #status/committed"
            },
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
