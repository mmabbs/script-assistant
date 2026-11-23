# Migrator, all twenty cases, one run each, on the final rules file

Run on 2026-10-13 with `_tools/research-run.py --suite migrator --agent script-asst:migrator --runs 1`. Agent: `agents/migrator.md` as of 2026-10-13 13:43, on `claude-opus-5-5`. Rules file: `_fixtures/rules/migrator-rules.md`, identical to the plugin's `references/migrator-rules.md` (2026-10-10).

## What changed since the 2026-10-04 run

1. **The prompts hand the batch the way the `/script-asst:run` skill does:** batch b1's pieces as the Run manager's scan returns them for the fixture, not "the whole of project/brain-dump.md." Every fixture scans to one batch, all from `brain-dump.md`. In case 14 the scan hands only the two comments, so the second date heading's untagged lines never reach the Migrator, as in a real run.
2. **The graders ran in code for the first time,** with `record-check.py` added as one line per run. The 2026-10-04 runs were graded by Claude reading the outputs.
3. **Case 20 is new.** Case 21 was written in the same session and run after the writer approved its Pass line. Its run is at the end of this file.

## Results

| Case | Checks passed | Pass line held |
| --- | --- | --- |
| 1 | 15 of 15 | yes |
| 2 | 10 of 10 | yes |
| 3 | 13 of 13, after the judge fix below | yes |
| 4 | 10 of 10 | yes |
| 5 | 22 of 22 | yes |
| 6 | 21 of 21 | yes |
| 7 | 52 of 52 | yes |
| 8 | 16 of 16 | yes |
| 9 | 21 of 21 | yes |
| 10 | 10 of 10 | yes |
| 11 | 9 of 9 | yes |
| 12 | 9 of 9 | yes |
| 13 | 8 of 8 | yes |
| 14 | 18 of 18 | yes |
| 15 | 13 of 13 | yes |
| 16 | 10 of 10 | yes |
| 17 | 22 of 22 | yes |
| 18 | 8 of 8 | yes |
| 19 | 21 of 21 | yes |
| 20 | 9 of 9 | yes |

20 of 20. Every record check passed. Cost: $7.12, judges included, plus about $0.03 for the case 3 regrade.

## Findings

1. **Case 3's one fail was the grader's.** `judge-standalone` failed the Area Note because "nothing in the file says who Tobias is" and because the Rationale line doesn't say what Tobias is the reason for. The source line never says who Tobias is, so adding it would break judge question 2 in eval-cases-migrator.md 05.3, and the Pass line holds the Rationale line word for word. The judge now says both are not failures. Regraded: PASS. The note changes are below.
2. **Spot-checked by hand against their Pass lines:** cases 5, 9, 10, 11, 14, 16, and 20. Each holds. Case 5 states the hedged name once ("I'm thinking a woman named Ansel") and says "the keeper before Mara" after. Case 10 graduates only the first idea and asks about the other two. Case 11 rejects only Mara's fear, writes the reason as the comment line below it (migrator-rules.md, the rule on where the reason goes), and changes "She gets seasick" to "Mara gets seasick," recorded as an edit. Case 14 leaves the ferry timetable line and asks whether it should move. Case 20 puts the ferry horn line in the Harrow Point note and asks nothing.
3. **Case 11's reason comment won't come back as new work.** CONTRACT.md 5.6 item 3 puts a rejected unit's moved line and its reason comment on the handled list.
4. **Added 2026-10-14: the runner never counted.** Six graders in cases 1, 7, 8, 12, and 17 use `match: "count:N"`, which `research-run.py` read as a plain "contains" until 2026-10-14. With counting fixed, all six regraded as PASS with the exact count. The grades below are from before the fix.

Each case's grades, note changes, unit record, and reply follow, so the run can be rebuilt if its folder is lost. The run folders were in the session's scratchpad.

## lost-detail-01-plain-copy r1: 15 of 15 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  judge-facts-preserved   Each of the five required details appears in the text:  - **214 steps:** "Mara's lighthouse has 214 steps" - **Counting aloud every night:** "she counts them aloud every night" - **A habit from her father:** "a habit from her father" - **March 3:** "the lamp failed on March 3" - **Her brother's boat went out:** "the night Mara's brother's boat went out"  The second line is framed as tentative ("M
PASS  judge-firmness   The second bullet keeps both hedges from the source: - It still opens with "Maybe": "Maybe the lamp failed on March 3, the night Mara's brother's boat went out." The lamp failure is not stated as fact. - It keeps the doubt word for word: "Not sure if it's too neat."
PASS  judge-standalone   **Evidence:** Both bullets are clear to someone reading only this note.  - **Bullet 1:** "Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father."   - "she" refers to Mara, who is named earlier in the same sentence.   - "her father" is therefore Mara's father.   - No pronoun is left without a referent. - **Bullet 2:** "Maybe the lamp failed on March 3, the
PASS  keeps-214  found '214'
PASS  keeps-aloud  found 'aloud'
PASS  keeps-brother  found 'brother'
PASS  keeps-father  found 'father'
PASS  keeps-hedge-maybe  found 'Maybe'
PASS  keeps-hedge-too-neat  found 'too neat'
PASS  keeps-march-3  found 'March 3'
PASS  no-other-status-tag  no match
PASS  provisional-tag-count  found '#status/provisional'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-mara-lighthouse.md work/project/Ideas/idea-mara-lighthouse.md
--- before/project/Ideas/idea-mara-lighthouse.md	2026-10-13 19:39:49
+++ work/project/Ideas/idea-mara-lighthouse.md	2026-10-13 19:40:12
@@ -4,3 +4,6 @@
 ---
 
 # Idea - Mara Lighthouse
+
+- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional
+- Maybe the lamp failed on March 3, the night Mara's brother's boat went out. Not sure if it's too neat.
```

### Unit record

```json
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
      "why": "The scope comment on line 13 covers this bullet, and the comment on line 15 routes it to idea-mara-lighthouse. Copied verbatim, keeping the writer's provisional tag and every specific (214 steps, aloud, every night, her father's habit)."
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
            "- Maybe the lamp failed on March 3, the night Mara's brother's boat went out. Not sure if it's too neat."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The scope comment on line 13 covers this bullet and line 15 routes it to idea-mara-lighthouse. It is untagged, so it stays tentative; the hedge \"Maybe\", the date, and the writer's rationale \"Not sure if it's too neat\" are kept, and \"her\" is replaced with Mara's name so the line reads on its own."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
I migrated both bullets in batch b1 (round 0) into `Ideas/idea-mara-lighthouse.md`. Nothing was left in place, there are no questions for you, and there was nothing I couldn't do.

- **u1** (brain-dump line 10, the lighthouse steps): copied word for word and keeps your `#status/provisional` tag. The comment on line 13 says which bullets migrate, and the one on line 15 says where they go.
- **u2** (brain-dump line 11, the lamp failing): untagged, so it stays tentative. I kept "Maybe", the March 3 date and your "Not sure if it's too neat." The only change is that "her brother's boat" now reads "Mara's brother's boat", so the line makes sense without the bullet above it.

Both lines sit under the note's `# Idea - Mara Lighthouse` heading, and they match the record exactly. I didn't touch `brain-dump.md`.

Record file: `run/unit-records.json`
```

## lost-detail-02-split-across-notes r1: 10 of 10 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  habits-names-tobias  found 'place at dinner for her brother Tobias'
PASS  judge-habits-standalone   The dinner line says who the place is for: "Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine." It gives both the relationship ("her brother") and the name ("Tobias"), so the line makes sense without the original bullet. It never uses a bare "him" or "he". The mention of the drowning is allowed.
PASS  judge-tobias-facts   The note states both required elements in one line: "Mara's brother Tobias drowned when she was nine." - The drowning is present: "Tobias drowned" - The age is present: "when she was nine"
PASS  no-status-tags-habits  no match
PASS  no-status-tags-tobias  no match
PASS  tobias-drowned  found 'drown'
PASS  tobias-nine  found 'nine'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-mara-habits.md work/project/Ideas/idea-mara-habits.md
--- before/project/Ideas/idea-mara-habits.md	2026-10-13 19:39:49
+++ work/project/Ideas/idea-mara-habits.md	2026-10-13 19:40:10
@@ -4,3 +4,5 @@
 ---
 
 # Idea - Mara Habits
+
+- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine.
diff -ru before/project/Ideas/idea-tobias.md work/project/Ideas/idea-tobias.md
--- before/project/Ideas/idea-tobias.md	2026-10-13 19:39:49
+++ work/project/Ideas/idea-tobias.md	2026-10-13 19:40:09
@@ -4,3 +4,5 @@
 ---
 
 # Idea - Tobias
+
+- Mara's brother Tobias drowned when she was nine.
```

### Unit record

```json
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
          "lines": [
            "- Mara's brother Tobias drowned when she was nine."
          ]
        },
        {
          "note": "Ideas/idea-mara-habits.md",
          "under": "# Idea - Mara Habits",
          "lines": [
            "- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes the drowning to idea-tobias and the dinner habit to idea-mara-habits; it sets no status, so the Brain Dump default (tentative) holds and no tag is written. The habits line names Mara, Tobias, and his drowning so it keeps its meaning on its own."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
Batch b1 is done: 1 unit migrated, as a split into two notes. Nothing was left in place and there are no questions.

- **u1:** I split the line at `brain-dump.md` line 10 into the two notes your comment on line 12 named:
  - `Ideas/idea-tobias.md`: `- Mara's brother Tobias drowned when she was nine.`
  - `Ideas/idea-mara-habits.md`: `- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine.`

  I reworded the habits line so it names Tobias and his drowning. Read alone, "she sets a place for him" would lose who "him" is and why it matters.
- **Status:** both copies are tentative and carry no tag. Your comment only said where the lines go, not what status they have, so the Brain Dump default applies.
- I wrote nothing in `brain-dump.md`.

