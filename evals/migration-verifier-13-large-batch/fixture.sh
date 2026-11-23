#!/usr/bin/env bash
set -euo pipefail

# Case 13, scale: twenty units over three date headings, three planted errors.
# The project as it stands after the migrator's pass of batch b1, before any
# pointer. Built by hand from the list below; every other unit is correct.
#
#   u8  (### 2026-10-07): the range comment covers the bullets from
#       "- Tobias taught Mara" to "- Tobias wanted to leave". The untagged
#       bullet just below the range, "What if Mara blames herself...", was
#       migrated too: a migration nobody asked for (scope). Its copy is
#       faithful, and the comment sits below it.
#   u11 (### 2026-10-08): a split. The idea-mara-lighthouse copy keeps
#       "maybe called Ewan"; the idea-harrow-point copy uses "Ewan" as settled
#       (lost-detail; migrator-rules.md 02.2, a hedged name).
#   u16 (### 2026-10-09): "every second Sunday" became "every Sunday"
#       (lost-detail).
#
# Decoys, all correct: u10's Area Note copy drops "I think", a note-to-self,
# from a committed line (migrator-rules.md 02.3); the three untagged lines
# under ### 2026-10-08 have no tag and no comment, so nothing asked for them;
# u9, u12, u13, u14 name no destination, so where they went is not judged.
#
# Piece sizes (CONTRACT.md 5.2 item 11): 2026-10-07 holds a comment, so all 8
# bullets count; 2026-10-08 has no comment, so its 6 tagged bullets count;
# 2026-10-09 holds comments, so all 6 count. 20 in all: one batch.

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

### 2026-10-07

- Tobias taught Mara to tie a bowline on the jetty steps.
- Tobias was saving for an outboard motor for the rowing boat.
- Tobias rowed across to the seal rocks on calm evenings.
- Tobias could name every ship by the sound of its engine.
- Maybe Tobias owed money to someone on the mainland.
- Tobias hated the foghorn and slept with wax in his ears.
- Tobias wanted to leave Harrow Point and work the North Sea rigs.
- What if Mara blames herself for not going with him that night?

%% Agent, migrate all the bullets between "- Tobias taught Mara" and "- Tobias wanted to leave" to idea-tobias. %%

### 2026-10-08

- Mara keeps the lamp lens polished with her mother's old silk scarf. #status/committed
- I think Mara only ever drinks tea, never coffee, since Tobias died. #status/committed
- What if the lens is worth more than the lighthouse?
- The relief keeper, maybe called Ewan, arrives each March and lodges above the pub on the quay. #status/provisional
- Mara won't let anyone else wind the clockwork. #status/committed
- Something about the gulls nesting on the gallery.
- The harbour freezes over in hard winters. #status/provisional
- Mara reads the shipping forecast aloud to an empty room every night. #status/provisional
- Check how often relief keepers actually rotated.

### 2026-10-09

- Tobias's rowing boat was never found, only one oar.
%% Agent, idea-tobias. %%

- Mara rows out to the seal rocks every second Sunday, the way Tobias did.
%% Agent, idea-mara-habits. %%

- The pub on the quay stops serving at nine in winter.
%% Agent, idea-harrow-point. %%

- Maybe the lighthouse is haunted, or maybe Mara just wants it to be.
%% Agent, idea-mara-lighthouse. %%

- The Board sends an inspector twice a year, in April and October.
%% Agent, idea-mara-lighthouse. %%

- Mara's hands shake when she climbs the last flight of stairs. #status/committed
%% Agent, char-mara. %%
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
- Mara polishes the lamp lens with her mother's old silk scarf.
- Since Tobias died, Mara drinks only tea, never coffee.
- Mara won't let anyone else wind the lamp's clockwork.
- Mara's hands shake when she climbs the last flight of stairs in the tower.

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

- Tobias worked summers on the ferry to the mainland.
- He kept a rowing boat tied up under the pier.
- Tobias taught Mara to tie a bowline on the jetty steps.
- Tobias was saving for an outboard motor for the rowing boat.
- Tobias rowed across to the seal rocks on calm evenings.
- Tobias could name every ship by the sound of its engine.
- Maybe Tobias owed money to someone on the mainland.
- Tobias hated the foghorn and slept with wax in his ears.
- Tobias wanted to leave Harrow Point and work the North Sea rigs.
- What if Mara blames herself for not going with Tobias that night?
- Tobias's rowing boat was never found, only one oar.

## Rejected
IDEA_EOF

cat > project/Ideas/idea-mara-habits.md << 'IDEA_EOF'
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits

- Mara walks the gallery every evening at dusk.
- Mara reads the shipping forecast aloud to an empty room every night. #status/provisional
- Mara rows out to the seal rocks every Sunday, the way Tobias did.

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
- The relief keeper, maybe called Ewan, arrives each March. #status/provisional
- Maybe the lighthouse is haunted, or maybe Mara just wants it to be.
- The Board sends an inspector to the lighthouse twice a year, in April and October.

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
- Ewan, the relief keeper, lodges above the pub on the quay. #status/provisional
- The harbour freezes over in hard winters. #status/provisional
- The pub on the quay stops serving at nine in winter.

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
          "text": "- Tobias taught Mara to tie a bowline on the jetty steps."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": [
            "- Tobias taught Mara to tie a bowline on the jetty steps."
          ]
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
          "line": 11,
          "text": "- Tobias was saving for an outboard motor for the rowing boat."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": [
            "- Tobias was saving for an outboard motor for the rowing boat."
          ]
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
          "line": 12,
          "text": "- Tobias rowed across to the seal rocks on calm evenings."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": [
            "- Tobias rowed across to the seal rocks on calm evenings."
          ]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u4",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- Tobias could name every ship by the sound of its engine."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": [
            "- Tobias could name every ship by the sound of its engine."
          ]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u5",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 14,
          "text": "- Maybe Tobias owed money to someone on the mainland."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": [
            "- Maybe Tobias owed money to someone on the mainland."
          ]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u6",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 15,
          "text": "- Tobias hated the foghorn and slept with wax in his ears."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": [
            "- Tobias hated the foghorn and slept with wax in his ears."
          ]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u7",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 16,
          "text": "- Tobias wanted to leave Harrow Point and work the North Sea rigs."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": [
            "- Tobias wanted to leave Harrow Point and work the North Sea rigs."
          ]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u8",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 17,
          "text": "- What if Mara blames herself for not going with him that night?"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": [
            "- What if Mara blames herself for not going with Tobias that night?"
          ]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u9",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 23,
          "text": "- Mara keeps the lamp lens polished with her mother's old silk scarf. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": [
            "- Mara polishes the lamp lens with her mother's old silk scarf."
          ]
        }
      ],
      "edits": [],
      "status": "committed"
    },
    {
      "id": "u10",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 24,
          "text": "- I think Mara only ever drinks tea, never coffee, since Tobias died. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": [
            "- Since Tobias died, Mara drinks only tea, never coffee."
          ]
        }
      ],
      "edits": [],
      "status": "committed"
    },
    {
      "id": "u11",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 26,
          "text": "- The relief keeper, maybe called Ewan, arrives each March and lodges above the pub on the quay. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "- The relief keeper, maybe called Ewan, arrives each March. #status/provisional"
          ]
        },
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- Ewan, the relief keeper, lodges above the pub on the quay. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional"
    },
    {
      "id": "u12",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 27,
          "text": "- Mara won't let anyone else wind the clockwork. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": [
            "- Mara won't let anyone else wind the lamp's clockwork."
          ]
        }
      ],
      "edits": [],
      "status": "committed"
    },
    {
      "id": "u13",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 29,
          "text": "- The harbour freezes over in hard winters. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- The harbour freezes over in hard winters. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional"
    },
    {
      "id": "u14",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 30,
          "text": "- Mara reads the shipping forecast aloud to an empty room every night. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-habits.md",
          "under": "# Idea - Mara Habits",
          "lines": [
            "- Mara reads the shipping forecast aloud to an empty room every night. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional"
    },
    {
      "id": "u15",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 35,
          "text": "- Tobias's rowing boat was never found, only one oar."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": [
            "- Tobias's rowing boat was never found, only one oar."
          ]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u16",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 38,
          "text": "- Mara rows out to the seal rocks every second Sunday, the way Tobias did."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-habits.md",
          "under": "# Idea - Mara Habits",
          "lines": [
            "- Mara rows out to the seal rocks every Sunday, the way Tobias did."
          ]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u17",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 41,
          "text": "- The pub on the quay stops serving at nine in winter."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- The pub on the quay stops serving at nine in winter."
          ]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u18",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 44,
          "text": "- Maybe the lighthouse is haunted, or maybe Mara just wants it to be."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "- Maybe the lighthouse is haunted, or maybe Mara just wants it to be."
          ]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u19",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 47,
          "text": "- The Board sends an inspector twice a year, in April and October."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "- The Board sends an inspector to the lighthouse twice a year, in April and October."
          ]
        }
      ],
      "edits": [],
      "status": "tentative"
    },
    {
      "id": "u20",
      "action": "migrate",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 50,
          "text": "- Mara's hands shake when she climbs the last flight of stairs. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": [
            "- Mara's hands shake when she climbs the last flight of stairs in the tower."
          ]
        }
      ],
      "edits": [],
      "status": "committed"
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
          "heading": "### 2026-10-07",
          "lines": [
            {
              "line": 19,
              "text": "%% Agent, migrate all the bullets between \"- Tobias taught Mara\" and \"- Tobias wanted to leave\" to idea-tobias. %%"
            }
          ]
        },
        {
          "note": "brain-dump.md",
          "heading": "### 2026-10-08",
          "lines": [
            {
              "line": 23,
              "text": "- Mara keeps the lamp lens polished with her mother's old silk scarf. #status/committed"
            },
            {
              "line": 24,
              "text": "- I think Mara only ever drinks tea, never coffee, since Tobias died. #status/committed"
            },
            {
              "line": 26,
              "text": "- The relief keeper, maybe called Ewan, arrives each March and lodges above the pub on the quay. #status/provisional"
            },
            {
              "line": 27,
              "text": "- Mara won't let anyone else wind the clockwork. #status/committed"
            },
            {
              "line": 29,
              "text": "- The harbour freezes over in hard winters. #status/provisional"
            },
            {
              "line": 30,
              "text": "- Mara reads the shipping forecast aloud to an empty room every night. #status/provisional"
            }
          ]
        },
        {
          "note": "brain-dump.md",
          "heading": "### 2026-10-09",
          "lines": [
            {
              "line": 36,
              "text": "%% Agent, idea-tobias. %%"
            },
            {
              "line": 39,
              "text": "%% Agent, idea-mara-habits. %%"
            },
            {
              "line": 42,
              "text": "%% Agent, idea-harrow-point. %%"
            },
            {
              "line": 45,
              "text": "%% Agent, idea-mara-lighthouse. %%"
            },
            {
              "line": 48,
              "text": "%% Agent, idea-mara-lighthouse. %%"
            },
            {
              "line": 50,
              "text": "- Mara's hands shake when she climbs the last flight of stairs. #status/committed"
            },
            {
              "line": 51,
              "text": "%% Agent, char-mara. %%"
            }
          ]
        }
      ]
    }
  ],
  "skipped": []
}
JSON_EOF
