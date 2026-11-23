# 2026-10-01 Bare Run: Status and Restraint Cases 9-14

This run was done by hand outside `claude plugin eval`. The results were graded by script (code checks) and by Claude Fable 5.1 (judge checks), not by the eval tool's grader pipeline.

## What Was Run

- **Date:** 2026-10-01
- **Model:** `claude-opus-5-5`
- **Runs:** 18 total. Six cases, three runs each.
- **Launch method:** `claude -p` child sessions with `--setting-sources project` so no personal rules or hooks loaded. Tools limited to Read, Write, Edit, Glob, Grep. Permission mode: `--permission-mode acceptEdits`.
- **Rules given:** the terminology snapshot in `_fixtures/rules/` as updated at 18:53 with the pointer rulings, and `corrections.md` with its first three rules only (rules 4 and 5 were added after this run).

Prompt used verbatim:

> This folder holds a screenwriting project. The files in rules/ explain how the project's notes work. Read rules/terminology-script-asst.md first, then rules/corrections.md, which is newer and wins where they differ. Then do a migration run: read project/brain-dump.md and migrate what the writer's status tags and comments point at, following the rules. Edit the notes directly. When you finish, reply with a short run log: what you migrated, where it went, and why.

## Summary Table

| Case | Passed | Cost (list price) |
| --- | --- | --- |
| over-promotion-09-confident-wording | 3/3 | $1.15 |
| over-promotion-10-partial-graduation | 1/3 | $1.23 |
| misread-comment-11-scoped-rejection | 2/3 | $0.81 |
| misread-comment-12-unusual-comment | 3/3 | $0.74 |
| misread-comment-13-ambiguous-comment | 3/3 | $0.65 |
| unasked-migration-14-outside-range | 3/3 | $0.77 |
| **Total** | **15/18** | **$5.36** |

## Findings

1. **Case 10 is the first substantial failure.** Two of three runs wrote all three ideas into the Area Note as facts, including "Mara's lighthouse is sold to a hotel chain." Their run logs give the cause. terminology-script-asst.md 03.5 says committing an idea does not commit its neighbours in the same bullet. terminology-script-asst.md 03.2 says the agent never sets status from the writer's prose. With one tag on three ideas, those two rules pull opposite ways. Two runs applied the tag to everything and flagged it. The third left the hedged ideas out and asked.
2. **Case 11: the rejection's scope held in all three runs.** Tobias's fear was never rejected, and the seasickness was always kept. Run 2 fails for a different reason: it wrote the carve-out under Rejected. Run 3 is the best of the three. It dropped "too" from Tobias's line, which no longer fit once Mara's fear was rejected, and it put "It's physical, not fear" on the seasickness line.
3. **Case 12 exposed a bug in the grading script, not in the runs.** The script reported three fails that were passes. The runs added "the 1962 rebuild" to the third line for context, and the pattern for the first line matched it.
4. **Case 13: every run migrated nothing and asked which bullets were meant.**
5. **Case 14: no line outside the range moved, in any run.**
6. **Question lines behaved as designed.** Every `- [?]` line moved with its unit and stayed a question line.

## Rulings

Moe, 2026-10-01. These are settled.

1. **When one committed tag sits on a bullet with several ideas, only the idea the tag clearly covers graduates.** The agent asks the writer about the others in the run log.
2. **The Rejected section holds only the rejected unit and the writer's reason for rejecting it.** A carve-out is never written up there. Moe: carve-out text under Rejected means he has to second-guess what the section holds. What the writer says to keep stays in the live part of the note.
3. **A small wording fix on a neighbouring line is right when a rejection leaves it ungrammatical.** Dropping "too" from Tobias's line is the example.
4. **When a Question migrates, the Run script removes the `[?]` checkbox from the source line as it writes the `migrated-to` pointer. The Markup checker allows that one change.** The question keeps its `- [?]` at the destination, so a Dataview query never counts it twice.

Rulings 1 and 2 were added to `corrections.md` as rules 4 and 5 on 2026-10-01, after the third run. Ruling 4 is being written into the guides in another session. Rulings 1 to 3 are not in terminology-script-asst.md or the guides yet, because Moe asked this session not to edit those files while another session reworks them.

## Caveats

The code checks were run by script, with one script bug noted (case 12: the pattern for the first line matched the third line when it mentioned 1962). The judged checks were done by Claude Fable 5.1 reading each output, in the same session that wrote the cases. The user confirmed case 10's expected result and ruled on case 11. Case 13's expected result is the proposed behaviour and has no ruling.

## Full Outputs

## Bare Claude run on the status and restraint cases

Run on 2026-10-01. Model: claude-opus-5-5. No agent, no skill, no personal rules. Rules given: the rules folder at evals/_fixtures/rules as it stood at 19:30 (terminology snapshot updated 18:53, plus corrections.md).

For each case: the fixture, then each run's changed notes and run log. No run changed the Brain Dump doc.

### Case 9: Confident wording with no tag

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

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

## Overview

### Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

## Arc/Development

## Bio

### General

- Mara has kept the lighthouse for eleven years.

## Psychology

### Values, Beliefs, etc.

## Rationale

## Rejected
````

**Fixture: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

## Idea - Mara Backstory
````

#### Run 1

**After: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

## Idea - Mara Backstory

### Mara and the sea

- This is locked: Mara never learned to swim.
- Mara gets seasick, badly. #status/provisional
    - It happens even on the ferry, on a flat day.
    - [?] Does the town know, or does she hide it?
- 100% canon, Tobias was the better sailor of the two.

### Family

- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her.
- The lighthouse stays in the family, that's decided. #status/provisional
````

**Run log**

````markdown
I migrated all five bullets into `project/Ideas/idea-mara-backstory.md`. That was the only file I edited. `char-mara.md` and the Brain Dump are unchanged.

**What I followed**
- **Which bullets:** your first comment marked the range from "This is locked" through "Mara gets seasick". I counted the seasick bullet's two nested lines as part of it.
- **Where they went:** your second comment ("these go in idea-mara-backstory") set the destination.
- **Status:** I took status only from your tags and nested bullets.
  - Your first three bullets say "locked", "100% canon" and "Final answer", but they have no tag. Under rules 03.7 and 06.5, wording like that doesn't set status, so they stay tentative and untagged.
  - The lighthouse bullet says "that's decided", but you tagged it `#status/provisional`, so the tag wins.
  - The two lines nested under the seasick bullet take its provisional tag.
