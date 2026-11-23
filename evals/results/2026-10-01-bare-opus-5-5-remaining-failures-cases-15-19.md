# 2026-10-01 Bare Run: Remaining Failures Cases 15-19

This run was done by hand outside `claude plugin eval`. The results were graded by script (code checks) and by Claude Fable 5.1 (judge checks), not by the eval tool's grader pipeline.

## What Was Run

- **Date:** 2026-10-01
- **Model:** `claude-opus-5-5`
- **Runs:** 15 total. Five cases, three runs each.
- **Launch method:** `claude -p` child sessions with `--setting-sources project` so no personal rules or hooks loaded. Tools limited to Read, Write, Edit, Glob, Grep. Permission mode: `--permission-mode acceptEdits`.
- **Rules given:** the terminology snapshot in `_fixtures/rules/` and `corrections.md` with all five rules.

Prompt used verbatim:

> This folder holds a screenwriting project. The files in rules/ explain how the project's notes work. Read rules/terminology-script-asst.md first, then rules/corrections.md, which is newer and wins where they differ. Then do a migration run: read project/brain-dump.md and migrate what the writer's status tags and comments point at, following the rules. Edit the notes directly. When you finish, reply with a short run log: what you migrated, where it went, and why.

## Summary Table

| Case                                      | Passed    | Cost (list price) |
| ----------------------------------------- | --------- | ----------------- |
| unit-record-15-split-and-merge            | 3/3       | $0.90             |
| tentative-in-area-note-16-tagged-child    | 3/3       | $0.85             |
| missed-unit-17-scattered-tags             | 3/3       | $0.75             |
| unasked-edit-18-typos-and-contradiction   | 3/3       | $0.74             |
| wrong-destination-19-no-destination-named | 3/3       | $0.89             |
| **Total**                                 | **15/15** | **$4.13**         |

## Findings

1. **Every case passed on every run.**
2. **Case 15: all three unit records were right.** Each showed the split as one source line with two copies, and the merge as two source lines with one copy.
3. **Case 18, observed: two of three runs fixed "dosnt" in the copy, and one kept it.** No run touched the existing lines. Moe ruled on 2026-10-01 that fixing the typo in the copy is fine.
4. **Case 19: every run put the Coyle bullet in the storm-night note** and spelled "that night" out as "the storm night." Moe ruled on 2026-10-01 that this is the right call.
5. **The grading script had one more bug.** In case 15 it counted a heading named "Ballast" as a second bullet and reported two false fails.

## Caveats

The code checks were run by script, with one script bug noted (case 15: the "cat is one bullet" check counted a heading named "Ballast" as a second bullet and reported false fails). The judged checks were done by Claude Fable 5.1 reading each output, in the same session that wrote the cases. The user has not reviewed the expected results for cases 15 to 19.

## Full Outputs

## Bare Claude run on the remaining failures

Run on 2026-10-01. Model: claude-opus-5-5. No agent, no skill, no personal rules. Rules given: the terminology snapshot in evals/\_fixtures/rules and corrections.md with all five rules.

For each case: the fixture, then each run's changed notes and run log. No run changed the Brain Dump doc.

### Case 15: Split and merge in one run

**Fixture: brain-dump.md**

```markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Pell rings the harbour bell by hand at dusk. He learned it from Tobias, who used to do it for pocket money.

%% Agent, migrate this. The bell ringing goes in idea-harrow-point, the part about Tobias in idea-tobias. %%

- The lighthouse cat is called Ballast.
- Mara's cat, Ballast, has one eye and sleeps in the lamp room.

%% Agent, these two are one idea. Merge them into one unit in idea-mara-lighthouse. %%

- The lamp room smells of paraffin and wet wool. #status/provisional

%% Agent, the paraffin line goes in idea-mara-lighthouse too. %%
```

**Fixture: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### People

- Coyle runs the Drowned Bell.

### Getting in and out

- The ferry runs twice a week.
```

**Fixture: Ideas/idea-mara-lighthouse.md**

```markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.

### The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
```

**Fixture: Ideas/idea-tobias.md**

```markdown
---
title: Idea - Tobias
type: [idea-note]
---

## Idea - Tobias
```

#### Run 1

**After: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### People

- Coyle runs the Drowned Bell.

### Getting in and out

- The ferry runs twice a week.

### The harbour bell

- Pell rings the harbour bell by hand at dusk. He learned it from Tobias.
```

**After: Ideas/idea-mara-lighthouse.md**

```markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.

### The lamp room

- Mara's cat, Ballast, is the lighthouse cat. It has one eye and sleeps in the lamp room.
- The lamp room smells of paraffin and wet wool. #status/provisional

### The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
```

**After: Ideas/idea-tobias.md**

```markdown
---
title: Idea - Tobias
type: [idea-note]
---

## Idea - Tobias

### The harbour bell

- Tobias used to ring the harbour bell by hand at dusk, for pocket money. Pell learned it from him, and now rings it himself.
```

**Run log**

```markdown
I migrated three units from `project/brain-dump.md` into three Idea Notes. All three moves came from your comments. I didn't edit the Brain Dump doc and didn't write any `migrated-to` pointers, since corrections.md 1 leaves those to the Run script.

### What went where, and why

**1. Pell and the harbour bell (split across two notes).** Your comment asked for the bell ringing in idea-harrow-point and the Tobias part in idea-tobias. Each piece keeps enough context to read on its own (corrections.md 3):

- **idea-harrow-point**, under a new heading "The harbour bell": "Pell rings the harbour bell by hand at dusk. He learned it from Tobias." I gave it its own heading rather than putting it under "People" because it's about the town's routine. I also kept it separate from "the Drowned Bell", which reads like a different place.
- **idea-tobias**, under a new heading "The harbour bell": "Tobias used to ring the harbour bell by hand at dusk, for pocket money. Pell learned it from him, and now rings it himself."
- The unit has no tag, so it stays tentative and I wrote no tag.

**2. Ballast the cat (two bullets merged into one unit).** Your comment said these two bullets are one idea and should become one unit in idea-mara-lighthouse.

- It sits under a new heading "The lamp room": "Mara's cat, Ballast, is the lighthouse cat. It has one eye and sleeps in the lamp room."
- You didn't give the cat a pronoun, so I used "it".
- It's tentative, so there's no tag.

**3. Paraffin smell.** Your comment sent it to idea-mara-lighthouse.

- It's under "The lamp room", next to Ballast, word for word, with your `#status/provisional` tag carried over. Migrating doesn't change status.

