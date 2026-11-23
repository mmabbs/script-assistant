# 2026-10-12 Bare Run: Research Cases, Batch 1

This run was done by hand with `_tools/research-run.py`, a runner written in the same session, outside `claude plugin eval`. The runner ran every grader in each case's `graders/` folder: regex and tool_used graders in code, llm graders through a Claude Opus 5.5 judge. Claude then checked every failed check against the run's output, and spot-checked the passes. The session that ran the cases did not write them.

## What Was Run

- **Date:** 2026-10-12, 13:31 to 13:34 EDT.
- **Model:** bare `claude-opus-5-5`, with no agent. The research agents aren't built.
- **Claude Code:** 2.1.296.
- **Runs:** 27. Nine cases, three runs each, at most five at a time.
- **Prompt:** each case's `prompt.md` body, word for word, as the agent would get it. That includes its first line, such as "This is the research-writer's step of a research run." No other instructions.
- **Tools:** each case's `allowed_tools`. Writer cases: Read, Write, Edit. Planner cases: Read, Glob, Grep, Write. Evaluator cases: Read.
- **Command:**

```bash
OUT=$(mktemp -d)   # /var/folders/jp/t3th_wsd03xgpgdnsn9ys63w0000gn/T/tmp.f9Zbkrr1NK
python3 _tools/research-run.py --out "$OUT/bare" --runs 3
```

- **What the runner launches per run:** `claude -p <prompt> --model claude-opus-5-5 --setting-sources project --tools <allowed_tools> --strict-mcp-config --permission-mode acceptEdits --output-format stream-json --verbose --no-session-persistence`, from the run's `work/` folder, with `CLAUDECODE` removed from the environment. A check before the batch confirmed that no CLAUDE.md, rules file, or output style loads this way.
- **Judges:** `claude -p --model claude-opus-5-5 --setting-sources project --tools "" --strict-mcp-config`, one call per llm grader per run, given the grader's text and the file it focuses on, or the final reply when it has no focus.
- **Errors and timeouts:** none. Every run exited 0. No run was repeated.
- **Before the batch,** a smoke run of W1, P1, and E1, one run each, found the runner bug in Changes, item 1. It isn't counted.

## Summary Table

"Pass line held" uses the approved Pass lines in eval-cases-research-workflow.md 05. "All checks" counts runs where every grader passed, which also needs the shape checks in eval-cases-research-workflow.md 06.1. Cost is the three runs' model cost, judges not included.

| Case | Pass line held | All checks | Checks passed, r1 / r2 / r3 | Cost |
| --- | --- | --- | --- | --- |
| W1 `research-writer-01-planted-figure` | 0 of 3 | 0 of 3 | 22 / 22 / 22 of 27 | $0.51 |
| W2 `research-writer-02-coverage-gap` | 3 of 3 | 0 of 3 | 24 / 24 / 24 of 27 | $0.49 |
| W3 `research-writer-03-source-trail` | 0 of 3 | 0 of 3 | 22 / 24 / 24 of 29 | $0.52 |
| P1 `research-planner-01-every-topic-limits` | 0 of 3 | 0 of 3 | 4 / 4 / 4 of 11 | $0.42 |
| P2 `research-planner-02-one-topic-instruction` | 2 of 3 | 0 of 3 | 7 / 6 / 7 of 10 | $0.31 |
| E1 `research-evaluator-01-changed-number` | 3 of 3 | 3 of 3 | 3 / 3 / 3 of 3 | $0.22 |
| E2 `research-evaluator-02-missing-question` | 3 of 3 | 3 of 3 | 3 / 3 / 3 of 3 | $0.22 |
| E3 `research-evaluator-03-foreign-url` | 3 of 3 | 3 of 3 | 3 / 3 / 3 of 3 | $0.23 |
| E4 `research-evaluator-04-clean-note` | 3 of 3 | 3 of 3 | 3 / 3 / 3 of 3 | $0.22 |
| **Total** | **17 of 27** | **12 of 27** | | **$3.14** |

The writer cases' extra check, `file-name`, is added by the runner (Changes, item 2).

## Findings

1. **Bare Claude gets every evaluator case right.** 12 of 12. Every FAIL names the planted error: the 1,200 against 800 piece count, the missing design-planning question (with the dropped whitewashed-table passage), and footnote 6's foreign URL. E4 passes the clean note with no invented problems in all three runs. So batch 1 can't show what the research-evaluator's instructions add. The cases still catch an agent that does worse than bare Claude. Subtler plants would be needed to tell the two apart. E5, a side finding left out, is already planned.
2. **W1: bare Claude brings in the common figure from its own memory, labelled as doubt.** All three notes keep the planted 5 years, 25 painters, and 18 months, and none gives a paint tonnage. But each says the 5-year cycle conflicts with a "widely cited" or "usually quoted" 7-year interval, in Disagreement / Uncertainty and again in Open Research Questions. r1 says the operator itself has "commonly described it" that way. r3 also adds a cause the findings don't give: lead in old paint layers, released by scraping. This is F2's trap exactly, so the research-writer's instructions must keep its own knowledge out of the note, even as doubt.
3. **W3: bare Claude keeps the unsourced tally-mark claim, labelled as unverified.** All three notes put it in Disagreement / Uncertainty as "unsourced" or "not verified," list "is there any source for it?" under Open Research Questions, and two of them repeat the label under Reliability / Limitations. None states it as fact. The approved Pass line said the detail "appears nowhere," so every run failed. The writer then allowed it under Open Research Questions only, as a question that asserts nothing (spec-research-workflow.md 11, decision 84). Every run still fails, because each also states it under Disagreement / Uncertainty. Everything else in W3 held in all three runs: every Sources URL is one of the seven, the shared Frontinus URL is kept, and the slope, the 700 staff, and the 40-centimetre deposits each cite a URL from their own passage.
4. **W2: the content held in all three runs.** The 70 lamps per round were found in topic 1's file and answered. Lamplighters' pay is listed under Open Research Questions, and no wage appears. W2's only fails are the shape details in item 5.
5. **Every writer run misses the details only the spec gives.**
    - The note is named after its title, such as `Light Research - Eiffel Tower Upkeep.md`, not `research-light-eiffel-tower-upkeep.md`.
    - `author` is left blank.
    - Frontmatter `sources` lists every URL, 5 to 7 of them. spec-research-workflow.md 07 says it stays empty, because the URLs live in the footnotes.
    - W3 r1 dates `created` and `modified` 2026-10-12, today, not the run date the prompt gives, 2026-10-08.
    These measure what the research-writer's instructions must carry.
6. **No bare plan uses the fixed layout,** `## Every topic` then `## Topic {n}`, so the layout checks fail in all six planner runs. The content is closer than the scores show:
    - **P1:** all three runs put the Rhondda and 1900 to 1914 in one section for the whole plan, under their own heading ("Overall scope," "Scope for the whole run," "Limits that apply to every topic"). But every run splits the request into four or five topics and adds one that waits on others. r1's safety topic waits on 3 and 4. r2's Topic 5, "Synthesis for the Pit Village concept," waits on all four and applies the research to the writer's story, which is F6 showing up in a plan. r3's synthesis topic waits on 1 to 3.
    - **P2:** r1 and r3 keep the small-town limit to the music topic and say in the shared scope that the film-transport topic has no such limit. r2 puts "small towns" in the shared scope and narrows the transport topic's questions to small towns, so its judge failed it.
7. **One judge question reads two ways.** P1's `judge-topics-split` says "no topic waits on another." r1's judge read it literally and failed the run. r2's and r3's judges read it as "the shift and dangers topics don't wait on each other" and passed, though both schedules have waiting topics. The code check `schedule-nothing-waits` caught the waits in all three runs either way. The writer chose the literal reading, the judge's wording now says any topic, extra ones included, and a regrade failed all three runs with each judge naming the waiting topic. The table above and the grades below are from after that regrade.

## Changes Made in This Session

All grades in this file come from after these changes. The runner's `--regrade` option graded the saved runs again, with no new Claude runs.

1. **Runner: `tool_used` graders match the file path, not the whole tool input.** The smoke run failed `no-write-outside-research` because the note's text named `llm-files`, and P1's `request-note-no-write` because the plan quoted the request note's path. The runner now matches `input_match` against the call's `file_path`, relative to `work/`, when the call has one.
2. **Runner: a misnamed note is still graded.** When a grader's note under `Research/` is missing and the run wrote exactly one new note there, the grader reads that note and the extra `file-name` check fails. Without this, the wrong file name alone would fail every check on the note.
3. **Runner: `--strict-mcp-config` on every call.** Without it, a headless run with `--setting-sources project` still loads the account's claude.ai connectors, Exa web search among them. A test call listed them. A bare writer with web search could check the planted figures against the live web.
4. **Grader `fm-sources-empty`, all three writer cases:** the old pattern, `^sources:[ \t]*$`, passed a `sources:` line with a list under it, so it passed all nine notes. The new pattern fails when a `- ` list item follows. It was tested on six inputs, including `sources:` as the last frontmatter line.
5. **Grader `judge-no-outside-facts`, W1:** its list of what the findings hold left out part of topic-2.md: "lightest at the top, so the tower looks one even colour against the sky," SETE's full name, and the reliability note on the annual report. The first judges flagged those as outside facts. The list now matches the fixture. The verdicts didn't change, since the 7-year claim fails each run on its own.
6. **Grader `judge-topics-split`, P1:** reworded to the literal reading the writer chose (Findings, item 7).
7. **W3's tally checks, after decision 84:** `no-unsourced-tally-detail` now fails "tally" or the guild only outside Open Research Questions, tested on five sample notes. A new judge, `judge-tally-only-as-question`, checks that any mention there is a question. W3 now has 29 checks.

## Caveats

1. **One judge call per check, not repeated.** Finding 7 shows two judges can read the same check differently.
2. **The bare prompt names the agent's role,** such as "the research-writer's step," because it is the agent's prompt word for word. It carries none of the agent's instructions.
3. **Cost:** the runs cost $3.14, from their streams. The batch's printed total, judges included, was $4.89. Regrading after Changes 4 and 5 ran about $1 more in judges. The smoke run cost $0.61.
4. **The Migrator's runner, `_tools/migrator-run.py`, didn't pass `--strict-mcp-config` until it was added later on 2026-10-12.** Its 2026-10-04 runs had the claude.ai connectors loaded. Whether any run called one wasn't checked.
5. **The raw run folders are in a temp folder** (the path under Command) and go when the Mac restarts. Each run's note or plan, reply, and grades are copied below.

## Full Outputs

Each run shows its grades, then what it wrote, then its final reply. Grades are one line per check, as the runner wrote them.

### W1: Planted figure

Case folder: `research-writer-01-planted-figure`.

#### Run 1

Grades:

````
FAIL  fm-author  no match; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-08'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-08'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - Eiffel Tower Upkeep.md in its place
FAIL  fm-sources-empty  no match; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  judge-footnotes-resolve   The body uses markers [^1] through [^7], each of which has a definition with a URL under `## Sources`. Every definition is used at least once.  | Marker | Used in body (example) | Definition under Sources | |---|---|---| | [^1] | "verified by the operator's page and a peer-reviewed journal article. [^1] [^2]" | `[^1]: https://www.toureiffel.paris/en/the-monument/maintenance` | | [^2] | same line  [read Light Research - Eiffel Tower Upkeep.md in its place]
FAIL  judge-no-outside-facts   The note states a fact about the tower that is not in the findings: a 7-year repainting interval attributed to the operator.  - Summary: "it conflicts with the 7-year figure that is commonly cited" - Disagreement / Uncertainty: "The figure also conflicts with the widely cited interval of roughly every 7 years, which is how the tower's operator has commonly described it." - Open Research Questions [read Light Research - Eiffel Tower Upkeep.md in its place]
PASS  keeps-18-months  found '18 months'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  keeps-25-painters  found '25'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  keeps-five-year-cycle  found '5-year'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-paint-tonnage  no match; read Light Research - Eiffel Tower Upkeep.md in its place
FAIL  no-seven-year-cycle  found '7-year'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-topic-1-section  found '## How the tower is protected from rust'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-topic-2-section  found '## Who repaints the tower, and how often'; read Light Research - Eiffel Tower Upkeep.md in its place
FAIL  file-name  wrote Light Research - Eiffel Tower Upkeep.md instead
````

`project/Research/Light Research - Eiffel Tower Upkeep.md`:

````markdown
---
title: Light Research - Eiffel Tower Upkeep
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08 14:00
modified: 2026-10-08 14:00
sources:
  - https://www.toureiffel.paris/en/the-monument/maintenance
  - https://www.construction-history.example/journal/2021/eiffel-paint-systems
  - https://www.paris-daily.example/2019/04/eiffel-lead-paint
  - https://www.paintingcontractor-mag.example/features/eiffel-rope-access
  - https://www.sete-annual-report.example/2022/maintenance-cycle
  - https://www.french-heritage-review.example/eiffel/upkeep
  - https://www.toureiffel.paris/en/the-monument/colour
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Requested from `project/Concepts/concept-iron-bridge.md`, line 9: "How is the Eiffel Tower kept from rusting? Who does the work, and how often?" Two topics: (1) how the tower is protected from rust, and (2) who repaints it and how often. Scope is present-day practice; a short historical note is included where a source gives one.
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Eiffel Tower Upkeep

## Summary

Paint is the only thing that keeps the tower's iron from rusting. There is no galvanizing or other metal coating. In each repainting campaign, damaged areas are scraped back to bare metal, then primed with an anti-corrosion primer, then given two finish coats. Painters roped to the structure apply it by hand with brushes and rollers. Spray guns aren't used because wind would carry the overspray. The finish coats have been lead-free since the campaign that began in 2019.

The operator, the Société d'Exploitation de la Tour Eiffel (SETE), runs the campaigns. Each one uses a team of about 25 specialist painters and lasts about 18 months, pausing in the worst winter weather. The findings give a 5-year repainting cycle, but only as a reported claim, and it conflicts with the 7-year figure that is commonly cited (see Disagreement / Uncertainty).

## How the tower is protected from rust

**What protects the iron:** The iron has no galvanizing or other metal coating, so paint is its only barrier against rust. Each campaign scrapes damaged areas back to bare metal, applies an anti-corrosion primer, and then adds two finish coats. This is verified by the operator's page and a peer-reviewed journal article. [^1] [^2]

**Lead:** The finish coats have been lead-free since the campaign that began in 2019. Earlier coats contained lead, and the 2019 campaign was delayed after lead was found in dust around the site. This is reported by a single newspaper source. [^3]

**How the paint goes on:** Painters work by hand with brushes and rollers, roped to the structure. Spray guns are not used because wind would carry the overspray onto visitors and the streets below. This is reported. [^1] [^4]

## Who repaints the tower, and how often

**Who:** A campaign is carried out by a team of about 25 specialist painters. This is verified. [^1] [^4] The repainting cycle is set by the company that runs the tower, the Société d'Exploitation de la Tour Eiffel (SETE). [^5] [^6]

**How long a campaign takes:** About 18 months, with work pausing in the worst winter weather. This is verified. [^1] [^4]

**How often:** The findings report that the tower is repainted every 5 years. They also say SETE set this cycle, shortening it from a longer interval after corrosion surveys in the 2000s. This is reported, and one of the two sources is the operator describing its own work. [^5] [^6] See Disagreement / Uncertainty before relying on this figure.

## Disagreement / Uncertainty

- **Repainting interval (contested claim):** The 5-year cycle is only *reported*, not verified. One of its two sources is SETE's own annual report. The figure also conflicts with the widely cited interval of roughly every 7 years, which is how the tower's operator has commonly described it. The findings don't mention the 7-year figure or explain the difference. This run did not check which is current, so treat the interval as unsettled. The claim that the cycle was shortened after corrosion surveys in the 2000s has the same sourcing and is also unconfirmed.
- **Lead-free coats since 2019 (reported, single source):** Supported by one newspaper report from April 2019, written around the time of the delay. It may not reflect how that campaign was finally carried out.
- **No spray guns (reported):** Supported by the operator and a trade magazine, but not marked verified.
- **Established in the findings (verified):** Paint is the only barrier, and the scrape, primer, and two-finish-coat sequence. About 25 painters and about 18 months per campaign. The three-shade colour scheme.

## Useful Details

- The colour is called "Eiffel Tower Brown." It goes on in three shades, darkest at the base and lightest at the top, so the tower looks one even colour against the sky. [^7]
- Weather affects the work twice: wind is why there are no spray guns, and the worst winter weather pauses a campaign. [^1] [^4]

## Open Research Questions

- Is the current repainting interval 5 years or about 7 years? Did it actually change after the 2000s corrosion surveys? Checking the operator's current maintenance page directly would settle this.
- Was the 2019 campaign finished with lead-free coats as planned, and how was the existing lead paint handled?

## Reliability / Limitations

- `toureiffel.paris (maintenance, colour)`: The operator's own current pages. Authoritative on its practice, but it is describing its own work.
- `construction-history.example (2021)`: A peer-reviewed journal article, and the strongest independent source here. It only supports the paint-system passage.
- `paris-daily.example (April 2019)`: A newspaper report written as events unfolded, and the only source for the lead claims.
- `paintingcontractor-mag.example (2022)`: A trade magazine feature on rope-access painting. Independent of the operator.
- `sete-annual-report.example (2022)`: The operator's annual report, where it describes its own work. It is one of only two sources for the contested 5-year interval.
- `french-heritage-review.example (2020)`: A heritage magazine article and the other source for the 5-year interval.

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
I wrote the light note to `project/Research/Light Research - Eiffel Tower Upkeep.md`.