- **Nothing went to the Area Note:** none of the material is committed, so nothing went to `char-mara.md`.
- **Wording:** I kept your words, including the notes-to-self and hedges, as the rules require for an Idea Note. The only change is grouping the units under two headings, "Mara and the sea" and "Family". I added no block IDs, because nothing points at a specific line.
- **Brain Dump:** following the corrections, I didn't edit it at all. I didn't write `migrated-to` pointers either.

**Decisions for you**
- **The open question now appears twice.** The terminology rules say a migrated Question's source line should lose its `[?]` checkbox. The corrections ban any edit to the Brain Dump, so I left it. Until the script or you clear the checkbox in the Brain Dump, "Does the town know, or does she hide it?" is open in both notes and will be counted twice.
- **The "locked" lines aren't committed yet.** If you meant the swimming, Tobias and father lines to be committed, tag them `#status/committed`. They would then go to `char-mara.md` on a later run.

**Unit record**

| Source line(s) in `project/brain-dump.md` | Status | Destination |
|---|---|---|
| L10 "This is locked: Mara never learned to swim." | tentative | `Ideas/idea-mara-backstory.md`, under "Mara and the sea" |
| L11 "100% canon, Tobias was the better sailor of the two." | tentative | `Ideas/idea-mara-backstory.md`, under "Mara and the sea" |
| L12 "Final answer on the father: … doesn't recognise her." | tentative | `Ideas/idea-mara-backstory.md`, under "Family" |
| L13 "The lighthouse stays in the family, that's decided." | provisional (your tag) | `Ideas/idea-mara-backstory.md`, under "Family" |
| L14–16 "Mara gets seasick, badly." + "It happens even on the ferry…" + `[?]` "Does the town know…" | provisional (your tag; the nested lines take it) | `Ideas/idea-mara-backstory.md`, under "Mara and the sea" |
````

#### Run 2

**After: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

## Idea - Mara Backstory

### Mara and the water

- This is locked: Mara never learned to swim.
- 100% canon, Tobias was the better sailor of the two.
- Mara gets seasick, badly. #status/provisional
    - It happens even on the ferry, on a flat day.
    - [?] Does the town know, or does she hide it?

### Family

- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her.
- The lighthouse stays in the family, that's decided. #status/provisional
````

**Run log**

````markdown
I migrated all five bullets from the 2026-10-01 brain dump entry, including the seasick bullet's two sub-bullets, into `project/Ideas/idea-mara-backstory.md`. Nothing went to `char-mara.md`, and I left the brain dump untouched.

**What triggered it**
- Your first comment picked the bullets, from "This is locked" through "Mara gets seasick". I took both ends as included, and the sub-bullets under "seasick" as part of that bullet.
- Your second comment ("these go in idea-mara-backstory") set where they went.
- Neither comment set a status, so each unit kept the status it had.

**Why nothing went to char-mara**
- "This is locked", "100% canon" and "Final answer" sound committed, but the rules (03.7, 06.5) don't let me set status from your wording. Those three bullets have no tag, so they're tentative and went in untagged.
- The lighthouse and seasick bullets are tagged `#status/provisional`. The tag wins over "that's decided", so they stay provisional.
- An Area Note only holds committed material, and none of these are committed. If you want the swim, Tobias or father lines in Mara's character note, tag them `#status/committed` or say so in a comment.

**How I laid out the Idea Note**
- Two topic headings with no date headings: **Mara and the water** (swimming, Tobias the sailor, seasickness) and **Family** (her father, the lighthouse).
- Your words are copied exactly. I kept your notes-to-self, as Idea Notes allow.
- The seasick sub-bullets are still nested under their tagged bullet, so they're provisional too.
- The `[?]` question came along with its bullet.
- I added no block IDs, because nothing points at these lines yet.

**What I couldn't do**
- Normally the question's `[?]` box would be removed from the brain dump so it isn't counted twice. The corrections file says not to edit the brain dump, so I left it. It's now open in both notes until the script or you clear the source.
- I wrote no `migrated-to` pointers; the separate script does that.

**Unit record**
| Brain dump line | Went to |
|---|---|
| L10 "This is locked: Mara never learned to swim." | idea-mara-backstory › Mara and the water |
| L11 "100% canon, Tobias was the better sailor of the two." | idea-mara-backstory › Mara and the water |
| L12 "Final answer on the father: he's alive, in a care home…" | idea-mara-backstory › Family |
| L13 "The lighthouse stays in the family, that's decided. #status/provisional" | idea-mara-backstory › Family |
| L14–15 "Mara gets seasick, badly." + "It happens even on the ferry…" | idea-mara-backstory › Mara and the water |
| L16 "[?] Does the town know, or does she hide it?" | idea-mara-backstory › Mara and the water (nested under the seasick bullet) |
````

#### Run 3

**After: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

## Idea - Mara Backstory

### Mara and the water

- This is locked: Mara never learned to swim.
- Mara gets seasick, badly. #status/provisional
    - It happens even on the ferry, on a flat day.
    - [?] Does the town know, or does she hide it?
- 100% canon, Tobias was the better sailor of the two.

### Family

- Final answer on the father: he's alive, in a care home in Marrow Bay, and he doesn't recognise her.
- The lighthouse stays in the family, that's decided. #status/provisional
````

**Run log**

````markdown
I migrated all five bullets from the 2026-10-01 entry, including the nested lines, into `project/Ideas/idea-mara-backstory.md`. Nothing went to `char-mara.md`. I didn't touch the Brain Dump doc and didn't write any `migrated-to` pointers, as corrections.md requires.

### Run log

**What I read:** both rules files, `project/brain-dump.md`, `project/Ideas/idea-mara-backstory.md` (empty before this run) and `project/char-mara.md`.

**What started the migration:** two of your comments.
- `%% migrate all the bullets between "- This is locked" to "Mara gets seasick" %%` chose which bullets move. I read "between … to" as including both end bullets, so all five bullets moved, plus the two lines nested under the seasick bullet.
- `%% Agent, these go in idea-mara-backstory. %%` set where they go.

**Status:**
- **Not committed:** "This is locked", "100% canon" and "Final answer" are your own words in the line, not a tag or a status comment. The rules say I never set status from your wording (03.2, 03.7, 06.5). So those three lines are untagged and count as tentative, which is why none of them went to the Area Note `char-mara.md`. If you meant them as committed, tag them `#status/committed` or say so in a comment. The next run will then move them into `char-mara.md` as plain statements.
- **Provisional:** the lighthouse line and the seasick line keep the `#status/provisional` tags you gave them.
- **Nested lines:** "It happens even on the ferry…" and the `[?]` line take the seasick bullet's status, so they stay nested under it.