### Other notes

- **New notes:** none.
- **Block IDs:** none needed, because nothing points at these lines.
- **Flags:** none. No unit had a tag sitting over several ideas (corrections.md 4), nothing was rejected, and no Work was proposed.
- **Could not do:** nothing.

### Unit record

| Unit                                                    | Source line(s) in brain-dump.md | Copy went to                                    |
| ------------------------------------------------------- | ------------------------------- | ----------------------------------------------- |
| Pell rings the bell / learned from Tobias               | L10                             | `Ideas/idea-harrow-point.md` (The harbour bell) |
| Tobias rang the bell for pocket money / taught Pell     | L10                             | `Ideas/idea-tobias.md` (The harbour bell)       |
| Ballast, Mara's one-eyed lighthouse cat                 | L14, L15 (merged)               | `Ideas/idea-mara-lighthouse.md` (The lamp room) |
| Lamp room smells of paraffin and wet wool (provisional) | L19                             | `Ideas/idea-mara-lighthouse.md` (The lamp room) |
```

#### Run 2

**After: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### People

- Coyle runs the Drowned Bell.

### The harbour bell

- Pell rings the harbour bell by hand at dusk. He learned it from Tobias.

### Getting in and out

- The ferry runs twice a week.
```

**After: Ideas/idea-mara-lighthouse.md**

```markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp room smells of paraffin and wet wool. #status/provisional

### Ballast

- The lighthouse cat is Mara's cat, Ballast. Ballast has one eye and sleeps in the lamp room.

### The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
```

**After: Ideas/idea-tobias.md**

```markdown
---
title: Idea - Tobias
type: [idea-note]
---

## Idea - Tobias

### The harbour bell

- Tobias used to ring the harbour bell by hand at dusk, for pocket money. Pell learned it from him.
```

**Run log**

```markdown
### Run log: migration, 2026-10-01

**Read:** `project/brain-dump.md`, the 2026-10-01 entry with three comments and one status tag. Following corrections 1, I didn't touch the Brain Dump doc: no `migrated-to` pointers, no block IDs. Nothing points at any line, so no block IDs were needed anywhere.

**Migrated:**

1. **Pell / harbour bell bullet, split across two notes.** Your comment said where each part goes.
   - The bell-ringing part went to `idea-harrow-point` under a new heading, **The harbour bell**. I kept "He learned it from Tobias" so the line still makes sense in that note (corrections 3).
   - The Tobias part went to `idea-tobias` under **The harbour bell**. It's reworded so Tobias is the subject: "Tobias used to ring the harbour bell by hand at dusk, for pocket money. Pell learned it from him." The bell and Pell stay in it as context. "At dusk" and "by hand" come from your "used to do it."
   - Both pieces are untagged, so they stay tentative.

2. **The two Ballast bullets, merged into one unit** in `idea-mara-lighthouse` under a new heading, **Ballast**, as your comment asked: "The lighthouse cat is Mara's cat, Ballast. Ballast has one eye and sleeps in the lamp room." It's untagged, so it stays tentative. I used "Ballast" rather than a pronoun because you haven't given the cat a gender.

3. **The paraffin line** went to `idea-mara-lighthouse` under the existing heading **The lamp**, because it's about the lamp room. It keeps your `#status/provisional` tag, since migrating never changes status. The bullet holds one idea, so corrections 4 didn't come up.

**New notes:** none. Every destination was named in a comment and already existed.

**Flagged:** nothing. One thing to be aware of: "smells of paraffin" sits next to "the lamp uses whale oil." Both are provisional or tentative, so I didn't flag it under 03.15.

**Unit record:**

| Unit                                      | Source line(s) in brain-dump.md                                                                                   | Copy went to                            |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Pell rings the bell, learned from Tobias  | L10 "Pell rings the harbour bell by hand at dusk. He learned it from Tobias, who used to do it for pocket money." | `project/Ideas/idea-harrow-point.md`    |
| Tobias rang the bell for pocket money     | L10 (same bullet)                                                                                                 | `project/Ideas/idea-tobias.md`          |
| Ballast, Mara's one-eyed lighthouse cat   | L14 "The lighthouse cat is called Ballast." + L15 "Mara's cat, Ballast, has one eye and sleeps in the lamp room." | `project/Ideas/idea-mara-lighthouse.md` |
| Lamp room smells of paraffin and wet wool | L19 "The lamp room smells of paraffin and wet wool. #status/provisional"                                          | `project/Ideas/idea-mara-lighthouse.md` |
```

#### Run 3

**After: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### People

- Coyle runs the Drowned Bell.

### Getting in and out

- The ferry runs twice a week.

### The harbour bell

- Pell rings the harbour bell by hand at dusk. He learned it from Tobias.
```

**After: Ideas/idea-mara-lighthouse.md**

```markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp room smells of paraffin and wet wool. #status/provisional

### The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.

### Ballast

- The lighthouse cat is Mara's cat, Ballast. Ballast has one eye and sleeps in the lamp room.
```

**After: Ideas/idea-tobias.md**

```markdown
---
title: Idea - Tobias
type: [idea-note]
---

## Idea - Tobias

### The harbour bell

- Tobias used to ring the harbour bell by hand for pocket money. Pell learned it from him, and now rings it by hand at dusk.
```

**Run log**

```markdown
I migrated everything your three comments pointed at, into three Idea Notes. I didn't touch `brain-dump.md`: no `migrated-to` pointers, no block IDs, no status tags, as the corrections require.

### Run log

**What triggered the run:** three of your comments and one `#status/provisional` tag. I didn't migrate any untagged prose on its own.

**1. Pell and the harbour bell → split into two notes, as your comment asked**

- **`idea-harrow-point`**, new heading "The harbour bell": "Pell rings the harbour bell by hand at dusk. He learned it from Tobias." I kept "learned it from Tobias" so the bell piece still makes sense in this note (corrections, item 3).
- **`idea-tobias`**, new heading "The harbour bell": "Tobias used to ring the harbour bell by hand for pocket money. Pell learned it from him, and now rings it by hand at dusk." I kept the Pell context so the Tobias piece reads on its own.
- **Status:** tentative, since the line had no tag. I wrote no tag.

