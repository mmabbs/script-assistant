#!/usr/bin/env bash
set -euo pipefail

# Case 21: the project as it stands when the retry run starts.
#
# The first run, run-2026-10-08-2100-migration, took the ### 2026-10-07 piece:
# the writer's comment sends both bullets to idea-lighthouse. Its unit for the
# green-ink line was kept: the copy sits in idea-lighthouse and the source line
# carries the Run manager's pointer. Its unit for the spare-key line was undone:
# no copy, no pointer. So the comment stayed off the handled list
# (spec-run-manager.md 07.1 item 9; 11 items 81 and 83), and the scan hands the
# piece to the migrator again.

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

### 2026-10-07

- The last keeper logged 38 nights of fog in her final winter, every one in green ink. [migrated-to:: [[Projects/project/Ideas/idea-lighthouse|idea-lighthouse]]]
- Mara finds the last keeper's spare key taped under the third stair from the top.

%% Agent, both of these belong in idea-lighthouse. %%
BD_EOF

cat > project/Ideas/idea-lighthouse.md << 'IDEA_EOF'
---
title: Idea - Lighthouse
type: [idea-note]
---

# Idea - Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
- The last keeper logged 38 nights of fog in her final winter, every one in green ink.
IDEA_EOF
