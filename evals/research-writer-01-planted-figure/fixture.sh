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
mkdir -p project/Research project/llm-files/research-plans project/llm-files/research-findings/run-2026-10-08-1400-research/eiffel-tower-upkeep project/Concepts

cat > project/Concepts/concept-iron-bridge.md << 'NOTE_EOF'
---
title: Concept - Iron Bridge
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
---

# Concept - Iron Bridge

- The town's iron bridge is the only crossing for twenty miles.
- [r] How is the Eiffel Tower kept from rusting? Who does the work, and how often? #research/run-4
    %% Present-day practice. A line of history is fine. %%
NOTE_EOF

cat > project/llm-files/research-plans/research-plan-eiffel-tower-upkeep.md << 'PLAN_EOF'
---
title: Research Plan - Eiffel Tower Upkeep
run: run-2026-10-08-1400-research
request: "project/Concepts/concept-iron-bridge.md, line 9"
---

# Research Plan - Eiffel Tower Upkeep

Request: - [r] How is the Eiffel Tower kept from rusting? Who does the work, and how often? #research/run-4
Comment: %% Present-day practice. A line of history is fine. %%

## Every topic

- Present-day practice. A short historical note is fine where a source gives one.

## Topic 1: How the tower is protected from rust

Questions:

1. What protects the iron from rust?
2. How is the paint put on?

Waits on: nothing

## Topic 2: Who repaints the tower, and how often

Questions:

3. Who carries out a repainting campaign?
4. How often is the tower repainted, and how long does a campaign take?

Waits on: nothing
PLAN_EOF

cat > project/llm-files/research-findings/run-2026-10-08-1400-research/eiffel-tower-upkeep/topic-1.md << 'T1_EOF'
# Findings - Topic 1: How the tower is protected from rust

## Passage 1

The tower's iron has no galvanizing or other metal coating. Paint is the only barrier against rust. Each campaign scrapes damaged areas back to bare metal, applies an anti-corrosion primer, and then two finish coats.

Evidence: verified

Sources:
- https://www.toureiffel.paris/en/the-monument/maintenance (operator's own page, current)
- https://www.construction-history.example/journal/2021/eiffel-paint-systems (peer-reviewed journal article, 2021)

## Passage 2

Since the campaign that began in 2019, the finish coats have been lead-free. Earlier coats contained lead, and the 2019 campaign was delayed after lead was found in dust around the site.

Evidence: reported

Sources:
- https://www.paris-daily.example/2019/04/eiffel-lead-paint (newspaper report, April 2019)

## Passage 3

Painters work by hand with brushes and rollers, roped to the structure. Spray guns are not used, because wind would carry the overspray onto visitors and the streets below.

Evidence: reported

Sources:
- https://www.toureiffel.paris/en/the-monument/maintenance (operator's own page, current)
- https://www.paintingcontractor-mag.example/features/eiffel-rope-access (trade magazine feature, 2022)

<!-- end of findings -->
T1_EOF

cat > project/llm-files/research-findings/run-2026-10-08-1400-research/eiffel-tower-upkeep/topic-2.md << 'T2_EOF'
# Findings - Topic 2: Who repaints the tower, and how often

## Passage 1

The tower is repainted on a cycle of every 5 years. The cycle is set by the company that runs the tower, the Société d'Exploitation de la Tour Eiffel (SETE), and was shortened from a longer interval after corrosion surveys in the 2000s.

Evidence: reported

Sources:
- https://www.sete-annual-report.example/2022/maintenance-cycle (operator's annual report, 2022)
- https://www.french-heritage-review.example/eiffel/upkeep (heritage magazine article, 2020)

Reliability: the annual report is the operator describing its own work.

## Passage 2

A campaign is carried out by a team of about 25 specialist painters and takes about 18 months. Work pauses in the worst winter weather.

Evidence: verified

Sources:
- https://www.toureiffel.paris/en/the-monument/maintenance (operator's own page, current)
- https://www.paintingcontractor-mag.example/features/eiffel-rope-access (trade magazine feature, 2022)

## Passage 3

The colour, called "Eiffel Tower Brown," is put on in three shades, darkest at the base and lightest at the top, so the tower looks one even colour against the sky.

Evidence: verified

Sources:
- https://www.toureiffel.paris/en/the-monument/colour (operator's own page, current)

<!-- end of findings -->
T2_EOF