**2. Ballast → merged into one unit in `idea-mara-lighthouse`, as your comment asked**

- Under a new heading "Ballast": "The lighthouse cat is Mara's cat, Ballast. Ballast has one eye and sleeps in the lamp room."
- All the details from both lines survived: lighthouse cat, Mara's, one eye, sleeps in the lamp room.
- **Status:** tentative, since neither line had a tag. I wrote no tag.

**3. The paraffin line → `idea-mara-lighthouse`, under "The lamp"**

- I copied it word for word and kept your `#status/provisional` tag. I put it under "The lamp" because it's about the lamp room.
- It sits next to the tentative whale-oil line. I didn't flag any tension between them, because the rules don't flag contradictions that involve tentative ideas.

**Other notes**

- None of the bullets held more than one idea under a single tag, so I have nothing to ask you about tag scope.
- No Questions migrated, and I proposed no Work Items.
- I didn't create a new Idea Note, because each of your comments named an existing one.

### Unit record

| Unit                                               | Source line(s) in `brain-dump.md` | Where each copy went            |
| -------------------------------------------------- | --------------------------------- | ------------------------------- |
| Pell rings the bell, learned from Tobias           | L10                               | `Ideas/idea-harrow-point.md`    |
| Tobias rang the bell for pocket money, taught Pell | L10                               | `Ideas/idea-tobias.md`          |
| Ballast, Mara's one-eyed lighthouse cat            | L14, L15 (merged)                 | `Ideas/idea-mara-lighthouse.md` |
| Lamp room smells of paraffin and wet wool          | L19                               | `Ideas/idea-mara-lighthouse.md` |
```

### Case 16: Provisional child under a committed parent

**Fixture: brain-dump.md**

```markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Mara keeps a logbook of every ship that passes. #status/committed
  - She writes it in pencil, never ink.
  - She has started leaving gaps in it on purpose. #status/provisional

%% Agent, the committed material belongs in char-mara. The provisional line goes in idea-mara-habits. %%
```

**Fixture: char-mara.md**

```markdown
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
```

**Fixture: Ideas/idea-mara-habits.md**

```markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

## Idea - Mara Habits
```

#### Run 1

**After: char-mara.md**

```markdown
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
- Mara keeps a logbook of every ship that passes. She writes the logbook in pencil, never ink.

## Psychology

### Values, Beliefs, etc.

## Rationale

## Rejected
```

**After: Ideas/idea-mara-habits.md**

```markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

## Idea - Mara Habits

### The logbook

- Mara has started leaving gaps on purpose in her logbook of every ship that passes. #status/provisional
```

**Run log**

```markdown
I migrated the 2026-10-01 entry in the brain dump into `char-mara.md` and `Ideas/idea-mara-habits.md`. I didn't touch `brain-dump.md`, so it has no `migrated-to` pointers yet; under corrections.md 1 the separate script adds those after the copies are checked.

**What I read:** the two rules files, then `project/brain-dump.md`, which has one dated entry (2026-10-01) and one comment from you. I also read `char-mara.md` and `Ideas/idea-mara-habits.md` before editing them.

**What I migrated, where, and why:**

1. **Committed material → `project/char-mara.md`, Bio > General.**
   - Added: "Mara keeps a logbook of every ship that passes. She writes the logbook in pencil, never ink."
   - The parent bullet is tagged `#status/committed`. The untagged "pencil, never ink" bullet under it takes the parent's tag (03.2).
   - Your comment sends the committed material to char-mara.
   - I rewrote both as plain statements and put "Mara" in place of "She" so the line reads on its own. Nothing was dropped. There was no reason given for the choice, so the Rationale section stays empty, and I added no status tag because character notes like this one don't carry them.

2. **Provisional material → `project/Ideas/idea-mara-habits.md`, under a new heading "The logbook".**
   - Added: "Mara has started leaving gaps on purpose in her logbook of every ship that passes. #status/provisional"
   - This bullet has its own `#status/provisional` tag, and your comment sends it to idea-mara-habits.
   - Correction 3 says each piece needs enough context to make sense in its own note, so I named Mara and the logbook, since "She" and "it" wouldn't make sense there. The logbook fact is repeated, which correction 3 allows. I worded it so the provisional tag clearly covers only the gaps, not the committed logbook.
   - "Has started" and "on purpose" are kept as you wrote them.

**What I flagged:** nothing. Each bullet holds one idea, so correction 4 didn't apply. There are no `- [?]` lines, no rejections, and no contradictions.

**Unit record:**

| Unit                                           | Source line(s)                       | Copy went to                            |
| ---------------------------------------------- | ------------------------------------ | --------------------------------------- |
| Mara keeps a logbook of every ship that passes | brain-dump.md L10                    | char-mara.md (Bio > General)            |
| She writes it in pencil, never ink             | brain-dump.md L11                    | char-mara.md (Bio > General)            |
| She has started leaving gaps in it on purpose  | brain-dump.md L12 (context from L10) | Ideas/idea-mara-habits.md (The logbook) |
```

#### Run 2

**After: char-mara.md**

```markdown
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
- Mara keeps a logbook of every ship that passes. She writes it in pencil, never in ink.

## Psychology

### Values, Beliefs, etc.

## Rationale

## Rejected
```

**After: Ideas/idea-mara-habits.md**

```markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

## Idea - Mara Habits

### The ship logbook

- Mara keeps a logbook of every ship that passes, and she has started leaving gaps in it on purpose. #status/provisional
```

**Run log**

```markdown
I migrated all three lines in the 2026-10-01 entry: two committed facts went to `char-mara.md` and the provisional line went to `idea-mara-habits.md`. I didn't edit `brain-dump.md` at all, and I wrote no `migrated-to` pointers or block IDs (corrections item 1).

### What went where, and why

**To `project/char-mara.md`, Bio › General** (committed, so it goes in the Area Note):

- "Mara keeps a logbook of every ship that passes. She writes it in pencil, never in ink."
- **Why:** the parent bullet is tagged `#status/committed`. The pencil line has no tag of its own, so it takes the parent's committed status. Your comment sends committed material to char-mara. I rewrote both as plain statements, without status tags as Area Notes require. There were no notes-to-self or reasons to carry, so I added nothing to Rationale.
- I put it under Bio › General, next to the existing fact about how long she's kept the lighthouse, because it's a fact about her routine. Psychology would also work if you read the pencil detail as a trait.

