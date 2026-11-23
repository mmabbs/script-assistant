# 2026-10-01 Bare Run: Lost Detail Cases 1-4

This run was done by hand outside `claude plugin eval`. The results were graded by script (code checks) and by Claude Fable 5.1 (judge checks), not by the eval tool's grader pipeline.

## What Was Run

- **Date:** 2026-10-01
- **Model:** `claude-opus-5-5`
- **Runs:** 12 total. Four cases, three runs each.
- **Launch method:** `claude -p` child sessions with `--setting-sources project` so no personal rules or hooks loaded. Tools limited to Read, Write, Edit, Glob, Grep. Permission mode: `--permission-mode acceptEdits`.
- **Rules given:** the only rules file was `terminology-script-asst.md`. The file `corrections.md` did not exist yet.

Prompt used verbatim:

> This folder holds a screenwriting project. The file rules/terminology-script-asst.md explains how the project's notes work. Read it first. Then do a migration run: read project/brain-dump.md and migrate what the writer's status tags and comments point at, following the rules. Edit the notes directly. When you finish, reply with a short run log: what you migrated, where it went, and why.

## Summary Table

| Case | Passed | Cost (list price) |
| --- | --- | --- |
| lost-detail-01-plain-copy | 3/3 | $1.08 |
| lost-detail-02-split-across-notes | 3/3 | $0.90 |
| lost-detail-03-area-note-rewrite | 3/3 | $0.76 |
| lost-detail-04-existing-text | 3/3 | $0.74 |
| **Total** | **12/12** | **$3.48** |

All four cases passed 3 of 3 against their Pass lines.

## Findings

1. Every run wrote `migrated-to` pointers into the Brain Dump doc, because `terminology-script-asst.md` says the agent writes them. The pre-writing graph gives that job to the Run script. The user ruled that the graph's version stands. This is why `corrections.md` now exists.
2. The pointers were written as short links such as `[[idea-mara-lighthouse]]`. The user ruled that a pointer must use the full vault path with display text.
3. In case 2, two of three runs repeated the drowning in the habits line and one did not. The user ruled that repeating it is fine.
4. The four cases are too easy to separate a Migrator from bare Claude given the rules. All passed on every run.

## Caveats

The code checks were run by script. The judged checks were done by Claude Fable 5.1 reading each output, and the same session wrote the cases. The fixtures are one or two bullets each.

## Full Outputs

## Bare Claude run on the four Migrator cases

Run on 2026-10-01. Model: claude-opus-5-5. No agent, no skill, no personal rules. Each run was given only the fixture project and a copy of terminology-script-asst.md.

For each run: the notes as bare Claude left them, then its run log.

### Case 1: Plain copy with specifics

#### Run 1

**brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional [migrated-to:: [[idea-mara-lighthouse]]]
- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat. [migrated-to:: [[idea-mara-lighthouse]]]

%% migrate all the bullets between "- Mara's lighthouse" to "Maybe the lamp failed" %%

%% Agent, these go in idea-mara-lighthouse. %%
````

**Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lighthouse and Mara's family

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional
- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat.
````

**Run log**

````markdown
### Run log: migration, 2026-10-01

**What triggered it:** There were two writer comments under the 2026-10-01 entry. The first says to migrate the bullets from "- Mara's lighthouse" through "Maybe the lamp failed". I read that range as including both ends, so it covers both bullets. The second names the destination: `idea-mara-lighthouse`.

**What I migrated: 2 Idea Units → `project/Ideas/idea-mara-lighthouse.md`**

1. **"Mara's lighthouse has 214 steps…"** stays **provisional**, because the writer tagged it `#status/provisional`. I copied the tag into the Idea Note, since migrating never changes status. All the details came across: 214 steps, counted aloud every night, a habit from her father.
2. **"Maybe the lamp failed on March 3…"** stays **tentative**. It had no tag, no parent bullet and no comment setting its status, so it gets the default. I didn't add a tag, because tentative is also the Idea Note's default. I kept "Maybe" and "Not sure if it's too neat" word for word. The second is a note-to-self that gives a reason, so it's rationale and stays with its unit.

