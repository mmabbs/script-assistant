#!/usr/bin/env bash
set -euo pipefail

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

%% Agent, anything I tag provisional under these three dates goes in idea-harrow-point. Leave the untagged lines where they are. %%

### 2026-10-01

- The bakery only opens when the baker's knee allows it.
- The post office doubles as the undertaker's. #status/provisional
- There are more boats than people in winter.
- Somebody repaints the war memorial every spring and nobody knows who.
- The chemist, Ferris, fills prescriptions from memory. #status/provisional
- Fog comes in from the east, which is the wrong direction.

### 2026-09-30

- Half the houses on Quay Street are let to a film company that never came.
- The primary school has nine pupils, all cousins. #status/provisional
- The church clock runs four minutes fast on purpose.
- Gulls have learned to open the bins outside the Drowned Bell.
- A seal called Mister Hale comes into the harbour every October. #status/provisional
- The bus shelter has had the same timetable since 1998.

### 2026-09-28

- The council sold the fish market roof for scrap in 2011. #status/provisional
- There's a rumour the vicar's wife ran the smuggling.
- Nobody locks their doors except Pell.
- The cliff path lost twelve metres to the sea last winter. #status/provisional
- Everyone's grandmother claims to have been the May Queen.
- The phone box is listed, so they can't remove it.
BD_EOF

cat > project/Ideas/idea-harrow-point.md << 'IDEA_EOF'
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point
IDEA_EOF
