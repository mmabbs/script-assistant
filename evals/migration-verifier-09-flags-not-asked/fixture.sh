#!/usr/bin/env bash
set -euo pipefail

# Case 9, V6 at the flags call: flags not asked for. The project as it stands
# after the run's writes, before any pointer, with the Edit guard's first-check
# flags. No typed request. f1, f2, f3 were not asked for: f1 has no comment and
# drops "maybe"; f2 has no record entry and no comment; f3's comment asked for
# spelling, but "may" became "will". f4 is the control: a typo fix its comment
# asked for.
#
# Nothing in this run came from the Brain Dump doc, so it has no new lines.
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
BD_EOF

cat > project/Ideas/idea-mara-lighthouse.md << 'IDEA_EOF'
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

- The causeway floods at every spring tide, twice a month.
- The Harrow Point light stands on a rock at the end of the headland.
- Mara owes the harbour board two years' rent on the keeper's cottage.

- Mara will sell the lighthouse lens to pay the debt.
%% Agent, please correct the spelling in that line. %%

## Rejected
IDEA_EOF

cat > project/Ideas/idea-tobias.md << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias worked summers on the ferry to the mainland.
- Tobias was afraid of the dark, like Mara.
- He kept a rowing boat tied up under the pier.

## Rejected
IDEA_EOF

cat > project/Ideas/idea-harrow-point.md << 'IDEA_EOF'
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- Harrow Point is a fishing village of about two hundred people.
- The pub on the quay is called the Drowned Anchor, run by a widower named Cal Brodie and his daughter.
%% Agent, fix the typo. %%

## Rejected
IDEA_EOF

cat > project/.runs/run-2026-10-09-2100-migration/flags-1.json << 'JSON_EOF'
{
  "flags": [
    {
      "id": "f1",
      "rule": "writer-line-edited",
      "note": "Ideas/idea-mara-lighthouse.md",
      "before": "- the causeway floods at spring tides, maybe twice a month",
      "after": "- The causeway floods at every spring tide, twice a month.",
      "unit": "b1-u1"
    },
    {
      "id": "f2",
      "rule": "unexplained-change",
      "note": "Ideas/idea-tobias.md",
      "before": "- Tobias was afraid of the dark.",
      "after": "- Tobias was afraid of the dark, like Mara.",
      "unit": ""
    },
    {
      "id": "f3",
      "rule": "writer-line-edited",
      "note": "Ideas/idea-mara-lighthouse.md",
      "before": "- Mara may sell the lihgthouse lens to pay the debt.",
      "after": "- Mara will sell the lighthouse lens to pay the debt.",
      "unit": "b1-u2"
    },
    {
      "id": "f4",
      "rule": "writer-line-edited",
      "note": "Ideas/idea-harrow-point.md",
      "before": "- The pub on the quay is called the Drowned Anchor, run by a widower named Cal Brodie and his dauhgter.",
      "after": "- The pub on the quay is called the Drowned Anchor, run by a widower named Cal Brodie and his daughter.",
      "unit": "b1-u3"
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
      "before": "- the causeway floods at spring tides, maybe twice a month",
      "after": "- The causeway floods at every spring tide, twice a month.",
      "unit": "b1-u1"
    },
    {
      "id": "f2",
      "rule": "unexplained-change",
      "note": "Ideas/idea-tobias.md",
      "before": "- Tobias was afraid of the dark.",
      "after": "- Tobias was afraid of the dark, like Mara.",
      "unit": ""
    },
    {
      "id": "f3",
      "rule": "writer-line-edited",
      "note": "Ideas/idea-mara-lighthouse.md",
      "before": "- Mara may sell the lihgthouse lens to pay the debt.",
      "after": "- Mara will sell the lighthouse lens to pay the debt.",
      "unit": "b1-u2"
    },
    {
      "id": "f4",
      "rule": "writer-line-edited",
      "note": "Ideas/idea-harrow-point.md",
      "before": "- The pub on the quay is called the Drowned Anchor, run by a widower named Cal Brodie and his dauhgter.",
      "after": "- The pub on the quay is called the Drowned Anchor, run by a widower named Cal Brodie and his daughter.",
      "unit": "b1-u3"
    }
  ],
  "units": {
    "b1-u1": {
      "id": "u1",
      "action": "edit",
      "sources": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 8,
          "text": "- the causeway floods at spring tides, maybe twice a month"
        }
      ],
      "copies": [],
      "edits": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 8,
          "before": "- the causeway floods at spring tides, maybe twice a month",
          "after": "- The causeway floods at every spring tide, twice a month."
        }
      ],
      "status": "tentative"
    },
    "b1-u2": {
      "id": "u2",
      "action": "edit",
      "sources": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 12,
          "text": "- Mara may sell the lihgthouse lens to pay the debt."
        }
      ],
      "copies": [],
      "edits": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "line": 12,
          "before": "- Mara may sell the lihgthouse lens to pay the debt.",
          "after": "- Mara will sell the lighthouse lens to pay the debt."
        }
      ],
      "status": "tentative"
    },
    "b1-u3": {
      "id": "u3",
      "action": "edit",
      "sources": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "line": 9,
          "text": "- The pub on the quay is called the Drowned Anchor, run by a widower named Cal Brodie and his dauhgter."
        }
      ],
      "copies": [],
      "edits": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "line": 9,
          "before": "- The pub on the quay is called the Drowned Anchor, run by a widower named Cal Brodie and his dauhgter.",
          "after": "- The pub on the quay is called the Drowned Anchor, run by a widower named Cal Brodie and his daughter."
        }
      ],
      "status": "tentative"
    }
  }
}
JSON_EOF