**To `project/Ideas/idea-mara-habits.md`, new heading "The ship logbook"** (provisional, so it goes in the Idea Note):

- "Mara keeps a logbook of every ship that passes, and she has started leaving gaps in it on purpose." `#status/provisional`
- **Why:** this line has its own `#status/provisional` tag, which overrides the parent's committed tag. Your comment sends it to idea-mara-habits. I added the logbook context so "it" makes sense without the Brain Dump doc (corrections item 3). It keeps the tag because untagged lines in an Idea Note count as tentative.
- **No new Idea Note:** your comment named an existing note, so I didn't create one.

### Flags

- The gaps idea relies on the committed logbook. I didn't add a `depends_on` link because the rules for those links (section 04) are still open pending the ledger. One can be added once that's settled.
- I found no bullet where one tag covered several ideas, no rejections and no Work Items.

### Unit record

| Unit                           | Source line(s)                       | Copy went to              |
| ------------------------------ | ------------------------------------ | ------------------------- |
| Logbook of every passing ship  | brain-dump.md L10                    | char-mara.md              |
| Writes it in pencil, never ink | brain-dump.md L11 (inherits L10 tag) | char-mara.md              |
| Leaving gaps on purpose        | brain-dump.md L12 (context from L10) | Ideas/idea-mara-habits.md |
```

#### Run 3

**After: char-mara.md**

```markdown
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
- Mara keeps a logbook of every ship that passes. She writes it in pencil, never in ink.

## Psychology

### Values, Beliefs, etc.

## Rationale

## Rejected
```

**After: Ideas/idea-mara-habits.md**

```markdown
---
title: Idea - Mara Habits
type: [idea-note]
---

## Idea - Mara Habits

### The logbook

- Mara has started leaving gaps on purpose in the logbook she keeps of every ship that passes. #status/provisional
```

**Run log**

```markdown
I migrated three units from the 2026-10-01 entry: two committed ones into char-mara and one provisional one into idea-mara-habits. I didn't change `brain-dump.md`, and I wrote no `migrated-to` pointers, because the corrections file says a separate script does that.

**What triggered migration:** the writer's two status tags (committed on the logbook bullet, provisional on the "gaps" bullet), plus the comment saying where each goes.

**Committed material, to `project/char-mara.md` (Bio › General)**

- The logbook bullet is tagged committed. The "pencil, never ink" bullet nested under it has no tag of its own, so it counts as committed too.
- I rewrote them for this note as: "Mara keeps a logbook of every ship that passes. She writes it in pencil, never in ink."
- I put it under Bio › General, next to the existing fact about her lighthouse years. It's a fact about her daily life, not her psychology.
- Area Notes don't carry status tags, so I added none. There was no rationale to move: neither bullet gives a reason for the choice.

**Provisional material, to `project/Ideas/idea-mara-habits.md`**

- The "gaps" bullet has its own provisional tag, which overrides the committed tag above it. That keeps it out of char-mara, and the comment sends it to idea-mara-habits.
- The note was empty, so I added a "The logbook" heading.
- On its own, "She has started leaving gaps in it" doesn't say who or what "it" is. Correction 3 says a piece split into another note keeps the context it needs, so I named Mara and the logbook: "Mara has started leaving gaps on purpose in the logbook she keeps of every ship that passes. #status/provisional". The meaning and the "on purpose" are unchanged, and the tag is carried over.

**Not done, and one question**

- The provisional line depends on the committed logbook fact, but I didn't add a `depends_on` link. That would need a block ID in char-mara, and the dependency rules are still marked Open pending the ledger.
- No bullet held more than one idea under a single tag, so correction 4 didn't apply.
- No questions, Gaps, rejections or Reviews were involved.
- Question for the writer: is a plain bullet under Bio › General the right home in char-mara, or do you want a "Habits" subsection?

**Unit record**

| #   | Source line(s) in `brain-dump.md`                                                           | Copy went to                                                |
| --- | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 1   | L10 "Mara keeps a logbook of every ship that passes. #status/committed"                     | `project/char-mara.md` (Bio › General)                      |
| 2   | L11 "She writes it in pencil, never ink." (counts as committed through L10)                 | `project/char-mara.md` (Bio › General), same line as unit 1 |
| 3   | L12 "She has started leaving gaps in it on purpose. #status/provisional" (context from L10) | `project/Ideas/idea-mara-habits.md` (The logbook)           |
```

### Case 17: Six tagged bullets among eighteen

**Fixture: brain-dump.md**

```markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

%% Agent, anything I tag provisional under these three dates goes in idea-harrow-point. Leave the untagged lines where they are. %%

#### 2026-10-01

- The bakery only opens when the baker's knee allows it.
- The post office doubles as the undertaker's. #status/provisional
- There are more boats than people in winter.
- Somebody repaints the war memorial every spring and nobody knows who.
- The chemist, Ferris, fills prescriptions from memory. #status/provisional
- Fog comes in from the east, which is the wrong direction.

#### 2026-09-30

- Half the houses on Quay Street are let to a film company that never came.
- The primary school has nine pupils, all cousins. #status/provisional
- The church clock runs four minutes fast on purpose.
- Gulls have learned to open the bins outside the Drowned Bell.
- A seal called Mister Hale comes into the harbour every October. #status/provisional
- The bus shelter has had the same timetable since 1998.

#### 2026-09-28

- The council sold the fish market roof for scrap in 2011. #status/provisional
- There's a rumour the vicar's wife ran the smuggling.
- Nobody locks their doors except Pell.
- The cliff path lost twelve metres to the sea last winter. #status/provisional
- Everyone's grandmother claims to have been the May Queen.
- The phone box is listed, so they can't remove it.
```

**Fixture: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point
```

#### Run 1

**After: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### Town services and people

- The post office doubles as the undertaker's. #status/provisional
- The chemist, Ferris, fills prescriptions from memory. #status/provisional
- The primary school has nine pupils, all cousins. #status/provisional

### Harbour and coast