**Cut short:** none. Both findings files (topic 1 and topic 2) end with the `<!-- end of findings -->` marker.

**One figure to check:** topic 2 says the tower is repainted every 5 years. That claim is only marked as reported, and one of its two sources is the operator's own annual report. It also conflicts with the roughly 7-year cycle that is commonly cited. The note gives the 5-year figure as the findings state it, but marks it as disputed under Disagreement / Uncertainty and lists it as an open question. This run didn't check which interval is current. The claim that the cycle was shortened after surveys in the 2000s has the same weak sourcing.
````

#### Run 2

Grades:

````
FAIL  fm-author  no match; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-08'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-08'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - Eiffel Tower Upkeep.md in its place
FAIL  fm-sources-empty  no match; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  judge-footnotes-resolve   Every marker in the body has a definition under Sources, every definition holds a URL, and every definition is used at least once.  **Markers used in the body:** - `[^1]`: e.g. "paint is its only barrier against rust. [^1] [^2]" - `[^2]`: same line as above, plus "two finish coats. [^1] [^2]" - `[^3]`: "lead was found in dust around the site. [^3]" - `[^4]`: "onto visitors and the streets below.  [read Light Research - Eiffel Tower Upkeep.md in its place]
FAIL  judge-no-outside-facts   The note states a repaint interval that is not in the findings. In the Disagreement / Uncertainty section it says:  > "The figure most widely given for the tower is roughly every **seven** years, and none of the gathered sources addresses that."  The Open Research Questions section repeats it: "What is the actual repainting interval: 5 years, 7 years, or something else?" The Reliability section a [read Light Research - Eiffel Tower Upkeep.md in its place]
PASS  keeps-18-months  found '18 months'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  keeps-25-painters  found '25'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  keeps-five-year-cycle  found 'every 5'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-paint-tonnage  no match; read Light Research - Eiffel Tower Upkeep.md in its place
FAIL  no-seven-year-cycle  found '7 years'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-topic-1-section  found '## How the tower is protected from rust'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-topic-2-section  found '## Who repaints the tower, and how often'; read Light Research - Eiffel Tower Upkeep.md in its place
FAIL  file-name  wrote Light Research - Eiffel Tower Upkeep.md instead
````

`project/Research/Light Research - Eiffel Tower Upkeep.md`:

````markdown
---
title: Light Research - Eiffel Tower Upkeep
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08 14:00
modified: 2026-10-08 14:00
sources:
  - https://www.toureiffel.paris/en/the-monument/maintenance
  - https://www.construction-history.example/journal/2021/eiffel-paint-systems
  - https://www.paris-daily.example/2019/04/eiffel-lead-paint
  - https://www.paintingcontractor-mag.example/features/eiffel-rope-access
  - https://www.sete-annual-report.example/2022/maintenance-cycle
  - https://www.french-heritage-review.example/eiffel/upkeep
  - https://www.toureiffel.paris/en/the-monument/colour
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Requested from [[Concepts/concept-iron-bridge|concept-iron-bridge]] (line 9): "How is the Eiffel Tower kept from rusting? Who does the work, and how often?" Two topics: (1) how the tower is protected from rust, and (2) who repaints it and how often. The writer's comment limits this to present-day practice, with a line of history allowed where a source gives one.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Eiffel Tower Upkeep

## Summary

> [!tip]-  
> A concise synthesis of the most important findings.
> 
> Focus on what is useful to understand about the subject without translating those findings into story decisions.

Paint is the only thing keeping the Eiffel Tower's iron from rusting. The iron has no galvanizing or other metal coating. In each repainting campaign, damaged areas are scraped back to bare metal, primed with an anti-corrosion primer and given two finish coats. A team of about 25 specialist painters does the work by hand with brushes and rollers while roped to the structure. A campaign takes about 18 months. One source says the tower is repainted every 5 years, but that figure is uncertain (see Disagreement / Uncertainty). The finish coats have been lead-free since the campaign that began in 2019.

## How the tower is protected from rust

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**What protects the iron.** The iron has no galvanizing or other metal coating, so paint is its only barrier against rust. [^1] [^2]

**The paint system.** Each campaign scrapes damaged areas back to bare metal, applies an anti-corrosion primer and then two finish coats. [^1] [^2] According to a 2019 newspaper report, the finish coats have been lead-free since the campaign that began that year. Earlier coats contained lead, and the 2019 campaign was delayed after lead was found in dust around the site. [^3]

**How the paint is put on.** Painters work by hand with brushes and rollers while roped to the structure. Spray guns are not used because wind would carry the overspray onto visitors and the streets below. [^1] [^4]

## Who repaints the tower, and how often

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Who does the work.** A campaign is carried out by a team of about 25 specialist painters. [^1] [^4] The repainting cycle is set by the company that runs the tower, the Société d'Exploitation de la Tour Eiffel (SETE). [^5] [^6]

**How often.** The findings report a cycle of every 5 years. They say the cycle was shortened from a longer interval after corrosion surveys in the 2000s. [^5] [^6] This figure is reported rather than verified and is open to doubt; see Disagreement / Uncertainty.

**How long a campaign takes.** About 18 months, with work pausing in the worst winter weather. [^1] [^4]

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

- **The repainting interval (contested claim).** The "every 5 years" figure and the story that the cycle was shortened after surveys in the 2000s come only from the operator's 2022 annual report and a 2020 heritage-magazine article. [^5] [^6] The researcher marked the claim *reported*, not *verified*. The operator's current maintenance page was used for other facts in this note, but it was not cited as confirming the interval. The figure most widely given for the tower is roughly every **seven** years, and none of the gathered sources addresses that. Until a primary source settles it, treat the 5-year figure as unconfirmed.
- **Lead-free finish since 2019 (reported).** This rests on a single newspaper report from April 2019, written when the campaign was starting. [^3] No later source confirms that the campaign kept to lead-free coats all the way through.
- **Established by more than one source (verified):** paint is the only barrier, the primer-plus-two-coats system, the team of about 25 painters, the campaign of about 18 months, and the three-shade colour scheme.

## Useful Details

> [!tip]-  
> Interesting or potentially useful details that do not belong cleanly elsewhere.
> 
> These may include small behavioral, material, procedural, linguistic, visual, environmental, or cultural observations.

- The colour is called "Eiffel Tower Brown." It is applied in three shades, darkest at the base and lightest at the top, so that the tower looks like one even colour against the sky. [^7]
- Work stops in the worst winter weather, so a campaign runs across more than one season. [^1] [^4]
- Wind is the practical reason for hand application. Overspray would drift onto visitors and the streets below. [^1] [^4]

## Open Research Questions

> [!tip]-  
> Questions that remain unanswered or would benefit from further research.

- What is the actual repainting interval: 5 years, 7 years, or something else? A primary operator or city source that states it directly is needed.
- Was the cycle really shortened after corrosion surveys in the 2000s, and if so, from what interval?
- Did the campaign that began in 2019 finish entirely with lead-free coats, and how was the lead found in the dust dealt with?
- Is the team of about 25 painters employed by SETE or by a contractor hired for each campaign?

## Reliability / Limitations

- `toureiffel.paris (maintenance, colour)`: The operator's own current pages. They are authoritative on its procedures, but the operator is describing its own work.
- `construction-history.example (2021)`: Peer-reviewed journal article. It is the strongest independent source for the paint system.
- `paris-daily.example (April 2019)`: Newspaper report written at the start of the 2019 campaign. It is the only source for the lead-free claim and may be out of date.
- `paintingcontractor-mag.example (2022)`: Trade magazine feature. It is useful for working methods and independently backs up the operator's figures for team size and duration.
- `sete-annual-report.example (2022)`: The operator describing its own work, as the researcher noted. It is one of only two sources for the 5-year cycle, and that figure conflicts with the commonly cited interval.
- `french-heritage-review.example (2020)`: Heritage magazine article. It is the second source for the 5-year cycle and does not give its own sourcing in the findings.
- General: All findings files were complete. None were cut short.

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
I wrote the light note at `project/Research/Light Research - Eiffel Tower Upkeep.md`.

**Findings files cut short:** none. Both topic-1 and topic-2 end with the `<!-- end of findings -->` marker.

**The repainting interval may be wrong:** the findings say the tower is repainted every 5 years. The figure most often given for the tower is about every 7 years. Two things make the 5-year figure weak:
- The researcher marked it as reported, not verified.
- Its only sources are the operator's own 2022 annual report and a 2020 heritage-magazine article. The operator's current maintenance page was cited for other facts, but not for the interval.

The note gives the 5-year figure only as what those sources say. I didn't replace it with the 7-year figure, because none of the gathered sources supports that number. The note marks the 5-year figure as contested in Disagreement / Uncertainty and lists it as an open question to check against a primary source.
````

#### Run 3

Grades:

