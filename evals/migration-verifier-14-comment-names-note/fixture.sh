#!/usr/bin/env bash
set -euo pipefail

# Case 14, V5: the comment names a note, and the copy went elsewhere. The
# project as it stands after the migrator's pass of batch b1, before any
# pointer.
#
# u1 is planted: a split. The comment sends the chandlery to idea-harrow-point
# and the only-shop habit to idea-mara-habits. The habit copy went where it was
# told. The chandlery copy, word for word the source, went to
# idea-mara-lighthouse, a plausible home for a line about lamp paraffin. A
# comment that names a note and was not followed is a scope problem
# (spec-migration-verifier.md 04.4 item 2); the problem points at the misplaced
# copy.
#
# u2 is correct: "migrate this" names no note, so where it went is not judged,
# even though it sits in idea-mara-lighthouse beside u1's misplaced copy.
# u3 is correct: the comment names Tobias's note by description, and the copy
# went there.

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

- Fenwick's chandlery on the quay is the only place left that sells lamp paraffin, and it's the only shop in the village Mara will set foot in.
%% Agent, the chandlery goes in idea-harrow-point, the only-shop habit in idea-mara-habits. %%

- Mara sweeps the lamp room every morning before she eats.
%% Agent, migrate this. %%

- Tobias was afraid of the dark until he was ten.
%% Agent, put this with the rest of Tobias's material. %%
BD_EOF

cat > project/Ideas/idea-harrow-point.md << 'IDEA_EOF'
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- Harrow Point is a fishing village of about two hundred people.
- The harbour is too shallow now for anything bigger than a creel boat.

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
- Fenwick's chandlery on the quay is the only place left that sells lamp paraffin.
- Mara sweeps the lamp room every morning before she eats.

## Rejected
IDEA_EOF

cat > project/Ideas/idea-mara-habits.md << 'IDEA_EOF'
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits

- Mara walks the gallery every evening at dusk.
- The only shop in the village Mara will set foot in is Fenwick's chandlery on the quay.

## Rejected
IDEA_EOF

cat > project/Ideas/idea-tobias.md << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias worked summers on the ferry to the mainland.
- He kept a rowing boat tied up under the pier.
- Tobias was afraid of the dark until he was ten.

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
          "text": "- Fenwick's chandlery on the quay is the only place left that sells lamp paraffin, and it's the only shop in the village Mara will set foot in."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Fenwick's chandlery on the quay is the only place left that sells lamp paraffin."]
        },
        {
          "note": "Ideas/idea-mara-habits.md",
          "under": "# Idea - Mara Habits",
          "lines": ["- The only shop in the village Mara will set foot in is Fenwick's chandlery on the quay."]
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
          "text": "- Mara sweeps the lamp room every morning before she eats."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Mara sweeps the lamp room every morning before she eats."]
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
          "text": "- Tobias was afraid of the dark until he was ten."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Tobias was afraid of the dark until he was ten."]
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
              "text": "%% Agent, the chandlery goes in idea-harrow-point, the only-shop habit in idea-mara-habits. %%"
            },
            {
              "line": 14,
              "text": "%% Agent, migrate this. %%"
            },
            {
              "line": 17,
              "text": "%% Agent, put this with the rest of Tobias's material. %%"
            }
          ]
        }
      ]
    }
  ],
  "skipped": []
}
JSON_EOF
