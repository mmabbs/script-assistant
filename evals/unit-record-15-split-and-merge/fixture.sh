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

### 2026-10-01

- Pell rings the harbour bell by hand at dusk. He learned it from Tobias, who used to do it for pocket money.

%% Agent, migrate this. The bell ringing goes in idea-harrow-point, the part about Tobias in idea-tobias. %%

- The lighthouse cat is called Ballast.
- Mara's cat, Ballast, has one eye and sleeps in the lamp room.

%% Agent, these two are one idea. Merge them into one unit in idea-mara-lighthouse. %%

- The lamp room smells of paraffin and wet wool. #status/provisional

%% Agent, the paraffin line goes in idea-mara-lighthouse too. %%
BD_EOF

cat > project/Ideas/idea-harrow-point.md << 'IDEA_EOF'
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## People

- Coyle runs the Drowned Bell.

## Getting in and out

- The ferry runs twice a week.
IDEA_EOF

cat > project/Ideas/idea-tobias.md << 'IDEA_EOF'
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias
IDEA_EOF

cat > project/Ideas/idea-mara-lighthouse.md << 'IDEA_EOF'
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
IDEA_EOF