The unit record is at `run/unit-records.json`.
```

## lost-detail-03-area-note-rewrite r1: 13 of 13 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  judge-facts-preserved   All three facts appear verbatim in one bullet under "Motivation and Intention":  > "- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job."  - **Lit for Tobias:** "keeps the lamp lit for Tobias" - **Not for ships:** "not for ships" - **Town believes she's only doing her job:** "the town believes she's only doing her job"
PASS  judge-notes-dropped   The phrase "I really like this" does not appear anywhere in the file, and no equivalent first-person aside does either. There is no "I," "me," "my," or other self-addressed remark.  The only evaluative line is in the Rationale section:  - "Tobias as the reason feels more honest than duty."  This is an impersonal design rationale that explains why the choice was made, and it sits in the section bu
PASS  judge-standalone   Two statements were added to the file, and both make sense on their own.  1. **Motivation line:** "Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job."    - The only pronouns are "she's" and "her." Both point to Mara, who is named at the start of the same sentence, so they are not ambiguous.    - "the lamp" makes sense because the file lists her occu
PASS  keeps-ships  found 'ships'
PASS  keeps-tobias  found 'Tobias'
PASS  keeps-town  found 'town'
PASS  no-status-tag  no match
PASS  note-to-self-dropped  no match
PASS  rationale-under-heading  found '# Rationale\n\n- Tobias as the reason feels more honest than duty'
PASS  rationale-word-for-word  found 'Tobias as the reason feels more honest than duty.'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/char-mara.md work/project/char-mara.md
--- before/project/char-mara.md	2026-10-13 19:39:49
+++ work/project/char-mara.md	2026-10-13 19:40:10
@@ -16,6 +16,8 @@
 
 ## Motivation and Intention
 
+- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job.
+
 # Bio
 
 ## General
@@ -25,5 +27,7 @@
 ## Values, Beliefs, etc.
 
 # Rationale
+
+- Tobias as the reason feels more honest than duty.
 
 # Rejected
```

### Unit record

```json
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
          "lines": [
            "- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job."
          ]
        },
        {
          "note": "char-mara.md",
          "under": "# Rationale",
          "lines": [
            "- Tobias as the reason feels more honest than duty."
          ]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The writer's comment routes this to char-mara, and the committed tag covers the bullet's one story sentence: her real reason for the lamp and the town's mistaken belief both stay, under Motivation and Intention. \"I really like this\" is a note-to-self and is dropped; \"Tobias as the reason feels more honest than duty\" is rationale and goes to Rationale in the writer's words."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
I migrated batch b1, round 0: 1 unit migrated, 0 left in place, 0 questions, 0 could-not entries.

**u1:** the bullet on line 10 of `brain-dump.md` carries `#status/committed`, and your comment routes it to `char-mara`. Both copies went into `char-mara.md`:
- **Under "Motivation and Intention":** "- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job." It was already a plain statement, so it went in word for word. The part about the town believing it's just her job stays in.
- **Under "Rationale":** "- Tobias as the reason feels more honest than duty." This is your wording, unchanged.
- **Dropped:** "I really like this." It says how you feel about the idea but gives no reason, so it doesn't go into the Area Note.

I made no changes to the Brain Dump doc. The Run manager adds the `migrated-to` pointer after the migration-verifier approves the copies.

The record file is `run/unit-records.json`.
```

## lost-detail-04-existing-text r1: 10 of 10 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  judge-facts-preserved   Under "## The lamp", the file keeps the source bullet word for word: "The lamp could run on something stranger than oil. Maybe it burns letters."  - **"stranger than oil"**: present, in "something stranger than oil". - **"letters"**: present, in "Maybe it burns letters." - **Hedge**: kept in both places. "could run on" hedges the first sentence and "Maybe" hedges the second, so the letters idea i
PASS  judge-nothing-added   The migrated bullet copies the source word for word: "The lamp could run on something stranger than oil. Maybe it burns letters." It adds nothing beyond that. The other bullet, "The lamp uses whale oil, which the town can no longer afford.", is the line the file already had, so it is not new content. The new bullet does not change it or link to it with any new claim, such as saying the town switc
PASS  keeps-hedge-maybe  found 'Maybe'
PASS  keeps-letters  found 'letters'
PASS  keeps-stranger-than-oil  found 'stranger than oil'
PASS  no-status-tags  no match
PASS  whale-oil-unchanged  found '- The lamp uses whale oil, which the town can no longer afford.'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-mara-lighthouse.md work/project/Ideas/idea-mara-lighthouse.md
--- before/project/Ideas/idea-mara-lighthouse.md	2026-10-13 19:39:49
+++ work/project/Ideas/idea-mara-lighthouse.md	2026-10-13 19:40:04
@@ -8,3 +8,4 @@
 ## The lamp
 
 - The lamp uses whale oil, which the town can no longer afford.
+- The lamp could run on something stranger than oil. Maybe it burns letters.
```

### Unit record

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
      "why": "The comment names idea-mara-lighthouse, and the unit is about the lamp's fuel, so it goes under The lamp next to the whale-oil line. Copied in the writer's words to keep both hedges ('could', 'Maybe'); it is an alternative to the whale-oil line, not a replacement for it."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
Batch b1, round 0: I migrated 1 unit and left nothing in place. There are no questions and nothing I couldn't do.

- **u1:** Your comment on line 12 of `brain-dump.md` asked for this, so I copied "- The lamp could run on something stranger than oil. Maybe it burns letters." (line 10) into `Ideas/idea-mara-lighthouse.md` under `## The lamp`.
  - I kept your wording exactly, so "could" and "Maybe" are still there.
  - It has no status tag, so it stays tentative by default.
  - It sits right after the whale-oil line. I didn't change that line: the new one is another possibility for the lamp, not a replacement.
- I wrote nothing in `brain-dump.md`.

The record file is at `run/unit-records.json`.
```

## lost-detail-05-dense-bullet r1: 22 of 22 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  judge-1987-hedged   Only one line mentions 1987 or the logging of ships, and it opens with "Maybe":  > "- Maybe the keeper before Mara logged every ship that didn't come back in the second logbook, 31 of them, going back to 1987."  Other lines mention the second logbook but not ship-logging or 1987. For example, "kept a second logbook nobody knew about" asserts only that the logbook exists, not what it records. No l
PASS  judge-ansel-hedged   The name appears only once, at its introduction, and the hedge comes with it: "The keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about."  Every other line about her uses a role and never the name: - "The last keeper left without telling anyone. Maybe she was pushed out." - "Maybe the keeper before Mara logged every ship that didn't come back in the second
PASS  judge-pell-hedged   Pell appears in only one line, and that line keeps the hedge:  > "I'll need to figure out who else had a key, possibly the harbourmaster, Pell."  The word "possibly" is still there, and the line frames Pell as an open question ("I'll need to figure out who else had a key"). No other line mentions Pell or states that Pell had a key.
PASS  keeps-1987  found '1987'
PASS  keeps-31-ships  found '31'
PASS  keeps-40th-step  found '40th'
PASS  keeps-ansel  found 'Ansel'
PASS  keeps-boat  found 'boat'
PASS  keeps-handwriting  found 'handwriting'
PASS  keeps-harbourmaster  found 'harbourmaster'
PASS  keeps-key  found 'key'
PASS  keeps-lamp-room  found 'lamp room'
PASS  keeps-logbook  found 'logbook'
PASS  keeps-pell  found 'Pell'
PASS  keeps-second  found 'second'
PASS  last-keeper-unchanged  found '- The last keeper left without telling anyone. Maybe she was pushed out.'
PASS  no-question-lines  no match
PASS  no-status-tags  no match
PASS  whale-oil-unchanged  found '- The lamp uses whale oil, which the town can no longer afford.'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-mara-lighthouse.md work/project/Ideas/idea-mara-lighthouse.md
--- before/project/Ideas/idea-mara-lighthouse.md	2026-10-13 19:39:49
+++ work/project/Ideas/idea-mara-lighthouse.md	2026-10-13 19:40:16
@@ -12,3 +12,7 @@
 ## The keeper before Mara
 
 - The last keeper left without telling anyone. Maybe she was pushed out.
+- The keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?
+- Maybe the keeper before Mara logged every ship that didn't come back in the second logbook, 31 of them, going back to 1987.
+- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.
+- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.
```

### Unit record

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
            "- The keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?",
            "- Maybe the keeper before Mara logged every ship that didn't come back in the second logbook, 31 of them, going back to 1987.",
            "- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.",
            "- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names idea-mara-lighthouse, and the bullet is about the keeper before Mara, so it goes under that heading. The dense bullet is split into four adjacent units (the logbook and where it's hidden, the ships it logs, who finds it, the last entry and the key), keeping every specific, hedge, and prose question; the name Ansel is hedged once where introduced and other lines use her role."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
I migrated batch b1 (round 0): one unit migrated, nothing left in place and no questions for you.

- **What moved:** The 2026-10-01 bullet about the keeper before Mara (`brain-dump.md`, line 10). Your comment on line 12 asked for it to go to `idea-mara-lighthouse`. It now sits in `Ideas/idea-mara-lighthouse.md` under "## The keeper before Mara", right after the line that was already there.
- **Split:** The bullet held several ideas, so I split it into four lines that sit together:
  1. The second logbook, and whether it's hidden in the lamp room or under the 40th step.
  2. The 31 ships that didn't come back, going back to 1987.
  3. Whether Mara or Tobias finds it, and how that changes why he took the boat out.
  4. The last entry in a different handwriting, and who else had a key: possibly the harbourmaster, Pell.
- **Wording:** Every detail, hedge and question in your wording is still there. "I'm thinking a woman named Ansel" appears once, where the keeper first comes up. The other lines call her "the keeper before Mara".
- **Status:** Tentative. The bullet had no tag and your comment didn't set a status, so it took the Brain Dump's default.
- **Not touched:** `brain-dump.md` is unchanged. The Run manager adds the `migrated-to` pointer later.

The record file is at `run/unit-records.json`.
```

## lost-detail-06-area-note-populated r1: 21 of 21 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  eleven-years-unchanged  found '- Mara has kept the lighthouse for eleven years.'
PASS  keeps-dark  found 'dark'
PASS  keeps-door  found 'door'
PASS  keeps-father  found 'father'
PASS  keeps-funeral  found 'funeral'
PASS  keeps-hook  found 'hook'
PASS  keeps-move  found 'move'
PASS  keeps-nineteen  found 'nineteen'
PASS  keeps-oilskin  found 'oilskin'
PASS  keeps-stroke  found 'stroke'
PASS  keeps-tobias  found 'Tobias'
PASS  keeps-winter  found 'winter'
PASS  no-status-tag  no match
PASS  note-to-self-dropped  no match
PASS  rationale-under-heading  found '# Rationale\n\n- A lighthouse keeper who is afraid of the sea is the whole joke of her.\n- The coat works better than a pho'
PASS  rationale-word-for-word  found 'The coat works better than a photograph because she has to walk past it every day.'
PASS  sea-joke-unchanged  found '- A lighthouse keeper who is afraid of the sea is the whole joke of her.'
PASS  tobias-drowned-unchanged  found "- Mara's younger brother Tobias drowned six years ago."
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/char-mara.md work/project/char-mara.md
--- before/project/char-mara.md	2026-10-13 19:40:14
+++ work/project/char-mara.md	2026-10-13 19:40:48
@@ -22,6 +22,9 @@
 
 - Mara has kept the lighthouse for eleven years.
 - Mara's younger brother Tobias drowned six years ago.
+- Mara took over the lighthouse at nineteen, the winter after her father's stroke.
+- Mara has never once let the lighthouse lamp go dark, not even on the night of Tobias's funeral.
+- Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it.
 
 # Psychology
 
@@ -30,5 +33,6 @@
 # Rationale
 
 - A lighthouse keeper who is afraid of the sea is the whole joke of her.
+- The coat works better than a photograph because she has to walk past it every day.
 
 # Rejected
```

