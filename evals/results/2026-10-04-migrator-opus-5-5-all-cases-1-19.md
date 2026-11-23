# 2026-10-04 Migrator Run: All Cases 1-19

This run was done by hand with `_tools/migrator-run.py`, outside `claude plugin eval`. The record checks were run by `_tools/record-check.py`. The case Pass lines were judged by a Claude Opus 5.5 worker session reading every output. The LLM graders in each case's `graders/` folder were not run.

## What Was Run

- **Date:** 2026-10-04, 17:35 to 17:43 EDT.
- **Agent:** `script-asst:migrator` (`agents/migrator.md`), model `claude-opus-5-5`, pinned in the agent file. Every run's stream reports `claude-opus-5-5`.
- **Claude Code:** 2.1.289.
- **Runs:** 57. Nineteen cases, three runs each, at most five at a time.
- **Rules given:** `_fixtures/rules/migrator-rules.md` alone. It is byte-identical to the plugin's `references/migrator-rules.md` (checked with `cmp` before the run).
- **Command:** four batches into one output folder, one batch per call:

```bash
OUT=$(mktemp -d)   # /var/folders/jp/t3th_wsd03xgpgdnsn9ys63w0000gn/T/tmp.rOsh85Dss6
python3 _tools/migrator-run.py --out "$OUT" --runs 3 --cases lost-detail-01-plain-copy lost-detail-02-split-across-notes lost-detail-03-area-note-rewrite lost-detail-04-existing-text lost-detail-05-dense-bullet
python3 _tools/migrator-run.py --out "$OUT" --runs 3 --cases lost-detail-06-area-note-populated lost-detail-07-batch-two-notes lost-detail-08-merge-by-comment over-promotion-09-confident-wording over-promotion-10-partial-graduation
python3 _tools/migrator-run.py --out "$OUT" --runs 3 --cases misread-comment-11-scoped-rejection misread-comment-12-unusual-comment misread-comment-13-ambiguous-comment unasked-migration-14-outside-range unit-record-15-split-and-merge
python3 _tools/migrator-run.py --out "$OUT" --runs 3 --cases tentative-in-area-note-16-tagged-child missed-unit-17-scattered-tags unasked-edit-18-typos-and-contradiction wrong-destination-19-no-destination-named
```

- **What the runner launches per run:** `claude -p <prompt> --agent script-asst:migrator --plugin-dir ~/.claude/plugins/local/script-asst --setting-sources project --tools Read,Write,Edit,Glob,Grep --permission-mode acceptEdits --output-format stream-json --verbose --no-session-persistence`, from the run's `work/` folder, with `CLAUDECODE` removed from the environment.
- **Errors and timeouts:** none. Every run exited 0. No run was repeated.

Prompt used verbatim, the same for all nineteen cases:

> This is a migration run. The project folder is project/. The rules file is rules/migrator-rules.md. The batch is the whole of project/brain-dump.md. The writer typed no request for this run. Write the unit record file to run/unit-records.json.

## Summary Table

Bare numbers are from eval-cases-migrator.md 06.2, 07.5, 08.7 and 09.6. A case passes only when its Pass line and the every-case checks in eval-cases-migrator.md 05.1 both hold. Record check counts runs where all five lines printed PASS.

| Case | Bare, passed | Migrator, passed | Record check | Cost |
| --- | --- | --- | --- | --- |
| lost-detail-01-plain-copy | 3 of 3 | 1 of 3 | 3 of 3 | $0.97 |
| lost-detail-02-split-across-notes | 3 of 3 | 3 of 3 | 3 of 3 | $0.94 |
| lost-detail-03-area-note-rewrite | 3 of 3 | 3 of 3 | 3 of 3 | $0.87 |
| lost-detail-04-existing-text | 3 of 3 | 1 of 3 | 3 of 3 | $0.83 |
| lost-detail-05-dense-bullet | 2 of 3 | 1 of 3 | 3 of 3 | $0.97 |
| lost-detail-06-area-note-populated | 3 of 3 | 3 of 3 | 3 of 3 | $1.01 |
| lost-detail-07-batch-two-notes | 3 of 3 | 1 of 3 | 3 of 3 | $1.31 |
| lost-detail-08-merge-by-comment | 3 of 3 | 2 of 3 | 3 of 3 | $0.89 |
| over-promotion-09-confident-wording | 3 of 3 | 3 of 3 | 3 of 3 | $1.09 |
| over-promotion-10-partial-graduation | 1 of 3 | 3 of 3 | 3 of 3 | $0.94 |
| misread-comment-11-scoped-rejection | 2 of 3 | 3 of 3 | 3 of 3 | $0.99 |
| misread-comment-12-unusual-comment | 3 of 3 | 3 of 3 | 3 of 3 | $0.88 |
| misread-comment-13-ambiguous-comment | 3 of 3 | 3 of 3 | 3 of 3 | $0.79 |
| unasked-migration-14-outside-range | 3 of 3 | 2 of 3 | 3 of 3 | $1.06 |
| unit-record-15-split-and-merge | 3 of 3 | 3 of 3 | 3 of 3 | $1.09 |
| tentative-in-area-note-16-tagged-child | 3 of 3 | 3 of 3 | 3 of 3 | $0.96 |
| missed-unit-17-scattered-tags | 3 of 3 | 3 of 3 | 3 of 3 | $1.04 |
| unasked-edit-18-typos-and-contradiction | 3 of 3 | 2 of 3 | 3 of 3 | $0.85 |
| wrong-destination-19-no-destination-named | 3 of 3 | 3 of 3 | 3 of 3 | $1.08 |
| **Total** | **53 of 57** | **46 of 57** | **57 of 57** | **$18.55** |

## Findings

1. **Nine of the eleven fails have one cause: a `#status/tentative` tag on an untagged copy.** Case 1 r1 and r2, case 4 r1 and r3, case 7 r1 and r3 (all fourteen copies), case 8 r2, case 14 r2 (all three copies) and case 18 r2. In every one of them the Pass line itself held. The status is right; the tag only restates the Idea Note's default. eval-cases-migrator.md 05.1 item 3 says "No tag means no tag", so each is a fail.
   - The agents name the cause. migrator-rules.md 03.7 item 1 says: "The Migrator writes a status tag at the destination, when it migrates an Idea Unit. The tag carries the status the writer set at the source." Case 1 r1: "I added it because the rules have me tag every migrated copy with its status." migrator-rules.md 03.3 item 3 says "A tag that only restates the default can go". The runs that left the tag off reasoned from the note's default: untagged in an Idea Note already means tentative. Case 4 r2 saw both readings: "The rules file also says to write a tag on migrated copies, so the Migration checker may flag this."
   - The bare runs never did this. The old terminology snapshot had a similar sentence (terminology-script-asst.md 03.2, "It writes the status the writer set as a tag where it migrates the unit"), but it was not a bullet of its own.
   - Without this one cause, the Migrator would have passed 55 of 57.
2. **Case 5: two of three runs let the hedged name drift.** r1 uses "Ansel" as settled on three later lines and r2 on one. r3 states the hedge once and says "the keeper before Mara" after. Bare was 2 of 3. The rule about stating a hedge once is not in the agent file or the rules file (spec-migrator.md 07 keeps it with the cases).
3. **Case 10 went from 1 of 3 to 3 of 3.** Every run graduated only the first idea and asked about the other two in `questions`. spec-migrator.md 07 item 1 is in the agent file.
4. **Case 11 went from 2 of 3 to 3 of 3.** Every run tagged the rejected line `#status/rejected`, gave the writer's reason, and kept the carve-out out of the Rejected section. Only r3 fixed the neighbouring lines ("She" to "Mara", dropped "too"), and recorded both in `edits`.
5. **The Brain Dump doc was untouched in all 57 runs.** In case 12, no run edited `brain-dump.md` and no Write or Edit call targeted it. Every run put the provisional tag on the copy only.
6. **Record checks: 57 of 57 runs passed all five.** Every record was written before the first note write. No run wrote outside `project/` and `run/`.
7. **Case 18: no run fixed "dosnt" in the copy.** Bare runs fixed it in two of three. Either way is allowed (eval-cases-migrator.md 09.4).

## Observed, Not Graded

1. **`left_in_place` is used for things that are not batch material.** Case 6 r2, case 11 r1 and r3, and case 16 r2 list the writer's routing comment. Case 6 r3 lists the migrated source line, to explain the dropped note-to-self. If the Run script renders `left_in_place` as "Left in place, and why", the writer will see these.
2. **Extra questions.** Case 9 r1 and r2 and case 14 r1 and r3 ask whether lines worded as decided ("This is locked", "Definitely keeping this") were meant as committed. No Pass line asks for this. Case 14 asked about the ferry line in all three runs.
3. **Small context loss in one split.** Case 15 r1's Tobias copy reads "Tobias used to ring the harbour bell by hand for pocket money", without "at dusk". The Harrow Point copy keeps "at dusk". r2 and r3 kept it in both.
4. **"Okay so" dropped.** All three case 5 runs dropped the writer's opening "Okay so" from an Idea Note copy. No Pass line covers it.
5. **Whole-note writes.** Case 11 r3 and case 17 r1 wrote the destination note with one Write call instead of Edit. The diffs show no change to existing lines beyond what the record holds.

## Caveats

1. The judged checks were done by Claude reading each output, not by the eval tool's LLM graders and not calibrated against Moe.
2. `record-check.py` check 5 confirms the record is written before the first note write. It cannot tell whether a later note change was preceded by a record rewrite. Case 11 r3 is the one run that changed the record after a note write; its tool calls were read by hand, and the record was rewritten first.
3. The cost per run is the `total_cost_usd` in each stream's result event. The runner prints them rounded; the four batch totals it printed were $4.59, $5.24, $4.80 and $3.92.
4. Outputs stay in `/var/folders/jp/t3th_wsd03xgpgdnsn9ys63w0000gn/T/tmp.rOsh85Dss6`, which is a temporary folder the system may clear.

## Full Outputs

For each case: the starting notes, then each run's verdict, every changed note after the run, the record file, and the record check. No run changed the Brain Dump doc.

### Case 1: Plain copy with specifics

Case folder: `lost-detail-01-plain-copy`

**Fixture: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional
- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat.

%% migrate all the bullets between "- Mara's lighthouse" to "Maybe the lamp failed" %%

%% Agent, these go in idea-mara-lighthouse. %%
````

#### Run 1

**Verdict: FAIL.** The Pass line holds: 214, aloud, her father, March 3 and her brother's boat all survive; "Maybe" and "Not sure if it's too neat" are kept; the first copy carries the provisional tag. Fails eval-cases-migrator.md 05.1 item 3 ("No tag means no tag"), and eval-cases-migrator.md 05.2 item 1 says the second copy carries none. Offending line: `- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat. #status/tentative`. The agent's reply gives its reason: "I added it because the rules have me tag every migrated copy with its status."

Cost: $0.32

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional
- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat. #status/tentative
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The writer's provisional tag and the migrate comment (lines 13 and 15) send it to idea-mara-lighthouse. Copied in the writer's words so the 214 steps, the nightly counting aloud, and the father's habit all stay together."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- Mara's lighthouse\" to \"Maybe the lamp failed\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat. #status/tentative"]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The migrate comment covers this bullet and the routing comment names idea-mara-lighthouse. Untagged in the Brain Dump doc, so tentative; copied verbatim to keep the hedge, the March 3 date, the brother's boat, and the writer's rationale."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: FAIL.** The Pass line holds, as in r1. Fails eval-cases-migrator.md 05.1 item 3 ("No tag means no tag"). Offending line: `- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat. #status/tentative`. Reply: "The rules say to write a status tag on every migrated copy".

Cost: $0.32

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional
- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat. #status/tentative
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The writer's provisional tag and the migrate comment both cover this bullet, and the routing comment sends it to idea-mara-lighthouse. Copied in the writer's words, keeping every specific (214 steps, aloud, every night, from her father)."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- Mara's lighthouse\" to \"Maybe the lamp failed\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat. #status/tentative"
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The migrate comment names this bullet as the end of its range, and the routing comment sends it to idea-mara-lighthouse. It is untagged, so it keeps the Brain Dump default, tentative; the hedge \"Maybe\" and the rationale \"Not sure if it's too neat\" stay with it."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Every planted specific survives. The hedge and "not sure if it's too neat" are kept. The first copy is provisional; the second carries no tag.