**Idea Note layout:** The note had no content yet. I added one heading, "The lighthouse and Mara's family", because both units are about the lighthouse and Mara's family history. I didn't reword either unit; they already read clearly.

**Brain Dump doc:** I added `[migrated-to:: [[idea-mara-lighthouse]]]` to the end of both source lines. Nothing else changed: no wording, no status tags, and both comments are still there.

**What I didn't do:**
- **No block IDs:** nothing points at either line.
- **No relationship links:** the lamp failure doesn't depend on the step-counting, and neither replaces or competes with the other.
- **No Work Items:** there were no `- [?]` lines to carry over, and this run doesn't flag Gaps.
- **No new Idea Note:** your comment named the existing one.
- **No run-log note file:** the rules haven't decided where a run log lives or what form it takes, so this message is the log.
````

#### Run 2

**brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional [migrated-to:: [[idea-mara-lighthouse]]]
- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat. [migrated-to:: [[idea-mara-lighthouse]]]

%% migrate all the bullets between "- Mara's lighthouse" to "Maybe the lamp failed" %%

%% Agent, these go in idea-mara-lighthouse. %%
````

**Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lighthouse

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional
- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat.
````

**Run log**

````markdown
### Run log: migration, 2026-10-01

**Read:** `project/brain-dump.md` (entry dated 2026-10-01) and `project/Ideas/idea-mara-lighthouse.md`.

**What triggered it:** two comments from you, no new tags. The first said which bullets migrate. The second said where they go. Following 06.5, I migrated only what those comments pointed at.

**Migrated:**

1. **"Mara's lighthouse has 214 steps… a habit from her father."** Moved to `idea-mara-lighthouse`, under a new heading, *The lighthouse*.
   - Its status stays provisional. Your tag `#status/provisional` went with it to the Idea Note, because migrating never changes status (03.13). Provisional material belongs in Idea Notes, not Area Notes (03.4).
2. **"Maybe the lamp failed on March 3… Not sure if it's too neat."** Moved to the same note, under the same heading.
   - It has no tag, so it's tentative by default (03.7). I didn't add a tag, since untagged lines in an Idea Note are already tentative.
   - I kept your wording exactly, including "Maybe" and "Not sure if it's too neat." That second phrase is your reason for doubting the idea, so it stays with the line (02.3, 01.3).

**Source lines:** both brain-dump lines are still there and unchanged. Each one now ends with `[migrated-to:: [[idea-mara-lighthouse]]]` (04.7). I added no status tags to the brain dump.

**Not done, and why:**
- **No block IDs and no `depends_on` link.** Nothing points at either line. The lamp failing doesn't rely on the step-counting habit being true.
- **No Gaps.** Gaps are a separate run (05.3), so this run doesn't open any.
- **No new Idea Note.** You named an existing one.
- **Your comments are untouched.** The agent never removes anything from the brain dump.

**One judgment call:** your first comment said to migrate the bullets "between" the two lines. If "between" excluded the two lines named, nothing would migrate, so I read it as including both ends: both bullets.
````

#### Run 3

**brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional [migrated-to:: [[idea-mara-lighthouse]]]
- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat. [migrated-to:: [[idea-mara-lighthouse]]]

%% migrate all the bullets between "- Mara's lighthouse" to "Maybe the lamp failed" %%

%% Agent, these go in idea-mara-lighthouse. %%
````

**Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lighthouse and Mara's nights

- Mara's lighthouse has 214 steps, and she counts them aloud every night, a habit from her father. #status/provisional
- Maybe the lamp failed on March 3, the night her brother's boat went out. Not sure if it's too neat.
````

**Run log**

````markdown
### Run log: migration run, 2026-10-01

**What I read:** `project/brain-dump.md` (the 2026-10-01 entry), `project/Ideas/idea-mara-lighthouse.md` (it was empty apart from its heading), and the rules.