### Unit record

```json
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
      "why": "The writer's committed tag covers the bullet's plain, unhedged statements, and the comment on line 12 routes it to char-mara, so it graduates as three plain statements under Bio > General with every specific kept; the coat reason goes to Rationale in the writer's words. \"I really want to keep this\" is a note-to-self with no reason, so it is dropped in the rewrite."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 12,
        "text": "%% Agent, this belongs in char-mara. %%"
      },
      "why": "Routing comment for u1. It is an instruction, not story material, so it is not copied."
    }
  ],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
Batch b1, round 0 is finished: 1 unit migrated, 1 item left in place and no questions.

- **Migrated (u1):** the committed bullet on line 10 of `brain-dump.md` went into `char-mara.md`, where your comment on line 12 sent it.
  - **Under Bio > General**, as three plain statements:
    - Mara took over the lighthouse at nineteen, the winter after her father's stroke.
    - Mara has never once let the lighthouse lamp go dark, not even on the night of Tobias's funeral.
    - Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it.
  - **Under Rationale**, in your words: "The coat works better than a photograph because she has to walk past it every day."
  - **Dropped:** "I really want to keep this." It's a note to yourself with no reason attached, and those don't go into an Area Note.
- **Judgement call:** the `#status/committed` tag is at the end of a bullet that holds several ideas. I read it as covering all of them, because none is hedged or left open. If you only meant to commit the coat, tell me and the lighthouse lines can be backed out.
- **Left in place:** the routing comment on line 12. It's an instruction, not story material.
- **Not flagged:** the new "took over at nineteen" line sits next to the existing ones ("kept the lighthouse for eleven years" and "Tobias drowned six years ago"). I didn't check those dates against each other, because checking for contradictions is the Reviewer's job.

I wrote nothing in `brain-dump.md`, and the copies match the record exactly.

Record file: `run/unit-records.json`
```

## lost-detail-07-batch-two-notes r1: 52 of 52 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  h-bullet-count  found '- '
PASS  h-keeps-1994  found '1994'
PASS  h-keeps-coyle  found 'Coyle'
PASS  h-keeps-deed  found 'deed'
PASS  h-keeps-drowned-bell  found 'Drowned Bell'
PASS  h-keeps-fridays  found 'Fridays'
PASS  h-keeps-harrow-point  found 'Harrow Point'
PASS  h-keeps-marrow-bay  found 'Marrow Bay'
PASS  h-keeps-notary  found 'notary'
PASS  h-keeps-one-road  found 'one road'
PASS  h-keeps-pell  found 'Pell'
PASS  h-keeps-sea-wall  found 'sea wall'
PASS  h-keeps-six-boats  found 'six boats'
PASS  h-keeps-spring-tide  found 'spring tide'
PASS  h-keeps-tab  found 'tab'
PASS  h-keeps-three-days  found 'three days'
PASS  h-keeps-too-cute  found 'too cute'
PASS  h-keeps-tuesdays  found 'Tuesdays'
PASS  h-keeps-twenty-two  found 'twenty-two'
PASS  h-keeps-two-winters  found 'two winters'
PASS  h-no-status-tags  no match
PASS  judge-h-bell-hedged   Only one line mentions the 1994 bell sale, and it keeps the hedge: "What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?" It opens with "What if" and ends with a question mark, so it presents the sale as a possibility, not a fact.  The other bell reference is the pub name, "There's a pub, the Drowned Bell." That line names the pub but says nothi
PASS  judge-h-ferry-hedged   Only one line states which days the ferry runs, and it keeps the hedge:  - "Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."  The only other ferry mention says nothing about the days: "the kids take the ferry to Marrow Bay, which means on bad days they just don't go." No line states the Tuesday/Friday schedule as fact.
PASS  judge-h-fleet-hedged   Only one line mentions the fleet numbers, and it keeps the hedge:  > "- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."  The opening word "Thinking" is preserved, just as in the source. No other line gives the fleet count as a fact. The other bullets are about the road, ferry, pub, church bell, school, and harbourmaster, and none of them
PASS  judge-h-no-hedge-added   None of the three flat statements picked up a hedge that wasn't in the source:  1. "The town is called Harrow Point and it has exactly one road in, which floods at spring tide." This matches the source word for word, with no hedge. 2. "The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go." This also matches the source exactly. It has
PASS  judge-h-notary-hedged   Only one line mentions Pell as notary, and it keeps the hedge:  > "- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."  The added clause "so every deed in town goes through him" follows from the hedged premise. It does not state the notary role as fact. No other line mentions Pell or a notary.
PASS  judge-s-240-hedged   There is one line that mentions the 2:40 departure, and it keeps the hedge:  - "Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."  "Maybe" is kept word for word from the source. The next sentence, "so he was cutting it close," builds on that hedged time but doesn't restate 2:40 as fact. No other line gives a departure time. The closest i
PASS  judge-s-coyle-hedged   Only one line mentions someone seeing the skiff leave, and it keeps both hedges word for word:  > "- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."  No other line names Coyle or says anyone saw the skiff. The other lines about the skiff ("Tobias took the skiff, not the trawler…", "Maybe he left at 2:40 in the morning…") describe Tobi
PASS  judge-s-generator-hedged   The generator comes up in exactly one line, and that line keeps the hedge word for word:  > "- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."  No other line mentions the generator, the Drowned Bell, or the wedding. Nothing else gives the generator as the cause of the lamp failure. The other line about the lamp ("I want the lamp to fail for 
PASS  judge-s-no-hedge-added   All four flat statements show up word-for-word with no hedge added:  1. "The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night." It is unchanged. 2. "Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock." It is unchanged. 3. "Mara was asleep in the watch room with the radio on channel 16, and she swears she heard
PASS  s-bullet-count  found '- '
PASS  s-keeps-240  found '2:40'
PASS  s-keeps-305  found '3:05'
PASS  s-keeps-channel-16  found 'channel 16'
PASS  s-keeps-coyle  found 'Coyle'
PASS  s-keeps-dock  found 'dock'
PASS  s-keeps-drowned-bell  found 'Drowned Bell'
PASS  s-keeps-eleven-minutes  found 'eleven minutes'
PASS  s-keeps-engine  found 'engine'
PASS  s-keeps-generator  found 'generator'
PASS  s-keeps-rocks  found 'rocks'
PASS  s-keeps-six-years  found 'six years'
PASS  s-keeps-skiff  found 'skiff'
PASS  s-keeps-trawler  found 'trawler'
PASS  s-keeps-two-flares  found 'two flares'
PASS  s-keeps-unfired  found 'unfired'
PASS  s-keeps-watch-room  found 'watch room'
PASS  s-keeps-wedding  found 'wedding'
PASS  s-no-status-tags  no match
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-harrow-point.md work/project/Ideas/idea-harrow-point.md
--- before/project/Ideas/idea-harrow-point.md	2026-10-13 19:40:22
+++ work/project/Ideas/idea-harrow-point.md	2026-10-13 19:41:11
@@ -4,3 +4,11 @@
 ---
 
 # Idea - Harrow Point
+
+- The town is called Harrow Point and it has exactly one road in, which floods at spring tide.
+- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days.
+- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute.
+- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow.
+- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?
+- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go.
+- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him.
diff -ru before/project/Ideas/idea-storm-night.md work/project/Ideas/idea-storm-night.md
--- before/project/Ideas/idea-storm-night.md	2026-10-13 19:40:22
+++ work/project/Ideas/idea-storm-night.md	2026-10-13 19:41:09
@@ -4,3 +4,11 @@
 ---
 
 # Idea - Storm Night
+
+- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night.
+- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock.
+- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close.
+- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing.
+- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding.
+- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet.
+- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years.
```

### Unit record

```json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\" / Agent, these go in idea-storm-night."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 24,
          "text": "- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "- The storm night: I want the lamp to fail for exactly eleven minutes, not the whole night."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the range the comment names, and the routing comment sends it to idea-storm-night. Untagged in the Brain Dump doc, so tentative; copied verbatim."
    },
    {
      "id": "u2",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\" / Agent, these go in idea-storm-night."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 25,
          "text": "- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range; the routing comment names idea-storm-night. Copied verbatim in source order."
    },
    {
      "id": "u3",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\" / Agent, these go in idea-storm-night."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 26,
          "text": "- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range; routed to idea-storm-night. Kept verbatim with its 'Maybe' hedge, directly after the Tobias line that 'he' refers to."
    },
    {
      "id": "u4",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\" / Agent, these go in idea-storm-night."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 27,
          "text": "- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range; routed to idea-storm-night. Copied verbatim."
    },
    {
      "id": "u5",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\" / Agent, these go in idea-storm-night."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 28,
          "text": "- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range; routed to idea-storm-night. Kept verbatim with its 'Possibly' hedge."
    },
    {
      "id": "u6",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\" / Agent, these go in idea-storm-night."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 29,
          "text": "- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range; routed to idea-storm-night. Copied verbatim."
    },
    {
      "id": "u7",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The storm night\" to \"I keep coming back\" / Agent, these go in idea-storm-night."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 30,
          "text": "- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-storm-night.md",
          "under": "# Idea - Storm Night",
          "lines": [
            "- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet of the commented range; routed to idea-storm-night. Copied verbatim, keeping 'maybe Coyle'."
    },
    {
      "id": "u8",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\" / Agent, these go in idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The town is called Harrow Point and it has exactly one road in, which floods at spring tide."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- The town is called Harrow Point and it has exactly one road in, which floods at spring tide."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "First bullet of the commented range; the routing comment sends it to idea-harrow-point. Untagged, so tentative; copied verbatim."
    },
    {
      "id": "u9",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\" / Agent, these go in idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range; routed to idea-harrow-point. Kept verbatim with its 'Maybe' hedge."
    },
    {
      "id": "u10",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\" / Agent, these go in idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 12,
          "text": "- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range; routed to idea-harrow-point. 'Not sure if that's too cute' is the writer's rationale and stays with the unit in an Idea Note."
    },
    {
      "id": "u11",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\" / Agent, these go in idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 13,
          "text": "- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range; routed to idea-harrow-point. Kept verbatim with its 'Thinking' and 'somehow' hedges."
    },
    {
      "id": "u12",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\" / Agent, these go in idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 14,
          "text": "- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?"
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range; routed to idea-harrow-point. Copied verbatim as a 'What if', placed after the pub line it refers to."
    },
    {
      "id": "u13",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\" / Agent, these go in idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 15,
          "text": "- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range; routed to idea-harrow-point. Copied verbatim; the consequence stays with its cause."
    },
    {
      "id": "u14",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "migrate all the bullets between \"- The town is called Harrow Point\" to \"Could be that the harbourmaster\" / Agent, these go in idea-harrow-point."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 16,
          "text": "- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet of the commented range; routed to idea-harrow-point. Kept verbatim with its 'Could be' hedge."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
I've migrated all 14 bullets in batch b1, round 0 into their two Idea Notes, as your comments asked.

- **Migrated:** 14 units.
  - Lines 24–30 of `brain-dump.md` (the 2026-09-30 entry) went into `Ideas/idea-storm-night.md`.
  - Lines 10–16 (the 2026-10-01 entry) went into `Ideas/idea-harrow-point.md`.
  - None of the bullets has a status tag, so all are tentative and the copies have no tags.
- **Wording:** I copied every bullet word for word and kept the original order, so no hedge was lost ("Maybe", "Possibly", "Could be", "maybe Coyle"). Your reason "Not sure if that's too cute" stays with the Drowned Bell line, as the rules say for an Idea Note.
- **Left in place:** 0. **Questions:** 0. **Could not do:** 0.
- **Brain Dump doc:** I wrote nothing in it. The Run manager adds the `migrated-to` pointers.

One thing to check when you read the result: the storm-night note mentions Coyle and the Drowned Bell, but who they are is only explained in the Harrow Point note. I didn't add that to the copies.

The record file is `run/unit-records.json`.
```

