# 2026-10-01 Bare Run: Lost Detail Cases 5-8

This run was done by hand outside `claude plugin eval`. The results were graded by script (code checks) and by Claude Fable 5.1 (judge checks), not by the eval tool's grader pipeline.

## What Was Run

- **Date:** 2026-10-01
- **Model:** `claude-opus-5-5`
- **Runs:** 12 total. Four cases, three runs each.
- **Launch method:** `claude -p` child sessions with `--setting-sources project` so no personal rules or hooks loaded. Tools limited to Read, Write, Edit, Glob, Grep. Permission mode: `--permission-mode acceptEdits`.
- **Rules given:** `terminology-script-asst.md` and `corrections.md`.

Prompt used verbatim:

> This folder holds a screenwriting project. The files in rules/ explain how the project's notes work. Read rules/terminology-script-asst.md first, then rules/corrections.md, which is newer and wins where they differ. Then do a migration run: read project/brain-dump.md and migrate what the writer's status tags and comments point at, following the rules. Edit the notes directly. When you finish, reply with a short run log: what you migrated, where it went, and why.

## Summary Table

| Case | Passed | Cost (list price) |
| --- | --- | --- |
| lost-detail-05-dense-bullet | 2/3 | $0.84 |
| lost-detail-06-area-note-populated | 3/3 | $0.98 |
| lost-detail-07-batch-two-notes | 3/3 | $0.89 |
| lost-detail-08-merge-by-comment | 3/3 | $0.73 |
| **Total** | **11/12** | **$3.43** |

## Findings

1. **Case 5, run 3, let a hedge drift.** The writer wrote "I'm thinking a woman named Ansel." Run 3 kept that hedge on one line, then used "Ansel" as a settled name on four other lines. Runs 1 and 2 said "the keeper before Mara" on the other lines. Moe ruled it technically a fail, and a small one. He also ruled that run 1's repeat of the hedge in a later section was unnecessary, and not a fail.
2. **The corrections file worked.** No run touched the Brain Dump doc, and every run log ended with a unit record.
3. **One run added context from a neighbouring line.** Case 7, run 1, wrote "the Drowned Bell, the town pub" and "Coyle, the Drowned Bell's landlord" in the storm-night note. That fits the ruling in eval-cases-migrator.md 06.3 item 3.
4. **There is still little room to improve.** Lost detail did not appear at fourteen bullets. It may only appear at real scale, on real material. The failures about status calls and restraint may separate a Migrator from bare Claude better.

## Caveats

The code checks were run by script. The judged checks were done by Claude Fable 5.1 reading each output, in the same session that wrote the cases. The user approved the Pass lines for cases 5 to 8 after the run, and ruled the case 5 run 3 hedge drift a fail, though a small one.

## Full Outputs

## Bare Claude run on the four harder Migrator cases

Run on 2026-10-01. Model: claude-opus-5-5. No agent, no skill, no personal rules. Each run was given the fixture project, a copy of terminology-script-asst.md, and corrections.md.

For each run: the notes as bare Claude left them, then its run log. The Brain Dump doc is shown once per case, because no run changed it.

### Case 5: Dense bullet into a populated Idea Note

**brain-dump.md (unchanged by every run)**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Okay so the keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step? Maybe she logged every ship that didn't come back, 31 of them, going back to 1987. Does Mara find it, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out. What if the last entry is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.

%% Agent, migrate this to idea-mara-lighthouse. %%
````

#### Run 1

**Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.

### The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
- The keeper before Mara: I'm thinking a woman named Ansel.

### The second logbook

