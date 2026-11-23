#!/usr/bin/env bash
set -euo pipefail

# The Almond request from the run of 2026-10-18 (Almond/.runs/run-2026-10-18-1807-research/requests.json),
# word for word, at its line, 14, in brain-dump.md. It had no comment. The lines above it are Almond's
# brain-dump.md as it stood, with the request still open. Nothing else from Almond is copied.
mkdir -p project/llm-files/research-plans run

cat > project/brain-dump.md << 'NOTE_EOF'
---
title: Brain Dump
aliases: [Brain Dump]
project:
created: 2026-09-21 12:33
modified: 2026-10-15 17:58
type: [brain-dump]
---

# Brain Dump

## 2026-10-14

- [r] Is anxiety "contagious"? #research/run-1
NOTE_EOF

# The request must sit on line 14, as the prompt says.
if [ "$(sed -n 14p project/brain-dump.md)" != '- [r] Is anxiety "contagious"? #research/run-1' ]; then
  echo "fixture.sh: the request is not on line 14" >&2
  exit 1
fi