## lost-detail-08-merge-by-comment r1: 16 of 16 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  judge-merged-unit   The note has a single merged bullet that carries all five required facts:  - **Counterclockwise:** "Mara's lamp turns counterclockwise" - **Wrong for the coast:** "which is wrong for this coast" - **Other lights go clockwise:** "every other light from here to Marrow Bay goes clockwise" - **Mechanism from 1911:** "The mechanism is from 1911." - **Grandfather and the mirror-image drawing:** "her gr
PASS  judge-on-purpose-hedged   The hedge stays attached to "on purpose" and nowhere else. The text says: "It goes the wrong way because her grandfather installed it from a mirror-image drawing, possibly on purpose." Here "possibly" modifies only "on purpose," so the deliberateness is not stated as fact.  The other facts are still stated flatly, with no hedge: - "Mara's lamp turns counterclockwise, which is wrong for this coast
PASS  keeps-1911  found '1911'
PASS  keeps-clockwise  found 'clockwise'
PASS  keeps-coast  found 'coast'
PASS  keeps-counterclockwise  found 'counterclockwise'
PASS  keeps-grandfather  found 'grandfather'
PASS  keeps-marrow-bay  found 'Marrow Bay'
PASS  keeps-mirror  found 'mirror'
PASS  keeps-purpose  found 'purpose'
PASS  merged-two-bullets  found '- '
PASS  no-status-tags  no match
PASS  whale-oil-unchanged  found '- The lamp uses whale oil, which the town can no longer afford.'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-mara-lighthouse.md work/project/Ideas/idea-mara-lighthouse.md
--- before/project/Ideas/idea-mara-lighthouse.md	2026-10-13 19:40:30
+++ work/project/Ideas/idea-mara-lighthouse.md	2026-10-13 19:40:45
@@ -8,3 +8,4 @@
 ## The lamp
 
 - The lamp uses whale oil, which the town can no longer afford.
+- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing, possibly on purpose.
```

### Unit record

```json
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
      "why": "The comment asks for one merged unit in idea-mara-lighthouse, so it goes under the existing lamp heading there. The merged line keeps every specific from all three lines (counterclockwise, wrong for this coast, Marrow Bay, 1911, the grandfather's mirror-image drawing) and the writer's hedge 'possibly on purpose'; no source line carries a tag, so the copy stays untagged."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
I merged the three lamp lines into a single unit in `Ideas/idea-mara-lighthouse.md`, as your comment asked.

- **Migrated:** 1 unit, built from brain-dump.md lines 10–12. It sits under `## The lamp`, after the whale-oil line:
  > - Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing, possibly on purpose.

  Every detail from the three lines is in it, and "possibly on purpose" stays as you hedged it. None of the source lines had a tag, so the merged line has none either and stays tentative.
- **Left in place:** 0
- **Questions:** 0
- **Record file:** `run/unit-records.json`

I didn't touch the brain-dump lines. The Run manager adds the `migrated-to` pointers to them after the verifier approves the merge.
```

## misread-comment-11-scoped-rejection r1: 9 of 9 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  has-too-passive  found 'too passive'
PASS  judge-rejected-section   The Rejected section exists and contains only the rejected idea plus its reason:  ``` ## Rejected  - Mara is afraid of the sea. #status/rejected %% It makes her too passive. %% ```  - The rejected line "Mara is afraid of the sea." is there. - The reason "It makes her too passive." is attached as a comment. - The carve-out is not in the Rejected section. Neither "keep the seasickness" nor "that's 
PASS  judge-rejected-tag   The line about Mara being afraid of the sea is in the Rejected section and carries the tag:  > ## Rejected > > - Mara is afraid of the sea. #status/rejected  No other line has `#status/rejected`. The lines in "Mara and the sea" are all untagged: - "Mara gets seasick even on the ferry." (kept, as the writer asked) - "Tobias was afraid of the sea too, which is why he took the skiff out, to prove so
PASS  judge-seasickness-stays-live   The seasickness line is still in the live part of the note, under "## Mara and the sea" and above "## Rejected":  > - Mara gets seasick even on the ferry.  It has been reworded from "She gets seasick even on the ferry" to "Mara gets seasick even on the ferry," but the meaning is the same. The only item in the Rejected section is a different idea, "Mara is afraid of the sea. #status/rejected", so 
PASS  judge-tobias-stays-live   Tobias's fear of the sea is in the live part of the note. It appears under "## Mara and the sea", above "## Rejected":  > - Tobias was afraid of the sea too, which is why he took the skiff out, to prove something.  The Rejected section has only Mara's fear:  > - Mara is afraid of the sea. #status/rejected > %% It makes her too passive. %%  The rejection was kept to Mara's fear, and Tobias's line 
PASS  superstition-unchanged  found '- The whole town has a superstition about saying "drown" out loud.'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-mara-backstory.md work/project/Ideas/idea-mara-backstory.md
--- before/project/Ideas/idea-mara-backstory.md	2026-10-13 19:40:33
+++ work/project/Ideas/idea-mara-backstory.md	2026-10-13 19:41:01
@@ -7,7 +7,11 @@
 
 ## Mara and the sea
 
-- Mara is afraid of the sea.
-- She gets seasick even on the ferry.
+- Mara gets seasick even on the ferry.
 - Tobias was afraid of the sea too, which is why he took the skiff out, to prove something.
 - The whole town has a superstition about saying "drown" out loud.
+
+## Rejected
+
+- Mara is afraid of the sea. #status/rejected
+%% It makes her too passive. %%
```

### Unit record

```json
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
            "%% It makes her too passive. %%"
          ]
        }
      ],
      "edits": [
        {
          "note": "Ideas/idea-mara-backstory.md",
          "line": 11,
          "before": "- She gets seasick even on the ferry.",
          "after": "- Mara gets seasick even on the ferry."
        }
      ],
      "status": "rejected",
      "status_from": "comment",
      "why": "The comment rejects only Mara's fear of the sea, so that line moves to a new Rejected section at the end of the Idea Note with the writer's reason. The seasickness line is the carve-out and stays live; its 'She' now names Mara because the line it leaned on is gone. Tobias's fear of the sea is a separate proposition outside the rejection's scope and is untouched."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "Ideas/idea-mara-backstory.md",
        "line": 11,
        "text": "- She gets seasick even on the ferry."
      },
      "why": "The writer's carve-out: 'Keep the seasickness, that's physical, not fear.' It stays in the live part of the note (only its pronoun is made explicit)."
    },
    {
      "source": {
        "note": "Ideas/idea-mara-backstory.md",
        "line": 12,
        "text": "- Tobias was afraid of the sea too, which is why he took the skiff out, to prove something."
      },
      "why": "The rejection names Mara's fear only. Tobias's fear is a different proposition, so the rejection is not widened to it."
    }
  ],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
Batch b1 is done: no units were migrated, 1 was rejected, 2 lines were left in place, and I have no questions for you.

**What changed, in `Ideas/idea-mara-backstory.md`:**
- I tagged "Mara is afraid of the sea." `#status/rejected` and moved it to a new `## Rejected` section at the end of the note. Your reason sits on the line below it as `%% It makes her too passive. %%`.
- I kept the seasickness line in the live part of the note, as you asked. I changed its "She" to "Mara" so it still reads on its own now that the line before it is gone. This is the only change to your wording.
- I left "Tobias was afraid of the sea too…" alone. Your comment rejected only Mara's fear, so it doesn't extend to Tobias.

**Worth a look:** the Tobias line's "too" now points back to a rejected idea. Changing it would change what the line says, so I didn't.

Nothing in `brain-dump.md` was changed. The record file is at `run/unit-records.json`.
```

## misread-comment-12-unusual-comment r1: 9 of 9 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  has-1962  found '1962'
PASS  has-old-church  found 'old church'
PASS  has-pell  found 'Pell'
PASS  judge-correct-tags   - Harbour-wall line has no status tag: "- The harbour wall was rebuilt in 1962 with stone from the old church." - Pell line carries the tag: "- Pell's family paid for the rebuild and never let anyone forget it. #status/provisional"  The tag is on the Pell line only, so it is not on the wrong line.
PASS  no-cursed  no match
PASS  one-provisional-tag  found '#status/provisional'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-harrow-point.md work/project/Ideas/idea-harrow-point.md
--- before/project/Ideas/idea-harrow-point.md	2026-10-13 19:40:34
+++ work/project/Ideas/idea-harrow-point.md	2026-10-13 19:40:54
@@ -4,3 +4,6 @@
 ---
 
 # Idea - Harrow Point
+
+- The harbour wall was rebuilt in 1962 with stone from the old church.
+- Pell's family paid for the rebuild and never let anyone forget it. #status/provisional
```

### Unit record