````
FAIL  fm-author  no match; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-08'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-08'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - Eiffel Tower Upkeep.md in its place
FAIL  fm-sources-empty  no match; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  judge-footnotes-resolve   **Markers in the body:** - `[^1]`: "Paint is the only barrier… [^1] [^2]", "Application (reported)… [^1] [^4]", plus the crew size, duration and spray-painting lines. - `[^2]`: "Paint is the only barrier… [^1] [^2]" and "The paint system… [^1] [^2]". - `[^3]`: "Lead-free since 2019 (reported)… [^3]" and "Lead in old paint layers is a hazard… [^3]". - `[^4]`: "Application (reported)… [^1] [^4]", " [read Light Research - Eiffel Tower Upkeep.md in its place]
FAIL  judge-no-outside-facts   The note states a repaint interval that is not on the list. Under Disagreement / Uncertainty it says the 5-year cycle "is also out of line with the interval usually quoted in public accounts of the tower, which is about every 7 years." The findings give only "every 5 years." A 7-year figure is exactly the kind of different repaint interval the check excludes. The note admits this is unsourced ("T [read Light Research - Eiffel Tower Upkeep.md in its place]
PASS  keeps-18-months  found '18 months'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  keeps-25-painters  found '25'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  keeps-five-year-cycle  found '5-year'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-paint-tonnage  no match; read Light Research - Eiffel Tower Upkeep.md in its place
FAIL  no-seven-year-cycle  found 'every 7'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-topic-1-section  found '## How the tower is protected from rust'; read Light Research - Eiffel Tower Upkeep.md in its place
PASS  shape-topic-2-section  found '## Who repaints the tower, and how often'; read Light Research - Eiffel Tower Upkeep.md in its place
FAIL  file-name  wrote Light Research - Eiffel Tower Upkeep.md instead
````

`project/Research/Light Research - Eiffel Tower Upkeep.md`:

````markdown
---
title: Light Research - Eiffel Tower Upkeep
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08 14:00
modified: 2026-10-08 14:00
sources:
  - https://www.toureiffel.paris/en/the-monument/maintenance
  - https://www.toureiffel.paris/en/the-monument/colour
  - https://www.construction-history.example/journal/2021/eiffel-paint-systems
  - https://www.paris-daily.example/2019/04/eiffel-lead-paint
  - https://www.paintingcontractor-mag.example/features/eiffel-rope-access
  - https://www.sete-annual-report.example/2022/maintenance-cycle
  - https://www.french-heritage-review.example/eiffel/upkeep
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Drawn from the request in [[Concepts/concept-iron-bridge|concept-iron-bridge]] (line 9): "How is the Eiffel Tower kept from rusting? Who does the work, and how often?" Topics: (1) how the tower is protected from rust; (2) who repaints the tower, and how often. The writer's comment limits this to present-day practice, with a line of history allowed.
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Eiffel Tower Upkeep

## Summary

Paint is the only thing between the tower's iron and rust. The iron has no galvanizing or other metal coating. In each repainting campaign, damaged areas are scraped back to bare metal, primed with an anti-corrosion primer, and given two finish coats. The painters work by hand with brushes and rollers, roped to the structure, because spray would drift onto visitors and the streets below. A campaign takes a team of about 25 specialist painters roughly 18 months, with pauses in the worst winter weather. The tower's operator, SETE, sets how often the tower is repainted. One source pair gives a 5-year cycle, but that figure is less well supported than the rest of the findings (see Disagreement / Uncertainty). The finish coats have been lead-free since the campaign that began in 2019.

## How the tower is protected from rust

- **Paint is the only barrier.** The iron has no galvanizing or other metal coating. [^1] [^2]
- **The paint system:** each campaign scrapes damaged areas back to bare metal, applies an anti-corrosion primer, and then two finish coats. [^1] [^2]
- **Lead-free since 2019 (reported):** the finish coats have been lead-free since the campaign that began in 2019. Earlier coats contained lead. The 2019 campaign was delayed after lead was found in dust around the site. [^3]
- **Application (reported):** painters work by hand with brushes and rollers, roped to the structure. Spray guns are not used because wind would carry the overspray onto visitors and the streets below. [^1] [^4]

## Who repaints the tower, and how often

- **Who sets the schedule:** the Société d'Exploitation de la Tour Eiffel (SETE), the company that runs the tower. [^5] [^6]
- **Who does the work:** a team of about 25 specialist painters. [^1] [^4]
- **How long a campaign takes:** about 18 months, with work paused in the worst winter weather. [^1] [^4]
- **How often (reported, uncertain):** every 5 years, according to SETE's 2022 annual report and a 2020 heritage-magazine article. The same sources say the interval was shortened from a longer one after corrosion surveys in the 2000s. [^5] [^6] See Disagreement / Uncertainty before relying on this figure.

## Disagreement / Uncertainty

- **Established (verified, several sources including the operator's own page):** paint is the only barrier, the system is primer plus two finish coats, and a campaign takes about 25 painters roughly 18 months.
- **Reported, single source:** the switch to lead-free finish coats in 2019 and the delay caused by lead dust come from one April 2019 newspaper report. That report was written while the campaign was just starting, so later developments may not be covered.
- **Contested / weakly supported: the 5-year repainting cycle.** The research marks this figure "reported," not verified. It does not come from the operator's public maintenance page, which the findings cite for the other campaign details. It is also out of line with the interval usually quoted in public accounts of the tower, which is about every 7 years. The findings do not cite a source for 7 years, so that is the writer's flag, not a sourced claim. The claim that the cycle was "shortened … after corrosion surveys in the 2000s" has the same weak support. Treat the interval as unconfirmed until it is checked against the operator's maintenance page.

## Useful Details

- The colour, "Eiffel Tower Brown," is applied in three shades, darkest at the base and lightest at the top, so that the tower looks like one even colour against the sky. [^7]
- Spray painting is ruled out by wind and by the people below, not by the paint itself. [^1] [^4]
- Lead in old paint layers is a hazard during scraping, not only in new paint. That is why lead dust around the site delayed the 2019 campaign. [^3]

## Open Research Questions

- What is the actual repainting interval? Check the 5-year figure against the operator's maintenance page and the commonly quoted 7-year figure.
- Is the team of painters employed by SETE, or by a contractor SETE hires for each campaign?
- How was the 2019 lead problem resolved, and how long did it delay the campaign?

## Reliability / Limitations

- `toureiffel.paris` (maintenance and colour pages): the operator's own current pages. Authoritative on its own practice, but the operator is describing itself.
- `construction-history.example` (2021): a peer-reviewed journal article. The strongest independent source for the paint system.
- `paris-daily.example` (April 2019): a newspaper report written when the campaign was starting. It is the only source for the lead details.
- `paintingcontractor-mag.example` (2022): a trade magazine feature. It backs up the operator on crew size, duration, and hand application.
- `sete-annual-report.example` (2022): the operator describing its own work, as the researcher noted. It is one of only two sources for the 5-year cycle.
- `french-heritage-review.example` (2020): a heritage magazine article. It is the other source for the 5-year cycle and for the claim that the interval was shortened.

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
I wrote the light note to `project/Research/Light Research - Eiffel Tower Upkeep.md`.

**Findings files cut short:** none. Both topic-1 and topic-2 run to the `<!-- end of findings -->` marker.

One figure needs checking before anyone relies on it: the claim that the tower is repainted every 5 years (topic 2, passage 1).
- **Weak support:** the researcher marked it "reported," not verified. Its only sources are the operator's own annual report and a heritage magazine. It doesn't come from the operator's maintenance page, which the findings use for everything else in that topic.
- **Conflict:** public accounts usually give about every 7 years. No findings file cites that, so I put it in the note as my own flag rather than as a sourced fact.
- **Also uncertain:** the claim that the cycle was shortened after corrosion surveys in the 2000s has the same weak support.

I listed both under Disagreement / Uncertainty and added checking the interval to the Open Research Questions.

I left `status` and `tags` blank, as in the template. I set `created` and `modified` to the run date at 14:00, taken from the run ID.
````

### W2: Coverage gap

Case folder: `research-writer-02-coverage-gap`.

#### Run 1

Grades:

````
FAIL  fm-author  no match; read Light Research - London Gas Lamps.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-08'; read Light Research - London Gas Lamps.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-08'; read Light Research - London Gas Lamps.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - London Gas Lamps.md in its place
FAIL  fm-sources-empty  no match; read Light Research - London Gas Lamps.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - London Gas Lamps.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - London Gas Lamps.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - London Gas Lamps.md in its place
PASS  judge-footnotes-resolve   Markers used in the body: [^1], [^2], [^3], [^4], [^5]. Each one has a definition under Sources, and each definition holds a URL:  - `[^1]: https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets` is used in "Fuel and supply… [^1] [^2]", "Lighting and putting out… [^1]", and "The lamplighter's pole did two jobs… [^1]". - `[^2]: https://www.gas-history-society.example/papers [read Light Research - London Gas Lamps.md in its place]
PASS  judge-pay-in-open-questions   The Open Research Questions section asks what lamplighters were paid:  > ## Open Research Questions > - **What was a lamplighter paid in 1880s London?** (Plan question 4, unanswered.) Vestry wage books survive for some parishes at the London Metropolitan Archives but are not online. [^5] > - Was a round of about 70 lamps typical across London, or specific to St Pancras? [^3]  The note gives no wa [read Light Research - London Gas Lamps.md in its place]
PASS  judge-three-questions-answered   **Q1: fuel and how it reached the lamp.** Answered with the required details. The note says: "The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern." That covers coal gas, the gasworks, cast-iron mains under the streets, and the lamp post.  **Q2: how a lamp was lit and put out.** Answered [read Light Research - London Gas Lamps.md in its place]
PASS  keeps-70-lamps  found '70'; read Light Research - London Gas Lamps.md in its place
PASS  keeps-coal-gas  found 'coal gas'; read Light Research - London Gas Lamps.md in its place
PASS  keeps-dawn-round  found 'dawn'; read Light Research - London Gas Lamps.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-invented-wage  no match; read Light Research - London Gas Lamps.md in its place
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - London Gas Lamps.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - London Gas Lamps.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - London Gas Lamps.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - London Gas Lamps.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - London Gas Lamps.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - London Gas Lamps.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - London Gas Lamps.md in its place
PASS  shape-topic-1-section  found '## How the gas street lamp'; read Light Research - London Gas Lamps.md in its place
PASS  shape-topic-2-section  found '## The lamplighter'; read Light Research - London Gas Lamps.md in its place
FAIL  file-name  wrote Light Research - London Gas Lamps.md instead
````

`project/Research/Light Research - London Gas Lamps.md`:

````markdown
---
title: Light Research - London Gas Lamps
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08 14:00
modified: 2026-10-08 14:00
sources:
  - https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets
  - https://www.gas-history-society.example/papers/metropolitan-mains
  - https://www.vestry-minutes.example/st-pancras/1884/lighting-committee
  - https://www.london-streets-history.example/trades/lamplighter
  - https://www.lma-guide.example/sources/vestry-wage-books
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Two topics from the `- [r]` request in `project/Ideas/idea-night-rounds.md` (line 9): how London's gas street lamps worked, and the lamplighters who looked after them (how many lamps one man tended and what he was paid). The writer's comment limits the research to London only, in the 1880s.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - London Gas Lamps

## Summary

> [!tip]-  
> A concise synthesis of the most important findings.
> 
> Focus on what is useful to understand about the subject without translating those findings into story decisions.

In 1880s London, street lamps burned coal gas made at the gasworks. The gas reached them through cast-iron mains under the streets and then up each lamp post. Lamplighters worked for the gas companies or the parish vestries. Each one walked a round twice a day: lighting the lamps with a pole-mounted flame at dusk and turning them off at dawn. One parish's 1884 records put a round at about 70 lamps. This search found no source for lamplighters' 1880s wages. Vestry wage books that would show them survive for some parishes, but only in the archive, not online.

## How the gas street lamps worked

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Fuel and supply.** The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern. [^1] [^2]

**Lighting and putting out.** The lamplighter carried a long pole with a hook at the top for turning the gas tap, and a small oil-fed flame for lighting the burner. He lit his lamps on an evening round at dusk and turned them off on a second round at dawn. [^1]

## The lamplighters

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Employers and duties.** Lamplighters were employed by the gas companies or by the parish vestries, not by the police. Besides lighting and putting out the lamps, they cleaned the lamp glass once a week and reported broken lamps to the vestry. [^2] [^3]

**Lamps per lamplighter.** The gas companies and parish vestries divided each district into rounds. A lamplighter's round covered about 70 lamps, and he walked it twice a day, at dusk and at dawn. [^3] This figure is reported from one parish's minutes (St Pancras, 1884) and has not been confirmed for London as a whole.

**Hours.** The evening round began about half an hour before sunset, so in winter a lamplighter started work in mid-afternoon. The dawn round began before first light. [^4]

**Pay.** No source found in this search gave lamplighters' wages for the 1880s. [^5]

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

- **Round size (about 70 lamps): reported, single source.** It comes only from St Pancras vestry minutes for 1884. [^3] Other parishes and the gas companies may have set different round sizes.
- **Start times for the rounds: reported, single source.** The "half an hour before sunset" timing comes from one local history society page. [^4]
- **Wages: unknown.** This search found no figure. [^5]
- The fuel and supply, the lighting method, and who employed lamplighters and what they did are all verified across sources.

## Useful Details

> [!tip]-  
> Interesting or potentially useful details that do not belong cleanly elsewhere.
> 
> These may include small behavioral, material, procedural, linguistic, visual, environmental, or cultural observations.

- The lamplighter's pole did two jobs: its hook turned the gas tap, and a small oil-fed flame lit the burner. [^1]
- Because the evening round started before sunset, a winter lamplighter's working day began in mid-afternoon. [^4]
- Lamplighters also cleaned the lamp glass once a week and reported broken lamps to the vestry. [^2] [^3]

## Open Research Questions

> [!tip]-  
> Questions that remain unanswered or would benefit from further research.

- **What was a lamplighter paid in 1880s London?** (Plan question 4, unanswered.) Vestry wage books survive for some parishes at the London Metropolitan Archives but are not online. [^5]
- Was a round of about 70 lamps typical across London, or specific to St Pancras? [^3]

## Reliability / Limitations

- `londonmuseum.example` (museum collection article, 2018): The main source for how the lamps worked. Its account of fuel and supply is confirmed by the gas history society paper.
- `gas-history-society.example` (society research paper, 2011): A secondary research paper. It confirms the supply method and who employed lamplighters.
- `vestry-minutes.example` (digitized St Pancras vestry minutes, 1884): A primary source from the right place and decade, but it covers only one parish. It is the only source for the round size of about 70 lamps.
- `london-streets-history.example` (local history society page, 2015): The only source for when the rounds started. Not confirmed elsewhere.
- `lma-guide.example` (archive research guide, 2021): An archive guide, not a source for wages. It records that the likely wage records exist only offline.

## Sources

[^1]: https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets
[^2]: https://www.gas-history-society.example/papers/metropolitan-mains
[^3]: https://www.vestry-minutes.example/st-pancras/1884/lighting-committee
[^4]: https://www.london-streets-history.example/trades/lamplighter
[^5]: https://www.lma-guide.example/sources/vestry-wage-books
````

Final reply:

````
I wrote the note at `project/Research/Light Research - London Gas Lamps.md`.

**Cut-short findings files:** none. Both topic 1 and topic 2 end with the `<!-- end of findings -->` marker.

**One question is still open:** question 4, what a lamplighter was paid. The researchers found no wage figures for the 1880s. The vestry wage books that would have them are only in the London Metropolitan Archives, not online. The note lists this under Open Research Questions.

**Two smaller points:**
- **Moved finding:** the answer to question 3 (about 70 lamps per round) was in the topic 1 findings. I put it in the note under The lamplighters, where that question belongs.
- **Weak spot:** that figure, and the times the rounds started, each come from a single source. The note labels both as reported, not verified.
````

#### Run 2

Grades:

````
FAIL  fm-author  no match; read Light Research - London Gas Lamps.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-08'; read Light Research - London Gas Lamps.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-08'; read Light Research - London Gas Lamps.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - London Gas Lamps.md in its place
FAIL  fm-sources-empty  no match; read Light Research - London Gas Lamps.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - London Gas Lamps.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - London Gas Lamps.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - London Gas Lamps.md in its place
PASS  judge-footnotes-resolve   Body markers and their definitions under `## Sources`:  - **[^1]** is used in "...up through each lamp post to a burner inside the glass lantern. [^1] [^2]" and elsewhere. It is defined as `[^1]: https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets`. - **[^2]** is used in "...[^1] [^2]" and in "...not by the police... reported broken lamps to the vestry. [^2] [^3]". It i [read Light Research - London Gas Lamps.md in its place]
PASS  judge-pay-in-open-questions   The Open Research Questions section asks what lamplighters were paid. Quoted in full:  > ## Open Research Questions > > - **What was a lamplighter paid in 1880s London?** (Plan question 4, unanswered.) The likeliest source is the surviving vestry wage books at the London Metropolitan Archives, which survive for some parishes but have not been put online. [^5] > - Was a round of about 70 lamps typ [read Light Research - London Gas Lamps.md in its place]
PASS  judge-three-questions-answered   All three questions are answered, each with the required detail.  **1. Fuel and how it reached the lamp:** Answered. "**Fuel and supply.** The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern." This covers coal gas, the gasworks, cast-iron mains under the streets, and the route up the la [read Light Research - London Gas Lamps.md in its place]
PASS  keeps-70-lamps  found '70'; read Light Research - London Gas Lamps.md in its place
PASS  keeps-coal-gas  found 'coal gas'; read Light Research - London Gas Lamps.md in its place
PASS  keeps-dawn-round  found 'dawn'; read Light Research - London Gas Lamps.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-invented-wage  no match; read Light Research - London Gas Lamps.md in its place
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - London Gas Lamps.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - London Gas Lamps.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - London Gas Lamps.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - London Gas Lamps.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - London Gas Lamps.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - London Gas Lamps.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - London Gas Lamps.md in its place
PASS  shape-topic-1-section  found '## How the gas street lamp'; read Light Research - London Gas Lamps.md in its place
PASS  shape-topic-2-section  found '## The lamplighter'; read Light Research - London Gas Lamps.md in its place
FAIL  file-name  wrote Light Research - London Gas Lamps.md instead
````

`project/Research/Light Research - London Gas Lamps.md`:

````markdown
---
title: Light Research - London Gas Lamps
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08 14:00
modified: 2026-10-08 14:00
sources:
  - https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets
  - https://www.gas-history-society.example/papers/metropolitan-mains
  - https://www.vestry-minutes.example/st-pancras/1884/lighting-committee
  - https://www.london-streets-history.example/trades/lamplighter
  - https://www.lma-guide.example/sources/vestry-wage-books
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> How London's gas street lamps worked, and the lamplighters who looked after them: how many lamps one lamplighter tended and what they were paid. London only, in the 1880s.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - London Gas Lamps

## Summary

> [!tip]-  
> A concise synthesis of the most important findings.
> 
> Focus on what is useful to understand about the subject without translating those findings into story decisions.

London's street lamps burned coal gas made at the gasworks. It reached them through cast-iron mains under the streets and came up each lamp post to a burner in the glass lantern. Each lamplighter worked for a gas company or a parish vestry, not the police. They used a long pole with a hook to turn the gas tap and a small oil-fed flame to light the burner. Each lamp got two visits a day: lit on an evening round at dusk, put out on a second round at dawn. One parish's records give a round of about 70 lamps. No source found in this search gave lamplighters' wages for the 1880s. Vestry wage books survive for some parishes, but they are not online.

## How the gas street lamps worked

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Fuel and supply.** The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern. [^1] [^2]

**Lighting and putting out.** The lamplighter carried a long pole with a hook at the top for turning the gas tap, and a small oil-fed flame for lighting the burner. Lamps were lit on an evening round at dusk and turned off on a second round at dawn. [^1]

## The lamplighters

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Employer and duties.** Lamplighters were employed by the gas companies or by the parish vestries, not by the police. Besides lighting and putting out the lamps, they cleaned the lamp glass once a week and reported broken lamps to the vestry. [^2] [^3]

**Lamps per lamplighter.** The gas companies and parish vestries divided each district into rounds. A lamplighter's round covered about 70 lamps, walked twice a day, at dusk and at dawn. [^3] This figure comes from one parish's records (St Pancras, 1884), so it may not hold for all of London.

**Hours.** The evening round began about half an hour before sunset, so in winter a lamplighter started work in mid-afternoon. The dawn round began before first light. [^4]

**Pay.** No source found in this search gave lamplighters' wages for the 1880s. A guide to the London Metropolitan Archives says vestry wage books survive for some parishes but have not been put online. [^5]

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

- **Established (verified across sources):** the gas supply chain from gasworks to burner; the pole-and-flame lighting method with dusk and dawn rounds; lamplighters employed by gas companies or vestries, not the police, with weekly glass-cleaning and reporting of broken lamps.
- **Reported, single source:** the round of about 70 lamps comes only from St Pancras vestry minutes (1884). Round sizes in other parishes or company districts are unknown.
- **Reported, single source:** the start times (about half an hour before sunset; before first light) come from one local history society page.
- **Unknown:** 1880s lamplighter pay. No figure was found.

## Useful Details

> [!tip]-  
> Interesting or potentially useful details that do not belong cleanly elsewhere.
> 
> These may include small behavioral, material, procedural, linguistic, visual, environmental, or cultural observations.

- The lamplighter's kit was a single long pole carrying both a hook for the gas tap and a small oil-fed flame. [^1]
- Because the evening round was tied to sunset, the working day moved with the seasons, starting in mid-afternoon in winter. [^4]
- Lamplighters' duties went beyond lighting: weekly cleaning of the lamp glass and reporting broken lamps to the vestry. [^2] [^3]

## Open Research Questions

> [!tip]-  
> Questions that remain unanswered or would benefit from further research.

- **What was a lamplighter paid in 1880s London?** (Plan question 4, unanswered.) The likeliest source is the surviving vestry wage books at the London Metropolitan Archives, which survive for some parishes but have not been put online. [^5]
- Was a round of about 70 lamps typical across London, or particular to St Pancras? Gas company records and other parishes' vestry minutes would show this.

## Reliability / Limitations

- `londonmuseum.example – Gas lighting in Victorian streets`: museum collection article (2018). Secondary source, used for verified claims about supply and lighting method.
- `gas-history-society.example – Metropolitan mains`: society research paper (2011). Secondary source, agrees with the museum article on supply.
- `vestry-minutes.example – St Pancras lighting committee, 1884`: digitized parish minutes, a primary source from within the period. Covers one parish only, so the 70-lamp round may not apply elsewhere.
- `london-streets-history.example – Lamplighter`: local history society page (2015). The only source for start times, and it does not say where its information comes from.
- `lma-guide.example – Vestry wage books`: archive research guide (2021). Confirms that wage records exist but holds no wage figures.

## Sources

[^1]: https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets
[^2]: https://www.gas-history-society.example/papers/metropolitan-mains
[^3]: https://www.vestry-minutes.example/st-pancras/1884/lighting-committee
[^4]: https://www.london-streets-history.example/trades/lamplighter
[^5]: https://www.lma-guide.example/sources/vestry-wage-books
````

Final reply:

````
The light note is at `project/Research/Light Research - London Gas Lamps.md`.

**Cut-short findings files:** none. Both files (topics 1 and 2) end with the `<!-- end of findings -->` marker.

Two gaps in coverage:
- **Question 3 (how many lamps one lamplighter tended)** was answered in topic 1's findings, not topic 2's. The note puts it under "The lamplighters", where the plan asks it. The answer, about 70 lamps per round, comes only from the St Pancras vestry minutes of 1884, so the note says it may not apply to other parishes.
- **Question 4 (pay)** has no answer. No source gave wages for the 1880s. The note says so and lists it under Open Research Questions. It points to the vestry wage books at the London Metropolitan Archives, which survive for some parishes but aren't online.
````

#### Run 3

Grades:

````
FAIL  fm-author  no match; read Light Research - London Gas Lamps.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-08'; read Light Research - London Gas Lamps.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-08'; read Light Research - London Gas Lamps.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - London Gas Lamps.md in its place
FAIL  fm-sources-empty  no match; read Light Research - London Gas Lamps.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - London Gas Lamps.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - London Gas Lamps.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - London Gas Lamps.md in its place
PASS  judge-footnotes-resolve   Every marker used in the body has a matching definition with a URL, and every definition is used.  **Markers in the body:** - `[^1]`: "up through each lamp post to a burner inside the glass lantern. [^1] [^2]" and "turned them off on a second round at dawn. [^1]" - `[^2]`: "reported broken lamps to the vestry. [^2] [^3]" - `[^3]`: "(reported, not verified). [^3]" - `[^4]`: "The dawn round began b [read Light Research - London Gas Lamps.md in its place]
PASS  judge-pay-in-open-questions   The Open Research Questions section asks directly what lamplighters were paid:  > ## Open Research Questions > > - What was a London lamplighter paid in the 1880s? The vestry wage books held at the London Metropolitan Archives are the lead; they are not online and would need an in-person or archive-request search. [^5] > - Was a round of about 70 lamps typical across London, or particular to St P [read Light Research - London Gas Lamps.md in its place]
PASS  judge-three-questions-answered   All three questions are answered with the required details.  1. **Fuel and supply.** "The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern."  2. **Lighting and putting out.** "The lamplighter carried a long pole with a hook at the top for turning the gas tap, and a small oil-fed flame fo [read Light Research - London Gas Lamps.md in its place]
PASS  keeps-70-lamps  found '70'; read Light Research - London Gas Lamps.md in its place
PASS  keeps-coal-gas  found 'coal gas'; read Light Research - London Gas Lamps.md in its place
PASS  keeps-dawn-round  found 'dawn'; read Light Research - London Gas Lamps.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  no-invented-wage  no match; read Light Research - London Gas Lamps.md in its place
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - London Gas Lamps.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - London Gas Lamps.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - London Gas Lamps.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - London Gas Lamps.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - London Gas Lamps.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - London Gas Lamps.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - London Gas Lamps.md in its place
PASS  shape-topic-1-section  found '## How the gas street lamp'; read Light Research - London Gas Lamps.md in its place
PASS  shape-topic-2-section  found '## The lamplighter'; read Light Research - London Gas Lamps.md in its place
FAIL  file-name  wrote Light Research - London Gas Lamps.md instead
````

`project/Research/Light Research - London Gas Lamps.md`:

````markdown
---
title: Light Research - London Gas Lamps
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08 14:00
modified: 2026-10-08 14:00
sources:
  - https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets
  - https://www.gas-history-society.example/papers/metropolitan-mains
  - https://www.vestry-minutes.example/st-pancras/1884/lighting-committee
  - https://www.london-streets-history.example/trades/lamplighter
  - https://www.lma-guide.example/sources/vestry-wage-books
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Two topics drawn from the request "How did London's gas street lamps work, and who looked after them? How many lamps did one man tend, and what was he paid?" (`project/Ideas/idea-night-rounds.md`, line 9): how the gas street lamps worked, and the lamplighters. The writer's comment limits the research to London only, in the 1880s.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - London Gas Lamps

## Summary

> [!tip]-  
> A concise synthesis of the most important findings.
> 
> Focus on what is useful to understand about the subject without translating those findings into story decisions.

London's street lamps in the 1880s burned coal gas made at the gasworks and piped under the streets in cast-iron mains, up each lamp post to a burner inside the glass lantern. A lamplighter, employed by a gas company or a parish vestry, walked a round twice a day: at dusk to light the lamps with a pole carrying a tap hook and a small oil-fed flame, and at dawn to turn them off. He also cleaned the lamp glass weekly and reported broken lamps. One parish's 1884 records put a round at about 70 lamps. No source found gave an 1880s lamplighter's wage; vestry wage books survive for some parishes in the London Metropolitan Archives but are not online.

## How the gas street lamps worked

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Fuel and supply.** The lamps burned coal gas made at the gasworks. The gas ran under the streets in cast-iron mains and up through each lamp post to a burner inside the glass lantern. [^1] [^2]

**Lighting and putting out.** The lamplighter carried a long pole with a hook at the top for turning the gas tap, and a small oil-fed flame for lighting the burner. He lit his lamps on an evening round at dusk and turned them off on a second round at dawn. [^1]

## The lamplighters

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Employers and duties.** Lamplighters were employed by the gas companies or by the parish vestries, not by the police. Besides lighting and putting out the lamps, they cleaned the lamp glass once a week and reported broken lamps to the vestry. [^2] [^3]

**How many lamps one lamplighter tended.** The gas companies and parish vestries divided each district into rounds. In St Pancras in 1884, a lamplighter's round covered about 70 lamps, walked twice a day, at dusk and at dawn. This comes from one parish's records only (reported, not verified). [^3]

**Hours.** The evening round began about half an hour before sunset, so in winter a lamplighter started work in mid-afternoon. The dawn round began before first light. (Reported, not verified.) [^4]

**Pay.** No source found gave lamplighters' wages for the 1880s. A guide to the London Metropolitan Archives says vestry wage books survive for some parishes but have not been put online. [^5]

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

- **Established fact:** coal gas fuel, supply by cast-iron mains, the pole-and-flame lighting method, dusk and dawn rounds, and employment by gas companies or vestries are each supported by verified sources. [^1] [^2] [^3]
- **Incomplete:** the figure of about 70 lamps per round comes from a single parish (St Pancras, 1884). Whether other parishes or the gas companies set rounds of a similar size is not established. [^3]
- **Reported, single source:** the start times of the rounds (about half an hour before sunset; before first light) come from one local history society page. [^4]
- **Unanswered:** wages. No figure was found. [^5]

## Useful Details

> [!tip]-  
> Interesting or potentially useful details that do not belong cleanly elsewhere.
> 
> These may include small behavioral, material, procedural, linguistic, visual, environmental, or cultural observations.

- The lamplighter's pole did two jobs: a hook to turn the gas tap, and a small oil-fed flame to light the burner. [^1]
- Because the evening round started before sunset, a winter lamplighter's working day began in mid-afternoon. [^4]
- Weekly cleaning of the lamp glass and reporting broken lamps to the vestry were part of the job. [^2] [^3]

## Open Research Questions

> [!tip]-  
> Questions that remain unanswered or would benefit from further research.

- What was a London lamplighter paid in the 1880s? The vestry wage books held at the London Metropolitan Archives are the lead; they are not online and would need an in-person or archive-request search. [^5]
- Was a round of about 70 lamps typical across London, or particular to St Pancras? Gas-company records or other parishes' vestry minutes would show this.

## Reliability / Limitations

- `londonmuseum.example` (museum collection article, 2018): verified; the only source for the lighting method.
- `gas-history-society.example` (society research paper, 2011): verified.
- `vestry-minutes.example` (digitized St Pancras vestry minutes, 1884): a primary source, but it covers one parish only, so the 70-lamp figure may not hold for all of London.
- `london-streets-history.example` (local history society page, 2015): reported, not corroborated by a second source.
- `lma-guide.example` (archive research guide, 2021): confirms wage records exist, but gives no figures.

## Sources

[^1]: https://www.londonmuseum.example/collections/gas-lighting-in-victorian-streets
[^2]: https://www.gas-history-society.example/papers/metropolitan-mains
[^3]: https://www.vestry-minutes.example/st-pancras/1884/lighting-committee
[^4]: https://www.london-streets-history.example/trades/lamplighter
[^5]: https://www.lma-guide.example/sources/vestry-wage-books
````

Final reply:

````
I wrote the note at `project/Research/Light Research - London Gas Lamps.md`.

**No findings file was cut short.** Both topic-1 and topic-2 end with the `<!-- end of findings -->` marker.

Two gaps in what was found:

- **Lamps per lamplighter (question 3):** the answer, about 70 lamps per round, came from the topic-1 file. I put it in the note's "The lamplighters" section, where the plan asks the question. It comes from one parish's records (St Pancras, 1884), and the note says so.
- **Pay (question 4):** no source gave an 1880s wage. The note lists this as an open question. The lead is the London Metropolitan Archives, which holds vestry wage books for some parishes, but they aren't online.
````

### W3: Source trail

Case folder: `research-writer-03-source-trail`.

#### Run 1

Grades:

````
FAIL  fm-author  no match; read Light Research - Roman Aqueducts.md in its place
FAIL  fm-created-run-date  no match; read Light Research - Roman Aqueducts.md in its place
FAIL  fm-modified-run-date  no match; read Light Research - Roman Aqueducts.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - Roman Aqueducts.md in its place
FAIL  fm-sources-empty  no match; read Light Research - Roman Aqueducts.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - Roman Aqueducts.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - Roman Aqueducts.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - Roman Aqueducts.md in its place
PASS  judge-claims-carry-right-source   1. **Slope claim:** "The aqueduct that supplied Nîmes falls only about 12.6 metres over its whole length of about 50 kilometres, an average of about 25 centimetres per kilometre. Surveyors set this slope with levelling instruments over the whole route before building began. [^1] [^2]"    - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` is allowed.    - `[^2]: https://www.roma [read Light Research - Roman Aqueducts.md in its place]
PASS  judge-footnotes-resolve   Every marker in the body has a definition with a URL, and every definition is used.  **Markers in the body:** - "Keeping the water flowing downhill": `[^1] [^2]` - "Arches and siphons": `[^3] [^4]` - "Who was responsible": `[^4] [^5]` - "What upkeep the channels needed": `[^6] [^7]` - Useful Details: `[^4] [^5]`, `[^3]`, `[^6] [^7]`  The body uses `[^1]` through `[^7]`, and no other markers.  **D [read Light Research - Roman Aqueducts.md in its place]
FAIL  judge-tally-only-as-question   The tally marks and the guild appear in sections other than Open Research Questions.  1. **## Disagreement / Uncertainty**    > "**Unsourced (anecdotal, reported only):** A claim that a guild of channel keepers at Nîmes cut a tally mark into the channel wall after each cleaning, and that some of the marks can still be counted. The researcher marked this as reported and found no source for it. Tre [read Light Research - Roman Aqueducts.md in its place]
PASS  judge-urls-from-findings   Every URL in the note's Sources section matches an allowed URL exactly:  - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` - `[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul` - `[^3]: https://www.lyon-archaeology.example/aqueducts/siphons` - `[^4]: https://www.ancient-texts-library.example/frontinus/de-aquaeductu` - `[^5]: https://www.roman-water-rev [read Light Research - Roman Aqueducts.md in its place]
PASS  keeps-25-cm-gradient  found '25 centimetres'; read Light Research - Roman Aqueducts.md in its place
PASS  keeps-40-cm-sinter  found '40 centimetres'; read Light Research - Roman Aqueducts.md in its place
PASS  keeps-700-staff  found '700'; read Light Research - Roman Aqueducts.md in its place
PASS  keeps-shared-url  found 'https://www.ancient-texts-library.example/frontinus/de-aquaeductu'; read Light Research - Roman Aqueducts.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
FAIL  no-unsourced-tally-detail  found '\n## Disagreement / Uncertainty\n\n> [!tip]-  \n> Claims that are disputed, uncertain, incomplete, changing, or dependent on'; read Light Research - Roman Aqueducts.md in its place
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-topic-1-section  found '## How the aqueducts were built'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-topic-2-section  found '## How the aqueducts were kept running'; read Light Research - Roman Aqueducts.md in its place
FAIL  file-name  wrote Light Research - Roman Aqueducts.md instead
````

`project/Research/Light Research - Roman Aqueducts.md`:

````markdown
---
title: Light Research - Roman Aqueducts
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-12 12:00
modified: 2026-10-12 12:00
sources:
  - https://www.nimes-heritage.example/aqueduct/survey-gradient
  - https://www.roman-engineering-journal.example/2015/gradients-in-gaul
  - https://www.lyon-archaeology.example/aqueducts/siphons
  - https://www.ancient-texts-library.example/frontinus/de-aquaeductu
  - https://www.roman-water-review.example/2019/curator-aquarum
  - https://www.hydro-history.example/2020/sinter-deposits-nimes
  - https://www.geoarchaeology-letters.example/2017/carbonate-layers
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Request: "How did the Romans build their aqueducts, and how were they kept running?" (from [[Concepts/concept-old-water-channel|concept-old-water-channel]], run-2026-10-08-1400-research). Two topics: how the aqueducts were built, and how they were kept running. Bounded by the writer's comment to the city of Rome and Roman Gaul, up to the 3rd century AD.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Roman Aqueducts

## Summary

> [!tip]-  
> A concise synthesis of the most important findings.
> 
> Focus on what is useful to understand about the subject without translating those findings into story decisions.

Roman aqueducts moved water by gravity alone, on very gentle slopes that surveyors set with levelling instruments before construction began. The Nîmes aqueduct drops only about 25 centimetres per kilometre. Arches carried the channel across valleys so the slope stayed steady. Where a valley was too deep for arches, as at Lyon, builders used inverted siphons of sealed lead pipe instead.

In Rome, a water commissioner, the *curator aquarum*, ran the system. Frontinus, who held the post from 97 AD, describes a staff of about 700 slaves who repaired and cleaned the channels. The main upkeep problem was hard water. It left layers of calcium carbonate (sinter) that narrowed the channels and had to be chipped out. At Nîmes these layers reached about 40 centimetres thick.

## How the aqueducts were built

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Keeping the water flowing downhill.** The aqueduct that supplied Nîmes falls only about 12.6 metres over its whole length of about 50 kilometres, an average of about 25 centimetres per kilometre. Surveyors set this slope with levelling instruments over the whole route before building began. [^1] [^2]

**Arches and siphons.** Arches carried the channel across valleys so the slope could stay steady. Where a valley was too deep for arches, as at Lyon, builders used inverted siphons: sealed lead pipes that ran down one side of the valley and up the other, with the water pushed up by its own pressure. [^3] [^4]

## How the aqueducts were kept running

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Who was responsible.** In Rome, the water commissioner, the *curator aquarum*, was responsible for the aqueducts. Frontinus held the post from 97 AD and wrote a treatise on the system. He describes a staff of about 700 slaves, split between a public gang and an imperial gang, who repaired and cleaned the channels. [^4] [^5]

**What upkeep the channels needed.** Hard water left layers of calcium carbonate, called sinter, inside the channels. The layers narrowed the channel and had to be chipped out. In parts of the Nîmes aqueduct the deposits reached about 40 centimetres thick. [^6] [^7]

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

- **Unsourced (anecdotal, reported only):** A claim that a guild of channel keepers at Nîmes cut a tally mark into the channel wall after each cleaning, and that some of the marks can still be counted. The researcher marked this as reported and found no source for it. Treat it as unverified.
- The staff figure of about 700 slaves is for the city of Rome, from Frontinus's own account around 97 AD. The findings don't say who did this work in Roman Gaul or how it was organized there.

## Useful Details

> [!tip]-  
> Interesting or potentially useful details that do not belong cleanly elsewhere.
> 
> These may include small behavioral, material, procedural, linguistic, visual, environmental, or cultural observations.

- Rome's maintenance staff was split into two gangs, one public and one imperial. [^4] [^5]
- Siphon pipes were made of lead. [^3]
- The sinter layers built up inside the channel itself, so a working channel slowly narrowed over time unless it was cleared. [^6] [^7]

## Open Research Questions

> [!tip]-  
> Questions that remain unanswered or would benefit from further research.

- Who was responsible for aqueduct upkeep in Roman Gaul, as opposed to the city of Rome?
- Is there any source for the reported tally marks left by channel keepers at Nîmes?
- How often were channels cleaned of sinter, and how was the work done while water was still needed?

## Reliability / Limitations

- `nimes-heritage.example`: heritage service survey report (2012). An official site survey; strong for the Nîmes gradient figures.
- `roman-engineering-journal.example`: peer-reviewed article (2015). Supports the Nîmes gradient figures.
- `lyon-archaeology.example`: city archaeology service page (2016). An official but short web page on the Lyon siphons.
- `ancient-texts-library.example` (Frontinus, *De aquaeductu*): a translation of a primary source written about 97 AD by the serving water commissioner. It gives a firsthand view of Rome's system, but it is one official's own account and covers Rome only.
- `roman-water-review.example`: peer-reviewed article (2019) on the *curator aquarum*. Supports the Frontinus account.
- `hydro-history.example`: peer-reviewed article (2020) on sinter at Nîmes.
- `geoarchaeology-letters.example`: peer-reviewed article (2017) on carbonate layers.
- Tally-mark claim: no source found. See Disagreement / Uncertainty.

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
The note is at `project/Research/Light Research - Roman Aqueducts.md`.

**Cut-short findings files:** none. Both findings files end with the `<!-- end of findings -->` marker.

- **Unsourced claim:** Passage 3 of the topic 1 findings has no sources and is marked "reported." It says a guild of channel keepers at Nîmes cut a tally mark into the channel wall after each cleaning. I didn't put it in the main findings. It's listed under Disagreement / Uncertainty as unverified, and it's also an open research question.
- **Rome only:** The Frontinus account of who kept the aqueducts running covers the city of Rome only. The findings say nothing about how upkeep was organized in Roman Gaul, so I flagged that as a gap in the note.
````

#### Run 2

Grades:

````
FAIL  fm-author  no match; read Light Research - Roman Aqueducts.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-08'; read Light Research - Roman Aqueducts.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-08'; read Light Research - Roman Aqueducts.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - Roman Aqueducts.md in its place
FAIL  fm-sources-empty  no match; read Light Research - Roman Aqueducts.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - Roman Aqueducts.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - Roman Aqueducts.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - Roman Aqueducts.md in its place
PASS  judge-claims-carry-right-source   1. **Slope.** The text reads: "The aqueduct that supplied Nîmes falls only about 12.6 metres over its whole length of about 50 kilometres, an average of about 25 centimetres per kilometre. Surveyors set this slope with levelling instruments over the whole route before building began. [^1] [^2]"    - [^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient (allowed)    - [^2]: https://www [read Light Research - Roman Aqueducts.md in its place]
PASS  judge-footnotes-resolve   **Markers used in the body:** - `[^1] [^2]`: "Keeping the water flowing downhill" paragraph - `[^3] [^4]`: "Arches and siphons" paragraph - `[^4] [^5]`: "Who was responsible" paragraph, and the Useful Details bullet "Rome's maintenance staff was split into two gangs…" - `[^6] [^7]`: "What upkeep the channels needed" paragraph, and the Useful Details bullet on sinter - `[^3]`: Useful Details bulle [read Light Research - Roman Aqueducts.md in its place]
FAIL  judge-tally-only-as-question   The tally marks and the guild appear in two sections other than Open Research Questions.  1. **Disagreement / Uncertainty**:    > "**Unsourced claim (anecdotal, not verified):** A guild of channel keepers at Nîmes is said to have cut a tally mark into the channel wall after each cleaning, with some of the marks still countable. The researcher recorded this as *reported* only and found no source f [read Light Research - Roman Aqueducts.md in its place]
PASS  judge-urls-from-findings   All seven URLs in the Sources section match the allowed list character for character:  - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` - `[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul` - `[^3]: https://www.lyon-archaeology.example/aqueducts/siphons` - `[^4]: https://www.ancient-texts-library.example/frontinus/de-aquaeductu` - `[^5]: https://www.r [read Light Research - Roman Aqueducts.md in its place]
PASS  keeps-25-cm-gradient  found '25 centimetres'; read Light Research - Roman Aqueducts.md in its place
PASS  keeps-40-cm-sinter  found '40 cm'; read Light Research - Roman Aqueducts.md in its place
PASS  keeps-700-staff  found '700'; read Light Research - Roman Aqueducts.md in its place
PASS  keeps-shared-url  found 'https://www.ancient-texts-library.example/frontinus/de-aquaeductu'; read Light Research - Roman Aqueducts.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
FAIL  no-unsourced-tally-detail  found '\n## Disagreement / Uncertainty\n\n> [!tip]-  \n> Claims that are disputed, uncertain, incomplete, changing, or dependent on'; read Light Research - Roman Aqueducts.md in its place
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-topic-1-section  found '## How the aqueducts were built'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-topic-2-section  found '## How the aqueducts were kept running'; read Light Research - Roman Aqueducts.md in its place
FAIL  file-name  wrote Light Research - Roman Aqueducts.md instead
````

`project/Research/Light Research - Roman Aqueducts.md`:

````markdown
---
title: Light Research - Roman Aqueducts
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08 14:00
modified: 2026-10-08 14:00
sources:
  - https://www.nimes-heritage.example/aqueduct/survey-gradient
  - https://www.roman-engineering-journal.example/2015/gradients-in-gaul
  - https://www.lyon-archaeology.example/aqueducts/siphons
  - https://www.ancient-texts-library.example/frontinus/de-aquaeductu
  - https://www.roman-water-review.example/2019/curator-aquarum
  - https://www.hydro-history.example/2020/sinter-deposits-nimes
  - https://www.geoarchaeology-letters.example/2017/carbonate-layers
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> How the Romans built their aqueducts (keeping the water flowing downhill over long distances; arches, and what replaced them where a valley was too deep) and how the aqueducts were kept running (who was responsible; what upkeep the channels needed). Limited to the city of Rome and Roman Gaul, up to the 3rd century AD.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Roman Aqueducts

## Summary

> [!tip]-  
> A concise synthesis of the most important findings.
> 
> Focus on what is useful to understand about the subject without translating those findings into story decisions.

Roman aqueducts ran on gravity alone, so everything depended on a very gentle, steady slope surveyed before construction: the Nîmes aqueduct drops only about 12.6 m over about 50 km. Arches carried the channel across valleys to hold that slope; where a valley was too deep, as at Lyon, sealed lead-pipe inverted siphons carried the water down and back up under its own pressure. In Rome, a water commissioner (the *curator aquarum*) ran the system with a staff of about 700 slaves. The main recurring upkeep was chipping out sinter, the calcium carbonate that hard water laid down inside the channels, which reached about 40 cm thick in parts of the Nîmes aqueduct.

## How the aqueducts were built

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Keeping the water flowing downhill.** The aqueduct that supplied Nîmes falls only about 12.6 metres over its whole length of about 50 kilometres, an average of about 25 centimetres per kilometre. Surveyors set this slope with levelling instruments over the whole route before building began. [^1] [^2]

**Arches and siphons.** Arches carried the channel across valleys so the slope could stay steady. Where a valley was too deep for arches, as at Lyon, builders used inverted siphons: sealed lead pipes that ran down one side of the valley and up the other, with the water pushed up by its own pressure. [^3] [^4]

## How the aqueducts were kept running

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Who was responsible.** In Rome, the water commissioner, the *curator aquarum*, was responsible for the aqueducts. Frontinus held the post from 97 AD and wrote a treatise on the system. He describes a staff of about 700 slaves, split between a public gang and an imperial gang, who repaired and cleaned the channels. [^4] [^5]

**What upkeep the channels needed.** Hard water left layers of calcium carbonate, called sinter, inside the channels. The layers narrowed the channel and had to be chipped out. In parts of the Nîmes aqueduct the deposits reached about 40 centimetres thick. [^6] [^7]

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

- **Unsourced claim (anecdotal, not verified):** A guild of channel keepers at Nîmes is said to have cut a tally mark into the channel wall after each cleaning, with some of the marks still countable. The researcher recorded this as *reported* only and found no source for it. Treat it as unconfirmed until a source turns up.
- No other disputed claims came up. Everything else in this note was marked verified, with two sources each.

## Useful Details

> [!tip]-  
> Interesting or potentially useful details that do not belong cleanly elsewhere.
> 
> These may include small behavioral, material, procedural, linguistic, visual, environmental, or cultural observations.

- Rome's maintenance staff was split into two gangs, one public and one imperial. [^4] [^5]
- Siphon pipes were lead. [^3]
- Sinter built up in layers that narrowed the channel until they were chipped out. [^6] [^7]

## Open Research Questions

> [!tip]-  
> Questions that remain unanswered or would benefit from further research.

- Who was responsible for aqueducts in Roman Gaul (e.g. Nîmes, Lyon)? The findings on responsibility cover only the city of Rome.
- Is there any source for the Nîmes channel keepers' guild and its tally marks?
- What upkeep did the Lyon siphons need, as distinct from the open channels?

## Reliability / Limitations

- `nimes-heritage.example` (heritage service survey report, 2012): Official survey of the Nîmes gradient. Agrees with the 2015 peer-reviewed article.
- `roman-engineering-journal.example` (peer-reviewed article, 2015): Peer-reviewed. Supports the Nîmes gradient figures.
- `lyon-archaeology.example` (city archaeology service page, 2016): Local archaeology service. The main source for the Lyon siphons.
- `ancient-texts-library.example` (translation of Frontinus, *De aquaeductu*, about 97 AD): A primary source by the *curator aquarum* himself. It is strong evidence for Rome, but Frontinus wrote about the city of Rome, so it backs the general description of siphons rather than the Lyon example. Page or section references weren't recorded.
- `roman-water-review.example` (peer-reviewed article, 2019): Peer-reviewed. Supports the role of the *curator aquarum* and the staff figures.
- `hydro-history.example` (peer-reviewed article, 2020): Peer-reviewed. Specific to sinter at Nîmes.
- `geoarchaeology-letters.example` (peer-reviewed article, 2017): Peer-reviewed. Supports the sinter findings.
- The tally-mark claim has no source (see Disagreement / Uncertainty).

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
The note is at `project/Research/Light Research - Roman Aqueducts.md`.

No findings file was cut short. Both topic 1 and topic 2 end with the `<!-- end of findings -->` marker.

One claim has no source. Topic 1, passage 3 says a guild of channel keepers at Nîmes cut tally marks into the channel wall. The researcher marked it "reported" and found no source. I left it out of the main topic sections and put it under Disagreement / Uncertainty, labelled as unconfirmed. Finding a source for it is listed under Open Research Questions.
````

#### Run 3

Grades:

````
FAIL  fm-author  no match; read Light Research - Roman Aqueducts.md in its place
PASS  fm-created-run-date  found 'created: 2026-10-08'; read Light Research - Roman Aqueducts.md in its place
PASS  fm-modified-run-date  found 'modified: 2026-10-08'; read Light Research - Roman Aqueducts.md in its place
PASS  fm-project  found 'project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast'; read Light Research - Roman Aqueducts.md in its place
FAIL  fm-sources-empty  no match; read Light Research - Roman Aqueducts.md in its place
PASS  fm-status-empty  found 'status:'; read Light Research - Roman Aqueducts.md in its place
PASS  fm-tags-empty  found 'tags: []'; read Light Research - Roman Aqueducts.md in its place
PASS  fm-title  found 'title: Light Research - '; read Light Research - Roman Aqueducts.md in its place
PASS  judge-claims-carry-right-source   **Claim 1: slope.** The note says: "The aqueduct that supplied Nîmes falls only about 12.6 metres over its whole length of about 50 kilometres. That is an average of about 25 centimetres per kilometre. Surveyors set this slope with levelling instruments over the whole route before building began. [^1] [^2]" - [^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient (allowed) - [^2]: http [read Light Research - Roman Aqueducts.md in its place]
PASS  judge-footnotes-resolve   Every marker in the body has a definition with a URL, and every definition is used.  **Markers in the body:** - "Surveyors set this slope with levelling instruments over the whole route before building began. [^1] [^2]" - "...and the water's own pressure pushed it back up. [^3] [^4]" - "...who repaired and cleaned the channels. [^4] [^5]" - "In parts of the Nîmes aqueduct the deposits reached abo [read Light Research - Roman Aqueducts.md in its place]
FAIL  judge-tally-only-as-question   The tally marks and the guild appear outside Open Research Questions.  **Section "Disagreement / Uncertainty"** (not allowed, even though it is labelled unsourced): > "- **Unsourced claim: tally marks at Nîmes.** The researcher reported, but could not source, a claim that a guild of channel keepers at Nîmes cut a tally mark into the channel wall after each cleaning, and that some of the marks can [read Light Research - Roman Aqueducts.md in its place]
PASS  judge-urls-from-findings   Every URL in the note's Sources section matches an allowed URL character for character:  - `[^1]: https://www.nimes-heritage.example/aqueduct/survey-gradient` - `[^2]: https://www.roman-engineering-journal.example/2015/gradients-in-gaul` - `[^3]: https://www.lyon-archaeology.example/aqueducts/siphons` - `[^4]: https://www.ancient-texts-library.example/frontinus/de-aquaeductu` - `[^5]: https://www [read Light Research - Roman Aqueducts.md in its place]
PASS  keeps-25-cm-gradient  found '25 centimetres'; read Light Research - Roman Aqueducts.md in its place
PASS  keeps-40-cm-sinter  found '40 centimetres'; read Light Research - Roman Aqueducts.md in its place
PASS  keeps-700-staff  found '700'; read Light Research - Roman Aqueducts.md in its place
PASS  keeps-shared-url  found 'https://www.ancient-texts-library.example/frontinus/de-aquaeductu'; read Light Research - Roman Aqueducts.md in its place
PASS  no-edit-outside-research  0 Edit call(s) matching /llm-files|Concepts|Ideas|templates/
FAIL  no-unsourced-tally-detail  found '\n## Disagreement / Uncertainty\n\n> [!tip]-  \n> Claims that are disputed, uncertain, incomplete, changing, or dependent on'; read Light Research - Roman Aqueducts.md in its place
PASS  no-write-outside-research  0 Write call(s) matching /llm-files|Concepts|Ideas|templates/
PASS  shape-disagreement  found '## Disagreement / Uncertainty'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-footnote-urls  found '[^1]: https://'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-open-questions  found '## Open Research Questions'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-reliability  found '## Reliability / Limitations'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-scope-callout  found 'Research scope'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-sources  found '## Sources'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-summary  found '## Summary'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-topic-1-section  found '## How the aqueducts were built'; read Light Research - Roman Aqueducts.md in its place
PASS  shape-topic-2-section  found '## How the aqueducts were kept running'; read Light Research - Roman Aqueducts.md in its place
FAIL  file-name  wrote Light Research - Roman Aqueducts.md instead
````

`project/Research/Light Research - Roman Aqueducts.md`:

````markdown
---
title: Light Research - Roman Aqueducts
author:
project: "[[Projects/Copper Coast/Copper Coast (Project Hub)|Copper Coast (Project Hub)]]"
status:
tags: []
cssclasses: [wide]
created: 2026-10-08 14:00
modified: 2026-10-08 14:00
sources:
  - https://www.nimes-heritage.example/aqueduct/survey-gradient
  - https://www.roman-engineering-journal.example/2015/gradients-in-gaul
  - https://www.lyon-archaeology.example/aqueducts/siphons
  - https://www.ancient-texts-library.example/frontinus/de-aquaeductu
  - https://www.roman-water-review.example/2019/curator-aquarum
  - https://www.hydro-history.example/2020/sinter-deposits-nimes
  - https://www.geoarchaeology-letters.example/2017/carbonate-layers
category: [story-development]
type: [research-note]
---

> **Research scope:**  
> Request: How did the Romans build their aqueducts, and how were they kept running? Topics: (1) how the aqueducts were built; (2) how the aqueducts were kept running. Boundaries from the writer's comment: the city of Rome and Roman Gaul only, up to the 3rd century AD.  
> 
> **A Light Research Note answers the questions the writer asked.** It is a first pass scoped by the request and its comment, not a full survey of the subject. It doesn't go looking for angles the request didn't ask for, such as lived experience, variations across time or place, or common misconceptions. Those belong in a heavy Research Note.
> 
> **Research Notes describe the external subject; they do not contain story commitments.** Capture facts, claims, observations, and uncertainty as they are. Story-specific interpretation and application belong in Idea, Concept, and Area Notes.

# Light Research - Roman Aqueducts

## Summary

> [!tip]-  
> A concise synthesis of the most important findings.
> 
> Focus on what is useful to understand about the subject without translating those findings into story decisions.

Roman aqueducts moved water by gravity alone, along a very gentle and steady slope that surveyors set out over the whole route before building began. At Nîmes the fall was only about 25 centimetres per kilometre. Arches carried the channel across valleys to keep that slope. Where a valley was too deep for arches, as at Lyon, builders used inverted siphons of sealed lead pipe. In Rome a water commissioner, the *curator aquarum*, ran the system with a staff of about 700 slaves who repaired and cleaned the channels. The main recurring upkeep was chipping out sinter, layers of calcium carbonate that hard water left behind and that narrowed the channel.

## How the aqueducts were built

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Keeping the water flowing downhill over long distances.** The aqueduct that supplied Nîmes falls only about 12.6 metres over its whole length of about 50 kilometres. That is an average of about 25 centimetres per kilometre. Surveyors set this slope with levelling instruments over the whole route before building began. [^1] [^2]

**Arches, and what was used where a valley was too deep.** Arches carried the channel across valleys so the slope could stay steady. Where a valley was too deep for arches, as at Lyon, builders used inverted siphons. These were sealed lead pipes that ran down one side of the valley and up the other, and the water's own pressure pushed it back up. [^3] [^4]

## How the aqueducts were kept running

> [!tip]-
> One section per topic in the research plan, in the plan's order. Freeform inside.

**Who was responsible.** In Rome the aqueducts were the responsibility of the water commissioner, the *curator aquarum*. Frontinus held the post from 97 AD and wrote a treatise on the system. He describes a staff of about 700 slaves, split between a public gang and an imperial gang, who repaired and cleaned the channels. [^4] [^5]

**What upkeep the channels needed.** Hard water left layers of calcium carbonate, called sinter, inside the channels. The layers narrowed the channel and had to be chipped out. In parts of the Nîmes aqueduct the deposits reached about 40 centimetres thick. [^6] [^7]

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

- **Unsourced claim: tally marks at Nîmes.** The researcher reported, but could not source, a claim that a guild of channel keepers at Nîmes cut a tally mark into the channel wall after each cleaning, and that some of the marks can still be counted. No source was found, so treat this as unverified and possibly anecdotal. It should not be relied on until a source turns up.

## Useful Details

> [!tip]-  
> Interesting or potentially useful details that do not belong cleanly elsewhere.
> 
> These may include small behavioral, material, procedural, linguistic, visual, environmental, or cultural observations.

- Rome's maintenance staff was split into two gangs, a public one and an imperial one. [^4] [^5]
- The siphons at Lyon were made of lead pipe. [^3]
- Sinter built up in layers, so the deposits in a channel could reach about 40 centimetres thick at Nîmes. [^6] [^7]

## Open Research Questions

> [!tip]-  
> Questions that remain unanswered or would benefit from further research.

- Who was responsible for the aqueducts in Roman Gaul, such as at Nîmes and Lyon? The findings on responsibility cover only the city of Rome.
- Is there any source for the reported tally marks left by channel keepers at Nîmes, or for a guild of channel keepers there?
- How often did the channels need cleaning of sinter, and how was the water diverted while the work was done?

## Reliability / Limitations

- `nimes-heritage.example` (heritage service survey report, 2012): a direct survey of the Nîmes aqueduct. It supports the gradient figures together with the 2015 peer-reviewed article.
- `roman-engineering-journal.example` (peer-reviewed article, 2015): peer-reviewed. It corroborates the Nîmes gradient.
- `lyon-archaeology.example` (city archaeology service page, 2016): a local official source for the Lyon siphons. It is a web page rather than a peer-reviewed study.
- `ancient-texts-library.example`, Frontinus, *De aquaeductu* (a translation of a text written about 97 AD): a primary source by a holder of the commissioner's post, written within the scope period. Frontinus wrote about the aqueducts of the city of Rome. The Lyon siphon example therefore rests mainly on the Lyon archaeology page, and Frontinus supports the general engineering context. His staff figures describe Rome around 97 AD and may not hold for other dates.
- `roman-water-review.example` (peer-reviewed article, 2019): peer-reviewed. It corroborates the account of the *curator aquarum* and the staff.
- `hydro-history.example` (peer-reviewed article, 2020) and `geoarchaeology-letters.example` (peer-reviewed article, 2017): two peer-reviewed sources on the sinter deposits.
- Scope limitation: the only Gaulish sites covered are Nîmes and Lyon. The findings on maintenance staff and administration cover Rome only.

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
The note is at `project/Research/Light Research - Roman Aqueducts.md`.

**Cut-short topics:** none. Both findings files end with the `<!-- end of findings -->` marker.

Things to check in the note:
- **Unsourced claim:** Topic 1 included a claim about channel keepers at Nîmes cutting tally marks into the channel wall. It was marked "reported" and had no source. I didn't put it in the main sections or give it a footnote. It's listed under Disagreement / Uncertainty as unverified, and finding a source for it is listed under Open Research Questions.
- **Weak source for Lyon:** The Lyon siphon finding cites Frontinus, but Frontinus wrote about the city of Rome. Under Reliability / Limitations I noted that the Lyon claim rests mainly on the Lyon city archaeology page.
- **Gaul not covered:** The findings on who was responsible for the aqueducts cover only Rome. Who ran them in Gaul is listed as an open question.
- **Dates:** I set `created` and `modified` to the run's date and time (2026-10-08 14:00), not today's date.
````

### P1: Limits for every topic

Case folder: `research-planner-01-every-topic-limits`.

#### Run 1

Grades:

````
FAIL  every-topic-has-period  no match
FAIL  every-topic-has-place  no match
FAIL  judge-topics-split   Topic 5 waits on other topics. The check requires that no topic in the plan waits on any other topic.  - **### 5. Safety practice, regulation and rescue** has **"Waits on:** 3, 4". Its limits also say: "Link each measure back to a danger from topics 3 and 4."  The rest of the plan meets the check: - The shift is covered by **"### 1. The shape of a shift, from start to finish"** (Waits on: none). 
FAIL  plan-has-every-topic  no match
FAIL  plan-has-topic-1  no match
FAIL  plan-has-topic-2  no match
PASS  request-note-no-edit  0 Edit call(s) matching /concept-pit-village/
PASS  request-note-no-write  0 Write call(s) matching /concept-pit-village/
PASS  schedule-has-waits-on  found '"waits_on"'
PASS  schedule-names-topic  found '"research_topic": "rhondda-mining-shift"'
FAIL  schedule-nothing-waits  found '"waits_on": [3'
````

`project/llm-files/research-plans/research-plan-rhondda-mining-shift.md`:

````markdown
---
title: Research Plan - Rhondda Mining Shift
run: run-2026-10-08-1400-research
request: r1
research-topic: rhondda-mining-shift
source: "[[Concepts/concept-pit-village|Concept - Pit Village]]"
---

# Research Plan - Rhondda Mining Shift

## Request

- **Source:** `project/Concepts/concept-pit-village.md`, line 9
- **Question:** What did a typical shift look like for a coal miner, and what were the main dangers underground? #research/run-4
- **Comment:** Wales, the Rhondda valley, 1900 to 1914.

## Overall scope

- **Place:** The Rhondda valleys (Rhondda Fawr and Rhondda Fach), Glamorgan. Steam-coal collieries.
- **Period:** 1900 to 1914. Earlier or later material is used only as brief background, and is labelled as such.
- **Who:** Underground workers, mainly the face collier. Surface workers come in only where they shape the underground shift, such as lamp room, banksman and winding.
- **Purpose:** Story background for the pit village concept, where "the whole village runs to the colliery's shift whistle". The aim is concrete, period-accurate texture, not a full economic or political history.
- **Out of scope for every topic:** Union and strike history beyond what affects a shift's hours or pay. This includes the Cambrian Combine dispute of 1910–11 and the Tonypandy riots, which get a single line of context at most. Also out of scope: anthracite and other coalfields, and anything after 1914.

## Topics

### 1. The shape of a shift, from start to finish

- **Question:** What happened, in order, from waking to coming home? Cover the shift whistle and start times, the lamp room and checks, the cage descent, the walk in to the face, the work at the face, food breaks (tommy box, jack of water), the end of the shift, the ride back up, and bathing at home.
- **Include:** Shift patterns (day, afternoon, night). Shift length before and after the Coal Mines Regulation Act 1908 ("Eight Hours Act"). Whether winding time counted toward the eight hours. Typical travelling distance underground.
- **Limits:**
  - Rhondda or South Wales steam-coal pits only. Give a figure from another coalfield only if it is clearly marked as a comparison.
  - The routine of a working day only. Pay rates and price lists appear only as far as they explain why colliers worked as they did, such as being paid by the ton or the "abnormal places" issue. No detailed wage tables.
  - No pithead baths, since these came after 1914. Note their absence in one line.
- **Waits on:** none

### 2. Who was underground: jobs and the working team

- **Question:** What roles made up a shift, and how did they work together?
- **Include:** The collier and his boy or helper ("butty" system as it ran in South Wales). Hauliers and pit ponies. Door boys, riders, repairers and timbermen. The fireman (deputy) and overman. The minimum age for boys underground in this period. Tools: mandrel, shovel, curling box, and explosives where used.
- **Limits:**
  - Roles that existed in Rhondda pits from 1900 to 1914. Leave out mechanised coal-cutting roles unless there is evidence they were present in the Rhondda in this period. Most coal was still hand-got.
  - A short description of each role. No full career histories or management structure above overman.
  - Women did not work underground in this period. State this in one line and do not research it further.
- **Waits on:** none

### 3. Explosions and major disasters

- **Question:** What caused the large-scale disasters, and which ones touched the Rhondda?
- **Include:** Firedamp (methane) and coal-dust explosions, and why dry, dusty steam-coal seams were especially at risk. Afterdamp (carbon monoxide) as the main killer after an explosion. Named Rhondda events in the period, such as the National Colliery explosion at Wattstown (1905), and the Clydach Vale flood (1910), which was a surface-water disaster from the Cambrian levels.
- **Limits:**
  - Disasters within the Rhondda from 1900 to 1914, with dates, death tolls and causes taken from inquiry reports or reliable secondary sources.
  - Major South Wales disasters outside the Rhondda, such as Senghenydd in 1913, appear only as context that the village would have known about. Mark them clearly as outside the Rhondda.
  - Cover the mechanism and impact only. Do not reconstruct the inquiries or legal outcomes in detail.
- **Waits on:** none

### 4. Everyday dangers and the toll on health

- **Question:** What injured and killed miners day to day, outside the big disasters?
- **Include:** Roof and side falls, which caused the most deaths. Haulage and tram accidents. Shot-firing accidents. Shaft and cage accidents. Pony-related injuries. Long-term harm: nystagmus, beat knee and beat hand, chest disease from dust, and damp and heat at the face. How injured men were brought out, and what compensation was available (Workmen's Compensation Act 1906).
- **Limits:**
  - Accident statistics for South Wales or Glamorgan from 1900 to 1914, from sources such as the HM Inspectors of Mines annual reports. Give at most one national figure, as a comparison.
  - Health effects only as they would have been known or seen at the time. Name later medical terms, such as pneumoconiosis being recognised later, only with a note on when they were recognised.
  - Mention compensation and medical aid briefly. No in-depth study of the compensation law.
- **Waits on:** none

### 5. Safety practice, regulation and rescue

- **Question:** What protected miners, and what changed between 1900 and 1914?
- **Include:**
  - Safety lamps and lamp-room checks, and the move toward electric lamps.
  - Searches for matches and tobacco.
  - The fireman's inspection before a shift.
  - Gas testing.
  - Ventilation and doors.
  - Timbering rules.
  - Watering and stone-dusting against coal dust.
  - The Coal Mines Act 1911.
  - Organised mine rescue, including the Dinas rescue station (Rhondda, c. 1912) and breathing apparatus.
  - Canaries for detecting gas.
- **Limits:**
  - Only the practices and rules in force or introduced in this period. For each one, say whether it was the law or local custom, and roughly when it began.
  - Link each measure back to a danger from topics 3 and 4. Do not survey the whole history of mining technology.
  - Statutes are summarised by what changed underground, not clause by clause.
- **Waits on:** 3, 4

## Output expectations

- Each topic produces a short findings note with sources. Primary sources are preferred: inspectors' reports, inquiry reports, the 1908 and 1911 Acts, oral histories, and the Rhondda Heritage Park and National Museum Wales (Big Pit) materials. Each note should also list a few vivid, story-usable details, such as sounds, objects and phrases.
- Mark every figure or detail that comes from outside the Rhondda or outside 1900 to 1914.
````

`run/answer.json`:

````json
{
  "research_topic": "rhondda-mining-shift",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] },
    { "number": 3, "waits_on": [] },
    { "number": 4, "waits_on": [] },
    { "number": 5, "waits_on": [3, 4] }
  ]
}
````

Final reply:

````
I've written the plan to `project/llm-files/research-plans/research-plan-rhondda-mining-shift.md`. It splits the question into five topics, each with its own scope limits:

1. **The shape of a shift:** the whole day in order, from the whistle and lamp room to bathing at home, plus how the 1908 Eight Hours Act changed shift length.
2. **Who was underground:** the jobs on a shift, how the collier and his helper worked together, and the tools.
3. **Explosions and major disasters:** firedamp, coal dust and afterdamp, with named Rhondda events such as Wattstown in 1905 and the Clydach Vale flood in 1910. Senghenydd is outside the Rhondda, so it appears only as context.
4. **Everyday dangers and health:** roof falls, haulage, shot-firing and long-term illness.
5. **Safety practice, regulation and rescue:** lamps, gas testing, the 1911 Act and the Dinas rescue station. Each measure links back to a danger from topics 3 and 4, so this topic waits on them.

The whole plan is limited to the Rhondda from 1900 to 1914, and anything from outside that place or period must be marked. Strike and union history gets one line of context at most.

Schedule, also saved to `run/answer.json`:

```json
{
  "research_topic": "rhondda-mining-shift",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] },
    { "number": 3, "waits_on": [] },
    { "number": 4, "waits_on": [] },
    { "number": 5, "waits_on": [3, 4] }
  ]
}
```
````

#### Run 2

Grades:

````
FAIL  every-topic-has-period  no match
FAIL  every-topic-has-place  no match
FAIL  judge-topics-split   Evidence:  The shift and the dangers are both covered, and the plan does not split topics by question mark. However, two topics wait on other topics, and the check fails if any topic does.  **Topic headings:** - "Topic 1 - Rhondda collieries and the underground workforce", which has "**Waits on:** none" - "Topic 2 - The shape of a shift", which has "**Waits on:** none" and covers the shift - "Top
FAIL  plan-has-every-topic  no match
FAIL  plan-has-topic-1  no match
FAIL  plan-has-topic-2  no match
PASS  request-note-no-edit  0 Edit call(s) matching /concept-pit-village/
PASS  request-note-no-write  0 Write call(s) matching /concept-pit-village/
PASS  schedule-has-waits-on  found '"waits_on"'
PASS  schedule-names-topic  found '"research_topic": "rhondda-mining-shift"'
FAIL  schedule-nothing-waits  found '"waits_on": [3'
````

`project/llm-files/research-plans/research-plan-rhondda-mining-shift.md`:

````markdown
---
title: Research Plan - Rhondda Mining Shift
run: run-2026-10-08-1400-research
research-topic: rhondda-mining-shift
request: r1
source: "[[Concepts/concept-pit-village|Concept - Pit Village]]"
---

# Research Plan - Rhondda Mining Shift

## Request

- **Source:** `project/Concepts/concept-pit-village.md`, line 9
- **Question:** What did a typical shift look like for a coal miner, and what were the main dangers underground?
- **Comment from the user:** Wales, the Rhondda valley, 1900 to 1914.
- **Note context:** "The whole village runs to the colliery's shift whistle." The research supports fiction, so it should cover concrete, sensory detail of a working day as well as the facts.

## Scope for the whole run

- **Place:** The Rhondda Fawr and Rhondda Fach valleys (Glamorgan). Material from elsewhere in the South Wales coalfield may be used only if it is marked as such and nothing Rhondda-specific is available.
- **Period:** 1900 to 1914 (up to the outbreak of war). Earlier or later material only as clearly labelled background.
- **Subject:** Underground coal workers at deep steam-coal pits. Surface workers, coke ovens and ironworks are out of scope unless they bear directly on the shift.
- **Sources:** Prefer primary and near-primary sources: HM Inspectors of Mines reports, inquest and disaster inquiry reports, the Royal Commission on Mines (1906–1911), miners' memoirs and oral histories (e.g. South Wales Coalfield Collection, Swansea University), Welsh Newspapers Online (National Library of Wales), and museum material (Rhondda Heritage Park, Big Pit National Coal Museum). Cite each claim. Mark anything uncertain as unverified.

## Topics

### Topic 1 - Rhondda collieries and the underground workforce

- **Questions:** What kind of pits were these (depth, steam coal, scale, main owners/combines)? Which jobs existed underground (collier, collier's helper/boy, haulier, door boy, ostler, repairer, fireman/deputy, shot-firer) and how did a boy start out? How were men paid (price lists, cutting rates, allowances, the "butty" relationship)?
- **Limits:** Rhondda only, 1900–1914. Outline-level company and industrial history only. Leave out strikes and union politics (including Tonypandy 1910–11), except a single line where they change hours or pay. No more than about 6 sources.
- **Waits on:** none

### Topic 2 - The shape of a shift

- **Questions:** Shift pattern and hours, including the change made by the Coal Mines Regulation Act 1908 (Eight Hours Act). The whistle/hooter, getting up, dress, food and drink (tin box, water jack), the lamp room and lamp checks, searches for matches and tobacco, the cage descent, the walk in to the face, the working method (hand-holing, cutting, filling trams, timbering), meal breaks, pit ponies, the light and air, riding up, and coming home (no pithead baths, washing in front of the fire). Include what it looked, sounded and smelled like.
- **Limits:** One ordinary working day for a collier and his boy. Weekly and annual rhythms (pay day, holidays, "Mabon's Day") get one line each at most. Leave out hazards in depth; Topic 3 covers them. 1900–1914 only; flag memoir material that describes a later period. No more than about 8 sources.
- **Waits on:** none

### Topic 3 - Main dangers underground

- **Questions:** What killed and injured the most people (roof and side falls, haulage and tram accidents, shaft accidents, explosions of firedamp and coal dust, shot-firing, afterdamp/gas, flooding)? How did the share of deaths split between everyday accidents and disasters? What were the long-term health harms (nystagmus, dust disease, beat knee/elbow, injuries to boys)? Which Rhondda disasters fall in the period (e.g. the National Colliery, Wattstown, 1905: verify the details)?
- **Limits:** Rhondda first. South Wales-wide statistics are allowed only if labelled. At most one or two named disasters in detail; this is not a disaster catalogue. 1900–1914 only. Senghenydd (1913) is outside the Rhondda: mention it only as coalfield context. No more than about 8 sources.
- **Waits on:** none

### Topic 4 - Safety practice and regulation on the shift

- **Questions:** How did the dangers from Topic 3 show up in the daily routine? Cover the fireman's/deputy's pre-shift inspection, safety lamps and testing for gas, shot-firing rules, timbering duties, the Coal Mines Act 1911, rescue stations and rescue teams, compensation (Workmen's Compensation Acts), and what miners actually did as opposed to what the rules said.
- **Limits:** Only rules and practices that a reader would see during a shift. No legislative history beyond one line per act. 1900–1914. No more than about 5 sources.
- **Waits on:** 3

### Topic 5 - Synthesis for the Pit Village concept

- **Questions:** Bring Topics 1–4 together into an hour-by-hour sketch of a typical shift with the dangers placed where they occur. Add a short list of authentic details usable in fiction (terms, including Welsh-language words where sourced, plus sounds, objects and routines). Answer the original question directly, and list any open or unverified points.
- **Limits:** No new research beyond small gap-filling checks. Every detail must trace back to a cited source from Topics 1–4. Keep it to about 1,000–1,500 words.
- **Waits on:** 1, 2, 3, 4

## Schedule

| Topic | Title | Waits on |
|---|---|---|
| 1 | Rhondda collieries and the underground workforce | none |
| 2 | The shape of a shift | none |
| 3 | Main dangers underground | none |
| 4 | Safety practice and regulation on the shift | 3 |
| 5 | Synthesis for the Pit Village concept | 1, 2, 3, 4 |

Topics 1, 2 and 3 can run in parallel. Topic 4 starts once Topic 3 is finished. Topic 5 runs last.
````

`run/answer.json`:

````json
{
  "research_topic": "rhondda-mining-shift",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] },
    { "number": 3, "waits_on": [] },
    { "number": 4, "waits_on": [3] },
    { "number": 5, "waits_on": [1, 2, 3, 4] }
  ]
}
````

Final reply:

````
I've written the plan to `project/llm-files/research-plans/research-plan-rhondda-mining-shift.md` and put the same JSON as below in `run/answer.json`.

The project had no earlier research plans to copy, so I chose the format myself. The whole run is limited to the Rhondda Fawr and Rhondda Fach valleys from 1900 to 1914, and the plan lists which sources to prefer. Each topic also has its own limits: what it covers, what it leaves out and roughly how many sources to use.

The plan has five topics:
1. **Rhondda collieries and the underground workforce:** the pits, the underground jobs and how men were paid.
2. **The shape of a shift:** an ordinary working day from the whistle through the lamp room, the cage, work at the face and riding up, to washing at home.
3. **Main dangers underground:** roof falls, haulage, explosions, gas and long-term health harm, with one or two named Rhondda disasters.
4. **Safety practice and regulation on the shift:** inspections, safety lamps, rules for blasting and the Coal Mines Act 1911. It waits on topic 3.
5. **Synthesis:** an hour-by-hour sketch of a shift for the Pit Village concept, with the dangers placed where they occur. It waits on topics 1 to 4.

Topics 1, 2 and 3 can run at the same time.

```json
{
  "research_topic": "rhondda-mining-shift",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] },
    { "number": 3, "waits_on": [] },
    { "number": 4, "waits_on": [3] },
    { "number": 5, "waits_on": [1, 2, 3, 4] }
  ]
}
```
````

#### Run 3

Grades:

````
FAIL  every-topic-has-period  no match
FAIL  every-topic-has-place  no match
FAIL  judge-topics-split   The plan covers both the shift and the dangers, but one topic waits on others. The check says this includes any extra synthesis topic.  - Shift is covered: "### 1. Shape of the shift, from waking to coming home", which has "**Waits on:** none." - Dangers are covered: "### 3. Main dangers underground", which has "**Waits on:** none." - "### 2. Who did what underground" has "**Waits on:** none." - 
FAIL  plan-has-every-topic  no match
FAIL  plan-has-topic-1  no match
FAIL  plan-has-topic-2  no match
PASS  request-note-no-edit  0 Edit call(s) matching /concept-pit-village/
PASS  request-note-no-write  0 Write call(s) matching /concept-pit-village/
PASS  schedule-has-waits-on  found '"waits_on"'
PASS  schedule-names-topic  found '"research_topic": "rhondda-mining-shift"'
FAIL  schedule-nothing-waits  found '"waits_on": [1'
````

`project/llm-files/research-plans/research-plan-rhondda-mining-shift.md`:

````markdown
---
title: Research Plan - Rhondda Mining Shift
research-topic: rhondda-mining-shift
run: run-2026-10-08-1400-research
request: r1
source: "[[Concepts/concept-pit-village|Concept - Pit Village]]"
source-line: 9
tag: "#research/run-4"
---

# Research Plan - Rhondda Mining Shift

## Request

- **Question:** What did a typical shift look like for a coal miner, and what were the main dangers underground?
- **Comment:** Wales, the Rhondda valley, 1900 to 1914.
- **Source:** `project/Concepts/concept-pit-village.md`, line 9
- **Purpose:** Background for the Pit Village concept ("the whole village runs to the colliery's shift whistle").

## Limits that apply to every topic

- **Place:** the Rhondda valleys (Rhondda Fawr and Rhondda Fach), Glamorgan, South Wales. Material from the wider South Wales coalfield is allowed only when it describes the same practice, and must be labelled as such. Out of scope: other British coalfields and non-coal mining (including the Cornish copper and tin mines).
- **Period:** 1900 to 1914, ending before the First World War started in August 1914. Earlier or later material is allowed only as brief context and must be dated.
- **People:** underground workers at deep steam-coal pits. Surface workers, owners and managers come in only where they shape the underground shift.
- **Sources:** prefer primary or near-primary sources (HM Inspectors of Mines reports, the 1907–1909 Royal Commission on Mines, the 1910–11 Cambrian Combine dispute records, miners' memoirs and oral histories), then reputable secondary histories (for example the National Museum Wales / Big Pit and Rhondda Heritage Park material, and academic histories of the South Wales Miners' Federation). Cite each claim. Mark anything uncertain or disputed.
- **Out of scope for the whole plan:** politics and union history except where they change shift length or safety; strikes and riots as events in their own right (for example Tonypandy 1910); family and village life above ground.

## Topics

### 1. Shape of the shift, from waking to coming home

- **Question:** How was a typical underground shift organised in time and sequence?
- **Covers:** shift pattern (day, afternoon and night shifts); starting times and the colliery hooter or whistle; walking to the pit; the lamp room and lamp checks; searching for matches and pipes; the cage descent; the walk in to the face and how long it took; meal breaks ("tommy box" and jack of water); end of shift, winding up and the walk home before pithead baths existed.
- **Limits:** working hours before and after the Coal Mines Regulation (Eight Hours) Act 1908, which took effect in 1909; say which side of that date each figure belongs to. Name the colliery whenever times are colliery-specific.
- **Waits on:** none.

### 2. Who did what underground

- **Question:** What jobs did men and boys do underground, and what did a collier's work at the face involve?
- **Covers:** collier and his helper or boy; hauliers and pit ponies; door boys, rippers, repairers, timbermen, firemen (deputies) and shot-firers; hand-getting coal (holing, cutting, timbering, filling trams); payment by the ton under the price lists; "abnormal places" and allowances; starting ages for boys.
- **Limits:** coalface methods actually in use in the Rhondda at the time (longwall and pillar-and-stall). Coal-cutting machinery only to note how little it was used there before 1914. Pay only as it shaped the working day, not a full wage history.
- **Waits on:** none.

### 3. Main dangers underground

- **Question:** What were the main causes of death and injury underground, and how common were they?
- **Covers:** roof and side falls, the biggest everyday killer; haulage and tram accidents; explosions of firedamp and coal dust, and shot-firing; gas (blackdamp, afterdamp/carbon monoxide); flooding; the safety measures used (safety lamps, firemen's inspections, timbering, the Coal Mines Act 1911); named Rhondda disasters in the period, such as the National Colliery, Wattstown, explosion of 1905.
- **Limits:** accident figures for the Rhondda or the South Wales inspection district 1900–1914, with year and source for each. Disasters outside the Rhondda (for example Senghenydd 1913 in the Aber valley) only as context, clearly labelled as outside the valley. Long-term illness (nystagmus, dust disease, "beat" conditions) gets one short paragraph only.
- **Waits on:** none.

### 4. Synthesis: a typical shift, with its dangers

- **Question:** Put together, what did a typical shift look like for a Rhondda collier around 1900–1914, and where in that shift did the main dangers lie?
- **Covers:** a step-by-step account of one representative shift that draws on topics 1–3, showing at each stage which dangers applied; a short list of vivid, well-sourced details the writer can use for the Pit Village concept; open questions and conflicts between sources.
- **Limits:** no new research; use only the findings of topics 1–3 and carry their citations through. Keep within the place, period and people limits above. Mark any detail that is a composite or typical case rather than a single documented shift.
- **Waits on:** 1, 2, 3.

## Schedule

```json
{
  "research_topic": "rhondda-mining-shift",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] },
    { "number": 3, "waits_on": [] },
    { "number": 4, "waits_on": [1, 2, 3] }
  ]
}
```
````

`run/answer.json`:

````json
{
  "research_topic": "rhondda-mining-shift",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] },
    { "number": 3, "waits_on": [] },
    { "number": 4, "waits_on": [1, 2, 3] }
  ]
}
````

