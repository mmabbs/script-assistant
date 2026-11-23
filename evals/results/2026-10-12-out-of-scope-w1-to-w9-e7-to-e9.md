# 2026-10-12 Agent Runs: Out-of-Scope Findings, W1 to W9 and E7 to E9

The research-writer and research-evaluator ran after their files took on spec-research-workflow.md 11 items 100 and 101: a finding outside the plan's limits may be left out, unless it plainly changes the answer to a plan question, and then the research-evaluator fails the note that leaves it out. The new cases W9, E8, and E9 test that. The five older research-writer cases and E7 ran again to check nothing broke. A worker who wrote no agent file wrote the new cases; the writer approved their Pass lines before the runs. Claude checked each failed check by hand and read the three W9 notes.

## What Was Run

- **Date:** 2026-10-12, 19:56 to 20:02 EDT.
- **Agents:** `script-asst:research-writer` (claude-opus-5-5) and `script-asst:research-evaluator` (claude-sonnet-5-5), each at effort high, as their agent files pin.
- **Claude Code:** 2.1.296.
- **Runs:** 27 agent runs, three per case. No bare runs.
- **Commands,** from the plugin's `evals/`:

```bash
python3 _tools/research-run.py --out <dir>/evaluator --agent script-asst:research-evaluator --runs 3 --cases research-evaluator-07-live-fog-signals research-evaluator-08-out-of-scope-kept research-evaluator-09-out-of-scope-dropped
python3 _tools/research-run.py --out <dir>/writer --agent script-asst:research-writer --runs 3 --cases research-writer-01-planted-figure research-writer-02-coverage-gap research-writer-03-source-trail research-writer-06-eight-topics research-writer-08-cut-short research-writer-09-out-of-scope-findings
```

- **Errors and timeouts:** none. Every run exited 0. No run was repeated.

## Summary Table

| Case | All checks | Checks passed, r1 / r2 / r3 | Earlier today |
| --- | --- | --- | --- |
| W1 `research-writer-01-planted-figure` | 2 of 3 | 27 / 26 / 27 of 27 | 3 of 3 |
| W2 `research-writer-02-coverage-gap` | 3 of 3 | 27 / 27 / 27 of 27 | 3 of 3 |
| W3 `research-writer-03-source-trail` | 3 of 3 | 29 / 29 / 29 of 29 | 3 of 3 |
| W6 `research-writer-06-eight-topics` | 3 of 3 | 54 / 54 / 54 of 54 | 3 of 3 |
| W8 `research-writer-08-cut-short` | 3 of 3 after the judge fix (2 of 3 before) | 30 / 30 / 30 of 30 | 3 of 3 |
| W9 `research-writer-09-out-of-scope-findings` | 3 of 3 | 28 / 28 / 28 of 28 | new |
| E7 `research-evaluator-07-live-fog-signals` | 3 of 3 | 6 / 6 / 6 of 6 | 3 of 3 |
| E8 `research-evaluator-08-out-of-scope-kept` | 3 of 3 | 4 / 4 / 4 of 4 | new |
| E9 `research-evaluator-09-out-of-scope-dropped` | 3 of 3 | 4 / 4 / 4 of 4 | new |

## Findings

1. **Items 100 and 101 work on every new case.** W9: every note keeps the 1875 to 1885 finding with its footnote, says in plain words it lies before the period asked about, and answers all four questions. All three put it in the Summary as the main finding and set it against the 1908 rider under Disagreement / Uncertainty. All three leave out the Kellard Brothers. E8: the research-evaluator passes the clean note in every run and never fails it for the Kellard Brothers. E9: it fails the note in every run with one "nothing dropped" problem naming the 1875 to 1885 passage, and no other problem.
2. **E7 no longer reports the bell passage.** This morning's live check failed the note over the dropped bell passage, which lay mostly outside the 1950s. None of today's three runs reports it, and each still names all three real problems. The extra overstatements some runs report also appeared in this morning's E7 runs.
3. **W8 r1 is a judge error, not an agent error.** `judge-nothing-from-cut-short` failed the note for listing "How was their work licensed or paid?" under Open Research Questions, saying the licence idea came from the cut-short file. That question is the plan's question 4 word for word (`research-plan-bathing-machines.md`), and listing an unanswered plan question is what research-writer.md rule 5 asks for. The judge now says a question that restates a plan question is not a topic 2 fact. A regrade of the saved runs, judges only, gives 3 of 3. The first regrade reused the old answer, because an interrupted regrade had saved the new prompt without an answer; the stale answers were set aside as `.stale` and the regrade run again.
4. **W1 r2 left out the `## Disagreement / Uncertainty` heading.** Its findings hold no contradictions, so nothing went missing, but research-writer.md "The File" item 4 lists that section in every note. It isn't tied to items 100 and 101. One run in three; this morning's three runs kept it. The writer accepted it as a slip that costs the reader nothing, with no rule added.
5. **Checked after the runs: the research-evaluator fails all three W9 notes.** It ran once on each saved W9 note, with E8's prompt, at $0.04 a run. Every note fails "matches findings" on a sentence that carries the 1875 to 1885 finding into the period asked about, with no footnote: r1 "By 1905 to 1914 the penny-farthing was no longer ordinary transport in England." (Summary, and a second sentence in Topic 1); r2 the same Summary sentence and "no English maker had offered in its catalogue for more than a decade"; r3 "a machine that had been out of production for over a decade, not ordinary transport." Passage 3 says penny-farthings were everyday transport "only from about 1875 to 1885" and that no maker offered one by 1892. It says nothing about 1905 to 1914. r2 and r3 also fail on calling one fall "the main danger," which topic-2.md never ranks. In a live run each note would go to the fix round.
6. **The fix round, tested the same way: 1 of 3 notes pass the second check.** Each W9 note went back to the research-writer with its problems, worded as `workflows/research.js` words a fix round, and then to the research-evaluator again. Costs: fix rounds $0.27, second checks $0.09.
    - **r3 passes.**
    - **r1 fails on a sentence the first check missed.** Disagreement / Uncertainty: "The two don't strictly conflict. But the 1908 evidence is a single photograph caption about a single rider, so it shows that such riding happened, not how common it was." The sentence was in the first draft.
    - **r2 fails on the sentences that explain why the finding is there.** "That earlier history falls outside the period asked about, but it bears on how to read the answer for 1905 to 1914." and "It is included because it changes how the 1905 to 1914 picture should be read." Both were in the first draft too, and the first check didn't report them. It also fails "Some people still rode them in those years," resting on one rider.
    - **Two causes.** The research-evaluator's first check doesn't report every problem, so the one fix round can't clear what it never heard about. That is spec-research-workflow.md 11 item 97's problem again. And research-writer.md rule 7 asks the writer to place the finding where it bears on the answer; the writer then explains how it bears, and that explanation fails as a conclusion no passage holds.
    - In a live run, r1 and r2 would come back failed, though each holds the decisive finding, footnoted.
    - **r2's fix round also wrote a stray file outside `Research/`:** `r2/work/README-fix-round.txt`, holding only "placeholder". The writer named the slip itself. None of the other five W9 fix rounds wrote outside `Research/`. This ran headless with acceptEdits, outside the permission hook, which now approves the writer's writes only in `Research/` and `draft-1.md` (spec-run-manager.md 11 items 89 and 94). Found 2026-10-30 in the run's transcript.
7. **After research-writer.md rule 7 dropped "Put it where it bears on the answer it changes," the whole chain passes 3 of 3.** The rule now says to state the finding, footnote it, say it lies outside what was asked, and stop, without explaining what it means for the scope asked about. W9 ran again through the runner (28 of 28 checks in each run, $0.82), then the research-evaluator, a fix round where it failed, and a second check ($0.25). r2 passed the first check. r1 failed on "The main danger was being thrown over the handlebars head first," and r3 on one sentence missing its footnotes; each fix round cleared its one problem, and the second check passed. No note explained what the earlier dates mean for 1905 to 1914. Raw folders: `w9-chain/` in the session's scratchpad.

## Caveats

1. **One judge call per check, not repeated.**
2. **Cost:** printed totals, judges included: research-writer $9.44, research-evaluator $0.97.
3. **The raw run folders are in the session's scratchpad** and go when the Mac restarts. Each run's grades, what it wrote, and its reply are copied below.

## Full Outputs

Each run shows its grades, then every file it wrote or changed, then its final reply.

### W1: Planted figure, research-writer agent

Case folder: `research-writer-01-planted-figure`. Run folder: `writer`.

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
PASS  judge-footnotes-resolve   Every marker used in the body has a definition with a URL, and every definition is used.  **Markers in the body:** - `[^1]` and `[^2]` appear together, e.g. "The iron has no galvanizing or other metal coating.[^1][^2]" - `[^3]` appears in "Since the campaign that began in 2019, the finish coats have been lead-free.[^3]" - `[^4]` appears with `[^1]`, e.g. "They don't use spray guns.[^1][^4]" - `[^
PASS  judge-no-outside-facts   Every factual claim the note makes about the tower matches an item on the list, or plainly restates one:  - **Rust protection:** "The tower's iron has no galvanizing or other metal coating, so paint is its only barrier against rust." This is list item 1. - **Paint system:** "Each campaign scrapes damaged areas back to bare metal. It then applies an anti-corrosion primer, followed by two finish co
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

File written: `project/Research/research-light-eiffel-tower-upkeep.md`

````
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
> Two topics: how the Eiffel Tower is protected from rust, and who repaints the tower and how often. Limits: present-day practice, with a short historical note where a source gives one.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Eiffel Tower Upkeep

## Summary

Paint is the only thing keeping the Eiffel Tower's iron from rusting. The iron has no galvanizing or other metal coating.[^1][^2] In each repainting campaign, damaged areas are scraped back to bare metal and given an anti-corrosion primer, followed by two finish coats.[^1][^2] Since the campaign that began in 2019, the finish coats have been lead-free.[^3] The painters work by hand with brushes and rollers while roped to the structure. They don't use spray guns.[^1][^4]

According to the operating company, the Société d'Exploitation de la Tour Eiffel (SETE), the tower is repainted every 5 years.[^5][^6] A campaign takes about 18 months and is carried out by a team of about 25 specialist painters.[^1][^4]

## How the tower is protected from rust

### What protects the iron

The tower's iron has no galvanizing or other metal coating, so paint is its only barrier against rust.[^1][^2]

### The paint system

Each campaign scrapes damaged areas back to bare metal. It then applies an anti-corrosion primer, followed by two finish coats.[^1][^2]

The finish coats have been lead-free since the campaign that began in 2019. Earlier coats contained lead. The 2019 campaign was delayed after lead was found in dust around the site.[^3]

### How the paint is put on

Painters apply the paint by hand with brushes and rollers while roped to the structure.[^1][^4] They don't use spray guns, because wind would carry the overspray onto visitors and the streets below.[^1][^4]

The colour, called "Eiffel Tower Brown," is applied in three shades. The darkest is at the base and the lightest at the top, so the tower looks like one even colour against the sky.[^7]

## Who repaints the tower, and how often

### Who does the work

A campaign is carried out by a team of about 25 specialist painters.[^1][^4] The repainting cycle is set by the company that runs the tower, the Société d'Exploitation de la Tour Eiffel (SETE).[^5][^6]

### How often, and for how long

The tower is repainted every 5 years.[^5][^6] The cycle used to be longer. It was shortened after corrosion surveys in the 2000s.[^5][^6]

A campaign takes about 18 months. Work pauses during the worst winter weather.[^1][^4]

## Disagreement / Uncertainty

- The lead-free finish coats, the lead in earlier coats, and the 2019 delay all come from a single newspaper report from April 2019.[^3] No other source in the findings confirms them.
- The 5-year cycle and its shortening after the 2000s corrosion surveys come from the operator's own annual report[^5] and from a heritage magazine article.[^6] The annual report is the operator describing its own work.[^5]

## Open Research Questions

- Who employs the team of about 25 specialist painters: SETE itself or an outside contractor?
- What did the longer repainting interval used to be before it was shortened to 5 years?

## Reliability / Limitations

- `toureiffel.paris (maintenance page)`: The operator's own page, current.
- `toureiffel.paris (colour page)`: The operator's own page, current. It is the only source for the three-shade colour scheme.
- `construction-history.example`: A peer-reviewed journal article, 2021.
- `paris-daily.example`: A newspaper report, April 2019. It is the only source for the lead-free finish coats and the 2019 delay.
- `paintingcontractor-mag.example`: A trade magazine feature, 2022.
- `sete-annual-report.example`: The operator's annual report, 2022. It is the operator describing its own work.
- `french-heritage-review.example`: A heritage magazine article, 2020.

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
PASS  judge-footnotes-resolve   The body uses seven distinct markers, and each one has a definition under Sources with a URL.  - `[^1]` appears in Summary, "What protects the iron", "How the paint is put on", "Who does the work" and "How often, and how long". Its definition is `[^1]: https://www.toureiffel.paris/en/the-monument/maintenance`. - `[^2]` appears in Summary and "What protects the iron". Its definition is `[^2]: http
PASS  judge-no-outside-facts   Every factual claim the note makes about the tower matches an item on the list or restates one plainly:  - **Rust protection:** "Paint is the only barrier against rust" and "The tower's iron has no galvanizing or other metal coating" match the first item. - **Campaign sequence:** "Damaged areas are scraped back to bare metal. / An anti-corrosion primer goes on. / Two finish coats follow" matches 
PASS  keeps-18-months  found '18 months'
PASS  keeps-25-painters  found '25'
PASS  keeps-five-year-cycle  found 'every 5'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-paint-tonnage  no match
PASS  no-seven-year-cycle  no match
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
FAIL  shape-disagreement  no match
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

File written: `project/Research/research-light-eiffel-tower-upkeep.md`

````
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
> Two topics: how the Eiffel Tower is protected from rust, and who repaints the tower and how often. Limits for the whole request: present-day practice, with a short historical note where a source gives one.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Eiffel Tower Upkeep

## Summary

Paint is the only thing standing between the Eiffel Tower's iron and rust. The iron has no galvanizing or other metal coating.[^1][^2] Each repainting campaign scrapes damaged areas back to bare metal, then puts on an anti-corrosion primer and two finish coats.[^1][^2] The finish coats have been lead-free since the campaign that began in 2019.[^3] Painters roped to the structure do the work by hand with brushes and rollers. They don't use spray guns.[^1][^4]

A team of about 25 specialist painters carries out each campaign. A campaign takes about 18 months, and work pauses in the worst winter weather.[^1][^4] The tower is repainted every 5 years. The company that runs the tower, the Société d'Exploitation de la Tour Eiffel (SETE), sets that cycle.[^5][^6]

## How the tower is protected from rust

### What protects the iron

The tower's iron has no galvanizing or other metal coating. Paint is the only barrier against rust.[^1][^2]

Each campaign follows the same sequence:[^1][^2]

1. Damaged areas are scraped back to bare metal.
2. An anti-corrosion primer goes on.
3. Two finish coats follow.

### Lead and the 2019 campaign

The finish coats have been lead-free since the campaign that began in 2019. Earlier coats contained lead. The 2019 campaign was delayed after lead was found in dust around the site.[^3]

### How the paint is put on

Painters work by hand with brushes and rollers, roped to the structure. Spray guns are not used, because wind would carry the overspray onto visitors and the streets below.[^1][^4]

## Who repaints the tower, and how often

### Who does the work

A campaign is carried out by a team of about 25 specialist painters.[^1][^4]

### How often, and how long

The tower is repainted on a cycle of every 5 years. The cycle is set by the company that runs the tower, the Société d'Exploitation de la Tour Eiffel (SETE). It was shortened from a longer interval after corrosion surveys in the 2000s.[^5][^6]

A campaign takes about 18 months. Work pauses in the worst winter weather.[^1][^4]

## Useful Details

The tower's colour is called "Eiffel Tower Brown." It is put on in three shades: darkest at the base and lightest at the top. The grading makes the tower look one even colour against the sky.[^7]

## Open Research Questions

- What was the longer repainting interval used before the cycle was shortened to every 5 years?
- Do the roughly 25 specialist painters work for SETE itself or for an outside contractor?

## Reliability / Limitations

- `toureiffel.paris (maintenance page)`: the operator's own page, current. It describes the operator's own work.
- `toureiffel.paris (colour page)`: the operator's own page, current. It describes the operator's own work.
- `SETE annual report, 2022`: the operator's annual report. The operator is describing its own work.
- `Construction history journal, 2021`: a peer-reviewed journal article.
- `Paris Daily, April 2019`: a newspaper report from April 2019, written at the start of the campaign it describes.
- `Painting contractor magazine, 2022`: a trade magazine feature.
- `French Heritage Review, 2020`: a heritage magazine article.

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
PASS  judge-footnotes-resolve   **Every marker has a definition.** The body uses exactly seven distinct markers, `[^1]` through `[^7]`: - `[^1]` and `[^2]`: "The iron has no galvanizing or other metal coating.[^1][^2]" - `[^3]`: "the finish coats have been lead-free.[^3]" - `[^4]`: "Spray guns aren't used.[^1][^4]" - `[^5]` and `[^6]`: "The tower is repainted every five years.[^5][^6]" - `[^7]`: "The tower's colour is called "E
PASS  judge-no-outside-facts   Every factual claim the note makes about the tower matches an item on the list or plainly restates one:  - **Rust protection:** "The tower's iron carries no galvanizing or other metal coating, so paint is the only barrier against rust." This matches the first fact. - **Campaign sequence:** "Damaged areas are scraped back to bare metal. / An anti-corrosion primer is applied. / Two finish coats go 
PASS  keeps-18-months  found '18 months'
PASS  keeps-25-painters  found '25'
PASS  keeps-five-year-cycle  found 'five-year'
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

File written: `project/Research/research-light-eiffel-tower-upkeep.md`

````
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
> Two topics: how the Eiffel Tower is protected from rust (what protects the iron, and how the paint is put on), and who repaints the tower and how often (who carries out a repainting campaign, how often the tower is repainted, and how long a campaign takes). Limits: present-day practice, with a short historical note where a source gives one.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Eiffel Tower Upkeep

## Summary

Paint is the only thing standing between the Eiffel Tower's iron and rust. The iron has no galvanizing or other metal coating.[^1][^2] Each repainting campaign scrapes damaged areas back to bare metal, applies an anti-corrosion primer, and then adds two finish coats.[^1][^2] Since the campaign that began in 2019, the finish coats have been lead-free.[^3] The paint goes on by hand, with brushes and rollers, from painters roped to the structure. Spray guns aren't used.[^1][^4]

The tower is repainted on a five-year cycle, set by its operator, the Société d'Exploitation de la Tour Eiffel (SETE).[^5][^6] A campaign is carried out by a team of about 25 specialist painters and takes about 18 months, with a pause in the worst winter weather.[^1][^4]

## How the tower is protected from rust

### What protects the iron

The tower's iron carries no galvanizing or other metal coating, so paint is the only barrier against rust.[^1][^2]

Each campaign follows the same sequence:[^1][^2]

1. Damaged areas are scraped back to bare metal.
2. An anti-corrosion primer is applied.
3. Two finish coats go on over the primer.

The finish coats have been lead-free since the campaign that began in 2019.[^3] Earlier coats contained lead. The 2019 campaign was delayed after lead was found in dust around the site.[^3]

### How the paint is put on

Painters work by hand with brushes and rollers, roped to the structure.[^1][^4] Spray guns aren't used, because wind would carry the overspray onto visitors and the streets below.[^1][^4]

## Who repaints the tower, and how often

### Who does the work

A repainting campaign is carried out by a team of about 25 specialist painters.[^1][^4] The repainting cycle is set by the company that runs the tower, the Société d'Exploitation de la Tour Eiffel (SETE).[^5][^6]

### How often, and how long

The tower is repainted every five years.[^5][^6] That cycle was shortened from a longer interval after corrosion surveys in the 2000s.[^5][^6]

A single campaign takes about 18 months.[^1][^4] Work pauses in the worst winter weather.[^1][^4]

## Disagreement / Uncertainty

- The lead-free finish coats, the lead in earlier coats, and the 2019 delay come from a single newspaper report from April 2019.[^3] No second source in the findings confirms them.
- One of the two sources for the five-year cycle is the operator's own annual report, so the operator is describing its own work there.[^5] The other source is a heritage magazine article from 2020.[^6]

## Useful Details

- The tower's colour is called "Eiffel Tower Brown."[^7]
- It's put on in three shades: darkest at the base and lightest at the top. This makes the tower look one even colour against the sky.[^7]

## Open Research Questions

- How long was the repainting interval before it was shortened, and what did the corrosion surveys of the 2000s find?
- Do the painters work for SETE directly or for an outside contractor?

## Reliability / Limitations

- `toureiffel.paris (maintenance and colour pages)`: the operator's own current pages, describing its own work.
- `Construction history journal (2021)`: a peer-reviewed journal article.
- `Paris daily newspaper (April 2019)`: a newspaper report. It's the only source for the lead-free coats and the 2019 lead delay.
- `Painting contractor trade magazine (2022)`: a trade magazine feature.
- `SETE annual report (2022)`: the annual report is the operator describing its own work.
- `French heritage review (2020)`: a heritage magazine article.

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

Case folder: `research-writer-02-coverage-gap`. Run folder: `writer`.

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
PASS  judge-footnotes-resolve   Every marker in the body has a definition with a URL, and every definition is used.  **Markers in the body:** - `[^1]`: Summary ("...to a burner inside the glass lantern.[^1][^2]") and under "Fuel and supply" and "Lighting and putting out". - `[^2]`: Summary, "Fuel and supply", and "Useful Details" ("not by the police.[^2][^3]"). - `[^3]`: Summary ("a round covered about 70 lamps.[^3]"), "How man
PASS  judge-pay-in-open-questions   The Open Research Questions section asks about pay directly:  > ## Open Research Questions > > - What was a lamplighter paid in 1880s London? The surviving vestry wage books at the London Metropolitan Archives are offline. > - Did the size of a round differ between parishes, or between vestry and gas-company lamplighters?  The note gives no wage figure anywhere. Every mention of pay says it was n
PASS  judge-three-questions-answered   **1. Fuel and how it reached the lamp:** answered with the required detail. Under "Fuel and supply": "The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and rose through each lamp post to a burner inside the glass lantern." This covers coal gas, the gasworks, cast-iron mains under the streets, and the lamp post.  **2. How a lamp was lit and put out:**
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

File written: `project/Research/research-light-london-gas-lamps.md`

````
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
> Two topics: how London's gas street lamps worked, and the lamplighters who looked after them (how many lamps one man tended, and what he was paid). Limits for the whole request: London only, and the 1880s.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - London Gas Lamps

## Summary

London's gas street lamps burned coal gas made at the gasworks, carried under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern.[^1][^2] A lamplighter lit them with a long pole that had a hook for turning the gas tap and a small oil-fed flame for lighting the burner, working an evening round at dusk and a second round at dawn to turn them off.[^1] Districts were divided into rounds by the gas companies and parish vestries; in the parish of St Pancras in 1884, a round covered about 70 lamps.[^3] No source found gave a lamplighter's wages for the 1880s; vestry wage books survive for some parishes but have not been put online.[^5]

## How the gas street lamps worked

### Fuel and supply

The lamps burned coal gas made at the gasworks.[^1][^2] The gas ran under the streets in cast-iron mains and rose through each lamp post to a burner inside the glass lantern.[^1][^2]

### Lighting and putting out

The lamplighter carried a long pole. At its top was a hook for turning the gas tap, and a small oil-fed flame for lighting the burner.[^1] He lit his lamps on an evening round at dusk and turned them off on a second round at dawn.[^1]

The evening round began about half an hour before sunset, so in winter a lamplighter started work in mid-afternoon. The dawn round began before first light.[^4]

## The lamplighters

### How many lamps one man tended

The gas companies and parish vestries divided each district into rounds.[^3] According to the 1884 minutes of the St Pancras vestry's lighting committee, a lamplighter's round covered about 70 lamps, and he walked it twice a day, at dusk and at dawn.[^3]

### Pay

No source found in this search gave lamplighters' wages for the 1880s. A guide to the London Metropolitan Archives says vestry wage books survive for some parishes but have not been put online.[^5]

## Disagreement / Uncertainty

- The figure of about 70 lamps per round comes from one parish's records (St Pancras, 1884), so it may not hold for other London parishes or for the gas companies' rounds.[^3]

## Useful Details

- Lamplighters were employed by the gas companies or by the parish vestries, not by the police.[^2][^3]
- Besides lighting and putting out the lamps, lamplighters cleaned the lamp glass once a week and reported broken lamps to the vestry.[^2][^3]

## Open Research Questions

- What was a lamplighter paid in 1880s London? The surviving vestry wage books at the London Metropolitan Archives are offline.
- Did the size of a round differ between parishes, or between vestry and gas-company lamplighters?

## Reliability / Limitations