```json
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
          "lines": [
            "- The harbour wall was rebuilt in 1962 with stone from the old church."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes the first bullet to idea-harrow-point. It sets no status for it, so it keeps the Brain Dump default and the copy carries no tag."
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
          "lines": [
            "- Pell's family paid for the rebuild and never let anyone forget it. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "comment",
      "why": "The comment routes the third bullet to idea-harrow-point and says it is provisional, so the copy carries #status/provisional. It sits right after the rebuild line it refers to."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 11,
        "text": "- The stone is cursed, obviously."
      },
      "why": "The writer's comment says to skip the second bullet."
    }
  ],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
I moved the first and third bullets from 2026-10-01 into the Harrow Point idea note, as your comment asked, and skipped the second.

- **Migrated: 2**
  - **First bullet (line 10)**, the harbour wall rebuilt in 1962 with church stone. Your comment gave it no status, so it has no tag and counts as tentative, like any untagged line.
  - **Third bullet (line 12)**, Pell's family paying for the rebuild. It's tagged `#status/provisional` because your comment called it provisional. I put it straight after the rebuild line because it's about that rebuild.
- **Left in place: 1.** "The stone is cursed, obviously." (line 11) stays in the brain dump only, because you said to skip it.
- **Questions: 0.**

The idea note was empty except for its title, so both lines sit under that title. Neither line was reworded, and I made no changes to the brain dump.

The unit record file is `run/unit-records.json`.
```

## misread-comment-13-ambiguous-comment r1: 8 of 8 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  judge-asks-which-bullets   Nothing was migrated: `"units": []` is empty, so no unit has a `copies` entry holding any of the four bullets. All four bullets (lines 10–13) are listed under `left_in_place`, each with the reason "the comment on line 15 doesn't say which bullets are 'the good ones'... nothing moves until the writer names the bullets."  There is an entry in `questions`, tied to the comment `"%% Agent, move the go
PASS  no-dog  no match
PASS  no-quiz  no match
PASS  no-second-lighthouse  no match
PASS  no-vicar  no match
PASS  record-check  all checks pass
```

### Note changes

```diff

```

### Unit record

```json
{
  "units": [],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- The pub quiz is rigged and has been for years."
      },
      "why": "Untagged, and the comment on line 15 doesn't say which bullets are 'the good ones'. Status can't come from the agent's own judgment of quality, so nothing moves until the writer names the bullets."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 11,
        "text": "- Coyle's dog is older than the ferry."
      },
      "why": "Untagged, and the comment on line 15 doesn't say which bullets are 'the good ones'. Status can't come from the agent's own judgment of quality, so nothing moves until the writer names the bullets."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 12,
        "text": "- There's a second lighthouse on the charts that nobody has ever found."
      },
      "why": "Untagged, and the comment on line 15 doesn't say which bullets are 'the good ones'. Status can't come from the agent's own judgment of quality, so nothing moves until the writer names the bullets."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- The vicar left in 2015 and was never replaced."
      },
      "why": "Untagged, and the comment on line 15 doesn't say which bullets are 'the good ones'. Status can't come from the agent's own judgment of quality, so nothing moves until the writer names the bullets."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 15,
        "text": "%% Agent, move the good ones to idea-harrow-point. %%"
      },
      "ask": "Which bullets under 2026-10-01 are 'the good ones'? The comment doesn't name any of them (the pub quiz, Coyle's dog, the second lighthouse, the vicar), so none were moved to idea-harrow-point."
    }
  ],
  "could_not": []
}
```

### Reply

```text
I moved nothing in batch b1. Your comment "move the good ones to idea-harrow-point" doesn't say which bullets you mean, and none of them has a status tag, so I asked instead of guessing.

- **Units migrated:** 0. I didn't write to any note.
- **Left in place:** 4, all from the 2026-10-01 entry in `brain-dump.md`:
  - the rigged pub quiz
  - Coyle's dog being older than the ferry
  - the second lighthouse nobody has found
  - the vicar who was never replaced
- **Questions:** 1. Which of those four bullets are "the good ones"? Once you name them, they can go to idea-harrow-point in the next run.
- **Record file:** `run/unit-records.json`
```

## missed-unit-17-scattered-tags r1: 22 of 22 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  left-bakery  no match
PASS  left-boats  no match
PASS  left-bus  no match
PASS  left-clock  no match
PASS  left-film  no match
PASS  left-fog  no match
PASS  left-gulls  no match
PASS  left-locks  no match
PASS  left-memorial  no match
PASS  left-phone  no match
PASS  left-queen  no match
PASS  left-smuggling  no match
PASS  migrated-ferris  found 'Ferris'
PASS  migrated-fish-market  found 'fish market'
PASS  migrated-mister-hale  found 'Mister Hale'
PASS  migrated-nine-pupils  found 'nine pupils'
PASS  migrated-twelve-metres  found 'twelve metres'
PASS  migrated-undertaker  found 'undertaker'
PASS  six-provisional-tags  found '#status/provisional'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-harrow-point.md work/project/Ideas/idea-harrow-point.md
--- before/project/Ideas/idea-harrow-point.md	2026-10-13 19:40:57
+++ work/project/Ideas/idea-harrow-point.md	2026-10-13 19:41:26
@@ -4,3 +4,10 @@
 ---
 
 # Idea - Harrow Point
+
+- The council sold the fish market roof for scrap in 2011. #status/provisional
+- The cliff path lost twelve metres to the sea last winter. #status/provisional
+- The primary school has nine pupils, all cousins. #status/provisional
+- A seal called Mister Hale comes into the harbour every October. #status/provisional
+- The post office doubles as the undertaker's. #status/provisional
+- The chemist, Ferris, fills prescriptions from memory. #status/provisional
```

### Unit record

```json
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
          "line": 30,
          "text": "- The council sold the fish market roof for scrap in 2011. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- The council sold the fish market roof for scrap in 2011. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-28; the writer's comment on line 8 routes provisional lines under these three dates to idea-harrow-point."
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
          "line": 33,
          "text": "- The cliff path lost twelve metres to the sea last winter. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- The cliff path lost twelve metres to the sea last winter. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-28; the writer's comment on line 8 routes provisional lines under these three dates to idea-harrow-point."
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
          "line": 22,
          "text": "- The primary school has nine pupils, all cousins. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- The primary school has nine pupils, all cousins. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-30; the writer's comment on line 8 routes provisional lines under these three dates to idea-harrow-point."
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
          "line": 25,
          "text": "- A seal called Mister Hale comes into the harbour every October. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- A seal called Mister Hale comes into the harbour every October. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-09-30; the writer's comment on line 8 routes provisional lines under these three dates to idea-harrow-point."
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
          "line": 13,
          "text": "- The post office doubles as the undertaker's. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- The post office doubles as the undertaker's. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-10-01; the writer's comment on line 8 routes provisional lines under these three dates to idea-harrow-point."
    },
    {
      "id": "u6",
      "action": "migrate",
      "trigger": {
        "kind": "tag",
        "text": "#status/provisional"
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 16,
          "text": "- The chemist, Ferris, fills prescriptions from memory. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "# Idea - Harrow Point",
          "lines": [
            "- The chemist, Ferris, fills prescriptions from memory. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Tagged provisional under 2026-10-01; the writer's comment on line 8 routes provisional lines under these three dates to idea-harrow-point."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 8,
        "text": "%% Agent, anything I tag provisional under these three dates goes in idea-harrow-point. Leave the untagged lines where they are. %%"
      },
      "why": "This is the writer's routing instruction, not story material. It was followed for u1 to u6, and the untagged lines under the three dates were left in place as it asks."
    }
  ],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
I copied all six lines you tagged provisional into the Harrow Point idea note, which was empty before. None were left out and I have no questions.

- **Moved:** six lines, two from each date. They are the fish market roof and the cliff path (28 Sept), the primary school and Mister Hale the seal (30 Sept), and the post office/undertaker's and Ferris the chemist (1 Oct). Each copy keeps your exact words and its `#status/provisional` tag. They're listed under the note's title with no subheadings, oldest date first.
- **Left in place:** one item, your routing comment at the top of the brain dump. It's an instruction to me rather than story material. As it asked, the untagged lines under those three dates stay where they are, and I changed nothing in the brain dump.

The record of these moves is at `run/unit-records.json`.
```

## over-promotion-09-confident-wording r1: 21 of 21 checks

### Grades

```text
PASS  area-note-eleven-years  found '- Mara has kept the lighthouse for eleven years.'
PASS  area-note-no-care-home  no match
PASS  area-note-no-sailor  no match
PASS  area-note-no-seasick  no match
PASS  area-note-no-swim  no match
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  judge-status-and-nesting   **1. The three confident lines carry no status tag.** - "This is locked: Mara never learned to swim." has no tag. - "100% canon, Tobias was the better sailor of the two." has no tag. - "Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her." has no tag.  None of the three contains a `#status/` tag.  **2. The two provisional lines each carry `#status/pr
PASS  keeps-care-home  found 'care home'
PASS  keeps-family  found 'stays in the family'
PASS  keeps-ferry  found 'ferry'
PASS  keeps-flat-day  found 'flat day'
PASS  keeps-marrow-bay  found 'Marrow Bay'
PASS  keeps-recognise  found 'recognise'
PASS  keeps-sailor  found 'sailor'
PASS  keeps-seasick  found 'seasick'
PASS  keeps-swim  found 'swim'
PASS  keeps-town-know  found 'town know'
PASS  no-committed-tag  no match
PASS  question-kept  found '- [?] Does the town know'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-mara-backstory.md work/project/Ideas/idea-mara-backstory.md
--- before/project/Ideas/idea-mara-backstory.md	2026-10-13 19:41:01
+++ work/project/Ideas/idea-mara-backstory.md	2026-10-13 19:41:38
@@ -4,3 +4,11 @@
 ---
 
 # Idea - Mara Backstory
+
+- This is locked: Mara never learned to swim.
+- 100% canon, Tobias was the better sailor of the two.
+- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her.
+- The lighthouse stays in the family, that's decided. #status/provisional
+- Mara gets seasick, badly. #status/provisional
+    - It happens even on the ferry, on a flat day.
+    - [?] Does the town know, or does she hide it?
```

### Unit record