Cost: $0.33

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional
- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- Mara's lighthouse\" to \"Maybe the lamp failed\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The migrate comment scopes this bullet and the routing comment names idea-mara-lighthouse. Copied in the writer's words, keeping every specific (214 steps, counting aloud nightly, the father's habit) and the writer's provisional tag."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- Mara's lighthouse\" to \"Maybe the lamp failed\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The migrate comment scopes this bullet and the routing comment names idea-mara-lighthouse. Copied verbatim with its hedge and rationale (\"Not sure if it's too neat.\"); untagged, so it stays tentative, which is the Idea Note's default and needs no tag."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 2: Split across two notes

Case folder: `lost-detail-02-split-across-notes`

**Fixture: Ideas/idea-mara-habits.md**

````markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits
````

**Fixture: Ideas/idea-tobias.md**

````markdown
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- Mara's brother Tobias drowned when she was nine. She still sets a place for him at dinner.

%% Agent, migrate this. The drowning goes in idea-tobias, the dinner habit in idea-mara-habits. %%
````

#### Run 1

**Verdict: PASS.** The habits line names Tobias: "Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine." Repeating the drowning is allowed (eval-cases-migrator.md 06.3 item 3). The Tobias line has "drowned" and her age. No tags.

Cost: $0.33

**After: Ideas/idea-mara-habits.md**

````markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits

- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine.
````

**After: Ideas/idea-tobias.md**

````markdown
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Mara's brother Tobias drowned when she was nine.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this. The drowning goes in idea-tobias, the dinner habit in idea-mara-habits."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara's brother Tobias drowned when she was nine. She still sets a place for him at dinner."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Mara's brother Tobias drowned when she was nine."]
        },
        {
          "note": "Ideas/idea-mara-habits.md",
          "under": "# Idea - Mara Habits",
          "lines": ["- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The writer's comment routes the drowning to idea-tobias and the dinner habit to idea-mara-habits. The habit copy names Mara and her brother Tobias, and keeps that he drowned when she was nine, so 'she' and 'him' still read correctly on their own; no tag is written because untagged lines in an Idea Note are already tentative, the source's default."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** Same copies as r1.

Cost: $0.32

**After: Ideas/idea-mara-habits.md**

````markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits

- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine.
````

**After: Ideas/idea-tobias.md**

````markdown
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Mara's brother Tobias drowned when she was nine.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this. The drowning goes in idea-tobias, the dinner habit in idea-mara-habits."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara's brother Tobias drowned when she was nine. She still sets a place for him at dinner."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Mara's brother Tobias drowned when she was nine."]
        },
        {
          "note": "Ideas/idea-mara-habits.md",
          "under": "# Idea - Mara Habits",
          "lines": ["- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes the drowning to idea-tobias and the dinner habit to idea-mara-habits. The habits line names Tobias and his drowning so 'him' still reads on its own; no tag was given, so both copies keep the Brain Dump default, tentative, which an Idea Note's untagged default already carries."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same copies as r1.

Cost: $0.29

**After: Ideas/idea-mara-habits.md**

````markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits

- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine.
````

**After: Ideas/idea-tobias.md**

````markdown
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Mara's brother Tobias drowned when she was nine.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this. The drowning goes in idea-tobias, the dinner habit in idea-mara-habits."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara's brother Tobias drowned when she was nine. She still sets a place for him at dinner."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Mara's brother Tobias drowned when she was nine."]
        },
        {
          "note": "Ideas/idea-mara-habits.md",
          "under": "# Idea - Mara Habits",
          "lines": ["- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The writer's comment routes the drowning to idea-tobias and the dinner habit to idea-mara-habits. The habit copy names Tobias and keeps the drowning so 'him' and 'still' read on their own; both copies stay untagged, since untagged in an Idea Note already means tentative."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 3: Rewrite into an Area Note

Case folder: `lost-detail-03-area-note-rewrite`

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job. I really like this. Tobias as the reason feels more honest than duty. #status/committed

%% Agent, this belongs in char-mara. %%
````

**Fixture: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Core

## Motivation and Intention

# Bio

## General

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
````

#### Run 1

**Verdict: PASS.** Both story facts stated plainly under Motivation and Intention. "I really like this" dropped. Rationale holds "Tobias as the reason feels more honest than duty." word for word. No status tag in the Area Note.

Cost: $0.29

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Core

## Motivation and Intention

- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job.

# Bio

## General

# Psychology

## Values, Beliefs, etc.

# Rationale

- Tobias as the reason feels more honest than duty.

# Rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job. I really like this. Tobias as the reason feels more honest than duty. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## Motivation and Intention",
          "lines": ["- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job."]
        },
        {
          "note": "char-mara.md",
          "under": "# Rationale",
          "lines": ["- Tobias as the reason feels more honest than duty."]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The committed tag covers the one story sentence, and the comment routes it to char-mara; it goes under Motivation and Intention with both specifics kept (Tobias rather than ships, and the town's belief that it's only her job). \"I really like this\" is a note-to-self and is dropped; the reason goes to Rationale in the writer's words."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** Same as r1.

Cost: $0.29

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Core

## Motivation and Intention

- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job.

# Bio

## General

# Psychology

## Values, Beliefs, etc.

# Rationale

- Tobias as the reason feels more honest than duty.

# Rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job. I really like this. Tobias as the reason feels more honest than duty. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## Motivation and Intention",
          "lines": ["- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job."]
        },
        {
          "note": "char-mara.md",
          "under": "# Rationale",
          "lines": ["- Tobias as the reason feels more honest than duty."]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The tag commits the story sentence, which holds both Mara's real reason and the town's belief, so both specifics graduate to char-mara as the comment routes, under Motivation and Intention. \"I really like this\" is a bare like and is dropped; \"Tobias as the reason feels more honest than duty\" is rationale and goes to Rationale in the writer's words."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same as r1, except the statement reads "...not for ships, while the town believes she is only doing her job." Both facts are there; "while" for "and" does not change a fact.

Cost: $0.29

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Core

## Motivation and Intention

- Mara keeps the lamp lit for Tobias, not for ships, while the town believes she is only doing her job.

# Bio

## General

# Psychology

## Values, Beliefs, etc.

# Rationale

- Tobias as the reason feels more honest than duty.

# Rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job. I really like this. Tobias as the reason feels more honest than duty. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## Motivation and Intention",
          "lines": ["- Mara keeps the lamp lit for Tobias, not for ships, while the town believes she is only doing her job."]
        },
        {
          "note": "char-mara.md",
          "under": "# Rationale",
          "lines": ["- Tobias as the reason feels more honest than duty."]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The tag commits the one-sentence story proposition, and the comment routes it to char-mara. The statement goes under Motivation and Intention and keeps the town's belief. The writer's reason goes under Rationale in the writer's words. \"I really like this\" is a bare note-to-self, so it is dropped."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 4: Existing text left alone

Case folder: `lost-detail-04-existing-text`

**Fixture: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- The lamp could run on something stranger than oil. Maybe it burns letters.

%% Agent, migrate this to idea-mara-lighthouse. %%
````

#### Run 1

**Verdict: FAIL.** The Pass line holds: the new unit is added and the whale-oil line is unchanged to the character. Fails eval-cases-migrator.md 05.1 item 3 ("No tag means no tag"). Offending line: `- The lamp could run on something stranger than oil. Maybe it burns letters. #status/tentative`. Reply: "I added `#status/tentative` to the copy because the rules say to tag what I migrate."

Cost: $0.28

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp could run on something stranger than oil. Maybe it burns letters. #status/tentative
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The lamp could run on something stranger than oil. Maybe it burns letters."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": ["- The lamp could run on something stranger than oil. Maybe it burns letters. #status/tentative"]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names idea-mara-lighthouse, and the unit is about the lamp's fuel, so it goes under The lamp next to the whale-oil line. It keeps the writer's words and hedges ('could', 'Maybe') and stays tentative by the Brain Dump default; the existing whale-oil line is left untouched as an alternative."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** New unit added with no tag; whale-oil line unchanged. The reply notes the conflict the other runs resolved the other way: "The rules file also says to write a tag on migrated copies, so the Migration checker may flag this."

Cost: $0.28

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp could run on something stranger than oil. Maybe it burns letters.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The lamp could run on something stranger than oil. Maybe it burns letters."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": [
            "- The lamp could run on something stranger than oil. Maybe it burns letters."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names idea-mara-lighthouse, and the unit is about the lamp's fuel, so it goes under The lamp, after the existing whale-oil line, which stays as it is. The two sentences stay together because \"it\" means the lamp, and the hedges are kept word for word."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: FAIL.** The Pass line holds, as in r1. Fails eval-cases-migrator.md 05.1 item 3 ("No tag means no tag"). Offending line: `- The lamp could run on something stranger than oil. Maybe it burns letters. #status/tentative`.

Cost: $0.27

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp could run on something stranger than oil. Maybe it burns letters. #status/tentative
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The lamp could run on something stranger than oil. Maybe it burns letters."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": ["- The lamp could run on something stranger than oil. Maybe it burns letters. #status/tentative"]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names idea-mara-lighthouse, and the unit is about the lamp, so it goes under 'The lamp' after the existing whale-oil line, which stays untouched as an alternative. The two sentences stay together because 'it' means the lamp; the comment sets no status, so it keeps the Brain Dump default, tentative."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 5: Dense bullet into a populated Idea Note

Case folder: `lost-detail-05-dense-bullet`

**Fixture: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- Okay so the keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step? Maybe she logged every ship that didn't come back, 31 of them, going back to 1987. Does Mara find it, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out. What if the last entry is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.

%% Agent, migrate this to idea-mara-lighthouse. %%
````

#### Run 1

**Verdict: FAIL.** Every specific survives (Ansel, second logbook, lamp room, 40th step, 31, 1987, different handwriting, key, harbourmaster, Pell), no question became a `- [?]` line, and the existing lines are unchanged. The hedge "I'm thinking a woman named Ansel" is stated once, then "Ansel" is used as a settled name on three later lines. Under the ruling in eval-cases-migrator.md 07.1 this is a small fail. Offending lines: `- Maybe Ansel logged every ship that didn't come back in her second logbook, 31 of them, going back to 1987.` / `- Does Mara find Ansel's second logbook, or does Tobias find it first? ...` / `- What if the last entry in Ansel's second logbook is in a different handwriting? ...`

Cost: $0.33

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
- The keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?
- Maybe Ansel logged every ship that didn't come back in her second logbook, 31 of them, going back to 1987.
- Does Mara find Ansel's second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.
- What if the last entry in Ansel's second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Okay so the keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step? Maybe she logged every ship that didn't come back, 31 of them, going back to 1987. Does Mara find it, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out. What if the last entry is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The keeper before Mara",
          "lines": ["- The keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?"]
        },
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The keeper before Mara",
          "lines": ["- Maybe Ansel logged every ship that didn't come back in her second logbook, 31 of them, going back to 1987."]
        },
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The keeper before Mara",
          "lines": ["- Does Mara find Ansel's second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out."]
        },
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The keeper before Mara",
          "lines": ["- What if the last entry in Ansel's second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes the bullet to idea-mara-lighthouse; it is about the keeper before Mara, so it goes under that heading, split into four adjacent units (the logbook and its hiding place, the ship log, who finds it, the handwriting and the key) with 'she' and 'it' replaced by Ansel and the logbook so each reads on its own. Untagged in the Brain Dump doc, so it stays tentative and carries no tag, matching the note's default; every specific, hedge, and prose question is kept, and only the filler 'Okay so' is dropped."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: FAIL.** Every specific survives, no `- [?]` line, existing lines unchanged. The hedge is stated once on the first line, "(I'm thinking a woman named Ansel)", but one later line uses the name as settled: `- Maybe Ansel logged every ship that didn't come back in the second logbook, 31 of them, going back to 1987.` "Maybe" there hedges the logging, not the name. Small fail under the ruling. The other later lines say "the second logbook".

Cost: $0.32

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
- The keeper before Mara (I'm thinking a woman named Ansel) kept a second logbook nobody knew about.
- Is the second logbook hidden in the lamp room or under the 40th step?
- Maybe Ansel logged every ship that didn't come back in the second logbook, 31 of them, going back to 1987.
- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.
- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Okay so the keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step? Maybe she logged every ship that didn't come back, 31 of them, going back to 1987. Does Mara find it, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out. What if the last entry is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The keeper before Mara",
          "lines": [
            "- The keeper before Mara (I'm thinking a woman named Ansel) kept a second logbook nobody knew about.",
            "- Is the second logbook hidden in the lamp room or under the 40th step?",
            "- Maybe Ansel logged every ship that didn't come back in the second logbook, 31 of them, going back to 1987.",
            "- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.",
            "- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes the whole bullet to idea-mara-lighthouse, and it belongs under the existing 'The keeper before Mara' heading. The dense bullet is split into adjacent lines, each naming the logbook or Ansel so it reads on its own, with every specific, hedge, and prose question kept; untagged in the Brain Dump doc, so tentative and no tag is written."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** The hedged name is stated once, with its hedge. The next line says "the keeper before Mara", and the others say "the second logbook". Every specific survives, no `- [?]` line, existing lines unchanged.

Cost: $0.32

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
- The keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?
- Maybe the keeper before Mara logged every ship that didn't come back in her second logbook, 31 of them, going back to 1987.
- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.
- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Okay so the keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step? Maybe she logged every ship that didn't come back, 31 of them, going back to 1987. Does Mara find it, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out. What if the last entry is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The keeper before Mara",
          "lines": [
            "- The keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?",
            "- Maybe the keeper before Mara logged every ship that didn't come back in her second logbook, 31 of them, going back to 1987.",
            "- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.",
            "- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes the bullet to idea-mara-lighthouse; it is about the keeper before Mara, so it goes under that heading after the existing line, split into four adjacent pieces that each name the logbook so they read on their own. The bullet is untagged in the Brain Dump doc, so it stays tentative, which is the Idea Note's default, and the prose questions and hedges stay in the writer's words."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 6: Long committed bullet into a populated Area Note

Case folder: `lost-detail-06-area-note-populated`

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- Mara took over the lighthouse at nineteen, the winter after her father's stroke, and she has never once let the lamp go dark, not even on the night of Tobias's funeral. I really want to keep this. She keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it. The coat works better than a photograph because she has to walk past it every day. #status/committed

%% Agent, this belongs in char-mara. %%
````

**Fixture: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Core

## Motivation and Intention

# Bio

## General

- Mara has kept the lighthouse for eleven years.
- Mara's younger brother Tobias drowned six years ago.

# Psychology

## Values, Beliefs, etc.

# Rationale

- A lighthouse keeper who is afraid of the sea is the whole joke of her.

# Rejected
````

#### Run 1

**Verdict: PASS.** Every fact stated plainly: nineteen, the winter after her father's stroke, the lamp never dark, the funeral night, the oilskin coat, the hook by the door, nobody may move it. "I really want to keep this" dropped. The photograph sentence is in Rationale word for word. All three existing lines unchanged; the eleven-years line is not merged.

Cost: $0.33

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Core

## Motivation and Intention

# Bio

## General

- Mara has kept the lighthouse for eleven years.
- Mara's younger brother Tobias drowned six years ago.
- Mara took over the lighthouse at nineteen, the winter after her father's stroke.
- Mara has never once let the lighthouse lamp go dark, not even on the night of Tobias's funeral.
- Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it.

# Psychology

## Values, Beliefs, etc.

# Rationale

- A lighthouse keeper who is afraid of the sea is the whole joke of her.
- The coat works better than a photograph because she has to walk past it every day.

# Rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara took over the lighthouse at nineteen, the winter after her father's stroke, and she has never once let the lamp go dark, not even on the night of Tobias's funeral. I really want to keep this. She keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it. The coat works better than a photograph because she has to walk past it every day. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": [
            "- Mara took over the lighthouse at nineteen, the winter after her father's stroke.",
            "- Mara has never once let the lighthouse lamp go dark, not even on the night of Tobias's funeral.",
            "- Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it."
          ]
        },
        {
          "note": "char-mara.md",
          "under": "# Rationale",
          "lines": [
            "- The coat works better than a photograph because she has to walk past it every day."
          ]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The trailing committed tag sits on a bullet of plain, unhedged statements, so it covers both the lighthouse and coat ideas; the comment routes the bullet to char-mara. Every specific is kept as plain statements under Bio > General, the coat's reason goes to Rationale in the writer's words, and the note-to-self \"I really want to keep this\" is dropped."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** Note identical to r1. The record lists the routing comment in `left_in_place`.

Cost: $0.33

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Core

## Motivation and Intention

# Bio

## General

- Mara has kept the lighthouse for eleven years.
- Mara's younger brother Tobias drowned six years ago.
- Mara took over the lighthouse at nineteen, the winter after her father's stroke.
- Mara has never once let the lighthouse lamp go dark, not even on the night of Tobias's funeral.
- Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it.

# Psychology

## Values, Beliefs, etc.

# Rationale

- A lighthouse keeper who is afraid of the sea is the whole joke of her.
- The coat works better than a photograph because she has to walk past it every day.

# Rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara took over the lighthouse at nineteen, the winter after her father's stroke, and she has never once let the lamp go dark, not even on the night of Tobias's funeral. I really want to keep this. She keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it. The coat works better than a photograph because she has to walk past it every day. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": [
            "- Mara took over the lighthouse at nineteen, the winter after her father's stroke.",
            "- Mara has never once let the lighthouse lamp go dark, not even on the night of Tobias's funeral.",
            "- Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it."
          ]
        },
        {
          "note": "char-mara.md",
          "under": "# Rationale",
          "lines": [
            "- The coat works better than a photograph because she has to walk past it every day."
          ]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "Every story statement in the bullet is plain and unhedged, so the writer's trailing committed tag covers all of them, and the comment routes the bullet to char-mara. The story facts went under Bio > General as plain statements with every specific kept (age nineteen, father's stroke, lamp never dark, funeral night, oilskin coat on the hook, nobody may move it). The coat-versus-photograph reason went to Rationale in the writer's words. The bare note-to-self 'I really want to keep this.' was dropped."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 12,
        "text": "%% Agent, this belongs in char-mara. %%"
      },
      "why": "Routing comment for u1. It was followed and stays in the Brain Dump doc as history."
    }
  ],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Note identical to r1. The record lists the migrated source line in `left_in_place` to explain the dropped note-to-self.

Cost: $0.35

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Core

## Motivation and Intention

# Bio

## General

- Mara has kept the lighthouse for eleven years.
- Mara's younger brother Tobias drowned six years ago.
- Mara took over the lighthouse at nineteen, the winter after her father's stroke.
- Mara has never once let the lighthouse lamp go dark, not even on the night of Tobias's funeral.
- Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it.

# Psychology

## Values, Beliefs, etc.

# Rationale

- A lighthouse keeper who is afraid of the sea is the whole joke of her.
- The coat works better than a photograph because she has to walk past it every day.

# Rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara took over the lighthouse at nineteen, the winter after her father's stroke, and she has never once let the lamp go dark, not even on the night of Tobias's funeral. I really want to keep this. She keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it. The coat works better than a photograph because she has to walk past it every day. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": [
            "- Mara took over the lighthouse at nineteen, the winter after her father's stroke.",
            "- Mara has never once let the lighthouse lamp go dark, not even on the night of Tobias's funeral.",
            "- Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it."
          ]
        },
        {
          "note": "char-mara.md",
          "under": "# Rationale",
          "lines": [
            "- The coat works better than a photograph because she has to walk past it every day."
          ]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The writer's committed tag covers every story proposition in the bullet, none of which is hedged, and the comment routes it to char-mara. The three propositions can each stand alone, so they graduate as separate plain statements under Bio > General with every specific kept; the coat sentence's reason goes to Rationale in the writer's words."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara took over the lighthouse at nineteen, the winter after her father's stroke, and she has never once let the lamp go dark, not even on the night of Tobias's funeral. I really want to keep this. She keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it. The coat works better than a photograph because she has to walk past it every day. #status/committed"
      },
      "why": "\"I really want to keep this.\" is a note-to-self with no reason given, so it is not rationale and is dropped from the Area Note rewrite. It stays in the Brain Dump doc."
    }
  ],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 7: Batch of fourteen bullets to two Idea Notes

Case folder: `lost-detail-07-batch-two-notes`

**Fixture: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point
````

**Fixture: Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- The town is called Harrow Point and it has exactly one road in, which floods at spring tide.
- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days.
- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute.
- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow.
- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?
- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go.
- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him.

%% migrate all the bullets between "- The town is called Harrow Point" to "Could be that the harbourmaster" %%

%% Agent, these go in idea-harrow-point. %%

### 2026-09-30

- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night.
- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock.
- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close.
- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing.
- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding.
- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet.
- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years.

%% migrate all the bullets between "- The storm night" to "I keep coming back" %%

%% Agent, these go in idea-storm-night. %%
````

#### Run 1

**Verdict: FAIL.** The Pass line holds: all fourteen land in the right note, every specific survives, the seven hedged bullets stay hedged, the seven flat ones gain no hedge ("Maybe he left" became "Maybe Tobias left", hedge kept). Fails eval-cases-migrator.md 05.1 item 3 ("No tag means no tag"): all fourteen copies end in `#status/tentative`, for example `- The town is called Harrow Point and it has exactly one road in, which floods at spring tide. #status/tentative`.

Cost: $0.43

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The town is called Harrow Point and it has exactly one road in, which floods at spring tide. #status/tentative
- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days. #status/tentative
- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute. #status/tentative
- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow. #status/tentative
- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name? #status/tentative
- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go. #status/tentative
- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him. #status/tentative
````

**After: Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night

- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night. #status/tentative
- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock. #status/tentative
- Maybe Tobias left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close. #status/tentative
- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing. #status/tentative
- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding. #status/tentative
- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet. #status/tentative
- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years. #status/tentative
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 10, "text": "- The town is called Harrow Point and it has exactly one road in, which floods at spring tide."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The town is called Harrow Point and it has exactly one road in, which floods at spring tide. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The migrate comment covers this bullet and the routing comment sends it to idea-harrow-point. Untagged in the Brain Dump doc, so tentative."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 11, "text": "- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment; routed to idea-harrow-point. Copied in the writer's words with the hedge kept."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 12, "text": "- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment; routed to idea-harrow-point. The writer's doubt stays attached to the idea."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 13, "text": "- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment; routed to idea-harrow-point. Both specifics and the hedge kept."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 14, "text": "- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?"}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name? #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment; routed to idea-harrow-point. Kept whole because the pub-name link depends on the bell sale."
    },
    {
      "id": "u6",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 15, "text": "- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment; routed to idea-harrow-point. Copied in the writer's words."
    },
    {
      "id": "u7",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 16, "text": "- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet in the migrate comment's range; routed to idea-harrow-point."
    },
    {
      "id": "u8",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 24, "text": "- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-storm-night. \"I want\" is not a status signal, so it stays tentative."
    },
    {
      "id": "u9",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 25, "text": "- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment; routed to idea-storm-night. The reason for the skiff stays with it."
    },
    {
      "id": "u10",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 26, "text": "- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Maybe Tobias left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment; routed to idea-storm-night. \"He\" becomes \"Tobias\" so the line reads on its own; times and hedge kept."
    },
    {
      "id": "u11",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 27, "text": "- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment; routed to idea-storm-night."
    },
    {
      "id": "u12",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 28, "text": "- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment; routed to idea-storm-night, where the routing comment sends the whole range, though it names the Drowned Bell."
    },
    {
      "id": "u13",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 29, "text": "- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment; routed to idea-storm-night."
    },
    {
      "id": "u14",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 30, "text": "- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet in the migrate comment's range; routed to idea-storm-night. Enthusiasm is not status, so it stays tentative."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** All fourteen copied word for word, in the right notes, with no tags.

Cost: $0.44

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The town is called Harrow Point and it has exactly one road in, which floods at spring tide.
- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days.
- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute.
- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow.
- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?
- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go.
- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him.
````

**After: Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night

- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night.
- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock.
- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close.
- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing.
- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding.
- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet.
- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 10, "text": "- The town is called Harrow Point and it has exactly one road in, which floods at spring tide."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The town is called Harrow Point and it has exactly one road in, which floods at spring tide."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the range the migrate comment names; the routing comment sends these bullets to idea-harrow-point. Untagged, so it stays tentative, the Idea Note default, and needs no tag."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 11, "text": "- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-harrow-point. Copied verbatim to keep the 'Maybe' hedge and the consequence."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 12, "text": "- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-harrow-point. The writer's rationale 'Not sure if that's too cute' stays with its unit, as Idea Notes keep it."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 13, "text": "- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-harrow-point. Copied verbatim to keep both numbers and the hedge."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 14, "text": "- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?"}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-harrow-point. Placed after the pub line it relates to; kept whole because the name origin depends on the bell sale."
    },
    {
      "id": "u6",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 15, "text": "- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-harrow-point. Copied verbatim with Marrow Bay and the consequence."
    },
    {
      "id": "u7",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 16, "text": "- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet of the commented range, routed to idea-harrow-point. Copied verbatim to keep the 'Could be' hedge."
    },
    {
      "id": "u8",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 24, "text": "- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "First bullet of the range the migrate comment names; the routing comment sends these bullets to idea-storm-night. Untagged, so it stays tentative, the Idea Note default; 'I want' does not set status."
    },
    {
      "id": "u9",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 25, "text": "- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-storm-night. Copied verbatim with its cause."
    },
    {
      "id": "u10",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 26, "text": "- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-storm-night. Placed right after the skiff line, which names Tobias, so 'he' reads correctly; both times and the hedge kept."
    },
    {
      "id": "u11",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 27, "text": "- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-storm-night. Copied verbatim with channel 16."
    },
    {
      "id": "u12",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 28, "text": "- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-storm-night. Copied verbatim to keep the 'Possibly' hedge and the wedding detail."
    },
    {
      "id": "u13",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 29, "text": "- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-storm-night. Copied verbatim; the prose 'nobody can explain yet' stays in the unit, not turned into a Question."
    },
    {
      "id": "u14",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 30, "text": "- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet of the commented range, routed to idea-storm-night. Copied verbatim to keep 'maybe Coyle' and 'six years'."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: FAIL.** Same as r1: the Pass line holds, and all fourteen copies end in `#status/tentative`. Fails eval-cases-migrator.md 05.1 item 3 ("No tag means no tag").

Cost: $0.44

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The town is called Harrow Point and it has exactly one road in, which floods at spring tide. #status/tentative
- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days. #status/tentative
- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute. #status/tentative
- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow. #status/tentative
- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name? #status/tentative
- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go. #status/tentative
- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him. #status/tentative
````

**After: Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night

- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night. #status/tentative
- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock. #status/tentative
- Maybe Tobias left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close. #status/tentative
- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing. #status/tentative
- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding. #status/tentative
- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet. #status/tentative
- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years. #status/tentative
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 10, "text": "- The town is called Harrow Point and it has exactly one road in, which floods at spring tide."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The town is called Harrow Point and it has exactly one road in, which floods at spring tide. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The migrate comment covers this bullet and the routing comment names idea-harrow-point. Untagged, so it stays tentative; words kept verbatim."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 11, "text": "- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-harrow-point. Kept verbatim with its hedge."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 12, "text": "- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-harrow-point. The writer's doubt stays attached to the idea in an Idea Note."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 13, "text": "- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-harrow-point. Kept verbatim, both numbers and the blame on the lamp intact."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 14, "text": "- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?"}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name? #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-harrow-point. Kept as one unit since the pub-name link depends on the bell sale."
    },
    {
      "id": "u6",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 15, "text": "- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-harrow-point. Kept verbatim."
    },
    {
      "id": "u7",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 16, "text": "- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet in the migrate comment's range; routed to idea-harrow-point. Kept verbatim with its hedge."
    },
    {
      "id": "u8",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 24, "text": "- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The migrate comment covers this bullet and the routing comment names idea-storm-night. Untagged, so tentative despite \"I want\"; kept verbatim."
    },
    {
      "id": "u9",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 25, "text": "- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-storm-night. Kept verbatim with its reason."
    },
    {
      "id": "u10",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 26, "text": "- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Maybe Tobias left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-storm-night. \"He\" is named as Tobias so the line reads on its own; times and hedge kept."
    },
    {
      "id": "u11",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 27, "text": "- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-storm-night. Kept verbatim."
    },
    {
      "id": "u12",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 28, "text": "- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-storm-night. Kept verbatim with its hedge."
    },
    {
      "id": "u13",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 29, "text": "- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-storm-night. Kept verbatim; the open mystery stays in the unit's words, not turned into a Question."
    },
    {
      "id": "u14",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 30, "text": "- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years. #status/tentative"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet in the migrate comment's range; routed to idea-storm-night. Kept verbatim with its hedge on Coyle."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 8: Merge by comment

Case folder: `lost-detail-08-merge-by-comment`

**Fixture: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- The lamp turns counterclockwise, which is wrong for this coast.
- Mara's lamp rotates the wrong way round. Every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911.
- It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose.

%% Agent, these three are the same idea said three ways. Merge them into one unit in idea-mara-lighthouse. %%
````

#### Run 1

**Verdict: PASS.** One merged unit with all three sources in the record. Wrong for this coast, Marrow Bay, clockwise, 1911, the grandfather and the mirror-image drawing survive. "possibly on purpose" stays on "on purpose" only. Whale-oil line unchanged. No tag.

Cost: $0.29

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing, possibly on purpose.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, these three are the same idea said three ways. Merge them into one unit in idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The lamp turns counterclockwise, which is wrong for this coast."
        },
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Mara's lamp rotates the wrong way round. Every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911."
        },
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": [
            "- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing, possibly on purpose."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment asks for the three lines to be merged into one unit in idea-mara-lighthouse; it sits under The lamp with the other lamp material. Every specific (counterclockwise, the coast, Marrow Bay, 1911, the grandfather's mirror-image drawing) and the hedge 'possibly on purpose' are kept, and the untagged lines stay tentative, the Idea Note default."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: FAIL.** The Pass line holds, as in r1. Fails eval-cases-migrator.md 05.1 item 3 ("No tag means no tag"). Offending line ends: `...installed it from a mirror-image drawing. Possibly on purpose. #status/tentative`.

Cost: $0.31

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose. #status/tentative
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, these three are the same idea said three ways. Merge them into one unit in idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The lamp turns counterclockwise, which is wrong for this coast."
        },
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Mara's lamp rotates the wrong way round. Every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911."
        },
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": [
            "- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose. #status/tentative"
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment asks for the three lines to be merged into one unit in idea-mara-lighthouse; it sits under The lamp. The merge keeps every specific (counterclockwise, Marrow Bay, 1911, the grandfather's mirror-image drawing) and the hedge 'Possibly on purpose.'"
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same merged line as r1, no tag.

Cost: $0.29

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing, possibly on purpose.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, these three are the same idea said three ways. Merge them into one unit in idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The lamp turns counterclockwise, which is wrong for this coast."
        },
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Mara's lamp rotates the wrong way round. Every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911."
        },
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": [
            "- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing, possibly on purpose."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment asks for the three lines to be merged into one unit in idea-mara-lighthouse; the merged line keeps every specific (counterclockwise, Marrow Bay, 1911, the grandfather's mirror-image drawing) and the hedge \"possibly on purpose\". It sits under the existing lamp heading, untagged because untagged means tentative in an Idea Note."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 9: Confident wording with no tag

Case folder: `over-promotion-09-confident-wording`

**Fixture: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

# Idea - Mara Backstory
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- This is locked: Mara never learned to swim.
- 100% canon, Tobias was the better sailor of the two.
- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her.
- The lighthouse stays in the family, that's decided. #status/provisional
- Mara gets seasick, badly. #status/provisional
    - It happens even on the ferry, on a flat day.
    - [?] Does the town know, or does she hide it?

%% migrate all the bullets between "- This is locked" to "Mara gets seasick" %%

%% Agent, these go in idea-mara-backstory. %%
````

**Fixture: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Bio

## General

- Mara has kept the lighthouse for eleven years.

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
````

#### Run 1

**Verdict: PASS.** All seven lines land in the Idea Note. The three confident lines carry no tag. Both provisional tags carry over; the nested lines stay nested; the `- [?]` line stays a question. char-mara.md unchanged. The record also asks whether the confident lines were meant as committed.

Cost: $0.36

**After: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

# Idea - Mara Backstory

- This is locked: Mara never learned to swim.
- 100% canon, Tobias was the better sailor of the two.
- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her.
- The lighthouse stays in the family, that's decided. #status/provisional
- Mara gets seasick, badly. #status/provisional
    - It happens even on the ferry, on a flat day.
    - [?] Does the town know, or does she hide it?
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\" / Agent, these go in idea-mara-backstory."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- This is locked: Mara never learned to swim."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": ["- This is locked: Mara never learned to swim."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The migrate comment covers this bullet and the routing comment names idea-mara-backstory. It has no tag, and \"This is locked\" is prose, which never sets status, so it stays tentative, copied in the writer's words."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\" / Agent, these go in idea-mara-backstory."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- 100% canon, Tobias was the better sailor of the two."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": ["- 100% canon, Tobias was the better sailor of the two."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "In the comment's range and routed to idea-mara-backstory. Untagged, so tentative despite \"100% canon\"; kept in the writer's words."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\" / Agent, these go in idea-mara-backstory."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": ["- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "In the comment's range and routed to idea-mara-backstory. Untagged, so tentative despite \"Final answer\"; it does not graduate to char-mara."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- The lighthouse stays in the family, that's decided. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": ["- The lighthouse stays in the family, that's decided. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The writer's provisional tag sets status over \"that's decided\"; the routing comment names idea-mara-backstory."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 14,
          "text": "- Mara gets seasick, badly. #status/provisional"
        },
        {
          "note": "brain-dump.md",
          "line": 15,
          "text": "    - It happens even on the ferry, on a flat day."
        },
        {
          "note": "brain-dump.md",
          "line": 16,
          "text": "    - [?] Does the town know, or does she hide it?"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": [
            "- Mara gets seasick, badly. #status/provisional",
            "    - It happens even on the ferry, on a flat day.",
            "    - [?] Does the town know, or does she hide it?"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional and routed to idea-mara-backstory. The nested child inherits the parent's tag, and the writer's Question moves with its unit, nested under it."
    }
  ],
  "left_in_place": [],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- This is locked: Mara never learned to swim."
      },
      "ask": "Lines 10-12 (\"This is locked\", \"100% canon\", \"Final answer\") sound settled but carry no status tag, so they went into idea-mara-backstory as tentative. If you mean any of them as committed, tag it #status/committed and it will graduate to char-mara."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** Same note as r1. The record asks about the confident lines and about "that's decided" on the provisional line.

Cost: $0.36

**After: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

# Idea - Mara Backstory

- This is locked: Mara never learned to swim.
- 100% canon, Tobias was the better sailor of the two.
- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her.
- The lighthouse stays in the family, that's decided. #status/provisional
- Mara gets seasick, badly. #status/provisional
    - It happens even on the ferry, on a flat day.
    - [?] Does the town know, or does she hide it?
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- This is locked: Mara never learned to swim."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": ["- This is locked: Mara never learned to swim."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The migrate comment covers this bullet and the routing comment sends it to idea-mara-backstory. It has no tag, so it stays tentative; 'locked' is prose and does not set status."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- 100% canon, Tobias was the better sailor of the two."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": ["- 100% canon, Tobias was the better sailor of the two."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-mara-backstory. Untagged, so tentative; '100% canon' is prose and does not set status."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": ["- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment and routed to idea-mara-backstory. Untagged, so tentative; 'Final answer' is prose and does not set status."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- The lighthouse stays in the family, that's decided. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": ["- The lighthouse stays in the family, that's decided. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Covered by the migrate comment and routed to idea-mara-backstory. The writer's provisional tag sets the status over the wording 'that's decided'."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 14,
          "text": "- Mara gets seasick, badly. #status/provisional"
        },
        {
          "note": "brain-dump.md",
          "line": 15,
          "text": "    - It happens even on the ferry, on a flat day."
        },
        {
          "note": "brain-dump.md",
          "line": 16,
          "text": "    - [?] Does the town know, or does she hide it?"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": [
            "- Mara gets seasick, badly. #status/provisional",
            "    - It happens even on the ferry, on a flat day.",
            "    - [?] Does the town know, or does she hide it?"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Last bullet in the migrate comment's range, routed to idea-mara-backstory. The nested detail inherits the parent's provisional tag, and the writer's Question moves with its unit."
    }
  ],
  "left_in_place": [],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- This is locked: Mara never learned to swim."
      },
      "ask": "Lines 10-12 say 'This is locked', '100% canon', and 'Final answer' but carry no tag, so they went to idea-mara-backstory as tentative. If you mean them as committed, tag them #status/committed and they will graduate to char-mara."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- The lighthouse stays in the family, that's decided. #status/provisional"
      },
      "ask": "This line says 'that's decided' but is tagged provisional, so it stays provisional in idea-mara-backstory. Change the tag to #status/committed if you want it in char-mara."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same note as r1. No questions.

Cost: $0.37

**After: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

# Idea - Mara Backstory

- This is locked: Mara never learned to swim.
- 100% canon, Tobias was the better sailor of the two.
- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her.
- The lighthouse stays in the family, that's decided. #status/provisional
- Mara gets seasick, badly. #status/provisional
    - It happens even on the ferry, on a flat day.
    - [?] Does the town know, or does she hide it?
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- This is locked: Mara never learned to swim."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": ["- This is locked: Mara never learned to swim."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The routing comment sends it to idea-mara-backstory. \"This is locked\" is wording, not a tag or comment, so it stays tentative by the Brain Dump default and keeps the writer's words; tag it #status/committed to graduate it to char-mara."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- 100% canon, Tobias was the better sailor of the two."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": ["- 100% canon, Tobias was the better sailor of the two."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The routing comment sends it to idea-mara-backstory. \"100% canon\" is wording, not a tag or comment, so it stays tentative by default; tag it #status/committed to graduate it."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": ["- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The routing comment sends it to idea-mara-backstory. \"Final answer\" is wording, not a tag or comment, so it stays tentative by default; tag it #status/committed to graduate it."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- The lighthouse stays in the family, that's decided. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": ["- The lighthouse stays in the family, that's decided. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The routing comment sends it to idea-mara-backstory. The writer's #status/provisional tag sets the status over \"that's decided\", so it goes to the Idea Note, not char-mara."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- This is locked\" to \"Mara gets seasick\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 14,
          "text": "- Mara gets seasick, badly. #status/provisional"
        },
        {
          "note": "brain-dump.md",
          "line": 15,
          "text": "    - It happens even on the ferry, on a flat day."
        },
        {
          "note": "brain-dump.md",
          "line": 16,
          "text": "    - [?] Does the town know, or does she hide it?"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": [
            "- Mara gets seasick, badly. #status/provisional",
            "    - It happens even on the ferry, on a flat day.",
            "    - [?] Does the town know, or does she hide it?"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The routing comment sends it to idea-mara-backstory. The writer's provisional tag sets the parent; the nested ferry line inherits it, and the writer's Question moves with its unit, nested under it."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 10: One committed tag on a bullet with three ideas

Case folder: `over-promotion-10-partial-graduation`

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed
    - [?] Did her father train her, or did she teach herself?

%% Agent, this belongs in char-mara. %%
````

**Fixture: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Bio

## General

- Mara has kept the lighthouse for eleven years.

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
````

#### Run 1

**Verdict: PASS.** Only the first idea graduates, with its `- [?]` nested under it. The second keeper and the hotel chain are in `left_in_place` and in one `questions` entry. Nothing about the hotel chain in the Area Note.

Cost: $0.31

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Bio

## General

- Mara has kept the lighthouse for eleven years.
- Mara is the only keeper the lighthouse has had since her father.
    - [?] Did her father train her, or did she teach herself?

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
        },
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "    - [?] Did her father train her, or did she teach herself?"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": [
            "- Mara is the only keeper the lighthouse has had since her father.",
            "    - [?] Did her father train her, or did she teach herself?"
          ]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The trailing committed tag clearly covers only the first idea, which graduates as a plain statement to char-mara as the comment routes it, under Bio > General beside her keeper history. The writer's [?] Question about her father moves with it, nested under the line, unrewritten."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "why": "\"A second keeper arriving from the mainland could be useful for conflict.\" The trailing committed tag doesn't clearly cover this idea; it reads as a possibility, so it stays tentative at the source and out of the Area Note."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "why": "\"The lighthouse being sold to a hotel chain feels promising.\" The trailing committed tag doesn't clearly cover this idea; it reads as a possibility, so it stays tentative at the source and out of the Area Note."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "ask": "Your #status/committed tag sits at the end of a bullet with three ideas. I graduated only \"Mara is the only keeper the light has had since her father.\" Did you also mean to commit the second keeper from the mainland, or the lighthouse being sold to a hotel chain? If so, tag or comment them separately."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** Same as r1.

Cost: $0.30

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Bio

## General

- Mara has kept the lighthouse for eleven years.
- Mara is the only keeper the lighthouse has had since her father.
    - [?] Did her father train her, or did she teach herself?

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
        },
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "    - [?] Did her father train her, or did she teach herself?"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": [
            "- Mara is the only keeper the lighthouse has had since her father.",
            "    - [?] Did her father train her, or did she teach herself?"
          ]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The trailing committed tag clearly covers only the first idea, Mara being the only keeper since her father; the comment routes it to char-mara, and it is her history, so it goes under Bio > General. The nested Question is about her father and that idea, so it moves with the unit unchanged and sits nested under it as Work."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "why": "\"A second keeper arriving from the mainland could be useful for conflict.\" is a separate possibility the trailing committed tag does not clearly cover, so it stays tentative at the source and out of the Area Note."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "why": "\"The lighthouse being sold to a hotel chain feels promising.\" is a separate possibility the trailing committed tag does not clearly cover, so it stays tentative at the source and out of the Area Note."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "ask": "The trailing #status/committed tag sits on a bullet with three ideas; I graduated only Mara being the only keeper since her father. Did you also mean to commit the second keeper from the mainland, or the lighthouse being sold to a hotel chain? If so, tag or comment them separately."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same as r1, with one question per held-back idea.

Cost: $0.32

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Bio

## General

