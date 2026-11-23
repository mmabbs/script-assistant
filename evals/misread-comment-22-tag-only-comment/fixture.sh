#!/usr/bin/env bash
set -euo pipefail

# Case 22: a comment that asks only for a status tag.
#
# The pane line's comment asks for a tag and nothing else, so the migrator adds
# the tag to the Brain Dump line, recorded as an edit unit, moves nothing, and
# asks in questions whether the line should move, naming idea-lighthouse.
# The tally line is the control: its comment asks for a tag and a move, so it
# gets both and lands in idea-tobias, provisional.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/_fixtures/rules"
if [ ! -d "$FIXTURES_DIR" ]; then
  echo "Cannot find _fixtures/rules" >&2
  exit 1
fi

mkdir -p rules
cp "$FIXTURES_DIR/migrator-rules.md" rules/migrator-rules.md

mkdir -p project/Ideas

cat > project/brain-dump.md << 'BD_EOF'
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-14

- The lamp room's north pane has a star-shaped crack, and Mara has never reported it to the lighthouse board.
%% Agent, tag this provisional. %%

- Tobias scratched a tally of his catches into the boathouse beam, and the last mark is only half cut.
%% Agent, tag this provisional and put it in idea-tobias. %%
BD_EOF

cat > project/Ideas/idea-lighthouse.md << 'IDEA_EOF'
---
title: Idea - Lighthouse
type: [idea-note]
---

# Idea - Lighthouse

## The lamp room

- The lamp room smells of paraffin and wet wool all winter.

## The tower

- The tower leans a few degrees toward the harbour, and the town jokes that it's homesick.
IDEA_EOF

cat > project/Ideas/idea-tobias.md << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

## Before the drowning

- Tobias fished alone, against his mother's wishes.
IDEA_EOF