```json
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
          "lines": [
            "- This is locked: Mara never learned to swim."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The line-18 comment scopes this bullet for migration and the line-20 comment routes it to idea-mara-backstory. It has no tag, so it stays tentative and goes to the Idea Note, not char-mara. \"This is locked\" is prose, and prose doesn't set status, so the words are kept as written."
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
          "lines": [
            "- 100% canon, Tobias was the better sailor of the two."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "This bullet is in the comment's range and the routing comment sends it to idea-mara-backstory. It has no tag, so \"100% canon\" doesn't commit it. It stays tentative with its wording unchanged."
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
          "lines": [
            "- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "This bullet is in the comment's range and goes to idea-mara-backstory as the routing comment says. It has no tag, so \"Final answer\" doesn't commit it. It stays tentative with its wording unchanged."
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
          "lines": [
            "- The lighthouse stays in the family, that's decided. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The writer's provisional tag sets the status even though the line says \"that's decided\". Provisional material goes to an Idea Note, and the routing comment names idea-mara-backstory."
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
      "why": "The parent's provisional tag makes it a migration trigger, and the routing comment sends it to idea-mara-backstory. Its nested child takes the parent's tag, and its Question moves with it, nested under the same line."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
I moved all five units from batch b1 into `Ideas/idea-mara-backstory.md`. I left nothing in place and have no questions for the writer.

- **Lines 10–12** ("This is locked…", "100% canon…", "Final answer on the father…"): your comment on line 18 picks out these bullets and the comment on line 20 sends them to idea-mara-backstory. None of them has a tag, so they stay tentative and their copies carry no tag. Words like "locked", "canon" and "final answer" don't make a line committed, so none of them went to `char-mara.md`. I kept the wording as you wrote it.
- **Line 13** (the lighthouse): it's tagged `#status/provisional`, and the tag wins over "that's decided." It stays provisional and went to the same idea note.
- **Line 14** (seasickness): it's provisional too. The nested ferry line takes its tag, and the `[?]` question stays nested under it in the idea note.

I didn't change anything in `brain-dump.md`.

Record file: `run/unit-records.json`
```

## over-promotion-10-partial-graduation r1: 10 of 10 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  eleven-years-unchanged  found '- Mara has kept the lighthouse for eleven years.'
PASS  has-only-keeper  found 'only keeper'
PASS  judge-asks-about-others   **The two left-out ideas are absent from `copies`.** The only copied lines are: - "- Mara is the only keeper the light has had since her father." - "    - [?] Did her father train her, or did she teach herself?"  Neither the second-keeper idea nor the hotel-chain idea appears there.  **`left_in_place` records both ideas as left behind:** - "\"A second keeper arriving from the mainland could be us
PASS  no-hotel  no match
PASS  no-second-keeper  no match
PASS  no-status-tag  no match
PASS  question-kept  found '- [?] Did her father train her, or did she teach herself'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/char-mara.md work/project/char-mara.md
--- before/project/char-mara.md	2026-10-13 19:41:13
+++ work/project/char-mara.md	2026-10-13 19:41:39
@@ -17,6 +17,8 @@
 ## General
 
 - Mara has kept the lighthouse for eleven years.
+- Mara is the only keeper the light has had since her father.
+    - [?] Did her father train her, or did she teach herself?
 
 # Psychology
```

### Unit record

```json
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
      "why": "The trailing committed tag clearly covers only the first idea, a plain statement of fact; the other two sentences are hedged possibilities ('could be useful', 'feels promising') and stay at the source (migrator-rules 04.2, 04.5). The comment routes it to char-mara, and the writer's nested Question about her father moves with it as Work under the line it belongs to."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "why": "\"A second keeper arriving from the mainland could be useful for conflict.\" is a separate idea the trailing committed tag does not clearly cover. It stays tentative at the source, so it stays out of the char-mara Area Note."
    },
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "why": "\"The lighthouse being sold to a hotel chain feels promising.\" is a separate idea the trailing committed tag does not clearly cover. It stays tentative at the source, so it stays out of the char-mara Area Note."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- Mara is the only keeper the light has had since her father. A second keeper arriving from the mainland could be useful for conflict. The lighthouse being sold to a hotel chain feels promising. #status/committed"
      },
      "ask": "The committed tag sits at the end of a bullet with three ideas. I graduated only \"Mara is the only keeper the light has had since her father\" into char-mara. Do you mean to commit the second keeper from the mainland and the hotel-chain sale too, or should they stay tentative (and perhaps go to an Idea Note)?"
    }
  ],
  "could_not": []
}
```

### Reply

```text
Batch b1 is done: 1 unit migrated, 2 ideas left in place and 1 question for you. The record is at `run/unit-records.json`.

**Migrated (u1).** The committed tag on line 10 sits at the end of a bullet that holds three ideas, and it clearly covers only the first one. Following your comment, I moved that one idea into `char-mara.md` under `## General`, as a plain statement:
- `- Mara is the only keeper the light has had since her father.`
- `    - [?] Did her father train her, or did she teach herself?`

**Check the Question line.** I brought it along from line 11 of `brain-dump.md`, though the batch only listed lines 10 and 13. Per the rules, a Question moves with the idea it belongs to. If line 11 wasn't meant to be in this batch, that copy and its record entry should come out.

**Left in place (2).** These ideas from line 10 stay in the Brain Dump as tentative ideas, outside the character note for Mara:
- "A second keeper arriving from the mainland could be useful for conflict."
- "The lighthouse being sold to a hotel chain feels promising."

**Question (1):** Did you mean the committed tag and the "belongs in char-mara" comment to cover the second keeper and the hotel-chain sale too? Or should those stay tentative, possibly in an Idea Note?

I wrote nothing in `brain-dump.md`.
```

## tentative-in-area-note-16-tagged-child r1: 10 of 10 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  eleven-years-unchanged  found '- Mara has kept the lighthouse for eleven years.'
PASS  gaps-in-idea-note  found 'gaps'
PASS  judge-gaps-provisional   The line about leaving gaps keeps its provisional tag: "- Mara has started leaving gaps in her logbook of passing ships on purpose. #status/provisional"  The wording was expanded from the source ("She has started leaving gaps in it on purpose" became "Mara has started leaving gaps in her logbook of passing ships on purpose"). The check only asks about the tag, so this doesn't affect the result.
PASS  logbook-in-area-note  found 'logbook'
PASS  no-gaps-in-area-note  no match
PASS  no-status-tag-in-area-note  no match
PASS  pencil-in-area-note  found 'pencil'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-mara-habits.md work/project/Ideas/idea-mara-habits.md
--- before/project/Ideas/idea-mara-habits.md	2026-10-13 19:41:20
+++ work/project/Ideas/idea-mara-habits.md	2026-10-13 19:41:47
@@ -4,3 +4,5 @@
 ---
 
 # Idea - Mara Habits
+
+- Mara has started leaving gaps in her logbook of passing ships on purpose. #status/provisional
diff -ru before/project/char-mara.md work/project/char-mara.md
--- before/project/char-mara.md	2026-10-13 19:41:20
+++ work/project/char-mara.md	2026-10-13 19:41:45
@@ -17,6 +17,8 @@
 ## General
 
 - Mara has kept the lighthouse for eleven years.
+- Mara keeps a logbook of every ship that passes.
+    - Mara writes her logbook in pencil, never ink.
 
 # Psychology
```

### Unit record

```json
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
          "lines": [
            "- Mara keeps a logbook of every ship that passes."
          ]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "tag",
      "why": "The writer tagged it committed and the comment routes the committed material to char-mara. It is a biographical habit, so it goes under Bio > General, with no status tag in the Area Note."
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
          "lines": [
            "    - Mara writes her logbook in pencil, never ink."
          ]
        }
      ],
      "edits": [],
      "status": "committed",
      "status_from": "parent tag",
      "why": "The untagged child inherits #status/committed from its parent bullet, so it is committed material the comment routes to char-mara. It is nested under the logbook line and names Mara and the logbook so it reads on its own."
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
          "lines": [
            "- Mara has started leaving gaps in her logbook of passing ships on purpose. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "Its own provisional tag overrides the committed parent, so it stays out of the Area Note; the comment routes it to idea-mara-habits. Reworded only to name Mara and the logbook so it reads without its parent."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
I migrated batch b1 (round 0): 3 units moved, nothing left in place, no questions, nothing I couldn't do. I wrote the record before touching any note, and the copies match it exactly.

- **u1, committed:** "Mara keeps a logbook of every ship that passes." went to `char-mara.md` under `## General`. It's a plain statement with no status tag, since a character note holds only committed material.
- **u2, committed because of its parent's tag:** "Mara writes her logbook in pencil, never ink." went to `char-mara.md`, nested under u1. I added Mara's name and the logbook so it reads on its own.
- **u3, provisional:** "Mara has started leaving gaps in her logbook of passing ships on purpose. #status/provisional" went to `Ideas/idea-mara-habits.md`. Its own provisional tag takes priority over the committed parent above it, so it stays out of the character note. I only reworded it to name Mara and the logbook.

**Decision for you:** u2 comes from line 11 ("She writes it in pencil, never ink."), which wasn't in the batch's list of changed lines. I included it because it has no tag of its own, sits under the committed bullet, and so counts as committed. Your comment sends all committed material to char-mara. If you didn't mean the pencil detail to go in, it's one line to drop from `char-mara.md` and from the record.

Record file: `run/unit-records.json`
```

## unasked-edit-18-typos-and-contradiction r1: 8 of 8 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  has-2019  found '2019'
PASS  has-key  found 'key'
PASS  no-status-tags  no match
PASS  tide-tables-unchanged  found '- Pell keeps the tide tables locked up.'
PASS  typo-line-unchanged  found '- The harbor masters office has no windows facing the see.'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-harrow-point.md work/project/Ideas/idea-harrow-point.md
--- before/project/Ideas/idea-harrow-point.md	2026-10-13 19:41:30
+++ work/project/Ideas/idea-harrow-point.md	2026-10-13 19:41:48
@@ -9,3 +9,4 @@
 
 - The harbor masters office has no windows facing the see.
 - Pell keeps the tide tables locked up.
+- Pell dosnt lock the tide tables anymore, he lost the key in 2019.
```

### Unit record

```json
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
          "lines": [
            "- Pell dosnt lock the tide tables anymore, he lost the key in 2019."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names idea-harrow-point. It goes under The harbour office, next to the other line about Pell and the tide tables. The two lines are tentative alternatives, so neither is flagged nor changed, and the writer's spelling is kept."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
Batch b1 is done: one unit migrated, nothing left in place, no questions.

- **What moved:** Your comment asked for the Pell bullet (`brain-dump.md`, line 10) to go to idea-harrow-point. I copied it to `Ideas/idea-harrow-point.md` under "The harbour office", right after the line saying Pell keeps the tide tables locked up.
- **Status:** It has no tag, so it stays tentative and the copy carries no tag.
- **Wording:** I copied the line exactly as you wrote it, "dosnt" included.
- **Left alone:**
  - The new line contradicts the one above it about the tables being locked. Both are tentative, so I treated them as alternatives you're exploring and didn't flag it.
  - I didn't fix the typos in that note's existing lines ("harbor masters", "see"), because nothing asked me to. Add a comment if you want them fixed.
  - I wrote nothing in the Brain Dump. The Run manager adds the `migrated-to` pointer later.

Record file: `run/unit-records.json`
```

