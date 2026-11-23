---
title: Terminology - Script Asst
project: "[[Projects/Script Asst/Script Asst (Project Hub)|Script Asst (Project Hub)]]"
cssclasses: [wide]
created: 2026-09-29 16:30
modified: 2026-09-29 18:31
---

# Terminology - Script Asst

> [!info] Approved
> Moe approved these definitions on 2026-09-29. The Open callouts mark parts that are still for the graph session. Change a definition only with Moe's approval, and log it in the changelog.

The terms this plugin uses, one definition each. This note covers the whole plugin. It holds the pre-writing terms and the phase names for now. Writing-phase and polish-phase terms join it later. The groups below are by topic, not by phase.

Two kinds of callout appear under some terms:

- **"Changes the guides"** marks a definition that departed from what the pre-writing guides said before 2026-09-29. The guides were updated to match on 2026-09-29. The callouts stay as a record.
- **"Open"** marks a part of a definition that isn't decided yet.

## Table of Contents

- 01 Notes and Places
    - 01.1 Brain Dump doc
    - 01.2 Idea Unit
    - 01.3 Idea Note
    - 01.4 Area Note
    - 01.5 Concept Note
    - 01.6 Scene Notes
    - 01.7 Rationale section
    - 01.8 Rejected section
    - 01.9 Work Items view
    - 01.10 Run
    - 01.11 Run log
- 02 What the Writer's Words Contain
    - 02.1 Story substance
    - 02.2 Notes-to-self
    - 02.3 Rationale
- 03 Standing
    - 03.1 Story authority
    - 03.2 Status
    - 03.3 Tentative
    - 03.4 Provisional
    - 03.5 Committed
    - 03.6 Rejected
    - 03.7 Default status
    - 03.8 Committed material and provisional material
    - 03.9 Thread
    - 03.10 Version
    - 03.11 Scoped
    - 03.12 Graduation
    - 03.13 Migrate
    - 03.14 Rejection scope
    - 03.15 Contradiction
- 04 Relationships and Pointers
    - 04.1 Block ID
    - 04.2 Iteration
    - 04.3 Lineage
    - 04.4 Alternative
    - 04.5 Replacement
    - 04.6 Story Dependency
    - 04.7 `migrated-to` pointer
- 05 Work
    - 05.1 Work Item and Work Type
    - 05.2 Question
    - 05.3 Gap
    - 05.4 Brainstorm
    - 05.5 Research
    - 05.6 Review
    - 05.7 Proposal
    - 05.8 Priority
    - 05.9 Open and Closed
    - 05.10 Closure outcomes
- 06 Metadata and Signals
    - 06.1 Metadata
    - 06.2 Comment
    - 06.3 Attribution
    - 06.4 Precedence
    - 06.5 Reading the writer's words
- 07 Phases and Project Documents
    - 07.1 Pre-writing, Writing, Polish
    - 07.2 Writer's Statement
- 08 Retired Terms

## 01 Notes and Places

### 01.1 Brain Dump doc

The note where the writer's material enters the system. It holds dated entries of ideas off the top of the writer's head, in any form: typed, transcribed from voice, pasted, a link, an image.

It is not a place to develop an idea at length. It is history: a record of what the writer thought, and when.

- **The agent never changes the writer's words here and never removes anything.**
- **The agent adds only four things, unless a writer's comment asks for more:** block IDs, `migrated-to` pointers, Brainstorm results opened by `[AGENT]`, and Research quick facts opened by `[AGENT]` (decisions-graph-prewriting-pt2.md 06 item 12; decisions-graph-prewriting-pt2.md 08 item 8). The Run script writes the block IDs and the pointers. The migrator writes nothing in the Brain Dump doc (graph-prewriting-v1.md 3).
- **The agent doesn't turn prose questions into `- [?]` lines.** The writer types `- [?]`. A question the writer leaves unmarked stays inside its unit's words and migrates with it. It isn't tracked as Work (decisions-graph-prewriting-pt2.md 06 item 9).
- **The agent never writes a status tag here.** A status tag in the Brain Dump doc is always the writer's.
- **Gaps and Reviews are never flagged here.**
- **Untagged material here is tentative.** Rejected material stays on its line, with its tag.

When the doc grows too long, it splits into a new doc, `{Project}/brain-dump-{N}`, at a date heading.

### 01.2 Idea Unit

The smallest piece of the writer's material that means something on its own. It is one idea, in the writer's words, with whatever sentences it needs to stay readable.

A single bullet can hold several Idea Units. "Someone could sell memories to finance university. Does the person know Lena?" stays together, because "the person" means the seller.

An Idea Unit records that the writer considered something. It does not mean the thing is true in the story.

The agent may create Idea Units of its own only when the writer asks, or when the agent's definition allows it. It labels them `[AGENT]`.

