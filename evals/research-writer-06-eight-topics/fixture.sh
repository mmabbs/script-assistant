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
mkdir -p project/Research project/llm-files/research-plans project/llm-files/research-findings/run-2026-10-09-1400-research/ice-trade project/Ideas

cat > project/Ideas/idea-ice-ship.md << 'NOTE_EOF'
---
title: Idea - The Ice Ship
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
---

# Idea - The Ice Ship

- A ship in the harbour with a hold full of melting ice.
- [r] How did the old ice trade work, from a frozen New England pond to a hot foreign port? How was the ice cut, stored, and loaded, how much melted on the voyage, and how was it kept once it landed? Who did the work, who bought the ice and for how much, and what ended the trade? #research/run-5
    %% The New England trade by sea, start to finish. %%
NOTE_EOF

cat > project/llm-files/research-plans/research-plan-ice-trade.md << 'PLAN_EOF'
---
title: Research Plan - Ice Trade
run: run-2026-10-09-1400-research
request: "project/Ideas/idea-ice-ship.md, line 9"
---

# Research Plan - Ice Trade

Request: - [r] How did the old ice trade work, from a frozen New England pond to a hot foreign port? How was the ice cut, stored, and loaded, how much melted on the voyage, and how was it kept once it landed? Who did the work, who bought the ice and for how much, and what ended the trade? #research/run-5
Comment: %% The New England trade by sea, start to finish. %%

## Every topic

- New England ice shipped by sea, from the trade's start to its end.

## Topic 1: Cutting the ice on the ponds

Questions:

1. When was pond ice ready to cut, and how thick did it have to be?
2. What tools cut the ice, and what size were the blocks?

Waits on: nothing

## Topic 2: Storing the ice before shipping

Questions:

3. How were the icehouses at the ponds built, and how much did they hold?
4. How much ice did they lose while it was stored?

Waits on: nothing

## Topic 3: Loading the ship

Questions:

5. How was the ice packed into the ship's hold?
6. What kept the cargo from melting or shifting at sea?

Waits on: nothing

## Topic 4: The voyage

Questions:

7. Where did the ice ships sail, and how long did the voyages take?
8. How much of the cargo melted on the way?

Waits on: nothing

## Topic 5: Ice houses at the far ports

Questions:

9. How were the ice houses at the far ports built, and how much did they hold?
10. Who ran them, and how was the ice sold?

Waits on: nothing

## Topic 6: The workers

Questions:

11. Who cut and handled the ice, and how were the crews organised?
12. What were the working conditions, and what were the dangers?

Waits on: nothing

## Topic 7: Buyers and prices

Questions:

13. Who bought the ice at the far ports?
14. What did the ice cost there?

Waits on: nothing

## Topic 8: The end of the trade

Questions:

15. What ended the trade?
16. When did the last cargoes sail?

Waits on: nothing
PLAN_EOF

# Eight findings files, about 19,500 words in all, each under the 2,500-word ceiling (spec 06 item 6)
cat > project/llm-files/research-findings/run-2026-10-09-1400-research/ice-trade/topic-1.md << 'T1_EOF'
# Findings - Topic 1: Cutting the ice on the ponds

## Passage 1

The harvest ran in the coldest weeks of the year, usually from the middle of January into February, once a long hard freeze had set in. The shipping firms preferred spring-fed ponds with no streams running in, because moving water froze unevenly and carried silt, leaves, and sawdust from upstream mills into the ice. Fresh Pond in Cambridge, Wenham Lake north of Salem, and Spy Pond in Arlington were the best known, and the firms bought or leased the shore rights so that no rival could cut there. A pond owner could earn more from one winter's ice rights than from a year of farming the land around it. Clear ice from a deep, still pond was the product the trade was built on. Buyers in hot ports judged ice by how clear it was, and cloudy ice was taken as a sign of dirty water even when it was not. Foremen kept daily notebooks through the season, recording the air temperature at dawn and noon, the wind, and any snowfall, because each of these changed how and when the ice could be cut.

Evidence: verified

Sources:
- https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview (local historical society article, 2017)
- https://www.new-england-industry.example/ice/pond-rights (regional industry history site, 2014)

Reliability: the industry history site cites no archive for the pond-rights figures.

## Passage 2

Ice was not cut until it was at least 14 inches thick. Thinner ice crumbled at the corners when it was handled, wasted space in the hold, and melted faster because a thin block has more surface for its weight. Each morning of the harvest a foreman walked the pond with a hand auger and bored test holes at set points, measuring the depth of clear ice and, separately, the depth of any white snow ice on top. Only the clear ice counted toward the thickness. If the readings fell short, the crew was sent to clear snow or stood idle, and the foreman wrote the readings in his notebook. Some firms paid a small bonus to the foreman whose pond reached cutting thickness first, because an early harvest could be in the icehouses before a thaw arrived. A pond could reach cutting thickness in one corner days before another, so cutting often began near the shaded shore and moved outward as the ice thickened.

Evidence: verified

Sources:
- https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview (local historical society article, 2017)
- https://www.harvard-business-archive.example/tudor-papers/harvest-instructions (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 3

Snow was the harvest's main enemy. A layer of snow on the pond acted like a blanket and slowed the freezing of the clear ice underneath. Worse, wet snow that froze on top turned into "snow ice," which was white, full of air, and weak. Crews cleared snow off the pond with horse-drawn scrapers, wide wooden boards dragged across the surface and tipped at the edge of the cleared area. On some ponds the crews bored holes through the ice and let the water flood the cleared surface, so that a fresh layer froze on top and the ice thickened faster. Flooding only worked in hard cold, because a layer that froze slowly would itself turn cloudy. The snow ice on top of a block was planed off before the block was stored, and a firm that skipped this step could lose a buyer. Snowfall in the middle of a harvest could stop all work for several days while the scrapers went over the pond again.

Evidence: reported

Sources:
- https://www.new-england-industry.example/ice/snow-and-flooding (regional industry history site, 2014)
- https://www.farm-journal-archive.example/1856/february/ice-for-market (digitized agricultural magazine, February 1856)

Reliability: the 1856 magazine article gives advice to farmers, not an account of a single harvest.

## Passage 4

Horses did most of the heavy work on the ice, pulling the scrapers and the cutting tools. They were shod with sharp-calked shoes, horseshoes with spikes that gripped the ice, and a blacksmith was kept near the larger ponds through the season to reset shoes that wore down. A horse that broke through into the water was the most common accident of the harvest. The crews kept ropes ready at the edge of the cut field, and the usual method was to loop a rope around the horse's neck and pull it tight, which made the animal hold its breath and float higher in the water, so that the men could drag it back onto solid ice. Accounts describe horses that went through two or three times in a season and kept working. The tool makers designed the marker and plough so that the horse walked on uncut ice beside the line being cut, never on the grooves themselves.

Evidence: reported

Sources:
- https://www.walden-region-history.example/oral-histories/ice-crews (oral history collection, transcribed 1974)
- https://www.farm-journal-archive.example/1856/february/ice-for-market (digitized agricultural magazine, February 1856)

Reliability: the rope method is described in oral histories and one magazine piece, with no count of how often it worked.

## Passage 5

Before the 1820s ice was cut by hand with axes, hand saws, and chisels. The blocks came out in uneven shapes and sizes, which made them hard to stack, and gaps between uneven blocks let in warm air. Hand cutting was also slow, so the amount a crew could take from a pond in a season was small. Nathaniel Jarvis Wyeth, a Cambridge hotel manager who later worked for the Tudor ice company, designed a horse-drawn cutter in 1825 and patented an improved version in 1829. His tools made blocks of one regular size, which could be stacked tightly in icehouses and ships' holds with little air between them. The shift from hand cutting to horse tools is described by historians as the change that made long voyages possible, because regular blocks lost less ice to melting. Wyeth's tools were copied quickly, and by the 1840s most commercial ponds in Massachusetts used some version of them.

Evidence: verified

Sources:
- https://www.mit-tech-history.example/inventors/wyeth-ice-tools (university history of technology page, 2018)
- https://www.patent-records.example/1829/wyeth-ice-cutting-apparatus (digitized patent record, 1829)

## Passage 6

The first horse tool on the ice was the "marker." It looked like a plough with a row of steel teeth set along a frame, drawn by one horse along a straight line laid out with a cord. Each pass scored a shallow groove, and a guide arm kept the next groove parallel to the last. When the whole field was scored in one direction, the marker was turned at a right angle and run across the first grooves, cutting the surface into a grid of squares. The grid was laid out so that the blocks came out 22 inches square on the surface. The second tool, called the "plough" by the crews, had longer teeth and was run along the same grooves again and again until each cut went about two-thirds of the way through the ice. The remaining third held the field together so that the men and horses could still walk on it while the cutting went on.

Evidence: verified

Sources:
- https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s (local historical society article on surviving tools, 2019)

## Passage 7

Once a field was grooved, the crews opened a channel to the shore by sawing out a strip of ice with long hand saws. Men with iron "breaking bars," flat chisels on long handles, then struck along the grooves to split the field into long rafts of blocks, then split the rafts into single blocks. A well-cut field split cleanly along the grooves, and a skilled bar man could tell from the sound of the strike whether the groove had gone deep enough. The split blocks floated in the open channel. Men with pike poles, long wooden poles with an iron hook and spike, pushed and pulled the blocks along the channel toward the shore in a line. Boys were often given the lighter work along the channel, guiding the floating blocks around corners. In very hard cold the channel had to be kept open by breaking the thin new ice that formed on it overnight.

Evidence: reported

Sources:
- https://www.new-england-industry.example/ice/breaking-and-floating (regional industry history site, 2014)
- https://www.walden-region-history.example/oral-histories/ice-crews (oral history collection, transcribed 1974)

Reliability: the oral histories were recorded from people who worked the last commercial harvests, long after the shipping trade ended.

## Passage 8

At the shore the blocks were lifted out of the channel and into the icehouse by an inclined elevator, a long wooden ramp with an endless chain running up it. Cleats on the chain caught each block and carried it up to the door at the level where the men inside were stacking. At first the chain was driven by a horse walking in a circle at a capstan, and from the 1850s the largest houses used small steam engines. A block that slipped back down the ramp could break a man's leg, so a man stood at the foot of the ramp to feed the blocks on one at a time. Before the block went up, a man with a scraper planed the top and bottom flat, removing any snow ice and making the block sit evenly in the stack. The elevator could run day and night when the weather held, with lanterns hung along the ramp.

Evidence: verified

Sources:
- https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview (local historical society article, 2017)
- https://www.steam-power-history.example/small-engines/ice-elevators (engineering history society page, 2012)

## Passage 9

Blocks were graded before they were stored. The clearest blocks, with no bubbles, no snow ice, and no dirt, were marked first quality and set aside for shipping. Blocks with a cloudy band or trapped leaves were second quality and were usually sold in the local market, to households and butchers in Boston and the nearby towns. Broken corners and chips were swept into the waste and left on the ice. The grading mattered because a buyer in a hot port paid for clear ice and was quick to complain about anything else. Agents abroad wrote back to the shippers about the quality of each cargo, and a firm whose cargo arrived cloudy could lose its place with a buyer for a whole season. The grading was done by eye by the foremen, and the papers of one firm show that the foremen were told to reject any block they would not want to see on a dinner table.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/harvest-instructions (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.boston-markets-history.example/ice/local-trade (local history society page, 2016)

## Passage 10

Foremen tested the clarity of the ice before the harvest began. A small block was cut from the field, carried to the shore, and held up against the light, and the foreman looked for bubbles, streaks, and specks of dirt. A block that showed a dark object clearly through its whole thickness was judged good enough for shipping. If the test block was cloudy, the foreman moved the cutting to another part of the pond, often further from the inlet or the shore, where the water had been stiller when it froze. The test was repeated every few days, because new snow or a thaw could change the ice from one week to the next.

Evidence: reported

Sources:
- https://www.walden-region-history.example/oral-histories/ice-crews (oral history collection, transcribed 1974)
- https://www.harvard-business-archive.example/tudor-papers/harvest-instructions (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 11

The weather could ruin a harvest. A thaw or a day of rain in the middle of the season softened the ice, flooded the grooves, and refroze them unevenly, and the field often had to be planed and cut again. A mild winter with too little cold, which the trade called an "open winter," left the ponds too thin to cut at all, and the shippers then bought ice from ponds further north, in Maine and New Hampshire, at a higher cost. In a good season a large pond could be cleared in two to three weeks. Firms kept crews and horses ready from the turn of the year so that no cold day was lost. Newspaper reports from the harvest seasons describe the work as a race against the weather, with crews cutting on Sundays when a thaw was forecast, against local custom. Several firms began to keep icehouses on two or more ponds so that one bad pond would not cost them the whole year.

Evidence: reported

Sources:
- https://www.boston-newspaper-archive.example/1858/january/ice-crop (digitized newspaper, January 1858)
- https://www.new-england-industry.example/ice/open-winters (regional industry history site, 2014)

## Passage 12

The harvest was counted in blocks, not weighed. A tally man stood at the top of the elevator with a board and made a mark for every block that went into the house, and at the end of each day the marks were added up and turned into tons by a fixed figure for the weight of a standard block. A first-quality block of the regular size weighed roughly 200 pounds, so the tally of blocks gave a quick estimate of the tonnage stored. The firms used the tally to plan the next year's sailings and to pay the pond owners, who were usually paid by the ton taken from their water. Pond owners sometimes sent their own man to keep a second tally, and disputes over the count are recorded in letters between the owners and the shipping firms. The tally was rough, because blocks varied in thickness from one part of the pond to another.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/pond-accounts (finding aid and transcriptions of a merchant's papers, 2009)