- A seal called Mister Hale comes into the harbour every October. #status/provisional
- The council sold the fish market roof for scrap in 2011. #status/provisional
- The cliff path lost twelve metres to the sea last winter. #status/provisional
```

**Run log**

```markdown
I migrated six units from the Brain Dump to `project/Ideas/idea-harrow-point.md`, which was empty before this run. They were the six lines you tagged provisional across the three dates, and I moved them on your comment at `project/brain-dump.md:8`.

**What I migrated, where it went, and why**

- **Where:** All six went into the Idea Note your comment named. I didn't create any other notes.
- **Why:** Each line carries your own `#status/provisional` tag, and your comment sends provisional lines under these dates to this note. Nothing went to an Area Note, because none of these lines is committed.
- **Status:** Every unit keeps its `#status/provisional` tag, since migrating never changes status. The words are unchanged because each line was already one clear idea with no hedges to keep.
- **Organization:** I grouped the units under two headings with no date headings, as an Idea Note requires: "Town services and people" and "Harbour and coast".
- **Left alone:** The 12 untagged lines stay in the Brain Dump, as your comment asked. I didn't edit the Brain Dump at all. I wrote no `migrated-to` pointers (the script writes those), no block IDs (nothing points at these lines yet) and no status tags.
- **Nothing to flag:** No bullet held more than one idea, so no tag's coverage is in question. There were no Questions, rejections or `[AGENT]` material.

**Unit record**

| #   | Source line (`project/brain-dump.md`)                                                                   | Copy went to                                           |
| --- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| 1   | L13 (2026-10-01): "The post office doubles as the undertaker's. #status/provisional"                    | `Ideas/idea-harrow-point.md`, Town services and people |
| 2   | L16 (2026-10-01): "The chemist, Ferris, fills prescriptions from memory. #status/provisional"           | `Ideas/idea-harrow-point.md`, Town services and people |
| 3   | L22 (2026-09-30): "The primary school has nine pupils, all cousins. #status/provisional"                | `Ideas/idea-harrow-point.md`, Town services and people |
| 4   | L25 (2026-09-30): "A seal called Mister Hale comes into the harbour every October. #status/provisional" | `Ideas/idea-harrow-point.md`, Harbour and coast        |
| 5   | L30 (2026-09-28): "The council sold the fish market roof for scrap in 2011. #status/provisional"        | `Ideas/idea-harrow-point.md`, Harbour and coast        |
| 6   | L33 (2026-09-28): "The cliff path lost twelve metres to the sea last winter. #status/provisional"       | `Ideas/idea-harrow-point.md`, Harbour and coast        |
```

#### Run 2

**After: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### Services and the people who run them

- The post office doubles as the undertaker's. #status/provisional
- The chemist, Ferris, fills prescriptions from memory. #status/provisional
- The primary school has nine pupils, all cousins. #status/provisional

### The town falling away

- The council sold the fish market roof for scrap in 2011. #status/provisional
- The cliff path lost twelve metres to the sea last winter. #status/provisional

### The harbour

- A seal called Mister Hale comes into the harbour every October. #status/provisional
```

**Run log**

```markdown
I migrated six units into `project/Ideas/idea-harrow-point.md`. I didn't change the Brain Dump doc.

**What I migrated and why**

- Your comment at the top of the brain dump said that anything tagged provisional under the three dates goes to idea-harrow-point, and that untagged lines stay where they are. Six lines carry `#status/provisional`, so those six moved.
- Each bullet holds a single idea, so I didn't split anything. None of them hides a second idea that a tag might or might not cover.
- The wording is yours, unchanged. The status stays provisional, and each line keeps its tag.
- The note had no content yet, so I organised it under three topic headings, with no date headings:
  - Services and the people who run them
  - The town falling away
  - The harbour
- I didn't add block IDs, because nothing points at these lines yet.

**What I left alone**

- The 12 untagged lines are tentative, and your comment said to leave them.
- I wrote no `migrated-to` pointers. Under the corrections, the script adds those after the check.

**Flags:** none. Nothing was rejected, there were no Questions, and no contradictions to flag. Provisional material isn't checked for them anyway.

**Unit record**

| #   | Source line (brain-dump.md)                                                   | Copied to                                               |
| --- | ----------------------------------------------------------------------------- | ------------------------------------------------------- |
| 1   | 2026-10-01: "The post office doubles as the undertaker's."                    | idea-harrow-point, Services and the people who run them |
| 2   | 2026-10-01: "The chemist, Ferris, fills prescriptions from memory."           | idea-harrow-point, Services and the people who run them |
| 3   | 2026-09-30: "The primary school has nine pupils, all cousins."                | idea-harrow-point, Services and the people who run them |
| 4   | 2026-09-30: "A seal called Mister Hale comes into the harbour every October." | idea-harrow-point, The harbour                          |
| 5   | 2026-09-28: "The council sold the fish market roof for scrap in 2011."        | idea-harrow-point, The town falling away                |
| 6   | 2026-09-28: "The cliff path lost twelve metres to the sea last winter."       | idea-harrow-point, The town falling away                |
```

#### Run 3

**After: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### Town services and institutions

- The post office doubles as the undertaker's. #status/provisional
- The chemist, Ferris, fills prescriptions from memory. #status/provisional
- The primary school has nine pupils, all cousins. #status/provisional
- The council sold the fish market roof for scrap in 2011. #status/provisional

### Coast and harbour

- A seal called Mister Hale comes into the harbour every October. #status/provisional
- The cliff path lost twelve metres to the sea last winter. #status/provisional
```

**Run log**

