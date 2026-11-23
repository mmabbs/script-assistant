#!/usr/bin/env bash
set -euo pipefail

# Locate _fixtures/rules relative to this script, fall back to absolute path
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/_fixtures/rules"
if [ ! -d "$FIXTURES_DIR" ]; then
  echo "Cannot find _fixtures/rules" >&2
  exit 1
fi

# Copy rules files
mkdir -p rules
cp "$FIXTURES_DIR/migrator-rules.md" rules/migrator-rules.md

# Create project files
mkdir -p project/Ideas

cat > project/brain-dump.md << 'BD_EOF'
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- The town is called Harrow Point and it has exactly one road in, which floods at spring tide.
- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days.
- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute.
- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow.
- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?
- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go.
- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him.

%% migrate all the bullets between "- The town is called Harrow Point" to "Could be that the harbourmaster" %%

%% Agent, these go in idea-harrow-point. %%

### 2026-09-30

- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night.
- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock.
- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close.
- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing.
- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding.
- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet.
- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years.

%% migrate all the bullets between "- The storm night" to "I keep coming back" %%

%% Agent, these go in idea-storm-night. %%
BD_EOF

cat > project/Ideas/idea-harrow-point.md << 'IDEA_EOF'
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point
IDEA_EOF

cat > project/Ideas/idea-storm-night.md << 'IDEA_EOF'
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night
IDEA_EOF