### 01.3 Idea Note

A note where related Idea Units are gathered so they can be developed. It is a workspace, not a record of what is decided.

- **The agent may decide that material earns a new Idea Note.** A writer's comment can also say which material earns one. Either way, the agent creates the note and organizes it. Its reason for creating a note, or not, goes in the run log. Whether this freedom survives depends on the tests (decisions-graph-prewriting-pt2.md 06 item 13).
- **The agent organizes it without a template.** Headings group clusters of ideas as needed. There are no date headings. Under each heading, the units read as a continuous train of thought.
- **Units keep the writer's meaning, specifics, and hedges. The agent may reword for readability, but never changes what an idea says or how firmly the writer holds it.**
- **Untagged units are tentative.**
- **It can hold** tentative and provisional material, Questions and other Work, and a Rejected section at the end.
- **A replaced unit stays in place, marked replaced.**

Frontmatter: `type: [idea-note]`. The first `type` value names a note's kind, and the agent reads it rather than the filename.

> [!question] Open
> How a replaced unit shows it was replaced. Only `replaces` on the new unit exists today. Handoff note, 04 item 19.

> [!note] Changes the guides
> The architecture guide, section 07, lists signals the agent uses to decide on its own that an idea earns a note. For now, the writer's comment decides.

### 01.4 Area Note

A note for one area of the story: a character, a relationship, a location, a group, a culture, a technology, an object, a theme, or a concept.

**An Area Note is the source of truth for committed material.** Every line in it must read correctly if every Idea Note disappeared.

It holds four things:

1) **Committed material,** rewritten as complete, plain statements. See 03.13 for how.
2) **Work about that material.**
3) **A Rationale section,** in the writer's words.
4) **A Rejected section,** at the end.

It never holds tentative or provisional material, and it carries no status tags.

> [!note] Changes the guides
> The architecture guide's Concept Note example, section 12, holds tentative and provisional lines. The metadata guide, section 07.4, says tentative and provisional lines in an Area Note carry a tag. Both go.

### 01.5 Concept Note

An Area Note for an idea the story is built around, whose rules or consequences reach across several areas of the story. Tradable memory is one: it touches Lena, her mother, the plot, the world's institutions, and the themes.

The admission test is that the idea cuts across areas. If it only shapes one area, it belongs in that area's note. Apart from that test, a Concept Note follows every Area Note rule.

### 01.6 Scene Notes

A note for one scene, in `{Project}/Plot/`, named `sc-{scene}.md`.

Expanded after the MVP build.

### 01.7 Rationale section

The section of an Area Note that holds the writer's reasons for committed choices.

It is in the writer's words. The agent never rewrites or summarizes it. See 02.3.

### 01.8 Rejected section

The last section of an Area Note or an Idea Note. Rejected material moves there, in the writer's words, with the writer's reason when one was given.

It keeps a rejected idea from being floated again without the writer knowing it was already turned down. Not every rejection has a reason. Sometimes it's just vibes.

The Brain Dump doc has no Rejected section. Rejected material there stays on its line, with its tag.

### 01.9 Work Items view

`{Project}/work-items.md`. A note made of Dataview queries that lists every Work Item across the project's notes, grouped by Work Type and by Open and Closed.

It stores nothing. The Work lives in the notes. No run writes to it.

### 01.10 Run

One pass of the plugin at one task. The writer starts every run. Nothing runs in the background.

There are five kinds of run: migration, Gaps, Review, Brainstorm, and Research (decisions-graph-prewriting-pt2.md 05 item 3).

- **The migration run works on whatever changed since the bookmark,** where the last migration run stopped.
- **The other four work on targets the writer picks when starting the run** (decisions-graph-prewriting-pt2.md 05 item 2).

> [!question] Open
> What a run does, step by step, and which agents take part. For the graph session.

### 01.11 Run log

A note the run writes when it finishes. It says what the run read, what it migrated and where, what it flagged, and what it could not do. It also says why each Idea Unit went where it did.

It is about the run, not the story. Story Work never goes in it.

> [!question] Open
> Its form and where it lives. For the graph session.

## 02 What the Writer's Words Contain

The writer's material mixes three kinds of words. The agent tells them apart, because each is handled differently.

### 02.1 Story substance

Anything the writer says about the story itself. That covers characters, events, relationships, rules of the world, and how those relate: causes, consequences, and contradictions.

"Lena's later sale contradicts her values" is story substance. It is the point of her arc, not an aside.

Story substance is never dropped. When it migrates into an Area Note, it is rewritten as plain statements, and every piece of it survives.

### 02.2 Notes-to-self

What the writer says about their own process or confidence, rather than about the story.