```markdown
I moved all six lines the writer tagged provisional into `project/Ideas/idea-harrow-point.md`. Nothing else was changed.

**Why:** The writer's comment at the top of the brain dump says anything tagged provisional under the three dates goes in idea-harrow-point, and untagged lines stay put. Only status tags and comments can trigger a move, so I moved the six tagged lines and left the 12 untagged ones.

**How:**

- **Wording:** I kept each line exactly as written. They were already readable single ideas.
- **Status:** The provisional tag came with each line to the new note, since moving material never changes its status. I didn't use any line's wording to decide its status.
- **Layout:** Idea Notes group ideas by topic, not by date, so I used two headings: "Town services and institutions" and "Coast and harbour".
- **Brain dump:** I didn't edit it at all. That means no `migrated-to` pointers (the separate script adds those after your work is checked) and no block IDs, because nothing points at these lines.

**Flags:** None. No line held more than one idea, so no tag needed splitting. There were no rejections, Questions or contradictions.

**Unit record**

| #   | Source line (brain-dump.md)                                                                       | Destination                                        |
| --- | ------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| 1   | 2026-10-01: "The post office doubles as the undertaker's. #status/provisional"                    | idea-harrow-point › Town services and institutions |
| 2   | 2026-10-01: "The chemist, Ferris, fills prescriptions from memory. #status/provisional"           | idea-harrow-point › Town services and institutions |
| 3   | 2026-09-30: "The primary school has nine pupils, all cousins. #status/provisional"                | idea-harrow-point › Town services and institutions |
| 4   | 2026-09-30: "A seal called Mister Hale comes into the harbour every October. #status/provisional" | idea-harrow-point › Coast and harbour              |
| 5   | 2026-09-28: "The council sold the fish market roof for scrap in 2011. #status/provisional"        | idea-harrow-point › Town services and institutions |
| 6   | 2026-09-28: "The cliff path lost twelve metres to the sea last winter. #status/provisional"       | idea-harrow-point › Coast and harbour              |
```

### Case 18: Typos and a contradiction in existing lines

**Fixture: brain-dump.md**

```markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- Pell dosnt lock the tide tables anymore, he lost the key in 2019.

%% Agent, migrate this to idea-harrow-point. %%
```

**Fixture: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### The harbour office

- The harbor masters office has no windows facing the see.
- Pell keeps the tide tables locked up.
```

#### Run 1

**After: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### The harbour office

- The harbor masters office has no windows facing the see.
- Pell keeps the tide tables locked up.
- Pell dosnt lock the tide tables anymore, he lost the key in 2019.
```

**Run log**

```markdown
I migrated the one unit the writer's comment pointed at. Nothing else in the Brain Dump doc had a tag or comment, so nothing else moved.

**What moved and where**

- The 2026-10-01 bullet about Pell no longer locking the tide tables went to `project/Ideas/idea-harrow-point.md`.
  - **Why this note:** the writer's comment said "migrate this to idea-harrow-point."
  - **Where in the note:** under "The harbour office", straight after "Pell keeps the tide tables locked up.", so the two tide-table lines read as one train of thought.

**Choices worth checking**

- **Status:** the line is untagged, so it stays tentative and I added no tag. Idea Notes default to tentative, and migrating never changes status.
- **Wording:** I copied the line exactly, including "dosnt". The rules let me reword Idea Note units for readability, but they also say fixing grammar is something a comment grants. Since there was no comment allowing it, I left the spelling alone. I didn't touch the existing typos either ("harbor masters", "see").
- **The two Pell lines conflict:** the existing line says Pell _keeps_ the tables locked up; the new one says he _doesn't anymore_. Both are tentative, so this is normal exploration and I didn't flag it. You didn't say the new line replaces the old one, so I added no `replaces` link and no block ID. If it is meant to replace it, tell me and I'll record that.
- **Brain Dump doc:** I didn't edit it. No `migrated-to` pointer, no block ID, no other changes. The script writes those after the check.
- **No new notes:** I didn't create any. The comment named an existing Idea Note.

**Unit record**

| Unit                                                       | Source line                                                                                                       | Copied to                                                  |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| Pell no longer locks the tide tables; lost the key in 2019 | `project/brain-dump.md` line 10 (2026-10-01): "Pell dosnt lock the tide tables anymore, he lost the key in 2019." | `project/Ideas/idea-harrow-point.md`, "The harbour office" |
```

#### Run 2

**After: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### The harbour office

- The harbor masters office has no windows facing the see.
- Pell keeps the tide tables locked up.
- Pell doesn't lock the tide tables anymore; he lost the key in 2019.
```

**Run log**

```markdown
I migrated the one unit your comment pointed at, into `project/Ideas/idea-harrow-point.md`.

**Read**

- `project/brain-dump.md`, entry 2026-10-01: one bullet with no status tag, followed by the comment `%% Agent, migrate this to idea-harrow-point. %%`.
- `project/Ideas/idea-harrow-point.md`, which already existed.

**Migrated**

- **"Pell dosnt lock the tide tables anymore, he lost the key in 2019."**
  - **Where:** in `idea-harrow-point.md`, under the existing "The harbour office" heading, right after "Pell keeps the tide tables locked up."
  - **Why there:** your comment named this note. The unit is about Pell and the tide tables, so it sits next to the line on the same subject.
  - **Status:** tentative. The line has no tag and no parent bullet, and your comment says where it goes but sets no status. Tentative is the default in both the Brain Dump doc and Idea Notes, so I added no status tag.
  - **Wording:** I fixed the spelling of "dosnt" and swapped the comma for a semicolon to make it easier to read. "Anymore," "lost the key" and "2019" are all kept.

**Left alone**

- **Brain Dump doc:** not edited. The separate script writes the `migrated-to` pointer once the copy is checked.
- **Existing line:** "Pell keeps the tide tables locked up" now contradicts the new unit. Both are tentative, so I didn't flag it. I also didn't add a `replaces` link, because a newer date doesn't settle a contradiction and you didn't say the new line replaces the old one. If it does, tell me and I'll record the replacement.
- **No new Idea Note:** your comment named an existing note.
- **No block IDs, Work Items or Gaps:** nothing points at the line, and tentative material gets no Gaps.

**Unit record**

| Unit                                                       | Source line(s)                                        | Copied to                            |
| ---------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------ |
| Pell no longer locks the tide tables; lost the key in 2019 | `project/brain-dump.md`, line 10 (comment on line 12) | `project/Ideas/idea-harrow-point.md` |
```

#### Run 3

**After: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### The harbour office

- The harbor masters office has no windows facing the see.
- Pell keeps the tide tables locked up.
- Pell doesn't lock the tide tables anymore. He lost the key in 2019.
```

**Run log**