- Mara has kept the lighthouse for eleven years.
- Mara is the only keeper the light has had since her father.
    - [?] Did her father train her, or did she teach herself?

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
        },
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "    - [?] Did her father train her, or did she teach herself?"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": [
            "- Mara is the only keeper the light has had since her father.",
            "    - [?] Did her father train her, or did she teach herself?"
          ]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The trailing committed tag clearly covers only the plain statement about Mara being the only keeper since her father; the comment routes it to char-mara, and it sits under Bio > General beside her eleven years as keeper. The writer's nested Question belongs to that idea, so it moves with it as Work."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "why": "\"A second keeper arriving from the mainland could be useful for conflict.\" The trailing committed tag does not clearly cover this idea, so it stays out of the Area Note at its source."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "why": "\"The lighthouse being sold to a hotel chain feels promising.\" The trailing committed tag does not clearly cover this idea, so it stays out of the Area Note at its source."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "ask": "Does the committed tag also cover \"A second keeper arriving from the mainland could be useful for conflict\"? I graduated only the line about Mara being the only keeper since her father; if you mean to commit this too, say so and where it goes."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "ask": "Does the committed tag also cover \"The lighthouse being sold to a hotel chain feels promising\"? It reads as a possibility, so I left it at the source; if you mean to commit it, say so and where it goes."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 11: Rejection scoped to one character, with a carve-out

Case folder: `misread-comment-11-scoped-rejection`

**Fixture: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

# Idea - Mara Backstory

## Mara and the sea

- Mara is afraid of the sea.
- She gets seasick even on the ferry.
- Tobias was afraid of the sea too, which is why he took the skiff out, to prove something.
- The whole town has a superstition about saying "drown" out loud.
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

%% Agent, in idea-mara-backstory: Mara being afraid of the sea is out. It makes her too passive. Keep the seasickness, that's physical, not fear. %%
````

#### Run 1

**Verdict: PASS.** Only Mara's fear moves to a new Rejected section, tagged `#status/rejected`, with "It makes her too passive." as the reason. Seasickness and Tobias's fear stay live. The carve-out is not written under Rejected. No other line carries the tag. Left as is: "She gets seasick" now has no name before it, and Tobias's line still says "too".

Cost: $0.31

**After: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

# Idea - Mara Backstory

## Mara and the sea

- She gets seasick even on the ferry.
- Tobias was afraid of the sea too, which is why he took the skiff out, to prove something.
- The whole town has a superstition about saying "drown" out loud.

## Rejected

- Mara is afraid of the sea. It makes her too passive. #status/rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "reject",
      "trigger": {
        "kind": "comment",
        "text": "Agent, in idea-mara-backstory: Mara being afraid of the sea is out. It makes her too passive. Keep the seasickness, that's physical, not fear."
      },
      "sources": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "line": 10,
          "text": "- Mara is afraid of the sea."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": [
            "## Rejected",
            "- Mara is afraid of the sea. It makes her too passive. #status/rejected"
          ]
        }
      ],
      "edits": [],
      "status": "rejected",
      "status_from": "comment",
      "why": "The comment rejects Mara's fear of the sea in idea-mara-backstory and gives the reason 'It makes her too passive', so the line moves to a new Rejected section at the end of the note with that reason. The rejection is scoped to Mara's fear only."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "Ideas/idea-mara-backstory.md",
        "line": 11,
        "text": "- She gets seasick even on the ferry."
      },
      "why": "The comment carves out the seasickness ('Keep the seasickness, that's physical, not fear'), so it stays in the live part of the note, unchanged and tentative."
    },
    {
      "source": {
        "note": "Ideas/idea-mara-backstory.md",
        "line": 12,
        "text": "- Tobias was afraid of the sea too, which is why he took the skiff out, to prove something."
      },
      "why": "The rejection covers Mara being afraid of the sea, not Tobias. Widening it to Tobias's fear would exceed the writer's scope, so the line stays."
    },
    {
      "source": {
        "note": "Ideas/idea-mara-backstory.md",
        "line": 13,
        "text": "- The whole town has a superstition about saying \"drown\" out loud."
      },
      "why": "Not addressed by the comment."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "%% Agent, in idea-mara-backstory: Mara being afraid of the sea is out. It makes her too passive. Keep the seasickness, that's physical, not fear. %%"
      },
      "why": "This is the writer's instruction, not an Idea Unit. It stays in the Brain Dump doc as the record of the rejection."
    }
  ],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** Same as r1, with the reason as a nested line under the rejected line. The record's `left_in_place` entry for Tobias's line notes that "too" now leans on the rejected line.

Cost: $0.30

**After: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

# Idea - Mara Backstory

## Mara and the sea

- She gets seasick even on the ferry.
- Tobias was afraid of the sea too, which is why he took the skiff out, to prove something.
- The whole town has a superstition about saying "drown" out loud.

## Rejected

- Mara is afraid of the sea. #status/rejected
    - It makes her too passive.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "reject",
      "trigger": {
        "kind": "comment",
        "text": "Agent, in idea-mara-backstory: Mara being afraid of the sea is out. It makes her too passive. Keep the seasickness, that's physical, not fear."
      },
      "sources": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "line": 10,
          "text": "- Mara is afraid of the sea."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": [
            "## Rejected",
            "- Mara is afraid of the sea. #status/rejected",
            "    - It makes her too passive."
          ]
        }
      ],
      "edits": [],
      "status": "rejected",
      "status_from": "comment",
      "why": "The writer's comment rejects Mara's fear of the sea in idea-mara-backstory, so the line moves to a new Rejected section at the end of that note with the writer's reason. The carve-out (seasickness) stays in the live part and is not written up in the Rejected section."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "Ideas/idea-mara-backstory.md",
        "line": 11,
        "text": "- She gets seasick even on the ferry."
      },
      "why": "The comment explicitly keeps the seasickness as physical, not fear. It stays in the live part of the note, unchanged and tentative."
    },
    {
      "source": {
        "note": "Ideas/idea-mara-backstory.md",
        "line": 12,
        "text": "- Tobias was afraid of the sea too, which is why he took the skiff out, to prove something."
      },
      "why": "The rejection is scoped to Mara being afraid of the sea. Tobias's fear is a separate proposition, and the Migrator never widens a rejection's scope. Its word \"too\" now leans on the rejected line; the writer may want to reword it."
    }
  ],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same rejection as r1. Two neighbour-line fixes, both in the record's `edits`: "She" became "Mara" on the seasickness line, and "too" was dropped from Tobias's line. eval-cases-migrator.md 08.8 item 3 rules this kind of fix is right, so it does not fail eval-cases-migrator.md 05.1 item 2. The agent added the "She" fix after writing the note, and rewrote the record before making it (spec-migrator.md 05.5 item 3).

Cost: $0.37

**After: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

# Idea - Mara Backstory

## Mara and the sea

- Mara gets seasick even on the ferry.
- Tobias was afraid of the sea, which is why he took the skiff out, to prove something.
- The whole town has a superstition about saying "drown" out loud.

## Rejected

- Mara is afraid of the sea. It makes her too passive. #status/rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "reject",
      "trigger": {
        "kind": "comment",
        "text": "Agent, in idea-mara-backstory: Mara being afraid of the sea is out. It makes her too passive. Keep the seasickness, that's physical, not fear."
      },
      "sources": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "line": 10,
          "text": "- Mara is afraid of the sea."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "under": "# Idea - Mara Backstory",
          "lines": [
            "## Rejected",
            "- Mara is afraid of the sea. It makes her too passive. #status/rejected"
          ]
        }
      ],
      "edits": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "line": 11,
          "before": "- She gets seasick even on the ferry.",
          "after": "- Mara gets seasick even on the ferry."
        },
        {
          "note": "Ideas/idea-mara-backstory.md",
          "line": 12,
          "before": "- Tobias was afraid of the sea too, which is why he took the skiff out, to prove something.",
          "after": "- Tobias was afraid of the sea, which is why he took the skiff out, to prove something."
        }
      ],
      "status": "rejected",
      "status_from": "comment",
      "why": "The comment rejects only Mara's fear of the sea, with the reason 'too passive', so that line moves to a new Rejected section at the end of the Idea Note. The 'too' in the Tobias line pointed back to the rejected fear, so it is dropped, and 'She' in the seasickness line becomes 'Mara' since its antecedent left. Tobias's own fear and the seasickness are not rejected and stay."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "Ideas/idea-mara-backstory.md",
        "line": 11,
        "text": "- She gets seasick even on the ferry."
      },
      "why": "The comment carves the seasickness out of the rejection ('Keep the seasickness, that's physical, not fear'), so it stays in the live part of the note, tentative. Only 'She' became 'Mara' (edit in u1)."
    },
    {
      "source": {
        "note": "Ideas/idea-mara-backstory.md",
        "line": 13,
        "text": "- The whole town has a superstition about saying \"drown\" out loud."
      },
      "why": "Not about Mara's fear of the sea; the comment does not touch it."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "%% Agent, in idea-mara-backstory: Mara being afraid of the sea is out. It makes her too passive. Keep the seasickness, that's physical, not fear. %%"
      },
      "why": "An instruction, not an Idea Unit. It stays in the Brain Dump doc as the record of the rejection."
    }
  ],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 12: Unusual but clear comment

Case folder: `misread-comment-12-unusual-comment`

**Fixture: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- The harbour wall was rebuilt in 1962 with stone from the old church.
- The stone is cursed, obviously.
- Pell's family paid for the rebuild and never let anyone forget it.

%% Agent, migrate the first and third bullets under this date to idea-harrow-point. The third one is provisional. Skip the second, I'm not sure about it. %%
````

#### Run 1

**Verdict: PASS.** First and third bullets land; the third carries `#status/provisional`, the first none. The cursed stone is in `left_in_place`. brain-dump.md unchanged, and no Write or Edit call targeted it.

Cost: $0.29

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The harbour wall was rebuilt in 1962 with stone from the old church.
- Pell's family paid for the rebuild and never let anyone forget it. #status/provisional
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate the first and third bullets under this date to idea-harrow-point. The third one is provisional. Skip the second, I'm not sure about it."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The harbour wall was rebuilt in 1962 with stone from the old church."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- The harbour wall was rebuilt in 1962 with stone from the old church."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names the first bullet and routes it to idea-harrow-point. It sets no status for this bullet, so it keeps the default, tentative, and stays untagged in the Idea Note."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate the first and third bullets under this date to idea-harrow-point. The third one is provisional. Skip the second, I'm not sure about it."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- Pell's family paid for the rebuild and never let anyone forget it."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- Pell's family paid for the rebuild and never let anyone forget it. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "comment",
      "why": "The comment names the third bullet, routes it to idea-harrow-point, and says it is provisional. It sits right after the rebuild line it refers to."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 11,
        "text": "- The stone is cursed, obviously."
      },
      "why": "The writer's comment says to skip the second bullet, so it stays in the Brain Dump doc."
    }
  ],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** Same as r1, with "the rebuild" spelled out as "the 1962 rebuild of the harbour wall". brain-dump.md unchanged, no call targeted it.

Cost: $0.30

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The harbour wall was rebuilt in 1962 with stone from the old church.
- Pell's family paid for the 1962 rebuild of the harbour wall and never let anyone forget it. #status/provisional
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate the first and third bullets under this date to idea-harrow-point. The third one is provisional. Skip the second, I'm not sure about it."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The harbour wall was rebuilt in 1962 with stone from the old church."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- The harbour wall was rebuilt in 1962 with stone from the old church."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names the first bullet and routes it to idea-harrow-point. It sets no status for this bullet, so it keeps the Brain Dump default, tentative, which is also the Idea Note default and needs no tag."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate the first and third bullets under this date to idea-harrow-point. The third one is provisional. Skip the second, I'm not sure about it."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- Pell's family paid for the rebuild and never let anyone forget it."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- Pell's family paid for the 1962 rebuild of the harbour wall and never let anyone forget it. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "comment",
      "why": "The comment routes the third bullet to idea-harrow-point and says it is provisional. \"The rebuild\" is spelled out as the 1962 harbour wall rebuild so the line reads on its own, and it sits right after the wall line."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 11,
        "text": "- The stone is cursed, obviously."
      },
      "why": "The writer's comment says to skip the second bullet because they are not sure about it."
    }
  ],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same as r1. brain-dump.md unchanged, no call targeted it.

Cost: $0.29

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The harbour wall was rebuilt in 1962 with stone from the old church.
- Pell's family paid for the rebuild and never let anyone forget it. #status/provisional
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate the first and third bullets under this date to idea-harrow-point. The third one is provisional. Skip the second, I'm not sure about it."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The harbour wall was rebuilt in 1962 with stone from the old church."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- The harbour wall was rebuilt in 1962 with stone from the old church."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names the first bullet and routes it to idea-harrow-point. The comment sets no status for it, so it keeps the Brain Dump default, tentative, which is also the Idea Note default, so it carries no tag."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate the first and third bullets under this date to idea-harrow-point. The third one is provisional. Skip the second, I'm not sure about it."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- Pell's family paid for the rebuild and never let anyone forget it."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- Pell's family paid for the rebuild and never let anyone forget it. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "comment",
      "why": "The comment names the third bullet, routes it to idea-harrow-point, and says it is provisional, so the copy carries #status/provisional. It sits right after the harbour wall line it builds on."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 11,
        "text": "- The stone is cursed, obviously."
      },
      "why": "The writer's comment says to skip the second bullet because they're not sure about it, so it stays in the Brain Dump doc."
    }
  ],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 13: Ambiguous comment

Case folder: `misread-comment-13-ambiguous-comment`

**Fixture: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- The pub quiz is rigged and has been for years.
- Coyle's dog is older than the ferry.
- There's a second lighthouse on the charts that nobody has ever found.
- The vicar left in 2015 and was never replaced.

%% Agent, move the good ones to idea-harrow-point. %%
````

#### Run 1

**Verdict: PASS.** Nothing migrated. One `questions` entry asks which bullets are "the good ones". All four bullets in `left_in_place`.

Cost: $0.27

No note changed.

**Record: run/unit-records.json**

````json
{
  "units": [],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- The pub quiz is rigged and has been for years."
      },
      "why": "Untagged, and the comment \"move the good ones\" doesn't say which bullets it means, so this line doesn't migrate until the writer says which ones are good (migrator-rules.md 08.7)."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 11,
        "text": "- Coyle's dog is older than the ferry."
      },
      "why": "Untagged, and the comment \"move the good ones\" doesn't say which bullets it means, so this line doesn't migrate until the writer says which ones are good (migrator-rules.md 08.7)."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 12,
        "text": "- There's a second lighthouse on the charts that nobody has ever found."
      },
      "why": "Untagged, and the comment \"move the good ones\" doesn't say which bullets it means, so this line doesn't migrate until the writer says which ones are good (migrator-rules.md 08.7)."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- The vicar left in 2015 and was never replaced."
      },
      "why": "Untagged, and the comment \"move the good ones\" doesn't say which bullets it means, so this line doesn't migrate until the writer says which ones are good (migrator-rules.md 08.7)."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 15,
        "text": "%% Agent, move the good ones to idea-harrow-point. %%"
      },
      "ask": "Which bullets under 2026-10-01 are \"the good ones\"? The comment doesn't name any, so nothing moved to idea-harrow-point. Name the bullets, or tag each one you want moved, and the next run will migrate them."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** Same as r1.

Cost: $0.27

No note changed.

**Record: run/unit-records.json**

````json
{
  "units": [],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- The pub quiz is rigged and has been for years."
      },
      "why": "Untagged. The only comment says \"move the good ones\" without naming which bullets, so nothing moves until the writer says which ones it means (rules 08.7)."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 11,
        "text": "- Coyle's dog is older than the ferry."
      },
      "why": "Untagged. The only comment says \"move the good ones\" without naming which bullets, so nothing moves until the writer says which ones it means (rules 08.7)."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 12,
        "text": "- There's a second lighthouse on the charts that nobody has ever found."
      },
      "why": "Untagged. The only comment says \"move the good ones\" without naming which bullets, so nothing moves until the writer says which ones it means (rules 08.7)."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- The vicar left in 2015 and was never replaced."
      },
      "why": "Untagged. The only comment says \"move the good ones\" without naming which bullets, so nothing moves until the writer says which ones it means (rules 08.7)."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 15,
        "text": "%% Agent, move the good ones to idea-harrow-point. %%"
      },
      "ask": "The comment says to move \"the good ones\" to idea-harrow-point but doesn't name any bullets, and I can't judge which ideas are good. Which of the four 2026-10-01 bullets (pub quiz, Coyle's dog, second lighthouse, vicar) should go?"
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same as r1.

Cost: $0.26

No note changed.

**Record: run/unit-records.json**

````json
{
  "units": [],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- The pub quiz is rigged and has been for years."
      },
      "why": "Untagged. The only comment says to move \"the good ones\" without naming which bullets those are, so this line has no clear trigger (migrator-rules.md 08.7, 10.4)."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 11,
        "text": "- Coyle's dog is older than the ferry."
      },
      "why": "Untagged. The only comment says to move \"the good ones\" without naming which bullets those are, so this line has no clear trigger (migrator-rules.md 08.7, 10.4)."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 12,
        "text": "- There's a second lighthouse on the charts that nobody has ever found."
      },
      "why": "Untagged. The only comment says to move \"the good ones\" without naming which bullets those are, so this line has no clear trigger (migrator-rules.md 08.7, 10.4)."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- The vicar left in 2015 and was never replaced."
      },
      "why": "Untagged. The only comment says to move \"the good ones\" without naming which bullets those are, so this line has no clear trigger (migrator-rules.md 08.7, 10.4)."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 15,
        "text": "%% Agent, move the good ones to idea-harrow-point. %%"
      },
      "ask": "Which of the four 2026-10-01 bullets (pub quiz, Coyle's dog, second lighthouse, vicar) are \"the good ones\"? The comment names a destination but not the bullets, so I moved nothing to idea-harrow-point."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 14: Lines outside the migrate range

Case folder: `unasked-migration-14-outside-range`

**Fixture: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- The harbour has a tide bell that rings itself when the swell is over two metres.
- Nobody in town will say who installed it. Pell claims it predates the lighthouse.
- People set their clocks by it even though it's never on time.
- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too.

%% migrate all the bullets between "- The harbour has a tide bell" to "People set their clocks" %%

%% Agent, these go in idea-harrow-point. %%

### 2026-09-29

- Definitely keeping this: Mara hums the shipping forecast when she's nervous.
- Coyle waters down the whisky and everyone knows. #town
- The lifeboat station closed in 2009.
    - Its slipway is where the kids swim now.
````

**Fixture: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Bio

## General

- Mara has kept the lighthouse for eleven years.

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
````

#### Run 1