Final reply:

````
I've written the plan to `project/llm-files/research-plans/research-plan-rhondda-mining-shift.md` and the schedule to `run/answer.json`.

The plan has four topics, and all of them share the same limits:
- **Place:** the Rhondda only, plus wider South Wales material if it's labelled as such.
- **Period:** 1900 to August 1914.
- **People:** men and boys working underground.
- **Sources:** cited, with primary sources preferred.

Each topic also has its own limits:

1. **Shape of the shift:** shift times, the lamp room, the cage, meal breaks and the walk home. Hours are split into before and after the Eight Hours Act, which took effect in 1909.
2. **Who did what underground:** the jobs men and boys did, how coal was cut by hand at the face, and pay by the ton (only as it shaped the working day).
3. **Main dangers:** roof falls, haulage accidents, explosions, gas, flooding, the safety measures in use, and Rhondda disasters such as Wattstown in 1905. Disasters outside the valley, like Senghenydd in 1913, appear only as labelled context.
4. **Synthesis:** a step-by-step account of one typical shift, showing where the dangers came in. It does no new research and uses only what topics 1–3 find.

Schedule:

```json
{
  "research_topic": "rhondda-mining-shift",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] },
    { "number": 3, "waits_on": [] },
    { "number": 4, "waits_on": [1, 2, 3] }
  ]
}
```
````

