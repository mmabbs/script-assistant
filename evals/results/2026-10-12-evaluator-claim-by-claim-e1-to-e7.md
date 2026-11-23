# 2026-10-12 Evaluator Runs: Claim by Claim, E1 to E7

After the first live run, the research-evaluator's first check reported 1 of a note's 3 real problems, so the fix round never heard about the other 2. The writer chose to make it work through the note sentence by sentence and report every problem in one answer (spec-research-workflow.md 11 item 97), and to keep the strict rule against reasoning steps (item 98). These runs test the updated agent file. A worker who wrote no agent file wrote E6 and E7. The runner is `_tools/research-run.py`.

## What Was Run

- **Date:** 2026-10-12, 18:00 to 18:08 EDT. Claude Code 2.1.296.
- **Agent:** `script-asst:research-evaluator`, claude-sonnet-5-5 at effort high, with the claim-by-claim order of work.
- **Runs:** E1 to E4, E6, and E7 on the agent, three each (18 runs). E6 and E7 on bare claude-opus-5-5, three each (6 runs).
- **New cases:**
  - **E6** `research-evaluator-06-three-errors`: three plants in the stained-glass note: a piece count changed to 600, a "which…" clause adding a conclusion, and a dropped answer to "How were the pieces cut to shape?"
  - **E7** `research-evaluator-07-live-fog-signals`: the live run's plan, findings, and first-draft fog-signal note, rebuilt by reverting the one sentence the fix round changed. The three problems the first live check missed or found: the Souter Point sentence and two "which…" clauses. The omitted bell finding is neither required nor penalized.
- **Errors and timeouts:** none.

## Summary Table

| Case | Agent: all checks | Bare: all checks |
| --- | --- | --- |
| E1 to E4 | 12 of 12 | 12 of 12 (earlier record) |
| E6 three errors | 3 of 3 | 3 of 3 |
| E7 live fog-signal note | 3 of 3 | 1 of 3 |

## Findings

1. **E7 shows the fix.** The agent named all three real problems in every run. Bare Claude did in one: r1 reported only the bell omission, and r3 missed the Souter Point sentence and the compressor clause.
2. **The agent also found more overstatements in the live note** that the live first check never reported: "Irish Lights discontinued its remaining explosive signals in 1972" (the source names one station's discontinuation, "along with similar signals around the coast") and "The big compressed-air signals needed engines, compressors, and air tanks" (the source says this of the largest diaphones). r2 also reported a coverage gap: how a siren worked and sounded. So the live note had more problems than the first check reported.
3. **No invented problems.** E4's clean note passed in all three runs with an empty problem list.
4. **E6 can't tell the agent from bare Claude.** A short note with three plants is easy to check in full. The live miss came from a long note, about 25 KB with over 35 footnotes, which is what E7 tests.

## Caveats

1. One judge call per check, not repeated.
2. **Cost:** printed totals, judges included: E1 to E4 $0.70, E6 agent $0.28, E6 bare $0.44, E7 agent $0.59, E7 bare $0.99.
3. The raw run folders are in the session's scratchpad. Each run's grades and reply are copied below.

## Full Outputs

Each run shows its grades, then every file it wrote or changed (none, for a Read-only agent), then its final reply.

### E1: Changed number, research-evaluator agent, claim by claim

Case folder: `research-evaluator-01-changed-number`. Run folder: `evaluator-a3`.

#### Run 1

Grades:

````
PASS  judge-fails-on-piece-count   The verdict is a failure: `"verdict": "fail"`. Lowercase "fail" is still a FAIL verdict.  The first problem names the mismatch directly: - `"where": "Building the window, paragraph 1"`, `"detail": "Note says \"A typical lancet window held about 1,200 pieces of glass.\"; topic-2.md Passage 1 says \"A typical lancet window held about 800 pieces of glass.\""`  The second problem flags the same piece
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{ "verdict": "fail",
  "problems": [
    { "check": "matches findings", "where": "Building the window, paragraph 1",
      "detail": "Note says \"A typical lancet window held about 1,200 pieces of glass.\"; topic-2.md Passage 1 says \"A typical lancet window held about 800 pieces of glass.\"" },
    { "check": "matches findings", "where": "Disagreement / Uncertainty, paragraph 1",
      "detail": "Note says \"The piece count of about 1,200 comes from a survey of one cathedral's lancets\"; topic-2.md Passage 1 gives the count as \"about 800 pieces\"." }
  ] }
```
````

#### Run 2

Grades:

````
PASS  judge-fails-on-piece-count   The verdict is fail: `"verdict":"fail"`. The check says a lowercase "fail" counts the same as FAIL.  Two problems are listed, and both name the piece-count mismatch:  1. `"where":"Building the window, paragraph 1"`, with the detail: `"The note says \"A typical lancet window held about 1,200 pieces of glass.\" topic-2.md, Passage 1, says \"A typical lancet window held about 800 pieces of glass.\""
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"matches findings","where":"Building the window, paragraph 1","detail":"The note says \"A typical lancet window held about 1,200 pieces of glass.\" topic-2.md, Passage 1, says \"A typical lancet window held about 800 pieces of glass.\""},{"check":"matches findings","where":"Disagreement / Uncertainty, paragraph 1","detail":"The note says \"The piece count of about 1,200 comes from a survey of one cathedral's lancets\". topic-2.md, Passage 1, gives the count as about 800."}]}
````

#### Run 3

Grades:

````
PASS  judge-fails-on-piece-count   The verdict is FAIL: `"verdict":"fail"`.  Both problems name the piece-count mismatch:  1. `"where":"Building the window, paragraph 1"`: "Note says \"A typical lancet window held about 1,200 pieces of glass.\" topic-2.md, Passage 1 says \"A typical lancet window held about 800 pieces of glass.\" The number is wrong." 2. `"where":"Disagreement / Uncertainty, paragraph 1"`: "Note says \"The piece c
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"matches findings","where":"Building the window, paragraph 1","detail":"Note says \"A typical lancet window held about 1,200 pieces of glass.\" topic-2.md, Passage 1 says \"A typical lancet window held about 800 pieces of glass.\" The number is wrong."},{"check":"matches findings","where":"Disagreement / Uncertainty, paragraph 1","detail":"Note says \"The piece count of about 1,200 comes from a survey of one cathedral's lancets\". topic-2.md, Passage 1 gives the count as \"about 800 pieces\". Correct the number here too."}]}
````