**Verdict: PASS.** The three bullets in range land in the Idea Note. The ferry line and every 2026-09-29 line stay; char-mara.md untouched. The record asks about the ferry line and about "Definitely keeping this".

Cost: $0.35

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The harbour has a tide bell that rings itself when the swell is over two metres.
- Nobody in town will say who installed the tide bell. Pell claims it predates the lighthouse.
- People set their clocks by the tide bell even though it's never on time.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The harbour has a tide bell that rings itself when the swell is over two metres."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- The harbour has a tide bell that rings itself when the swell is over two metres."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The range comment names this bullet as the first to migrate, and the routing comment sends it to idea-harrow-point. Untagged in the Brain Dump doc, so it stays tentative."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Nobody in town will say who installed it. Pell claims it predates the lighthouse."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- Nobody in town will say who installed the tide bell. Pell claims it predates the lighthouse."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-harrow-point. \"it\" became \"the tide bell\" so the line reads on its own."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- People set their clocks by it even though it's never on time."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- People set their clocks by the tide bell even though it's never on time."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The last bullet the range comment names, routed to idea-harrow-point. \"it\" became \"the tide bell\" so the line reads on its own."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "why": "Outside the range the comment names, which ends at \"People set their clocks\". It has no status tag, and \"This one should live with the town stuff too\" is prose rather than a comment, so it does not trigger migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 21,
        "text": "- Definitely keeping this: Mara hums the shipping forecast when she's nervous."
      },
      "why": "No status tag and no comment. \"Definitely keeping this\" is prose, which never sets status or triggers migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 22,
        "text": "- Coyle waters down the whisky and everyone knows. #town"
      },
      "why": "#town is not a status tag, and no comment covers this line, so nothing triggers migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 23,
        "text": "- The lifeboat station closed in 2009."
      },
      "why": "No status tag and no comment, so nothing triggers migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 24,
        "text": "    - Its slipway is where the kids swim now."
      },
      "why": "Nested under an untagged parent, with no tag or comment of its own, so nothing triggers migration."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "ask": "This bullet says it should live with the town stuff, but it falls just outside your migrate range, which ends at \"People set their clocks\". Should it go to idea-harrow-point with the tide bell lines? If so, add a tag or widen the comment."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 21,
        "text": "- Definitely keeping this: Mara hums the shipping forecast when she's nervous."
      },
      "ask": "\"Definitely keeping this\" reads like a commitment, but there is no tag or comment, so it stayed tentative and in place. If you want it in char-mara, tag it #status/committed."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: FAIL.** The Pass line holds: nothing outside the range moved. Fails eval-cases-migrator.md 05.1 item 3 ("No tag means no tag"): all three copies end in `#status/tentative`, for example `- The harbour has a tide bell that rings itself when the swell is over two metres. #status/tentative`.

Cost: $0.34

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The harbour has a tide bell that rings itself when the swell is over two metres. #status/tentative
- Nobody in town will say who installed the tide bell. Pell claims it predates the lighthouse. #status/tentative
- People set their clocks by the tide bell even though it's never on time. #status/tentative
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The harbour has a tide bell that rings itself when the swell is over two metres."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- The harbour has a tide bell that rings itself when the swell is over two metres. #status/tentative"]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "First bullet of the range the migrate comment names; the routing comment sends it to idea-harrow-point. Untagged in the Brain Dump doc, so it stays tentative."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Nobody in town will say who installed it. Pell claims it predates the lighthouse."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- Nobody in town will say who installed the tide bell. Pell claims it predates the lighthouse. #status/tentative"]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the named range; routed to idea-harrow-point. \"It\" is replaced with \"the tide bell\" so the line reads on its own."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- People set their clocks by it even though it's never on time."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- People set their clocks by the tide bell even though it's never on time. #status/tentative"]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet of the named range; routed to idea-harrow-point. \"It\" is replaced with \"the tide bell\" so the line reads on its own."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "why": "Outside the range the migrate comment names, which ends at \"People set their clocks\", and it has no status tag. \"This one should live with the town stuff too\" is prose, not a tag or comment, so it does not trigger migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 21,
        "text": "- Definitely keeping this: Mara hums the shipping forecast when she's nervous."
      },
      "why": "No status tag and no comment. \"Definitely keeping this\" is prose and does not set status or trigger migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 22,
        "text": "- Coyle waters down the whisky and everyone knows. #town"
      },
      "why": "#town is not a status tag, and no comment covers the line, so nothing triggers migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 23,
        "text": "- The lifeboat station closed in 2009."
      },
      "why": "No status tag and no comment."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 24,
        "text": "    - Its slipway is where the kids swim now."
      },
      "why": "No status tag on it or its parent, and no comment."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "ask": "This bullet sits just past the end of your migrate range, but its prose says it should live with the town stuff too. Do you want it migrated to idea-harrow-point with the tide bell lines? If so, extend the range or add a comment."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same as r1, but the copies keep "it" word for word instead of "the tide bell".

Cost: $0.36

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The harbour has a tide bell that rings itself when the swell is over two metres.
- Nobody in town will say who installed it. Pell claims it predates the lighthouse.
- People set their clocks by it even though it's never on time.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The harbour has a tide bell that rings itself when the swell is over two metres."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- The harbour has a tide bell that rings itself when the swell is over two metres."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "First bullet of the range the line-15 comment names; the line-17 comment routes it to idea-harrow-point. Untagged in the Brain Dump doc, so it stays tentative, which is also the Idea Note's default, so no tag is needed."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Nobody in town will say who installed it. Pell claims it predates the lighthouse."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- Nobody in town will say who installed it. Pell claims it predates the lighthouse."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range and routed to idea-harrow-point. It sits directly under the tide bell line, so \"it\" still reads clearly."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- People set their clocks by it even though it's never on time."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- People set their clocks by it even though it's never on time."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet of the commented range, routed to idea-harrow-point. It follows the tide bell lines, so \"it\" still reads clearly."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "why": "Outside the range the line-15 comment names, which ends at \"People set their clocks\". \"This one should live with the town stuff too\" is prose inside the bullet, not a comment or tag, so it doesn't trigger migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 21,
        "text": "- Definitely keeping this: Mara hums the shipping forecast when she's nervous."
      },
      "why": "No status tag and no comment. \"Definitely keeping this\" is prose, which never sets status or triggers migration, so it stays tentative at its source and doesn't go to char-mara."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 22,
        "text": "- Coyle waters down the whisky and everyone knows. #town"
      },
      "why": "#town is not a status tag, and no comment covers the line, so nothing triggers migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 23,
        "text": "- The lifeboat station closed in 2009."
      },
      "why": "No status tag and no comment, so nothing triggers migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 24,
        "text": "    - Its slipway is where the kids swim now."
      },
      "why": "Nested under an untagged parent, with no tag or comment of its own, so nothing triggers migration."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "ask": "This bullet says it should live with the town stuff, but it falls just outside the migrate range in your comment, so I left it. Should it go to idea-harrow-point with the tide bell lines? If so, add a tag or a comment."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 21,
        "text": "- Definitely keeping this: Mara hums the shipping forecast when she's nervous."
      },
      "ask": "\"Definitely keeping this\" reads like a commitment, but there's no tag or comment, so I didn't migrate it to char-mara. If you want it committed, add #status/committed or a comment."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 15: Split and merge in one run

Case folder: `unit-record-15-split-and-merge`

**Fixture: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## People

- Coyle runs the Drowned Bell.

## Getting in and out

- The ferry runs twice a week.
````

**Fixture: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
````

**Fixture: Ideas/idea-tobias.md**

````markdown
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- Pell rings the harbour bell by hand at dusk. He learned it from Tobias, who used to do it for pocket money.

%% Agent, migrate this. The bell ringing goes in idea-harrow-point, the part about Tobias in idea-tobias. %%

- The lighthouse cat is called Ballast.
- Mara's cat, Ballast, has one eye and sleeps in the lamp room.

%% Agent, these two are one idea. Merge them into one unit in idea-mara-lighthouse. %%

- The lamp room smells of paraffin and wet wool. #status/provisional

%% Agent, the paraffin line goes in idea-mara-lighthouse too. %%
````

#### Run 1

**Verdict: PASS.** The record shows the split as one source with two copies (idea-harrow-point, idea-tobias) and the merge as two sources with one copy. Every copy written is in the record and every record copy is in the notes (record-check lines 2 and 4).

Cost: $0.37

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## People

- Coyle runs the Drowned Bell.
- Pell rings the harbour bell by hand at dusk.

## Getting in and out

- The ferry runs twice a week.
````

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp room smells of paraffin and wet wool. #status/provisional

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.

## Ballast

- The lighthouse cat is Mara's cat, Ballast, who has one eye and sleeps in the lamp room.
````

**After: Ideas/idea-tobias.md**

````markdown
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias used to ring the harbour bell by hand for pocket money. Pell learned it from him.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this. The bell ringing goes in idea-harrow-point, the part about Tobias in idea-tobias."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Pell rings the harbour bell by hand at dusk. He learned it from Tobias, who used to do it for pocket money."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## People",
          "lines": ["- Pell rings the harbour bell by hand at dusk."]
        },
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Tobias used to ring the harbour bell by hand for pocket money. Pell learned it from him."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names both notes. Pell's bell ringing sits with the town's other people; the Tobias copy names the bell and Pell so it reads on its own."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, these two are one idea. Merge them into one unit in idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 14,
          "text": "- The lighthouse cat is called Ballast."
        },
        {
          "note": "brain-dump.md",
          "line": 15,
          "text": "- Mara's cat, Ballast, has one eye and sleeps in the lamp room."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "## Ballast",
            "- The lighthouse cat is Mara's cat, Ballast, who has one eye and sleeps in the lamp room."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment asks for one merged unit in idea-mara-lighthouse. No existing heading fits the cat, so it gets its own heading at the end of the note."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, the paraffin line goes in idea-mara-lighthouse too."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 19,
          "text": "- The lamp room smells of paraffin and wet wool. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": ["- The lamp room smells of paraffin and wet wool. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The comment routes it to idea-mara-lighthouse, and it is about the lamp room, so it goes under The lamp. The writer's provisional tag carries over."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** Same record shape as r1.

Cost: $0.35

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## People

- Coyle runs the Drowned Bell.
- Pell rings the harbour bell by hand at dusk.

## Getting in and out

- The ferry runs twice a week.
````

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp room smells of paraffin and wet wool. #status/provisional

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.

## Ballast

- Ballast, Mara's cat, is the lighthouse cat. Ballast has one eye and sleeps in the lamp room.
````

**After: Ideas/idea-tobias.md**

````markdown
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias used to ring the harbour bell by hand at dusk for pocket money. Pell learned it from him.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this. The bell ringing goes in idea-harrow-point, the part about Tobias in idea-tobias."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Pell rings the harbour bell by hand at dusk. He learned it from Tobias, who used to do it for pocket money."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## People",
          "lines": ["- Pell rings the harbour bell by hand at dusk."]
        },
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Tobias used to ring the harbour bell by hand at dusk for pocket money. Pell learned it from him."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names both notes. The bell ringing is Pell's, so it sits under People in idea-harrow-point; the Tobias line names the bell and Pell so it reads on its own."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, these two are one idea. Merge them into one unit in idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 14,
          "text": "- The lighthouse cat is called Ballast."
        },
        {
          "note": "brain-dump.md",
          "line": 15,
          "text": "- Mara's cat, Ballast, has one eye and sleeps in the lamp room."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "## Ballast",
            "- Ballast, Mara's cat, is the lighthouse cat. Ballast has one eye and sleeps in the lamp room."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment asks for one merged unit in idea-mara-lighthouse. No existing heading fits the cat, so a new Ballast heading goes at the end of the note."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 19,
          "text": "- The lamp room smells of paraffin and wet wool. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": ["- The lamp room smells of paraffin and wet wool. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The provisional tag triggers migration and the comment routes it to idea-mara-lighthouse. It describes the lamp room, so it goes under The lamp."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same record shape as r1.

Cost: $0.37

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## People

- Coyle runs the Drowned Bell.
- Pell rings the harbour bell by hand at dusk.

## Getting in and out

- The ferry runs twice a week.
````

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp room smells of paraffin and wet wool. #status/provisional

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.

## Ballast

- The lighthouse cat is Mara's cat, Ballast. Ballast has one eye and sleeps in the lamp room.
````

**After: Ideas/idea-tobias.md**

````markdown
---
title: Idea - Tobias
type: [idea-note]
---

# Idea - Tobias

- Tobias used to ring the harbour bell by hand at dusk for pocket money. Pell learned it from him.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this. The bell ringing goes in idea-harrow-point, the part about Tobias in idea-tobias."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Pell rings the harbour bell by hand at dusk. He learned it from Tobias, who used to do it for pocket money."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## People",
          "lines": ["- Pell rings the harbour bell by hand at dusk."]
        },
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": ["- Tobias used to ring the harbour bell by hand at dusk for pocket money. Pell learned it from him."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment splits the bullet and names both notes. The bell ringing sits with Harrow Point's people; the Tobias copy names the bell and Pell so it reads on its own."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, these two are one idea. Merge them into one unit in idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 14,
          "text": "- The lighthouse cat is called Ballast."
        },
        {
          "note": "brain-dump.md",
          "line": 15,
          "text": "- Mara's cat, Ballast, has one eye and sleeps in the lamp room."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "## Ballast",
            "- The lighthouse cat is Mara's cat, Ballast. Ballast has one eye and sleeps in the lamp room."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment says the two lines are one idea and names the note. The note had no heading for the cat, so the merged unit gets its own."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, the paraffin line goes in idea-mara-lighthouse too."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 19,
          "text": "- The lamp room smells of paraffin and wet wool. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": ["- The lamp room smells of paraffin and wet wool. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The comment names the note and the writer's tag makes it provisional, so the copy keeps the tag. It is about the lamp room, so it goes under The lamp."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 16: Provisional child under a committed parent

Case folder: `tentative-in-area-note-16-tagged-child`

**Fixture: Ideas/idea-mara-habits.md**

````markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- Mara keeps a logbook of every ship that passes. #status/committed
    - She writes it in pencil, never ink.
    - She has started leaving gaps in it on purpose. #status/provisional

%% Agent, the committed material belongs in char-mara. The provisional line goes in idea-mara-habits. %%
````

**Fixture: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Bio

## General

- Mara has kept the lighthouse for eleven years.

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
````

#### Run 1

**Verdict: PASS.** Logbook and pencil lines in char-mara.md with no tag. The gaps line is not in the Area Note; it is in idea-mara-habits with `#status/provisional`.

Cost: $0.31

**After: Ideas/idea-mara-habits.md**

````markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits

- Mara has started leaving gaps in her ship logbook on purpose. #status/provisional
````

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Bio

## General

- Mara has kept the lighthouse for eleven years.
- Mara keeps a logbook of every ship that passes.
- Mara writes her ship logbook in pencil, never ink.

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara keeps a logbook of every ship that passes. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara keeps a logbook of every ship that passes."]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The writer's tag commits the line and the comment routes the committed material to char-mara. It is a fact about Mara's life, so it sits under Bio > General, with no status tag because char-mara is an Area Note."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "    - She writes it in pencil, never ink."
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara writes her ship logbook in pencil, never ink."]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "parent tag",
      "why": "The untagged child inherits #status/committed from its parent bullet, and the comment sends the committed material to char-mara. Rewritten to name Mara and the logbook so it reads on its own."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "    - She has started leaving gaps in it on purpose. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-habits.md",
          "under": "# Idea - Mara Habits",
          "lines": ["- Mara has started leaving gaps in her ship logbook on purpose. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The child's own provisional tag overrides the committed parent, so it stays out of the Area Note. The comment routes the provisional line to idea-mara-habits; reworded only to name Mara and the logbook."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** Same as r1.

Cost: $0.33

**After: Ideas/idea-mara-habits.md**

````markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits

- Mara has started leaving gaps on purpose in her logbook of every ship that passes. #status/provisional
````

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Bio

## General

- Mara has kept the lighthouse for eleven years.
- Mara keeps a logbook of every ship that passes.
- Mara writes her logbook in pencil, never ink.

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara keeps a logbook of every ship that passes. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara keeps a logbook of every ship that passes."]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The writer's tag commits the line, and the comment routes the committed material to char-mara. It is a habit of her daily life, so it goes under Bio > General, with no status tag because it is an Area Note."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "    - She writes it in pencil, never ink."
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara writes her logbook in pencil, never ink."]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "parent tag",
      "why": "The untagged child inherits its parent's committed tag, and the comment routes committed material to char-mara. It is rewritten to name Mara and the logbook so it reads on its own, directly after the logbook line."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "    - She has started leaving gaps in it on purpose. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-habits.md",
          "under": "# Idea - Mara Habits",
          "lines": ["- Mara has started leaving gaps on purpose in her logbook of every ship that passes. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The child's own provisional tag outranks its committed parent, so it stays out of the Area Note; the comment routes it to idea-mara-habits. It names Mara and the logbook so it reads without its parent."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 14,
        "text": "%% Agent, the committed material belongs in char-mara. The provisional line goes in idea-mara-habits. %%"
      },
      "why": "A routing comment, not story material. It was followed for u1, u2, and u3."
    }
  ],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same as r1.

Cost: $0.32

**After: Ideas/idea-mara-habits.md**

````markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

# Idea - Mara Habits

- Mara has started leaving gaps in her logbook of passing ships on purpose. #status/provisional
````

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

# Overview

## Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

# Arc/Development

# Bio

## General

- Mara has kept the lighthouse for eleven years.
- Mara keeps a logbook of every ship that passes.
- Mara writes her logbook in pencil, never ink.

# Psychology

## Values, Beliefs, etc.

# Rationale

# Rejected
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/committed"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara keeps a logbook of every ship that passes. #status/committed"
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara keeps a logbook of every ship that passes."]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The writer's tag commits the line and the comment routes committed material to char-mara. It is a fact about Mara's life, so it goes under Bio > General, without a status tag as an Area Note requires."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, the committed material belongs in char-mara. The provisional line goes in idea-mara-habits."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "    - She writes it in pencil, never ink."
        }
      ],
      "copies": [
        {
          "note": "char-mara.md",
          "under": "## General",
          "lines": ["- Mara writes her logbook in pencil, never ink."]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "parent tag",
      "why": "The untagged child is nested under the committed parent, so it inherits committed, and the comment routes committed material to char-mara. Rewritten to name Mara and the logbook so it reads on its own."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "    - She has started leaving gaps in it on purpose. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-habits.md",
          "under": "# Idea - Mara Habits",
          "lines": ["- Mara has started leaving gaps in her logbook of passing ships on purpose. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The writer's own provisional tag outranks the committed parent, so it stays out of the Area Note; the comment routes it to idea-mara-habits. Reworded only to name Mara and the logbook so it reads on its own."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 17: Six tagged bullets among eighteen

Case folder: `missed-unit-17-scattered-tags`

**Fixture: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

%% Agent, anything I tag provisional under these three dates goes in idea-harrow-point. Leave the untagged lines where they are. %%

### 2026-10-01

- The bakery only opens when the baker's knee allows it.
- The post office doubles as the undertaker's. #status/provisional
- There are more boats than people in winter.
- Somebody repaints the war memorial every spring and nobody knows who.
- The chemist, Ferris, fills prescriptions from memory. #status/provisional
- Fog comes in from the east, which is the wrong direction.

### 2026-09-30

- Half the houses on Quay Street are let to a film company that never came.
- The primary school has nine pupils, all cousins. #status/provisional
- The church clock runs four minutes fast on purpose.
- Gulls have learned to open the bins outside the Drowned Bell.
- A seal called Mister Hale comes into the harbour every October. #status/provisional
- The bus shelter has had the same timetable since 1998.

### 2026-09-28

- The council sold the fish market roof for scrap in 2011. #status/provisional
- There's a rumour the vicar's wife ran the smuggling.
- Nobody locks their doors except Pell.
- The cliff path lost twelve metres to the sea last winter. #status/provisional
- Everyone's grandmother claims to have been the May Queen.
- The phone box is listed, so they can't remove it.
````

#### Run 1

**Verdict: PASS.** All six tagged bullets land with their tags; all twelve untagged bullets are in `left_in_place`. The note was written with one Write call rather than Edit; the diff shows additions only.

Cost: $0.35

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The post office doubles as the undertaker's. #status/provisional
- The chemist, Ferris, fills prescriptions from memory. #status/provisional
- The primary school has nine pupils, all cousins. #status/provisional
- A seal called Mister Hale comes into the harbour every October. #status/provisional
- The council sold the fish market roof for scrap in 2011. #status/provisional
- The cliff path lost twelve metres to the sea last winter. #status/provisional
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 13, "text": "- The post office doubles as the undertaker's. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The post office doubles as the undertaker's. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-10-01; the comment on line 8 routes provisional lines under these dates to idea-harrow-point."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 16, "text": "- The chemist, Ferris, fills prescriptions from memory. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The chemist, Ferris, fills prescriptions from memory. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-10-01; the comment on line 8 routes provisional lines under these dates to idea-harrow-point."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 22, "text": "- The primary school has nine pupils, all cousins. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The primary school has nine pupils, all cousins. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-30; the comment on line 8 routes provisional lines under these dates to idea-harrow-point."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 25, "text": "- A seal called Mister Hale comes into the harbour every October. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- A seal called Mister Hale comes into the harbour every October. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-30; the comment on line 8 routes provisional lines under these dates to idea-harrow-point."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 30, "text": "- The council sold the fish market roof for scrap in 2011. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The council sold the fish market roof for scrap in 2011. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-28; the comment on line 8 routes provisional lines under these dates to idea-harrow-point."
    },
    {
      "id": "u6",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 33, "text": "- The cliff path lost twelve metres to the sea last winter. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The cliff path lost twelve metres to the sea last winter. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-28; the comment on line 8 routes provisional lines under these dates to idea-harrow-point."
    }
  ],
  "left_in_place": [
    {"source": {"note": "brain-dump.md", "line": 12, "text": "- The bakery only opens when the baker's knee allows it."}, "why": "Untagged; the comment on line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 14, "text": "- There are more boats than people in winter."}, "why": "Untagged; the comment on line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 15, "text": "- Somebody repaints the war memorial every spring and nobody knows who."}, "why": "Untagged; the comment on line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 17, "text": "- Fog comes in from the east, which is the wrong direction."}, "why": "Untagged; the comment on line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 21, "text": "- Half the houses on Quay Street are let to a film company that never came."}, "why": "Untagged; the comment on line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 23, "text": "- The church clock runs four minutes fast on purpose."}, "why": "Untagged; the comment on line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 24, "text": "- Gulls have learned to open the bins outside the Drowned Bell."}, "why": "Untagged; the comment on line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 26, "text": "- The bus shelter has had the same timetable since 1998."}, "why": "Untagged; the comment on line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 31, "text": "- There's a rumour the vicar's wife ran the smuggling."}, "why": "Untagged; the comment on line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 32, "text": "- Nobody locks their doors except Pell."}, "why": "Untagged; the comment on line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 34, "text": "- Everyone's grandmother claims to have been the May Queen."}, "why": "Untagged; the comment on line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 35, "text": "- The phone box is listed, so they can't remove it."}, "why": "Untagged; the comment on line 8 says to leave untagged lines where they are."}
  ],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** Same as r1.