Examples: "I think," "definitely," "maybe," "for now," "not sure yet," "keep pushing on this," "I'll need to unpack this later."

A note-to-self that gives a reason for a story choice is rationale (02.3). "I really like that direction" on its own is a note-to-self. "Her mother selling memories feels more emotionally useful than Lena selling her own" is rationale.

The agent reads notes-to-self to understand the writer's intent. They never set an idea's status (03.2). They stay as written in the Brain Dump doc and Idea Notes. They are dropped when material is rewritten into an Area Note, because an Area Note records the decision, not the deliberation. A note-to-self that mattered gets baked into the committed material itself.

### 02.3 Rationale

A note-to-self that gives a reason for a story choice. It says why an idea is wanted, kept, preferred, or rejected. A bare like or dislike with no reason is a note-to-self, not rationale. The writer does not give a reason for every choice, only where the reason helps the agent understand the story.

Examples: "Her mother selling memories feels more emotionally useful than Lena selling her own." "They're pulling focus from the parts I actually care about." "Not sure if that's too Black Mirror."

Rationale is never dropped and never rewritten:

- In the Brain Dump doc and Idea Notes, it stays with its unit, inside the writer's notes-to-self. The Brain Dump doc has no Rationale section.
- In an Area Note, it goes in the Rationale section.
- With a rejected unit, it goes to the Rejected section.

## 03 Standing

### 03.1 Story authority

How strongly the writer has told the system to treat an idea as true, right now.

It is recorded as a status. It is separate from how much the writer likes an idea, how urgent the idea is, and which note it belongs in.

### 03.2 Status

The `#status/` tag family that records story authority. There are exactly four: tentative, provisional, committed, rejected.

- **The writer sets status** with a tag, a comment, or a tagged parent bullet. An untagged bullet nested under a tagged parent inherits the parent's tag. With none of those, a unit takes its note's default (03.7).
- **The agent never sets status from the writer's prose** (decisions-graph-prewriting-pt2.md 06 item 10). It writes the status the writer set as a tag where it migrates the unit. It never writes a status tag in the Brain Dump doc.
- **Deleting a tag returns the unit to its default status** (03.7).
- **"Unresolved" is not a status.** Something unresolved is a Question.

Status is not a ladder. An idea doesn't have to climb from tentative through provisional to committed. An idea may jump from a brain dump doc to an Area Note.

### 03.3 Tentative

"What if this is true?"

A possibility. It can be explored, compared, and kept. The agent does not build on it or treat it as true. Tentative material never gets Gaps.

### 03.4 Provisional

"For now, let's assume this is true."

A working assumption the writer wants to explore further: opening up options, then narrowing them down. The agent may build on it inside its own thread. Anything built on it stays tentative unless the writer raises it.

Not every idea passes through provisional. A character's name can go straight from untagged to committed.

Provisional material lives in Idea Notes, never in Area Notes. It gets scoped Gaps (03.11).

### 03.5 Committed

"This is true."

The writer has decided it is part of the story. Committed material migrates into Area Notes, rewritten as plain statements.

Committing an idea does not commit its unresolved details, or the ideas next to it in the same bullet. The writer can still change a committed idea later. Committed material gets Gaps.

### 03.6 Rejected

"This is not true," within the scope the writer gives (03.14).

The agent never deletes rejected material. In an Area Note or Idea Note, it moves to the Rejected section. In the Brain Dump doc, it stays on its line.

A writer's comment can reject by description: "Agent, reject all material that involves Lena being a professional clown." The agent tags every matching unit `#status/rejected`, except in the Brain Dump doc. There it writes no status tag unless a comment says to (decisions-graph-prewriting-pt2.md 06 item 11). It honors any carve-out in the comment: "…but preserve her early career motivation of wanting to improve childhood welfare."

### 03.7 Default status

What an untagged unit's status is, based on where it sits:

- **Brain Dump doc and Idea Notes:** tentative.
- **Area Notes:** committed, since they hold nothing else.
- **A Rejected section:** rejected.

The default applies whenever a unit has no tag, no comment that sets its status, and no tagged parent bullet. The writer's words don't change it. "Lena's mother definitely sold memories" in the Brain Dump doc is tentative until the writer tags it or a comment commits it. "Definitely" alone doesn't set committed (decisions-graph-prewriting-pt2.md 06 item 10).

### 03.8 Committed material and provisional material

The two base terms for where the story stands.

- **Committed material** is everything the writer has committed to. It lives in Area Notes. When pointing at specific pieces, say "committed choices."
- **Provisional material** is everything the writer is treating as true for now. It lives in Idea Notes.

Other terms build on these two: committed version, provisional version (03.10), committed contradiction, provisional contradiction (03.15).

> [!note] Changes the guides
> Replaces "working story model," "established story knowledge," "working version," "operative," "developmental contradiction," and "story contradiction." See 08.