### E2: Missing question, research-evaluator agent, claim by claim

Case folder: `research-evaluator-02-missing-question`. Run folder: `evaluator-a3`.

#### Run 1

Grades:

````
PASS  judge-fails-on-missing-question   The verdict is fail: `"verdict":"fail"`.  Both problems name the missing design-planning answer:  1. Coverage: "Plan question 4 under Topic 2, \"How did glaziers plan the design before cutting?\", is neither answered in the note nor listed under Open Research Questions. Open Research Questions holds only the kiln-temperature item." 2. Nothing dropped: "topic-2.md Passage 2 answers plan question 4
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"coverage","where":"Building the window and Open Research Questions","detail":"Plan question 4 under Topic 2, \"How did glaziers plan the design before cutting?\", is neither answered in the note nor listed under Open Research Questions. Open Research Questions holds only the kiln-temperature item."},{"check":"nothing dropped","where":"Building the window","detail":"topic-2.md Passage 2 answers plan question 4. It says the glazier \"drew the design full size on a whitewashed wooden table\", the pieces were cut and laid out over the drawing, and the table was then washed and whitened again for the next design. It has a URL, https://www.medievalcraft-journal.example/2014/theophilus-glazing. The note leaves it out entirely."}]}
````

#### Run 2

Grades:

````
PASS  judge-fails-on-missing-question   The verdict is FAIL: `"verdict": "fail"`.  Both problems flag the missing design question:  1. Coverage problem (where: "Building the window / Open Research Questions"): "Plan question 4 under Topic 2, \"How did glaziers plan the design before cutting?\", is neither answered in the note nor listed under Open Research Questions." 2. Nothing-dropped problem (where: "Building the window"): "topic-2.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{ "verdict": "fail",
  "problems": [
    { "check": "coverage", "where": "Building the window / Open Research Questions",
      "detail": "Plan question 4 under Topic 2, \"How did glaziers plan the design before cutting?\", is neither answered in the note nor listed under Open Research Questions." },
    { "check": "nothing dropped", "where": "Building the window",
      "detail": "topic-2.md Passage 2 answers plan question 4. It says \"the glazier drew the design full size on a whitewashed wooden table. The pieces were cut and laid out over the drawing. When the panel was finished, the table was washed and whitened again for the next design.\" It has a URL (https://www.medievalcraft-journal.example/2014/theophilus-glazing). None of it appears in the note." } ] }
````

#### Run 3

Grades:

````
PASS  judge-fails-on-missing-question   The reply gives the verdict `"verdict":"fail"`, and both of its problems name the missing design-planning answer.  - **First problem** ("nothing dropped", "Building the window (whole section)"): "topic-2.md Passage 2 answers plan question 4. It says \"the glazier drew the design full size on a whitewashed wooden table. The pieces were cut and laid out over the drawing.\" ... The note leaves it ou
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"nothing dropped","where":"Building the window (whole section)","detail":"topic-2.md Passage 2 answers plan question 4. It says \"the glazier drew the design full size on a whitewashed wooden table. The pieces were cut and laid out over the drawing.\" It has a URL, https://www.medievalcraft-journal.example/2014/theophilus-glazing, and Evidence: verified. The note leaves it out."},{"check":"coverage","where":"Building the window / Open Research Questions","detail":"Plan question 4 under Topic 2, \"How did glaziers plan the design before cutting?\", is neither answered in the note nor listed under Open Research Questions. The only open question is about kiln temperature."}]}
````

### E3: Foreign URL, research-evaluator agent, claim by claim

Case folder: `research-evaluator-03-foreign-url`. Run folder: `evaluator-a3`.

#### Run 1

Grades:

````
PASS  judge-fails-on-foreign-url   The verdict is fail: `"verdict":"fail"`.  Two of the problems name footnote 6 and the glass-history-blog URL as not coming from the findings:  - Problem 1 (Building the window, paragraph 1): "cites [^6], https://www.glass-history-blog.example/2022/lancet-windows. That URL appears in no findings file." - Problem 2 (Disagreement / Uncertainty, paragraph 1): "cites the foreign URL glass-history-blog
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"matches findings","where":"Building the window, paragraph 1","detail":"The sentence \"A typical lancet window held about 800 pieces of glass.[^5][^6]\" cites [^6], https://www.glass-history-blog.example/2022/lancet-windows. That URL appears in no findings file. In topic-2.md Passage 1, the 800-piece claim is backed by https://www.stainedglassmuseum.example/collections/how-a-window-is-made and https://www.archaeology-review.example/2018/chartres-lancet-survey. Replace [^6] with the archaeology-review URL, or drop it."},{"check":"matches findings","where":"Disagreement / Uncertainty, paragraph 1","detail":"The sentence \"The piece count of about 800 comes from a survey of one cathedral's lancets and may not hold elsewhere.[^6]\" cites the foreign URL glass-history-blog.example. In topic-2.md Passage 1, the survey source is https://www.archaeology-review.example/2018/chartres-lancet-survey. The footnote must use that URL."},{"check":"matches findings","where":"Making the coloured glass, paragraph 1, sentence 2","detail":"\"Red made this way came out so dark it was nearly black.\" has no footnote of its own. It is a claim from topic-1.md Passage 1, whose URLs are vam.ac.uk and corpusvitrearum.example. It needs a footnote."}]}
````

#### Run 2

Grades:

