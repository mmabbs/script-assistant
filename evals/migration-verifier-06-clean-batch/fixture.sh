#!/usr/bin/env bash
set -euo pipefail

# Case 6, V4: clean batch. The project as it stands after the migrator's pass
# of batch b1, before any pointer. Every unit is correct. u4 carries the
# writer's reason as a comment on the line below its Rejected line, the settled
# form (migrator-rules.md 08.5). u5's comment names no
# destination, so where it went is not judged.
#
# Line numbers in the record are as the notes stood when the run started.
# Pre-run layout of Ideas/idea-mara-lighthouse.md:
#   6  # Idea - Mara Lighthouse
#   8  - The Harrow Point light stands on a rock at the end of the headland.
#   9  - Mara lives alone in the keeper's cottage at the foot of the tower.
#   10 (blank)
#   11 - Mara keeps a dog called Skipper.        <- u4 source
#   12 %% Agent, reject the dog. It makes her too cosy. %%
#   13 (blank)
#   14 ## Rejected

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

- Tobias wanted to be a lighthouse keeper too, before the accident.
%% Agent, idea-tobias. %%

- The causeway floods twice a month, and Mara times her supply runs around the tide table.
%% Agent, the flooding goes in idea-harrow-point, the supply runs in idea-mara-lighthouse. %%

- The new keeper could be someone from the mainland who's never seen the sea.
- What if the relief keeper is scared of the water?
%% Agent, these two are the same idea. Merge them into idea-mara-lighthouse. %%

- Tobias kept a tin of sea glass under his bed.
%% Agent, migrate this. %%
BD_EOF

cat > project/Ideas/idea-tobias.md << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias worked summers on the ferry to the mainland.
- He kept a rowing boat tied up under the pier.
- Tobias wanted to be a lighthouse keeper too, before the accident.
- Tobias kept a tin of sea glass under his bed.

## Rejected
IDEA_EOF

cat > project/Ideas/idea-harrow-point.md << 'IDEA_EOF'
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- Harrow Point is a fishing village of about two hundred people.
- The harbour is too shallow now for anything bigger than a creel boat.
- The causeway to Harrow Point floods twice a month.

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
- Mara times her supply runs around the tide table, because the causeway floods twice a month.
- The relief keeper could be someone from the mainland who has never seen the sea and is scared of the water.

%% Agent, reject the dog. It makes her too cosy. %%

## Rejected

- Mara keeps a dog called Skipper. #status/rejected
%% It makes her too cosy. %%
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
          "text": "- Tobias wanted to be a lighthouse keeper too, before the accident."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Tobias wanted to be a lighthouse keeper too, before the accident."]
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
          "text": "- The causeway floods twice a month, and Mara times her supply runs around the tide table."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- The causeway to Harrow Point floods twice a month."]
        },
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Mara times her supply runs around the tide table, because the causeway floods twice a month."]
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
          "text": "- The new keeper could be someone from the mainland who's never seen the sea."
        },
        {
          "note": "brain-dump.md",
          "line": 17,
          "text": "- What if the relief keeper is scared of the water?"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- The relief keeper could be someone from the mainland who has never seen the sea and is scared of the water."]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u4",
      "action": "reject",
      "sources": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 11,
          "text": "- Mara keeps a dog called Skipper."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## Rejected",
          "lines": ["- Mara keeps a dog called Skipper. #status/rejected", "%% It makes her too cosy. %%"]
        }
      ],
      "edits": [],
      "status": "rejected"
    },
    {
      "id": "u5",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 20,
          "text": "- Tobias kept a tin of sea glass under his bed."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Tobias kept a tin of sea glass under his bed."]
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
              "text": "%% Agent, the flooding goes in idea-harrow-point, the supply runs in idea-mara-lighthouse. %%"
            },
            {
              "line": 18,
              "text": "%% Agent, these two are the same idea. Merge them into idea-mara-lighthouse. %%"
            },
            {
              "line": 21,
              "text": "%% Agent, migrate this. %%"
            }
          ]
        },
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "heading": null,
          "lines": [
            {
              "line": 12,
              "text": "%% Agent, reject the dog. It makes her too cosy. %%"
            }
          ]
        }
      ]
    }
  ],
  "skipped": []
}
JSON_EOF