Reliability: the figure for the weight of a block is the firm's own working figure, not a measured average.

## Passage 13

By the 1850s the tools of the harvest were made and sold as complete sets by firms that specialised in them, many of them in the Hudson valley of New York, where a large ice trade supplied New York City. A set for a large pond included one or two markers, several ploughs, hand saws up to six feet long, breaking bars, pike poles, ice tongs, and the scrapers for snow. The makers printed catalogues with engravings of each tool and instructions for its use, and the catalogues are now one of the main sources for how the work was done. The tools changed little over the life of the shipping trade. A set bought in the 1850s could still be in use thirty years later, with new teeth fitted to the markers and ploughs by a local blacksmith. Several sets survive in museum collections in Massachusetts and New York.

Evidence: verified

Sources:
- https://www.hudson-valley-museum.example/collections/ice-tool-catalogues (museum collection page, 2020)
- https://www.mit-tech-history.example/inventors/wyeth-ice-tools (university history of technology page, 2018)

<!-- end of findings -->
T1_EOF

cat > project/llm-files/research-findings/run-2026-10-09-1400-research/ice-trade/topic-2.md << 'T2_EOF'
# Findings - Topic 2: Storing the ice before shipping

## Passage 1

The harvest came in over a few weeks in winter, but the ships sailed all year round, so the ice had to be stored for months before it was loaded. The shipping firms built their icehouses on the shore of the pond itself, so that the blocks could go straight from the channel up the elevator and into storage. The houses stood above ground. This was a change from the older farm practice of keeping ice in pits dug into a hillside, which held only a few tons and let groundwater seep in. An above-ground house could be built as large as the firm wanted and filled from a single elevator. It also kept the ice away from the warm soil, which in summer gave off heat into a buried pit. Because the houses stood near the railway lines that ran to the Boston wharves, ice could be sent to a ship within a day of the order.

Evidence: verified

Sources:
- https://www.cambridge-historical.example/fresh-pond/icehouses (local historical society article, 2017)
- https://www.new-england-industry.example/ice/storage-history (regional industry history site, 2014)

## Passage 2

The walls were the key to the design. An icehouse had two wooden walls, an outer and an inner, built a little apart, with the space between them packed with an insulating fill. Sawdust from the timber mills was the usual fill, and spent tanbark from the leather tanneries was also used. Some houses had three walls with two layers of fill. Frederic Tudor and Nathaniel Wyeth tested different fills in the 1820s and 1830s by building small trial houses and weighing the ice in them at the start and end of the summer. They found that a dry fill kept the ice far better than a damp one, and the houses were built with wide eaves so that rain did not run down the outer wall and soak into the fill. Tudor's notes from these trials are among the papers held by the business archive, and they record that the trials were repeated over several summers.

Evidence: verified

Sources:
- https://www.harvard-business-archive.example/tudor-papers/storage-trials (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.mit-tech-history.example/inventors/wyeth-ice-tools (university history of technology page, 2018)

## Passage 3

The largest houses were huge. The biggest icehouse on Fresh Pond held about 9,400 tons of ice when full and was taller than a three-storey building. It was built as a row of rooms side by side under one long roof, each room filled and emptied on its own, so that opening one room for loading did not let warm air into the rest. A house of this size took the whole of a good harvest from a large pond. Contemporary engravings show the house as a long, windowless block with a row of doors stacked one above another on the side facing the elevator. The doors at each height were opened as the ice rose inside, and boarded shut as soon as the stack passed them. Smaller firms built houses that held a few hundred tons and sold most of their ice in the local market.

Evidence: verified

Sources:
- https://www.cambridge-historical.example/fresh-pond/icehouses (local historical society article, 2017)
- https://www.massachusetts-engravings.example/prints/fresh-pond-ice-works-1852 (museum print catalogue entry, engraving dated 1852)

Reliability: the size of the house comes from the historical society article, which cites a company prospectus.

## Passage 4

The roof was steep, with vents along the ridge. Warm air rose to the top of the house and escaped through the vents, so the air around the ice stayed as cold as possible. The vents were covered with louvres to keep out rain and snow. Most houses were painted white or a light colour on the outside, to reflect the summer sun. Some builders added a layer of hay or straw in the roof space as further insulation. A writer in an agricultural magazine advised farmers building small houses on the same plan to make the roof vent large enough to put a hand through, and to keep it open all year. The magazine's advice was aimed at farms, but it describes the same features the commercial houses used, on a smaller scale.

Evidence: reported

Sources:
- https://www.farm-journal-archive.example/1859/june/building-an-ice-house (digitized agricultural magazine, June 1859)
- https://www.new-england-industry.example/ice/storage-history (regional industry history site, 2014)

Reliability: the magazine writes for farmers, not for the shipping firms.

## Passage 5