````
PASS  judge-fails-on-foreign-url   The verdict is fail: `"verdict": "fail"`.  Both problems name footnote 6 and the glass-history-blog URL as not coming from the findings:  - Problem 1 ("Building the window, paragraph 1"): "[^6] is https://www.glass-history-blog.example/2022/lancet-windows. That URL appears in no findings file. topic-2.md Passage 1 lists only https://www.stainedglassmuseum.example/collections/how-a-window-is-made 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{ "verdict": "fail",
  "problems": [
    { "check": "matches findings", "where": "Building the window, paragraph 1",
      "detail": "The note cites [^6] for the cames and soldering sentence and for \"A typical lancet window held about 800 pieces of glass.\" [^6] is https://www.glass-history-blog.example/2022/lancet-windows. That URL appears in no findings file. topic-2.md Passage 1 lists only https://www.stainedglassmuseum.example/collections/how-a-window-is-made and https://www.archaeology-review.example/2018/chartres-lancet-survey. Replace [^6] with a URL from that list." },
    { "check": "matches findings",
      "where": "Disagreement / Uncertainty, paragraph 1",
      "detail": "The note says \"The piece count of about 800 comes from a survey of one cathedral's lancets and may not hold elsewhere.[^6]\" [^6] is glass-history-blog.example, which is in no findings file. topic-2.md Passage 1 attributes the survey to https://www.archaeology-review.example/2018/chartres-lancet-survey. That URL is not in the Sources section, even though the Reliability section names archaeology-review.example." }
  ]
}
```
````

#### Run 3

Grades:

````
PASS  judge-fails-on-foreign-url   The verdict is a fail: `"verdict": "fail"`. The check wants the verdict to be FAIL, and lowercase "fail" counts as that verdict.  Both problems name footnote 6 and the glass-history-blog URL as not coming from the findings:  - Problem 1 (Building the window, paragraph 1): "cites footnote 6, https://www.glass-history-blog.example/2022/lancet-windows. That URL is in no findings file." - Problem 2 (
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
```json
{ "verdict": "fail",
  "problems": [
    { "check": "matches findings", "where": "Building the window, paragraph 1",
      "detail": "The claim \"A typical lancet window held about 800 pieces of glass.[^5][^6]\" cites footnote 6, https://www.glass-history-blog.example/2022/lancet-windows. That URL is in no findings file. The passage holding the 800-piece claim is topic-2.md Passage 1. Its URLs are stainedglassmuseum.example/collections/how-a-window-is-made and https://www.archaeology-review.example/2018/chartres-lancet-survey. The fix is to cite the archaeology-review URL for this claim." },
    { "check": "matches findings", "where": "Disagreement / Uncertainty, paragraph 1",
      "detail": "The note says \"The piece count of about 800 comes from a survey of one cathedral's lancets and may not hold elsewhere.[^6]\" Footnote 6 is glass-history-blog.example, which is in no findings file. topic-2.md Passage 1 gives the survey source as https://www.archaeology-review.example/2018/chartres-lancet-survey. The footnote should point to that URL. The Sources list should drop the unsupported glass-history-blog URL." }
  ] }
```
````

### E4: Clean note, research-evaluator agent, claim by claim

Case folder: `research-evaluator-04-clean-note`. Run folder: `evaluator-a3`.

#### Run 1

Grades:

````
PASS  judge-passes-clean-note   The reply's verdict is PASS: `{"verdict":"pass","problems":[]}`. The verdict field is `"pass"`, and the problems list is empty (`"problems":[]`). Since no problems were raised, there is nothing invented to quote.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict":"pass","problems":[]}
````

#### Run 2

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

#### Run 3

Grades:

````
PASS  judge-passes-clean-note   The reply's verdict is PASS: `{"verdict": "pass", "problems": []}`. The `"problems"` list is empty, so no problems were raised and none were invented.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
````

Final reply:

````
{"verdict": "pass", "problems": []}
````

### E6: Three errors, research-evaluator agent, claim by claim

Case folder: `research-evaluator-06-three-errors`. Run folder: `e6-agent`.

#### Run 1

Grades:

````
PASS  judge-names-changed-piece-count   The verdict is `"verdict":"fail"`.  One of the problems names the mismatch directly: - `{"check":"matches findings","where":"Disagreement / Uncertainty, paragraph 1","detail":"Note says \"The piece count of about 600\"; topic-2.md Passage 1 says \"A typical lancet window held about 800 pieces of glass.\" The note's own Building the window section also says 800."}`  That problem puts the 600 figur
PASS  judge-names-missing-cutting-question   The reply gives the verdict `"verdict":"fail"`, which is a FAIL verdict.  Two of its problems name the missing cutting answer:  - **Coverage:** `"Plan question 2 under Topic 1, \"How were the pieces cut to shape?\", is neither answered in the note nor listed under Open Research Questions."` - **Nothing dropped:** `"topic-1.md Passage 2 answers plan question 2. It says pieces were cut with a red-h
PASS  judge-names-which-clause   Evidence:  - The verdict is FAIL: `"verdict":"fail"` - The first problem names the larger-openings clause and says the findings don't support it:   - `"check":"matches findings","where":"Building the window, paragraph 3"`   - `"Note says armatures \"carried the weight of the leaded panels, which let the builders make the window openings far larger than before.[^4]\". topic-2.md Passage 3 says onl
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict":"fail"'
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"matches findings","where":"Building the window, paragraph 3","detail":"Note says armatures \"carried the weight of the leaded panels, which let the builders make the window openings far larger than before.[^4]\". topic-2.md Passage 3 says only \"Iron bars, called armatures, ran across the window opening and carried the weight of the leaded panels.\" The \"which let the builders make the window openings far larger\" clause is a conclusion the passage doesn't state."},{"check":"matches findings","where":"Disagreement / Uncertainty, paragraph 1","detail":"Note says \"The piece count of about 600\"; topic-2.md Passage 1 says \"A typical lancet window held about 800 pieces of glass.\" The note's own Building the window section also says 800."},{"check":"coverage","where":"Making the coloured glass / Open Research Questions","detail":"Plan question 2 under Topic 1, \"How were the pieces cut to shape?\", is neither answered in the note nor listed under Open Research Questions."},{"check":"nothing dropped","where":"Making the coloured glass","detail":"topic-1.md Passage 2 answers plan question 2. It says pieces were cut with a red-hot iron drawn along a marked line, then trimmed with a grozing iron. The passage has a URL (medievalcraft-journal.example/2016/glass-cutting-methods). The note leaves it out."}]}
````

#### Run 2

Grades:

