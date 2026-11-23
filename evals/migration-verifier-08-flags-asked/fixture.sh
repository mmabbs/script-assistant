#!/usr/bin/env bash
set -euo pipefail

# Case 8, V3 at the flags call: flags asked for. The project as it stands after
# the run's writes, before any pointer, with the Edit guard's first-check flags.
# f1 to f4 were asked for: f1, f2, f3 by a comment, f4 by the typed request
# (the request is only in the prompt). f3 changes a fact, and its comment asked
# for exactly that change. f5 is the control: no record entry and no comment.
#
# Line numbers in verify-flags.json are as the notes stood when the run
# started. No line was added or removed above them, so they are the same now.

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

- Mara refuses to go out on a boat, ever. #status/committed
%% Agent, mark this one committed. %%
BD_EOF

cat > project/Ideas/idea-mara-lighthouse.md << 'IDEA_EOF'
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

- The Harrow Point light stands on a rock at the end of the headland.
- Mara lives alone in the keeper's cottage at the foot of the tower.

- Mara repaints the gallery railing every spring. It's the only job she enjoys.
%% Agent, please correct the spelling in that line. %%

## Rejected
IDEA_EOF

cat > project/Ideas/idea-tobias.md << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias drowned off the north jetty when Mara was nine.
- Tobias was afraid of the dark, like Mara.
- He kept a rowing boat tied up under the pier.

## Rejected
IDEA_EOF

cat > project/char-mara.md << 'CHAR_EOF'
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper
- **Age**: 34
%% Agent, Mara is thirty-four now, not thirty-two. Update this. %%

# Arc/Development

# Bio

## General

- Mara has kept the lighthouse for eleven years.
- [AGENT] Mara stays at Harrow Point because leaving would mean leaving the water where Tobias drowned.

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
CHAR_EOF

cat > project/.runs/run-2026-10-09-2100-migration/flags-1.json << 'JSON_EOF'
{
  "flags": [
    {
      "id": "f1",
      "rule": "writer-line-edited",
      "note": "Ideas/idea-mara-lighthouse.md",
      "before": "- Mara repaints the gallery railing evrey spring, its the only job she enjoys.",
      "after": "- Mara repaints the gallery railing every spring. It's the only job she enjoys.",
      "unit": "b1-u1"
    },
    {
      "id": "f2",
      "rule": "brain-dump-status-tag",
      "note": "brain-dump.md",
      "before": "- Mara refuses to go out on a boat, ever.",
      "after": "- Mara refuses to go out on a boat, ever. #status/committed",
      "unit": "b1-u2"
    },
    {
      "id": "f3",
      "rule": "writer-line-edited",
      "note": "char-mara.md",
      "before": "- **Age**: 32",
      "after": "- **Age**: 34",
      "unit": "b1-u3"
    },
    {
      "id": "f4",
      "rule": "agent-line-added",
      "note": "char-mara.md",
      "before": "",
      "after": "- [AGENT] Mara stays at Harrow Point because leaving would mean leaving the water where Tobias drowned.",
      "unit": "b1-u4"
    },
    {
      "id": "f5",
      "rule": "unexplained-change",
      "note": "Ideas/idea-tobias.md",
      "before": "- Tobias was afraid of the dark.",
      "after": "- Tobias was afraid of the dark, like Mara.",
      "unit": ""
    }
  ]
}
JSON_EOF

cat > project/.runs/run-2026-10-09-2100-migration/verify-flags.json << 'JSON_EOF'
{
  "flags": [
    {
      "id": "f1",
      "rule": "writer-line-edited",
      "note": "Ideas/idea-mara-lighthouse.md",
      "before": "- Mara repaints the gallery railing evrey spring, its the only job she enjoys.",
      "after": "- Mara repaints the gallery railing every spring. It's the only job she enjoys.",
      "unit": "b1-u1"
    },
    {
      "id": "f2",
      "rule": "brain-dump-status-tag",
      "note": "brain-dump.md",
      "before": "- Mara refuses to go out on a boat, ever.",
      "after": "- Mara refuses to go out on a boat, ever. #status/committed",
      "unit": "b1-u2"
    },
    {
      "id": "f3",
      "rule": "writer-line-edited",
      "note": "char-mara.md",
      "before": "- **Age**: 32",
      "after": "- **Age**: 34",
      "unit": "b1-u3"
    },
    {
      "id": "f4",
      "rule": "agent-line-added",
      "note": "char-mara.md",
      "before": "",
      "after": "- [AGENT] Mara stays at Harrow Point because leaving would mean leaving the water where Tobias drowned.",
      "unit": "b1-u4"
    },
    {
      "id": "f5",
      "rule": "unexplained-change",
      "note": "Ideas/idea-tobias.md",
      "before": "- Tobias was afraid of the dark.",
      "after": "- Tobias was afraid of the dark, like Mara.",
      "unit": ""
    }
  ],
  "units": {
    "b1-u1": {
      "id": "u1",
      "action": "edit",
      "sources": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 11,
          "text": "- Mara repaints the gallery railing evrey spring, its the only job she enjoys."
        }
      ],
      "copies": [],
      "edits": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 11,
          "before": "- Mara repaints the gallery railing evrey spring, its the only job she enjoys.",
          "after": "- Mara repaints the gallery railing every spring. It's the only job she enjoys."
        }
      ],
      "status": "tentative"
    },
    "b1-u2": {
      "id": "u2",
      "action": "edit",
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara refuses to go out on a boat, ever."
        }
      ],
      "copies": [],
      "edits": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "before": "- Mara refuses to go out on a boat, ever.",
          "after": "- Mara refuses to go out on a boat, ever. #status/committed"
        }
      ],
      "status": "committed"
    },
    "b1-u3": {
      "id": "u3",
      "action": "edit",
      "sources": [
        {
          "note": "char-mara.md",
          "line": 12,
          "text": "- **Age**: 32"
        }
      ],
      "copies": [],
      "edits": [
        {
          "note": "char-mara.md",
          "line": 12,
          "before": "- **Age**: 32",
          "after": "- **Age**: 34"
        }
      ],
      "status": "committed"
    },
    "b1-u4": {
      "id": "u4",
      "action": "edit",
      "sources": [],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": [
            "- [AGENT] Mara stays at Harrow Point because leaving would mean leaving the water where Tobias drowned."
          ]
        }
      ],
      "edits": [],
      "status": "committed"
    }
  }
}
JSON_EOF