### 03.9 Thread

A chain of connected ideas the writer is developing together, where later ideas depend on earlier ones. "Lena and her boyfriend's relationship arc" is a thread. So is "the cop foot-chase sequence."

A thread is provisional or committed. The agent traces a thread by following `depends_on` links (04.6).

> [!question] Open
> Whether the agent also needs a label that names a thread, so it can find a thread's members without following every link. For the graph session.

### 03.10 Version

One of two or more competing takes on the same story element. "Lena's mother sold memories when Lena was young" and "Lena sold her own memories" are two versions of Lena's history with the trade.

- **A provisional version** is one the writer is trying out.
- **A committed version** is the one the writer chose.

Two contradicting provisional versions can run at the same time, though that's rare.

### 03.11 Scoped

Limited to one provisional thread.

A scoped Gap is something a provisional thread needs in order to hold together. Suppose two provisional ideas: Ed has a deep fear of pain and heights, and Ed is a skydiving instructor. How he got from one to the other isn't earned yet. That is a scoped Gap.

- **While a thread is provisional, only its scoped Gaps are worked.** Its effects on the rest of the story wait, because fixing them is wasted work if the writer rejects the thread.
- **Unless the writer asks.** When the writer's comment asks, a provisional thread is checked against committed material, and the check returns scoped Gaps (decisions-graph-prewriting-pt2.md 07 item 5).
- **Scoped Gaps are weighed only against other Gaps in the same thread.**
- **When the thread is committed, its Gaps are no longer scoped.**
- **When the thread is rejected, its scoped Gaps are marked possibly moot.** This needs dependency tracking (05.10).

### 03.12 Graduation

When material becomes committed and migrates into one or more Area Notes, rewritten as plain statements.

Only the committed material graduates. Its uncommitted neighbors stay where they are. Graduation doesn't have to pass through an Idea Note: a committed line can go straight from the Brain Dump doc into an Area Note. Graduation is about authority, not quality. A dull choice the writer committed to still graduates.

### 03.13 Migrate

To carry an Idea Unit from one note to another: from the Brain Dump doc to an Idea Note, from an Idea Note to an Area Note, or from the Brain Dump doc straight to an Area Note.

- **The source keeps its line.** The Run script adds a `migrated-to` pointer to it once the copy is approved (04.7). The migrator never writes the pointer.
- **A Question migrates with its unit.** The source line loses its `[?]` checkbox, so the Question is never counted twice.
- **Migrating never changes status.**
- **Into an Idea Note, the unit keeps the writer's meaning, specifics, and hedges** (01.3).
- **Into an Area Note, the unit is rewritten** as complete, plain statements that read correctly without any Idea Note. The agent keeps every specific and every piece of story substance. It drops only notes-to-self. The rationale goes to the Rationale section, in the writer's words.

Example: "But Lena eventually selling one herself would be a strong contradiction in her behaviour; I think that happens later in the story" becomes "Lena eventually sells a memory herself, against her lifelong contempt for the trade."

Moving a rejected unit into its note's Rejected section is not migrating. That happens inside one note.

> [!note] Changes the guides
> Replaces "filing," "filed," and "moving" wherever they mean carrying a unit between notes.

### 03.14 Rejection scope

How far a rejection reaches, as the writer states it. It might cover a whole concept, one character, one use, or only "not yet."

The agent never widens a rejection:

- "The university version can probably go… it could belong to another character" rejects the idea for Lena, not for the project.
- "Don't establish detection technology yet" rejects it for now, not forever.

### 03.15 Contradiction

Two pieces of material that can't both be true.

- **A committed contradiction** is between two committed pieces. It is a real problem in the story. The agent flags it.
- **A provisional contradiction** is between two provisional versions. It is allowed and rare. The agent does not flag it.
- **Contradictions among tentative ideas** are normal exploration. The agent does not flag them.

A newer date never settles a contradiction. A later idea doesn't replace an earlier one unless the writer says so.

**Provisional material that contradicts committed material is not flagged while it is provisional.** It is one of the thread's wider effects, and those wait (03.11). When the thread is committed, it is checked against all committed material, and any contradiction left is a committed contradiction.

The exception: when the writer's comment asks, a provisional thread is checked against committed material while it is still provisional, and the check returns scoped Gaps (decisions-graph-prewriting-pt2.md 07 item 5).

## 04 Relationships and Pointers

### 04.1 Block ID

A short label at the end of a line, like `^lena01`, that lets another line point at that exact line.

The agent adds one only where something points at the line: `depends_on`, `replaces`, `alt_to`, `developed_from`, or a Work Item. The writer never types them.