**What started the migration:** Two comments from the writer. The first says to migrate the bullets from "Mara's lighthouse" through "Maybe the lamp failed." I counted both end bullets as included, so that's both bullets in the entry. The second names where they go: `idea-mara-lighthouse`. The rules say only the writer's tags and comments start a migration (06.5), so these two comments were enough.

**What I migrated:**

1. **"Mara's lighthouse has 214 steps… a habit from her father."**
   - Moved to `project/Ideas/idea-mara-lighthouse.md`.
   - It stays **provisional** because the writer tagged it `#status/provisional`. I carried the tag over, since a migration never changes status (03.13).
   - I kept the details as written: 214 steps, counting them aloud every night, the habit coming from her father.

2. **"Maybe the lamp failed on March 3… Not sure if it's too neat."**
   - Moved to the same Idea Note.
   - It stays **tentative**. It has no tag, no comment sets its status, and it has no tagged parent bullet. So it keeps the default status and gets no tag in the Idea Note (03.7).
   - I kept the writer's "Maybe" and the date. "Not sure if it's too neat" is the writer's doubt about the idea, so it stays with the bullet in their own words (01.3, 02.3).

**Where it went:** Both bullets are under one heading, "The lighthouse and Mara's nights," because they're one cluster about the lighthouse. Idea Notes don't use date headings (01.3). I didn't need to reword either bullet to make it readable, so the wording is the writer's.

**Source lines:** Each bullet in the Brain Dump now ends with `[migrated-to:: [[idea-mara-lighthouse]]]` (04.7). I didn't change any of the writer's words there, didn't add status tags, and didn't touch either comment.

**What I didn't do, and why:**
- **No block IDs and no `depends_on` links.** Nothing points at either line. The lamp bullet mentions the lighthouse but doesn't depend on the step-count bullet (04.6).
- **No Questions, Gaps, or Reviews.** This was a migration run, and neither bullet has a `- [?]` the writer typed.
- **No separate run-log note.** The rules haven't settled what a run log looks like or where it lives (01.11), so this reply is the run log.
````

### Case 2: Split across two notes

#### Run 1

**brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Mara's brother Tobias drowned when she was nine. She still sets a place for him at dinner. [migrated-to:: [[idea-tobias]], [[idea-mara-habits]]]

%% Agent, migrate this. The drowning goes in idea-tobias, the dinner habit in idea-mara-habits. %%
````

**Ideas/idea-mara-habits.md**

````markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

## Idea - Mara Habits

### Dinner

- Mara still sets a place for her brother Tobias at dinner, though he drowned when she was nine.
````

**Ideas/idea-tobias.md**

````markdown
---
title: Idea - Tobias
type: [idea-note]
---

## Idea - Tobias

### His death

- Mara's brother Tobias drowned when she was nine.
````

**Run log**

````markdown
### Run log: migration, 2026-10-01

**What I read:** `project/brain-dump.md`. It has one entry, dated 2026-10-01: a single bullet followed by a writer's comment. The bullet has no status tag. The comment is what triggered this migration (06.5).

**What I migrated:** The bullet holds two Idea Units. The comment told me where to split it and where each part goes.

1. **The drowning** went to `project/Ideas/idea-tobias.md`, under a new heading "His death":
   > Mara's brother Tobias drowned when she was nine.

   This is the writer's sentence unchanged.

2. **The dinner habit** went to `project/Ideas/idea-mara-habits.md`, under a new heading "Dinner":
   > Mara still sets a place for her brother Tobias at dinner, though he drowned when she was nine.

   On its own, "She still sets a place for him" wouldn't make sense in this note. So I named who "she" and "him" are and added when he drowned, using only facts from the same bullet. The meaning and the word "still" are kept (01.3).

**Source line:** The brain dump bullet keeps the writer's words. I added `[migrated-to:: [[idea-tobias]], [[idea-mara-habits]]]` at the end of the line (04.7). I removed nothing.