- The keeper before Mara (I'm thinking Ansel) kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?
- Maybe she logged every ship that didn't come back in the second logbook, 31 of them, going back to 1987.
- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.
- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.
````

**Run log**

````markdown
### Run log: migration, 2026-10-01

**What I read:** `rules/terminology-script-asst.md`, `rules/corrections.md`, `project/brain-dump.md` and `project/Ideas/idea-mara-lighthouse.md`.

**What triggered the migration:** The only trigger was the writer's comment `%% Agent, migrate this to idea-mara-lighthouse. %%`. It points at the one bullet above it, under 2026-10-01. The brain dump has no status tags.

**What I migrated:** I copied that bullet into `project/Ideas/idea-mara-lighthouse.md` as five Idea Units.
- **Ansel's name:** I put this under the existing heading **The keeper before Mara**, since it's about who that keeper was.
- **The logbook:** I added a new heading, **The second logbook**, for the four units about it. The bullet is mostly about the logbook, so it reads better as its own group than packed under the keeper heading.

**How I handled it:**
- **Status:** Nothing is tagged, so every unit is tentative (the Idea Note default). I wrote no status tags.
- **Hedges:** I kept the writer's hedges and specifics: "I'm thinking", "Maybe", "What if", "possibly", 31 ships, 1987, the 40th step, Pell the harbourmaster.
- **Context:** Each unit names the second logbook (or "the keeper before Mara") so it makes sense on its own line (corrections item 3).
- **Questions:** The writer's questions are in plain prose, not marked `- [?]`. So they stay inside their units' words and aren't tracked as Work.
- **Block IDs:** I added none, because nothing points at these lines.
- **Brain Dump:** I didn't touch the Brain Dump doc and wrote no `migrated-to` pointers (corrections item 1).
- **Overlap I left alone:** The note already says "The last keeper left without telling anyone. Maybe she was pushed out." That probably means Ansel, but the writer hasn't said so, so I didn't merge the two or link them.

**Not done / flagged:** Nothing. No new Idea Note was needed because the writer named where the material goes.

#### Unit record
Source for all five units: `project/brain-dump.md`, line 10 (2026-10-01 bullet). Each went to `project/Ideas/idea-mara-lighthouse.md`.

| # | Source text (from line 10) | Destination heading |
|---|---|---|
| 1 | "the keeper before Mara, I'm thinking a woman named Ansel" | The keeper before Mara |
| 2 | "…kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?" | The second logbook |
| 3 | "Maybe she logged every ship that didn't come back, 31 of them, going back to 1987." | The second logbook |
| 4 | "Does Mara find it, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out." | The second logbook |
| 5 | "What if the last entry is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell." | The second logbook |
````

#### Run 2

**Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.

### The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
- The keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about.

#### The second logbook

- Is the keeper's second logbook hidden in the lamp room or under the 40th step?
- Maybe the keeper before Mara logged every ship that didn't come back in the second logbook, 31 of them, going back to 1987.
- Does Mara find the second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.
- What if the last entry in the second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.
````

**Run log**

````markdown
### Run log: migration run, 2026-10-01

**Read:** `rules/terminology-script-asst.md`, `rules/corrections.md`, `project/brain-dump.md`, `project/Ideas/idea-mara-lighthouse.md`

**What triggered it:** The brain dump had one comment, `%% Agent, migrate this to idea-mara-lighthouse. %%`, under the single bullet in the 2026-10-01 entry. There were no status tags.

**What I migrated:** That bullet went into `project/Ideas/idea-mara-lighthouse.md` as five units. All five are tentative, because the bullet had no tag and untagged material in an Idea Note is tentative. So I wrote no status tags.

**Where it went and why:**
- **Under the existing "The keeper before Mara" heading:** the unit naming Ansel and the second logbook. It's about the same keeper as the line already there.
- **Under a new "The second logbook" subheading:** the logbook's details, as one train of thought.
- **Each unit names its subject** ("the keeper's second logbook", "the keeper before Mara"), so it still makes sense once split off from the original bullet.
- **Hedges kept:** "I'm thinking", "Maybe", "What if", "possibly".
- **I didn't spread the name "Ansel" to the other units.** It's hedged in your words, and repeating it would make it read as settled.
- **Your questions stay as prose inside their units.** You didn't mark any with `- [?]`, so none of them are tracked as Questions.
- **Your notes-to-self stay too.** For example, "I'll need to figure out who else had a key" is kept, because Idea Notes keep them.
- **Each Tobias question stays with its follow-on sentence.** "If Tobias found it first…" only makes sense with the question before it. Likewise, the key/Pell sentence stays with the handwriting question it follows from.

**Not done, and why:**
- **The brain dump isn't touched, and it has no `migrated-to` pointer.** `corrections.md` item 1 says not to edit it; a script adds the pointers later.
- **No block IDs.** Nothing points at these lines yet.
- **No new Idea Note.** You named the destination.
- **Nothing flagged.** "Left without telling anyone / maybe pushed out" and the new Ansel material don't clash, and they're all tentative ideas anyway, so I wouldn't flag a contradiction there.

**Unit record** (source: `project/brain-dump.md`, 2026-10-01, line 10; destination: `project/Ideas/idea-mara-lighthouse.md` for every unit):

| # | Source sentences | Destination |
|---|---|---|
| 1 | "Okay so the keeper before Mara, I'm thinking a woman named Ansel, kept a second logbook nobody knew about." | "The keeper before Mara" |
| 2 | "Is it hidden in the lamp room or under the 40th step?" | "The second logbook" |
| 3 | "Maybe she logged every ship that didn't come back, 31 of them, going back to 1987." | "The second logbook" |
| 4 | "Does Mara find it, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out." | "The second logbook" |
| 5 | "What if the last entry is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell." | "The second logbook" |
````

#### Run 3

**Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.

### The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
- I'm thinking the keeper before Mara is a woman named Ansel.
- Ansel kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?
- Maybe in the second logbook Ansel logged every ship that didn't come back, 31 of them, going back to 1987.
- Does Mara find Ansel's second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out.
- What if the last entry in Ansel's second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell.
````

**Run log**

````markdown
I moved the single brain-dump bullet about the keeper before Mara into `project/Ideas/idea-mara-lighthouse.md`. I didn't touch the Brain Dump doc and didn't add any `migrated-to` pointers, because `corrections.md` says not to.

**What triggered it:** the writer's comment `%% Agent, migrate this to idea-mara-lighthouse. %%` (`brain-dump.md:12`) points at the only bullet in the 2026-10-01 entry. The bullet has no status tag, so it stays tentative. That is already the Idea Note's default, so I didn't add a tag.

**Where it went:** under the existing heading "The keeper before Mara", after the line already there. That heading is about the same keeper, so I didn't create a new heading or note.

**How it was handled:**
- **Split into five units:** one each for Ansel's name, the hidden logbook, the 31 lost ships, who finds the logbook, and the handwriting and key.
- **Hedges kept:** "I'm thinking", "Maybe", "What if", "possibly" and "I'll need to figure out" all stay. Under the rules, an Idea Note keeps notes-to-self as written.
- **Specifics kept:** the lamp room or the 40th step, 31 ships, 1987, Tobias and the boat, and Pell the harbourmaster.
- **Context added:** units after the first say "Ansel's second logbook" or "the second logbook" where the original said "it", so each line makes sense on its own (corrections item 3).
- **Questions left as prose:** the writer didn't mark any as `- [?]`, so I didn't make them into Work Items.
- **Nothing else added:** no block IDs, since nothing points at these lines. I didn't record any lineage, replacement or dependency links either.

**Possible connection, not acted on:** the existing line "The last keeper left without telling anyone. Maybe she was pushed out." may be about Ansel. The writer didn't say so, so I didn't link or merge them. Both are tentative.

**Unit record** (every source line is the bullet at `project/brain-dump.md:10`):

| # | Unit (as it now reads) | Source text | Went to |
|---|---|---|---|
| 1 | I'm thinking the keeper before Mara is a woman named Ansel. | "the keeper before Mara, I'm thinking a woman named Ansel" | idea-mara-lighthouse |
| 2 | Ansel kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step? | "kept a second logbook nobody knew about. Is it hidden in the lamp room or under the 40th step?" | idea-mara-lighthouse |
| 3 | Maybe in the second logbook Ansel logged every ship that didn't come back, 31 of them, going back to 1987. | "Maybe she logged every ship that didn't come back, 31 of them, going back to 1987." | idea-mara-lighthouse |
| 4 | Does Mara find Ansel's second logbook, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out. | "Does Mara find it, or does Tobias find it first? If Tobias found it first, that changes why he took the boat out." | idea-mara-lighthouse |
| 5 | What if the last entry in Ansel's second logbook is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell. | "What if the last entry is in a different handwriting? I'll need to figure out who else had a key, possibly the harbourmaster, Pell." | idea-mara-lighthouse |
````

### Case 6: Long committed bullet into a populated Area Note

**brain-dump.md (unchanged by every run)**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Mara took over the lighthouse at nineteen, the winter after her father's stroke, and she has never once let the lamp go dark, not even on the night of Tobias's funeral. I really want to keep this. She keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it. The coat works better than a photograph because she has to walk past it every day. #status/committed

%% Agent, this belongs in char-mara. %%
````

#### Run 1

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

## Bio

### General

- Mara has kept the lighthouse for eleven years.
- Mara's younger brother Tobias drowned six years ago.
- Mara took over the lighthouse at nineteen, the winter after her father's stroke.
- Mara has never once let the lamp go dark, not even on the night of Tobias's funeral.
- Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it.

## Psychology

### Values, Beliefs, etc.

## Rationale

- A lighthouse keeper who is afraid of the sea is the whole joke of her.
- The coat works better than a photograph because she has to walk past it every day.

## Rejected
````

**Run log**

````markdown
### Run log: migration, 2026-10-01

**What I read:** `project/brain-dump.md`, which has one dated entry (2026-10-01), and `project/char-mara.md`, the Area Note the entry was sent to.

**What triggered the migration:** The single bullet is tagged `#status/committed`, and a comment under it says `%% Agent, this belongs in char-mara. %%`. A committed unit goes to an Area Note (terminology 03.5, 03.12), and the comment names which one. Nothing else in the Brain Dump has a tag or comment, so nothing else moved.

**What I migrated and where it went:** Everything went to `project/char-mara.md`. Area Note units are rewritten as plain statements (03.13), so I split the bullet into separate facts:
- **Story substance**, added under *Bio > General*, next to the existing lines about her time at the lighthouse and Tobias:
  - "Mara took over the lighthouse at nineteen, the winter after her father's stroke."
  - "Mara has never once let the lamp go dark, not even on the night of Tobias's funeral."
  - "Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it."
- **Rationale**, added word for word to the *Rationale* section: "The coat works better than a photograph because she has to walk past it every day." It gives a reason for a story choice, so it can't be rewritten (02.3).
- **Dropped:** "I really want to keep this." It's a note-to-self with no reason attached, so it doesn't go into an Area Note (02.2).

**What I didn't do, and why:**
- **Brain Dump left untouched.** `corrections.md` item 1 forbids editing it, so it has no `migrated-to` pointer. The separate script will add that.
- **No block IDs added**, because nothing points at these lines.
- **No Gaps or Reviews proposed.** This is a migration run. The new lines fit what was already there: she took over at 19 and has kept the lighthouse for 11 years, so she's 30. Tobias drowned 6 years ago. I found no committed contradiction.
- **No new Idea Note.** The comment sent the material straight to the Area Note.

**Judgment call:** The rationale line says "The coat" without naming Tobias's oilskin. Rationale has to stay in your words, so I left it as is. It sits in Mara's note right next to the coat line, so it should still read clearly.

#### Unit record

| Unit | Source line | Copy went to |
| --- | --- | --- |
| Took over the lighthouse at nineteen, after her father's stroke | brain-dump.md:10 (sentence 1, first part) | char-mara.md: Bio > General |
| Never let the lamp go dark, even on the night of Tobias's funeral | brain-dump.md:10 (sentence 1, second part) | char-mara.md: Bio > General |
| Keeps Tobias's oilskin coat by the door; nobody may move it | brain-dump.md:10 (sentence 3) | char-mara.md: Bio > General |
| Rationale: the coat works better than a photograph | brain-dump.md:10 (sentence 4) | char-mara.md: Rationale |
| "I really want to keep this." (note-to-self) | brain-dump.md:10 (sentence 2) | Not migrated (dropped) |
````

#### Run 2

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

## Bio

### General

- Mara has kept the lighthouse for eleven years.
- Mara's younger brother Tobias drowned six years ago.
- Mara took over the lighthouse at nineteen, the winter after her father's stroke.
- Mara has never once let the lighthouse lamp go dark, not even on the night of Tobias's funeral.
- Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it.

## Psychology

### Values, Beliefs, etc.

## Rationale

- A lighthouse keeper who is afraid of the sea is the whole joke of her.
- The coat works better than a photograph because she has to walk past it every day.

## Rejected
````

**Run log**

````markdown
### Run log: migration, 2026-10-01

**What I read:** `project/brain-dump.md`, which has one entry dated 2026-10-01. It holds one bullet tagged `#status/committed`, followed by the comment `%% Agent, this belongs in char-mara. %%`. That bullet is the only thing a tag or comment pointed at, so it's the only thing I migrated.

**What I migrated and where:** The whole bullet went to `project/char-mara.md`. It went straight from the Brain Dump to the Area Note. The tag makes it committed material, so it belongs in an Area Note, and the comment named this note.

- **Story substance:** I split it into three plain statements under Bio > General, next to the existing timeline facts there:
  - Mara took over the lighthouse at nineteen, the winter after her father's stroke.
  - Mara has never once let the lighthouse lamp go dark, not even on the night of Tobias's funeral.
  - Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it.
- **Rationale:** "The coat works better than a photograph because she has to walk past it every day." This gives a reason for a story choice, so it went into the Rationale section in your exact words.
- **Dropped:** "I really want to keep this." It's a like with no reason attached, so it counts as a note-to-self. Those get dropped when material is rewritten into an Area Note.
- **Status tag:** I didn't add one in char-mara, because Area Notes carry no status tags.

**What I didn't do:**
- **Brain Dump untouched:** Following `corrections.md` item 1, I made no edits to the Brain Dump at all. That means no `migrated-to` pointer and no block ID; your separate script will write the pointer.
- **No new note:** Everything fit in an existing Area Note.
- **Flags:** Nothing was flagged. The new facts fit the ones already in the note. Eleven years as keeper, starting at nineteen, makes Mara about 30, and Tobias's death six years ago falls inside her time as keeper.

**Unit record:**

| Unit | Source line | Went to |
| --- | --- | --- |
| Took over the lighthouse at nineteen, after father's stroke | brain-dump.md:10 | char-mara.md, Bio > General |
| Never let the lamp go dark, not even the night of Tobias's funeral | brain-dump.md:10 | char-mara.md, Bio > General |
| Keeps Tobias's oilskin coat by the door, nobody may move it | brain-dump.md:10 | char-mara.md, Bio > General |
| Rationale: coat works better than a photograph… | brain-dump.md:10 | char-mara.md, Rationale |
| (Routing comment) | brain-dump.md:12 | Used for routing, not migrated |
````

#### Run 3

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

## Bio

### General

- Mara has kept the lighthouse for eleven years.
- Mara's younger brother Tobias drowned six years ago.
- Mara took over the lighthouse at nineteen, the winter after her father's stroke.
- Mara has never once let the lighthouse lamp go dark, not even on the night of Tobias's funeral.
- Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it.

## Psychology

### Values, Beliefs, etc.

## Rationale

- A lighthouse keeper who is afraid of the sea is the whole joke of her.
- The coat works better than a photograph because she has to walk past it every day.

## Rejected
````

**Run log**

````markdown
### Run log: migration, 2026-10-01

**What I read:** `project/brain-dump.md`, which has one entry dated 2026-10-01. It is a single bullet tagged `#status/committed`, followed by the comment `%% Agent, this belongs in char-mara. %%`.

**What triggered the migration:** the writer's `#status/committed` tag, plus the comment naming the destination. Nothing else in the Brain Dump doc carries a tag or comment.

**Where it went:** all of it went to `project/char-mara.md`. The comment named that note, and the material only concerns Mara, so no Concept Note or Idea Note was needed.

- **Bio > General:** three plain statements, rewritten from the bullet. I spelled out "Mara" and "Tobias" in each line so every line makes sense on its own. I made one small clarification: "the lamp" became "the lighthouse lamp."
- **Rationale:** "The coat works better than a photograph because she has to walk past it every day." This is the writer's reason for keeping the coat, so I copied it word for word.
- **Dropped:** "I really want to keep this." It's a note-to-self with no reason attached, so it isn't rationale. Area Notes drop those.
- **No status tags written:** Area Notes don't carry them.
- **No block IDs added:** nothing points at these lines.

**Contradiction check:** I found no conflict with the lines already in `char-mara.md`. Taking over the lighthouse at nineteen and keeping it for eleven years makes her about 30. Tobias drowned six years ago, while she was already the keeper, so being on duty the night of his funeral fits.

**What I didn't do:** following `rules/corrections.md` item 1, I didn't edit the Brain Dump doc and wrote no `migrated-to` pointers. A separate script adds those.

#### Unit record

| Unit | Source line | Copy went to |
|---|---|---|
| Mara took over the lighthouse at nineteen, the winter after her father's stroke. | `brain-dump.md` line 10 | `char-mara.md` → Bio > General |
| Mara has never once let the lighthouse lamp go dark, not even on the night of Tobias's funeral. | `brain-dump.md` line 10 | `char-mara.md` → Bio > General |
| Mara keeps Tobias's oilskin coat on the hook by the door, and nobody is allowed to move it. | `brain-dump.md` line 10 | `char-mara.md` → Bio > General |
| The coat works better than a photograph because she has to walk past it every day. (rationale) | `brain-dump.md` line 10 | `char-mara.md` → Rationale |
| I really want to keep this. (note-to-self) | `brain-dump.md` line 10 | Not migrated (dropped) |
````

### Case 7: Batch of fourteen bullets to two Idea Notes

**brain-dump.md (unchanged by every run)**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- The town is called Harrow Point and it has exactly one road in, which floods at spring tide.
- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days.
- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute.
- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow.
- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?
- The school closed two winters ago, the kids take the ferry to Marrow Bay, which means on bad days they just don't go.
- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him.

%% migrate all the bullets between "- The town is called Harrow Point" to "Could be that the harbourmaster" %%

%% Agent, these go in idea-harrow-point. %%

#### 2026-09-30

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

**Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### Getting in and out

- The town is called Harrow Point and it has exactly one road in, which floods at spring tide.
- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days.
- The school closed two winters ago. The kids take the ferry to Marrow Bay, which means on bad days they just don't go.

### The Drowned Bell

- There's a pub in Harrow Point, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute.
- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?

### Work and offices

- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow.
- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him.
````

**Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

## Idea - Storm Night

### The lamp failure

- On the storm night, I want the lamp to fail for exactly eleven minutes, not the whole night.
- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell, the town pub, for a wedding.

### Tobias leaves

- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock.
- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close.

### Mara in the watch room

- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing.

### Afterward

- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet.
- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, the Drowned Bell's landlord, and said nothing for six years.
````

**Run log**

````markdown
I migrated all 14 bullets into the two Idea Notes your comments named. I didn't create any new notes.

**Run log: migration, 2026-10-01**

**What I read:** `rules/terminology-script-asst.md`, `rules/corrections.md`, `project/brain-dump.md`, and the two Idea Notes, which were both empty.

**What triggered migration:** two pairs of comments in the brain dump.
- **2026-10-01:** one comment said to migrate the bullets from "The town is called Harrow Point" to "Could be that the harbourmaster". A second comment sent them to `idea-harrow-point`. That's 7 bullets.
- **2026-09-30:** one comment said to migrate the bullets from "The storm night" to "I keep coming back". A second comment sent them to `idea-storm-night`. That's 7 bullets.

**How I handled them:**
- **Status:** none of the bullets had a tag or a comment setting status, so all of them are tentative. That's the default for Idea Notes, so I wrote no status tags. Words like "maybe," "could be" and "I want" stayed as written and didn't change anyone's status.
- **Wording:** I kept your wording, hedges and specifics. Your notes-to-self stayed with their units, including the reason-like "Not sure if that's too cute." I didn't turn any questions into `- [?]` lines; "What if the church bell…" and "which nobody can explain yet" stay inside their units.
- **Organization:** I grouped related bullets under topic headings, with no date headings.
- **Context added (correction 3):** in `idea-storm-night` I described the Drowned Bell as "the town pub" and Coyle as "the Drowned Bell's landlord." Both facts are yours, from the Harrow Point bullets. Without them, those two lines wouldn't make sense on their own in that note.
- **Light rewording:**
  - "The storm night: I want…" became "On the storm night, I want…"
  - The school bullet became two sentences.
  - The pub bullet now reads "a pub in Harrow Point."
- **Not done (correction 1):** I didn't edit the brain dump and didn't write any `migrated-to` pointers. I added no block IDs either, because nothing points at these lines yet.
- **Nothing flagged:** I flagged no contradictions, Gaps or Reviews. Contradictions between tentative ideas are normal exploration, and none of these run types were requested.

**Unit record**

| # | Source line (brain-dump.md) | Went to | Heading |
|---|---|---|---|
| 1 | L10 "The town is called Harrow Point…" | idea-harrow-point | Getting in and out |
| 2 | L11 "Maybe the ferry only runs…" | idea-harrow-point | Getting in and out |
| 3 | L15 "The school closed two winters ago…" | idea-harrow-point | Getting in and out |
| 4 | L12 "There's a pub, the Drowned Bell…" | idea-harrow-point | The Drowned Bell |
| 5 | L14 "What if the church bell was sold in 1994…" | idea-harrow-point | The Drowned Bell |
| 6 | L13 "Thinking the fishing fleet is down to six…" | idea-harrow-point | Work and offices |
| 7 | L16 "Could be that the harbourmaster, Pell…" | idea-harrow-point | Work and offices |
| 8 | L24 "The storm night: I want the lamp to fail…" | idea-storm-night | The lamp failure |
| 9 | L28 "Possibly the lamp failed because the backup generator…" | idea-storm-night | The lamp failure |
| 10 | L25 "Tobias took the skiff…" | idea-storm-night | Tobias leaves |
| 11 | L26 "Maybe he left at 2:40…" | idea-storm-night | Tobias leaves |
| 12 | L27 "Mara was asleep in the watch room…" | idea-storm-night | Mara in the watch room |
| 13 | L29 "There were two flares found…" | idea-storm-night | Afterward |
| 14 | L30 "I keep coming back to the idea that someone saw…" | idea-storm-night | Afterward |
````

#### Run 2

**Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### Getting in and out

- The town is called Harrow Point and it has exactly one road in, which floods at spring tide.
- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days.
- The school closed two winters ago. The kids take the ferry to Marrow Bay, which means on bad days they just don't go.

### The Drowned Bell and the church bell

- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute.
- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?

### Livelihoods and power

- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow.
- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him.
````

**Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

## Idea - Storm Night

### The lamp failure

- I want the lamp to fail for exactly eleven minutes on the storm night, not the whole night.
- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding.

### Tobias leaves

- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock.
- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close.

### Mara in the watch room

- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing.

### Afterward

- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet.
- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years.
````

**Run log**

````markdown
### Run log: migration, 2026-10-01

**What I read:** `project/brain-dump.md`, with entries dated 2026-09-30 and 2026-10-01. The brain dump has no status tags. Each entry ends with two writer comments: one marks which bullets to migrate, and the other names the destination note.

**What I migrated:**
- **2026-10-01 entry:** all 7 bullets, from "The town is called Harrow Point" through "Could be that the harbourmaster", went to `project/Ideas/idea-harrow-point.md`. Your comment named that note.
- **2026-09-30 entry:** all 7 bullets, from "The storm night" through "I keep coming back", went to `project/Ideas/idea-storm-night.md`. Your comment named that note.

I read "between X to Y" as including both the first and last bullet, so both are migrated.

**How I handled it:**
- **Status:** No status tags were written. None of the bullets had a tag or a comment setting a status, so they stay tentative, which is the default in Idea Notes. Words like "Maybe", "Possibly" and "I want" don't set a status.
- **Organisation:** I added topic headings and no date headings. Harrow Point is grouped as: getting in and out; the Drowned Bell and the church bell; livelihoods and power. Storm Night is grouped as: the lamp failure; Tobias leaves; Mara in the watch room; afterward.
- **Wording:** The text is almost word for word. All hedges and notes-to-self stay in place, such as "Not sure if that's too cute", "I keep coming back to the idea" and "nobody can explain yet". Since the Storm Night note drops the "The storm night:" lead-in, I moved "on the storm night" into the lamp line so it still makes sense. I also split the school bullet into two sentences to make it easier to read.
- **What I left out:** I added no `[?]` lines, because prose questions like "What if…" stay inside their unit's words. I added no block IDs, because nothing points at these lines. I didn't write any Gaps or Reviews.
- **Brain dump:** Not edited, and no `migrated-to` pointers were written. The corrections file says the script handles those.
- **Split bullets:** None. Each bullet went whole to one note, so the corrections rule about carrying context didn't apply. Coyle and the Drowned Bell also appear in Storm Night with no explanation, but that note sits next to Harrow Point, so I left them as you wrote them.
- **New Idea Notes:** I didn't create any, because both destination notes already existed.

#### Unit record

| Source line (brain-dump.md) | Went to |
|---|---|
| L10 Harrow Point, one road in, floods at spring tide | idea-harrow-point |
| L11 Ferry Tuesdays and Fridays only | idea-harrow-point |
| L12 Drowned Bell, Coyle's tab for the dead | idea-harrow-point |
| L13 Fishing fleet six from twenty-two, blamed on the lamp | idea-harrow-point |
| L14 Church bell sold in 1994 for the sea wall, the pub's name | idea-harrow-point |
| L15 School closed, kids ferry to Marrow Bay | idea-harrow-point |
| L16 Pell, harbourmaster and only notary | idea-harrow-point |
| L24 Lamp fails for exactly eleven minutes | idea-storm-night |
| L25 Tobias took the skiff, trawler engine in pieces | idea-storm-night |
| L26 Left at 2:40, low water at 3:05 | idea-storm-night |
| L27 Mara asleep in the watch room, radio on ch. 16 | idea-storm-night |
| L28 Backup generator lent to the Drowned Bell | idea-storm-night |
| L29 Two unfired flares on the rocks | idea-storm-night |
| L30 Someone, maybe Coyle, saw the skiff leave | idea-storm-night |
````

#### Run 3

**Ideas/idea-harrow-point.md**

````markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### Getting in and out

- The town is called Harrow Point and it has exactly one road in, which floods at spring tide.
- Maybe the ferry only runs on Tuesdays and Fridays, so anyone who misses it is stuck for three days.
- The school closed two winters ago. The kids take the ferry to Marrow Bay, which means on bad days they just don't go.

### The Drowned Bell

- There's a pub, the Drowned Bell, and the landlord, Coyle, keeps a tab for the dead. Not sure if that's too cute.
- What if the church bell was sold in 1994 to pay for the sea wall, and that's where the pub got its name?

### Work and authority in town

- Thinking the fishing fleet is down to six boats from twenty-two, and people blame the lamp for it somehow.
- Could be that the harbourmaster, Pell, is also the only notary, so every deed in town goes through him.
````

**Ideas/idea-storm-night.md**

````markdown
---
title: Idea - Storm Night
type: [idea-note]
---

## Idea - Storm Night

### The lamp failure

- On the storm night, I want the lamp to fail for exactly eleven minutes, not the whole night.
- Possibly the lamp failed because the backup generator had been lent to the Drowned Bell for a wedding.

### Tobias leaves

- Tobias took the skiff, not the trawler, because the trawler's engine was already in pieces on the dock.
- Maybe he left at 2:40 in the morning. The tide table says low water was at 3:05, so he was cutting it close.

### Mara in the watch room

- Mara was asleep in the watch room with the radio on channel 16, and she swears she heard nothing.

### What was found, and who saw

- There were two flares found on the rocks afterward, both unfired, which nobody can explain yet.
- I keep coming back to the idea that someone saw the skiff leave, maybe Coyle, and said nothing for six years.
````

**Run log**

````markdown
## Run log: migration run, 2026-10-01

**What I read:** `rules/terminology-script-asst.md`, `rules/corrections.md` (where they differ, corrections wins), and `project/brain-dump.md`. Both Idea Notes were empty before this run.

**What started the migration:** Each date block in the brain dump has two comments from the writer. One says which bullets to migrate and the other names the destination note. There are no status tags in the brain dump. Per 06.5, plain prose alone wouldn't have started a migration.

**What I migrated and where it went**
- **2026-10-01 block, 7 bullets → `project/Ideas/idea-harrow-point.md`**, as the writer's comment directed. I grouped them under three headings: Getting in and out, The Drowned Bell, and Work and authority in town.
- **2026-09-30 block, 7 bullets → `project/Ideas/idea-storm-night.md`**, as the writer's comment directed. I grouped them under four headings: The lamp failure, Tobias leaves, Mara in the watch room, and What was found, and who saw.

**How I handled them**
- **Endpoints included:** I read "between X to Y" as including the first and last bullets. Without them, the "these go in…" comments would have nothing to point at.
- **Status:** Every unit is untagged, so all of them stay tentative, which is the default for Idea Notes (03.7). I wrote no status tags, and I set no status from words like "I want" or "Maybe."
- **Writer's words kept:** I kept every hedge, specific and note-to-self with its unit, for example "Not sure if that's too cute," "Maybe," "Could be," "Possibly" and "which nobody can explain yet."
- **Prose questions:** The church-bell "What if…?" stays as prose. I didn't turn it into a `- [?]` line.
- **Rewording:** I made two small changes for readability:
  - "The storm night: I want…" became "On the storm night, I want…"
  - I split the school bullet's run-on sentence into two sentences.
- **Bullets split across notes:** None, so correction 3 didn't come up. Two storm-night units mention the Drowned Bell and Coyle from the Harrow Point note. They read clearly as they are, so I didn't add any context.
- **Not done:**
  - I made no edits to the brain dump and wrote no `migrated-to` pointers. Correction 1 says a separate script writes the pointers.
  - I added no block IDs, because nothing points at these lines yet.
  - I created no new notes; both destinations already existed.
  - I flagged no Gaps or Reviews, since this was a migration run.

**Unit record**

Line numbers below are from `project/brain-dump.md`.

| Source line(s) | Unit (opening words) | Copy went to |
| --- | --- | --- |
| 10 | The town is called Harrow Point… | idea-harrow-point |
| 11 | Maybe the ferry only runs on Tuesdays and Fridays… | idea-harrow-point |
| 12 | There's a pub, the Drowned Bell… Coyle… | idea-harrow-point |
| 13 | Thinking the fishing fleet is down to six boats… | idea-harrow-point |
| 14 | What if the church bell was sold in 1994… | idea-harrow-point |
| 15 | The school closed two winters ago… | idea-harrow-point |
| 16 | Could be that the harbourmaster, Pell… | idea-harrow-point |
| 24 | The storm night: lamp fails for exactly eleven minutes… | idea-storm-night |
| 25 | Tobias took the skiff, not the trawler… | idea-storm-night |
| 26 | Maybe he left at 2:40… low water at 3:05… | idea-storm-night |
| 27 | Mara was asleep in the watch room… | idea-storm-night |
| 28 | Possibly the lamp failed because the backup generator… | idea-storm-night |
| 29 | Two flares found on the rocks… unfired… | idea-storm-night |
| 30 | Someone saw the skiff leave, maybe Coyle… | idea-storm-night |
````

### Case 8: Merge by comment

**brain-dump.md (unchanged by every run)**

````markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- The lamp turns counterclockwise, which is wrong for this coast.
- Mara's lamp rotates the wrong way round. Every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911.
- It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose.

%% Agent, these three are the same idea said three ways. Merge them into one unit in idea-mara-lighthouse. %%
````

#### Run 1

**Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.
- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose.
````

**Run log**

````markdown
I've finished the migration run. One unit moved, into one note.

**Read:** `project/brain-dump.md`, entry for 2026-10-01: three bullets and one writer's comment.

**What triggered it:** The comment `%% Agent, these three are the same idea said three ways. Merge them into one unit in idea-mara-lighthouse. %%`. The three bullets have no status tags, so the comment was the only trigger.

**Migrated:**
- I merged the three bullets into one unit in `project/Ideas/idea-mara-lighthouse.md`, under the existing **The lamp** heading. That's where the existing lamp material is, so I didn't make a new heading.
- **Why it went there:** the writer's comment named the note.
- **What I kept:** every specific in the three bullets.
  - The lamp turns counterclockwise, which is wrong for this coast.
  - Every other light from here to Marrow Bay goes clockwise.
  - The mechanism is from 1911.
  - The cause is her grandfather installing it from a mirror-image drawing.
- **The hedge:** "Possibly on purpose" stays as its own sentence, so how firmly the writer holds the idea doesn't change.
- **Changed:** the unit's status didn't change. It has no tag, so it stays tentative, which is the default in an Idea Note.

**Not done, on purpose:**
- **No changes to the Brain Dump:** I didn't touch it and wrote no `migrated-to` pointers. `corrections.md` #1 says a separate script writes those.
- **No new Idea Note:** the comment named an existing one.
- **No tags, block IDs or Work Items:** the comment didn't call for any, and nothing points at the new line.

**Unit record:**

| Unit | Source lines (`brain-dump.md`) | Copy went to |
| --- | --- | --- |
| Mara's lamp turns the wrong way (merged) | Lines 10, 11 and 12 (2026-10-01) | `project/Ideas/idea-mara-lighthouse.md` → The lamp |
````

#### Run 2

**Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.
- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose.
````

**Run log**

````markdown
I merged the three lamp bullets into one unit in the Mara lighthouse Idea Note. Nothing else needed migrating.

**What drove the run:** The 2026-10-01 entry in the Brain Dump has no status tags. It has one comment: *"Agent, these three are the same idea said three ways. Merge them into one unit in idea-mara-lighthouse."* That comment is the only migration trigger.

**What went where:**
- **Destination:** `project/Ideas/idea-mara-lighthouse.md`, under the existing heading `## The lamp`. It sits right after the whale-oil line, since both describe the lamp. I didn't add a dependency between them because neither relies on the other.
- **The merged unit:** "Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose."
- **Why it reads like that:** In an Idea Note, a unit keeps all of the writer's meaning, specifics and hedges. So I kept "wrong for this coast," the Marrow Bay comparison, the 1911 date, the grandfather and the mirror-image drawing. I kept "Possibly on purpose" word for word so the hedge survives.
- **Status:** The unit is tentative. None of the source lines had a tag and the comment doesn't set a status. Idea Notes don't put a tag on tentative material, so I didn't write one.

**Things to check:**
- The comment calls the three bullets the same idea, but the third one adds something new: a cause (the grandfather installed it from a mirror-image drawing, possibly on purpose). I merged them as asked and kept the cause whole. If you'd rather keep "why it turns the wrong way" as a separate unit, it's easy to split back out.
- Following `corrections.md`, I didn't touch the Brain Dump doc at all. There are no `migrated-to` pointers, because the separate script writes those after this is checked.
- I didn't create any new notes, Work Items or block IDs. Nothing points at the new line, so it doesn't need a block ID.

**Unit record:**

| Unit | Source lines (`project/brain-dump.md`, 2026-10-01) | Copy went to |
| --- | --- | --- |
| Mara's lamp turns the wrong way, and why | Line 10: "The lamp turns counterclockwise, which is wrong for this coast."<br>Line 11: "Mara's lamp rotates the wrong way round. Every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911."<br>Line 12: "It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose." | `project/Ideas/idea-mara-lighthouse.md` (one copy) |
````

#### Run 3

**Ideas/idea-mara-lighthouse.md**

````markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.
- Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose.
````

**Run log**

````markdown
I merged the three lamp bullets from the 2026-10-01 brain dump entry into one unit and added it under **## The lamp** in `project/Ideas/idea-mara-lighthouse.md`. Nothing else in the brain dump had a tag or comment, so nothing else moved.

**Run log**

- **What I read:** the 2026-10-01 entry in `project/brain-dump.md`. The only thing that could trigger migration was your comment saying the three lines are one idea and should be merged into idea-mara-lighthouse. None of the lines had a status tag.
- **What I migrated:** one unit, put together from the three bullets:
  > Mara's lamp turns counterclockwise, which is wrong for this coast: every other light from here to Marrow Bay goes clockwise. The mechanism is from 1911. It goes the wrong way because her grandfather installed it from a mirror-image drawing. Possibly on purpose.
- **Where and why:** your comment named the note. The unit sits under the existing "The lamp" heading, after the whale-oil line, because it's about the same lamp.
- **How I merged it:**
  - I kept every specific: counterclockwise, wrong for this coast, Marrow Bay, clockwise elsewhere, 1911, the grandfather, the mirror-image drawing.
  - I kept the hedge "Possibly on purpose," and I didn't make the grandfather explanation any more or less certain than you wrote it.
  - The first two bullets both say the lamp turns the wrong way. I stated that once.
- **Status:** the unit is tentative. It had no tag in the brain dump, and tentative is the default in an Idea Note, so I didn't add a tag.
- **What I didn't do:**
  - I didn't edit the brain dump at all, so there are no `migrated-to` pointers. The corrections file says a separate script adds them later.
  - I added no block IDs, because nothing points at this line.
  - I flagged nothing. The unit is tentative, which doesn't get Gaps, and Reviews only happen when you ask.
  - I didn't create a new Idea Note, because the existing one fits.

**Unit record**

| Unit | Source lines (`brain-dump.md`) | Copy went to |
| --- | --- | --- |
| Lamp turns counterclockwise; grandfather's mirror-image drawing | L10, L11, L12 (comment at L14) | `project/Ideas/idea-mara-lighthouse.md`, "The lamp" |
````