> [!question] Open
> Everything below this callout is subject to a ledger. These relationships exist to track how ideas connect and change over time. Whether they live inline in the notes, in a ledger, or both depends on how the ledger is built. For the graph session.

### 04.2 Iteration

How an idea changed over time, compared to other ideas. There are three relationships: Lineage, Alternative, and Replacement.

Iteration is history. It stays true even after the story changes. It is separate from status.

### 04.3 Lineage

`[developed_from:: …]`. B grew out of A.

Recorded on B, pointing at A's line.

### 04.4 Alternative

`[alt_to:: …]`. A and B are competing versions of the same story element, and both are still live.

"I'm testing this version, not replacing anything yet" is an Alternative.

### 04.5 Replacement

`[replaces:: …]`. B took A's place.

- **It is recorded on B, pointing at A's line.**
- **Replacement doesn't reject A by itself.** A's status is a separate fact.
- **The agent never reads "testing" as a replacement.**

### 04.6 Story Dependency

`[depends_on:: …]`. One piece of material relies on another being true. If A changed, B might stop working.

- **The agent records it on B, pointing at A's line.** The writer never tracks dependencies.
- **It describes the story as it stands now, not history.** When the dependency goes away, the link goes.
- **A mention or a wikilink is not a dependency.** A line that names Lena doesn't depend on her note.

Chains of dependencies form threads (03.9).

### 04.7 `migrated-to` pointer

`[migrated-to:: [[…]]]`. An inline field on a source line that names the note or notes its unit migrated to, as a wikilink to the file. The wikilink uses the full vault path, with the file name as display text: `[migrated-to:: [[Projects/{Project}/Ideas/idea-tradable-memory|idea-tradable-memory]]]`.

The Run script writes one at every hop, after the Migration checker approves the copy (graph-prewriting-v1.md 5 item 4). The migrator never writes it. It is the only link between a source and its destination. Lines in the destination carry no link back. Obsidian's backlinks panel shows the reverse direction.

## 05 Work

### 05.1 Work Item and Work Type

A **Work Item** is a task line in a note that says something needs doing. "Work" means Work Items in general.

A **Work Type** is the kind of Work Item. Its checkbox character shows it:

| Work Type | Line |
| --- | --- |
| Question | `- [?]` |
| Gap | `- [g]` |
| Brainstorm | `- [b]` |
| Research | `- [r]` |
| Review | `- [R]` |
    
A Work Item's status in the story is separate from its own state. A Gap on committed material is not "committed."

> [!note] Changes the guides
> Retires "Work line" as a separate term, and retires the Opportunity type and its `- [*]` character. See 08.

### 05.2 Question

Something the writer hasn't decided or answered yet. Written as `- [?]`.

- How a Question differs from a Gap, with examples: `Projects/Script Asst/prewriting-phase/guide-work-types.md` 02.
- The full definition: `guide-work-types.md` 09.
- Why the writer types `- [?]` and the agent doesn't convert prose questions, and how a Question migrates with its unit: guide-metadata-and-markup.md 14.

### 05.3 Gap

Missing material that causes a plot hole or leaves something unearned. Written as `- [g]`.

- How a Gap differs from a Question, with examples: `Projects/Script Asst/prewriting-phase/guide-work-types.md` 02.
- Which material gets Gaps, including scoped Gaps: `guide-work-types.md` 05.
- The full definition: `guide-work-types.md` 09.

### 05.4 Brainstorm

A writer's request for the agent to think something through. Written as `- [b]`. It comes in two kinds, and the writer's comment says which:

- **Expansive:** "What does this idea open up? What consequences should I know about?"
- **Corrective:** "I need a solution to this one problem." For example: "Lena has no weapons. How does she get out of the room where the five-man hit squad has her cornered?"

The agent's ideas come back labeled `[AGENT]`, as tentative material. They can live in the Brain Dump doc.

**An exploratory expansive Brainstorm doesn't have to fit the committed choices.** It follows the writer's comment. The Writer's Statement is still its context (decisions-graph-prewriting-pt2.md 08 item 7).

> [!question] Open
> For an expansive Brainstorm that must fit the committed choices, the context it needs, so a solution doesn't cause unwanted ripples, has to come from a ledger. Holding a record is cheaper than having the agent work it out every time, and the agent's context is limited. Corrective Brainstorms and exploratory expansive ones don't wait for it (decisions-graph-prewriting-pt2.md 08 item 7). How that ledger is built is for the ledger pass.

### 05.5 Research

A request for facts. "Give me the 101 on the House's and Senate's powers." Written as `- [r]`. Research can apply anywhere, the Brain Dump doc included.

