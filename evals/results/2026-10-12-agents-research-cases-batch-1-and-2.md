# 2026-10-12 Agent Runs: Research Cases, Batches 1 and 2

The Research workflow's three graded agents ran on every batch-1 case, and the research-writer ran on the two new batch-2 cases, W6 and W8. Bare Claude also ran on W6 and W8, so they have a baseline. The runner is `_tools/research-run.py`, with `--agent` for the agent runs. It ran every grader in each case's `graders/` folder. Claude checked each run's results against its output, and read two notes by hand. The session that wrote the agent files didn't write the cases, and the workers who wrote the agent files didn't read the cases.

## What Was Run

- **Date:** 2026-10-12, 15:56 to 16:26 EDT.
- **Agents:** `script-asst:research-writer` (claude-opus-5-5), `script-asst:research-planner` (claude-opus-5-5), `script-asst:research-evaluator` (claude-sonnet-5-5), each at effort high, as their agent files pin. The streams confirm each model.
- **Claude Code:** 2.1.296.
- **Runs:** 33 agent runs, three per case, on the agent files as they stood after the writer's rulings of 2026-10-12. Plus 6 bare runs of W6 and W8 on claude-opus-5-5.
- **Commands,** from the plugin's `evals/`:

```bash
python3 _tools/research-run.py --out <dir>/writer-a1 --agent script-asst:research-writer --runs 3 --cases research-writer-01-planted-figure research-writer-02-coverage-gap research-writer-03-source-trail research-writer-06-eight-topics research-writer-08-cut-short
python3 _tools/research-run.py --out <dir>/planner-a2 --agent script-asst:research-planner --runs 3 --cases research-planner-01-every-topic-limits research-planner-02-one-topic-instruction
python3 _tools/research-run.py --out <dir>/evaluator-a2 --agent script-asst:research-evaluator --runs 3 --cases research-evaluator-01-changed-number research-evaluator-02-missing-question research-evaluator-03-foreign-url research-evaluator-04-clean-note
python3 _tools/research-run.py --out <dir>/bare-w6w8 --runs 3 --cases research-writer-06-eight-topics research-writer-08-cut-short
```

- **Errors and timeouts:** none. Every run exited 0. No run was repeated.

## Summary Table

"All checks" counts runs where every grader passed. Bare batch-1 figures are from `2026-10-12-bare-opus-5-5-research-cases-batch-1.md`.

| Case | Agent: all checks | Agent: checks passed, r1 / r2 / r3 | Bare: all checks |
| --- | --- | --- | --- |
| W1 `research-writer-01-planted-figure` | 3 of 3 | 27 / 27 / 27 of 27 | 0 of 3 |
| W2 `research-writer-02-coverage-gap` | 3 of 3 | 27 / 27 / 27 of 27 | 0 of 3 |
| W3 `research-writer-03-source-trail` | 3 of 3 | 29 / 29 / 29 of 29 | 0 of 3 |
| W6 `research-writer-06-eight-topics` | 3 of 3 | 54 / 54 / 54 of 54 | 0 of 3 (52 of 54 each) |
| W8 `research-writer-08-cut-short` | 3 of 3 | 30 / 30 / 30 of 30 | 0 of 3 (24 / 22 / 22 of 30) |
| P1 `research-planner-01-every-topic-limits` | 3 of 3 | 11 / 11 / 11 of 11 | 0 of 3 |
| P2 `research-planner-02-one-topic-instruction` | 3 of 3 | 10 / 10 / 10 of 10 | 0 of 3 |
| E1 to E4 | 12 of 12 | 3 of 3 each | 12 of 12 |
| **Total, agents** | **33 of 33** | | |

## Findings

1. **Every agent holds every Pass line in 3 of 3 runs,** the bar in plan-research-workflow.md 05 item 4. The research-evaluator stays at 12 of 12.
2. **What bare Claude got wrong, the agents get right.** W1: no 7-year figure, no doubt from memory. W3: the tally marks appear nowhere outside Open Research Questions. Every writer note has the `research-light-{research-topic}.md` name, `author: research-writer`, empty `sources`, and the run date with no time. Every plan uses the fixed layout, with nothing waiting in P1.
3. **W6, eight topics and 19,508 words of findings: nothing lost.** Every one of the 16 planted details and every footnote survived, in all three agent runs. Bare Claude also kept all 16 details; its two fails are the file name and `author`. So at 8 topics a single research-writer doesn't lose material or footnotes, and spec-research-workflow.md 11 item 59 doesn't reopen (item 68).
4. **W8, a cut-short file: the trap works.** Bare Claude used the cut-short file in all three runs, with its planted name, badges, and source sites. The agent named topic 2 as cut short in all three, used nothing from it, and listed both dipper questions under Open Research Questions. In r1, read by hand, the open question's wording about dippers comes from topic 1's file, not topic 2's.
5. **The evaluator cases still can't tell the agent from bare Claude.** Both get 12 of 12. Later batches need subtler plants, as the bare-run record said.

## Caveats

1. **One judge call per check, not repeated.**
2. **Earlier runs, before the writer's rulings.** The research-planner and research-evaluator also ran once on their first drafts, 15:52 to 15:56: P1 and P2 6 of 6, E1 to E4 12 of 12. Their files then changed (taken topic names; the own-passage footnote check), so they ran again. Only the second runs are below.
3. **Cost:** printed totals, judges included: research-writer $9.03, research-planner $0.42, research-evaluator $0.65, bare W6 and W8 $6.06. The first planner and evaluator runs cost $1.21.
4. **The raw run folders are in the session's scratchpad** and go when the Mac restarts. Each run's grades, what it wrote, and its reply are copied below.

## Full Outputs

Each run shows its grades, then every file it wrote or changed, then its final reply.

### W1: Planted figure, research-writer agent

Case folder: `research-writer-01-planted-figure`. Run folder: `writer-a1`.

#### Run 1

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-08'
PASS  fm-modified-run-date  found 'modified: 2026-10-08'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-footnotes-resolve   Every marker in the body has a definition under Sources, every definition holds a URL, and every definition is used at least once.  - **Markers in the body:** [^1] through [^7].   - [^1] and [^2] appear in "paint is the only thing keeping rust off it.[^1][^2]"   - [^3] appears in "the finish coats have been lead-free.[^3]"   - [^4] appears in "Spray guns aren't used.[^1][^4]"   - [^5] and [^6] ap
PASS  judge-no-outside-facts   Every factual claim the note makes about the tower matches an item on the findings list or plainly restates one:  - **Rust protection:** "The tower's iron carries no galvanizing or other metal coating. Paint is the only barrier against rust." This matches item 1. - **Coating system:** "Each campaign scrapes damaged areas back to bare metal, applies an anti-corrosion primer, and then puts two fini
PASS  keeps-18-months  found '18 months'
PASS  keeps-25-painters  found '25'
PASS  keeps-five-year-cycle  found 'every 5'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-paint-tonnage  no match
PASS  no-seven-year-cycle  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## How the tower is protected from rust'
PASS  shape-topic-2-section  found '## Who repaints the tower, and how often'
PASS  file-name  expected name written
````

`project/Research/research-light-eiffel-tower-upkeep.md`:

````markdown
---
title: Light Research - Eiffel Tower Upkeep
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08
modified: 2026-10-08
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Topics: (1) how the Eiffel Tower is protected from rust; (2) who repaints the tower, and how often. Limits: present-day practice, with a short historical note where a source gives one.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Eiffel Tower Upkeep

## Summary

The tower's iron has no galvanizing or other metal coating, so paint is the only thing keeping rust off it.[^1][^2] In each repainting campaign, damaged areas are scraped back to bare metal, then an anti-corrosion primer goes on, followed by two finish coats.[^1][^2] Since the campaign that began in 2019, the finish coats have been lead-free.[^3] Painters work by hand with brushes and rollers while roped to the structure. Spray guns aren't used.[^1][^4]

The Société d'Exploitation de la Tour Eiffel (SETE), the company that runs the tower, sets the repainting cycle. That cycle is every 5 years.[^5][^6] A campaign takes about 18 months and is carried out by a team of about 25 specialist painters.[^1][^4]

## How the tower is protected from rust

### What protects the iron

The tower's iron carries no galvanizing or other metal coating. Paint is the only barrier against rust.[^1][^2]

The paint goes on as a layered system. Each campaign scrapes damaged areas back to bare metal, applies an anti-corrosion primer, and then puts two finish coats on top.[^1][^2]

### Lead and the 2019 campaign

Earlier coats of paint on the tower contained lead. Since the campaign that began in 2019, the finish coats have been lead-free. That 2019 campaign was delayed after lead was found in dust around the site.[^3]

### How the paint is put on

The painters work by hand with brushes and rollers, roped to the structure.[^1][^4] Spray guns aren't used because wind would carry the overspray onto visitors and onto the streets below.[^1][^4]

## Who repaints the tower, and how often

### Who sets the cycle and who does the work

The repainting cycle is set by the Société d'Exploitation de la Tour Eiffel (SETE), the company that runs the tower.[^5][^6] The campaign itself is carried out by a team of about 25 specialist painters.[^1][^4]

### How often, and for how long

The tower is repainted every 5 years.[^5][^6] The cycle used to be longer and was shortened after corrosion surveys in the 2000s.[^5][^6]

A campaign takes about 18 months. Work pauses during the worst of the winter weather.[^1][^4]

## Disagreement / Uncertainty

- The 5-year cycle, and its shortening after the 2000s corrosion surveys, come partly from the operator's own annual report, in which the operator is describing its own work.[^5] The other source for this figure is a heritage magazine article.[^6]
- Only a newspaper report supports the move to lead-free finish coats and the 2019 delay over lead in site dust.[^3]

## Useful Details

- The tower's colour is called "Eiffel Tower Brown." It goes on in three shades, darkest at the base and lightest at the top, so that the tower looks like one even colour against the sky.[^7]

## Open Research Questions

- What were the painters' qualifications or employer for a campaign? The findings describe them only as about 25 specialist painters.
- What was the repainting interval before it was shortened after the 2000s corrosion surveys?

## Reliability / Limitations

- `toureiffel.paris (maintenance page)`: the operator's own page, current.
- `toureiffel.paris (colour page)`: the operator's own page, current.
- `construction-history.example`: peer-reviewed journal article, 2021.
- `paris-daily.example`: newspaper report, April 2019.
- `paintingcontractor-mag.example`: trade magazine feature, 2022.
- `sete-annual-report.example`: operator's annual report, 2022. The annual report is the operator describing its own work.
- `french-heritage-review.example`: heritage magazine article, 2020.

## Sources

[^1]: https://www.toureiffel.paris/en/the-monument/maintenance
[^2]: https://www.construction-history.example/journal/2021/eiffel-paint-systems
[^3]: https://www.paris-daily.example/2019/04/eiffel-lead-paint
[^4]: https://www.paintingcontractor-mag.example/features/eiffel-rope-access
[^5]: https://www.sete-annual-report.example/2022/maintenance-cycle
[^6]: https://www.french-heritage-review.example/eiffel/upkeep
[^7]: https://www.toureiffel.paris/en/the-monument/colour
````

Final reply:

````
```json
{ "note": "Research/research-light-eiffel-tower-upkeep.md", "cut_short_topics": [] }
```
````

#### Run 2

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-08'
PASS  fm-modified-run-date  found 'modified: 2026-10-08'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-footnotes-resolve   **Markers used in the body:** [^1] through [^7]. Every one has a definition under Sources. - [^1] and [^2] appear in the Summary ("The iron has no galvanizing or other metal coating.[^1][^2]") and in "What protects the iron." - [^3] appears in the Summary ("the finish coats have been lead-free.[^3]") and in "Lead in the paint." - [^4] appears in the Summary ("Spray guns aren't used.[^1][^4]") and
PASS  judge-no-outside-facts   Every factual claim the note makes about the tower matches an item on the list or plainly restates one:  - **Rust protection:** "The tower's iron has no galvanizing or other metal coating. Paint is the only barrier against rust." This matches the first item. - **Campaign steps:** "Damaged areas are scraped back to bare metal. / An anti-corrosion primer is applied. / Two finish coats go on top." T
PASS  keeps-18-months  found '18 months'
PASS  keeps-25-painters  found '25'
PASS  keeps-five-year-cycle  found 'every 5'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-paint-tonnage  no match
PASS  no-seven-year-cycle  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## How the tower is protected from rust'
PASS  shape-topic-2-section  found '## Who repaints the tower, and how often'
PASS  file-name  expected name written
````

`project/Research/research-light-eiffel-tower-upkeep.md`:

````markdown
---
title: Light Research - Eiffel Tower Upkeep
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08
modified: 2026-10-08
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Two topics: how the Eiffel Tower is protected from rust, and who repaints the tower and how often. The research covers present-day practice, with a short historical note where a source gives one.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Eiffel Tower Upkeep

## Summary

Paint is the only thing that keeps the Eiffel Tower's iron from rusting. The iron has no galvanizing or other metal coating.[^1][^2] In each repainting campaign, damaged areas are scraped back to bare metal and given an anti-corrosion primer and then two finish coats.[^1][^2] Since the campaign that began in 2019, the finish coats have been lead-free.[^3] Painters work by hand with brushes and rollers while roped to the structure. Spray guns aren't used.[^1][^4]

The tower is repainted every 5 years. That cycle is set by the operating company, the Société d'Exploitation de la Tour Eiffel (SETE).[^5][^6] A campaign takes a team of about 25 specialist painters about 18 months.[^1][^4]

## How the tower is protected from rust

### What protects the iron

The tower's iron has no galvanizing or other metal coating. Paint is the only barrier against rust.[^1][^2]

Each repainting campaign follows three steps:[^1][^2]

1. Damaged areas are scraped back to bare metal.
2. An anti-corrosion primer is applied.
3. Two finish coats go on top.

### Lead in the paint

Since the campaign that began in 2019, the finish coats have been lead-free. Earlier coats contained lead.[^3] The 2019 campaign was delayed after lead was found in dust around the site.[^3]

### How the paint is put on

Painters apply the paint by hand with brushes and rollers. They are roped to the structure while they work.[^1][^4] Spray guns aren't used, because wind would carry the overspray onto visitors and the streets below.[^1][^4]

## Who repaints the tower, and how often

### Who does the work

A repainting campaign is carried out by a team of about 25 specialist painters.[^1][^4] The repainting cycle is set by the company that runs the tower, the Société d'Exploitation de la Tour Eiffel (SETE).[^5][^6]

### How often, and how long

The tower is repainted every 5 years.[^5][^6] The cycle used to be longer. It was shortened after corrosion surveys in the 2000s.[^5][^6]

A campaign takes about 18 months.[^1][^4] Work stops during the worst winter weather.[^1][^4]

## Disagreement / Uncertainty

The sources don't contradict each other. Two points rest on narrower sourcing than the rest:

- The 5-year cycle and its shortening after the 2000s corrosion surveys come from the operator's own annual report, which describes the operator's own work, and from a heritage magazine article.[^5][^6]
- The switch to lead-free finish coats in 2019, and the delay caused by lead found in dust around the site, come from a single newspaper report from April 2019.[^3]

## Useful Details

- The tower's colour is called "Eiffel Tower Brown."[^7]
- It is applied in three shades, darkest at the base and lightest at the top, so that the tower looks one even colour against the sky.[^7]

## Open Research Questions

- How many painters were on the team in earlier campaigns, and how long did those campaigns take?
- What was the repainting interval before it was shortened in the 2000s?

## Reliability / Limitations

- `toureiffel.paris (maintenance page)`: The operator's own page, current.
- `construction-history.example`: Peer-reviewed journal article, 2021.
- `paris-daily.example`: Newspaper report, April 2019.
- `paintingcontractor-mag.example`: Trade magazine feature, 2022.
- `sete-annual-report.example`: The operator's annual report, 2022. It is the operator describing its own work.
- `french-heritage-review.example`: Heritage magazine article, 2020.
- `toureiffel.paris (colour page)`: The operator's own page, current.

## Sources

[^1]: https://www.toureiffel.paris/en/the-monument/maintenance
[^2]: https://www.construction-history.example/journal/2021/eiffel-paint-systems
[^3]: https://www.paris-daily.example/2019/04/eiffel-lead-paint
[^4]: https://www.paintingcontractor-mag.example/features/eiffel-rope-access
[^5]: https://www.sete-annual-report.example/2022/maintenance-cycle
[^6]: https://www.french-heritage-review.example/eiffel/upkeep
[^7]: https://www.toureiffel.paris/en/the-monument/colour
````

Final reply:

````
```json
{ "note": "Research/research-light-eiffel-tower-upkeep.md", "cut_short_topics": [] }
```
````

#### Run 3

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-08'
PASS  fm-modified-run-date  found 'modified: 2026-10-08'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-footnotes-resolve   Every marker in the body has a matching definition with a URL, and every definition is used.  **Markers used in the body:** - `[^1]` and `[^2]`: "The iron has no galvanizing or other metal coating.[^1][^2]" - `[^3]`: "The finish coats have been lead-free since the campaign that began in 2019.[^3]" - `[^4]`: "They don't use spray guns.[^1][^4]" - `[^5]` and `[^6]`: "SETE… sets this cycle.[^5][^6]"
PASS  judge-no-outside-facts   Every factual claim the note makes about the tower matches an item on the list or plainly restates one:  - **Rust protection:** "Paint is the only thing that keeps the Eiffel Tower's iron from rusting. The iron has no galvanizing or other metal coating." This matches item 1. - **Campaign sequence:** "Damaged areas are scraped back to bare metal. / An anti-corrosion primer is applied. / Two finish
PASS  keeps-18-months  found '18 months'
PASS  keeps-25-painters  found '25'
PASS  keeps-five-year-cycle  found 'every 5'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-paint-tonnage  no match
PASS  no-seven-year-cycle  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## How the tower is protected from rust'
PASS  shape-topic-2-section  found '## Who repaints the tower, and how often'
PASS  file-name  expected name written
````

`project/Research/research-light-eiffel-tower-upkeep.md`:

````markdown
---
title: Light Research - Eiffel Tower Upkeep
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08
modified: 2026-10-08
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Two topics: how the Eiffel Tower is protected from rust, and who repaints the tower and how often. Limited to present-day practice, with a short historical note where a source gives one.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Eiffel Tower Upkeep

## Summary

Paint is the only thing that keeps the Eiffel Tower's iron from rusting. The iron has no galvanizing or other metal coating.[^1][^2] In each repainting campaign, painters scrape damaged areas back to bare metal, put on an anti-corrosion primer, and then add two finish coats.[^1][^2] They work by hand with brushes and rollers while roped to the structure. They don't use spray guns.[^1][^4] The finish coats have been lead-free since the campaign that began in 2019.[^3]

A team of about 25 specialist painters carries out each campaign, which takes about 18 months.[^1][^4] The tower is repainted every 5 years. The Société d'Exploitation de la Tour Eiffel (SETE), the company that runs the tower, sets this cycle.[^5][^6]

## How the tower is protected from rust

### What protects the iron

The tower's iron has no galvanizing or other metal coating. Paint is the only barrier against rust.[^1][^2]

Each campaign follows the same sequence:[^1][^2]

1. Damaged areas are scraped back to bare metal.
2. An anti-corrosion primer is applied.
3. Two finish coats go on top.

### Lead in the paint

The finish coats have been lead-free since the campaign that began in 2019. Earlier coats contained lead. The 2019 campaign was delayed after lead was found in dust around the site.[^3]

### How the paint is put on

Painters work by hand with brushes and rollers, roped to the structure.[^1][^4] Spray guns are not used, because wind would carry the overspray onto visitors and the streets below.[^1][^4]

## Who repaints the tower, and how often

### Who does the work

A team of about 25 specialist painters carries out each campaign.[^1][^4]

### How often, and for how long

The tower is repainted every 5 years. The Société d'Exploitation de la Tour Eiffel (SETE), the company that runs the tower, sets the cycle.[^5][^6] As a short historical note, the cycle used to be longer. It was shortened after corrosion surveys in the 2000s.[^5][^6]

A campaign takes about 18 months. Work pauses during the worst winter weather.[^1][^4]

## Disagreement / Uncertainty

- **Repainting cycle:** The 5-year figure comes from the operator's 2022 annual report, which is the operator describing its own work,[^5] and from a 2020 heritage magazine article.[^6]
- **Lead-free finish coats:** The change to lead-free coats and the lead found in dust in 2019 come from a single newspaper report from April 2019.[^3]

## Useful Details

- The tower's colour is called "Eiffel Tower Brown." It is put on in three shades, darkest at the base and lightest at the top, so that the tower looks one even colour against the sky.[^7]

## Open Research Questions

- What was the repainting interval before the corrosion surveys of the 2000s shortened it?
- Where on the tower was the lead dust found in 2019, and how long was the campaign delayed?

## Reliability / Limitations

- `toureiffel.paris (maintenance page)`: the operator's own page, current.
- `construction-history.example`: peer-reviewed journal article, 2021.
- `paris-daily.example`: newspaper report, April 2019. It is the only source for the lead-free coats and the 2019 delay.
- `paintingcontractor-mag.example`: trade magazine feature, 2022.
- `sete-annual-report.example`: the operator's 2022 annual report. It is the operator describing its own work.
- `french-heritage-review.example`: heritage magazine article, 2020.
- `toureiffel.paris (colour page)`: the operator's own page, current.

## Sources

[^1]: https://www.toureiffel.paris/en/the-monument/maintenance
[^2]: https://www.construction-history.example/journal/2021/eiffel-paint-systems
[^3]: https://www.paris-daily.example/2019/04/eiffel-lead-paint
[^4]: https://www.paintingcontractor-mag.example/features/eiffel-rope-access
[^5]: https://www.sete-annual-report.example/2022/maintenance-cycle
[^6]: https://www.french-heritage-review.example/eiffel/upkeep
[^7]: https://www.toureiffel.paris/en/the-monument/colour
````

Final reply:

````
```json
{ "note": "Research/research-light-eiffel-tower-upkeep.md", "cut_short_topics": [] }
```
````

### W2: Coverage gap, research-writer agent

Case folder: `research-writer-02-coverage-gap`. Run folder: `writer-a1`.

#### Run 1

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-08'
PASS  fm-modified-run-date  found 'modified: 2026-10-08'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-footnotes-resolve   Every marker used in the body has a matching definition under Sources, each definition holds a URL, and each definition is used at least once.  - **[^1]** is used in the Summary ("…to a burner inside a glass lantern.[^1][^2]") and in "How the gas street lamps worked". It is defined as `https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets`. - **[^2]** is used in the Summa
PASS  judge-pay-in-open-questions   The Open Research Questions section asks what lamplighters were paid:  > ## Open Research Questions > > - What was a London lamplighter paid in the 1880s? Could the surviving vestry wage books at the London Metropolitan Archives answer this?[^5] > - Were rounds in other parishes, or rounds run by the gas companies, about the same size as the St Pancras rounds?  The note gives no wage figure anywh
PASS  judge-three-questions-answered   All three questions are answered, each with the required details.  **1. Fuel and how it reached the lamp.** Answered in full. Under "How the gas street lamps worked": "The lamps burned coal gas, made at the gasworks. The gas ran under the streets in cast-iron mains, then up through each lamp post to a burner inside the glass lantern." This covers coal gas, the gasworks, cast-iron mains under the 
PASS  keeps-70-lamps  found '70'
PASS  keeps-coal-gas  found 'coal gas'
PASS  keeps-dawn-round  found 'dawn'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-invented-wage  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## How the gas street lamp'
PASS  shape-topic-2-section  found '## The lamplighter'
PASS  file-name  expected name written
````

`project/Research/research-light-london-gas-lamps.md`:

````markdown
---
title: Light Research - London Gas Lamps
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08
modified: 2026-10-08
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Two topics: how London's gas street lamps worked, and the lamplighters who looked after them, including how many lamps one man tended and what he was paid. Limited to London, in the 1880s.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - London Gas Lamps

## Summary

London's street lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside a glass lantern.[^1][^2] A lamplighter lit the lamps with a long pole that had a hook at the top for turning the gas tap and a small oil-fed flame for lighting the burner. He made an evening round at dusk to light them and a second round at dawn to turn them off.[^1]

The gas companies and parish vestries divided each district into rounds. In St Pancras in 1884 a round covered about 70 lamps.[^3] Lamplighters worked for the gas companies or the parish vestries, not the police.[^2][^3] The sources found don't give their pay. Vestry wage books survive for some parishes, but they have not been put online.[^5]

## How the gas street lamps worked

**Fuel and supply.** The lamps burned coal gas, made at the gasworks. The gas ran under the streets in cast-iron mains, then up through each lamp post to a burner inside the glass lantern.[^1][^2]

**Lighting and putting out.** The lamplighter carried a long pole. At its top was a hook for turning the gas tap and a small oil-fed flame for lighting the burner. He lit his lamps on an evening round at dusk and turned them off on a second round at dawn.[^1]

## The lamplighters

**Who employed them.** Lamplighters were employed by the gas companies or by the parish vestries, not by the police.[^2][^3]

**How many lamps.** The gas companies and parish vestries divided each district into rounds. According to the St Pancras vestry's lighting committee minutes for 1884, a lamplighter's round covered about 70 lamps. He walked it twice a day, at dusk and at dawn.[^3]

**Pay.** The London Metropolitan Archives' research guide says vestry wage books survive for some parishes but have not been put online.[^5]

## Disagreement / Uncertainty

- **The figure of about 70 lamps per round comes from one parish.** It is from the St Pancras vestry minutes of 1884, and those minutes cover only that parish.[^3] Whether rounds in other parishes, or rounds run by the gas companies, were a similar size is not established.

## Useful Details

- **Other duties.** Besides lighting the lamps and putting them out, lamplighters cleaned the lamp glass once a week and reported broken lamps to the vestry.[^2][^3]
- **Hours.** The evening round began about half an hour before sunset, so in winter a lamplighter started work in mid-afternoon. The dawn round began before first light.[^4]

## Open Research Questions

- What was a London lamplighter paid in the 1880s? Could the surviving vestry wage books at the London Metropolitan Archives answer this?[^5]
- Were rounds in other parishes, or rounds run by the gas companies, about the same size as the St Pancras rounds?

## Reliability / Limitations

- `londonmuseum.example`, "Gas lighting in Victorian streets": museum collection article, 2018.
- `gas-history-society.example`, "Metropolitan mains": society research paper, 2011.
- `vestry-minutes.example`, St Pancras lighting committee, 1884: digitized parish vestry minutes. They cover one parish only.
- `london-streets-history.example`, "Lamplighter": local history society page, 2015.
- `lma-guide.example`, "Vestry wage books": archive research guide, 2021.

## Sources

[^1]: https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets
[^2]: https://www.gas-history-society.example/papers/metropolitan-mains
[^3]: https://www.vestry-minutes.example/st-pancras/1884/lighting-committee
[^4]: https://www.london-streets-history.example/trades/lamplighter
[^5]: https://www.lma-guide.example/sources/vestry-wage-books
````

Final reply:

````
```json
{ "note": "Research/research-light-london-gas-lamps.md", "cut_short_topics": [] }
```
````

#### Run 2

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-08'
PASS  fm-modified-run-date  found 'modified: 2026-10-08'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-footnotes-resolve   Markers used in the body: [^1], [^2], [^3], [^4], [^5].  - [^1] appears in "…to a burner inside a glass lantern.[^1][^2]". Its definition is "[^1]: https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets". - [^2] appears in "…not the police.[^2][^3]". Its definition is "[^2]: https://www.gas-history-society.example/papers/metropolitan-mains". - [^3] appears in "…a round cov
PASS  judge-pay-in-open-questions   The Open Research Questions section asks the pay question directly:  > ## Open Research Questions > > - What was a London lamplighter paid in the 1880s? Vestry wage books held at the London Metropolitan Archives may give the figure.[^5] > - Did the size of a round differ between parishes, or between rounds run by the gas companies and those run by the vestries?  The note gives no wage figure anyw
PASS  judge-three-questions-answered   1. **Fuel and delivery.** Answered with the required details. "The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern."  2. **Lighting and putting out.** Answered with the required details. "The lamplighter carried a long pole. It had a hook at the top for turning the gas tap and a small o
PASS  keeps-70-lamps  found '70'
PASS  keeps-coal-gas  found 'coal gas'
PASS  keeps-dawn-round  found 'dawn'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-invented-wage  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## How the gas street lamp'
PASS  shape-topic-2-section  found '## The lamplighter'
PASS  file-name  expected name written
````

`project/Research/research-light-london-gas-lamps.md`:

````markdown
---
title: Light Research - London Gas Lamps
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08
modified: 2026-10-08
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Two topics: how London's gas street lamps worked, and the lamplighters who looked after them (how many lamps one man tended, and what he was paid). Limited to London only, in the 1880s.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - London Gas Lamps

## Summary

London's gas street lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside a glass lantern.[^1][^2] A lamplighter lit them with a long pole that had a hook for turning the gas tap and a small oil-fed flame for lighting the burner. He made an evening round at dusk to light them and a second round at dawn to put them out.[^1]

Lamplighters worked for the gas companies or the parish vestries, not the police.[^2][^3] The companies and vestries divided each district into rounds. In the 1884 minutes of one parish, St Pancras, a round covered about 70 lamps.[^3] The findings give no wage figure. Vestry wage books survive for some parishes but have not been put online.[^5]

## How the gas street lamps worked

**Fuel and supply.** The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern.[^1][^2]

**Lighting and putting out.** The lamplighter carried a long pole. It had a hook at the top for turning the gas tap and a small oil-fed flame for lighting the burner.[^1] He lit his lamps on an evening round at dusk and turned them off on a second round at dawn.[^1] The evening round began about half an hour before sunset, so in winter a lamplighter started work in mid-afternoon. The dawn round began before first light.[^4]

## The lamplighters

**Employer.** Lamplighters were employed by the gas companies or by the parish vestries, not by the police.[^2][^3]

**Lamps per man.** The gas companies and parish vestries divided each district into rounds. A lamplighter's round covered about 70 lamps, and he walked it twice a day, at dusk and at dawn.[^3] This figure comes from the 1884 lighting committee minutes of one parish, St Pancras.[^3]

**Duties beyond lighting.** Besides lighting the lamps and putting them out, lamplighters cleaned the lamp glass once a week and reported broken lamps to the vestry.[^2][^3]

**Pay.** A guide to the London Metropolitan Archives says vestry wage books survive for some parishes but have not been put online.[^5]

## Disagreement / Uncertainty

The figure of about 70 lamps per round comes from the minutes of a single parish, St Pancras, in 1884.[^3] The findings don't show whether rounds elsewhere in London were the same size.

## Useful Details

- In winter, because the evening round began about half an hour before sunset, a lamplighter's working day started in mid-afternoon.[^4]
- Lamplighters reported broken lamps to the vestry.[^2][^3]

## Open Research Questions

- What was a London lamplighter paid in the 1880s? Vestry wage books held at the London Metropolitan Archives may give the figure.[^5]
- Did the size of a round differ between parishes, or between rounds run by the gas companies and those run by the vestries?

## Reliability / Limitations

- `London Museum, "Gas lighting in Victorian streets"`: museum collection article, 2018.
- `Gas History Society, "Metropolitan mains"`: society research paper, 2011.
- `St Pancras vestry minutes, lighting committee, 1884`: digitized parish vestry minutes. They cover one parish only.
- `London streets history, "Lamplighter"`: local history society page, 2015.
- `London Metropolitan Archives guide, "Vestry wage books"`: archive research guide, 2021.

## Sources

[^1]: https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets
[^2]: https://www.gas-history-society.example/papers/metropolitan-mains
[^3]: https://www.vestry-minutes.example/st-pancras/1884/lighting-committee
[^4]: https://www.london-streets-history.example/trades/lamplighter
[^5]: https://www.lma-guide.example/sources/vestry-wage-books
````

Final reply:

````
```json
{ "note": "Research/research-light-london-gas-lamps.md", "cut_short_topics": [] }
```

I couldn't open the example note at `/Users/mabbs/.claude/plugins/local/script-asst/references/research-light-example.md` because permission to read it wasn't granted. I set the note's layout from the template copy alone. Neither findings file was cut short. The findings give no 1880s wage for lamplighters, so that question is listed under Open Research Questions.
````

#### Run 3

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-08'
PASS  fm-modified-run-date  found 'modified: 2026-10-08'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-footnotes-resolve   Every marker used in the body has a matching definition under Sources, and each definition holds a URL:  - `[^1]` is used, for example in "...to a burner inside the glass lantern.[^1][^2]". It is defined as `[^1]: https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets`. - `[^2]` is used, for example in "...reported broken lamps to the vestry.[^2][^3]". It is defined as `[^
PASS  judge-pay-in-open-questions   The Open Research Questions section asks about lamplighters' pay:  > ## Open Research Questions > > - What was a London lamplighter paid in the 1880s? A London Metropolitan Archives guide says vestry wage books survive for some parishes but are not online.[^5] > - Did round sizes in other London parishes, or under the gas companies, match the St Pancras figure of about 70 lamps?  The note gives n
PASS  judge-three-questions-answered   1. **Fuel and supply.** The answer and its detail are both present: "The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains, then up through each lamp post to a burner inside the glass lantern."  2. **Lighting and putting out.** The answer and its detail are both present: "The lamplighter carried a long pole with a hook at the top, used to turn the gas ta
PASS  keeps-70-lamps  found '70'
PASS  keeps-coal-gas  found 'coal gas'
PASS  keeps-dawn-round  found 'dawn'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-invented-wage  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## How the gas street lamp'
PASS  shape-topic-2-section  found '## The lamplighter'
PASS  file-name  expected name written
````

`project/Research/research-light-london-gas-lamps.md`:

````markdown
---
title: Light Research - London Gas Lamps
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08
modified: 2026-10-08
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Topics: how London's gas street lamps worked (fuel, supply, lighting and putting out), and the lamplighters (how many lamps one man tended, and his pay). Limits: London only; the 1880s.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - London Gas Lamps

## Summary

London's street lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern.[^1][^2] A lamplighter turned the gas tap with a hooked pole and lit the burner with a small oil-fed flame. He lit his lamps on an evening round at dusk and put them out on a second round at dawn.[^1]

Lamplighters worked for the gas companies or the parish vestries, not the police. Besides lighting and putting out the lamps, they cleaned the lamp glass once a week and reported broken lamps to the vestry.[^2][^3] The 1884 minutes of one parish, St Pancras, put a round at about 70 lamps.[^3] The sources found give no wage figure for the 1880s.[^5]

## How the gas street lamps worked

**Fuel and supply.** The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains, then up through each lamp post to a burner inside the glass lantern.[^1][^2]

**Lighting and putting out.** The lamplighter carried a long pole with a hook at the top, used to turn the gas tap, and a small oil-fed flame for lighting the burner.[^1] He lit his lamps on an evening round at dusk and turned them off on a second round at dawn.[^1]

## The lamplighters

**Employers and duties.** Lamplighters were employed by the gas companies or by the parish vestries, not by the police. Besides lighting and putting out the lamps, they cleaned the lamp glass once a week and reported broken lamps to the vestry.[^2][^3]

**Lamps per man.** The gas companies and parish vestries divided each district into rounds. In the St Pancras vestry minutes of 1884, a lamplighter's round covered about 70 lamps, and he walked it twice a day, at dusk and at dawn.[^3]

**Hours.** The evening round began about half an hour before sunset, so in winter a lamplighter started work in mid-afternoon. The dawn round began before first light.[^4]

## Disagreement / Uncertainty

- **When the evening round began.** One source says the lamps were lit on an evening round at dusk.[^1] Another says the evening round began about half an hour before sunset.[^4]
- **How typical 70 lamps was.** The figure of about 70 lamps per round comes from the 1884 minutes of a single parish, St Pancras.[^3] The findings don't show whether rounds elsewhere in London were the same size.

## Useful Details

- Lamplighters' duties went beyond lighting: weekly cleaning of the lamp glass, and reporting broken lamps to the vestry.[^2][^3]
- In winter, the early evening round meant a lamplighter's working day began in mid-afternoon.[^4]
- Vestry wage books survive for some London parishes but have not been put online, according to a London Metropolitan Archives research guide.[^5]

## Open Research Questions

- What was a London lamplighter paid in the 1880s? A London Metropolitan Archives guide says vestry wage books survive for some parishes but are not online.[^5]
- Did round sizes in other London parishes, or under the gas companies, match the St Pancras figure of about 70 lamps?

## Reliability / Limitations

- `London Museum, "Gas lighting in Victorian streets"`: museum collection article, 2018.
- `Gas History Society, "Metropolitan mains"`: society research paper, 2011.
- `St Pancras vestry minutes, 1884, lighting committee`: digitized parish vestry minutes, 1884. The minutes cover one parish.
- `London streets history, "Lamplighter"`: local history society page, 2015.
- `London Metropolitan Archives guide, "Vestry wage books"`: archive research guide, 2021.

## Sources

[^1]: https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets
[^2]: https://www.gas-history-society.example/papers/metropolitan-mains
[^3]: https://www.vestry-minutes.example/st-pancras/1884/lighting-committee
[^4]: https://www.london-streets-history.example/trades/lamplighter
[^5]: https://www.lma-guide.example/sources/vestry-wage-books
````

Final reply:

````
```json
{ "note": "Research/research-light-london-gas-lamps.md", "cut_short_topics": [] }
```

I couldn't read the example note at `/Users/mabbs/.claude/plugins/local/script-asst/references/research-light-example.md` because the permission request wasn't granted. I wrote the note from the template copy and the rules alone. Neither findings file was cut short. The pay question (Q4) had no wage figure in the findings, so it's listed under Open Research Questions.
````

### W3: Source trail, research-writer agent

Case folder: `research-writer-03-source-trail`. Run folder: `writer-a1`.

#### Run 1

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-08'
PASS  fm-modified-run-date  found 'modified: 2026-10-08'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-claims-carry-right-source   **1. Slope:** The line "That is an average drop of about 25 centimetres per kilometre.[^1][^2]" carries [^1] and [^2]. The 12.6 m / 50 km figure in the Summary also carries [^1][^2]. - [^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient (allowed) - [^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul (allowed)  **2. Water commissioner / Frontinus / staff of abo
PASS  judge-footnotes-resolve   Every body marker has a definition with a URL: - `[^1]` and `[^2]` appear in "drops only about 12.6 metres over roughly 50 kilometres...[^1][^2]". They are defined as `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` and `[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul`. - `[^3]` and `[^4]` appear in "builders used inverted siphons...[^3][^4]". They ar
PASS  judge-tally-only-as-question   The tally marks and the channel keepers appear in exactly one place, under the **Open Research Questions** heading:  > "Is there a source for the tally marks that channel keepers at Nîmes are said to have cut into the channel wall?"  It is phrased as a question. "Are said to have" reports the claim without stating it as fact, so the entry asserts nothing.  I checked every other section: Summary, 
PASS  judge-urls-from-findings   All seven URLs in the Sources section match the allowed list exactly, character for character:  - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` - `[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul` - `[^3]: https://www.lyon-archaeology.example/aqueducts/siphons` - `[^4]: https://www.ancient-texts-library.example/frontinus/de-aquaeductu` - `[^5]: http
PASS  keeps-25-cm-gradient  found '25 centimetres'
PASS  keeps-40-cm-sinter  found '40 centimetres'
PASS  keeps-700-staff  found '700'
PASS  keeps-shared-url  found 'https://www.ancient-texts-library.example/frontinus/de-aquaeductu'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-unsourced-tally-detail  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## How the aqueducts were built'
PASS  shape-topic-2-section  found '## How the aqueducts were kept running'
PASS  file-name  expected name written
````

`project/Research/research-light-roman-aqueducts.md`:

````markdown
---
title: Light Research - Roman Aqueducts
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08
modified: 2026-10-08
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Two topics: how the Roman aqueducts were built, and how they were kept running. Limited to the city of Rome and Roman Gaul, up to the 3rd century AD.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Roman Aqueducts

## Summary

Roman aqueducts moved water using gravity alone, on very gentle slopes. The aqueduct that supplied Nîmes drops only about 12.6 metres over roughly 50 kilometres, and surveyors set that slope with levelling instruments before building began.[^1][^2] Arches carried the channel across valleys so the slope could stay steady. Where a valley was too deep for arches, as at Lyon, builders used inverted siphons: sealed lead pipes that took the water down one side and up the other.[^3][^4]

In Rome, the water commissioner (the curator aquarum) was responsible for the system. Frontinus held the post from 97 AD and describes a staff of about 700 slaves who repaired and cleaned the channels.[^4][^5] The main upkeep task was removing sinter, layers of calcium carbonate that hard water left inside the channels. Sinter narrowed the channel and had to be chipped out. At Nîmes it built up to about 40 centimetres thick in places.[^6][^7]

## How the aqueducts were built

### Keeping the water flowing downhill

The aqueduct that supplied Nîmes falls only about 12.6 metres over its whole length of about 50 kilometres. That is an average drop of about 25 centimetres per kilometre.[^1][^2]

Surveyors set this slope with levelling instruments along the whole route before building began.[^1][^2]

### Arches, and what replaced them in deep valleys

Arches carried the channel across valleys so the slope could stay steady.[^3][^4]

Where a valley was too deep for arches, as at Lyon, builders used inverted siphons. These were sealed lead pipes that ran down one side of the valley and up the other. The water's own pressure pushed it back up the far side.[^3][^4]

## How the aqueducts were kept running

### Who was responsible

In Rome, the water commissioner, called the curator aquarum, was responsible for the aqueducts.[^4][^5]

Frontinus held the post from 97 AD and wrote a treatise on the system.[^4][^5] He describes a staff of about 700 slaves who repaired and cleaned the channels. The staff was split into two gangs, one public and one imperial.[^4][^5]

### Upkeep of the channels

Hard water left layers of calcium carbonate, called sinter, inside the channels.[^6][^7] The layers narrowed the channel and had to be chipped out.[^6][^7]

In parts of the Nîmes aqueduct, the deposits reached about 40 centimetres thick.[^6][^7]

## Disagreement / Uncertainty


## Open Research Questions

- Is there a source for the tally marks that channel keepers at Nîmes are said to have cut into the channel wall?

## Reliability / Limitations

- `nimes-heritage.example`: Survey report by the Nîmes heritage service, 2012.
- `roman-engineering-journal.example`: Peer-reviewed article, 2015.
- `lyon-archaeology.example`: Page from the Lyon city archaeology service, 2016.
- `ancient-texts-library.example`: A translation of Frontinus's own treatise, written about 97 AD. It is a primary source from the official in charge of Rome's water supply.
- `roman-water-review.example`: Peer-reviewed article, 2019.
- `hydro-history.example`: Peer-reviewed article, 2020.
- `geoarchaeology-letters.example`: Peer-reviewed article, 2017.

## Sources

[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient
[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul
[^3]: https://www.lyon-archaeology.example/aqueducts/siphons
[^4]: https://www.ancient-texts-library.example/frontinus/de-aquaeductu
[^5]: https://www.roman-water-review.example/2019/curator-aquarum
[^6]: https://www.hydro-history.example/2020/sinter-deposits-nimes
[^7]: https://www.geoarchaeology-letters.example/2017/carbonate-layers
````

Final reply:

````
```json
{ "note": "Research/research-light-roman-aqueducts.md", "cut_short_topics": [] }
```
````

#### Run 2

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-08'
PASS  fm-modified-run-date  found 'modified: 2026-10-08'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-claims-carry-right-source   1. **Slope claim:** The body says "That is an average drop of about 25 centimetres per kilometre.[^1] [^2]" The Summary also says "drops only about 12.6 metres over about 50 kilometres... before building began.[^1]"    - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` is allowed.    - `[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul` is allowed.  2. 
PASS  judge-footnotes-resolve   **Markers in the body:** Every marker from [^1] to [^7] appears in the body at least once. - `[^1]` and `[^2]` appear together: "That is an average drop of about 25 centimetres per kilometre.[^1] [^2]" - `[^3]` and `[^4]` appear together: "Arches carried the channel across valleys so that the slope could stay steady.[^3] [^4]" - `[^4]` and `[^5]` appear together: "In Rome, the aqueducts were the 
PASS  judge-tally-only-as-question   The tally marks appear in one place only, under **Open Research Questions**, phrased as a question:  > ## Open Research Questions > - Is there a source for the tally marks said to have been cut into the channel wall at Nîmes after each cleaning?  The wording "said to have been cut" reports the claim without asserting it, which is close to the check's own example. The question form holds.  The gui
PASS  judge-urls-from-findings   Every URL in the note's Sources section matches an approved URL character for character:  - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` - `[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul` - `[^3]: https://www.lyon-archaeology.example/aqueducts/siphons` - `[^4]: https://www.ancient-texts-library.example/frontinus/de-aquaeductu` - `[^5]: https://ww
PASS  keeps-25-cm-gradient  found '25 centimetres'
PASS  keeps-40-cm-sinter  found '40 centimetres'
PASS  keeps-700-staff  found '700'
PASS  keeps-shared-url  found 'https://www.ancient-texts-library.example/frontinus/de-aquaeductu'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-unsourced-tally-detail  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## How the aqueducts were built'
PASS  shape-topic-2-section  found '## How the aqueducts were kept running'
PASS  file-name  expected name written
````

`project/Research/research-light-roman-aqueducts.md`:

````markdown
---
title: Light Research - Roman Aqueducts
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08
modified: 2026-10-08
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Topics: how the aqueducts were built, and how the aqueducts were kept running. Limited to the city of Rome and Roman Gaul, up to the 3rd century AD.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Roman Aqueducts

## Summary

Roman aqueducts moved water by gravity on a very gentle, carefully surveyed slope. The aqueduct that supplied Nîmes drops only about 12.6 metres over about 50 kilometres, and surveyors set that slope with levelling instruments before building began.[^1] Arches carried the channel across valleys so the slope could stay steady. Where a valley was too deep for arches, as at Lyon, builders used inverted siphons of sealed lead pipe instead.[^3]

In Rome, the water commissioner (the curator aquarum) was responsible for the system. Frontinus, who held the post from 97 AD, describes a staff of about 700 slaves who repaired and cleaned the channels.[^4] The channels needed sinter chipped out: the calcium carbonate that hard water left inside them, which narrowed the channel. At Nîmes it built up to about 40 centimetres thick in places.[^6]

## How the aqueducts were built

### Keeping the water flowing downhill

The aqueduct that supplied Nîmes is about 50 kilometres long and falls only about 12.6 metres over its whole length. That is an average drop of about 25 centimetres per kilometre.[^1] [^2]

That slope was set before construction. Surveyors used levelling instruments to fix the gradient over the whole route before building began.[^1] [^2]

### Arches, and what replaced them in deep valleys

Arches carried the channel across valleys so that the slope could stay steady.[^3] [^4]

Some valleys were too deep for arches. In those places, as at Lyon, builders used inverted siphons. These were sealed lead pipes that ran down one side of the valley and up the other. The water's own pressure pushed it back up the far side.[^3] [^4]

## How the aqueducts were kept running

### Who was responsible

In Rome, the aqueducts were the responsibility of the water commissioner, the curator aquarum.[^4] [^5]

Frontinus held this post from 97 AD and wrote a treatise on the water system.[^4] [^5]

Frontinus describes a staff of about 700 slaves who repaired and cleaned the channels. The staff was split into two gangs, one public and one imperial.[^4] [^5]

### What upkeep the channels needed

The water was hard and left layers of calcium carbonate, called sinter, on the inside of the channels.[^6] [^7]

These layers narrowed the channel and had to be chipped out.[^6] [^7]

In parts of the Nîmes aqueduct the sinter deposits reached about 40 centimetres thick.[^6] [^7]

## Disagreement / Uncertainty

## Open Research Questions

- Is there a source for the tally marks said to have been cut into the channel wall at Nîmes after each cleaning?

## Reliability / Limitations

- `https://www.nimes-heritage.example/aqueduct/survey-gradient`: heritage service survey report, 2012.
- `https://www.roman-engineering-journal.example/2015/gradients-in-gaul`: peer-reviewed article, 2015.
- `https://www.lyon-archaeology.example/aqueducts/siphons`: city archaeology service page, 2016.
- `https://www.ancient-texts-library.example/frontinus/de-aquaeductu`: translation of Frontinus, written about 97 AD. An ancient primary source, by the man who held the post of water commissioner.
- `https://www.roman-water-review.example/2019/curator-aquarum`: peer-reviewed article, 2019.
- `https://www.hydro-history.example/2020/sinter-deposits-nimes`: peer-reviewed article, 2020.
- `https://www.geoarchaeology-letters.example/2017/carbonate-layers`: peer-reviewed article, 2017.

## Sources

[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient
[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul
[^3]: https://www.lyon-archaeology.example/aqueducts/siphons
[^4]: https://www.ancient-texts-library.example/frontinus/de-aquaeductu
[^5]: https://www.roman-water-review.example/2019/curator-aquarum
[^6]: https://www.hydro-history.example/2020/sinter-deposits-nimes
[^7]: https://www.geoarchaeology-letters.example/2017/carbonate-layers
````

Final reply:

````
```json
{ "note": "Research/research-light-roman-aqueducts.md", "cut_short_topics": [] }
```
````

#### Run 3

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-08'
PASS  fm-modified-run-date  found 'modified: 2026-10-08'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-claims-carry-right-source   **Claim 1: Slope.** The note says: "falls only about 12.6 metres over its whole length of about 50 kilometres, an average of about 25 centimetres per kilometre. [^1] [^2]" - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` is allowed. - `[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul` is allowed.  **Claim 2: Commissioner, Frontinus, staff of 700.** T
PASS  judge-footnotes-resolve   **Markers in the body:** `[^1]` through `[^7]` all appear. For example: - "[^1] [^2]" follows the Nîmes gradient claims. - "[^3] [^4]" follows the arches and siphons claims. - "[^4] [^5]" follows the curator aquarum and Frontinus claims. - "[^6] [^7]" follows the sinter claims.  **Definitions under Sources:** each one has a URL. - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient
PASS  judge-tally-only-as-question   The tally marks appear in exactly one place, and that place is allowed:  - **Open Research Questions:** "Is there a source for the tally marks said to have been cut into the channel walls at Nîmes after each cleaning?"  This entry is phrased as a question. The words "said to have been" mark the claim as reported, not as fact, so the entry asserts nothing.  The guild of channel keepers does not ap
PASS  judge-urls-from-findings   All seven URLs in the Sources section match the allowed list character for character:  - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` is on the list. - `[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul` is on the list. - `[^3]: https://www.lyon-archaeology.example/aqueducts/siphons` is on the list. - `[^4]: https://www.ancient-texts-library.example
PASS  keeps-25-cm-gradient  found '25 centimetres'
PASS  keeps-40-cm-sinter  found '40 centimetres'
PASS  keeps-700-staff  found '700'
PASS  keeps-shared-url  found 'https://www.ancient-texts-library.example/frontinus/de-aquaeductu'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-unsourced-tally-detail  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## How the aqueducts were built'
PASS  shape-topic-2-section  found '## How the aqueducts were kept running'
PASS  file-name  expected name written
````

`project/Research/research-light-roman-aqueducts.md`:

````markdown
---
title: Light Research - Roman Aqueducts
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08
modified: 2026-10-08
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Topics: (1) how the aqueducts were built; (2) how the aqueducts were kept running. Limits: the city of Rome and Roman Gaul only, up to the 3rd century AD.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Roman Aqueducts

## Summary

Roman aqueducts moved water by gravity on very gentle, carefully surveyed slopes. The aqueduct supplying Nîmes drops only about 12.6 metres over about 50 kilometres, and surveyors set that slope with levelling instruments before building began. [^1] [^2] Arches carried the channel across valleys so the slope could stay steady. Where a valley was too deep for arches, as at Lyon, builders used inverted siphons: sealed lead pipes that ran down one side of the valley and up the other. [^3] [^4]

In Rome, a water commissioner, the curator aquarum, was responsible for the aqueducts. Frontinus, who held the post from 97 AD, describes a staff of about 700 slaves who repaired and cleaned the channels. [^4] [^5] A main upkeep task was removing sinter, layers of calcium carbonate left by hard water. Sinter narrowed the channels and had to be chipped out, and in parts of the Nîmes aqueduct it reached about 40 centimetres thick. [^6] [^7]

## How the aqueducts were built

### Keeping the water flowing downhill

The aqueduct that supplied Nîmes falls only about 12.6 metres over its whole length of about 50 kilometres, an average of about 25 centimetres per kilometre. [^1] [^2]

Surveyors set this slope with levelling instruments over the whole route before building began. [^1] [^2]

### Arches and siphons

Arches carried the channel across valleys so the slope could stay steady. [^3] [^4]

Where a valley was too deep for arches, as at Lyon, builders used inverted siphons. These were sealed lead pipes that ran down one side of the valley and up the other, and the water's own pressure pushed it up the far side. [^3] [^4]

## How the aqueducts were kept running

### Who was responsible

In Rome, the water commissioner, the curator aquarum, was responsible for the aqueducts. [^4] [^5]

Frontinus held the post from 97 AD and wrote a treatise on the system. [^4] [^5]

He describes a staff of about 700 slaves who repaired and cleaned the channels. The staff was split between a public gang and an imperial gang. [^4] [^5]

### Upkeep of the channels

Hard water left layers of calcium carbonate, called sinter, inside the channels. [^6] [^7]

The layers narrowed the channel and had to be chipped out. [^6] [^7]

In parts of the Nîmes aqueduct the deposits reached about 40 centimetres thick. [^6] [^7]

## Disagreement / Uncertainty

## Open Research Questions

- Is there a source for the tally marks said to have been cut into the channel walls at Nîmes after each cleaning?

## Reliability / Limitations

- `nimes-heritage.example`: heritage service survey report, 2012.
- `roman-engineering-journal.example`: peer-reviewed article, 2015.
- `lyon-archaeology.example`: city archaeology service page, 2016.
- `ancient-texts-library.example`: translation of Frontinus's treatise, written about 97 AD. A primary account by the official who held the post.
- `roman-water-review.example`: peer-reviewed article, 2019.
- `hydro-history.example`: peer-reviewed article, 2020.
- `geoarchaeology-letters.example`: peer-reviewed article, 2017.

## Sources

[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient
[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul
[^3]: https://www.lyon-archaeology.example/aqueducts/siphons
[^4]: https://www.ancient-texts-library.example/frontinus/de-aquaeductu
[^5]: https://www.roman-water-review.example/2019/curator-aquarum
[^6]: https://www.hydro-history.example/2020/sinter-deposits-nimes
[^7]: https://www.geoarchaeology-letters.example/2017/carbonate-layers
````

Final reply:

````
```json
{ "note": "Research/research-light-roman-aqueducts.md", "cut_short_topics": [] }
```
````

### W6: Eight topics, research-writer agent

Case folder: `research-writer-06-eight-topics`. Run folder: `writer-a1`.

#### Run 1

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-09'
PASS  fm-modified-run-date  found 'modified: 2026-10-09'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-footnotes-resolve   Every marker in the body has a matching definition with a URL, and every definition is used at least once.  - **Definitions:** The Sources section defines `[^1]` through `[^92]` with no gaps. Each holds a URL. For example, `[^1]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview` and `[^92]: https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882`. - **No u
PASS  judge-planted-details-cite-own-url   All eight details appear in the note, and each carries a footnote whose URL under Sources matches the one given.  1. **Topic 1, 22-inch blocks.** The body says "laid out so the blocks came out 22 inches square on the surface. ... The remaining third held the field together so men and horses could still walk on it.[^9]". The Summary says "The grid was laid out so blocks came out 22 inches square o
PASS  judge-reply-no-cut-short   The reply names no topic or file as cut short. The structured output says so directly: `"cut_short_topics": []`. The only file it says it couldn't use is the example note. It says it "couldn't read the example note because I didn't have permission to open that file." That file is not one of the findings files, and the reply doesn't call it truncated or say it was missing its closing line. Nothing
PASS  judge-sixteen-questions-answered   All sixteen questions get the findings' answer, and none is listed as open when the findings answer it.  1. **Cutting time and thickness.** "usually from mid-January into February, once a long hard freeze had set in"; "Ice was not cut until it was at least 14 inches thick"; "Each morning a foreman walked the pond with a hand auger, boring test holes… only clear ice counted." 2. **Tools and block 
PASS  keeps-t1-14-inches  found '14 inch'
PASS  keeps-t1-22-inch-blocks  found '22 inch'
PASS  keeps-t2-17-percent-loss  found '17 percent'
PASS  keeps-t2-9400-tons  found '9,400'
PASS  keeps-t3-pumped-every-4-hours  found 'four hours'
PASS  keeps-t3-sawdust-1-to-11  found '11 tons'
PASS  keeps-t4-130-days  found '130 days'
PASS  keeps-t4-38-percent-loss  found '38 percent'
PASS  keeps-t5-1250-tons  found '1,250'
PASS  keeps-t5-barcia  found 'Barcia'
PASS  keeps-t6-75-men  found '75'
PASS  keeps-t6-nine-drownings  found 'nine harvest-crew drown'
PASS  keeps-t7-2-half-cents  found '2½'
PASS  keeps-t7-3-annas  found '3 annas'
PASS  keeps-t8-12-tons-a-day  found '12 tons'
PASS  keeps-t8-margaret-ellery  found 'Margaret Ellery'
PASS  keeps-url-topic-1  found 'https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s'
PASS  keeps-url-topic-2  found 'https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage'
PASS  keeps-url-topic-3  found 'https://www.maritime-salem.example/papers/stowing-ice-1850'
PASS  keeps-url-topic-4  found 'https://www.ice-trade-voyages.example/logs/calcutta-melt-study'
PASS  keeps-url-topic-5  found 'https://www.havana-archive.example/colonial-trade/ice-depot-1840s'
PASS  keeps-url-topic-6  found 'https://www.labor-history-ne.example/winter-work/harvest-crew-sizes'
PASS  keeps-url-topic-7  found 'https://www.gulf-commerce.example/price-current/ice-1860'
PASS  keeps-url-topic-8  found 'https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## Cut'
PASS  shape-topic-2-section  found '## Stor'
PASS  shape-topic-3-section  found '## Load'
PASS  shape-topic-4-section  found '## The voyage'
PASS  shape-topic-5-section  found '## Ice houses at the far port'
PASS  shape-topic-6-section  found '## The worker'
PASS  shape-topic-7-section  found '## Buyers and price'
PASS  shape-topic-8-section  found '## The end'
PASS  file-name  expected name written
````

`project/Research/research-light-ice-trade.md`:

````markdown
---
title: Light Research - Ice Trade
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-09
modified: 2026-10-09
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> How the New England ice trade by sea worked, from the trade's start to its end, across eight topics: cutting the ice on the ponds; storing the ice before shipping; loading the ship; the voyage; ice houses at the far ports; the workers; buyers and prices; and the end of the trade. Boundary: New England ice shipped by sea, from the trade's start to its end.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Ice Trade

## Summary

The trade began with a failed cargo from Boston to Martinique in 1806, sent by Frederic Tudor, which mostly melted on the wharf because the island had no ice house.[^38] By the 1820s Tudor was shipping regularly to Havana and the southern United States, building an ice house before the first cargo arrived.[^38]

Ice was harvested in the coldest weeks, usually mid-January into February,[^1] and was not cut until the clear ice was at least 14 inches thick.[^1] Horse-drawn tools, first designed by Nathaniel Jarvis Wyeth in 1825 and patented in improved form in 1829, cut blocks of one regular size that stacked tightly.[^7] The grid was laid out so blocks came out 22 inches square on the surface.[^9] The ice was stored in large above-ground, double-walled icehouses packed with sawdust on the pond shores;[^17][^19] the biggest on Fresh Pond held about 9,400 tons.[^17] One surviving 1847 ledger records a loss of about 17 percent over a season in storage.[^23]

Ice travelled outward in ordinary merchant ships that would otherwise have left Boston in ballast, which made carriage cheap.[^29] Holds were lined with an inner plank wall packed with sawdust,[^32] loaded at one ton of sawdust to every 11 tons of ice,[^34] sealed, and pumped every four hours for the whole voyage.[^36] Voyages ran from two to three weeks to the Caribbean[^42] to about 130 days to Calcutta,[^41] where a study of surviving papers found an average loss of 38 percent.[^47] Short routes often lost under a tenth.[^30]

At the far ports the ice went into purpose-built houses, such as the round brick Calcutta house holding about 1,250 tons,[^50] and was sold by weight in the early morning.[^60][^44] Calcutta's price in the 1830s and 1840s was 3 annas a pound;[^60] New Orleans' price had fallen to about 2½ cents a pound by 1860.[^76] Harvest work was done first by local farmers, then increasingly by Irish and later French-Canadian labourers, in crews of about 75 men on the largest ponds.[^63][^64][^66][^67]

The trade peaked around 1860 and was nearly over by the 1880s, ended by a combination of the Civil War, ice-making machines, steamships, and the growing home market for natural ice.[^30][^78] The last recorded cargo to Calcutta sailed in 1882 aboard the bark *Margaret Ellery*.[^92]

## Cutting the ice on the ponds

**When the ice was cut.** The harvest ran in the coldest weeks of the year, usually from mid-January into February, once a long hard freeze had set in.[^1] Firms preferred spring-fed ponds with no inflowing streams, because moving water froze unevenly and carried silt, leaves, and mill sawdust into the ice.[^1][^2] Fresh Pond in Cambridge, Wenham Lake north of Salem, and Spy Pond in Arlington were the best known, and firms bought or leased the shore rights to keep rivals out.[^1][^2] A pond owner could earn more from one winter's ice rights than from a year of farming the land around it.[^2] Foremen kept daily notebooks recording dawn and noon air temperature, wind, and snowfall.[^1]

**Thickness.** Ice was not cut until it was at least 14 inches thick. Thinner ice crumbled at the corners, wasted hold space, and melted faster because a thin block has more surface for its weight.[^1][^3] Each morning a foreman walked the pond with a hand auger, boring test holes at set points and measuring the clear ice separately from any white snow ice on top; only clear ice counted.[^1][^3] If readings fell short, the crew cleared snow or stood idle. Some firms paid a bonus to the foreman whose pond reached cutting thickness first.[^3] Cutting often began near the shaded shore and moved outward as the ice thickened.[^1]

**Snow.** Snow insulated the pond and slowed freezing, and wet snow that froze on top became weak, air-filled "snow ice."[^4][^5] Crews cleared snow with horse-drawn scrapers, wide wooden boards dragged across the surface.[^4] On some ponds they bored holes and flooded the cleared surface so a fresh layer froze on top; this worked only in hard cold, since slow-freezing layers turned cloudy.[^4][^5] Snow ice was planed off before storage.[^4] Mid-harvest snowfall could stop all work for several days.[^5]

**Clarity testing.** Before the harvest a small block was cut, carried ashore, and held up to the light; a block through which a dark object showed clearly through its whole thickness was judged good enough to ship. If cloudy, the cutting moved to another part of the pond, often further from the inlet or shore. The test was repeated every few days.[^6][^3]

**Tools before and after Wyeth.** Before the 1820s ice was cut by hand with axes, hand saws, and chisels, producing uneven blocks that stacked poorly and let in warm air.[^7] Nathaniel Jarvis Wyeth, a Cambridge hotel manager who later worked for the Tudor ice company, designed a horse-drawn cutter in 1825 and patented an improved version in 1829.[^7][^8] Historians describe the shift to horse tools as the change that made long voyages possible, because regular blocks lost less to melting. By the 1840s most commercial ponds in Massachusetts used some version of his tools.[^7]

**The marker and plough.** The "marker" looked like a plough with a row of steel teeth on a frame, drawn by one horse along a line laid out with a cord. Each pass scored a shallow groove; a guide arm kept the next groove parallel. The field was then scored at a right angle to make a grid, laid out so the blocks came out 22 inches square on the surface. The second tool, the "plough," had longer teeth and was run along the same grooves until each cut went about two-thirds of the way through. The remaining third held the field together so men and horses could still walk on it.[^9] The tools were designed so the horse walked on uncut ice beside the line, not on the grooves.[^6][^5]

**Horses.** Horses pulled the scrapers and cutting tools, shod with sharp-calked shoes, horseshoes with spikes that gripped the ice; a blacksmith was kept near the larger ponds to reset worn shoes.[^6][^5] A horse breaking through was the most common accident of the harvest. Crews looped a rope around the horse's neck and pulled it tight, which made the animal hold its breath and float higher, so the men could drag it out. Accounts describe horses going through two or three times in a season and continuing to work.[^6][^5]

**Breaking out and floating.** A channel to shore was sawn out with long hand saws. Men with iron "breaking bars," flat chisels on long handles, split the field along the grooves into long rafts and then single blocks; a skilled bar man could tell by the sound of the strike whether a groove was deep enough. Men with pike poles, long wooden poles with an iron hook and spike, moved the floating blocks along the channel. In very hard cold the channel had to be kept open by breaking the thin new ice that formed overnight.[^10][^6]

**Into the icehouse.** At shore, an inclined elevator, a long wooden ramp with an endless cleated chain, carried each block up to the door where men were stacking. It was first driven by a horse at a capstan; from the 1850s the largest houses used small steam engines. A man at the foot fed blocks on one at a time, since a block slipping back could break a man's leg. Each block's top and bottom were planed flat first. The elevator could run day and night with lanterns along the ramp.[^1][^11]

**Grading.** The clearest blocks, with no bubbles, snow ice, or dirt, were first quality and set aside for shipping. Blocks with a cloudy band or trapped leaves were second quality and usually sold locally to households and butchers in Boston and nearby towns. Broken corners and chips were left on the ice.[^3][^12] Grading was by eye; one firm's papers tell foremen to reject any block they would not want to see on a dinner table.[^3] Agents abroad wrote back about each cargo's quality, and a firm whose cargo arrived cloudy could lose a buyer for a season.[^3][^12]

**Counting.** The harvest was counted, not weighed. A tally man at the top of the elevator marked each block on a board, and the daily total was converted to tons using a fixed weight for a standard block, roughly 200 pounds for a first-quality block of regular size. The tally was used to plan sailings and to pay pond owners, usually paid by the ton; owners sometimes sent their own man to keep a second tally, and disputes are recorded in letters.[^15]

**Weather.** A thaw or rain mid-season softened the ice and flooded the grooves, which refroze unevenly, often forcing the field to be planed and recut. A mild "open winter" left ponds too thin to cut, and shippers then bought ice from ponds in Maine and New Hampshire at higher cost. A large pond could be cleared in two to three weeks in a good season. Newspaper reports describe crews cutting on Sundays, against local custom, when a thaw was forecast. Several firms kept icehouses on two or more ponds as insurance against a bad pond.[^13][^14]

**Tool sets.** By the 1850s tools were sold as complete sets by specialist makers, many in the Hudson valley of New York. A set for a large pond included one or two markers, several ploughs, hand saws up to six feet long, breaking bars, pike poles, ice tongs, and snow scrapers. Makers' catalogues, with engravings and instructions, are now a main source for how the work was done. The tools changed little over the trade's life; a set bought in the 1850s could still be in use thirty years later with new teeth fitted.[^16][^7]

## Storing the ice before shipping

**Location and form.** Because the harvest came in a few winter weeks but ships sailed all year, ice was stored for months. The firms built icehouses on the pond shore so blocks went straight from the channel up the elevator. The houses stood above ground, a change from older farm pits dug into hillsides, which held only a few tons, let in groundwater, and absorbed heat from warm summer soil.[^17][^18] Houses near the rail lines to the Boston wharves could get ice to a ship within a day of an order.[^17][^18]

**Walls and fill.** Each house had two wooden walls set a little apart, with the space packed with insulating fill, usually sawdust from timber mills, sometimes spent tanbark from tanneries; some houses had three walls and two fill layers. Tudor and Wyeth tested fills in the 1820s and 1830s by building small trial houses and weighing the ice at the start and end of summer, over several summers. They found dry fill kept ice far better than damp fill, so houses had wide eaves to keep rain off the outer wall.[^19][^7]

**Size.** The biggest icehouse on Fresh Pond held about 9,400 tons when full and was taller than a three-storey building. It was a row of rooms under one long roof, each filled and emptied separately so opening one did not warm the rest. Engravings show a long windowless block with doors stacked one above another on the elevator side; doors at each height were opened as the ice rose inside and boarded shut once the stack passed them. Smaller firms built houses holding a few hundred tons and sold mostly locally.[^17][^20]

**Roof.** Roofs were steep, with louvred vents along the ridge so warm air could escape. Most houses were painted white or a light colour to reflect the sun, and some had hay or straw in the roof space.[^21][^18]

**Drainage.** Water was more dangerous to stored ice than warm air, because ice standing in melt melted much faster. Floors were built over gravel or broken stone with a drain to the pond, covered with a thick layer of sawdust for the blocks to sit on. A blocked drain could cost much of the bottom layers in a single warm month. One firm's papers record dismissing a keeper who let a drain freeze in early spring, flooding the lowest room when the weather turned.[^19]

**Stacking and unloading.** Blocks were set on edge, tight together, each layer laid across the one below like brickwork, with gaps filled by ice chips; air in the gaps was the main source of melting inside the stack. A full room was topped with a deep layer of hay or sawdust. Stackers worked at freezing temperatures and counted among the most skilled men, since a bad stack could lean and fall as lower blocks melted.[^17][^6] For shipping, ice was removed from the top down; men cleared the covering and broke apart blocks that had frozen together, then sent them down a chute to rail wagons. Only one room was opened at a time and shut the same day; the keeper used the oldest ice first and saved the best-packed rooms for the hottest months. Blocks were scraped of fill before loading.[^3][^12]

**Keepers.** Each large house had a keeper living beside it year-round, often in a cottage against the end wall, who checked drains and vents, watched for fire, kept the ledger of ice in and out, directed stacking, and chose which room to open for each order. Firms hired keepers who could read, write, and keep figures. Their surviving letters to the Boston office, about weekly through the summer, are mostly short reports on weather, the stack, and repairs.[^22] From the 1850s some keepers recorded thermometer readings above the stack morning and evening beside the outside temperature; a rising inside reading meant a door left open or a clogged vent.[^22]

**Loss in storage.** The ledgers of one Fresh Pond icehouse for 1847 show a loss of about 17 percent between the end of the harvest in March and the last autumn sailing, mostly in July and August. The keeper blamed the heat and a roof vent left shut, and noted that a room left unopened until autumn lost less than one opened for loading in June. Historians treat this ledger, the only surviving whole-season record for a single house, as the standard figure.[^23] Large houses lost less than small ones because a big stack has less surface for its weight, which is the main reason firms built ever-larger houses through the 1840s and 1850s.[^28][^18] (For other figures and the problem of comparing them, see Disagreement / Uncertainty.)

**Getting to the harbour.** From the early 1840s a branch railway ran from Fresh Pond to the Charlestown wharves on Boston harbour, cutting a wagon journey that could cost noticeable ice on a hot day to under an hour. The ice wagons had thick sawdust-packed sides, and trains ran at night in summer. The ice firms were among the railway's largest customers in the 1840s.[^24][^17] Firms also kept smaller wharf icehouses holding a few hundred tons each, built on the same double-walled plan, where ice was held a few days before a sailing. Ice was not kept there long, as the harbour air was warmer and damper and the houses stood on piers over the water.[^25]

## Loading the ship

**The ships.** Ice went in ordinary merchant ships. Boston imported much from the tropics but had little to send out, so many ships left in ballast; ice gave them a paying outward cargo, and owners charged low rates, one reason the trade could pay. Older ships were often chosen because the firms' carpenters altered the holds.[^29][^30]

**Preparing the hold.** Holds were emptied, swept, and dried, and a hold that had carried fish, hides, or molasses was scrubbed and aired for days, since any smell could pass into the ice. One agent wrote that a cargo tasting of fish was sold at a loss to a butcher. Firms kept a list of ships they would not charter, and avoided ships that had carried coal, whose dust came out black on the ice.[^31]

**The lining.** A carpenter built an inner wall of pine planks set in from the hull on all sides, across the floor, and up under the deck beams, with sawdust packed between: a box inside the hull built like the icehouses on shore. Sailors called it the "ice ceiling." A carpenter and two helpers took about a week for a ship of middling size.[^32][^29] The floor came first: rough timber dunnage to lift the cargo clear of bilge water, then the lining floor, then a deep sawdust bed, with gaps at the sides so melt ran to the bilge for the pumps. A badly built floor left the bottom layer standing in water, and loss from the bottom layer was the largest single loss on most recorded voyages.[^32]

**Sawdust.** Sawdust filled gaps, held blocks still, and slowed warming. Firms bought pine sawdust from Maine mills, where it was waste, and shipped it to Boston by schooner.[^34] An 1850 paper by a Salem merchant gives the ratio of one ton of sawdust to every 11 tons of ice: less saved weight but cost more ice; more took space that could carry ice.[^34] Sawdust had to be dry, since wet sawdust froze onto the blocks in a crust that conducted heat inward. It was stored in covered wharf sheds and turned in fine weather to dry, and damp loads were spread in the sun.[^33][^29]

**Stowing.** Stevedores lowered blocks through the hatch in slings and set them by hand on edge, tight together, each layer across the one below, pushing chips and sawdust into every gap; a stack with air spaces melted from the inside out. Firms used the same experienced gangs when they could. The mate watched the stow and signed for the cargo.[^35][^29] Ships usually carried less ice than their rated tonnage, because of the weight and space of lining and sawdust. Ice was stowed low and spread evenly from bow to stern for stability.[^32][^36]

**Sealing.** The full stack was covered with sawdust and then hay. Hatches were closed, covered with tarred canvas, and battened down with bars nailed across; some ships added an inner hatch cover with sawdust between. The master signed a note of the time of sealing, sent back to the firm by the first mail.[^32][^36] The hatches stayed sealed until port, even in calm weather; some masters sealed the joins with wax or pitch so tampering would show, and the firms' instructions say a master who opened them without good cause would answer for the lost ice.[^37]

**Against shifting.** A shifted cargo could break the lining. Stevedores drove timber battens between stack and lining at intervals and wedged the top layers against the deck beams; a tight, well-packed stow also held the blocks still. Logbooks record voyages where heavy weather loosened the stack, each arriving with a much smaller cargo; one master wrote that he heard the ice "working" in the hold during a gale and could do nothing.[^36]

**Pumping.** The crew pumped the bilge every four hours, day and night, for the whole voyage, and the mate logged the strokes needed to clear it. The stroke count was a rough measure of melting: a sudden rise meant a shifted stow or broken lining, and missed pumpings let water rise into the bottom ice. Strokes rose steadily as ships entered warmer waters.[^36] With the hatches sealed, the pumping log was the only sign of how the cargo was faring.[^37]

**Speed of loading.** Stevedores worked through the night or early morning; a middling ship could be loaded in one to two days, with ice arrivals at the wharf timed to the hour. The ship sailed on the next tide if the wind allowed, and masters who waited for return cargo before sailing were told to stop.[^35][^37]

**Cargo size.** Cargoes grew through the 1840s as larger ships were chartered and loading crews grew more skilled. Size was limited less by the ship than by how much the far port could sell; firms planned sailings port by port from what each agent said he could sell.[^30][^31]

## The voyage

**Routes.** The longest regular route ran from Boston to Calcutta: south through the Atlantic, across the equator, round the Cape of Good Hope, and north across the Indian Ocean, crossing the equator again before the Hooghly River. It took about 130 days.[^41][^36] The Caribbean routes, to Havana, Martinique, Jamaica, and other islands, took two to three weeks with fair winds; Havana became one of the steadiest markets, with ships every few weeks.[^42][^43] The southern U.S. ports, Charleston, Savannah, Mobile, and above all New Orleans, were the largest market by volume; New Orleans took more New England ice than any other port by the 1850s. That voyage took several weeks, round Florida and across the Gulf, and some ice went on upriver by steamboat.[^44][^30] Ice also went, less regularly, to Rio de Janeiro and other Brazilian ports, Valparaíso, Bombay, Madras, Hong Kong and other Chinese ports, and a few cargoes to Australia; some routes were dropped after a few years as unprofitable.[^30][^45]

**First Calcutta voyage.** The first cargo to Calcutta sailed from Boston in May 1833 on the *Tuscany* and arrived in September. It caused a sensation: newspapers described the blocks, residents came to the river to see them, and merchants raised money for an ice house. The voyage made a profit and regular sailings followed.[^46][^41]

**Timing.** Calcutta sailings were timed to arrive in the hot season, about March to June, so ships left Boston in autumn and early winter, which also meant the first weeks were spent in cold northern waters with almost no loss. Firms avoided summer sailings to India where they could. The Caribbean and southern ports got ice all year, most in the hot months.[^41][^30]

**Where the melting happened.** Logbook stroke counts were low in the first weeks, rose sharply near the equator, and stayed high to port. On the Calcutta route the second tropical crossing, near the end, was the worst; ice that reached the Cape in good condition could still lose a large share in the last weeks.[^36] Calms in the doldrums cost ice with no distance gained, and masters were told to keep moving and take routes that avoided known calm zones even if longer.[^36][^37] From the 1840s many ice ships were towed up the Hooghly by steam tugs, cutting a passage of days to a day or less; agents paid for the tow as worth the ice saved.[^49][^31]

**How much melted.** A study comparing ice signed for in Boston with ice unloaded in Calcutta, for every voyage where both papers survive, found an average loss of 38 percent, varying widely with season, voyage length, and the stow.[^47] The Caribbean and southern routes lost far less: a well-stowed cargo to Havana or New Orleans often lost under a tenth.[^30] One firm's papers show the Caribbean trade paying for losses on the Indian trade in more than one year.[^15]

**Fast ships and records.** Firms paid more to charter fast ships for India, since fewer days in the tropics meant less loss, and chose the same few masters for the Indian run year after year; for short routes the cheapest ship was usually taken.[^41] Masters kept a separate printed ice book with columns for date, position, deck air temperature, sea temperature, and pumping strokes, sent back to Boston to judge masters and routes. Some filled them daily; others left gaps of a week or more.[^36][^37]

**Stops and news.** Calcutta-bound ships sometimes called at Cape Town or Mauritius and sold some ice; masters were told to sell quickly and reseal within the hour. New Orleans ships sometimes called at Key West or Havana.[^37][^45] News of a Calcutta voyage could take most of a year to reach Boston, so sailings were planned on months-old reports; some letters later came by the faster overland route through Egypt.[^31][^48]

**Return cargoes.** Ships came back from Calcutta with jute, linen, indigo, saltpetre, and spices, often worth more than the ice; some historians argue the ice voyage made sense to shipowners mainly because it put a ship in Calcutta for a valuable return cargo, according to a peer-reviewed economic history article. Caribbean ships returned with sugar, molasses, and coffee. Linings were removed in the far port.[^30][^29]

## Ice houses at the far ports

**First rule.** The Martinique failure taught the trade to build the ice house before the ice arrived. From the 1810s firms built or rented one in each port before sending regular cargoes, sometimes a converted warehouse with extra inner walls, sometimes a new building, and sent carpenters from Boston with the first cargo.[^38][^28]

**Calcutta.** Paid for by a merchants' subscription after the 1833 arrival and opened a few years later, it was a round brick building near the river with thick walls and a domed roof, holding about 1,250 tons when full; the round shape gave the least wall surface for the space.[^50][^51] It followed the Boston double-wall plan but in brick, since wood suffered from termites and monsoon rot. The fill came from Boston at first and later from local materials; the floor drained to the river, and the dome was raised over a ventilated space.[^50][^52] It was run by an agent sent from Boston with local staff who unloaded ships at night and before dawn; the agent also answered to the merchants' committee that had paid for it, which complained when ice ran short.[^31][^50]

**Havana.** The Tudor firm built its house near the harbour in the 1820s after the Spanish colonial government granted it a monopoly on selling ice in the city, in return for keeping the city supplied year-round; it could be fined for running out. The monopoly was renewed several times.[^54][^31] Some Havana houses were partly sunk below street level where the earth was cooler, which kept the lowest layers noticeably colder; this worked only on dry ground.[^53][^52] Ships could not come alongside near the house, so ice went ashore in lighters at night by lantern and was carried by hand and cart; the landing was moved closer to the house in the 1840s.[^43] The house was run through the 1840s by the firm's agent, local merchant Joaquín Barcia, who sold ice by ticket: customers paid at the city office for a set weight and collected at the house door, so no money changed hands there, the door could open and shut quickly, and the office kept an exact count.[^58]

**New Orleans and the South.** New Orleans had several large competing ice houses on the levee by the 1840s, next to the unloading wharves, and competition kept prices lower; some also supplied river steamboats.[^44][^55] Houses there stood fully above ground because of the low wet ground.[^53][^52] By the 1850s carts delivered ice in insulated boxes to hotels, bars, and households with standing orders.[^44] Charleston and Savannah had smaller wooden houses on brick piers holding a few weeks' sales, often owned by local merchants who bought whole cargoes from Boston firms, and sometimes left empty in winter.[^57][^44]

**Other ports.** Bombay and Madras got masonry houses on the Calcutta model in the late 1830s and early 1840s, both smaller than Calcutta's. The Madras house stood near the beach because ice came ashore through the surf in small boats.[^52][^56] Hong Kong's first house, in the 1840s, was granite, on the waterfront; its trade was small and irregular.[^59]

**How ice was sold.** Houses opened only from first light to mid-morning, keeping doors shut through the heat; in Calcutta the hours were printed in the newspapers and latecomers were turned away.[^50][^60] Ice was sold by weight on a scale at the door, and some houses kept blocks pre-cut to standard weights.[^44][^60] Hotels, clubs, hospitals, and military messes had monthly accounts and were often served before the queue, prompting newspaper complaints.[^60][^31] Customers carried ice home in blankets or flannel in baskets or cloth-lined boxes, and it lasted about a day at home; wealthier households had ice chests shipped from Boston.[^61][^50] Agents in new ports gave ice away at first and taught bar owners, cooks, and doctors to use it; Tudor's diary records doing this in Havana and Charleston before charging.[^38][^62] Agents were usually paid a share of sales and quarrelled with Boston over bad cargoes; some were local merchants, others young Boston men sent to learn the business.[^31]

**Losses at the far ports.** Agents report losses in the tropical houses running higher, month for month, than any recorded at the ponds, and tried to sell each cargo before the next arrived.[^31]

## The workers

**Who did the harvest.** Early crews were mostly local farmers and sons in the slack farm season, paid for their horses as well as themselves; some families worked the same pond for generations.[^63][^1] From the 1840s a growing share were Irish immigrants, many arriving during and after the famine, hired for unskilled ice work while skilled jobs often stayed with local men; some lived in shanties near the ponds.[^64][^65] In later decades French-Canadian labourers came south, some from New England mill towns and some from Quebec for the season; by the 1870s some crews on large ponds were mostly French-Canadian.[^66] In short years, agents hired men off Boston streets and paid their train fares.[^64]

**Organisation.** A crew on the largest ponds numbered about 75 men, in gangs working in sequence: snow scrapers, marker and plough, bar men, channel men with pike poles, elevator gang, and stackers. The slowest gang set the pace, and the foreman moved men between gangs; a smaller pond might use a third as many.[^67] Each crew's foreman answered to the firm's superintendent, chose when and where to cut and whom to hire, and kept the notebook; some served one firm twenty years or more.[^3] Labourers were hired by the day from those gathered on the shore at dawn, with no promise of work next day.[^6] Skilled men, marker drivers, stackers, and bar men, were hired for the season at higher pay, and firms wrote to ask them back each year.[^3][^63] Pay came weekly on Saturday evening at the shore shanty, with board deducted.[^15]

**Others.** Boys from about twelve guided blocks, swept chips, ran messages, and fetched coffee, for less pay.[^6][^63] Women did not work on the ice but ran boarding houses, cooked for the shanties, washed and dried wet clothing, and took on farm work; firms' accounts record payments usually under the household's name.[^63][^15] The ship-loading stevedores were a separate year-round waterfront workforce, in gangs under a boss contracting per ship, paid by the ton.[^35] At far ports, local porters hired by the agent did the carrying in Calcutta, and in Havana the firm's depot hired enslaved men from their owners to unload ships; almost nothing is recorded of their own experience.[^70][^31]

**Conditions.** The day ran from first light to dark; before a forecast thaw, elevators and stacking crews worked into the night by lantern and some crews worked Sundays, with no extra pay for a long day unless the foreman agreed.[^13] Cold was the hardship every account mentions: frostbite of fingers, ears, and feet was common. Men wore layers of wool, felt boots with leather overshoes, and iron "creepers" strapped to their boots. A man who got wet could freeze before reaching shelter, so anyone who fell in was sent straight to the shanty fire.[^6][^69] Larger ponds' shanties kept coffee and soup hot and served a hot midday meal; outside men slept in boarding houses or seasonal bunkhouses.[^6]

**Dangers.** Men slipped, cut themselves on saws and bars, and were crushed by slipping blocks or shifting stacks; a block falling from the top of the elevator could kill. Firms paid an injured man nothing beyond days already worked.[^69][^6] The worst danger was falling through the cut field, the channel, or thin overnight ice, where a man could be carried under by the current or trapped among blocks. A count of newspaper reports for the Cambridge ponds found nine harvest-crew drownings between 1850 and 1860, mostly men who fell into the channel at night. Firms put up no railings or lights along the channel until late in the trade.[^69][^13]

**Conflict and hardship.** Newspapers report fights between local men and Irish labourers in years of scarce work; foremen sometimes kept the groups in separate gangs, and tension eased as Irish sons moved into skilled jobs.[^65][^68] In the 1850s and 1860s crews on several ponds struck for higher daily pay when a thaw was forecast, for a day or two until the firms agreed; firms then hired outside men and blacklisted strikers.[^71][^64] An open winter meant no harvest wage, and Boston charities reported more families seeking help in the winters after one.[^72]

## Buyers and prices

**Calcutta.** The first buyers were British residents: East India Company officials, army officers, merchants, and their families, using ice in drinks, desserts, and to cool rooms. Wealthy Indian merchant and landowning families also bought from the early years and were regular customers by the 1840s; for most of the population ice was far too costly.[^50][^61] Ice sold at the door for 3 annas a pound (an anna being a sixteenth of a rupee) in the 1830s and 1840s, holding steady for most of those decades; account customers sometimes paid less by private agreement.[^60][^30] Hospitals were among the largest account customers and got a reduced rate for a daily hot-season contract.[^73][^60] Clubs and officers' messes served iced drinks through the hot season, and clubs' records show ice among their largest hot-month costs.[^61]

**Madras and Bombay.** Prices in both cities were above Calcutta's for the same years, as Madras ice came through the surf and Bombay got fewer cargoes. Buyers were similar: British residents, clubs and messes, hospitals, and wealthy Indian and Parsi merchant families.[^56][^75]

**Havana.** Main buyers were cafés, confectioners making ice creams and sorbets, and wealthy households; cafés bought on account and households by ticket. Within a generation ice went from a luxury of the rich to a common pleasure in the city's cafés.[^54][^62] Under the monopoly the firm agreed to a maximum price, which the government revised several times and could lower if supplies ran short or the public complained, so the firm could not raise prices in the hottest weeks.[^54]

**New Orleans and the South.** New Orleans used ice on a scale no other port matched: bars serving every class, hotels, households, meat and fish markets, and river steamboats. By the 1850s the local press described daily ice as a necessity.[^44][^74] Prices fell steadily from the 1830s to the 1850s as competing firms and houses arrived, and more people bought as the price fell; firms made money on volume.[^44][^30] By 1860 ice sold for about 2½ cents a pound at the levee houses, according to the city's weekly price current, rising in hot months and when a ship was late.[^76] Ordinary households bought regularly by the 1850s, from street carts and grocers.[^74] Steamboats took ice upriver and sold some at river towns.[^74][^77] In Charleston and Savannah, buyers were planters, merchants, hotels, and taverns.[^57] In the southern ports butchers, fishmongers, and dairies were large daily buyers.[^44][^40] During New Orleans' yellow fever epidemics of the 1850s, hospitals bought heavily, the city government bought ice for hospitals and the poor, and some firms gave ice free to the sick.[^73]

**Hong Kong.** Buyers were the British garrison, trading-house merchants, and ships in harbour; notices show long gaps with no ice in the colony at all.[^59]

**What drove prices.** At every far port prices were lowest just after a ship arrived and highest when stock ran low, and a port that ran dry had no ice at any price until the next ship.[^60][^43] Ice cost almost nothing at the pond; a cost study found ice lost in transit and storage was the largest single cost on the long routes, larger than carriage.[^30] Boston firms fought price wars, flooding a contested port and undercutting until a rival quit, then raising prices again.[^31][^30] At small ports without ice houses, ice was sold from an open hatch at whatever buyers would pay, both well above and well below regular prices.[^37]

## The end of the trade

**What ended it.** The trade by sea peaked around 1860 and was nearly over by the 1880s. Historians point to no single cause but to war, ice-making machines, steamships, and the growth of the home market, in an order that differed by port.[^30][^78]

**The Civil War.** The Union blockade from 1861 closed the southern ports; New Orleans was shut to Boston ships until Union forces took it in 1862. Southern hospitals went short, and the shortage pushed southern businessmen toward machine-made ice.[^79][^44] Some Carré machines were run through the blockade for hospitals and the wealthy.[^82] Trade resumed to New Orleans from 1862 and elsewhere after 1865, but firms found ice houses damaged or sold and agents gone, and late-1860s southern cargoes were well below late-1850s levels.[^79][^30]

**Machines.** John Gorrie patented an ice machine in 1851; Ferdinand Carré developed an ammonia machine in France in the late 1850s; James Harrison built ice machines in Australia in the 1850s. These were costly and made little ice at first.[^80][^81] New Orleans' first commercial ice factory opened in 1868 on the Carré pattern, making about 12 tons a day, with more following over the next decade.[^83][^44] Through the 1870s factory ice became cheaper than shipped ice once melt loss was counted, and in the southern ports the shift took about twenty years.[^30] Some firms cut prices to drive out factories, which closed a few small ones in the 1870s but could not last.[^44] Early factory ice was cloudy and distrusted, slowing the switch in some ports, until factories learned to make clear ice by the 1880s.[^80][^84] Calcutta got a machine-ice company in the late 1870s, with Bombay and Madras following, and the Calcutta ice house lost its trade within a few years.[^85][^50] In Havana the colonial government stopped renewing the monopoly after the American war and factories opened in the 1870s; Cuba's wars for independence from 1868 also disrupted trade.[^54][^89]

**Steamships and the home market.** As steamships took over the routes to Asia, especially after the Suez Canal opened in 1869, the supply of cheap outward sailing ships shrank, and steamship carriage cost more.[^41][^30] Meanwhile northern and Midwestern cities, breweries, meat packers, and refrigerated rail cars absorbed all the ice New England and Hudson valley ponds could cut, and many firms turned to the home market.[^16][^78] Ponds near Boston were fouled or built over, and Fresh Pond became Cambridge's water supply, with harvesting restricted and then stopped.[^86][^78] Tudor died in 1864, and other firms merged into home-market companies.[^87][^28]

**The last cargoes.** Calcutta cargoes dwindled through the 1870s to one or two ships in some years; the Bombay and Madras trade ended earlier.[^90][^30] The last recorded cargo to Calcutta sailed from Boston in 1882 aboard the bark *Margaret Ellery*, consigned to the old ice house company; no later ice ship appears in the Calcutta register, and her master noted the cargo arrived in fair condition.[^92] The Boston papers that had celebrated the first ice ships printed no reports of the last ones.[^91] For later Caribbean and southern shipments, see Disagreement / Uncertainty.

## Disagreement / Uncertainty

**Storage loss.** The 1847 Fresh Pond ledger records about 17 percent over a season.[^23] A general history says a well-built house lost a fifth to a third over a summer, and small houses sometimes half, giving no source for these figures.[^28] An archives research note warns that ledgers kept by counting blocks show smaller losses than ledgers kept by weighing, because counting hides shrinkage in blocks that did not break, so figures from the two methods cannot be compared. The 1847 ledger used weighing.[^26][^18]

**Voyage loss to Calcutta.** The logbook study gives an average of 38 percent.[^47] A general history says well-stowed ships lost about a quarter and attributes higher losses to poor stowing rather than voyage length, without saying how the figure was reached.[^28] Neither source says which years its figure covers.[^28] The study's authors themselves note that surviving papers may come disproportionately from better-run voyages, since firms were more likely to keep records of voyages that went well.[^47]

**When the shipping trade ended.** Some histories put the end in the early 1880s. A general history says Caribbean cargoes continued irregularly into the 1890s and small shipments went to southern ports into the early twentieth century when local factories could not keep up, giving no source for the later shipments.[^28][^78]

**Thinly supported figures.** The short-route loss figure of under a tenth is an estimate from a small number of voyages.[^30] The drowning count may miss deaths not reported in newspapers.[^69] The number of Carré machines brought through the blockade is not known.[^82] The rope method for rescuing horses is described with no count of how often it worked.[^6]

## Useful Details

- Icehouses burned easily because of dry sawdust and hay, often in summer when a spark from a passing railway engine could catch the outer wall. The ice usually survived standing in the ruins but then melted within days unless loaded at once. Fire led some firms to build in separate sections, and some carried no insurance.[^27][^18]
- Maine mills, which had once burned or dumped their sawdust in the river, came to depend on selling it to the trade; Boston buyers inspected each schooner load by hand and paid by dryness.[^33]
- The hold linings were removed in the far port and the planks often sold there, as timber was scarce in some tropical ports.[^32]
- In the early years sailors feared melting ice would sink the ship; Tudor's diary records trouble finding crews. By the 1840s sailors with ice experience were valued for knowing the pumping routine.[^38][^28] Insurance records show ice ships lost in about the same numbers as other ships on the same routes.[^39]
- Marine insurers at first refused ice cargoes entirely; later policies excluded loss from melting, which the shipper bore.[^39][^30]
- Masters and agents often stowed apples, butter, and cheese in pockets in the ice as private trade; agents' letters report apples arriving in Calcutta and Havana in better shape than after a month in a Boston cellar.[^31][^40]
- Some masters said ships rolled more in the last weeks as the ice melted and the ship rose.[^36]
- Calcutta's merchants gave the *Tuscany*'s master a gift in thanks.[^46]
- Frederic Tudor, once in debtors' prison, became one of Boston's richest men by the 1840s, known as the "Ice King"; profits came mostly from the southern and Caribbean markets.[^38][^28]
- Some Indian households in 1830s Calcutta questioned whether ice handled by foreign sailors and porters was clean; the doubts faded by the 1840s.[^60]
- Historians argue the New England firms created the demand that later ice factories supplied, according to peer-reviewed food and economic history articles.[^62][^30]
- The Madras ice house was later a home, then a school, and still stands on the seafront as a museum; the Calcutta house was pulled down in the late nineteenth century, and the Havana house has not been traced.[^56][^50] The Tudor firm's papers are the largest single source on the trade.[^87]
- After the sea trade, harvest crews kept cutting for the home market; Maine and Hudson valley ponds employed more men in the 1880s than the Boston ponds had at the sea trade's height.[^88] Home natural-ice harvests continued into the 1920s and 1930s, with the last commercial harvests on many New England ponds in the 1930s and 1940s.[^78][^6]
- The "icebox" and the "iceman" grew out of the habit of using ice that the trade helped spread.[^84]

## Open Research Questions

- What did harvest labourers, skilled men, and boys earn per day, and how did ice prices compare across ports in a common currency?
- What exact maximum prices did the Havana monopoly set, and how did they change?
- Which years do the competing Calcutta loss figures cover?
- Do shipping registers or port records show any New England ice cargoes to the Caribbean or the southern ports after 1882?
- How large were the Bombay, Madras, Havana, and New Orleans ice houses in tons?

## Reliability / Limitations

- `New England industry history site (pond rights)`[^2]: cites no archive for the pond-rights figures.
- `Agricultural magazine, February 1856`[^5]: gives advice to farmers, not an account of a single harvest.
- `Agricultural magazine, June 1859`[^21]: written for farmers, not the shipping firms.
- `Walden-region oral histories`[^6]: recorded from people who worked the last commercial harvests, long after the shipping trade ended, and may not describe the early trade; the horse-rescue method is described with no count of how often it worked.
- `Tudor papers, pond accounts`[^15]: the block weight is the firm's own working figure, not a measured average.
- `Cambridge historical society, icehouses`[^17]: the Fresh Pond house size comes from a company prospectus.
- `Boston newspaper, August 1868`[^27]: covers one fire; the industry site gives no count of fires.
- `General history book excerpt`[^28]: gives its storage-loss and Calcutta voyage-loss figures, and its claim of later shipments, without sources.
- `Tudor papers, agents' letters`[^31]: the fish-tasting cargo comes from one agent's letter; agents report far-port losses in general terms not comparable with the pond ledgers; the price-war letters describe the firm's tactics from its own side.
- `Logbook collection`[^36]: the remark on ships rolling more comes from masters' comments, not measurement.
- `Tudor diary excerpts`[^38]: record Tudor's own view of his difficulties.
- `Economic history article, 2010`[^30]: its short-route loss figure is an estimate from a small number of voyages.
- `Calcutta melt study`[^47]: its authors note that surviving papers may come from the better-run voyages.
- `Colonial architecture article, 2016`[^52]: compares ports, giving the Havana design as a contrast to Calcutta.
- `Hong Kong heritage page`[^59]: relies on newspaper notices and gives no building records.
- `Memoir collection`[^61]: written by British residents describing their own households and experience.
- `Calcutta newspaper notices`[^60]: reports on Indian customers were written by British newspapers.
- `Boston newspaper, January 1851`[^68]: reports are short and give one side.
- `Havana dock-labour contracts`[^70]: contracts and letters by employers; no account by the workers survives.
- `Boston newspaper, February 1866`[^71]: takes the firms' side.
- `Labour history page on conditions`[^69]: the drowning count comes from newspaper reports, which may have missed some deaths.
- `Civil war commerce page on Carré machines`[^82]: the number of machines brought through the blockade is not known.
- `Gulf commerce page on New Orleans`[^44]: gives no list of the factories that closed.
- `Havana monopoly records`[^54]: end before the monopoly's last years; the later account comes from a university research project.[^89]

## Sources

[^1]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview
[^2]: https://www.new-england-industry.example/ice/pond-rights
[^3]: https://www.harvard-business-archive.example/tudor-papers/harvest-instructions
[^4]: https://www.new-england-industry.example/ice/snow-and-flooding
[^5]: https://www.farm-journal-archive.example/1856/february/ice-for-market
[^6]: https://www.walden-region-history.example/oral-histories/ice-crews
[^7]: https://www.mit-tech-history.example/inventors/wyeth-ice-tools
[^8]: https://www.patent-records.example/1829/wyeth-ice-cutting-apparatus
[^9]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s
[^10]: https://www.new-england-industry.example/ice/breaking-and-floating
[^11]: https://www.steam-power-history.example/small-engines/ice-elevators
[^12]: https://www.boston-markets-history.example/ice/local-trade
[^13]: https://www.boston-newspaper-archive.example/1858/january/ice-crop
[^14]: https://www.new-england-industry.example/ice/open-winters
[^15]: https://www.harvard-business-archive.example/tudor-papers/pond-accounts
[^16]: https://www.hudson-valley-museum.example/collections/ice-tool-catalogues
[^17]: https://www.cambridge-historical.example/fresh-pond/icehouses
[^18]: https://www.new-england-industry.example/ice/storage-history
[^19]: https://www.harvard-business-archive.example/tudor-papers/storage-trials
[^20]: https://www.massachusetts-engravings.example/prints/fresh-pond-ice-works-1852
[^21]: https://www.farm-journal-archive.example/1859/june/building-an-ice-house
[^22]: https://www.harvard-business-archive.example/tudor-papers/keepers-letters
[^23]: https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage
[^24]: https://www.railroad-history-ma.example/branches/charlestown-ice-line
[^25]: https://www.boston-harbour-history.example/wharves/charlestown-ice-houses
[^26]: https://www.ma-archives.example/ice-ledgers/methods-note
[^27]: https://www.boston-newspaper-archive.example/1868/august/icehouse-fire
[^28]: https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt
[^29]: https://www.maritime-boston.example/trade/outward-cargoes
[^30]: https://www.economic-history-review.example/2010/ice-shipping-costs
[^31]: https://www.harvard-business-archive.example/tudor-papers/agents-letters
[^32]: https://www.maritime-salem.example/papers/ship-fittings-for-ice
[^33]: https://www.maine-lumber-history.example/mills/sawdust-trade
[^34]: https://www.maritime-salem.example/papers/stowing-ice-1850
[^35]: https://www.boston-harbour-history.example/wharves/stevedores
[^36]: https://www.sailing-ship-logs.example/collections/ice-voyages
[^37]: https://www.harvard-business-archive.example/tudor-papers/masters-instructions
[^38]: https://www.harvard-business-archive.example/tudor-papers/diary-excerpts
[^39]: https://www.insurance-history.example/marine/perishable-cargoes
[^40]: https://www.food-history-quarterly.example/2014/new-england-apples-abroad
[^41]: https://www.maritime-boston.example/routes/boston-calcutta
[^42]: https://www.maritime-boston.example/routes/caribbean
[^43]: https://www.havana-archive.example/colonial-trade/shipping-arrivals
[^44]: https://www.gulf-commerce.example/ports/new-orleans-ice-imports
[^45]: https://www.maritime-boston.example/routes/other-ports
[^46]: https://www.calcutta-history-society.example/1833/first-ice-ship
[^47]: https://www.ice-trade-voyages.example/logs/calcutta-melt-study
[^48]: https://www.postal-history-review.example/2009/overland-mail-to-india
[^49]: https://www.calcutta-history-society.example/port/hooghly-pilots-and-tugs
[^50]: https://www.calcutta-history-society.example/buildings/the-ice-house
[^51]: https://www.british-library-images.example/calcutta/ice-house-1840s
[^52]: https://www.colonial-architecture-journal.example/2016/cold-storage-in-bengal
[^53]: https://www.havana-archive.example/colonial-trade/building-permits
[^54]: https://www.havana-archive.example/colonial-trade/ice-monopoly
[^55]: https://www.louisiana-archives.example/levee/warehouse-registers
[^56]: https://www.madras-heritage.example/beach-road/ice-house
[^57]: https://www.lowcountry-history.example/charleston/ice-trade
[^58]: https://www.havana-archive.example/colonial-trade/ice-depot-1840s
[^59]: https://www.hongkong-heritage.example/waterfront/early-ice-house
[^60]: https://www.calcutta-gazette-archive.example/notices/ice-house-hours
[^61]: https://www.memoirs-of-empire.example/collections/calcutta-domestic-life
[^62]: https://www.food-history-quarterly.example/2012/ice-cream-in-the-tropics
[^63]: https://www.labor-history-ne.example/winter-work/farm-families
[^64]: https://www.labor-history-ne.example/winter-work/irish-labour
[^65]: https://www.immigration-history-journal.example/2012/boston-irish-winter-work
[^66]: https://www.immigration-history-journal.example/2015/french-canadians-in-new-england
[^67]: https://www.labor-history-ne.example/winter-work/harvest-crew-sizes
[^68]: https://www.boston-newspaper-archive.example/1851/january/disturbance-on-the-ice
[^69]: https://www.labor-history-ne.example/winter-work/ice-crews-conditions
[^70]: https://www.havana-archive.example/colonial-trade/dock-labour-contracts
[^71]: https://www.boston-newspaper-archive.example/1866/february/ice-strike
[^72]: https://www.boston-newspaper-archive.example/1880/march/open-winter-hardship
[^73]: https://www.medical-history-journal.example/2013/ice-in-tropical-medicine
[^74]: https://www.louisiana-archives.example/newspapers/daily-ice-reports
[^75]: https://www.bombay-gazette-archive.example/notices/ice-sales
[^76]: https://www.gulf-commerce.example/price-current/ice-1860
[^77]: https://www.river-history-review.example/2011/steamboat-provisioning
[^78]: https://www.new-england-industry.example/ice/decline
[^79]: https://www.civil-war-commerce.example/blockade/ice-shortage
[^80]: https://www.mit-tech-history.example/inventors/early-refrigeration
[^81]: https://www.patent-records.example/1851/gorrie-ice-machine
[^82]: https://www.civil-war-commerce.example/blockade/carre-machines
[^83]: https://www.louisiana-archives.example/business/ice-manufacturing-charters
[^84]: https://www.food-history-quarterly.example/2016/clear-ice-and-cloudy-ice
[^85]: https://www.calcutta-history-society.example/industry/bengal-ice-factory
[^86]: https://www.cambridge-historical.example/fresh-pond/water-supply
[^87]: https://www.harvard-business-archive.example/tudor-papers/finding-aid-overview
[^88]: https://www.labor-history-ne.example/winter-work/after-the-sea-trade
[^89]: https://www.cuba-commerce-history.example/1870s/manufactures
[^90]: https://www.ice-trade-voyages.example/registers/calcutta-arrivals
[^91]: https://www.boston-newspaper-archive.example/1880s/ice-coverage-survey
[^92]: https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882
````

Final reply:

````
I've finished the light note. I checked it against the findings, removed one repeated point and fixed a footnote that pointed to the wrong source. I couldn't read the example note because I didn't have permission to open that file, so I followed the template's layout only.

```json
{ "note": "Research/research-light-ice-trade.md", "cut_short_topics": [] }
```
````

#### Run 2

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-09'
PASS  fm-modified-run-date  found 'modified: 2026-10-09'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-footnotes-resolve   **Every marker has a definition.** The body uses markers from `[^1]` through `[^92]`. No marker outside that range appears, such as `[^93]`. Sources has a definition line for every number from 1 to 92.  **Every definition holds a URL.** Each of the 92 definition lines is a single `https://` URL. For example: - `[^1]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview` - `[^9
PASS  judge-planted-details-cite-own-url   All eight details appear in the note, and each carries a footnote that resolves to the expected URL.  1. **Topic 1, blocks 22 inches square:** "cutting a grid that gave blocks 22 inches square.[^9]" The Summary also has "regular blocks 22 inches square.[^7][^9]" Under Sources: "[^9]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s". 2. **Topic 2, about 17 percent lost in 1847
PASS  judge-reply-no-cut-short   The reply names no topic as cut short. Its only claim about truncation is an empty list: `"cut_short_topics": []`. That matches the fact that all eight findings files ended with `<!-- end of findings -->`. The reply calls no file incomplete or missing its closing line.
PASS  judge-sixteen-questions-answered   All sixteen questions are answered with the findings' answers. Each is quoted below.  1. **Cutting time and thickness:** "usually from the middle of January into February, once a long hard freeze had set in" and "Ice was not cut until it was at least 14 inches thick." The note adds: "Each morning a foreman walked the pond with a hand auger and bored test holes… only the clear ice counted." 2. **T
PASS  keeps-t1-14-inches  found '14 inch'
PASS  keeps-t1-22-inch-blocks  found '22 inch'
PASS  keeps-t2-17-percent-loss  found '17 percent'
PASS  keeps-t2-9400-tons  found '9,400'
PASS  keeps-t3-pumped-every-4-hours  found '4 hours'
PASS  keeps-t3-sawdust-1-to-11  found '11 tons'
PASS  keeps-t4-130-days  found '130 days'
PASS  keeps-t4-38-percent-loss  found '38 percent'
PASS  keeps-t5-1250-tons  found '1,250'
PASS  keeps-t5-barcia  found 'Barcia'
PASS  keeps-t6-75-men  found '75'
PASS  keeps-t6-nine-drownings  found 'nine drown'
PASS  keeps-t7-2-half-cents  found '2½'
PASS  keeps-t7-3-annas  found '3 annas'
PASS  keeps-t8-12-tons-a-day  found '12 tons'
PASS  keeps-t8-margaret-ellery  found 'Margaret Ellery'
PASS  keeps-url-topic-1  found 'https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s'
PASS  keeps-url-topic-2  found 'https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage'
PASS  keeps-url-topic-3  found 'https://www.maritime-salem.example/papers/stowing-ice-1850'
PASS  keeps-url-topic-4  found 'https://www.ice-trade-voyages.example/logs/calcutta-melt-study'
PASS  keeps-url-topic-5  found 'https://www.havana-archive.example/colonial-trade/ice-depot-1840s'
PASS  keeps-url-topic-6  found 'https://www.labor-history-ne.example/winter-work/harvest-crew-sizes'
PASS  keeps-url-topic-7  found 'https://www.gulf-commerce.example/price-current/ice-1860'
PASS  keeps-url-topic-8  found 'https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## Cut'
PASS  shape-topic-2-section  found '## Stor'
PASS  shape-topic-3-section  found '## Load'
PASS  shape-topic-4-section  found '## The voyage'
PASS  shape-topic-5-section  found '## Ice houses at the far port'
PASS  shape-topic-6-section  found '## The worker'
PASS  shape-topic-7-section  found '## Buyers and price'
PASS  shape-topic-8-section  found '## The end'
PASS  file-name  expected name written
````

`project/Research/research-light-ice-trade.md`:

````markdown
---
title: Light Research - Ice Trade
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-09
modified: 2026-10-09
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Topics: cutting the ice on the ponds; storing the ice before shipping; loading the ship; the voyage; ice houses at the far ports; the workers; buyers and prices; the end of the trade. Boundary: New England ice shipped by sea, from the trade's start to its end.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Ice Trade

## Summary

The New England ice trade took clear ice from Massachusetts ponds such as Fresh Pond in Cambridge, Wenham Lake and Spy Pond, and buyers in hot ports judged it by how clear it was.[^1] The harvest ran from about the middle of January into February, and ice was not cut until it had at least 14 inches of clear ice.[^1][^3] Horse-drawn tools, first designed by Nathaniel Wyeth in 1825, cut the ice into regular blocks 22 inches square.[^7][^9] The blocks were stored for months in large icehouses on the pond shore. These had double walls packed with sawdust, and the largest at Fresh Pond held about 9,400 tons.[^17][^19] One Fresh Pond house's ledger for 1847 records a loss of about 17 percent over the season.[^23]

The ice went to sea in ordinary merchant ships that would otherwise have left Boston in ballast.[^29][^30] Carpenters lined each hold with a planked "ice ceiling" packed with sawdust. The ice was stowed with one ton of sawdust for every 11 tons of ice, and the hatches stayed sealed until port.[^32][^34][^37] Voyages took two to three weeks to the Caribbean and about 130 days to Calcutta.[^42][^41] A study of logbooks found that ships on the Calcutta run lost 38 percent of their ice on average. Short routes often lost under a tenth.[^47][^30]

At the far ports, ice houses such as Calcutta's round brick building, which held about 1,250 tons, sold ice by weight in the early morning.[^50][^60] They were run by agents who were usually paid a share of the sales.[^31] The harvest crews were local farmers at first, then Irish labourers from the 1840s and French-Canadians in later decades. On the largest ponds a crew numbered about 75 men, and the men worked in hard cold with a real risk of drowning.[^63][^65][^66][^67][^69]

Buyers ranged from British residents and hospitals in Calcutta to cafés in Havana and ordinary households in New Orleans.[^50][^61][^62][^74] Ice sold for 3 annas a pound in Calcutta in the 1830s and 1840s, and for about 2½ cents a pound in New Orleans by 1860.[^60][^76] No single cause ended the trade. War, ice-making machines, steamships, and a growing home market came together.[^30][^78] The last recorded cargo to Calcutta sailed in 1882.[^92] Sources disagree on when shipments by sea ended altogether.[^28][^78]

## Cutting the ice on the ponds

**When the ice was ready.** The harvest ran in the coldest weeks of the year, usually from the middle of January into February, once a long hard freeze had set in.[^1][^2] The firms preferred spring-fed ponds with no streams running in. Moving water froze unevenly and carried silt, leaves, and sawdust from upstream mills into the ice.[^1][^2] The firms bought or leased shore rights so that no rival could cut there, and a pond owner could earn more from one winter's ice rights than from a year of farming the land around it.[^1][^2] Foremen kept daily notebooks through the season, recording the air temperature at dawn and noon, the wind, and any snowfall.[^1][^2]

Ice was not cut until it was at least 14 inches thick. Thinner ice crumbled at the corners when it was handled, wasted space in the hold, and melted faster.[^1][^3] Each morning a foreman walked the pond with a hand auger and bored test holes at set points. He measured the clear ice separately from any white snow ice on top, and only the clear ice counted. If the readings fell short, the crew was sent to clear snow or stood idle.[^1][^3] Some firms paid a small bonus to the foreman whose pond reached cutting thickness first. Cutting often began near the shaded shore and moved outward as the ice thickened.[^1][^3]

Before the harvest began, the foreman cut a small test block, held it up against the light, and looked for bubbles, streaks, and dirt. If a dark object showed clearly through the whole thickness, the ice was good enough for shipping. If the block was cloudy, the cutting moved to another part of the pond, often further from the inlet or the shore. The test was repeated every few days.[^6][^3]

**Snow and weather.** Snow on the pond slowed the freezing of the clear ice underneath. Wet snow that froze on top became "snow ice," which was white, full of air, and weak.[^4][^5] Crews cleared snow with horse-drawn scrapers, which were wide wooden boards dragged across the surface. On some ponds they bored holes and let water flood the cleared surface so that a fresh layer froze on top. Flooding only worked in hard cold.[^4][^5] A snowfall could stop all work for several days.[^4][^5]

A thaw or a day of rain softened the ice, flooded the grooves, and refroze them unevenly, so the field often had to be planed and cut again.[^13][^14] A mild "open winter" left the ponds too thin to cut. The shippers then bought ice from ponds in Maine and New Hampshire at a higher cost.[^13][^14] In a good season a large pond could be cleared in two to three weeks. Crews sometimes cut on Sundays when a thaw was forecast, against local custom. Several firms kept icehouses on two or more ponds.[^13][^14]

**The tools.** Before the 1820s, ice was cut by hand with axes, hand saws, and chisels into blocks of uneven shape. These were hard to stack and left gaps that let in warm air.[^7][^8] Nathaniel Jarvis Wyeth was a Cambridge hotel manager who later worked for the Tudor ice company. He designed a horse-drawn cutter in 1825 and patented an improved version in 1829.[^7][^8] Historians describe the move to horse tools as the change that made long voyages possible, because regular blocks lost less ice. By the 1840s most commercial ponds in Massachusetts used some version of Wyeth's tools.[^7][^8]

The first horse tool was the "marker," a plough-like frame with a row of steel teeth, drawn by one horse along a line laid out with a cord. A guide arm kept each groove parallel to the last. When the field had been scored one way, the marker was run across at a right angle, cutting a grid that gave blocks 22 inches square.[^9] The "plough" had longer teeth and was run along the same grooves until each cut went about two-thirds of the way through the ice. The remaining third held the field together so that men and horses could still walk on it.[^9] The horse walked on uncut ice beside the line being cut.[^6][^5]

The horses were shod with sharp-calked shoes, which had spikes that gripped the ice, and a blacksmith was kept near the larger ponds.[^6][^5] A horse breaking through into the water was the most common accident of the harvest. Crews looped a rope around its neck and pulled it tight. This made the horse hold its breath and float higher, so that the men could drag it back onto the ice.[^6][^5]

**Breaking, floating, and lifting.** Crews sawed a channel to the shore with long hand saws. Men with iron "breaking bars," flat chisels on long handles, then split the field along the grooves into rafts, and the rafts into single blocks.[^10][^6] Men with pike poles pushed the blocks along the channel. Pike poles were long wooden poles with an iron hook and spike. Boys guided the blocks around corners, and in hard cold the channel had to be kept open by breaking the new ice that formed overnight.[^10][^6]

At the shore an inclined elevator carried the blocks up into the icehouse. It was a long wooden ramp with an endless chain whose cleats caught each block.[^1][^11] A horse at a capstan drove the chain at first, and from the 1850s the largest houses used small steam engines.[^1][^11] Before a block went up, a man planed its top and bottom flat to remove any snow ice. The elevator could run day and night by lantern light.[^1][^11]

**Grading and counting.** The clearest blocks were marked first quality and set aside for shipping. Blocks with a cloudy band or trapped leaves were usually sold locally, to households and butchers in Boston and nearby towns.[^3][^12] Foremen graded the blocks by eye. One firm told them to reject any block they would not want to see on a dinner table.[^3][^12] A tally man at the top of the elevator marked every block, and the count was turned into tons using the firm's figure of roughly 200 pounds for a regular first-quality block. Pond owners were usually paid by the ton, and disputes over the count are recorded.[^15]

By the 1850s, tools were sold as complete sets by specialist firms, many of them in the Hudson valley. A set held markers, ploughs, hand saws up to six feet long, breaking bars, pike poles, ice tongs, and snow scrapers.[^16][^7] The makers' catalogues are one of the main sources for how the work was done. The tools changed little, and a set bought in the 1850s could still be in use thirty years later.[^16][^7]

## Storing the ice before shipping

**Why and where.** The harvest came in over a few weeks, but ships sailed all year, so the ice had to be stored for months.[^17][^18] The firms built their icehouses above ground on the shore of the pond itself. The older farm practice had been to keep ice in hillside pits, which held only a few tons and let groundwater seep in.[^17][^18] The houses stood near the railway lines to the Boston wharves, so ice could be sent to a ship within a day of the order.[^17][^18]

**How they were built.** An icehouse had an outer and an inner wooden wall. The space between them was packed with sawdust from the timber mills or with spent tanbark, and some houses had three walls.[^19][^7] Frederic Tudor and Nathaniel Wyeth tested fills in the 1820s and 1830s by weighing the ice in small trial houses at the start and end of summer. They found that a dry fill kept ice far better than a damp one, and the houses were given wide eaves to keep rain out of the fill.[^19][^7] The roof was steep, with louvred vents along the ridge that let warm air escape. Most houses were painted white or a light colour, and some had hay or straw in the roof space.[^21][^18]

Ice standing in water melted much faster than ice standing in air. So the floors were built over a bed of gravel or broken stone, with a drain running out to the pond, and were covered with a thick layer of sawdust. A house with a blocked drain could lose a large part of its bottom layers in a single warm month.[^19] One firm's papers record the dismissal of a keeper who let a drain freeze over.[^19]

**How much they held.** The biggest icehouse on Fresh Pond held about 9,400 tons when full and was taller than a three-storey building.[^17][^20] It was a row of rooms under one long roof. Each room was filled and emptied on its own, so that opening one did not let warm air into the rest.[^17][^20] Engravings show a long, windowless block with doors stacked one above another. The doors were boarded shut as the ice rose past them.[^17][^20] Smaller firms built houses that held a few hundred tons and sold mostly to the local market.[^17][^20]

**Stacking, keeping, and taking out.** The blocks were set on edge, tight against each other, with each layer laid across the one below like brickwork. Gaps were filled with ice chips, and a full room was covered with a deep layer of hay or sawdust.[^17][^6] The stackers were counted among the most skilled men of the harvest, because a badly laid stack could lean and fall.[^17][^6] Each large house had a keeper who lived beside it all year. He checked the drains, vents, and doors, watched for fire, kept the ledger, and wrote to the Boston office about once a week.[^22] From the 1850s some keepers recorded thermometer readings above the stack each morning and evening.[^22]

When a ship was ready, the ice was taken out from the top of the stack down, one room at a time. The blocks had often frozen together and were broken apart with bars. They were scraped clean of fill and sent down a chute to the railway wagons. Keepers used the oldest ice first and kept the best-packed rooms for the hottest months.[^3][^12]

From the early 1840s a railway branch line ran from Fresh Pond to the Charlestown wharves and cut the journey to under an hour. Its wagons had thick sides packed with sawdust, and in summer the trains ran at night.[^24][^17] The firms also kept smaller wharf icehouses holding a few hundred tons each. Ice was held there only for the few days before a ship sailed, because the harbour air was warmer and damper.[^25]

**Loss in storage.** The ledger of one Fresh Pond icehouse for 1847 shows that the house lost about 17 percent of its ice between the end of the harvest in March and the last autumn sailing. Most of the loss came in July and August.[^23] The keeper blamed the heat and a roof vent that had been left shut. He also recorded that a room left unopened until autumn lost less than one opened in June.[^23] The ledger is the only surviving record of a whole season's loss for a single house, and historians use it as the standard figure.[^23] Large houses lost less than small ones because a big stack has less surface for its weight. This was the main reason the firms built ever-larger houses through the 1840s and 1850s.[^28][^18]

## Loading the ship

**The ships.** Boston merchants brought home large tropical cargoes but had little to send out, so many ships left in ballast. Ice gave them a paying outward cargo, and shipowners charged low rates to carry it.[^29][^30] Older ships were often chosen, because owners did not want their best ships altered with linings.[^29][^30] The ice firms kept a list of ships they would not charter. A hold that had carried fish, hides, or molasses was scrubbed and aired for days, because smells passed into the ice, and ships that had carried coal were avoided.[^31]

**The lining.** A carpenter built an inner wall of pine planks a little way in from the hull on all sides, across the floor, and up under the deck beams. The space between was packed with sawdust. Sailors called this lining the "ice ceiling."[^32][^29] Building it took a carpenter and two helpers about a week for a ship of middling size. The lining was taken out in the far port, and the planks were often sold there.[^32][^29] The floor was laid on rough timber called dunnage, with a deep bed of sawdust on top and gaps at the sides so that melt ran into the bilge. A badly built floor left the bottom layer standing in water, and the loss from the bottom layer was the largest single loss on most voyages that kept records.[^32]

**Sawdust.** The firms bought pine sawdust, a waste product of the Maine timber mills, and brought it to Boston by schooner. An 1850 paper by a Salem merchant sets the ratio at one ton of sawdust for every 11 tons of ice. With less sawdust, the paper says, more ice was lost than the sawdust saved, and more sawdust took up space that could have carried ice.[^34] The sawdust had to be dry. Wet sawdust froze into a crust that conducted heat into the ice. The firms dried their sawdust in covered sheds on the wharves, and the price of a load depended on how dry it was.[^33][^29]

**Stowing and sealing.** Stevedores lowered the blocks through the hatch in slings and stacked them as in the icehouses: on edge, tight, each layer across the one below. Ice chips and sawdust were pushed into every gap, and the mate signed for the cargo.[^35][^29] The ice was stowed low and spread evenly from bow to stern. Ships usually carried less ice than their rated tonnage because of the weight and space of the lining.[^32][^36] Timber battens were driven between the stack and the lining, and the top layers were wedged against the deck beams so that the cargo could not shift.[^36] On top went a thick layer of sawdust and then hay. The hatches were closed, covered with tarred canvas, battened down, and barred. Some ships fitted a second inner hatch cover with sawdust between the two.[^32][^36]

The hatches stayed sealed until port. Some masters sealed the joins with wax or pitch so that any tampering would show. A master who opened them at sea without good cause would answer for the lost ice.[^37] Melt water was pumped from the bilge every 4 hours, day and night, and the mate logged the number of strokes. The strokes were a rough measure of how fast the ice was melting, and a sudden rise meant the stow had shifted or the lining had broken.[^36]

Loading was done at night or in the early morning and took one to two days for a ship of middling size. The ship sailed on the next tide if the wind allowed, and masters who waited for return goods were told to stop.[^35][^37] Cargoes grew through the 1840s. Their size was limited less by the ship than by what the far port could sell.[^30][^31] Marine insurers at first refused ice cargoes. Later policies excluded loss from melting, so the shipper bore that risk.[^39][^30]

## The voyage

**Beginnings.** Frederic Tudor sent his first cargo from Boston to Martinique in 1806. There was no ice house there, and most of the ice melted on the wharf.[^38][^28] He lost money on that voyage and on several that followed, and he spent time in a debtors' prison in the 1810s. By the 1820s he was shipping regularly to Havana and to southern US ports.[^38][^28]

**Routes and times.** Ships to Havana, Martinique, Jamaica, and the other islands took two to three weeks with fair winds. Havana became one of the steadiest markets, with ships arriving every few weeks.[^42][^43] The southern US ports were the largest market by volume: Charleston, Savannah, Mobile, and above all New Orleans, which by the 1850s took more New England ice than any other port. The voyage to New Orleans took several weeks.[^44][^30] Ice also went to Rio de Janeiro, Valparaíso, Bombay, Madras, Hong Kong and other Chinese ports, and a few cargoes went to Australia. Some of these routes were given up after a few years.[^30][^45]

The longest regular route ran from Boston to Calcutta. It went south through the Atlantic, round the Cape of Good Hope, and north across the Indian Ocean to the Hooghly River, crossing the equator twice, and took about 130 days.[^41][^36] The first Calcutta cargo sailed on the *Tuscany* in May 1833 and arrived that September. The arrival caused a sensation, the voyage made a profit, and regular sailings followed.[^46][^41] Calcutta sailings were timed to arrive in the hot season, from about March to June. Ships therefore left Boston in autumn and early winter and spent their first weeks in cold northern waters.[^41][^30] Ships bound for Calcutta sometimes called at Cape Town or Mauritius and sold some ice there. Masters were told to reseal the hatches within the hour.[^37][^45] From the 1840s many ice ships were towed up the Hooghly by steam tugs, which cut the passage to a day or less.[^49][^31]

The firms paid more to charter fast ships for India, because fewer days in the tropics meant less melting. They chose the same few masters for the Indian run year after year.[^41] On short routes the cheapest ship was usually chosen.[^41]

**How much melted.** Most of the melting happened in the tropics. Logbooks show the pumping strokes low in the first weeks, rising sharply near the equator, and staying high. On the Calcutta route the second crossing of the tropics was the worst.[^36] A study compared the weight of ice signed for in Boston with the weight unloaded in Calcutta for every voyage where both papers survive. On average the ships lost 38 percent of their ice, and the loss varied widely with the season, the length of the voyage, and the stow.[^47] On the Caribbean and southern routes a well-stowed cargo often lost under a tenth of its ice. One firm's papers show the Caribbean trade paying for losses on the Indian trade in more than one year.[^30][^15] A ship becalmed in the doldrums could drift for days or weeks while the ice melted. Masters were told to keep moving and to avoid known calm zones.[^36][^37]

Masters kept a separate printed "ice book" with columns for the date, the ship's position, the air temperature on deck, the sea temperature, and the pumping strokes. The books went back to Boston and are the main source for the logbook study. Some masters filled them in daily, while others left gaps of a week or more.[^36][^37]

**Return cargoes.** Ships came back from Calcutta with jute, linen, indigo, saltpetre, and spices, and from the Caribbean with sugar, molasses, and coffee.[^30][^29] Some historians argue, in a peer-reviewed economic history article, that the Calcutta ice voyage made sense to shipowners mainly because it put a ship in Calcutta to collect a valuable return cargo.[^30]

## Ice houses at the far ports

**The first rule.** After Martinique, the trade built the ice house before the ice arrived. From the 1810s the firms built or rented a house in each port before sending regular cargoes. Some were converted warehouses with extra walls added inside, and the firms sent carpenters from Boston with the first cargo to a new port.[^38][^28]

**How they were built and what they held.** The Calcutta ice house was paid for by a subscription among the city's merchants after the 1833 cargo and opened a few years later. It was a round brick building near the river with thick walls and a domed roof. When full it held about 1,250 tons, and the round shape gave the smallest wall surface for the space inside.[^50][^51] It had an inner and an outer wall with packed fill, at first brought from Boston and later local. It was built of brick because termites and monsoon damp destroyed wood. Its floor drained to the river, and the dome stood over a ventilated space.[^50][^52]

In Havana the houses were partly sunk into the ground, where the earth stayed cooler. In low, wet New Orleans the houses had to stand fully above ground.[^53][^52] Havana's house was built by the Tudor firm near the harbour in the 1820s, after the Spanish colonial government granted the firm a monopoly. In return the firm promised to keep the city supplied and could be fined for running out.[^54][^31] By the 1840s New Orleans had several large ice houses on the levee, owned by competing firms and standing beside the wharves.[^44][^55] Houses on the Calcutta model were built in Bombay and Madras in the late 1830s and early 1840s. Neither was as large as Calcutta's. The Madras house stood near the beach because ice was landed through the surf in small boats.[^52][^56] Charleston and Savannah had smaller wooden houses on the Boston plan, raised on brick piers. They held enough ice for a few weeks of local sales.[^57][^44] Hong Kong got a granite ice house on the waterfront in the 1840s.[^59]

**Who ran them.** The Calcutta house was run by an agent sent out from Boston with a staff of local workers. The agent also answered to the merchants' committee that had paid for the building.[^31][^50] In Havana the house was run through the 1840s by Joaquín Barcia, a local merchant who was the firm's agent there.[^58] Agents were usually paid a share of the sales, which led to quarrels with Boston when a poor cargo cut sales. Some agents were local merchants and others were young men sent out from Boston.[^31] Some ports had no firm-run house. The smaller southern houses were often owned by local merchants who bought whole cargoes from the Boston firms.[^57][^44]

**How the ice was sold.** The houses opened only from first light to the middle of the morning, and customers or their servants queued with baskets. In Calcutta the hours were printed in the newspapers, and latecomers were turned away.[^50][^60] Ice was sold by weight on a scale at the door. Some houses kept blocks of standard weights ready inside.[^44][^60] Barcia sold by ticket: a customer bought a ticket for a set weight at the city office and exchanged it at the ice house door. No money changed hands at the door, so it could be opened and shut quickly.[^58] Hotels, clubs, hospitals, and military messes had accounts billed monthly and were often served before the queue, which led to complaints in the newspapers.[^60][^31] In New Orleans by the 1850s, carts with insulated boxes delivered to standing orders each morning. Delivery was rare in Havana and Calcutta.[^44]

Customers carried ice home wrapped in blankets or flannel, and at home it lasted a day or so. Wealthier households had ice chests shipped from Boston.[^61][^50] In ports where ice was new, agents gave it away at first and showed bar owners, cooks, and doctors how to use it. Tudor's diary records free ice in Havana and Charleston until the habit took hold.[^38][^62] Agents' letters report losses in the far-port houses that ran higher, month for month, than any loss recorded at the ponds. The agents tried to sell each cargo before the next one arrived.[^31]

## The workers

**Who did the work.** In the early years most of the men on the ice were local farmers and their sons, working in the slack season. They brought their own horses and were paid for the horse as well as the man.[^63][^1] From the 1840s a growing share were Irish immigrants. They were hired in large numbers for the unskilled jobs, while the skilled jobs often stayed with local men, and some lived through the winter in shanties near the ponds.[^64][^65] In later decades French-Canadian labourers came south, some from the New England mill towns and some from Quebec for the season. By the 1870s some crews on the larger ponds were mostly French-Canadian.[^66] When local labour ran short, agents hired men off the street in Boston and paid their train fares to the ponds.[^64] Boys worked on the ice from about the age of twelve, for less pay.[^6][^63] Women did not work on the ice. They ran boarding houses, cooked for the shanties, and washed the crews' wet clothing, and the firms' accounts usually paid them under the household's name.[^63][^15]

**How the crews were organised.** On the largest ponds a crew numbered about 75 men, divided into gangs in sequence. There were gangs for snow scraping, marker and plough, the breaking bars, the channel, the elevator, and stacking. The foreman moved men between gangs to keep the blocks moving, and a smaller pond might use a third as many men.[^67] Each crew had a foreman who answered to the firm's superintendent for the pond. He decided when and where to cut and whom to hire. Several foremen stayed with one firm for twenty years or more.[^3]

Labourers were hired by the day at the edge of the pond, with no promise of work the next day.[^6] The skilled men were the marker drivers, stackers, and bar men. They were hired for the season, paid more, and written to before each season to ask them back.[^3][^63] Pay came every Saturday evening at the shore shanty, with board deducted.[^15] Newspapers reported fights between local men and Irish labourers in years when work was short, and foremen sometimes kept the groups in separate gangs.[^65][^68] In the 1850s and 1860s crews sometimes struck when a thaw was forecast. The strikes lasted a day or two and ended when the firms agreed. Afterwards the firms hired outside men and kept lists of strikers.[^71][^64]

The ship loaders were a separate, year-round waterfront workforce. They worked in gangs under a boss who contracted with the ice firms for each ship and were paid by the ton loaded.[^35] At the far ports, Calcutta porters hired by the agent carried the blocks at night. In Havana, colonial records show the firm's depot hiring enslaved men from their owners to unload the ships.[^70][^31]

**Conditions and dangers.** The day ran from first light to dark. In busy seasons the elevators and stackers worked into the night by lantern light and on Sundays, and a long day paid no more unless the foreman agreed.[^13] The men stood on the ice all day below freezing, often in wind, and frostbite was common. They wore layers of wool, felt boots with leather overshoes, and iron "creepers" strapped on to grip the ice. A man who got wet could freeze before reaching shelter, so anyone who fell in was sent straight to the shanty fire.[^6][^69] On the larger ponds the firms kept coffee and soup hot in a shore shanty and gave a hot midday meal.[^6]

Men slipped, cut themselves on saws and bars, and were crushed by blocks on the elevator or in shifting stacks. A block falling from the top of the elevator could kill a man, and the firms paid an injured man nothing beyond the days he had worked.[^69][^6] The worst danger was falling through into the channel or the thin new ice that formed over it at night. A count of newspaper reports recorded nine drownings among harvest crews on the Cambridge ponds between 1850 and 1860, most of them at night. The firms put up no railings or lights along the channel until late in the trade.[^69][^13] An open winter meant no harvest and no winter wage. In the winters after an open season, Boston charities reported more families seeking help.[^72]

## Buyers and prices

**Who bought the ice.** In Calcutta the first buyers were British residents, including East India Company officials, army officers, and merchants. Wealthy Indian merchant and landowning families also bought ice from the early years. For most of the city's people, ice was far too costly.[^50][^61] Newspaper reports from the 1830s say some Indian households doubted at first that ice handled by foreign sailors and porters was clean. By the 1840s, Indian buyers were a large share of the private customers.[^60] Clubs and officers' messes served iced drinks through the hot season, and the clubs' records show ice as one of their largest regular costs.[^61] In every hot port, hospitals were among the most important buyers, using ice for fevers, heatstroke, and wounds. In Calcutta they were among the largest account customers and received a reduced rate in return for a daily contract.[^73][^60]

In Havana the main buyers were cafés, confectioners making ice creams and sorbets, and wealthy households. Within a generation, ice there went from a luxury of the rich to a common pleasure in the cafés.[^54][^62] New Orleans used ice on a scale no other port matched. Bars, hotels, households, the meat and fish markets, and the river steamboats all bought it, and by the 1850s the local press described ice as a necessity.[^44][^74] Some steamboats sold ice in the river towns, carrying the habit inland.[^74][^77] In Charleston and Savannah, planters, merchants, hotels, and taverns bought ice.[^57] In Madras and Bombay the buyers were much the same as in Calcutta, and included Parsi merchant families.[^56][^75] In Hong Kong the buyers were the garrison, the trading houses, and ships in the harbour, and notices show months with no ice in the colony.[^59]

**What it cost.** In Calcutta in the 1830s and 1840s, ice sold at the door for 3 annas a pound, an anna being a sixteenth of a rupee. The price held steady for most of those years, and account customers sometimes paid less.[^60][^30] Prices in Madras and Bombay were above those in Calcutta.[^56][^75] In Havana the monopoly carried a maximum price that the government revised several times, so the firm could not raise prices in the hottest weeks.[^54] New Orleans prices fell steadily from the 1830s to the 1850s as competing firms arrived.[^44][^30] By 1860 the city's weekly "price current" gave about 2½ cents a pound at the levee houses. That put ice within reach of ordinary working households for at least part of the year.[^76]

In every far port, prices were lowest just after a ship arrived and highest when the next ship was overdue. When a house ran dry, ice could not be had at any price.[^60][^43] At small ports with no ice house, ice sold straight from the hold went for whatever buyers would pay.[^37] In ports where Boston firms competed, price wars gave buyers periods of cheap ice that ended suddenly.[^31][^30] At the pond, the ice itself cost almost nothing. On the long routes, the ice lost in transit and storage was the largest single cost, larger than carriage.[^30] Tudor became one of the richest men in Boston by the 1840s and was known as the "Ice King." His profits came mostly from the southern and Caribbean markets.[^38][^28]

## The end of the trade

**What ended it.** The sea trade peaked around 1860 and was nearly over by the 1880s. Historians point to several causes that came together: war, ice-making machines, steamships, and the growth of the home market.[^30][^78] During the Civil War the Union blockade closed New Orleans to Boston ships until the city fell in 1862, and the Confederacy went without shipped ice for most of the war.[^79][^44] Some Carré ammonia ice machines came in through the blockade.[^82] After the war, the firms found their ice houses damaged or sold and their agents gone. Cargoes to the southern ports in the late 1860s were well below the levels of the late 1850s.[^79][^30]

Ice machines dated from before the war. John Gorrie patented one in 1851, Ferdinand Carré developed an ammonia machine in the late 1850s, and James Harrison built machines in Australia in the 1850s.[^80][^81] New Orleans got its first ice factory in 1868, making about 12 tons a day at first.[^83][^44] Through the 1870s, factory ice became cheaper than shipped ice once melting losses were counted.[^30] Early machine ice was cloudy and buyers distrusted it, which slowed the switch in some ports until factories learned to make clear ice by the 1880s.[^80][^84] Some Boston firms cut prices to drive out the factories, and a few small ones closed in the 1870s, but the tactic could not last.[^44] Ice factories opened in Calcutta in the late 1870s, and the Calcutta ice house lost its trade within a few years.[^85][^50] In Havana the monopoly was not renewed after the American war and factories opened in the 1870s.[^54][^89]

Steamships took over the routes to Asia, especially after the Suez Canal opened in 1869, and the supply of cheap sailing ships for the outward voyage shrank.[^41][^30] At home, demand for natural ice from households, breweries, meat packers, and refrigerated railway cars grew fast. Many firms turned to this home market.[^16][^78] The ponds near Boston were fouled as the city grew. Fresh Pond became a water supply and its harvest was stopped.[^86][^78] Tudor died in 1864, and other firms merged into larger companies that dealt mostly in the home market.[^87][^28] The harvest crews kept cutting for the home market, and the ice stevedores went back to general cargo.[^88]

**When the last cargoes sailed.** The Indian trade dwindled through the 1870s, and in some years only one or two ships went. The Bombay and Madras trade ended before Calcutta's.[^90][^30] The last recorded cargo of New England ice to Calcutta sailed from Boston in 1882 aboard the bark *Margaret Ellery*. No later ice ship appears in the Calcutta register.[^92] The Boston papers printed no reports of the last ships.[^91] Natural ice from the home trade lasted until the 1920s and 1930s, and the last commercial harvests on many New England ponds came in the 1930s and 1940s.[^78][^6]

## Disagreement / Uncertainty

- **Loss in storage.** The 1847 ledger gives about 17 percent for one Fresh Pond house over a season.[^23] A general history says a well-built house lost between a fifth and a third over a summer and small houses sometimes half, but it gives no source.[^28] Ledgers that counted blocks show smaller losses than ledgers that weighed them, and historians warn that figures from the two methods cannot be compared.[^26][^18]
- **Loss on the Calcutta run.** The logbook study gives an average of 38 percent.[^47] A general history says well-stowed ships lost about a quarter and blames higher losses on poor stowing, but gives no source.[^28] The two figures may describe different periods, but neither source says which years it covers.[^28] The study's authors note that the voyages whose papers survive may have been the better-run ones.[^47] The figure of under a tenth for the short routes is an estimate from a small number of voyages.[^30]
- **When the trade ended.** Some histories put the end in the early 1880s. A general history says cargoes to the Caribbean continued irregularly into the 1890s, and that small shipments to southern ports went on into the early twentieth century.[^28][^78] The difference may come from whether a writer counts only the long Asian voyages or any ice sent by sea from New England.[^28][^78]
- **The end of the Havana monopoly.** The colonial records end before the monopoly's last years. The account of its end comes from a later research project.[^54][^89]
- **Machines through the blockade.** The number of Carré machines brought through is not known.[^82]

## Useful Details

- In the trade's early years, sailors on the Boston waterfront believed melting ice would sink a ship. Tudor wrote that he had trouble finding crews. By the 1840s, sailors who had made several ice voyages were valued for knowing the pumping routine.[^38][^28] Insurance records show ice ships lost at sea in about the same numbers as other ships on the same routes.[^39]
- Apples, butter, and cheese were stowed in pockets cut into the ice stack, usually as the private trade of the master or agent. Agents' letters say the apples arrived in Calcutta and Havana in better condition than a month in a Boston cellar would have left them.[^31][^40]
- News of a Calcutta voyage could take most of a year to reach Boston. Some letters later went by the faster overland route through Egypt.[^31][^48]
- Icehouses burned. Dry sawdust and hay caught easily, sometimes from a passing railway engine's spark. The ice usually survived standing in the ruins but melted within days.[^27][^18]
- The Madras ice house was later a home and then a school, and it now stands on the seafront as a museum. The Calcutta house was pulled down in the late nineteenth century, and the Havana house has not been traced.[^56][^50] The Tudor firm's papers are the largest single source on how the trade worked.[^87]
- Historians argue, in peer-reviewed food and economic history articles, that the New England firms created the demand that later ice factories supplied.[^62][^30]
- The "icebox" and the "iceman" belong more to the later home trade than to the sea trade, but they grew out of the habit of using ice that the sea trade helped to spread.[^84]

## Open Research Questions

- How much ice did the far-port houses in Havana, New Orleans, Bombay, and Madras hold?
- What maximum prices did the Havana monopoly set, and what did ice cost in Madras and Bombay?
- What daily wages did harvest labourers and the skilled men earn?
- How large were losses in the far-port ice houses, as figures?
- When did the last cargoes sail to Havana and to the southern US ports?

## Reliability / Limitations

- `Regional industry history site (pond rights)`[^2]: cites no archive for the pond-rights figures.
- `Agricultural magazine, February 1856`[^5]: gives advice to farmers, not an account of a single harvest. The rope method for rescuing horses rests on this piece and oral histories, with no count of how often it worked.
- `Oral history collection, transcribed 1974`[^6]: recorded from people who worked the last commercial harvests, long after the shipping trade ended. It may not describe the early trade.
- `Tudor papers, pond accounts`[^15]: the 200-pound block weight is the firm's own working figure, not a measured average.
- `Local historical society article on icehouses`[^17]: the size of the Fresh Pond house comes from a company prospectus.
- `Agricultural magazine, June 1859`[^21]: written for farmers, not for the shipping firms.
- `Newspaper, August 1868 (icehouse fire)`[^27]: covers one fire. The industry history site gives no count of fires.
- `Book excerpt on a publisher's site`[^28]: gives its storage-loss figures, its Calcutta-loss figure, and its later-shipments claim without a source.
- `Tudor papers, agents' letters`[^31]: the fish-tasting cargo story comes from one letter. The letters describe the firm's tactics from its own side and report far-port losses only in general terms.
- `Digitized logbook collection`[^36]: the comment on ships rolling more comes from masters' remarks, not measurement.
- `Tudor papers, diary excerpts`[^38]: record Tudor's own view of his difficulties.
- `Peer-reviewed article on ice shipping costs`[^30]: the short-route loss figure is an estimate from a small number of voyages.
- `Calcutta melt study`[^47]: the voyages whose papers survive may be the better-run ones.
- `Peer-reviewed architecture article`[^52]: compares ports and gives the Havana design as a contrast to Calcutta.
- `Hong Kong heritage society page`[^59]: relies on newspaper notices and gives no building records.
- `Digitized memoir collection`[^61]: written by British residents describing their own households.
- `Calcutta newspaper notices`[^60]: British newspapers writing about Indian customers.
- `Newspaper, January 1851 (disturbance on the ice)`[^68]: short reports that give one side.
- `Havana dock labour contracts`[^70]: employers' records. No account by the workers survives in these collections.
- `Newspaper, February 1866 (ice strike)`[^71]: takes the firms' side.
- `Labour history page on conditions`[^69]: the drowning count comes from newspaper reports, which may have missed some deaths.
- `University project page on Carré machines`[^82]: the number of machines brought through the blockade is not known.
- `Business history society page on New Orleans`[^44]: gives no list of the factories that closed.
- `Havana colonial monopoly records`[^54]: end before the monopoly's last years. The later account comes from a research project.

## Sources

[^1]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview
[^2]: https://www.new-england-industry.example/ice/pond-rights
[^3]: https://www.harvard-business-archive.example/tudor-papers/harvest-instructions
[^4]: https://www.new-england-industry.example/ice/snow-and-flooding
[^5]: https://www.farm-journal-archive.example/1856/february/ice-for-market
[^6]: https://www.walden-region-history.example/oral-histories/ice-crews
[^7]: https://www.mit-tech-history.example/inventors/wyeth-ice-tools
[^8]: https://www.patent-records.example/1829/wyeth-ice-cutting-apparatus
[^9]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s
[^10]: https://www.new-england-industry.example/ice/breaking-and-floating
[^11]: https://www.steam-power-history.example/small-engines/ice-elevators
[^12]: https://www.boston-markets-history.example/ice/local-trade
[^13]: https://www.boston-newspaper-archive.example/1858/january/ice-crop
[^14]: https://www.new-england-industry.example/ice/open-winters
[^15]: https://www.harvard-business-archive.example/tudor-papers/pond-accounts
[^16]: https://www.hudson-valley-museum.example/collections/ice-tool-catalogues
[^17]: https://www.cambridge-historical.example/fresh-pond/icehouses
[^18]: https://www.new-england-industry.example/ice/storage-history
[^19]: https://www.harvard-business-archive.example/tudor-papers/storage-trials
[^20]: https://www.massachusetts-engravings.example/prints/fresh-pond-ice-works-1852
[^21]: https://www.farm-journal-archive.example/1859/june/building-an-ice-house
[^22]: https://www.harvard-business-archive.example/tudor-papers/keepers-letters
[^23]: https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage
[^24]: https://www.railroad-history-ma.example/branches/charlestown-ice-line
[^25]: https://www.boston-harbour-history.example/wharves/charlestown-ice-houses
[^26]: https://www.ma-archives.example/ice-ledgers/methods-note
[^27]: https://www.boston-newspaper-archive.example/1868/august/icehouse-fire
[^28]: https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt
[^29]: https://www.maritime-boston.example/trade/outward-cargoes
[^30]: https://www.economic-history-review.example/2010/ice-shipping-costs
[^31]: https://www.harvard-business-archive.example/tudor-papers/agents-letters
[^32]: https://www.maritime-salem.example/papers/ship-fittings-for-ice
[^33]: https://www.maine-lumber-history.example/mills/sawdust-trade
[^34]: https://www.maritime-salem.example/papers/stowing-ice-1850
[^35]: https://www.boston-harbour-history.example/wharves/stevedores
[^36]: https://www.sailing-ship-logs.example/collections/ice-voyages
[^37]: https://www.harvard-business-archive.example/tudor-papers/masters-instructions
[^38]: https://www.harvard-business-archive.example/tudor-papers/diary-excerpts
[^39]: https://www.insurance-history.example/marine/perishable-cargoes
[^40]: https://www.food-history-quarterly.example/2014/new-england-apples-abroad
[^41]: https://www.maritime-boston.example/routes/boston-calcutta
[^42]: https://www.maritime-boston.example/routes/caribbean
[^43]: https://www.havana-archive.example/colonial-trade/shipping-arrivals
[^44]: https://www.gulf-commerce.example/ports/new-orleans-ice-imports
[^45]: https://www.maritime-boston.example/routes/other-ports
[^46]: https://www.calcutta-history-society.example/1833/first-ice-ship
[^47]: https://www.ice-trade-voyages.example/logs/calcutta-melt-study
[^48]: https://www.postal-history-review.example/2009/overland-mail-to-india
[^49]: https://www.calcutta-history-society.example/port/hooghly-pilots-and-tugs
[^50]: https://www.calcutta-history-society.example/buildings/the-ice-house
[^51]: https://www.british-library-images.example/calcutta/ice-house-1840s
[^52]: https://www.colonial-architecture-journal.example/2016/cold-storage-in-bengal
[^53]: https://www.havana-archive.example/colonial-trade/building-permits
[^54]: https://www.havana-archive.example/colonial-trade/ice-monopoly
[^55]: https://www.louisiana-archives.example/levee/warehouse-registers
[^56]: https://www.madras-heritage.example/beach-road/ice-house
[^57]: https://www.lowcountry-history.example/charleston/ice-trade
[^58]: https://www.havana-archive.example/colonial-trade/ice-depot-1840s
[^59]: https://www.hongkong-heritage.example/waterfront/early-ice-house
[^60]: https://www.calcutta-gazette-archive.example/notices/ice-house-hours
[^61]: https://www.memoirs-of-empire.example/collections/calcutta-domestic-life
[^62]: https://www.food-history-quarterly.example/2012/ice-cream-in-the-tropics
[^63]: https://www.labor-history-ne.example/winter-work/farm-families
[^64]: https://www.labor-history-ne.example/winter-work/irish-labour
[^65]: https://www.immigration-history-journal.example/2012/boston-irish-winter-work
[^66]: https://www.immigration-history-journal.example/2015/french-canadians-in-new-england
[^67]: https://www.labor-history-ne.example/winter-work/harvest-crew-sizes
[^68]: https://www.boston-newspaper-archive.example/1851/january/disturbance-on-the-ice
[^69]: https://www.labor-history-ne.example/winter-work/ice-crews-conditions
[^70]: https://www.havana-archive.example/colonial-trade/dock-labour-contracts
[^71]: https://www.boston-newspaper-archive.example/1866/february/ice-strike
[^72]: https://www.boston-newspaper-archive.example/1880/march/open-winter-hardship
[^73]: https://www.medical-history-journal.example/2013/ice-in-tropical-medicine
[^74]: https://www.louisiana-archives.example/newspapers/daily-ice-reports
[^75]: https://www.bombay-gazette-archive.example/notices/ice-sales
[^76]: https://www.gulf-commerce.example/price-current/ice-1860
[^77]: https://www.river-history-review.example/2011/steamboat-provisioning
[^78]: https://www.new-england-industry.example/ice/decline
[^79]: https://www.civil-war-commerce.example/blockade/ice-shortage
[^80]: https://www.mit-tech-history.example/inventors/early-refrigeration
[^81]: https://www.patent-records.example/1851/gorrie-ice-machine
[^82]: https://www.civil-war-commerce.example/blockade/carre-machines
[^83]: https://www.louisiana-archives.example/business/ice-manufacturing-charters
[^84]: https://www.food-history-quarterly.example/2016/clear-ice-and-cloudy-ice
[^85]: https://www.calcutta-history-society.example/industry/bengal-ice-factory
[^86]: https://www.cambridge-historical.example/fresh-pond/water-supply
[^87]: https://www.harvard-business-archive.example/tudor-papers/finding-aid-overview
[^88]: https://www.labor-history-ne.example/winter-work/after-the-sea-trade
[^89]: https://www.cuba-commerce-history.example/1870s/manufactures
[^90]: https://www.ice-trade-voyages.example/registers/calcutta-arrivals
[^91]: https://www.boston-newspaper-archive.example/1880s/ice-coverage-survey
[^92]: https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882
````

Final reply:

````
```json
{ "note": "Research/research-light-ice-trade.md", "cut_short_topics": [] }
```
````

#### Run 3

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-09'
PASS  fm-modified-run-date  found 'modified: 2026-10-09'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-footnotes-resolve   **Markers to definitions:** Every marker in the body has a matching definition under Sources. The numbers run from [^1] to [^92] with no [^51]. There is no [^51] marker in the body and no [^51] definition, so the gap breaks nothing.  **Definitions have URLs:** Every definition line holds a URL. For example: - "[^1]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview" - "[^50
PASS  judge-planted-details-cite-own-url   All eight details appear in the note, and each carries a footnote whose URL under Sources matches the given URL.  1. **Topic 1 (22-inch blocks):** "cut a grid that produced blocks 22 inches square on the surface.[^9]" (also in the Summary: "laid out 22 inches square on the surface.[^9]")    - `[^9]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s` matches. 2. **Topic 2 (17 pe
PASS  judge-reply-no-cut-short   The reply names no topic as cut short: `"cut_short_topics": []`. The list is empty. It only identifies the note path, `"Research/research-light-ice-trade.md"`, and doesn't call any file incomplete or say it was missing its closing line.
PASS  judge-sixteen-questions-answered   All sixteen questions are answered with the findings' answers. None is answered only in general terms, and none is wrongly listed as open.  1. **Ice readiness.** "usually from the middle of January into February, once a long hard freeze had set in"; "Ice was not cut until it was at least 14 inches thick"; "Each morning a foreman walked the pond with a hand auger and bored test holes." 2. **Tools 
PASS  keeps-t1-14-inches  found '14 inch'
PASS  keeps-t1-22-inch-blocks  found '22 inch'
PASS  keeps-t2-17-percent-loss  found '17 percent'
PASS  keeps-t2-9400-tons  found '9,400'
PASS  keeps-t3-pumped-every-4-hours  found '4 hours'
PASS  keeps-t3-sawdust-1-to-11  found '11 tons'
PASS  keeps-t4-130-days  found '130 days'
PASS  keeps-t4-38-percent-loss  found '38 percent'
PASS  keeps-t5-1250-tons  found '1,250'
PASS  keeps-t5-barcia  found 'Barcia'
PASS  keeps-t6-75-men  found '75'
PASS  keeps-t6-nine-drownings  found 'nine drown'
PASS  keeps-t7-2-half-cents  found '2½'
PASS  keeps-t7-3-annas  found '3 annas'
PASS  keeps-t8-12-tons-a-day  found '12 tons'
PASS  keeps-t8-margaret-ellery  found 'Margaret Ellery'
PASS  keeps-url-topic-1  found 'https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s'
PASS  keeps-url-topic-2  found 'https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage'
PASS  keeps-url-topic-3  found 'https://www.maritime-salem.example/papers/stowing-ice-1850'
PASS  keeps-url-topic-4  found 'https://www.ice-trade-voyages.example/logs/calcutta-melt-study'
PASS  keeps-url-topic-5  found 'https://www.havana-archive.example/colonial-trade/ice-depot-1840s'
PASS  keeps-url-topic-6  found 'https://www.labor-history-ne.example/winter-work/harvest-crew-sizes'
PASS  keeps-url-topic-7  found 'https://www.gulf-commerce.example/price-current/ice-1860'
PASS  keeps-url-topic-8  found 'https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## Cut'
PASS  shape-topic-2-section  found '## Stor'
PASS  shape-topic-3-section  found '## Load'
PASS  shape-topic-4-section  found '## The voyage'
PASS  shape-topic-5-section  found '## Ice houses at the far port'
PASS  shape-topic-6-section  found '## The worker'
PASS  shape-topic-7-section  found '## Buyers and price'
PASS  shape-topic-8-section  found '## The end'
PASS  file-name  expected name written
````

`project/Research/research-light-ice-trade.md`:

````markdown
---
title: Light Research - Ice Trade
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-09
modified: 2026-10-09
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Topics: cutting the ice on the ponds; storing the ice before shipping; loading the ship; the voyage; ice houses at the far ports; the workers; buyers and prices; the end of the trade. Limit for every topic: New England ice shipped by sea, from the trade's start to its end.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Ice Trade

## Summary

The sea trade in New England ice began with a failure: Frederic Tudor's first cargo, sent from Boston to Martinique in 1806, mostly melted on the wharf because there was no ice house to keep it in.[^38] The trade grew through the 1840s and 1850s, peaked around 1860, and was nearly over by the 1880s.[^30]

Ice was cut in the coldest weeks of winter, usually mid-January into February.[^1] It was not cut until the clear ice was at least 14 inches thick.[^1] From the late 1820s, horse-drawn tools based on Nathaniel Wyeth's designs cut the ice into regular blocks.[^7] These were laid out 22 inches square on the surface.[^9] The blocks were stored in double-walled, sawdust-filled icehouses on the pond shores. The largest, on Fresh Pond, held about 9,400 tons.[^17] One surviving ledger shows a house losing about 17 percent of its ice over the 1847 season.[^23]

Ships were lined inside the hold like an icehouse. They were packed with one ton of sawdust for every 11 tons of ice.[^34] Once sealed, the hatches stayed shut until port,[^37] and the bilge was pumped every 4 hours.[^36] The longest regular voyage, Boston to Calcutta, took about 130 days.[^41] A logbook study found an average loss of 38 percent of the ice on that route.[^47] Voyages to the Caribbean took two to three weeks,[^42] and well-stowed cargoes on the short routes often lost under a tenth.[^30] New Orleans took more New England ice than any other port by the 1850s.[^44]

At the far ports the ice went into purpose-built ice houses. Calcutta's was a round brick building holding about 1,250 tons.[^50] The ice was sold by weight in the early morning.[^60] Calcutta ice cost 3 annas a pound in the 1830s and 1840s.[^60] New Orleans ice sold for about 2½ cents a pound by 1860.[^76]

The pond crews were at first local farmers.[^63] From the 1840s more of them were Irish immigrants,[^64] and in later decades French-Canadians.[^66] On the largest ponds a crew numbered about 75 men.[^67]

No single cause ended the trade. Historians point to the Civil War, ice-making machines, steamships, and the growth of the home market for natural ice.[^30] The last recorded cargo to Calcutta sailed in 1882 aboard the bark Margaret Ellery.[^92]

## Cutting the ice on the ponds

### When the ice was ready

The harvest ran in the coldest weeks of the year, usually from the middle of January into February, once a long hard freeze had set in.[^1] The shipping firms preferred spring-fed ponds with no streams running in. Moving water froze unevenly and carried silt, leaves, and sawdust from upstream mills into the ice.[^2] Fresh Pond in Cambridge, Wenham Lake north of Salem, and Spy Pond in Arlington were the best known. The firms bought or leased the shore rights so that no rival could cut there.[^2] A pond owner could earn more from one winter's ice rights than from a year of farming the land around it.[^2] Buyers in hot ports judged ice by its clarity, and they took cloudy ice as a sign of dirty water even when it was not.[^1] Foremen kept daily notebooks through the season, recording the air temperature at dawn and noon, the wind, and any snowfall.[^1]

Ice was not cut until it was at least 14 inches thick. Thinner ice crumbled at the corners when handled and wasted space in the hold. It also melted faster, because a thin block has more surface for its weight.[^1] Each morning a foreman walked the pond with a hand auger and bored test holes at set points. He measured the depth of clear ice separately from any white snow ice on top, and only the clear ice counted.[^3] If the readings fell short, the crew was sent to clear snow or stood idle.[^3] Some firms paid a small bonus to the foreman whose pond reached cutting thickness first.[^3] One part of a pond could reach thickness days before another, so cutting often began near the shaded shore and moved outward.[^1]

Snow was the harvest's main enemy. It slowed the freezing underneath like a blanket. Wet snow that froze on top became "snow ice," which was white, full of air, and weak.[^4] Crews cleared snow with horse-drawn scrapers, wide wooden boards dragged across the surface.[^4] On some ponds the crews bored holes and let water flood the cleared surface so a fresh layer froze on top. This worked only in hard cold, because slow-freezing layers turned cloudy.[^5] Snowfall in the middle of a harvest could stop all work for several days.[^4]

Foremen also tested clarity. A small block was cut, carried to shore, and held up against the light. If a dark object showed clearly through its whole thickness, the ice was good enough for shipping. If the test block was cloudy, cutting moved to a stiller part of the pond, often further from the inlet or the shore. The test was repeated every few days.[^6]

The weather could ruin a harvest. A thaw or rain softened the ice and flooded the grooves, and the field often had to be planed and cut again.[^14] A mild winter, which the trade called an "open winter," left ponds too thin to cut. The shippers then bought ice from ponds further north, in Maine and New Hampshire, at higher cost.[^14] In a good season a large pond could be cleared in two to three weeks.[^13] Newspaper reports describe crews cutting on Sundays when a thaw was forecast, against local custom.[^13] Several firms kept icehouses on two or more ponds so that one bad pond would not cost them the whole year.[^14]

### Tools and block size

Before the 1820s ice was cut by hand with axes, hand saws, and chisels. The uneven blocks were hard to stack, and the gaps between them let in warm air.[^7] Nathaniel Jarvis Wyeth was a Cambridge hotel manager who later worked for the Tudor ice company. He designed a horse-drawn cutter in 1825 and patented an improved version in 1829.[^8] His tools made blocks of one regular size, which stacked tightly with little air between them.[^7] Historians describe the shift to horse tools as the change that made long voyages possible, because regular blocks lost less ice to melting.[^7] By the 1840s most commercial ponds in Massachusetts used some version of Wyeth's tools.[^7]

The first tool on the ice was the "marker." It was a plough-like frame with a row of steel teeth, drawn by one horse along a straight line laid out with a cord. A guide arm kept each groove parallel to the last. Once the field was scored one way, the marker was run across at a right angle, which cut a grid that produced blocks 22 inches square on the surface.[^9] The "plough" had longer teeth. It was run along the same grooves until each cut went about two-thirds of the way through the ice. The remaining third held the field together so men and horses could still walk on it.[^9]

Horses were shod with sharp-calked shoes, horseshoes with spikes that gripped the ice. A blacksmith was kept near the larger ponds through the season to reset them.[^6] The marker and plough were designed so the horse walked on uncut ice beside the line being cut.[^5]

The crews then sawed out a channel to the shore with long hand saws. Men with iron "breaking bars," flat chisels on long handles, split the field along the grooves into rafts and then into single blocks.[^10] A skilled bar man could tell from the sound whether the groove had gone deep enough.[^10] Men with pike poles, long wooden poles with an iron hook and spike, moved the floating blocks along the channel to shore.[^10]

At the shore an inclined elevator lifted the blocks into the icehouse. This was a long wooden ramp with an endless chain whose cleats caught each block. At first a horse at a capstan drove it, and from the 1850s the largest houses used small steam engines.[^11] Before each block went up, a man planed the top and bottom flat to remove snow ice and make it sit evenly in the stack.[^1] The elevator could run day and night when the weather held, with lanterns hung along the ramp.[^1]

The clearest blocks were graded first quality and set aside for shipping. Blocks with a cloudy band or trapped leaves were second quality and were usually sold locally, to households and butchers in Boston and nearby towns.[^12] One firm's papers tell foremen to reject any block they would not want to see on a dinner table.[^3]

The harvest was counted in blocks, not weighed. A tally man at the top of the elevator marked each block, and the day's marks were turned into tons using a fixed figure: a first-quality block of the regular size weighed roughly 200 pounds.[^15] Pond owners were usually paid by the ton taken from their water. Some sent their own man to keep a second tally, and disputes over the count survive in letters.[^15]

By the 1850s, firms that specialised in harvest tools sold them as complete sets, many of these makers in the Hudson valley of New York. A set for a large pond included markers, ploughs, hand saws up to six feet long, breaking bars, pike poles, ice tongs, and snow scrapers.[^16] The tools changed little over the life of the trade. A set bought in the 1850s could still be in use thirty years later, with new teeth fitted by a local blacksmith.[^16]

## Storing the ice before shipping

### How the pond icehouses were built

The harvest took a few weeks but the ships sailed all year, so ice was stored for months. The firms built their icehouses on the pond shore, so blocks went straight from the channel up the elevator into storage.[^17] The houses stood above ground. The older farm practice was a pit dug into a hillside, which held only a few tons and let groundwater seep in.[^18] An above-ground house could be built as large as a firm wanted, and it kept the ice away from soil that gave off heat in summer.[^18]

An icehouse had two wooden walls set a little apart, with the space between packed with an insulating fill. Sawdust from the timber mills was the usual fill, and spent tanbark from tanneries was also used. Some houses had three walls with two layers of fill.[^19] In the 1820s and 1830s Frederic Tudor and Nathaniel Wyeth tested fills by building small trial houses and weighing the ice in them at the start and end of summer.[^19] They found dry fill kept ice far better than damp fill, so houses were built with wide eaves to keep rain off the outer wall.[^19]

The biggest icehouse on Fresh Pond held about 9,400 tons when full and was taller than a three-storey building.[^17] It was a row of rooms under one long roof, each filled and emptied on its own, so that opening one room did not let warm air into the rest.[^17] An engraving dated 1852 shows a long, windowless block with a row of doors stacked one above another on the elevator side. The doors at each height were opened as the ice rose inside and boarded shut once the stack passed them.[^20] Smaller firms built houses holding a few hundred tons and sold most of their ice locally.[^17]

The roof was steep, with louvred vents along the ridge to let warm air escape. Most houses were painted white or a light colour to reflect the sun, and some had hay or straw in the roof space.[^18] The floors were built over gravel or broken stone, with a drain running out to the pond, and covered with a thick layer of sawdust. Ice standing in melt water melted much faster than ice standing in air.[^19] One firm's papers record the dismissal of a keeper who let a drain freeze over in early spring, which flooded the lowest room when the weather turned.[^19]

Inside, blocks were set on edge, tight together, with each layer laid across the one below like brickwork. Gaps were filled with ice chips, and a full room was covered with a deep layer of hay or sawdust.[^17] The stackers counted among the most skilled men of the harvest, because a badly laid stack could lean and fall as the lower blocks melted.[^6]

Each large house had a keeper who lived beside it all year, often in a small cottage against the end wall. He checked drains and vents, watched for fire, kept the ledger of ice in and out, and chose which room to open for each order.[^22] Keepers wrote to the Boston office about once a week through the summer.[^22] From the 1850s some keepers hung thermometers above the stack and recorded readings morning and evening beside the outside temperature. A rising reading inside meant an open door or a clogged vent.[^22]

When a ship was ready, ice was taken from the top of the stack down. The blocks had often frozen together and were broken apart with bars. Only one room was opened at a time, and the oldest ice was used first.[^3] The blocks were scraped clean of fill before loading.[^12]

From the early 1840s a railway branch line ran from Fresh Pond to the wharves at Charlestown, on Boston harbour, and cut the journey to under an hour.[^24] Before it, ice went by horse-drawn wagon, and a hot day on the road could cost a wagon a noticeable part of its load.[^24] Railway wagons on the ice line had thick sawdust-packed sides, and in summer the trains ran at night.[^24] The firms also kept smaller wharf icehouses at Charlestown, built on the same plan but holding only a few hundred tons each. Ice was held there only for the few days before a ship sailed, because the harbour air was warmer and damper.[^25]

Fire was a constant risk, because the dry sawdust and hay burned easily. Several large Massachusetts icehouses were lost to fire, often in summer, sometimes from a spark from a passing railway engine.[^18] The ice inside usually survived as a block in the ruins but then melted in the open within days unless it could be loaded at once.[^27]

### How much was lost in storage

The ledgers of one Fresh Pond icehouse for 1847 record the ice put in at the end of the harvest and the weight taken out for each sailing. Between the end of the harvest in March and the last autumn sailing, the house lost about 17 percent of its ice. Most of that loss came in July and August, and the keeper's notes blame the heat and a roof vent left shut.[^23] This is the only surviving record of a whole season's loss for a single house, and historians use it as the standard figure.[^23] The keeper also recorded that a room left unopened until autumn lost less than a room opened for loading in June.[^23]

Large houses lost less than small ones, because a big stack has less surface for its weight.[^18] This is given as the main reason the firms built ever-larger houses through the 1840s and 1850s.[^18] A house with a blocked drain could lose a large part of its bottom layers in a single warm month.[^19]

## Loading the ship

### Ships and holds

The ice went to sea in ordinary merchant ships. Boston merchants brought goods home from the tropics but had little to send out, so many ships left Boston in ballast. Ice gave them a paying outward cargo, and shipowners carried it at low rates.[^29] This cheap carriage was one reason the trade could make money.[^30] Older ships were often chosen, because the ice firms' carpenters built linings into the hold.[^29]

Before loading, the hold was emptied, swept, and aired, because any smell could pass into the ice. One agent wrote that a cargo tasting of fish was sold off at a loss to a butcher. The firms kept a list of ships they would not charter, and they avoided ships that had carried coal.[^31]

A carpenter built a lining inside the hold. This was an inner wall of pine planks set a little in from the hull on all sides, with the space packed with sawdust. It ran across the floor and up under the deck beams, making a box inside the hull on the icehouse plan.[^32] Sailors called it the "ice ceiling." It took a carpenter and two helpers about a week for a ship of middling size.[^32] Rough timber dunnage on the bottom lifted the cargo clear of bilge water. The lining floor and a deep bed of sawdust went on top, with gaps at the sides so melt ran into the bilge for the pumps.[^32] The bottom layer standing in water was the largest single loss on most voyages that kept records.[^32]

### Packing the ice

A Salem merchant's printed paper of 1850 gives the proportion: one ton of sawdust for every 11 tons of ice. Less sawdust cost more ice than it saved, and more took up space that could have carried ice.[^34] The pine sawdust came by schooner from the timber mills of Maine, where it was a waste product.[^34] It had to be dry. Wet sawdust froze into a crust that conducted heat into the ice, so the firms stored it in covered sheds and turned it over in fine weather.[^33] Boston buyers inspected each schooner load by hand and paid according to its dryness.[^33]

Stevedores lowered the blocks through the hatch in slings and stowed them by hand, on edge, tight together, each layer across the one below. Chips and sawdust were pushed into every gap.[^35] A bad stow left air spaces, and the stack then melted from the inside out. The mate watched the stow and signed for the cargo.[^35] Ships usually carried less ice than their rated tonnage because of the weight and space of the lining and sawdust. The ice was stowed low and spread evenly from bow to stern.[^32]

Loading was fast. A middling ship could be loaded in one to two days, with the stevedores working through the night or early morning when the air was coolest.[^35] Firms timed the ice's arrival at the wharf to the hour. Masters were told not to wait for return goods before sailing.[^37]

### Keeping the cargo from melting or shifting

When the stack reached the top of the lining, it was covered with thick sawdust and then hay. The hatches were closed, covered with tarred canvas, and battened down. Some ships fitted a second, inner hatch cover with sawdust between the two.[^32] The aim was to keep the air in the hold as still as possible.[^36]

To stop shifting, stevedores drove timber battens between the stack and the lining and wedged the top layers against the deck beams.[^36] Logbooks record voyages where heavy weather loosened the stack, and each ship arrived with a much smaller cargo. One master wrote that he heard the ice "working" in the hold during a gale and could do nothing about it.[^36]

The crew pumped the bilge every 4 hours, day and night. The mate logged the number of strokes needed to clear it, which gave a rough measure of the melt, and a sudden rise meant a shifted stow or a broken lining.[^36] The hatches stayed sealed until port. Some masters had the joins sealed with wax or pitch so that tampering would show. The firms' instructions said a master who opened the hatches without good cause would answer for the lost ice.[^37]

Marine insurers at first refused ice cargoes. Later policies covered the ship and a share of the cargo but excluded melting, so the shipper bore that risk.[^39]

## The voyage

### Routes and times

Tudor's 1806 cargo to Martinique arrived to no ice house and no one who knew what to use it for. He lost money on that voyage and several more, and spent time in a debtors' prison in the 1810s.[^38] By the 1820s he was shipping ice regularly to Havana and to ports in the southern United States.[^38]

The longest regular route ran from Boston to Calcutta. It crossed the Atlantic and the equator, rounded the Cape of Good Hope, and crossed the Indian Ocean and the equator again before reaching the Hooghly River. The voyage took about 130 days.[^41] The first ice cargo to Calcutta sailed in May 1833 on the ship Tuscany and arrived that September. Newspapers described the blocks and residents came to the river to see them.[^46] The voyage made a profit, and regular sailings followed.[^46] Calcutta sailings left Boston in autumn and early winter, to arrive in the hot season from about March to June. The first weeks were then spent in cold northern waters.[^41] From the 1840s many ice ships were towed up the Hooghly by steam tugs, which cut the passage to a day or less.[^49]

Caribbean voyages to Havana, Martinique, Jamaica, and other islands took two to three weeks with fair winds. Havana became one of the steadiest markets, with ships arriving every few weeks through the year.[^42] The southern United States ports were the largest market by volume: Charleston, Savannah, Mobile, and above all New Orleans. The voyage to New Orleans took several weeks, and some ice went on up the Mississippi by steamboat.[^44] The southern trade carried most of the ice that left Boston in most years.[^30] Ice also went to Rio de Janeiro, Valparaíso, Bombay, Madras, Hong Kong, and a few cargoes to Australia. Some of these routes were given up after a few years because the ice could not be sold at a profit.[^45]

The firms preferred fast ships for the long routes and paid more to charter them. For the short routes the cheapest available ship was usually chosen.[^41] Ships returning from Calcutta brought jute, linen, indigo, saltpetre, and spices.[^30] Some historians argue that the ice voyage made sense to shipowners mainly because it put a ship in Calcutta to collect a valuable return cargo.[^30]

### How much melted

Logbooks show the pumping strokes low in the first weeks out of Boston. They rose sharply near the equator and stayed high until port.[^36] On the Calcutta route the second tropical crossing, near the end of the voyage, was the worst.[^36] A becalmed ship in the doldrums could drift for days while the ice melted.[^36] Masters were told to keep moving and avoid known calm zones even by a longer route.[^37]

A study compared the ice signed for in Boston with the ice unloaded in Calcutta for every voyage where both papers survive. On average the ships lost 38 percent of their ice, and single voyages varied widely with season, voyage length, and stow.[^47] The study's authors note that the surviving papers may come from the better-run voyages.[^47] On the Caribbean and southern routes, a well-stowed cargo often lost under a tenth of its ice.[^30] One firm's papers show the Caribbean trade paying for losses on the Indian trade in more than one year.[^15]

Masters kept a separate printed "ice book" with columns for date, position, air and sea temperature, and pumping strokes. These books are the main source for the Calcutta loss study.[^36]

## Ice houses at the far ports

### Building and capacity

After Martinique, the trade's rule was to build the ice house before the ice arrived. From the 1810s the firms built or rented one in each port before sending regular cargoes. Some were converted warehouses with extra inner walls, and others were new buildings.[^38] The firms sent carpenters from Boston with the first cargo to a new port.[^38]

Calcutta's merchants paid for an ice house by subscription after the 1833 cargo, and it opened a few years later. It was a round brick building near the river with thick walls and a domed roof, and it held about 1,250 tons. The round shape gave the smallest wall surface for the space inside.[^50] It followed the Boston double-wall plan but in brick, because wood was attacked by termites and rotted in the monsoon. The floor drained to the river, and the roof was raised over a ventilated space.[^50]

In Havana and some other ports, ice houses were partly sunk into the ground, where the earth was cooler. On low wet ground such as New Orleans they had to stand fully above ground.[^53] The Havana house was built by the Tudor firm near the harbour in the 1820s.[^54] New Orleans had several large ice houses on the levee by the 1840s, owned by competing firms and standing beside the unloading wharves.[^55] Bombay and Madras got masonry ice houses on the Calcutta model in the late 1830s and early 1840s, neither as large as Calcutta's.[^52] At Madras, which had no sheltered harbour, every block came ashore through the surf in small boats.[^56] Charleston and Savannah had smaller wooden houses on brick piers, holding a few weeks of sales. Local merchants often owned them, buying ice by the cargo from the Boston firms.[^57] Hong Kong's first ice house, built of island granite, dated from the 1840s.[^59]

Ice kept far worse in the tropical houses than at home, and agents reported losses higher, month for month, than any recorded at the ponds.[^31]

### Who ran them and how the ice was sold

The Havana house operated under a monopoly granted by the Spanish colonial government in return for a promise to keep the city supplied. The government could fine the firm for running out.[^54] Through the 1840s it was run by the firm's agent, a local merchant named Joaquín Barcia.[^58] Barcia sold by ticket. A customer bought a ticket for a set weight at the firm's city office and collected the ice at the house door, so no money changed hands there.[^58]

The Calcutta house was run by an agent sent from Boston with a staff of local workers.[^31] The agent also dealt with the merchants' committee that had paid for the building, which complained when ice ran short.[^31] Agents were usually paid a share of sales rather than a wage. Some were local merchants and others were young Boston men sent out to learn the business.[^31] In Havana, ships unloaded into lighters, flat-bottomed harbour boats, and the unloading was done at night by lantern.[^43]

The houses opened at first light and closed by mid-morning. In Calcutta the hours were printed in the newspapers, and late customers were turned away.[^50] Ice was sold by weight on a scale at the door.[^44] Some houses kept blocks pre-cut to standard weights to save time.[^60] Hotels, clubs, hospitals, and military messes had monthly accounts and were often served before the queue.[^60] In New Orleans by the 1850s, carts with insulated boxes delivered to standing orders each morning. In Havana and Calcutta delivery was rare.[^44] In ports where ice was new, agents first gave it away, and Tudor's diary records doing so in Havana and Charleston until the habit took hold.[^38] Agents also showed cooks how to make ice cream and sold ice chests shipped from Boston.[^62]

## The workers

### Who did the work

In the early years most men on the ice were local farmers and their sons, working in the farming slack season. They brought their own horses and were paid for the horse as well as the man.[^63] From the 1840s a growing share were Irish immigrants. They were hired in large numbers for the unskilled jobs, while the skilled jobs often stayed with local men.[^65] Some Irish labourers wintered in shanties near the ponds.[^64] In later decades French-Canadians came to the Massachusetts ponds. By the 1870s some large-pond crews were mostly French-Canadian.[^66] In short seasons, agents hired men off Boston streets and paid their train fares out.[^64] Boys worked from about the age of twelve, for less pay, guiding blocks, sweeping chips, and carrying messages.[^6] Women did not work on the ice but ran boarding houses, cooked, and dried clothing. The firms' accounts record these payments under the household's name.[^15]

### How the crews were organised

On the largest ponds a crew numbered about 75 men, divided into gangs for snow scraping, marking and ploughing, barring, channel work, the elevator, and stacking. The slowest gang set the pace, and the foreman moved men between gangs.[^67] Labourers were hired by the day at the pond edge, with no promise of work the next day.[^6] Skilled men, such as marker drivers, stackers, and bar men, were hired for the season and paid more.[^3] Each crew's foreman answered to the firm's superintendent for the pond.[^3] Labourers were paid on Saturday evening at the shore shanty, less board.[^15] The Boston ship stevedores were a separate, year-round waterfront workforce paid by the ton loaded.[^35] At the far ports, Calcutta's agent hired local porters.[^31] In Havana, the firm's depot hired enslaved men from their owners to unload the ships.[^70]

### Conditions and dangers

Men stood on the ice all day in temperatures well below freezing. Frostbite was common. They wore wool layers, felt boots with leather overshoes, and iron "creepers" strapped to the boots.[^69] A man who fell into the channel was sent straight to the shanty fire.[^6] Larger ponds had a shore shanty with hot coffee and soup and a hot midday meal.[^6] The day ran from first light to dark, and when a thaw threatened the crews worked into the night by lantern.[^13] Injuries from falls, saws, bars, and slipping blocks were common, and the firms paid an injured man nothing beyond the days he had worked.[^69] A horse breaking through into the water was the most common accident of the harvest.[^6] A count of newspaper reports for the Cambridge ponds found nine drownings among harvest crews between 1850 and 1860, mostly in the open channel at night.[^69]

Newspapers report fights between local men and Irish labourers in years when work was short.[^68] Crews sometimes struck when a thaw was forecast. Strikes in the 1850s and 1860s lasted a day or two and ended when the firms agreed.[^71] The firms then hired outside men and blacklisted strikers.[^64] An open winter meant no winter wage, and Boston charities reported more families seeking help after one.[^72]

## Buyers and prices

### Who bought the ice

In Calcutta the first buyers were British residents: East India Company officials, army officers, and merchants and their families.[^50] Wealthy Indian merchant and landowning families also bought from the early years, and for most of the city's people ice was far too costly.[^50] Some Indian households doubted at first that ice handled by foreign sailors and porters was clean. By the 1840s Indian buyers were a large share of the private customers.[^60] Clubs and officers' messes served iced drinks through the hot season.[^61] Hospitals were among the largest account customers, and Calcutta doctors argued in the newspapers that ice saved lives.[^60] Doctors in the hot ports used ice for fever, heatstroke, wounds, and inflammation, and New Orleans hospitals bought it in large amounts in the yellow fever epidemics of the 1850s.[^73]

In Havana the main buyers were cafés, confectioners making ice creams and sorbets, and wealthy households.[^62] Ice there spread from a luxury of the rich to a common pleasure in the cafés within a generation.[^62] New Orleans used ice on a scale no other port matched, in bars, hotels, households, and the meat and fish markets.[^44] By the 1850s ordinary households in New Orleans bought it, and small amounts were sold from carts and by grocers.[^74] River steamboats took ice on board and sold some in towns upriver.[^77] In Charleston and Savannah the buyers were planters, merchants, hotels, and taverns.[^57] Butchers, fishmongers, and dairies in the southern ports bought daily.[^44] In Hong Kong the buyers were the garrison, merchants, and ships in harbour.[^59]

### What it cost

In the 1830s and 1840s Calcutta ice sold at the door for 3 annas a pound, an anna being a sixteenth of a rupee. The price held steady for most of those two decades.[^60] At that price, daily buying took a noticeable part of a household's income.[^30] Account customers sometimes paid less by private agreement with the agent,[^60] and hospitals got a reduced rate for a daily contract.[^73] Madras and Bombay prices were above Calcutta's for the same years.[^75] In Havana the firm agreed to a maximum price under its monopoly, and the government revised it several times.[^54] New Orleans prices fell steadily from the 1830s to the 1850s as competing firms arrived, and the firms made their money on volume.[^44] By 1860 ice there sold for about 2½ cents a pound at the levee houses, rising in hot months and when a ship was late.[^76]

Everywhere, prices were lowest just after a ship arrived and highest when the next was overdue.[^60] At small ports with no ice house, masters sold from the hold at whatever buyers would pay.[^37] Ice cost almost nothing at the pond. A cost study found that ice lost in transit and storage was the largest single cost on the long routes, larger than carriage.[^30] Boston firms fought price wars, underselling a rival in a port and raising prices once the rival left.[^31] Tudor became one of the richest men in Boston by the 1840s and was known as the "Ice King."[^38]

## The end of the trade

### What ended it

The Civil War (1861 to 1865) cut off the southern trade. New Orleans was closed to Boston ships until Union forces took it in 1862.[^79] Ice machines already existed. John Gorrie of Apalachicola patented one in 1851.[^81] Ferdinand Carré developed an ammonia machine in the late 1850s, and James Harrison built machines in Australia in the 1850s.[^80] During the war some Carré machines were brought into the Confederacy through the blockade.[^82] After the war, shipping to the southern ports stayed well below late-1850s levels.[^30]

New Orleans got its first commercial ice factory in 1868, making about 12 tons a day at first.[^83] Some Boston firms cut prices to drive factories out, which worked against a few small ones in the 1870s but could not last.[^44] Through the 1870s factory ice in the South became cheaper than shipped ice once melting was counted.[^30] Early factory ice was cloudy and distrusted, but by the 1880s the best was as clear as natural ice.[^80] Calcutta began making machine ice in the late 1870s, followed by Bombay and Madras.[^85] In Havana the monopoly was not renewed, factories opened in the 1870s, and Cuba's wars for independence from 1868 disrupted trade.[^89]

Steamships, especially after the Suez Canal opened in 1869, shrank the supply of cheap outward sailing ships.[^41] Meanwhile the home market in the North and Midwest could take all the ice the ponds could cut, by rail.[^78] Ponds near Boston were fouled, and Fresh Pond became a Cambridge water supply.[^86] Tudor died in 1864, and other firms merged into home-market companies.[^87]

### When the last cargoes sailed

The Indian trade dwindled through the 1870s, sometimes to one or two ships a year, and the Bombay and Madras trade ended before Calcutta's.[^90] The last recorded New England ice cargo to Calcutta sailed from Boston in 1882 aboard the bark Margaret Ellery. No later ice ship appears in the Calcutta register.[^92] Her master noted the cargo arrived in fair condition.[^92] The Boston papers printed no reports of the last ships.[^91]

## Disagreement / Uncertainty

- **Storage loss.** The 1847 Fresh Pond ledger, kept by weighing sample blocks, shows about 17 percent lost over a season.[^23] A general history says a well-built house lost a fifth to a third, and small houses sometimes half, but gives no source.[^28] Ledgers kept by counting blocks show smaller losses than those kept by weighing, so figures from the two methods cannot be set side by side.[^26]
- **Voyage loss to Calcutta.** The logbook study gives an average of 38 percent, while noting that the surviving papers may favour better-run voyages.[^47] A general history says well-stowed ships lost about a quarter and puts higher losses down to poor stowing rather than voyage length. It does not say how it reached the figure.[^28] Neither source says which years its figure covers.[^28]
- **Short-route loss.** The "under a tenth" figure for the Caribbean and southern routes is an estimate from a small number of voyages.[^30]
- **When the trade ended.** Some histories put the end in the early 1880s.[^78] A general history says Caribbean cargoes continued irregularly into the 1890s and small shipments to southern ports into the early twentieth century, without a source for the later shipments.[^28]
- **The Calcutta ice house after the factories.** One account says it lost its trade within a few years of the late-1870s factory opening and was later pulled down.[^85] The register account says that after the 1882 voyage it sold only factory ice.[^92]
- **The Carré machines.** The number brought through the Civil War blockade is not known.[^82]
- **Drownings.** The count of nine drownings comes from newspaper reports, which may have missed some deaths.[^69]
- **Havana's later years.** The colonial records end before the monopoly's last years. The later account comes from a research project.[^89]

## Useful Details

- The usual rescue for a horse that went through the ice was to loop a rope around its neck and pull it tight. This made the animal hold its breath and float higher, so the men could drag it out. Some horses went through two or three times a season and kept working.[^6]
- Sawdust buying turned a waste product that Maine mills had once burned or dumped into a saleable one.[^33]
- The ice lining planks were often sold in the far port, since timber was scarce in some tropical ports.[^32]
- Early sailors feared melting ice would sink the ship. Tudor's diary records sailors who signed on and then left before sailing.[^38] Insurance records list ice ships lost in about the same numbers as other cargoes on the same routes.[^39]
- Masters and agents packed apples, butter, and cheese in pockets cut into the stack as private trade. Agents' letters mention apples arriving in Calcutta and Havana in better state than a month in a Boston cellar would leave them.[^40]
- Cargo size was limited less by the ship than by how much each port could sell. Office letters repeatedly ask agents how much ice each port could take each month.[^31]
- News of a Calcutta voyage could take most of a year to reach Boston. Once the overland route through Egypt opened, some letters went that way.[^48]
- Calcutta servants carried ice home in baskets on their heads at a run, wrapped in blankets or flannel. At home it lasted a day or so.[^61]
- Masters bound for Calcutta sometimes sold ice at Cape Town or Mauritius and were told to reseal the hatches within the hour.[^37]
- Calcutta's merchants gave the master of the Tuscany a gift in thanks.[^46]
- The Madras ice house survives, later used as a home and a school and now a museum. The Havana house has not been traced.[^56]
- Historians argue the New England firms created the demand that later ice factories supplied.[^62]
- The home trade in natural ice lasted until the 1920s and 1930s. The last commercial harvests on many New England ponds were in the 1930s and 1940s.[^78]
- The words "icebox" and "iceman" belong to the home trade that grew out of the habit of using ice.[^84]
- The papers of the Tudor firm survive in a business archive and are the largest single source on the trade.[^87]
- After the sea trade, the harvest crews kept cutting for the home market, the stevedores returned to general cargo, and the skills of stowing ice for a four-month voyage were no longer needed.[^88]
- By the 1880s the large ponds of Maine and the Hudson valley employed more men than the Boston ponds had at the sea trade's height.[^88]

## Open Research Questions

- What were the daily wages of harvest labourers and skilled men?
- What maximum price did the Havana monopoly set for ice?
- What were the actual prices of ice in Madras and Bombay?
- What figures exist for ice lost in the far-port ice houses?
- How many Carré machines reached the Confederacy?

## Reliability / Limitations

- `new-england-industry.example (pond rights)`: cites no archive for the pond-rights figures.[^2]
- `farm-journal-archive.example (1856)`: gives advice to farmers, not an account of a single harvest.[^5]
- `farm-journal-archive.example (1859)`: writes for farmers, not for the shipping firms.[^21]
- `walden-region-history.example (oral histories)`: recorded from people who worked the last commercial harvests, long after the shipping trade ended, so they may not describe the early trade. The rope method for horses is described with no count of how often it worked.[^6]
- `harvard-business-archive.example (pond accounts)`: the block weight is the firm's own working figure, not a measured average.[^15]
- `cambridge-historical.example (icehouses)`: the size of the Fresh Pond house comes from a company prospectus.[^17]
- `boston-newspaper-archive.example (1868 fire)`: covers one fire. The industry site gives no count of fires.[^27]
- `popular-history-press.example (book excerpt)`: gives storage and voyage loss figures, and the later shipments, without a source.[^28]
- `harvard-business-archive.example (agents' letters)`: the fish-tasting cargo comes from one agent's letter. Agents report far-port losses in general terms, and the letters give the firm's own side of its price tactics.[^31]
- `harvard-business-archive.example (diary excerpts)`: records Tudor's own view of his difficulties.[^38]
- `sailing-ship-logs.example`: the comment on rolling comes from masters' remarks, not measurement.[^36]
- `economic-history-review.example`: the short-route loss figure is an estimate from a small number of voyages.[^30]
- `ice-trade-voyages.example (melt study)`: surviving papers may come from the better-run voyages.[^47]
- `colonial-architecture-journal.example`: compares ports and gives the Havana design as a contrast to Calcutta.[^52]
- `hongkong-heritage.example`: relies on newspaper notices and gives no building records.[^59]
- `memoirs-of-empire.example`: by British residents, describing their own households.[^61]
- `boston-newspaper-archive.example (1851)`: short reports giving one side.[^68]
- `havana-archive.example (dock labour contracts)`: employers' records, with no account by the workers.[^70]
- `boston-newspaper-archive.example (1866 strike)`: takes the firms' side.[^71]
- `labor-history-ne.example (conditions)`: the drowning count comes from newspaper reports, which may have missed some deaths.[^69]
- `calcutta-gazette-archive.example`: British newspapers writing about Indian customers.[^60]
- `civil-war-commerce.example (Carré machines)`: the number of machines is not known.[^82]
- `gulf-commerce.example (New Orleans)`: gives no list of the factories that closed.[^44]
- `cuba-commerce-history.example`: the colonial records end before the monopoly's last years, and the later account comes from this project.[^89]

## Sources

[^1]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview
[^2]: https://www.new-england-industry.example/ice/pond-rights
[^3]: https://www.harvard-business-archive.example/tudor-papers/harvest-instructions
[^4]: https://www.new-england-industry.example/ice/snow-and-flooding
[^5]: https://www.farm-journal-archive.example/1856/february/ice-for-market
[^6]: https://www.walden-region-history.example/oral-histories/ice-crews
[^7]: https://www.mit-tech-history.example/inventors/wyeth-ice-tools
[^8]: https://www.patent-records.example/1829/wyeth-ice-cutting-apparatus
[^9]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s
[^10]: https://www.new-england-industry.example/ice/breaking-and-floating
[^11]: https://www.steam-power-history.example/small-engines/ice-elevators
[^12]: https://www.boston-markets-history.example/ice/local-trade
[^13]: https://www.boston-newspaper-archive.example/1858/january/ice-crop
[^14]: https://www.new-england-industry.example/ice/open-winters
[^15]: https://www.harvard-business-archive.example/tudor-papers/pond-accounts
[^16]: https://www.hudson-valley-museum.example/collections/ice-tool-catalogues
[^17]: https://www.cambridge-historical.example/fresh-pond/icehouses
[^18]: https://www.new-england-industry.example/ice/storage-history
[^19]: https://www.harvard-business-archive.example/tudor-papers/storage-trials
[^20]: https://www.massachusetts-engravings.example/prints/fresh-pond-ice-works-1852
[^21]: https://www.farm-journal-archive.example/1859/june/building-an-ice-house
[^22]: https://www.harvard-business-archive.example/tudor-papers/keepers-letters
[^23]: https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage
[^24]: https://www.railroad-history-ma.example/branches/charlestown-ice-line
[^25]: https://www.boston-harbour-history.example/wharves/charlestown-ice-houses
[^26]: https://www.ma-archives.example/ice-ledgers/methods-note
[^27]: https://www.boston-newspaper-archive.example/1868/august/icehouse-fire
[^28]: https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt
[^29]: https://www.maritime-boston.example/trade/outward-cargoes
[^30]: https://www.economic-history-review.example/2010/ice-shipping-costs
[^31]: https://www.harvard-business-archive.example/tudor-papers/agents-letters
[^32]: https://www.maritime-salem.example/papers/ship-fittings-for-ice
[^33]: https://www.maine-lumber-history.example/mills/sawdust-trade
[^34]: https://www.maritime-salem.example/papers/stowing-ice-1850
[^35]: https://www.boston-harbour-history.example/wharves/stevedores
[^36]: https://www.sailing-ship-logs.example/collections/ice-voyages
[^37]: https://www.harvard-business-archive.example/tudor-papers/masters-instructions
[^38]: https://www.harvard-business-archive.example/tudor-papers/diary-excerpts
[^39]: https://www.insurance-history.example/marine/perishable-cargoes
[^40]: https://www.food-history-quarterly.example/2014/new-england-apples-abroad
[^41]: https://www.maritime-boston.example/routes/boston-calcutta
[^42]: https://www.maritime-boston.example/routes/caribbean
[^43]: https://www.havana-archive.example/colonial-trade/shipping-arrivals
[^44]: https://www.gulf-commerce.example/ports/new-orleans-ice-imports
[^45]: https://www.maritime-boston.example/routes/other-ports
[^46]: https://www.calcutta-history-society.example/1833/first-ice-ship
[^47]: https://www.ice-trade-voyages.example/logs/calcutta-melt-study
[^48]: https://www.postal-history-review.example/2009/overland-mail-to-india
[^49]: https://www.calcutta-history-society.example/port/hooghly-pilots-and-tugs
[^50]: https://www.calcutta-history-society.example/buildings/the-ice-house
[^52]: https://www.colonial-architecture-journal.example/2016/cold-storage-in-bengal
[^53]: https://www.havana-archive.example/colonial-trade/building-permits
[^54]: https://www.havana-archive.example/colonial-trade/ice-monopoly
[^55]: https://www.louisiana-archives.example/levee/warehouse-registers
[^56]: https://www.madras-heritage.example/beach-road/ice-house
[^57]: https://www.lowcountry-history.example/charleston/ice-trade
[^58]: https://www.havana-archive.example/colonial-trade/ice-depot-1840s
[^59]: https://www.hongkong-heritage.example/waterfront/early-ice-house
[^60]: https://www.calcutta-gazette-archive.example/notices/ice-house-hours
[^61]: https://www.memoirs-of-empire.example/collections/calcutta-domestic-life
[^62]: https://www.food-history-quarterly.example/2012/ice-cream-in-the-tropics
[^63]: https://www.labor-history-ne.example/winter-work/farm-families
[^64]: https://www.labor-history-ne.example/winter-work/irish-labour
[^65]: https://www.immigration-history-journal.example/2012/boston-irish-winter-work
[^66]: https://www.immigration-history-journal.example/2015/french-canadians-in-new-england
[^67]: https://www.labor-history-ne.example/winter-work/harvest-crew-sizes
[^68]: https://www.boston-newspaper-archive.example/1851/january/disturbance-on-the-ice
[^69]: https://www.labor-history-ne.example/winter-work/ice-crews-conditions
[^70]: https://www.havana-archive.example/colonial-trade/dock-labour-contracts
[^71]: https://www.boston-newspaper-archive.example/1866/february/ice-strike
[^72]: https://www.boston-newspaper-archive.example/1880/march/open-winter-hardship
[^73]: https://www.medical-history-journal.example/2013/ice-in-tropical-medicine
[^74]: https://www.louisiana-archives.example/newspapers/daily-ice-reports
[^75]: https://www.bombay-gazette-archive.example/notices/ice-sales
[^76]: https://www.gulf-commerce.example/price-current/ice-1860
[^77]: https://www.river-history-review.example/2011/steamboat-provisioning
[^78]: https://www.new-england-industry.example/ice/decline
[^79]: https://www.civil-war-commerce.example/blockade/ice-shortage
[^80]: https://www.mit-tech-history.example/inventors/early-refrigeration
[^81]: https://www.patent-records.example/1851/gorrie-ice-machine
[^82]: https://www.civil-war-commerce.example/blockade/carre-machines
[^83]: https://www.louisiana-archives.example/business/ice-manufacturing-charters
[^84]: https://www.food-history-quarterly.example/2016/clear-ice-and-cloudy-ice
[^85]: https://www.calcutta-history-society.example/industry/bengal-ice-factory
[^86]: https://www.cambridge-historical.example/fresh-pond/water-supply
[^87]: https://www.harvard-business-archive.example/tudor-papers/finding-aid-overview
[^88]: https://www.labor-history-ne.example/winter-work/after-the-sea-trade
[^89]: https://www.cuba-commerce-history.example/1870s/manufactures
[^90]: https://www.ice-trade-voyages.example/registers/calcutta-arrivals
[^91]: https://www.boston-newspaper-archive.example/1880s/ice-coverage-survey
[^92]: https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882
````

Final reply:

````
```json
{ "note": "Research/research-light-ice-trade.md", "cut_short_topics": [] }
```
````

### W8: Cut short, research-writer agent

Case folder: `research-writer-08-cut-short`. Run folder: `writer-a1`.

#### Run 1

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-09'
PASS  fm-modified-run-date  found 'modified: 2026-10-09'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-dipper-questions-open   The Open Research Questions section lists both topic-2 questions as unanswered:  > ## Open Research Questions > > - Who were the dippers, beyond being the female attendants who helped women bathers into the water? What did their work involve? > - How was the dippers' work licensed or paid? > - How were the male attendants on men's machines licensed or paid, and did their work differ from the dipp
PASS  judge-footnotes-resolve   **Markers in the body:** `[^1]`, `[^2]`, `[^3]`, `[^4]`, `[^5]`. Each has a definition under Sources:  - `[^1]` is used in the body, for example "…out of sight of the beach.[^1]". It is defined as `[^1]: https://www.seaside-heritage.example/collections/bathing-machines`. - `[^2]` is used in "…men's machines had male attendants.[^2]". It is defined as `[^2]: https://www.victorian-leisure-journal.e
PASS  judge-nothing-from-cut-short   None of the topic 2 facts appears anywhere in the note. Each one is absent:  - **Strong local women, fishermen's wives and daughters, waist-deep for hours in all weather:** Not present. The only description of dippers is under "How a bather used one": "Women bathers were helped into the water by female attendants called dippers, who stood in the sea beside the steps." That matches the topic 1 wor
PASS  judge-reply-names-topic-2   The reply flags topic 2 and no other topic as cut short: `"cut_short_topics": [2]`. Topics 1 and 3 are not in that list.
PASS  keeps-3-feet  found '3 feet'
PASS  keeps-60-yards  found '60 yards'
PASS  keeps-winch  found 'winch'
PASS  no-badge  no match
PASS  no-cut-short-urls  no match
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-wrenfield  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## The bathing machine'
PASS  shape-topic-3-section  found '## Keeping men and women apart'
PASS  file-name  expected name written
````

`project/Research/research-light-bathing-machines.md`:

````markdown
---
title: Light Research - Bathing Machines
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-09
modified: 2026-10-09
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Topics: the bathing machine (what it was, how it was moved into the sea, and how a bather used it); the dippers (who they were, what they did, and how their work was licensed or paid); and keeping men and women apart (the rules that separated the sexes on the beach, and when and how mixed bathing became allowed). Limits: British seaside resorts only, in the years 1840 to 1900.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Bathing Machines

## Summary

A bathing machine was a small wooden hut on four large wheels that was pulled into the sea with the bather inside, so that the bather could change into a costume on the way out and step down into the water out of sight of the beach.[^1] At most resorts a horse did the pulling, though a few resorts with steep shingle beaches hauled the machines up and down on a cable worked by a winch on the shore.[^3] Women bathers were helped into the water by female attendants called dippers, and men's machines had male attendants.[^2]

Men and women bathed from separate stretches of beach. Under the Town Police Clauses Act of 1847, town councils could set bathing areas by bylaw and fine anyone who broke the rules, and many resorts required the men's machines to stand at least 60 yards from the women's.[^5] Men at many resorts bathed naked until the 1860s, which was one reason for the distance, and from the 1860s most resorts' bylaws required men to wear a costume.[^5] Mixed bathing began to be allowed at some resorts in the 1890s, usually for families, and the bathing machine fell out of use as it spread.[^1]

## The bathing machine

### What it was

A bathing machine was a small wooden hut on four large wheels, with a door at each end and steps leading down from the seaward door.[^1]

### How it was moved into the sea

At most resorts a horse pulled the machine into the sea and back again.[^1] The attendant, who either owned or hired the machine, led the horse out until the water stood about 3 feet deep at the steps. He then unhitched the horse and brought it round to the landward end, ready to pull the machine back up to the beach.[^1]

At a few resorts with steep shingle beaches, a winch on the shore hauled the machines up and down on a cable instead of a horse pulling them.[^3]

### How a bather used one

The bather climbed into the machine on the beach in ordinary clothes. While the machine was pulled out into the sea, the bather changed inside it into a bathing costume. When the machine stopped, the bather went down the steps straight into the water, out of sight of the beach.[^1]

Women bathers were helped into the water by female attendants called dippers, who stood in the sea beside the steps. Men's machines had male attendants, who were sometimes called bathers or guides.[^2]

A bather paid for a set time in the machine, usually half an hour. When the time was up the attendant rang a bell or waved a flag, and a bather who stayed too long paid for a second turn.[^4]

## Keeping men and women apart

### The rules that kept them apart

Most resorts set aside separate stretches of beach for men's machines and women's machines.[^5] Local bylaws made under the Town Police Clauses Act of 1847 gave town councils the power to set the bathing areas and to fine anyone who broke the rules.[^5] At many resorts the bylaws required the men's machines to stand at least 60 yards from the women's.[^5]

Men at many resorts bathed naked until the 1860s, and this was one reason for keeping the sexes far apart.[^5] From the 1860s, bylaws at most resorts required men to wear a costume, usually a one-piece garment that covered the body from neck to knee.[^5]

### When and how mixed bathing became allowed

Mixed bathing, with men and women in the water together, began to be allowed at some resorts in the 1890s, usually for families.[^5] The change spread slowly, and some town councils still opposed it into the 1900s.[^5]

As mixed bathing spread, the bathing machine fell out of use. Fixed beach huts and tents on the sand replaced it.[^1]

## Disagreement / Uncertainty

- **Dates for mixed bathing vary by town.** The source on mixed bathing says local practice varied widely and that dates differ from town to town.[^5] The 1890s is when it began at some resorts, not a date that held everywhere, and some councils were still opposing it into the 1900s.[^5]
- **Which resorts used winches is unclear.** The source for winch-hauled machines covers a single town and names the resorts that used winches without giving dates.[^3]

## Useful Details

- Bathing machines were painted in bright colours or stripes, and each one carried its owner's name.[^1]
- On busy summer mornings at the large resorts, bathers queued on the beach for a free machine.[^4]

## Open Research Questions

- Who were the dippers, beyond being the female attendants who helped women bathers into the water? What did their work involve?
- How was the dippers' work licensed or paid?
- How were the male attendants on men's machines licensed or paid, and did their work differ from the dippers'?

## Reliability / Limitations

- `seaside-heritage.example (museum collection article, 2018)`: a museum collection article.
- `victorian-leisure-journal.example (2014)`: a peer-reviewed article.
- `coastal-towns-archive.example (local history society page, 2012)`: covers one town and names the winch resorts without dates.
- `resort-guides-digitized.example (1865 Brighton visitors' guide)`: a digitized resort guidebook from 1865.
- `legal-history-review.example (2011)`: a peer-reviewed article. It says local practice varied widely and dates differ from town to town.

## Sources

[^1]: https://www.seaside-heritage.example/collections/bathing-machines
[^2]: https://www.victorian-leisure-journal.example/2014/the-bathing-machine
[^3]: https://www.coastal-towns-archive.example/hastings/beach-engineering
[^4]: https://www.resort-guides-digitized.example/1865/brighton-visitors-guide
[^5]: https://www.legal-history-review.example/2011/seaside-bylaws
````

Final reply:

````
```json
{ "note": "Research/research-light-bathing-machines.md", "cut_short_topics": [2] }
```
````

#### Run 2

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-09'
PASS  fm-modified-run-date  found 'modified: 2026-10-09'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-dipper-questions-open   The Open Research Questions section lists both topic 2 questions as unanswered:  > ## Open Research Questions > > - Who were the dippers, and what did they do beyond helping women bathers into the water at the machine steps? > - How was the dippers' work licensed or paid?  The first bullet covers who the dippers were and what they did. It takes account of the one usable fact from topic 1 ("helpin
PASS  judge-footnotes-resolve   Markers used in the body: [^1], [^2], [^3], [^4], [^5]. All five have definitions under Sources, and each definition holds a URL:  - `[^1]: https://www.seaside-heritage.example/collections/bathing-machines`, used in "A bathing machine was a small wooden hut on four large wheels…[^1]" and elsewhere. - `[^2]: https://www.victorian-leisure-journal.example/2014/the-bathing-machine`, used in "Women ba
PASS  judge-nothing-from-cut-short   None of the topic 2 facts appear anywhere in the note. Each dipper mention stays within what topic 1 allows:  - **Summary:** "Women bathers were helped into the water by female attendants called dippers, and men's machines had male attendants." This is topic 1 content. - **How a bather used one:** "Women bathers were helped into the water by female attendants called dippers, who stood in the sea 
PASS  judge-reply-names-topic-2   The reply names topic 2, and only topic 2, as cut short: `"cut_short_topics": [2]`. The list leaves out topics 1 and 3, so neither is called cut short. The reply does not say that no file was cut short.
PASS  keeps-3-feet  found '3 feet'
PASS  keeps-60-yards  found '60 yards'
PASS  keeps-winch  found 'winch'
PASS  no-badge  no match
PASS  no-cut-short-urls  no match
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-wrenfield  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## The bathing machine'
PASS  shape-topic-3-section  found '## Keeping men and women apart'
PASS  file-name  expected name written
````

`project/Research/research-light-bathing-machines.md`:

````markdown
---
title: Light Research - Bathing Machines
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-09
modified: 2026-10-09
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Topics: the bathing machine (what it was, how it was moved into the sea, and how a bather used one); the dippers (who they were, what they did, and how their work was licensed or paid); and keeping men and women apart (the rules that separated them on the beach, and when and how mixed bathing became allowed). Limits: British seaside resorts only, in the years 1840 to 1900.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Bathing Machines

## Summary

A bathing machine was a small wooden hut on four large wheels that let a bather change into a costume while being pulled into the sea, then step down straight into the water out of sight of the beach.[^1] At most resorts a horse pulled it out and back; at a few resorts with steep shingle beaches, a winch on the shore hauled it on a cable instead.[^3] Women bathers were helped into the water by female attendants called dippers, and men's machines had male attendants.[^2] Bathers paid for a set time, usually half an hour.[^4]

Men's and women's machines stood on separate stretches of beach, under local bylaws made under the Town Police Clauses Act of 1847, which let town councils set bathing areas and fine those who broke the rules.[^5] Men at many resorts bathed naked until the 1860s, after which most resorts' bylaws required a costume.[^2] Mixed bathing began to be allowed at some resorts in the 1890s, usually for families, and as it spread the bathing machine fell out of use, replaced by fixed beach huts and tents on the sand.[^5][^1]

## The bathing machine

### What it was

A bathing machine was a small wooden hut on four large wheels, with a door at each end and steps down from the seaward door.[^1] Machines were painted in bright colours or stripes, and each carried its owner's name.[^1]

### How it was moved into the sea

At most resorts a horse pulled the machine into the sea and back.[^1] The attendant, who owned or hired the machine, led the horse out until the water stood about 3 feet deep at the steps, unhitched it, and brought it round to the landward end, ready to pull the machine back to the beach.[^1]

At a few resorts with steep shingle beaches, the machines were hauled up and down on a cable by a winch on the shore instead of by a horse.[^3]

### How a bather used one

A bather climbed in on the beach in ordinary clothes, and the machine was pulled out into the sea while the bather changed inside into a bathing costume.[^1] When the machine stopped, the bather went down the steps straight into the water, out of sight of the beach.[^1]

Women bathers were helped into the water by female attendants called dippers, who stood in the sea beside the steps.[^2] Men's machines had male attendants, sometimes called bathers or guides.[^2]

A bather paid for a set time in the machine, usually half an hour, and the attendant rang a bell or waved a flag when the time was up.[^4] A bather who stayed too long paid for a second turn.[^4] On busy summer mornings at the large resorts, bathers queued on the beach for a free machine.[^4]

## Keeping men and women apart

### The rules

Most resorts set aside separate stretches of beach for men's and women's machines.[^5] Local bylaws made under the Town Police Clauses Act of 1847 gave town councils the power to set the bathing areas and to fine anyone who broke the rules.[^5] At many resorts the bylaws required the men's machines to stand at least 60 yards from the women's.[^5]

Men at many resorts bathed naked until the 1860s, which was one reason for keeping the sexes far apart.[^2] From the 1860s bylaws at most resorts required men to wear a costume, usually a one-piece garment covering the body from neck to knee.[^2]

### When and how mixed bathing became allowed

Mixed bathing, with men and women in the water together, began to be allowed at some resorts in the 1890s, usually for families.[^5] The change spread slowly and was still opposed by some town councils into the 1900s.[^5] As mixed bathing spread, the bathing machine fell out of use and was replaced by fixed beach huts and tents on the sand.[^1]

## Disagreement / Uncertainty

- **Dates of mixed bathing vary by town.** The legal-history source says local practice varied widely and that dates differ from town to town; the 1890s start and the slow spread into the 1900s are a general pattern, not a date that held everywhere.[^5]
- **Which resorts used winches is undated.** The source for winch-hauled machines covers one town and names the winch resorts without giving dates, so it is unclear when within 1840 to 1900 winches were in use.[^3]

## Open Research Questions

- Who were the dippers, and what did they do beyond helping women bathers into the water at the machine steps?
- How was the dippers' work licensed or paid?

## Reliability / Limitations

- `seaside-heritage.example (museum collection article, 2018)`: museum collection article.
- `victorian-leisure-journal.example (2014)`: peer-reviewed article.
- `coastal-towns-archive.example (local history society page, 2012)`: covers one town (Hastings) and names the winch resorts without dates.
- `resort-guides-digitized.example (1865 Brighton visitors' guide)`: a digitized resort guidebook from 1865, describing practice at the time.
- `legal-history-review.example (2011)`: peer-reviewed article; it says local practice varied widely and dates differ from town to town.

## Sources

[^1]: https://www.seaside-heritage.example/collections/bathing-machines
[^2]: https://www.victorian-leisure-journal.example/2014/the-bathing-machine
[^3]: https://www.coastal-towns-archive.example/hastings/beach-engineering
[^4]: https://www.resort-guides-digitized.example/1865/brighton-visitors-guide
[^5]: https://www.legal-history-review.example/2011/seaside-bylaws
````

Final reply:

````
```json
{ "note": "Research/research-light-bathing-machines.md", "cut_short_topics": [2] }
```
````

#### Run 3

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-09'
PASS  fm-modified-run-date  found 'modified: 2026-10-09'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-dipper-questions-open   The Open Research Questions section lists both topic 2 questions as unanswered:  > ## Open Research Questions > > - Who were the dippers: where were they drawn from, and what did their work involve beyond helping women bathers into the water from the machine steps? > - How was the dippers' work licensed or paid? > - Were the male attendants on men's machines licensed or paid differently from dipp
PASS  judge-footnotes-resolve   **Markers used in the body:** [^1], [^2], [^3], [^4], [^5]. No other markers appear.  **Every marker has a definition with a URL** under `## Sources`: - `[^1]: https://www.seaside-heritage.example/collections/bathing-machines` - `[^2]: https://www.victorian-leisure-journal.example/2014/the-bathing-machine` - `[^3]: https://www.coastal-towns-archive.example/hastings/beach-engineering` - `[^4]: htt
PASS  judge-nothing-from-cut-short   None of the topic 2 facts appears anywhere in the note. Each one is checked below.  - **Strong local women, fishermen's wives and daughters, waist-deep for hours in all weather:** absent. The open question asks where dippers "were drawn from" but gives no answer. - **Led each bather from the steps and plunged her under the waves, thought good for health:** absent. No plunging and no health claim 
PASS  judge-reply-names-topic-2   The reply names topic 2, and only topic 2, as cut short: `"cut_short_topics": [2]`. It does not list topic 1 or topic 3.
PASS  keeps-3-feet  found '3 feet'
PASS  keeps-60-yards  found '60 yards'
PASS  keeps-winch  found 'winch'
PASS  no-badge  no match
PASS  no-cut-short-urls  no match
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-wrenfield  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## The bathing machine'
PASS  shape-topic-3-section  found '## Keeping men and women apart'
PASS  file-name  expected name written
````

`project/Research/research-light-bathing-machines.md`:

````markdown
---
title: Light Research - Bathing Machines
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-09
modified: 2026-10-09
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Three topics: the bathing machine (what it was, how it was moved into the sea, and how a bather used one); the dippers (who they were, what they did, and how their work was licensed or paid); and keeping men and women apart (the rules that separated the sexes on the beach, and when and how mixed bathing became allowed). Limited to British seaside resorts, 1840 to 1900.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Bathing Machines

## Summary

A bathing machine was a small wooden hut on four large wheels, which a bather entered on the beach in ordinary clothes and changed inside while it was pulled out into the sea, then left by steps straight into the water, out of sight of the beach.[^1] At most resorts a horse pulled it; at a few steep shingle beaches a shore winch hauled it on a cable.[^1][^3] Women bathers were helped into the water by female attendants called dippers, and men's machines had male attendants.[^2] Bathers paid for a set time, usually half an hour.[^4]

Most resorts kept separate stretches of beach for men's and women's machines, under local bylaws made with powers from the Town Police Clauses Act of 1847, which also let councils fine rule-breakers.[^5] Men at many resorts bathed naked until the 1860s, after which bylaws at most resorts required a costume.[^2][^5] Mixed bathing began to be allowed at some resorts in the 1890s, usually for families, and spread slowly; as it spread, the bathing machine fell out of use.[^5][^1]

## The bathing machine

### What it was

A bathing machine was a small wooden hut on four large wheels, with a door at each end and steps down from the seaward door.[^1] Machines were painted in bright colours or stripes, and each carried its owner's name.[^1]

### How it was moved into the sea

At most resorts a horse pulled the machine into the sea and back.[^1] The attendant, who owned or hired the machine, led the horse out until the water stood about 3 feet deep at the steps, unhitched it, and brought it round to the landward end, ready to pull the machine back to the beach.[^1]

At a few resorts with steep shingle beaches, the machines were instead hauled up and down on a cable by a winch on the shore.[^3]

### How a bather used one

A bather climbed in on the beach in ordinary clothes, and the machine was pulled out into the sea while the bather changed inside into a bathing costume.[^1] When the machine stopped, the bather went down the steps straight into the water, out of sight of the beach.[^1]

Women bathers were helped into the water by female attendants called dippers, who stood in the sea beside the steps.[^2] Men's machines had male attendants, sometimes called bathers or guides.[^2]

A bather paid for a set time in the machine, usually half an hour, and the attendant rang a bell or waved a flag when the time was up.[^4] A bather who stayed too long paid for a second turn.[^4] On busy summer mornings at the large resorts, bathers queued on the beach for a free machine.[^4]

## Keeping men and women apart

### The rules

Most resorts set aside separate stretches of beach for men's and women's machines.[^5] Local bylaws made under the Town Police Clauses Act of 1847 gave town councils the power to set the bathing areas and to fine anyone who broke the rules.[^5] At many resorts the bylaws required the men's machines to stand at least 60 yards from the women's.[^5]

Men at many resorts bathed naked until the 1860s, which was one reason for keeping the sexes far apart.[^2] From the 1860s, bylaws at most resorts required men to wear a costume, usually a one-piece garment covering the body from neck to knee.[^5]

### When and how mixed bathing became allowed

Mixed bathing, with men and women in the water together, began to be allowed at some resorts in the 1890s, usually for families.[^5] The change spread slowly and was still opposed by some town councils into the 1900s.[^5]

As mixed bathing spread, the bathing machine fell out of use and was replaced by fixed beach huts and tents on the sand.[^1]

## Disagreement / Uncertainty

- **Dates for mixed bathing vary by town.** The source on mixed bathing says local practice varied widely and dates differ from town to town, so the 1890s start and the slow spread are a general pattern, not a fixed date for any one resort.[^5]
- **Which resorts used winches is undated.** The source for winch-hauled machines covers one town and names the winch resorts without dates, so when winches were used there is not established.[^3]
- **Some details rest on a single period source.** The half-hour turn, the bell or flag, the charge for a second turn, and the morning queues come from one digitized resort guidebook of 1865.[^4]

## Useful Details

- Machines were painted in bright colours or stripes and carried the owner's name.[^1]
- The attendant who led the horse either owned or hired the machine.[^1]
- The men's costume required from the 1860s was usually a one-piece garment from neck to knee.[^5]
- Fixed beach huts and tents on the sand replaced the bathing machine as mixed bathing spread.[^1]

## Open Research Questions

- Who were the dippers: where were they drawn from, and what did their work involve beyond helping women bathers into the water from the machine steps?
- How was the dippers' work licensed or paid?
- Were the male attendants on men's machines licensed or paid differently from dippers?
- When, and at which resorts, were machines hauled by winch rather than by horse?

## Reliability / Limitations

- `seaside-heritage.example (museum collection article, 2018)`: no reliability or limitation note was given in the findings.
- `victorian-leisure-journal.example (peer-reviewed article, 2014)`: no reliability or limitation note was given in the findings.
- `coastal-towns-archive.example (local history society page, 2012)`: covers one town and names the winch resorts without dates.
- `resort-guides-digitized.example (digitized resort guidebook, 1865)`: no reliability or limitation note was given in the findings.
- `legal-history-review.example (peer-reviewed article, 2011)`: says local practice varied widely and dates differ from town to town.

## Sources

[^1]: https://www.seaside-heritage.example/collections/bathing-machines
[^2]: https://www.victorian-leisure-journal.example/2014/the-bathing-machine
[^3]: https://www.coastal-towns-archive.example/hastings/beach-engineering
[^4]: https://www.resort-guides-digitized.example/1865/brighton-visitors-guide
[^5]: https://www.legal-history-review.example/2011/seaside-bylaws
````

Final reply:

````
```json
{ "note": "Research/research-light-bathing-machines.md", "cut_short_topics": [2] }
```
````

### P1: Limits for every topic, research-planner agent

Case folder: `research-planner-01-every-topic-limits`. Run folder: `planner-a2`.

#### Run 1

Grades:

````
PASS  every-topic-has-period  found '## Every topic\n\nLimit the research to coal mining in the Rhondda valley, South Wales, between 1900 and 1914'
PASS  every-topic-has-place  found '## Every topic\n\nLimit the research to coal mining in the Rhondda'
PASS  judge-topics-split   The plan has two topics, one for the shift and one for the dangers, and neither waits on the other.  - **"## Topic 1"** covers the shift: "What did a typical shift look like for a coal miner? Cover the day from start to finish: when the shift began and how long it lasted, getting to the pit and going down the shaft..." - **"## Topic 2"** covers the dangers: "What were the main dangers underground
PASS  plan-has-every-topic  found '## Every topic'
PASS  plan-has-topic-1  found '## Topic 1'
PASS  plan-has-topic-2  found '## Topic 2'
PASS  request-note-no-edit  0 Edit call(s) matching /concept-pit-village/
PASS  request-note-no-write  0 Write call(s) matching /concept-pit-village/
PASS  schedule-has-waits-on  found '"waits_on"'
PASS  schedule-names-topic  found '"research_topic": "rhondda-mining-shift"'
PASS  schedule-nothing-waits  no match
````

`project/llm-files/research-plans/research-plan-rhondda-mining-shift.md`:

````markdown
## Every topic

Limit the research to coal mining in the Rhondda valley, South Wales, between 1900 and 1914.

## Topic 1

What did a typical shift look like for a coal miner? Cover the day from start to finish: when the shift began and how long it lasted, getting to the pit and going down the shaft, the walk to the coal face, the work done there and the tools used, breaks and food, who worked alongside the miner (such as boys, hauliers, and other roles), how the work was paid, and coming back up at the end of the shift.

## Topic 2

What were the main dangers underground for a coal miner? Cover the kinds of hazards (such as gas explosions, coal dust, roof falls, flooding, haulage and machinery accidents, and long-term illnesses), how often they caused injury or death, and the safety measures and equipment in use at the time.
````

`run/answer.json`:

````json
{ "research_topic": "rhondda-mining-shift",
  "topics": [
    { "n": 1, "waits_on": [] },
    { "n": 2, "waits_on": [] } ] }
````

Final reply:

````
```json
{ "research_topic": "rhondda-mining-shift",
  "topics": [
    { "n": 1, "waits_on": [] },
    { "n": 2, "waits_on": [] } ] }
```
````

#### Run 2

Grades:

````
PASS  every-topic-has-period  found '## Every topic\n\nKeep to coal mining in the Rhondda valley, South Wales, from 1900 to 1914'
PASS  every-topic-has-place  found '## Every topic\n\nKeep to coal mining in the Rhondda'
PASS  judge-topics-split   The plan has two topics, and they match the two subjects in the request:  - **"## Topic 1"** covers the shift: "What did a typical shift look like for a coal miner? When did it start and end, and how long was it? ... how did the shift end and the miners come back up?" - **"## Topic 2"** covers the dangers: "What were the main dangers underground for coal miners? Cover the hazards they faced (expl
PASS  plan-has-every-topic  found '## Every topic'
PASS  plan-has-topic-1  found '## Topic 1'
PASS  plan-has-topic-2  found '## Topic 2'
PASS  request-note-no-edit  0 Edit call(s) matching /concept-pit-village/
PASS  request-note-no-write  0 Write call(s) matching /concept-pit-village/
PASS  schedule-has-waits-on  found '"waits_on"'
PASS  schedule-names-topic  found '"research_topic": "rhondda-mining-shift"'
PASS  schedule-nothing-waits  no match
````

`project/llm-files/research-plans/research-plan-rhondda-mining-shift.md`:

````markdown
## Every topic

Keep to coal mining in the Rhondda valley, South Wales, from 1900 to 1914.

## Topic 1

What did a typical shift look like for a coal miner? When did it start and end, and how long was it? How did miners get to the pit, go down, and reach the coalface? What work did they do through the shift, and who did which jobs (colliers, their boy helpers, hauliers, others)? When did they break or eat, and how did the shift end and the miners come back up?

## Topic 2

What were the main dangers underground for coal miners? Cover the hazards they faced (explosions, firedamp and other gases, coal dust, roof falls, haulage and machine accidents, flooding, and others), how often each one caused injury or death, and what miners and pit owners did to guard against them.
````

`run/answer.json`:

````json
{ "research_topic": "rhondda-mining-shift",
  "topics": [
    { "n": 1, "waits_on": [] },
    { "n": 2, "waits_on": [] } ] }
````

Final reply:

````
```json
{ "research_topic": "rhondda-mining-shift",
  "topics": [
    { "n": 1, "waits_on": [] },
    { "n": 2, "waits_on": [] } ] }
```
````

#### Run 3

Grades:

````
PASS  every-topic-has-period  found '## Every topic\n\nKeep to coal mining in the Rhondda valley, South Wales, from 1900 to 1914'
PASS  every-topic-has-place  found '## Every topic\n\nKeep to coal mining in the Rhondda'
PASS  judge-topics-split   The plan has two topics, and each covers one of the requested subjects:  - **"## Topic 1"** covers the shift. It opens with "What did a typical shift look like for a coal miner?" and goes on to start and end times, getting to the coal face, the work done, crew roles, and meals and breaks. - **"## Topic 2"** covers the dangers. It opens with "What were the main dangers underground for a coal miner
PASS  plan-has-every-topic  found '## Every topic'
PASS  plan-has-topic-1  found '## Topic 1'
PASS  plan-has-topic-2  found '## Topic 2'
PASS  request-note-no-edit  0 Edit call(s) matching /concept-pit-village/
PASS  request-note-no-write  0 Write call(s) matching /concept-pit-village/
PASS  schedule-has-waits-on  found '"waits_on"'
PASS  schedule-names-topic  found '"research_topic": "rhondda-mining-shift"'
PASS  schedule-nothing-waits  no match
````

`project/llm-files/research-plans/research-plan-rhondda-mining-shift.md`:

````markdown
## Every topic

Keep to coal mining in the Rhondda valley, South Wales, from 1900 to 1914.

## Topic 1

What did a typical shift look like for a coal miner? When did it start and end, and how long was it? How did miners get to the coal face and back, and what work filled the hours in between? Who worked together underground, and what jobs did each person do? What did miners eat and drink below ground, and when did they take breaks?

## Topic 2

What were the main dangers underground for a coal miner? What were the common causes of death and injury, such as explosions, roof falls, and haulage accidents? Which long-term health risks came from the work? How often did accidents happen, and which major disasters struck the valley in this period? What safety measures, equipment, and rules were in use at the time?
````

`run/answer.json`:

````json
{ "research_topic": "rhondda-mining-shift",
  "topics": [
    { "n": 1, "waits_on": [] },
    { "n": 2, "waits_on": [] } ] }
````

Final reply:

````
```json
{ "research_topic": "rhondda-mining-shift",
  "topics": [
    { "n": 1, "waits_on": [] },
    { "n": 2, "waits_on": [] } ] }
```
````

### P2: An instruction for one topic, research-planner agent

Case folder: `research-planner-02-one-topic-instruction`. Run folder: `planner-a2`.

#### Run 1

Grades:

````
PASS  every-topic-no-small-town  no match
PASS  judge-instruction-placement   The small-town limit appears only in the music topic. Topic 1 asks "How did a silent film get its music in a small-town British cinema of the 1920s?" and ends with: "Cover only small-town cinemas. Leave out the big city picture palaces."  `## Every topic` says only "Cover British cinemas in the 1920s, the silent film era." It has no small-town limit.  Topic 2, the film-transport topic, asks "How 
PASS  judge-topics-cover-request   The plan has two separate topics, one for each subject. Neither is missing, and they are not merged.  - **Music:** The heading "## Topic 1" opens with "How did a silent film get its music in a small-town British cinema of the 1920s?" It then covers who played the music, what they played, how they fitted it to the screen, and how they were hired and paid. - **Moving prints:** The heading "## Topic
PASS  plan-has-every-topic  found '## Every topic'
PASS  plan-has-topic-1  found '## Topic 1'
PASS  plan-has-topic-2  found '## Topic 2'
PASS  plan-keeps-small-town  found 'small-town'
PASS  request-note-no-edit  0 Edit call(s) matching /idea-picture-house/
PASS  request-note-no-write  0 Write call(s) matching /idea-picture-house/
PASS  schedule-names-topic  found '"research_topic": "silent-film-cinemas"'
````

`project/llm-files/research-plans/research-plan-silent-film-cinemas.md`:

````markdown
## Every topic

Cover British cinemas in the 1920s, the silent film era.

## Topic 1

How did a silent film get its music in a small-town British cinema of the 1920s? Who played it: a lone pianist, a small band, or a mechanical instrument? What did they play: improvised music, cue sheets, stock music books, or scores sent out with the film? How did the musicians fit the music to what was on screen? How were they hired and paid?

Cover only small-town cinemas. Leave out the big city picture palaces.

## Topic 2

How were film prints moved from town to town in 1920s Britain? Who owned the prints, and how did they get from the renters and distributors to the cinemas: by rail, by road, by post, or carried by hand? How were the cans packed and handled, given that nitrate film could catch fire? How did a print pass from one cinema to the next, and how long did a cinema keep it?
````

`run/answer.json`:

````json
{ "research_topic": "silent-film-cinemas",
  "topics": [
    { "n": 1, "waits_on": [] },
    { "n": 2, "waits_on": [] } ] }
````

Final reply:

````
```json
{ "research_topic": "silent-film-cinemas",
  "topics": [
    { "n": 1, "waits_on": [] },
    { "n": 2, "waits_on": [] } ] }
```
````

#### Run 2

Grades:

````
PASS  every-topic-no-small-town  no match
PASS  judge-instruction-placement   The small-town limit appears only in the music topic. Topic 1 ("How did a silent film get its music in a 1920s British cinema?") ends with: "Limit for this topic: only small-town cinemas. Leave out the big city picture palaces."  It is not under `## Every topic`, which says only: "Cinemas in Britain in the 1920s (the silent film era, before sound film took over)."  It is not under Topic 2 ("How w
PASS  judge-topics-cover-request   The plan keeps the two subjects as separate topics, each with its own heading and question:  - **Topic 1 (music):** "## Topic 1" — "How did a silent film get its music in a 1920s British cinema?" Its sub-questions are all about music: "Who played the music: a solo pianist, a small band or orchestra, an organist…" and "cue sheets sent with the film, published collections of mood music, or full sco
PASS  plan-has-every-topic  found '## Every topic'
PASS  plan-has-topic-1  found '## Topic 1'
PASS  plan-has-topic-2  found '## Topic 2'
PASS  plan-keeps-small-town  found 'small-town'
PASS  request-note-no-edit  0 Edit call(s) matching /idea-picture-house/
PASS  request-note-no-write  0 Write call(s) matching /idea-picture-house/
PASS  schedule-names-topic  found '"research_topic": "silent-film-cinemas"'
````

`project/llm-files/research-plans/research-plan-silent-film-cinemas.md`:

````markdown
## Every topic

Cinemas in Britain in the 1920s (the silent film era, before sound film took over).

## Topic 1

How did a silent film get its music in a 1920s British cinema?

- Who played the music: a solo pianist, a small band or orchestra, an organist, or something else? How were these musicians hired, paid, and scheduled?
- Where did the music come from: improvised, cue sheets sent with the film, published collections of mood music, or full scores? How did the musicians know what to play and when?
- What instruments or machines were used: pianos, organs, gramophones, or effects for sounds?
- How did the music fit around the show: rehearsal, timing to the picture, and the programme as a whole?

Limit for this topic: only small-town cinemas. Leave out the big city picture palaces.

## Topic 2

How were film prints moved from town to town in 1920s Britain?

- Who owned and sent out the prints: distributors (renters), exchanges, or others? How did a cinema book a film and get its copy?
- How did the prints travel: rail, road, post, carriers, or by hand? What containers were used?
- How were prints shared between cinemas, and how did a print move along a circuit of towns over the weeks of its run?
- What rules and risks came with moving the film stock itself, such as the fire risk of nitrate film, damage, and wear on the prints?
````

`run/answer.json`:

````json
{ "research_topic": "silent-film-cinemas",
  "topics": [
    { "n": 1, "waits_on": [] },
    { "n": 2, "waits_on": [] } ] }
````

Final reply:

````
```json
{ "research_topic": "silent-film-cinemas",
  "topics": [
    { "n": 1, "waits_on": [] },
    { "n": 2, "waits_on": [] } ] }
```
````

#### Run 3

Grades:

````
PASS  every-topic-no-small-town  no match
PASS  judge-instruction-placement   The limit is in the music topic. Topic 1, which asks how a silent film got its music, says: "Only small-town cinemas. Leave out the big city picture palaces." Its opening question also says "in a small-town British cinema in the 1920s."  The limit is not under `## Every topic`. That section only says: "Keep to British cinemas in the 1920s." It does not mention small towns or picture palaces.  The
PASS  judge-topics-cover-request   The plan has two separate topics, one for each subject.  **Music in the cinema:** The heading is "## Topic 1". It opens: "How did a silent film get its music in a small-town British cinema in the 1920s?" It goes on to ask who played it ("a pianist, an organist, a small band"), how they got the music ("cue sheets, published collections, or making it up on the spot"), and "How did the music follow 
PASS  plan-has-every-topic  found '## Every topic'
PASS  plan-has-topic-1  found '## Topic 1'
PASS  plan-has-topic-2  found '## Topic 2'
PASS  plan-keeps-small-town  found 'small-town'
PASS  request-note-no-edit  0 Edit call(s) matching /idea-picture-house/
PASS  request-note-no-write  0 Write call(s) matching /idea-picture-house/
PASS  schedule-names-topic  found '"research_topic": "silent-film-cinemas"'
````

`project/llm-files/research-plans/research-plan-silent-film-cinemas.md`:

````markdown
## Every topic

Keep to British cinemas in the 1920s.

## Topic 1

How did a silent film get its music in a small-town British cinema in the 1920s? Who played it: a pianist, an organist, a small band? How did they choose or get the music, such as cue sheets, published collections, or making it up on the spot? How did the music follow what was on screen?

Only small-town cinemas. Leave out the big city picture palaces.

## Topic 2

How were film prints moved from town to town in 1920s Britain? Who sent and received them, such as distributors, renters, or exchanges? How did they travel: rail, road, post, or by hand? How were they packed and handled, and how long did a cinema keep a print before it went on to the next town?
````

`run/answer.json`:

````json
{ "research_topic": "silent-film-cinemas",
  "topics": [
    { "n": 1, "waits_on": [] },
    { "n": 2, "waits_on": [] } ] }
````

Final reply:

````
```json
{ "research_topic": "silent-film-cinemas",
  "topics": [
    { "n": 1, "waits_on": [] },
    { "n": 2, "waits_on": [] } ] }
```
````

### E1: Changed number, research-evaluator agent

Case folder: `research-evaluator-01-changed-number`. Run folder: `evaluator-a2`.

#### Run 1

Grades:

````
PASS  judge-fails-on-piece-count   Evidence: - Verdict: `"verdict":"fail"` - Problem 1 names the mismatch directly: `"Note says \"A typical lancet window held about 1,200 pieces of glass.\" topic-2.md, Passage 1, says \"A typical lancet window held about 800 pieces of glass.\""` (where: "Building the window, paragraph 1") - Problem 2 also flags the piece count: `"Note says \"The piece count of about 1,200 comes from a survey of on
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"matches findings","where":"Building the window, paragraph 1","detail":"Note says \"A typical lancet window held about 1,200 pieces of glass.\" topic-2.md, Passage 1, says \"A typical lancet window held about 800 pieces of glass.\""},{"check":"matches findings","where":"Disagreement / Uncertainty, paragraph 1","detail":"Note says \"The piece count of about 1,200 comes from a survey of one cathedral's lancets\". topic-2.md, Passage 1, gives the count as about 800 pieces."}]}
````

#### Run 2

Grades:

````
PASS  judge-fails-on-piece-count   Verdict: `"verdict":"fail"`  Problems: 1. `"where":"Building the window, paragraph 1"`, `"detail":"Note says \"A typical lancet window held about 1,200 pieces of glass.\" topic-2.md, Passage 1, says \"A typical lancet window held about 800 pieces of glass.\""`. This names the piece-count mismatch directly: 1,200 in the note against 800 in the findings. 2. `"where":"Disagreement / Uncertainty, par
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"matches findings","where":"Building the window, paragraph 1","detail":"Note says \"A typical lancet window held about 1,200 pieces of glass.\" topic-2.md, Passage 1, says \"A typical lancet window held about 800 pieces of glass.\""},{"check":"matches findings","where":"Disagreement / Uncertainty, paragraph 1","detail":"Note says \"The piece count of about 1,200 comes from a survey of one cathedral's lancets\". topic-2.md, Passage 1, gives the count as about 800 pieces."}]}
````

#### Run 3

Grades:

````
PASS  judge-fails-on-piece-count   Evidence:  - **Verdict:** `"verdict":"fail"`. The check requires FAIL, and this matches. The lowercase spelling doesn't change the meaning. - **Problem 1** names the piece-count mismatch directly: `"Note says \"A typical lancet window held about 1,200 pieces of glass.\"; topic-2.md, Passage 1, says \"A typical lancet window held about 800 pieces of glass.\""` That is the exact 1,200 vs. 800 confl
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"matches findings","where":"Building the window, paragraph 1","detail":"Note says \"A typical lancet window held about 1,200 pieces of glass.\"; topic-2.md, Passage 1, says \"A typical lancet window held about 800 pieces of glass.\""},{"check":"matches findings","where":"Disagreement / Uncertainty, paragraph 1","detail":"Note says \"The piece count of about 1,200 comes from a survey of one cathedral's lancets\"; topic-2.md, Passage 1, gives the count as about 800 pieces."}]}
````

### E2: Missing question, research-evaluator agent

Case folder: `research-evaluator-02-missing-question`. Run folder: `evaluator-a2`.

#### Run 1

Grades:

````
PASS  judge-fails-on-missing-question   The verdict is `"verdict":"fail"`, which is what the check requires.  Both problems point to the missing design-planning answer:  1. The coverage problem names the question directly: *"Plan question 4 under Topic 2, \"How did glaziers plan the design before cutting?\", is neither answered in the note nor listed under Open Research Questions."*  2. The nothing-dropped problem names the whitewashed
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"coverage","where":"Building the window / Open Research Questions","detail":"Plan question 4 under Topic 2, \"How did glaziers plan the design before cutting?\", is neither answered in the note nor listed under Open Research Questions."},{"check":"nothing dropped","where":"Building the window","detail":"topic-2.md Passage 2 answers plan question 4: the glazier drew the design full size on a whitewashed wooden table, laid the cut pieces over the drawing, and washed and whitened the table again for the next design. It cites https://www.medievalcraft-journal.example/2014/theophilus-glazing. The note leaves it out and has no footnote for that URL."}]}
````

#### Run 2

Grades:

````
PASS  judge-fails-on-missing-question   The verdict is `"verdict":"fail"`.  The reply raises two problems, and both point to the missing design-planning answer:  1. Coverage problem: "Plan question 4 under Topic 2, \"How did glaziers plan the design before cutting?\", is neither answered in the note nor listed under Open Research Questions." 2. Nothing-dropped problem: "topic-2.md Passage 2 answers plan question 4. It says \"the glazie
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"coverage","where":"Building the window, and Open Research Questions","detail":"Plan question 4 under Topic 2, \"How did glaziers plan the design before cutting?\", is neither answered in the note nor listed under Open Research Questions."},{"check":"nothing dropped","where":"Building the window","detail":"topic-2.md Passage 2 answers plan question 4. It says \"the glazier drew the design full size on a whitewashed wooden table. The pieces were cut and laid out over the drawing. When the panel was finished, the table was washed and whitened again for the next design.\" Its URL is https://www.medievalcraft-journal.example/2014/theophilus-glazing. The note leaves this out, and the URL is not in its Sources."}]}
````

#### Run 3

Grades:

````
PASS  judge-fails-on-missing-question   The verdict is `"verdict":"fail"`, which is FAIL.  Two of its problems name the missing design question and the whitewashed table:  1. Coverage problem: *"Plan question 4 under Topic 2, \"How did glaziers plan the design before cutting?\", is neither answered in the note nor listed under Open Research Questions."* 2. Nothing-dropped problem: *"topic-2.md Passage 2 answers plan question 4. It says
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"coverage","where":"Building the window / Open Research Questions","detail":"Plan question 4 under Topic 2, \"How did glaziers plan the design before cutting?\", is neither answered in the note nor listed under Open Research Questions."},{"check":"nothing dropped","where":"Building the window","detail":"topic-2.md Passage 2 answers plan question 4. It says the glazier \"drew the design full size on a whitewashed wooden table\", the pieces were cut and laid out over the drawing, and the table was washed and whitened again for the next design. It has a URL (medievalcraft-journal.example/2014/theophilus-glazing). The note leaves it out."}]}
````

### E3: Foreign URL, research-evaluator agent

Case folder: `research-evaluator-03-foreign-url`. Run folder: `evaluator-a2`.

#### Run 1

Grades:

````
PASS  judge-fails-on-foreign-url   Evidence:  - **Verdict:** `"verdict": "fail"`. This is FAIL, as the check requires. - **Problem 1** (`"where": "Building the window, paragraph 1"`) names both footnote 6 and the URL, and says it is not from the findings: "cites footnote 6, https://www.glass-history-blog.example/2022/lancet-windows. That URL appears in no findings file." - **Problem 2** (`"where": "Disagreement / Uncertainty, para
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{ "verdict": "fail",
  "problems": [
    { "check": "matches findings", "where": "Building the window, paragraph 1",
      "detail": "The claim \"A typical lancet window held about 800 pieces of glass.[^5][^6]\" cites footnote 6, https://www.glass-history-blog.example/2022/lancet-windows. That URL appears in no findings file. topic-2.md Passage 1 gives the 800-piece claim these URLs: stainedglassmuseum.example/collections/how-a-window-is-made and archaeology-review.example/2018/chartres-lancet-survey. The note's Sources section never lists the archaeology-review URL." },
    { "check": "matches findings", "where": "Disagreement / Uncertainty, paragraph 1",
      "detail": "The claim \"The piece count of about 800 comes from a survey of one cathedral's lancets and may not hold elsewhere.[^6]\" rests on footnote 6, glass-history-blog.example, which is in no findings file. topic-2.md Passage 1 attributes the survey to https://www.archaeology-review.example/2018/chartres-lancet-survey." } ] }
```
````

#### Run 2

Grades:

````
PASS  judge-fails-on-foreign-url   The verdict is a failure: `"verdict": "fail"`. The check wants FAIL, and lowercase "fail" says the same thing.  Both problems point to footnote 6 and that URL as not coming from the findings.  - Problem 1 (Building the window, paragraph 1): "cites [^6], https://www.glass-history-blog.example/2022/lancet-windows. That URL appears in no findings file." - Problem 2 (Disagreement / Uncertainty, parag
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{ "verdict": "fail",
  "problems": [
    { "check": "matches findings", "where": "Building the window, paragraph 1",
      "detail": "The sentence \"A typical lancet window held about 800 pieces of glass.[^5][^6]\" cites [^6], https://www.glass-history-blog.example/2022/lancet-windows. That URL appears in no findings file. topic-2.md Passage 1 gives the 800-piece claim these URLs: stainedglassmuseum.example/collections/how-a-window-is-made and archaeology-review.example/2018/chartres-lancet-survey." },
    { "check": "matches findings", "where": "Disagreement / Uncertainty, paragraph 1",
      "detail": "The note says \"The piece count of about 800 comes from a survey of one cathedral's lancets and may not hold elsewhere.[^6]\" Footnote 6 is a URL found in no findings file. The survey URL in topic-2.md Passage 1 is https://www.archaeology-review.example/2018/chartres-lancet-survey, and it is missing from the Sources section. The Reliability section names archaeology-review.example, but no footnote points to it." }
  ] }
```
````

#### Run 3

Grades:

````
PASS  judge-fails-on-foreign-url   Verdict: `"verdict": "fail"`. That matches the expected FAIL, case-insensitively.  Both problems name footnote 6 and the glass-history-blog URL as not coming from the findings:  1. Problem 1, at "Building the window, paragraph 1": "cites footnote 6, https://www.glass-history-blog.example/2022/lancet-windows. That URL appears in neither topic-1.md nor topic-2.md." 2. Problem 2, at "Disagreement / 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{ "verdict": "fail",
  "problems": [
    { "check": "matches findings", "where": "Building the window, paragraph 1",
      "detail": "The sentence \"A typical lancet window held about 800 pieces of glass.[^5][^6]\" cites footnote 6, https://www.glass-history-blog.example/2022/lancet-windows. That URL appears in neither topic-1.md nor topic-2.md. Topic-2.md Passage 1 lists only stainedglassmuseum.example/collections/how-a-window-is-made and archaeology-review.example/2018/chartres-lancet-survey. The footnote should be the archaeology-review URL." },
    { "check": "matches findings", "where": "Disagreement / Uncertainty, paragraph 1",
      "detail": "The note says \"The piece count of about 800 comes from a survey of one cathedral's lancets and may not hold elsewhere.[^6]\". Footnote 6 is the glass-history-blog URL, which is in no findings file. Topic-2.md Passage 1 attributes this survey to https://www.archaeology-review.example/2018/chartres-lancet-survey, and that URL is not in the Sources section." }
  ] }
```
````

### E4: Clean note, research-evaluator agent

Case folder: `research-evaluator-04-clean-note`. Run folder: `evaluator-a2`.

#### Run 1

Grades:

````
PASS  judge-passes-clean-note   The reply's verdict is PASS: `{"verdict": "pass", "problems": []}`. It lists no problems, so there's no invented problem to quote.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "pass", "problems": []}
````

#### Run 2

Grades:

````
PASS  judge-passes-clean-note   The reply's verdict is PASS: `{"verdict": "pass", "problems": []}`. The `"verdict"` field reads `"pass"` (lowercase, but clearly PASS). The `"problems"` array is empty, so no problems are listed and none were invented.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "pass", "problems": []}
````

#### Run 3

Grades:

````
PASS  judge-passes-clean-note   The reply's verdict is PASS: `{"verdict":"pass","problems":[]}`. The `"problems"` list is empty, so it names no invented problem.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"pass","problems":[]}
````

### W6: Eight topics, bare claude-opus-5-5

Case folder: `research-writer-06-eight-topics`. Run folder: `bare-w6w8`.

#### Run 1

Grades:

````
FAIL  fm-author  no match; read Light Research - Ice Trade.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-09'; read Light Research - Ice Trade.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-09'; read Light Research - Ice Trade.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - Ice Trade.md in its place
PASS  fm-sources-empty  found 'sources:'; read Light Research - Ice Trade.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - Ice Trade.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - Ice Trade.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - Ice Trade.md in its place
PASS  judge-footnotes-resolve   **Markers to definitions:** Every marker in the body falls in the range [^1] to [^91]. Each of these numbers has exactly one definition line under Sources. No body marker lacks a definition, and none falls outside the range.  **Every definition has a URL:** All 91 definition lines start with an `https://` URL. For example: - "[^1]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-o [read Light Research - Ice Trade.md in its place]
PASS  judge-planted-details-cite-own-url   All eight details appear in the note, and each carries a footnote whose Sources entry is the expected URL.  1. **Topic 1, the 22-inch blocks.** The note says: "The field was then cross-scored at right angles into a grid of **22-inch squares**.[^8]" Under Sources: "[^8]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s". This matches.  2. **Topic 2, the 17% storage loss.** The  [read Light Research - Ice Trade.md in its place]
PASS  judge-reply-no-cut-short   The reply names no topic or file as cut short. It says outright: "**Cut short:** none. All eight findings files end with the `<!-- end of findings -->` marker, and none has a passage that stops partway."  Elsewhere the reply mentions that "The findings had no wage figures and no prices for Havana, Madras or Bombay." That describes missing content, not a truncated file. No topic is called incomple
PASS  judge-sixteen-questions-answered   All sixteen questions are answered with the findings' answers. Nothing listed under Open Research Questions contradicts an answered question.  1. **Cutting season and thickness:** "usually mid-January into February, after a long hard freeze"; "not cut until it was at least **14 inches** thick, and only clear ice counted"; "Each morning the foreman bored test holes with a hand auger." 2. **Tools a [read Light Research - Ice Trade.md in its place]
PASS  keeps-t1-14-inches  found '14 inch'; read Light Research - Ice Trade.md in its place
PASS  keeps-t1-22-inch-blocks  found '22-inch'; read Light Research - Ice Trade.md in its place
PASS  keeps-t2-17-percent-loss  found '17%'; read Light Research - Ice Trade.md in its place
PASS  keeps-t2-9400-tons  found '9,400'; read Light Research - Ice Trade.md in its place
PASS  keeps-t3-pumped-every-4-hours  found '4 hours'; read Light Research - Ice Trade.md in its place
PASS  keeps-t3-sawdust-1-to-11  found '11 tons'; read Light Research - Ice Trade.md in its place
PASS  keeps-t4-130-days  found '130 days'; read Light Research - Ice Trade.md in its place
PASS  keeps-t4-38-percent-loss  found '38%'; read Light Research - Ice Trade.md in its place
PASS  keeps-t5-1250-tons  found '1,250'; read Light Research - Ice Trade.md in its place
PASS  keeps-t5-barcia  found 'Barcia'; read Light Research - Ice Trade.md in its place
PASS  keeps-t6-75-men  found '75'; read Light Research - Ice Trade.md in its place
PASS  keeps-t6-nine-drownings  found 'nine drown'; read Light Research - Ice Trade.md in its place
PASS  keeps-t7-2-half-cents  found '2½'; read Light Research - Ice Trade.md in its place
PASS  keeps-t7-3-annas  found '3 annas'; read Light Research - Ice Trade.md in its place
PASS  keeps-t8-12-tons-a-day  found '12 tons'; read Light Research - Ice Trade.md in its place
PASS  keeps-t8-margaret-ellery  found 'Margaret Ellery'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-1  found 'https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-2  found 'https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-3  found 'https://www.maritime-salem.example/papers/stowing-ice-1850'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-4  found 'https://www.ice-trade-voyages.example/logs/calcutta-melt-study'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-5  found 'https://www.havana-archive.example/colonial-trade/ice-depot-1840s'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-6  found 'https://www.labor-history-ne.example/winter-work/harvest-crew-sizes'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-7  found 'https://www.gulf-commerce.example/price-current/ice-1860'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-8  found 'https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882'; read Light Research - Ice Trade.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - Ice Trade.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - Ice Trade.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - Ice Trade.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - Ice Trade.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - Ice Trade.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - Ice Trade.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-1-section  found '## Cut'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-2-section  found '## Stor'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-3-section  found '## Load'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-4-section  found '## The voyage'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-5-section  found '## Ice houses at the far port'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-6-section  found '## The worker'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-7-section  found '## Buyers and price'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-8-section  found '## The end'; read Light Research - Ice Trade.md in its place
FAIL  file-name  wrote Light Research - Ice Trade.md instead
````

`project/Research/Light Research - Ice Trade.md`:

````markdown
---
title: Light Research - Ice Trade
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-09 14:00
modified: 2026-10-09 14:00
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> How the New England ice trade by sea worked, from the trade's start (1806) to its end (1880s and after): cutting the ice on the ponds, storing it before shipping, loading the ship, the voyage and how much melted, the ice houses at the far ports, the workers, the buyers and prices, and what ended the trade. From the request in `project/Ideas/idea-ice-ship.md` (line 9), with the comment "The New England trade by sea, start to finish."  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Ice Trade

## Summary

> [!tip]-  
> A concise synthesis of the most important findings.
> 
> Focus on what is useful to understand about the subject without translating those findings into story decisions.

The trade began in 1806, when Frederic Tudor sent a cargo from Boston to Martinique. There was no ice house to receive it, and most of it melted on the wharf.[^39] By the 1820s Tudor was shipping regularly to Havana and the southern US ports. The trade peaked around 1860 and was nearly over by the 1880s.[^30][^78]

**The chain.** The work ran in this order:

1. In January and February, crews cut clear ice at least 14 inches thick from spring-fed ponds such as Fresh Pond, Wenham Lake and Spy Pond. They used horse-drawn markers and ploughs (designed by Nathaniel Wyeth, 1825–29) that turned out regular 22-inch blocks.[^1][^6][^8]
2. The blocks were stored in huge double-walled, sawdust-filled icehouses on the pond shore. The largest held about 9,400 tons. One 1847 ledger records a 17% loss over the season.[^17][^23]
3. A rail branch carried the ice to the Charlestown wharves.[^26] It was stowed tight in ordinary merchant ships that would otherwise have sailed in ballast. Each hold got a sawdust-packed "ice ceiling" lining, and the hatches were sealed for the whole voyage.[^29][^32][^37]
4. Voyages took 2–3 weeks to the Caribbean and about 130 days to Calcutta.[^41][^42] Calcutta voyages lost 38% of the ice on average. Short routes often lost under a tenth.[^47][^30]
5. At the far ports the ice went into purpose-built ice houses, such as Calcutta's round brick house holding about 1,250 tons. Agents sold it by weight in the early morning only.[^50][^60]

**Workers.** Local farmers, Irish immigrants from the 1840s and later French-Canadians did the cutting. Waterfront stevedores loaded the ships, and local porters (in Havana, hired enslaved men) unloaded them at the far end.[^63][^64][^66][^35][^68]

**Buyers and prices.**
- Calcutta: British residents, wealthy Indian merchants, hospitals and clubs. Ice sold at 3 annas a pound in the 1830s–40s.[^60]
- New Orleans: the largest market. By 1860 ice sold at about 2½ cents a pound to ordinary households.[^44][^75]

**The end.** No single cause ended the trade. The causes were:
- the Civil War blockade of the southern ports
- ice-making machines (New Orleans' first factory opened in 1868; Indian factories followed in the late 1870s)
- steamships and the Suez Canal, which removed the cheap outward sailing ships
- a booming home market for natural ice[^79][^83][^85][^41][^78]

The last recorded Calcutta cargo sailed in 1882 on the bark *Margaret Ellery*.[^90] Sources disagree about when the last ice went by sea to anywhere.[^25]

## Cutting the ice on the ponds

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**When and where.** The harvest ran in the coldest weeks, usually mid-January into February, after a long hard freeze.[^1] Firms preferred spring-fed ponds with no inflowing streams. Moving water froze unevenly and carried silt, leaves and mill sawdust into the ice. The best-known ponds were Fresh Pond (Cambridge), Wenham Lake (north of Salem) and Spy Pond (Arlington). Firms bought or leased shore rights so rivals could not cut there.[^1][^2]

**Thickness.** Ice was not cut until it was at least **14 inches** thick, and only clear ice counted. White "snow ice" on top did not. Thinner ice crumbled at the corners, wasted hold space and melted faster. Each morning the foreman bored test holes with a hand auger and logged the readings. Cutting often began near the shaded shore and moved outward as the ice thickened.[^1][^3]

**Snow and flooding.** Snow slowed freezing and turned into weak snow ice. Horse-drawn wooden scrapers cleared it. On some ponds crews bored holes and flooded the cleared surface so a fresh layer froze on top. This only worked in hard cold. Snow ice was planed off each block before storage.[^4][^5]

**Tools.** Before the 1820s ice was cut by hand with axes, saws and chisels. The blocks came out irregular, stacked badly and let in warm air. Nathaniel Jarvis Wyeth designed a horse-drawn cutter in 1825 and patented an improved version in 1829. His tools made regular blocks that stacked tightly, and historians credit this with making long voyages possible. By the 1840s most commercial Massachusetts ponds used some version of them.[^6][^7]
- The **marker** was a plough-like frame with a row of steel teeth, drawn by one horse along a cord line. A guide arm kept each groove parallel to the last. The field was then cross-scored at right angles into a grid of **22-inch squares**.[^8]
- The **plough** had longer teeth and was run along the grooves until each cut went about two-thirds through the ice. The remaining third held the field together for men and horses to walk on.[^8]
- **Long hand saws** opened a channel to shore.[^9]
- **Breaking bars** were flat chisels on long handles. They split the field into rafts and then single blocks along the grooves.[^9][^10]
- **Pike poles** had an iron hook and spike. They pushed the floating blocks along the channel to shore.[^9][^10]
- An **inclined elevator** was a ramp with an endless cleated chain. A horse at a capstan drove it, or from the 1850s a small steam engine. It lifted blocks to the icehouse door, and blocks were planed flat top and bottom first.[^1][^11]
- By the 1850s complete tool sets were sold by specialist makers, many in the Hudson valley. A set included markers, ploughs, saws up to six feet long, bars, pike poles, tongs and scrapers. Tools changed little over the life of the trade.[^13][^6]

**Block size and weight.** Blocks were 22 inches square on the surface. A first-quality block weighed roughly **200 pounds** by the firm's working figure. The harvest was counted in blocks by a tally man at the top of the elevator and converted to tons. Pond owners were usually paid by the ton.[^8][^12]

## Storing the ice before shipping

**Construction.** The shipping firms built above-ground icehouses on the pond shore, so blocks went straight from the channel up the elevator. This replaced the older farm pits, which held only a few tons and let in groundwater.[^17][^18]
- **Walls:** two wooden walls (sometimes three) with the gap packed with sawdust or spent tanbark. Tudor and Wyeth ran trial houses in the 1820s–30s and found dry fill far better than damp. Wide eaves kept rain out of the fill.[^19][^6]
- **Roof:** steep, with louvred ridge vents to let warm air escape. Houses were usually painted white, and sometimes hay or straw was laid in the roof space.[^21][^18]
- **Floor:** a gravel or broken-stone bed with a drain to the pond, covered with sawdust. Melt had to drain at once, because ice standing in water melted much faster than ice in air.[^19]
- **Layout:** big houses were built as a row of rooms under one long roof. Each room was filled and emptied on its own. A stack of doors on the elevator side was boarded shut as the ice rose past each one.[^17][^20]
- **Stacking:** blocks were set on edge, tight together, with each layer crossing the one below like brickwork. Gaps were filled with chips, and the top was covered with deep hay or sawdust.[^17][^10]

**Capacity.** The biggest Fresh Pond house held about **9,400 tons** and stood taller than a three-storey building. It took the whole of a good harvest from a large pond. Smaller firms' houses held a few hundred tons.[^17][^20] Smaller icehouses on the Charlestown wharves, also holding a few hundred tons each, kept ice for a few days before a sailing.[^27]

**Loss in storage.** The only surviving whole-season ledger for a single house is from a Fresh Pond icehouse in 1847. It shows a loss of about **17%** between the end of the harvest in March and the last autumn sailing. Most of the loss came in July and August, and the keeper blamed the heat and a roof vent left shut. Historians treat it as the standard figure.[^23] A room left unopened until autumn lost less than one opened in June.[^23] Larger houses lost proportionally less than small ones, which is why firms kept building bigger houses through the 1840s–50s.[^25][^18] See Disagreement for the wider ranges given elsewhere.

**Keepers.** Each large house had a keeper who lived beside it all year, often in a cottage against the end wall. The keeper checked drains and vents, kept the ledger of ice in and out, and chose which room to open for each order, oldest ice first. Keepers wrote to the Boston office about once a week.[^22][^3] From the 1850s some keepers logged thermometer readings above the stack.[^22]

**Taking ice out.** Ice was taken from the top of the stack down, one room at a time, and the doors were shut again the same day. Blocks that had frozen together were broken apart with bars and scraped clean of fill before loading.[^3][^14] From the early 1840s a rail branch ran from Fresh Pond to the Charlestown wharves in under an hour. It used sawdust-insulated wagons, and trains ran at night in summer.[^26][^17]

## Loading the ship

**The ships.** These were ordinary merchant ships, not purpose-built. Many would otherwise have left Boston in ballast, because Boston imported far more from the tropics than it exported. Ice gave them a paying outward cargo at low freight rates, and this cheap carriage was key to the trade's profit. Older ships were often chosen because the hold had to be altered.[^29][^30] Holds were swept, scrubbed and aired. Ships that had carried fish, hides, molasses or coal were avoided, because smells and coal dust passed into the ice.[^31]

**Lining ("ice ceiling").** A carpenter built an inner wall of pine planks a little way in from the hull on all sides, across the floor and up under the deck beams. The gap was packed with sawdust, giving a box inside the hull on the icehouse plan. A carpenter and two helpers took about a week for a middling ship. The lining was taken out at the far port, and the planks were often sold there.[^32][^29]

**Floor and drainage.** Rough timber dunnage was laid over the hull bottom, then the lining floor, then a deep bed of sawdust. Gaps at the sides let melt run into the bilge for pumping. A badly built floor left the bottom layer standing in water, and this was the largest single loss on most recorded voyages.[^32]

**Packing.**
- Stevedores lowered the blocks through the hatch in slings and stowed them as in the icehouse: on edge, tight together, with layers crossed.[^35][^29]
- Every gap was filled with chips and sawdust, at a ratio of **one ton of sawdust to 11 tons of ice** (a Salem merchant's printed paper of 1850).[^33]
- Sawdust was pine waste from the Maine mills, brought by schooner. It had to be dry, because wet sawdust froze into a heat-conducting crust. Loads were priced by dryness.[^34][^29][^33]
- Ice was stowed low and evenly from bow to stern. Ships carried less than their rated tonnage because of the weight and space of the lining and sawdust.[^32][^36]
- A middling ship was loaded in **one to two days**, working at night or early morning, and sailed on the next tide.[^35][^37]

**Keeping it from melting or shifting at sea.**
- The top of the stack was covered with sawdust and then hay. The hatches were closed, covered with tarred canvas and battened down. Some ships fitted a second inner hatch with sawdust between the two.[^32][^36]
- Hatches stayed sealed until port. Some joins were waxed or pitched so tampering would show, and a master who opened them without cause answered for the lost ice.[^37]
- Timber battens were driven between the stack and the lining, and the top layers were wedged against the deck beams to stop shifting. Logbooks record voyages where heavy weather loosened the stack and the cargo arrived much reduced.[^36]
- The bilge was pumped **every 4 hours**, day and night. The mate logged the strokes needed, which were the only measure of how fast the ice was melting. A sudden rise meant the stow had shifted or the lining had broken.[^36]
- Insurers excluded melting losses (in early years they refused ice cargoes altogether), so the shipper bore the whole risk of melt.[^38][^30]

## The voyage

**Routes and durations.**

| Route | Typical duration | Notes |
|---|---|---|
| Boston–Calcutta | about 130 days | Via the Cape of Good Hope, crossing the equator twice, then up the Hooghly River. The longest regular route.[^41][^36] |
| Boston–Caribbean (Havana, Martinique, Jamaica, etc.) | 2–3 weeks with fair winds | Havana was one of the steadiest markets, with ships every few weeks.[^42][^43] |
| Boston–southern US (Charleston, Savannah, Mobile, New Orleans) | several weeks to New Orleans | The largest market by volume. By the 1850s New Orleans took more New England ice than any other port in the world.[^44][^30] |
| Other | not given | Rio de Janeiro, Valparaíso, Bombay, Madras, Hong Kong, a few to Australia. Less regular, and some routes were given up.[^30][^45] |

- The first Calcutta cargo sailed in May 1833 on the *Tuscany* and arrived in September. It was a sensation in the city and made a profit.[^46][^41]
- Calcutta sailings left Boston in autumn and early winter to arrive in the hot season (about March–June). The cold first weeks cost almost no ice.[^41][^30]
- Fast ships were preferred for India, cheap ones for the short routes.[^41] From the 1840s steam tugs towed ships up the Hooghly in a day or less.[^48][^31]

**Melt loss.**
- Most melting happened in the tropics. Pumping strokes were low in the first weeks out and rose sharply near the equator. On the Calcutta route the second tropical crossing, at the end of the voyage, was the worst.[^36]
- A study of surviving logbooks and cargo receipts for the Calcutta run found an average loss of **38%** between Boston and Calcutta, varying widely by season, length of voyage and stow.[^47]
- Caribbean and southern routes often lost **under a tenth** on a well-stowed cargo.[^30]
- Calms (the doldrums) were especially costly. Masters were told to keep moving at all costs.[^36][^37]

## Ice houses at the far ports

**Building first.** After the Martinique failure of 1806, firms built or rented an ice house in each port before sending regular cargoes. Some were converted warehouses with added inner walls, others new buildings. Carpenters were sent from Boston with the first cargo.[^39][^25]

**Construction and capacity.**
- **Calcutta:** paid for by a subscription among the city's merchants after the 1833 cargo, and opened a few years later. A round brick building near the river with thick double walls, a domed roof over a ventilated space, and a floor draining to the river. It held about **1,250 tons**. It was brick because wood suffered from termites and monsoon rot.[^50][^51][^52]
- **Havana:** built by the Tudor firm near the harbour in the 1820s. It was partly sunk below street level, where the earth was cooler.[^54][^53][^52]
- **New Orleans:** several large houses on the levee by the 1840s, owned by competing firms. They stood fully above ground because the ground was wet, and sat next to the unloading wharves.[^44][^56][^53]
- **Bombay and Madras:** built late 1830s/early 1840s on the Calcutta model, with masonry walls and drained floors, smaller than Calcutta. The Madras house stood by the beach, because ice came ashore through the surf in small boats.[^52][^57]
- **Charleston and Savannah:** smaller wooden houses on the Boston plan, raised on brick piers. They held a few weeks' stock and were often owned by local merchants who bought whole cargoes.[^58][^44]
- **Hong Kong:** a granite waterfront house of the 1840s. The trade there was small and irregular.[^59]

Losses in the tropical houses ran higher, month for month, than any recorded at the ponds, so agents tried to sell each cargo before the next arrived.[^31]

**Who ran them.** Each house was run by the firm's agent, either a local merchant or a young man sent from Boston, usually paid a share of sales.[^31] In Havana the agent was local merchant **Joaquín Barcia** through the 1840s, under a Spanish colonial monopoly that required the firm to keep the city supplied.[^55][^54] The Calcutta agent came from Boston and had local staff. He also answered to the merchants' committee that had funded the building.[^31][^50]

**How the ice was sold.**
- **By weight:** on a scale at the door. Some houses kept blocks pre-cut to standard weights.[^44][^60]
- **Opening hours:** first light to mid-morning only. Calcutta printed its hours in the newspapers and turned latecomers away.[^50][^60]
- **Tickets:** in Havana, customers bought a ticket for a set weight at the city office and redeemed it at the house door, so no money changed hands there.[^55]
- **Accounts:** hotels, clubs, hospitals and military messes were billed monthly and often served before the queue.[^60][^31]
- **Delivery:** New Orleans carts delivered in insulated boxes by the 1850s. Delivery was rare in Havana and Calcutta.[^44]
- **Carrying home:** customers wrapped ice in blankets or flannel in baskets or cloth-lined boxes, and it lasted a day or so. Wealthier households bought Boston-made ice chests.[^61][^50]
- **Promotion:** in new ports agents first gave ice away and showed bar owners, cooks and doctors how to use it.[^39][^62]

## The workers

**Who did the work.**
- **Pond crews:** at first local farmers and their sons in the farming slack season. They brought their own horses and were paid for man and horse.[^63][^1] From the 1840s more and more were Irish immigrants, many arriving during and after the famine, who mostly got the unskilled jobs.[^64][^65] In later decades French-Canadians came, some from New England mill towns and some down from Quebec for the season. By the 1870s some crews were mostly French-Canadian.[^66]
- **Boys:** from about age twelve, for lighter jobs such as guiding blocks along the channel, sweeping chips and carrying messages. They were paid less.[^10][^63]
- **Women:** did not work on the ice. They ran boarding houses, cooked and washed, and ran the farms while the men were away.[^63][^12]
- **Ship loading:** a separate, year-round waterfront workforce of stevedores in gangs under a boss who contracted per ship, paid by the ton loaded.[^35]
- **Far ports:** in Calcutta, porters hired by the agent. In Havana, enslaved men hired from their owners.[^68][^31]

**How crews were organised.**
- A large pond's crew numbered about **75 men**, in gangs working in sequence: snow scrapers, marker and plough, bar men, channel men, elevator, and stackers. A smaller pond used about a third as many.[^67]
- Each crew had a foreman under the firm's pond superintendent.[^67][^3]
- Labourers were hired by the day at the pond edge, with no promise of the next day's work.[^10]
- Skilled men (marker drivers, bar men, stackers) were hired for the season at higher pay and asked back each year.[^3][^63]
- Pay came weekly on Saturday evening at the shore shanty, with board deducted.[^12]

**Working conditions.**
- The working day ran from first light to dark. Before a forecast thaw crews worked into the night by lantern and on Sundays, with no extra pay unless the foreman agreed.[^15]
- Cold and frostbite were constant. Men wore layers of wool, felt boots with overshoes and iron "creepers" strapped to their boots.[^10][^69]
- The firms fed the crews on large ponds, with hot coffee and soup in the shore shanty and a midday meal.[^10]

**Dangers.**
- **Falling through.** This was the worst danger. A newspaper count records **nine drownings** on the Cambridge ponds in 1850–60, mostly men falling into the open channel at night. There were no railings or lights until late in the trade.[^69][^15]
- **Wet clothing.** A man who got wet could freeze before reaching shelter.[^10][^69]
- **Injuries.** Men were hurt by saws and bars and crushed by blocks slipping on the elevator or stacks shifting. There was no pay beyond days already worked.[^69][^10]
- **Labour tensions.** Fights broke out between local and Irish men.[^65][^70] Strikes in the 1850s–60s timed to forecast thaws lasted a day or two and were followed by blacklists.[^71][^64]
- **Open winters.** A mild winter meant no harvest and no winter wage, and Boston charities saw more families seeking help.[^72]

## Buyers and prices

**Who bought.**
- **Calcutta:** at first British residents (East India Company officials, officers, merchants). Wealthy Indian merchant and landowning families bought from the early years and were a large share of private customers by the 1840s. Hospitals and clubs/messes were among the biggest accounts. Most of the population could not afford ice.[^50][^61][^60][^73]
- **Bombay and Madras:** much the same mix, including Parsi merchant families.[^57][^74]
- **Havana:** cafés, confectioners (ices and sorbets) and wealthy households. Within a generation ice spread from a luxury to a common café pleasure.[^54][^62]
- **New Orleans:** bars serving every class, hotels, households, meat and fish markets, and river steamboats, which also carried the habit to upriver towns. By the 1850s the press called ice a necessity.[^44][^76][^77]
- **Charleston and Savannah:** planters, merchants, hotels and taverns.[^58]
- **Hong Kong:** the garrison, trading-house merchants and ships in harbour.[^59]
- **Everywhere:** hospitals, especially for fevers. In New Orleans that meant the yellow fever epidemics of the 1850s.[^73]

**What it cost.**
- **Calcutta:** **3 annas a pound** at the door (an anna = 1/16 rupee). The price held steady through the 1830s–40s. Account customers sometimes paid less, and hospitals got a reduced contract rate.[^60][^30][^73]
- **New Orleans:** prices fell steadily from the 1830s to the 1850s as competing firms arrived. By 1860 ice sold for **about 2½ cents a pound** on the levee (city "price current"), rising in hot months and when ships were late.[^44][^30][^75]
- **Havana:** a maximum price fixed under the monopoly and revised several times by the colonial government. No figure is recorded in the findings.[^54]
- **Madras and Bombay:** higher than Calcutta.[^57][^74]
- **Every port:** the price was lowest just after a ship arrived and highest when the stock ran low.[^60][^43]
- **Price wars:** periodic undercutting between Boston firms gave buyers spells of cheap ice.[^31][^30]
- **Where the money went:** the ice cost almost nothing at the pond. On long routes the largest single cost was ice lost to melting, larger than freight.[^30]

## The end of the trade

**What ended it.** Several changes came together after a peak around 1860, and their order differed by port.[^30][^78]
- **Civil War (1861–65):** the Union blockade closed the southern ports. New Orleans was shut to Boston ships until 1862. Carré ice machines were smuggled in through the blockade, number unknown. After the war, southern cargoes stayed well below 1850s levels.[^79][^80][^44]
- **Ice machines:** Gorrie patented one in 1851, Carré developed an ammonia machine in the late 1850s, and Harrison built machines in the 1850s.[^81][^82]
  - New Orleans' first commercial factory opened in **1868**, making about 12 tons a day at first.[^83][^44]
  - Through the 1870s factory ice became cheaper than shipped ice, once melt loss was counted.[^30]
  - Boston firms tried price-cutting against the factories, which closed a few small ones but could not last.[^44]
  - Early factory ice was cloudy and distrusted. By the 1880s the best was as clear as pond ice.[^81][^84]
  - Calcutta had a factory by the late 1870s, and Bombay and Madras followed.[^85][^50]
  - Havana's monopoly lapsed after the US war, and local factories opened in the 1870s.[^54][^88]
- **Steamships:** after the Suez Canal opened in 1869, the supply of cheap outward sailing ships to Asia shrank.[^41][^30]
- **Home market:** booming demand for natural ice in US cities and refrigerated rail cars meant the ponds could sell everything by rail with far less loss.[^13][^78]
- **Other factors:** urban growth fouled the ponds near Boston, and Fresh Pond became Cambridge's water supply.[^86] Tudor died in 1864, and the founding firms faded or merged.[^87][^25]

**When the last cargoes sailed.**
- **Calcutta:** the trade dwindled through the 1870s, some years seeing only one or two ships. The **last recorded cargo** sailed from Boston in **1882** on the bark *Margaret Ellery*, arriving "in fair condition." No later ice ship appears in the Calcutta register.[^89][^90]
- **Bombay and Madras:** the trade there ended before Calcutta's.[^89]
- **Havana:** shipped ice kept arriving in falling amounts into the 1870s.[^88]
- **Overall:** whether the sea trade ended in the 1880s or ran on into the 1890s and 1900s is disputed (see below). The end went unreported in the Boston papers.[^25][^78][^91]

## Disagreement / Uncertainty

> [!tip]-  
> Claims that are disputed, uncertain, incomplete, changing, or dependent on interpretation.
> 
> Distinguish clearly between:
> 
> - established fact
> 
> - expert consensus
> 
> - plausible interpretation
> 
> - contested claim
> 
> - anecdotal evidence
> 
> - speculation

- **Storage loss (contested figures).** The 1847 Fresh Pond ledger records about 17%. It is a documented primary record, and historians treat it as the standard figure.[^23] A popular history says well-built houses lost a fifth to a third over a summer, and small houses up to half, but gives no source.[^25] The two may also differ by method: ledgers kept by counting blocks show smaller losses than ledgers kept by weighing, and the two kinds of figure cannot be compared directly. The 1847 ledger weighed sample blocks.[^24][^18]
- **Calcutta voyage loss (contested figures).** The logbook study's average is 38%, based on primary records. The authors note the surviving papers may favour better-run voyages, so the true average could be higher.[^47] A general history says about a quarter for well-stowed ships, blaming poor stowage for anything higher, with no stated source. Neither source says which years its figure covers, and stowing improved over time.[^25]
- **Short-route loss.** The "under a tenth" figure is an estimate from a small number of voyages.[^30]
- **When the trade ended (contested).** Some histories say the early 1880s. A general history says Caribbean cargoes ran irregularly into the 1890s, with occasional southern shipments into the early 1900s, but gives no source. The difference may come from what counts as "the trade."[^25][^78] The 1882 *Margaret Ellery* voyage is the last *recorded* Calcutta cargo, not necessarily the last ice by sea.[^90]
- **Calcutta ice house after the factory.** One source says the house lost its trade within a few years of the late-1870s factory opening.[^85] Another records an 1882 ice cargo consigned to the ice house company, after which it sold only factory ice.[^90] Both can be true, but the exact timing is unclear.
- **Block weight.** The 200 lb figure is the firm's working figure, not a measured average.[^12]
- **Drownings.** The nine-drowning count (1850–60) comes from newspaper reports and may be an undercount.[^69]
- **Machines through the blockade.** The number of Carré machines smuggled in is unknown.[^80]
- **Price-cutting against factories.** The claim that this closed a few factories comes with no list of which ones.[^44]
- **Havana's later years.** The colonial records end before the monopoly's final years. The later account rests on a research project.[^88]
- **Anecdotal material.** The fish-tasting cargo comes from one agent's letter.[^31] Remarks about ships rolling more as the ice melted are masters' comments, not measurements.[^36] The rope method of rescuing horses rests on oral histories and one magazine piece.[^10][^5]

## Useful Details

> [!tip]-  
> Interesting or potentially useful details that do not belong cleanly elsewhere.
> 
> These may include small behavioral, material, procedural, linguistic, visual, environmental, or cultural observations.

**On the ponds**
- Foremen kept daily notebooks of dawn and noon temperature, wind and snowfall.[^1]
- One firm told foremen to reject any block "they would not want to see on a dinner table." Second-quality (cloudy) ice went to Boston households and butchers.[^3][^14]
- To test clarity, foremen held a test block against the light. If a dark object showed clearly through its whole thickness, it was good enough to ship.[^10]
- Horses wore sharp-calked shoes, and a blacksmith stayed near large ponds. A horse that broke through was rescued by looping a rope round its neck and pulling it tight, which made it hold its breath and float higher.[^10][^5]
- An "open winter" (too mild to cut) forced firms to buy ice from Maine and New Hampshire. Crews cut on Sundays when a thaw was forecast, against local custom.[^15][^16]
- Pond owners sometimes sent their own tally man, and disputes over the count survive in letters.[^12]

**In storage**
- Icehouses burned easily. Dry sawdust and hay could be set alight by sparks from railway engines. The ice usually survived the fire as a block in the ruins, then melted within days.[^28][^18]
- One keeper was dismissed for letting a drain freeze, which flooded the lowest room.[^19]

**At sea**
- Sailors called the hold lining the "ice ceiling."[^32]
- Early sailors feared melting ice would sink the ship, and some deserted before sailing. By the 1840s men experienced in the pumping routine were valued.[^39][^25]
- Masters kept a separate printed "ice book" recording position, deck and sea temperature, and pumping strokes.[^36][^37]
- Apples, butter and cheese rode in pockets cut into the stack as private trade, and agents reported apples arriving in Calcutta and Havana in fine condition.[^31][^40]
- One master heard the ice "working" in the hold during a gale and could do nothing, because the hatches could not be opened at sea.[^36]
- Ships calling at Cape Town, Mauritius, Key West or Havana sold ice off the top of the stack and were to reseal the hatches within the hour.[^37][^45]
- Return cargoes from Calcutta (jute, linen, indigo, saltpetre, spices) were often worth more than the ice.[^30][^29]
- News of a Calcutta voyage could take most of a year to reach Boston.[^31][^49]

**At the far ports**
- In Havana, ice was unloaded into lighters at night by lantern and carried ashore.[^43]
- In Calcutta, servants ran the ice baskets home on their heads, and a home "pot in a pot" kept ice about a day.[^61]
- In the 1830s some Calcutta households doubted the cleanliness of ice handled by foreign sailors.[^60]

**Afterwards**
- Tudor, once in debtors' prison, became the "Ice King," one of Boston's richest men by the 1840s.[^39][^25]
- The Madras ice house survives, altered, and is now a museum.[^57] The Tudor papers are the largest single source on the trade.[^87]
- The words "icebox" and "iceman" grew out of the wider natural-ice habit.[^84]

## Open Research Questions

> [!tip]-  
> Questions that remain unanswered or would benefit from further research.

- **Pay:** what labourers, skilled men, foremen and stevedores were actually paid. No wage figures appear in the findings.
- **Pond prices:** what pond owners were paid per ton, and what ice cost in Boston.
- **Havana prices:** actual figures, including the monopoly's maximum prices.
- **Madras and Bombay prices:** actual figures.
- **Calcutta prices after the 1840s:** what the ice cost later.
- **Far-port losses:** how much ice the tropical ice houses lost, as figures comparable to the 1847 pond ledger.
- **Cargo size:** typical cargo tonnage per voyage on each route. The findings say cargoes grew through the 1840s but give no figures.[^30]
- **Last sailings elsewhere:** the date and ship of the last cargo to Havana, New Orleans and the other southern ports.
- **Calcutta ice house:** exact opening and demolition dates.
- **Far-port workers:** what is known of the porters and enslaved dock workers who unloaded the ice. No account by the workers survives in these collections.[^68]
- **Block thickness:** at least 14 inches is the minimum, but the findings give no typical thickness.

## Reliability / Limitations

- `Tudor papers (harvard-business-archive.example)`: the core primary source (diaries, instructions, letters, accounts), but it is one firm's view. Agents' letters and price-war tactics are told from the firm's side.[^31]
- `Fresh Pond 1847 ledger (ma-archives.example)`: a primary record, but the only whole-season storage record for a single house.[^23]
- `Calcutta melt study (ice-trade-voyages.example)`: systematic, but may be biased toward better voyages whose papers survived.[^47]
- `Popular history book excerpt (popular-history-press.example)`: often gives figures with no source (storage loss, voyage loss, end date).[^25]
- `Regional industry history site (new-england-industry.example)`: cites no archive for the pond-rights figures.[^2]
- `Walden-region oral histories (1974)`: recorded from workers on the last commercial harvests, long after the sea trade ended, so they may not describe the early trade.[^10]
- `Farm journal articles (1856, 1859)`: advice to farmers, not accounts of commercial harvests or houses.[^5][^21]
- `Boston newspapers`: short reports, and the strike and fight coverage gives one side (the firms').[^70][^71]
- `Calcutta memoirs and gazette`: British residents describing their own households and Indian customers.[^61][^60]
- `Havana dock-labour records`: employer contracts only.[^68]
- `Hong Kong heritage page`: relies on newspaper notices, with no building records.[^59]
- `Fresh Pond icehouse capacity`: the historical society article sources the figure to a company prospectus.[^17]

## Sources

[^1]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview (local historical society article, 2017)
[^2]: https://www.new-england-industry.example/ice/pond-rights (regional industry history site, 2014)
[^3]: https://www.harvard-business-archive.example/tudor-papers/harvest-instructions (merchant's papers, 2009)
[^4]: https://www.new-england-industry.example/ice/snow-and-flooding (regional industry history site, 2014)
[^5]: https://www.farm-journal-archive.example/1856/february/ice-for-market (agricultural magazine, February 1856)
[^6]: https://www.mit-tech-history.example/inventors/wyeth-ice-tools (university history of technology page, 2018)
[^7]: https://www.patent-records.example/1829/wyeth-ice-cutting-apparatus (patent record, 1829)
[^8]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s (local historical society article, 2019)
[^9]: https://www.new-england-industry.example/ice/breaking-and-floating (regional industry history site, 2014)
[^10]: https://www.walden-region-history.example/oral-histories/ice-crews (oral history collection, transcribed 1974)
[^11]: https://www.steam-power-history.example/small-engines/ice-elevators (engineering history society page, 2012)
[^12]: https://www.harvard-business-archive.example/tudor-papers/pond-accounts (merchant's papers, 2009)
[^13]: https://www.hudson-valley-museum.example/collections/ice-tool-catalogues (museum collection page, 2020)
[^14]: https://www.boston-markets-history.example/ice/local-trade (local history society page, 2016)
[^15]: https://www.boston-newspaper-archive.example/1858/january/ice-crop (newspaper, January 1858)
[^16]: https://www.new-england-industry.example/ice/open-winters (regional industry history site, 2014)
[^17]: https://www.cambridge-historical.example/fresh-pond/icehouses (local historical society article, 2017)
[^18]: https://www.new-england-industry.example/ice/storage-history (regional industry history site, 2014)
[^19]: https://www.harvard-business-archive.example/tudor-papers/storage-trials (merchant's papers, 2009)
[^20]: https://www.massachusetts-engravings.example/prints/fresh-pond-ice-works-1852 (museum print catalogue, engraving 1852)
[^21]: https://www.farm-journal-archive.example/1859/june/building-an-ice-house (agricultural magazine, June 1859)
[^22]: https://www.harvard-business-archive.example/tudor-papers/keepers-letters (merchant's papers, 2009)
[^23]: https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage (state archives, transcribed ledger, digitized 2015)
[^24]: https://www.ma-archives.example/ice-ledgers/methods-note (state archives research note, 2015)
[^25]: https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt (book excerpt, 2005)
[^26]: https://www.railroad-history-ma.example/branches/charlestown-ice-line (railway historical society page, 2013)
[^27]: https://www.boston-harbour-history.example/wharves/charlestown-ice-houses (local history society page, 2011)
[^28]: https://www.boston-newspaper-archive.example/1868/august/icehouse-fire (newspaper, August 1868)
[^29]: https://www.maritime-boston.example/trade/outward-cargoes (maritime museum article, 2016)
[^30]: https://www.economic-history-review.example/2010/ice-shipping-costs (peer-reviewed article, 2010)
[^31]: https://www.harvard-business-archive.example/tudor-papers/agents-letters (merchant's papers, 2009)
[^32]: https://www.maritime-salem.example/papers/ship-fittings-for-ice (museum research paper, 2008)
[^33]: https://www.maritime-salem.example/papers/stowing-ice-1850 (transcription of a merchant's printed paper, 1850)
[^34]: https://www.maine-lumber-history.example/mills/sawdust-trade (state historical society article, 2015)
[^35]: https://www.boston-harbour-history.example/wharves/stevedores (local history society page, 2011)
[^36]: https://www.sailing-ship-logs.example/collections/ice-voyages (digitized logbook collection, various dates)
[^37]: https://www.harvard-business-archive.example/tudor-papers/masters-instructions (merchant's papers, 2009)
[^38]: https://www.insurance-history.example/marine/perishable-cargoes (insurance history society article, 2012)
[^39]: https://www.harvard-business-archive.example/tudor-papers/diary-excerpts (merchant's papers, 2009)
[^40]: https://www.food-history-quarterly.example/2014/new-england-apples-abroad (peer-reviewed article, 2014)
[^41]: https://www.maritime-boston.example/routes/boston-calcutta (maritime museum article, 2016)
[^42]: https://www.maritime-boston.example/routes/caribbean (maritime museum article, 2016)
[^43]: https://www.havana-archive.example/colonial-trade/shipping-arrivals (port records, 1830s–1850s)
[^44]: https://www.gulf-commerce.example/ports/new-orleans-ice-imports (business history society page, 2013)
[^45]: https://www.maritime-boston.example/routes/other-ports (maritime museum article, 2016)
[^46]: https://www.calcutta-history-society.example/1833/first-ice-ship (local history society article, 2011)
[^47]: https://www.ice-trade-voyages.example/logs/calcutta-melt-study (university research project report, 2018)
[^48]: https://www.calcutta-history-society.example/port/hooghly-pilots-and-tugs (local history society article, 2011)
[^49]: https://www.postal-history-review.example/2009/overland-mail-to-india (peer-reviewed article, 2009)
[^50]: https://www.calcutta-history-society.example/buildings/the-ice-house (local history society article, 2011)
[^51]: https://www.british-library-images.example/calcutta/ice-house-1840s (library image catalogue, drawing 1840s)
[^52]: https://www.colonial-architecture-journal.example/2016/cold-storage-in-bengal (peer-reviewed article, 2016)
[^53]: https://www.havana-archive.example/colonial-trade/building-permits (city records, 1820s–1850s)
[^54]: https://www.havana-archive.example/colonial-trade/ice-monopoly (colonial government records, 1820s–1840s)
[^55]: https://www.havana-archive.example/colonial-trade/ice-depot-1840s (commercial records, 1840s)
[^56]: https://www.louisiana-archives.example/levee/warehouse-registers (state archives catalogue, 1840s)
[^57]: https://www.madras-heritage.example/beach-road/ice-house (heritage trust page, 2019)
[^58]: https://www.lowcountry-history.example/charleston/ice-trade (local history society page, 2014)
[^59]: https://www.hongkong-heritage.example/waterfront/early-ice-house (heritage society page, 2017)
[^60]: https://www.calcutta-gazette-archive.example/notices/ice-house-hours (newspaper notices, 1830s–1850s)
[^61]: https://www.memoirs-of-empire.example/collections/calcutta-domestic-life (memoir collection, 1840s–1860s)
[^62]: https://www.food-history-quarterly.example/2012/ice-cream-in-the-tropics (peer-reviewed article, 2012)
[^63]: https://www.labor-history-ne.example/winter-work/farm-families (regional labour history project page, 2016)
[^64]: https://www.labor-history-ne.example/winter-work/irish-labour (regional labour history project page, 2016)
[^65]: https://www.immigration-history-journal.example/2012/boston-irish-winter-work (peer-reviewed article, 2012)
[^66]: https://www.immigration-history-journal.example/2015/french-canadians-in-new-england (peer-reviewed article, 2015)
[^67]: https://www.labor-history-ne.example/winter-work/harvest-crew-sizes (regional labour history project page, 2016)
[^68]: https://www.havana-archive.example/colonial-trade/dock-labour-contracts (colonial records, 1830s–1850s)
[^69]: https://www.labor-history-ne.example/winter-work/ice-crews-conditions (regional labour history project page, 2016)
[^70]: https://www.boston-newspaper-archive.example/1851/january/disturbance-on-the-ice (newspaper, January 1851)
[^71]: https://www.boston-newspaper-archive.example/1866/february/ice-strike (newspaper, February 1866)
[^72]: https://www.boston-newspaper-archive.example/1880/march/open-winter-hardship (newspaper, March 1880)
[^73]: https://www.medical-history-journal.example/2013/ice-in-tropical-medicine (peer-reviewed article, 2013)
[^74]: https://www.bombay-gazette-archive.example/notices/ice-sales (newspaper notices, 1840s)
[^75]: https://www.gulf-commerce.example/price-current/ice-1860 (commercial price paper, 1860)
[^76]: https://www.louisiana-archives.example/newspapers/daily-ice-reports (newspaper collection, 1840s–1850s)
[^77]: https://www.river-history-review.example/2011/steamboat-provisioning (peer-reviewed article, 2011)
[^78]: https://www.new-england-industry.example/ice/decline (regional industry history site, 2014)
[^79]: https://www.civil-war-commerce.example/blockade/ice-shortage (university history project page, 2015)
[^80]: https://www.civil-war-commerce.example/blockade/carre-machines (university history project page, 2015)
[^81]: https://www.mit-tech-history.example/inventors/early-refrigeration (university history of technology page, 2018)
[^82]: https://www.patent-records.example/1851/gorrie-ice-machine (patent record, 1851)
[^83]: https://www.louisiana-archives.example/business/ice-manufacturing-charters (state archives catalogue, 1868)
[^84]: https://www.food-history-quarterly.example/2016/clear-ice-and-cloudy-ice (peer-reviewed article, 2016)
[^85]: https://www.calcutta-history-society.example/industry/bengal-ice-factory (local history society article, 2011)
[^86]: https://www.cambridge-historical.example/fresh-pond/water-supply (local historical society article, 2017)
[^87]: https://www.harvard-business-archive.example/tudor-papers/finding-aid-overview (finding aid, 2009)
[^88]: https://www.cuba-commerce-history.example/1870s/manufactures (university research project page, 2014)
[^89]: https://www.ice-trade-voyages.example/registers/calcutta-arrivals (university research project register, 2018)
[^90]: https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882 (shipping register, 1882)
[^91]: https://www.boston-newspaper-archive.example/1880s/ice-coverage-survey (newspaper archive research note, 2019)
````

Final reply:

````
The light note is written: `project/Research/Light Research - Ice Trade.md`

**Cut short:** none. All eight findings files end with the `<!-- end of findings -->` marker, and none has a passage that stops partway.

The note has one section per topic in the plan's order, and every claim carries a footnote to its source. Where sources gave different figures, the note sets them side by side in the Disagreement / Uncertainty section:
- **Ice lost in storage:** the 1847 ledger says 17%; a book with no stated source says a fifth to a third.
- **Ice lost on the Calcutta voyage:** a logbook study says 38% on average; the same book says about a quarter.
- **When the trade ended:** some histories say the early 1880s, others say ice still went by sea into the 1890s and later.

The findings had no wage figures and no prices for Havana, Madras or Bombay, so those are listed under Open Research Questions.

I copied the frontmatter from the template, including its Copper Coast project link. I set the created/modified date to the run date (2026-10-09 14:00). I left `author`, `status`, `tags` and `sources` blank because nothing said how to fill them.
````

#### Run 2

Grades:

````
FAIL  fm-author  no match; read Light Research - Ice Trade.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-09'; read Light Research - Ice Trade.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-09'; read Light Research - Ice Trade.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - Ice Trade.md in its place
PASS  fm-sources-empty  found 'sources:'; read Light Research - Ice Trade.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - Ice Trade.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - Ice Trade.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - Ice Trade.md in its place
PASS  judge-footnotes-resolve   Every marker in the body has a matching definition, every definition holds a URL, and every definition is used at least once.  **Markers in the body:** Taken together, the body markers cover every number from [^1] through [^92], with no gaps and nothing above 92. Some numbers that appear only once or twice: - [^7]: "patented an improved version in 1829.…[^6][^7]" - [^11]: "by small steam engines… [read Light Research - Ice Trade.md in its place]
PASS  judge-planted-details-cite-own-url   All eight details appear in the note, and each carries a footnote that resolves to its given URL under Sources.  1. **22-inch squares.** "making a grid of **22-inch squares**.[^8]"    [^8]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s ✓  2. **About 17% loss in 1847.** "The 1847 ledger of one Fresh Pond house records a loss of **about 17%** between the end of the harvest in [read Light Research - Ice Trade.md in its place]
PASS  judge-reply-no-cut-short   The reply names no topic or file as cut short. It says outright: "**None of the findings files was cut short.** All eight end with the `<!-- end of findings -->` marker, and none stops partway through a passage."  The "Open Research Questions" line ("what the findings didn't cover, such as wages, cargo sizes in tons...") is about gaps in the content. It doesn't say any file was truncated or missi
PASS  judge-sixteen-questions-answered   All sixteen questions are answered with the findings' answers, and none is listed as open.  1. **Cutting time and thickness:** "usually mid-January into February, after a long hard freeze." It says "Ice was not cut until it had **at least 14 inches of clear ice**" and "Each morning a foreman bored test holes with a hand auger." 2. **Tools and block size:** "Nathaniel Jarvis Wyeth designed a horse [read Light Research - Ice Trade.md in its place]
PASS  keeps-t1-14-inches  found '14 inch'; read Light Research - Ice Trade.md in its place
PASS  keeps-t1-22-inch-blocks  found '22-inch'; read Light Research - Ice Trade.md in its place
PASS  keeps-t2-17-percent-loss  found '17%'; read Light Research - Ice Trade.md in its place
PASS  keeps-t2-9400-tons  found '9,400'; read Light Research - Ice Trade.md in its place
PASS  keeps-t3-pumped-every-4-hours  found '4 hours'; read Light Research - Ice Trade.md in its place
PASS  keeps-t3-sawdust-1-to-11  found '11 tons'; read Light Research - Ice Trade.md in its place
PASS  keeps-t4-130-days  found '130 days'; read Light Research - Ice Trade.md in its place
PASS  keeps-t4-38-percent-loss  found '38%'; read Light Research - Ice Trade.md in its place
PASS  keeps-t5-1250-tons  found '1,250'; read Light Research - Ice Trade.md in its place
PASS  keeps-t5-barcia  found 'Barcia'; read Light Research - Ice Trade.md in its place
PASS  keeps-t6-75-men  found '75'; read Light Research - Ice Trade.md in its place
PASS  keeps-t6-nine-drownings  found 'nine drown'; read Light Research - Ice Trade.md in its place
PASS  keeps-t7-2-half-cents  found '2½'; read Light Research - Ice Trade.md in its place
PASS  keeps-t7-3-annas  found '3 annas'; read Light Research - Ice Trade.md in its place
PASS  keeps-t8-12-tons-a-day  found '12 tons'; read Light Research - Ice Trade.md in its place
PASS  keeps-t8-margaret-ellery  found 'Margaret Ellery'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-1  found 'https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-2  found 'https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-3  found 'https://www.maritime-salem.example/papers/stowing-ice-1850'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-4  found 'https://www.ice-trade-voyages.example/logs/calcutta-melt-study'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-5  found 'https://www.havana-archive.example/colonial-trade/ice-depot-1840s'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-6  found 'https://www.labor-history-ne.example/winter-work/harvest-crew-sizes'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-7  found 'https://www.gulf-commerce.example/price-current/ice-1860'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-8  found 'https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882'; read Light Research - Ice Trade.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - Ice Trade.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - Ice Trade.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - Ice Trade.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - Ice Trade.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - Ice Trade.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - Ice Trade.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-1-section  found '## Cut'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-2-section  found '## Stor'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-3-section  found '## Load'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-4-section  found '## The voyage'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-5-section  found '## Ice houses at the far port'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-6-section  found '## The worker'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-7-section  found '## Buyers and price'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-8-section  found '## The end'; read Light Research - Ice Trade.md in its place
FAIL  file-name  wrote Light Research - Ice Trade.md instead
````

`project/Research/Light Research - Ice Trade.md`:

````markdown
---
title: Light Research - Ice Trade
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-09 14:00
modified: 2026-10-09 14:00
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> From the `- [r]` request in [[idea-ice-ship]] (line 9): how the old ice trade worked from a frozen New England pond to a hot foreign port. The research plan split it into eight topics: cutting the ice, storing it before shipping, loading the ship, the voyage, ice houses at the far ports, the workers, buyers and prices, and the end of the trade. The writer's comment limits the scope to the New England trade by sea, start to finish: roughly from the first cargo in 1806 to the last cargoes in the 1880s (or later; see Disagreement / Uncertainty).  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Ice Trade

## Summary

> [!tip]-  
> A concise synthesis of the most important findings.
> 
> Focus on what is useful to understand about the subject without translating those findings into story decisions.

The trade shipped clear pond ice from Massachusetts (Fresh Pond, Wenham Lake, Spy Pond) to the Caribbean, the American South, India, and a few other ports, from Frederic Tudor's failed first cargo to Martinique in 1806 until about the 1880s. Every stage was organised against melting:

- **Cutting:** ice was cut from mid-January into February once it was at least 14 inches of clear ice. From 1825 Nathaniel Wyeth's horse-drawn marker and plough cut it into regular 22-inch-square blocks of about 200 lb.
- **Storage:** blocks were stored in huge double-walled, sawdust-filled icehouses on the pond shore. One 1847 ledger records a loss of about 17% over a season.
- **Loading:** the ice went by rail to the Charlestown wharves. It was packed into ordinary merchant ships that would otherwise have sailed in ballast, inside a sawdust-lined "ice ceiling", at about 1 ton of sawdust to 11 tons of ice. The hatches were then sealed for the whole voyage.
- **The voyage:** Caribbean voyages took 2–3 weeks and often lost under a tenth of the cargo. The Calcutta run took about 130 days and lost an average of 38% in the best study, though another estimate puts it at about a quarter.
- **Far ports:** each port needed an ice house built before the ice arrived. The Calcutta house was round, brick, and held about 1,250 tons. Ice was sold by weight in the early morning, by ticket in Havana.
- **Workers and buyers:** the work was done by farmers, Irish immigrants and later French-Canadians, hired by the day under skilled foremen, in hard and dangerous conditions. Buyers began as colonial elites, hospitals, clubs and cafés. In New Orleans, the largest market, falling prices (about 2½¢/lb by 1860) brought ice into ordinary households.
- **The end:** the trade peaked around 1860. The Civil War, ice-making machines, steamships, and a booming home market for natural ice ended it. The last recorded Calcutta cargo sailed in 1882.

## Cutting the ice on the ponds

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**When and where.** The harvest ran in the coldest weeks, usually mid-January into February, after a long hard freeze.[^1] Firms preferred spring-fed ponds with no inflowing streams, because moving water froze unevenly and carried silt and mill sawdust. They bought or leased shore rights to keep rivals off. A pond owner could earn more from one winter's ice rights than from a year of farming.[^1][^2]

**Thickness.** Ice was not cut until it had **at least 14 inches of clear ice**. Thinner ice crumbled, wasted hold space, and melted faster. Each morning a foreman bored test holes with a hand auger and measured the clear ice and the white "snow ice" on top separately; only clear ice counted. Cutting often began near the shaded shore and moved outward as the ice thickened.[^1][^3] Foremen also tested clarity by holding a test block up to the light: if a dark object showed clearly through the block, the ice was good enough to ship.[^10][^3]

**Snow.** Snow insulated the ice and slowed freezing. Wet snow froze into weak, white snow ice. Crews cleared snow with horse-drawn scrapers. Some flooded the cleared surface through bored holes to thicken the ice, which only worked in hard cold.[^4][^5] A thaw or rain could ruin a cut field. In an "open winter" (too mild to freeze), firms bought ice from Maine and New Hampshire at higher cost. A large pond could be cleared in 2–3 weeks in a good season.[^13][^14]

**Tools.** Before the 1820s ice was cut by hand with axes, saws, and chisels, which gave uneven blocks that stacked badly. Nathaniel Jarvis Wyeth designed a horse-drawn cutter in 1825 and patented an improved version in 1829. Historians credit regular blocks with making long voyages possible, and by the 1840s most commercial ponds in Massachusetts used his tools in some form.[^6][^7] The sequence was:

1. **Marker:** a plough-like frame with steel teeth, drawn by one horse along a cord line. It scored parallel grooves, then cross-grooves at a right angle, making a grid of **22-inch squares**.[^8]
2. **Plough:** longer teeth, run repeatedly along the grooves until they were about two-thirds of the way through the ice. The last third held the field together for men and horses.[^8]
3. **Channel and breaking bars:** a channel to shore was sawn out with long hand saws. Men with iron breaking bars split the field into rafts, then into single blocks.[^9][^10]
4. **Pike poles:** blocks were floated along the channel to shore.[^9]
5. **Elevator:** an inclined ramp with an endless cleated chain carried the blocks up into the icehouse. It was driven by a horse capstan, and in the largest houses from the 1850s by small steam engines. Before going up, the blocks were planed flat and stripped of snow ice.[^1][^11]

Horses wore spiked ("calked") shoes, and a blacksmith was kept near the larger ponds.[^10][^5] By the 1850s complete tool sets were sold by specialist makers, many in the Hudson valley. Their catalogues are now a main source on the work.[^16][^6]

**Block size and grading.** A standard first-quality block weighed **roughly 200 lb**. This was the firm's working figure, not a measured average. Blocks were tallied by count at the elevator and converted to tons.[^15] Clear blocks were graded first quality and set aside for shipping. Cloudy blocks or blocks with leaves in them were second quality and sold locally in Boston.[^3][^12]

## Storing the ice before shipping

**Construction.** The shipping firms built above-ground icehouses on the pond shore, fed straight from the elevator. These replaced the older farm ice pits, which held only a few tons and let groundwater in.[^17][^18] The keys to the design were:

- **Double walls** (sometimes triple) with the gap packed with sawdust or spent tanbark. Tudor and Wyeth's trial houses of the 1820s–30s showed that dry fill kept ice far better than damp fill, so the houses had wide eaves.[^19][^6]
- **Steep roofs with louvred ridge vents** to let warm air escape. The outsides were painted white or a light colour, and there was sometimes hay in the roof space.[^21][^18]
- **Drained floors** over gravel or broken stone, with a drain to the pond and a sawdust bed under the stack. Ice standing in melt water melted much faster than ice in air.[^19]
- **Separate rooms** under one long roof. Each was filled and emptied on its own, with stacked doors that were boarded shut as the ice rose.[^17][^20]

Blocks were stacked on edge, tight together, with each layer crossing the one below like brickwork. Gaps were filled with ice chips, and the top was covered with hay or sawdust.[^17][^10] A resident keeper ran each large house: drains, vents, doors, fire watch, and the in/out ledger.[^22]

**Capacity.** The biggest Fresh Pond house held **about 9,400 tons** and was taller than a three-storey building. This figure comes from a company prospectus cited by the historical society.[^17][^20] Smaller firms' houses held a few hundred tons.[^17] Small wharf icehouses at Charlestown, also a few hundred tons each, held ice for a few days before loading.[^25] From the early 1840s a rail line ran from Fresh Pond to the Charlestown wharves in under an hour, in sawdust-lined wagons that ran at night in summer.[^24]

**Loss in storage.** The 1847 ledger of one Fresh Pond house records a loss of **about 17%** between the end of the harvest in March and the last autumn sailing. Most of it was in July and August. The ledger is the only surviving whole-season record for a single house and is used as the standard figure.[^23] It weighed sample blocks; ledgers that only counted blocks understate loss, and the two kinds of figure can't be compared directly.[^26] A popular history gives a fifth to a third for a well-built house, and up to half for small ones, without a source (see Disagreement / Uncertainty).[^28] Large houses lost proportionally less than small ones, which is why the houses kept getting bigger.[^18]

## Loading the ship

**Preparation.** The ice went in ordinary merchant ships, often older ones. Many would otherwise have left Boston in ballast, so owners carried ice cheaply.[^29][^30] Holds were swept, scrubbed, and aired, because smells passed into the ice. Ships that had carried fish, hides, or coal were avoided.[^31]

**The "ice ceiling".** A carpenter built a lining of pine planks a little in from the hull on all sides, across the floor and under the deck beams, with sawdust packed between. This took about a week for a mid-sized ship.[^32][^29] The floor went in first: dunnage (rough timber) to lift the cargo above the bilge, then the lining floor, then a deep bed of sawdust. Gaps at the sides let melt water run to the pumps. A badly drained floor caused the largest single loss on most recorded voyages.[^32]

**Packing.** Stevedores lowered blocks in slings and stowed them like the icehouse stacks: on edge, tight, each layer crossing the one below, with chips and sawdust in every gap.[^35][^29] An 1850 Salem merchant's paper gives the ratio of **1 ton of sawdust to every 11 tons of ice**. The sawdust was pine waste from Maine mills, brought by schooner, and had to be dry, because wet sawdust froze into a heat-conducting crust.[^34][^33] The ice was stowed low and evenly for stability, and ships usually carried less than their rated tonnage.[^32][^36] Loading took 1–2 days and was done at night or early morning. The ship sailed on the next tide.[^35][^37]

**What kept it from melting or shifting.**

- **Sealed hatches:** the top of the stack was covered with sawdust, then hay. The hatches were covered with tarred canvas and battened, sometimes with a second inner cover. They stayed shut until port, and a master who opened them without cause answered for the lost ice.[^32][^36][^37]
- **Bracing:** timber battens were driven between the stack and the lining, and the top layers were wedged against the deck beams. Logbooks record heavily reduced cargoes after gales loosened the stow.[^36]
- **Pumping:** melt water was pumped every 4 hours, day and night. The stroke count, logged by the mate, was the only gauge of how the ice was faring.[^36]

## The voyage

**Routes and times.**

| Route | Voyage time | Notes |
|---|---|---|
| Caribbean (Havana, Martinique, Jamaica, etc.) | 2–3 weeks with fair winds | Havana was one of the steadiest markets, with ships every few weeks.[^42][^43] |
| US South (Charleston, Savannah, Mobile, New Orleans) | Several weeks (New Orleans) | Largest market by volume. By the 1850s New Orleans took more New England ice than any port in the world.[^44][^30] |
| Calcutta, via the Cape of Good Hope | About 130 days | Crossed the equator twice and finished up the Hooghly River.[^41][^36] |
| Bombay, Madras, Hong Kong, Rio, Valparaíso, Australia | Varied | Less regular. Some were tried for a few years and dropped.[^30][^45] |

The first cargo, to Martinique in 1806, mostly melted on the wharf because there was no ice house.[^38][^28] The first Calcutta cargo sailed in May 1833 on the *Tuscany* and arrived that September.[^46][^41] Calcutta sailings left Boston in autumn and early winter so the ice arrived in the March–June hot season. This also meant the first weeks at sea were spent in cold water.[^41][^30] From the 1840s, steam tugs towed ships up the Hooghly in a day or less.[^49]

**Melting on the way.** Most of the melting happened in the tropics. Pumping strokes rose sharply near the equator. On the Calcutta run the second tropical crossing, late in the voyage, was the worst.[^36] Losses on each route:

- **Calcutta:** a study of surviving logbooks and cargo receipts found an **average loss of 38%** between Boston and Calcutta, varying widely by season, voyage length, and stow. The authors warn that the surviving papers may favour the better-run voyages.[^47] A popular history says about a quarter for well-stowed ships (see Disagreement / Uncertainty).[^28]
- **Caribbean and southern routes:** a well-stowed cargo often lost **under a tenth**. This is an estimate from a small number of voyages.[^30][^15]
- **Calms:** becalming in the doldrums cost ice, and masters were told to avoid known calm zones even at the cost of distance.[^36][^37]

## Ice houses at the far ports

**The rule.** After the Martinique failure, the trade learned to build the ice house first. From the 1810s firms built or rented one in each port before sending regular cargoes, sometimes by converting a warehouse, and sent carpenters from Boston with the first cargo.[^38][^28]

**Construction and capacity.**

- **Calcutta:** paid for by a subscription among the city's merchants after 1833. It was a round brick building near the river with thick double walls, a domed roof over a ventilated space, and a floor that drained to the river. When full it held **about 1,250 tons**. It was built of brick because termites and monsoon damp destroyed wood.[^50][^51][^52] It was pulled down in the late 19th century.[^50]
- **Havana:** built by the Tudor firm in the 1820s, partly sunk into the ground so the lower layers stayed cooler.[^53][^52] The ships unloaded into lighters (flat-bottomed harbour boats) at night.[^43]
- **New Orleans:** several competing houses on the levee by the 1840s, fully above ground because the ground was wet. They stood next to the wharves.[^44][^55]
- **Bombay and Madras:** built in the late 1830s to early 1840s on the Calcutta model, but smaller. Madras ice came through the surf in small boats.[^52][^56] The Madras house survives, altered, as a museum.[^56]
- **Charleston and Savannah:** smaller wooden houses on the Boston plan, raised on brick piers, often owned by local merchants who bought whole cargoes.[^57]
- **Hong Kong:** a granite house on the waterfront from the 1840s. The trade there was small and irregular.[^59]

Tropical houses lost ice faster, month for month, than the pond houses, though the agents never gave comparable figures.[^31]

**Who ran them.** Each house was run by the firm's agent: either a man sent from Boston (as in Calcutta, with local staff) or a local merchant (Joaquín Barcia in Havana in the 1840s). Agents were usually paid a share of sales rather than a wage.[^31][^50][^58] In Havana the Tudor firm held a **monopoly from the Spanish colonial government**. In return it had to keep the city supplied all year, under a fixed maximum price, and could be fined for running out.[^54]

**How ice was sold.**

- **Hours:** early morning only, from first light to mid-morning. In Calcutta the hours were printed in the newspapers.[^50][^60]
- **By weight:** weighed on a scale at the door. Some houses kept blocks precut to standard weights.[^44][^60]
- **Tickets in Havana:** customers bought a ticket for a set weight at the city office and handed it in at the house door, so no money changed hands there.[^58]
- **Accounts:** hotels, clubs, hospitals, and military messes were billed monthly and often served before the queue.[^60][^31]
- **Delivery:** carts in New Orleans by the 1850s. Delivery was rare in Havana and Calcutta.[^44]
- **Teaching:** in new ports, agents gave ice away until the habit took hold, showed people how to use it, and sold ice chests shipped from Boston.[^38][^62]

## The workers

**Who did the work.**

- **Local farmers and their sons**, in the early years. The harvest fell in the farm's slack season, and the men were paid for their horses as well as themselves.[^63][^1]
- **Irish immigrants**, from the 1840s, mostly in unskilled jobs. Some lived in shanties near the ponds.[^64][^65]
- **French-Canadians**, in later decades, some from the mill towns and some coming down from Quebec for the season. By the 1870s some crews on the larger ponds were mostly French-Canadian.[^66]
- **Boys** from about age 12, guiding blocks, sweeping chips, and carrying messages, for less pay.[^10][^63]
- **Women** did not work on the ice. They ran boarding houses, cooked, and dried clothes, and the firms usually paid them in the household's name.[^63][^15]
- **Stevedores** loaded the ships. They were a separate, year-round waterfront workforce, worked in gangs under a contracting boss, and were paid by the ton.[^35]
- **Far-port labour:** porters hired by the agent in Calcutta. In Havana the depot hired enslaved men from their owners to unload the ships.[^70][^31]

**How crews were organised.** A large pond had a crew of **about 75 men**, divided into gangs: snow scrapers, marker and plough, bar men, channel men, elevator, and stackers. The gangs worked in sequence, so the slowest set the pace. A smaller pond used about a third as many men.[^67] A foreman, answering to the firm's pond superintendent, chose where and when to cut and whom to hire.[^3] Labourers were **hired by the day at the pond edge**, with no promise of work the next day.[^10] Skilled men (marker drivers, bar men, stackers) were hired for the season at higher pay and invited back each year.[^3][^63] Pay came weekly, on Saturday evening, with board deducted.[^15] When local labour was short, men were brought from Boston by train.[^64]

**Conditions and dangers.**

- **Cold:** frostbite was common. Men wore wool layers, felt boots with overshoes, and iron "creepers" on their boots. Wet clothing could kill.[^10][^69]
- **Hours:** first light to dark. When a thaw threatened there was night work by lantern and sometimes Sunday work, with no extra pay unless the foreman agreed.[^13]
- **Falling through:** this was the worst danger. A newspaper count found **nine drownings** among Cambridge pond crews from 1850 to 1860, mostly men who fell into the open channel at night. Railings and lights came only late in the trade.[^69][^13]
- **Injuries:** saws, bars, slipping blocks on the elevator, and shifting stacks. Injured men got no pay beyond the days already worked.[^69][^10]
- **Open winters:** no harvest meant no winter wage, and Boston charities reported more families seeking help afterwards.[^72]
- **Strikes and tension:** short strikes over daily pay were timed for when a thaw was forecast (1850s–60s), and the firms blacklisted strikers.[^71][^64] There were also fights between local and Irish crews.[^65][^68]

## Buyers and prices

**Who bought.**

- **Calcutta:** British residents (East India Company officials, officers, merchants), and wealthy Indian merchant and landowning families, who were a large share of private buyers by the 1840s. Hospitals, clubs, and officers' messes were the big account customers. For most of the city ice was unaffordable.[^50][^61][^73]
- **Havana:** cafés, confectioners making ices and sorbets, and wealthy households. Ice spread to common café use within a generation.[^54][^62]
- **New Orleans:** everyone, by the 1850s: bars, hotels, households, meat and fish markets, river steamboats, and hospitals during the yellow fever epidemics.[^44][^74][^77][^73]
- **Charleston and Savannah:** planters, merchants, hotels, and taverns.[^57]
- **Madras and Bombay:** British residents, clubs, messes, hospitals, and wealthy Indian and Parsi families.[^56][^75]
- **Hong Kong:** the garrison, the trading houses, and ships in the harbour.[^59]

**What it cost.**

- **Calcutta, 1830s–40s:** **3 annas a pound** at the door (an anna was 1/16 rupee). The price was steady for two decades. Account customers sometimes paid less, and hospitals got a reduced contract rate.[^60][^30][^73]
- **Madras and Bombay:** higher than Calcutta.[^56][^75]
- **Havana:** capped by the government's maximum price, which was revised several times.[^54]
- **New Orleans:** fell steadily from the 1830s to the 1850s as competition grew. It was **about 2½¢ a pound by 1860** (from the city's weekly "price current"), rising in hot months and when ships were late.[^44][^30][^76]
- **Everywhere:** cheapest just after a ship arrived, dearest when the next was overdue. When a port ran dry, ice could not be had at any price.[^60][^43] Price wars between Boston firms brought short spells of cheap ice.[^31][^30]

The ice cost almost nothing at the pond. On the long routes the largest single cost in the price was ice lost to melting in transit and storage, larger even than carriage.[^30]

## The end of the trade

**What ended it.** The trade peaked around 1860 and was nearly over by the 1880s. No single cause ended it:[^30][^78]

- **The Civil War (1861–65):** the blockade closed the southern ports. New Orleans, the largest market, was cut off until 1862. Shortages pushed the South toward machine ice, and some Carré ammonia machines were run through the blockade. After the war, southern cargoes recovered only partly.[^79][^82][^44]
- **Ice machines:** Gorrie patented one in 1851, Carré's came in the late 1850s, and Harrison built them in Australia in the 1850s. These early machines were small and costly to run.[^80][^81] New Orleans got its first ice factory in 1868, at about 12 tons a day.[^83] Through the 1870s factory ice became cheaper than shipped ice once melt loss was counted.[^30] Early machine ice was cloudy and buyers distrusted it, which slowed the switch until the factories made clear ice by the 1880s.[^80][^84] Indian factories opened in the late 1870s and 1880s.[^85] Havana's monopoly lapsed after the US war, and local factories opened there in the 1870s.[^54][^89]
- **Steamships and Suez (1869):** these shrank the supply of cheap outward-bound sailing ships.[^41][^30]
- **The home market:** US cities, breweries, meat packers, and refrigerated rail cars could take all the ice the ponds cut, with no voyage.[^16][^78]
- **Other factors:** the ponds near Boston were fouled or built over, and Fresh Pond became Cambridge's water supply.[^86] Tudor died in 1864, and his firm declined.[^87] The harvest crews kept cutting for the home market, and the stevedores went back to general cargo.[^88]

**When the last cargoes sailed.** The Indian trade dwindled through the 1870s, and Bombay and Madras ended before Calcutta.[^90] The **last recorded Calcutta cargo sailed from Boston in 1882** on the bark *Margaret Ellery*. No later ice ship appears in the Calcutta register, and the Boston papers didn't report it.[^92][^91] Some histories put the end of the whole sea trade in the early 1880s. One general history has irregular Caribbean cargoes into the 1890s and occasional shipments to southern ports into the early 20th century.[^28][^78] Natural ice itself lasted at home until the 1920s–40s.[^78][^10]

## Disagreement / Uncertainty

> [!tip]-  
> Claims that are disputed, uncertain, incomplete, changing, or dependent on interpretation.
> 
> Distinguish clearly between:
> 
> - established fact
> 
> - expert consensus
> 
> - plausible interpretation
> 
> - contested claim
> 
> - anecdotal evidence
> 
> - speculation

- **Storage loss (contested figures).** The 1847 Fresh Pond ledger records about 17%, a documented figure for one house and one season.[^23] A popular history says a fifth to a third for well-built houses, and up to half for small ones, without a source.[^28] The method also changes the figure: ledgers that weigh blocks show more loss than ledgers that count them, so figures from different houses can't be compared.[^26]
- **Calcutta voyage loss (contested figures).** The logbook study gives an average of 38%, possibly biased low because the surviving papers favour better-run voyages.[^47] The popular history gives about a quarter for well-stowed ships, without a source, and blames higher losses on poor stowing.[^28] Neither says which years it covers, and the stow improved over time.
- **Short-route loss.** "Under a tenth" is an estimate from a small number of voyages.[^30]
- **End date (definitional).** The early 1880s if the trade means the long Asian voyages; into the 1890s or the 1900s if it means any New England ice sent by sea. The later shipments are unsourced.[^28][^78]
- **Block weight.** About 200 lb was the firm's working figure, not a measured average, and block thickness varied across a pond.[^15]
- **Havana monopoly's end.** The colonial records stop before its last years. The account of it lapsing after the US war comes from a later research project.[^54][^89]
- **Carré machines through the blockade.** Their number is unknown.[^82]
- **Price wars against factories.** The claim that factories closed in the 1870s comes with no list of which ones.[^44]

## Useful Details

> [!tip]-  
> Interesting or potentially useful details that do not belong cleanly elsewhere.
> 
> These may include small behavioral, material, procedural, linguistic, visual, environmental, or cultural observations.

- A horse that fell through the ice was rescued by tightening a rope around its neck, so it held its breath and floated higher, and then hauled out. Some horses went through two or three times a season.[^10][^5]
- A skilled bar man could tell by the sound of a strike whether the groove was deep enough.[^9]
- One firm told its foremen to reject any block they would not want to see on a dinner table.[^3]
- From the 1850s some keepers logged thermometer readings above the stack, morning and evening, beside the outside temperature.[^22]
- Icehouses burned easily, often in summer from railway sparks. The ice inside usually survived, standing in the ruins.[^27][^18]
- Sailors in the early years feared that melting ice would sink the ship. Tudor struggled to find crews.[^38]
- Marine insurers at first refused ice cargoes. Later policies excluded loss from melting, so the shipper bore it.[^39][^30]
- Masters and agents packed apples, butter, and cheese into pockets in the stack as private trade. The apples reached Calcutta and Havana in good condition.[^31][^40]
- One master logged hearing the ice "working" in the hold during a gale, unable to open the hatches.[^36]
- Masters kept a separate printed "ice book" with columns for date, position, deck and sea temperature, and pump strokes.[^36][^37]
- Bilge pump stroke counts rose steadily as ships entered warm waters. In one log the mate noted the strokes beside each day's "no wind."[^36]
- The return cargoes (jute, indigo, saltpetre, and spices from Calcutta; sugar, molasses, and coffee from the Caribbean) were often worth more than the ice.[^30][^29]
- The ice ceiling planks were often sold in timber-poor tropical ports.[^32]
- News from Calcutta took most of a year to reach Boston, later shortened by the overland mail through Egypt.[^31][^48]
- Calcutta servants ran home with the ice in blanket-wrapped baskets on their heads. At home it lasted about a day in a felt-lined box.[^61]
- Some Indian households in the 1830s doubted that ice handled by foreign sailors was clean. The source is British newspapers.[^60]
- Tudor, once in debtors' prison, became one of the richest men in Boston, the "Ice King." Most of the profit came from the southern and Caribbean trade.[^38][^28]

## Open Research Questions

> [!tip]-  
> Questions that remain unanswered or would benefit from further research.

- Actual prices in Havana (the maximum-price figures), Madras, Bombay, and Hong Kong. The findings give only relative statements.
- Wages: what a day labourer, a skilled man, a boy, or a stevedore was paid.
- Typical cargo sizes in tons for the Caribbean, southern, and Calcutta routes.
- Loss rates inside the far-port ice houses, as figures.
- Wholesale prices to local merchants who bought whole cargoes (Charleston, Savannah).
- Which years the 38% and "about a quarter" Calcutta loss figures cover.
- The experience of the far-port workers, including the enslaved men hired in Havana. Only the employers' records survive in the sources consulted.

## Reliability / Limitations

- `Tudor papers (business archive)`: the largest single source, but written from the firm's side. This includes its price-war tactics, the diary's view of Tudor's own difficulties, and the agents' letters, which report far-port losses only in general terms.[^31][^38]
- `The Frozen Water Trade (book excerpt)`: gives loss figures and late end dates with no sources.[^28]
- `Walden-region oral histories (1974)`: recorded from people who worked the last commercial harvests, long after the sea trade. They may not describe the early trade.[^10]
- `Farm journal articles (1856, 1859)`: general advice to farmers, not accounts of the commercial harvests or houses.[^5][^21]
- `New England industry history site`: cites no archive for the pond-rights figures and gives no count of icehouse fires.[^2][^18]
- `Calcutta logbook study`: the surviving papers may be biased toward better-run voyages.[^47]
- `Boston newspapers`: short, one-sided reports on the crew fights and strikes (the strike reports take the firms' side). The drowning count may miss deaths.[^68][^71][^69]
- `Calcutta memoirs and gazette`: British residents describing their own households, and British papers describing Indian customers.[^61][^60]
- `Havana dock-labour records`: employers' contracts only. No account by the workers survives.[^70]
- `Masters' logbook remarks`: claims such as ships rolling more as the ice melted are impressions, not measurements.[^36]
- `Fresh Pond icehouse capacity`: comes from a company prospectus, via the historical society.[^17]

## Sources

[^1]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview
[^2]: https://www.new-england-industry.example/ice/pond-rights
[^3]: https://www.harvard-business-archive.example/tudor-papers/harvest-instructions
[^4]: https://www.new-england-industry.example/ice/snow-and-flooding
[^5]: https://www.farm-journal-archive.example/1856/february/ice-for-market
[^6]: https://www.mit-tech-history.example/inventors/wyeth-ice-tools
[^7]: https://www.patent-records.example/1829/wyeth-ice-cutting-apparatus
[^8]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s
[^9]: https://www.new-england-industry.example/ice/breaking-and-floating
[^10]: https://www.walden-region-history.example/oral-histories/ice-crews
[^11]: https://www.steam-power-history.example/small-engines/ice-elevators
[^12]: https://www.boston-markets-history.example/ice/local-trade
[^13]: https://www.boston-newspaper-archive.example/1858/january/ice-crop
[^14]: https://www.new-england-industry.example/ice/open-winters
[^15]: https://www.harvard-business-archive.example/tudor-papers/pond-accounts
[^16]: https://www.hudson-valley-museum.example/collections/ice-tool-catalogues
[^17]: https://www.cambridge-historical.example/fresh-pond/icehouses
[^18]: https://www.new-england-industry.example/ice/storage-history
[^19]: https://www.harvard-business-archive.example/tudor-papers/storage-trials
[^20]: https://www.massachusetts-engravings.example/prints/fresh-pond-ice-works-1852
[^21]: https://www.farm-journal-archive.example/1859/june/building-an-ice-house
[^22]: https://www.harvard-business-archive.example/tudor-papers/keepers-letters
[^23]: https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage
[^24]: https://www.railroad-history-ma.example/branches/charlestown-ice-line
[^25]: https://www.boston-harbour-history.example/wharves/charlestown-ice-houses
[^26]: https://www.ma-archives.example/ice-ledgers/methods-note
[^27]: https://www.boston-newspaper-archive.example/1868/august/icehouse-fire
[^28]: https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt
[^29]: https://www.maritime-boston.example/trade/outward-cargoes
[^30]: https://www.economic-history-review.example/2010/ice-shipping-costs
[^31]: https://www.harvard-business-archive.example/tudor-papers/agents-letters
[^32]: https://www.maritime-salem.example/papers/ship-fittings-for-ice
[^33]: https://www.maine-lumber-history.example/mills/sawdust-trade
[^34]: https://www.maritime-salem.example/papers/stowing-ice-1850
[^35]: https://www.boston-harbour-history.example/wharves/stevedores
[^36]: https://www.sailing-ship-logs.example/collections/ice-voyages
[^37]: https://www.harvard-business-archive.example/tudor-papers/masters-instructions
[^38]: https://www.harvard-business-archive.example/tudor-papers/diary-excerpts
[^39]: https://www.insurance-history.example/marine/perishable-cargoes
[^40]: https://www.food-history-quarterly.example/2014/new-england-apples-abroad
[^41]: https://www.maritime-boston.example/routes/boston-calcutta
[^42]: https://www.maritime-boston.example/routes/caribbean
[^43]: https://www.havana-archive.example/colonial-trade/shipping-arrivals
[^44]: https://www.gulf-commerce.example/ports/new-orleans-ice-imports
[^45]: https://www.maritime-boston.example/routes/other-ports
[^46]: https://www.calcutta-history-society.example/1833/first-ice-ship
[^47]: https://www.ice-trade-voyages.example/logs/calcutta-melt-study
[^48]: https://www.postal-history-review.example/2009/overland-mail-to-india
[^49]: https://www.calcutta-history-society.example/port/hooghly-pilots-and-tugs
[^50]: https://www.calcutta-history-society.example/buildings/the-ice-house
[^51]: https://www.british-library-images.example/calcutta/ice-house-1840s
[^52]: https://www.colonial-architecture-journal.example/2016/cold-storage-in-bengal
[^53]: https://www.havana-archive.example/colonial-trade/building-permits
[^54]: https://www.havana-archive.example/colonial-trade/ice-monopoly
[^55]: https://www.louisiana-archives.example/levee/warehouse-registers
[^56]: https://www.madras-heritage.example/beach-road/ice-house
[^57]: https://www.lowcountry-history.example/charleston/ice-trade
[^58]: https://www.havana-archive.example/colonial-trade/ice-depot-1840s
[^59]: https://www.hongkong-heritage.example/waterfront/early-ice-house
[^60]: https://www.calcutta-gazette-archive.example/notices/ice-house-hours
[^61]: https://www.memoirs-of-empire.example/collections/calcutta-domestic-life
[^62]: https://www.food-history-quarterly.example/2012/ice-cream-in-the-tropics
[^63]: https://www.labor-history-ne.example/winter-work/farm-families
[^64]: https://www.labor-history-ne.example/winter-work/irish-labour
[^65]: https://www.immigration-history-journal.example/2012/boston-irish-winter-work
[^66]: https://www.immigration-history-journal.example/2015/french-canadians-in-new-england
[^67]: https://www.labor-history-ne.example/winter-work/harvest-crew-sizes
[^68]: https://www.boston-newspaper-archive.example/1851/january/disturbance-on-the-ice
[^69]: https://www.labor-history-ne.example/winter-work/ice-crews-conditions
[^70]: https://www.havana-archive.example/colonial-trade/dock-labour-contracts
[^71]: https://www.boston-newspaper-archive.example/1866/february/ice-strike
[^72]: https://www.boston-newspaper-archive.example/1880/march/open-winter-hardship
[^73]: https://www.medical-history-journal.example/2013/ice-in-tropical-medicine
[^74]: https://www.louisiana-archives.example/newspapers/daily-ice-reports
[^75]: https://www.bombay-gazette-archive.example/notices/ice-sales
[^76]: https://www.gulf-commerce.example/price-current/ice-1860
[^77]: https://www.river-history-review.example/2011/steamboat-provisioning
[^78]: https://www.new-england-industry.example/ice/decline
[^79]: https://www.civil-war-commerce.example/blockade/ice-shortage
[^80]: https://www.mit-tech-history.example/inventors/early-refrigeration
[^81]: https://www.patent-records.example/1851/gorrie-ice-machine
[^82]: https://www.civil-war-commerce.example/blockade/carre-machines
[^83]: https://www.louisiana-archives.example/business/ice-manufacturing-charters
[^84]: https://www.food-history-quarterly.example/2016/clear-ice-and-cloudy-ice
[^85]: https://www.calcutta-history-society.example/industry/bengal-ice-factory
[^86]: https://www.cambridge-historical.example/fresh-pond/water-supply
[^87]: https://www.harvard-business-archive.example/tudor-papers/finding-aid-overview
[^88]: https://www.labor-history-ne.example/winter-work/after-the-sea-trade
[^89]: https://www.cuba-commerce-history.example/1870s/manufactures
[^90]: https://www.ice-trade-voyages.example/registers/calcutta-arrivals
[^91]: https://www.boston-newspaper-archive.example/1880s/ice-coverage-survey
[^92]: https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882
````

Final reply:

````
I've written the light note at `project/Research/Light Research - Ice Trade.md`.

**None of the findings files was cut short.** All eight end with the `<!-- end of findings -->` marker, and none stops partway through a passage.

The note has one section for each of the eight topics, in the plan's order, and answers all 16 questions. The main conflicts are listed under Disagreement / Uncertainty:
- **Ice lost in storage:** about 17% in the 1847 ledger, against a fifth to a third in a book with no source for it.
- **Ice lost on the Calcutta voyage:** an average of 38% in the logbook study, against about a quarter in the same unsourced book.
- **When the trade ended:** some histories say the early 1880s; one says shipments went on into the 1890s or later.

Open Research Questions lists what the findings didn't cover, such as wages, cargo sizes in tons, and actual prices in Havana and the Indian ports.

I dated the note's `created` and `modified` fields to the run, 2026-10-09 14:00, and left `author`, `status`, `tags` and `sources` blank as in the template. The scope block links to `[[idea-ice-ship]]`, which is the request's source.
````

#### Run 3

Grades:

````
FAIL  fm-author  no match; read Light Research - Ice Trade.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-09'; read Light Research - Ice Trade.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-09'; read Light Research - Ice Trade.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - Ice Trade.md in its place
PASS  fm-sources-empty  found 'sources:'; read Light Research - Ice Trade.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - Ice Trade.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - Ice Trade.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - Ice Trade.md in its place
PASS  judge-footnotes-resolve   All 115 footnote markers in the body have a matching definition under Sources. Each definition holds a URL, and each definition is used at least once.  - **Every marker is defined.** Markers run from `[^1]` to `[^115]`, and Sources defines `[^1]` through `[^115]` with no gaps. The highest marker in the body is `[^115]`, in "the overland route through Egypt shortened the wait.[^53][^115]". It matc [read Light Research - Ice Trade.md in its place]
PASS  judge-planted-details-cite-own-url   All eight details appear in the note, and each carries a footnote resolving to the required URL.  1. **22-inch blocks scored by the horse-drawn marker.** The note reads "The marker was then run at right angles across the first grooves to make a grid of blocks 22 inches square.[^7]". Footnote 7 is `https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s`. ✔ 2. **17% loss over the 1847 [read Light Research - Ice Trade.md in its place]
PASS  judge-reply-no-cut-short   The reply doesn't say any topic or file was cut short. It says the opposite outright: "None of the findings files were cut short. All eight end with the `<!-- end of findings -->` marker."  The rest of the reply covers source disagreements, the front-matter project link, and duplicate footnotes. None of it calls a file incomplete or says one is missing its closing line.
PASS  judge-sixteen-questions-answered   All sixteen questions are answered with the findings' content. None is answered only in general terms, and no answered question is listed as open.  1. **When the ice was cut and how thick:** "usually mid-January into February, after a long hard freeze"; "not cut until it held at least 14 inches of clear ice"; "Each morning a foreman bored test holes with a hand auger." 2. **Tools and block size:* [read Light Research - Ice Trade.md in its place]
PASS  keeps-t1-14-inches  found '14 inch'; read Light Research - Ice Trade.md in its place
PASS  keeps-t1-22-inch-blocks  found '22-inch'; read Light Research - Ice Trade.md in its place
PASS  keeps-t2-17-percent-loss  found '17%'; read Light Research - Ice Trade.md in its place
PASS  keeps-t2-9400-tons  found '9,400'; read Light Research - Ice Trade.md in its place
PASS  keeps-t3-pumped-every-4-hours  found '4 hours'; read Light Research - Ice Trade.md in its place
PASS  keeps-t3-sawdust-1-to-11  found '11 tons'; read Light Research - Ice Trade.md in its place
PASS  keeps-t4-130-days  found '130 days'; read Light Research - Ice Trade.md in its place
PASS  keeps-t4-38-percent-loss  found '38%'; read Light Research - Ice Trade.md in its place
PASS  keeps-t5-1250-tons  found '1,250'; read Light Research - Ice Trade.md in its place
PASS  keeps-t5-barcia  found 'Barcia'; read Light Research - Ice Trade.md in its place
PASS  keeps-t6-75-men  found '75'; read Light Research - Ice Trade.md in its place
PASS  keeps-t6-nine-drownings  found 'nine drown'; read Light Research - Ice Trade.md in its place
PASS  keeps-t7-2-half-cents  found '2½'; read Light Research - Ice Trade.md in its place
PASS  keeps-t7-3-annas  found '3 annas'; read Light Research - Ice Trade.md in its place
PASS  keeps-t8-12-tons-a-day  found '12 tons'; read Light Research - Ice Trade.md in its place
PASS  keeps-t8-margaret-ellery  found 'Margaret Ellery'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-1  found 'https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-2  found 'https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-3  found 'https://www.maritime-salem.example/papers/stowing-ice-1850'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-4  found 'https://www.ice-trade-voyages.example/logs/calcutta-melt-study'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-5  found 'https://www.havana-archive.example/colonial-trade/ice-depot-1840s'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-6  found 'https://www.labor-history-ne.example/winter-work/harvest-crew-sizes'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-7  found 'https://www.gulf-commerce.example/price-current/ice-1860'; read Light Research - Ice Trade.md in its place
PASS  keeps-url-topic-8  found 'https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882'; read Light Research - Ice Trade.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - Ice Trade.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - Ice Trade.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - Ice Trade.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - Ice Trade.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - Ice Trade.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - Ice Trade.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-1-section  found '## Cut'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-2-section  found '## Stor'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-3-section  found '## Load'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-4-section  found '## The voyage'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-5-section  found '## Ice houses at the far port'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-6-section  found '## The worker'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-7-section  found '## Buyers and price'; read Light Research - Ice Trade.md in its place
PASS  shape-topic-8-section  found '## The end'; read Light Research - Ice Trade.md in its place
FAIL  file-name  wrote Light Research - Ice Trade.md instead
````

`project/Research/Light Research - Ice Trade.md`:

````markdown
---
title: Light Research - Ice Trade
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-09 14:00
modified: 2026-10-09 14:00
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> The New England ice trade by sea, from its start (1806) to its end (1880s), traced from frozen pond to hot foreign port. Topics: cutting the ice on the ponds; storing it before shipping; loading the ship; the voyage; ice houses at the far ports; the workers; buyers and prices; the end of the trade. Request: "How did the old ice trade work, from a frozen New England pond to a hot foreign port?" (from `project/Ideas/idea-ice-ship.md`, line 9). Comment: "The New England trade by sea, start to finish."  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Ice Trade

## Summary

> [!tip]-  
> A concise synthesis of the most important findings.
> 
> Focus on what is useful to understand about the subject without translating those findings into story decisions.

The trade began in 1806, when Frederic Tudor sent a cargo from Boston to Martinique. The ice arrived, but there was nowhere to store it and most of it melted.[^1] Its first rule came from that failure: build the ice house before the ice arrives.[^1][^2]

- **Harvest.** Ice was cut in January and February from clear, spring-fed ponds such as Fresh Pond and Wenham Lake. It had to be at least 14 inches thick.[^3][^4] Nathaniel Wyeth's horse-drawn marker and plough, introduced from 1825 and patented in 1829, cut regular 22-inch blocks of about 200 lb. Regular blocks stacked tightly enough to make long voyages possible.[^5][^6][^7][^8]
- **Storage.** The ice was stored for months in huge double-walled, sawdust-filled houses at the ponds. The largest held about 9,400 tons.[^9] One house's 1847 ledger records a 17% loss over the season.[^10]
- **Loading.** The ice went to sea in ordinary merchant ships that would otherwise have left Boston in ballast, so freight was cheap. Each hold got a sawdust-packed lining. The blocks were stowed tight on edge, the hatches were sealed for the whole voyage, and the melt was pumped out every 4 hours.[^11][^12][^13]
- **Routes and loss.** The southern US ports, led by New Orleans, took the most ice. The Caribbean (Havana above all) was short and profitable. Calcutta, about 130 days away, was the famous long route. Ships on it lost an average of 38% of their cargo, against under a tenth on the short routes.[^14][^15][^16][^17]
- **Far ports.** Ice was sold by weight from ice houses that opened only in the early morning. The buyers were colonial elites, hospitals, clubs and cafés, and in New Orleans ordinary households. By 1860 the price there had fallen to about 2½ cents a pound.[^18][^19][^20][^21]
- **Labour.** The work was done by local farmers, then increasingly by Irish and later French-Canadian day labourers. Year-round stevedores loaded the ships, and local porters and hired enslaved men handled the ice abroad.[^22][^23][^24][^25]
- **The end.** The trade peaked around 1860. The Civil War, ice-making machines, steamships and a booming home market for natural ice ended it.[^26] The last recorded Calcutta cargo sailed in 1882.[^27]

## Cutting the ice on the ponds

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**When the ice was ready.** The harvest ran in the coldest weeks, usually mid-January into February, after a long hard freeze.[^3] Firms preferred spring-fed ponds with no inflowing streams, because moving water froze unevenly and carried silt and mill sawdust. Fresh Pond (Cambridge), Wenham Lake (north of Salem) and Spy Pond (Arlington) were the best known. Firms bought or leased the shore rights to keep rivals out.[^3][^28]

Ice was not cut until it held at least 14 inches of clear ice, and white "snow ice" on top did not count. Thinner ice crumbled at the corners, wasted hold space and melted faster.[^3][^4] Each morning a foreman bored test holes with a hand auger and logged the readings in a notebook, along with the dawn and noon temperatures, the wind and any snow.[^3][^4] Cutting often began by the shaded shore and moved outward as the ice thickened.[^4]

Snow was the main enemy. It insulated the ice so it froze more slowly, and wet snow refroze as weak, white snow ice. Crews cleared it with horse-drawn scrapers. On some ponds they also flooded the cleared surface through bored holes to thicken it, which only worked in hard cold.[^29][^30] An "open winter" (a mild one) left the ponds too thin to cut. Shippers then bought dearer ice from Maine and New Hampshire. A thaw or rain mid-season could mean re-planing and recutting a field.[^31][^32] A large pond could be cleared in two to three weeks in a good season.[^31]

**Tools and block size.** Before the 1820s ice was cut by hand with axes, saws and chisels. The blocks were uneven, stacked badly and let warm air in.[^5] Nathaniel Jarvis Wyeth, a Cambridge hotel manager who later worked for Tudor, designed a horse-drawn cutter in 1825 and patented an improved version in 1829. By the 1840s most commercial Massachusetts ponds used some version of his tools.[^5][^6] The sequence of work:

1. **Marker.** A one-horse frame with steel teeth, run along a corded line, scored parallel grooves. A guide arm kept the next groove parallel. The marker was then run at right angles across the first grooves to make a grid of blocks 22 inches square.[^7]
2. **Plough.** A tool with longer teeth was run repeatedly along the same grooves until each cut went about two-thirds through the ice. The uncut third held the field together so men and horses could still walk on it.[^7]
3. **Channel and breaking bars.** Men opened a channel to shore with long hand saws. Bar men split the field along the grooves with "breaking bars," flat chisels on long handles, first into rafts and then into single blocks.[^33][^34]
4. **Pike poles.** Men and boys poled the floating blocks along the channel to shore.[^33][^34]
5. **Elevator.** An inclined chain elevator carried the blocks up into the icehouse. It was driven by a horse capstan, and in the largest houses from the 1850s by small steam engines. Each block was planed flat and cleared of snow ice before it went up.[^35][^36]

A standard first-quality block weighed roughly 200 lb. A tally man counted blocks and turned the count into tons using that figure, and pond owners were paid by the ton.[^8] By the 1850s complete tool sets were sold by specialist makers, many of them in the Hudson valley. The tools changed little over the life of the trade.[^37][^6]

**Grading.** Clear blocks were graded first quality and set aside for shipping. Cloudy or leaf-flecked blocks went to the local Boston market.[^38][^39] Foremen tested clarity by holding a test block up to the light. If they could see a dark object clearly through the full thickness, the ice was good enough.[^40][^38]

## Storing the ice before shipping

**Construction.** The shipping firms built icehouses above ground on the pond shore, so blocks went straight from the channel up the elevator. This replaced the older farm pits dug into hillsides.[^41][^42] The walls were the key feature: an outer and an inner wooden wall, with sawdust or spent tanbark packed between. Some houses had three walls and two layers of fill.[^43][^6] Tudor's and Wyeth's trial houses in the 1820s and 1830s showed that dry fill kept ice far better than damp fill. Houses were therefore built with wide eaves to keep rain off the walls.[^43]

Other features:[^44][^42][^45][^46]
- A steep roof with louvred ridge vents, so warm air could escape.
- A white or light-painted exterior.
- Sometimes hay or straw in the roof space.
- A floor laid over gravel with a drain to the pond, topped with thick sawdust. Ice standing in meltwater melted far faster than ice in air.

Inside, the blocks were set on edge, tight together, each layer laid across the one below like brickwork. Gaps were filled with chips, and the full stack was capped with hay or sawdust.[^41][^47] The stackers were counted among the most skilled men on the harvest.[^41]

**Capacity.** The largest Fresh Pond house held about 9,400 tons. It was taller than a three-storey building and was built as a row of rooms under one roof, so that each room could be filled and emptied separately.[^41][^48] Smaller firms' houses held a few hundred tons.[^41] Smaller houses also stood on the Charlestown wharves, holding a few hundred tons each, to bridge the gap between train and ship.[^49]

From the early 1840s a rail branch ran from Fresh Pond to the Charlestown wharves in under an hour. Its wagons were sawdust-insulated, and in summer the trains ran at night.[^50][^41] A resident keeper looked after each large house. He checked drains and vents, kept the in/out ledger and wrote weekly to the Boston office.[^51] From the 1850s some keepers also logged thermometer readings.[^51]

**Loss in storage.** The 1847 ledger of one Fresh Pond house, kept by weighing samples, records a loss of about 17% between the end of the March harvest and the last autumn sailing. Most of it came in July and August. The keeper blamed the heat and a roof vent left shut. This is the only surviving full-season record for a single house, and historians use it as the standard figure.[^10] A room left unopened until autumn lost less than one opened in June.[^10] Bigger houses lost less, because a big stack has less surface for its weight. That is why houses grew larger through the 1840s and 1850s.[^52][^42] A popular history gives a much wider range; see Disagreement / Uncertainty.

## Loading the ship

**Ships.** The ice went in ordinary merchant ships. Boston imported far more than it exported, so many ships left in ballast. Ice gave them a paying outward cargo, and owners carried it cheaply. Older ships were preferred because the hold had to be fitted with a lining.[^11][^12] Holds were scrubbed and aired before loading, because smells passed into the ice. Ships that had carried fish, hides, molasses or coal were avoided or blacklisted.[^53]

**Packing the hold.** Carpenters built an "ice ceiling": an inner pine lining a little way in from the hull on all sides, packed with sawdust. It turned the hold into an icehouse box. Building one took a carpenter and two helpers about a week for a middling ship.[^54][^11]

1. Dunnage (rough timber) went on the bottom of the hold to keep the cargo clear of the bilge. The lining floor and a deep sawdust bed went on top, with gaps at the sides so melt could drain to the pumps.[^55]
2. The blocks were lowered in slings and stowed by hand, on edge, tight together, each layer crosswise to the one below. Chips and sawdust were pushed into every gap.[^56][^11]
3. The ratio was one ton of sawdust to every 11 tons of ice, according to an 1850 paper by a Salem merchant.[^57] The sawdust was pine waste from Maine mills, brought by schooner, and it had to be dry. Wet sawdust froze to the blocks and conducted heat into them.[^58]
4. The stack was capped with sawdust and hay. The hatches were then closed, covered with tarred canvas and battened down; some ships added a second inner hatch with sawdust between.[^59][^60]

Loading took one to two days for a middling ship and was done at night or in the early morning. The ship sailed on the next tide.[^56][^61]

**Stopping melting and shifting.** Battens were driven between the stack and the lining, and the top layers were wedged against the deck beams. A stack that worked loose in heavy weather meant a much smaller cargo on arrival.[^62] The cargo was stowed low and evenly so the ship sat level. Ships carried less ice than their rated tonnage.[^63] The crew pumped the bilge every 4 hours, day and night, and logged the number of strokes. The stroke count was the only gauge of how fast the ice was melting.[^13] The hatches stayed sealed until port, and a master who opened them without good cause answered for the loss.[^64] Insurers excluded melt loss, so the shipper bore it.[^65][^12]

## The voyage

**Routes and times.**

| Route | Typical passage | Notes |
| --- | --- | --- |
| Caribbean (Havana, Martinique, Jamaica, etc.) | 2–3 weeks with fair winds | Havana one of the steadiest markets; ships every few weeks[^66][^67] |
| Southern US (Charleston, Savannah, Mobile, New Orleans) | Several weeks to New Orleans | Largest market by volume; New Orleans took more New England ice than any other port by the 1850s[^15][^12] |
| Calcutta via the Cape of Good Hope | About 130 days | Crossed the equator twice; first cargo on the *Tuscany*, May–Sept 1833[^14][^60][^68] |
| Bombay, Madras, Hong Kong, Brazil, Valparaíso, Australia | Varied | Less regular; some routes abandoned as unprofitable[^69][^12] |

Calcutta sailings left Boston in autumn and early winter. That way the ice arrived for the March–June hot season and spent its first weeks in cold northern waters.[^14][^12] Caribbean and southern ports were sent ice all year.[^14] Fast ships were chartered for India.[^14] From the 1840s steam tugs towed ships up the Hooghly River, cutting a passage of several days to a day or less.[^70][^53] Masters kept a separate printed "ice book" with columns for position, air and sea temperature, and pumping strokes.[^60][^64]

**How much melted.** Most melting happened in the tropics. Pumping strokes rose sharply near the equator, and the second tropical crossing on the Calcutta run was the worst.[^60] A study of surviving logbooks and receipts found an average loss of **38%** between Boston and Calcutta, varying widely by season, voyage length and stow.[^16] A well-stowed cargo to Havana or New Orleans often lost under a tenth.[^17][^8] Calms in the doldrums cost ice with no distance gained, and masters were told to avoid known calm zones.[^60][^64] Stops at Cape Town, Mauritius or Key West meant opening the hatches, and masters were told to sell quickly and reseal within the hour.[^64][^69]

## Ice houses at the far ports

**Construction and capacity.** The rule after Martinique was that the ice house came first. Firms sent Boston carpenters with the first cargo to a new port to build one or convert a warehouse.[^1][^2]

| Port | Building | Capacity / notes |
| --- | --- | --- |
| Calcutta | Round brick building with a domed roof near the river, paid for by merchants' subscription after 1833. Double walls with packed fill, drained floor, ventilated roof space | About 1,250 tons; brick because of termites and monsoon rot[^71][^72][^73] |
| Havana | Built by Tudor near the harbour in the 1820s, partly sunk below street level for cooler earth | Run under a Spanish colonial monopoly[^74][^73][^75] |
| New Orleans | Several competing houses on the levee by the 1840s, fully above ground (wet ground) | Competition kept prices lower[^73][^15][^76] |
| Bombay, Madras | Masonry, built in the late 1830s and early 1840s on the Calcutta model. Madras house on the beach, with ice landed through the surf | Smaller than Calcutta[^77][^78] |
| Charleston, Savannah | Wood on the Boston plan, raised on brick piers | A few weeks' stock; often owned by local merchants[^79] |
| Hong Kong | Granite waterfront house, 1840s | Small, irregular trade[^80] |

Ice kept much worse in the tropical houses than at the ponds, so agents tried to sell each cargo before the next arrived.[^53]

**Who ran them and how ice was sold.** The Calcutta house was run by an agent sent from Boston with local staff, answerable also to the merchants' committee.[^53][^71] In Havana the agent was a local merchant, Joaquín Barcia, through the 1840s. He sold by **ticket**: customers paid at the city office for a set weight, then redeemed the ticket at the ice house door.[^81] Agents were usually paid a share of sales.[^53]

Ice was sold by weight on a scale at the door. Some houses kept pre-cut blocks of standard weights.[^19][^82] Houses opened at first light and shut by mid-morning; in Calcutta the hours were printed in the newspapers.[^71][^82] Hotels, clubs, hospitals and military messes had monthly accounts and were often served before the queue.[^82][^53] New Orleans had morning delivery carts by the 1850s, while Havana and Calcutta customers mostly collected their ice.[^15] Customers carried ice home wrapped in flannel or blankets in baskets.[^83] In new ports, agents gave ice away until the habit took, and showed people how to cool drinks and make ice cream.[^2][^84]

## The workers

**Who did the work.**
- **Harvest crews.** In the early years these were local farmers and their sons, paid for themselves and their horses during the farm's slack season.[^22][^85] From the 1840s more and more were Irish immigrants, many of them famine-era arrivals, mostly in unskilled jobs.[^23][^86] In the later decades French-Canadian labourers came, and by the 1870s some large-pond crews were mostly French-Canadian.[^87]
- **Boys** from about age twelve guided blocks, swept chips and fetched coffee, for less pay than men.[^34][^22]
- **Women** did not work on the ice. They ran boarding houses, cooked and dried clothes, and the firms' accounts usually paid them under the household's name.[^22][^8]
- **Ship loading** was done by year-round waterfront stevedores, working in gangs under a contracting boss and paid by the ton.[^24]
- **At the far ports** the ice was handled by local porters in Calcutta. In Havana the depot hired enslaved men from their owners to unload the ships.[^25][^53]

**Organisation.** A large-pond crew numbered about 75 men in sequential gangs: snow scrapers, marker and plough, bar men, channel men, elevator, and stackers. The slowest gang set the pace.[^88] A foreman ran each crew under the firm's superintendent.[^38] Labourers were hired by the day at the pond edge, with no promise of work the next day.[^34] Skilled men (marker drivers, stackers, bar men) were hired for the season at higher pay, and firms wrote to ask them back each year.[^38][^22] Pay came on Saturday evenings at the shore shanty, with board deducted.[^8]

**Conditions and dangers.** The workday ran from first light to dark, with lantern work and Sunday cutting when a thaw threatened.[^31] Hazards included:
- Cold and frostbite; men wore wool layers, felt boots and iron "creepers."[^34][^89]
- Wet clothing, which could freeze a man before he reached shelter.[^34][^89]
- Saw and bar cuts, and crushing by blocks on the elevator or a shifting stack. Injured men were paid nothing beyond days already worked.[^89][^34]
- Falling into the open channel. Newspaper reports count nine drownings on the Cambridge ponds between 1850 and 1860, mostly at night.[^89][^31]

Horses falling through the ice were the most common accident.[^34][^30] There were brawls between local and Irish workers,[^86][^90] and short strikes in the 1850s and 1860s timed to thaw forecasts.[^91][^23] Open winters left the labourers without winter wages.[^92]

## Buyers and prices

**Who bought.**
- **Calcutta:** British residents (East India Company officials, officers, merchants), and from early on wealthy Indian families, who by the 1840s were a large share of private customers. Most of the city could not afford ice.[^71][^83] Some Indian households at first doubted its cleanliness.[^82]
- **Everywhere hot:** hospitals were key buyers, using ice for fever, heatstroke and wounds. Calcutta's hospitals had a reduced contract rate, and New Orleans hospitals bought heavily in the 1850s yellow fever epidemics.[^93] Clubs, hotels and messes bought daily.[^83]
- **Havana:** cafés, confectioners (ices and sorbets) and wealthy households.[^75][^84]
- **New Orleans:** bars, hotels, households, meat and fish markets, and river steamboats. By the 1850s the local press called ice a necessity.[^15][^94][^95]
- **Charleston and Savannah:** planters, merchants, hotels and taverns.[^79]
- **Hong Kong:** the garrison, trading houses and ships' officers.[^80]

**What it cost.**
- **Calcutta, 1830s–1840s:** 3 annas a pound (1 anna = 1/16 rupee), steady for about two decades. Account customers sometimes paid less.[^19][^12]
- **Madras and Bombay:** dearer than Calcutta.[^78][^96]
- **Havana:** capped by a government-set maximum under the monopoly, revised several times.[^75]
- **New Orleans:** fell steadily from the 1830s, as competition raised volume, to about **2½ cents a pound by 1860** (city "price current"). The price was higher in the hot months and when ships were late.[^20][^12]

Everywhere, prices were lowest just after a ship arrived and highest when stock ran low. Ice could run out entirely.[^82][^67] The ice cost almost nothing at the pond; ice lost in transit and storage was the largest single cost on the long routes.[^12] The trade made Tudor, the "Ice King," one of the richest men in Boston by the 1840s.[^1] Most profits came from the southern and Caribbean markets.[^1]

## The end of the trade

**What ended it.** No single cause ended the trade. It peaked around 1860, then declined, and by the 1880s long-distance shipping was nearly over.[^26][^97]

- **Civil War (1861–65).** The Union blockade closed the southern ports, and New Orleans was shut until 1862.[^98][^15] Carré ammonia machines were run through the blockade.[^99] After the war, southern cargoes were well below 1850s levels.[^98][^12]
- **Ice machines.** There were early machines by Gorrie (patent 1851), Carré (late 1850s) and Harrison (1850s).[^100][^101] New Orleans's first ice factory opened in 1868 at about 12 tons a day.[^102] By the 1870s factory ice undercut shipped ice once melt loss was counted.[^12] Early machine ice was cloudy and distrusted, which slowed the switch, but it was as clear as natural ice by the 1880s.[^100][^103] Calcutta had a factory by the late 1870s, and Havana factories opened in the 1870s as the monopoly lapsed.[^104][^105]
- **Steamships and the Suez Canal (1869)** shrank the supply of cheap sailing ships going out in ballast.[^14][^12]
- **The home market.** Demand from northern US cities, breweries, meat packers and refrigerated rail cars absorbed the pond output.[^37][^97]
- **Other factors.** The ponds near Boston were fouled or built over, and Fresh Pond became Cambridge's water supply.[^106] Tudor died in 1864.[^107]

**When the last cargoes sailed.** The Indian trade dwindled through the 1870s, and Bombay and Madras ended before Calcutta.[^108] The last recorded Calcutta cargo sailed from Boston in **1882** on the bark *Margaret Ellery*. No later ice ship appears in the Calcutta register.[^27] Some Caribbean and southern shipments may have continued later (see below).[^52][^97] The end passed almost unreported in Boston.[^109] Natural ice for the home market lasted until the 1920s–1940s.[^97]

## Disagreement / Uncertainty

> [!tip]-  
> Claims that are disputed, uncertain, incomplete, changing, or dependent on interpretation.
> 
> Distinguish clearly between:
> 
> - established fact
> 
> - expert consensus
> 
> - plausible interpretation
> 
> - contested claim
> 
> - anecdotal evidence
> 
> - speculation

- **Storage loss (contested figures).** The 1847 Fresh Pond ledger records about 17% over a season, based on weighed samples.[^10] A popular history says a well-built house lost a fifth to a third, and small houses up to half, but gives no source.[^52] The two can't be compared directly. Ledgers that counted blocks show smaller losses than ledgers that weighed them, so loss figures from different houses use incompatible methods.[^110]
- **Calcutta voyage loss (contested figures).** The logbook study finds a 38% average. Its authors warn that surviving papers may over-represent the better-run voyages, so the true average could be higher.[^16] The popular history says well-stowed ships lost about a quarter, with no source and no period given. The gap may reflect improving stowage over time, but neither source dates its figure.[^111]
- **Short-route loss.** "Under a tenth" is an estimate from a small number of voyages.[^17]
- **When the trade ended.** Some histories put the end in the early 1880s. A general history says Caribbean cargoes continued irregularly into the 1890s, and small southern shipments into the early 1900s, but gives no source. The difference may come down to whether "the trade" means the long Asian voyages or any New England ice sent by sea.[^52][^97] The 1882 *Margaret Ellery* voyage is the last *recorded Calcutta* cargo.[^27]
- **End of the Havana monopoly.** The colonial records stop before the monopoly's last years, so the account of its lapse comes from a later research project.[^75][^105]
- **Order of causes of decline.** Historians agree the causes combined. The order in which they mattered varied by port.[^26]
- **Anecdotal or one-sided material.** This includes the fish-tasting cargo (one agent's letter), sailors' early fear of ice cargoes (Tudor's own diary), the rope method for rescuing horses, and ships rolling more as the ice melted (masters' remarks, not measurement).[^53][^113][^30][^63]

## Useful Details

> [!tip]-  
> Interesting or potentially useful details that do not belong cleanly elsewhere.
> 
> These may include small behavioral, material, procedural, linguistic, visual, environmental, or cultural observations.

- To rescue a horse that broke through the ice, crews looped a rope around its neck and pulled it tight. This made the horse hold its breath and float higher, so it could be hauled out. The horses wore spiked, sharp-calked shoes, and a blacksmith was kept near the large ponds.[^34][^30]
- A skilled bar man could tell from the sound of a strike whether the groove was deep enough.[^33]
- One firm told its foremen to reject any block they would not want to see on a dinner table.[^38]
- A pond owner could earn more from one winter's ice rights than from a year of farming the land around it.[^28] Pond owners sometimes sent their own tally man, and disputes over the count survive in letters.[^8]
- One firm dismissed a keeper after he let a drain freeze in early spring, which flooded the lowest room.[^46]
- Icehouses burned easily: dry sawdust and hay caught sparks from passing railway engines. The ice often survived the fire as a block in the ruins, then melted within days.[^112][^42]
- Masters signed a note of the hour the hatches were sealed. Some sealed the joins with wax or pitch so any tampering would show.[^59][^64] In one log a master wrote that he heard the ice "working" in the hold during a gale.[^62]
- In the early years Boston sailors feared that melting ice would sink the ship, and some deserted before sailing.[^113]
- Apples, butter and cheese rode to Calcutta and Havana in pockets cut into the stack, as the master's or agent's private trade.[^53][^114]
- The ship's lining planks were often sold in timber-poor tropical ports.[^54] Return cargoes included jute, indigo, saltpetre and spices from Calcutta, and sugar, molasses and coffee from the Caribbean.[^12]
- The *Tuscany*'s arrival in Calcutta in 1833 drew crowds to the river, and the city's merchants gave her master a gift.[^68]
- Havana ships unloaded into lighters at night, by lantern.[^67] Calcutta servants ran home with baskets of ice on their heads.[^83]
- News of a Calcutta voyage could take most of a year to reach Boston. Later, the overland route through Egypt shortened the wait.[^53][^115]
- The Madras ice house still stands, much altered, as a museum. The Calcutta house was pulled down in the late nineteenth century, and the Havana house has not been traced.[^78][^71]
- "Icebox" and "iceman" grew out of the ice-using habit that the trade helped spread, though they belong more to the home trade.[^103]

## Open Research Questions

> [!tip]-  
> Questions that remain unanswered or would benefit from further research.

- What did harvest labourers, stevedores and ship crews actually earn? The findings describe how they were paid but give no wage figures.
- What did ice cost in Havana, Charleston, Bombay and Madras? The findings give no prices for those ports.
- How large was a typical cargo, in tons, on each route and in each decade?
- Which years do the competing loss figures cover, for both storage and the Calcutta voyage?
- How large were the Havana and New Orleans ice houses?
- Which sea shipments, if any, continued after 1882, and when did the last Caribbean or southern cargo sail?
- What were the working lives of the far-port workers, including the enslaved men hired in Havana, like? No account by the workers themselves survives in these collections.

## Reliability / Limitations

- `harvard-business-archive.example/tudor-papers/*`: These are the largest single source, but they are one firm's own papers. They show its tactics, discipline and complaints from its own side. Tudor's diary records his own view of his difficulties.
- `ma-archives.example/ice-ledgers/wyeth-1847-shrinkage`: The only surviving full-season storage-loss record for a single house. It covers one house in one year.
- `ice-trade-voyages.example/logs/calcutta-melt-study`: Surviving voyage papers may favour well-run voyages.
- `popular-history-press.example/books/the-frozen-water-trade-excerpt`: A general-audience book excerpt. It gives storage-loss, voyage-loss and late-shipment figures without sources.
- `new-england-industry.example/ice/*`: A regional industry site. It cites no archive for its pond-rights figures and gives no count of icehouse fires.
- `walden-region-history.example/oral-histories/ice-crews`: Transcribed in 1974 from people who worked the last commercial harvests, long after the sea trade ended. It may not describe the early trade.
- `farm-journal-archive.example/*`: Advice to farmers, not accounts of commercial harvests or houses.
- `economic-history-review.example/2010/ice-shipping-costs`: The short-route loss figure is an estimate from a few voyages.
- `sailing-ship-logs.example/collections/ice-voyages`: Remarks such as ships rolling more as the ice melted are masters' impressions. Some ice books have gaps of a week or more.
- `boston-newspaper-archive.example/*`: Reports of strikes take the firms' side, reports of fights are short and one-sided, and the drowning count may miss deaths.
- `havana-archive.example/colonial-trade/dock-labour-contracts`: Employers' records only. No account by the workers survives.
- `havana-archive.example/colonial-trade/ice-monopoly`: The records end before the monopoly's last years.
- `memoirs-of-empire.example/collections/calcutta-domestic-life`: British residents describing their own households.
- `calcutta-gazette-archive.example/notices/ice-house-hours`: British newspapers writing about Indian customers.
- `hongkong-heritage.example/waterfront/early-ice-house`: Relies on newspaper notices, with no building records.
- `colonial-architecture-journal.example/2016/cold-storage-in-bengal`: Describes Havana's design mainly as a contrast to Calcutta.
- `gulf-commerce.example/ports/new-orleans-ice-imports`: Gives no list of the factories that closed during the 1870s price war.
- `civil-war-commerce.example/blockade/carre-machines`: The number of machines brought through the blockade is unknown.
- `harvard-business-archive.example/tudor-papers/pond-accounts`: The 200 lb block weight is the firm's working figure, not a measured average.
- `cambridge-historical.example/fresh-pond/icehouses`: The 9,400-ton capacity comes from a company prospectus.

## Sources

[^1]: https://www.harvard-business-archive.example/tudor-papers/diary-excerpts
[^2]: https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt
[^3]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview
[^4]: https://www.harvard-business-archive.example/tudor-papers/harvest-instructions
[^5]: https://www.mit-tech-history.example/inventors/wyeth-ice-tools
[^6]: https://www.patent-records.example/1829/wyeth-ice-cutting-apparatus
[^7]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s
[^8]: https://www.harvard-business-archive.example/tudor-papers/pond-accounts
[^9]: https://www.cambridge-historical.example/fresh-pond/icehouses
[^10]: https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage
[^11]: https://www.maritime-boston.example/trade/outward-cargoes
[^12]: https://www.economic-history-review.example/2010/ice-shipping-costs
[^13]: https://www.sailing-ship-logs.example/collections/ice-voyages
[^14]: https://www.maritime-boston.example/routes/boston-calcutta
[^15]: https://www.gulf-commerce.example/ports/new-orleans-ice-imports
[^16]: https://www.ice-trade-voyages.example/logs/calcutta-melt-study
[^17]: https://www.economic-history-review.example/2010/ice-shipping-costs
[^18]: https://www.calcutta-history-society.example/buildings/the-ice-house
[^19]: https://www.calcutta-gazette-archive.example/notices/ice-house-hours
[^20]: https://www.gulf-commerce.example/price-current/ice-1860
[^21]: https://www.medical-history-journal.example/2013/ice-in-tropical-medicine
[^22]: https://www.labor-history-ne.example/winter-work/farm-families
[^23]: https://www.labor-history-ne.example/winter-work/irish-labour
[^24]: https://www.boston-harbour-history.example/wharves/stevedores
[^25]: https://www.havana-archive.example/colonial-trade/dock-labour-contracts
[^26]: https://www.economic-history-review.example/2010/ice-shipping-costs
[^27]: https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882
[^28]: https://www.new-england-industry.example/ice/pond-rights
[^29]: https://www.new-england-industry.example/ice/snow-and-flooding
[^30]: https://www.farm-journal-archive.example/1856/february/ice-for-market
[^31]: https://www.boston-newspaper-archive.example/1858/january/ice-crop
[^32]: https://www.new-england-industry.example/ice/open-winters
[^33]: https://www.new-england-industry.example/ice/breaking-and-floating
[^34]: https://www.walden-region-history.example/oral-histories/ice-crews
[^35]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview
[^36]: https://www.steam-power-history.example/small-engines/ice-elevators
[^37]: https://www.hudson-valley-museum.example/collections/ice-tool-catalogues
[^38]: https://www.harvard-business-archive.example/tudor-papers/harvest-instructions
[^39]: https://www.boston-markets-history.example/ice/local-trade
[^40]: https://www.walden-region-history.example/oral-histories/ice-crews
[^41]: https://www.cambridge-historical.example/fresh-pond/icehouses
[^42]: https://www.new-england-industry.example/ice/storage-history
[^43]: https://www.harvard-business-archive.example/tudor-papers/storage-trials
[^44]: https://www.farm-journal-archive.example/1859/june/building-an-ice-house
[^45]: https://www.new-england-industry.example/ice/storage-history
[^46]: https://www.harvard-business-archive.example/tudor-papers/storage-trials
[^47]: https://www.walden-region-history.example/oral-histories/ice-crews
[^48]: https://www.massachusetts-engravings.example/prints/fresh-pond-ice-works-1852
[^49]: https://www.boston-harbour-history.example/wharves/charlestown-ice-houses
[^50]: https://www.railroad-history-ma.example/branches/charlestown-ice-line
[^51]: https://www.harvard-business-archive.example/tudor-papers/keepers-letters
[^52]: https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt
[^53]: https://www.harvard-business-archive.example/tudor-papers/agents-letters
[^54]: https://www.maritime-salem.example/papers/ship-fittings-for-ice
[^55]: https://www.maritime-salem.example/papers/ship-fittings-for-ice
[^56]: https://www.boston-harbour-history.example/wharves/stevedores
[^57]: https://www.maritime-salem.example/papers/stowing-ice-1850
[^58]: https://www.maine-lumber-history.example/mills/sawdust-trade
[^59]: https://www.maritime-salem.example/papers/ship-fittings-for-ice
[^60]: https://www.sailing-ship-logs.example/collections/ice-voyages
[^61]: https://www.harvard-business-archive.example/tudor-papers/masters-instructions
[^62]: https://www.sailing-ship-logs.example/collections/ice-voyages
[^63]: https://www.maritime-salem.example/papers/ship-fittings-for-ice
[^64]: https://www.harvard-business-archive.example/tudor-papers/masters-instructions
[^65]: https://www.insurance-history.example/marine/perishable-cargoes
[^66]: https://www.maritime-boston.example/routes/caribbean
[^67]: https://www.havana-archive.example/colonial-trade/shipping-arrivals
[^68]: https://www.calcutta-history-society.example/1833/first-ice-ship
[^69]: https://www.maritime-boston.example/routes/other-ports
[^70]: https://www.calcutta-history-society.example/port/hooghly-pilots-and-tugs
[^71]: https://www.calcutta-history-society.example/buildings/the-ice-house
[^72]: https://www.british-library-images.example/calcutta/ice-house-1840s
[^73]: https://www.colonial-architecture-journal.example/2016/cold-storage-in-bengal
[^74]: https://www.havana-archive.example/colonial-trade/building-permits
[^75]: https://www.havana-archive.example/colonial-trade/ice-monopoly
[^76]: https://www.louisiana-archives.example/levee/warehouse-registers
[^77]: https://www.colonial-architecture-journal.example/2016/cold-storage-in-bengal
[^78]: https://www.madras-heritage.example/beach-road/ice-house
[^79]: https://www.lowcountry-history.example/charleston/ice-trade
[^80]: https://www.hongkong-heritage.example/waterfront/early-ice-house
[^81]: https://www.havana-archive.example/colonial-trade/ice-depot-1840s
[^82]: https://www.calcutta-gazette-archive.example/notices/ice-house-hours
[^83]: https://www.memoirs-of-empire.example/collections/calcutta-domestic-life
[^84]: https://www.food-history-quarterly.example/2012/ice-cream-in-the-tropics
[^85]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview
[^86]: https://www.immigration-history-journal.example/2012/boston-irish-winter-work
[^87]: https://www.immigration-history-journal.example/2015/french-canadians-in-new-england
[^88]: https://www.labor-history-ne.example/winter-work/harvest-crew-sizes
[^89]: https://www.labor-history-ne.example/winter-work/ice-crews-conditions
[^90]: https://www.boston-newspaper-archive.example/1851/january/disturbance-on-the-ice
[^91]: https://www.boston-newspaper-archive.example/1866/february/ice-strike
[^92]: https://www.boston-newspaper-archive.example/1880/march/open-winter-hardship
[^93]: https://www.medical-history-journal.example/2013/ice-in-tropical-medicine
[^94]: https://www.louisiana-archives.example/newspapers/daily-ice-reports
[^95]: https://www.river-history-review.example/2011/steamboat-provisioning
[^96]: https://www.bombay-gazette-archive.example/notices/ice-sales
[^97]: https://www.new-england-industry.example/ice/decline
[^98]: https://www.civil-war-commerce.example/blockade/ice-shortage
[^99]: https://www.civil-war-commerce.example/blockade/carre-machines
[^100]: https://www.mit-tech-history.example/inventors/early-refrigeration
[^101]: https://www.patent-records.example/1851/gorrie-ice-machine
[^102]: https://www.louisiana-archives.example/business/ice-manufacturing-charters
[^103]: https://www.food-history-quarterly.example/2016/clear-ice-and-cloudy-ice
[^104]: https://www.calcutta-history-society.example/industry/bengal-ice-factory
[^105]: https://www.cuba-commerce-history.example/1870s/manufactures
[^106]: https://www.cambridge-historical.example/fresh-pond/water-supply
[^107]: https://www.harvard-business-archive.example/tudor-papers/finding-aid-overview
[^108]: https://www.ice-trade-voyages.example/registers/calcutta-arrivals
[^109]: https://www.boston-newspaper-archive.example/1880s/ice-coverage-survey
[^110]: https://www.ma-archives.example/ice-ledgers/methods-note
[^111]: https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt
[^112]: https://www.boston-newspaper-archive.example/1868/august/icehouse-fire
[^113]: https://www.harvard-business-archive.example/tudor-papers/diary-excerpts
[^114]: https://www.food-history-quarterly.example/2014/new-england-apples-abroad
[^115]: https://www.postal-history-review.example/2009/overland-mail-to-india
````

Final reply:

````
I wrote the note to `project/Research/Light Research - Ice Trade.md`.

None of the findings files were cut short. All eight end with the `<!-- end of findings -->` marker.

- **Disagreements:** The sources disagree on three things, and the note records each one in its "Disagreement / Uncertainty" section:
  - **Ice lost in storage:** the 1847 ledger gives 17%, but an unsourced popular history says a fifth to a third.
  - **Ice lost on the Calcutta voyage:** the logbook study gives an average of 38%, but the same popular history says about a quarter.
  - **When the trade ended:** some sources say the early 1880s, others the 1890s or early 1900s. The last recorded Calcutta cargo sailed in 1882.
- **Front matter:** I left the project link from the template as it was, pointing to Copper Coast. If this note belongs to a different project hub, that link needs changing.
- **Footnotes:** Some sources appear more than once in the Sources list, under different footnote numbers. Obsidian displays them correctly, but merging the repeats would make the list shorter.
````

### W8: Cut short, bare claude-opus-5-5

Case folder: `research-writer-08-cut-short`. Run folder: `bare-w6w8`.

#### Run 1

Grades:

````
FAIL  fm-author  no match
PASS  fm-created-run-date  found 'created: 2026-10-09'
PASS  fm-modified-run-date  found 'modified: 2026-10-09'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
FAIL  judge-dipper-questions-open   The Open Research Questions section covers only the second question (pay and licensing). It does not list the first question, who the dippers were or what they did, as unanswered.  The section reads:  > ## Open Research Questions > > - How were dippers paid: by the bather, by the machine owner, or by the town? What did a dip cost? (Question 4; the findings were cut short.) > - Were dippers licens
PASS  judge-footnotes-resolve   Every marker in the body has a matching definition with a URL, and all eight definitions are used.  **Markers in the body, with an example use of each:** - [^1]: "...each one carried its owner's name. [^1] [^2]". Also used under "How it was moved", "How a bather used it" and "Mixed bathing". - [^2]: "...out of sight of the beach. [^1] [^2]". Also used for male attendants and under "Costume". - [^
FAIL  judge-nothing-from-cut-short   Several topic 2 facts appear in the note, stated as fact, hedge, or question context.  **Strong local women, fishermen's wives/daughters, waist-deep for hours in all weather** - *Summary*: "These were strong local women, often from fishing families, who stood in the sea and plunged each bather under the waves." - *The dippers*: "Dippers were strong local women, often the wives and daughters of fi
PASS  judge-reply-names-topic-2   The reply names topic 2 as cut short: "**Cut short: Topic 2** (the dippers). The findings file for that topic has no `<!-- end of findings -->` marker and holds only two passages."  It does not name any other topic as cut short. It says the others finished normally: "The findings for Topics 1 and 3 ended normally."
PASS  keeps-3-feet  found '3 feet'
PASS  keeps-60-yards  found '60 yards'
PASS  keeps-winch  found 'winch'
FAIL  no-badge  found 'badge'
FAIL  no-cut-short-urls  found 'seaside-trades-history.example'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
FAIL  no-wrenfield  found 'Wrenfield'
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## The bathing machine'
PASS  shape-topic-3-section  found '## Keeping men and women apart'
PASS  file-name  expected name written
````

`project/Research/research-light-bathing-machines.md`:

````markdown
---
title: Light Research - Bathing Machines
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-09 14:00
modified: 2026-10-09 14:00
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Three topics from the request in [[concept-beach-huts|Concept - The Beach Huts]]: how the bathing machine worked, who the dippers were, and the rules that kept men and women apart. Limited to British seaside resorts, 1840 to 1900.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Bathing Machines

## Summary

A bathing machine was a wooden changing hut on four wheels. A horse pulled it into the sea while the bather changed inside, so the bather could step from the seaward door straight into the water without being seen from the beach. At a few steep shingle beaches, a winch on the shore did the hauling instead. Bathers paid for a set time, usually half an hour.

Women bathers were handled by dippers. These were strong local women, often from fishing families, who stood in the sea and plunged each bather under the waves. At the larger resorts dippers were licensed by the town commissioners and wore numbered brass badges.

Town bylaws made under the Town Police Clauses Act 1847 set separate stretches of beach for men and women, often at least 60 yards apart. Men often bathed naked until the 1860s, after which costumes were required. Some resorts began to allow mixed bathing in the 1890s, and as it spread the bathing machine gave way to fixed beach huts and tents.

The findings on the dippers were cut short, so how dippers were paid is still unanswered.

## The bathing machine

**What it was.** A small wooden hut on four large wheels, with a door at each end and steps down from the seaward door. Machines were painted in bright colours or stripes, and each one carried its owner's name. [^1] [^2] *(verified)*

**How it was moved.** At most resorts a horse pulled the machine. The attendant, who owned or hired the machine, led the horse out until the water was about 3 feet deep at the steps. They then unhitched the horse and brought it round to the landward end, ready to pull the machine back. At a few resorts with steep shingle beaches, a winch on the shore hauled the machines up and down on a cable instead. [^1] [^3] *(verified)*

**How a bather used it.** The bather climbed in on the beach in ordinary clothes and changed into a bathing costume while the machine was pulled out. When it stopped, they went down the steps straight into the water, out of sight of the beach. [^1] [^2] *(verified)*

- Women were helped into the water by female attendants called dippers, who stood in the sea beside the steps. Men's machines had male attendants, sometimes called bathers or guides. [^2] *(reported)*
- A bather paid for a set time, usually half an hour. The attendant rang a bell or waved a flag when the time was up, and a bather who stayed too long paid for a second turn. On busy summer mornings at the large resorts, people queued on the beach for a free machine. [^4] *(reported, from an 1865 Brighton guidebook)*

## The dippers

**Who they were and what they did.** Dippers were strong local women, often the wives and daughters of fishermen, who stood waist-deep in the sea for hours in all weather. Each dipper took a woman bather from the machine steps, led her into the water, and plunged her under the waves, which people thought was good for the health. [^5] [^6] *(reported)*

- The best-known dipper at Scarborough in the 1850s was Hannah Wrenfield. She worked the same stretch of beach for over thirty years and was said to have dipped several thousand women. [^5] [^6] *(reported; the number comes from a local obituary)*

**Licensing.** At the larger resorts, the town commissioners licensed dippers. A licensed dipper wore a numbered brass badge on a strap across her shoulder, and her number was entered in the town's register of beach workers. The licence was renewed every May, before the season opened. [^7] *(verified, from Brighton records, 1850s to 1870s)*

**Pay.** No findings. The findings file for this topic was cut short.

## Keeping men and women apart

**The rules.** Most resorts set aside separate stretches of beach for men's machines and women's machines. Local bylaws made under the Town Police Clauses Act 1847 let town councils set the bathing areas and fine anyone who broke the rules. At many resorts the bylaws required men's machines to stand at least 60 yards from women's. [^8] [^4] *(verified)*

**Costume.** Men at many resorts bathed naked until the 1860s, which was one reason for keeping the sexes far apart. From the 1860s, bylaws at most resorts required men to wear a costume, usually a one-piece garment covering the body from neck to knee. [^2] [^8] *(reported)*

**Mixed bathing.** Some resorts began to allow mixed bathing, with men and women in the water together, in the 1890s, usually for families. The change spread slowly, and some town councils still opposed it into the 1900s. As mixed bathing spread, the bathing machine fell out of use and was replaced by fixed beach huts and tents on the sand. [^8] [^1] *(reported)*

## Disagreement / Uncertainty

- **Established (verified):** how the machine was built and moved, how a bather used it, dipper licensing at the larger resorts, and separate beaches under the 1847 Act's bylaws.
- **Reported, single source:** the half-hour hire period, bell or flag signals, and queues come from one 1865 Brighton guidebook and may not apply to every resort. Men's attendants being called "bathers" or "guides" also rests on one article.
- **Anecdotal:** Hannah Wrenfield's "several thousand" women dipped comes from a local obituary.
- **Varies by place:** the dates for mixed bathing differ from town to town, and local practice varied widely. "The 1890s" is a general pattern, not a fixed date. The 60-yard gap held at "many" resorts, not all of them.
- **Unclear:** which resorts used winches, and when, is not dated in the source.

## Useful Details

- Each machine carried its owner's name and was painted in bright colours or stripes.
- The machine was taken out until the water was about 3 feet deep at the steps.
- The horse was unhitched and walked round to the landward end while the bather was in the water.
- A licensed dipper's badge was numbered brass, worn on a strap across the shoulder.
- Dipper licences were renewed every May.
- Men's costumes after the 1860s were usually one piece, from neck to knee.

## Open Research Questions

- How were dippers paid: by the bather, by the machine owner, or by the town? What did a dip cost? (Question 4; the findings were cut short.)
- Were dippers licensed at smaller resorts, or only at the larger ones?
- Which resorts used winches instead of horses, and in which years?
- What did a machine cost to hire, and did prices differ between men's and women's machines?

## Reliability / Limitations

- **Topic 2 findings:** the file has no end-of-findings marker, so it was cut short. It holds only two passages, and the question on pay has no answer.
- `coastal-towns-archive.example` (Hastings): covers one town and names the winch resorts without dates.
- `seaside-trades-history.example` / `yorkshire-coast-archive.example`: the number of women dipped comes from a local obituary.
- `east-sussex-records.example`: Brighton records only. Licensing practice elsewhere is assumed for "larger resorts" but not shown.
- `resort-guides-digitized.example` (1865 Brighton guide): a single primary source for hire times and queues, from one resort and one year.
- `legal-history-review.example`: says local practice varied widely and dates differ from town to town.

## Sources

[^1]: https://www.seaside-heritage.example/collections/bathing-machines (museum collection article, 2018)
[^2]: https://www.victorian-leisure-journal.example/2014/the-bathing-machine (peer-reviewed article, 2014)
[^3]: https://www.coastal-towns-archive.example/hastings/beach-engineering (local history society page, 2012)
[^4]: https://www.resort-guides-digitized.example/1865/brighton-visitors-guide (digitized resort guidebook, 1865)
[^5]: https://www.seaside-trades-history.example/occupations/dippers (local history society page, 2016)
[^6]: https://www.yorkshire-coast-archive.example/scarborough/beach-workers (digitized town records with catalogue notes, 1840s to 1860s)
[^7]: https://www.east-sussex-records.example/brighton/beach-licences (county record office catalogue entry, 1850s to 1870s)
[^8]: https://www.legal-history-review.example/2011/seaside-bylaws (peer-reviewed article, 2011)
````

Final reply:

````
I wrote the light note at `project/Research/research-light-bathing-machines.md`.

**Cut short: Topic 2** (the dippers). The findings file for that topic has no `<!-- end of findings -->` marker and holds only two passages. As a result, question 4 is only half answered: the note covers how dippers were licensed but has nothing on how they were paid. I've flagged that gap in the topic's section and listed it under Open Research Questions and Reliability / Limitations.

The findings for Topics 1 and 3 ended normally. The note has one section for each of the plan's three topics, in the plan's order.
````

#### Run 2

Grades:

````
FAIL  fm-author  no match; read Light Research - Bathing Machines.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-09'; read Light Research - Bathing Machines.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-09'; read Light Research - Bathing Machines.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - Bathing Machines.md in its place
FAIL  fm-sources-empty  no match; read Light Research - Bathing Machines.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - Bathing Machines.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - Bathing Machines.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - Bathing Machines.md in its place
FAIL  judge-dipper-questions-open   The Open Research Questions section lists payment and touches on licensing, but it never lists "who the dippers were / what they did" as unanswered.  The section in full:  > ## Open Research Questions > > - **How were dippers paid?** (Plan question 4.) The topic 2 findings stop after the licensing passage, with no end-of-findings marker, so the research was cut short and payment is unanswered. Di [read Light Research - Bathing Machines.md in its place]
PASS  judge-footnotes-resolve   **Every marker in the body has a definition:** - `[^1]`: e.g. "Machines were painted in bright colours or stripes, and each carried its owner's name. [^1] [^2]" - `[^2]`: same line, and "Men's machines had male attendants, sometimes called bathers or guides. [^2]" - `[^3]`: "hauled up and down on a cable by a winch on the shore instead of by a horse. [^3]" - `[^4]`: "bathers queued on the beach f [read Light Research - Bathing Machines.md in its place]
FAIL  judge-nothing-from-cut-short   Topic 2 facts show up in many places in the note:  **Summary** - "Women bathers were handled by dippers: strong local women, often from fishing families, who stood in the sea and led or plunged each bather under the waves." - "At the larger resorts dippers were licensed and wore numbered badges."  **The dippers** - "Dippers were strong local women, often the wives and daughters of fishermen, who  [read Light Research - Bathing Machines.md in its place]
PASS  judge-reply-names-topic-2   The reply names topic 2 as cut short: "**Cut short: topic 2 (The dippers).** That findings file has no `<!-- end of findings -->` marker and stops after the licensing passage."  It names no other topic as cut short. It says the other two were complete: "Topics 1 and 3 came back complete."
PASS  keeps-3-feet  found '3 feet'; read Light Research - Bathing Machines.md in its place
PASS  keeps-60-yards  found '60 yards'; read Light Research - Bathing Machines.md in its place
PASS  keeps-winch  found 'winch'; read Light Research - Bathing Machines.md in its place
FAIL  no-badge  found 'badge'; read Light Research - Bathing Machines.md in its place
FAIL  no-cut-short-urls  found 'seaside-trades-history.example'; read Light Research - Bathing Machines.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
FAIL  no-wrenfield  found 'Wrenfield'; read Light Research - Bathing Machines.md in its place
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - Bathing Machines.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - Bathing Machines.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - Bathing Machines.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - Bathing Machines.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - Bathing Machines.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - Bathing Machines.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - Bathing Machines.md in its place
PASS  shape-topic-1-section  found '## The bathing machine'; read Light Research - Bathing Machines.md in its place
PASS  shape-topic-3-section  found '## Keeping men and women apart'; read Light Research - Bathing Machines.md in its place
FAIL  file-name  wrote Light Research - Bathing Machines.md instead
````

`project/Research/Light Research - Bathing Machines.md`:

````markdown
---
title: Light Research - Bathing Machines
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-09 14:00
modified: 2026-10-09 14:00
sources:
  - https://www.seaside-heritage.example/collections/bathing-machines
  - https://www.victorian-leisure-journal.example/2014/the-bathing-machine
  - https://www.coastal-towns-archive.example/hastings/beach-engineering
  - https://www.resort-guides-digitized.example/1865/brighton-visitors-guide
  - https://www.seaside-trades-history.example/occupations/dippers
  - https://www.yorkshire-coast-archive.example/scarborough/beach-workers
  - https://www.east-sussex-records.example/brighton/beach-licences
  - https://www.legal-history-review.example/2011/seaside-bylaws
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Three topics from the request in [[concept-beach-huts]]: the bathing machine itself, the dippers who worked them, and the rules that kept men and women apart (including when mixed bathing came in). The writer's comment limits this to British seaside resorts, 1840 to 1900.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Bathing Machines

## Summary

> [!tip]-  
> A concise synthesis of the most important findings.
> 
> Focus on what is useful to understand about the subject without translating those findings into story decisions.

A bathing machine was a wheeled wooden changing hut. It was pulled into the sea, usually by a horse, so a bather could change on the way out and step down into the water out of sight of the beach. Women bathers were handled by dippers: strong local women, often from fishing families, who stood in the sea and led or plunged each bather under the waves. At the larger resorts dippers were licensed and wore numbered badges. Local bylaws under the Town Police Clauses Act of 1847 kept men's and women's machines on separate stretches of beach. From the 1860s men had to wear costumes. Mixed bathing began at some resorts in the 1890s, and as it spread the machines gave way to fixed beach huts and tents. The findings on dippers were cut short: nothing came back on how dippers were paid.

## The bathing machine

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**What it was.** A small wooden hut on four large wheels, with a door at each end and steps down from the seaward door. Machines were painted in bright colours or stripes, and each carried its owner's name. [^1] [^2]

**How it was moved.** At most resorts a horse pulled the machine into the sea and back. The attendant, who owned or hired the machine, led the horse out until the water stood about 3 feet deep at the steps, unhitched it, and brought it round to the landward end, ready to pull the machine back to the beach. [^1] [^3] At a few resorts with steep shingle beaches the machines were hauled up and down on a cable by a winch on the shore instead of by a horse. [^3]

**How a bather used one.** The bather climbed in on the beach in ordinary clothes and changed into a bathing costume inside while the machine was pulled out. When it stopped, the bather went down the steps straight into the water, out of sight of the beach. [^1] [^2] Women were helped into the water by female attendants (dippers) standing in the sea beside the steps. Men's machines had male attendants, sometimes called bathers or guides. [^2]

**Time and payment.** A bather paid for a set time in the machine, usually half an hour. The attendant rang a bell or waved a flag when the time was up, and a bather who stayed too long paid for a second turn. On busy summer mornings at the large resorts, bathers queued on the beach for a free machine. [^4]

## The dippers

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Who they were and what they did.** Dippers were strong local women, often the wives and daughters of fishermen, who stood waist-deep in the sea for hours in all weather. They took each woman bather from the machine steps, led her into the water, and plunged her under the waves, which was thought to be good for the health. [^5] [^6]

The best-known dipper at Scarborough in the 1850s was Hannah Wrenfield. She worked the same stretch of beach for over thirty years and was said to have dipped several thousand women. [^5] [^6]

**Licensing.** At the larger resorts dippers had to be licensed by the town commissioners. A licensed dipper wore a numbered brass badge on a strap across her shoulder, and the number was entered in the town's register of beach workers. The licence was renewed every May, before the season opened. [^7]

**Pay.** No findings. The findings for this topic were cut short (see Open Research Questions).

## Keeping men and women apart

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**The rules.** Most resorts set aside separate stretches of beach for men's and women's machines. Local bylaws made under the Town Police Clauses Act of 1847 gave town councils the power to set the bathing areas and to fine anyone who broke the rules. [^8] [^4] At many resorts the bylaws required the men's machines to stand at least 60 yards from the women's. [^8] [^4]

**Costume.** Men at many resorts bathed naked until the 1860s, which was one reason for keeping the sexes far apart. From the 1860s, bylaws at most resorts required men to wear a costume, usually a one-piece garment covering the body from neck to knee. [^2] [^8]

**Mixed bathing.** Mixed bathing, with men and women in the water together, began to be allowed at some resorts in the 1890s, usually for families. The change spread slowly, and some town councils still opposed it into the 1900s. As mixed bathing spread, the bathing machine fell out of use and was replaced by fixed beach huts and tents on the sand. [^8] [^1]

## Disagreement / Uncertainty

> [!tip]-  
> Claims that are disputed, uncertain, incomplete, changing, or dependent on interpretation.
> 
> Distinguish clearly between:
> 
> - established fact
> 
> - expert consensus
> 
> - plausible interpretation
> 
> - contested claim
> 
> - anecdotal evidence
> 
> - speculation

- **Established (verified in the findings):** the machine's construction and use; horse-drawn operation and the roughly 3-foot depth; separate beaches under 1847-Act bylaws and the 60-yard rule; dipper licensing with numbered badges at the larger resorts.
- **Reported, not verified:**
  - The male/female attendant split. Rests on one journal article.
  - The half-hour time slot, the bell or flag, and queuing. Rests on one 1865 Brighton guidebook, so it may not hold for other resorts or other decades.
  - The dippers' social background and the plunging practice.
  - Men bathing naked until the 1860s, and the 1860s costume bylaws.
  - Mixed bathing from the 1890s.
- **Anecdotal:** that Hannah Wrenfield dipped "several thousand women" comes from a local obituary.
- **Varies by place:** the dates for mixed bathing differ from town to town, and local practice varied widely. "Most resorts" and "many resorts" in the findings shouldn't be read as all.
- **Partly outside scope:** the opposition to mixed bathing "into the 1900s" and the machine's replacement by beach huts run past the 1900 end of the plan's period. The findings give no date for the replacement.

## Useful Details

> [!tip]-  
> Interesting or potentially useful details that do not belong cleanly elsewhere.
> 
> These may include small behavioral, material, procedural, linguistic, visual, environmental, or cultural observations.

- Each machine carried its owner's name painted on it, in bright colours or stripes. [^1]
- The horse was unhitched once the machine was out and walked round to the landward end. [^1]
- Male attendants were sometimes called "bathers" or "guides". [^2]
- A dipper's brass badge hung on a strap across her shoulder. [^7]
- Dipper licences were renewed every May. [^7]
- Overstaying the half-hour meant paying for a second turn. [^4]

## Open Research Questions

- **How were dippers paid?** (Plan question 4.) The topic 2 findings stop after the licensing passage, with no end-of-findings marker, so the research was cut short and payment is unanswered. Did dippers earn wages from machine owners, take a share of fees, or get tips from bathers? And what did a licence cost?
- Which resorts used the shingle-beach winch system, and when? [^3]
- Who licensed dippers at smaller resorts, if anyone? The findings cover only the larger ones.
- When, roughly, did beach huts and tents replace machines at particular resorts?

## Reliability / Limitations

- `seaside-heritage.example` (museum collection article, 2018): general overview; reliable for the machine itself.
- `victorian-leisure-journal.example` (peer-reviewed article, 2014): the only source for the male/female attendant split.
- `coastal-towns-archive.example` (local history society page, 2012): covers one town (Hastings) and names the winch resorts without dates.
- `resort-guides-digitized.example` (1865 Brighton visitors' guide): a primary source, but for one resort in one year.
- `seaside-trades-history.example` (local history society page, 2016): the dipper count comes from a local obituary.
- `yorkshire-coast-archive.example` (digitized Scarborough town records, 1840s to 1860s): primary records with catalogue notes.
- `east-sussex-records.example` (county record office catalogue entry, Brighton, 1850s to 1870s): supports licensing, but for Brighton; "the larger resorts" is a generalisation from it.
- `legal-history-review.example` (peer-reviewed article, 2011): says local practice varied widely and dates differ by town.
- General: the dippers topic came back incomplete.

## Sources

[^1]: https://www.seaside-heritage.example/collections/bathing-machines
[^2]: https://www.victorian-leisure-journal.example/2014/the-bathing-machine
[^3]: https://www.coastal-towns-archive.example/hastings/beach-engineering
[^4]: https://www.resort-guides-digitized.example/1865/brighton-visitors-guide
[^5]: https://www.seaside-trades-history.example/occupations/dippers
[^6]: https://www.yorkshire-coast-archive.example/scarborough/beach-workers
[^7]: https://www.east-sussex-records.example/brighton/beach-licences
[^8]: https://www.legal-history-review.example/2011/seaside-bylaws
````

Final reply:

````
I wrote the light note at `project/Research/Light Research - Bathing Machines.md`.

**Cut short: topic 2 (The dippers).** That findings file has no `<!-- end of findings -->` marker and stops after the licensing passage. So plan question 4, on how dippers were paid, has no answer. The note says so in the dippers section and lists it first under Open Research Questions. Topics 1 and 3 came back complete.

I left `tags` empty as the template has it. The `created` and `modified` fields use the run date (2026-10-09 14:00).
````

#### Run 3

Grades:

````
FAIL  fm-author  no match; read Light Research - Bathing Machines.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-09'; read Light Research - Bathing Machines.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-09'; read Light Research - Bathing Machines.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - Bathing Machines.md in its place
FAIL  fm-sources-empty  no match; read Light Research - Bathing Machines.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - Bathing Machines.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - Bathing Machines.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - Bathing Machines.md in its place
FAIL  judge-dipper-questions-open   The Open Research Questions section lists the pay question but not the question of who the dippers were or what they did. The section reads in full:  > - How were dippers paid: by the bather, by the machine owner, or by fee per dip? (Question 4 is only half answered. The dippers findings were cut short.) > - Did the dippers findings contain more material that was lost when the file was cut short? [read Light Research - Bathing Machines.md in its place]
PASS  judge-footnotes-resolve   **Markers in the body.** The body uses exactly eight markers, [^1] through [^8]. Examples: - [^1], [^2]: "each carried its owner's name. [^1] [^2]" - [^3]: "hauled the machines up and down on a cable instead. [^1] [^3]" - [^4]: "bathers queued on the beach for a free machine. [^4]" - [^5], [^6]: "which was thought to be good for the health. [^5] [^6]" - [^7]: "renewed every May, before the season [read Light Research - Bathing Machines.md in its place]
FAIL  judge-nothing-from-cut-short   The note uses topic 2 facts in many sections, both as plain fact and as hedges.  **Summary** - "Women bathers were handled by female "dippers": strong local women, often from fishing families, who led each bather into the water and plunged her under." (strong local women, fishing families, plunging) - "At the larger resorts the town commissioners licensed dippers and gave them numbered badges." ( [read Light Research - Bathing Machines.md in its place]
PASS  judge-reply-names-topic-2   The reply names topic 2 as cut short: "**Cut short: topic 2 (the dippers).** Its findings file has no end-of-findings marker and contains only two passages."  It names no other topic as cut short. It says the others were complete: "Topics 1 and 3 were complete."
PASS  keeps-3-feet  found '3 feet'; read Light Research - Bathing Machines.md in its place
PASS  keeps-60-yards  found '60 yards'; read Light Research - Bathing Machines.md in its place
PASS  keeps-winch  found 'winch'; read Light Research - Bathing Machines.md in its place
FAIL  no-badge  found 'badge'; read Light Research - Bathing Machines.md in its place
FAIL  no-cut-short-urls  found 'seaside-trades-history.example'; read Light Research - Bathing Machines.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
FAIL  no-wrenfield  found 'Wrenfield'; read Light Research - Bathing Machines.md in its place
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - Bathing Machines.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - Bathing Machines.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - Bathing Machines.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - Bathing Machines.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - Bathing Machines.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - Bathing Machines.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - Bathing Machines.md in its place
PASS  shape-topic-1-section  found '## The bathing machine'; read Light Research - Bathing Machines.md in its place
PASS  shape-topic-3-section  found '## Keeping men and women apart'; read Light Research - Bathing Machines.md in its place
FAIL  file-name  wrote Light Research - Bathing Machines.md instead
````

`project/Research/Light Research - Bathing Machines.md`:

````markdown
---
title: Light Research - Bathing Machines
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-09 14:00
modified: 2026-10-09 14:00
sources:
  - https://www.seaside-heritage.example/collections/bathing-machines
  - https://www.victorian-leisure-journal.example/2014/the-bathing-machine
  - https://www.coastal-towns-archive.example/hastings/beach-engineering
  - https://www.resort-guides-digitized.example/1865/brighton-visitors-guide
  - https://www.seaside-trades-history.example/occupations/dippers
  - https://www.yorkshire-coast-archive.example/scarborough/beach-workers
  - https://www.east-sussex-records.example/brighton/beach-licences
  - https://www.legal-history-review.example/2011/seaside-bylaws
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Requested from `project/Concepts/concept-beach-huts.md`, line 9: how bathing machines at Victorian seaside resorts worked, who the dippers who ran them were, and what rules kept men and women apart on the beach. Three topics: the bathing machine, the dippers, and keeping men and women apart. Limited to British seaside resorts, 1840 to 1900.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Bathing Machines

## Summary

> [!tip]-  
> A concise synthesis of the most important findings.
> 
> Focus on what is useful to understand about the subject without translating those findings into story decisions.

A bathing machine was a wheeled wooden hut. It was pulled into the sea, usually by a horse, while the bather changed inside, so that the bather could step down into the water out of sight of the beach. Attendants ran the machines. Women bathers were handled by female "dippers": strong local women, often from fishing families, who led each bather into the water and plunged her under. At the larger resorts the town commissioners licensed dippers and gave them numbered badges. Under bylaws made through the Town Police Clauses Act of 1847, men's and women's machines were kept on separate stretches of beach, often at least 60 yards apart. Men at many resorts bathed naked until the 1860s, when costumes became compulsory. Some resorts began allowing mixed bathing in the 1890s, and as it spread the bathing machine gave way to fixed beach huts and tents.

## The bathing machine

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**What it was.** A small wooden hut on four large wheels, with a door at each end and steps down from the seaward door. Machines were painted in bright colours or stripes and each carried its owner's name. [^1] [^2]

**How it was moved.** At most resorts a horse pulled the machine into the sea and back. The attendant, who owned or hired the machine, led the horse out until the water stood about 3 feet deep at the steps. They then unhitched the horse and brought it round to the landward end, ready to pull the machine back to the beach. [^1] At a few resorts with steep shingle beaches, a winch on the shore hauled the machines up and down on a cable instead. [^1] [^3]

**How a bather used it.** The bather climbed in on the beach in ordinary clothes and changed into a bathing costume while the machine was pulled out. When it stopped, the bather went down the steps straight into the water, out of sight of the beach. [^1] [^2] Women bathers were helped into the water by female attendants, the dippers, who stood in the sea beside the steps. Men's machines had male attendants, sometimes called "bathers" or "guides." [^2]

**Time and payment.** Bathers paid for a set time in the machine, usually half an hour. The attendant rang a bell or waved a flag when the time was up, and a bather who stayed too long paid for a second turn. On busy summer mornings at the large resorts, bathers queued on the beach for a free machine. [^4]

## The dippers

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Who they were and what they did.** Dippers were strong local women, often the wives and daughters of fishermen, who stood waist-deep in the sea for hours in all weather. They took each woman bather from the machine steps, led her into the water, and plunged her under the waves, which was thought to be good for the health. [^5] [^6]

The best-known dipper at Scarborough in the 1850s was Hannah Wrenfield. She worked the same stretch of beach for over thirty years and was said to have dipped several thousand women. [^5] [^6]

**Licensing.** At the larger resorts, dippers had to be licensed by the town commissioners. A licensed dipper wore a numbered brass badge on a strap across her shoulder, and the number was entered in the town's register of beach workers. The licence was renewed every May, before the season opened. [^7]

**Pay.** Nothing found. See Open Research Questions.

## Keeping men and women apart

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Separate beaches.** Most resorts set aside separate stretches of beach for men's and women's machines. Local bylaws made under the Town Police Clauses Act of 1847 gave town councils the power to set the bathing areas and to fine anyone who broke the rules. At many resorts the bylaws required men's machines to stand at least 60 yards from women's. [^8] [^4]

**Costume rules.** Men at many resorts bathed naked until the 1860s, which was one reason for keeping the sexes far apart. From the 1860s, bylaws at most resorts required men to wear a costume, usually a one-piece garment covering the body from neck to knee. [^2] [^8]

**Mixed bathing.** Some resorts began to allow mixed bathing, with men and women in the water together, in the 1890s, usually for families. The change spread slowly, and some town councils still opposed it into the 1900s. As mixed bathing spread, the bathing machine fell out of use and was replaced by fixed beach huts and tents on the sand. [^8] [^1]

## Disagreement / Uncertainty

> [!tip]-  
> Claims that are disputed, uncertain, incomplete, changing, or dependent on interpretation.
> 
> Distinguish clearly between:
> 
> - established fact
> 
> - expert consensus
> 
> - plausible interpretation
> 
> - contested claim
> 
> - anecdotal evidence
> 
> - speculation

- **Verified by the researchers:** the machine's design and how it was used; horse and winch haulage; dipper licensing and badges; separate beaches and the 1847 Act bylaws.
- **Reported, not verified:** attendants' titles ("dipper," "bather," "guide"); half-hour hire periods and bells or flags; who the dippers were and the dipping practice; male nude bathing until the 1860s and the costume bylaws that followed; the dates for mixed bathing and for the machine falling out of use.
- **Anecdotal:** the claim that Hannah Wrenfield dipped "several thousand" women comes from a local obituary.
- **Varies by place:** the legal-history source says local practice varied widely and dates differ from town to town. The 1860s and 1890s dates and the 60-yard distance should be read as typical, not universal.
- **Incomplete:** the findings for the dippers topic end abruptly, without the researcher's end marker, so that topic may be missing material (see Reliability / Limitations).

## Useful Details

> [!tip]-  
> Interesting or potentially useful details that do not belong cleanly elsewhere.
> 
> These may include small behavioral, material, procedural, linguistic, visual, environmental, or cultural observations.

- Each machine bore its owner's name and was painted in bright colours or stripes. [^1]
- A licensed dipper's numbered brass badge hung from a strap across her shoulder. [^7]
- Dipper licences were renewed every May, before the season opened. [^7]
- Hire time was signalled with a bell or a flag. [^4]
- The water was about 3 feet deep at the steps when the horse was unhitched. [^1]
- Men's costume covered the body from neck to knee. [^2] [^8]

## Open Research Questions

> [!tip]-  
> Questions that remain unanswered or would benefit from further research.

- How were dippers paid: by the bather, by the machine owner, or by fee per dip? (Question 4 is only half answered. The dippers findings were cut short.)
- Did the dippers findings contain more material that was lost when the file was cut short? Topic 2 could be re-run.
- Which resorts used winch-hauled machines, and when? The source names them without dates.
- What did a machine hire cost, and how did prices vary between resorts?
- When did particular resorts allow mixed bathing? Dates vary by town.

## Reliability / Limitations

- `topic-2 findings (the dippers)`: the file was cut short. It has no end-of-findings marker and contains only two passages. The question of how dippers were paid has no findings, and other material may be missing.
- `https://www.coastal-towns-archive.example/hastings/beach-engineering`: a local history society page covering one town. It names the winch resorts without dates.
- `https://www.seaside-trades-history.example/occupations/dippers`: the "several thousand women" figure for Hannah Wrenfield comes from a local obituary.
- `https://www.legal-history-review.example/2011/seaside-bylaws`: says local practice varied widely and dates differ from town to town.
- `https://www.resort-guides-digitized.example/1865/brighton-visitors-guide`: a period guidebook for one resort, the sole source for the hire-time and queuing details.
- `https://www.east-sussex-records.example/brighton/beach-licences`: a catalogue entry for Brighton records, 1850s to 1870s. The sole source for licensing, so other resorts may have differed.

## Sources

[^1]: https://www.seaside-heritage.example/collections/bathing-machines (museum collection article, 2018)
[^2]: https://www.victorian-leisure-journal.example/2014/the-bathing-machine (peer-reviewed article, 2014)
[^3]: https://www.coastal-towns-archive.example/hastings/beach-engineering (local history society page, 2012)
[^4]: https://www.resort-guides-digitized.example/1865/brighton-visitors-guide (digitized resort guidebook, 1865)
[^5]: https://www.seaside-trades-history.example/occupations/dippers (local history society page, 2016)
[^6]: https://www.yorkshire-coast-archive.example/scarborough/beach-workers (digitized town records with catalogue notes, 1840s to 1860s)
[^7]: https://www.east-sussex-records.example/brighton/beach-licences (county record office catalogue entry, 1850s to 1870s)
[^8]: https://www.legal-history-review.example/2011/seaside-bylaws (peer-reviewed article, 2011)
````

Final reply:

````
The note is at `project/Research/Light Research - Bathing Machines.md`.

**Cut short: topic 2 (the dippers).** Its findings file has no end-of-findings marker and contains only two passages. Nothing was found on how dippers were paid, so question 4 is only half answered. More material may also be missing. The note says this in Open Research Questions and in Reliability / Limitations. Topics 1 and 3 were complete.

I kept the template's `project:` link to the Copper Coast hub as it was. I set the created and modified dates to the run date, 2026-10-09 14:00.
````