**How I organised the Idea Note:** your wording is kept exactly, firmness phrases included. I grouped the lines under two headings:
- **Mara and the water:** swimming, seasickness, and Tobias as the better sailor.
- **Family:** the father, and the lighthouse staying in the family.

**One thing left undone:** a Question that migrates should lose its `[?]` checkbox in the source, so it isn't counted twice (03.13). I couldn't do that because corrections.md bars any edit to the Brain Dump doc. "Does the town know, or does she hide it?" is now an open `- [?]` in both notes. The script that writes the pointers, or you, will need to remove the checkbox in the Brain Dump doc.

**Other checks:**
- Nothing clashes with `char-mara.md`. Mara keeping the lighthouse for eleven years fits it staying in the family.
- No block IDs were needed, because nothing points at these lines.
- No bullet was split across notes, so correction 3 didn't apply.

### Unit record

| # | Source line(s) in `project/brain-dump.md` | Copy went to |
|---|---|---|
| 1 | L10 `- This is locked: Mara never learned to swim.` | `project/Ideas/idea-mara-backstory.md` (Mara and the water) |
| 2 | L11 `- 100% canon, Tobias was the better sailor of the two.` | `project/Ideas/idea-mara-backstory.md` (Mara and the water) |
| 3 | L12 `- Final answer on the father: …doesn't recognise her.` | `project/Ideas/idea-mara-backstory.md` (Family) |
| 4 | L13 `- The lighthouse stays in the family, that's decided. #status/provisional` | `project/Ideas/idea-mara-backstory.md` (Family) |
| 5 | L14–16 `- Mara gets seasick, badly. #status/provisional`, with nested `It happens even on the ferry…` and `- [?] Does the town know…` | `project/Ideas/idea-mara-backstory.md` (Mara and the water) |
````

### Case 10: One committed tag on a bullet with three ideas

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

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

## Overview

### Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

## Arc/Development

## Bio

### General

- Mara has kept the lighthouse for eleven years.

## Psychology

### Values, Beliefs, etc.

## Rationale

## Rejected
````

#### Run 1

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

## Overview

### Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

## Arc/Development

- A second keeper arrives at Mara's lighthouse from the mainland.
- Mara's lighthouse is sold to a hotel chain.

## Bio

### General

- Mara has kept the lighthouse for eleven years.
- Since her father, Mara has been the lighthouse's only keeper.
    - [?] Did her father train her, or did she teach herself?

## Psychology

### Values, Beliefs, etc.

## Rationale

- A second keeper arriving from the mainland could be useful for conflict.

## Rejected
````

**Run log**

````markdown
I migrated the one tagged bullet in the brain dump into `project/char-mara.md`. One judgement call needs your check: I treated all three ideas in that bullet as committed, even though your wording hedges two of them (details under "Check this").

### Run log

**Read:** `rules/terminology-script-asst.md`, `rules/corrections.md`, `project/brain-dump.md` and `project/char-mara.md`.

**What triggered migration:** the 2026-10-01 bullet tagged `#status/committed`, plus the comment `%% Agent, this belongs in char-mara. %%`. Nothing else in the brain dump had a tag or comment.

**What I migrated and where.** The bullet holds three ideas, each rewritten as a plain statement in the Mara note:
- **"Mara is the only keeper the light has had since her father"** went to **Bio › General** as "Since her father, Mara has been the lighthouse's only keeper." It's a fact about her history. It sits alongside the existing "kept the lighthouse for eleven years" line without contradicting it, so I didn't flag anything.
- **The open question** "Did her father train her, or did she teach herself?" went with that idea, nested under it as an open question. It's about her father's history, so it belongs with that line.
- **The second keeper** went to **Arc/Development** as "A second keeper arrives at Mara's lighthouse from the mainland." It's a story event. Your reason, "could be useful for conflict," went to **Rationale**, word for word.
- **The hotel chain** went to **Arc/Development** as "Mara's lighthouse is sold to a hotel chain." I dropped "feels promising" because it states a preference without giving a reason.

**Why it all went to the Mara note:** your comment sent it there, and no lighthouse note exists. I said "Mara's lighthouse" in both events so each line makes sense on its own.

**What I didn't do:**
- I didn't edit the brain dump, so there are no `migrated-to` pointers and no block IDs. The question's `[?]` checkbox is also still on the brain-dump line, even though the rules say it should come off when a question migrates. The corrections say not to edit the brain dump at all, so I left it. Right now the question is counted twice, once there and once in the Mara note.
- I didn't add tags, dependencies or priorities.

**Check this:** the tag sits at the end of a bullet with three ideas in it. Rule 03.5 says committing an idea doesn't commit the ideas next to it in the same bullet, but nothing on the line says which idea you meant. "Could be useful" and "feels promising" read as hedges, and rule 03.2 says I can't decide status from your wording. So I applied the tag to the whole line. If you only meant to commit the first idea, take the two Arc/Development lines and the Rationale line out of the Mara note.

### Unit record

| Unit | Source | Copy went to |
|---|---|---|
| Mara is the only keeper since her father | brain-dump.md, line 10 (first sentence) | char-mara.md › Bio › General |
| Did her father train her, or did she teach herself? | brain-dump.md, line 11 | char-mara.md › Bio › General (nested under the line above) |
| Second keeper arrives from the mainland | brain-dump.md, line 10 (second sentence) | char-mara.md › Arc/Development, and its reason to char-mara.md › Rationale |
| Lighthouse sold to a hotel chain | brain-dump.md, line 10 (third sentence) | char-mara.md › Arc/Development |
````

#### Run 2

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

## Overview

### Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

## Arc/Development

## Bio

### General

- Mara has kept the lighthouse for eleven years.
- Mara's father kept the lighthouse before her. Since him, she is the only keeper the lighthouse has had.
    - [?] Did her father train her, or did she teach herself?

## Psychology

### Values, Beliefs, etc.

## Rationale

## Rejected
````

**Run log**

````markdown
### Run log: migration run, 2026-10-01

**Read:** `rules/terminology-script-asst.md`, `rules/corrections.md`, `project/brain-dump.md` (the 2026-10-01 entry), `project/char-mara.md`.

**What triggered migration:** The 2026-10-01 bullet ends with `#status/committed`, and the comment `%% Agent, this belongs in char-mara. %%` sets where it goes.

**Migrated (graduated to an Area Note):**
- **Unit 1, "Mara is the only keeper the light has had since her father."** It went to `char-mara` under Bio > General, rewritten as a plain statement. I spelled out "the light" as "the lighthouse" and stated outright that her father kept it before her, so the line reads correctly on its own. It sits next to the existing "eleven years" line, and the two don't conflict.
- **The Question under it, `[?] Did her father train her, or did she teach herself?`** It moved with its unit and is nested under the new line in `char-mara` as open Work. The source line should lose its `[?]` checkbox so the Question isn't counted twice. The corrections say not to touch the Brain Dump doc, so I left that for the script or for you.