- **The writer's comment says where the findings go.** A quick lookup's fact goes under the `- [r]` line, opened by `[AGENT]`. A heavy run writes a research note, `{Project}/Research/research-{research-topic}.md` (decisions-graph-prewriting-pt2.md 08 item 8).
- **Whether a run fans out is the writer's call, by comment** (decisions-graph-prewriting-pt2.md 08 item 9).
- **Its inner steps aren't designed yet.** Research is confirmed as an agent task (decisions-graph-prewriting-pt2.md 08 item 4).

### 05.6 Review

A check across a provisional thread or committed material for anything that's present but no longer fits, such as an inconsistency, a committed contradiction, or a changed name ("Leon is suddenly called Joel in these scenes. Was that intended?"). Written as `- [R]`. Never flagged in the Brain Dump doc.

- **Missing material is a Gap, not a Review.** Gaps belong to the Gaps run (05.3).
- **A Review happens only when the writer asks.** The writer's comment names what changed and what to check against it, for example `%% Review char-lena against the new rule that sold memories are gone %%`. The writer supplies the dependency, so the agent doesn't trace it.
- **The agent proposes `- [R] [AGENT]` lines** in the notes that need a second look. Provisional material can get scoped Reviews, and committed material can get Reviews.
- **The automatic kind waits for the ledger.** In that kind, code finds what relies on a change (decisions-graph-prewriting-pt2.md 09 item 4).

> [!note] Changes the guides
> The guides call this Work Type "Review Need." This note uses "Review."

### 05.7 Proposal

Everything the agent offers is a proposal. Brainstorm results are always proposals. So is any Gap or Review the agent claims, because a claimed Gap or issue isn't true by default.

- **A proposed Work Item is a Work Item from the start.** It appears with its Work Type's checkbox, opened by `[AGENT]`: `- [g] [AGENT] …`.
- **The writer doesn't signal acceptance.** A proposal the writer leaves in place stands.
- **The writer rejects a proposed Work Item by marking it `- [-]`.**
- **A proposal keeps its `[AGENT]` label even after it stands.** The label shows where the material came from, and where it still needs the writer's own touch.
- **Brainstormed ideas come back as tentative Idea Units, opened by `[AGENT]`.** They can live in the Brain Dump doc.
- **Work the writer writes is not a proposal.**

> [!question] Open
> Whether a ledger keeps the history of which proposals stood and which were rejected. For the graph session.

### 05.8 Priority

How soon a Work Item should be worked on, based on how much depends on it.

The agent weighs necessity first: required work before optional work. Then it weighs how much other material the Work affects, how deep those effects run, and how much rework it risks if it's solved later.

Priority is not urgency and not preference. The point is not to perfect something small that a bigger fix will undo.

- **A priority appears on a Work Item's line only when the writer writes it, or when the agent writes it after weighing that Work against the Work around it.**
- **A writer-set priority wins.**
- **No Work Item gets a priority by default,** including a proposal that stands.
- **Before scene notes exist, the agent has no view across threads.** It weighs scoped Gaps within their thread, and ranks threads by what they mean to the story.

> [!question] Open
> How the agent does the weighing. Until that is designed, no agent writes priority. For the graph session.

### 05.9 Open and Closed

The two states of a Work Item.

- **Open:** the line shows its Work Type's checkbox character.
- **Closed:** the line is `- [x]` when resolved, or `- [-]` when declined (05.10).

There is no in-progress state and no deferred state. A closed line no longer shows what Work Type it was.

- [x] dfdf  [completion:: 2026-09-29]
- [-] dfdsfsddfsf
### 05.10 Closure outcomes

How a Work Item closed:

- **Resolved,** `- [x]`: the need was met.
- **Declined,** `- [-]`: the writer chose not to pursue it. A rejected proposal is declined.
- **Moot:** something upstream changed, and the need went away.

A closing reason can follow on the line, when there is one.

> [!question] Open
> Moot only means something when the agent tracks what depends on what. Without dependency tracking, the agent can't know a need went away. The same holds for marking an item "possibly moot," including the scoped Gaps of a rejected thread (03.11). Subject to the ledger. For the graph session.

## 06 Metadata and Signals

### 06.1 Metadata

Anything added to a note that describes the material instead of being part of it:

- tags, such as `#status/committed`
- comments, `%% … %%`
- inline fields, `[key:: value]`
- task checkboxes
- block IDs
- `[AGENT]` labels

The writer's metadata outranks the agent's reading (06.4).

> [!note] Changes the guides
> Retires "marker." Say which kind of metadata you mean instead.

### 06.2 Comment

`%% Agent, … %%`. A direct instruction from the writer to the agent.

Comments are for anything that isn't a clean yes or no: sending material to a note ("this belongs in Lena's note"), a rejection with a carve-out, "this earns an Idea Note," or permission to fix grammar in a line. A comment counts the same as a tag the writer typed.

### 06.3 Attribution