- `London Museum, "Gas lighting in Victorian streets"`: museum collection article, 2018.
- `Gas History Society, "Metropolitan mains"`: society research paper, 2011.
- `St Pancras vestry minutes, lighting committee, 1884`: digitized parish vestry minutes; they cover one parish.
- `London Streets History, "Lamplighter"`: local history society page, 2015.
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
PASS  judge-footnotes-resolve   Every marker in the body has a matching definition with a URL, and every definition is used:  - **[^1]** is used in "a burner inside the glass lantern.[^1][^2]" and elsewhere. It is defined as `[^1]: https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets`. - **[^2]** is used in "The lamps burned coal gas made at the gasworks.[^1][^2]" and elsewhere. It is defined as `[^2]:
PASS  judge-pay-in-open-questions   The Open Research Questions section asks what lamplighters were paid:  > ## Open Research Questions > > - What was a London lamplighter paid in the 1880s? The vestry wage books that survive for some parishes at the London Metropolitan Archives have not been put online.[^5] > - Did lamplighters' rounds in other London parishes, or on gas-company rounds, also cover about 70 lamps?  The note gives n
PASS  judge-three-questions-answered   **Q1: Fuel and how it reached the lamp.** Answered with the required detail. - "The lamps burned coal gas made at the gasworks." - "The gas reached each lamp through cast-iron mains under the streets. From the mains it ran up through the lamp post to a burner inside the glass lantern."  **Q2: How a lamp was lit and put out.** Answered with the required detail. - "The lamplighter carried a long po
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

File written: `project/Research/research-light-london-gas-lamps.md`

````
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
> Two topics: how London's gas street lamps worked (their fuel, how the gas reached them, and how they were lit and put out), and the lamplighters (how many lamps one man looked after and what he was paid). Limits: London only, and the 1880s.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - London Gas Lamps

## Summary

London's street lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern.[^1][^2] A lamplighter lit the lamp with a long pole. The pole had a hook at the top for turning the gas tap and a small oil-fed flame for lighting the burner. He lit his lamps on an evening round at dusk and turned them off on a second round at dawn.[^1] The gas companies and parish vestries divided each district into rounds. In St Pancras parish's 1884 vestry minutes, one round covered about 70 lamps.[^3] The lamplighters worked for the gas companies or the parish vestries, not for the police.[^2][^3] For pay, a guide to the London Metropolitan Archives says vestry wage books survive for some parishes but have not been put online.[^5]

## How the gas street lamps worked

### Fuel and supply

The lamps burned coal gas made at the gasworks.[^1][^2] The gas reached each lamp through cast-iron mains under the streets. From the mains it ran up through the lamp post to a burner inside the glass lantern.[^1][^2]

### Lighting and putting out

The lamplighter carried a long pole with two working parts: a hook at the top for turning the gas tap, and a small oil-fed flame for lighting the burner.[^1] To light a lamp, he turned on the tap with the hook and lit the burner with the flame. He put it out by turning the gas tap off.[^1]

He worked two rounds a day. On the evening round, at dusk, he lit his lamps. On a second round, at dawn, he turned them off.[^1] The evening round began about half an hour before sunset, so in winter a lamplighter started work in mid-afternoon. The dawn round began before first light.[^4]

## The lamplighters

### How many lamps one man looked after

The gas companies and parish vestries divided each district into rounds. In St Pancras, a lamplighter's round covered about 70 lamps, and he walked it twice a day, at dusk and at dawn.[^3] This figure comes from the 1884 minutes of the St Pancras vestry's lighting committee, which cover that one parish.[^3]

### Who employed them

Lamplighters were employed by the gas companies or by the parish vestries, not by the police.[^2][^3]

### Pay records

A guide to the London Metropolitan Archives says vestry wage books survive for some parishes but have not been put online.[^5]

## Disagreement / Uncertainty

- **Lamps per round:** The figure of about 70 lamps comes from one parish's records, the 1884 St Pancras vestry minutes.[^3] Whether rounds elsewhere in London were the same size is not settled by these findings.

## Useful Details

- Besides lighting and putting out the lamps, lamplighters cleaned the lamp glass once a week and reported broken lamps to the vestry.[^2][^3]

## Open Research Questions

- What was a London lamplighter paid in the 1880s? The vestry wage books that survive for some parishes at the London Metropolitan Archives have not been put online.[^5]
- Did lamplighters' rounds in other London parishes, or on gas-company rounds, also cover about 70 lamps?

## Reliability / Limitations

- `London Museum, "Gas lighting in Victorian streets"`: Museum collection article, 2018.
- `Gas History Society, "Metropolitan mains"`: Society research paper, 2011.
- `St Pancras vestry minutes, lighting committee, 1884`: Digitized parish vestry minutes, 1884. The minutes cover one parish.
- `London street history, "Lamplighter"`: Local history society page, 2015.
- `London Metropolitan Archives guide, "Vestry wage books"`: Archive research guide, 2021.

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
PASS  judge-footnotes-resolve   Every marker in the body has a definition with a URL, and every definition is used.  - **[^1]** is used in the Summary ("burner inside the glass lantern.[^1][^2]"), and under Fuel and supply and Lighting and putting out. Its definition is `[^1]: https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets`. - **[^2]** is used in the Summary, Fuel and supply, and "not by the poli
PASS  judge-pay-in-open-questions   The Open Research Questions section asks what lamplighters were paid. Its first bullet reads:  > - What was a lamplighter in 1880s London paid? The surviving vestry wage books held at the London Metropolitan Archives, which have not been put online, are the lead the search turned up.[^5]  The full section:  > ## Open Research Questions > > - What was a lamplighter in 1880s London paid? The surviv
PASS  judge-three-questions-answered   All three questions are answered, each with the required details.  1. **Fuel and how it reached the lamp.** Under "Fuel and supply": "The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern." This covers coal gas, the gasworks, the cast-iron mains under the streets, and the route up the lam
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

File written: `project/Research/research-light-london-gas-lamps.md`

````
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
> Two topics: how London's gas street lamps worked (their fuel, how it reached the lamp, and how a lamp was lit and put out), and the lamplighters (how many lamps one man looked after, and what he was paid). Limits for the whole request: London only, and the 1880s.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - London Gas Lamps

## Summary

London's gas street lamps burned coal gas made at the gasworks, which ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern.[^1][^2] A lamplighter lit them on an evening round at dusk, using a long hooked pole to turn the gas tap and a small oil-fed flame to light the burner, and turned them off on a second round at dawn.[^1] The gas companies and parish vestries divided each district into rounds; St Pancras vestry minutes from 1884 put a round at about 70 lamps.[^3] No source found gave lamplighters' wages for the 1880s; vestry wage books survive for some parishes but have not been put online.[^5]

## How the gas street lamps worked

### Fuel and supply

The lamps burned coal gas made at the gasworks.[^1][^2] The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern.[^1][^2]

### Lighting and putting out

The lamplighter carried a long pole with a hook at the top for turning the gas tap, and a small oil-fed flame for lighting the burner.[^1] He lit his lamps on an evening round at dusk and turned them off on a second round at dawn.[^1]

The evening round began about half an hour before sunset, so in winter a lamplighter started work in mid-afternoon.[^4] The dawn round began before first light.[^4]

## The lamplighters

### Who employed them and what they did

Lamplighters were employed by the gas companies or by the parish vestries, not by the police.[^2][^3] Besides lighting and putting out the lamps, they cleaned the lamp glass once a week and reported broken lamps to the vestry.[^2][^3]

### How many lamps one man tended

The gas companies and parish vestries divided each district into rounds.[^3] A lamplighter's round covered about 70 lamps, and he walked it twice a day, at dusk and at dawn.[^3] This figure comes from the 1884 lighting committee minutes of a single parish, St Pancras.[^3]

### Pay

No source found in this search gave lamplighters' wages for the 1880s.[^5] A guide to the London Metropolitan Archives says vestry wage books survive for some parishes but have not been put online.[^5]

## Disagreement / Uncertainty

- The figure of about 70 lamps per round rests on one parish's records (St Pancras, 1884).[^3] Whether rounds elsewhere in London were the same size is not established by the sources found.

## Open Research Questions

- What was a lamplighter in 1880s London paid? The surviving vestry wage books held at the London Metropolitan Archives, which have not been put online, are the lead the search turned up.[^5]
- Did the size of a lamplighter's round in other London parishes, or under the gas companies, match the roughly 70 lamps recorded for St Pancras?

## Reliability / Limitations

- `London Museum, "Gas lighting in Victorian streets"`: museum collection article, 2018.
- `Gas History Society, "Metropolitan mains"`: society research paper, 2011.
- `St Pancras vestry, lighting committee minutes, 1884`: digitized parish vestry minutes; the minutes cover one parish.
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
````

### W3: Source trail, research-writer agent

Case folder: `research-writer-03-source-trail`. Run folder: `writer`.

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
PASS  judge-claims-carry-right-source   1. **Slope.** "That is an average of about 25 centimetres per kilometre. [^1] [^2]" and "falls only about 12.6 metres over its whole length of about 50 kilometres." Both footnotes are allowed:    - [^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient    - [^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul  2. **Water commissioner, Frontinus and the staff of ab
PASS  judge-footnotes-resolve   Every marker in the body has a definition under Sources, every definition holds a URL, and every definition is used in the body.  **Markers in the body:** - `[^1]` and `[^2]`: "surveyors set that slope over the whole route before building began. [^1] [^2]" and in "Keeping the water flowing downhill." - `[^3]`: "builders used inverted siphons of sealed lead pipe. [^3] [^4]" and in "Arches, and wha
PASS  judge-tally-only-as-question   The tally marks appear in exactly one place, under Open Research Questions, phrased as a question:  > **## Open Research Questions** > "- Is there a source for the tally marks at Nîmes, said to have been cut into the channel wall after each cleaning?"  The entry is borderline. It goes beyond the check's example ("Is there a source for the tally marks at Nîmes?") by restating the claim's detail ("
PASS  judge-urls-from-findings   The Sources section has seven URLs, and each one matches an entry on the allowed list character for character:  - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` - `[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul` - `[^3]: https://www.lyon-archaeology.example/aqueducts/siphons` - `[^4]: https://www.ancient-texts-library.example/frontinus/de-aquaeduct
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

File written: `project/Research/research-light-roman-aqueducts.md`

````
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
> Topic 1: How the aqueducts were built. Topic 2: How the aqueducts were kept running. Limited to the city of Rome and Roman Gaul, up to the 3rd century AD.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Roman Aqueducts

## Summary

Roman aqueducts moved water by gravity on a very gentle, steady slope. The aqueduct that supplied Nîmes drops only about 12.6 metres over about 50 kilometres, and surveyors set that slope over the whole route before building began. [^1] [^2] Arches carried the channel across valleys to keep the slope steady. Where a valley was too deep for arches, as at Lyon, builders used inverted siphons of sealed lead pipe. [^3] [^4]

In Rome, the water commissioner (the *curator aquarum*) was responsible for the aqueducts, and a staff of about 700 slaves repaired and cleaned the channels. [^4] [^5] The main upkeep problem the findings describe is sinter: layers of calcium carbonate left by hard water, which narrowed the channel and had to be chipped out. [^6] [^7]

## How the aqueducts were built

### Keeping the water flowing downhill

The aqueduct that supplied Nîmes falls only about 12.6 metres over its whole length of about 50 kilometres. That is an average of about 25 centimetres per kilometre. [^1] [^2]

Surveyors set this slope with levelling instruments over the whole route before building began. [^1] [^2]

### Arches, and what replaced them in deep valleys

Arches carried the channel across valleys so the slope could stay steady. [^3] [^4]

Where a valley was too deep for arches, as at Lyon, builders used inverted siphons. These were sealed lead pipes that ran down one side of the valley and up the other. The water was pushed up the far side by its own pressure. [^3] [^4]

## How the aqueducts were kept running

### Who was responsible

In Rome, the water commissioner, the *curator aquarum*, was responsible for the aqueducts. [^4] [^5]

Frontinus held the post from 97 AD and wrote a treatise on the system. [^4] [^5] He describes a staff of about 700 slaves, split between a public gang and an imperial gang, who repaired and cleaned the channels. [^4] [^5]

### What upkeep the channels needed

Hard water left layers of calcium carbonate, called sinter, inside the channels. [^6] [^7] The layers narrowed the channel and had to be chipped out. [^6] [^7] In parts of the Nîmes aqueduct the deposits reached about 40 centimetres thick. [^6] [^7]

## Disagreement / Uncertainty

The findings don't contradict each other. Several key figures are given as approximations: the Nîmes aqueduct's length of about 50 kilometres and its fall of about 12.6 metres [^1] [^2], the staff of about 700 slaves in Rome [^4] [^5], and sinter deposits of about 40 centimetres at Nîmes. [^6] [^7]

## Open Research Questions

- Who was responsible for keeping the aqueducts working in Roman Gaul? The findings on responsibility cover the city of Rome only.
- Beyond removing sinter, what other upkeep did the channels need, such as repairs to the structure or to the lead siphon pipes?
- Is there a source for the tally marks at Nîmes, said to have been cut into the channel wall after each cleaning?

## Reliability / Limitations

- `nimes-heritage.example`: Heritage service survey report, 2012.
- `roman-engineering-journal.example`: Peer-reviewed article, 2015.
- `lyon-archaeology.example`: City archaeology service page, 2016.
- `ancient-texts-library.example`: Translation of Frontinus's treatise, written about 97 AD. A primary source by the official who held the post of water commissioner.
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
PASS  judge-claims-carry-right-source   1. **Slope claim:** The note says "That is an average of about 25 centimetres per kilometre.[^1][^2]" and "falls only about 12.6 metres over about 50 kilometres ... [^1][^2]".    - [^1] is `https://www.nimes-heritage.example/aqueduct/survey-gradient`, which is allowed.    - [^2] is `https://www.roman-engineering-journal.example/2015/gradients-in-gaul`, which is allowed.  2. **Commissioner / Front
PASS  judge-footnotes-resolve   Every marker in the body has a definition with a URL, and every definition is used.  **Markers used in the body:** [^1] through [^7]. - "[^1][^2]": Nîmes gradient, Summary and "Keeping the water flowing downhill" - "[^3][^4]": arches and siphons - "[^4][^5]": curator aquarum and Frontinus - "[^6][^7]": sinter  **Definitions under Sources:** seven, each with a URL. - "[^1]: https://www.nimes-herit
PASS  judge-tally-only-as-question   The tally marks appear in only one place, under **## Open Research Questions**:  > "- Is there a source for the tally marks said to have been cut into the channel wall at Nîmes after each cleaning?"  This entry is phrased as a question. The words "said to have been" attribute the claim to someone else rather than state it as fact. The guild of channel keepers is not mentioned anywhere in the note
PASS  judge-urls-from-findings   The Sources section contains seven URLs, and each matches an entry on the allowed list character for character:  - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` - `[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul` - `[^3]: https://www.lyon-archaeology.example/aqueducts/siphons` - `[^4]: https://www.ancient-texts-library.example/frontinus/de-aquaeduc
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

File written: `project/Research/research-light-roman-aqueducts.md`

````
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
> Topics: (1) how the aqueducts were built; (2) how the aqueducts were kept running. Limits for every topic: the city of Rome and Roman Gaul only, up to the 3rd century AD.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Roman Aqueducts

## Summary

Roman aqueducts moved water by gravity on very gentle, carefully surveyed slopes. The aqueduct that supplied Nîmes falls only about 12.6 metres over about 50 kilometres, a slope that surveyors set with levelling instruments before building began.[^1][^2] Arches carried the channel across valleys so the slope could stay steady. Where a valley was too deep for arches, as at Lyon, builders used inverted siphons: sealed lead pipes that ran down one side of the valley and up the other.[^3][^4]

In Rome, the water commissioner (the curator aquarum) was responsible for the aqueducts. Frontinus, who held the post from 97 AD, describes a staff of about 700 slaves who repaired and cleaned the channels.[^4][^5] The main routine upkeep was removing sinter, layers of calcium carbonate left by hard water. Sinter narrowed the channels and had to be chipped out. In parts of the Nîmes aqueduct it reached about 40 centimetres thick.[^6][^7]

## How the aqueducts were built

### Keeping the water flowing downhill

The aqueduct that supplied Nîmes is about 50 kilometres long and falls only about 12.6 metres over that whole length. That is an average of about 25 centimetres per kilometre.[^1][^2]

Surveyors set this slope with levelling instruments over the whole route before building began.[^1][^2]

### Arches, and what replaced them in deep valleys

Arches carried the channel across valleys so that the slope could stay steady.[^3][^4]

Where a valley was too deep for arches, builders used inverted siphons. Lyon is one example.[^3][^4] An inverted siphon was a set of sealed lead pipes that ran down one side of the valley and up the other. The water was pushed up the far side by its own pressure.[^3][^4]

## How the aqueducts were kept running

### Who was responsible

In Rome, the aqueducts were the responsibility of the water commissioner, the curator aquarum.[^4][^5]

Frontinus held the post from 97 AD and wrote a treatise on the water system.[^4][^5] He describes a staff of about 700 slaves who repaired and cleaned the channels. The staff was split into two gangs, a public gang and an imperial gang.[^4][^5]

### What upkeep the channels needed

Hard water left layers of calcium carbonate, called sinter, inside the channels.[^6][^7] The layers narrowed the channel and had to be chipped out.[^6][^7] In parts of the Nîmes aqueduct, the deposits reached about 40 centimetres thick.[^6][^7]

## Disagreement / Uncertainty

## Open Research Questions

- Is there a source for the tally marks said to have been cut into the channel wall at Nîmes after each cleaning?
- Who was responsible for running and maintaining the aqueducts in Roman Gaul, such as at Nîmes and Lyon?

## Reliability / Limitations

- `nimes-heritage.example`: heritage service survey report, 2012.
- `roman-engineering-journal.example`: peer-reviewed article, 2015.
- `lyon-archaeology.example`: city archaeology service page, 2016.
- `ancient-texts-library.example`: translation of Frontinus's treatise, written about 97 AD. A primary source by the curator aquarum himself.
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
PASS  judge-claims-carry-right-source   1. **Slope claim:** "The aqueduct that supplied Nîmes falls only about 12.6 metres over its whole length of about 50 kilometres. That is an average fall of about 25 centimetres per kilometre. [^1] [^2]"    - [^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient (allowed)    - [^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul (allowed)    - The Summary repeats 
PASS  judge-footnotes-resolve   Markers used in the body: [^1] through [^7]. Each one appears at least once, for example "falls only about 25 centimetres per kilometre on average. [^1] [^2]", "builders used inverted siphons of sealed lead pipe. [^3] [^4]", "a staff of about 700 slaves who repaired and cleaned the channels. [^4] [^5]" and "reached about 40 centimetres thick. [^6] [^7]".  Definitions under Sources: there are seve
PASS  judge-tally-only-as-question   The tally marks and the guild appear in exactly one place.  **Open Research Questions:** > "Is there a source for a guild of channel keepers at Nîmes cutting tally marks into the channel wall after each cleaning?"  This is phrased as a question about whether a source exists, so it asserts nothing. It closely matches the allowed example, "Is there a source for the tally marks at Nîmes?"  They appe
PASS  judge-urls-from-findings   All seven URLs in the note's Sources section match the allowed list character for character:  - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` - `[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul` - `[^3]: https://www.lyon-archaeology.example/aqueducts/siphons` - `[^4]: https://www.ancient-texts-library.example/frontinus/de-aquaeductu` - `[^5]: https:
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

File written: `project/Research/research-light-roman-aqueducts.md`

````
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

Roman aqueducts kept water moving by gravity along a very shallow, steady slope that surveyors set with levelling instruments before building began. The aqueduct that supplied Nîmes falls only about 25 centimetres per kilometre on average. [^1] [^2] Arches carried the channel across valleys to keep that slope steady, and where a valley was too deep for arches, as at Lyon, builders used inverted siphons of sealed lead pipe. [^3] [^4]

In Rome, the water commissioner (the curator aquarum) was responsible for the aqueducts. Frontinus, who held the post from 97 AD, describes a staff of about 700 slaves who repaired and cleaned the channels. [^4] [^5] A main upkeep task was chipping out the calcium carbonate (sinter) that hard water left inside the channels, which in parts of the Nîmes aqueduct reached about 40 centimetres thick. [^6] [^7]

## How the aqueducts were built

### Keeping the water flowing downhill

The aqueduct that supplied Nîmes falls only about 12.6 metres over its whole length of about 50 kilometres. That is an average fall of about 25 centimetres per kilometre. [^1] [^2]

Surveyors set this slope with levelling instruments over the whole route before building began. [^1] [^2]

### Arches, and what replaced them in deep valleys

Arches carried the channel across valleys so that the slope could stay steady. [^3] [^4]

Where a valley was too deep for arches, as at Lyon, builders used inverted siphons. These were sealed lead pipes that ran down one side of the valley and up the other, with the water pushed up the far side by its own pressure. [^3] [^4]

## How the aqueducts were kept running

### Who was responsible

In Rome, the water commissioner, the curator aquarum, was responsible for the aqueducts. [^4] [^5]

Frontinus held the post from 97 AD and wrote a treatise on the system. [^4] [^5] He describes a staff of about 700 slaves, split between a public gang and an imperial gang, who repaired and cleaned the channels. [^4] [^5]

### What upkeep the channels needed

Hard water left layers of calcium carbonate, called sinter, inside the channels. [^6] [^7] The layers narrowed the channel and had to be chipped out. [^6] [^7]

In parts of the Nîmes aqueduct, the deposits reached about 40 centimetres thick. [^6] [^7]

## Disagreement / Uncertainty

The sources give the key figures as approximations rather than exact measurements: the Nîmes aqueduct's length (about 50 kilometres), its fall (about 12.6 metres), and its average gradient (about 25 centimetres per kilometre) [^1] [^2]; the size of the Rome water staff (about 700 slaves) [^4] [^5]; and the thickness of the sinter deposits at Nîmes (about 40 centimetres). [^6] [^7]

The account of the staff in Rome comes from Frontinus's own treatise, written by the man who held the post. [^4] [^5]

## Open Research Questions

- Is there a source for a guild of channel keepers at Nîmes cutting tally marks into the channel wall after each cleaning?
- Who was responsible for keeping the aqueducts in Roman Gaul, such as at Nîmes and Lyon, working?

## Reliability / Limitations

- `nimes-heritage.example`: heritage service survey report, 2012.
- `roman-engineering-journal.example`: peer-reviewed article, 2015.
- `lyon-archaeology.example`: city archaeology service page, 2016.
- `ancient-texts-library.example`: translation of Frontinus's treatise, written about 97 AD. A primary source written by the water commissioner himself.
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

Case folder: `research-writer-06-eight-topics`. Run folder: `writer`.

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
PASS  judge-footnotes-resolve   **Every marker has a definition.** Body markers run from `[^1]` to `[^92]`, and no marker uses a number above 92. Sources defines every number from `[^1]` through `[^92]` with no gaps. For example, the highest marker, "aboard the bark *Margaret Ellery*…[^92]", matches `[^92]: https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882`.  **Every definition holds a URL.** All 92 defin
PASS  judge-planted-details-cite-own-url   All eight details appear in the note, and each carries a footnote whose Sources URL matches the one given.  1. **Topic 1 (22-inch blocks):** "making a grid laid out so that blocks came out 22 inches square on the surface.[^9]". The Summary also has "scored the ice into blocks 22 inches square.[^7][^9]". [^9] is https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s. ✔ 2. **Topic 2 (
PASS  judge-reply-no-cut-short   The reply names no topic or file as cut short. Its only statement about truncation is an empty list: `"cut_short_topics": []`. That says no file was cut short, which the check counts as a pass. The other field, `"note": "Research/research-light-ice-trade.md"`, is just the output note path. It does not claim any findings file was incomplete or missing its closing line.
PASS  judge-sixteen-questions-answered   All sixteen questions are answered with the findings' content.  1. **When was pond ice ready, and how thick:** "usually from the middle of January into February, once a long hard freeze had set in"; "Ice was not cut until it was at least 14 inches thick"; "Each morning a foreman walked the pond with a hand auger and bored test holes." 2. **Tools and block size:** Wyeth "designed a horse-drawn cut
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

File written: `project/Research/research-light-ice-trade.md`

````
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
> Eight topics: cutting the ice on the ponds; storing the ice before shipping; loading the ship; the voyage; ice houses at the far ports; the workers; buyers and prices; and the end of the trade. Boundary: New England ice shipped by sea, from the trade's start to its end.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Ice Trade

## Summary

The New England ice trade began with a failed cargo from Boston to Martinique in 1806, sent by Frederic Tudor. Most of that ice melted on the wharf because there was nowhere to keep it.[^38] By the 1820s Tudor was shipping ice regularly to Havana and the southern United States, and he had learned to build an ice house before the first cargo arrived.[^38] The trade grew through the 1840s and 1850s, peaked around 1860, and was nearly over by the 1880s.[^30][^78]

Ice was cut in the coldest weeks, usually from mid-January into February, from spring-fed ponds such as Fresh Pond, Wenham Lake, and Spy Pond.[^1] It had to be at least 14 inches thick.[^1] Horse-drawn markers and ploughs, which grew out of Nathaniel Wyeth's designs of 1825 and 1829, scored the ice into blocks 22 inches square.[^7][^9] The ice was then stored in huge double-walled, sawdust-filled icehouses on the pond shores. The largest held about 9,400 tons.[^17] One house's ledger for 1847 shows about 17 percent of the ice lost between the March harvest and the last autumn sailing.[^23]

The ice went to sea in ordinary merchant ships that would otherwise have sailed out in ballast. This made carriage cheap.[^29][^30] The ships were fitted with a sawdust-packed lining, and the cargo was stowed tight at one ton of sawdust per 11 tons of ice.[^32][^34] The hatches were sealed for the whole voyage and the bilge pumped every 4 hours.[^37][^36] Voyages ran from two to three weeks to the Caribbean up to about 130 days to Calcutta.[^42][^41] A study of surviving papers puts the average loss on the Calcutta run at 38 percent.[^47] Well-stowed cargoes on the short routes often lost under a tenth.[^30]

At the far ports the ice went into purpose-built ice houses. The brick, domed Calcutta house held about 1,250 tons.[^50] Agents ran these houses and sold the ice by weight, in the early morning only, and in Havana by ticket.[^60][^58] Buyers ranged from British residents, clubs, and hospitals in Calcutta to the bars, food trades, and ordinary households of New Orleans.[^50][^44] Calcutta's price was 3 annas a pound in the 1830s and 1840s.[^60] By 1860 New Orleans paid about 2½ cents a pound.[^76]

No single cause ended the trade. The Civil War, ice-making machines, steamships, and the growing home market for natural ice all played a part.[^30][^78] The last recorded cargo to Calcutta sailed in 1882 on the bark *Margaret Ellery*.[^92] Sources disagree about when the last cargoes went anywhere by sea.[^28][^78]

## Cutting the ice on the ponds

**When the ice was ready.** The harvest ran in the coldest weeks of the year, usually from the middle of January into February, once a long hard freeze had set in.[^1] The shipping firms preferred spring-fed ponds with no streams running in. Moving water froze unevenly and carried silt, leaves, and sawdust from upstream mills into the ice.[^1][^2] Fresh Pond in Cambridge, Wenham Lake north of Salem, and Spy Pond in Arlington were the best known. The firms bought or leased the shore rights so that no rival could cut there.[^1][^2] Clear ice from a deep, still pond was the product the trade was built on. Buyers in hot ports judged ice by its clearness and took cloudy ice as a sign of dirty water, even when it was not.[^1] Foremen kept daily notebooks through the season, recording the dawn and noon air temperature, the wind, and any snowfall.[^1]

Ice was not cut until it was at least 14 inches thick. Thinner ice crumbled at the corners when handled, wasted space in the hold, and melted faster, because a thin block has more surface for its weight.[^1][^3] Each morning a foreman walked the pond with a hand auger and bored test holes at set points. He measured the depth of clear ice and, separately, any white snow ice on top. Only the clear ice counted.[^1][^3] If the readings fell short, the crew cleared snow or stood idle.[^1][^3] A pond could reach cutting thickness in one corner days before another, so cutting often began near the shaded shore and moved outward.[^1][^3]

Before the harvest, foremen also tested the ice for clearness. A small block was cut, carried ashore, and held up against the light. If a dark object showed clearly through its whole thickness, the ice was good enough for shipping. If the block was cloudy, cutting moved elsewhere on the pond, often further from the inlet or shore. The test was repeated every few days.[^6][^3]

**Snow and weather.** Snow slowed the freezing of the clear ice underneath. Wet snow that froze on top became "snow ice," which was white, airy, and weak.[^4][^5] Crews cleared snow with horse-drawn scrapers, which were wide wooden boards dragged across the surface.[^4][^5] On some ponds, crews bored holes and let water flood the cleared surface so that the ice thickened faster. This only worked in hard cold, since a slowly frozen layer turned cloudy.[^4][^5] A thaw or rain mid-season could flood and refreeze the grooves unevenly, and the field then had to be planed and cut again.[^13][^14] A mild "open winter" left the ponds too thin to cut at all. Shippers then bought ice from ponds further north, in Maine and New Hampshire, at a higher cost.[^13][^14] In a good season a large pond could be cleared in two to three weeks. Newspapers described crews cutting on Sundays, against local custom, when a thaw was forecast.[^13][^14]

**Tools and block size.** Before the 1820s ice was cut by hand with axes, hand saws, and chisels. This was slow, and it gave uneven blocks that stacked badly and let warm air into the gaps.[^7][^8] Nathaniel Jarvis Wyeth, a Cambridge hotel manager who later worked for the Tudor ice company, designed a horse-drawn cutter in 1825 and patented an improved version in 1829.[^7][^8] His tools made blocks of one regular size that stacked tightly in icehouses and holds. Historians describe this shift as the change that made long voyages possible. By the 1840s most commercial ponds in Massachusetts used some version of the tools.[^7][^8]

The first horse tool was the "marker," a plough-like frame with a row of steel teeth, drawn by one horse along a line laid out with a cord. A guide arm kept each groove parallel to the last. The field was scored in one direction, then crosswise, making a grid laid out so that blocks came out 22 inches square on the surface.[^9] The "plough" had longer teeth and was run along the same grooves until each cut went about two-thirds through the ice. The remaining third held the field together so that men and horses could still walk on it.[^9] The horse walked on uncut ice beside the line being cut, never on the grooves.[^6][^5]

Crews then sawed out a channel to the shore with long hand saws. Men with iron "breaking bars," which were flat chisels on long handles, split the field along the grooves into rafts and then into single blocks.[^10][^6] Men with pike poles pushed the floating blocks along the channel to shore.[^10][^6] At the shore an inclined elevator lifted the blocks into the icehouse. This was a wooden ramp with an endless cleated chain, driven at first by a horse at a capstan and, from the 1850s, by small steam engines in the largest houses.[^1][^11] Before going up, each block was planed flat on top and bottom to remove snow ice.[^1][^11]

A first-quality block of the regular size weighed roughly 200 pounds. That was the firm's working figure, which the tally men used to turn block counts into tons.[^15] By the 1850s complete tool sets were made and sold by specialist firms, many in the Hudson valley of New York. A set for a large pond included markers, ploughs, hand saws up to six feet long, breaking bars, pike poles, ice tongs, and snow scrapers.[^16][^7] The tools changed little over the life of the shipping trade.[^16][^7]

**Grading.** The clearest blocks, with no bubbles, snow ice, or dirt, were marked first quality and set aside for shipping. Blocks with a cloudy band or trapped leaves were second quality and usually sold locally.[^3][^12] One firm's papers show foremen told to reject any block they would not want to see on a dinner table.[^3][^12]

## Storing the ice before shipping

**How the pond icehouses were built.** The harvest came in over a few weeks, but ships sailed all year, so the ice was stored for months.[^17][^18] The firms built their icehouses above ground on the pond shore, so that blocks went straight from the channel up the elevator. This replaced the older farm practice of hillside pits, which held only a few tons and let groundwater in.[^17][^18]

The walls were the key to the design. A house had an outer and an inner wooden wall a little apart, with the space packed with sawdust from timber mills or with spent tanbark from tanneries. Some houses had three walls with two layers of fill.[^19][^7] Tudor and Wyeth tested fills in the 1820s and 1830s by building small trial houses and weighing the ice in them at the start and end of summer. They found that dry fill kept ice far better than damp fill, so the houses were built with wide eaves to keep rain off the outer walls.[^19][^7]

The roof was steep, with louvred vents along the ridge to let warm air escape. Most houses were painted white or a light colour, and some had hay or straw in the roof space.[^21][^18] The floors sat over a bed of gravel or broken stone with a drain to the pond, covered with thick sawdust, because ice standing in water melted much faster than ice standing in air.[^19] Inside, blocks were stacked on edge, tight together, each layer laid across the one below like brickwork. Gaps were filled with ice chips, and a full room was topped with a deep layer of hay or sawdust.[^17][^6]

**How much they held.** The biggest icehouse on Fresh Pond held about 9,400 tons when full and was taller than a three-storey building.[^17] It was built as a row of rooms under one long roof, each filled and emptied on its own, so that opening one room did not let warm air into the rest.[^17][^20] A row of doors was stacked one above another on the elevator side. Each door was boarded shut as the stack rose past it.[^17][^20] Smaller firms built houses holding a few hundred tons.[^17][^20] The firms also kept smaller wharf icehouses at Charlestown, built on the same plan and holding a few hundred tons each. Ice was brought there a few days before a sailing and not kept long, because the harbour air was warmer and damper.[^25]

**Keepers and handling.** Each large house had a keeper who lived beside it all year. He checked the drains and vents, kept the doors shut, watched for fire, and kept the ledger of ice in and out.[^22] Ice was taken out from the top down, one room at a time, with the doors shut again the same day. The oldest ice went first, and the best-packed rooms were kept for the hottest months.[^3][^12] From the early 1840s a railway branch ran from Fresh Pond to the Charlestown wharves, cutting the trip to under an hour. Its wagons were packed with sawdust, and in summer the trains ran at night.[^24][^17]

**How much was lost.** The ledgers of one Fresh Pond icehouse for 1847 show about 17 percent of the ice lost between the end of the harvest in March and the last autumn sailing. Most of the loss came in July and August.[^23] The keeper blamed the heat and a roof vent left shut. He also recorded that a room left unopened until autumn lost less than one opened in June.[^23] This is the only surviving record of a whole season's loss for a single house, and historians use it as the standard figure.[^23] Large houses lost less than small ones because a big stack has less surface for its weight. This is the main reason the firms built ever-larger houses through the 1840s and 1850s.[^28][^18] A house with a blocked drain could lose a large part of its bottom layers in a single warm month.[^19] Other figures and the problem of comparing them are under Disagreement / Uncertainty.

## Loading the ship

**The ships.** Ice went to sea in ordinary merchant ships. Boston imported much from the tropics but had little to send out, so many ships would otherwise have left in ballast. Ice gave them a paying outward cargo, and owners charged low rates to carry it.[^29][^30] Older ships were often chosen, because the ice firms' carpenters built linings into the hold.[^29][^30] Holds were emptied, swept, and dried first. Ships whose holds smelled of fish, hides, or molasses were scrubbed and aired, and ships that had carried coal were avoided.[^31]

**Packing the hold.** A carpenter built a lining, called the "ice ceiling," inside the hold. This was an inner wall of pine planks set in from the hull on all sides, with sawdust packed between. It ran across the floor and up under the deck beams, making a box like the icehouses ashore.[^32][^29] It took a carpenter and two helpers about a week for a ship of middling size.[^32][^29] Rough timber dunnage went on the bottom of the hull, then the lining floor, then a deep bed of sawdust. Gaps at the sides let melt run into the bilge.[^32]

Stevedores stowed the blocks on edge, tight together, each layer across the one below. They lowered the blocks through the hatch in slings, set them by hand, and pushed ice chips and sawdust into every gap.[^35][^29] A Salem merchant's printed paper of 1850 gives the ratio as one ton of sawdust for every 11 tons of ice.[^34] Less sawdust saved weight but cost more ice, and more took space that could have carried ice.[^34] The sawdust had to be dry, because wet sawdust froze into a crust that conducted heat into the ice. Pine sawdust came from Maine mills by schooner and was dried on the wharf if it arrived damp.[^33][^29]

Ice was stowed low and spread evenly from bow to stern. Ships usually carried less ice than their rated tonnage because of the weight of the lining and sawdust and the space they took up.[^32][^36] Loading was fast, often through the night or early morning. A ship of middling size could be loaded in one to two days and sailed on the next tide if the wind allowed.[^35][^37]

**Keeping the cargo from melting or shifting.** When the stack reached the top of the lining, it was covered with sawdust and then hay. The hatches were closed, covered with tarred canvas, and battened down. Some ships fitted a second inner hatch cover with sawdust between the two.[^32][^36] Once sealed, the hatches stayed sealed until port. Some masters sealed the joins with wax or pitch, and the firms' instructions held a master answerable for ice lost by opening them without good cause.[^37]

To stop shifting, stevedores drove timber battens between the stack and the lining and wedged the top layers against the deck beams.[^36] Logbooks record a few voyages where heavy weather loosened the stack, and in each case the ship arrived with a much smaller cargo.[^36] The crew pumped the bilge every 4 hours, day and night, and the mate logged the number of strokes. The stroke count was a rough measure of melting, and a sudden rise meant the stow had shifted or the lining had broken.[^36] Marine insurers excluded loss from melting, so the shipper bore that risk. This was one reason the firms worked so hard on the stow, the lining, and fast loading.[^39][^30]

## The voyage

**Routes and times.** Tudor's first cargo went to Martinique in 1806 and failed.[^38][^28] The Caribbean routes, to Havana, Martinique, Jamaica, and other islands, took two to three weeks with fair winds. Havana became one of the steadiest markets, with ships every few weeks.[^42][^43] The southern U.S. ports were the largest market by volume: Charleston, Savannah, Mobile, and above all New Orleans. By the 1850s New Orleans took more New England ice than any other port in the world. That voyage took several weeks, around Florida and across the Gulf.[^44][^30] Ice also went to Rio de Janeiro and other Brazilian ports, to Valparaíso, to Bombay, Madras, Hong Kong, and other Chinese ports, and in a few cargoes to Australia. Some of these routes were dropped after a few years as unprofitable.[^30][^45]

The longest regular route was Boston to Calcutta. Ships went south through the Atlantic, round the Cape of Good Hope, and across the Indian Ocean to the Hooghly River, crossing the equator twice. The voyage took about 130 days.[^41][^36] The first cargo sailed in May 1833 on the ship *Tuscany* and arrived that September to a sensation in the city.[^46][^41] Sailings were timed to arrive in the hot season, from about March to June, so ships left Boston in autumn and early winter. That also kept the first weeks of the voyage in cold northern waters.[^41][^30] From the 1840s many ships were towed up the Hooghly by steam tugs, which cut a passage of days to a day or less.[^49][^31] The firms paid more for fast ships on the Indian run, since fewer days in the tropics meant less melting.[^41]

**How much melted.** Most melting happened in the tropics. Pump strokes stayed low in the first weeks out of Boston, rose sharply near the equator, and stayed high. On the Calcutta route the second crossing of the tropics, near the end of the voyage, was the worst.[^36] A study comparing ice signed for in Boston with ice unloaded in Calcutta, for every voyage where both papers survive, found an average loss of 38 percent, varying widely by season, voyage length, and stow.[^47] On the Caribbean and southern routes a well-stowed cargo often lost under a tenth of its ice.[^30][^15] Being becalmed in the doldrums cost ice with no distance gained, and masters were told to keep moving at all costs.[^36][^37] Stops on the way meant opening the hatches, so masters were told to sell quickly and reseal within the hour.[^37][^45] Masters kept a separate printed "ice book" recording position, air and sea temperature, and pump strokes. These books are the main source for the Calcutta loss study.[^36][^37]

## Ice houses at the far ports

**Building them.** Martinique taught the first rule: build the ice house before the ice arrives. From the 1810s the firms built or rented an ice house in each port before sending regular cargoes. Some were converted warehouses with extra walls inside, others new buildings to the firm's plan, and carpenters were sent from Boston with the first cargo.[^38][^28]

The Calcutta ice house was paid for by a subscription among the city's merchants after the 1833 cargo and opened a few years later. It was a round brick building near the river, with thick walls and a domed roof, and when full it held about 1,250 tons. The round shape gave the least wall surface for the space inside.[^50][^51] It followed the Boston plan of inner and outer walls with packed fill between, but in brick, because wood suffered from termites and monsoon damp. Its floor drained to the river, and the roof was raised over a ventilated space.[^50][^52] Bombay and Madras got ice houses in the late 1830s and early 1840s on the Calcutta model, both smaller. At Madras, ice came through the surf in small boats.[^52][^56]

In Havana and some other ports the houses were partly sunk below street level, where the earth stayed cooler. That only worked on dry ground, and in New Orleans the houses stood fully above ground.[^53][^52] New Orleans had several competing ice houses on the levee by the 1840s, next to the unloading wharves.[^44][^55] Charleston and Savannah had smaller wooden houses on the Boston plan, raised on brick piers. They held a few weeks' supply and were often owned by local merchants who bought whole cargoes from the Boston firms.[^57][^44] Hong Kong's first ice house, built in the 1840s, was of local granite on the waterfront.[^59] Ice kept far less well in the tropical houses than at home, so agents tried to sell each cargo before the next arrived.[^31]

**Who ran them.** The Calcutta house was run by an agent sent from Boston, with local workers who unloaded, stacked, and served. The agent also dealt with the merchants' committee that had paid for the building.[^31][^50] The Havana house was built by the Tudor firm in the 1820s under a monopoly granted by the Spanish colonial government, which could fine the firm for running out of ice.[^54][^31] Through the 1840s it was run by the firm's agent, a local merchant named Joaquín Barcia.[^58] Agents were usually paid a share of sales. Some were local merchants and others were young men sent out from Boston to learn the business.[^31]

**How ice was sold.** Houses opened only from first light to mid-morning. Customers or their servants queued with baskets, and in Calcutta the hours were printed in the newspapers.[^50][^60] Ice was sold by weight on a scale at the door. Some houses kept blocks ready cut to standard weights.[^44][^60] In Havana, Barcia sold by ticket: the customer paid at the firm's office in the city and collected the ice at the house door, so no money changed hands there.[^58] Large buyers such as hotels, clubs, hospitals, and military messes had monthly accounts and were often served before the queue.[^60][^31] In New Orleans by the 1850s, carts delivered ice in insulated boxes each morning, though delivery was rare in Havana and Calcutta.[^44] In ports where ice was new, agents first gave it away. They showed bar owners how to cool drinks and cooks how to make ice cream, and they persuaded doctors to use ice for fevers.[^38][^62]

## The workers

**Who did the work.** In the early years most of the men on the ice were local farmers and their sons, working in the farming slack season and paid for their horses as well as themselves.[^63][^1] From the 1840s a growing share were Irish immigrants. The firms hired them for the unskilled jobs, while the skilled jobs often stayed with local men.[^64][^65] In later decades French-Canadian labourers came to the Massachusetts ponds, and by the 1870s some crews on the larger ponds were mostly French-Canadian.[^66] When local labour was short, the firms hired men in Boston and paid their train fares out.[^64] Boys from about twelve guided blocks, swept chips, and carried messages, for less pay than men.[^6][^63] Women did not work on the ice, but they ran boarding houses, cooked, and dried the crews' clothes.[^63][^15]

The loading was done by a different workforce: year-round stevedores on the Boston and Charlestown wharves, who worked in gangs under a boss contracted for each ship and were paid by the ton.[^35] At the far ports, local workers handled the ice. In Calcutta these were porters hired by the agent. In Havana, colonial records show the depot hiring enslaved men from their owners to unload the ships.[^70][^31]

**How crews were organised.** A crew on the largest ponds numbered about 75 men, divided into gangs: snow scrapers, marker and plough, bar men, channel men, elevator, and stackers. The slowest gang set the pace, and a smaller pond might use a third as many men.[^67] Each crew had a foreman who answered to the firm's superintendent for the pond. The foreman chose when and where to cut and whom to hire.[^3] Skilled men, such as marker drivers, stackers, and bar men, were hired for the whole season at higher pay.[^3][^63] Labourers were hired by the day at the pond's edge, with no promise of work the next day, according to oral histories from the last commercial harvests.[^6] Pay came weekly, on Saturday evening at the shore shanty, with board deducted.[^15]

**Conditions and dangers.** The cold was the hardship every account mentions. Frostbite was common. Men wore layers of wool, felt boots with leather overshoes, and spiked iron "creepers," and wet clothing was the great danger.[^6][^69] Shanties on the larger ponds kept coffee and soup hot all day, and the men had a hot midday meal.[^6] Days ran from first light to dark, sometimes into the night by lantern and on Sundays, with no extra pay unless the foreman agreed.[^13] Men slipped, cut themselves on saws and bars, and were crushed by blocks slipping on the elevator or by shifting stacks. Injured men got nothing beyond the days already worked.[^69][^6] The worst danger was falling through. A count of local newspaper reports found nine drownings among harvest crews on the Cambridge ponds between 1850 and 1860, mostly men who fell into the open channel at night.[^69][^13] Breaking through was also the commonest accident for the horses.[^6][^5]

Newspapers report fights between local men and Irish labourers in lean years.[^65][^68] They also report one- or two-day strikes in the 1850s and 1860s, timed for when a thaw was forecast. The firms answered by blacklisting strikers and hiring outside men.[^71][^64] An open winter meant no winter wage, and Boston charities reported more families seeking help afterward.[^72]

## Buyers and prices

**Who bought.** In Calcutta the first buyers were British residents: East India Company officials, army officers, merchants, and their families. Wealthy Indian merchants and landowning families were regular customers by the 1840s. For most of the city, ice was far too costly.[^50][^61] Hospitals were among the most important buyers in every hot port.[^73][^60] Clubs and officers' messes bought daily.[^61] In Madras and Bombay the buyers were much the same, including Parsi merchant families.[^56][^75] In Havana the main buyers were cafés, confectioners, and wealthy households, and ice spread to a common pleasure in the cafés within a generation.[^54][^62] In Charleston and Savannah buyers were planters, merchants, hotels, and taverns.[^57] In Hong Kong they were the garrison, the trading houses, and ships in harbour.[^59]

New Orleans used ice on a scale no other port matched. Its bars, hotels, households, meat and fish markets, and the river steamboats all bought it, and by the 1850s ordinary households bought it regularly.[^44][^74] Butchers, fishmongers, and dairies across the southern ports were large, steady buyers.[^44][^40] Some steamboats sold ice at river towns along the way.[^74][^77]

**What it cost.** In the 1830s and 1840s ice in Calcutta sold at the door for 3 annas a pound, an anna being a sixteenth of a rupee. The price held steady for most of those two decades, and account customers sometimes paid less.[^60][^30] Hospitals there got a reduced rate for a contract to take ice daily through the hot season.[^73] Prices in Madras and Bombay were above Calcutta's for the same years.[^56][^75] In Havana the firm agreed to a maximum price as part of its monopoly, and the government revised that maximum several times.[^54] In New Orleans, prices fell steadily from the 1830s to the 1850s as competing firms arrived.[^44][^30] By 1860 ice there sold for about 2½ cents a pound, rising in hot months or when a ship was late.[^76] In every port, prices were lowest just after a ship arrived and highest when stock ran low. When a house ran dry, there was no ice at any price.[^60][^43] Small ports with no ice house bought straight from a ship's hold at whatever buyers would pay.[^37] Price wars between Boston firms gave contested ports spells of cheap ice.[^31][^30]

Ice itself cost almost nothing at the pond. A cost study found that ice lost in transit and storage was the largest single cost on the long routes, larger than carriage.[^30] Tudor, once in debtors' prison, became one of Boston's richest men by the 1840s and was known as the "Ice King." His profits came mostly from the southern and Caribbean markets.[^38][^28]

## The end of the trade

**What ended it.** The sea trade peaked around 1860, declined slowly and then quickly, and was nearly over by the 1880s. Historians name several causes that came together, in a different order of importance in each port: war, ice-making machines, steamships, and a growing home market for natural ice.[^30][^78]

The Civil War (1861–1865) cut off the southern trade. New Orleans was closed to Boston ships until Union forces took it in 1862.[^79][^44] Some Carré ammonia machines were brought through the blockade to make ice for hospitals, showing southern businessmen that ice could be made on the spot.[^82] Early machines by Gorrie (patented 1851), Carré, and Harrison had not threatened the ships, being costly and small in output.[^80][^81] After the war, southern cargoes stayed well below their late-1850s levels.[^79][^30] New Orleans got its first ice factory in 1868, making about 12 tons a day at first, and more followed.[^83][^44] Through the 1870s the cost of factory ice fell below that of shipped ice once melt loss was counted. In the southern ports the shift happened within about twenty years of the first factories opening.[^30] Some firms tried undercutting the factories, which closed a few in the 1870s but could not work for long.[^44] Early factory ice was cloudy and distrusted, which slowed the switch in some ports by several years until factories learned to make clear ice by the 1880s.[^80][^84]

In India, factories opened in the 1870s and 1880s, with Calcutta's from the late 1870s, and the Calcutta ice house lost its trade within a few years.[^85][^50] Cargoes to Calcutta grew smaller and rarer through the 1870s, and Bombay and Madras ended first.[^90][^30] In Havana the colonial government stopped renewing the monopoly after the American war, and factories opened in the 1870s. Cuba's wars for independence from 1868 also disrupted trade.[^54][^89] Steamships took over the Asian routes, especially after the Suez Canal opened in 1869, which shrank the supply of cheap sailing ships for the outward voyage.[^41][^30] Meanwhile the home market for natural ice grew fast, and many firms turned to it.[^16][^78] Tudor died in 1864, and the old firms lost the people who had known how to run the sea trade.[^87][^28] The ponds near Boston were also built around and fouled, and Fresh Pond became Cambridge's water supply, so the harvest moved to cleaner ponds further north.[^86][^78]

**When the last cargoes sailed.** The last recorded cargo of New England ice to Calcutta sailed from Boston in 1882 aboard the bark *Margaret Ellery*, and no later ice ship appears in the Calcutta register. Her master noted that the cargo arrived in fair condition.[^92] For the trade as a whole, sources disagree; see Disagreement / Uncertainty. The end went unreported in the Boston papers.[^91]

## Disagreement / Uncertainty

- **Storage loss.** The 1847 Fresh Pond ledger shows about 17 percent lost over a season.[^23] A general history says a well-built house lost a fifth to a third over a summer, and small houses sometimes half, but it gives no source.[^28][^18] Keepers measured loss in two ways. Counting blocks hid the loss from blocks that shrank without breaking. Weighing samples, as in the 1847 ledger, showed more. Historians warn that figures from the two methods cannot be compared directly.[^26][^18]
- **Loss on the Calcutta voyage.** The logbook study gives an average of 38 percent. Its authors note that the voyages whose papers survive may have been the better-run ones.[^47] A general history says well-stowed ships lost about a quarter, and blames higher losses on poor stowing. It gives no method, and neither source says which years its figure covers.[^28]
- **Loss on the short routes.** The "under a tenth" figure is an estimate from a small number of voyages.[^30]
- **Loss in far-port ice houses.** Agents reported losses higher, month for month, than any recorded at the ponds, but only in general terms that cannot be compared with the pond ledgers.[^31]
- **When the trade ended.** Some histories put the end in the early 1880s.[^28][^78] A general history says Caribbean cargoes continued irregularly into the 1890s, and small shipments to the southern ports went on into the early twentieth century in years when local factories fell short. It gives no source for these later shipments. The difference may lie in whether a writer counts only the long voyages to Asia or any ice sent by sea.[^28][^78]
- **Ice voyages and return cargoes.** Some historians argue that the ice voyage made sense to shipowners mainly because it put a ship in Calcutta to collect a valuable return cargo of jute, linen, indigo, saltpetre, and spices.[^30][^29]
- **One-sided records.** The records of the far-port workers in Havana and Calcutta are employers' contracts and letters. No workers' account survives in these collections.[^70][^31] The newspaper reports of strikes take the firms' side.[^71]

## Useful Details

- The usual way to rescue a horse that broke through was to loop a rope around its neck and pull it tight. This made it hold its breath and float higher, so the men could drag it out. Some horses went through two or three times a season and kept working.[^6][^5]
- Some firms paid a bonus to the foreman whose pond reached cutting thickness first.[^1][^3]
- A tally man at the top of the elevator marked every block. Pond owners, who were usually paid by the ton, sometimes sent their own man to keep a second tally, and disputes over the count survive in letters.[^15]
- One firm dismissed a keeper who let a drain freeze over in early spring, flooding the lowest room.[^19]
- From the 1850s some keepers recorded thermometer readings above the stack morning and evening. A rising reading signalled an open door or clogged vent.[^22]
- Icehouses burned, often in summer, when a spark from a passing railway engine could catch the dry fill. The ice usually survived, standing in the ruins, and then melted within days.[^27][^18]
- The planks of the "ice ceiling" were often sold in the far port, since timber was scarce in some tropical ports.[^32][^29]
- An agent wrote that a cargo tasting of fish was sold off at a loss to a butcher.[^31]
- Apples, butter, and cheese were stowed in pockets cut into the ice stack, usually as the master's or agent's private trade. Agents' letters mention apples arriving in Calcutta and Havana in better state than after a month in a Boston cellar.[^31][^40]
- Early sailors feared melting ice would sink the ship. Tudor wrote that he struggled to find crews.[^38][^28] Insurance records show ice ships lost at about the same rate as other cargoes on the same routes.[^39]
- Some masters said ships rolled more in the last weeks at sea as the ice melted and the ship rose.[^32][^36]
- News of a Calcutta voyage could take most of a year to reach Boston. Some letters later came by the faster overland route through Egypt.[^31][^48]
- In Havana, ice was unloaded into lighters at night by lantern and carried to the house by hand and cart.[^43]
- Calcutta servants carried ice home on their heads at a run, wrapped in blankets or flannel. At home it lasted about a day, and wealthier households had ice chests shipped from Boston.[^61][^50]
- Some 1830s Indian households doubted whether ice handled by foreign sailors and porters was clean. By the 1840s Indian buyers were a large share of private customers.[^60]
- The Madras ice house survives, altered, on the seafront and is now a museum. The Calcutta house was pulled down in the late nineteenth century, and the Havana house has not been traced.[^56][^50]
- The Tudor firm's papers survive in a business archive and are the largest single source on how the trade worked.[^87][^56]
- After the sea trade ended, the Boston ice stevedores went back to general cargo, and the skills of stowing ice for a long voyage were not needed again.[^88]

## Open Research Questions

- What were the actual maximum prices set for ice in Havana, and what did it cost in Madras, Bombay, and Hong Kong in figures?
- When did the last cargoes of New England ice sail to the Caribbean and the southern U.S. ports?
- Are there storage-loss figures for any pond icehouse besides the 1847 Fresh Pond ledger, or loss figures in numbers for the far-port ice houses?
- How much did the harvest labourers, skilled men, and stevedores earn per day or per ton?

## Reliability / Limitations

- `new-england-industry.example/ice/pond-rights`: cites no archive for the pond-rights figures.
- `farm-journal-archive.example/1856/february/ice-for-market`: gives advice to farmers, not an account of a single harvest. With the oral histories, it is the only source for the horse-rescue rope method, with no count of how often it worked.
- `farm-journal-archive.example/1859/june/building-an-ice-house`: writes for farmers, not for the shipping firms.
- `walden-region-history.example/oral-histories/ice-crews`: recorded from people who worked the last commercial harvests, long after the shipping trade ended; may not describe the early trade.
- `harvard-business-archive.example/tudor-papers/pond-accounts`: the weight of a block is the firm's own working figure, not a measured average.
- `cambridge-historical.example/fresh-pond/icehouses`: the size of the largest house comes from a company prospectus.
- `boston-newspaper-archive.example/1868/august/icehouse-fire`: covers one fire; the industry history site gives no count of fires.
- `popular-history-press.example/books/the-frozen-water-trade-excerpt`: gives its storage-loss and Calcutta-loss figures without a source, and no source for shipments after the 1880s.
- `harvard-business-archive.example/tudor-papers/agents-letters`: the fish-tasting cargo story comes from one agent's letter; agents report far-port losses in general terms, not as comparable figures; the letters describe the firm's price tactics from its own side.
- `harvard-business-archive.example/tudor-papers/diary-excerpts`: records Tudor's own view of his difficulties.
- `sailing-ship-logs.example/collections/ice-voyages`: the comment on rolling comes from masters' remarks, not from any measurement.
- `ice-trade-voyages.example/logs/calcutta-melt-study`: the voyages whose papers survive may have been the better-run ones.
- `economic-history-review.example/2010/ice-shipping-costs`: the loss figure for the short routes is an estimate from a small number of voyages.
- `colonial-architecture-journal.example/2016/cold-storage-in-bengal`: compares ports and gives the Havana design as a contrast to Calcutta.
- `hongkong-heritage.example/waterfront/early-ice-house`: relies on newspaper notices and gives no building records.
- `memoirs-of-empire.example/collections/calcutta-domestic-life`: by British residents, describing their own households and experience only.
- `calcutta-gazette-archive.example/notices/ice-house-hours`: reports on Indian customers were written by British newspapers.
- `boston-newspaper-archive.example/1851/january/disturbance-on-the-ice`: the reports are short and give one side.
- `havana-archive.example/colonial-trade/dock-labour-contracts`: contracts and letters by employers; no account by the workers survives in these collections.
- `boston-newspaper-archive.example/1866/february/ice-strike`: takes the firms' side.
- `labor-history-ne.example/winter-work/ice-crews-conditions`: the drowning count comes from newspaper reports, which may have missed some deaths.
- `civil-war-commerce.example/blockade/carre-machines`: the number of machines brought through the blockade is not known.
- `gulf-commerce.example/ports/new-orleans-ice-imports`: gives no list of the factories that closed.
- `havana-archive.example/colonial-trade/ice-monopoly`: the colonial records end before the monopoly's last years; the later account comes from a university research project.

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
PASS  judge-footnotes-resolve   The body uses every marker from [^1] to [^92], and each one has a definition under Sources that holds a URL.  **Each marker has a definition with a URL.** There are 92 definitions, [^1] to [^92], and every one is a URL. The first is "[^1]: https://www.harvard-business-archive.example/tudor-papers/diary-excerpts" and the last is "[^92]: https://www.boston-newspaper-archive.example/1880s/ice-covera
PASS  judge-planted-details-cite-own-url   All eight details appear in the note, and each carries a footnote that resolves to the specified URL under Sources.  1. **Topic 1, 22-inch blocks:** "The marker was then run at a right angle across the first grooves, scoring a grid that gave blocks 22 inches square on the surface.[^28]"    - `[^28]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s` ✓ 2. **Topic 2, 17 percent l
PASS  judge-reply-no-cut-short   The reply names no topic as cut short. Its only claim about truncation is an empty list: `"cut_short_topics": []`. It gives no file or topic name and says nothing about any file being incomplete or missing its closing line.
PASS  judge-sixteen-questions-answered   All sixteen questions are answered with the findings' answers. None is answered only in general terms, and none is wrongly listed as open.  1. **When ice was ready to cut, and how thick:** "usually from the middle of January into February, once a long hard freeze had set in"; "Ice was not cut until it was at least 14 inches thick"; "a foreman walked the pond with a hand auger and bored test holes
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

File written: `project/Research/research-light-ice-trade.md`

````
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
> Eight topics: cutting the ice on the ponds; storing the ice before shipping; loading the ship; the voyage; ice houses at the far ports; the workers; buyers and prices; and the end of the trade. Limited to New England ice shipped by sea, from the trade's start to its end.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Ice Trade

## Summary

The New England ice trade by sea began with a loss. In 1806 Frederic Tudor sent a cargo from Boston to Martinique, where there was no ice house, and most of the ice melted on the wharf.[^1][^2] By the 1820s he was shipping ice regularly to Havana and to ports in the southern United States, having learned to build an ice house before the first cargo arrived.[^1]

The ice was harvested from spring-fed ponds such as Fresh Pond in Cambridge, usually from the middle of January into February, and was not cut until the clear ice was at least 14 inches thick.[^3] It was stored for months in large above-ground icehouses on the pond shores. These had double walls packed with sawdust, and the largest on Fresh Pond held about 9,400 tons.[^4] The one surviving whole-season ledger, for a Fresh Pond house in 1847, records a loss of about 17 percent between the end of the harvest and the last autumn sailing.[^5]

The ice went to sea in ordinary merchant ships. Many of them would otherwise have left Boston in ballast, so carrying ice was cheap.[^6][^7] The holds were lined with an inner wall of planks and sawdust, and one ton of sawdust was loaded for every 11 tons of ice.[^8] Voyages to the Caribbean took two to three weeks.[^9] New Orleans took more New England ice than any other port in the world by the 1850s.[^10] The longest regular route, Boston to Calcutta, took about 130 days.[^11] A study of the surviving papers for the Calcutta run found an average loss of 38 percent on the way.[^12] At the far ports the ice was kept in purpose-built ice houses, such as the brick Calcutta house that held about 1,250 tons.[^13] It was sold by weight[^17] and only in the early morning.[^13]

The harvest crews were at first local farmers and their sons.[^14] From the 1840s more and more of them were Irish immigrants,[^15] and in the later decades many were French-Canadian.[^16] In Calcutta ice sold for 3 annas a pound through the 1830s and 1840s.[^17] In New Orleans it was down to about 2½ cents a pound by 1860.[^18]

The trade peaked around 1860 and was nearly over by the 1880s. Historians name no single cause, but several changes coming together: war, ice-making machines, steamships, and the growing home market for natural ice.[^7][^19] The last recorded cargo to Calcutta sailed in 1882 aboard the bark *Margaret Ellery*.[^20] Sources disagree about when the last sea cargoes of any kind sailed (see Disagreement / Uncertainty).

## Cutting the ice on the ponds

**When and where.** The harvest ran in the coldest weeks of the year, usually from the middle of January into February, once a long hard freeze had set in.[^3] The shipping firms preferred spring-fed ponds with no streams running in. Moving water froze unevenly and carried silt, leaves, and sawdust from upstream mills into the ice.[^3] Fresh Pond in Cambridge, Wenham Lake north of Salem, and Spy Pond in Arlington were the best known. The firms bought or leased the shore rights so that no rival could cut there.[^3][^22] Foremen kept daily notebooks through the season, recording the air temperature at dawn and noon, the wind, and any snowfall.[^3]

**Thickness.** Ice was not cut until it was at least 14 inches thick.[^3][^21] Thinner ice crumbled at the corners when it was handled, wasted space in the hold, and melted faster, because a thin block has more surface for its weight.[^3] Each morning of the harvest a foreman walked the pond with a hand auger and bored test holes at set points. He measured the clear ice and, separately, any white snow ice on top. Only the clear ice counted toward the thickness.[^3][^21] One corner of a pond could reach cutting thickness days before another, so cutting often began near the shaded shore and moved outward.[^3]

**Snow and weather.** Snow on the pond acted like a blanket and slowed the freezing of the clear ice underneath. Wet snow that froze on top turned into "snow ice," which was white, full of air, and weak.[^23][^24] Crews cleared the snow with horse-drawn scrapers, wide wooden boards dragged across the surface.[^23][^24] On some ponds they bored holes and let water flood the cleared surface so that a fresh layer froze on top. This only worked in hard cold, because a layer that froze slowly would itself turn cloudy.[^23][^24] Snowfall in the middle of a harvest could stop work for several days.[^23] A thaw or rain could soften the ice and flood the grooves, and the field often had to be planed and cut again.[^32][^33] A mild "open winter" left the ponds too thin to cut at all, and the shippers then bought ice from ponds further north, in Maine and New Hampshire, at a higher cost.[^32][^33] In a good season a large pond could be cleared in two to three weeks, and newspaper reports describe crews cutting on Sundays when a thaw was forecast.[^32][^33]

**Clarity.** Clear ice from a deep, still pond was the product the trade was built on. Buyers in hot ports took cloudy ice as a sign of dirty water even when it was not.[^3][^22] Before the harvest a foreman cut a small block and held it up to the light. If a dark object showed clearly through its whole thickness, the ice was judged good enough for shipping. If not, cutting moved to another part of the pond. The test was repeated every few days.[^25][^21]

**Tools.** Before the 1820s ice was cut by hand with axes, hand saws, and chisels. The blocks came out uneven, which made them hard to stack and let warm air into the gaps.[^26][^27] Nathaniel Jarvis Wyeth, a Cambridge hotel manager who later worked for the Tudor ice company, designed a horse-drawn cutter in 1825 and patented an improved version in 1829.[^26][^27] His tools made blocks of one regular size that stacked tightly. Historians describe the shift to horse tools as the change that made long voyages possible, because regular blocks lost less ice to melting.[^26][^27] By the 1840s most commercial ponds in Massachusetts used some version of these tools.[^26][^27]

The first horse tool on the ice was the "marker," a frame with a row of steel teeth drawn by one horse along a line laid out with a cord. A guide arm kept each groove parallel to the last. The marker was then run at a right angle across the first grooves, scoring a grid that gave blocks 22 inches square on the surface.[^28] The "plough," with longer teeth, was run along the same grooves until each cut went about two-thirds of the way through the ice. The remaining third held the field together so that men and horses could still walk on it.[^28] The tools were designed so that the horse walked on uncut ice beside the line, never on the grooves.[^25][^24] The horses wore sharp-calked shoes, and a blacksmith was kept near the larger ponds to reset them.[^25][^24]

By the 1850s the tools were sold as complete sets by specialist makers, many of them in the Hudson valley of New York. A set for a large pond included one or two markers, several ploughs, hand saws up to six feet long, breaking bars, pike poles, ice tongs, and snow scrapers.[^35][^26] The tools changed little over the life of the trade. A set bought in the 1850s could still be in use thirty years later, with new teeth fitted by a local blacksmith.[^35][^26]

**Breaking out and lifting.** The crews sawed a channel to the shore with long hand saws. Men with iron "breaking bars," flat chisels on long handles, split the field along the grooves into long rafts, then into single blocks. Men with pike poles moved the floating blocks along the channel to the shore.[^29][^25] At the shore an inclined elevator carried the blocks up into the icehouse. This was a wooden ramp with an endless cleated chain, driven at first by a horse at a capstan and, from the 1850s, in the largest houses by small steam engines.[^3][^30] Before each block went up, a man planed its top and bottom flat, removing any snow ice.[^3][^30]

**Size, weight, and grading.** A first-quality block of the regular size weighed roughly 200 pounds, a figure the firm worked with rather than a measured average.[^34] A tally man at the top of the elevator marked each block, and the count was turned into tons. Pond owners, usually paid by the ton, sometimes kept their own tally.[^34] Blocks were graded by eye. The clearest went for shipping, while blocks with a cloudy band or trapped leaves were usually sold locally in Boston and nearby towns.[^21][^31] One firm told its foremen to reject any block they would not want to see on a dinner table.[^21][^31]

## Storing the ice before shipping

**Why and where.** The harvest came in over a few weeks, but the ships sailed all year, so the ice had to be stored for months.[^4][^36] The firms built their icehouses on the pond shore so the blocks could go straight up the elevator. The houses stood above ground, a change from the older farm practice of ice pits dug into a hillside, which held only a few tons and let groundwater seep in.[^4][^36]

**Construction.** An icehouse had two wooden walls, an outer and an inner, with the space between them packed with an insulating fill. The usual fill was sawdust from the timber mills, and spent tanbark from the tanneries was also used. Some houses had three walls with two layers of fill.[^37][^26] Frederic Tudor and Nathaniel Wyeth tested fills in the 1820s and 1830s by weighing the ice in small trial houses at the start and end of summer. They found that a dry fill kept ice far better than a damp one, so the houses were built with wide eaves to keep rain off the walls.[^37][^26] The roofs were steep, with louvred vents along the ridge to let warm air escape. Most houses were painted white or a light colour, and some builders added hay or straw in the roof space.[^39][^36] The floors were built over gravel or broken stone, with a drain to the pond and a thick layer of sawdust on top. Ice standing in water melted much faster than ice standing in air.[^37]

**Size.** The biggest icehouse on Fresh Pond held about 9,400 tons when full and was taller than a three-storey building. It was built as a row of rooms under one long roof, each filled and emptied on its own, so that opening one room did not let warm air into the rest.[^4][^38] Engravings show a long, windowless block with doors stacked one above another on the elevator side. The doors were opened as the ice rose and boarded shut once the stack passed them.[^4][^38] Smaller firms built houses that held a few hundred tons and sold most of their ice locally.[^4][^38]

**Stacking and keeping.** Blocks were stacked on edge, tight together, with each layer laid across the one below like brickwork. Ice chips filled the gaps, and full rooms were topped with a deep layer of hay or sawdust.[^4][^25] Each large house had a keeper who lived beside it all year. He checked the drains and vents, watched for fire, kept the ledger of ice in and out, and chose which room to open for each order.[^40]

**To the harbour.** From the early 1840s a railway branch ran from Fresh Pond to the wharves at Charlestown, cutting the trip to under an hour. Its wagons had thick wooden sides packed with sawdust, and in summer the trains ran at night.[^41][^4] The firms also kept smaller wharf icehouses of a few hundred tons each, built on the same plan. Ice was held there only for a few days before a sailing.[^42] When a ship was ready, ice was taken out from the top of the stack down, one room at a time, and scraped clean of fill before loading.[^21][^31]

**Loss in storage.** The ledgers of one Fresh Pond icehouse for 1847 record a loss of about 17 percent between the end of the harvest in March and the last autumn sailing. Most of it came in July and August.[^5] It is the only surviving record of a whole season's loss for a single house, and historians of the trade use it as the standard figure.[^5] The keeper noted that a room left unopened until autumn lost less than one opened for loading in June.[^5] Large houses lost less than small ones, because a big stack has less surface for its weight. This is the main reason the firms built ever-larger houses through the 1840s and 1850s.[^2][^36] For a higher estimate and a caution about how loss was measured, see Disagreement / Uncertainty.

## Loading the ship

**The ships.** The ice went to sea in ordinary merchant ships, not ships built for the trade.[^6][^7] Boston's merchants brought home large cargoes from the tropics but had little to send out, so many ships left in ballast. Ice gave them a paying outward cargo, and shipowners carried it at low rates.[^6][^7] Older ships were often chosen, because owners did not want their best ships altered by the linings.[^6][^7] Holds were emptied, swept, and dried, because any smell could pass into the ice. Ships that had carried coal were avoided, because the dust came out black on the ice.[^45]

**The lining.** A carpenter built an inner wall of pine planks a little way in from the hull on all sides, with sawdust packed between. The lining ran across the floor and up under the deck beams, making a box inside the hull on the plan of the icehouses ashore.[^46][^6] Sailors called it the "ice ceiling." Building it took a carpenter and two helpers about a week for a ship of middling size.[^46][^6] The floor went in first: rough timber (dunnage) to lift the cargo clear of the bilge, then the lining floor, then a deep bed of sawdust. Gaps at the sides let melt run down to the pumps.[^46] On most voyages that kept records, the bottom layer of ice was the largest single loss.[^46]

**Sawdust.** The firms brought pine sawdust from the timber mills of Maine by schooner.[^8] A Salem merchant's paper of 1850 gives the proportion as one ton of sawdust for every 11 tons of ice. Less sawdust cost more ice than it saved, and more took up space that could have carried ice.[^8] The sawdust had to be dry, because wet sawdust froze onto the blocks and conducted heat into them. Damp loads were spread on the wharf in the sun before use.[^47][^6]

**Stowing.** Stevedores lowered the blocks through the hatch in slings and stacked them as in the icehouses: on edge, tight together, with each layer laid across the one below and every gap filled with chips and sawdust.[^48][^6] The ice was stowed low and spread evenly from bow to stern. Ships usually carried less ice than their rated tonnage, because of the weight of the lining and sawdust and the space they took.[^46][^49] A ship of middling size could be loaded in one to two days. The work was done at night or early in the morning, and the ship sailed on the next tide if the wind allowed.[^48][^50]

**Against melting.** The top of the stack was covered with sawdust and then hay. The hatches were closed, covered with tarred canvas, and battened down, and some ships fitted a second, inner hatch cover with sawdust between the two.[^46][^49] Once sealed, the hatches stayed shut until port. The firms' instructions say a master who opened them at sea without good cause would answer for the lost ice.[^50] Melt water was pumped from the bilge every 4 hours, day and night. The mate logged the number of strokes, which was the only sign of how the cargo was faring.[^49][^50]

**Against shifting.** Stevedores drove timber battens between the stack and the lining and wedged the top layers against the deck beams. A tight stow with plenty of sawdust also held the blocks still.[^49] Logbooks record a few voyages where heavy weather loosened the stack, and each of those ships arrived with a much smaller cargo. In one log the master writes that he heard the ice "working" in the hold during a gale.[^49] A sudden rise in pumping strokes meant the stow had shifted or the lining had broken.[^49]

**Insurance.** Early marine insurers refused to cover ice at all. Later policies covered the ship and a share of the cargo but excluded loss from melting, so the shipper bore that risk.[^51][^7]

## The voyage

**Routes and times.** The longest regular route ran from Boston to Calcutta. Ships went south through the Atlantic, round the Cape of Good Hope, and across the Indian Ocean, crossing the equator twice, and the voyage took about 130 days.[^11][^49] The first ice cargo to Calcutta sailed in May 1833 on the ship *Tuscany* and arrived that September. It made a profit, and regular sailings followed.[^55][^11] The Caribbean routes to Havana, Martinique, Jamaica, and other islands took two to three weeks with fair winds, and Havana became one of the steadiest markets.[^9][^53] The southern US ports were the largest market by volume: Charleston, Savannah, Mobile, and above all New Orleans, a voyage of several weeks around Florida and across the Gulf.[^10][^7] Ice also went, less regularly, to Rio de Janeiro and other Brazilian ports, Valparaíso, Bombay, Madras, Hong Kong and other Chinese ports, and in a few cargoes to Australia. Some of these routes were dropped after a few years.[^7][^54]

**Timing.** Calcutta sailings were timed to arrive in the hot season, about March to June, so ships left Boston in the autumn and early winter. The first weeks were then spent in cold northern waters, where almost no ice was lost.[^11][^7] The Caribbean and southern ports were sent ice all year, with the most ships in the hot months.[^11][^7]

**Melting.** Most melting happened in the tropics. Pumping strokes were low in the first weeks out of Boston and rose sharply near the equator. On the Calcutta run the second tropical crossing, at the end of the voyage, was the worst.[^49] A study of logbooks and cargo receipts on the Calcutta run found an average loss of 38 percent between Boston and Calcutta, varying widely with season, length of voyage, and stow.[^12] The short routes lost much less: a well-stowed cargo to Havana or New Orleans often lost under a tenth.[^7][^34] Calms cost ice. A ship becalmed in the doldrums could drift for days or weeks, and masters were told to avoid known calm zones even by a longer route.[^49][^50] The firms paid more to charter fast ships for the Indian run.[^11] From the 1840s many ice ships were towed up the Hooghly River to Calcutta by steam tugs, which cut a passage of days to a day or less.[^57][^45]

**Records and news.** Masters kept a separate printed "ice book" with columns for date, position, air and sea temperature, and pumping strokes. Several survive and are the main source for the Calcutta loss study.[^49][^50] The Boston office learned how a Calcutta voyage had gone only when the agent's letter came home, which could take most of a year. The overland mail route through Egypt later shortened the wait.[^45][^56]

## Ice houses at the far ports

**The first rule.** The failure at Martinique taught the trade to build the ice house before the ice arrived. From the 1810s onward the firms built or rented an ice house in each port before sending regular cargoes. Some were converted warehouses with extra walls added inside, and some were new buildings to the firm's plan, overseen by carpenters sent from Boston.[^1][^2]

**Calcutta.** The Calcutta house was paid for by a subscription among the city's merchants after the first cargo of 1833 and opened a few years later. It was a round brick building near the river, with thick walls and a domed roof, and held about 1,250 tons when full.[^13][^58] It followed the Boston plan of an inner and outer wall with a packed space between, but in brick, because wood was attacked by termites and rotted in the monsoon. The floor drained to the river, and the roof was raised over a ventilated space.[^13][^59] It was run by an agent sent from Boston, with local staff who unloaded, stacked, and served. The agent also answered to the merchants' committee that had paid for the building.[^45][^13]

**Havana.** The Tudor firm built its Havana ice house near the harbour in the 1820s, after the Spanish colonial government granted it a monopoly on selling ice in the city. In return the firm promised to keep the city supplied, and it could be fined for running out.[^61][^45] In Havana and some other ports the ice houses were partly sunk below street level, where the earth was cooler.[^60][^59] Ships could not come alongside near the house, so ice was unloaded into lighters at night and carried ashore by hand and in carts.[^53] The house was run for the firm through the 1840s by a local merchant, Joaquín Barcia. He sold ice by ticket: a customer bought a ticket for a set weight at the firm's office and collected the ice at the house door, so no money changed hands there.[^65]

**New Orleans and the southern ports.** By the 1840s New Orleans had several large ice houses on the levee, owned by competing firms, beside the wharves where the ships unloaded. The ground was too low and wet to sink them.[^10][^62][^60] Charleston and Savannah had smaller wooden houses on the Boston plan, raised on brick piers. They were often owned by local merchants who bought whole cargoes from the Boston firms.[^64][^10]

**Bombay, Madras, Hong Kong.** Bombay and Madras got ice houses in the late 1830s and early 1840s on the Calcutta model, both smaller than Calcutta's. At Madras the ice came ashore through the surf in small boats.[^59][^63] Hong Kong's first ice house, built of island granite, dates from the 1840s, and its trade was small and irregular.[^66]

**How ice was sold.** The houses opened only from first light to mid-morning. Customers or their servants queued with baskets, and in Calcutta the hours were printed in the newspapers.[^13][^17] Ice was sold by weight on a scale at the door. Some houses kept blocks pre-cut to standard weights.[^10][^17] Hotels, clubs, hospitals, and military messes had monthly accounts and were often served before the queue.[^17][^45] In New Orleans by the 1850s, carts delivered ice each morning to standing orders. In Havana and Calcutta delivery was rare.[^10] In new ports the agents gave ice away at first and showed bar owners, cooks, and doctors how to use it, then began charging.[^1][^68] Agents were usually paid a share of sales rather than a wage.[^45] Ice kept far less well in the tropical houses than at home, so agents tried to sell each cargo before the next arrived.[^45]

## The workers

**Who.** The harvest fell in the slack season of the farming year. In the early years most of the men were local farmers and their sons, who brought their own horses and were paid for horse and man.[^14][^3] From the 1840s a growing share were Irish immigrants. They were hired in large numbers for the unskilled jobs, while the skilled jobs often stayed with local men.[^15][^69] In the later decades French-Canadian labourers came to the Massachusetts ponds, and by the 1870s some crews on the larger ponds were mostly French-Canadian.[^16] Boys from about twelve guided blocks in the channel, swept chips, and carried messages, for less pay than men.[^25][^14] Women did not work on the ice, but they ran boarding houses, cooked, and dried the crews' wet clothes. The firms' accounts record those payments under the name of the household.[^14][^34] In hard winters, agents hired men off the Boston streets and paid their train fares to the ponds.[^15]

**How the crews were organised.** On the largest ponds a crew numbered about 75 men, divided into gangs: snow scrapers, marker and plough, bar men, channel men, elevator, and stackers inside the house. The slowest gang set the pace, and a smaller pond might use a third as many men.[^70] Each crew had a foreman, answering to the firm's superintendent for the pond, who decided when and where to cut and whom to hire.[^21] Labourers were hired by the day at the pond's edge, with no promise of work the next day.[^25] Skilled men (marker drivers, stackers, bar men) were hired for the season, paid more, and asked back each year.[^21][^14] Pay came on Saturday evening at the shore shanty, with board deducted for those who boarded with the firm.[^34]

**Loading crews and far ports.** The stevedores who loaded the ships were a separate, year-round waterfront workforce. They worked in gangs under a boss who contracted with the firms, and were paid by the ton.[^48] At the far ports, porters hired by the agent carried the blocks in Calcutta. In Havana, colonial records show the firm's depot hiring enslaved men from their owners to unload the ships.[^73][^45]

**Conditions.** The working day ran from first light to dark. When a thaw was forecast, the elevators and stacking crews ran into the night by lantern light, sometimes on Sundays, with no extra pay unless the foreman agreed.[^32] Every account mentions the cold. Frostbite of fingers, ears, and feet was common. Men wore layers of wool, felt boots with leather overshoes, and iron "creepers" strapped to the boots.[^25][^72] On the larger ponds the firms kept a shore shanty with a stove, hot coffee and soup, and a midday meal.[^25] Fights between local men and Irish labourers are reported in newspapers, and foremen sometimes kept the groups in separate gangs.[^69][^71] Crews sometimes struck when a thaw was forecast. Strikes in the 1850s and 1860s lasted a day or two and ended when the firms agreed, after which the firms kept lists of strikers.[^74][^15] A mild winter meant no harvest and no winter wage for men around Boston.[^75]

**Dangers.** The worst danger was falling through. A man in the channel could be carried under the ice or trapped among the blocks. A count of newspaper reports for the Cambridge ponds recorded nine drownings among harvest crews between 1850 and 1860, most of them men who fell into the open channel at night.[^72][^32] The firms put up no railings or lights along the channel until late in the trade.[^72][^32] Men slipped, cut themselves on saws and bars, and were crushed by blocks slipping on the elevator or stacks shifting. A block falling from the top of the elevator could kill a man.[^72][^25] Injured men were paid nothing beyond the days already worked.[^72][^25]

## Buyers and prices

**Calcutta and India.** The first buyers in Calcutta were the British residents: East India Company officials, army officers, merchants, and their families.[^13][^67] Wealthy Indian merchant and landowning families also bought from the early years and were regular customers by the 1840s. For most of the city's population ice was far too costly.[^13][^67] Hospitals and officers' messes were among the largest account customers, and clubs served iced drinks through the hot season.[^17][^76][^67] In the 1830s and 1840s ice sold at the Calcutta ice house door for 3 annas a pound (an anna being a sixteenth of a rupee). The price held steady for most of those two decades, and account customers sometimes paid less by private agreement.[^17][^7] Hospitals got a reduced rate in return for a contract to take ice every day of the hot season.[^76] In Madras and Bombay ice cost more than in Calcutta, and the buyers were much the same, including wealthy Indian and Parsi merchant families.[^63][^78]

**Havana.** The main buyers were cafés, confectioners making ice creams and sorbets, and wealthy households. Within a generation ice spread from a luxury of the rich to a common pleasure in the cafés.[^61][^68] The price was capped: under the monopoly the firm agreed a maximum price, which the government revised several times, so it could not raise prices in the hottest weeks.[^61]

**New Orleans and the South.** New Orleans used ice on a scale no other port matched: bars, hotels, households, meat and fish markets, and the river steamboats, which also carried ice to towns upriver.[^10][^77][^79] Prices there fell steadily from the 1830s to the 1850s as competing firms and ice houses arrived, and the firms made their money on volume.[^10][^7] By 1860 ice sold for about 2½ cents a pound at the levee ice houses, rising in the hot months and when a ship was late.[^18] By the 1850s ordinary households in New Orleans and other southern cities bought ice regularly.[^77] In Charleston and Savannah the buyers were planters, merchants, hotels, and taverns.[^64]

**Hong Kong.** The buyers were the British garrison, the trading-house merchants, and ships in the harbour, and ice was on sale only after a ship had arrived.[^66]

**What set the price.** The ice cost almost nothing at the pond. A study of the trade's costs found that ice lost in transit and storage was the largest single cost on the long routes, larger than carriage.[^7] In every far port the price was lowest just after a ship arrived and highest when stocks ran low.[^17][^53] At small ports with no ice house, masters sold from the open hatch at whatever buyers would pay.[^50] The Boston firms fought price wars, sending extra cargoes to undersell a rival and then raising the price once the market was theirs.[^45][^7]

## The end of the trade

**What ended it.** The trade grew through the 1840s and 1850s and peaked around 1860. Historians name no single cause, but several changes coming together, in a different order from port to port.[^7][^19]

- *The Civil War.* The Union blockade (1861–1865) closed New Orleans to the Boston ships until Union forces took the city in 1862. The Confederacy went without shipped ice for most of the war.[^80][^10] Some Carré ice machines were brought through the blockade, showing southern businessmen that ice could be made on the spot.[^83] The southern trade returned after the war but not to its old size.[^80][^7]
- *Ice-making machines.* John Gorrie patented an ice machine in 1851, Ferdinand Carré developed an ammonia machine in the late 1850s, and James Harrison built machines in Australia in the 1850s. These early machines were costly and small.[^81][^82] New Orleans got its first commercial ice factory in 1868, making about 12 tons a day at first, and more followed.[^84][^10] Through the 1870s factory ice in the southern ports became cheaper than shipped ice once melt was counted. The shift there took about twenty years from the first factories.[^7] Early factory ice was cloudy and distrusted, which slowed the switch by several years in some ports, until the factories learned to make clear ice by the 1880s.[^81][^85] Some Boston firms tried to undersell the factories. This closed a few small ones in the 1870s but could not last.[^10] Factories opened in Calcutta in the late 1870s, and in Bombay and Madras after, and the Calcutta ice house lost its trade within a few years.[^86][^13] Havana's monopoly was not renewed after the American war, and factories opened there in the 1870s. Cuba's wars for independence from 1868 also disrupted trade.[^61][^90]
- *Steamships.* As steamers took over the routes to Asia, especially after the Suez Canal opened in 1869, the supply of cheap outward-bound sailing ships shrank. Ice on a steamer cost more to carry, and the coal took space.[^11][^7]
- *The home market (outside the sea trade asked about).* American cities in the North and Midwest used more and more natural ice, and the New England ponds could sell all they cut at home by rail. Many firms turned from the sea trade to this market.[^35][^19] This lies outside the request's limits, but it bears on why the sea trade ended.
- *Ponds and people.* The ponds near Boston were built around and fouled. Fresh Pond became Cambridge's water supply, and harvesting there was restricted and then stopped.[^87][^19] Frederic Tudor died in 1864, and his family ran the firm for some years with less success. Other firms merged into companies dealing mostly in the home market.[^88][^2]

**The last cargoes.** The Indian trade dwindled through the 1870s, some years seeing only one or two ships, and the Bombay and Madras trade ended before Calcutta's.[^91][^7] The last recorded cargo of New England ice to Calcutta sailed from Boston in 1882 aboard the bark *Margaret Ellery*. The Calcutta register lists no later ice ship, and the master's ice book says the cargo arrived in fair condition.[^20] The Boston papers that had celebrated the first ice ships printed no reports of the last ones.[^92] For the end of the sea trade as a whole, sources disagree (see below).

## Disagreement / Uncertainty

**Loss in storage (contested figures).** The 1847 Fresh Pond ledger, kept by weighing, shows about 17 percent lost over a season.[^5] A general history of the trade says a well-built house lost between a fifth and a third over a summer, and small houses sometimes half, but it gives no source.[^2] The two figures may not be comparable. Ledgers kept by counting blocks hide the loss from blocks that shrank but did not break, so they show smaller losses than ledgers kept by weighing. Historians warn that the two methods give figures that cannot be set side by side.[^43][^36]

**Loss on the Calcutta voyage (contested figures).** The logbook study found an average loss of 38 percent.[^12] Its authors note that the surviving papers may be from the better-run voyages.[^12] A general history says well-stowed ships lost about a quarter, and that higher losses came from poor stowing rather than voyage length, but it does not say how it reached that figure.[^2] The two may describe different periods, since stowing improved over the trade's life, but neither source says which years its figure covers.[^2]

**Loss on the short routes (estimate).** The "under a tenth" figure for Havana and New Orleans is an estimate from a small number of voyages.[^7]

**When the sea trade ended (contested).** Some histories say it ended in the early 1880s. A general history says cargoes to the Caribbean went on irregularly into the 1890s, and small shipments to the southern ports into the early twentieth century in years when local factories could not keep up. The later shipments are given without a source.[^2][^19] The difference may come from what each writer counts as the trade: the long voyages to Asia, or any ice sent by sea from New England.[^2][^19]

**Return cargoes (interpretation).** Some historians argue that the Calcutta ice voyage made sense to shipowners mainly because it put a ship in Calcutta to collect a valuable return cargo of jute, linen, indigo, saltpetre, and spices.[^7][^6]

**Other gaps.** The number of Carré machines brought through the blockade is not known.[^83] The drowning count for the Cambridge ponds comes from newspaper reports, which may have missed some deaths.[^72][^32] The agents in the far ports reported tropical storage losses only in general terms, not as figures comparable with the pond ledgers.[^45]

## Useful Details

- A horse that broke through the ice was the most common accident of the harvest. The usual rescue was to loop a rope around the horse's neck and pull it tight, which made it hold its breath and float higher so the men could drag it out. Accounts describe horses that went through two or three times in a season and kept working.[^25][^24]
- Some firms paid a small bonus to the foreman whose pond reached cutting thickness first.[^3][^21]
- A pond owner could earn more from one winter's ice rights than from a year of farming the land around it.[^3][^22]
- The elevator could run day and night when the weather held, with lanterns hung along the ramp.[^3][^30]
- A skilled bar man could tell from the sound of the strike whether a groove had gone deep enough.[^29][^25]
- From the 1850s some keepers hung thermometers above the stack and logged morning and evening readings beside the outside temperature. A rising reading meant a door left open or a clogged vent.[^40]
- One firm's papers record the dismissal of a keeper who let a drain freeze in early spring, which flooded the lowest room when the weather turned.[^37]
- Icehouses burned. The dry sawdust and hay caught easily, sometimes from a passing railway engine's spark. The ice inside usually survived, then melted in the open within days.[^44][^36]
- In the first years sailors feared ice cargoes would melt and sink the ship. Tudor's diary records trouble finding crews.[^1][^2] Insurance records later show ice ships lost in about the same numbers as other cargoes on the same routes.[^51]
- Agents in Calcutta and Havana received apples, butter, and cheese packed in pockets in the ice stack, usually as the private trade of the master or agent. The apples arrived in better state than after a month in a Boston cellar.[^45][^52]
- The hold lining's planks were often sold in the far port, since timber was scarce in some tropical ports.[^46][^6]
- An agent reported that a cargo tasting of fish was sold off at a loss to a butcher.[^45]
- Ships bound for Calcutta sometimes stopped at Cape Town or Mauritius and sold some ice. Masters were told to reseal the hatches within the hour.[^50][^54]
- Calcutta servants carried ice home in blanket-wrapped baskets on their heads at a run. Wealthier households had wooden ice chests shipped from Boston.[^67][^13]
- The Calcutta ice house was pulled down in the late nineteenth century. The Madras house survives, altered, as a museum on the seafront, and the Havana house has not been traced.[^63][^13]
- When the sea trade ended, the ice stevedores on the Boston wharves went back to general cargo. The far-port agents joined the new factories, went into other trades, or returned home.[^89]
- The Tudor firm's papers survive in a business archive and are the largest single source on how the trade worked.[^88]

## Open Research Questions

- What maximum price did the Havana colonial government set for ice, and how did it change?
- What did harvest labourers, skilled men, and stevedores earn per day or per ton?
- Which years do the 38 percent and "about a quarter" Calcutta loss figures each cover?
- When did the last sea cargo of New England ice to the Caribbean or the southern ports sail?

## Reliability / Limitations

- `new-england-industry.example (regional industry history site)`: cites no archive for the pond-rights figures. Gives no count of icehouse fires.
- `farm-journal-archive.example, February 1856 (digitized agricultural magazine)`: gives advice to farmers, not an account of a single harvest.
- `farm-journal-archive.example, June 1859 (digitized agricultural magazine)`: writes for farmers, not for the shipping firms.
- `walden-region-history.example (oral history collection, transcribed 1974)`: recorded from people who worked the last commercial harvests, long after the shipping trade ended, so it may not describe the early trade. The rope method for rescuing horses is described here and in one magazine piece, with no count of how often it worked.
- `harvard-business-archive.example, pond accounts (merchant's papers)`: the weight of a block is the firm's own working figure, not a measured average.
- `harvard-business-archive.example, diary excerpts (merchant's papers)`: records Tudor's own view of his difficulties.
- `harvard-business-archive.example, agents' letters (merchant's papers)`: the fish-tasting cargo story comes from one agent's letter. The letters describe the firm's price-war tactics from its own side, and they report far-port losses in general terms, not as comparable figures.
- `cambridge-historical.example, icehouses (local historical society article)`: the size of the largest Fresh Pond house comes from a company prospectus the article cites.
- `boston-newspaper-archive.example, August 1868 (digitized newspaper)`: covers one fire.
- `popular-history-press.example (book excerpt on a publisher's site)`: gives its storage-loss and Calcutta-loss figures without a source, and gives no source for the later shipments.
- `sailing-ship-logs.example (digitized logbook collection)`: masters' remark that ships rolled more as the ice melted comes from logbook comments, not measurement.
- `economic-history-review.example (peer-reviewed article)`: its loss figure for the short routes is an estimate from a small number of voyages.
- `ice-trade-voyages.example, Calcutta melt study (university research project report)`: the voyages whose papers survive may have been the better-run ones.
- `colonial-architecture-journal.example (peer-reviewed article)`: compares ports and gives the Havana design as a contrast to Calcutta.
- `hongkong-heritage.example (heritage society page)`: relies on newspaper notices and gives no building records.
- `memoirs-of-empire.example (digitized memoir collection)`: by British residents, describing their own households.
- `boston-newspaper-archive.example, January 1851 (digitized newspaper)`: the reports are short and give one side.
- `havana-archive.example, dock labour contracts (digitized colonial records)`: the records are contracts and letters by employers. No account by the workers survives in these collections.
- `boston-newspaper-archive.example, February 1866 (digitized newspaper)`: takes the firms' side.
- `labor-history-ne.example, conditions (regional labour history project page)`: the drowning count comes from newspaper reports, which may have missed some deaths.
- `calcutta-gazette-archive.example (digitized newspaper notices)`: the reports on Indian buyers' doubts were written by British newspapers about Indian customers.
- `civil-war-commerce.example, Carré machines (university history project page)`: says the number of machines brought through the blockade is not known.
- `gulf-commerce.example, New Orleans ice imports (business history society page)`: gives no list of the factories that closed.
- `havana-archive.example, ice monopoly (digitized colonial government records)`: the records end before the monopoly's last years. The later account comes from the cuba-commerce-history research project.

## Sources

[^1]: https://www.harvard-business-archive.example/tudor-papers/diary-excerpts
[^2]: https://www.popular-history-press.example/books/the-frozen-water-trade-excerpt
[^3]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview
[^4]: https://www.cambridge-historical.example/fresh-pond/icehouses
[^5]: https://www.ma-archives.example/ice-ledgers/wyeth-1847-shrinkage
[^6]: https://www.maritime-boston.example/trade/outward-cargoes
[^7]: https://www.economic-history-review.example/2010/ice-shipping-costs
[^8]: https://www.maritime-salem.example/papers/stowing-ice-1850
[^9]: https://www.maritime-boston.example/routes/caribbean
[^10]: https://www.gulf-commerce.example/ports/new-orleans-ice-imports
[^11]: https://www.maritime-boston.example/routes/boston-calcutta
[^12]: https://www.ice-trade-voyages.example/logs/calcutta-melt-study
[^13]: https://www.calcutta-history-society.example/buildings/the-ice-house
[^14]: https://www.labor-history-ne.example/winter-work/farm-families
[^15]: https://www.labor-history-ne.example/winter-work/irish-labour
[^16]: https://www.immigration-history-journal.example/2015/french-canadians-in-new-england
[^17]: https://www.calcutta-gazette-archive.example/notices/ice-house-hours
[^18]: https://www.gulf-commerce.example/price-current/ice-1860
[^19]: https://www.new-england-industry.example/ice/decline
[^20]: https://www.lloyds-register-archive.example/voyages/margaret-ellery-1882
[^21]: https://www.harvard-business-archive.example/tudor-papers/harvest-instructions
[^22]: https://www.new-england-industry.example/ice/pond-rights
[^23]: https://www.new-england-industry.example/ice/snow-and-flooding
[^24]: https://www.farm-journal-archive.example/1856/february/ice-for-market
[^25]: https://www.walden-region-history.example/oral-histories/ice-crews
[^26]: https://www.mit-tech-history.example/inventors/wyeth-ice-tools
[^27]: https://www.patent-records.example/1829/wyeth-ice-cutting-apparatus
[^28]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s
[^29]: https://www.new-england-industry.example/ice/breaking-and-floating
[^30]: https://www.steam-power-history.example/small-engines/ice-elevators
[^31]: https://www.boston-markets-history.example/ice/local-trade
[^32]: https://www.boston-newspaper-archive.example/1858/january/ice-crop
[^33]: https://www.new-england-industry.example/ice/open-winters
[^34]: https://www.harvard-business-archive.example/tudor-papers/pond-accounts
[^35]: https://www.hudson-valley-museum.example/collections/ice-tool-catalogues
[^36]: https://www.new-england-industry.example/ice/storage-history
[^37]: https://www.harvard-business-archive.example/tudor-papers/storage-trials
[^38]: https://www.massachusetts-engravings.example/prints/fresh-pond-ice-works-1852
[^39]: https://www.farm-journal-archive.example/1859/june/building-an-ice-house
[^40]: https://www.harvard-business-archive.example/tudor-papers/keepers-letters
[^41]: https://www.railroad-history-ma.example/branches/charlestown-ice-line
[^42]: https://www.boston-harbour-history.example/wharves/charlestown-ice-houses
[^43]: https://www.ma-archives.example/ice-ledgers/methods-note
[^44]: https://www.boston-newspaper-archive.example/1868/august/icehouse-fire
[^45]: https://www.harvard-business-archive.example/tudor-papers/agents-letters
[^46]: https://www.maritime-salem.example/papers/ship-fittings-for-ice
[^47]: https://www.maine-lumber-history.example/mills/sawdust-trade
[^48]: https://www.boston-harbour-history.example/wharves/stevedores
[^49]: https://www.sailing-ship-logs.example/collections/ice-voyages
[^50]: https://www.harvard-business-archive.example/tudor-papers/masters-instructions
[^51]: https://www.insurance-history.example/marine/perishable-cargoes
[^52]: https://www.food-history-quarterly.example/2014/new-england-apples-abroad
[^53]: https://www.havana-archive.example/colonial-trade/shipping-arrivals
[^54]: https://www.maritime-boston.example/routes/other-ports
[^55]: https://www.calcutta-history-society.example/1833/first-ice-ship
[^56]: https://www.postal-history-review.example/2009/overland-mail-to-india
[^57]: https://www.calcutta-history-society.example/port/hooghly-pilots-and-tugs
[^58]: https://www.british-library-images.example/calcutta/ice-house-1840s
[^59]: https://www.colonial-architecture-journal.example/2016/cold-storage-in-bengal
[^60]: https://www.havana-archive.example/colonial-trade/building-permits
[^61]: https://www.havana-archive.example/colonial-trade/ice-monopoly
[^62]: https://www.louisiana-archives.example/levee/warehouse-registers
[^63]: https://www.madras-heritage.example/beach-road/ice-house
[^64]: https://www.lowcountry-history.example/charleston/ice-trade
[^65]: https://www.havana-archive.example/colonial-trade/ice-depot-1840s
[^66]: https://www.hongkong-heritage.example/waterfront/early-ice-house
[^67]: https://www.memoirs-of-empire.example/collections/calcutta-domestic-life
[^68]: https://www.food-history-quarterly.example/2012/ice-cream-in-the-tropics
[^69]: https://www.immigration-history-journal.example/2012/boston-irish-winter-work
[^70]: https://www.labor-history-ne.example/winter-work/harvest-crew-sizes
[^71]: https://www.boston-newspaper-archive.example/1851/january/disturbance-on-the-ice
[^72]: https://www.labor-history-ne.example/winter-work/ice-crews-conditions
[^73]: https://www.havana-archive.example/colonial-trade/dock-labour-contracts
[^74]: https://www.boston-newspaper-archive.example/1866/february/ice-strike
[^75]: https://www.boston-newspaper-archive.example/1880/march/open-winter-hardship
[^76]: https://www.medical-history-journal.example/2013/ice-in-tropical-medicine
[^77]: https://www.louisiana-archives.example/newspapers/daily-ice-reports
[^78]: https://www.bombay-gazette-archive.example/notices/ice-sales
[^79]: https://www.river-history-review.example/2011/steamboat-provisioning
[^80]: https://www.civil-war-commerce.example/blockade/ice-shortage
[^81]: https://www.mit-tech-history.example/inventors/early-refrigeration
[^82]: https://www.patent-records.example/1851/gorrie-ice-machine
[^83]: https://www.civil-war-commerce.example/blockade/carre-machines
[^84]: https://www.louisiana-archives.example/business/ice-manufacturing-charters
[^85]: https://www.food-history-quarterly.example/2016/clear-ice-and-cloudy-ice
[^86]: https://www.calcutta-history-society.example/industry/bengal-ice-factory
[^87]: https://www.cambridge-historical.example/fresh-pond/water-supply
[^88]: https://www.harvard-business-archive.example/tudor-papers/finding-aid-overview
[^89]: https://www.labor-history-ne.example/winter-work/after-the-sea-trade
[^90]: https://www.cuba-commerce-history.example/1870s/manufactures
[^91]: https://www.ice-trade-voyages.example/registers/calcutta-arrivals
[^92]: https://www.boston-newspaper-archive.example/1880s/ice-coverage-survey
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
PASS  judge-footnotes-resolve   Every body marker has a matching definition under Sources, every definition holds a URL, and every definition is cited in the body.  **Definitions present:** [^1]–[^50], [^52], [^54]–[^76], [^78]–[^83], [^85], [^86], [^87], [^89]–[^92]. Each is a URL, for example "[^1]: https://www.cambridge-historical.example/fresh-pond/ice-harvest-overview" and "[^92]: https://www.lloyds-register-archive.exampl
PASS  judge-planted-details-cite-own-url   All eight details appear in the note, and each carries a footnote whose Sources entry is the expected URL.  1. **Topic 1, 22-inch blocks.** "The grid was laid out so the blocks came out 22 inches square on the surface.[^9]" The Summary also gives "22 inches square on the surface,[^9]".    - `[^9]: https://www.cambridge-historical.example/fresh-pond/ice-marker-1840s` ✓ 2. **Topic 2, 17 percent los
PASS  judge-reply-no-cut-short   The reply names no topic as cut short. The only relevant field is `"cut_short_topics": []`, an empty list. That means no file or topic was reported as truncated, incomplete, or missing its closing line. The other field, `"note": "Research/research-light-ice-trade.md"`, is a file path and makes no claim about truncation.
PASS  judge-sixteen-questions-answered   All sixteen questions are answered with the findings' substance:  1. **Ice readiness:** "usually from the middle of January into February, once a long hard freeze had set in"; "not cut until it was at least 14 inches thick"; "Each morning a foreman walked the pond with a hand auger and bored test holes." 2. **Tools and block size:** Wyeth "designed a horse-drawn cutter in 1825 and patented an imp
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

File written: `project/Research/research-light-ice-trade.md`

````
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
> Eight topics: cutting the ice on the ponds; storing the ice before shipping; loading the ship; the voyage; ice houses at the far ports; the workers; buyers and prices; and the end of the trade. Limit for every topic: New England ice shipped by sea, from the trade's start to its end.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Ice Trade

## Summary

The New England ice trade by sea began badly. Frederic Tudor's first cargo went from Boston to Martinique in 1806 and mostly melted on the wharf, because the island had no ice house. By the 1820s he was shipping ice regularly to Havana and to ports in the southern United States, having learned to build an ice house before the first cargo arrived.[^38]

The chain ran from a frozen pond to a customer's basket in a hot port. Ice was cut in the coldest weeks, usually mid-January into February, once a long hard freeze had set in.[^1] Clear ice had to be at least 14 inches thick.[^1] From the late 1820s, horse-drawn tools designed by Nathaniel Wyeth cut it into blocks of one regular size.[^7] The grid made blocks 22 inches square on the surface,[^9] and the firm's working figure for a standard block was roughly 200 pounds.[^15] The blocks were stored for months in large, double-walled, sawdust-filled icehouses on the pond shore.[^17] The largest house on Fresh Pond held about 9,400 tons.[^17] A surviving 1847 ledger records a loss of about 17 percent over one season.[^23]

The ice sailed in ordinary merchant ships that would otherwise have left Boston in ballast, so carriage was cheap.[^29] The holds were lined to make an insulated box,[^32] packed with about one ton of sawdust for every 11 tons of ice,[^34] and sealed until arrival.[^37] The crew pumped out melt water every 4 hours.[^36] The longest regular route, Boston to Calcutta, took about 130 days.[^41] A logbook study found an average loss of 38 percent on that run.[^47] The Caribbean runs took two to three weeks,[^42] and the short routes often lost under a tenth of the ice.[^30] New Orleans took more New England ice than any other port by the 1850s.[^44]

At the far ports, agents ran insulated ice houses. Calcutta's was a round brick building holding about 1,250 tons.[^50] They sold ice by weight in the early morning hours.[^60] Calcutta prices stood at 3 annas a pound in the 1830s and 1840s.[^60] By 1860, New Orleans ice sold for about 2½ cents a pound.[^76] The harvest crews were local farmers at first, then increasingly Irish immigrants from the 1840s,[^65] and French-Canadians in the later decades.[^66] Their work was cold and dangerous.[^69]

The sea trade peaked around 1860 and was nearly over by the 1880s. War, ice-making machines, steamships, and the growth of the home market for natural ice all played a part.[^30] The last recorded New England ice cargo to Calcutta sailed in 1882 on the bark *Margaret Ellery*.[^92] Sources disagree about when the shipping trade ended altogether.[^28]

## Cutting the ice on the ponds

**When the ice was ready.** The harvest ran in the coldest weeks of the year, usually from the middle of January into February, once a long hard freeze had set in.[^1] Ice was not cut until it was at least 14 inches thick. Thinner ice crumbled at the corners when handled, wasted space in the hold, and melted faster, because a thin block has more surface for its weight.[^1] Each morning a foreman walked the pond with a hand auger and bored test holes at set points. He measured the clear ice and, separately, any white snow ice on top. Only the clear ice counted toward the thickness.[^3] If the readings fell short, the crew was sent to clear snow or stood idle.[^3] Some firms paid a small bonus to the foreman whose pond reached cutting thickness first.[^3] Because one corner of a pond could be ready days before another, cutting often began near the shaded shore and moved outward.[^1]

**Which ponds.** The shipping firms preferred spring-fed ponds with no streams running in. Moving water froze unevenly and carried silt, leaves, and sawdust from upstream mills into the ice.[^1] Fresh Pond in Cambridge, Wenham Lake north of Salem, and Spy Pond in Arlington were the best known. The firms bought or leased the shore rights so that no rival could cut there.[^1] A pond owner could earn more from one winter's ice rights than from a year of farming the land around it.[^2] Clear ice was the product the trade was built on. Buyers in hot ports judged ice by its clarity and took cloudy ice as a sign of dirty water, even when it was not.[^1]

**Clarity tests and snow.** Before the harvest, a foreman cut a small block, held it up against the light, and looked for bubbles, streaks, and dirt. A block that showed a dark object clearly through its whole thickness was good enough for shipping.[^6] If the test block was cloudy, cutting moved to stiller water further from the inlet or shore. The test was repeated every few days.[^6] Snow was the harvest's main enemy. It slowed freezing underneath, and wet snow that froze on top became "snow ice," which was white, airy, and weak.[^4] Crews cleared snow with horse-drawn scrapers: wide wooden boards dragged across the surface.[^4] On some ponds they bored holes and flooded the cleared surface so a fresh layer froze on top. This only worked in hard cold, because slow freezing made the new layer cloudy.[^4]

**From hand tools to horse tools.** Before the 1820s, ice was cut by hand with axes, hand saws, and chisels. That made uneven blocks that stacked badly and let warm air into the gaps.[^7] Nathaniel Jarvis Wyeth, a Cambridge hotel manager who later worked for the Tudor ice company, designed a horse-drawn cutter in 1825 and patented an improved version in 1829.[^8] Historians describe the move from hand cutting to horse tools as the change that made long voyages possible, because regular blocks lost less ice to melting.[^7] By the 1840s, most commercial ponds in Massachusetts used some version of Wyeth's tools.[^7]

**The cutting sequence.** The first tool was the "marker," a plough-like frame with a row of steel teeth. One horse drew it along a straight line laid out with a cord, and a guide arm kept each groove parallel to the last.[^9] Once the field was scored one way, the marker was run across at a right angle to make a grid. The grid was laid out so the blocks came out 22 inches square on the surface.[^9] The "plough," with longer teeth, was run along the same grooves again and again until each cut went about two-thirds of the way through. The remaining third held the field together so men and horses could still walk on it.[^9] The horses walked on uncut ice beside the line being cut, never on the grooves.[^5] Horses wore sharp-calked shoes, which had spikes that gripped the ice, and a blacksmith was kept near the larger ponds.[^6]

Crews then sawed a channel to the shore with long hand saws. Men with iron "breaking bars," flat chisels on long handles, split the field along the grooves into rafts and then into single blocks.[^10] A skilled bar man could tell from the sound of the strike whether a groove was deep enough.[^10] Men with pike poles pushed the floating blocks along the channel to the shore.[^10]

**Up the elevator.** At the shore, an inclined elevator carried the blocks into the icehouse. It was a long wooden ramp with an endless chain whose cleats caught each block.[^11] At first a horse at a capstan drove the chain. From the 1850s, the largest houses used small steam engines.[^11] Before each block went up, a man planed its top and bottom flat, removing snow ice so it sat evenly in the stack.[^1] The elevator could run day and night by lantern when the weather held.[^1]

**Grading and tallying.** The clearest blocks were marked first quality and set aside for shipping. Blocks with a cloudy band or trapped leaves were second quality and usually sold locally, to households and butchers in Boston and nearby towns.[^12] One firm's papers tell foremen to reject any block they would not want to see on a dinner table.[^3] The harvest was counted, not weighed. A tally man at the top of the elevator marked each block, and the marks were turned into tons by a fixed figure for a standard block of roughly 200 pounds.[^15] Pond owners were usually paid by the ton taken and sometimes sent their own man to keep a second tally.[^15]

**Weather and pace.** A thaw or rain mid-season softened the ice and flooded the grooves, and the field often had to be planed and cut again.[^14] In an "open winter," too mild to cut, the shippers bought ice from ponds further north, in Maine and New Hampshire, at a higher cost.[^14] In a good season a large pond could be cleared in two to three weeks.[^14] Several firms kept icehouses on two or more ponds so that one bad pond would not cost them the whole year.[^14]

**Tool sets.** By the 1850s, specialist firms sold the tools as complete sets, many of them made in the Hudson valley of New York. A large set included one or two markers, several ploughs, hand saws up to six feet long, breaking bars, pike poles, ice tongs, and snow scrapers.[^16] The makers' printed catalogues are now one of the main sources for how the work was done.[^16] The tools changed little over the life of the shipping trade.[^16]

## Storing the ice before shipping

**Where and why.** The harvest came in over a few weeks, but ships sailed all year, so ice was stored for months.[^17] The firms built their icehouses on the pond shore, above ground, so blocks went straight from the channel up the elevator.[^17] This replaced the older farm practice of keeping ice in hillside pits. Those held only a few tons, let groundwater seep in, and took heat from warm summer soil.[^18]

**Walls, roof, and floor.** An icehouse had two wooden walls built a little apart, with the gap packed with insulating fill. Sawdust from timber mills was usual, and spent tanbark from tanneries was also used. Some houses had three walls with two layers of fill.[^19] In the 1820s and 1830s, Frederic Tudor and Nathaniel Wyeth tested fills in small trial houses, weighing the ice at the start and end of summer. They found a dry fill kept ice far better than a damp one.[^19] Houses therefore had wide eaves to keep rain off the outer walls.[^19] Roofs were steep, with louvred vents along the ridge to let warm air escape.[^18] Most houses were painted white or a light colour, and some had hay or straw in the roof space.[^21] Water was more dangerous than warm air. Floors were built over gravel or broken stone, with a drain to the pond and a thick layer of sawdust on top.[^19] A house with a blocked drain could lose a large part of its bottom layers in a single warm month.[^19]

**Capacity.** The biggest icehouse on Fresh Pond held about 9,400 tons when full and was taller than a three-storey building.[^17] It was built as a row of rooms under one long roof, each filled and emptied on its own, so opening one did not warm the rest.[^17] Contemporary engravings show a long, windowless block with doors stacked one above another on the elevator side. Each door was boarded shut as the stack rose past it.[^20] Smaller firms built houses holding a few hundred tons and sold mostly to the local market.[^17] The firms also kept smaller icehouses on the Charlestown wharves, each holding a few hundred tons. These held ice brought down a few days before a sailing. Ice was not kept there long, because the harbour air was warmer and damper.[^25]

**Stacking and taking out.** Blocks were set on edge, tight against each other, with each layer laid across the one below like brickwork. Chips filled the gaps, and a full room was topped with a deep layer of hay or sawdust.[^17] Air in the gaps was the main source of melting inside a stack.[^17] When a ship was ready, ice came out from the top down, one room at a time. Frozen-together blocks were broken apart with bars, and the fill was scraped off so no sawdust went on board.[^3]

**The keeper.** Each large icehouse had a keeper who lived beside it all year. He checked drains and vents, kept the doors shut, watched for fire, and kept the ledger of ice in and out.[^22] He chose which room to open for each order, using the oldest ice first and keeping the best-packed rooms for the hottest months.[^3] From the 1850s some keepers hung thermometers above the stack. A rising reading showed a door left open or a clogged vent.[^22]

**How much was lost.** The ledgers of one Fresh Pond icehouse for 1847 show a loss of about 17 percent between the end of the harvest in March and the last autumn sailing. Most of the loss came in July and August.[^23] The keeper blamed the heat and a roof vent that had been left shut.[^23] A room left unopened until autumn lost less than one opened in June.[^23] It is the only surviving record of a whole season's loss for a single house, and historians use it as the standard figure.[^23] Large houses lost less than small ones, because a big stack has less surface for its weight. This is the main reason the firms built ever-larger houses through the 1840s and 1850s.[^18] Other figures for storage loss are under Disagreement / Uncertainty.

**Getting it to the harbour.** From the early 1840s, a railway branch ran from Fresh Pond to the Charlestown wharves and cut the trip to under an hour. Before that, wagons on a hot road could lose a noticeable part of their load.[^24] The ice wagons had thick wooden sides packed with sawdust, and in summer the trains ran at night.[^24]

## Loading the ship

**The ships.** Ice went in ordinary merchant ships. Boston imported much from the tropics but had little to send out, so many ships left in ballast. Ice gave them a paying outward cargo, and owners charged low rates to carry it.[^30] Older ships were often chosen, because the ice firms' carpenters built linings into the hold.[^29] Holds were emptied, swept, and aired first, because any smell could pass into the ice. The firms kept a list of ships whose holds could not be cleaned, and ships that had carried coal were avoided.[^31]

**The lining.** A carpenter built an inner wall of pine planks a little in from the hull on all sides, with sawdust packed between. The lining ran across the floor and up under the deck beams, making a box inside the hull on the icehouse plan.[^32] Sailors called it the "ice ceiling." It took a carpenter and two helpers about a week for a ship of middling size.[^32] The floor was laid on rough timber called dunnage, to lift the cargo clear of the bilge, and topped with a deep bed of sawdust. Gaps at the sides let melt run to the pumps.[^32] On most voyages that kept records, the loss from the bottom layer was the largest single loss.[^32]

**Packing the ice.** Stevedores lowered the blocks through the hatch in slings and stowed them as the icehouse crews did: on edge, tight, each layer across the one below, with chips and sawdust pushed into every gap.[^35] A Salem merchant's paper of 1850 sets the ratio at one ton of sawdust for every 11 tons of ice. Less saved weight but cost more ice than it saved, and more took space that could carry ice.[^34] The sawdust had to be dry, because wet sawdust froze onto the blocks and conducted heat in.[^33] Ice was stowed low and spread evenly from bow to stern to keep the ship stable and level. Ships usually carried less ice than their rated tonnage, because of the weight and space of the lining and sawdust.[^32] A ship of middling size could be loaded in one to two days, often through the night or early morning, and sailed on the next tide if the wind allowed.[^35]

**Stopping it melting or shifting.** The top of the stack was covered with sawdust and then hay. The hatches were closed, covered with tarred canvas, and battened down. Some ships also fitted a second, inner hatch cover with sawdust between the two.[^32] Moving air carried heat to the ice, so the aim was to keep the air in the hold as still as possible.[^32] Once sealed, the hatches stayed sealed until port. The firms' instructions warned that a master who opened them without good cause would answer for the lost ice.[^37] To stop the cargo shifting, stevedores drove timber battens between the stack and the lining and wedged the top layers against the deck beams.[^36] Logbooks record a few voyages where heavy weather loosened the stack, and each arrived with a much smaller cargo.[^36] Melt water was pumped out every 4 hours, day and night. The mate logged the strokes needed to clear the bilge, which served as a rough gauge of melting. A sudden rise meant the stow had shifted or the lining had broken.[^36]

**Who bore the risk.** Early marine insurers refused to cover ice at all. Later policies covered the ship and a share of the cargo but excluded loss from melting, so the shipper bore it.[^39]

## The voyage

**Routes.** The longest regular route ran from Boston to Calcutta. Ships went south through the Atlantic, rounded the Cape of Good Hope, and crossed the Indian Ocean to the Hooghly River, crossing the equator twice. The voyage took about 130 days.[^41] The first Calcutta cargo sailed in May 1833 on the ship *Tuscany* and arrived that September. It caused a sensation, made a profit, and led to regular sailings.[^46] The Caribbean routes, to Havana, Martinique, Jamaica, and the other islands, took two to three weeks with fair winds. Havana became one of the steadiest markets, with ships every few weeks.[^42] The southern United States ports were the largest market by volume: Charleston, Savannah, Mobile, and above all New Orleans. The voyage to New Orleans took several weeks.[^44] The southern trade carried most of the ice that left Boston in most years.[^30] Less regular routes went to Rio de Janeiro, Valparaíso, Bombay, Madras, Hong Kong and other Chinese ports, and a few cargoes to Australia. Some of these were dropped after a few years as unprofitable.[^45]

**Timing and speed.** Calcutta sailings were timed to arrive in the hot season, about March to June. Ships therefore left Boston in autumn and early winter, which also kept the hold cool in the first weeks.[^41] The Caribbean and southern ports got ice all year, with the most ships in the hot months.[^41] Firms paid more for fast ships on the India run.[^41] Calms near the equator, the doldrums, cost ice with no distance gained, and masters were told to keep moving at all costs.[^37] From the 1840s, many ice ships were towed up the Hooghly by steam tugs, cutting days of sailing to a day or less.[^49] Masters kept a separate printed "ice book" with columns for date, position, air and sea temperature, and pumping strokes.[^36]

**How much melted.** Most melting happened in the tropics. Pumping strokes were low in the first weeks out of Boston, rose sharply near the equator, and stayed high. On the Calcutta route the second tropical crossing was the worst.[^36] A study comparing ice signed for in Boston with ice unloaded in Calcutta found an average loss of 38 percent, varying widely with season, voyage length, and the stow.[^47] The short routes lost much less: a well-stowed cargo to Havana or New Orleans often lost under a tenth.[^30] One firm's papers show the Caribbean trade paying for losses on the Indian trade in more than one year.[^15] A competing, lower estimate for Calcutta is under Disagreement / Uncertainty.

**Return cargoes.** Ships came back from Calcutta with jute, linen, indigo, saltpetre, and spices, and from the Caribbean with sugar, molasses, and coffee.[^30] The return cargo was often worth more than the ice. Some historians of the trade, in a peer-reviewed economic history, argue that shipowners took ice voyages mainly to put a ship in Calcutta for that return cargo.[^30] Linings were removed in the far port.[^30]

## Ice houses at the far ports

**Build first.** The Martinique failure taught the rule to build the ice house before the ice arrives. From the 1810s the firms built or rented one in each port before sending regular cargoes, sometimes a converted warehouse with extra walls inside, and sent carpenters from Boston with the first cargo.[^38]

**Calcutta.** The Calcutta ice house was paid for by a subscription among the city's merchants after the 1833 cargo and opened a few years later. It was a round brick building near the river with thick walls and a domed roof, and it held about 1,250 tons when full. The round shape gave the least wall surface for the space inside.[^50] It followed the Boston plan of inner and outer walls with fill between, but in brick, because termites and monsoon damp ruined wood. Its floor drained to the river, and the dome sat over a ventilated space.[^52] An agent sent out from Boston ran it with local staff, and the merchants' committee that had paid for it complained when ice ran short.[^31]

**Other ports.** In Havana and some other ports, the houses were partly sunk below street level, where the earth stayed cooler. On low wet ground, as at New Orleans, houses had to stand fully above ground.[^52] The Tudor firm built the Havana house near the harbour in the 1820s under a monopoly granted by the Spanish colonial government. The firm had to keep the city supplied all year and could be fined for running out.[^54] Ice was rowed ashore in lighters at night and carried to the house.[^43] By the 1840s New Orleans had several large competing houses on the levee next to the wharves.[^55] Bombay and Madras got masonry houses on the Calcutta model in the late 1830s and early 1840s, both smaller than Calcutta's. At Madras, ice came ashore through the surf in small boats.[^56] Charleston and Savannah had smaller wooden houses raised on brick piers, often owned by local merchants who bought whole cargoes from the Boston firms.[^57] Hong Kong's granite waterfront house dates from the 1840s. Its trade was small and irregular.[^59]

**Running and selling.** In Havana the firm's agent, a local merchant named Joaquín Barcia, ran the house through the 1840s and sold ice by ticket. Customers bought a ticket for a set weight at the city office and collected the ice at the house door, so no money changed hands there.[^58] Ice was sold by weight on a large scale at the door. Some houses kept blocks pre-cut to standard weights.[^44] Houses opened only from first light to mid-morning. In Calcutta the hours were printed in the newspapers, and latecomers were turned away.[^60] Large buyers such as hotels, clubs, hospitals, and military messes had monthly accounts and were often served before the queue.[^60] In New Orleans by the 1850s, carts delivered ice in insulated boxes to standing orders. In Havana and Calcutta, delivery was rare.[^44] Agents were usually paid a share of sales and quarrelled with Boston over cargoes that arrived in poor condition.[^31] Ice kept far less well in the tropical houses, so agents tried to sell each cargo before the next arrived.[^31] Where ice was new, agents gave it away at first and taught bar owners, cooks, and doctors to use it. Tudor's diary records doing this in Havana and Charleston before charging.[^38]

## The workers

**Who.** In the early years, most men on the ice were local farmers and their sons, harvesting in farming's slack season. They brought their own horses and were paid for the horse as well as the man.[^63] From the 1840s, a growing share were Irish immigrants. The firms hired them in large numbers for unskilled jobs, while skilled jobs often stayed with local men.[^64] In the later decades, French-Canadian labourers came south, some from New England mill towns and some from Quebec for the season. By the 1870s, some crews on the larger ponds were mostly French-Canadian.[^66] When local labour was short, agents hired men off the Boston streets and paid their train fares out.[^64] Boys from about age twelve guided blocks, swept chips, and ran messages for less pay.[^6] Women did not work on the ice. They ran boarding houses, cooked for the shanties, and dried wet clothing, and the firms' accounts usually record payments under the household's name.[^63]

**Organisation.** Labourers were hired by the day at the pond's edge, with no promise of work the next day.[^6] (That account comes from oral histories of the last commercial harvests.) Skilled men, the marker drivers, stackers, and bar men, were hired for the season and paid more.[^3] Each crew had a foreman who answered to the firm's superintendent for the pond.[^3] On the largest ponds a crew numbered about 75 men, divided into gangs: snow scrapers, marker and plough, bar men, channel men, elevator, and stackers. The slowest gang set the pace.[^67] Pay came weekly on Saturday evening at the shore shanty, less board.[^15] The ship-loading stevedores were a separate, year-round waterfront workforce, working in gangs paid by the ton.[^35] At the far ports, Calcutta porters carried blocks at night. In Havana, colonial records show the depot hiring enslaved men from their owners to unload the ships.[^70]

**Conditions and dangers.** The cold is the hardship every account mentions. Frostbite was common, and men wore layers of wool, felt boots, and spiked iron "creepers." A man who got wet was sent straight to the shanty fire.[^69] The firms fed the larger crews with hot coffee, soup, and a midday meal.[^6] Days ran from first light to dark, and when a thaw was forecast the work ran into the night and onto Sundays without extra pay unless the foreman agreed.[^13] Men slipped, cut themselves on saws and bars, and were crushed by blocks on the elevator. Injured men were paid nothing beyond days already worked.[^69] The worst danger was falling through. A count of newspaper reports for the Cambridge ponds found nine drownings among harvest crews between 1850 and 1860, most in the open channel at night. No railings or lights went up until late in the trade.[^69] Horses also broke through, and crews looped a rope around the animal's neck to make it float higher and dragged it out.[^6] Newspapers reported fights between local and Irish men, especially in years when work was short. Foremen sometimes kept the groups in separate gangs.[^68] Crews sometimes struck for higher daily pay when a thaw was forecast, and the firms answered by blacklisting strikers.[^71] An open winter meant no winter wage, and Boston charities reported more families seeking help afterwards.[^72]

## Buyers and prices

**Calcutta and India.** The first buyers were British residents: East India Company officials, army officers, merchants, and their families. Wealthy Indian merchant and landowning families bought from the early years and were regular customers by the 1840s. For most of the city, ice was far too costly.[^50] Ice sold at the door for 3 annas a pound (an anna being a sixteenth of a rupee) through most of the 1830s and 1840s. Account customers sometimes paid less by private agreement.[^60] Hospitals were among the largest account customers and got a reduced rate in return for taking ice every day of the hot season.[^73] Clubs and officers' messes served iced drinks all season.[^61] Ice cost more in Madras and Bombay than in Calcutta, with similar buyers including Parsi merchant families.[^75]

**Havana.** The main buyers were cafés, confectioners making ice creams and sorbets, and wealthy households. Within a generation, ice went from a luxury of the rich to a common pleasure in the city's cafés.[^62] Under the monopoly, the firm agreed to a maximum price, which the government revised several times. The firm could not raise prices in the hottest weeks.[^54]

**The southern United States.** New Orleans used ice on a scale no other port matched: bars, hotels, households, meat and fish markets, and river steamboats. By the 1850s the local press called it a necessity rather than a luxury.[^74] Prices there fell steadily from the 1830s to the 1850s as competing firms and houses arrived, and the firms made their money on volume.[^44] By 1860 the city's price current, a weekly commercial paper, gave about 2½ cents a pound at the levee houses, rising in hot months and when ships were late. At that price ice was within reach of ordinary working households for at least part of the year.[^76] In Charleston and Savannah, the buyers were planters, merchants, hotels, and taverns.[^57] In Hong Kong they were the garrison, the trading-house merchants, and ships in harbour.[^59]

**What drove the price.** The ice cost almost nothing at the pond. A study of the trade's costs found that ice lost in transit and storage was the largest single cost on the long routes, larger than carriage.[^30] In every port, prices were lowest just after a ship arrived and highest when the next was overdue.[^60] Boston firms fought price wars, underselling a rival in a port until it gave up and then raising the price again.[^31] At small ports with no ice house, masters sold from an open hatch at whatever buyers would pay.[^37] The trade made Tudor one of Boston's richest men by the 1840s, known as the "Ice King." The profits came mostly from the southern and Caribbean markets.[^38]

## The end of the trade

**What ended it.** The sea trade grew through the 1840s and 1850s, peaked around 1860, and declined, slowly and then quickly. By the 1880s the long-distance trade was nearly over. No single cause ended it, and the order of causes differed from port to port.[^30]

- **War.** In the American Civil War (1861–1865), the Union blockade closed New Orleans to Boston ships until Union forces took the city in 1862. The Confederacy went without shipped ice for most of the war, and the shortage pushed southern businessmen toward machines.[^79] After the war the southern trade returned, but well below late-1850s levels.[^79]
- **Machines.** John Gorrie patented an ice machine in 1851.[^81] Ferdinand Carré developed an ammonia machine in the late 1850s, and James Harrison built machines in Australia in the 1850s. These early machines were costly and made little ice.[^80] Some Carré machines were run through the blockade during the war.[^82] New Orleans got its first commercial ice factory in 1868, making about 12 tons a day at first, and more followed.[^83] Through the 1870s, factory ice became cheaper than shipped ice once melt losses were counted.[^30] The Boston firms tried undercutting the factories, which closed a few small ones in the 1870s but could not last.[^44] Early factory ice was cloudy and distrusted, which slowed the switch in some ports until clear factory ice arrived by the 1880s.[^80] In Havana the monopoly was not renewed after the American war, and factories opened in the 1870s.[^89] Cuba's independence wars from 1868 also disrupted trade.[^89] In India, factories opened in the 1870s and 1880s. Calcutta's began in the late 1870s, and the old ice house lost its trade within a few years.[^85]
- **Steamships.** The trade relied on cheap sailing ships that would otherwise sail empty. As steamships took the Asian routes, especially after the Suez Canal opened in 1869, that supply shrank, and carrying ice by steam cost more.[^41]
- **The home market and the ponds.** Demand for natural ice grew fast in northern and midwestern American cities, and the ponds could sell all they cut at home by rail, so many firms turned away from the sea. This home trade lies outside the sea trade this note covers, but it bears on why the sea trade ended.[^78] Fresh Pond became Cambridge's water supply and harvesting there stopped, and other ponds near Boston were built over.[^86]
- **People.** Tudor died in 1864, and his firm did less well under his family. Other firms merged into home-market companies.[^87]

**The last cargoes.** The Indian trade dwindled through the 1870s, with some years seeing only one or two ships. The Bombay and Madras trade ended before Calcutta's.[^90] The last recorded New England ice cargo to Calcutta sailed from Boston in 1882 aboard the bark *Margaret Ellery*. No later ice ship appears in the Calcutta register, and the master noted that the cargo arrived in fair condition.[^92] The Boston papers printed no reports of the last ships.[^91] Whether any shipments continued after the early 1880s is disputed (see below).

## Disagreement / Uncertainty

- **Storage loss.** The 1847 Fresh Pond ledger, which weighed sample blocks, gives about 17 percent for a season.[^23] A general history says a well-built house lost between a fifth and a third over a summer, and small houses sometimes half. It gives no source for these figures.[^28] An archives research note warns that ledgers kept by counting blocks show smaller losses than ledgers kept by weighing, so figures from the two methods cannot be set side by side.[^26]
- **Voyage loss to Calcutta.** A logbook study found an average of 38 percent.[^47] Its authors note that the surviving papers may come from the better-run voyages.[^47] A general history says well-stowed ships lost about a quarter and blames higher losses on poor stowing, without saying how it reached the figure. Neither source says which years its figure covers.[^28] The "under a tenth" figure for the short routes is an estimate from a small number of voyages.[^30]
- **When the shipping trade ended.** Some histories say the early 1880s. A general history says Caribbean cargoes continued irregularly into the 1890s, and small shipments to southern ports went on into the early twentieth century when factories could not keep up. It gives no source for the later shipments.[^28] The 1882 *Margaret Ellery* voyage is the last recorded cargo to Calcutta specifically.[^92]
- **Rescuing horses.** The rope method is described in oral histories and one magazine piece, with no count of how often it worked.[^6]
- **Blockade machines.** The number of Carré machines brought through the blockade is not known.[^82]
- **Lasting effect.** Historians of the trade argue that the New England firms created the demand that later ice factories supplied.[^62]

## Useful Details

- Foremen kept daily notebooks of dawn and noon temperature, wind, and snowfall.[^1]
- Newspapers described the harvest as a race against the weather, with Sunday cutting against local custom when a thaw was forecast.[^13]
- The hold linings were often sold as timber in the far port, since timber was scarce in some tropical ports.[^32]
- Maine sawmills came to depend on selling sawdust, once a waste they burned or dumped, to the Boston trade. Buyers checked each schooner load by hand for dryness.[^33]
- In the first years, sailors feared that melting ice would sink the ship. Tudor's diary records crews deserting before sailing.[^38] Insurance records later show ice ships lost in about the same numbers as other ships on the same routes.[^39]
- Apples, butter, and cheese rode in pockets cut into the stack, usually as the master's or agent's private trade. They arrived in Calcutta and Havana in good condition.[^40]
- An agent reported a cargo tasting of fish being sold at a loss to a butcher.[^31]
- In one logbook, a master heard the ice "working" in the hold during a gale and could do nothing, since the hatches could not be opened at sea.[^36]
- News of a Calcutta voyage could take most of a year to reach Boston. Some letters later went by the faster overland route through Egypt.[^48]
- Calcutta ships sometimes sold ice at Cape Town or Mauritius, with masters told to reseal within the hour.[^37]
- An agent's letter complains of a ship that waited three days at the Hooghly mouth for a tug.[^49]
- Calcutta's ice house appears in paintings and later photographs of the riverside.[^50]
- Calcutta servants carried ice home in blanket-wrapped baskets on their heads at a run. At home it lasted about a day in a felt-lined box or a pot within a pot.[^61]
- Some Indian households in the 1830s questioned whether ice handled by foreign sailors and porters was clean, according to British newspapers.[^60]
- Icehouses burned, often in summer, sometimes from railway sparks. The ice inside usually survived the fire and then melted within days unless it could be loaded at once.[^27]
- The Madras ice house still stands on the seafront, altered, and is now a museum.[^56] The Calcutta house was pulled down, and the Havana house has not been traced.[^50]
- The Tudor firm's papers are the largest single source on how the trade worked.[^87]

## Open Research Questions

- What were the Havana maximum prices in figures, and how did they change at each revision?
- What did ice cost in Madras and Bombay in figures?
- Which years do the general history's figures for storage and voyage loss cover?
- What were the daily wages of harvest labourers and skilled men?
- Did any New England ice cargoes sail to the Caribbean or the southern ports after the early 1880s, and when was the last?

## Reliability / Limitations

- `new-england-industry.example/ice/pond-rights`: cites no archive for the pond-rights figures.
- `farm-journal-archive.example/1856/february/ice-for-market`: gives advice to farmers, not an account of a single harvest.
- `farm-journal-archive.example/1859/june/building-an-ice-house`: written for farmers, not for the shipping firms.
- `walden-region-history.example/oral-histories/ice-crews`: recorded from people who worked the last commercial harvests, long after the shipping trade ended, so it may not describe the early trade. The horse-rescue method is described with no count of how often it worked.
- `harvard-business-archive.example/tudor-papers/pond-accounts`: the figure for the weight of a block is the firm's own working figure, not a measured average.
- `cambridge-historical.example/fresh-pond/icehouses`: the size of the largest house comes from a company prospectus.
- `ma-archives.example/ice-ledgers/methods-note`: loss figures from counting and from weighing cannot be set side by side.
- `ice-trade-voyages.example/logs/calcutta-melt-study`: the voyages whose papers survive may have been the better-run ones.
- `boston-newspaper-archive.example/1868/august/icehouse-fire`: covers one fire. The industry history site gives no count of fires.
- `popular-history-press.example/books/the-frozen-water-trade-excerpt`: a book excerpt for a general audience that gives its storage-loss, voyage-loss, and late-shipment figures without a source.
- `harvard-business-archive.example/tudor-papers/agents-letters`: the fish-tasting story comes from one agent's letter. Agents report far-port losses in general terms, not comparable figures. The letters describe the firm's tactics from its own side and mention local workers only in passing.
- `harvard-business-archive.example/tudor-papers/diary-excerpts`: records Tudor's own view of his difficulties.
- `sailing-ship-logs.example/collections/ice-voyages`: the comment on ships rolling comes from masters' remarks, not measurement.
- `economic-history-review.example/2010/ice-shipping-costs`: the loss figure for the short routes is an estimate from a small number of voyages.
- `colonial-architecture-journal.example/2016/cold-storage-in-bengal`: compares ports and gives the Havana design as a contrast to Calcutta.
- `hongkong-heritage.example/waterfront/early-ice-house`: relies on newspaper notices and gives no building records.
- `memoirs-of-empire.example/collections/calcutta-domestic-life`: by British residents describing their own households only.
- `calcutta-gazette-archive.example/notices/ice-house-hours`: reports on Indian customers were written by British newspapers.
- `boston-newspaper-archive.example/1851/january/disturbance-on-the-ice`: short reports that give one side.
- `boston-newspaper-archive.example/1866/february/ice-strike`: takes the firms' side.
- `havana-archive.example/colonial-trade/dock-labour-contracts`: employers' contracts. No account by the workers survives in these collections.
- `labor-history-ne.example/winter-work/ice-crews-conditions`: the drowning count comes from newspaper reports, which may have missed some deaths.
- `civil-war-commerce.example/blockade/carre-machines`: the number of machines brought through the blockade is not known.
- `gulf-commerce.example/ports/new-orleans-ice-imports`: gives no list of the factories that closed.
- `havana-archive.example/colonial-trade/ice-monopoly`: the colonial records end before the monopoly's last years. The later account comes from `cuba-commerce-history.example/1870s/manufactures`.

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
[^78]: https://www.new-england-industry.example/ice/decline
[^79]: https://www.civil-war-commerce.example/blockade/ice-shortage
[^80]: https://www.mit-tech-history.example/inventors/early-refrigeration
[^81]: https://www.patent-records.example/1851/gorrie-ice-machine
[^82]: https://www.civil-war-commerce.example/blockade/carre-machines
[^83]: https://www.louisiana-archives.example/business/ice-manufacturing-charters
[^85]: https://www.calcutta-history-society.example/industry/bengal-ice-factory
[^86]: https://www.cambridge-historical.example/fresh-pond/water-supply
[^87]: https://www.harvard-business-archive.example/tudor-papers/finding-aid-overview
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

Case folder: `research-writer-08-cut-short`. Run folder: `writer`.

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
PASS  judge-dipper-questions-open   The Open Research Questions section lists both topic 2 questions as unanswered:  > ## Open Research Questions > > - Who were the dippers beyond being female attendants who stood in the sea beside the machine steps, and what exactly did their work involve? > - How was the dippers' work licensed or paid? > - Which resorts used winches rather than horses, and in which years?  - **Bullet 1** covers "
PASS  judge-footnotes-resolve   Every marker in the body has a definition with a URL. Every definition is used.  **Markers in the body:** [^1], [^2], [^3], [^4], [^5]. Each appears several times. - [^1] and [^2]: "A bathing machine was a small wooden hut on four large wheels… [^1] [^2]" - [^3]: "a winch on the shore hauled it on a cable instead. [^1] [^3]" - [^4]: "A bather who stayed too long paid for a second turn. [^4]" - [^
FAIL  judge-nothing-from-cut-short   **Open Research Questions:** > "How was the dippers' work licensed or paid?"  This question assumes the dippers were licensed. That comes only from the cut-short topic 2 fact: "At the larger resorts dippers were licensed by the town commissioners… and renewed the licence every May." Topic 1 says only that dippers were female attendants who stood in the sea beside the steps. It says nothing about 
PASS  judge-reply-names-topic-2   The reply names topic 2, and only topic 2, as cut short: `"cut_short_topics": [2]`. It does not list topic 1 or topic 3, and it does not claim that no file was cut short.
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

File written: `project/Research/research-light-bathing-machines.md`

````
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
> Topics: the bathing machine; the dippers; keeping men and women apart. Limits: British seaside resorts only, in the years 1840 to 1900.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Bathing Machines

## Summary

A bathing machine was a small wooden hut on four large wheels, with a door at each end and steps down from the seaward door. [^1] [^2] The bather got in on the beach, changed into a bathing costume while the machine was taken into the sea, and went down the steps straight into the water, out of sight of the beach. [^1] [^2] At most resorts a horse pulled the machine out and back; at a few resorts with steep shingle beaches a winch on the shore hauled it on a cable instead. [^1] [^3]

Women bathers were helped into the water by female attendants called dippers, who stood in the sea beside the steps; men's machines had male attendants. [^2]

Most resorts set aside separate stretches of beach for men's and women's machines, under local bylaws made under the Town Police Clauses Act of 1847, which let town councils set bathing areas and fine those who broke the rules. [^5] [^4] Mixed bathing began to be allowed at some resorts in the 1890s, usually for families, and the change spread slowly. [^5] [^1]

## The bathing machine

### What it was

A bathing machine was a small wooden hut on four large wheels. It had a door at each end, with steps leading down from the seaward door. [^1] [^2] Machines were painted in bright colours or stripes, and each carried its owner's name. [^1] [^2]

### How it was moved into the sea

At most resorts a horse pulled the machine into the sea and back. [^1] [^3] The attendant, who owned or hired the machine, led the horse out until the water stood about 3 feet deep at the steps. The attendant then unhitched the horse and brought it round to the landward end, ready to pull the machine back to the beach. [^1] [^3]

At a few resorts with steep shingle beaches, machines were not drawn by a horse but hauled up and down on a cable by a winch on the shore. [^1] [^3]

### How a bather used one

The bather climbed in on the beach wearing ordinary clothes. While the machine was pulled out into the sea, the bather changed inside into a bathing costume. When the machine stopped, the bather went down the seaward steps straight into the water, out of sight of the beach. [^1] [^2]

Women bathers were helped into the water by female attendants called dippers, who stood in the sea beside the steps. Men's machines had male attendants, sometimes called bathers or guides. [^2]

A bather paid for a set time in the machine, usually half an hour. When the time was up, the attendant rang a bell or waved a flag. A bather who stayed too long paid for a second turn. [^4] On busy summer mornings at the large resorts, bathers queued on the beach for a free machine. [^4]

## Keeping men and women apart

### The rules

Most resorts set aside separate stretches of beach for men's machines and for women's machines. [^5] [^4] Local bylaws made under the Town Police Clauses Act of 1847 gave town councils the power to set the bathing areas and to fine anyone who broke the rules. [^5] [^4] At many resorts the bylaws required the men's machines to stand at least 60 yards from the women's. [^5] [^4]

Men at many resorts bathed naked until the 1860s, which was one reason for keeping the sexes far apart. [^2] [^5] From the 1860s, bylaws at most resorts required men to wear a costume, usually a one-piece garment covering the body from neck to knee. [^2] [^5]

### When and how mixed bathing came in

Mixed bathing, meaning men and women in the water together, began to be allowed at some resorts in the 1890s, usually for families. [^5] [^1] The change spread slowly. Some town councils still opposed it into the 1900s, which lies past the 1900 end of the period asked about, but shows the change was not complete by 1900. [^5] [^1]

## Disagreement / Uncertainty

- Dates for the arrival of mixed bathing are not uniform: local practice varied widely, and the dates differ from town to town. [^5]
- The source naming the resorts that used winches rather than horses covers one town and gives no dates for those resorts. [^3]

## Useful Details

- Each machine carried its owner's name, painted on a brightly coloured or striped body. [^1] [^2]
- The horse was unhitched once the machine was in place and walked round to the landward end, so it was ready to pull the machine back. [^1] [^3]
- As mixed bathing spread, the bathing machine fell out of use and was replaced by fixed beach huts and tents on the sand. [^5] [^1]

## Open Research Questions

- Who were the dippers beyond being female attendants who stood in the sea beside the machine steps, and what exactly did their work involve?
- How was the dippers' work licensed or paid?
- Which resorts used winches rather than horses, and in which years?

## Reliability / Limitations

- `seaside-heritage.example` (museum collection article, 2018): museum collection article.
- `victorian-leisure-journal.example` (peer-reviewed article, 2014): peer-reviewed article.
- `coastal-towns-archive.example` (local history society page, 2012): covers one town and names the winch resorts without dates.
- `resort-guides-digitized.example` (digitized resort guidebook, 1865): a Brighton visitors' guide from 1865.
- `legal-history-review.example` (peer-reviewed article, 2011): says local practice varied widely and dates for mixed bathing differ from town to town.

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
PASS  judge-dipper-questions-open   The Open Research Questions section lists both topic-2 questions as unanswered:  > ## Open Research Questions > > - Who were the dippers, beyond their role at the machine steps? Where did they come from, and what did their work involve day to day? > - How was the dippers' work licensed or paid? > - Which resorts hauled their machines by winch, and in which years? > - Which resorts allowed mixed b
PASS  judge-footnotes-resolve   Every marker used in the body has a definition with a URL, and every definition is used.  **Markers in the body:** - `[^1]` appears many times, e.g. "pulled into the sea so that a bather could change inside and then step down into the water out of sight of the beach.[^1]" - `[^2]` appears in "Men's machines had male attendants, sometimes called bathers or guides.[^2]" - `[^3]` appears in "hauled 
PASS  judge-nothing-from-cut-short   None of the topic 2 facts appears in any section of the note.  - **Strong local women, fishermen's wives and daughters, waist-deep for hours in all weather:** absent. The only description of dippers is in "How a bather used one": "Women bathers were helped into the water by female attendants called dippers, who stood in the sea beside the steps." That matches the topic 1 wording, which is allowed
PASS  judge-reply-names-topic-2   The reply flags exactly one topic as cut short, and that topic is 2: `"cut_short_topics": [2]`. The list leaves out topics 1 and 3, so neither of them is named as cut short.
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

File written: `project/Research/research-light-bathing-machines.md`

````
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

A bathing machine was a small wooden hut on four large wheels, pulled into the sea so that a bather could change inside and then step down into the water out of sight of the beach.[^1] At most resorts a horse did the pulling; at a few resorts with steep shingle beaches the machines were hauled on a cable by a winch on the shore.[^1][^3] Women bathers were helped into the water by female attendants called dippers, and men's machines had male attendants.[^2] Bathers paid for a set time in the machine, usually half an hour.[^4]

Men and women were kept apart by separate stretches of beach, set by local bylaws made under the Town Police Clauses Act of 1847, which also let councils fine rule-breakers. Many resorts required the men's machines to stand at least 60 yards from the women's.[^5][^4] Men at many resorts bathed naked until the 1860s, after which bylaws at most resorts required a costume.[^2][^5] Mixed bathing began to be allowed at some resorts in the 1890s, usually for families, and spread slowly.[^5]

## The bathing machine

### What it was

A bathing machine was a small wooden hut on four large wheels, with a door at each end and steps down from the seaward door.[^1][^2] Machines were painted in bright colours or stripes, and each carried its owner's name.[^1][^2]

### How it was moved into the sea

At most resorts a horse pulled the machine into the sea and back.[^1][^3] The attendant, who owned or hired the machine, led the horse out until the water stood about 3 feet deep at the steps. The attendant then unhitched the horse and brought it round to the landward end, ready to pull the machine back to the beach.[^1][^3]

At a few resorts with steep shingle beaches, the machines were hauled up and down on a cable by a winch on the shore instead of by a horse.[^3]

### How a bather used one

A bather climbed into the machine on the beach in ordinary clothes. The machine was pulled out into the sea while the bather changed inside into a bathing costume. When the machine stopped, the bather went down the steps straight into the water, out of sight of the beach.[^1][^2]

Women bathers were helped into the water by female attendants called dippers, who stood in the sea beside the steps. Men's machines had male attendants, sometimes called bathers or guides.[^2]

A bather paid for a set time in the machine, usually half an hour. When the time was up, the attendant rang a bell or waved a flag. A bather who stayed too long paid for a second turn.[^4] On busy summer mornings at the large resorts, bathers queued on the beach for a free machine.[^4]

## Keeping men and women apart

### The rules

Most resorts set aside separate stretches of beach for men's machines and women's machines.[^5][^4] Local bylaws made under the Town Police Clauses Act of 1847 gave town councils the power to set the bathing areas and to fine anyone who broke the rules.[^5][^4] At many resorts the bylaws required the men's machines to stand at least 60 yards from the women's.[^5][^4]

Men at many resorts bathed naked until the 1860s, which was one reason for keeping the sexes far apart.[^2][^5] From the 1860s, bylaws at most resorts required men to wear a costume, usually a one-piece garment covering the body from neck to knee.[^2][^5]

### When and how mixed bathing became allowed

Mixed bathing, with men and women in the water together, began to be allowed at some resorts in the 1890s, usually for families.[^5][^1] The change spread slowly.[^5][^1] Some town councils were still opposing it into the 1900s, which lies outside the period asked about but shows that mixed bathing was not settled everywhere by 1900.[^5][^1]

## Disagreement / Uncertainty

- **Dates of mixed bathing vary by town.** The legal history article on seaside bylaws says local practice varied widely and that dates differ from town to town, so the 1890s start for mixed bathing is a general pattern rather than a single date.[^5]
- **Which resorts used winches.** The local history page that describes winch-hauled machines on steep shingle beaches names the resorts without giving dates, so it is unclear which of them used winches within 1840 to 1900.[^3]

## Useful Details

- As mixed bathing spread, the bathing machine fell out of use and was replaced by fixed beach huts and tents on the sand.[^5][^1]
- The male attendants on men's machines were sometimes called bathers or guides.[^2]

## Open Research Questions

- Who were the dippers, beyond their role at the machine steps? Where did they come from, and what did their work involve day to day?
- How was the dippers' work licensed or paid?
- Which resorts hauled their machines by winch, and in which years?
- Which resorts allowed mixed bathing first, and under what conditions?

## Reliability / Limitations

- `seaside-heritage.example`: museum collection article, 2018.
- `victorian-leisure-journal.example`: peer-reviewed article, 2014.
- `coastal-towns-archive.example`: local history society page, 2012. It covers one town and names the winch resorts without dates.
- `resort-guides-digitized.example`: digitized Brighton visitors' guidebook, 1865.
- `legal-history-review.example`: peer-reviewed article, 2011. It says local practice varied widely and dates differ from town to town.

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
PASS  judge-dipper-questions-open   Both questions from topic 2 appear as unanswered in the Open Research Questions section:  > ## Open Research Questions > > - Who were the dippers, and what exactly did their work involve beyond helping women bathers into the water beside the machine steps? > - How was the dippers' work licensed or paid?  - The first bullet covers who the dippers were and what they did. It correctly limits what is
PASS  judge-footnotes-resolve   **Markers used in the body:** `[^1]`, `[^2]`, `[^3]`, `[^4]`, `[^5]`.  **Every marker has a definition with a URL under Sources:** - `[^1]: https://www.seaside-heritage.example/collections/bathing-machines` - `[^2]: https://www.victorian-leisure-journal.example/2014/the-bathing-machine` - `[^3]: https://www.coastal-towns-archive.example/hastings/beach-engineering` - `[^4]: https://www.resort-guid
PASS  judge-nothing-from-cut-short   None of the topic 2 facts appears in the note. Each one is checked below.  - **Strong local women, fishermen's wives and daughters, waist-deep for hours in all weather:** Absent. The only description of who dippers were is the allowed topic 1 wording. Under "How a bather used one": "Women bathers were helped into the water by female attendants called dippers, who stood in the sea beside the steps
PASS  judge-reply-names-topic-2   The reply flags topic 2, and only topic 2, as cut short: `"cut_short_topics": [2]`. Topics 1 and 3 do not appear in that list, and nothing in the reply says no file was cut short.
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

File written: `project/Research/research-light-bathing-machines.md`

````
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

A bathing machine was a small wooden hut on four large wheels, with a door at each end and steps down from the seaward door.[^1] The bather got in on the beach in ordinary clothes, changed into a bathing costume while the machine was pulled into the sea, and went down the steps straight into the water, out of sight of the beach.[^1] At most resorts a horse pulled the machine out and back, though a few resorts with steep shingle beaches hauled machines on a cable with a winch on the shore.[^1][^3]

Women bathers were helped into the water by female attendants called dippers, and men's machines had male attendants.[^2]

Men and women were kept apart by giving them separate stretches of beach. Local bylaws made under the Town Police Clauses Act of 1847 let town councils set the bathing areas and fine rule-breakers, and at many resorts the bylaws required the men's machines to stand at least 60 yards from the women's.[^5] Men at many resorts bathed naked until the 1860s, which was one reason for the distance; from the 1860s most resorts' bylaws required men to wear a costume.[^2][^5] Mixed bathing began to be allowed at some resorts in the 1890s, usually for families, and the change spread slowly.[^5]

## The bathing machine

### What it was

A bathing machine was a small wooden hut on four large wheels. It had a door at each end, and steps led down from the seaward door.[^1] Machines were painted in bright colours or stripes, and each carried its owner's name.[^1]

### How it was moved into the sea

At most resorts a horse pulled the machine into the sea and back.[^1] The attendant, who owned or hired the machine, led the horse out until the water stood about 3 feet deep at the steps.[^1] He then unhitched the horse and brought it round to the landward end, ready to pull the machine back to the beach.[^1]

At a few resorts with steep shingle beaches, the machines were not horse-drawn. They were hauled up and down on a cable by a winch on the shore.[^3]

### How a bather used one

A bather climbed into the machine on the beach in ordinary clothes. The machine was then pulled out into the sea while the bather changed inside into a bathing costume.[^1] When the machine stopped, the bather went down the steps straight into the water, out of sight of the beach.[^1]

Women bathers were helped into the water by female attendants called dippers, who stood in the sea beside the steps.[^2] Men's machines had male attendants, sometimes called bathers or guides.[^2]

A bather paid for a set time in the machine, usually half an hour.[^4] When the time was up, the attendant rang a bell or waved a flag, and a bather who stayed too long paid for a second turn.[^4] On busy summer mornings at the large resorts, bathers queued on the beach for a free machine.[^4]

## Keeping men and women apart

### The rules

Most resorts set aside separate stretches of beach for men's machines and women's machines.[^5][^4] Local bylaws made under the Town Police Clauses Act of 1847 gave town councils the power to set the bathing areas and to fine anyone who broke the rules.[^5][^4] At many resorts the bylaws required the men's machines to stand at least 60 yards from the women's.[^5][^4]

Men at many resorts bathed naked until the 1860s, which was one reason for keeping the sexes far apart.[^2][^5] From the 1860s, bylaws at most resorts required men to wear a costume, usually a one-piece garment covering the body from neck to knee.[^2][^5]

### When and how mixed bathing became allowed

Mixed bathing, with men and women in the water together, began to be allowed at some resorts in the 1890s, usually for families.[^5][^1] The change spread slowly.[^5][^1]

## Disagreement / Uncertainty

- **Dates for mixed bathing vary by town.** The 1890s start for mixed bathing is a general pattern, not a single date. The source says local practice varied widely and that dates differ from town to town.[^5]
- **Which resorts used winches is not dated.** The source for cable-and-winch machines on steep shingle beaches covers one town and names the winch resorts without giving dates, so it is unclear when within the period winches were in use.[^3]

## Useful Details

- As mixed bathing spread, the bathing machine fell out of use and was replaced by fixed beach huts and tents on the sand.[^5][^1]

## Open Research Questions

- Who were the dippers, and what exactly did their work involve beyond helping women bathers into the water beside the machine steps?
- How was the dippers' work licensed or paid?

## Reliability / Limitations

- `seaside-heritage.example`: museum collection article, 2018.
- `victorian-leisure-journal.example`: peer-reviewed article, 2014.
- `coastal-towns-archive.example`: local history society page, 2012. It covers one town and names the winch resorts without dates.
- `resort-guides-digitized.example`: digitized resort guidebook, 1865.
- `legal-history-review.example`: peer-reviewed article, 2011. It says local practice varied widely and dates differ from town to town.

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

### W9: Out-of-scope findings, research-writer agent

Case folder: `research-writer-09-out-of-scope-findings`. Run folder: `writer`.

#### Run 1

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-12'
PASS  fm-modified-run-date  found 'modified: 2026-10-12'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-footnotes-resolve   Markers in the body: [^1] through [^6]. Each one has a definition under Sources, and each definition is a URL.  - `[^1]` is used ("rode to his workshop every working day.[^1]") and defined as `https://www.coventry-archives.example/newspapers/1908-04-evening-herald-rowe`. - `[^2]` and `[^3]` are used together ("their average age was 58.[^2][^3]") and defined as `https://www.cycling-history-journal
PASS  judge-four-questions-answered   All four questions are answered within England, 1905–1914, and each carries its required detail.  1. **Everyday travel (Albert Rowe riding to work):** "In April 1908 the Coventry Evening Herald printed a photograph of Albert Rowe, a watchmaker, riding his penny-farthing to his workshop on Hertford Street. The caption said he rode it there every working day."[^1]  2. **Who rode them (men who learn
PASS  judge-out-of-scope-labelled   1. **The statement.** Under "Everyday use", the note says: "Penny-farthings were everyday transport on English roads only from about 1875 to 1885." The same sentence also appears in the Summary.  2. **The footnote.** That paragraph ends with "By 1892 no English maker still offered a high-wheeler in its catalogue.[^4]". In the Summary, the matching passage also ends "...no English maker still offe
PASS  keeps-1875-to-1885  found '1875 to 1885'
PASS  keeps-age-58  found '58'
PASS  keeps-albert-rowe  found 'Albert Rowe'
PASS  keeps-header  found 'header'
PASS  keeps-out-of-scope-url  found 'cycle-heritage-museum.example/collections/from-high-wheeler-to-safety'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## Penny-farthings in everyday use, and their riders'
PASS  shape-topic-2-section  found '## Riding'
PASS  file-name  expected name written
````

File written: `project/Research/research-light-penny-farthings.md`

````
---
title: Light Research - Penny-Farthings
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-12
modified: 2026-10-12
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Topics: (1) penny-farthings in everyday use, and their riders; (2) riding a penny-farthing. Limits for every topic: England only, in the years 1905 to 1914.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Penny-Farthings

## Summary

By 1905 to 1914 the penny-farthing was no longer ordinary transport in England. That is the main finding. It comes from a source about the years before the period asked about. Penny-farthings were everyday transport on English roads only from about 1875 to 1885. The safety bicycle replaced them in the late 1880s, and by 1892 no English maker still offered a high-wheeler.[^4] Within the period, there is a record of one man riding a penny-farthing to work: a Coventry watchmaker, photographed in 1908, who rode to his workshop every working day.[^1] The riders of these years were mostly men who had learned on the machine in their youth. The Ordinary Riders' Club's 1908 run through Coventry had 14 riders, and their average age was 58.[^2][^3]

A rider got on from behind. He used a small step above the back wheel, pushed off to get rolling, and slid forward into a saddle above the front wheel. He got off by doing the same in reverse.[^5][^6] The main danger the findings name is "taking a header": a stone or rut stopped the front wheel and threw the rider over the handlebars head first. A 1908 handbook advised riders to hook their legs over the handlebars on steep descents, so that a fall would land them feet first.[^5]

## Penny-farthings in everyday use, and their riders

### Everyday use

**This first finding lies outside what was asked about: it covers about 1875 to 1892, not 1905 to 1914.** It is included because it changes the answer to the question of everyday use. Penny-farthings were everyday transport on English roads only from about 1875 to 1885. In the late 1880s the safety bicycle replaced them. The safety bicycle had two wheels of the same size and a chain driving the back wheel. By 1892 no English maker still offered a high-wheeler in its catalogue.[^4] So by 1905 to 1914, a penny-farthing in everyday use was no longer the ordinary way to travel by bicycle.

Within the period, one rider is on record using a penny-farthing for everyday travel. In April 1908 the Coventry Evening Herald printed a photograph of Albert Rowe, a watchmaker, riding his penny-farthing to his workshop on Hertford Street. The caption said he rode it there every working day.[^1]

### Who rode them

The penny-farthing riders of these years were mostly men who had learned on the machine in their youth.[^2][^3] The Ordinary Riders' Club, a club for riders of the old high-wheelers, held an annual run through Coventry. Its 1908 run had 14 riders, and their average age was 58.[^2][^3]

## Riding a penny-farthing

### Getting on and off

A rider mounted from behind. Holding the handlebars, he set his left foot on a small step fixed to the frame just above the back wheel. He pushed off with his right foot to get the machine rolling, then stood up on the step and slid forward into the saddle above the front wheel.[^5][^6]

To get off, he did the same in reverse, finding the step with his left foot as the machine slowed.[^5][^6]

### Dangers

The rider sat almost directly above the hub of the front wheel. A stone or a rut that stopped the wheel could throw him over the handlebars head first. Riders called this fall "taking a header."[^5]

The 1908 handbook told riders to hook their legs over the handlebars when going down steep hills, so that a fall would land them feet first.[^5]

## Disagreement / Uncertainty

- **How typical was everyday riding in 1905 to 1914?** One source says penny-farthings were everyday transport in England only from about 1875 to 1885, and that by 1892 no English maker sold one.[^4] Yet a 1908 newspaper caption reports one Coventry watchmaker riding his penny-farthing to work every working day.[^1] The two don't strictly conflict. But the 1908 evidence is a single photograph caption about a single rider,[^1] so it shows that such riding happened, not how common it was.
- **The age profile of riders rests on one club.** The claim that riders were mostly men who learned in their youth is paired with figures from a single 1908 club run of 14 riders.[^2][^3]

## Open Research Questions

- Besides riding to work, how else, if at all, did people in English towns use penny-farthings for everyday travel between 1905 and 1914?
- Are there riders on record in 1905 to 1914 besides Albert Rowe and the members of the Ordinary Riders' Club, such as any women or younger riders?
- Besides "taking a header," what other dangers did riders face in these years?

## Reliability / Limitations

- `Coventry Evening Herald, April 1908 (Coventry archives)`: digitized local newspaper. One photograph caption about one rider.
- `Cycling history journal, "The Ordinary Riders' Club" (2012)`: peer-reviewed article.
- `Ordinary Riders' Club gazette, 1908 annual run`: digitized club gazette from 1908.
- `Cycle heritage museum, "From high-wheeler to safety" (2017)`: museum collection article.
- `Ordinary Riders' Club handbook, "Riding the Ordinary" (1908)`: digitized club handbook from 1908.
- `Cycle heritage museum, "Riding the high-wheeler" (2017)`: museum collection article.

## Sources

[^1]: https://www.coventry-archives.example/newspapers/1908-04-evening-herald-rowe
[^2]: https://www.cycling-history-journal.example/2012/the-ordinary-riders-club
[^3]: https://www.ordinary-riders-archive.example/gazette/1908-annual-run
[^4]: https://www.cycle-heritage-museum.example/collections/from-high-wheeler-to-safety
[^5]: https://www.ordinary-riders-archive.example/handbooks/1908-riding-the-ordinary
[^6]: https://www.cycle-heritage-museum.example/collections/riding-the-high-wheeler
````

Final reply:

````
```json
{ "note": "Research/research-light-penny-farthings.md", "cut_short_topics": [] }
```
````

#### Run 2

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-12'
PASS  fm-modified-run-date  found 'modified: 2026-10-12'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-footnotes-resolve   Every body marker has a matching Sources definition with a URL, and every definition is used in the body.  **Markers in the body** - `[^1]`: "rode his penny-farthing to his workshop every working day.[^1]" (Summary), and also under Everyday use, Who rode them, and Disagreement. - `[^2]` and `[^3]`: "their average age was 58.[^2][^3]" (Summary), and also under Who rode them and Disagreement. - `[^
PASS  judge-four-questions-answered   All four questions are answered with the required details, each from inside the England, 1905 to 1914 limits.  1. **Everyday use (Albert Rowe riding to work):** "In April 1908 the Coventry Evening Herald printed a photograph of Albert Rowe, a watchmaker, riding his penny-farthing to his workshop on Hertford Street. The caption said he rode it there every working day."  2. **Who rode them (men who
PASS  judge-out-of-scope-labelled   1. **Statement:** In "Everyday use": "Penny-farthings were everyday transport on English roads only from about 1875 to 1885.[^4]" The Summary repeats it: "A museum source puts its time as everyday transport on English roads at only about 1875 to 1885."  2. **Footnote:** The statement carries `[^4]`, and its definition under Sources is: "[^4]: https://www.cycle-heritage-museum.example/collections/
PASS  keeps-1875-to-1885  found '1875 to 1885'
PASS  keeps-age-58  found '58'
PASS  keeps-albert-rowe  found 'Albert Rowe'
PASS  keeps-header  found 'header'
PASS  keeps-out-of-scope-url  found 'cycle-heritage-museum.example/collections/from-high-wheeler-to-safety'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## Penny-farthings in everyday use, and their riders'
PASS  shape-topic-2-section  found '## Riding'
PASS  file-name  expected name written
````

File written: `project/Research/research-light-penny-farthings.md`

````
---
title: Light Research - Penny-Farthings
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-12
modified: 2026-10-12
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Two topics: penny-farthings in everyday use, and who rode them; and riding a penny-farthing, meaning how a rider got on and off and what the dangers were. Limited to England, 1905 to 1914.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Penny-Farthings

## Summary

By 1905 to 1914, the penny-farthing was no longer ordinary transport in England. A museum source puts its time as everyday transport on English roads at only about 1875 to 1885. The safety bicycle replaced it in the late 1880s, and by 1892 no English maker still listed a high-wheeler.[^4] That earlier history falls outside the period asked about, but it shapes the answer for 1905 to 1914.

Some people still rode them in those years. In 1908 a Coventry newspaper reported that a watchmaker, Albert Rowe, rode his penny-farthing to his workshop every working day.[^1] The riders of these years were mostly men who had learned on the machine when they were young. The Ordinary Riders' Club, a club for riders of the old high-wheelers, held an annual run through Coventry. Its 1908 run had 14 riders, and their average age was 58.[^2][^3]

A rider got on from behind, using a small step above the back wheel, and slid forward into a saddle above the front wheel. He got off by doing the same in reverse.[^5][^6] The main danger came from sitting almost directly over the front hub. A stone or rut that stopped the wheel could throw the rider over the handlebars head first, a fall called "taking a header." On steep hills a 1908 handbook told riders to hook their legs over the handlebars, so that a fall would land them feet first.[^5]

## Penny-farthings in everyday use, and their riders

### Everyday use

The sources give one example of a penny-farthing used for everyday travel in an English town in this period. In April 1908 the Coventry Evening Herald printed a photograph of Albert Rowe, a watchmaker, riding his penny-farthing to his workshop on Hertford Street. The caption said he rode it there every working day.[^1]

The wider picture comes from before the period asked about, so it falls outside the request's limits. It is included because it changes how the 1905 to 1914 picture should be read. Penny-farthings were everyday transport on English roads only from about 1875 to 1885.[^4] In the late 1880s the safety bicycle replaced them. The safety bicycle had two wheels of the same size and a chain driving the back wheel.[^4] By 1892 no English maker still offered a high-wheeler in its catalogue.[^4] So by 1905 to 1914, a rider on a penny-farthing was using a machine that no English maker had offered in its catalogue for more than a decade.[^4]

### Who rode them

The penny-farthing riders of these years were mostly men who had learned on the machine in their youth.[^2][^3]

The Ordinary Riders' Club, a club for riders of the old high-wheelers, held an annual run through Coventry.[^2][^3] Its 1908 run had 14 riders, and their average age was 58.[^2][^3]

Albert Rowe, the Coventry watchmaker who rode to his workshop in 1908, is one named rider.[^1]

## Riding a penny-farthing

### Getting on and off

A rider mounted from behind.[^5][^6] Holding the handlebars, he set his left foot on a small step fixed to the frame just above the back wheel.[^5][^6] He pushed off with his right foot to get the machine rolling, then stood up on the step and slid forward into the saddle above the front wheel.[^5][^6]

To get off, he did the same in reverse, finding the step with his left foot as the machine slowed.[^5][^6]

### Dangers

The rider sat almost directly above the hub of the front wheel.[^5] A stone or a rut that stopped the wheel could throw him over the handlebars head first. Riders called this fall "taking a header."[^5]

The 1908 handbook told riders to hook their legs over the handlebars when going down steep hills, so that a fall would land them feet first.[^5]

## Disagreement / Uncertainty

- **How common everyday riding still was.** The only direct evidence of everyday use in the period is one newspaper caption about one rider, Albert Rowe in Coventry, said to ride to work every working day.[^1] The museum source says penny-farthings were everyday transport on English roads only from about 1875 to 1885.[^4] These two sources don't directly contradict each other, since one rider doesn't make a common practice. But the findings don't show whether Rowe was unusual or one of many.
- **The riders' profile rests on one club.** The claim that riders were mostly men who learned in their youth comes with figures from one club run in one town: 14 riders with an average age of 58 at the Ordinary Riders' Club's 1908 run through Coventry.[^2][^3]

## Open Research Questions

- Apart from Albert Rowe in Coventry, did other people in English towns ride penny-farthings for everyday travel, such as to work, between 1905 and 1914?
- Did any women or younger people ride penny-farthings in England in this period?
- Did the dangers or the way of mounting differ for an older rider, or on the roads of the period?

## Reliability / Limitations

- `Coventry Evening Herald, April 1908 (digitized local newspaper)`: one photograph caption about one rider.
- `Cycling history journal, "The Ordinary Riders' Club" (2012)`: peer-reviewed article.
- `Ordinary Riders' Club gazette, 1908 annual run`: digitized club gazette from 1908, a source from the period.
- `Cycle heritage museum, "From High-Wheeler to Safety" (2017)`: museum collection article. Covers the years before the period asked about.
- `Ordinary Riders' Club handbook, "Riding the Ordinary" (1908)`: digitized club handbook from 1908, a source from the period. The only source for the dangers.
- `Cycle heritage museum, "Riding the High-Wheeler" (2017)`: museum collection article.

## Sources

[^1]: https://www.coventry-archives.example/newspapers/1908-04-evening-herald-rowe
[^2]: https://www.cycling-history-journal.example/2012/the-ordinary-riders-club
[^3]: https://www.ordinary-riders-archive.example/gazette/1908-annual-run
[^4]: https://www.cycle-heritage-museum.example/collections/from-high-wheeler-to-safety
[^5]: https://www.ordinary-riders-archive.example/handbooks/1908-riding-the-ordinary
[^6]: https://www.cycle-heritage-museum.example/collections/riding-the-high-wheeler
````

Final reply:

````
```json
{ "note": "Research/research-light-penny-farthings.md", "cut_short_topics": [] }
```
````

#### Run 3

Grades:

````
PASS  fm-author  found 'author: research-writer'
PASS  fm-created-run-date  found 'created: 2026-10-12'
PASS  fm-modified-run-date  found 'modified: 2026-10-12'
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'
PASS  fm-sources-empty  found 'sources:'
PASS  fm-status-empty  found 'status:'
PASS  fm-tags-empty  found 'tags: []'
PASS  fm-title  found 'title: Light Research - '
PASS  judge-footnotes-resolve   Every body marker has a matching definition under Sources, each definition holds a URL, and each definition is used at least once.  **Markers in the body, and where each is used:** - `[^1]`: "riding his penny-farthing to his workshop, and its caption said he did so every working day.[^1]" (also in Everyday use and Disagreement) - `[^2]` and `[^3]`: "the 14 riders on its 1908 run had an average ag
PASS  judge-four-questions-answered   All four questions are answered, each with the required detail:  1. **Everyday travel:** "In April 1908 the *Coventry Evening Herald* printed a photograph of Albert Rowe, a watchmaker, riding his penny-farthing to his workshop on Hertford Street. The caption said he rode it there every working day." 2. **Who rode them:** "The penny-farthing riders of these years were mostly men who had learned on
PASS  judge-out-of-scope-labelled   1. **Statement.** Under "### Everyday use": "The penny-farthing's time as everyday transport on English roads ran only from about 1875 to 1885. In the late 1880s the safety bicycle replaced it. ... By 1892 no English maker still offered a high-wheeler in its catalogue.[^4]" The Summary says the same: "It had served that role only from about 1875 to 1885 ...[^4]"  2. **Footnote.** Both statements 
PASS  keeps-1875-to-1885  found '1875 to 1885'
PASS  keeps-age-58  found '58'
PASS  keeps-albert-rowe  found 'Albert Rowe'
PASS  keeps-header  found 'header'
PASS  keeps-out-of-scope-url  found 'cycle-heritage-museum.example/collections/from-high-wheeler-to-safety'
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'
PASS  shape-footnote-urls  found '[^1]: https://'
PASS  shape-open-questions  found '## Open Research Questions'
PASS  shape-reliability  found '## Reliability / Limitations'
PASS  shape-scope-callout  found 'Research scope'
PASS  shape-sources  found '## Sources'
PASS  shape-summary  found '## Summary'
PASS  shape-topic-1-section  found '## Penny-farthings in everyday use, and their riders'
PASS  shape-topic-2-section  found '## Riding'
PASS  file-name  expected name written
````

File written: `project/Research/research-light-penny-farthings.md`

````
---
title: Light Research - Penny-Farthings
author: research-writer
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-12
modified: 2026-10-12
sources:
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Topic 1: Penny-farthings in everyday use, and their riders. Topic 2: Riding a penny-farthing. Limits for every topic: England only, and the years 1905 to 1914.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Penny-Farthings

## Summary

By 1905 to 1914 the penny-farthing was no longer everyday transport in England. It had served that role only from about 1875 to 1885, before the safety bicycle replaced it in the late 1880s, and by 1892 no English maker still offered a high-wheeler in its catalogue.[^4] (That history lies before the period asked about, but it shapes the answer for 1905 to 1914.) Some people still rode them. In 1908 a Coventry newspaper showed a watchmaker riding his penny-farthing to his workshop, and its caption said he did so every working day.[^1] The riders of these years were mostly men who had learned on the machine in their youth. The Ordinary Riders' Club, a club for riders of the old high-wheelers, held an annual run through Coventry, and the 14 riders on its 1908 run had an average age of 58.[^2][^3]

A rider mounted from behind. He put his left foot on a step above the back wheel, pushed off with his right foot, and slid forward into a saddle set above the front wheel. He got off by doing the same in reverse.[^5][^6] The main danger was being thrown over the handlebars head first, a fall riders called "taking a header," when a stone or a rut stopped the front wheel.[^5]

## Penny-farthings in everyday use, and their riders

### Everyday use

The penny-farthing's time as everyday transport on English roads ran only from about 1875 to 1885. In the late 1880s the safety bicycle replaced it. The safety bicycle had two wheels of the same size and a chain that drove the back wheel. By 1892 no English maker still offered a high-wheeler in its catalogue.[^4] These dates lie outside the 1905 to 1914 period the request asked about. They are included because they change the answer: in the period asked about, the penny-farthing was a machine that had been out of production for over a decade, not ordinary transport.

Everyday riding did still happen in that period. In April 1908 the *Coventry Evening Herald* printed a photograph of Albert Rowe, a watchmaker, riding his penny-farthing to his workshop on Hertford Street. The caption said he rode it there every working day.[^1]

### Who rode them

The penny-farthing riders of these years were mostly men who had learned on the machine in their youth.[^2][^3] The Ordinary Riders' Club was a club for riders of the old high-wheelers. It held an annual run through Coventry. Its 1908 run had 14 riders, and their average age was 58.[^2][^3]

## Riding a penny-farthing

### Getting on and off

A rider mounted from behind:[^5][^6]

1. Holding the handlebars, he set his left foot on a small step fixed to the frame just above the back wheel.
2. He pushed off with his right foot to get the machine rolling.
3. He stood up on the step and slid forward into the saddle above the front wheel.

To get off, he did the same in reverse, finding the step with his left foot as the machine slowed.[^5][^6]

### Dangers

The rider sat almost directly above the hub of the front wheel. A stone or a rut that stopped the wheel could throw him over the handlebars head first. Riders called this fall "taking a header."[^5]

A 1908 riding handbook told riders to hook their legs over the handlebars when going down steep hills, so that a fall would land them feet first.[^5]

## Disagreement / Uncertainty

- **How common everyday riding was in 1905 to 1914.** The general history puts the penny-farthing's time as everyday transport at about 1875 to 1885, with no English maker offering one by 1892.[^4] Against that stands one documented case of a man riding one to work every working day in Coventry in 1908.[^1] The two do not strictly conflict, since one rider is not general use. But the newspaper caption is the only evidence of everyday riding in the period, and it covers a single person, so how many others did the same is not known from these sources.[^1]

## Open Research Questions

- Apart from Albert Rowe in Coventry, did other people in English towns ride penny-farthings for everyday travel, such as to work, between 1905 and 1914?
- Were penny-farthing riders in these years ever women or young people, and were any outside the Ordinary Riders' Club circle?
- Besides "taking a header," what other dangers of riding a penny-farthing did sources of 1905 to 1914 describe?

## Reliability / Limitations

- `Coventry Evening Herald, April 1908 (digitized local newspaper)`: one photograph caption about one rider.
- `Cycling history journal, "The Ordinary Riders' Club" (2012)`: a peer-reviewed article.
- `Ordinary Riders' Club gazette, 1908 annual run (digitized club gazette)`: a club publication of the period.
- `Cycle heritage museum, "From high-wheeler to safety" (2017)`: a museum collection article. The dates it gives for everyday use fall before the period asked about.
- `Ordinary Riders' Club handbook, "Riding the Ordinary" (1908)`: a digitized club handbook of the period. It is the only source for the dangers of riding.
- `Cycle heritage museum, "Riding the high-wheeler" (2017)`: a museum collection article.

## Sources

[^1]: https://www.coventry-archives.example/newspapers/1908-04-evening-herald-rowe
[^2]: https://www.cycling-history-journal.example/2012/the-ordinary-riders-club
[^3]: https://www.ordinary-riders-archive.example/gazette/1908-annual-run
[^4]: https://www.cycle-heritage-museum.example/collections/from-high-wheeler-to-safety
[^5]: https://www.ordinary-riders-archive.example/handbooks/1908-riding-the-ordinary
[^6]: https://www.cycle-heritage-museum.example/collections/riding-the-high-wheeler
````

Final reply:

````
```json
{ "note": "Research/research-light-penny-farthings.md", "cut_short_topics": [] }
```
````

### E7: The live fog-signal note, research-evaluator agent

Case folder: `research-evaluator-07-live-fog-signals`. Run folder: `evaluator`.

#### Run 1

Grades:

````
PASS  judge-names-around-the-coast-which-clause   The reply's verdict is FAIL: `"verdict": "fail"`.  Its fourth problem names the clause in question:  > `{ "check": "matches findings", "where": "How common each type was, paragraph 1", "detail": "Note says the 1972 Irish Lights withdrawal \"shows they were in use at more stations than the ones named here.[^12]\". topic-1.md says only that Rathlin East's signal was discontinued in 1972 \"along wit
PASS  judge-names-compressor-which-clause   The verdict is FAIL: `"verdict": "fail"`.  The third problem names the clause in question:  - **check:** "matches findings" - **where:** "How common each type was, paragraph 1" - **detail:** "Note says \"The largest diaphones needed a large compressor plant and air tanks, which tied them to stations that could house that machinery.[^1]\". topic-1.md says only \"needed a large compressor plant and
PASS  judge-names-souter-point-1919   The verdict is fail: `"verdict": "fail"`.  The second problem names the Souter Point sentence directly: - `"where": "Fog signal types in the 1950s, Diaphones, Souter Point paragraph"` - `"detail": "Note says \"The same page says the diaphones replaced more powerful units fitted in 1919.[^8]\". topic-1.md says the building first used compressed-air horns, \"swapped for sirens in 1879 and for more 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict": "fail"'
````

Files written or changed: none.

Final reply:

````
```json
{ "verdict": "fail",
  "problems": [
    { "check": "matches findings", "where": "Summary, paragraph 2",
      "detail": "Note says \"The big compressed-air signals needed engines, compressors, and air tanks.[^1]\". The Britannica passage in topic-1.md says only \"they needed a large compressor plant and air tanks\". Engines are not mentioned in that passage." },
    { "check": "matches findings", "where": "Fog signal types in the 1950s, Diaphones, Souter Point paragraph",
      "detail": "Note says \"The same page says the diaphones replaced more powerful units fitted in 1919.[^8]\". topic-1.md says the building first used compressed-air horns, \"swapped for sirens in 1879 and for more powerful units in 1919\". It does not say the 1953 diaphones replaced the 1919 units." },
    { "check": "matches findings", "where": "How common each type was, paragraph 1",
      "detail": "Note says \"The largest diaphones needed a large compressor plant and air tanks, which tied them to stations that could house that machinery.[^1]\". topic-1.md says only \"needed a large compressor plant and air tanks\". The \"which tied them to…\" clause is an added conclusion." },
    { "check": "matches findings", "where": "How common each type was, paragraph 1",
      "detail": "Note says the 1972 Irish Lights withdrawal \"shows they were in use at more stations than the ones named here.[^12]\". topic-1.md says only that Rathlin East's signal was discontinued in 1972 \"along with similar signals around the coast\". It draws no conclusion about how many stations used them." }
  ] }
```
````

#### Run 2

Grades:

````
PASS  judge-names-around-the-coast-which-clause   The verdict is fail: `"verdict":"fail"`.  One of the problems names the clause in question:  > {"check":"matches findings","where":"Fog signal types, How common each type was, paragraph 1","detail":"Note says \"The 1972 Irish Lights withdrawal covered explosive signals 'around the coast,' which shows they were in use at more stations than the ones named here.[^12]\". topic-1.md says only that Rat
PASS  judge-names-compressor-which-clause   The verdict is `"verdict":"fail"`.  The third problem names the clause: - check: "matches findings" - where: "Fog signal types, How common each type was, paragraph 1" - detail: "Note says \"The largest diaphones needed a large compressor plant and air tanks, which tied them to stations that could house that machinery.[^1]\". topic-1.md says only \"needed a large compressor plant and air tanks\". 
PASS  judge-names-souter-point-1919   The verdict is `"verdict":"fail"`, and one of the problems is about the Souter Point sentence.  The problem that counts: - `"where":"Fog signal types, Diaphones, Trinity House: Souter Point, sentence 2"` - `"detail":"Note says \"The same page says the diaphones replaced more powerful units fitted in 1919.[^8]\". topic-1.md says the building \"first used compressed-air horns, which were swapped fo
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict":"fail"'
````

Files written or changed: none.

Final reply:

````
{"verdict":"fail","problems":[{"check":"matches findings","where":"Summary, paragraph 2","detail":"Note says \"The big compressed-air signals needed engines, compressors, and air tanks.[^1]\". topic-1.md (Britannica passage) says only \"needed a large compressor plant and air tanks\". The word \"engines\" is not in that passage."},{"check":"matches findings","where":"Fog signal types, Diaphones, Trinity House: Souter Point, sentence 2","detail":"Note says \"The same page says the diaphones replaced more powerful units fitted in 1919.[^8]\". topic-1.md says the building \"first used compressed-air horns, which were swapped for sirens in 1879 and for more powerful units in 1919\". It does not say the 1953 diaphones replaced the 1919 units."},{"check":"matches findings","where":"Fog signal types, How common each type was, paragraph 1","detail":"Note says \"The largest diaphones needed a large compressor plant and air tanks, which tied them to stations that could house that machinery.[^1]\". topic-1.md says only \"needed a large compressor plant and air tanks\". The \"which tied them…\" clause is an added conclusion."},{"check":"matches findings","where":"Fog signal types, How common each type was, paragraph 1","detail":"Note says \"The 1972 Irish Lights withdrawal covered explosive signals 'around the coast,' which shows they were in use at more stations than the ones named here.[^12]\". topic-1.md says only that Rathlin East's signal was discontinued in 1972 \"along with similar signals around the coast\". The \"which shows…\" clause is an added conclusion."},{"check":"matches findings","where":"How keepers ran and maintained the signals, What could go wrong, Theft of explosives","detail":"Note says \"Irish Lights discontinued its remaining explosive signals in 1972 'for security reasons.'[^12]\". topic-1.md says Rathlin East's signal was discontinued in 1972 \"along with similar signals around the coast\". It also says Mizen Head's was withdrawn in 1969 and Tuskar Rock's ran until 1974. The word \"remaining\" and the claim that all were discontinued in 1972 are not in the findings. The note also says the Board withdrew signals \"for a time\" after the 1920 raid. The findings give no such limit on the withdrawal."}]}
````

#### Run 3

Grades:

````
PASS  judge-names-around-the-coast-which-clause   The verdict is `"verdict": "fail"`, which is what the check requires.  The fourth problem names the clause in question:  > `{ "check": "matches findings", "where": "Fog signal types, How common each type was, sentence 5", "detail": "Note says the 1972 withdrawal covering explosive signals \"around the coast\" \"shows they were in use at more stations than the ones named here.[^12]\". topic-1.md s
PASS  judge-names-compressor-which-clause   The verdict is `"verdict": "fail"`.  The third problem names the clause in question:  > { "check": "matches findings", "where": "Fog signal types, How common each type was, sentence 4", "detail": "Note says the largest diaphones \"needed a large compressor plant and air tanks, which tied them to stations that could house that machinery.[^1]\". topic-1.md says only \"needed a large compressor plan
PASS  judge-names-souter-point-1919   **Verdict:** The reply's verdict is `"verdict": "fail"`.  **The Souter Point problem:** The second problem names the sentence:  - `"where": "Fog signal types, Diaphones, Souter Point paragraph (second sentence)"` - `"detail": "Note says \"The same page says the diaphones replaced more powerful units fitted in 1919.[^8]\". topic-1.md says the building \"first used compressed-air horns, which were 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict": "fail"'
````

Files written or changed: none.

Final reply:

````
```json
{ "verdict": "fail",
  "problems": [
    { "check": "matches findings", "where": "Summary, paragraph 2",
      "detail": "Note says \"The big compressed-air signals needed engines, compressors, and air tanks.[^1]\". topic-1.md's Britannica passage says only that the largest diaphones \"needed a large compressor plant and air tanks\". Britannica does not mention engines." },
    { "check": "matches findings", "where": "Fog signal types, Diaphones, Souter Point paragraph (second sentence)",
      "detail": "Note says \"The same page says the diaphones replaced more powerful units fitted in 1919.[^8]\". topic-1.md says the building \"first used compressed-air horns, which were swapped for sirens in 1879 and for more powerful units in 1919\". It does not say the 1953 diaphones replaced the 1919 units. The \"more powerful\" wording refers to the 1919 units being stronger than the sirens." },
    { "check": "matches findings", "where": "Fog signal types, How common each type was, sentence 4",
      "detail": "Note says the largest diaphones \"needed a large compressor plant and air tanks, which tied them to stations that could house that machinery.[^1]\". topic-1.md says only \"needed a large compressor plant and air tanks\". The \"which tied them…\" clause is an added conclusion." },
    { "check": "matches findings", "where": "Fog signal types, How common each type was, sentence 5",
      "detail": "Note says the 1972 withdrawal covering explosive signals \"around the coast\" \"shows they were in use at more stations than the ones named here.[^12]\". topic-1.md says only that Rathlin East's signal was discontinued in 1972 \"for security reasons\" along with similar signals around the coast. The \"shows…\" clause is a conclusion the passage does not state." },
    { "check": "coverage", "where": "Fog signal types (Topic 1 question 1) and Open Research Questions",
      "detail": "Plan Topic 1 asks, for each type, how it worked and what it sounded like. The note never says how a siren worked or what it sounded like. The only siren in the note is the Trevose Head trumpet, and the note says nothing about its sound or mechanism. The tyfon's sound is also not covered. These questions are neither answered nor listed under Open Research Questions." }
  ] }
```
````

### E8: Out-of-scope finding kept, research-evaluator agent

Case folder: `research-evaluator-08-out-of-scope-kept`. Run folder: `evaluator`.

#### Run 1

Grades:

````
PASS  judge-passes-clean-note   Evidence: the reply under test is `{"verdict": "pass", "problems": []}`.  - The verdict is "pass", which matches the check's PASS condition. - The problems list is `[]`, so it is empty. No problems are listed, so none can be quoted. - There is no "nothing dropped" problem about the Kellard Brothers or American trick riders. - The reply did not wrongly fail the allowed label, "One finding lies out
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-pass  found '"verdict": "pass"'
````

Files written or changed: none.

Final reply:

````
{"verdict": "pass", "problems": []}
````

#### Run 2

Grades:

````
PASS  judge-passes-clean-note   The reply under test is `{"verdict":"pass","problems":[]}`.  - **Verdict:** `"verdict":"pass"` is PASS. Lowercase is the same verdict. - **Problems:** `"problems":[]` is empty. There are no problems to quote. - **Invented problems:** none. Nothing objects to the out-of-period label "One finding lies outside the 1905 to 1914 period asked about." Nothing raises a "nothing dropped" problem about the
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-pass  found '"verdict":"pass"'
````

Files written or changed: none.

Final reply:

````
{"verdict":"pass","problems":[]}
````

#### Run 3

Grades:

````
PASS  judge-passes-clean-note   The reply gives a verdict of PASS and an empty problems list: `{"verdict":"pass","problems":[]}`. The verdict value is lowercase ("pass"), but it clearly means PASS. With no problems listed, nothing was invented. There is no "nothing dropped" complaint about the Kellard Brothers or American trick riders. The reply also does not object to the out-of-period penny-farthing finding or its label.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-pass  found '"verdict":"pass"'
````

Files written or changed: none.

Final reply:

````
{"verdict":"pass","problems":[]}
````

### E9: Out-of-scope finding dropped, research-evaluator agent

Case folder: `research-evaluator-09-out-of-scope-dropped`. Run folder: `evaluator`.

#### Run 1

Grades:

````
PASS  judge-names-dropped-period-passage   **Verdict:** The reply gives `"verdict":"fail"`. Condition 1 holds.  **Problems:** The reply contains exactly one problem:  > `{"check":"nothing dropped","where":"Topic 1 (Penny-farthings in everyday use, and their riders), and Disagreement / Uncertainty","detail":"topic-1.md Passage 3 (https://www.cycle-heritage-museum.example/collections/from-high-wheeler-to-safety) says: \"Penny-farthings were
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict":"fail"'
````

Files written or changed: none.

Final reply:

````
{"verdict":"fail","problems":[{"check":"nothing dropped","where":"Topic 1 (Penny-farthings in everyday use, and their riders), and Disagreement / Uncertainty","detail":"topic-1.md Passage 3 (https://www.cycle-heritage-museum.example/collections/from-high-wheeler-to-safety) says: \"Penny-farthings were everyday transport on English roads only from about 1875 to 1885. In the late 1880s the safety bicycle ... replaced them, and by 1892 no English maker still offered a high-wheeler in its catalogue.\" This lies outside the plan's 1905–1914 limit, but it plainly changes the answer to plan question 1, on everyday travel by penny-farthing in English towns. It suggests the question rests on a wrong period. The note leaves it out and gives only the single Albert Rowe caption as evidence of everyday use. Add the finding, with its footnote, to Topic 1 or to Disagreement / Uncertainty."}]}
````

#### Run 2

Grades:

````
PASS  judge-names-dropped-period-passage   Evidence:  1. **The verdict is FAIL.** The reply says `"verdict":"fail"`.  2. **A "nothing dropped" problem names the left-out passage.** The reply has one problem, with `"check":"nothing dropped"`.    - Where: `"Penny-farthings in everyday use, and their riders (whole section); Open Research Questions"`    - Detail: `"topic-1.md Passage 3 says penny-farthings were everyday English transport \"on
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict":"fail"'
````

Files written or changed: none.

Final reply:

````
{"verdict":"fail","problems":[{"check":"nothing dropped","where":"Penny-farthings in everyday use, and their riders (whole section); Open Research Questions","detail":"topic-1.md Passage 3 says penny-farthings were everyday English transport \"only from about 1875 to 1885\". It says the safety bicycle replaced them in the late 1880s, and that \"by 1892 no English maker still offered a high-wheeler in its catalogue.\" The passage lies outside the plan's 1905–1914 limit. It plainly changes the answer to plan question 1 (everyday use in English towns, such as riding to work), because it shows everyday use had ended long before the plan's period. The note leaves it out. It also lists \"Did other people in English towns ride penny-farthings for everyday travel between 1905 and 1914?\" as open, with no mention of this finding. Add the finding with its footnote, https://www.cycle-heritage-museum.example/collections/from-high-wheeler-to-safety."}]}
````

#### Run 3

Grades:

````
PASS  judge-names-dropped-period-passage   Evidence:  1. **The verdict is FAIL.** The reply gives `"verdict":"fail"`.  2. **A "nothing dropped" problem names the left-out passage.** There is one problem, with `"check":"nothing dropped"`. Its detail names the passage and its URL: "topic-1.md Passage 3 (https://www.cycle-heritage-museum.example/collections/from-high-wheeler-to-safety) says penny-farthings were everyday transport on English 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict":"fail"'
````

Files written or changed: none.

Final reply:

````
{"verdict":"fail","problems":[{"check":"nothing dropped","where":"Penny-farthings in everyday use, and their riders (whole section); also Open Research Questions","detail":"topic-1.md Passage 3 (https://www.cycle-heritage-museum.example/collections/from-high-wheeler-to-safety) says penny-farthings were everyday transport on English roads \"only from about 1875 to 1885\", that the safety bicycle replaced them in the late 1880s, and that \"by 1892 no English maker still offered a high-wheeler in its catalogue.\" It is England-only, but it falls outside the 1905–1914 limit. It plainly changes the answer to plan question 1, which asks how people used penny-farthings for everyday travel in English towns. It shows everyday use ended decades before the plan's period. The note leaves it out. It presents Albert Rowe's daily ride as the answer and lists only \"Did other people in English towns ride penny-farthings for everyday travel between 1905 and 1914?\" as open. Add this finding with its footnote."}]}
````