**Status:** Both units are still tentative. The bullet had no tag, and the comment only says where things go, not what status they have, so the default applies (03.2, 03.7). Untagged units in an Idea Note count as tentative, so I added no tags. Migrating never changes status.

**What I didn't add, and why:**
- **Block IDs:** nothing points at either line (04.1).
- **A `depends_on` link from the habit to the drowning:** dependencies track provisional and committed threads, and these units are tentative. That part of the rules is also still marked Open (04).
- **New Idea Notes:** the comment named two notes that already exist.
- **Work Items:** the bullet has no `- [?]` line, and Gaps and Reviews aren't part of a migration run.

**What I couldn't do:** The rules don't say yet what form a run log takes or where it's saved (01.11 is still Open). So this reply is the log, and I didn't write a log note to disk.
````

#### Run 2

**brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Mara's brother Tobias drowned when she was nine. She still sets a place for him at dinner. [migrated-to:: [[idea-tobias]], [[idea-mara-habits]]]

%% Agent, migrate this. The drowning goes in idea-tobias, the dinner habit in idea-mara-habits. %%
````

**Ideas/idea-mara-habits.md**

````markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

## Idea - Mara Habits

### At dinner

- Mara still sets a place for her brother Tobias at dinner.
````

**Ideas/idea-tobias.md**

````markdown
---
title: Idea - Tobias
type: [idea-note]
---

## Idea - Tobias

### His death

- Mara's brother Tobias drowned when she was nine.
````

**Run log**

````markdown
### Run log: migration, 2026-10-01

**What I read:** `project/brain-dump.md`. It has one entry, dated 2026-10-01. That entry is one bullet with no status tag, followed by a writer's comment that says to migrate it.

**What I migrated:** The comment named two destinations for the one bullet, so I split it into two Idea Units (01.2):

1. **The drowning went to `Ideas/idea-tobias.md`**, as "Mara's brother Tobias drowned when she was nine." It sits under a new heading, "His death".
2. **The dinner habit went to `Ideas/idea-mara-habits.md`**, as "Mara still sets a place for her brother Tobias at dinner." It sits under a new heading, "At dinner". In the original, "him" only made sense next to the first sentence. I changed it to "her brother Tobias" so the line reads on its own. That's allowed for readability (01.3). "Still" stays, because it's the writer's specific.

**Why:** The comment told me where each part goes. Only the writer's tags and comments trigger migration (06.5), and this comment did.

**Status:** Both units are tentative. The bullet had no tag, and the comment only said where the material goes, not its status. Idea Notes default to tentative (03.7), so I wrote no status tag. Migrating doesn't change status (03.13).

**Source line:** The writer's words are untouched. I added `[migrated-to:: [[idea-tobias]], [[idea-mara-habits]]]` to the end of the bullet (04.7). The bullet had no `[?]` to remove. I added no block IDs, because nothing points at these lines (04.1).

**Not done:**
- **No new Idea Notes:** both destination notes already existed.
- **No `depends_on` link:** the dinner habit depends on Tobias having died, but both units are tentative. Threads only form from provisional or committed material (03.9), and the dependency fields are still Open, waiting on the ledger.
- **Nothing flagged:** I flagged no Gaps or Reviews. Tentative material never gets Gaps (03.3), and neither kind is flagged in the Brain Dump doc (01.1).
- **No run-log file:** the run log's form and where it lives are still Open (01.11), so this reply is the log.
````

#### Run 3

**brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Mara's brother Tobias drowned when she was nine. She still sets a place for him at dinner. [migrated-to:: [[idea-tobias]], [[idea-mara-habits]]]

%% Agent, migrate this. The drowning goes in idea-tobias, the dinner habit in idea-mara-habits. %%
````

**Ideas/idea-mara-habits.md**

````markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

## Idea - Mara Habits

- Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine.
````

**Ideas/idea-tobias.md**

````markdown
---
title: Idea - Tobias
type: [idea-note]
---

## Idea - Tobias

- Mara's brother Tobias drowned when she was nine.
````

**Run log**

