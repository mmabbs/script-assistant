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
mkdir -p project/Research project/llm-files/research-plans project/llm-files/research-findings/run-2026-10-08-1400-research/roman-aqueducts project/Concepts

cat > project/Concepts/concept-old-water-channel.md << 'NOTE_EOF'
---
title: Concept - The Old Water Channel
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
---

# Concept - The Old Water Channel

- The town still draws water from a channel older than the town.
- [r] How did the Romans build their aqueducts, and how were they kept running? #research/run-4
    %% The city of Rome and Roman Gaul. Up to the 3rd century AD. %%
NOTE_EOF

cat > project/llm-files/research-plans/research-plan-roman-aqueducts.md << 'PLAN_EOF'
---
title: Research Plan - Roman Aqueducts
run: run-2026-10-08-1400-research
request: "project/Concepts/concept-old-water-channel.md, line 9"
---

# Research Plan - Roman Aqueducts

Request: - [r] How did the Romans build their aqueducts, and how were they kept running? #research/run-4
Comment: %% The city of Rome and Roman Gaul. Up to the 3rd century AD. %%

## Every topic

- The city of Rome and Roman Gaul only.
- Up to the 3rd century AD.

## Topic 1: How the aqueducts were built

Questions:

1. How did builders keep the water flowing downhill over long distances?
2. Why were arches used, and what was used where a valley was too deep?

Waits on: nothing

## Topic 2: How the aqueducts were kept running

Questions:

3. Who was responsible for keeping the aqueducts working?
4. What upkeep did the channels need?

Waits on: nothing
PLAN_EOF

cat > project/llm-files/research-findings/run-2026-10-08-1400-research/roman-aqueducts/topic-1.md << 'T1_EOF'
# Findings - Topic 1: How the aqueducts were built

## Passage 1

The aqueduct that supplied Nîmes falls only about 12.6 metres over its whole length of about 50 kilometres, an average of about 25 centimetres per kilometre. Surveyors set this slope with levelling instruments over the whole route before building began.

Evidence: verified

Sources:
- https://www.nimes-heritage.example/aqueduct/survey-gradient (heritage service survey report, 2012)
- https://www.roman-engineering-journal.example/2015/gradients-in-gaul (peer-reviewed article, 2015)

## Passage 2

Arches carried the channel across valleys so the slope could stay steady. Where a valley was too deep for arches, as at Lyon, builders used inverted siphons: sealed lead pipes that ran down one side of the valley and up the other, with the water pushed up by its own pressure.

Evidence: verified

Sources:
- https://www.lyon-archaeology.example/aqueducts/siphons (city archaeology service page, 2016)
- https://www.ancient-texts-library.example/frontinus/de-aquaeductu (translation of Frontinus, written about 97 AD)

## Passage 3

A guild of channel keepers at Nîmes cut a tally mark into the channel wall after each cleaning, and some of the marks can still be counted.

Evidence: reported

Sources: none found

<!-- end of findings -->
T1_EOF

cat > project/llm-files/research-findings/run-2026-10-08-1400-research/roman-aqueducts/topic-2.md << 'T2_EOF'
# Findings - Topic 2: How the aqueducts were kept running

## Passage 1

In Rome, the water commissioner, the curator aquarum, was responsible for the aqueducts. Frontinus held the post from 97 AD and wrote a treatise on the system. He describes a staff of about 700 slaves, split between a public gang and an imperial gang, who repaired and cleaned the channels.

Evidence: verified

Sources:
- https://www.ancient-texts-library.example/frontinus/de-aquaeductu (translation of Frontinus, written about 97 AD)
- https://www.roman-water-review.example/2019/curator-aquarum (peer-reviewed article, 2019)

## Passage 2

Hard water left layers of calcium carbonate, called sinter, inside the channels. The layers narrowed the channel and had to be chipped out. In parts of the Nîmes aqueduct the deposits reached about 40 centimetres thick.

Evidence: verified

Sources:
- https://www.hydro-history.example/2020/sinter-deposits-nimes (peer-reviewed article, 2020)
- https://www.geoarchaeology-letters.example/2017/carbonate-layers (peer-reviewed article, 2017)

<!-- end of findings -->
T2_EOF
