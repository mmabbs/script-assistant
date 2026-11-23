#!/usr/bin/env bash
set -euo pipefail

# Case 3, V5: scope. The project as it stands after the migrator's pass of
# batch b1, before any pointer. Planted: u2 rejects idea-harrow-point's hotel
# line, wider than "for Mara's story only"; u3 makes a wording fix on the
# neighbouring causeway line that no comment asked for. u1 is correct.
#
# Line numbers in the record are as the notes stood when the run started.
# Pre-run layout of Ideas/idea-mara-lighthouse.md:
#   6  # Idea - Mara Lighthouse
#   8  - The Harrow Point light stands on a rock at the end of the headland.
#   9  - Mara lives alone in the keeper's cottage at the foot of the tower.
#   10 - the causeway floods at spring tides, about twice a month
#   11 (blank)
#   12 - The lighthouse is sold to a hotel chain, and Mara has to leave.   <- u1 source
#   13 %% Agent, the hotel sale is out for Mara's story only. The town can still have it. %%
#   14 (blank)
#   15 ## Rejected
# Pre-run layout of Ideas/idea-harrow-point.md:
#   6  # Idea - Harrow Point
#   8  - Harrow Point is a fishing village of about two hundred people.
#   9  - A hotel chain buys the old harbour cottages and the pier.          <- u2 source
#   10 - The harbour is too shallow now for anything bigger than a creel boat.
#   11 (blank)
#   12 ## Rejected

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

- Mara's radio is the only link to the mainland when the causeway floods.
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
- The causeway floods at spring tides, about twice a month.
- Mara's radio is the only link to the mainland when the causeway floods.

%% Agent, the hotel sale is out for Mara's story only. The town can still have it. %%

## Rejected

- The lighthouse is sold to a hotel chain, and Mara has to leave. #status/rejected
IDEA_EOF

cat > project/Ideas/idea-harrow-point.md << 'IDEA_EOF'
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- Harrow Point is a fishing village of about two hundred people.
- The harbour is too shallow now for anything bigger than a creel boat.

## Rejected

- A hotel chain buys the old harbour cottages and the pier. #status/rejected
IDEA_EOF

cat > project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json << 'JSON_EOF'
{
  "units": [
    {
      "id": "u1",
      "action": "reject",
      "sources": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 12,
          "text": "- The lighthouse is sold to a hotel chain, and Mara has to leave."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## Rejected",
          "lines": ["- The lighthouse is sold to a hotel chain, and Mara has to leave. #status/rejected"]
        }
      ],
      "edits": [],
      "status": "rejected"
    },
    {
      "id": "u2",
      "action": "reject",
      "sources": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "line": 9,
          "text": "- A hotel chain buys the old harbour cottages and the pier."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## Rejected",
          "lines": ["- A hotel chain buys the old harbour cottages and the pier. #status/rejected"]
        }
      ],
      "edits": [],
      "status": "rejected"
    },
    {
      "id": "u3",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara's radio is the only link to the mainland when the causeway floods."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Mara's radio is the only link to the mainland when the causeway floods."]
        }
      ],
      "edits": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 10,
          "before": "- the causeway floods at spring tides, about twice a month",
          "after": "- The causeway floods at spring tides, about twice a month."
        }
      ],
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
              "line": 13,
              "text": "%% Agent, the hotel sale is out for Mara's story only. The town can still have it. %%"
            }
          ]
        }
      ]
    }
  ],
  "skipped": []
}
JSON_EOF
