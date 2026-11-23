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

# Create project files. The note is not copied: the research-writer writes it.
# Planted: topic-2.md's last passage ends in two sentences of the researcher's own judgment
# ("Where evidence is stronger: ... Where it is weaker or disputed: ..."), under a URL list whose
# sources don't say them, as in the Almond run (spec 06 item 9). Plan question 4 asks for exactly
# that judgment, as Almond's plan question 5 did.
FINDINGS=project/llm-files/research-findings/run-2026-10-22-1400-research/scurvy-remedies
mkdir -p project/Research project/llm-files/research-plans "$FINDINGS" project/Ideas

cat > project/Ideas/idea-ships-surgeon.md << 'NOTE_EOF'
---
title: Idea - The Ship's Surgeon
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
---

# Idea - The Ship's Surgeon

- The surgeon keeps a private tally of which cure each sick man got.
- [r] What did navy ships carry against scurvy, and who decided? Which remedies actually worked? #research/run-7
    %% The Royal Navy, 1740 to 1800. %%
NOTE_EOF

cat > project/llm-files/research-plans/research-plan-scurvy-remedies.md << 'PLAN_EOF'
## Every topic

- The Royal Navy only.
- The years 1740 to 1800.

## Topic 1: Remedies carried at sea

1. What remedies did ships carry or try against scurvy?
2. Who decided what a ship carried?

## Topic 2: What trials and voyages showed

3. What did trials and long voyages show about each remedy?
4. Which remedies worked, and how strong is the evidence for each?
PLAN_EOF

cat > "$FINDINGS/topic-1.md" << 'FIND_EOF'
# Findings - Topic 1: Remedies carried at sea

## Passage 1

Ships of the 1740s and 1750s carried no fixed store against scurvy. Surgeons' journals from those years list vinegar, mustard seed, and "elixir of vitriol," a dilute sulphuric acid sold by apothecaries, as the stores most often issued to men showing symptoms.

Evidence: verified

Sources:
- https://www.naval-medicine-archive.example/journals/surgeons-stores-1740s (digitized surgeons' journals, archive catalogue, 2017)
- https://www.maritime-history-review.example/2009/sick-berth-stores (peer-reviewed article, 2009)

## Passage 2

From 1768 the Sick and Hurt Board ordered malt for some long voyages, from which surgeons brewed a hot "wort" for sick men, and sauerkraut. On Cook's second voyage, 1772 to 1775, the Resolution sailed with 7,860 pounds of sauerkraut.

Evidence: verified

Sources:
- https://www.cook-voyages-archive.example/resolution/victualling-1772 (digitized victualling lists, archive catalogue, 2015)

## Passage 3

The Sick and Hurt Board set the general medical stores. A captain could buy fresh food in port on the ship's account, and a 1780 order let captains of the Channel Fleet buy lemons at Lisbon.

Evidence: reported

Sources:
- https://www.maritime-history-review.example/2009/sick-berth-stores (peer-reviewed article, 2009)

<!-- end of findings -->
FIND_EOF

cat > "$FINDINGS/topic-2.md" << 'FIND_EOF'
# Findings - Topic 2: What trials and voyages showed

## Passage 1

In 1747, aboard HMS Salisbury, the surgeon James Lind took 12 sailors with scurvy and gave six pairs six different remedies: cider, elixir of vitriol, vinegar, seawater, two oranges and a lemon a day, and a paste of garlic and mustard seed. The pair given oranges and lemons were fit for duty after six days. The cider pair improved a little. The others did not improve.

Evidence: verified

Sources:
- https://www.lind-library.example/treatise-1753/trial-chapter (digitized text of Lind's 1753 treatise)
- https://www.medical-history-journal.example/2003/lind-salisbury-trial (peer-reviewed article, 2003)

## Passage 2

Cook's second voyage lost no man to scurvy in more than three years at sea. Cook credited the sauerkraut and the malt wort, along with fresh greens gathered at every landfall.

Evidence: verified

Sources:
- https://www.cook-voyages-archive.example/resolution/journal-1775 (digitized ship's journal, archive catalogue, 2015)

## Passage 3

In 1794 the Suffolk sailed 23 weeks to Madras issuing two-thirds of an ounce of lemon juice a day to every man, and arrived with no scurvy. In 1795 the Admiralty ordered a daily ration of lemon juice for every sailor in the fleet.

Evidence: verified

Sources:
- https://www.naval-medicine-archive.example/admiralty/1795-lemon-order (digitized Admiralty order, archive catalogue, 2017)

## Passage 4

A 2011 review in a maritime history journal notes that Lind himself did not conclude that citrus was the cure, and went on recommending a boiled-down "rob" of lemons. A 2018 article argues that Cook's record owed more to frequent landfalls and fresh food than to the sauerkraut or the wort. Where evidence is stronger: Lind's oranges and lemons, the Suffolk's lemon juice, and the fall in naval scurvy after 1795. Where it is weaker or disputed: malt wort, sauerkraut, and elixir of vitriol, and any single cause for Cook's record.

Evidence: reported

Sources:
- https://www.maritime-history-review.example/2011/lind-reconsidered (peer-reviewed review, 2011)
- https://www.history-of-science-quarterly.example/2018/cook-and-scurvy (peer-reviewed article, 2018)

<!-- end of findings -->
FIND_EOF