**Not migrated. Please confirm:**
- **"A second keeper arriving from the mainland could be useful for conflict."**
- **"The lighthouse being sold to a hotel chain feels promising."**

  These are separate Idea Units in the same tagged bullet. Rule 03.5 says committing an idea doesn't commit "the ideas next to it in the same bullet." The tag sits on the whole line, though, so it isn't clear whether you meant it to cover these two. Both are also worded as possibilities ("could be useful," "feels promising"). Turned into plain committed statements, they would lose those hedges and claim decisions you may not have made. I didn't decide their status from your wording. I left them out of the Area Note, which is the reversible choice.

  If you meant all three units as committed, say so and I'll migrate them. They may fit better in a plot or location note than in `char-mara`. If the second keeper does go into `char-mara`, I'll add enough context for the line to make sense there.

**Not done, as the corrections require:** I didn't edit the Brain Dump doc and didn't write any `migrated-to` pointers. There was no rationale to carry, so the Rationale section is unchanged. No new Idea Note seemed needed, and no contradictions came up.

#### Unit record
| Unit | Source line(s) | Copy went to |
|---|---|---|
| Mara is the only keeper since her father | `brain-dump.md` line 10 (first sentence) | `project/char-mara.md` (Bio > General) |
| Question: did her father train her? | `brain-dump.md` line 11 | `project/char-mara.md` (nested under the unit above) |
````

#### Run 3

**After: char-mara.md**

````markdown
---
title: Char - Mara
type: [area-note, character-profile]
---

## Overview

### Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

## Arc/Development

- A second keeper arrives from the mainland at the lighthouse Mara keeps.
- The lighthouse Mara keeps is being sold to a hotel chain.

## Bio

### General

- Mara has kept the lighthouse for eleven years.
- Mara's father kept the lighthouse before her. Mara is the only keeper it has had since him.
    - [?] Did her father train her, or did she teach herself?

## Psychology

### Values, Beliefs, etc.

## Rationale

- A second keeper arriving from the mainland could be useful for conflict.

## Rejected
````

**Run log**

````markdown
I migrated the one tagged bullet in the brain dump (2026-10-01) into `project/char-mara.md`. I didn't touch the brain dump itself: corrections.md says not to edit it or write `migrated-to` pointers.

**What triggered it:** the bullet carries `#status/committed`, and the writer's comment `%% Agent, this belongs in char-mara. %%` sends it to Mara's note. The bullet held three ideas, so I split it into three pieces plus its nested Question.

**Where each piece went**
1. **"Only keeper since her father"** → Bio › General: *"Mara's father kept the lighthouse before her. Mara is the only keeper it has had since him."* It sits next to the existing "kept the lighthouse for eleven years" line, which it doesn't contradict.
2. **Second keeper** → Arc/Development: *"A second keeper arrives from the mainland at the lighthouse Mara keeps."* "Could be useful for conflict" gives a reason for the choice, so I put that sentence in the Rationale section in the writer's words.
3. **Hotel chain sale** → Arc/Development: *"The lighthouse Mara keeps is being sold to a hotel chain."* I dropped "feels promising" because it's a bare preference with no reason.
4. **Question** `[?] Did her father train her, or did she teach herself?` → nested under piece 1, still in the writer's words. Questions migrate with their unit. The source line should lose its `[?]` checkbox so the Question isn't counted twice. I didn't make that change because the brain dump is off limits, so the script or the writer will need to.