`[AGENT]` marks material the agent generated: Idea Units it created, Work it proposed, Brainstorm results, and notes it adds to the writer's lines. It opens the agent's text:

- An agent line: `- [b] [AGENT] …`
- A note on the writer's line: `- [?] Are they the one who introduced Lena to the idea? [AGENT] possibly moot: …`

Material the agent only migrated or rewrote keeps its original owner and carries no label. Anything unlabeled is the writer's.

### 06.4 Precedence

Which signal wins when two say different things about the same unit, on the same question.

For status:

1) The writer's metadata or comment.
2) A tagged parent bullet.
3) The default status of where the unit sits.

The writer's words aren't a level for status. The agent never sets status from them (decisions-graph-prewriting-pt2.md 06 item 10).

On other questions, the writer's metadata or comment still outranks the writer's words, and the words still count where the guides say they do. Iteration the writer states in words is one: "This replaces yesterday's version" (guide-metadata-and-markup.md 05.2).

The agent's own reading never outranks the writer's metadata.

Precedence applies only when both signals answer the same question. A comment about where material goes and a tag about its status don't compete.

### 06.5 Reading the writer's words

How the agent works out meaning and intent from what the writer wrote. It reads whole sentences in context, never single keywords.

- **It never works out status this way.** Status comes from the writer's tag, a comment, or a tagged parent bullet (03.2; decisions-graph-prewriting-pt2.md 06 item 10).
- **It keeps the words' hedges and specifics** when it rewords a unit in an Idea Note (01.3).
- **The Migration checker uses them** to catch a copy that lost a hedge (decisions-graph-prewriting-pt2.md 12 item 2).

"I definitely prefer this, but don't commit to it yet" is not committed, whatever "definitely" suggests.

Natural language is the writer's primary interface. Even when the writer states a status outright, the agent still reasons about everything else.

**Only the writer's status tags and comments trigger migration.** Plain prose doesn't. The writer tags each line, or writes a comment that says which bullets migrate (decisions-graph-prewriting-pt2.md 06 item 1).

> [!note] Changes the guides
> Replaces "NLI," short for natural-language inference.

## 07 Phases and Project Documents

### 07.1 Pre-writing, Writing, Polish

The plugin's three phases. They are the industry terms. "Phase" means only these three.

- **Pre-writing:** developing the story before the script. Brain dumps, Idea Notes, Area Notes.
- **Writing:** drafting and rewriting the screenplay. Drafts are numbered inside this phase, and rewriting belongs here.
- **Polish:** spelling, grammar, and format. Rewriting passes are not polish.

Source for Writing and Polish: `Projects/Script Asst/spec-script-asst-plugin.md` 04.

### 07.2 Writer's Statement

`{Project}/writers-statement.md`. The agent's primer for the project. It holds what the writer is trying to make and the context the agent needs to read story facts correctly: intent, tone, deliberate withholding, choices that look like problems but are intended.

It doesn't stop the agent from noticing things. It changes what the agent may conclude from them. It is a context input for every Gap and Brainstorm judgment.

Its sections are explained in `Projects/Script Asst/guide-writers-statement.md`.

## 08 Retired Terms

For reading older notes. Each term, and what replaces it.

| Retired | Use instead |
| --- | --- |
| Commentary | Notes-to-self (02.2) or rationale (02.3) |
| Working version | Provisional version or committed version (03.10) |
| Working story model | Committed material (03.8) |
| Established story knowledge | Committed material (03.8) |
| Operative | "Provisional or committed" |
| Developmental contradiction | Provisional contradiction, or a contradiction among tentative ideas (03.15) |
| Story contradiction | Committed contradiction (03.15) |
| Filing, filed, moving (between notes) | Migrate (03.13) |
| Work line | Work Item (05.1) |
| Opportunity, `- [*]` | Brainstorm, expansive kind (05.4) |
| Review Need | Review (05.6) |
| Acceptance, as a writer signal | None needed. A proposal left in place stands (05.7). |
| Deferred, `[deferred]` | Dropped. The writer's own priority says "not now." |
| In progress, `- [/]` | Dropped |
| Idea, `- [I]` | Dropped |
| Marker | Name the kind of metadata (06.1) |
| NLI | Reading the writer's words (06.5) |
| `source` property | Dropped. The `migrated-to` pointer and Obsidian's backlinks do the job. |

## Changelog

- 2026-10-01: the `migrated-to` pointer is written by the Run script, never by the migrator, to match graph-prewriting-v1.md 3 and graph-prewriting-v1.md 5 item 4. Ruled by Moe after a test run showed the old wording made an agent write the pointers itself.
    - 01.1: the Run script writes the block IDs and the pointers. The migrator writes nothing in the Brain Dump doc.
    - 03.13: the Run script adds the pointer once the copy is approved.
    - 04.7: the Run script writes the pointer at every hop, after the Migration checker approves the copy. The wikilink uses the full vault path with the file name as display text.