````markdown
### Run log: migration, 2026-10-01

**Read:** `project/brain-dump.md`, entry dated 2026-10-01. It has one bullet with no status tag, and one writer's comment: *"Agent, migrate this. The drowning goes in idea-tobias, the dinner habit in idea-mara-habits."*

**Migrated:** I split the bullet into two Idea Units along the line the comment drew.

1. **"Mara's brother Tobias drowned when she was nine."** This went to `project/Ideas/idea-tobias.md` because the comment named that note. It's in the writer's exact words.
2. **The dinner habit** went to `project/Ideas/idea-mara-habits.md` because the comment named that note. In the source, "She still sets a place for him" only makes sense next to the sentence before it. So I reworded it to stand alone: "Mara still sets a place at dinner for her brother Tobias, who drowned when she was nine." The meaning and specifics are unchanged, and nothing new was added. The drowning detail appears in both notes only so this line reads correctly by itself.

**Status:** Both units are tentative. The writer used no tag and no parent bullet, and the comment only said where the units go, not their status. Tentative is the default in Idea Notes, so I wrote no status tag.

**Source:** The Brain Dump line keeps its words. I added one `migrated-to` pointer at the end of it, listing both notes: `[[idea-tobias]], [[idea-mara-habits]]`. I left the writer's comment in place, since nothing in the Brain Dump doc gets removed.

**Not done, on purpose:**
- **No block IDs:** no other line points at either unit.
- **No `depends_on` link:** the dinner habit relies on the drowning, but both units are tentative, and dependency links are for provisional or committed threads.
- **No headings:** each note holds a single unit, so there's nothing to group yet.
- **No Work Items, Gaps or Reviews:** none were marked, and neither is flagged for tentative material.
- **No new Idea Notes:** both destination notes already existed.

**Open point:** The rules don't say where a run log lives yet (01.11 is still Open), so this log is only in this reply. It isn't saved as a note.
````

### Case 3: Rewrite into an Area Note

#### Run 1

**brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job. I really like this. Tobias as the reason feels more honest than duty. #status/committed [migrated-to:: [[char-mara]]]

%% Agent, this belongs in char-mara. %%
````

**char-mara.md**

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

## Core

### Motivation and Intention

- Mara keeps the lighthouse lamp lit for Tobias, not for ships.
- The town believes Mara keeps the lamp lit only because it is her job.

## Bio

### General

## Psychology

### Values, Beliefs, etc.

## Rationale

- Tobias as the reason feels more honest than duty.

## Rejected
````

**Run log**

````markdown
I migrated one Idea Unit, the 2026-10-01 bullet about Mara and Tobias, from the brain dump to `project/char-mara.md`.

**Why it moved, and where**
- **Why it moved:** The writer tagged the bullet `#status/committed`. Committed material belongs in Area Notes.
- **Why char-mara:** The writer's comment `%% Agent, this belongs in char-mara. %%` named the note.
- **Section:** I put it under **Core › Motivation and Intention**, because the bullet is about why Mara keeps the lamp lit. This placement was my call; the comment only named the note.

**What I wrote in char-mara**
- **Story content**, rewritten as two plain statements:
  - "Mara keeps the lighthouse lamp lit for Tobias, not for ships."
  - "The town believes Mara keeps the lamp lit only because it is her job."
- **Rationale section:** "Tobias as the reason feels more honest than duty." It's copied word for word, because it gives a reason for a story choice and rationale is never rewritten.
- **Dropped:** "I really like this." It's a note-to-self with no reason attached, and Area Notes leave those out.
- **No status tag in char-mara**, because Area Notes don't carry status tags.

**What changed in the brain dump**
- I added `[migrated-to:: [[char-mara]]]` to the end of the source line. I didn't change any of the writer's words or the tag.
- I added no block ID, because nothing points at that line.