## unasked-migration-14-outside-range r1: 18 of 18 checks

### Grades

```text
PASS  area-note-eleven-years  found '- Mara has kept the lighthouse for eleven years.'
PASS  area-note-no-hums  no match
PASS  area-note-no-lifeboat  no match
PASS  area-note-no-whisky  no match
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  has-clocks  found 'clocks'
PASS  has-pell  found 'Pell'
PASS  has-predates  found 'predates'
PASS  has-tide-bell  found 'tide bell'
PASS  has-two-metres  found 'two metres'
PASS  no-hums  no match
PASS  no-lifeboat  no match
PASS  no-slipway  no match
PASS  no-status-tags  no match
PASS  no-timetable  no match
PASS  no-whisky  no match
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-harrow-point.md work/project/Ideas/idea-harrow-point.md
--- before/project/Ideas/idea-harrow-point.md	2026-10-13 19:41:48
+++ work/project/Ideas/idea-harrow-point.md	2026-10-13 19:42:20
@@ -4,3 +4,7 @@
 ---
 
 # Idea - Harrow Point
+
+- The harbour has a tide bell that rings itself when the swell is over two metres.
+- Nobody in town will say who installed the tide bell. Pell claims it predates the lighthouse.
+- People set their clocks by the tide bell even though it's never on time.
```

### Unit record

```json
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
          "lines": [
            "- The harbour has a tide bell that rings itself when the swell is over two metres."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "First bullet of the range the line 15 comment names; the line 17 comment routes it to idea-harrow-point. Untagged, so it stays tentative."
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
          "lines": [
            "- Nobody in town will say who installed the tide bell. Pell claims it predates the lighthouse."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Inside the commented range, routed to idea-harrow-point by the line 17 comment. \"it\" becomes \"the tide bell\" so the line reads on its own."
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
          "lines": [
            "- People set their clocks by the tide bell even though it's never on time."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "Last bullet of the commented range, routed to idea-harrow-point by the line 17 comment. \"it\" becomes \"the tide bell\" so the line reads on its own."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "why": "Outside the range the line 15 comment names, which ends at \"People set their clocks\". The bullet's own \"should live with the town stuff too\" is prose, not a comment or tag, so it does not trigger migration."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 13,
        "text": "- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."
      },
      "ask": "This bullet sits just past the migration range, but its prose says it should live with the town material. Do you want it migrated to idea-harrow-point too? If so, add a comment or tag to it."
    }
  ],
  "could_not": []
}
```

### Reply

```text
Batch b1, round 0 is finished: 3 units migrated, 1 bullet left in place, 1 question for the writer.

- **Migrated:** The three bullets in the range on lines 10–12 of `brain-dump.md` (the tide bell, who installed it, people setting their clocks by it) now sit under `# Idea - Harrow Point` in `Ideas/idea-harrow-point.md`. The comment on line 17 sent them there. None of them was tagged, so they stay tentative. On lines 11 and 12 I changed "it" to "the tide bell" so each line makes sense by itself.
- **Left in place:** The ferry-timetable bullet on line 13 comes after the range ends at "People set their clocks". It does say "This one should live with the town stuff too", but that's ordinary writing, not a comment or tag, so it doesn't count as an instruction to migrate.
- **Question:** I asked the writer whether line 13 should go to idea-harrow-point too. If so, they need to add a comment or tag to it.

Nothing was written in the Brain Dump doc.

Record file: `run/unit-records.json`
```

## unit-record-15-split-and-merge r1: 13 of 13 checks

### Grades

```text
PASS  bell-in-harrow-point  found 'bell by hand at dusk'
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  harrow-coyle-unchanged  found '- Coyle runs the Drowned Bell.'
PASS  harrow-ferry-unchanged  found '- The ferry runs twice a week.'
PASS  judge-cat-merged   Under the "## Ballast" heading, both source bullets became one bullet:  > "- The lighthouse cat is Mara's cat, Ballast. Ballast has one eye and sleeps in the lamp room."  That bullet has all three required facts: - **Name:** "Mara's cat, Ballast" - **One eye:** "Ballast has one eye" - **Lamp room:** "sleeps in the lamp room"  No other bullet in the file mentions the cat, so nothing is split acros
PASS  judge-unit-record   1. **Bell bullet (u1):** It is one unit with exactly one source:    > `"line": 10, "text": "- Pell rings the harbour bell by hand at dusk. He learned it from Tobias, who used to do it for pocket money."`     It has two copies, one per note:    > `"note": "Ideas/idea-harrow-point.md"` … `"- Pell rings the harbour bell by hand at dusk."`     > `"note": "Ideas/idea-tobias.md"` … `"- Tobias used to r
PASS  lighthouse-last-keeper-unchanged  found '- The last keeper left without telling anyone. Maybe she was pushed out.'
PASS  lighthouse-whale-oil-unchanged  found '- The lamp uses whale oil, which the town can no longer afford.'
PASS  paraffin-provisional  found 'paraffin and wet wool. #status/provisional'
PASS  tobias-in-tobias-note  found 'Tobias'
PASS  tobias-pocket-money  found 'pocket money'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-harrow-point.md work/project/Ideas/idea-harrow-point.md
--- before/project/Ideas/idea-harrow-point.md	2026-10-13 19:41:49
+++ work/project/Ideas/idea-harrow-point.md	2026-10-13 19:42:18
@@ -8,6 +8,7 @@
 ## People
 
 - Coyle runs the Drowned Bell.
+- Pell rings the harbour bell by hand at dusk.
 
 ## Getting in and out
 
diff -ru before/project/Ideas/idea-mara-lighthouse.md work/project/Ideas/idea-mara-lighthouse.md
--- before/project/Ideas/idea-mara-lighthouse.md	2026-10-13 19:41:49
+++ work/project/Ideas/idea-mara-lighthouse.md	2026-10-13 19:42:23
@@ -8,7 +8,12 @@
 ## The lamp
 
 - The lamp uses whale oil, which the town can no longer afford.
+- The lamp room smells of paraffin and wet wool. #status/provisional
 
 ## The keeper before Mara
 
 - The last keeper left without telling anyone. Maybe she was pushed out.
+
+## Ballast
+
+- The lighthouse cat is Mara's cat, Ballast. Ballast has one eye and sleeps in the lamp room.
diff -ru before/project/Ideas/idea-tobias.md work/project/Ideas/idea-tobias.md
--- before/project/Ideas/idea-tobias.md	2026-10-13 19:41:49
+++ work/project/Ideas/idea-tobias.md	2026-10-13 19:42:20
@@ -4,3 +4,5 @@
 ---
 
 # Idea - Tobias
+
+- Tobias used to ring the harbour bell by hand for pocket money. Pell learned it from him.
```

### Unit record

```json
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
          "lines": [
            "- Pell rings the harbour bell by hand at dusk."
          ]
        },
        {
          "note": "Ideas/idea-tobias.md",
          "under": "# Idea - Tobias",
          "lines": [
            "- Tobias used to ring the harbour bell by hand for pocket money. Pell learned it from him."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment names both notes. Pell's bell ringing sits with the town's people in idea-harrow-point; the Tobias copy names the bell and Pell so it reads on its own."
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
      "why": "The comment asks for one merged unit in idea-mara-lighthouse. No existing heading fits the cat, so it gets its own heading."
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
          "lines": [
            "- The lamp room smells of paraffin and wet wool. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The comment routes it to idea-mara-lighthouse, and the writer's provisional tag goes with it. It sits under The lamp, with the other lamp material."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
Batch b1 is migrated. I wrote the record file first, then the copies, and both say the same thing.

**Totals:** 3 units migrated, 0 left in place, 0 questions, nothing I couldn't do.

- **u1, split:** the bell line (brain-dump.md line 10) went to two notes, as your comment said. "Pell rings the harbour bell by hand at dusk." is under People in idea-harrow-point. The Tobias part went into idea-tobias, reworded so it makes sense by itself: "Tobias used to ring the harbour bell by hand for pocket money. Pell learned it from him." Both are tentative, since the source line has no tag.
- **u2, merge:** I combined the two Ballast lines (14 and 15) into one, as you asked: "The lighthouse cat is Mara's cat, Ballast. Ballast has one eye and sleeps in the lamp room." No existing heading in idea-mara-lighthouse fit, so I added a new "Ballast" heading at the end of that note. It's tentative.
- **u3:** the paraffin line (19) went to idea-mara-lighthouse under "The lamp" and keeps your `#status/provisional` tag.

I didn't write anything in brain-dump.md. The `migrated-to` links back to the source lines get added later in the run.

Record file: `run/unit-records.json`
```

## wrong-destination-19-no-destination-named r1: 21 of 21 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  captain-13th-in-harrow  found '13th'
PASS  captain-odd-in-harrow  found 'Odd'
PASS  coyle-pub-in-storm  found 'closed the pub'
PASS  foghorn-in-storm  found 'foghorn'
PASS  harrow-coyle-unchanged  found '- Coyle runs the Drowned Bell.'
PASS  harrow-ferry-unchanged  found '- The ferry runs twice a week.'
PASS  judge-lens-under-lamp   The lens line sits under the "The lamp" heading, as the second bullet after "- The lamp uses whale oil, which the town can no longer afford." The text reads "- The lamp's lens was cracked by a gull in 2003. #status/provisional". This comes before the "## The keeper before Mara" heading, which starts the next section.
PASS  lens-2003-in-lighthouse  found '2003'
PASS  lens-gull-in-lighthouse  found 'gull'
PASS  lighthouse-last-keeper-unchanged  found '- The last keeper left without telling anyone. Maybe she was pushed out.'
PASS  lighthouse-whale-oil-unchanged  found '- The lamp uses whale oil, which the town can no longer afford.'
PASS  no-13th-in-lighthouse  no match
PASS  no-13th-in-storm  no match
PASS  no-foghorn-in-harrow  no match
PASS  no-foghorn-in-lighthouse  no match
PASS  no-gull-in-harrow  no match
PASS  no-gull-in-storm  no match
PASS  storm-lamp-failed-unchanged  found '- The lamp failed for eleven minutes.'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-harrow-point.md work/project/Ideas/idea-harrow-point.md
--- before/project/Ideas/idea-harrow-point.md	2026-10-13 19:41:50
+++ work/project/Ideas/idea-harrow-point.md	2026-10-13 19:42:15
@@ -12,3 +12,4 @@
 ## Getting in and out
 
 - The ferry runs twice a week.
+- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional
diff -ru before/project/Ideas/idea-mara-lighthouse.md work/project/Ideas/idea-mara-lighthouse.md
--- before/project/Ideas/idea-mara-lighthouse.md	2026-10-13 19:41:50
+++ work/project/Ideas/idea-mara-lighthouse.md	2026-10-13 19:42:18
@@ -8,6 +8,7 @@
 ## The lamp
 
 - The lamp uses whale oil, which the town can no longer afford.
+- The lamp's lens was cracked by a gull in 2003. #status/provisional
 
 ## The keeper before Mara
 
diff -ru before/project/Ideas/idea-storm-night.md work/project/Ideas/idea-storm-night.md
--- before/project/Ideas/idea-storm-night.md	2026-10-13 19:41:50
+++ work/project/Ideas/idea-storm-night.md	2026-10-13 19:42:16
@@ -8,3 +8,11 @@
 ## The lamp failure
 
 - The lamp failed for eleven minutes.
+
+## The foghorn
+
+- On the storm night the foghorn was already broken. #status/provisional
+
+## The town that night
+
+- On the storm night, Coyle closed the pub early, which he never does. #status/provisional
```