```markdown
I migrated the one unit your comment pointed at. It went into `project/Ideas/idea-harrow-point.md`.

### Run log

**What I read:** `project/brain-dump.md`, which has one entry under 2026-10-01. That entry is one bullet with a comment below it saying "migrate this to idea-harrow-point." I also read `project/Ideas/idea-harrow-point.md`, where it was going.

**What I migrated, and why:**

- **"Pell dosnt lock the tide tables anymore, he lost the key in 2019."**
  - **Why:** your comment asked for it, and only tags and comments trigger migration. It has no status tag, so it stays tentative, the default in both notes. I didn't add a tag.
  - **Where it went:** `idea-harrow-point.md`, under **The harbour office**, right after "Pell keeps the tide tables locked up." It's next to the other line about Pell and the tide tables.
  - **How it's written now:** "Pell doesn't lock the tide tables anymore. He lost the key in 2019." I fixed the spelling of "doesn't" and split the run-on sentence. The meaning and the 2019 date are unchanged, and the original had no hedges to keep.

**What I didn't do:**

- I left the Brain Dump doc as it was. A separate script writes the `migrated-to` pointer after the copy is checked.
- I didn't add block IDs, because nothing points at the new line.
- I didn't fix the typos already in the Idea Note ("harbor masters," "see"). They're your lines, and no comment asked me to fix them.

**Needs your call:** the new line contradicts the one above it ("Pell keeps the tide tables locked up"). Both are tentative ideas, so I didn't flag it as a problem. A newer date doesn't make one replace the other, so I didn't mark the old line as replaced. If the new line is meant to replace it, tell me in a comment.

**Bullets split across notes:** none. **Bullets with one tag covering several ideas:** none.

### Unit record

| Unit                                                       | Source line(s)                                       | Copy went to                                                     |
| ---------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------- |
| Pell no longer locks the tide tables; lost the key in 2019 | `project/brain-dump.md` line 10 (comment on line 12) | `project/Ideas/idea-harrow-point.md`, under "The harbour office" |
```

### Case 19: Tags with no destination named

**Fixture: brain-dump.md**

```markdown
---
title: Brain Dump
type: [brain-dump]
---

## Brain Dump

#### 2026-10-01

- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional
- On the storm night the foghorn was already broken. #status/provisional
- The lamp's lens was cracked by a gull in 2003. #status/provisional
- Coyle closed the pub early that night, which he never does. #status/provisional
```

**Fixture: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### People

- Coyle runs the Drowned Bell.

### Getting in and out

- The ferry runs twice a week.
```

**Fixture: Ideas/idea-mara-lighthouse.md**

```markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.

### The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
```

**Fixture: Ideas/idea-storm-night.md**

```markdown
---
title: Idea - Storm Night
type: [idea-note]
---

## Idea - Storm Night

### The lamp failure

- The lamp failed for eleven minutes.
```

#### Run 1

**After: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### People

- Coyle runs the Drowned Bell.

### Getting in and out

- The ferry runs twice a week.
- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional
```

**After: Ideas/idea-mara-lighthouse.md**

```markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp's lens was cracked by a gull in 2003. #status/provisional

### The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
```

**After: Ideas/idea-storm-night.md**

```markdown
---
title: Idea - Storm Night
type: [idea-note]
---

## Idea - Storm Night

### The lamp failure

- The lamp failed for eleven minutes.

### The foghorn

- On the storm night the foghorn was already broken. #status/provisional

### In town

- On the storm night, Coyle closed the pub early, which he never does. #status/provisional
```

**Run log**

```markdown
I migrated all four lines from the 2026-10-01 entry into the existing Idea Notes. I didn't edit `brain-dump.md` at all, and I wrote no `migrated-to` pointers (per `corrections.md` item 1).

### Run log

**What triggered it:** each of the four lines has a `#status/provisional` tag the writer typed. There were no comments. Provisional material belongs in Idea Notes, never Area Notes, so nothing went to an Area Note. I didn't create any Area Notes or new Idea Notes, because the three existing Idea Notes already cover these topics. Each unit kept its `#status/provisional` tag where it landed, since an untagged line in an Idea Note would count as tentative.

**Where each one went, and why:**

- **Odd, the ferry captain, won't sail on the 13th** → `idea-harrow-point`, under "Getting in and out". It's about the ferry, which already sits in that section ("The ferry runs twice a week").
- **The foghorn was already broken on the storm night** → `idea-storm-night`, under a new "The foghorn" heading. It's an event on the storm night, but it isn't the lamp failure, so it didn't fit under "The lamp failure".
- **A gull cracked the lamp's lens in 2003** → `idea-mara-lighthouse`, under "The lamp". It's history of the lamp itself, not something that happened on the storm night, so it sits with the whale-oil line.
- **Coyle closed the pub early that night** → `idea-storm-night`, under a new "In town" heading. In the brain dump it follows the storm-night line, so I took "that night" to mean the storm night. I reworded it to "On the storm night, Coyle closed the pub early, which he never does" so it makes sense on its own in the note.

**Needs your check:**

- Did you mean the storm night with "that night" on the Coyle line? I worked that out from the line's position, and the line doesn't actually say it. If it's a different night, the unit belongs somewhere else, probably under People in `idea-harrow-point`.
- I didn't add "the Drowned Bell" to the Coyle line. Your other note implies the pub is the Drowned Bell, but the line itself doesn't say so.

No bullets held more than one idea, nothing was rejected, and there were no Questions (`[?]` items) to carry along.

### Unit record

| Source line (brain-dump.md, 2026-10-01)                                | Copied to                                                 |
| ---------------------------------------------------------------------- | --------------------------------------------------------- |
| Line 10: "The ferry captain, Odd, refuses to sail on the 13th."        | `project/Ideas/idea-harrow-point.md` (Getting in and out) |
| Line 11: "On the storm night the foghorn was already broken."          | `project/Ideas/idea-storm-night.md` (The foghorn)         |
| Line 12: "The lamp's lens was cracked by a gull in 2003."              | `project/Ideas/idea-mara-lighthouse.md` (The lamp)        |
| Line 13: "Coyle closed the pub early that night, which he never does." | `project/Ideas/idea-storm-night.md` (In town)             |
```

#### Run 2

**After: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### People

- Coyle runs the Drowned Bell.

### Getting in and out

- The ferry runs twice a week.
- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional
```

**After: Ideas/idea-mara-lighthouse.md**

```markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lighthouse lamp's lens was cracked by a gull in 2003. #status/provisional

### The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
```

**After: Ideas/idea-storm-night.md**

```markdown
---
title: Idea - Storm Night
type: [idea-note]
---

## Idea - Storm Night

### The lamp failure

- The lamp failed for eleven minutes.

### The foghorn

- On the storm night the foghorn was already broken. #status/provisional

### Coyle and the pub

- Coyle closed the pub early on the storm night, which he never does. #status/provisional
```