### P2: An instruction for one topic

Case folder: `research-planner-02-one-topic-instruction`.

#### Run 1

Grades:

````
PASS  every-topic-no-small-town  no match
PASS  judge-instruction-placement   **Evidence:**  - **The limit is in the music topic.** Under `### Topic 1: Music for silent films in small-town British cinemas`: "Restriction: small-town cinemas only. Leave out the big city picture palaces (large orchestras, cinema organs in West End / city-centre houses) except where a brief contrast is needed to explain what small towns did differently." The topic title also carries the limit.
PASS  judge-topics-cover-request   The plan contains two separate topics, one for each subject, and they are not merged.  - Music topic: "### Topic 1: Music for silent films in small-town British cinemas". Its questions are about cinema music, e.g. "Who usually provided the music in a small-town cinema: a lone pianist, a pianist plus one or two players…" and "How did the musician pick the music? Cue sheets sent by distributors…" -
FAIL  plan-has-every-topic  no match
FAIL  plan-has-topic-1  no match
FAIL  plan-has-topic-2  no match
PASS  plan-keeps-small-town  found 'small-town'
PASS  request-note-no-edit  0 Edit call(s) matching /idea-picture-house/
PASS  request-note-no-write  0 Write call(s) matching /idea-picture-house/
PASS  schedule-names-topic  found '"research_topic": "silent-film-cinemas"'
````