**What I didn't do**
- **No new Idea Note:** This is a single committed unit with a named destination, so none was needed.
- **Nothing flagged:** The rules don't allow flagging in the brain dump, and nothing in char-mara contradicts the new lines.
- **No separate run log note:** The rules haven't decided its form or where it lives, so this reply is the log.
- **Tobias is still undefined:** No note says who Tobias is. I kept the name as the writer wrote it and didn't add a Gap, because Gaps belong to a separate Gaps run.
````

#### Run 2

**brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job. I really like this. Tobias as the reason feels more honest than duty. #status/committed [migrated-to:: [[char-mara]]]

%% Agent, this belongs in char-mara. %%
````

**char-mara.md**

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

## Core

### Motivation and Intention

- Mara keeps the lighthouse lamp lit for Tobias, not for the ships. The town believes she keeps it lit only because it is her job.

## Bio

### General

## Psychology

### Values, Beliefs, etc.

## Rationale

- Tobias as the reason feels more honest than duty.

## Rejected
````

**Run log**

````markdown
### Run log: migration, 2026-10-01

**What I read:** `project/brain-dump.md`, which has one entry (2026-10-01). It holds one Idea Unit, tagged `#status/committed`, and an `%% Agent, this belongs in char-mara. %%` comment.

**What I migrated:** the Mara/Tobias unit, from the Brain Dump doc straight into `project/char-mara.md`. The writer's tag committed it and the comment named the note, so it went directly to the Area Note without an Idea Note (03.12).

**Where it went and why:**
- **Story substance** went under *Core → Motivation and Intention*, rewritten as plain statements (03.13): "Mara keeps the lighthouse lamp lit for Tobias, not for the ships. The town believes she keeps it lit only because it is her job." I put it there because the line is about why she does what she does. Every specific is kept: the lamp, Tobias, not ships, and what the town believes.
- **Rationale**, "Tobias as the reason feels more honest than duty.", went to the *Rationale* section in the writer's exact words (02.3). It gives a reason for the choice.
- **Note-to-self**, "I really like this.", was dropped from the Area Note. It's a like with no reason attached (02.2). It stays in the Brain Dump doc as written.

**Source line:** I added `[migrated-to:: [[char-mara]]]` to the end of the Brain Dump line (04.7). The writer's words, the tag and the comment are unchanged.

**One judgment call:** I didn't write a `#status/committed` tag in char-mara. Section 03.2 says the agent writes the writer's status tag where a unit migrates. But 01.4 says Area Notes carry no status tags, and 03.7 says untagged material in an Area Note counts as committed by default. I followed 01.4, since it's the more specific rule for this destination. You may want to settle that conflict in the terminology note.

**Not done:** I added no block IDs because nothing points at these lines, and no Idea Note was needed. Nothing was flagged; Gaps and Reviews aren't part of a migration run.
````

#### Run 3

**brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Mara keeps the lamp lit for Tobias, not for ships, and the town believes she's only doing her job. I really like this. Tobias as the reason feels more honest than duty. #status/committed [migrated-to:: [[char-mara]]]

%% Agent, this belongs in char-mara. %%
````

**char-mara.md**

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

## Core

### Motivation and Intention

- Mara keeps the lighthouse lamp lit for Tobias, not for ships.
- The town believes Mara keeps the lamp lit only because it is her job.

## Bio

### General

## Psychology

### Values, Beliefs, etc.

## Rationale

- Tobias as the reason feels more honest than duty.

## Rejected
````

**Run log**

````markdown
### Run log: migration run, 2026-10-01

**What I read:** `project/brain-dump.md`, which has one entry dated 2026-10-01, and `project/char-mara.md`, which was the target.

**What I migrated:** one Idea Unit, the Mara/Tobias lamp line.
- **Why it migrated:** you tagged it `#status/committed`, and your comment `%% Agent, this belongs in char-mara. %%` names where it goes. Under 06.5 a tag or comment is what triggers migration. A committed unit graduates into an Area Note (03.12).
- **Where it went:** `project/char-mara.md`, under **Core → Motivation and Intention**. I rewrote it as two plain statements (03.13):
  - "Mara keeps the lighthouse lamp lit for Tobias, not for ships."
  - "The town believes Mara keeps the lamp lit only because it is her job."
  
  Both the real motive and what the town believes are kept, because the gap between them is part of the story.