````
PASS  judge-names-changed-piece-count   The verdict is `"verdict":"fail"`.  One problem names the mismatch directly: - `{"check":"matches findings","where":"Disagreement / Uncertainty, paragraph 1","detail":"Note says \"The piece count of about 600\". topic-2.md Passage 1 says \"about 800 pieces of glass\"."}`  This problem points to the Disagreement / Uncertainty section. It sets the note's "about 600" piece count against the findings
PASS  judge-names-missing-cutting-question   The verdict is `"verdict":"fail"`, as the check requires.  Two of the problems cover the missing cutting question:  - **Coverage problem** (where: "Making the coloured glass / Open Research Questions"): "Plan question 2 under Topic 1, \"How were the pieces cut to shape?\", is neither answered in the note nor listed under Open Research Questions." - **Nothing-dropped problem** (where: "Making the 
PASS  judge-names-which-clause   The reply's verdict is a failure: `"verdict":"fail"`.  Its first problem names the larger-openings clause and says the findings don't support it: - `"check":"matches findings","where":"Building the window, paragraph 3"` - `"Note says \"which let the builders make the window openings far larger than before\". topic-2.md Passage 3 says only \"Iron bars, called armatures, ran across the window openi
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict":"fail"'
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"matches findings","where":"Building the window, paragraph 3","detail":"Note says \"which let the builders make the window openings far larger than before\". topic-2.md Passage 3 says only \"Iron bars, called armatures, ran across the window opening and carried the weight of the leaded panels.\" It says nothing about larger openings, so that clause is an added conclusion."},{"check":"matches findings","where":"Disagreement / Uncertainty, paragraph 1","detail":"Note says \"The piece count of about 600\". topic-2.md Passage 1 says \"about 800 pieces of glass\"."},{"check":"coverage","where":"Making the coloured glass / Open Research Questions","detail":"Plan question 2 under Topic 1, \"How were the pieces cut to shape?\", is neither answered in the note nor listed under Open Research Questions."},{"check":"nothing dropped","where":"Making the coloured glass","detail":"topic-1.md Passage 2 answers plan question 2. It says pieces were cut by drawing a red-hot iron along a marked line so the glass cracked, then trimmed with a grozing iron. The source is medievalcraft-journal.example/2016/glass-cutting-methods. The note leaves it out."}]}
````

#### Run 3

Grades:

````
PASS  judge-names-changed-piece-count   The verdict is a fail: `"verdict":"fail"`.  One of the problems names the mismatch, with `"where":"Disagreement / Uncertainty, paragraph 1"`. Its detail reads: "Note says \"The piece count of about 600\". topic-2.md Passage 1 says \"A typical lancet window held about 800 pieces of glass.\" The note's number is wrong, and it also contradicts the 800 given in Building the window, paragraph 1."  Tha
PASS  judge-names-missing-cutting-question   The reply's verdict is FAIL: `"verdict":"fail"`.  Two of its problems name the missing cutting answer:  - **Coverage problem:** "Plan question 2 under Topic 1, \"How were the pieces cut to shape?\", is neither answered in the note nor listed under Open Research Questions." - **Nothing-dropped problem:** "topic-1.md Passage 2 answers plan question 2. It says pieces were cut by drawing a red-hot ir
PASS  judge-names-which-clause   The verdict is `"verdict":"fail"`. The first problem names the larger-openings clause and calls it unsupported by the findings:  > {"check":"matches findings","where":"Building the window, paragraph 3","detail":"Note says \"which let the builders make the window openings far larger than before.[^4]\". topic-2.md Passage 3 says only \"Iron bars, called armatures, ran across the window opening and 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict":"fail"'
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"matches findings","where":"Building the window, paragraph 3","detail":"Note says \"which let the builders make the window openings far larger than before.[^4]\". topic-2.md Passage 3 says only \"Iron bars, called armatures, ran across the window opening and carried the weight of the leaded panels.\" It says nothing about larger openings."},{"check":"matches findings","where":"Disagreement / Uncertainty, paragraph 1","detail":"Note says \"The piece count of about 600\". topic-2.md Passage 1 says \"A typical lancet window held about 800 pieces of glass.\" The note's number is wrong, and it also contradicts the 800 given in Building the window, paragraph 1."},{"check":"coverage","where":"Making the coloured glass / Open Research Questions","detail":"Plan question 2 under Topic 1, \"How were the pieces cut to shape?\", is neither answered in the note nor listed under Open Research Questions."},{"check":"nothing dropped","where":"Making the coloured glass","detail":"topic-1.md Passage 2 answers plan question 2. It says pieces were cut by drawing a red-hot iron along a marked line to crack the glass, and the edge was then trimmed with a grozing iron. It has a URL (medievalcraft-journal.example/2016/glass-cutting-methods), but the note leaves it out entirely."}]}
````

### E6: Three errors, bare claude-opus-5-5

Case folder: `research-evaluator-06-three-errors`. Run folder: `e6-bare`.

#### Run 1

Grades:

````
PASS  judge-names-changed-piece-count   The verdict is `"verdict": "fail"`.  The fourth problem names the mismatch:  > {"check": "matches findings", "where": "Disagreement / Uncertainty", "detail": "This section gives the piece count as 'about 600'. The findings (Topic 2 Passage 1) and the note's own body say about 800."}  It identifies the right section (Disagreement / Uncertainty) and the 600 figure. It contrasts that figure with the
PASS  judge-names-missing-cutting-question   The verdict is fail: `"verdict": "fail"`.  Two of the problems name the missing cutting answer:  - **Coverage:** "Plan question 2 (How were the pieces cut to shape?) is not answered anywhere in the note. Topic 1 findings answer it in Passage 2: a red-hot iron was drawn along a marked line to crack the glass, and a grozing iron was used to trim the edge." - **Nothing dropped:** "Topic 1 Passage 2 
PASS  judge-names-which-clause   The verdict is a fail: `"verdict": "fail"`.  One problem names the larger-openings clause and says the findings don't support it:  > `{"check": "matches findings", "where": "Building the window, armatures paragraph", "detail": "The clause 'which let the builders make the window openings far larger than before' is not in the findings. Topic 2 Passage 3 only says the armatures ran across the openin
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict": "fail"'
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "coverage", "where": "Making the coloured glass", "detail": "Plan question 2 (How were the pieces cut to shape?) is not answered anywhere in the note. Topic 1 findings answer it in Passage 2: a red-hot iron was drawn along a marked line to crack the glass, and a grozing iron was used to trim the edge."}, {"check": "nothing dropped", "where": "Making the coloured glass / Sources", "detail": "Topic 1 Passage 2 (cutting with a hot iron, grozing iron trimming, diamond cutters coming much later) is missing from the note. Its source, https://www.medievalcraft-journal.example/2016/glass-cutting-methods, is also missing from the Sources list."}, {"check": "matches findings", "where": "Building the window, armatures paragraph", "detail": "The clause 'which let the builders make the window openings far larger than before' is not in the findings. Topic 2 Passage 3 only says the armatures ran across the opening and carried the weight of the leaded panels."}, {"check": "matches findings", "where": "Disagreement / Uncertainty", "detail": "This section gives the piece count as 'about 600'. The findings (Topic 2 Passage 1) and the note's own body say about 800."}]}
````