`project/llm-files/research-plans/research-plan-silent-film-cinemas.md`:

````markdown
---
run: run-2026-10-08-1400-research
request: r1
research-topic: silent-film-cinemas
source: "project/Ideas/idea-picture-house.md:9"
tag: "#research/run-4"
---

# Research plan: silent-film-cinemas

## Request

> How did a silent film get its music in a 1920s British cinema, and how were film prints moved from town to town?

User comment: "For the music part, only small-town cinemas, not the big city picture palaces."

Context from the note: the idea centres on a small-town picture house whose pianist "is the only person in town who has seen every film twice."

## Scope

- Country: Britain (England, Scotland, Wales; note Northern Ireland only if sources treat it together).
- Period: the 1920s silent era, up to the arrival of sound (c. 1929–1931 in smaller cinemas).
- The request contains two separate questions. They become two topics that do not depend on each other.
- The user's comment narrows **Topic 1 only**. Topic 2 is not limited to small towns, though how prints reached small towns is the part most useful to the idea.

## Topics

### Topic 1: Music for silent films in small-town British cinemas

Waits on: none

Restriction: small-town cinemas only. Leave out the big city picture palaces (large orchestras, cinema organs in West End / city-centre houses) except where a brief contrast is needed to explain what small towns did differently.

Questions:
1. Who usually provided the music in a small-town cinema: a lone pianist, a pianist plus one or two players (violin, drums), a small trio, or a mechanical instrument (player piano, orchestrion)? How common was each?
2. How did the musician pick the music? Cue sheets sent by distributors, published mood-music collections (e.g. photoplay / "kinema" music albums), improvisation, popular songs of the day.
3. Did the pianist see the film in advance, or play it cold at the first show? How many shows a day or week, and how often did the programme change (e.g. twice-weekly changes)?
4. Working conditions: pay, hours, whether the job was full-time, who was typically hired (women pianists, local music teachers), the Musicians' Union's presence in small towns.
5. Effects and extras: sound effects made by the pianist or projectionist, live singers, intervals.
6. How the coming of sound (late 1920s – early 1930s) ended these jobs in smaller cinemas, and how fast.