**Run log**

```markdown
### Run log: migration, 2026-10-01

**What I read:** `project/brain-dump.md`, entry 2026-10-01. It has four bullets, all tagged `#status/provisional` by you, and no comments. Provisional material belongs in Idea Notes, so all four went to the existing Idea Notes. Each copy keeps your `#status/provisional` tag, because an untagged line in an Idea Note would count as tentative. I didn't change anyone's status.

**What I migrated:**

1. **The ferry captain Odd won't sail on the 13th** → `idea-harrow-point`, under "Getting in and out". It sits next to the ferry schedule, which is the material it relates to.
2. **The foghorn was already broken on the storm night** → `idea-storm-night`, under a new heading "The foghorn". It's an event of the storm night, and it isn't part of the lamp failure, so it doesn't go under that heading.
3. **A gull cracked the lamp's lens in 2003** → `idea-mara-lighthouse`, under "The lamp". It's about the lamp's history, not the storm night. I changed "The lamp's lens" to "The lighthouse lamp's lens" so the line makes sense on its own.
4. **Coyle closed the pub early "that night", which he never does** → `idea-storm-night`, under a new heading "Coyle and the pub". I read "that night" as the storm night because of the bullet above it, and wrote it as "early on the storm night". **Please confirm.** If you meant a different night, I'll move the line, probably to the People section of `idea-harrow-point`, since Coyle runs the Drowned Bell there.

**What I didn't do:**

- I didn't add any `migrated-to` pointers and made no edits to the Brain Dump doc. The script handles those.
- I added no block IDs because nothing points at these lines. I also didn't add any dependency links. The cracked lens might connect to the lamp failure, but you haven't said it does, so I didn't link them.
- I didn't create any new Idea Notes because all four units fit existing ones.
- No bullet held more than one idea, so the rule on tags over several ideas didn't apply.

**Unit record:**

| Unit                 | Source line (brain-dump.md, 2026-10-01)                                | Copy went to                                              |
| -------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------- |
| Odd refuses the 13th | Line 10: "The ferry captain, Odd, refuses to sail on the 13th."        | `project/Ideas/idea-harrow-point.md` → Getting in and out |
| Foghorn broken       | Line 11: "On the storm night the foghorn was already broken."          | `project/Ideas/idea-storm-night.md` → The foghorn         |
| Lens cracked 2003    | Line 12: "The lamp's lens was cracked by a gull in 2003."              | `project/Ideas/idea-mara-lighthouse.md` → The lamp        |
| Coyle closes early   | Line 13: "Coyle closed the pub early that night, which he never does." | `project/Ideas/idea-storm-night.md` → Coyle and the pub   |
```

#### Run 3

**After: Ideas/idea-harrow-point.md**

```markdown
---
title: Idea - Harrow Point
type: [idea-note]
---

## Idea - Harrow Point

### People

- Coyle runs the Drowned Bell.

### Getting in and out

- The ferry runs twice a week.
- The ferry captain, Odd, refuses to sail on the 13th. #status/provisional
```

**After: Ideas/idea-mara-lighthouse.md**

```markdown
---
title: Idea - Mara Lighthouse
type: [idea-note]
---

## Idea - Mara Lighthouse

### The lamp

- The lamp uses whale oil, which the town can no longer afford.
- The lamp's lens was cracked by a gull in 2003. #status/provisional

### The keeper before Mara

- The last keeper left without telling anyone. Maybe she was pushed out.
```

**After: Ideas/idea-storm-night.md**

```markdown
---
title: Idea - Storm Night
type: [idea-note]
---

## Idea - Storm Night

### The lamp failure

- The lamp failed for eleven minutes.

### The foghorn

- On the storm night the foghorn was already broken. #status/provisional

### In town

- Coyle closed the pub early on the storm night, which he never does. #status/provisional
```

**Run log**

```markdown
I migrated all four tagged lines from the 2026-10-01 entry in the brain dump into existing Idea Notes. One placement relies on my reading of "that night" and needs you to confirm it (see below).

**What I read:** both rules files, `project/brain-dump.md` and the three Idea Notes.

**What I migrated:** all four lines were tagged `#status/provisional`, so they could only go to Idea Notes. Area Notes never hold provisional material. Each copy keeps the `#status/provisional` tag, the writer's meaning and any hedges.

1. **Odd, the ferry captain** → `idea-harrow-point`, under "Getting in and out", next to the ferry schedule. It's about getting to the island.
2. **The foghorn was already broken** → `idea-storm-night`, under a new heading, "The foghorn". It's an event of the storm night, but not part of the lamp failure.
3. **The gull cracked the lens in 2003** → `idea-mara-lighthouse`, under "The lamp". It's about the lamp's history, not the storm night.
4. **Coyle closed the pub early** → `idea-storm-night`, under a new heading, "In town". It's an odd thing that happened on the storm night.

**Needs your check:**

- **Coyle's line:** the original says "that night". It sits right under the storm-night line, so I read it as the storm night. Without that, "that night" means nothing in its new note, so the copy says "on the storm night" instead. If you meant a different night, the line belongs elsewhere.
- **Lens line:** if the cracked lens is meant to explain the storm-night lamp failure, it may belong in `idea-storm-night` instead. I left it with the lamp's history because you didn't say it was linked.

**What I didn't do:**

- I didn't edit `brain-dump.md` and didn't write any `migrated-to` pointers. The script handles those.
- I added no block IDs, because nothing points at these lines.
- I created no new Idea Notes; the existing three covered everything.
- None of the bullets held more than one idea, and there were no rejections, Questions or comments.

**Unit record**
| Source line (brain-dump.md, 2026-10-01) | Went to |
| --- | --- |
| L10 "The ferry captain, Odd, refuses to sail on the 13th." | `project/Ideas/idea-harrow-point.md` (Getting in and out) |
| L11 "On the storm night the foghorn was already broken." | `project/Ideas/idea-storm-night.md` (The foghorn) |
| L12 "The lamp's lens was cracked by a gull in 2003." | `project/Ideas/idea-mara-lighthouse.md` (The lamp) |
| L13 "Coyle closed the pub early that night, which he never does." | `project/Ideas/idea-storm-night.md` (In town) |
```