Cost: $0.35

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The post office doubles as the undertaker's. #status/provisional
- The chemist, Ferris, fills prescriptions from memory. #status/provisional
- The primary school has nine pupils, all cousins. #status/provisional
- A seal called Mister Hale comes into the harbour every October. #status/provisional
- The council sold the fish market roof for scrap in 2011. #status/provisional
- The cliff path lost twelve metres to the sea last winter. #status/provisional
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 13, "text": "- The post office doubles as the undertaker's. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The post office doubles as the undertaker's. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-10-01; the comment on line 8 routes every provisional line under these three dates to idea-harrow-point."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 16, "text": "- The chemist, Ferris, fills prescriptions from memory. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The chemist, Ferris, fills prescriptions from memory. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-10-01; the comment on line 8 routes it to idea-harrow-point."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 22, "text": "- The primary school has nine pupils, all cousins. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The primary school has nine pupils, all cousins. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-30; the comment on line 8 routes it to idea-harrow-point."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 25, "text": "- A seal called Mister Hale comes into the harbour every October. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- A seal called Mister Hale comes into the harbour every October. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-30; the comment on line 8 routes it to idea-harrow-point."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 30, "text": "- The council sold the fish market roof for scrap in 2011. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The council sold the fish market roof for scrap in 2011. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-28; the comment on line 8 routes it to idea-harrow-point."
    },
    {
      "id": "u6",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 33, "text": "- The cliff path lost twelve metres to the sea last winter. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The cliff path lost twelve metres to the sea last winter. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-28; the comment on line 8 routes it to idea-harrow-point."
    }
  ],
  "left_in_place": [
    {"source": {"note": "brain-dump.md", "line": 12, "text": "- The bakery only opens when the baker's knee allows it."}, "why": "Untagged; the comment says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 14, "text": "- There are more boats than people in winter."}, "why": "Untagged; the comment says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 15, "text": "- Somebody repaints the war memorial every spring and nobody knows who."}, "why": "Untagged; the comment says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 17, "text": "- Fog comes in from the east, which is the wrong direction."}, "why": "Untagged; the comment says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 21, "text": "- Half the houses on Quay Street are let to a film company that never came."}, "why": "Untagged; the comment says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 23, "text": "- The church clock runs four minutes fast on purpose."}, "why": "Untagged; the comment says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 24, "text": "- Gulls have learned to open the bins outside the Drowned Bell."}, "why": "Untagged; the comment says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 26, "text": "- The bus shelter has had the same timetable since 1998."}, "why": "Untagged; the comment says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 31, "text": "- There's a rumour the vicar's wife ran the smuggling."}, "why": "Untagged; the comment says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 32, "text": "- Nobody locks their doors except Pell."}, "why": "Untagged; the comment says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 34, "text": "- Everyone's grandmother claims to have been the May Queen."}, "why": "Untagged; the comment says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 35, "text": "- The phone box is listed, so they can't remove it."}, "why": "Untagged; the comment says to leave untagged lines where they are."}
  ],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same as r1.

Cost: $0.35

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The post office doubles as the undertaker's. #status/provisional
- The chemist, Ferris, fills prescriptions from memory. #status/provisional
- The primary school has nine pupils, all cousins. #status/provisional
- A seal called Mister Hale comes into the harbour every October. #status/provisional
- The council sold the fish market roof for scrap in 2011. #status/provisional
- The cliff path lost twelve metres to the sea last winter. #status/provisional
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 13, "text": "- The post office doubles as the undertaker's. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The post office doubles as the undertaker's. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-10-01; the comment at line 8 routes provisional lines under these dates to idea-harrow-point."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 16, "text": "- The chemist, Ferris, fills prescriptions from memory. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The chemist, Ferris, fills prescriptions from memory. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-10-01; the comment at line 8 routes provisional lines under these dates to idea-harrow-point."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 22, "text": "- The primary school has nine pupils, all cousins. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The primary school has nine pupils, all cousins. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-30; the comment at line 8 routes provisional lines under these dates to idea-harrow-point."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 25, "text": "- A seal called Mister Hale comes into the harbour every October. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- A seal called Mister Hale comes into the harbour every October. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-30; the comment at line 8 routes provisional lines under these dates to idea-harrow-point."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 30, "text": "- The council sold the fish market roof for scrap in 2011. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The council sold the fish market roof for scrap in 2011. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-28; the comment at line 8 routes provisional lines under these dates to idea-harrow-point."
    },
    {
      "id": "u6",
      "action": "migrate",
      "trigger": {"kind": "tag", "text": "#status/provisional"},
      "sources": [
        {"note": "brain-dump.md", "line": 33, "text": "- The cliff path lost twelve metres to the sea last winter. #status/provisional"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The cliff path lost twelve metres to the sea last winter. #status/provisional"]}
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-28; the comment at line 8 routes provisional lines under these dates to idea-harrow-point."
    }
  ],
  "left_in_place": [
    {"source": {"note": "brain-dump.md", "line": 12, "text": "- The bakery only opens when the baker's knee allows it."}, "why": "Untagged, and the comment at line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 14, "text": "- There are more boats than people in winter."}, "why": "Untagged, and the comment at line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 15, "text": "- Somebody repaints the war memorial every spring and nobody knows who."}, "why": "Untagged, and the comment at line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 17, "text": "- Fog comes in from the east, which is the wrong direction."}, "why": "Untagged, and the comment at line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 21, "text": "- Half the houses on Quay Street are let to a film company that never came."}, "why": "Untagged, and the comment at line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 23, "text": "- The church clock runs four minutes fast on purpose."}, "why": "Untagged, and the comment at line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 24, "text": "- Gulls have learned to open the bins outside the Drowned Bell."}, "why": "Untagged, and the comment at line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 26, "text": "- The bus shelter has had the same timetable since 1998."}, "why": "Untagged, and the comment at line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 31, "text": "- There's a rumour the vicar's wife ran the smuggling."}, "why": "Untagged, and the comment at line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 32, "text": "- Nobody locks their doors except Pell."}, "why": "Untagged, and the comment at line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 34, "text": "- Everyone's grandmother claims to have been the May Queen."}, "why": "Untagged, and the comment at line 8 says to leave untagged lines where they are."},
    {"source": {"note": "brain-dump.md", "line": 35, "text": "- The phone box is listed, so they can't remove it."}, "why": "Untagged, and the comment at line 8 says to leave untagged lines where they are."}
  ],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 18: Typos and a contradiction in existing lines

Case folder: `unasked-edit-18-typos-and-contradiction`

**Fixture: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## The harbour office

- The harbor masters office has no windows facing the see.
- Pell keeps the tide tables locked up.
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- Pell dosnt lock the tide tables anymore, he lost the key in 2019.

%% Agent, migrate this to idea-harrow-point. %%
````

#### Run 1

**Verdict: PASS.** Both existing lines unchanged to the character, typos included. The new unit is added; it keeps "dosnt".

Cost: $0.28

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## The harbour office