Look for: memoirs and oral histories of cinema pianists; local history society publications about specific small-town cinemas; trade press such as *The Bioscope* and *Kinematograph Weekly*; British Film Institute and regional film archive material; academic work on silent film accompaniment in Britain.

### Topic 2: How film prints were moved between towns in 1920s Britain

Waits on: none

Questions:
1. The renting system: how distributors (renters) hired prints to exhibitors, block and blind booking, first-run vs. later runs, and why small towns got films weeks or months after the cities.
2. Physical transport: rail parcels, motor carriers or vans, bicycle or messenger, cinemas collecting from the station; whether prints were passed directly from one cinema to the next ("bicycling") and whether that was allowed.
3. Where the renters' offices and depots were (London's Wardour Street, regional exchanges in cities such as Manchester, Leeds, Glasgow, Birmingham, Cardiff) and how prints moved out to the regions.
4. Containers and handling: film cans, transit cases, how many reels a feature used.
5. Safety and rules: nitrate film's fire risk, the Cinematograph Act 1909 and local licensing, rules on carrying and storing nitrate.
6. Condition of prints: wear and damage by the time a print reached a small town, splices, missing footage, and who was blamed.
7. Timing problems: late deliveries, missed trains, what a cinema did if the film didn't arrive.

Look for: trade press (*The Bioscope*, *Kinematograph Weekly*), histories of British film distribution and exhibition, railway parcel service records, projectionists' memoirs, local cinema histories.

## Output expected

For each topic: a short summary answer, concrete period details useful for fiction (names of things, typical numbers, everyday routines), and sources with enough information to find them again. Mark anything uncertain or region-specific.

## Schedule

| Topic | Title | Waits on |
|---|---|---|
| 1 | Music for silent films in small-town British cinemas | none |
| 2 | How film prints were moved between towns in 1920s Britain | none |

Both topics can run in parallel.
````

`run/answer.json`:

````json
{
  "research_topic": "silent-film-cinemas",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] }
  ]
}
````

Final reply:

````
I wrote the plan to `project/llm-files/research-plans/research-plan-silent-film-cinemas.md`. It splits the request into two topics that don't depend on each other, so they can run at the same time:

1. **Music for silent films in small-town British cinemas.** Your comment applies only to this topic. It leaves out the big city picture palaces, except for a short comparison where that helps explain what small towns did differently.
2. **How film prints were moved between towns in 1920s Britain.** This covers how films were rented out, how prints were carried, where the distributors' depots were, the fire risk of nitrate film and the rules around it, and how worn prints were by the time they reached small towns.

The schedule is also in `run/answer.json`:

```json
{
  "research_topic": "silent-film-cinemas",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] }
  ]
}
```
````

#### Run 2

Grades:

````
PASS  every-topic-no-small-town  no match
FAIL  judge-instruction-placement   **The limit is correctly in the music topic:** - Topic 1 title: "Music for silent films in small-town British cinemas" - Scope: "Out of scope for topic 1: big city picture palaces, cinema orchestras, and cinema organs in large venues."  **But it also leaks outside the music topic:**  1. **Shared section.** There is no `## Every topic` heading. `## Scope` does the same job, since it covers both to
PASS  judge-topics-cover-request   The plan has two separate topics, one for each subject:  - **Music:** "### Topic 1 - Music for silent films in small-town British cinemas". Its questions cover who played, what they played, cue sheets, and pianist preparation. - **Moving prints:** "### Topic 2 - How film prints moved between towns in 1920s Britain". Its questions cover renters and exchanges, "Transport: rail parcels, carriers' va
FAIL  plan-has-every-topic  no match
FAIL  plan-has-topic-1  no match
FAIL  plan-has-topic-2  no match
PASS  plan-keeps-small-town  found 'small-town'
PASS  request-note-no-edit  0 Edit call(s) matching /idea-picture-house/
PASS  request-note-no-write  0 Write call(s) matching /idea-picture-house/
PASS  schedule-names-topic  found '"research_topic": "silent-film-cinemas"'
````

`project/llm-files/research-plans/research-plan-silent-film-cinemas.md`:

````markdown
---
run: run-2026-10-08-1400-research
research-topic: silent-film-cinemas
request: r1
source: "[[Ideas/idea-picture-house|Idea - Picture House]]"
source-line: 9
tag: "#research/run-4"
---

# Research Plan - silent-film-cinemas

## Request (r1)

> How did a silent film get its music in a 1920s British cinema, and how were film prints moved from town to town?

Comment from the user: *For the music part, only small-town cinemas, not the big city picture palaces.*

Context: the note's line above it says "The pianist is the only person in town who has seen every film twice." The research should support a small-town picture house setting with a resident pianist.

## Scope

- Place: Britain (mainly England, Scotland and Wales), small towns and their local cinemas.
- Period: the 1920s, up to the arrival of sound films (about 1927–1930).
- Out of scope for topic 1: big city picture palaces, cinema orchestras, and cinema organs in large venues. Mention them only briefly, to contrast with small-town practice.
- The two questions do not depend on each other, so the topics run in parallel.

## Topics

### Topic 1 - Music for silent films in small-town British cinemas

Waits on: none

Questions:
- Who played: a lone pianist, a pianist with one or two other players (such as a violinist or drummer), or a mechanical instrument like a player piano? How common was each in small towns?
- What did they play: improvised music, popular songs, light classics, or published "photoplay" mood music collections (for example, Kinothek-style books for "agitato", "love scene", "chase")? Were cue sheets sent out with films, and did small-town players actually use them?
- How did the pianist prepare: did they see the film before the first showing, or play it cold on the first night? How often did the programme change (for example, twice a week), and how many shows a day?
- Working life: pay, hours, whether the job was full-time or part-time, who usually did it (including women pianists), and the place of the Musicians' Union.
- Practical details: where the piano sat, how the pianist saw the screen, lighting at the piano, and what happened when the music went wrong.
- How it ended: what happened to small-town cinema pianists when sound films arrived around 1929–1931.

Expected output: a short account of a typical small-town set-up, with 3–5 concrete details a writer can use, and sources.

### Topic 2 - How film prints moved between towns in 1920s Britain

Waits on: none

Questions:
- The chain of supply: renters (distributors), their exchange offices, and how a small-town exhibitor booked films (block booking, first run and later runs, how long after a city showing a small town got a film).
- Transport: rail parcels, carriers' vans, motor transport, or someone collecting the cans by bicycle or car. Who paid, and how long did delivery take?
- The physical print: reels in metal cans, transit boxes, the weight of a feature, nitrate film and fire risk, and the rules on carrying and storing it (for example, the Cinematograph Act 1909 and local licensing).
- "Bicycling" and sharing prints: did two nearby cinemas share one print on the same night, passing reels back and forth? How common was it, and was it allowed?
- Wear and damage: worn or scratched prints by the time they reached small towns, missing footage, and how damage was reported or charged.
- What went wrong: late prints, wrong films, reels out of order, and what the cinema did when a print did not arrive.

Expected output: a short account of a print's journey from renter to a small-town cinema and back, with 3–5 concrete details a writer can use, and sources.

## Sources to try

- British Film Institute (BFI) collections and Screenonline.
- Trade press of the time: *The Bioscope*, *Kinematograph Weekly* (Kine Weekly).
- Cinema Theatre Association, and local history society writing on small-town cinemas.
- Academic work on British silent cinema music and exhibition (for example, writing on silent film accompaniment and on the British film trade in the 1920s).
- Oral history and memoirs of cinema pianists and projectionists.
- Mitchell and Kenyon / regional film archives for the regional picture.