- **Rationale:** "Tobias as the reason feels more honest than duty." This went into char-mara's **Rationale** section word for word, because it gives a reason for a story choice (02.3).
- **Dropped:** "I really like this." It's a bare like with no reason, so it counts as a note-to-self (02.2). Area Notes record the decision, not the deliberation. Your original line in the Brain Dump still has it.
- **No status tag in char-mara:** Area Notes carry no tags, and their default status is already committed (01.4, 03.7).

**Source line:** your words and tag in the Brain Dump are unchanged. I added only `[migrated-to:: [[char-mara]]]` at the end of the line (04.7). I added no block ID, because nothing points at the line yet.

**Not done / flagged:**
- I created no Idea Note. The unit went straight to its Area Note, as your comment said.
- I didn't look for Gaps or Reviews. A migration run doesn't do that, and nothing in the Brain Dump asked for it.
- Tobias has no note of his own, and the dump doesn't say who he is. I named him only as you did and assumed nothing about him.
- I didn't save this run log as a note, because 01.11 leaves its form and location open. This reply is the log.
- There's no bookmark mechanism in the folder, so I treated the whole Brain Dump as new since the last run.
````

### Case 4: Existing text left alone

#### Run 1

**brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- The lamp could run on something stranger than oil. Maybe it burns letters. [migrated-to:: [[idea-mara-lighthouse]]]

%% Agent, migrate this to idea-mara-lighthouse. %%
````

**Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp could run on something stranger than oil. Maybe it burns letters.
````

**Run log**

````markdown
I migrated one Idea Unit, the only one your comment pointed at.

**Read:** `project/brain-dump.md` (the 2026-10-01 entry) and `project/Ideas/idea-mara-lighthouse.md`.

**Migrated**
- **Unit:** "The lamp could run on something stranger than oil. Maybe it burns letters."
- **Where it went:** `project/Ideas/idea-mara-lighthouse.md`, under `## The lamp`, right after the whale-oil line.
- **Why:** your comment `%% Agent, migrate this to idea-mara-lighthouse. %%` sits right under this bullet, and there's nothing else in the entry. A comment counts the same as a tag, so it triggers migration (rules 06.2 and 06.5).
- **Status:** tentative. The line has no tag and no tagged parent, and your comment only says where the unit goes, not its status. Migrating never changes status, so it carries no tag in the Idea Note (rules 03.7 and 03.13).
- **Wording:** copied exactly. "Could" and "Maybe" are your hedges, and an Idea Note has to keep them (rule 01.3).

**Source line:** stays in the Brain Dump, with `[migrated-to:: [[idea-mara-lighthouse]]]` added. Your comment is untouched, and nothing in the Brain Dump was changed or removed (rules 01.1 and 04.7).

**Not done, on purpose**
- **No link to the whale-oil line.** "Burns letters" and "uses whale oil" look like competing takes on the lamp's fuel. You didn't say whether the new idea replaces the old one or sits beside it, so I left the relationship out. If it isn't recorded, I didn't need a block ID either (rule 04.1). Two tentative ideas that contradict each other are normal exploration, so I didn't flag them (rule 03.15). If you want them recorded as competing versions, tell me with a comment.
- **No new Idea Note.** The note you named already exists and has a section on the lamp.
- **No Questions, Gaps, or Reviews added.**
- **No separate run-log note.** Where run logs live and what they look like is still open (rule 01.11), so this reply is the log.
````

#### Run 2

**brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- The lamp could run on something stranger than oil. Maybe it burns letters. [migrated-to:: [[idea-mara-lighthouse]]]

%% Agent, migrate this to idea-mara-lighthouse. %%
````

**Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp could run on something stranger than oil. Maybe it burns letters.
````

**Run log**

````markdown
### Run log: migration, 2026-10-01

