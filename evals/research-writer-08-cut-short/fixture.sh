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
mkdir -p project/Research project/llm-files/research-plans project/llm-files/research-findings/run-2026-10-09-1400-research/bathing-machines project/Concepts

cat > project/Concepts/concept-beach-huts.md << 'NOTE_EOF'
---
title: Concept - The Beach Huts
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
---

# Concept - The Beach Huts

- The row of beach huts below the cliff was once the town's bathing station.
- [r] How did the bathing machines at Victorian seaside resorts work? Who were the dippers who ran them, and what rules kept men and women apart on the beach? #research/run-5
    %% British resorts, 1840 to 1900. %%
NOTE_EOF

cat > project/llm-files/research-plans/research-plan-bathing-machines.md << 'PLAN_EOF'
---
title: Research Plan - Bathing Machines
run: run-2026-10-09-1400-research
request: "project/Concepts/concept-beach-huts.md, line 9"
---

# Research Plan - Bathing Machines

Request: - [r] How did the bathing machines at Victorian seaside resorts work? Who were the dippers who ran them, and what rules kept men and women apart on the beach? #research/run-5
Comment: %% British resorts, 1840 to 1900. %%

## Every topic

- British seaside resorts only.
- The years 1840 to 1900.

## Topic 1: The bathing machine

Questions:

1. What was a bathing machine, and how was it moved into the sea?
2. How did a bather use one?

Waits on: nothing

## Topic 2: The dippers

Questions:

3. Who were the dippers, and what did they do?
4. How was their work licensed or paid?

Waits on: nothing

## Topic 3: Keeping men and women apart

Questions:

5. What rules kept men and women apart on the beach?
6. When and how did mixed bathing become allowed?

Waits on: nothing
PLAN_EOF

# topic-2.md is cut short: it stops after a whole passage, with no closing line (spec 08 item 9)
cat > project/llm-files/research-findings/run-2026-10-09-1400-research/bathing-machines/topic-1.md << 'T1_EOF'
# Findings - Topic 1: The bathing machine

## Passage 1

A bathing machine was a small wooden hut on four large wheels, with a door at each end and steps down from the seaward door. A bather climbed in on the beach in ordinary clothes, and the machine was pulled out into the sea while the bather changed inside into a bathing costume. When the machine stopped, the bather went down the steps straight into the water, out of sight of the beach. Machines were painted in bright colours or stripes, and each carried its owner's name.

Evidence: verified

Sources:
- https://www.seaside-heritage.example/collections/bathing-machines (museum collection article, 2018)
- https://www.victorian-leisure-journal.example/2014/the-bathing-machine (peer-reviewed article, 2014)

## Passage 2

At most resorts a horse pulled the machine into the sea and back. The attendant, who owned or hired the machine, led the horse out until the water stood about 3 feet deep at the steps, unhitched it, and brought it round to the landward end ready to pull the machine back to the beach. At a few resorts with steep shingle beaches, the machines were hauled up and down on a cable by a winch on the shore instead of by a horse.

Evidence: verified

Sources:
- https://www.seaside-heritage.example/collections/bathing-machines (museum collection article, 2018)
- https://www.coastal-towns-archive.example/hastings/beach-engineering (local history society page, 2012)

Reliability: the society page covers one town and names the winch resorts without dates.

## Passage 3

Women bathers were helped into the water by female attendants called dippers, who stood in the sea beside the steps. Men's machines had male attendants, sometimes called bathers or guides.

Evidence: reported

Sources:
- https://www.victorian-leisure-journal.example/2014/the-bathing-machine (peer-reviewed article, 2014)

## Passage 4

A bather paid for a set time in the machine, usually half an hour, and the attendant rang a bell or waved a flag when the time was up. A bather who stayed too long paid for a second turn. On busy summer mornings at the large resorts, bathers queued on the beach for a free machine.

Evidence: reported

Sources:
- https://www.resort-guides-digitized.example/1865/brighton-visitors-guide (digitized resort guidebook, 1865)

<!-- end of findings -->
T1_EOF

cat > project/llm-files/research-findings/run-2026-10-09-1400-research/bathing-machines/topic-2.md << 'T2_EOF'
# Findings - Topic 2: The dippers

## Passage 1

Dippers were strong local women, often the wives and daughters of fishermen, who stood waist-deep in the sea for hours in all weather. Their work was to take each woman bather from the machine steps, lead her into the water, and plunge her under the waves, which was thought to be good for the health. The best-known dipper at Scarborough in the 1850s was Hannah Wrenfield, who worked the same stretch of beach for over thirty years and was said to have dipped several thousand women.

Evidence: reported

Sources:
- https://www.seaside-trades-history.example/occupations/dippers (local history society page, 2016)
- https://www.yorkshire-coast-archive.example/scarborough/beach-workers (digitized town records with catalogue notes, 1840s to 1860s)

Reliability: the claim about the number of women dipped comes from a local obituary.

## Passage 2

At the larger resorts dippers had to be licensed by the town commissioners. A licensed dipper wore a numbered brass badge on a strap across her shoulder, and the number was entered in the town's register of beach workers. The licence was renewed every May before the season opened.

Evidence: verified

Sources:
- https://www.east-sussex-records.example/brighton/beach-licences (county record office catalogue entry, 1850s to 1870s)
T2_EOF

cat > project/llm-files/research-findings/run-2026-10-09-1400-research/bathing-machines/topic-3.md << 'T3_EOF'
# Findings - Topic 3: Keeping men and women apart

## Passage 1

Most resorts set aside separate stretches of beach for men's and women's machines. Local bylaws made under the Town Police Clauses Act of 1847 gave town councils the power to set the bathing areas and to fine anyone who broke the rules. At many resorts the bylaws required the men's machines to stand at least 60 yards from the women's.

Evidence: verified

Sources:
- https://www.legal-history-review.example/2011/seaside-bylaws (peer-reviewed article, 2011)
- https://www.resort-guides-digitized.example/1865/brighton-visitors-guide (digitized resort guidebook, 1865)

## Passage 2

Men at many resorts bathed naked until the 1860s, which was one reason for keeping the sexes far apart. From the 1860s bylaws at most resorts required men to wear a costume, usually a one-piece garment covering the body from neck to knee.

Evidence: reported

Sources:
- https://www.victorian-leisure-journal.example/2014/the-bathing-machine (peer-reviewed article, 2014)
- https://www.legal-history-review.example/2011/seaside-bylaws (peer-reviewed article, 2011)

## Passage 3

Mixed bathing, with men and women in the water together, began to be allowed at some resorts in the 1890s, usually for families. The change spread slowly and was still opposed by some town councils into the 1900s. As mixed bathing spread, the bathing machine fell out of use and was replaced by fixed beach huts and tents on the sand.

Evidence: reported

Sources:
- https://www.legal-history-review.example/2011/seaside-bylaws (peer-reviewed article, 2011)
- https://www.seaside-heritage.example/collections/bathing-machines (museum collection article, 2018)

Reliability: the article says local practice varied widely and dates differ from town to town.

<!-- end of findings -->
T3_EOF