#### Run 2

Grades:

````
PASS  judge-names-changed-piece-count   The verdict is `"verdict": "fail"`.  The fourth problem names the mismatch: `{"check": "matches findings", "where": "Disagreement / Uncertainty", "detail": "This section gives the piece count as 'about 600'. The findings (Topic 2 Passage 1) and the note's own Building the window section both say about 800."}`  It places the 600 piece count under Disagreement / Uncertainty and sets it against the 
PASS  judge-names-missing-cutting-question   The reply's verdict is FAIL, quoted as `"verdict": "fail"`.  Two of its problems say the cutting question and its finding are missing:  - **Coverage problem (Making the coloured glass):** "Question 2 (how were the pieces cut to shape?) gets no answer anywhere in the note. Topic 1 Passage 2 answers it: a red-hot iron was drawn along a marked line, then the edge was trimmed with a grozing iron." - 
PASS  judge-names-which-clause   The verdict is a fail: `"verdict": "fail"`.  One of the problems names the larger-openings clause as unsupported by the findings:  > `{"check": "matches findings", "where": "Building the window, armatures paragraph", "detail": "The clause 'which let the builders make the window openings far larger than before' isn't in the findings. Topic 2 Passage 3 only says the armatures ran across the opening
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict": "fail"'
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "coverage", "where": "Making the coloured glass", "detail": "Question 2 (how were the pieces cut to shape?) gets no answer anywhere in the note. Topic 1 Passage 2 answers it: a red-hot iron was drawn along a marked line, then the edge was trimmed with a grozing iron. Diamond cutters came much later."}, {"check": "nothing dropped", "where": "Making the coloured glass / Sources", "detail": "Topic 1 Passage 2 (verified) is missing from the note: the hot-iron cracking, the grozing iron, and the later arrival of diamond cutters. Its source, https://www.medievalcraft-journal.example/2016/glass-cutting-methods, is also missing from the Sources list."}, {"check": "matches findings", "where": "Building the window, armatures paragraph", "detail": "The clause 'which let the builders make the window openings far larger than before' isn't in the findings. Topic 2 Passage 3 only says the armatures ran across the opening and carried the weight of the leaded panels."}, {"check": "matches findings", "where": "Disagreement / Uncertainty", "detail": "This section gives the piece count as 'about 600'. The findings (Topic 2 Passage 1) and the note's own Building the window section both say about 800."}]}
````

#### Run 3

Grades:

````
PASS  judge-names-changed-piece-count   The reply's verdict is FAIL: `"verdict": "fail"`.  One of its problems names the piece-count mismatch directly:  > `{"check": "matches findings", "where": "Disagreement / Uncertainty", "detail": "This section says 'about 600' pieces. The findings and the note's own Building the window section both say about 800."}`  This problem points to the right section (Disagreement / Uncertainty). It quotes 
PASS  judge-names-missing-cutting-question   The verdict is fail: `"verdict": "fail"`.  Two of the reply's problems point to the missing cutting answer:  - **Dropped finding:** `{"check": "nothing dropped", "where": "Making the coloured glass (topic-1.md, Passage 2)", "detail": "The note leaves out the passage on cutting entirely: cracking the glass along a marked line with a red-hot iron, trimming it with a grozing iron, and diamond cutter
PASS  judge-names-which-clause   The reply's verdict is FAIL: `"verdict": "fail"`.  One of its problems names the larger-openings clause and says the findings don't support it:  > `{"check": "matches findings", "where": "Building the window, armatures paragraph", "detail": "The note adds 'which let the builders make the window openings far larger than before'. No findings file supports this. topic-2.md Passage 3 only says the ar
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict": "fail"'
````

Final reply:

````
```json
{"verdict": "fail", "problems": [
  {"check": "nothing dropped", "where": "Making the coloured glass (topic-1.md, Passage 2)", "detail": "The note leaves out the passage on cutting entirely: cracking the glass along a marked line with a red-hot iron, trimming it with a grozing iron, and diamond cutters coming much later. Its source (medievalcraft-journal.example/2016/glass-cutting-methods) is also missing from Sources."},
  {"check": "coverage", "where": "Making the coloured glass", "detail": "Plan question 2 ('How were the pieces cut to shape?') goes unanswered, even though the findings answer it."},
  {"check": "matches findings", "where": "Disagreement / Uncertainty", "detail": "This section says 'about 600' pieces. The findings and the note's own Building the window section both say about 800."},
  {"check": "matches findings", "where": "Building the window, armatures paragraph", "detail": "The note adds 'which let the builders make the window openings far larger than before'. No findings file supports this. topic-2.md Passage 3 only says the armatures crossed the opening and carried the weight of the panels."}
]}
```
````

### E7: The live fog-signal note, research-evaluator agent, claim by claim

Case folder: `research-evaluator-07-live-fog-signals`. Run folder: `e7-agent`.

#### Run 1

Grades:

````
PASS  judge-names-around-the-coast-which-clause   The verdict is a fail: `"verdict":"fail"`.  One problem names the clause the check targets: - `"where":"Fog signal types in the 1950s, How common each type was, sentence 5"` - `"detail":"Note says the 1972 withdrawal \"shows they were in use at more stations than the ones named here.\" topic-1.md says only that the Rathlin East signal was discontinued in 1972 \"for security reasons\" \"along with
PASS  judge-names-compressor-which-clause   The reply's verdict is FAIL: `"verdict":"fail"`.  One of its problems names the clause in question. It is filed under "How common each type was":  > {"check":"matches findings","where":"Fog signal types in the 1950s, How common each type was, sentence 4","detail":"Note says \"which tied them to stations that could house that machinery.\" topic-1.md says only that the largest diaphones \"needed a 
PASS  judge-names-souter-point-1919   The verdict is FAIL: `"verdict":"fail"`.  The first problem names the Souter Point sentence directly: - `"where":"Fog signal types in the 1950s, Diaphones, Trinity House: Souter Point, sentence 3"` - `"detail":"Note says \"the diaphones replaced more powerful units fitted in 1919.\" topic-1.md says only that the building \"first used compressed-air horns, which were swapped for sirens in 1879 and
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict":"fail"'
````

Final reply:

````
{"verdict":"fail","problems":[{"check":"matches findings","where":"Fog signal types in the 1950s, Diaphones, Trinity House: Souter Point, sentence 3","detail":"Note says \"the diaphones replaced more powerful units fitted in 1919.\" topic-1.md says only that the building \"first used compressed-air horns, which were swapped for sirens in 1879 and for more powerful units in 1919.\" It does not say diaphones replaced the 1919 units. The 1953 diaphones are a separate statement on that page."},{"check":"matches findings","where":"Fog signal types in the 1950s, How common each type was, sentence 4","detail":"Note says \"which tied them to stations that could house that machinery.\" topic-1.md says only that the largest diaphones \"needed a large compressor plant and air tanks.\" The \"which…\" clause adds a conclusion the passage does not state."},{"check":"matches findings","where":"Fog signal types in the 1950s, How common each type was, sentence 5","detail":"Note says the 1972 withdrawal \"shows they were in use at more stations than the ones named here.\" topic-1.md says only that the Rathlin East signal was discontinued in 1972 \"for security reasons\" \"along with similar signals around the coast.\" The \"shows…\" conclusion is not in the passage."},{"check":"matches findings","where":"Summary, paragraph 2, sentence 2","detail":"Note says \"The big compressed-air signals needed engines, compressors, and air tanks.[^1]\" The Britannica passage in topic-1.md says the largest diaphones \"needed a large compressor plant and air tanks.\" It does not mention engines and does not cover all big compressed-air signals."},{"check":"matches findings","where":"How keepers ran and maintained the signals, What could go wrong, Theft of explosives, sentence 2","detail":"Note says \"Irish Lights discontinued its remaining explosive signals in 1972.\" topic-1.md says only that Rathlin East's signal was discontinued in 1972 \"along with similar signals around the coast.\" It says Loop Head ended in 1972. It also says Tuskar Rock's explosive signal ran until 1974. \"Remaining\" is unsupported and conflicts with the Tuskar date."}]}
````

#### Run 2

Grades:

````
PASS  judge-names-around-the-coast-which-clause   The verdict is fail: `"verdict": "fail"`.  The third problem names the clause in question: - check: "matches findings" - where: "How common each type was, paragraph 1, last sentence" - detail: "Note says the 1972 withdrawal \"shows they were in use at more stations than the ones named here.\" topic-1.md says only that Rathlin East's signal was discontinued in 1972 \"along with similar signals aro
PASS  judge-names-compressor-which-clause   The verdict is fail: `"verdict": "fail"`.  The second problem names the clause: - check: "matches findings" - where: "How common each type was, paragraph 1, fourth sentence" - detail: "Note says \"The largest diaphones needed a large compressor plant and air tanks, which tied them to stations that could house that machinery.\" topic-1.md says only \"needed a large compressor plant and air tanks.\
PASS  judge-names-souter-point-1919   The verdict is FAIL: `"verdict": "fail"`.  The first problem names the Souter Point sentence. Its location is "Fog signal types in the 1950s, Diaphones, Trinity House: Souter Point paragraph, second footnoted sentence". Its detail reads:  > "Note says \"the diaphones replaced more powerful units fitted in 1919.\" topic-1.md says only that the building \"first used compressed-air horns, which were
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict": "fail"'
````

Final reply:

````
```json
{ "verdict": "fail",
  "problems": [
    { "check": "matches findings", "where": "Fog signal types in the 1950s, Diaphones, Trinity House: Souter Point paragraph, second footnoted sentence",
      "detail": "Note says \"the diaphones replaced more powerful units fitted in 1919.\" topic-1.md says only that the building \"first used compressed-air horns, which were swapped for sirens in 1879 and for more powerful units in 1919.\" It does not say the 1953 diaphones replaced the 1919 units. The \"more powerful\" comparison is with the sirens, not the diaphones." },
    { "check": "matches findings", "where": "How common each type was, paragraph 1, fourth sentence",
      "detail": "Note says \"The largest diaphones needed a large compressor plant and air tanks, which tied them to stations that could house that machinery.\" topic-1.md says only \"needed a large compressor plant and air tanks.\" The \"which tied them to stations…\" clause is a conclusion the findings don't state." },
    { "check": "matches findings", "where": "How common each type was, paragraph 1, last sentence",
      "detail": "Note says the 1972 withdrawal \"shows they were in use at more stations than the ones named here.\" topic-1.md says only that Rathlin East's signal was discontinued in 1972 \"along with similar signals around the coast.\" It does not state the conclusion about more stations." },
    { "check": "matches findings", "where": "What could go wrong, Theft of explosives paragraph, second sentence",
      "detail": "Note says \"Irish Lights discontinued its remaining explosive signals in 1972 'for security reasons.'\" topic-1.md gives the 1972 date and the \"security reasons\" wording for Rathlin East, and says Loop Head's signal was discontinued in 1972 as well. It says Mizen Head's signal was withdrawn in 1969 and Tuskar Rock's ran until 1974. The findings do not say the 1972 withdrawal covered all remaining signals." },
    { "check": "coverage", "where": "Fog signal types in the 1950s / Open Research Questions",
      "detail": "Plan Topic 1 question 1 asks how each type worked and sounded. The note gives no explanation of how a siren worked or what it sounded like, and the Sirens and trumpets section covers only the Trevose installation. The question is neither answered nor listed under Open Research Questions." }
  ] }
```
````

#### Run 3

Grades:

````
PASS  judge-names-around-the-coast-which-clause   The reply's verdict is FAIL: `"verdict": "fail"`.  One of its problems names the target clause and says the findings don't support it. That problem is under "matches findings", at "How common each type was, sentence 5":  > "Note says the 1972 withdrawal \"around the coast\" \"shows they were in use at more stations than the ones named here.[^12]\". topic-1.md only says Rathlin East's signal was d
PASS  judge-names-compressor-which-clause   The verdict is fail: `"verdict": "fail"`.  One problem names the clause in question:  > `{ "check": "matches findings", "where": "How common each type was, sentence 4", "detail": "Note says \"The largest diaphones needed a large compressor plant and air tanks, which tied them to stations that could house that machinery.[^1]\". topic-1.md says only \"needed a large compressor plant and air tanks\"
PASS  judge-names-souter-point-1919   The verdict is FAIL: `"verdict": "fail"`.  One of the problems names the Souter Point sentence directly:  - **check:** "matches findings" - **where:** "Fog signal types in the 1950s, Diaphones, Souter Point paragraph" - **detail:** "Note says \"the diaphones replaced more powerful units fitted in 1919.[^8]\". topic-1.md says only that the building \"first used compressed-air horns, which were swa
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict": "fail"'
````

Final reply:

````
```json
{ "verdict": "fail",
  "problems": [
    { "check": "matches findings", "where": "Summary, paragraph 2",
      "detail": "Note says \"The big compressed-air signals needed engines, compressors, and air tanks.[^1]\". topic-1.md gives the Britannica passage as \"they needed a large compressor plant and air tanks\". Engines are not in that Britannica passage." },
    { "check": "matches findings", "where": "Fog signal types in the 1950s, Diaphones, Souter Point paragraph",
      "detail": "Note says \"the diaphones replaced more powerful units fitted in 1919.[^8]\". topic-1.md says only that the building \"first used compressed-air horns, which were swapped for sirens in 1879 and for more powerful units in 1919\", and that the Stone-Chance diaphones were fitted in 1953. It does not say the diaphones replaced the 1919 units." },
    { "check": "matches findings", "where": "How common each type was, sentence 4",
      "detail": "Note says \"The largest diaphones needed a large compressor plant and air tanks, which tied them to stations that could house that machinery.[^1]\". topic-1.md says only \"needed a large compressor plant and air tanks\". The \"which tied them…\" clause is an added conclusion." },
    { "check": "matches findings", "where": "How common each type was, sentence 5",
      "detail": "Note says the 1972 withdrawal \"around the coast\" \"shows they were in use at more stations than the ones named here.[^12]\". topic-1.md only says Rathlin East's signal was discontinued in 1972 \"for security reasons\" along with similar signals around the coast. The \"shows…\" clause is an added conclusion." },
    { "check": "matches findings", "where": "What could go wrong, Theft of explosives paragraph",
      "detail": "Note says \"Irish Lights discontinued its remaining explosive signals in 1972\". topic-1.md says Rathlin East was discontinued in 1972 along with similar signals. It also gives Mizen Head withdrawn in 1969 and Tuskar Rock's explosive signal lasting until 1974. No passage says 1972 ended all of the remaining signals." },
    { "check": "nothing dropped", "where": "Fog signal types in the 1950s (no bells section)",
      "detail": "topic-1.md has a Bells passage that answers the plan's Topic 1 question on how each type worked and what powered it. Britannica says bell strikers were driven by weight-driven clockwork or by a compressed-gas piston, usually carbon dioxide. It also says no source places a bell in service at a British lighthouse in the 1950s, and that Start Point's 1860s bell ran on a falling weight and was replaced by a siren. The note leaves all of this out and only lists the open question \"Was any bell still in service…\"." } ] }
```
````

### E7: The live fog-signal note, bare claude-opus-5-5

Case folder: `research-evaluator-07-live-fog-signals`. Run folder: `e7-bare`.

#### Run 1

Grades:

````
FAIL  judge-names-around-the-coast-which-clause   The verdict is FAIL (`"verdict": "fail"`), but none of the reported problems mentions the targeted clause.  There is only one problem, and it is about the missing bells section: - `"check": "nothing dropped"`, `"where": "Fog signal types in the 1950s (no bells section); Open Research Questions"`, `"detail": "Topic 1 has a findings block on bells, and the plan asks about bells by name. The note le
FAIL  judge-names-compressor-which-clause   The verdict is FAIL (`"verdict": "fail"`), but none of the problems names the diaphone clause. There is only one problem:  - `"check": "nothing dropped"`, `"where": "Fog signal types in the 1950s (no bells section); Open Research Questions"`. Its detail is about the bells finding being left out: "Topic 1 has a findings block on bells... The note leaves almost all of it out... A short bells entry 
FAIL  judge-names-souter-point-1919   Evidence: The verdict is FAIL (`"verdict": "fail"`). The check, though, also needs one of the reported problems to name the Souter Point sentence, and none does.  The reply lists only one problem:  - check: "nothing dropped" - where: "Fog signal types in the 1950s (no bells section); Open Research Questions" - detail: "Topic 1 has a findings block on bells, and the plan asks about bells by name. 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict": "fail"'
````

Final reply:

````
```json
{"verdict": "fail", "problems": [{"check": "nothing dropped", "where": "Fog signal types in the 1950s (no bells section); Open Research Questions", "detail": "Topic 1 has a findings block on bells, and the plan asks about bells by name. The note leaves almost all of it out. It never says that no source the researcher found put a bell in service at a British lighthouse in the 1950s. It also leaves out Britannica's account of how bells were struck: by weight-driven clockwork, or by a piston run on compressed gas, usually carbon dioxide. It also leaves out Canmore's note that the earliest warnings at some NLB stations were cliff-top bells, later replaced by compressed-air foghorns. All that is left is the open question 'Was any bell still in service at a British lighthouse in the 1950s?', so the reader cannot tell that the researcher looked and found nothing. A short bells entry should give this negative result, with the Britannica and Canmore detail as context and labelled as outside the decade."}]}
```
````

#### Run 2

Grades:

````
PASS  judge-names-around-the-coast-which-clause   The verdict is `"verdict": "fail"`.  One problem names the clause directly. Under check "matches findings", where "Fog signal types in the 1950s > How common each type was", it says: "The note says the 1972 withdrawal 'shows they were in use at more stations than the ones named here.' The findings only say Rathlin East's signal was discontinued 'along with similar signals around the coast.' Loop 
PASS  judge-names-compressor-which-clause   The verdict is a fail: `"verdict": "fail"`.  One problem names the clause. It is the second problem, a "matches findings" check located at "Fog signal types in the 1950s > How common each type was". Its detail says: "The line saying the size of the compressor plant 'tied them to stations that could house that machinery' is also the writer's inference, not a finding."  That quotes the clause in qu
PASS  judge-names-souter-point-1919   Evidence:  - The verdict is `"verdict": "fail"`. - One problem names the Souter Point sentence directly. Its location is `"Fog signal types in the 1950s > Diaphones > Trinity House: Souter Point"`, and its detail reads: "The note says 'The same page says the diaphones replaced more powerful units fitted in 1919.' The findings report two separate things: the page says the signal was upgraded to mo
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict": "fail"'
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "matches findings", "where": "Fog signal types in the 1950s > Explosive signals > Trinity House: Beachy Head; Starting, keeping the rhythm, and stopping > Explosive charges", "detail": "The note cites Worldwide Lighthouses [^10] for 'one of the last lighthouses still using explosive signals' and for the 'Signal, Fog, Mk I' gun-cotton charge. Topic 1 says the first claim came from a search-tool summary of a different source. It says the Mk I claim came only from search-tool summaries that trace to Wikipedia's Foghorn article, and was not verified. The body also states the Mk I as plain fact twice, and under the Beachy Head heading. The findings call it a separate Trinity House development and do not tie it to Beachy Head or to the 1950s."}, {"check": "matches findings", "where": "Fog signal types in the 1950s > How common each type was", "detail": "The note says the 1972 withdrawal 'shows they were in use at more stations than the ones named here.' The findings only say Rathlin East's signal was discontinued 'along with similar signals around the coast.' Loop Head, which the note names, is one of those. The findings give no count, so the note's claim goes beyond them. The line saying the size of the compressor plant 'tied them to stations that could house that machinery' is also the writer's inference, not a finding."}, {"check": "matches findings", "where": "Fog signal types in the 1950s > Diaphones > Trinity House: Souter Point", "detail": "The note says 'The same page says the diaphones replaced more powerful units fitted in 1919.' The findings report two separate things: the page says the signal was upgraded to more powerful units in 1919, and the current diaphones were fitted in 1953. The page is not reported as saying that the diaphones replaced the 1919 units."}, {"check": "nothing dropped", "where": "Fog signal types in the 1950s (no bell section); Open Research Questions", "detail": "Topic 1 reports that no source it found places a bell in service at a British lighthouse in the 1950s. It also gives Britannica's description of how bell strikers worked (weight-driven clockwork, or a piston driven by compressed gas, usually CO2). The note keeps none of this and only asks whether any bell was in service as an open question. It also drops the Baily/East Pier caveat that the sources give no date for when those diaphones were replaced."}]}
````

#### Run 3

Grades:

````
PASS  judge-names-around-the-coast-which-clause   The verdict is fail: `"verdict": "fail"`.  The second problem names the clause and says the findings don't support it. It is filed under check "matches findings", where "Fog signal types in the 1950s > How common each type was": > "The note says the 1972 withdrawal of signals 'around the coast' 'shows they were in use at more stations than the ones named here.' The findings say only that Rathlin 
FAIL  judge-names-compressor-which-clause   The verdict is FAIL (`"verdict": "fail"`), but neither problem names the diaphone compressor-plant clause.  The two problems are:  1. **Beachy Head citation.** "The note says 'One source calls Beachy Head one of the last lighthouses still using explosive signals' and cites [^10] (Worldwide Lighthouses)... The citation attributes the claim to the wrong source..." 2. **1972 withdrawal.** "The note 
FAIL  judge-names-souter-point-1919   The verdict is FAIL (`"verdict": "fail"`), but neither of the two problems mentions the Souter Point sentence.  The two problems are: 1. Beachy Head: "The note says 'One source calls Beachy Head one of the last lighthouses still using explosive signals' and cites [^10] (Worldwide Lighthouses)... The citation attributes the claim to the wrong source..." 2. How common each type was: "The note says 
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
PASS  verdict-fail  found '"verdict": "fail"'
````

Final reply:

````
{"verdict": "fail", "problems": [{"check": "matches findings", "where": "Fog signal types in the 1950s > Explosive signals > Trinity House: Beachy Head (East Sussex)", "detail": "The note says 'One source calls Beachy Head one of the last lighthouses still using explosive signals' and cites [^10] (Worldwide Lighthouses). In topic-1, that claim comes from 'a search-tool summary of another source' (the same one that gives 1976 and the ELG 500), not from Worldwide Lighthouses. The citation attributes the claim to the wrong source, and the note should say it comes only from an unnamed search-tool summary."}, {"check": "matches findings", "where": "Fog signal types in the 1950s > How common each type was", "detail": "The note says the 1972 withdrawal of signals 'around the coast' 'shows they were in use at more stations than the ones named here.' The findings say only that Rathlin East's signal was discontinued in 1972 'along with similar signals around the coast'. They do not say other stations used explosive signals beyond the ones named, and Loop Head, which is named, was also discontinued in 1972. This conclusion goes beyond the findings and should be removed or worded as uncertain."}]}
````