- The harbor masters office has no windows facing the see.
- Pell keeps the tide tables locked up.
- Pell dosnt lock the tide tables anymore, he lost the key in 2019.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Pell dosnt lock the tide tables anymore, he lost the key in 2019."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## The harbour office",
          "lines": ["- Pell dosnt lock the tide tables anymore, he lost the key in 2019."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names idea-harrow-point. It sits under The harbour office, next to the other Pell tide-tables line, as an alternative under exploration; the writer's words are kept as typed and no neighbouring line is changed."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: FAIL.** The Pass line holds, as in r1. Fails eval-cases-migrator.md 05.1 item 3 ("No tag means no tag"). Offending line: `- Pell dosnt lock the tide tables anymore, he lost the key in 2019. #status/tentative`.

Cost: $0.28

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## The harbour office

- The harbor masters office has no windows facing the see.
- Pell keeps the tide tables locked up.
- Pell dosnt lock the tide tables anymore, he lost the key in 2019. #status/tentative
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Pell dosnt lock the tide tables anymore, he lost the key in 2019."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## The harbour office",
          "lines": ["- Pell dosnt lock the tide tables anymore, he lost the key in 2019. #status/tentative"]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes the line to idea-harrow-point. It sits under The harbour office, next to the other line about Pell and the tide tables, in the writer's words; untagged in the Brain Dump doc, so tentative."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same as r1.

Cost: $0.29

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## The harbour office

- The harbor masters office has no windows facing the see.
- Pell keeps the tide tables locked up.
- Pell dosnt lock the tide tables anymore, he lost the key in 2019.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Pell dosnt lock the tide tables anymore, he lost the key in 2019."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## The harbour office",
          "lines": ["- Pell dosnt lock the tide tables anymore, he lost the key in 2019."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names idea-harrow-point, and the line is about Pell and the tide tables, so it goes under The harbour office next to the other tide-tables line. Copied in the writer's words; no comment asked for spelling fixes or changes to neighbouring lines, and contradictions are not the Migrator's to flag."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

### Case 19: Tags with no destination named

Case folder: `wrong-destination-19-no-destination-named`

**Fixture: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## People

- Coyle runs the Drowned Bell.

## Getting in and out

- The ferry runs twice a week.
````

**Fixture: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
````

**Fixture: Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night

## The lamp failure

- The lamp failed for eleven minutes.
````

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

# Brain Dump

### 2026-10-01

- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional
- On the storm night the foghorn was already broken. #status/provisional
- The lamp's lens was cracked by a gull in 2003. #status/provisional
- Coyle closed the pub early that night, which he never does. #status/provisional
````

#### Run 1

**Verdict: PASS.** Ferry captain in the town note, foghorn in the storm-night note, lens under "The lamp" in the lighthouse note, Coyle in the storm-night note (the ruling in eval-cases-migrator.md 09.5). The Coyle copy keeps "that night" word for word.

Cost: $0.36

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## People

- Coyle runs the Drowned Bell.

## Getting in and out

- The ferry runs twice a week.
- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional
````

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp's lens was cracked by a gull in 2003. #status/provisional

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
````

**After: Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night

## The lamp failure

- The lamp failed for eleven minutes.

## The foghorn

- On the storm night the foghorn was already broken. #status/provisional

## Coyle and the pub

- Coyle closed the pub early that night, which he never does. #status/provisional
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## Getting in and out",
          "lines": ["- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. The ferry captain belongs with the ferry schedule under Getting in and out in the Harrow Point Idea Note."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- On the storm night the foghorn was already broken. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "## The foghorn",
            "- On the storm night the foghorn was already broken. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. The line is about the storm night, so it goes in the Storm Night Idea Note under a new foghorn heading, because the foghorn is not the lamp."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- The lamp's lens was cracked by a gull in 2003. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": ["- The lamp's lens was cracked by a gull in 2003. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. The crack is part of the lamp's history, not the storm night, so it goes under The lamp in the Mara Lighthouse Idea Note."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- Coyle closed the pub early that night, which he never does. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "## Coyle and the pub",
            "- Coyle closed the pub early that night, which he never does. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. In this entry \"that night\" reads as the storm night, so the line goes in the Storm Night Idea Note in the writer's words, not under Coyle in Harrow Point."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 2

**Verdict: PASS.** Same placements as r1; the Coyle copy says "on the storm night".

Cost: $0.36

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## People

- Coyle runs the Drowned Bell.

## Getting in and out

- The ferry runs twice a week.
- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional
````

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp's lens was cracked by a gull in 2003. #status/provisional

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
````

**After: Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night

## The lamp failure

- The lamp failed for eleven minutes.

## The foghorn

- On the storm night the foghorn was already broken. #status/provisional

## The pub

- Coyle closed the pub early on the storm night, which he never does. #status/provisional
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": { "kind": "tag", "text": "#status/provisional" },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## Getting in and out",
          "lines": ["- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. The line is about the ferry, so it sits next to the ferry schedule under Getting in and out in the Harrow Point Idea Note."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": { "kind": "tag", "text": "#status/provisional" },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- On the storm night the foghorn was already broken. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "## The foghorn",
            "- On the storm night the foghorn was already broken. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. It is about the storm night, so it goes in the Storm Night Idea Note, under a new foghorn heading because the existing heading covers only the lamp failure."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": { "kind": "tag", "text": "#status/provisional" },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- The lamp's lens was cracked by a gull in 2003. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": ["- The lamp's lens was cracked by a gull in 2003. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. It is history about the lighthouse lamp itself (2003), not about the storm night, so it goes under The lamp in the Mara Lighthouse Idea Note."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": { "kind": "tag", "text": "#status/provisional" },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- Coyle closed the pub early that night, which he never does. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "## The pub",
            "- Coyle closed the pub early on the storm night, which he never does. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. \"That night\" follows the storm-night line in the same entry, so the unit is an event of the storm night and goes in the Storm Night Idea Note, not with Coyle's standing description in Harrow Point. \"That night\" is spelled out as \"the storm night\" so the line reads on its own."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Run 3

**Verdict: PASS.** Same as r2.

Cost: $0.35

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## People

- Coyle runs the Drowned Bell.

## Getting in and out

- The ferry runs twice a week.
- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional
````

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp's lens was cracked by a gull in 2003. #status/provisional

## The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
````

**After: Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night

## The lamp failure

- The lamp failed for eleven minutes.

## The foghorn

- On the storm night the foghorn was already broken. #status/provisional

## Coyle's pub

- Coyle closed the pub early on the storm night, which he never does. #status/provisional
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## Getting in and out",
          "lines": ["- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. The line is about the ferry, which idea-harrow-point already covers under Getting in and out."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- On the storm night the foghorn was already broken. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "## The foghorn",
            "- On the storm night the foghorn was already broken. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. The line is about what failed on the storm night, so it goes to idea-storm-night under a new foghorn heading, since the existing heading covers only the lamp."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- The lamp's lens was cracked by a gull in 2003. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": ["- The lamp's lens was cracked by a gull in 2003. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. The line is lighthouse history about the lamp, not about the storm night, so it goes under The lamp in idea-mara-lighthouse."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- Coyle closed the pub early that night, which he never does. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "## Coyle's pub",
            "- Coyle closed the pub early on the storm night, which he never does. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. 'That night' follows the storm-night line in the same entry, so the line goes to idea-storm-night, reworded to name the storm night so it reads on its own."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

## Re-run after the 03.7 fix: cases 1, 4, 7, 8, 14, 18

Nine of the first run's eleven fails came from one cause: a `#status/tentative` tag on a copy whose source had no status tag (Findings item 1 above). This re-run checks the fix to the rules file against the six cases those nine fails came from. It was run and graded the same way as the first run: by hand with `_tools/migrator-run.py`, record checks by `_tools/record-check.py`, Pass lines judged by a Claude Opus 5.5 worker session reading every output. The LLM graders were not run.

### What Was Run

- **Date:** 2026-10-04, 18:07 to 18:09 EDT.
- **Agent:** `script-asst:migrator` (`agents/migrator.md`, unchanged since 16:51), model `claude-opus-5-5`. Every run's stream reports `claude-opus-5-5`.
- **Claude Code:** 2.1.289.
- **Runs:** 18. Six cases, three runs each, at most five at a time, in one call.
- **Rules given:** `_fixtures/rules/migrator-rules.md` alone, saved at 18:06:31. It is byte-identical to the plugin's `references/migrator-rules.md` (checked with `cmp` before grading).
- **What changed in the rules file since the first run:** migrator-rules.md 03.7 now says a migrated copy carries the status tag the writer gave its source, or the one the writer's comment asks for, and the Migrator never chooses a tag. A source with no tag gets a copy with no tag, and the Migrator never writes `#status/tentative`. The source-citation lines were also removed, and every "Moe:" became "The writer:". The 03.7 wording was read in the file, and the file no longer contains "Moe"; the other two changes were not diffed, because no copy of the old file was kept beside it.
- **Command:**

```bash
OUT=$(mktemp -d)   # /var/folders/jp/t3th_wsd03xgpgdnsn9ys63w0000gn/T/tmp.0GiGjzyv6f
python3 _tools/migrator-run.py --out "$OUT" --runs 3 --cases lost-detail-01-plain-copy lost-detail-04-existing-text lost-detail-07-batch-two-notes lost-detail-08-merge-by-comment unasked-migration-14-outside-range unasked-edit-18-typos-and-contradiction
```

- **Errors and timeouts:** none. Every run exited 0 with an empty stderr. No run was repeated.
- **Prompt:** the same as the first run.

### Summary Table

| Case | First run, passed | Re-run, passed |
| --- | --- | --- |
| lost-detail-01-plain-copy | 1 of 3 | 3 of 3 |
| lost-detail-04-existing-text | 1 of 3 | 3 of 3 |
| lost-detail-07-batch-two-notes | 1 of 3 | 3 of 3 |
| lost-detail-08-merge-by-comment | 2 of 3 | 3 of 3 |
| unasked-migration-14-outside-range | 2 of 3 | 3 of 3 |
| unasked-edit-18-typos-and-contradiction | 2 of 3 | 3 of 3 |
| **Total** | **9 of 18** | **18 of 18** |

Record check: 18 of 18 runs passed all five lines. Cost per case: $0.84, $0.77, $1.25, $0.85, $0.99, $0.82. **Total cost: $5.52.**

### Findings

1. **The fix holds.** No copy in any of the 18 runs carries a status tag its source line did not have. The only tag written anywhere was case 1's `#status/provisional`, and its source carried it. Every untagged unit's record says `"status": "tentative"`, `"status_from": "default"`, and the replies say why, for example case 4 r2: "It had no status tag, so the copy has none and stays tentative."
2. **Nothing else regressed.** The Brain Dump doc is byte-identical before and after in all 18 runs. No existing line in a destination note changed. case 14's char-mara.md is unchanged in all three runs.
3. **Three copies spell out a pronoun.** Case 1 r2 ("Mara's brother's boat") and case 7 r1 and r3 ("Maybe Tobias left"). Each keeps its hedge and adds nothing the source does not say, the same kind of change as the first run's case 7 r1.
4. **Not graded:** case 14 r2 again asks whether "Definitely keeping this" was meant as committed; r1 and r3 ask only about the ferry line. In case 18, no run fixed "dosnt", as in the first run.

### Caveats

1. The judged checks were done by Claude reading each output, not by the eval tool's LLM graders and not calibrated against the writer.
2. Three runs per case is a small sample. In the first run the habit showed in 9 of these 18 runs; here it showed in none.
3. The cost per run is the `total_cost_usd` in each stream's result event. The runner printed a total of $5.52.
4. Outputs stay in `/var/folders/jp/t3th_wsd03xgpgdnsn9ys63w0000gn/T/tmp.0GiGjzyv6f`, which is a temporary folder the system may clear.

### Re-run Outputs

For each case: each run's verdict, every changed note after the run, the record file, and the record check. The starting notes are the same as in the case's first-run entry under Full Outputs. No run changed the Brain Dump doc.

#### Case 1: Plain copy with specifics

Case folder: `lost-detail-01-plain-copy`. Starting notes: see Case 1 under Full Outputs.

##### Run 1

**Verdict: PASS.** Both units land in the Idea Note, word for word. 214, aloud, her father, March 3 and her brother's boat all survive; "Maybe" and "Not sure if it's too neat" are kept. The first copy keeps the writer's `#status/provisional`; the second carries no tag. Brain Dump doc unchanged. No copy carries a status tag its source line did not have.

Cost: $0.27

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional
- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- Mara's lighthouse\" to \"Maybe the lamp failed\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The scoping comment names this bullet and the routing comment sends it to idea-mara-lighthouse. Copied in the writer's words, keeping the 214 steps, the nightly counting, the father, and the writer's provisional tag."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- Mara's lighthouse\" to \"Maybe the lamp failed\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The scoping comment names this bullet and the routing comment sends it to idea-mara-lighthouse. Untagged, so tentative with no tag; copied verbatim to keep the date, the hedge, and the writer's rationale."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

##### Run 2

**Verdict: PASS.** Same as r1, with one word changed in the second copy: "the night her brother's boat went out" became "the night Mara's brother's boat went out". The pronoun is spelled out so the line stands alone; it states nothing the source does not, and "brother" is still there for eval-cases-migrator.md 05.2 item 1. The second copy carries no tag. No copy carries a status tag its source line did not have.

Cost: $0.28

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional
- Maybe the lamp failed on March 3, the night Mara's brother's boat went out. Not sure if it's too neat.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- Mara's lighthouse\" to \"Maybe the lamp failed\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional"]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The scoping comment names this bullet and the routing comment sends it to idea-mara-lighthouse. Copied word for word with the writer's provisional tag, keeping the 214 steps, the nightly counting, and the father."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- Mara's lighthouse\" to \"Maybe the lamp failed\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": ["- Maybe the lamp failed on March 3, the night Mara's brother's boat went out. Not sure if it's too neat."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The scoping comment names this bullet and the routing comment sends it to idea-mara-lighthouse. It has no tag, so it stays tentative; \"her\" became \"Mara's\" so the line reads on its own, and the hedge, the date, and the writer's \"too neat\" rationale are kept."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

##### Run 3

**Verdict: PASS.** Same as r1, both copies word for word. The second copy carries no tag. No copy carries a status tag its source line did not have.

Cost: $0.28

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional
- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- Mara's lighthouse\" to \"Maybe the lamp failed\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The comment on line 13 scopes this bullet for migration and the comment on line 15 routes it to idea-mara-lighthouse. Copied word for word, with every specific (214 steps, the nightly count, the father's habit) and the writer's provisional tag."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- Mara's lighthouse\" to \"Maybe the lamp failed\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "# Idea - Mara Lighthouse",
          "lines": [
            "- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The same two comments scope this bullet and route it to idea-mara-lighthouse. Copied word for word, so it keeps the hedge \"Maybe\", the date March 3, and the writer's rationale \"Not sure if it's too neat.\" Untagged, so it stays tentative and the copy carries no tag."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Case 4: Existing text left alone

Case folder: `lost-detail-04-existing-text`. Starting notes: see Case 4 under Full Outputs.

##### Run 1

**Verdict: PASS.** The new unit is added under The lamp, word for word, with no tag. The whale-oil line is unchanged to the character. No copy carries a status tag its source line did not have.

Cost: $0.26

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp could run on something stranger than oil. Maybe it burns letters.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The lamp could run on something stranger than oil. Maybe it burns letters."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": ["- The lamp could run on something stranger than oil. Maybe it burns letters."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes it to idea-mara-lighthouse, and it belongs under The lamp. It is copied word for word to keep the hedges, and it sits after the whale-oil line as an alternative, so that line is left untouched."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

##### Run 2

**Verdict: PASS.** Same as r1. The reply says: "It had no status tag, so the copy has none and stays tentative." No copy carries a status tag its source line did not have.

Cost: $0.26

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp could run on something stranger than oil. Maybe it burns letters.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The lamp could run on something stranger than oil. Maybe it burns letters."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": ["- The lamp could run on something stranger than oil. Maybe it burns letters."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes the bullet to idea-mara-lighthouse; it is about the lamp, so it goes under 'The lamp', in the writer's words with its hedges kept. The source is untagged, so the copy carries no tag."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

##### Run 3

**Verdict: PASS.** Same as r1. No copy carries a status tag its source line did not have.

Cost: $0.25

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp could run on something stranger than oil. Maybe it burns letters.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The lamp could run on something stranger than oil. Maybe it burns letters."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": ["- The lamp could run on something stranger than oil. Maybe it burns letters."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names idea-mara-lighthouse, and the line is about the lamp, so it goes under The lamp, kept word for word with its hedges. It sits next to the whale-oil line as an alternative, and that line is left as it is."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Case 7: Batch of fourteen bullets to two Idea Notes

Case folder: `lost-detail-07-batch-two-notes`. Starting notes: see Case 7 under Full Outputs.

##### Run 1

**Verdict: PASS.** All fourteen land in the right note, and every planted specific survives. The seven hedged bullets stay hedged and the seven flat ones gain no hedge. Thirteen copies are word for word; "Maybe he left at 2:40" became "Maybe Tobias left at 2:40", hedge kept, as in the first run's r1. No copy carries a tag. No copy carries a status tag its source line did not have.

Cost: $0.42

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The town is called Harrow Point and it has exactly one road in, which floods at spring tide.
- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days.
- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute.
- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow.
- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?
- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go.
- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him.
````

**After: Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night

- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night.
- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock.
- Maybe Tobias left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close.
- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing.
- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding.
- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet.
- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 10, "text": "- The town is called Harrow Point and it has exactly one road in, which floods at spring tide."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The town is called Harrow Point and it has exactly one road in, which floods at spring tide."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The migrate comment covers this bullet and the routing comment sends it to idea-harrow-point. Untagged, so it stays tentative; copied in the writer's words."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 11, "text": "- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the migrate range; routed to idea-harrow-point by the writer's comment. Copied verbatim, keeping the hedge."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 12, "text": "- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the migrate range; routed to idea-harrow-point. The writer's note-to-self stays attached to the idea in an Idea Note."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 13, "text": "- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the migrate range; routed to idea-harrow-point. Copied verbatim with both numbers and the hedge."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 14, "text": "- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?"}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the migrate range; routed to idea-harrow-point. Prose question stays inside the unit; not turned into a [?] line."
    },
    {
      "id": "u6",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 15, "text": "- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the migrate range; routed to idea-harrow-point. Kept whole since the consequence depends on the ferry detail."
    },
    {
      "id": "u7",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 16, "text": "- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet of the migrate range; routed to idea-harrow-point. Copied verbatim with its hedge."
    },
    {
      "id": "u8",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 24, "text": "- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "First bullet of the migrate range; the routing comment sends it to idea-storm-night. Untagged, so tentative; copied verbatim."
    },
    {
      "id": "u9",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 25, "text": "- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the migrate range; routed to idea-storm-night. Untagged in the Brain Dump doc, so tentative despite the plain wording."
    },
    {
      "id": "u10",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 26, "text": "- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Maybe Tobias left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the migrate range; routed to idea-storm-night. \"He\" is replaced with \"Tobias\" so the line reads on its own; both times and the hedge are kept."
    },
    {
      "id": "u11",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 27, "text": "- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the migrate range; routed to idea-storm-night. Copied verbatim."
    },
    {
      "id": "u12",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 28, "text": "- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the migrate range; routed to idea-storm-night. Copied verbatim with its hedge."
    },
    {
      "id": "u13",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 29, "text": "- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the migrate range; routed to idea-storm-night. Copied verbatim."
    },
    {
      "id": "u14",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 30, "text": "- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet of the migrate range; routed to idea-storm-night. Copied verbatim, keeping the writer's framing and hedge."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

##### Run 2

**Verdict: PASS.** All fourteen copied word for word into the right notes, with no tags. No copy carries a status tag its source line did not have.

Cost: $0.42

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The town is called Harrow Point and it has exactly one road in, which floods at spring tide.
- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days.
- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute.
- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow.
- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?
- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go.
- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him.
````

**After: Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night

- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night.
- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock.
- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close.
- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing.
- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding.
- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet.
- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 10, "text": "- The town is called Harrow Point and it has exactly one road in, which floods at spring tide."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The town is called Harrow Point and it has exactly one road in, which floods at spring tide."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment scopes this bullet to migrate and the comment \"Agent, these go in idea-harrow-point.\" routes it there. Untagged in the Brain Dump doc, so it stays tentative and carries no tag."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 11, "text": "- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "In the comment's migrate range and routed to idea-harrow-point. Copied verbatim to keep the \"Maybe\" hedge."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 12, "text": "- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "In the comment's migrate range and routed to idea-harrow-point. The writer's \"Not sure if that's too cute\" is rationale and stays with the unit."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 13, "text": "- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "In the comment's migrate range and routed to idea-harrow-point. Copied verbatim with both numbers and the hedge."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 14, "text": "- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?"}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?"]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "In the comment's migrate range and routed to idea-harrow-point. Kept whole: the pub's name is a consequence of the bell sale, so the parts don't stand apart."
    },
    {
      "id": "u6",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 15, "text": "- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "In the comment's migrate range and routed to idea-harrow-point. Copied verbatim."
    },
    {
      "id": "u7",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [{"note": "brain-dump.md", "line": 16, "text": "- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."}],
      "copies": [{"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet of the comment's migrate range, routed to idea-harrow-point. Copied verbatim to keep the \"Could be\" hedge."
    },
    {
      "id": "u8",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 24, "text": "- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment scopes this bullet to migrate and the comment \"Agent, these go in idea-storm-night.\" routes it there. Untagged, so tentative; \"I want\" doesn't set status."
    },
    {
      "id": "u9",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 25, "text": "- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "In the comment's migrate range and routed to idea-storm-night. Copied verbatim."
    },
    {
      "id": "u10",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 26, "text": "- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "In the comment's migrate range and routed to idea-storm-night. Placed right after the Tobias line so \"he\" reads correctly; both times kept."
    },
    {
      "id": "u11",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 27, "text": "- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "In the comment's migrate range and routed to idea-storm-night. Copied verbatim."
    },
    {
      "id": "u12",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 28, "text": "- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "In the comment's migrate range and routed to idea-storm-night. Copied verbatim to keep the \"Possibly\" hedge."
    },
    {
      "id": "u13",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 29, "text": "- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "In the comment's migrate range and routed to idea-storm-night. Copied verbatim; not turned into a Question."
    },
    {
      "id": "u14",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [{"note": "brain-dump.md", "line": 30, "text": "- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."}],
      "copies": [{"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."]}],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet of the comment's migrate range, routed to idea-storm-night. Copied verbatim with the \"maybe Coyle\" hedge."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

##### Run 3

**Verdict: PASS.** Same as r1, including "Maybe Tobias left at 2:40". No copy carries a tag. No copy carries a status tag its source line did not have.

Cost: $0.42

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The town is called Harrow Point and it has exactly one road in, which floods at spring tide.
- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days.
- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute.
- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow.
- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?
- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go.
- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him.
````

**After: Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

# Idea - Storm Night

- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night.
- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock.
- Maybe Tobias left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close.
- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing.
- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding.
- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet.
- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [
        {"note": "brain-dump.md", "line": 10, "text": "- The town is called Harrow Point and it has exactly one road in, which floods at spring tide."}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The town is called Harrow Point and it has exactly one road in, which floods at spring tide."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The migrate comment covers this bullet and the routing comment sends it to idea-harrow-point. Copied in the writer's words, untagged, as it was untagged at the source."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [
        {"note": "brain-dump.md", "line": 11, "text": "- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment, routed to idea-harrow-point. Kept verbatim with its hedge and the consequence."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [
        {"note": "brain-dump.md", "line": 12, "text": "- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute."}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment, routed to idea-harrow-point. The writer's rationale \"Not sure if that's too cute\" stays with the unit in an Idea Note."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [
        {"note": "brain-dump.md", "line": 13, "text": "- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment, routed to idea-harrow-point. Kept verbatim, with both numbers and the hedge."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [
        {"note": "brain-dump.md", "line": 14, "text": "- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?"}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?"]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment, routed to idea-harrow-point. The prose question stays inside the unit, unconverted."
    },
    {
      "id": "u6",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [
        {"note": "brain-dump.md", "line": 15, "text": "- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go."}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment, routed to idea-harrow-point. Kept verbatim with its consequence."
    },
    {
      "id": "u7",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\""},
      "sources": [
        {"note": "brain-dump.md", "line": 16, "text": "- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."}
      ],
      "copies": [
        {"note": "Ideas/idea-harrow-point.md", "under": "# Idea - Harrow Point", "lines": ["- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet in the migrate comment's range, routed to idea-harrow-point. Kept verbatim."
    },
    {
      "id": "u8",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [
        {"note": "brain-dump.md", "line": 24, "text": "- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night."}
      ],
      "copies": [
        {"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The migrate comment covers this bullet and the routing comment sends it to idea-storm-night. \"I want\" is a note-to-self, not a status, so it stays tentative and verbatim."
    },
    {
      "id": "u9",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [
        {"note": "brain-dump.md", "line": 25, "text": "- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock."}
      ],
      "copies": [
        {"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment, routed to idea-storm-night. Kept verbatim with its cause."
    },
    {
      "id": "u10",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [
        {"note": "brain-dump.md", "line": 26, "text": "- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."}
      ],
      "copies": [
        {"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Maybe Tobias left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment, routed to idea-storm-night. \"he\" is replaced with \"Tobias\" so the unit reads on its own; times and the hedge are kept."
    },
    {
      "id": "u11",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [
        {"note": "brain-dump.md", "line": 27, "text": "- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing."}
      ],
      "copies": [
        {"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment, routed to idea-storm-night. Kept verbatim, including the channel number."
    },
    {
      "id": "u12",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [
        {"note": "brain-dump.md", "line": 28, "text": "- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."}
      ],
      "copies": [
        {"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment, routed to idea-storm-night by the writer even though it names the pub. Kept verbatim."
    },
    {
      "id": "u13",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [
        {"note": "brain-dump.md", "line": 29, "text": "- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet."}
      ],
      "copies": [
        {"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Covered by the migrate comment, routed to idea-storm-night. Kept verbatim; \"which nobody can explain yet\" stays as the writer's words, not turned into a Question."
    },
    {
      "id": "u14",
      "action": "migrate",
      "trigger": {"kind": "comment", "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\""},
      "sources": [
        {"note": "brain-dump.md", "line": 30, "text": "- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."}
      ],
      "copies": [
        {"note": "Ideas/idea-storm-night.md", "under": "# Idea - Storm Night", "lines": ["- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."]}
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet in the migrate comment's range, routed to idea-storm-night. Kept verbatim with the hedge on Coyle and the six years."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Case 8: Merge by comment

Case folder: `lost-detail-08-merge-by-comment`. Starting notes: see Case 8 under Full Outputs.

##### Run 1

**Verdict: PASS.** One merged unit, with all three source lines in the record. Wrong for this coast, Marrow Bay, clockwise, 1911, the grandfather and the mirror-image drawing survive. "Possibly on purpose." stays its own sentence and qualifies only "on purpose". Whale-oil line unchanged. No tag. No copy carries a status tag its source line did not have.

Cost: $0.28

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, these three are the same idea said three ways. Merge them into one unit in idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The lamp turns counterclockwise, which is wrong for this coast."
        },
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Mara's lamp rotates the wrong way round. Every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911."
        },
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": [
            "- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment asks for the three lines to be merged into one unit in idea-mara-lighthouse; it goes under the existing 'The lamp' heading. The merge keeps every specific (counterclockwise, this coast, Marrow Bay, 1911, the grandfather's mirror-image drawing) and the hedge 'Possibly on purpose', and the untagged sources stay tentative with no tag."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

##### Run 2

**Verdict: PASS.** The same merged line as r1, character for character, with no tag. No copy carries a status tag its source line did not have.

Cost: $0.28

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, these three are the same idea said three ways. Merge them into one unit in idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The lamp turns counterclockwise, which is wrong for this coast."
        },
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Mara's lamp rotates the wrong way round. Every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911."
        },
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": [
            "- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment asks for the three lines merged into one unit in idea-mara-lighthouse; it goes under the existing lamp heading. The merge keeps every specific (counterclockwise, this coast, Marrow Bay, 1911, the grandfather's mirror-image drawing) and the hedge 'Possibly on purpose', and no source carries a tag, so the copy stays untagged."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

##### Run 3

**Verdict: PASS.** The same merged line as r1, character for character, with no tag. No copy carries a status tag its source line did not have.

Cost: $0.28

**After: Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

# Idea - Mara Lighthouse

## The lamp

- The lamp uses whale oil, which the town can no longer afford.
- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, these three are the same idea said three ways. Merge them into one unit in idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The lamp turns counterclockwise, which is wrong for this coast."
        },
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Mara's lamp rotates the wrong way round. Every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911."
        },
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The lamp",
          "lines": [
            "- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment asks for the three lines to be merged into one unit in idea-mara-lighthouse; it goes under the existing lamp heading. The merged line keeps every specific (counterclockwise, this coast, Marrow Bay, 1911, the grandfather's mirror-image drawing) and the hedge 'Possibly on purpose.'"
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Case 14: Lines outside the migrate range

Case folder: `unasked-migration-14-outside-range`. Starting notes: see Case 14 under Full Outputs.

##### Run 1

**Verdict: PASS.** The three bullets in range land in the Idea Note word for word, with no tags. The ferry line and every 2026-09-29 line stay, all five listed in `left_in_place`. char-mara.md unchanged. One question, about the ferry line. No copy carries a status tag its source line did not have.

Cost: $0.33

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The harbour has a tide bell that rings itself when the swell is over two metres.
- Nobody in town will say who installed it. Pell claims it predates the lighthouse.
- People set their clocks by it even though it's never on time.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The harbour has a tide bell that rings itself when the swell is over two metres."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- The harbour has a tide bell that rings itself when the swell is over two metres."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "First bullet in the range the line 15 comment names. The line 17 comment, \"Agent, these go in idea-harrow-point\", routes it to that Idea Note. It is untagged, so the copy is untagged."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Nobody in town will say who installed it. Pell claims it predates the lighthouse."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- Nobody in town will say who installed it. Pell claims it predates the lighthouse."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, and routed to idea-harrow-point by the line 17 comment. It sits directly after the tide bell line, so \"it\" still clearly means the bell."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- People set their clocks by it even though it's never on time."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- People set their clocks by it even though it's never on time."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet in the commented range, and routed to idea-harrow-point by the line 17 comment. It follows the bell lines, so \"it\" still clearly means the bell."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "why": "Outside the range the line 15 comment names, which ends at \"People set their clocks\". \"This one should live with the town stuff too\" is prose in the bullet, not a tag or a comment, so it doesn't trigger migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 21,
        "text": "- Definitely keeping this: Mara hums the shipping forecast when she's nervous."
      },
      "why": "No status tag and no comment. \"Definitely keeping this\" is prose, and prose doesn't set status or trigger migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 22,
        "text": "- Coyle waters down the whisky and everyone knows. #town"
      },
      "why": "#town is not a status tag, and no comment covers this line, so it doesn't migrate."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 23,
        "text": "- The lifeboat station closed in 2009."
      },
      "why": "No status tag and no comment, so it doesn't migrate."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 24,
        "text": "    - Its slipway is where the kids swim now."
      },
      "why": "Nested under an untagged parent, with no tag or comment of its own, so it doesn't migrate."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "ask": "This line falls just outside your migrate range, which ends at \"People set their clocks\", but its own words say it should live with the town stuff. Do you want it migrated to idea-harrow-point too? If so, extend the comment's range or tag the line."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

##### Run 2

**Verdict: PASS.** Same as r1, with a second question about "Definitely keeping this". No copy carries a status tag its source line did not have.

Cost: $0.33

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The harbour has a tide bell that rings itself when the swell is over two metres.
- Nobody in town will say who installed it. Pell claims it predates the lighthouse.
- People set their clocks by it even though it's never on time.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The harbour has a tide bell that rings itself when the swell is over two metres."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- The harbour has a tide bell that rings itself when the swell is over two metres."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "First bullet in the comment's migrate range; the routing comment \"Agent, these go in idea-harrow-point.\" names the destination. Untagged in the Brain Dump doc, so it stays tentative with no tag."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Nobody in town will say who installed it. Pell claims it predates the lighthouse."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- Nobody in town will say who installed it. Pell claims it predates the lighthouse."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the comment's migrate range, routed to idea-harrow-point by the writer. Placed directly after the tide bell line so \"it\" still reads as the bell."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- People set their clocks by it even though it's never on time."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- People set their clocks by it even though it's never on time."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet in the comment's migrate range, routed to idea-harrow-point by the writer. Kept next to the other tide bell lines so \"it\" still reads as the bell."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "why": "Outside the range the migrate comment names (it ends at \"People set their clocks\"), and it carries no status tag. The prose \"should live with the town stuff too\" is not a comment, so it does not trigger migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 21,
        "text": "- Definitely keeping this: Mara hums the shipping forecast when she's nervous."
      },
      "why": "No status tag and no comment. \"Definitely keeping this\" is prose and sets no status, so the line does not migrate to char-mara."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 22,
        "text": "- Coyle waters down the whisky and everyone knows. #town"
      },
      "why": "#town is not a status tag and no comment covers the line, so it does not migrate."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 23,
        "text": "- The lifeboat station closed in 2009."
      },
      "why": "No status tag and no comment, so it does not migrate."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 24,
        "text": "    - Its slipway is where the kids swim now."
      },
      "why": "No status tag, no comment, and its parent bullet carries no tag, so it does not migrate."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "ask": "This bullet falls just outside your migrate range, but its prose says it should live with the town stuff too. Do you want it migrated to idea-harrow-point? If so, extend the comment's range or tag it."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 21,
        "text": "- Definitely keeping this: Mara hums the shipping forecast when she's nervous."
      },
      "ask": "This line says \"Definitely keeping this\" but has no tag or comment, so it stayed put. If you mean it as committed for char-mara, tag it #status/committed or add a comment."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

##### Run 3

**Verdict: PASS.** Same as r1. No copy carries a status tag its source line did not have.

Cost: $0.32

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

- The harbour has a tide bell that rings itself when the swell is over two metres.
- Nobody in town will say who installed it. Pell claims it predates the lighthouse.
- People set their clocks by it even though it's never on time.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The harbour has a tide bell that rings itself when the swell is over two metres."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- The harbour has a tide bell that rings itself when the swell is over two metres."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "First bullet in the range the migrate comment names. The second comment routes these bullets to idea-harrow-point; untagged, so the copy stays untagged."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Nobody in town will say who installed it. Pell claims it predates the lighthouse."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- Nobody in town will say who installed it. Pell claims it predates the lighthouse."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-harrow-point. It sits directly after the tide bell line so \"it\" still reads as the bell."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The harbour has a tide bell\" to \"People set their clocks\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- People set their clocks by it even though it's never on time."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": ["- People set their clocks by it even though it's never on time."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet of the commented range, routed to idea-harrow-point. Placed right after the other tide bell lines so \"it\" still reads as the bell."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "why": "Outside the range the migrate comment names (it ends at \"People set their clocks\") and has no status tag. \"This one should live with the town stuff too\" is prose, not a comment, so it doesn't trigger migration."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 21,
        "text": "- Definitely keeping this: Mara hums the shipping forecast when she's nervous."
      },
      "why": "No status tag and no comment. \"Definitely keeping this\" is prose, which never sets status or triggers migration, so it stays tentative and does not graduate to char-mara."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 22,
        "text": "- Coyle waters down the whisky and everyone knows. #town"
      },
      "why": "#town is not a status tag and no comment covers this line, so it doesn't migrate."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 23,
        "text": "- The lifeboat station closed in 2009."
      },
      "why": "No status tag and no comment, so it doesn't migrate."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 24,
        "text": "    - Its slipway is where the kids swim now."
      },
      "why": "Nested under an untagged parent, with no tag or comment of its own, so it doesn't migrate."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "ask": "Your migrate comment ends at \"People set their clocks\", so this ferry timetable line wasn't migrated, even though its prose says it should live with the town stuff. Should it go to idea-harrow-point too? If so, extend the comment's range or add a comment on it."
    }
  ],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

#### Case 18: Typos and a contradiction in existing lines

Case folder: `unasked-edit-18-typos-and-contradiction`. Starting notes: see Case 18 under Full Outputs.

##### Run 1

**Verdict: PASS.** Both existing lines unchanged to the character, typos included; the contradicted line stays. The new unit is added word for word, keeping "dosnt", with no tag. No copy carries a status tag its source line did not have.

Cost: $0.27

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## The harbour office

- The harbor masters office has no windows facing the see.
- Pell keeps the tide tables locked up.
- Pell dosnt lock the tide tables anymore, he lost the key in 2019.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Pell dosnt lock the tide tables anymore, he lost the key in 2019."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## The harbour office",
          "lines": ["- Pell dosnt lock the tide tables anymore, he lost the key in 2019."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes the line to idea-harrow-point. It sits under The harbour office, next to the other Pell tide-tables line, in the writer's words."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

##### Run 2

**Verdict: PASS.** Same as r1. No copy carries a status tag its source line did not have.

Cost: $0.28

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## The harbour office

- The harbor masters office has no windows facing the see.
- Pell keeps the tide tables locked up.
- Pell dosnt lock the tide tables anymore, he lost the key in 2019.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Pell dosnt lock the tide tables anymore, he lost the key in 2019."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## The harbour office",
          "lines": ["- Pell dosnt lock the tide tables anymore, he lost the key in 2019."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes the line to idea-harrow-point, and it goes under the harbour office heading next to the other line about Pell and the tide tables. It is copied in the writer's words, and neighbouring lines are left as they are."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

##### Run 3

**Verdict: PASS.** Same as r1. No copy carries a status tag its source line did not have.

Cost: $0.27

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

# Idea - Harrow Point

## The harbour office

- The harbor masters office has no windows facing the see.
- Pell keeps the tide tables locked up.
- Pell dosnt lock the tide tables anymore, he lost the key in 2019.
````

**Record: run/unit-records.json**

````json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Pell dosnt lock the tide tables anymore, he lost the key in 2019."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## The harbour office",
          "lines": ["- Pell dosnt lock the tide tables anymore, he lost the key in 2019."]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes the line to idea-harrow-point; it sits under 'The harbour office' next to the existing tide-tables line. Copied in the writer's words with no tag, since the source is untagged; no comment allowed spelling fixes, and contradictions with neighbouring tentative lines are not flagged."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
````

**Record check**

````text
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
````

## Re-run after the hedged-name rule: case 5

Run on 2026-10-04, about 18:12 EDT. Same command, agent, and prompt as the first run. One change in the rules file: migrator-rules.md 02.2's Idea Note bullet gained the hedged-name rule (a hedge on a name or detail is stated once, where it is introduced, and the name or detail is not used as settled on other lines). The 03.7 fix from the earlier re-run is also in the file.

| Case | Bare | First run | Re-run |
| --- | --- | --- | --- |
| lost-detail-05-dense-bullet | 2 of 3 | 1 of 3 | 3 of 3 |

Graded by the orchestrating session, which also wrote the rule, by reading each run's added lines against the Pass line in eval-cases-migrator.md 07.1. In all three runs "Ansel" appears once, with its hedge, and every other line says "the keeper before Mara". Every planted specific is present. No question became a `- [?]` line. The diffs show only added lines. Cost: $0.97.

### Case 5, re-run 1: pass

Lines added to `Ideas/idea-mara-lighthouse.md`:

```markdown
- The keeper before Mara, who I'm thinking is a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?
- Maybe the keeper before Mara logged every ship that didn't come back in the second logbook, 31 of them, going back to 1987.
- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.
- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.
```

Record file:

```json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Okay so the keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step? Maybe she logged every ship that didn't come back, 31 of them, going back to 1987. Does Mara find it, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out. What if the last entry is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The keeper before Mara",
          "lines": [
            "- The keeper before Mara, who I'm thinking is a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?",
            "- Maybe the keeper before Mara logged every ship that didn't come back in the second logbook, 31 of them, going back to 1987.",
            "- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.",
            "- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names idea-mara-lighthouse, and the bullet is about the keeper before Mara, so it goes under that heading as a split into four adjacent lines that keep every specific and hedge (the name Ansel hedged once, then 'the keeper before Mara'). The key question stays with the handwriting line because 'who else had a key' follows from it."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

Record check:

```
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
```

### Case 5, re-run 2: pass

Lines added to `Ideas/idea-mara-lighthouse.md`:

```markdown
- The keeper before Mara (I'm thinking a woman named Ansel) kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?
- Maybe the keeper before Mara logged every ship that didn't come back in that second logbook, 31 of them, going back to 1987.
- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.
- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.
```

Record file:

```json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Okay so the keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step? Maybe she logged every ship that didn't come back, 31 of them, going back to 1987. Does Mara find it, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out. What if the last entry is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The keeper before Mara",
          "lines": [
            "- The keeper before Mara (I'm thinking a woman named Ansel) kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?",
            "- Maybe the keeper before Mara logged every ship that didn't come back in that second logbook, 31 of them, going back to 1987.",
            "- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.",
            "- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names idea-mara-lighthouse, and the whole bullet is about the keeper before Mara, so it goes under that heading as four adjacent Idea Units: the logbook and where it is hidden, the ship log, who finds it, and the handwriting with the key question. The name hedge on Ansel is stated once where she is introduced, and every hedge, question, and specific (40th step, 31 ships, 1987, Pell) is kept; untagged, so it stays tentative."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

Record check:

```
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
```

### Case 5, re-run 3: pass

Lines added to `Ideas/idea-mara-lighthouse.md`:

```markdown
- The keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about.
- Is the second logbook hidden in the lamp room or under the 40th step?
- Maybe the keeper before Mara logged every ship that didn't come back in the second logbook, 31 of them, going back to 1987.
- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.
- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.
```

Record file:

```json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, migrate this to idea-mara-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- Okay so the keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step? Maybe she logged every ship that didn't come back, 31 of them, going back to 1987. Does Mara find it, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out. What if the last entry is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-mara-lighthouse.md",
          "under": "## The keeper before Mara",
          "lines": [
            "- The keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about.",
            "- Is the second logbook hidden in the lamp room or under the 40th step?",
            "- Maybe the keeper before Mara logged every ship that didn't come back in the second logbook, 31 of them, going back to 1987.",
            "- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.",
            "- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names idea-mara-lighthouse, and the bullet is about the keeper before Mara, so it goes under that heading. The dense bullet is split into adjacent lines that each name the logbook or the keeper so they read on their own; the hedge on the name Ansel is stated once where she is introduced, and every other specific and hedge (maybe, 31 ships, 1987, the 40th step, possibly Pell) is kept."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

Record check:

```
PASS  record file exists, parses, and has the spec 05.2 fields
PASS  every added line is in the record (copies[].lines or edits[].after)
PASS  every removed or changed line is in the record (reject sources or edits[].before)
PASS  every copies[].lines entry appears in the note it names
PASS  the record file is written before the first Write/Edit to project/
```