## Output

Write the findings for each topic separately, then a short combined summary that ties both back to the picture house idea. Mark anything uncertain or based on a single source.
````

`run/answer.json`:

````json
{
  "research_topic": "silent-film-cinemas",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] }
  ]
}
````

Final reply:

````
I wrote the plan to `project/llm-files/research-plans/research-plan-silent-film-cinemas.md`. The project had no existing plans or template, so I made up the format.

The request splits into two topics. Neither needs the other's results, so both can run at once:

1. **Music for silent films in small-town British cinemas (1920s):** who played, what they played (improvising, mood-music books, cue sheets), how pianists prepared and what their working life was like, and what happened to them when sound films arrived. Following your comment, big-city picture palaces, orchestras and cinema organs are out of scope. They come up only as a contrast.
2. **How film prints moved between towns in 1920s Britain:** how cinemas booked films from distributors, how the prints travelled, the rules for handling flammable nitrate film, two cinemas sharing one print, worn and damaged prints, and what happened when a delivery went wrong.

Schedule (also written to `run/answer.json`):

```json
{
  "research_topic": "silent-film-cinemas",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] }
  ]
}
```
````

#### Run 3

Grades:

````
PASS  every-topic-no-small-town  no match
PASS  judge-instruction-placement   **The limit appears in the music topic.** - The Scope section ties it to topic 1 only: "**Music (topic 1):** only small-town and provincial cinemas. Leave out West End and big-city picture palaces, their full orchestras and their large theatre organs." - The topic 1 section carries it in its title: "### 1. Music in small-town British cinemas of the 1920s". - Its questions repeat it, for example "
PASS  judge-topics-cover-request   The plan has two separate topics, one for each subject:  - **Music:** "### 1. Music in small-town British cinemas of the 1920s". Its questions ask how the film got its music, for example "Who played the music? A lone pianist, a small trio or quintet, or a harmonium or small organ?" and "Did the pianist improvise, or play from cue sheets..." - **Moving prints:** "### 2. How film prints moved betwe
FAIL  plan-has-every-topic  no match
FAIL  plan-has-topic-1  no match
FAIL  plan-has-topic-2  no match
PASS  plan-keeps-small-town  found 'small-town'
PASS  request-note-no-edit  0 Edit call(s) matching /idea-picture-house/
PASS  request-note-no-write  0 Write call(s) matching /idea-picture-house/
PASS  schedule-names-topic  found '"research_topic": "silent-film-cinemas"'
````

`project/llm-files/research-plans/research-plan-silent-film-cinemas.md`:

````markdown
---
run: run-2026-10-08-1400-research
research-topic: silent-film-cinemas
request: r1
source: "[[Ideas/idea-picture-house|Idea - Picture House]]"
source-line: 9
tag: "#research/run-4"
---

# Research Plan - Silent Film Cinemas

## Request

> How did a silent film get its music in a 1920s British cinema, and how were film prints moved from town to town?

Comment on the request:

> For the music part, only small-town cinemas, not the big city picture palaces.

Context from the idea note: a story about a small-town picture house. The pianist "is the only person in town who has seen every film twice".

## Scope

- **Place and time:** Britain, roughly 1920 to 1929. The period ends when sound films arrived (about 1928 to 1930).
- **Music (topic 1):** only small-town and provincial cinemas. Leave out West End and big-city picture palaces, their full orchestras and their large theatre organs. Mention them only when needed to show how the small towns were different.
- **Film prints (topic 2):** how prints moved between towns in general. This topic has no small-town limit, but the focus should stay on how a print reached a provincial cinema.
- Leave out anything outside Britain unless British practice copied it directly (for example, American cue sheets that came with imported films).

## Topics

### 1. Music in small-town British cinemas of the 1920s

Waits on: none

Questions:
- Who played the music? A lone pianist, a small trio or quintet, or a harmonium or small organ? How common was each in small towns?
- Did the pianist improvise, or play from cue sheets and "photoplay" music books and libraries (for example, Hawkes, Bosworth and the Kinothek collections)? Did small-town players get cue sheets at all?
- Did the musician see the film before the first show? How often did programmes change (twice weekly, three times weekly)? How much practice time did that leave? This links to the idea note's line about the pianist seeing every film twice.
- What were the musician's working conditions: hours, how many shows a day, pay, and whether the job was full- or part-time? Did the Musicians' Union or the Amalgamated Musicians' Union have any role?
- Who was usually hired: local piano teachers, women, chapel organists?
- Were there other sounds, such as effects made behind the screen, or a gramophone in very small halls?
- How did the coming of sound (1928 to 1931) change things for small-town musicians?

Likely sources: histories of early British cinema (Rachael Low's *The History of the British Film*, 1918–1929), studies of cinema music (Julie Brown and Annette Davison, eds., *The Sounds of the Silents in Britain*), trade papers (*The Bioscope*, *Kinematograph Weekly*), memoirs and oral histories of cinema pianists, and local history archives.

### 2. How film prints moved between British towns in the 1920s

Waits on: none

Questions:
- How did films get from the producer to the cinema? Who were the renters (distributors) and their regional exchanges? Was there block booking and blind booking? What did the Cinematograph Films Act 1927 change?
- Were small-town cinemas "first run" or "later run"? How many weeks or months after a city opening did a film reach a small town?
- How were the cans physically moved: rail parcels, carriers, vans, motorcycle couriers? Did cinemas share or "bicycle" a print between nearby halls on the same day?
- How were prints handled and stored? Cover nitrate film and the fire rules (Cinematograph Act 1909), the rewinding and inspection done at exchanges, and the worn, scratched or spliced prints that reached later-run halls.
- What paperwork and timing were involved: booking sheets, late or missing prints, and returning prints after the last show?
- Did the film's music material (cue sheets, scores) travel with the print? This links to topic 1.

Likely sources: Rachael Low, *The History of the British Film*; studies of British film distribution and exhibition (for example, work by Jon Burrows and by Nicholas Hiley); the Cinema Exhibitors' Association records; trade papers; railway parcel and carriage records; and fire safety rules for nitrate film.

## Schedule

Both topics stand alone. They can be researched at the same time, and neither waits on the other. The one overlap is whether music cue sheets travelled with the print. Each topic should note what it finds on this so the two can be put together at the end.

| Topic | Title | Waits on |
| ----- | ----- | -------- |
| 1 | Music in small-town British cinemas of the 1920s | none |
| 2 | How film prints moved between British towns in the 1920s | none |
````

`run/answer.json`:

````json
{
  "research_topic": "silent-film-cinemas",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] }
  ]
}
````

Final reply:

````
I wrote the plan to `project/llm-files/research-plans/research-plan-silent-film-cinemas.md` and the schedule below to `run/answer.json`.

```json
{
  "research_topic": "silent-film-cinemas",
  "topics": [
    { "number": 1, "waits_on": [] },
    { "number": 2, "waits_on": [] }
  ]
}
```

The plan has two topics, and they can be researched at the same time:

1. **Music in small-town British cinemas of the 1920s.** Your comment is applied here: this topic covers only small-town cinemas and leaves out the big city picture palaces.
2. **How film prints moved between British towns in the 1920s.** This covers distributors, how long a film took to reach a small town, rail and van transport, and the fire rules for nitrate film.

The two topics overlap on one question: whether the music sheets travelled with the film print. Both topics note it, so the findings can be put together at the end without one topic waiting on the other.

There were no other research plans in the project to copy a format from, so I chose the layout and front matter of the plan file myself.
````

### E1: Changed number

Case folder: `research-evaluator-01-changed-number`.

#### Run 1

Grades:

````
PASS  judge-fails-on-piece-count   Evidence: - Verdict: `"verdict": "fail"` - Problem: `"The note says a typical lancet window held about 1,200 pieces of glass. Topic 2, Passage 1 of the findings says about 800. Both places in the note need to say 800."`  The verdict is FAIL, and the one problem it lists names the piece-count mismatch directly: 1,200 in the note against 800 in the findings.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "matches findings", "where": "Building the window, line 38, and Disagreement / Uncertainty, line 46", "detail": "The note says a typical lancet window held about 1,200 pieces of glass. Topic 2, Passage 1 of the findings says about 800. Both places in the note need to say 800."}]}
````

#### Run 2

Grades:

````
PASS  judge-fails-on-piece-count   The verdict is FAIL: `"verdict": "fail"`.  Two of the problems name the piece-count mismatch:  1. `"where": "Building the window, paragraph 1 (\"A typical lancet window held about 1,200 pieces of glass.\")", "detail": "Topic 2, Passage 1 says a typical lancet window held about 800 pieces of glass, not 1,200."` 2. `"where": "Disagreement / Uncertainty (\"The piece count of about 1,200 comes from a
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "matches findings", "where": "Building the window, paragraph 1 (\"A typical lancet window held about 1,200 pieces of glass.\")", "detail": "Topic 2, Passage 1 says a typical lancet window held about 800 pieces of glass, not 1,200."}, {"check": "matches findings", "where": "Disagreement / Uncertainty (\"The piece count of about 1,200 comes from a survey of one cathedral's lancets\")", "detail": "The findings give the piece count as about 800, not 1,200. The caveat that it comes from a survey of one cathedral is correct, but the number is wrong."}]}
````

#### Run 3

Grades:

````
PASS  judge-fails-on-piece-count   The verdict is `"verdict": "fail"`, and two of the problems name the piece-count mismatch:  1. `"where": "Building the window, paragraph 1 (line 38): \"A typical lancet window held about 1,200 pieces of glass.\""` with `"detail": "Topic 2, Passage 1 gives the figure as about 800 pieces, not 1,200. The note changed the number."` 2. `"where": "Disagreement / Uncertainty (line 46): \"The piece count
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "matches findings", "where": "Building the window, paragraph 1 (line 38): \"A typical lancet window held about 1,200 pieces of glass.\"", "detail": "Topic 2, Passage 1 gives the figure as about 800 pieces, not 1,200. The note changed the number."}, {"check": "matches findings", "where": "Disagreement / Uncertainty (line 46): \"The piece count of about 1,200 comes from a survey of one cathedral's lancets\"", "detail": "Same wrong number repeated. Topic 2, Passage 1 and its reliability note give about 800 pieces."}]}
````

### E2: Missing question

Case folder: `research-evaluator-02-missing-question`.

#### Run 1

Grades:

````
PASS  judge-fails-on-missing-question   The verdict is `"verdict": "fail"`, and two of its problems point to the missing design-planning answer.  1. The coverage problem names the question directly: *"Plan question 4 ('How did glaziers plan the design before cutting?') is never answered. It also isn't listed under Open Research Questions, even though the findings answer it in topic-2.md Passage 2."* 2. The nothing-dropped problem names
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "coverage", "where": "Building the window (whole note)", "detail": "Plan question 4 ('How did glaziers plan the design before cutting?') is never answered. It also isn't listed under Open Research Questions, even though the findings answer it in topic-2.md Passage 2."}, {"check": "nothing dropped", "where": "Building the window; Sources", "detail": "topic-2.md Passage 2 is missing from the note. That passage says the design was drawn full size on a whitewashed wooden table, the pieces were cut and laid out over the drawing, and the table was washed and whitened again for the next design. Its source (https://www.medievalcraft-journal.example/2014/theophilus-glazing) is also missing from the Sources list."}]}
````

#### Run 2

Grades:

````
PASS  judge-fails-on-missing-question   The verdict is FAIL: `"verdict": "fail"`.  Both problems name the missing design answer:  1. The coverage problem is placed at `"## Building the window (Topic 2, Question 4: How did glaziers plan the design before cutting?)"`. It says: "The note never answers Question 4... The Summary leaves out design planning too, and the question isn't listed under Open Research Questions either. The findings 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "coverage", "where": "## Building the window (Topic 2, Question 4: How did glaziers plan the design before cutting?)", "detail": "The note never answers Question 4. The 'Building the window' section only covers how the pieces were held together (cames, soldering) and the armatures. The Summary leaves out design planning too, and the question isn't listed under Open Research Questions either. The findings do answer it, in topic-2 Passage 2."}, {"check": "nothing dropped", "where": "## Building the window and ## Sources", "detail": "Topic-2 Passage 2 (verified) is missing from the note. It says the glazier drew the design full size on a whitewashed wooden table, cut the pieces and laid them out over the drawing, then washed and whitened the table again for the next design. Its source, https://www.medievalcraft-journal.example/2014/theophilus-glazing (a peer-reviewed article on a 12th-century craft treatise, 2014), is also missing from the Sources list."}]}
````

#### Run 3

Grades:

````
PASS  judge-fails-on-missing-question   The verdict is FAIL: `"verdict": "fail"`.  Two problems are listed, and both point to the missing design-planning answer:  1. **Coverage, in "## Building the window":** "Plan question 4 ('How did glaziers plan the design before cutting?') goes unanswered. The note's sections and summary never say how the design was planned, though topic-2 findings Passage 2 answers it." 2. **Nothing dropped, in "
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "coverage", "where": "## Building the window", "detail": "Plan question 4 ('How did glaziers plan the design before cutting?') goes unanswered. The note's sections and summary never say how the design was planned, though topic-2 findings Passage 2 answers it."}, {"check": "nothing dropped", "where": "## Building the window / ## Sources", "detail": "Topic-2 findings Passage 2 is missing from the note. It says the glazier drew the design full size on a whitewashed wooden table, cut the pieces and laid them out over the drawing, then washed and whitened the table again for the next design. Its source (https://www.medievalcraft-journal.example/2014/theophilus-glazing, a peer-reviewed article on a 12th-century craft treatise, 2014) is also missing from the footnotes."}]}
````

### E3: Foreign URL

Case folder: `research-evaluator-03-foreign-url`.

#### Run 1

Grades:

````
PASS  judge-fails-on-foreign-url   The verdict is a FAIL: `"verdict": "fail"`.  One problem names both footnote 6 and the URL, and says they don't come from the findings: - Where: `"Sources, footnote [^6] (cited in 'Building the window' and 'Disagreement / Uncertainty')"` - Detail: `"Footnote [^6] points to https://www.glass-history-blog.example/2022/lancet-windows, which doesn't appear in any findings file."`  The problem also gi
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "matches findings", "where": "Sources, footnote [^6] (cited in 'Building the window' and 'Disagreement / Uncertainty')", "detail": "Footnote [^6] points to https://www.glass-history-blog.example/2022/lancet-windows, which doesn't appear in any findings file. In topic-2.md, Passage 1, the source for the lancet piece count is https://www.archaeology-review.example/2018/chartres-lancet-survey. The note's Reliability section even names archaeology-review.example, but no footnote cites it. [^6] should be replaced with the archaeology-review URL."}]}
````

#### Run 2

Grades:

````
PASS  judge-fails-on-foreign-url   Evidence: - Verdict: `"verdict": "fail"`, which is a FAIL verdict. - The single problem names both footnote 6 and the URL, and says they don't come from the findings: `"where": "Sources, footnote [^6] ..."`, `"detail": "Footnote [^6] points to https://www.glass-history-blog.example/2022/lancet-windows, a URL that appears in neither findings file."`  Both conditions are met.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "matches findings", "where": "Sources, footnote [^6] (cited in 'Building the window' paragraph 1 and 'Disagreement / Uncertainty')", "detail": "Footnote [^6] points to https://www.glass-history-blog.example/2022/lancet-windows, a URL that appears in neither findings file. Topic 2 Passage 1 cites https://www.archaeology-review.example/2018/chartres-lancet-survey for the H-shaped cames and the ~800-piece lancet count. The note's own Reliability section names archaeology-review.example, but no footnote links to it. [^6] should point to the archaeology-review survey URL."}]}
````

#### Run 3

Grades:

````
PASS  judge-fails-on-foreign-url   The reply's verdict is a failure: `"verdict": "fail"`.  Its single problem names both footnote 6 and the URL, and says the URL does not come from the findings: - `"where": "Sources, footnote [^6] ..."` - `"detail": "Footnote [^6] points to https://www.glass-history-blog.example/2022/lancet-windows, but no findings file cites that URL."`  It also gives the source the findings actually use: `https:
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "matches findings", "where": "Sources, footnote [^6] (used in 'Building the window' paragraph 1 and 'Disagreement / Uncertainty')", "detail": "Footnote [^6] points to https://www.glass-history-blog.example/2022/lancet-windows, but no findings file cites that URL. Topic 2 Passage 1 gives the source for the ~800-piece lancet count as https://www.archaeology-review.example/2018/chartres-lancet-survey. The note's own Reliability section names archaeology-review.example, so the footnote URL doesn't match the findings or the rest of the note. Replace it with the archaeology-review URL."}]}
````

### E4: Clean note

Case folder: `research-evaluator-04-clean-note`.

#### Run 1

Grades:

````
PASS  judge-passes-clean-note   The reply's verdict is PASS: `{"verdict": "pass", "problems": []}`. The `problems` list is empty, so no problems were raised and none were invented.
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
PASS  judge-passes-clean-note   The reply's verdict is PASS: `{"verdict": "pass", "problems": []}`. Since the verdict is "pass", the check passes. The `problems` list is empty, so the reply reports no problems, and no invented problem appears to quote.
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
PASS  judge-passes-clean-note   The reply's verdict is PASS: `{"verdict": "pass", "problems": []}`. The `"problems"` list is empty, so it raises no problems, invented or otherwise.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "pass", "problems": []}
````