**What I read:** `project/brain-dump.md`, which has one entry for 2026-10-01, and `project/Ideas/idea-mara-lighthouse.md` as the destination.

**What triggered the migration:** The only status tag or comment in the brain dump is `%% Agent, migrate this to idea-mara-lighthouse. %%`. It sits right under the one bullet in that entry, so I took "this" to mean that bullet.

**What I migrated:**
- **Unit:** "The lamp could run on something stranger than oil. Maybe it burns letters."
- **Where it went:** `idea-mara-lighthouse.md`, under the existing **The lamp** heading, after the whale-oil line. The heading already covers what the lamp burns.
- **Why it's worded this way:** An Idea Note must keep the writer's meaning, specifics, and hedges (01.3, 03.13). The line was already short and readable, so I kept it word for word, including "could" and "Maybe".
- **Status:** Still tentative, with no tag added. The writer set no tag, and migrating never changes status (03.2, 03.7, 03.13).
- **Source line:** I added `[migrated-to:: [[idea-mara-lighthouse]]]` to the brain-dump line. The writer's words and the comment are otherwise unchanged (01.1, 04.7).

**What I didn't do:**
- **Iteration links:** "Burns letters" competes with the whale-oil line, but I added no `replaces` or `alt_to` link. The writer didn't say it replaces that line or is being tested against it, and I don't infer iteration on my own (04.4, 04.5).
- **The contradiction:** I didn't flag it. Both lines are tentative, and contradictions between tentative ideas are normal exploration (03.15).
- **Block IDs:** I added none, because no other line points at either one (04.1).
- **New Idea Note:** I didn't create one. The comment named an existing note.
- **Work:** I added no Questions or other Work. The unit has no `- [?]` lines.

**What I flagged:** Nothing.
````

#### Run 3

**brain-dump.md**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- The lamp could run on something stranger than oil. Maybe it burns letters. [migrated-to:: [[idea-mara-lighthouse]]]

%% Agent, migrate this to idea-mara-lighthouse. %%
````

**Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp could run on something stranger than oil. Maybe it burns letters.
````

**Run log**

````markdown
### Run log: migration run, 2026-10-01

**What I read:** `project/brain-dump.md`, which has one entry under 2026-10-01, and `project/Ideas/idea-mara-lighthouse.md`.

**What triggered migration:** your comment `%% Agent, migrate this to idea-mara-lighthouse. %%`. The brain dump had no status tags, so that comment was the only trigger.

**What I migrated:**

| Idea Unit | From | To | Status |
| --- | --- | --- | --- |
| "The lamp could run on something stranger than oil. Maybe it burns letters." | `brain-dump.md`, 2026-10-01 | `idea-mara-lighthouse.md`, under **## The lamp** | Tentative, so no tag |

**Why it went where it did:**
- **Destination:** your comment named the note. It went under "The lamp" because that's the heading for the lamp's fuel.
- **Kept as one unit:** "Maybe it burns letters" is one guess at what "something stranger" could be, so the two sentences belong together.
- **Wording:** I copied it word for word. "Could" and "maybe" are your hedges, and an Idea Note keeps them (01.3).
- **Status:** the line had no tag and no tagged parent, and the comment only said where it goes. That makes it tentative, the default (03.7), and migrating doesn't change status (03.13). Untagged lines in an Idea Note are tentative, so I added no tag.

**Changes to the brain dump:** I only added `[migrated-to:: [[idea-mara-lighthouse]]]` to the end of the source line (04.7). Your words and your comment are unchanged.

**What I flagged:** nothing.
- The new line competes with "The lamp uses whale oil…", but both are tentative. Contradictions between tentative ideas are normal exploration and don't get flagged (03.15).
- I didn't add an `alt_to` link or block IDs. You didn't say the two are competing versions, and the relationship fields are still open pending the ledger (04.1 callout). If you want them linked, tell me in a comment.

**What I couldn't do:** I didn't write a separate run-log note. Its form and location are still open for the graph session (01.11), so this reply is the log.
````