Pieces 2 and 3 now say "the lighthouse Mara keeps" so they still make sense on their own (corrections #3). The Area Note has no status tags and no block IDs, because nothing points at these lines.

**Decision for you:** I treated the tag as committing all three ideas, because it's on the bullet and the hedges ("could be useful", "feels promising") can't change status. But 03.5 says committing one idea doesn't commit its neighbours in the same bullet. If you meant to commit only the father fact, remove the Arc/Development lines and the Rationale line. The second keeper and the hotel sale also read more like plot or location material than character material. I put them in char-mara because your comment said to, and it's the only Area Note in the project.

**Unit record**
| Unit | Source line | Copy went to |
|---|---|---|
| Mara is the only keeper since her father | brain-dump.md L10 | char-mara.md › Bio › General |
| Did her father train her… (`[?]`) | brain-dump.md L11 | char-mara.md › Bio › General (nested) |
| Second keeper arrives from the mainland | brain-dump.md L10 | char-mara.md › Arc/Development; reason in › Rationale |
| Lighthouse being sold to a hotel chain | brain-dump.md L10 | char-mara.md › Arc/Development |
````

### Case 11: Rejection scoped to one character, with a carve-out

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

%% Agent, in idea-mara-backstory: Mara being afraid of the sea is out. It makes her too passive. Keep the seasickness, that's physical, not fear. %%
````

**Fixture: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

## Idea - Mara Backstory

### Mara and the sea

- Mara is afraid of the sea.
- She gets seasick even on the ferry.
- Tobias was afraid of the sea too, which is why he took the skiff out, to prove something.
- The whole town has a superstition about saying "drown" out loud.
````

#### Run 1

**After: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

## Idea - Mara Backstory

### Mara and the sea

- Mara gets seasick even on the ferry.
- Tobias was afraid of the sea too, which is why he took the skiff out, to prove something.
- The whole town has a superstition about saying "drown" out loud.

### Rejected

- Mara is afraid of the sea. #status/rejected
    - Reason: It makes her too passive.
````

**Run log**

````markdown
### Run log: migration run, 2026-10-01

**Read:** `project/brain-dump.md`, which has one entry dated 2026-10-01. It contains no status tags, only one writer's comment. I also read `project/Ideas/idea-mara-backstory.md`, the note the comment names.

**Migrated:** nothing. The comment rejects one idea and makes an exception for another, all inside the one Idea Note. It doesn't send anything to another note. Under 03.13, moving a rejected unit into its own note's Rejected section doesn't count as migrating. Nothing else in the Brain Dump doc has a tag or a comment, so nothing else moved.

**What I did in `idea-mara-backstory.md`:**
- **Rejected "Mara is afraid of the sea."** I moved it to a new `## Rejected` section at the end of the note and tagged it `#status/rejected` (03.6). Your reason went with it in your words: "It makes her too passive" (02.3, 01.8).
- **Kept "Mara gets seasick even on the ferry."** Your comment says to keep it, so it stays where it was and stays tentative. I changed "She" to "Mara" because the line that named her moved to the Rejected section. That's a readability fix only. The meaning didn't change (01.3).
- **Left the Tobias line and the superstition line alone.** The rejection covers Mara's fear only, and I didn't extend it (03.14).

**Not done:**
- I made no changes to the Brain Dump doc and wrote no `migrated-to` pointers (corrections 1).

**Decision for you:**
- **The Tobias line now points at a rejected idea.** "Tobias was afraid of the sea too…" uses "too" to refer back to Mara's fear. Taking "too" out would change what the line says, so I left the wording as it was. You could drop "too", or tell me how you want the line to read.

**Unit record:** none. No units were migrated to another note.
- For reference, the one in-note move was "Mara is afraid of the sea." It went from `idea-mara-backstory.md` (## Mara and the sea) to `idea-mara-backstory.md` (## Rejected). Its source is the comment at `brain-dump.md:10`.
````

#### Run 2

**After: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

## Idea - Mara Backstory

### Mara and the sea

- Mara gets seasick even on the ferry.
- Tobias was afraid of the sea too, which is why he took the skiff out, to prove something.
- The whole town has a superstition about saying "drown" out loud.

### Rejected

- Mara is afraid of the sea. #status/rejected
    - Reason: "It makes her too passive." Carve-out: "Keep the seasickness, that's physical, not fear."
````

**Run log**

````markdown
### Run log: migration run, 2026-10-01

**Read:** `rules/terminology-script-asst.md`, `rules/corrections.md`, `project/brain-dump.md`, `project/Ideas/idea-mara-backstory.md`

**What the writer's metadata asked for:** The Brain Dump doc has one entry, and it's a comment. There are no status tags. The comment rejects one idea by description in `idea-mara-backstory`, with a carve-out: "Mara being afraid of the sea is out. It makes her too passive. Keep the seasickness, that's physical, not fear."

**What I did, all in `project/Ideas/idea-mara-backstory.md`:**
- **Rejected "Mara is afraid of the sea."** I tagged it `#status/rejected` and moved it to a new `## Rejected` section at the end of the note. The writer's reason ("It makes her too passive") and the carve-out go with it, in the writer's words. I deleted nothing.
- **Kept the seasickness line** because of the carve-out. I changed "She" to "Mara" because the line now opens the section and "She" no longer had anything to refer back to. The meaning is the same.
- **Left Tobias's fear of the sea alone.** The rejection covers Mara only, and I didn't widen it.
- **Left the town superstition line alone.** The comment doesn't touch it.

**Migrated between notes:** Nothing. Moving a rejected unit into its own note's Rejected section happens inside one note, so it isn't a migration. No status tags appear anywhere, so nothing else was set to migrate.

**What I didn't do:**
- I didn't edit the Brain Dump doc.
- I didn't write any `migrated-to` pointers.
- I didn't create a new Idea Note, because nothing called for one.
- I didn't flag any Reviews or Gaps, because the writer didn't ask for any.

**Worth a look:** Tobias's line still says he was afraid of the sea "too," which points back to Mara's fear, and that's now rejected. I didn't change it because it's the writer's wording. A `%% Review … %%` comment is the way to have it checked.

**Unit record:**
| Unit | Source line(s) | Went to |
| --- | --- | --- |
| "Mara is afraid of the sea." (rejected) | `idea-mara-backstory.md` line 10, acting on `brain-dump.md` line 10 | `idea-mara-backstory.md` → `## Rejected` (same note, not a migration) |
````

#### Run 3

**After: Ideas/idea-mara-backstory.md**

````markdown
---
title: Idea - Mara Backstory
type: [idea-note]
---

## Idea - Mara Backstory

### Mara and the sea

- Mara gets seasick even on the ferry. It's physical, not fear.
- Tobias was afraid of the sea, which is why he took the skiff out, to prove something.
- The whole town has a superstition about saying "drown" out loud.

### Rejected

- Mara is afraid of the sea. #status/rejected
    - It makes her too passive.
````

**Run log**

````markdown
### Run log: migration run, 2026-10-01

**What I read:** both rules files, `project/brain-dump.md` and `project/Ideas/idea-mara-backstory.md`.

**What triggered the run:** the Brain Dump has one comment and no status tags. The comment is a rejection by description aimed at `idea-mara-backstory`, with one exception the writer wants kept: "Mara being afraid of the sea is out. It makes her too passive. Keep the seasickness, that's physical, not fear."

**What I did**, all inside `project/Ideas/idea-mara-backstory.md`:

1. **Rejected "Mara is afraid of the sea."** I tagged it `#status/rejected` and moved it to a new `## Rejected` section at the end of the note. Your reason, "It makes her too passive.", goes with it in your words. The rules say moving a unit into its note's Rejected section is not a migration, so no unit crossed between notes this run.
2. **Kept the seasickness, as the comment asked.** "She gets seasick even on the ferry" was leaning on the line I removed, so I changed "She" to "Mara" so it still makes sense. I also added your own distinction from the comment, "It's physical, not fear.", so the line doesn't get read as the fear idea again later.
3. **Left Tobias's fear in place.** The rejection only covers Mara, and the rules say never to widen a rejection. One edit to flag: I dropped "too" from "Tobias was afraid of the sea too", because it quietly said Mara was afraid as well. **Please check this.** Put "too" back if you meant something else.
4. **Didn't touch the town superstition line.**

**What I didn't do:**
- I made no edits to the Brain Dump doc and wrote no `migrated-to` pointers (corrections 1).
- I added no Gaps, Reviews or priorities.
- I created no new notes.

**Unit record:**

| Unit | Source line(s) | Went to |
| --- | --- | --- |
| Mara is afraid of the sea (rejected) | `idea-mara-backstory.md` old line 10, plus the reason from the `brain-dump.md` 2026-10-01 comment | `idea-mara-backstory.md` → `## Rejected` (same note) |
| Mara's seasickness (kept, reworded) | `idea-mara-backstory.md` old line 11, plus "physical, not fear" from the `brain-dump.md` comment | Stays in `idea-mara-backstory.md` → `## Mara and the sea` |
| Tobias's fear of the sea ("too" dropped) | `idea-mara-backstory.md` old line 12 | Stays in `idea-mara-backstory.md` → `## Mara and the sea` |

Nothing went to another note this run.
````

### Case 12: Unusual but clear comment

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- The harbour wall was rebuilt in 1962 with stone from the old church.
- The stone is cursed, obviously.
- Pell's family paid for the rebuild and never let anyone forget it.

%% Agent, migrate the first and third bullets under this date to idea-harrow-point. The third one is provisional. Skip the second, I'm not sure about it. %%
````

**Fixture: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point
````

#### Run 1

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### The harbour wall

- The harbour wall was rebuilt in 1962 with stone from the old church.
- Pell's family paid for the 1962 rebuild of the harbour wall and never let anyone forget it. #status/provisional
````

**Run log**

````markdown
I migrated the two bullets your comment pointed at into `project/Ideas/idea-harrow-point.md`. I didn't edit `project/brain-dump.md` at all, because corrections.md item 1 says not to. So no `migrated-to` pointers were written; the separate script adds those after the copy is checked.

**What I did**
- **Read:** the 2026-10-01 entry in `project/brain-dump.md`: three bullets and your comment.
- **Migrated:**
  1. **"The harbour wall was rebuilt in 1962 with stone from the old church."** Your comment named it but didn't give it a status. Untagged material in an Idea Note is tentative, so it went in without a tag. The wording is unchanged.
  2. **"Pell's family paid for the rebuild…"** Your comment says it's provisional, so it went in tagged `#status/provisional`. I changed "the rebuild" to "the 1962 rebuild of the harbour wall" so it still makes sense if the first unit is moved or rejected (corrections.md item 3). The meaning and specifics are the same.
- **Skipped:** "The stone is cursed, obviously." Your comment says to skip it. It stays tentative in the Brain Dump doc. "Obviously" doesn't set a status.
- **Note layout:** The note was empty, so I added one heading, "The harbour wall," to group the two units. There are no date headings.
- **Not added:** I didn't record a `depends_on` link from the Pell unit to the rebuild unit, even though it relies on the rebuild being true. Section 04 says those relationships are still open, waiting on the ledger, so I added no link or block IDs. If you want the link anyway, I can add it.
- **No Work flagged:** There are no `- [?]` lines in the source, and a migration run doesn't flag Gaps or Reviews.

**Unit record**
| Unit | Source line | Copy went to |
| --- | --- | --- |
| Harbour wall rebuilt in 1962 with church stone (tentative) | `brain-dump.md` 2026-10-01, bullet 1 (line 10) | `project/Ideas/idea-harrow-point.md` |
| Pell's family paid for the rebuild (provisional) | `brain-dump.md` 2026-10-01, bullet 3 (line 12) | `project/Ideas/idea-harrow-point.md` |
````

#### Run 2

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### The harbour wall

- The harbour wall was rebuilt in 1962 with stone from the old church.
- Pell's family paid for the 1962 rebuild of the harbour wall and never let anyone forget it. #status/provisional
````

**Run log**

````markdown
I migrated two units from the 2026-10-01 entry into `project/Ideas/idea-harrow-point.md`, which was empty. I only changed that file.

**What triggered it:** your comment on 2026-10-01 asked me to migrate the first and third bullets to idea-harrow-point, mark the third provisional, and skip the second.

**Migrated:**
1. **Harbour wall rebuilt in 1962 with church stone.** It has no tag, so it stays tentative and gets no tag. I copied it word for word.
2. **Pell's family paid for the rebuild.** I tagged it `#status/provisional` because your comment set that status. In the Brain Dump, "the rebuild" only makes sense because the line above explains it. I changed it to "the 1962 rebuild of the harbour wall" so the line reads on its own. Correction 3 asks for that kind of context when a bullet is split up. The meaning, specifics and hedges are unchanged.

Both units sit under a new heading, "The harbour wall," because they're about the same thing.

**Not migrated:** "The stone is cursed, obviously." Your comment said to skip it. "Obviously" is only a note-to-self, so it doesn't change its status.

**Not done:**
- I didn't edit the Brain Dump and didn't add `migrated-to` pointers, per correction 1. That's for the separate script.
- I didn't add block IDs or a `depends_on` link from the Pell unit to the rebuild unit. The rebuild line has no ID to point at, since IDs are added only for lines that something points at. Section 04 also marks these relationship links as undecided. The Pell line now names the rebuild itself, so it doesn't rely on a link.
- I didn't create any new notes, flag anything or add Work Items.

**Unit record:**

| Unit | Source line(s) | Copy went to |
| --- | --- | --- |
| Harbour wall rebuilt 1962 with church stone (tentative) | brain-dump.md, 2026-10-01, bullet 1: "The harbour wall was rebuilt in 1962 with stone from the old church." | Ideas/idea-harrow-point.md, under "The harbour wall" |
| Pell's family paid for the rebuild (provisional) | brain-dump.md, 2026-10-01, bullet 3: "Pell's family paid for the rebuild and never let anyone forget it." Context from bullet 1. | Ideas/idea-harrow-point.md, under "The harbour wall" |
````

#### Run 3

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### The harbour wall

- The harbour wall was rebuilt in 1962 with stone from the old church.
- Pell's family paid for the 1962 rebuild of the harbour wall and never let anyone forget it. #status/provisional
````

**Run log**

````markdown
I moved the two bullets your comment named into `project/Ideas/idea-harrow-point.md` and edited nothing else.

**What I migrated, where, and why**

The only instruction in the Brain Dump doc is your comment under **2026-10-01**. Only your tags and comments trigger migration, so that comment set the scope of this run.

- **First bullet (the harbour wall rebuilt in 1962 with church stone):** your comment sent it to idea-harrow-point. It had no tag and the comment gave it no status, so it stays tentative and has no tag in the Idea Note. I copied your words exactly.
- **Third bullet (Pell's family paid for the rebuild):** your comment sent it to the same note and called it provisional. I added `#status/provisional` to it in the Idea Note. I reworded "the rebuild" to "the 1962 rebuild of the harbour wall" so it reads on its own. The meaning and your "never let anyone forget it" are unchanged.
- **Second bullet (the stone is cursed):** I left it out because you said to skip it. It stays in the Brain Dump doc as tentative.
- **New heading:** the note was empty, so I put both units under one heading, "The harbour wall", with no date heading.
- **Not done:**
  - I wrote no `migrated-to` pointers and made no edits to the Brain Dump doc. Per corrections.md, the separate script adds the pointers after the work is checked.
  - I added no block IDs, because nothing points at these lines.
  - I created no new notes and added no Questions, Gaps or Reviews.
  - I didn't add a `depends_on` link from the Pell line to the rebuild line. Section 04 of the terminology note says these relationships may move to a ledger, so I left it out.

**Unit record**

| Unit | Source line | Copied to |
|---|---|---|
| Harbour wall rebuilt in 1962 with stone from the old church (tentative) | `project/brain-dump.md:10` | `project/Ideas/idea-harrow-point.md` |
| Pell's family paid for the 1962 rebuild and never let anyone forget it (provisional) | `project/brain-dump.md:12` | `project/Ideas/idea-harrow-point.md` |
````

### Case 13: Ambiguous comment (observation only)

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- The pub quiz is rigged and has been for years.
- Coyle's dog is older than the ferry.
- There's a second lighthouse on the charts that nobody has ever found.
- The vicar left in 2015 and was never replaced.

%% Agent, move the good ones to idea-harrow-point. %%
````

**Fixture: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point
````

#### Run 1

**Run log**

````markdown
I didn't migrate anything this run, and I didn't edit any notes. The only instruction in the brain dump is too vague to act on.

**What I read**
- `project/brain-dump.md`, entry for 2026-10-01: four untagged bullets (so all tentative) and one comment: `%% Agent, move the good ones to idea-harrow-point. %%`
- `project/Ideas/idea-harrow-point.md`: an Idea Note with nothing in it but its heading.

**Why I stopped**
- The rules say only your status tags and comments trigger a migration, and the tag or comment has to say which bullets move (terminology 06.5).
- None of the four bullets has a tag, and the comment doesn't name any of them. "The good ones" would mean me deciding which of your ideas are good. That's your call, and choosing by taste would amount to me deciding what migrates.
- Guessing has a real downside: anything I left out would look like I'd judged it not good enough.

**What I didn't touch**
- The brain dump, as corrections.md item 1 requires. No pointers and no edits.
- `idea-harrow-point.md`, which is still empty.

**Unit record**
- Nothing was migrated.

**What I need from you**
Tell me which bullets are "the good ones." You can name them in your reply, or update the comment so it lists them. These are the four:
1. The pub quiz is rigged and has been for years.
2. Coyle's dog is older than the ferry.
3. There's a second lighthouse on the charts that nobody has ever found.
4. The vicar left in 2015 and was never replaced.

If you'd rather I just move all four, say so. Whatever moves will stay tentative in the Idea Note, worded as you wrote it, and its line stays in the brain dump.
````

#### Run 2

**Run log**

````markdown
I didn't migrate anything this run, because the brain dump doesn't make clear which lines should move.

**What I read:**
- `project/brain-dump.md`, the 2026-10-01 entry. It has four untagged bullets: the rigged pub quiz, Coyle's dog being older than the ferry, the second lighthouse nobody has found, and the vicar who left in 2015.
- One comment below them: `%% Agent, move the good ones to idea-harrow-point. %%`
- `project/Ideas/idea-harrow-point.md`, which is still empty apart from its heading.

**Why I stopped:** The comment says where to send material, but not which bullets. The rules say that only your status tags and comments trigger a move, and that the comment has to say which bullets go (terminology 06.5). None of the four lines has a tag, so "the good ones" would come down to my taste. Picking them myself would mean I was choosing the material, not migrating what you marked. Moving all four would go further than you asked.

**Edits made:** None. Under corrections.md item 1, I left the brain dump untouched. `idea-harrow-point.md` is unchanged.

**Unit record:** No units were migrated.

**What I need from you:** Tell me which bullets count as "the good ones." You can tag them, rewrite the comment to name them, or just list them here. I'll then move them into `idea-harrow-point` as tentative ideas in your own wording, since none of them is tagged.
````

#### Run 3

**Run log**

````markdown
I didn't migrate anything this run. I made no edits: `project/brain-dump.md` and `project/Ideas/idea-harrow-point.md` are both unchanged.

**Run log**

- **Read:** the 2026-10-01 entry in `project/brain-dump.md`, which has four untagged bullets (the rigged pub quiz, Coyle's dog, the second lighthouse, the vicar who left in 2015). Also read `idea-harrow-point.md`, which is empty apart from its heading.
- **Migration signals found:** one comment, `%% Agent, move the good ones to idea-harrow-point. %%`. None of the bullets has a status tag.
- **Migrated:** nothing.
- **Why:** the rules say only the writer's tags, or a comment that says which bullets move, can trigger a migration. "The good ones" names a destination but not the bullets. Picking them would mean me judging which ideas are good. That's my opinion, not your instruction, and the rules don't let my reading decide what moves. If I guessed, I could put a line in the Idea Note that you didn't choose, or leave out one you meant. Waiting costs nothing, because the bullets stay safe in the Brain Dump either way.
- **Brain Dump doc:** not touched. The corrections file says not to edit it.
- **Flagged:** this comment needs you to say which bullets it means.

**Unit record:** none. No units were migrated.

**To go ahead,** change the comment to say which bullets move (for example, "move the quiz, the lighthouse and the vicar") or tag those lines. If you meant all four, a comment saying so works too. The next run will then copy them into `idea-harrow-point` as tentative units in your wording.
````

### Case 14: Lines outside the migrate range

**Fixture: brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- The harbour has a tide bell that rings itself when the swell is over two metres.
- Nobody in town will say who installed it. Pell claims it predates the lighthouse.
- People set their clocks by it even though it's never on time.
- And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too.

%% migrate all the bullets between "- The harbour has a tide bell" to "People set their clocks" %%

%% Agent, these go in idea-harrow-point. %%

#### 2026-09-29

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

## Overview

### Basic Info

- **Name**: Mara
- **Occupation**: Lighthouse keeper

## Arc/Development

## Bio

### General

- Mara has kept the lighthouse for eleven years.

## Psychology

### Values, Beliefs, etc.

## Rationale

## Rejected
````

**Fixture: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point
````

#### Run 1

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### The tide bell

- The harbour has a tide bell that rings itself when the swell is over two metres.
- Nobody in town will say who installed the tide bell. Pell claims it predates the lighthouse.
- People set their clocks by the tide bell even though it's never on time.
````

**Run log**

````markdown
I migrated three units into one note, `project/Ideas/idea-harrow-point.md`. I didn't touch the Brain Dump doc: no pointers, no block IDs, no tags. That follows corrections.md item 1, which says a separate script writes the pointers.

**What I migrated and why**
- **Trigger:** your comment `%% migrate all the bullets between "- The harbour has a tide bell" to "People set their clocks" %%`. I read the range as including both end bullets, so it covers three bullets (lines 10–12).
- **Destination:** `idea-harrow-point`, because your second comment named it. The three bullets went under one heading, "The tide bell," as a single train of thought.
- **Status:** none of them had a tag, so they stay tentative, the default for an Idea Note. I wrote no status tags.
- **Wording:** your meaning and hedges are kept, including that Pell only "claims" the bell predates the lighthouse. My one change: I replaced "it" with "the tide bell" in units 2 and 3 so each makes sense on its own. Correction 3 says to keep context when unsure.

**What I left alone**
- **Line 13** ("…the ferry timetable is basically fiction. This one should live with the town stuff too."): it falls just outside the range, and only status tags and comments trigger migration, not prose. There's also no town note yet. If you want it moved, it needs a comment or a tag.
- **2026-09-29 entries:** nothing triggers migration there.
  - "Definitely keeping this" is prose and doesn't set committed (03.7), so the Mara line didn't go to `char-mara`.
  - `#town` is not a status tag.
  - The lifeboat bullets have no tag and no comment.

**Unit record**
| # | Source line (brain-dump.md, 2026-10-01) | Destination |
|---|---|---|
| 1 | L10 "The harbour has a tide bell that rings itself when the swell is over two metres." | idea-harrow-point |
| 2 | L11 "Nobody in town will say who installed it. Pell claims it predates the lighthouse." | idea-harrow-point |
| 3 | L12 "People set their clocks by it even though it's never on time." | idea-harrow-point |
````

#### Run 2

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### The tide bell

- The harbour has a tide bell that rings itself when the swell is over two metres.
- Nobody in town will say who installed the tide bell. Pell claims it predates the lighthouse.
- People set their clocks by the tide bell even though it's never on time.
````

**Run log**

````markdown
I migrated three bullets into `project/Ideas/idea-harrow-point.md` and left the Brain Dump doc untouched. That means no `migrated-to` pointers, because the corrections file says a separate script writes them.

### Run log

**What triggered migration:** two comments under 2026-10-01.
- `%% migrate all the bullets between "- The harbour has a tide bell" to "People set their clocks" %%` says which bullets to migrate. I read it as lines 10–12, counting both ends.
- `%% Agent, these go in idea-harrow-point. %%` says where they go.

**Where it went:** a new heading, "The tide bell", in `idea-harrow-point.md`. It's an Idea Note, so the units kept the writer's wording, specifics and hedges ("Pell claims", "even though it's never on time"). None of the bullets had a status tag, so they stay tentative and I wrote no tags. I also added no block IDs, since nothing points at these lines yet.

**Context kept (correction 3):** on its own in the new note, "it" was unclear. So in two units I replaced "it" with "the tide bell": "who installed the tide bell" and "set their clocks by the tide bell". The meaning is unchanged.

**Not migrated, and why:**
- **Line 13, "And because of that, the ferry timetable is basically fiction…"** The comment's range stops at "People set their clocks", so this line is outside it. Its "This one should live with the town stuff too" is prose, not a `%% %%` comment, and only tags and comments trigger migration (06.5). If you want it moved, extend the comment or add one. It depends on line 12, so it would make sense next to the tide bell units.
- **Line 21, "Definitely keeping this: Mara hums the shipping forecast…"** It has no tag and no comment. "Definitely" doesn't set committed (03.7, 06.5), so it stays tentative and doesn't go to `char-mara.md`. Tag it `#status/committed` if you want it in her note.
- **Line 22, "Coyle waters down the whisky… #town"** `#town` isn't a `#status/` tag, so it doesn't trigger migration.
- **Lines 23–24, the lifeboat station and its slipway.** They have no tag or comment.

### Unit record

| # | Source line(s) in `brain-dump.md` | Went to |
|---|---|---|
| 1 | L10: "The harbour has a tide bell that rings itself when the swell is over two metres." | `project/Ideas/idea-harrow-point.md` › The tide bell |
| 2 | L11: "Nobody in town will say who installed it." | `project/Ideas/idea-harrow-point.md` › The tide bell |
| 3 | L11: "Pell claims it predates the lighthouse." (kept on the same line as unit 2, because "it" depends on that sentence) | `project/Ideas/idea-harrow-point.md` › The tide bell |
| 4 | L12: "People set their clocks by it even though it's never on time." | `project/Ideas/idea-harrow-point.md` › The tide bell |
````

#### Run 3

**After: Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### The tide bell

- The harbour has a tide bell that rings itself when the swell is over two metres.
- Nobody in town will say who installed the tide bell. Pell claims it predates the lighthouse.
- People set their clocks by the tide bell even though it's never on time.
````

**Run log**

````markdown
I migrated three bullets from the 2026-10-01 entry into `project/Ideas/idea-harrow-point.md`. Nothing else qualified. I didn't touch the Brain Dump doc and wrote no `migrated-to` pointers, because the corrections file says a separate script writes those.

### Run log

**What triggered the run.** Two comments in the 2026-10-01 entry:
- `%% migrate all the bullets between "- The harbour has a tide bell" to "People set their clocks" %%` picks out lines 10 to 12.
- `%% Agent, these go in idea-harrow-point. %%` names the destination.

**What I migrated.** The three bullets in that range, which all describe the tide bell. They went into the Idea Note under a new heading, **The tide bell**. They have no status tag, so they stay tentative (the default) and carry no tag in the Idea Note. Each bullet keeps the writer's meaning, details and hedges, including "Pell claims" and "never on time." The only rewording is "it" → "the tide bell," so each line makes sense without the line before it. I added no block IDs because nothing points at these lines.

**What I didn't migrate, and why.**
- **Line 13, "And because of that, the ferry timetable is basically fiction. This one should live with the town stuff too."** It sits outside the range the comment names. The "town stuff" request is written in plain text, not inside a `%% %%` comment, and the rules say only status tags and comments trigger migration. There's also no town note yet. If you want it migrated, add a comment. It depends on line 12 (the clocks), so it needs that context wherever it goes.
- **2026-09-29 entry.** It has no status tags and no comments. "Definitely keeping this" (the Mara line) is plain text, so it doesn't count as a commit, and `#town` isn't a status tag. None of those lines migrated, and `char-mara.md` is unchanged. If you meant to commit the Mara line, tag it `#status/committed` and it can go straight to her character note.
- **No bookmark.** I couldn't find a record of where the last migration run stopped, so I read the whole Brain Dump doc. Only the comments above asked for migration.

### Unit record

| Unit | Source line (brain-dump.md, 2026-10-01) | Copied to |
| --- | --- | --- |
| Tide bell rings itself above a two-metre swell | L10 "The harbour has a tide bell that rings itself when the swell is over two metres." | `project/Ideas/idea-harrow-point.md` |
| Nobody will say who installed it; Pell's claim | L11 "Nobody in town will say who installed it. Pell claims it predates the lighthouse." | `project/Ideas/idea-harrow-point.md` |
| Clocks set by the bell | L12 "People set their clocks by it even though it's never on time." | `project/Ideas/idea-harrow-point.md` |
````