Water was more dangerous to stored ice than warm air. Melt from the stack had to drain away at once, because ice standing in water melted much faster than ice standing in air. The floors were built over a bed of gravel or broken stone with a drain running out to the pond, and covered with a thick layer of sawdust that the blocks were stacked on. A house with a blocked drain could lose a large part of its bottom layers in a single warm month. The firms sent a man through the houses in summer to check that the drains were running. The papers of one firm record the dismissal of a keeper who let a drain freeze over in early spring, which flooded the lowest room when the weather turned.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/storage-trials (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 6

Each large icehouse had a keeper who lived beside it all year, often in a small cottage built against the end wall. The keeper checked the drains and vents, kept the doors shut, watched for fire, and kept the ledger of ice in and ice out. In the harvest he directed the stacking crews, and in the shipping season he chose which room to open for each order. The firms hired keepers who could read and write and keep figures, because the ledgers were the firm's only record of what it held. A keeper's letters to the firm's office in Boston survive for several houses. They are mostly short reports of the weather, the state of the stack, and requests for repairs to the roof or the doors, and they show the keeper writing to the office about once a week through the summer.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/keepers-letters (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 7

The ledgers of one Fresh Pond icehouse for the season of 1847 record the weight of ice put in at the end of the harvest and the weight taken out for each sailing. Over the season the house lost about 17 percent of its ice between the end of the harvest in March and the last autumn sailing. The ledger shows that most of the loss came in July and August. The keeper's notes beside the figures blame the heat of those months and a roof vent that had been left shut. The ledger is the only surviving record of a whole season's loss for a single house, and historians of the trade use it as the standard figure for how much stored ice was lost. The keeper also recorded that a room left unopened until autumn lost less than a room opened for loading in June.

Evidence: verified

Sources:
- https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage (state archives catalogue entry with transcribed ledger, digitized 2015)

## Passage 8

From the early 1840s a railway branch line ran from Fresh Pond to the wharves at Charlestown, on Boston harbour. Before the railway, ice went to the harbour in horse-drawn wagons, and a hot day on the road could cost a wagon a noticeable part of its load. The railway cut the journey to under an hour. Wagons on the ice line were built with thick wooden sides packed with sawdust, like small moving icehouses, and the trains ran at night in summer to avoid the heat of the day. The railway's own records show that the ice firms were among its largest customers in the 1840s. The line made the pond icehouses into the first stage of a chain that ran from the pond to the ship's hold with as little time in the open as possible.

Evidence: verified

Sources:
- https://www.railroad-history-ma.example/branches/charlestown-ice-line (railway historical society page, 2013)
- https://www.cambridge-historical.example/fresh-pond/icehouses (local historical society article, 2017)

## Passage 9

The firms also kept smaller icehouses on the Charlestown wharves. Ice was brought down from the ponds a few days before a ship was due to sail and held in the wharf houses until the hold was ready. The wharf houses let the loading crews work without waiting for trains, and they kept a reserve on hand if a ship came in early. They were built on the same plan as the pond houses, with double walls and sawdust fill, but held only a few hundred tons each. Ice was not kept in the wharf houses for long, because the harbour air was warmer and damper than the air at the ponds, and the houses stood on wooden piers over the water.

Evidence: reported

Sources:
- https://www.boston-harbour-history.example/wharves/charlestown-ice-houses (local history society page, 2011)

## Passage 10

Keepers measured loss in two ways. The common way was to count the blocks put in at the harvest and the blocks taken out, and to turn both counts into tons using the firm's standard weight for a block. The more careful way, used in the 1847 ledger, was to weigh a sample of blocks on a platform scale each time a room was opened, because blocks that had stood for months weighed less than fresh ones even when they looked whole. Counting blocks hid the loss from blocks that had shrunk but not broken, so ledgers kept by counting show smaller losses than ledgers kept by weighing. Historians who compare loss figures from different houses warn that the two methods give figures that cannot be set side by side.

Evidence: reported

Sources:
- https://www.ma-archives.example/ice-ledgers/methods-note (state archives research note, 2015)
- https://www.new-england-industry.example/ice/storage-history (regional industry history site, 2014)

## Passage 11

Inside the house the blocks were stacked as tightly as possible. The men placed each block on its edge, close against the next, and laid each layer across the one below it, like brickwork, so that the stack held together. The small gaps between blocks were filled with ice chips swept up from the cutting. Air in the gaps was the main source of melting inside the stack, so a tight stack kept better than a loose one. When a room was full, the top of the stack was covered with a deep layer of hay or sawdust before the doors were shut. The stacking crews worked inside the house at freezing temperatures, and they were counted among the most skilled men of the harvest, because a badly laid stack could lean and fall as the lower blocks melted.

Evidence: verified

Sources:
- https://www.cambridge-historical.example/fresh-pond/icehouses (local historical society article, 2017)
- https://www.walden-region-history.example/oral-histories/ice-crews (oral history collection, transcribed 1974)

## Passage 12

When a ship was ready, the ice was taken out of the house from the top of the stack down. The men opened the door nearest the top of the ice, cleared away the hay or sawdust, and broke the blocks apart with bars, because the blocks had often frozen together over the months. The blocks then went down a chute or ramp to the railway wagons. Only one room was opened at a time, and the doors were shut again the same day. A keeper's job was to judge which room to open, using the oldest ice first and keeping the best-packed rooms for the hottest months. The blocks taken out were scraped clean of the fill before they were loaded, so that the sawdust from the house did not go on board mixed with the ice.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/harvest-instructions (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.boston-markets-history.example/ice/local-trade (local history society page, 2016)

## Passage 13

From the 1850s some keepers hung thermometers inside the larger icehouses, in the space above the stack, and recorded the reading each morning and evening alongside the outside temperature. The readings showed the keepers how well the roof vents were working: on a hot day the air above the stack stayed far cooler than the air outside as long as the vents were open and the doors shut. A rising reading inside the house was a sign that a door had been left open or a vent had clogged. The thermometer readings survive in a few of the keepers' ledgers, written in a separate column beside the record of ice taken out.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/keepers-letters (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 14

Icehouses burned. The dry sawdust in the walls and the hay on the stacks caught fire easily, and the long wooden houses burned fast once a fire started. Several large icehouses on the Massachusetts ponds were lost to fire during the life of the trade, often in summer, when the fill was driest and a spark from a passing railway engine could set the outer wall alight. The ice inside usually survived the fire, standing in a block in the ruins of the house, but it then melted in the open within days unless it could be loaded at once. Fire was the reason some firms moved to building houses in separate sections, so that a fire in one section did not spread to the rest. Insurance for icehouses was costly, and some firms carried none.

Evidence: reported

Sources:
- https://www.boston-newspaper-archive.example/1868/august/icehouse-fire (digitized newspaper, August 1868)
- https://www.new-england-industry.example/ice/storage-history (regional industry history site, 2014)

Reliability: the newspaper report covers one fire; the industry site gives no count of fires.

## Passage 15

Other sources give wider ranges for storage loss than the 1847 ledger. A history of the trade written for a general audience says that a well-built house lost between a fifth and a third of its ice over a summer, and that small houses lost far more, sometimes half. It gives no source for these figures. The difference matters because the loss in storage decided how much ice a firm had to harvest to fill its contracts. Large houses lost less than small ones, because a big stack has less surface for its weight, the same reason thick blocks melted more slowly than thin ones. This is the main reason the shipping firms built ever-larger houses through the 1840s and 1850s.

Evidence: reported

Sources:
- https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt (book excerpt on a publisher's site, 2005)
- https://www.new-england-industry.example/ice/storage-history (regional industry history site, 2014)

Reliability: the book excerpt gives its loss figures without a source.

<!-- end of findings -->
T2_EOF

cat > project/llm-files/research-findings/run-2026-10-09-1400-research/ice-trade/topic-3.md << 'T3_EOF'
# Findings - Topic 3: Loading the ship

## Passage 1

The ice went to sea in ordinary merchant ships, not ships built for the trade. Boston's merchants sent large amounts of goods home from the tropics, such as sugar, cotton, and spices, but had little to send out, so many ships left Boston in ballast, carrying stone or gravel only to keep them stable. Ice gave these ships a paying cargo on the outward voyage. Shipowners charged low rates to carry it, because the alternative was sailing with no cargo at all, and this cheap carriage was one of the reasons the trade could make money. Older ships were often chosen, because the ice firms' carpenters built linings into the hold and the owners did not want their best ships altered. The ships returned with tropical cargo in the same holds, once the linings were removed.

Evidence: verified

Sources:
- https://www.maritime-boston.example/trade/outward-cargoes (maritime museum article, 2016)
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

## Passage 2

Before any ice went on board, the hold was emptied, swept, and left open to dry. Any smell in the hold could pass into the ice, and a hold that had carried fish, hides, or molasses was scrubbed and aired for days. Buyers in the hot ports used the ice in drinks and food, and an agent in one port wrote back to Boston that a cargo tasting of fish was sold off at a loss to a butcher. The ice firms kept a list of ships they would not charter because their holds could not be cleaned. Ships that had carried coal were also avoided, because coal dust worked into the timbers and came out black on the ice.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/agents-letters (finding aid and transcriptions of a merchant's papers, 2009)

Reliability: the story of the fish-tasting cargo comes from one agent's letter.

## Passage 3

The ship's carpenter, or a carpenter sent by the ice firm, built a lining inside the hold. The lining was an inner wall of pine planks, set a little way in from the hull on all sides, with the space between packed with sawdust. The same lining ran across the floor of the hold and up under the deck beams. The result was a box inside the hull, built on the same plan as the icehouses on shore. Sailors called the lining the "ice ceiling." It was taken out in the far port and the planks were often sold there, since timber was scarce in some tropical ports. Building the lining took a carpenter and two helpers about a week for a ship of middling size.

Evidence: verified

Sources:
- https://www.maritime-salem.example/papers/ship-fittings-for-ice (museum research paper, 2008)
- https://www.maritime-boston.example/trade/outward-cargoes (maritime museum article, 2016)

## Passage 4

The floor of the hold was laid first. A layer of rough timber, called dunnage, went on the bottom of the hull to lift the cargo clear of any water in the bilge. On top of the dunnage the carpenters laid the floor of the lining, and on top of that a deep bed of sawdust. Gaps were left at the sides of the floor so that melt could run down into the bilge, where the ship's pumps could reach it. A hold with a badly built floor kept the bottom layer of ice standing in water for the whole voyage, and the loss from the bottom layer was the largest single loss on most voyages that kept records.

Evidence: verified

Sources:
- https://www.maritime-salem.example/papers/ship-fittings-for-ice (museum research paper, 2008)

## Passage 5

The sawdust had to be dry. Wet sawdust froze onto the blocks in the hold and made a solid crust that conducted heat into the ice instead of keeping it out, and it also added weight to the cargo for no benefit. The firms stored their sawdust in covered sheds on the wharves and turned it over in fine weather to dry it. A load of sawdust that arrived damp from Maine was spread out on the wharf in the sun before it was used. Buyers of sawdust in the Boston trade inspected each schooner load by hand, and the price paid for a load depended on how dry it was. The mills in Maine came to depend on the trade, which turned a waste they had once burned or dumped in the river into a product they could sell.

Evidence: reported

Sources:
- https://www.maine-lumber-history.example/mills/sawdust-trade (state historical society article, 2015)
- https://www.maritime-boston.example/trade/outward-cargoes (maritime museum article, 2016)

## Passage 6

Sawdust did the same work in the ship that it did in the icehouse. It filled the gaps, held the blocks still, and slowed the warming of the ice. The firms bought pine sawdust from the timber mills of Maine, where it was a waste product, and brought it to Boston by schooner. A paper by a Salem merchant written in 1850 sets out the quantities: a hold was loaded with one ton of sawdust for every 11 tons of ice. The paper says that less sawdust saved weight but cost more ice than it saved, and more sawdust took up space that could have carried ice. The merchant wrote the paper for other shippers, and it was printed and passed around the Salem and Boston trade.

Evidence: verified

Sources:
- https://www.maritime-salem.example/papers/stowing-ice-1850 (museum transcription of a merchant's printed paper, 1850)

## Passage 7

The stevedores stowed the blocks in the hold the same way the icehouse crews stacked them: on edge, tight against each other, each layer laid across the one below. The blocks were lowered through the hatch in slings and set in place by hand. Ice chips and sawdust were pushed into every gap. Experienced ice stevedores were in demand on the Boston and Charlestown wharves, and the firms used the same gangs for every ship when they could. A bad stow left air spaces in the stack, and a stack with air spaces melted from the inside out. The mate of each ship was responsible for watching the stow and signing for the cargo once it was in.

Evidence: reported

Sources:
- https://www.boston-harbour-history.example/wharves/stevedores (local history society page, 2011)
- https://www.maritime-boston.example/trade/outward-cargoes (maritime museum article, 2016)

## Passage 8

Ice is heavy, and a ship loaded with ice sat low in the water. Ships usually carried less ice than their rated tonnage, partly because of the weight of the lining and the sawdust and partly because the space lost to the lining reduced what the hold could take. The ice was stowed low and spread evenly from bow to stern, so that the ship stayed stable and sat level. A master who loaded too much ice found his ship sluggish and wet in heavy seas. As the voyage went on and the ice melted, the ship rose in the water and grew lighter, which some masters said made her roll more in the last weeks at sea.

Evidence: reported

Sources:
- https://www.maritime-salem.example/papers/ship-fittings-for-ice (museum research paper, 2008)
- https://www.sailing-ship-logs.example/collections/ice-voyages (digitized logbook collection, various dates)

Reliability: the comment on rolling comes from masters' remarks in logbooks, not from any measurement.

## Passage 9

When the stack reached the top of the lining, it was covered with a thick layer of sawdust and then a layer of hay. The hatches were then closed, covered with tarred canvas, and battened down, with wooden bars nailed across them to hold the canvas tight. The aim was to keep the air in the hold as still as possible, because moving air carried heat to the ice. Some ships also fitted a second, inner hatch cover below the deck, with sawdust between the two. The master signed a note stating the time the hatches were sealed, and the note was sent back to the firm with the first mail.

Evidence: verified

Sources:
- https://www.maritime-salem.example/papers/ship-fittings-for-ice (museum research paper, 2008)
- https://www.sailing-ship-logs.example/collections/ice-voyages (digitized logbook collection, various dates)

## Passage 10

A cargo that shifted at sea could break the lining and let warm air and water into the stack. To stop the blocks moving, the stevedores drove timber battens between the stack and the lining at intervals, and wedged the top layers against the deck beams. A tight stow with plenty of sawdust also held the blocks still. Logbooks record a few voyages where heavy weather loosened the stack, and in each case the ship arrived with a much smaller cargo than it left with. In one logbook the master writes that he heard the ice "working" in the hold during a gale and could do nothing about it, because the hatches could not be opened at sea.

Evidence: reported

Sources:
- https://www.sailing-ship-logs.example/collections/ice-voyages (digitized logbook collection, various dates)

## Passage 11

Melt water was pumped out of the bilge on a fixed schedule. The crew worked the pumps every 4 hours, day and night, for the whole voyage, and the mate entered each pumping in the log with the number of strokes needed to clear the bilge. The number of strokes was a rough measure of how fast the ice was melting, and masters watched it closely. A sudden rise meant that the stow had shifted or the lining had broken. Water left in the bilge rose into the bottom layers of ice and melted them faster, so missing a pumping cost ice. The logbooks show the strokes rising steadily as a ship sailed into warmer waters and the hold warmed.

Evidence: verified

Sources:
- https://www.sailing-ship-logs.example/collections/ice-voyages (digitized logbook collection, various dates)

## Passage 12

Once the hatches were sealed, they stayed sealed until the ship reached port. The crew were forbidden to open them, even in calm weather, because each opening let warm air into the hold. Some masters had the hatch covers sealed with wax or pitch at the joins so that any tampering would show. The firms' instructions to masters, which survive in copies, say that a master who opened the hatches at sea without good cause would answer for the lost ice. The rule meant that no one could see the condition of the cargo until it arrived, so the pumping log was the only sign of how the ice was faring.

Evidence: verified

Sources:
- https://www.harvard-business-archive.example/tudor-papers/masters-instructions (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 13

Loading was done fast. The ice came from the wharf icehouses or straight from the railway wagons, and the stevedores worked through the night or in the early morning when the air was coolest. A ship of middling size could be loaded in one to two days. The firms timed the ice's arrival at the wharf to the hour, so that blocks did not sit in the sun on the wharf. Once the hatches were sealed, the ship sailed on the next tide if the wind allowed. Every day in port with the ice on board was a day of melting with no distance gained, and masters who waited for a cargo of return goods before sailing were told to stop doing so.

Evidence: reported

Sources:
- https://www.boston-harbour-history.example/wharves/stevedores (local history society page, 2011)
- https://www.harvard-business-archive.example/tudor-papers/masters-instructions (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 14

In the first years of the trade, sailors were afraid of ice cargoes. A common belief on the Boston waterfront was that melting ice would fill the hold with water and sink the ship. Frederic Tudor wrote in his diary that he had trouble finding crews for his early voyages, and that some sailors signed on and then left the ship before it sailed. The fear faded as voyages arrived safely. By the 1840s ice ships were crewed like any other merchant ship, and sailors who had made several ice voyages were valued because they knew the pumping routine.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/diary-excerpts (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt (book excerpt on a publisher's site, 2005)

Reliability: the diary records Tudor's own view of his difficulties.

## Passage 15

Marine insurers were slow to cover ice. In the early years they refused to insure ice cargoes at all, on the grounds that the cargo was certain to lose part of itself on every voyage. Later policies covered the ship and a share of the cargo, but excluded loss from melting, which the insurers treated as normal wear rather than an accident. The shipper bore the risk of melting. This was one of the reasons the firms worked so hard on the stow, the lining, and the speed of loading: no one else would pay for the ice that turned to water on the way.

Evidence: reported

Sources:
- https://www.insurance-history.example/marine/perishable-cargoes (insurance history society article, 2012)
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

## Passage 16

Ships carrying ice often carried small amounts of other perishable goods packed among the blocks. Apples from New England orchards, butter in tubs, and cheeses were stowed in pockets cut into the stack, and they arrived in the tropics in good condition, where they sold well because they could not be had locally. The goods were usually the private trade of the master or the firm's agent rather than the firm's own cargo. Some firms disliked the practice because the pockets weakened the stow and the goods had to be dug out on arrival, which meant opening the stack before it was unloaded. Others allowed it as a way of keeping good masters content. Agents' letters mention apples arriving in Calcutta and Havana in better state than the same apples would have been after a month in a Boston cellar.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/agents-letters (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.food-history-quarterly.example/2014/new-england-apples-abroad (peer-reviewed article, 2014)

## Passage 17

Cargoes grew over the life of the trade. The early voyages carried a cargo of a size that a single small ship could take, and the firms' records show cargoes rising through the 1840s as larger ships were chartered and the loading crews grew more skilled. The size of a cargo was limited less by the ship than by the market at the far end: a port that could sell only so much ice before it melted in the ice house there was not sent more. The firms planned each year's sailings port by port, matching the size of each cargo to what the agent at that port said he could sell. Letters from the firm's office to its agents ask, again and again, how much ice each port could take in each month of the coming year.

Evidence: reported

Sources:
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)
- https://www.harvard-business-archive.example/tudor-papers/agents-letters (finding aid and transcriptions of a merchant's papers, 2009)

<!-- end of findings -->
T3_EOF

cat > project/llm-files/research-findings/run-2026-10-09-1400-research/ice-trade/topic-4.md << 'T4_EOF'
# Findings - Topic 4: The voyage

## Passage 1

The trade began with a failure. Frederic Tudor sent his first cargo of ice from Boston to the island of Martinique in the Caribbean in 1806. The ice arrived, but there was no ice house to keep it in and no one on the island knew what to do with it, and most of it melted on the wharf while Tudor's brother tried to sell it. Tudor lost money on the voyage and on several that followed, and he spent time in a debtors' prison in the 1810s. He kept trying, and by the 1820s he was shipping ice regularly to Havana and to ports in the southern United States, where he had learned to build an ice house before the first cargo arrived.

Evidence: verified

Sources:
- https://www.harvard-business-archive.example/tudor-papers/diary-excerpts (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt (book excerpt on a publisher's site, 2005)

## Passage 2

The longest regular route ran from Boston to Calcutta, in British India. A ship on this route sailed south through the Atlantic, crossed the equator, rounded the Cape of Good Hope at the tip of Africa, and sailed north across the Indian Ocean, crossing the equator a second time before reaching the Hooghly River. The voyage from Boston to Calcutta took about 130 days. It was one of the longest voyages any perishable cargo made in the age of sail, and the trade's success on this route was the thing most often reported in the newspapers of the time as proof that ice could be carried anywhere.

Evidence: verified

Sources:
- https://www.maritime-boston.example/routes/boston-calcutta (maritime museum article, 2016)
- https://www.sailing-ship-logs.example/collections/ice-voyages (digitized logbook collection, various dates)

## Passage 3

The Caribbean routes were far shorter. Ships for Havana, Martinique, Jamaica, and the other islands made the voyage in two to three weeks with fair winds. Havana became one of the steadiest markets of the whole trade, with ships arriving every few weeks through the year. The short voyage meant that ice reached the Caribbean ports in much better condition than it reached India, and the firms could send smaller, more frequent cargoes. The Caribbean ports were also where the firms had first learned how to sell ice, and the habits formed there were carried to the longer routes.

Evidence: verified

Sources:
- https://www.maritime-boston.example/routes/caribbean (maritime museum article, 2016)
- https://www.havana-archive.example/colonial-trade/shipping-arrivals (digitized port records, 1830s to 1850s)

## Passage 4

The southern ports of the United States were the largest market by volume. Ships sailed from Boston to Charleston, Savannah, Mobile, and above all New Orleans, which took more New England ice than any other port in the world by the 1850s. The voyage to New Orleans took several weeks, down the Atlantic coast, around Florida, and across the Gulf of Mexico to the mouth of the Mississippi. From New Orleans some of the ice went up the river by steamboat to towns along the Mississippi. The southern trade was steady and close, and it carried most of the ice that left Boston in most years, even though the long Indian route got most of the attention.

Evidence: verified

Sources:
- https://www.gulf-commerce.example/ports/new-orleans-ice-imports (business history society page, 2013)
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

## Passage 5

Ice also went to South America and to other ports in Asia. Ships carried it to Rio de Janeiro and other Brazilian ports, to Valparaíso in Chile, and, after the Calcutta trade had proved itself, to Bombay and Madras in India and to Hong Kong and other ports in China. A few cargoes went to Australia. These routes were less regular than Calcutta, Havana, or New Orleans, and some were tried for only a few years before the firms gave them up because the ice could not be sold at a profit. The firms' records list these ports alongside a note of whether each voyage made or lost money.

Evidence: reported

Sources:
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)
- https://www.maritime-boston.example/routes/other-ports (maritime museum article, 2016)

## Passage 6

The first cargo of ice to Calcutta sailed from Boston in May 1833 on the ship Tuscany and arrived in September of that year. The arrival caused a sensation in the city. Local newspapers printed descriptions of the clear blocks being unloaded, and residents came down to the river to see them. The merchants of Calcutta raised money among themselves to build a proper ice house for later cargoes. The voyage made a profit for its backers, and regular sailings to Calcutta followed. The ship's master was given a gift by the city's merchants in thanks for bringing the cargo.

Evidence: verified

Sources:
- https://www.calcutta-history-society.example/1833/first-ice-ship (local history society article, 2011)
- https://www.maritime-boston.example/routes/boston-calcutta (maritime museum article, 2016)

## Passage 7

Most of the melting happened in the tropics. Logbooks show the pumping strokes, which tracked the melt, low in the first weeks out of Boston, rising sharply as the ship crossed into the warm waters near the equator, and staying high until the ship reached port. On the Calcutta route the ship crossed the tropics twice, and the second crossing, near the end of the voyage when the hold had been warming for months, was the worst. Ice that reached the Cape of Good Hope in good condition could still lose a large share in the last weeks of the voyage.

Evidence: verified

Sources:
- https://www.sailing-ship-logs.example/collections/ice-voyages (digitized logbook collection, various dates)

## Passage 8

Sailings to Calcutta were timed so that the ice arrived in the hot season, from about March to June, when demand in the city was highest and the price best. Working back from the voyage time, this meant that ships left Boston in the autumn and early winter. Leaving in the cold months had a second benefit: the first weeks of the voyage were spent in cold northern waters, where the hold stayed cool and almost no ice was lost. A ship that left Boston in summer started losing ice from the day it sailed, and the firms avoided summer sailings to India where they could. The Caribbean and southern ports were sent ice all year, with the most ships in the hot months.

Evidence: reported

Sources:
- https://www.maritime-boston.example/routes/boston-calcutta (maritime museum article, 2016)
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

## Passage 9

The steadiest figure for loss on the long route comes from a study of the surviving logbooks and cargo receipts for the Calcutta run. The study compared the weight of ice signed for in Boston with the weight unloaded in Calcutta for every voyage where both papers survive. On average the ships lost 38 percent of their ice between Boston and Calcutta. The loss on single voyages varied widely around that average, depending on the season, the length of the voyage, and the state of the stow. The study's authors note that the voyages whose papers survive may have been the better-run ones, since a firm was more likely to keep the papers of a voyage that went well.

Evidence: verified

Sources:
- https://www.ice-trade-voyages.example/logs/calcutta-melt-study (university research project report, 2018)

## Passage 10

The Caribbean and southern routes lost much less. Because the voyage was a matter of weeks rather than months, a well-stowed cargo to Havana or New Orleans often lost under a tenth of its ice. The short routes were where the firms made their steadiest profits, and the low loss was a large part of why. A firm that shipped to both the Caribbean and India could set the two side by side in its books, and the papers of one firm show that the Caribbean trade paid for losses on the Indian trade in more than one year.

Evidence: reported

Sources:
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)
- https://www.harvard-business-archive.example/tudor-papers/pond-accounts (finding aid and transcriptions of a merchant's papers, 2009)

Reliability: the article's figure for the short routes is an estimate from a small number of voyages.

## Passage 11

Calm weather cost ice. A ship becalmed near the equator, in the band of light and shifting winds that sailors called the doldrums, could drift for days or weeks under a hot sun while the ice melted with no distance gained. Masters on ice ships were told to keep moving at all costs and to take any route that avoided known calm zones, even if it was longer on the chart. Logbooks record masters complaining of calms in language that grows sharper with each day becalmed, and in one log the mate notes the pumping strokes beside each day's entry of "no wind."

Evidence: reported

Sources:
- https://www.sailing-ship-logs.example/collections/ice-voyages (digitized logbook collection, various dates)
- https://www.harvard-business-archive.example/tudor-papers/masters-instructions (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 12

The firms preferred fast ships for the long routes. A faster ship spent fewer days in the tropics and so lost less ice, and the firms paid more to charter ships known for speed when they were sending ice to India. Some of the fast American ships of the 1840s and 1850s carried ice to Calcutta on their outward voyage before loading tea or other cargoes in Asia for the return. For the short routes, speed mattered less and the cheapest ship available was usually chosen. The firms' records show the same few masters chosen for the Indian run year after year.

Evidence: reported

Sources:
- https://www.maritime-boston.example/routes/boston-calcutta (maritime museum article, 2016)

## Passage 13

Another estimate of loss on the Calcutta run is lower. A general history of the trade says that well-stowed ships lost about a quarter of their ice on the way to Calcutta, and that higher losses came from poor stowing rather than from the length of the voyage. The book does not say how this figure was reached. It is lower than the average found in the logbook study. The two figures may describe different periods, since the stow improved over the life of the trade, but neither source says which years its figure covers.

Evidence: reported

Sources:
- https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt (book excerpt on a publisher's site, 2005)

Reliability: the book excerpt gives no source for its loss figure.

## Passage 14

Ships returning from Calcutta brought back Indian goods: jute, linen, indigo dye, saltpetre for gunpowder, and spices. The return cargo was often worth more than the ice had been, and some historians of the trade argue that the ice voyage made sense to shipowners mainly because it put a ship in Calcutta to collect a valuable return cargo. On the Caribbean routes, ships came back with sugar, molasses, and coffee. The linings were removed in the far port so that the hold could take the return cargo, and the sawdust was usually sold or dumped there.

Evidence: verified

Sources:
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)
- https://www.maritime-boston.example/trade/outward-cargoes (maritime museum article, 2016)

## Passage 15

Ice ships were lost at sea like any other ships, to storms, fire, and wrecks on unknown reefs. The ice cargo itself did not make a ship more likely to sink, despite the early fears of sailors. Insurance records list ice ships among the vessels lost in the hurricane seasons of the Caribbean and the cyclone seasons of the Bay of Bengal, in about the same numbers as ships with other cargoes on the same routes. A ship that was lost took its ice with it, and the firm bore that loss along with the melt loss on every other voyage.

Evidence: reported

Sources:
- https://www.insurance-history.example/marine/perishable-cargoes (insurance history society article, 2012)

## Passage 16

The firm in Boston learned how a voyage had gone only when the mail came back. For Calcutta this could take most of a year: the ship's passage out, then a letter on the next ship home. The agent's letter reported the date of arrival, the weight of ice unloaded, its condition, and the price it was fetching. The firms planned the next season's sailings on news that was months old, and a bad report from Calcutta could arrive after the next ship had already sailed. Some letters were sent by the faster overland route through Egypt once that route opened, which shortened the wait.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/agents-letters (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.postal-history-review.example/2009/overland-mail-to-india (peer-reviewed article, 2009)

## Passage 17

Some ships stopped on the way. Ships bound for Calcutta sometimes called at Cape Town or at the island of Mauritius in the Indian Ocean for water and food, and some sold part of their ice there. A stop meant opening the hatches, which let warm air into the hold, so masters were told to sell what they could quickly and seal the hatches again within the hour. Ships for New Orleans sometimes called at Key West or Havana, where small amounts of ice could be sold from the top of the stack. The firms allowed these sales because a port that had never had ice was a new market to try.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/masters-instructions (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.maritime-boston.example/routes/other-ports (maritime museum article, 2016)

## Passage 18

The last part of the Calcutta voyage was the passage up the Hooghly River from the Bay of Bengal, a river with shifting sandbanks that ships could only enter with a local pilot. Sailing up against the current could take days. From the 1840s many ice ships were towed up the river by steam tugs, which cut the passage to a day or less. The firms' agents paid for the tow, judging that the ice saved was worth more than the fee. The tug was ordered ahead of time, and an agent's letter complains of a ship that waited three days at the river mouth for a tug that had gone to another vessel.

Evidence: reported

Sources:
- https://www.calcutta-history-society.example/port/hooghly-pilots-and-tugs (local history society article, 2011)
- https://www.harvard-business-archive.example/tudor-papers/agents-letters (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 19

Masters kept a separate record for the ice, apart from the ship's ordinary log. The firms gave each master a printed book with columns for the date, the ship's position, the air temperature on deck, the temperature of the sea, and the pumping strokes. The books were sent back to Boston at the end of the voyage, and the firms used them to judge masters and routes. Several of these ice books survive and are the main source for the logbook study of loss on the Calcutta run. They show that some masters filled them in with care every day and others left gaps of a week or more.

Evidence: verified

Sources:
- https://www.sailing-ship-logs.example/collections/ice-voyages (digitized logbook collection, various dates)
- https://www.harvard-business-archive.example/tudor-papers/masters-instructions (finding aid and transcriptions of a merchant's papers, 2009)

<!-- end of findings -->
T4_EOF

cat > project/llm-files/research-findings/run-2026-10-09-1400-research/ice-trade/topic-5.md << 'T5_EOF'
# Findings - Topic 5: Ice houses at the far ports

## Passage 1

The failure at Martinique in 1806 taught the trade its first rule: build the ice house before the ice arrives. Without a place to keep it, a cargo had to be sold off the ship in a few days, at whatever price the market would pay, and most of it melted before it could be sold. From the 1810s onward the firms built or rented an ice house in each port before sending regular cargoes. In some ports the first ice house was a converted warehouse with extra walls added inside; in others it was a new building put up to the firm's own plan. The firms sent carpenters from Boston with the first cargo to a new port to see the work done.

Evidence: verified

Sources:
- https://www.harvard-business-archive.example/tudor-papers/diary-excerpts (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt (book excerpt on a publisher's site, 2005)

## Passage 2

The Calcutta ice house was paid for by a subscription among the city's merchants after the first cargo arrived in 1833, and it opened a few years later. It was a round building of brick near the river, with thick walls and a domed roof, and when full it held about 1,250 tons of ice. The round shape gave the smallest wall surface for the space inside. The building was one of the best known in the city's European quarter, and it appears in several paintings and later photographs of the riverside.

Evidence: verified

Sources:
- https://www.calcutta-history-society.example/buildings/the-ice-house (local history society article, 2011)
- https://www.british-library-images.example/calcutta/ice-house-1840s (library image catalogue entry, drawing dated 1840s)

## Passage 3

The Calcutta house followed the plan of the Boston icehouses, with an inner and outer wall and a packed space between, but it was built of brick instead of wood. Wood in Calcutta was attacked by termites and rotted in the damp of the monsoon. The space between the walls was packed with a fill brought from Boston at first and later with local materials. The floor drained to the river through a channel. The roof was raised over a ventilated space, so that hot air under the dome could escape before it reached the ice.

Evidence: reported

Sources:
- https://www.calcutta-history-society.example/buildings/the-ice-house (local history society article, 2011)
- https://www.colonial-architecture-journal.example/2016/cold-storage-in-bengal (peer-reviewed article, 2016)

## Passage 4

In Havana and some other ports the ice houses were partly sunk into the ground. The lower part of the building was dug below the level of the street, where the earth stayed cooler than the air, and the upper part stood above it with thick walls and a raised roof. Sinking the building only worked where the ground was dry; in ports built on low wet ground, such as New Orleans, the houses had to stand fully above ground. The sunken design kept the lowest layers of ice noticeably colder than the top layers.

Evidence: reported

Sources:
- https://www.havana-archive.example/colonial-trade/building-permits (digitized city records, 1820s to 1850s)
- https://www.colonial-architecture-journal.example/2016/cold-storage-in-bengal (peer-reviewed article, 2016)

Reliability: the architecture article compares ports and gives the Havana design as a contrast to Calcutta.

## Passage 5

The Havana ice house was built by the Tudor firm near the harbour in the 1820s, after the firm was granted the right to sell ice in the city. The right was a monopoly granted by the Spanish colonial government, which ruled Cuba, in return for a promise to keep the city supplied. The firm had to keep ice on hand through the year, and the government could fine it for running out. The monopoly was renewed several times. It gave the firm a market with no rivals in one of the hottest and busiest ports of the Caribbean.

Evidence: verified

Sources:
- https://www.havana-archive.example/colonial-trade/ice-monopoly (digitized colonial government records, 1820s to 1840s)
- https://www.harvard-business-archive.example/tudor-papers/agents-letters (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 6

New Orleans had several large ice houses on the levee by the 1840s, owned by different firms competing for the same market. The houses stood next to the wharves where the ice ships unloaded, so the ice went from the hold into storage in a few hours. Competition between the New Orleans houses kept prices lower there than in ports with a single seller. Some of the houses also stored ice for the river steamboats, which took it on board for their passengers and for sale in the towns upriver.

Evidence: verified

Sources:
- https://www.gulf-commerce.example/ports/new-orleans-ice-imports (business history society page, 2013)
- https://www.louisiana-archives.example/levee/warehouse-registers (state archives catalogue entry, 1840s)

## Passage 7

Bombay and Madras got ice houses after Calcutta had shown the trade could work in India. Both were built in the late 1830s and early 1840s on the Calcutta model, with thick masonry walls and drained floors. The Madras house stood close to the beach, because Madras had no sheltered harbour and the ice was brought ashore through the surf in small boats, which meant every block was handled more and lost more on the way to the house. Neither house was as large as the one in Calcutta.

Evidence: reported

Sources:
- https://www.colonial-architecture-journal.example/2016/cold-storage-in-bengal (peer-reviewed article, 2016)
- https://www.madras-heritage.example/beach-road/ice-house (heritage trust page, 2019)

## Passage 8

Charleston and Savannah had smaller ice houses, built of wood on the Boston plan and raised on brick piers to keep them off the damp ground. They held enough for a few weeks of local sales, and were filled from ships that called every few weeks in summer. In winter the southern ports needed little ice, and the houses were sometimes left empty for months and used to store other goods. The smaller southern houses were often owned by local merchants who bought ice by the cargo from the Boston firms and sold it on, rather than by the firms themselves.

Evidence: reported

Sources:
- https://www.lowcountry-history.example/charleston/ice-trade (local history society page, 2014)
- https://www.gulf-commerce.example/ports/new-orleans-ice-imports (business history society page, 2013)

## Passage 9

In Havana the ice ships could not come alongside a wharf near the ice house, so the ice was unloaded into lighters, flat-bottomed harbour boats, and rowed ashore. The blocks were then carried from the landing to the ice house by hand and in carts. The unloading was done at night, by lantern, to keep the blocks out of the sun. Each handling cost ice, and the firm's records show a steady effort to shorten the distance from the landing to the house, including a change of landing place in the 1840s to one closer to the building.

Evidence: reported

Sources:
- https://www.havana-archive.example/colonial-trade/shipping-arrivals (digitized port records, 1830s to 1850s)

## Passage 10

The Havana house was run for the Tudor firm by its agent there, a local merchant named Joaquín Barcia, who managed the house and its sales through the 1840s. Barcia sold the ice by ticket. A customer bought a ticket at the firm's office in the city for a set weight of ice, then took the ticket to the door of the ice house and was handed the ice there. The ticket system meant that no money changed hands at the ice house door, so the door could be opened and shut quickly, and the office could keep an exact count of what was sold. Barcia's monthly accounts, sent to Boston, list the tickets sold by weight.

Evidence: verified

Sources:
- https://www.havana-archive.example/colonial-trade/ice-depot-1840s (digitized commercial records with catalogue notes, 1840s)

## Passage 11

Hong Kong got its first ice house in the 1840s, soon after the British took the island, built by a firm that shipped ice from Boston by way of the Indian ports. It stood on the waterfront and was built of granite, which was quarried on the island. The Hong Kong trade was small and irregular, because the voyage was even longer than the voyage to Calcutta and the ice arrived in poorer condition. Records of the house are thin, and most of what is known comes from newspaper notices announcing the arrival of ice and the hours of sale.

Evidence: reported

Sources:
- https://www.hongkong-heritage.example/waterfront/early-ice-house (heritage society page, 2017)

Reliability: the heritage page relies on newspaper notices and gives no building records.

## Passage 12

The Calcutta ice house was run by an agent sent out from Boston, with a staff of local workers who unloaded the ships, stacked the ice, and served the customers. The agent's letters home describe the labour of unloading a ship in the heat: the work was done at night and in the hours before dawn, and the blocks were carried from the river to the house as fast as possible. The agent also dealt with the merchants' committee that had paid for the building, which kept an interest in how the house was run and complained when ice ran short.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/agents-letters (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.calcutta-history-society.example/buildings/the-ice-house (local history society article, 2011)

## Passage 13

The ice houses opened for sale only in the early morning. The doors were opened at first light and closed again by the middle of the morning, before the heat of the day. Customers or their servants queued at the door with baskets. Keeping the doors shut through the heat saved more ice than any other rule of the far-port houses. In Calcutta the hours were printed in the newspapers, and a customer who came late was turned away until the next morning.

Evidence: verified

Sources:
- https://www.calcutta-history-society.example/buildings/the-ice-house (local history society article, 2011)
- https://www.calcutta-gazette-archive.example/notices/ice-house-hours (digitized newspaper notices, 1830s to 1850s)

## Passage 14

Customers carried ice home wrapped in blankets or flannel, inside a basket or a wooden box lined with cloth. Servants in Calcutta carried the baskets on their heads at a run, and descriptions of the morning rush to the ice house appear in several British memoirs of life in the city. At home the ice was kept in a box lined with felt or in a pot of water inside a larger pot, and it lasted a day or so. The wealthier households had a wooden ice chest shipped out from Boston for the purpose.

Evidence: reported

Sources:
- https://www.memoirs-of-empire.example/collections/calcutta-domestic-life (digitized memoir collection, 1840s to 1860s)
- https://www.calcutta-history-society.example/buildings/the-ice-house (local history society article, 2011)

Reliability: the memoirs are by British residents and describe their own households.

## Passage 15

Ice was sold by weight. Each house kept a large scale at the door, and the ice was weighed out in front of the customer. In ports where the ticket system was used, the weight was printed on the ticket and checked on the scale. In others the customer paid at the door. Weighing at the door was slow, and some houses kept a stock of blocks cut to standard weights ready inside the door, so that a customer could be handed a block of the weight asked for without waiting.

Evidence: reported

Sources:
- https://www.gulf-commerce.example/ports/new-orleans-ice-imports (business history society page, 2013)
- https://www.calcutta-gazette-archive.example/notices/ice-house-hours (digitized newspaper notices, 1830s to 1850s)

## Passage 16

Large buyers had accounts. Hotels, clubs, hospitals, and the military messes took ice every day and were billed by the month rather than paying at the door. In Calcutta the hospitals and the officers' messes were among the largest customers. Account customers were often served first, before the queue, which caused complaints in the newspapers from private buyers who had waited since dawn. The firms valued the account customers because their demand was steady through the year.

Evidence: reported

Sources:
- https://www.calcutta-gazette-archive.example/notices/ice-house-hours (digitized newspaper notices, 1830s to 1850s)
- https://www.harvard-business-archive.example/tudor-papers/agents-letters (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 17

Some houses delivered. In New Orleans by the 1850s, carts carrying ice in insulated boxes went round the streets each morning delivering to hotels, bars, and households that had standing orders. Delivery spread the ice further through the city but cost ice to the heat along the way, so it was only worth doing in a city with enough customers close together. In Havana and Calcutta, delivery was rare and most ice was collected from the house door.

Evidence: reported

Sources:
- https://www.gulf-commerce.example/ports/new-orleans-ice-imports (business history society page, 2013)

## Passage 18

Ice kept far less well in the tropical ice houses than in the houses at home. The air outside was hot all year, and the ground under the houses was warm. Agents' letters report losses in the far-port houses that ran higher, month for month, than any loss recorded at the ponds. The agents tried to sell each cargo before the next arrived, so that ice did not sit in the house for long. A cargo that arrived while the house was still full was a problem, because there was nowhere good to put it.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/agents-letters (finding aid and transcriptions of a merchant's papers, 2009)

Reliability: the agents report losses in general terms, not as figures that can be compared with the pond ledgers.

## Passage 19

Agents had to teach people how to use ice. In ports where ice was new, the agents handed out ice free at first, showed bar owners how to cool drinks, showed cooks how to make ice cream, and persuaded doctors to use ice to cool patients with fever. Tudor's own diary records that he gave ice away in Havana and Charleston until the habit took hold, and then began charging. The agents also sold ice chests shipped from Boston, so that buyers could keep their ice at home for longer and so buy more of it.

Evidence: verified

Sources:
- https://www.harvard-business-archive.example/tudor-papers/diary-excerpts (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.food-history-quarterly.example/2012/ice-cream-in-the-tropics (peer-reviewed article, 2012)

## Passage 20

The agents were usually paid a share of the sales rather than a fixed wage. This gave them a reason to sell as much as possible, but it also led to quarrels with the firms in Boston when a cargo arrived in poor condition and sales fell. Several agents' letters argue that a bad cargo was the fault of the stow in Boston, not of the agent's selling. Some agents were local merchants who also traded in other goods; others were young men from Boston sent out to learn the business.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/agents-letters (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 21

The buildings outlived the trade in some ports. The Madras ice house was later used as a home and then as a school, and it still stands on the Madras seafront, now a museum. The Calcutta house was pulled down in the late nineteenth century. The Havana house was absorbed into the buildings of the harbour and has not been traced. The surviving building in Madras is the best physical evidence for how the far-port houses were built, though it was altered for each of its later uses.

Evidence: verified

Sources:
- https://www.madras-heritage.example/beach-road/ice-house (heritage trust page, 2019)
- https://www.calcutta-history-society.example/buildings/the-ice-house (local history society article, 2011)

<!-- end of findings -->
T5_EOF

cat > project/llm-files/research-findings/run-2026-10-09-1400-research/ice-trade/topic-6.md << 'T6_EOF'
# Findings - Topic 6: The workers

## Passage 1

The harvest came in the slack season of the farming year, when there was little work on the land, and in the early years of the trade most of the men on the ice were local farmers and their sons. They brought their own horses and were paid for the horse as well as the man. For a farm family the ice harvest was a source of cash in the months when the farm earned nothing. Some farmers worked the same pond every winter for decades, and their families kept the job from one generation to the next. Local newspapers listed the farms that sent men and teams to the larger ponds.

Evidence: verified

Sources:
- https://www.labor-history-ne.example/winter-work/farm-families (regional labour history project page, 2016)
- https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview (local historical society article, 2017)

## Passage 2

From the 1840s a growing share of the harvest crews were Irish immigrants. Large numbers of Irish families arrived in Boston in the 1840s, many of them during and after the famine in Ireland, and the men took whatever labouring work they could find. The ice harvest was one of the few kinds of work available in midwinter. The firms hired Irish labourers in large numbers for the unskilled jobs on the ice, while the skilled jobs often stayed with local men. Some of the Irish labourers lived through the winter in shanties put up near the ponds.

Evidence: verified

Sources:
- https://www.labor-history-ne.example/winter-work/irish-labour (regional labour history project page, 2016)
- https://www.immigration-history-journal.example/2012/boston-irish-winter-work (peer-reviewed article, 2012)

## Passage 3

Men were hired by the day at the edge of the pond. On a morning when the ice was ready, the foremen chose the men they wanted from those who had gathered on the shore, and the rest were sent away. Men who were chosen one day had no promise of work the next. The system gave the firms a crew that could grow or shrink with the weather, and it left the labourers without work on any day the weather stopped the harvest. Oral histories describe men walking several miles to a pond before dawn on the chance of a day's hire.

Evidence: reported

Sources:
- https://www.walden-region-history.example/oral-histories/ice-crews (oral history collection, transcribed 1974)

Reliability: the oral histories come from the last commercial harvests and may not describe the early trade.

## Passage 4

Some jobs on the ice needed skill and were kept by the same men year after year. The men who drove the marker had to keep the lines straight, because a crooked grid made blocks of uneven size. The stackers inside the icehouse had to build a stack that would stand for months. The bar men had to split the blocks cleanly along the grooves. These men were hired for the whole season, not by the day, and were paid more than the labourers. The firms kept lists of their skilled men and wrote to them before each season to ask them back.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/harvest-instructions (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.labor-history-ne.example/winter-work/farm-families (regional labour history project page, 2016)

## Passage 5

Each crew had a foreman, who answered to the firm's superintendent for the pond. The foreman decided when to start cutting, where to cut, and which men to hire, and he kept the daily notebook of weather and ice thickness. A good foreman was the most valuable man on the pond, and the firms competed to hire the best. Several foremen worked for the same firm for twenty years or more, and the firms' papers include letters from foremen giving advice on new tools and methods.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/harvest-instructions (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 6

The firms brought in labourers from outside the district when the local supply was short. In a hard winter when several ponds were ready at once, agents went to Boston and hired men off the street, and the firms paid their train fares out to the ponds. The outside men were less skilled and less used to the cold, and foremen's notebooks complain that they worked slowly and left early. In years of plenty the firms took only local men and the regular Irish crews.

Evidence: reported

Sources:
- https://www.labor-history-ne.example/winter-work/irish-labour (regional labour history project page, 2016)

## Passage 7

Women did not work on the ice itself, but the harvest depended on their work on shore. Women ran the boarding houses where outside men slept, cooked the meals served in the shore shanties, and washed and dried the crews' wet clothing overnight. On farms that sent men and horses to the ponds, the women and older children took on the farm's winter work while the men were away. The firms' accounts show payments to women for meals and lodging, usually under the name of the household rather than the woman herself.

Evidence: reported

Sources:
- https://www.labor-history-ne.example/winter-work/farm-families (regional labour history project page, 2016)
- https://www.harvard-business-archive.example/tudor-papers/pond-accounts (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 8

In the later decades of the trade, French-Canadian labourers came south to the Massachusetts ponds for the harvest. Many of them already worked in the New England mill towns and took the ice work as a winter job; others came down from Quebec for the season and went home in the spring. The firms valued them as men used to hard cold. By the 1870s some crews on the larger ponds were mostly French-Canadian, and foremen's notebooks from that time record names that are almost all French.

Evidence: reported

Sources:
- https://www.immigration-history-journal.example/2015/french-canadians-in-new-england (peer-reviewed article, 2015)

## Passage 9

On the largest ponds a harvest crew numbered about 75 men. The crew was divided into gangs, each with its own task: a gang to scrape snow, a gang on the marker and plough, a gang of bar men splitting the blocks, channel men with pike poles moving the blocks to shore, a gang at the elevator, and a gang of stackers inside the house. The gangs worked in sequence, so the speed of the slowest gang set the speed of the whole crew, and the foreman moved men between gangs during the day to keep the blocks moving. A smaller pond might use only a third as many men with the same gangs in smaller numbers.

Evidence: verified

Sources:
- https://www.labor-history-ne.example/winter-work/harvest-crew-sizes (regional labour history project page, 2016)

## Passage 10

The labourers were paid at the end of each week, on Saturday evening at the shore shanty, from a cash box the superintendent brought out from the firm's office. Men who boarded with the firm had the cost of their board taken out of their pay. A man hired by the day who worked only part of a week was paid for the days he worked. The pay books for one pond survive for several seasons and list each man by name, the days he worked, and what he was paid, and they are one of the few records of the individual labourers.

Evidence: verified

Sources:
- https://www.harvard-business-archive.example/tudor-papers/pond-accounts (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 11

The mixed crews did not always get along. Newspaper reports describe fights on the ice between local men and Irish labourers, especially in years when work was short and the two groups competed for places on the crew. The local men resented the newcomers for working for lower pay, and the Irish labourers resented being kept out of the skilled jobs. Foremen sometimes kept the groups in separate gangs to avoid trouble. The tension eased in later decades as the Irish families settled and their sons took up the skilled jobs themselves.

Evidence: reported

Sources:
- https://www.immigration-history-journal.example/2012/boston-irish-winter-work (peer-reviewed article, 2012)
- https://www.boston-newspaper-archive.example/1851/january/disturbance-on-the-ice (digitized newspaper, January 1851)

Reliability: the newspaper reports are short and give one side.

## Passage 12

The working day ran from first light to dark, which in midwinter was a short day. When the weather was right and a thaw was forecast, the firms ran the elevators and the stacking crews into the night by lantern light, and some crews worked on Sundays. The labourers were paid by the day, and a long day earned no more than a short one unless the foreman agreed to pay extra. Newspaper reports from busy seasons describe lanterns on the ice late into the night.

Evidence: reported

Sources:
- https://www.boston-newspaper-archive.example/1858/january/ice-crop (digitized newspaper, January 1858)

## Passage 13

The cold was the hardship every account mentions. The men stood on the ice all day in temperatures well below freezing, often in wind with no shelter. Frostbite of the fingers, ears, and feet was common. The men wore several layers of wool, felt boots with leather overshoes, and iron "creepers," small spiked plates strapped to the boots to grip the ice. Wet clothing was the great danger, because a man who got wet on the ice could freeze before he reached shelter, so men who fell into the channel were sent straight to the fire in the shore shanty.

Evidence: verified

Sources:
- https://www.walden-region-history.example/oral-histories/ice-crews (oral history collection, transcribed 1974)
- https://www.labor-history-ne.example/winter-work/ice-crews-conditions (regional labour history project page, 2016)

## Passage 14

The firms fed the crews on the larger ponds. A shanty on the shore had a stove where coffee and soup were kept hot all day, and the men were given a hot midday meal. Men who came from a distance slept in boarding houses near the ponds or in bunkhouses the firms put up for the season. The food and shelter were a large part of what made the work bearable, and oral histories remember the shanty fire as the centre of the harvest.

Evidence: reported

Sources:
- https://www.walden-region-history.example/oral-histories/ice-crews (oral history collection, transcribed 1974)

## Passage 15

Boys worked on the ice too, usually from about the age of twelve. They guided floating blocks along the channel with short poles, swept chips from the cleared field, carried messages between the gangs, and fetched coffee from the shanty. Boys were paid less than men for the same hours. Some of the men interviewed for the oral histories had first worked on the ice as boys alongside their fathers.

Evidence: reported

Sources:
- https://www.walden-region-history.example/oral-histories/ice-crews (oral history collection, transcribed 1974)
- https://www.labor-history-ne.example/winter-work/farm-families (regional labour history project page, 2016)

## Passage 16

The men who loaded the ships were a different workforce from the harvest crews. The ice stevedores on the Boston and Charlestown wharves worked all year, loading ice and other cargoes, and they belonged to the waterfront rather than to the farms. They worked in gangs under a boss who contracted with the ice firms for each ship. Their work was paid by the ton loaded, and the fastest gangs were the best paid on the wharves.

Evidence: reported

Sources:
- https://www.boston-harbour-history.example/wharves/stevedores (local history society page, 2011)

## Passage 17

At the far ports the ice was handled by local workers. In Calcutta, porters hired by the agent carried the blocks from the ships to the ice house, working at night and in the hours before dawn. In Havana, colonial records show that the firm's depot hired enslaved men from their owners to unload the ice ships, as was common for dock work in the city at the time. The agents' letters mention these workers only in passing, and almost nothing is recorded of their own experience of the work.

Evidence: reported

Sources:
- https://www.havana-archive.example/colonial-trade/dock-labour-contracts (digitized colonial records, 1830s to 1850s)
- https://www.harvard-business-archive.example/tudor-papers/agents-letters (finding aid and transcriptions of a merchant's papers, 2009)

Reliability: the records are contracts and letters by employers; no account by the workers survives in these collections.

## Passage 18

Harvest crews sometimes struck. In seasons when the ice was ready and a thaw was forecast, the labourers knew the firms could not afford a day's delay, and crews on several ponds stopped work and demanded higher daily pay. Newspaper reports from the 1850s and 1860s describe strikes lasting a day or two that ended when the firms agreed. The firms answered by hiring outside men in later seasons and by keeping lists of strikers they would not hire again.

Evidence: reported

Sources:
- https://www.boston-newspaper-archive.example/1866/february/ice-strike (digitized newspaper, February 1866)
- https://www.labor-history-ne.example/winter-work/irish-labour (regional labour history project page, 2016)

Reliability: the newspaper reports take the firms' side.

## Passage 19

Injuries were common. Men slipped and fell on the ice, cut themselves with the long saws and the breaking bars, and were crushed when blocks slipped on the elevator or a stack shifted in the icehouse. A block that fell from the top of the elevator could kill a man. The firms paid nothing to an injured man beyond the days he had already worked, and men who were hurt went home and hoped to be well before the next harvest.

Evidence: reported

Sources:
- https://www.labor-history-ne.example/winter-work/ice-crews-conditions (regional labour history project page, 2016)
- https://www.walden-region-history.example/oral-histories/ice-crews (oral history collection, transcribed 1974)

## Passage 20

A mild winter was a disaster for the labourers. When the ponds did not freeze thick enough, there was no harvest and no winter wage, and the men who depended on the ice for their winter cash had none. In these years the firms bought ice from ponds further north and hired crews there, so the work moved north and the men around Boston went without. Charities in Boston reported larger numbers of families seeking help in the winters after an open season.

Evidence: reported

Sources:
- https://www.boston-newspaper-archive.example/1880/march/open-winter-hardship (digitized newspaper, March 1880)

## Passage 21

The worst danger on the ice was falling through. The cut field, the open channel, and the thin new ice that formed over the channel at night were all traps for men working in the dark or in snow. A man who went into the channel could be carried under the ice by the current or trapped among the floating blocks. A count of local newspaper reports for the Cambridge ponds recorded nine drownings among harvest crews between 1850 and 1860, most of them men who fell into the open channel at night. The firms put up no railings or lights along the channel until late in the trade.

Evidence: reported

Sources:
- https://www.labor-history-ne.example/winter-work/ice-crews-conditions (regional labour history project page, 2016)
- https://www.boston-newspaper-archive.example/1858/january/ice-crop (digitized newspaper, January 1858)

Reliability: the drowning count comes from newspaper reports, which may have missed some deaths.

<!-- end of findings -->
T6_EOF

cat > project/llm-files/research-findings/run-2026-10-09-1400-research/ice-trade/topic-7.md << 'T7_EOF'
# Findings - Topic 7: Buyers and prices

## Passage 1

In Calcutta the first buyers were the British residents of the city: officials of the East India Company, army officers, merchants, and their families. They bought ice to cool drinks, to make iced desserts, and to cool rooms in the worst of the hot season. Wealthy Indian merchants and landowning families also bought ice from the early years, and by the 1840s they were among the ice house's regular customers. For most of the city's population ice was far too costly to buy at all.

Evidence: verified

Sources:
- https://www.calcutta-history-society.example/buildings/the-ice-house (local history society article, 2011)
- https://www.memoirs-of-empire.example/collections/calcutta-domestic-life (digitized memoir collection, 1840s to 1860s)

## Passage 2

In the 1830s and 1840s, ice in Calcutta sold at the ice house door for 3 annas a pound, an anna being a sixteenth of a rupee. The price was printed in the newspaper notices that announced the ice house's hours, and it held steady for most of those two decades. At that price a household that bought ice every day spent a noticeable part of its income on it, and ice remained a mark of comfort and status. Prices paid by account customers were sometimes lower, by private agreement with the agent.

Evidence: verified

Sources:
- https://www.calcutta-gazette-archive.example/notices/ice-house-hours (digitized newspaper notices, 1830s to 1850s)
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

## Passage 3

Hospitals were among the most important buyers in every hot port. Doctors used ice to bring down fevers, to cool patients with heatstroke, and to treat wounds and inflammation. In Calcutta the hospitals were among the ice house's largest account customers, and doctors' letters in the city's newspapers argued that ice saved lives in the hot season. In New Orleans, ice was used in the yellow fever epidemics of the 1850s, and the hospitals bought it in large amounts during each outbreak.

Evidence: verified

Sources:
- https://www.medical-history-journal.example/2013/ice-in-tropical-medicine (peer-reviewed article, 2013)
- https://www.calcutta-gazette-archive.example/notices/ice-house-hours (digitized newspaper notices, 1830s to 1850s)

## Passage 4

Clubs, hotels, and military messes bought ice every day. In Calcutta the clubs of the British residents served iced drinks through the hot season, and the officers' messes did the same. Visitors to the city wrote home about iced claret and iced water served at dinner, and about the luxury of cold drinks in a city where the temperature in the hot season rarely fell at night. The clubs' own records show ice as one of their largest regular costs in the hot months.

Evidence: reported

Sources:
- https://www.memoirs-of-empire.example/collections/calcutta-domestic-life (digitized memoir collection, 1840s to 1860s)

Reliability: the memoirs describe the experience of British residents only.

## Passage 5

In Havana, the main buyers were cafés, confectioners, and the households of the wealthy. The cafés served iced drinks and the confectioners made ice creams and sorbets, which became a feature of the city's evening life around the main squares. Wealthy households bought ice daily through the hot months. The firm's agent there sold to the cafés on account and to households by ticket. Ice in Havana spread from a luxury of the rich to a common pleasure in the city's cafés within a generation.

Evidence: verified

Sources:
- https://www.havana-archive.example/colonial-trade/ice-monopoly (digitized colonial government records, 1820s to 1840s)
- https://www.food-history-quarterly.example/2012/ice-cream-in-the-tropics (peer-reviewed article, 2012)

## Passage 6

The price of ice in Havana was not set by the market alone. Under the monopoly granted by the Spanish colonial government, the firm agreed to a maximum price in return for its sole right to sell, and the government could lower the maximum if supplies ran short or the public complained. The government's records show the maximum price being revised several times. The monopoly gave the firm a secure market, but the fixed maximum meant it could not raise prices in the hottest weeks when demand was highest.

Evidence: verified

Sources:
- https://www.havana-archive.example/colonial-trade/ice-monopoly (digitized colonial government records, 1820s to 1840s)

## Passage 7

New Orleans used ice on a scale no other port matched. Its bars served iced drinks to every class of customer, its hotels used ice in their dining rooms and kitchens, and its households bought ice for the kitchen and the sickroom. The city's meat and fish markets packed their goods in ice. River steamboats bought ice at New Orleans for their passengers' drinks and their kitchens. By the 1850s the city's daily ice consumption was described in the local press as a necessity rather than a luxury.

Evidence: verified

Sources:
- https://www.gulf-commerce.example/ports/new-orleans-ice-imports (business history society page, 2013)
- https://www.louisiana-archives.example/newspapers/daily-ice-reports (digitized newspaper collection, 1840s to 1850s)

## Passage 8

In Madras and Bombay, ice cost more than in Calcutta. At Madras every block had to be brought through the surf in small boats, which lost ice and added labour, and Bombay received fewer and less regular cargoes. Newspaper notices in both cities give prices above those printed in Calcutta for the same years. The buyers were much the same as in Calcutta: the British residents, the clubs and messes, the hospitals, and wealthy Indian and Parsi merchant families.

Evidence: reported

Sources:
- https://www.madras-heritage.example/beach-road/ice-house (heritage trust page, 2019)
- https://www.bombay-gazette-archive.example/notices/ice-sales (digitized newspaper notices, 1840s)

## Passage 9

In Charleston and Savannah, the buyers were planters, merchants, hotels, and taverns. Planters' families who spent the summer in the cities bought ice for their households, and the taverns served iced drinks to their customers through the long southern summer. Some plantation households inland had ice carried out to them from the city by wagon and kept it in small icehouses of their own. The markets in these cities were smaller than New Orleans and were often supplied by local merchants who bought whole cargoes from the Boston firms.

Evidence: reported

Sources:
- https://www.lowcountry-history.example/charleston/ice-trade (local history society page, 2014)

## Passage 10

Prices in New Orleans fell steadily from the 1830s to the 1850s. When ice first arrived regularly, it was sold at a high price to a small market of hotels and wealthy households. As more firms shipped ice to the city and built competing ice houses on the levee, the price came down, and as the price came down, more people bought ice. The fall in price was what turned ice from a luxury into an everyday good in the city. The firms made their money on the larger volume rather than on the price of each pound.

Evidence: verified

Sources:
- https://www.gulf-commerce.example/ports/new-orleans-ice-imports (business history society page, 2013)
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

## Passage 11

By 1860, ice in New Orleans sold for about 2½ cents a pound at the ice houses on the levee. The figure comes from the city's weekly "price current," a commercial paper that printed the prices of goods in the city's markets. The price current also shows that the price varied with the season, rising in the hot months and when a ship was late, and falling when several ships arrived together. At this price ice was within reach of ordinary working households in the city for at least part of the year.

Evidence: verified

Sources:
- https://www.gulf-commerce.example/price-current/ice-1860 (digitized commercial price paper with society notes, 1860)

## Passage 12

By the 1850s ordinary households in New Orleans and other southern cities bought ice regularly, not only the rich. Small amounts were sold from carts in the street, and grocers kept ice for their customers. Visitors from the North and from Europe remarked on how freely ice was used in the southern cities, in drinks served in the cheapest bars. The southern trade was by far the largest part of the whole ice trade by volume, and most of its customers were ordinary people buying a little at a time.

Evidence: reported

Sources:
- https://www.louisiana-archives.example/newspapers/daily-ice-reports (digitized newspaper collection, 1840s to 1850s)

## Passage 13

The river steamboats on the Mississippi were steady buyers at New Orleans. Each boat took on ice before it sailed upriver, packed in a small icehouse on board, and served iced drinks to its passengers through the voyage. Some boats also sold ice at the river towns where they stopped, which carried the habit of ice inland, to towns that would never see an ice ship. The steamboat trade appears in the New Orleans papers as a separate line in the reports of the city's ice sales.

Evidence: reported

Sources:
- https://www.louisiana-archives.example/newspapers/daily-ice-reports (digitized newspaper collection, 1840s to 1850s)
- https://www.river-history-review.example/2011/steamboat-provisioning (peer-reviewed article, 2011)

## Passage 14

In Hong Kong the buyers were the British garrison, the merchants of the trading houses, and the ships in the harbour, which bought ice for their officers' tables. The market was small, and ice was sold only when a ship had recently arrived. Newspaper notices in Hong Kong announced each arrival of ice and the hours when it could be bought, and the notices stop for months at a time, showing long gaps when there was no ice in the colony at all.

Evidence: reported

Sources:
- https://www.hongkong-heritage.example/waterfront/early-ice-house (heritage society page, 2017)

## Passage 15

Butchers, fishmongers, and dairies in the southern ports were large buyers. Ice let them keep meat and fish for a day or two longer in the heat, and it let dairies keep milk and butter from souring. In New Orleans the fish market bought ice by the cartload each morning. The use of ice by the food trades changed what could be sold in a hot city, and it made the food trades into steady customers who bought ice every day of the year.

Evidence: reported

Sources:
- https://www.gulf-commerce.example/ports/new-orleans-ice-imports (business history society page, 2013)
- https://www.food-history-quarterly.example/2014/new-england-apples-abroad (peer-reviewed article, 2014)

## Passage 16

The ice itself cost almost nothing at the pond. Most of the price a buyer paid at a far port went on getting the ice there: the harvest labour, the storage, the sawdust, the carriage by sea, the far-port ice house, and above all the ice lost to melting along the way. A study of the trade's costs found that the ice lost in transit and storage was the largest single cost on the long routes, larger than the cost of carriage. This is why the firms worked so hard to reduce melting: every ton saved was a ton that could be sold.

Evidence: verified

Sources:
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

## Passage 17

The ice trade made fortunes. Frederic Tudor, who had been in debtors' prison in his early years, became one of the richest men in Boston by the 1840s, and was known as the "Ice King." Several other Boston firms also grew rich on the trade. The profits came mostly from the steady southern and Caribbean markets, while the Indian trade brought fame and a smaller, less certain profit. Tudor's papers show him moving money between his ice business and other ventures, not all of which succeeded.

Evidence: verified

Sources:
- https://www.harvard-business-archive.example/tudor-papers/diary-excerpts (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt (book excerpt on a publisher's site, 2005)

## Passage 18

The Boston firms competed hard with each other. When a rival firm sent ice to a port Tudor supplied, Tudor sometimes sent extra cargoes and cut his price until the rival gave up, then raised the price again once the market was his. Rivals did the same to him. These price wars are recorded in the firms' letters to their agents, which order the agents to undersell a rival at any cost. Buyers in the contested ports enjoyed periods of cheap ice that ended as suddenly as they began.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/agents-letters (finding aid and transcriptions of a merchant's papers, 2009)
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

Reliability: the letters describe the firm's own tactics from its own side.

## Passage 19

Some buyers in Calcutta were wary of the ice at first. Newspaper reports from the 1830s say that some Indian households questioned whether ice handled by foreign sailors and porters was clean, and that some refused to use it. The same reports describe the doubts fading as the ice house became a familiar part of the city. By the 1840s Indian buyers were a large share of the ice house's private customers.

Evidence: reported

Sources:
- https://www.calcutta-gazette-archive.example/notices/ice-house-hours (digitized newspaper notices, 1830s to 1850s)

Reliability: the reports were written by British newspapers about Indian customers.

## Passage 20

Prices rose and fell with the arrival of ships. In every far port, the price was lowest just after a ship arrived and the ice house was full, and highest when the stock was running low and the next ship was overdue. When a port ran out altogether, ice could not be had at any price until the next ship. Newspaper reports from Calcutta and Havana record the public anger when the ice house ran dry in the hot season. The agents tried to spread their sales so that the house never emptied before the next cargo arrived.

Evidence: reported

Sources:
- https://www.calcutta-gazette-archive.example/notices/ice-house-hours (digitized newspaper notices, 1830s to 1850s)
- https://www.havana-archive.example/colonial-trade/shipping-arrivals (digitized port records, 1830s to 1850s)

## Passage 21

At small ports with no ice house, ice was sometimes sold straight from a ship's hold. A ship bound for a larger port would call, open one hatch, and sell from the top of the stack to whoever came down to the water: planters, shopkeepers, ship captains, and doctors. Prices at these sales were whatever the buyers would pay, and the masters' accounts show prices both well above and well below those at the regular ice houses. The sales were quick, because every hour the hatch stood open cost ice from the rest of the cargo.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/masters-instructions (finding aid and transcriptions of a merchant's papers, 2009)

## Passage 22

Hospitals were sometimes sold ice at a lower price than private buyers. The Calcutta ice house gave the hospitals a reduced rate in return for a contract to take ice every day of the hot season. In New Orleans during the fever epidemics, the city government bought ice for the hospitals and for the poor, and some firms gave ice free for the sick. These arrangements were noticed in the newspapers and helped the firms' standing in the cities they supplied.

Evidence: reported

Sources:
- https://www.medical-history-journal.example/2013/ice-in-tropical-medicine (peer-reviewed article, 2013)

## Passage 23

The ice trade also changed what people expected. In the ports it reached, people came to treat cold drinks and iced food as normal parts of life in the hot season, and they kept buying ice when it later came from local factories instead of from New England. Historians of the trade argue that the New England firms created the demand that the later ice factories supplied. The habit of cold drinks in the hot ports outlived the ships that first brought the ice.

Evidence: reported

Sources:
- https://www.food-history-quarterly.example/2012/ice-cream-in-the-tropics (peer-reviewed article, 2012)
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

<!-- end of findings -->
T7_EOF

cat > project/llm-files/research-findings/run-2026-10-09-1400-research/ice-trade/topic-8.md << 'T8_EOF'
# Findings - Topic 8: The end of the trade

## Passage 1

The ice trade by sea grew through the 1840s and 1850s and reached its height in the years around 1860. After that it declined, slowly at first and then quickly, and by the 1880s the long-distance shipping of New England ice was nearly over. No single cause ended it. Historians of the trade point to several changes that came together: war, machines that made ice, steamships, and the growth of the home market for natural ice. The order in which these mattered differed from port to port.

Evidence: verified

Sources:
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)
- https://www.new-england-industry.example/ice/decline (regional industry history site, 2014)

## Passage 2

The American Civil War, from 1861 to 1865, cut off the southern trade. The Union navy blockaded the Confederate ports, and New Orleans, the largest single market for New England ice, was closed to the Boston ships until Union forces took the city in 1862. The Confederate states went without shipped ice for most of the war. Hospitals in the South were short of ice for the wounded and the fevered, and the shortage was one of the pressures that pushed southern businessmen toward making ice by machine.

Evidence: verified

Sources:
- https://www.civil-war-commerce.example/blockade/ice-shortage (university history project page, 2015)
- https://www.gulf-commerce.example/ports/new-orleans-ice-imports (business history society page, 2013)

## Passage 3

Machines for making ice had been invented before the war. John Gorrie, a doctor in Apalachicola, Florida, built a machine in the 1840s to cool the rooms of fever patients and patented an ice-making machine in 1851, but he could not find backers and died poor. In France, Ferdinand Carré developed an ammonia machine in the late 1850s that could make ice in useful amounts. In Australia, James Harrison built ice machines in the 1850s. None of these early machines threatened the ships at first, because they were costly to run and made small amounts.

Evidence: verified

Sources:
- https://www.mit-tech-history.example/inventors/early-refrigeration (university history of technology page, 2018)
- https://www.patent-records.example/1851/gorrie-ice-machine (digitized patent record, 1851)

## Passage 4

During the war, some Carré machines were brought into the Confederacy through the blockade, by ships that slipped past the Union navy from Mexico and the Caribbean. They were set up to make ice for hospitals and for the few who could pay. The amounts were small, but the machines showed southern businessmen that ice could be made on the spot. After the war, the southern ports never went back to depending wholly on ships from New England.

Evidence: reported

Sources:
- https://www.civil-war-commerce.example/blockade/carre-machines (university history project page, 2015)

Reliability: the project page says the number of machines brought through the blockade is not known.

## Passage 5

The southern trade came back after the war, but not to its old size. Boston firms sent ice to New Orleans again from 1862, once the city was in Union hands, and to the other southern ports after 1865. They found the ice houses damaged or sold, the old agents gone, and buyers who had learned to do without. The firms rebuilt some of the houses and hired new agents. Shipping records show cargoes to the southern ports in the late 1860s well below the levels of the late 1850s.

Evidence: reported

Sources:
- https://www.civil-war-commerce.example/blockade/ice-shortage (university history project page, 2015)
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

## Passage 6

Some of the Boston firms answered the machines by cutting prices, sending more ice to the southern ports and selling it cheaply to drive the new factories out of business, as they had once done to rival shippers. The tactic worked against a few small factories in the 1870s, which closed. It could not work for long, because each new factory made ice more cheaply than the last, and the firms were selling at a loss to hold a market they could not keep.

Evidence: reported

Sources:
- https://www.gulf-commerce.example/ports/new-orleans-ice-imports (business history society page, 2013)

Reliability: the society page gives no list of the factories that closed.

## Passage 7

New Orleans got its first commercial ice factory in 1868, a few years after the war. It used ammonia machines on the Carré pattern and produced about 12 tons a day at first, a small amount next to the cargoes the ships had brought, but it made ice every day of the year with no voyage and no loss to melting on the way. More factories followed in the city over the next decade. Each one took a share of the market that the ships had once held.

Evidence: verified

Sources:
- https://www.louisiana-archives.example/business/ice-manufacturing-charters (state archives catalogue entry, 1868)
- https://www.gulf-commerce.example/ports/new-orleans-ice-imports (business history society page, 2013)

## Passage 8

Factory ice became cheaper than shipped ice. As the machines improved through the 1870s, the cost of making a ton of ice in a southern factory fell below the cost of cutting, storing, shipping, and storing again a ton of New England ice, once the ice lost to melting was counted. The factories could also sell ice in summer when the ships were slow to arrive. In the southern ports the shift happened within about twenty years of the first factories opening.

Evidence: verified

Sources:
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

## Passage 9

Machine ice was cloudy at first. Early factory ice was full of air bubbles and looked white or grey beside the clear pond ice, and buyers who were used to clear blocks from New England distrusted it. Some buyers believed cloudy ice was dirty or unhealthy. The factories learned to make clear ice by stirring or blowing air through the water as it froze, and by the 1880s the best factory ice was as clear as natural ice. The early preference for natural ice slowed the switch to factory ice by several years in some ports.

Evidence: reported

Sources:
- https://www.mit-tech-history.example/inventors/early-refrigeration (university history of technology page, 2018)
- https://www.food-history-quarterly.example/2016/clear-ice-and-cloudy-ice (peer-reviewed article, 2016)

## Passage 10

In India, local ice factories opened in the 1870s and 1880s. A company in Calcutta began making ice by machine in the late 1870s, and similar factories followed in Bombay and Madras. The factories sold ice at prices the shipped ice could not match, and they did not depend on a voyage of four months. The Calcutta ice house that had been the pride of the city's merchants lost its trade within a few years of the factory opening, and it was later pulled down.

Evidence: reported

Sources:
- https://www.calcutta-history-society.example/industry/bengal-ice-factory (local history society article, 2011)
- https://www.calcutta-history-society.example/buildings/the-ice-house (local history society article, 2011)

## Passage 11

Steamships changed the economics of the long routes. The ice trade had relied on sailing ships that would otherwise have left Boston with no cargo, which meant cheap carriage. As steamships took over the routes to Asia, especially after the Suez Canal opened in 1869 and gave steamers a short route to India that sailing ships could not use well, the supply of cheap sailing ships for the outward voyage shrank. Carrying ice on a steamship was faster but cost more, and the steamship's coal took space that might have carried ice.

Evidence: verified

Sources:
- https://www.maritime-boston.example/routes/boston-calcutta (maritime museum article, 2016)
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

## Passage 12

At the same time the home market for natural ice was growing fast. American cities in the North and Midwest used more and more ice for households, breweries, meat packing, and the new refrigerated railway cars that carried meat and fruit across the country. The New England and Hudson valley ponds could sell all the ice they could cut at home, by rail, with no long voyage and far less loss. Many firms turned from the sea trade to the home market, which kept the ponds busy into the early twentieth century.

Evidence: verified

Sources:
- https://www.hudson-valley-museum.example/collections/ice-tool-catalogues (museum collection page, 2020)
- https://www.new-england-industry.example/ice/decline (regional industry history site, 2014)

## Passage 13

The ponds near Boston also became less useful as the city grew. Houses, roads, and factories spread around the ponds, and the water was fouled by runoff and waste. Fresh Pond was taken over as a water supply for the city of Cambridge, and harvesting on it was restricted and then stopped. Other ponds near Boston were filled in or built over. The trade moved to cleaner ponds and lakes further from the city, in northern Massachusetts, New Hampshire, and Maine.

Evidence: verified

Sources:
- https://www.cambridge-historical.example/fresh-pond/water-supply (local historical society article, 2017)
- https://www.new-england-industry.example/ice/decline (regional industry history site, 2014)

## Passage 14

The old firms passed away with their founders. Frederic Tudor died in 1864, during the war, and his firm was run by his family for some years afterwards with less success. Other ice firms were merged into larger companies that dealt mostly in the home market. The sea trade, which had always been a small number of firms with skilled agents in each port, lost the people who had known how to run it. Several historians describe the trade's last years as a slow winding down by firms whose interest had moved elsewhere.

Evidence: reported

Sources:
- https://www.harvard-business-archive.example/tudor-papers/finding-aid-overview (finding aid for a merchant's papers, 2009)
- https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt (book excerpt on a publisher's site, 2005)

## Passage 15

The workers of the shipping trade moved with it. The harvest crews kept cutting ice, now for the home market, and the large ponds of Maine and the Hudson valley employed more men in the 1880s than the Boston ponds had at the height of the sea trade. The ice stevedores on the Boston wharves went back to general cargo. The agents in the far ports either joined the new factories, went into other trades, or returned home. The skills of stowing ice for a four-month voyage were not needed again.

Evidence: reported

Sources:
- https://www.labor-history-ne.example/winter-work/after-the-sea-trade (regional labour history project page, 2016)

## Passage 16

Natural ice itself lasted far longer than the sea trade. The home trade in natural ice from northern ponds and rivers went on in the United States until the 1920s and 1930s, when electric refrigerators in homes and electric ice plants in towns made it unnecessary. The last commercial harvests on many New England ponds were in the 1930s and 1940s. By then the sea trade to Calcutta and Havana was a matter for local historians.

Evidence: verified

Sources:
- https://www.new-england-industry.example/ice/decline (regional industry history site, 2014)
- https://www.walden-region-history.example/oral-histories/ice-crews (oral history collection, transcribed 1974)

## Passage 17

In Havana the monopoly ended and local factories took over. The colonial government stopped renewing the firm's sole right to sell ice in the years after the American war, and ice factories opened in the city in the 1870s. Shipped ice continued to arrive for some years, competing with the factories, but in falling amounts. Cuba's own wars for independence, which began in 1868, also disrupted trade with the island.

Evidence: reported

Sources:
- https://www.havana-archive.example/colonial-trade/ice-monopoly (digitized colonial government records, 1820s to 1840s)
- https://www.cuba-commerce-history.example/1870s/manufactures (university research project page, 2014)

Reliability: the colonial records end before the monopoly's last years; the later account comes from the research project.

## Passage 18

The Indian trade dwindled through the 1870s. Cargoes to Calcutta became smaller and less frequent, and some years saw only one or two ships. The firms kept the route going mainly for the sake of established customers and the return cargoes, but each year the agents reported lower sales against the local factories. The Bombay and Madras trade ended before the Calcutta trade did.

Evidence: reported

Sources:
- https://www.ice-trade-voyages.example/registers/calcutta-arrivals (university research project register, 2018)
- https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)

## Passage 19

Sources disagree about when the shipping trade ended altogether. Some histories say it ended in the early 1880s; a general history of the trade says that cargoes to the Caribbean continued irregularly into the 1890s, and that small shipments of natural ice to the southern ports went on into the early twentieth century in years when the local factories could not keep up. The difference may come from what each writer counts as the trade: the long voyages to Asia, or any ice sent by sea from New England.

Evidence: reported

Sources:
- https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt (book excerpt on a publisher's site, 2005)
- https://www.new-england-industry.example/ice/decline (regional industry history site, 2014)

Reliability: the book excerpt gives no source for the later shipments.

## Passage 20

The end of the trade was hardly noticed at the time. The Boston newspapers that had reported the first ice ships to Calcutta and Havana with pride printed no reports of the last ones. By the 1880s the sea trade was a small part of a much larger natural ice business, and the newspapers' attention had moved to the home market, the size of each winter's harvest, and the price of ice in the cities. The first full histories of the sea trade were written in the twentieth century, from the firms' papers and the ships' records.

Evidence: reported

Sources:
- https://www.boston-newspaper-archive.example/1880s/ice-coverage-survey (newspaper archive research note, 2019)

## Passage 21

The ice trade left words behind. The "icebox," a wooden cabinet lined with metal and packed with a block of ice, came into wide use in American homes during the years of the natural ice trade, and the word stayed in use long after electric refrigerators replaced the real thing. The "iceman" who delivered blocks to homes remained a familiar figure in American cities into the twentieth century. Both belong more to the home trade than to the sea trade, but they grew out of the habit of using ice that the sea trade helped to spread.

Evidence: reported

Sources:
- https://www.food-history-quarterly.example/2016/clear-ice-and-cloudy-ice (peer-reviewed article, 2016)

## Passage 22

The tools and buildings of the shipping trade mostly disappeared. The large icehouses on the Massachusetts ponds burned, were pulled down, or were left to rot once the harvest stopped. The harvest tools went to scrap or into barns, and some sets later passed into museums. The Madras ice house survives, altered, as does a handful of small farm icehouses in New England. The papers of the Tudor firm survive in a business archive and are the largest single source on how the trade worked.

Evidence: verified

Sources:
- https://www.harvard-business-archive.example/tudor-papers/finding-aid-overview (finding aid for a merchant's papers, 2009)
- https://www.madras-heritage.example/beach-road/ice-house (heritage trust page, 2019)

## Passage 23

The last recorded cargo of New England ice to Calcutta sailed from Boston in 1882 aboard the bark Margaret Ellery. The register of arrivals at Calcutta for that year lists her cargo as ice, consigned to the old ice house company, and no later ice ship appears in the register. The ship's master noted in the ice book that the cargo arrived in fair condition. After her voyage the Calcutta ice house sold only factory ice, and the voyage that had begun with the Tuscany in 1833 ended with no notice in the Boston papers.

Evidence: verified

Sources:
- https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882 (digitized shipping register with catalogue notes, 1882)

<!-- end of findings -->
T8_EOF