- 2026-09-30, later: applies decisions-graph-prewriting-pt2.md 14 item 6, from decisions-graph-prewriting-pt2.md 06 item 10, now Settled. Status comes from the writer's tag, a comment, or a tagged parent bullet, else the note's default. The agent never sets status from the writer's prose. Approved by Moe.
    - 02.2: notes-to-self show intent, not status.
    - 03.2: "The agent reads status from the writer's words" replaced. The writer sets status. Nested untagged bullets inherit a tagged parent's tag.
    - 03.7: the default applies whenever no tag, comment, or tagged parent sets status. "Definitely" alone doesn't set committed.
    - 06.4: for status, the ladder is the writer's metadata or comment, then a tagged parent bullet, then the default. The writer's words still count on other questions, such as Iteration stated in words.
    - 06.5: covers meaning and intent, not status. The agent keeps hedges when rewording, and the Migration checker uses them.
- 2026-09-30, later: 01.1's Brain Dump additions back to four. Research quick facts opened by `[AGENT]` take the slot the dropped prose-question conversion left (decisions-graph-prewriting-pt2.md 08 item 8). This corrects the "three" in the entry below. Directed by the orchestrating session.
- 2026-09-30: applies decisions from decisions-graph-prewriting-pt2.md 14 items 1, 2, 5, and 7 to 15. Approved by Moe. Items 3, 4, and 6 held.
    - 01.1: the agent adds three things, not four, unless a writer's comment asks for more. It no longer turns prose questions into `- [?]` lines (decisions-graph-prewriting-pt2.md 06 items 9 and 12).
    - 01.3: the agent may decide that material earns a new Idea Note, pending the tests. Its reason goes in the run log (decisions-graph-prewriting-pt2.md 06 item 13).
    - 01.10: a run is one pass at one task. Five run kinds. Only the migration run works from the bookmark (decisions-graph-prewriting-pt2.md 05).
    - 03.6: no agent status tag in the Brain Dump doc for a rejection by description, unless a comment says to (decisions-graph-prewriting-pt2.md 06 item 11).
    - 03.11 and 03.15: a provisional thread is checked against committed material when the writer's comment asks, and the check returns scoped Gaps (decisions-graph-prewriting-pt2.md 07 item 5).
    - 05.2: the pointer to guide-metadata-and-markup.md 14 describes no conversion.
    - 05.4: exploratory expansive Brainstorms don't have to fit the committed choices. The Open callout's ledger need narrowed to expansive Brainstorms that must fit them, and pointed at the ledger pass (decisions-graph-prewriting-pt2.md 08 item 7).
    - 05.5: Research no longer TBD. Where findings go and fan-out are the writer's call, by comment (decisions-graph-prewriting-pt2.md 08 items 8 and 9).
    - 05.6: Review no longer TBD. Gaps removed from what a Review finds. Review on request, `- [R] [AGENT]` proposals, the automatic kind waits for the ledger (decisions-graph-prewriting-pt2.md 09 item 4).
    - 06.5: Open callout closed. Only the writer's status tags and comments trigger migration (decisions-graph-prewriting-pt2.md 06 item 1).
- 2026-09-29, later: rationale defined as a note-to-self that gives a reason for a story choice (disposition decision 72). 02.2 and 02.3 updated; the Open callout on the line between them closed. Approved by Moe in chat.
- 2026-09-29, later: Brainstorm results can live in the Brain Dump doc, opened by `[AGENT]` (disposition decision 71). 01.1 lists four agent additions; 05.4 and 05.7 say where results can live. Approved by Moe.
- 2026-09-29, later: the guides, conventions, templates, and demos now match these definitions; the intro says the "Changes the guides" callouts are a record.
- 2026-09-29, later: approved by Moe. Idea Note `type` written as a list.
- 2026-09-29, later: Moe's review. New 01.6 Scene Notes, 01.6 to 01.10 renumbered. 03.15: provisional material contradicting committed material settled by the scoped-thread rule. 04: Block ID moved first; the rest marked Open, subject to a ledger, and renumbered. 05.2 and 05.3 cut to a definition plus pointers to `guide-work-types.md`. 05.4: context comes from a ledger. 05.7 rewritten: every agent offering is a proposal, a Work Item from the start, rejected with `- [-]`, keeps `[AGENT]`. 05.9 and 05.10: `- [x]` resolved, `- [-]` declined, Moot needs dependency tracking.
- 2026-09-29: created as a draft for Moe's review. Terms come from the list Moe approved in the guides-evaluation session. Definitions follow `Projects/Script Asst/prewriting-guides-disposition.md` section 0, decisions 1 to 53.
