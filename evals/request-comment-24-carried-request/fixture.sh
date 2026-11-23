#!/usr/bin/env bash
set -euo pipefail

# Case 24: a request carried over as a comment.
#
# The run of 2026-10-21 had a typed request: "everything about the fog bell goes
# into idea-lighthouse, tagged or not". Its unit for the drowning line was undone,
# so close wrote the request as an [AGENT] comment under that line
# (spec-run-manager.md 11 item 96). The writer added the wedding-rings line after
# that run. It has no tag and no comment, so nothing asks for it, though the
# request's words would cover it (spec-migrator.md 07 item 6: for the line above
# it only).

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

### 2026-10-20

- The fog bell rings on its own the night before every drowning.
    %% [AGENT] Your request from the migration run of 2026-10-21, for this line: "everything about the fog bell goes into idea-lighthouse, tagged or not" %%
- The fog bell was cast from melted wedding rings.
BD_EOF

cat > project/Ideas/idea-lighthouse.md << 'IDEA_EOF'
---
title: Idea - Lighthouse
type: [idea-note]
---

# Idea - Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
IDEA_EOF