### Unit record

```json
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
          "lines": [
            "- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. The ferry captain belongs with the ferry line under Getting in and out in the Harrow Point Idea Note."
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
          "under": "## The lamp failure",
          "lines": [
            "## The foghorn",
            "- On the storm night the foghorn was already broken. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. It is about the storm night, so it goes in the Storm Night Idea Note under a new foghorn heading, since it is not about the lamp."
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
          "lines": [
            "- The lamp's lens was cracked by a gull in 2003. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. It is a fact about the lighthouse lamp's history, not the storm night, so it joins The lamp in the Mara Lighthouse Idea Note."
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
          "under": "## The foghorn",
          "lines": [
            "## The town that night",
            "- On the storm night, Coyle closed the pub early, which he never does. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "No destination was named. \"That night\" is the storm night from the line above, so it goes in the Storm Night Idea Note, reworded to name the storm night so it reads on its own."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
I've migrated all four tagged lines from batch b1 (round 0) into existing Idea Notes. None were left in place, there are no questions and nothing failed. The record is at `run/unit-records.json`.

You didn't name any destinations, so I chose each one from what the line is about:

| Unit | Source line | Where it went | Status |
| --- | --- | --- | --- |
| u1 | line 10, ferry captain Odd | `Ideas/idea-harrow-point.md`, under "Getting in and out", next to the line about the ferry | provisional |
| u2 | line 11, broken foghorn | `Ideas/idea-storm-night.md`, under a new heading "## The foghorn" | provisional |
| u3 | line 12, lens cracked in 2003 | `Ideas/idea-mara-lighthouse.md`, under "The lamp" | provisional |
| u4 | line 13, Coyle closing the pub | `Ideas/idea-storm-night.md`, under a new heading "## The town that night" | provisional |

- **u3:** I put the cracked lens with the lighthouse lamp rather than the storm night, because it happened in 2003, not that night.
- **u4:** I read "that night" as the storm night from the line above. I reworded the copy so it reads on its own: "On the storm night, Coyle closed the pub early, which he never does." If you meant a different night, that wording is wrong.

Each copy keeps your `#status/provisional` tag. The two new headings are in the record, and I didn't change `brain-dump.md`.
```

## wrong-destination-20-placement-from-context r1: 9 of 9 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  ferry-horn-in-harrow  found 'half-step apart'
PASS  judge-no-question-about-horn   The `questions` array is empty: `"questions": []`. No entry asks where the ferry horn / fog signal line belongs.  The agent placed the line itself instead of asking. Unit u2 copies "- The ferry horn and the fog signal sit a half-step apart, so on foggy mornings nobody can tell which is which. #status/provisional" into `"Ideas/idea-harrow-point.md"` under `"## Getting in and out"`. Its reason is: 
PASS  no-ferry-horn-in-lighthouse  no match
PASS  no-ferry-horn-in-storm  no match
PASS  no-ferry-horn-question  no match
PASS  wound-by-hand-in-lighthouse  found 'wound by hand'
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-harrow-point.md work/project/Ideas/idea-harrow-point.md
--- before/project/Ideas/idea-harrow-point.md	2026-10-13 19:41:53
+++ work/project/Ideas/idea-harrow-point.md	2026-10-13 19:42:18
@@ -12,3 +12,5 @@
 ## Getting in and out
 
 - The ferry runs twice a week.
+- Harrow Point is the last stop on the ferry line, and fog sits on it most mornings. #status/provisional
+- The ferry horn and the fog signal sit a half-step apart, so on foggy mornings nobody can tell which is which. #status/provisional
diff -ru before/project/Ideas/idea-lighthouse.md work/project/Ideas/idea-lighthouse.md
--- before/project/Ideas/idea-lighthouse.md	2026-10-13 19:41:53
+++ work/project/Ideas/idea-lighthouse.md	2026-10-13 19:42:20
@@ -8,6 +8,7 @@
 ## The lamp
 
 - The lamp uses whale oil, which the town can no longer afford.
+- The lamp has to be wound by hand every four hours. #status/provisional
 
 ## The keeper before Mara
```

### Unit record

```json
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
          "text": "- Harrow Point is the last stop on the ferry line, and fog sits on it most mornings. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## Getting in and out",
          "lines": [
            "- Harrow Point is the last stop on the ferry line, and fog sits on it most mornings. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "The line is about Harrow Point and how the ferry reaches it, so it joins the existing ferry line under Getting in and out in the Harrow Point Idea Note."
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
          "text": "- The ferry horn and the fog signal sit a half-step apart, so on foggy mornings nobody can tell which is which. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-harrow-point.md",
          "under": "## Getting in and out",
          "lines": [
            "- The ferry horn and the fog signal sit a half-step apart, so on foggy mornings nobody can tell which is which. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "It continues the ferry-and-fog thought from u1 about Harrow Point's mornings, so it sits directly after u1 under Getting in and out."
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
          "text": "- The lamp has to be wound by hand every four hours. #status/provisional"
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-lighthouse.md",
          "under": "## The lamp",
          "lines": [
            "- The lamp has to be wound by hand every four hours. #status/provisional"
          ]
        }
      ],
      "edits": [],
      "status": "provisional",
      "status_from": "tag",
      "why": "It is a standing fact about how the lighthouse lamp works, so it goes under The lamp in the Lighthouse Idea Note rather than the Storm Night note, which is about one event."
    }
  ],
  "left_in_place": [],
  "questions": [],
  "could_not": []
}
```

### Reply

```text
Batch b1, round 0, is finished: I moved all 3 lines into existing Idea Notes, word for word, and each copy keeps its `#status/provisional` tag. Nothing was left in place and I have no questions for you.

- **u1:** Line 10 ("Harrow Point is the last stop on the ferry line, and fog sits on it most mornings") went to `Ideas/idea-harrow-point.md` under "## Getting in and out". It sits next to the existing line about the ferry running twice a week.
- **u2:** Line 11 (the ferry horn and the fog signal being a half-step apart) went to the same note and heading, directly after u1, because it carries on the ferry-and-fog thought. Since it mentions the fog signal, it could also belong in the Lighthouse note, but I put it in one place only.
- **u3:** Line 12 ("The lamp has to be wound by hand every four hours") went to `Ideas/idea-lighthouse.md` under "## The lamp". It's a standing fact about how the lamp works, so it doesn't belong in `idea-storm-night.md`, which is about one event.

I didn't create any new notes and didn't change anything in `brain-dump.md`. The record is at `run/unit-records.json`.
```

## Case 21, run after the writer approved its Pass line

Run on 2026-10-13, right after the twenty, set up the same way. Pass line approved by the writer on 2026-10-13. 6 of 6 checks; the Pass line holds: the spare-key line was copied once, the green-ink line, whose pointer already names idea-lighthouse, was not copied again, and the record lists it in `left_in_place`. Cost: $0.30, judge included.

### retry-21-no-second-copy r1: 6 of 6 checks

#### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  judge-no-green-ink-copy-in-record   There is a single `copies` entry across all units, in u1, and its only line concerns the spare key: `"lines": ["- Mara finds the last keeper's spare key taped under the third stair from the top."]`  The fog/green-ink bullet shows up only where the check allows it: - In `left_in_place`: `"text": "- The last keeper logged 38 nights of fog in her final winter, every one in green ink. [migrated-to:: 
PASS  no-second-green-ink-copy  no match
PASS  spare-key-in-lighthouse  found 'third stair'
PASS  record-check  all checks pass
```

#### Note changes

```diff
diff -ru before/project/Ideas/idea-lighthouse.md work/project/Ideas/idea-lighthouse.md
--- before/project/Ideas/idea-lighthouse.md	2026-10-13 20:08:11
+++ work/project/Ideas/idea-lighthouse.md	2026-10-13 20:08:28
@@ -13,3 +13,4 @@
 
 - The last keeper left without telling anyone. Maybe she was pushed out.
 - The last keeper logged 38 nights of fog in her final winter, every one in green ink.
+- Mara finds the last keeper's spare key taped under the third stair from the top.
```

#### Unit record

```json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "Agent, both of these belong in idea-lighthouse."
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 11,
          "text": "- Mara finds the last keeper's spare key taped under the third stair from the top."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-lighthouse.md",
          "under": "## The keeper before Mara",
          "lines": [
            "- Mara finds the last keeper's spare key taped under the third stair from the top."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The comment routes both bullets to idea-lighthouse. This one is about the last keeper's key, so it goes under the keeper heading, next to the green-ink log line."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 10,
        "text": "- The last keeper logged 38 nights of fog in her final winter, every one in green ink. [migrated-to:: [[Projects/project/Ideas/idea-lighthouse|idea-lighthouse]]]"
      },
      "why": "Its migrated-to pointer already names idea-lighthouse, and the line is already there under ## The keeper before Mara. Not copied again."
    }
  ],
  "questions": [],
  "could_not": []
}
```

#### Reply

```text
I finished batch b1, round 0: one unit migrated, one line left in place and no questions for you.

- **Migrated (u1):** I copied "Mara finds the last keeper's spare key taped under the third stair from the top." from `brain-dump.md` line 11 into `Ideas/idea-lighthouse.md`. Your comment on line 13 sends both bullets to idea-lighthouse. It went under "## The keeper before Mara", right after the green-ink log line, because both are about the last keeper. It has no tag, so it stays tentative.
- **Left in place:** Line 10, the green-ink fog log, already has a `migrated-to` pointer to idea-lighthouse and is already in that note. I didn't copy it a second time.

I wrote nothing in the Brain Dump doc. The unit record file is at `run/unit-records.json`.
```
