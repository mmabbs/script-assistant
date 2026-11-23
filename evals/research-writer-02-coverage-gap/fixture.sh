#!/usr/bin/env bash
set -euo pipefail

# Locate _fixtures/research relative to this script, fall back to absolute path
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FIXTURES_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)/_fixtures/research"
if [ ! -d "$FIXTURES_DIR" ]; then
  echo "Cannot find _fixtures/research" >&2
  exit 1
fi

# Copy the note template
mkdir -p templates
cp "$FIXTURES_DIR/research-template.md" templates/research-template.md
# The project's own template copy carries the hub link (spec 07 item 1)
sed -i.bak 's#^project:.*#project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"#' templates/research-template.md && rm templates/research-template.md.bak

# Create project files
mkdir -p project/Research project/llm-files/research-plans project/llm-files/research-findings/run-2026-10-08-1400-research/london-gas-lamps project/Ideas

cat > project/Ideas/idea-night-rounds.md << 'NOTE_EOF'
---
title: Idea - Night Rounds
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
---

# Idea - Night Rounds

- Opening image: the street goes dark one lamp at a time, at dawn.
- [r] How did London's gas street lamps work, and who looked after them? How many lamps did one man tend, and what was he paid? #research/run-4
    %% London only. The 1880s. %%
NOTE_EOF

cat > project/llm-files/research-plans/research-plan-london-gas-lamps.md << 'PLAN_EOF'
---
title: Research Plan - London Gas Lamps
run: run-2026-10-08-1400-research
request: "project/Ideas/idea-night-rounds.md, line 9"
---

# Research Plan - London Gas Lamps

Request: - [r] How did London's gas street lamps work, and who looked after them? How many lamps did one man tend, and what was he paid? #research/run-4
Comment: %% London only. The 1880s. %%

## Every topic

- London only.
- The 1880s.

## Topic 1: How the gas street lamps worked

Questions:

1. What fuel did the lamps burn, and how did it reach the lamp?
2. How was a lamp lit, and how was it put out?

Waits on: nothing

## Topic 2: The lamplighters

Questions:

3. How many lamps did one lamplighter look after?
4. What was a lamplighter paid?

Waits on: nothing
PLAN_EOF

cat > project/llm-files/research-findings/run-2026-10-08-1400-research/london-gas-lamps/topic-1.md << 'T1_EOF'
# Findings - Topic 1: How the gas street lamps worked

## Passage 1

The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern.

Evidence: verified

Sources:
- https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets (museum collection article, 2018)
- https://www.gas-history-society.example/papers/metropolitan-mains (society research paper, 2011)

## Passage 2

The lamplighter carried a long pole with a hook at the top for turning the gas tap, and a small oil-fed flame for lighting the burner. He lit his lamps on an evening round at dusk and turned them off on a second round at dawn.

Evidence: verified

Sources:
- https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets (museum collection article, 2018)

## Passage 3

The gas companies and parish vestries divided each district into rounds. A lamplighter's round covered about 70 lamps, and he walked it twice a day, at dusk and at dawn.

Evidence: reported

Sources:
- https://www.vestry-minutes.example/st-pancras/1884/lighting-committee (digitized parish vestry minutes, 1884)

Reliability: the minutes cover one parish.

<!-- end of findings -->
T1_EOF

cat > project/llm-files/research-findings/run-2026-10-08-1400-research/london-gas-lamps/topic-2.md << 'T2_EOF'
# Findings - Topic 2: The lamplighters

## Passage 1

Lamplighters were employed by the gas companies or by the parish vestries, not by the police. Besides lighting and putting out the lamps, they cleaned the lamp glass once a week and reported broken lamps to the vestry.

Evidence: verified

Sources:
- https://www.gas-history-society.example/papers/metropolitan-mains (society research paper, 2011)
- https://www.vestry-minutes.example/st-pancras/1884/lighting-committee (digitized parish vestry minutes, 1884)

## Passage 2

The evening round began about half an hour before sunset, so in winter a lamplighter started work in mid-afternoon. The dawn round began before first light.

Evidence: reported

Sources:
- https://www.london-streets-history.example/trades/lamplighter (local history society page, 2015)

## Passage 3

No source found in this search gave lamplighters' wages for the 1880s. A guide to the London Metropolitan Archives says vestry wage books survive for some parishes but have not been put online.

Evidence: verified

Sources:
- https://www.lma-guide.example/sources/vestry-wage-books (archive research guide, 2021)

<!-- end of findings -->
T2_EOF
