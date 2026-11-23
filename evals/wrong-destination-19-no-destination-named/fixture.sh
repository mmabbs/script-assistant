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

- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional
- On the storm night the foghorn was already broken. #status/provisional
- The lamp's lens was cracked by a gull in 2003. #status/provisional
- Coyle closed the pub early that night, which he never does. #status/provisional
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

cat > project/Ideas/idea-storm-night.md << 'IDEA_EOF'
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night

## The lamp failure

- The lamp failed for eleven minutes.
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
