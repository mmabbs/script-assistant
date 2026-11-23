# migrator-rules

This is the migrator's rulebook.

## Table of Contents

- Part A: The Notes
    - 01 The Notes and What Each Holds
        - 01.1 Brain Dump doc
        - 01.2 Idea Unit
        - 01.3 Idea Note
        - 01.4 Area Note
        - 01.5 Concept Note
        - 01.6 Rationale section
        - 01.7 Rejected section
        - 01.8 Reading a note's kind
    - 02 What the migrator May Do With the Writer's Words
        - 02.1 The two hard limits
        - 02.2 The rules for each note
        - 02.3 Filled Area Note demonstration
- Part B: Status
    - 03 Where Status Comes From
        - 03.1 The four statuses
        - 03.2 Status comes from tags and comments, never prose
        - 03.3 The default for each note
        - 03.4 Precedence
        - 03.5 Scope before precedence
        - 03.6 Keyword traps
        - 03.7 Where the migrator writes status tags
        - 03.8 Migrating never changes status
    - 04 One Bullet, Several Ideas
        - 04.1 Status applies to ideas, not bullets
        - 04.2 Tag scope
        - 04.3 Nested bullets and separate lines
        - 04.4 Committed parent, unresolved properties
        - 04.5 Partial graduation
- Part C: Reading and Placing
    - 05 Reading the Words
        - 05.1 What an Idea Unit is
        - 05.2 The natural brain-dump range
        - 05.3 Story substance, notes-to-self, and rationale
    - 06 Split and Merge
        - 06.1 Merging related Idea Units
        - 06.2 Splitting a dense source unit
        - 06.3 Duplicate, variant, consequence, or component
        - 06.4 The Spot example
    - 07 Choosing a Destination
        - 07.1 Status and destination are separate
        - 07.2 When material earns an Idea Note
        - 07.3 Idea Note layout
        - 07.4 Graduation
        - 07.5 Concept Note admission
        - 07.6 One unit, several notes
        - 07.7 The writer's routing comment wins
- Part D: Instructions and Limits
    - 08 Comments
        - 08.1 A comment counts as the writer's metadata
        - 08.2 Rejection and its scope
        - 08.3 Rejection by description, with a carve-out
        - 08.4 Reassignment
        - 08.5 Where rejected material goes
        - 08.6 A comment can allow more
        - 08.7 An unclear comment
        - 08.8 A comment that asks only for a tag
    - 09 Questions and Attribution
        - 09.1 Questions
        - 09.2 Work lines
        - 09.3 Attribution
    - 10 What the migrator Never Does
        - 10.1 Who writes what
        - 10.2 Nothing in the Brain Dump doc
        - 10.3 No Gaps, dependencies, or contradictions
        - 10.4 Only tags and comments trigger migration
        - 10.5 Where the migrator sits in a migration run

## Part A: The Notes

### 01 The Notes and What Each Holds

#### 01.1 Brain Dump doc

- **The Brain Dump doc is where the writer's material enters the system.** It holds dated entries of ideas off the top of the writer's head, in any form: typed, transcribed from voice, pasted, a link, an image.
- **How the material got there doesn't matter.** A voice transcript, a typed note, and a pasted paragraph are all information in the Brain Dump doc. An Idea Unit can include a web link or a wikilink to an image in `Attachments/`, and it is still a valid Idea Unit.
- **It is history: a record of what the writer thought, and when.** It is not a place to develop any one idea at length.
- **Untagged material here is tentative.** Rejected material stays on its line, with its tag.
- **Migrating copies an Idea Unit into its destination.** The Brain Dump doc is never trimmed. An Idea Unit's current standing lives on the migrated copy.
- **It has no Rationale section and no Rejected section.**
- **Its `type` list holds `brain-dump`:** `type: [brain-dump]`.

What the migrator may and may not write here: migrator-rules.md 02.2 and 10.2.

#### 01.2 Idea Unit

The smallest piece of the writer's material that means something on its own. It is one idea, in the writer's words, with whatever sentences it needs to stay readable. A single bullet can hold several Idea Units. An Idea Unit records that the writer considered something. It does not mean the thing is true in the story.

How to read Idea Units out of a bullet: migrator-rules.md 05.

#### 01.3 Idea Note

- **An Idea Note is a workspace where related Idea Units are gathered to be developed.** It is not a record of what is decided. An Idea Unit can exist without an Idea Note.
- **Its `type` list holds `idea-note`:** `type: [idea-note]`.
- **It can hold** tentative and provisional material, alternatives, contradictions, consequences, the writer's rationale, Questions and other Work, and a Rejected section at the end.
- **An Idea Unit in an Idea Note is tentative unless tagged otherwise.**
- **`type: [idea-note]` means the file is an Idea Note: a workspace.** It does not mean every possibility inside it has the same status, nor does it make the note's contents committed.

When material earns an Idea Note, and how one is laid out: migrator-rules.md 07.2 and 07.3.

#### 01.4 Area Note

An Area Note is a note for one area of the story: a character, a relationship, a location, a group, a culture, a technology, an object, a theme, or a concept. Its `type` list holds `area-note`.

**An Area Note is the source of truth for committed material.** Every line in it must read correctly if every Idea Note disappeared. It holds four things:

1) committed material, rewritten as complete, plain statements (see migrator-rules.md 02.2);
2) Work about that material;
3) a Rationale section, in the writer's words;
4) a Rejected section, at the end.

**It never holds tentative or provisional material, and it carries no status tags outside its Rejected section.** Each rejected line there keeps its `#status/rejected` tag (migrator-rules.md 08.5). Tentative and provisional material stays on its line at its source, in the Brain Dump doc or an Idea Note.

**A provisional or tentative line the writer left in an Area Note stays there.** That is a line tagged `#status/provisional` or `#status/tentative`. The migrator doesn't move, retag, or rewrite it. It asks the writer about it once, in the run log. The rule above is about what the migrator writes into an Area Note. This one covers a line the writer put there. It is not an exception the migrator makes. The writer's reason is the one quoted in migrator-rules.md 08.8.

Scene Notes, in `{Project}/Plot/`, are their own kind of note, not Area Notes. Their rules come after the MVP build.

#### 01.5 Concept Note

An Area Note for an idea the story is built around, whose rules or consequences reach across several areas of the story. Tradable memory is one: it touches Lena, her mother, the plot, the world's institutions, and the themes. A Concept Note follows every Area Note rule.

The admission test: migrator-rules.md 07.5.

#### 01.6 Rationale section

The section of an Area Note that holds the writer's reasons for committed choices, in the writer's words. What counts as rationale: migrator-rules.md 05.3.

#### 01.7 Rejected section

The last section of an Area Note or an Idea Note. It holds the note's rejected material, in the writer's words, with the writer's reason when one was given.

It keeps a rejected idea from being floated again without the writer knowing it was already turned down. Not every rejection has a reason. Sometimes it's just vibes.

The Brain Dump doc has no Rejected section.

#### 01.8 Reading a note's kind

```yaml
---
type: [idea-note]
---
```

- **The kind is whichever of `brain-dump`, `idea-note`, or `area-note` the note's `type` list holds, in any position.** A note holds only one of the three. The migrator reads the kind from here, not from the filename. Filenames are fragile, and the filename prefix is for the writer's at-a-glance lookups.
- **Three kinds change what the migrator does:**
    - **`brain-dump`:** untagged lines are tentative.
    - **`idea-note`:** untagged lines are tentative.
    - **`area-note`:** untagged lines are committed. The note carries no status tags outside its Rejected section.
- **A note the migrator creates gets its kind's frontmatter, and nothing else.** Four properties, in this order: `title`, `project` (copied from the source note's `project`, or left empty when the source has none), `created` (the run's date and time, as `YYYY-MM-DD HH:mm`), and `type`. `title` follows the template's form: `Idea - {Idea}`, `Char - {Name}`, `Relationship - {A} and {B}`, `Concept - {Concept}`, `Loc - {Location}`, `Group - {Group}`, `Culture - {Culture}`, `Tech - {Tech}`, `Object - {Object}`. The frontmatter is not in the record: the record holds body lines only.

| Note | File | `type` |
| --- | --- | --- |
| Idea Note | `Ideas/idea-{idea}.md` | `[idea-note]` |
| Character | `char-{character}.md` | `[area-note, character-profile, character-bio]` |
| Relationship | `rel-{char-a}-{char-b}.md` | `[area-note, relationship-profile]` |
| Concept Note | `Concepts/concept-{concept}.md` | `[area-note]` |
| Worldbuilding | `Worldbuilding/loc-{location}.md`, `group-{group}.md`, `culture-{culture}.md`, `tech-{tech}.md`, `obj-{worldbuilding-object}.md` | `[area-note]` |

`themes.md` is one note per project. The migrator never creates it.

### 02 What the migrator May Do With the Writer's Words

#### 02.1 The two hard limits

**Two hard limits hold in every note.** The migrator never deletes an idea. It never adds story material unless the writer asks for it or the agent's definition permits it, and it opens anything it adds with `[AGENT]`.

The migrator also never:

- changes the writer's words beyond what each kind of note allows (migrator-rules.md 02.2);
- raises a status the writer didn't grant;
- lets an uncommitted idea ride into an Area Note on a committed neighbor's back;
- reads preference, enthusiasm, or a later date as authority;
- asks the writer to maintain metadata.

#### 02.2 The rules for each note

**Beyond the two hard limits, what the migrator may do with the writer's words depends on the note:**

- **Brain Dump doc:** nothing. The words are untouched. The migrator writes nothing here (migrator-rules.md 10.2). A prose question stays in its bullet (migrator-rules.md 09.1).
- **Idea Note:** units keep the writer's meaning, specifics, and hedges. The migrator may reword for readability, but never changes what an idea says or how firmly the writer holds it. When the writer hedges a name or a detail, the migrator states the hedge once, where the name or detail is introduced, and doesn't use it as settled on other lines. Other lines refer to the thing by its role.
- **Area Note:** committed material is rewritten as complete, plain statements that read correctly if every Idea Note disappeared. The migrator keeps every specific and every piece of story substance, and drops only notes-to-self. A note-to-self that mattered gets baked into the committed material itself, because an Area Note records the decision, not the deliberation. Rationale goes to the Rationale section, in the writer's words. The migrator never rewrites or summarizes it. Work lines and Questions are not rewritten. migrator-rules.md 02.3 shows the result.
- **Any note:** a writer's comment can allow more, for example "fix the grammar here."

#### 02.3 Filled Area Note demonstration

A Concept Note is an Area Note, so it follows the Area Note rules (migrator-rules.md 01.4). It holds committed material only, rewritten as complete, plain statements that read correctly without any Idea Note. It carries no status tags outside its Rejected section. Its Questions are Work about the committed material. Its Rationale section keeps the writer's words. Its Rejected section comes last.

**The rewrite keeps every specific and every piece of story substance, and drops only notes-to-self.** "But Lena eventually selling one herself would be a strong contradiction in her behaviour; I think that happens later in the story" becomes "Lena eventually sells a memory herself, against her lifelong contempt for the trade." The contradiction is story substance, so it stays. "I think" is a note-to-self, so it goes.

```markdown
---
type: [area-note]
---

# Tradable Memory

## Core Idea

- Memory trading is part of the world.

## Story Version

- Lena can't recover a sold memory. Once it's gone, it's gone.
- A sold memory is still gone if the buyer dies.

## Story Implications

- Corporations purchase employee memories.

## Manifestations

- Lena's mother sold memories when Lena was young, so Lena grew up despising the trade.
- Lena eventually sells a memory herself, against her lifelong contempt for the trade.
    - [?] Not sure what forces her to cross that line yet.

## Rationale

- Her mother selling memories feels more emotionally useful than Lena selling her own.
- I prefer the childhood-sale version right now because it gives her something personal to be angry about. But I don't want her whole character built around victimhood.

## Rejected

%% Committed material the writer later rejects moves here. %%
```

Everything tentative or provisional about tradable memory stays in the Idea Note: the provisional working rule on repeated extraction, the provisional detection rule, the tentative student seller and its consequences, and the tentative line about what "repeated" means, with its unmarked questions inside it. Each migrates here only when the writer commits it. Committing the Concept doesn't commit its unresolved details.

The Question sits nested under the line it belongs to, so it reads correctly on its own. The writer typed it as a `- [?]` line. The migrator doesn't turn prose into Questions (migrator-rules.md 09.1). Unresolved material is a Question, written as `- [?]`, not a fifth status.

**A Concept Note, like any Area Note, holds no agent-written summary,** such as a "Core Idea" paragraph in the agent's words, unless the writer asks for one.

## Part B: Status

### 03 Where Status Comes From

`#status/...` represents the current story authority of an extracted idea. It answers:

> How should Script Assistant treat this proposition right now?

It does not answer how much the writer likes the idea, which file should receive it, or whether it should be collected with other Idea Units.

#### 03.1 The four statuses

The settled family is:

```text
#status/tentative
#status/provisional
#status/committed
#status/rejected
```

**Unresolved material is not a fifth status.** It is a Question, written as `- [?]`.

- **`#status/tentative`.** Canonical meaning: "What if this is true?" The idea is a possibility. It can be explored, compared, kept, or developed, but the system does not treat it as true. The agent doesn't build on it.
- **`#status/provisional`.** Canonical meaning: "For now, let's assume this is true." The proposition is a working assumption. The agent may build around it and use it to organize downstream development, while preserving that the writer may reverse it. Provisional material lives in Idea Notes, never in Area Notes. A provisional line the writer left in an Area Note stays there (migrator-rules.md 01.4).
- **`#status/committed`.** Canonical meaning: "This is true." The writer has decided it is part of the story. Committed material migrates into Area Notes, rewritten as complete, plain statements. That is graduation.
- **`#status/rejected`.** Canonical meaning: "This is not true." The proposition is no longer viable in the relevant scope. Rejection may apply to an entire idea or only to one use, character, context, or variation.

**The four statuses are not a ladder.** Most Idea Units go from untagged straight to committed or rejected. Provisional is only for a thread the writer is exploring. A character's name can go straight to committed. An idea can go straight from the Brain Dump doc to an Area Note.

No idea-level status property was settled. Do not invent one. The settled writer-facing form is `#status/...`.

#### 03.2 Status comes from tags and comments, never prose

- **The writer sets a unit's status with a tag, a comment, or a tagged parent bullet.** With none of those, the unit takes the note's default.
- **The migrator never sets status from the writer's prose.** Natural language is the primary interface for meaning. Status is different.
- **The migrator still reads the writer's words, whole sentences in context.** It keeps their hedges and specifics when it rewords a unit in an Idea Note. The migration-verifier uses them to catch a copy that lost a hedge.

#### 03.3 The default for each note

A line with no status tag still has a status. The kind of note it sits in sets it, and the kind is whichever of the three the note's `type` list holds (migrator-rules.md 01.8):

- **In the Brain Dump doc and in Idea Notes,** untagged means tentative.
- **In Area Notes,** untagged means committed. Area Notes hold only committed material, so they carry no status tags outside the Rejected section. Concept Notes are Area Notes.
- **In a Rejected section,** a line is rejected. Each line there also carries `#status/rejected`, which the migrator writes before it moves the line (migrator-rules.md 08.5).

This has three consequences:

1) Untagged Idea Units in the Brain Dump doc need no tag.
2) The live part of an Area Note needs no status tags at all. Tentative and provisional material never goes there; it stays on its line at its source.
3) Deleting a tag changes the fact, by the note's default. A tag that only restates the default can go. A tag that carries a fact stays.

#### 03.4 Precedence

Precedence is a conflict-resolution rule, not a ranking of which communication mode the system uses most often. It applies only when two signals address the same question, on the same axis, about the same proposition, and disagree.

For status, for the same proposition:

```text
1. the writer's metadata (a tag, a comment, or an inline field), or the writer's explicit instruction in a comment
2. a tagged parent bullet
3. the note's default
```

- **The writer's prose isn't a level for status.** The migrator never sets status from it.
- **The writer's metadata and the writer's explicit instruction sit on the same level.** An agent's tag never outranks the writer's.
- **The note's default is the last level.** It applies to any line with no tag, no comment that sets its status, and no tagged parent bullet. The prose doesn't change it.
- **A "maybe" line in an Area Note points to a mistake.** The unit was tentative at its source, and tentative material never belongs in an Area Note. The migration-verifier catches that kind of mistake by comparing the copy with its source.

**When a status tag and the surface wording seem to conflict, the tag sets the status.** The wording never does. These examples assume the writer wrote the tag.

```markdown
- Memory trading is definitely part of the world. #status/tentative
```

The tag says that the proposition remains tentative despite the word "definitely." The source wording should be preserved, but the proposition should not graduate as committed.

```markdown
- Maybe memories can be bought and sold. #status/committed
```

The explicit tag grants committed status despite the tentative surface form. The purpose of the example is to teach precedence, not recommend contradictory writing.

The migrator still reads the writer's words, for meaning and to work out which ideas a tag covers (migrator-rules.md 04.2). A tag does not license the migrator to stop reading or to spread one tag across unrelated ideas.

#### 03.5 Scope before precedence

Consider:

```markdown
### September 9

- I definitely prefer this, but don't commit to it yet. #status/tentative

%% Agent, the material about Lena's attitude toward memory trading belongs in [[Projects/{Project}/char-lena|char-lena]]. %%
```

The migrator should reason as follows:

- The whole utterance, not the word "definitely," describes tentative authority.
- The explicit status tag sets it. The words don't.
- The comment provides routing for Lena's attitude; it does not alter the status of unrelated material.
- `[[Projects/{Project}/char-lena|char-lena]]` identifies the related entity; it does not itself assign status.
- The date supplies chronological context; it does not establish preference or supersession.

**Precedence applies only after scope.** An explicit routing comment and a status tag do not conflict if one controls destination and the other controls authority.

#### 03.6 Keyword traps

Status is never assigned from words, isolated or whole. Only the writer's tag, a comment, or a tagged parent sets it. These traps still matter for meaning. They show why the migrator reads whole sentences, and why it keeps hedges when it rewords a unit.

```markdown
- I definitely prefer this, but don't commit to it yet.
```

`definitely` does not mean committed. The whole utterance explicitly withholds commitment. A keyword matcher may seize on "definitely" and assign committed. Reading the whole sentence reaches the opposite result.

```markdown
- I really like that direction. Keep pushing on the mother version, but don't throw out Lena selling her own memories yet.
```

"Really like" and "keep pushing" communicate evaluation and developmental priority. They do not establish the mother version as story truth or reject the competing Lena version.

```markdown
- I think this is probably the version, unless I come up with something better.
```

The hedging and retained reversibility matter. The migrator should read the complete statement rather than treat "the version" as an automatic commitment.

#### 03.7 Where the migrator writes status tags

- **A migrated copy carries the status tag the writer gave its source, or the one the writer's comment asks for. The migrator never chooses a tag.** A source with no tag gets a copy with no tag.
- **The migrator never writes `#status/tentative`.** Tentative is the name for untagged material, not a tag the migrator adds.
- **It writes `#status/rejected` on a unit it rejects, then moves the unit to the Rejected section** (migrator-rules.md 08.5).
- **It never writes a status tag in the live part of an Area Note.** The only status tag an Area Note carries is `#status/rejected`, inside its Rejected section.
- **It never writes a status tag in the Brain Dump doc unless a writer's comment says to** (migrator-rules.md 08.6). The Brain Dump doc is history. A status tag there is the writer's, or one the writer asked for, and it wins.
- **A writer's tag wins, in the Brain Dump doc and in a migrated copy alike.** An agent's tag never outranks the writer's. If the writer already tagged an idea, the agent has no reason to tag it again.
- **A tag in a migrated copy that doesn't match its source's status is one of two things:** the writer's correction, which wins, or an agent mistake to be corrected.

#### 03.8 Migrating never changes status

**Migrating never changes status.** An Idea Unit migrated into an Idea Note keeps its status until the writer's tags or comments change it. Graduation rewrites committed material as complete, plain statements, and the status does not change in the rewrite.

### 04 One Bullet, Several Ideas

#### 04.1 Status applies to ideas, not bullets

One natural source unit can contain several authority states. This is the September 9 bullet:

```markdown
- Lena's mother definitely sold memories when Lena was young. Lena therefore grew up despising the trade. But Lena eventually selling one herself would be a strong contradiction in her behaviour; I think that happens later in the story. Not sure what forces her to cross that line yet.
```

The ideas in it describe different standings:

- the mother sold memories — committed;
- Lena grew up despising the trade — committed consequence;
- Lena later sells a memory — committed intent;
- what forces the sale — unresolved, not a status. It is a Question only if the writer types it as `- [?]`. Otherwise it stays inside the unit as unmarked text;
- the contradiction with Lena's values — relationship among propositions, not a separate status.

**The migrator doesn't set these from the wording.** Untagged, with no comment, every idea in the bullet takes the Brain Dump doc's default, tentative. If the writer tags the bullet, or a comment sets its status, the migrator works out which ideas the tag or comment covers.

A tag placed at the end of a dense bullet may have ambiguous scope. The migrator must determine which proposition the writer meant it to modify rather than automatically applying it to everything in the Markdown unit.

#### 04.2 Tag scope

A tag placed near a source unit does not automatically apply to every proposition inside that unit.

**Clear scope:**

```markdown
- Let's use that as the working rule: isolated sales are usually manageable, repeated extraction increases the risk of cognitive and emotional impairment. #status/provisional
```

The tag clearly modifies the stated rule.

**Ambiguous trailing scope:**

```markdown
- The mother selling Lena-related memories stays. I don't know yet whether she knowingly chose those specific memories or whether the clinic determines what's extracted according to value. Those produce very different versions of the mother, so keep both possibilities open. #status/committed
```

The bullet contains:

1) the mother sold Lena-related memories — committed;
2) she knowingly chose those memories — tentative;
3) the clinic selected them by value — tentative;
4) both property variants should remain open — developmental instruction.

The trailing tag should not be spread across the whole bullet. Reading the whole sentence shows that the commitment applies to the parent idea, while the sentence explicitly keeps both mechanisms unresolved. Applying `#status/committed` to the whole bullet would be wrong.

**Mixed authority in one source unit:**

```markdown
- Memory trading is definitely part of the world. Does selling a memory remove it from the seller or just create a copy? Rich people collecting childhood memories feels promising.
```

The ideas in it describe:

- committed existence;
- an open Question about the mechanic;
- tentative collector possibility.

Untagged, the whole bullet is tentative. The words alone don't commit the first idea. Adding one status tag to the end without clarifying scope leaves the migrator to work out which idea it covers. A comment that names the idea is more reliable.

**The rule for anyone adding a tag, writer or agent: add it only when the proposition and its authority are both clear.** Leave mixed, qualified, or structurally tangled material untagged, or scope it with a comment. Untagged, it keeps the note's default, and the migrator still reads the whole utterance for meaning.

#### 04.3 Nested bullets and separate lines

**An untagged bullet nested under a parent bullet that carries a status tag inherits the parent's tag.** The writer: "The ideas that will be developed will have #status/provisional. Depending on how related they are, they might be nested untagged bullets under a parent bullet that carries the tag, which means the child bullets inherit the parent's tag."

**Separate lines don't inherit.** A provisional proposition may organize development without donating its status to its consequences.

```markdown
- Assume for the moment that the university can detect recent memory transfers but can't reliably prove what was transferred.
```

That provisional rule generates possibilities:

```markdown
- If that's true, students could get flagged just for having undergone extraction, even if they sold an unrelated childhood memory to pay rent.
- That could create an ugly presumption of cheating.
- The institution might end up policing people's economic survival rather than merely fighting academic dishonesty.
```

The children are development spawned by the provisional parent. They remain tentative unless the writer independently grants them stronger authority. They are separate lines, not nested bullets, so they stay tentative.

#### 04.4 Committed parent, unresolved properties

Commitment to existence does not commit every property. In both examples below, suppose the writer commits the first idea with a tag or a comment. The wording alone wouldn't commit it.

```markdown
- I think memory trading should definitely be part of the world.
- [?] Does selling a memory remove it from the seller or just create a copy?
```

The existence of memory trading is committed. The transfer mechanic remains an open Question.

The same pattern appears in the trailing-tag example in migrator-rules.md 04.2, with the writer's tag or comment covering only the parent idea.

**The migrator must not promote the entire cluster merely because its parent idea is committed.**

Only the committed parent migrates into an Area Note, rewritten as a plain statement: "The mother sold Lena-related memories." The two tentative variants stay where they are, in the Brain Dump doc or an Idea Note. An Area Note holds only committed material, so the variants never sit there as possibilities. The open Question about the transfer mechanic can migrate with its unit and sit in the Area Note as Work.

#### 04.5 Partial graduation

**Only the propositions with committed authority graduate, never the whole bullet as a block.**

Suppose the writer's tag or comment commits the first idea. The migrator works out which ideas it covers (migrator-rules.md 04.2). The word "definitely" doesn't commit anything on its own.

```markdown
- Memory trading is definitely part of the world. Corporations buying employee memories could be useful. Rich people collecting childhood memories feels promising.
```

Only the first idea is committed. The corporate and collector possibilities remain tentative. Graduation applies to the committed idea, not to the whole topical cluster.

A bullet can also mix a commitment with a Question, as in the mixed-authority example in migrator-rules.md 04.2. Only the existence of memory trading is committed. The removal-versus-copy mechanic is an open Question. The collector idea remains tentative. The migrator must not graduate the whole bullet as a block.

If corporate purchasing later "stays," and the writer tags or comments it, it graduates independently. If memory collectors later become "out," and the writer tags or comments that, they become rejected independently.

## Part C: Reading and Placing

### 05 Reading the Words

#### 05.1 What an Idea Unit is

An Idea Unit is the smallest independently meaningful developmental proposition pulled out of the Brain Dump doc.

Its existence means:

> The writer generated or considered this possibility.

It does not mean:

> This is true in the story.

- **An Idea Unit is a semantic unit, not necessarily a Markdown unit.** A Markdown bullet is a source unit. It is not automatically one Idea Unit. One bullet may contain one Idea Unit, several Idea Units, notes-to-self, rationale, questions, and instructions.
- **The migrator pulls a ball-of-yarn bullet apart and groups the pieces, including pieces from different notes.** What the migrator says an Idea Unit is about is the migrator's reading. The Idea Unit itself belongs to the writer.
- **Pulling a bullet apart doesn't mean every sentence becomes its own Idea Unit in its own note.** A piece keeps the sentences it needs to stay readable. If a question says "the person" and means the seller named in the sentence before it, the two stay together (migrator-rules.md 05.2).
- **How the migrator handles an Idea Unit's words depends on the note it sits in.** See migrator-rules.md 02.2.
- **The writer checks how the migrator grouped Idea Units, by reading the migrated result.** There is no automated check.

#### 05.2 The natural brain-dump range

**Several related propositions:**

```markdown
### September 1

- Maybe memories are currency somehow. People sell traumatic memories? Or rich people buy childhood memories because nostalgia becomes a luxury product. Could also be how Lena paid for school. Not sure if that's too Black Mirror.
```

The migrator should pull out at least these Idea Units, each in the writer's words:

1) "Maybe memories are currency somehow."
2) "People sell traumatic memories?"
3) "Or rich people buy childhood memories because nostalgia becomes a luxury product."
4) "Could also be how Lena paid for school."

The final sentence is rationale: the writer's judgment of how familiar the idea feels. It is not another story proposition.

**A natural ball of yarn:**

```markdown
### September 17

- Someone could sell memories to finance university. Does the person know Lena? Are they the one who introduced Lena to the idea? What if selling memories does in fact have a negative cognitive effect? Can they blunt their intelligence that way? What if the university has this underground culture of kids selling to another memories that can help the other excel in school? I'll need to unpack the aspects/types of memories that can be sold, and whether they impact intelligence...
```

The migrator should not preserve this as one undifferentiated "memory-selling idea." It contains:

- a tentative student seller;
- a question about the seller's relationship to Lena;
- a possible causal role in introducing Lena to memory selling;
- a possible cognitive cost;
- a possible loss of intelligence;
- a possible underground campus market;
- a possible transfer of useful academic knowledge;
- an explicit need for further development of memory types and their relationship to intelligence.

That list is the migrator's reading. The Idea Units stay in the writer's words. One way the pieces could group:

1) "Someone could sell memories to finance university. Does the person know Lena? Are they the one who introduced Lena to the idea?" — the seller, the question about Lena, and the introduction role. The two questions stay with the first sentence because "the person" and "they" mean the seller.
2) "What if selling memories does in fact have a negative cognitive effect? Can they blunt their intelligence that way?" — the cognitive cost and the loss of intelligence.
3) "What if the university has this underground culture of kids selling to another memories that can help the other excel in school?" — the campus market and the transfer of academic knowledge.
4) "I'll need to unpack the aspects/types of memories that can be sold, and whether they impact intelligence..." — the need for further development.

Those units share a source block and a conceptual neighborhood, but they do not necessarily share status or destination.

#### 05.3 Story substance, notes-to-self, and rationale

The writer's material mixes three kinds of words. The migrator tells them apart, because each is handled differently.

- **Story substance** is anything the writer says about the story itself. That covers characters, events, relationships, rules of the world, and how those relate: causes, consequences, and contradictions. "Lena's later sale contradicts her values" is story substance. It is the point of her arc, not an aside.
- **Notes-to-self** are what the writer says about their own process or confidence, rather than about the story. Examples: "I think," "definitely," "maybe," "for now," "not sure yet," "keep pushing on this," "I'll need to unpack this later." Notes-to-self show the writer's intent, not an idea's status.
- **Rationale** is a note-to-self that gives a reason for a story choice. It says why an idea is wanted, kept, preferred, or rejected. A bare like or dislike with no reason is a note-to-self, not rationale. Examples: "Her mother selling memories feels more emotionally useful than Lena selling her own." "They're pulling focus from the parts I actually care about." "Not sure if that's too Black Mirror."

The writer's notes-to-self and rationale stay attached to the idea they are about.

```markdown
- Maybe her mother sold memories instead. I really like that direction. Keep pushing on the mother version, but don't throw out Lena selling her own memories yet.
```

The migrator should distinguish:

- **story substance:** "Maybe her mother sold memories instead.";
- **notes-to-self:** "I really like that direction," "Keep pushing on the mother version," and "don't throw out Lena selling her own memories yet." None of them gives a reason, so none is rationale.

"I really like that direction" should not become an Idea Unit such as "The mother version is likeable." "Keep pushing" is not stronger story authority. Notes-to-self and rationale shape how the migrator reads the idea. They never become facts about the story.

**Where rationale goes.** A note-to-self that gives a reason is rationale, and rationale is kept wherever the idea goes. The writer does not owe a reason for every choice.

- **In the Brain Dump doc and Idea Notes,** rationale stays with its unit, among the writer's notes-to-self. The Brain Dump doc has no Rationale section.
- **In an Area Note,** it goes in the Rationale section, in the writer's words.
- **Notes-to-self are dropped only when material is rewritten into an Area Note** (migrator-rules.md 02.2).
- **Metadata must not erase rationale.** Rationale often matters later when comparing versions or understanding what an idea is meant to accomplish.

### 06 Split and Merge

"Merge" and "split" describe agent operations. They are not settled writer-facing metadata directives.

#### 06.1 Merging related Idea Units

Several source units may express or develop the same underlying possibility, including units in different notes:

```markdown
### September 1

- Maybe memories can be bought and sold.
- Rich people collecting other people's childhood memories feels promising.

### September 3

- Corporations buying employee memories could be useful, especially if they can purchase work-related experience when someone leaves a company.

### September 9

- Memory trading is definitely part of the world.
```

**Merging means recognizing that these units contribute to a shared developmental object** such as `Tradable Memory`, while preserving each unit's meaning, status, and date, and the pointer at its source.

**Merging does not mean flattening them into one claim.** The luxury market, corporate ownership, and the existence of memory trading are related, but they are different propositions and may have different authority.

#### 06.2 Splitting a dense source unit

Consider:

```markdown
- Maybe the dead can leave memories behind, and corporations can buy them.
```

Splitting means recognizing separate developmental threads:

1) memories may persist after death;
2) corporations may purchase memories.

These propositions may later interact, but one concerns persistence and the other commercial ownership. They should not be forced into the same destination merely because they appeared in one sentence.

**When the threads sit in one sentence, the Idea Unit may still be the whole sentence, migrated to two places.** The split is in where it goes, not in rewriting the writer's words.

**The split test: can each part be true without the other?** If so, the parts can split. When split pieces land in the same Idea Note, they sit next to each other, not at opposite ends of a list. Pieces can still go to different notes when their destinations differ.

#### 06.3 Duplicate, variant, consequence, or component

Shared vocabulary is not enough to justify merging.

- "Maybe memories can be sold" and "Memories have financial value" may be near-duplicates or two formulations of the same core possibility.
- "People can only sell memories they actively want to forget" is a variant or proposed rule governing memory sales.
- "Debt can literally shorten someone's life" is a consequence in the lifespan-selling example, not a restatement of the core idea.
- "Memory banks are federally regulated institutions" is a component of the world system generated around memory trading, not the Concept itself.

**The migrator should identify the relationship before choosing a structure.**

#### 06.4 The Spot example

The writer: "It should only pay attention to the construction of the words when things are being migrated." That includes "merging/splitting requires understanding the words and ensuring context isn't lost within that idea unit when it's moved."

The writer's example, word for word. "Intake" is the earlier placeholder name for the migration run.

> **Intake** -- correct read: "Lena's childhood trauma involves her dog Spot getting hit by a car. The ghost of Spot guilt-trips her in Plot Present." --> Intake's concerns: "the two ideas here can be split into two separate bullets in the Idea Note, since "guilt-tripping Spot-as-ghost" can be true whether or not he was hit by a car. Similarly, she can still be traumatized by the event without the inclusion of the ghost dog as a character. It's also best that these two bullets succeed each other, rather than moving one bullet all the way down a list of bullets in the Idea Note".
>
> **Intake -- incorrect read: "Lena's childhood trauma involves her dog Spot getting hit by a car. The ghost of Spot guilt-trips her in Plot Present." --> Intake's false concern: "Hmmm, this idea clashes with one about Lena growing up in a household that couldn't afford pets. Did their economic situation change at some point? That's a gap."

### 07 Choosing a Destination

#### 07.1 Status and destination are separate

The same idea can move between statuses without changing what it is about.

```text
“Maybe Lena sold memories to pay for university.”
    status: tentative
    semantic area: Character / Lena

“For now, assume Lena sold memories to pay for university.”
    status: provisional
    semantic area: Character / Lena

“Lena sold memories to pay for university.”
    status: committed
    semantic area: Character / Lena
```

The status changes. The semantic subject does not. Each wording describes its status. The writer still sets the status with a tag, a comment, or a tagged parent bullet.

**Committed status triggers graduation into an Area Note. It does not specify which one.** The writer may grant authority without naming a destination:

```markdown
- Corporations purchasing employee memories stays. That feels like an important consequence of the system. #status/committed
```

The migrator should follow the writer's tag, preserve the rationale, and decide whether the material updates the `Tradable Memory` Concept, a corporate Worldbuilding note, or both. A Concept Note is one type of Area Note, so both of these are candidates:

```text
{Project}/Concepts/concept-tradable-memory.md
{Project}/Worldbuilding/culture-memory-economy.md
```

or both.

#### 07.2 When material earns an Idea Note

- **Not every Idea Unit needs a note.** The migrator may decide that material earns an Idea Note. A writer's comment can also say which material earns one:

```markdown
%% Agent, the memory-trading material earns its own Idea Note. %%
```

- **There is no size threshold.** One load-bearing bullet can earn a note, and half a page of Idea Units can be rejected outright. When the writer states an intent, the migrator acts on it.
- **Once the writer asks, or the migrator decides, the migrator creates the note and organizes it without a template.**
- **Its reason for creating a note, or not, goes in the run log.**

#### 07.3 Idea Note layout

- **An Idea Note has no date headings.**
- **Headings group Idea Units by semantic cluster, as needed.** Under each heading, the units run as a continuous train of thought.
- **The Rejected section comes last.**
- **Whether a topic gets one Idea Note or two is decided case by case.**
- **The existence of an Idea Note grants none of its contents committed status.** The note records a development space.

#### 07.4 Graduation

Graduation is when material becomes committed and migrates into one or more Area Notes, rewritten as complete, plain statements.

It means:

> Treat this as true, unless the writer later changes it.

It does not mean:

- the idea is permanent;
- the idea is artistically excellent;
- an Idea Note is mandatory first;
- the writer has specified a file operation;
- every neighboring idea graduates with it.

**Graduation is not a directive.** A `#status/committed` tag grants story authority. The migrator must still decide whether the proposition should update a Concept Note, create one because the idea is cross-cutting, update Worldbuilding material, affect Character notes, or migrate to several Area Notes at once.

**Direct graduation without an Idea Note.** An explicit commitment can migrate directly from the Brain Dump doc into an Area Note:

```markdown
### September 9

- Lena's mother definitely sold memories when Lena was young. #status/committed
```

The writer's tag is what tells the migrator to migrate the line. The migrator does not need to create a temporary Idea Note merely to satisfy a lifecycle ceremony. It can update:

```text
{Project}/char-lena.md
```

and, if the mother has her own Area Note:

```text
{Project}/char-lenas-mother.md
```

The Run manager then adds a `migrated-to` pointer at the source.

**Graduation is not quality.** The writer can commit a functional but unexciting choice, and it still graduates. The writer can also call a possibility "promising" or say "I really like that," and it remains tentative if the writer has not made it provisional or committed. The system tracks authority, not its own aesthetic ranking.

#### 07.5 Concept Note admission

The positive admission criterion is:

> Create or maintain a Concept Note when an idea is something the story is built around and its rules or implications propagate across several story domains.

- **Concept is not a miscellaneous category** for anything that does not fit Character, Plot, Theme, Worldbuilding, or Research. It has downstream effects on most, if not all, of these areas.
- **If it only shapes one area, it belongs in that area's note.**

**Concept is a generative proposition.** Compare:

```text
Concept:
Memories can be bought and sold.

Character:
Lena despises memory trading because her mother sold memories.

Plot:
Lena eventually sells a memory herself.

Worldbuilding:
Memory banks are regulated institutions.
```

The Concept asks, "What is this idea, as this story understands it?" Worldbuilding asks, "If this idea is true, how does the world work?" Character and Plot ask how the committed idea shows up through a person and through events.

**Concept versus Worldbuilding.** "Memories can be traded" is a story-generating Concept. "The university publicly prohibits memory trading for academic purposes while quietly knowing it happens" is a possible institutional consequence and therefore Worldbuilding. They are related, but not interchangeable. The second depends on the first and specifies how one part of the world responds.

**One Concept, multiple Area manifestations.** A committed `Tradable Memory` Concept may connect to:

- **Character:** Lena, her mother, and the student seller;
- **Plot:** Lena eventually crossing the line and selling a memory;
- **Worldbuilding:** extraction rules, markets, detection, and institutional policy;
- **Group:** organizations that buy, regulate, or oppose memory sales;
- **Location:** a university campus where an underground trade may operate;
- **Theme:** identity, ownership of self, sacrifice, and economic coercion.

#### 07.6 One unit, several notes

**One committed source unit may have several semantic destinations.** A proposition about memory trading can update a Concept Note, a Character note, and Worldbuilding material without having several different statuses merely because it appears in several places.

#### 07.7 The writer's routing comment wins

The writer normally supplies story material and intent while the migrator reasons about extraction, structure, routing, relationships, and system representation. When the writer already knows the destination, the division of labor is not absolute:

```markdown
- Lena therefore grew up despising the trade.

%% Agent, the material about Lena's attitude toward memory trading belongs in [[Projects/{Project}/char-lena|char-lena]]. %%
```

The comment explicitly routes the material to:

```text
{Project}/char-lena.md
```

- **With the comment, the migrator follows the override and extracts the idea correctly.** The writer has supplied one explicit destination.
- **Without the comment, the migrator infers the Character destination and determines whether other notes are also affected.**
- **When explicit writer input and agent inference disagree, the writer wins.**
- **The migrator still reasons about everything the explicit signal does not settle.**
- **A routing comment does not automatically change status.** It says where material goes. The status comes from the tag, comment, or tagged parent on its line (migrator-rules.md 03.5).

## Part D: Instructions and Limits

### 08 Comments

#### 08.1 A comment counts as the writer's metadata

- **A writer's instruction in a comment counts the same as the writer's metadata.** `%% Agent, add a committed status here %%` and typing `#status/committed` are the same signal. The tag is usually just faster to write. Both set the same status. In the Brain Dump doc, only the typed tag moves the line (migrator-rules.md 08.8).
- **A comment is a direct instruction from the writer to the agent:** `%% Agent, … %%`. Comments are for anything that isn't a clean yes or no: sending material to a note ("this belongs in Lena's note"), a rejection with a carve-out, "this earns an Idea Note," or permission to fix grammar in a line.
- **A comment the run wrote to carry the writer's request counts as the writer's comment.** `%% [AGENT] Your request from the migration run of 2026-10-23, for this line: "…" %%` holds the writer's own typed request, word for word, from a run whose work on that line was undone or missed. Follow it as the writer's instruction, for the line above it only. Its `[AGENT]` label shows only who wrote the comment; the words are the writer's.
- **Comments win, and nothing fails on a narrow definition.** The writer: "There shouldn't be such tight constraints in this plugin such that the agent simply ignores comments or silently fails b/c of some narrow definition. It's still permitted to communicate with me for whatever reason -- clarification, etc. -- "outside" its role. What I don't want to see is "cannot proceed b/c you asked me to turn a letter into lower-case"".

Routing comments: migrator-rules.md 07.7. Comments that say material earns an Idea Note: migrator-rules.md 07.2.

#### 08.2 Rejection and its scope

**Rejection must be interpreted at the scope the writer supplies.** The writer sets the rejection itself with a `#status/rejected` tag or a comment. "Can probably go" or "are out" alone doesn't reject anything. The words, and the writer's comments, give its scope.

```markdown
- The university version can probably go. Actually, save it somewhere. It could belong to another character.

%% Agent, if the university-memory idea comes out of Lena's material, don't discard it. Keep it available for reassignment. %%
```

The following proposition is being rejected for Lena:

```text
Lena sold memories to finance university.
```

The generalized proposition remains viable:

```text
Someone sold memories to finance university.
```

Removing the idea from:

```text
{Project}/char-lena.md
```

does not reject it for the whole project. The idea can remain available for another Character or in an Idea Note.

By contrast:

```markdown
- Memory collectors are out. They're pulling focus from the parts I actually care about.
```

rejects that variation everywhere, not just for one character.

**A rejection's scope can be a whole concept, one character, one use, or "not yet."** "Don't establish detection technology yet" rejects it for now, not forever. The migrator never widens it.

#### 08.3 Rejection by description, with a carve-out

A comment can reject by description, with a carve-out:

```markdown
%% Agent, the premise that Lena is a professional clown is now rejected, but preserve her early career motivation of wanting to improve childhood welfare. %%
```

- **The migrator tags every matching unit `#status/rejected`, then moves it to its note's Rejected section** (migrator-rules.md 08.5). It leaves the carved-out material alone.
- **In the Brain Dump doc, the unit stays on its line, and the migrator writes no status tag unless a comment says to.** There, the rejection comment is the record.
- **Not every rejection comes with a reason.**

The writer on why a tag can't do this job: "Rejections with comments require reasoning b/c some units might have one idea that's rejected, but the rest pass. You can't convey that in a tag."

#### 08.4 Reassignment

**The migrator follows the writer's reassignment comment.** The reassignment comment in migrator-rules.md 08.2 changes handling. It prevents removal from one context from being mistaken for project-wide rejection. It does not define a new status, and it does not establish a general reassignment tag.

#### 08.5 Where rejected material goes

- **In an Idea Note or Area Note, the migrator tags rejected material `#status/rejected`, then moves it, in the writer's words, to the Rejected section at the end, with the writer's reason when one was given.** This holds in an Area Note too. The tag lets a Dataview query find every rejected line, and the section keeps the note clean.
- **In the Brain Dump doc, rejected material stays on its line.**
- **Moving a rejected unit into its note's Rejected section is not migrating.** That happens inside one note.
- **The writer's reason stays with the line.** When the writer tags the collectors rejection in migrator-rules.md 08.2 `#status/rejected`, or rejects it in a comment, the rationale, "pulling focus," still stays with the line. It goes with the unit to the Rejected section of an Idea Note or Area Note. It can keep the rejected idea from being floated again for reasons that ignore the writer's concern.
- **The reason goes on the line below the rejected line, as a comment that holds only the reason, in the writer's words:** `%% They're pulling focus from the parts I actually care about. %%`. The rejected line itself is its source line with its `#status/rejected` tag, and nothing else. The instruction part of the writer's comment, such as "Agent, reject this," is not copied.

#### 08.6 A comment can allow more

- **In any note, a writer's comment can allow more than these rules do,** for example "fix the grammar here."
- **A comment can ask the migrator to add status tags in the Brain Dump doc.** The writer: "I might have a comment that tells the agent to add tags just b/c I'm feeling cute."
- **A comment can ask the migrator to convert prose questions** (migrator-rules.md 09.1).

#### 08.7 An unclear comment

**When the migrator can't tell what a comment means, it asks the writer in the run log and finishes the rest of the run.** It never guesses. "Move the good ones" names no bullets, so nothing moves and the run log asks which ones are meant.

#### 08.8 A comment that asks only for a tag

- **In the Brain Dump doc, a comment that asks only for a status tag doesn't move the line.** The migrator adds the tag. Then it asks the writer in the run log whether the line should move, and names the note it would fit. `%% Agent, tag this provisional. %%` under a Brain Dump line gets the tag and a question. It gets no copy in an Idea Note.
- **In an Idea Note, a comment that asks only for a tag works as a typed tag does.** `%% Agent, tag this committed. %%` there gets the tag, and the line graduates to its Area Note (migrator-rules.md 10.4).
- **A tag the writer typed still triggers migration** (migrator-rules.md 10.4).
- **A comment that asks for a tag and a move gets both.** The migrator adds the tag and migrates the line.
- **This narrows 08.1 and 10.4, in the Brain Dump doc only.** There, the comment sets the same status a typed tag would (migrator-rules.md 08.1). It just doesn't move the line. The writer's words in migrator-rules.md 10.4, "#status/provisional in the brain dump is the instruction for the agent to migrate idea units into their own Idea Note," hold for a tag the writer typed. They don't hold for a tag the migrator adds because a comment asked for it.
- **The writer on why:** "It's one of those things where, in the middle of composition, I might have marked an idea to explore, but didn't pause to create a dedicated area note for it, or even pause to consider if it needs such a note. More often than not, it'll be in the form of a question work item that should sit there, to be picked up by dataview."

### 09 Questions and Attribution

#### 09.1 Questions

The writer uses `- [?]` for unresolved, actionable questions:

```markdown
### September 1

- Maybe memories can be bought and sold.
- [?] Does selling a memory remove it from the seller or just create a copy?
- Rich people collecting other people's childhood memories feels promising.
```

- **Do not duplicate that meaning** with a new `#status/unresolved` tag, a `[question]` marker, or a parallel question property.
- **The question may still contribute development context to an Idea Note or Area Note,** but it is not a tentative assertion that either mechanic is true.
- **The writer types `- [?]`. The migrator doesn't turn prose questions into Questions.** When the writer asks a question inside a bullet and doesn't mark it, the question stays inside the unit's words and migrates with its unit. It isn't tracked as Work. This holds in every note, the Brain Dump doc included. The prose questions in the ball of yarn ("Does the person know Lena?") stay inside their Idea Units, in the writer's words, and migrate with them (migrator-rules.md 05.2).
- **A writer's comment can still ask the migrator to convert questions.** Then the migrator moves the question, and any sentence that belongs to it ("Maybe almost none of it."), out of the bullet into a nested `- [?]` line directly under it. They move verbatim and are cut from the bullet. The Question is still the writer's.
- **A Question moves with its Idea Unit.** When an Idea Unit is migrated, its Questions go with it. One Question, one checkbox, in the note where the unit now lives.
- **The Run manager, not the migrator, removes the `[?]` from the source line.** The source line loses its `[?]` and becomes an ordinary bullet, with a `migrated-to` pointer to the note the unit went to. The Run manager removes the `[?]` at the moment it writes the `migrated-to` pointer on that line, after the migration-verifier approves the copy. This holds at every hop, Idea Note lines included.
- **In an Area Note, a Question sits nested under the line it belongs to,** so it reads correctly on its own (migrator-rules.md 02.3).

#### 09.2 Work lines

- **Work lines and Questions are not rewritten.**
- **The writer types Work as a task line with its Work Type's checkbox character.** The migrator doesn't infer Work task lines from prose.

#### 09.3 Attribution

- **Attribution covers only new material.** When the migrator migrates or rewrites material that belongs to the writer, that material keeps its original owner and carries no label.
- **`[AGENT]` opens the agent's text.** It does not wrap the text in brackets:

```markdown
- [AGENT] Heavy sellers may develop a recognizable social stigma.
```

- **A note the agent adds to the writer's line starts with the label too.**

### 10 What the migrator Never Does

#### 10.1 Who writes what

- **The migrator writes migrated copies and Rejected sections.**
- **The Run manager alone writes `migrated-to` pointers, block IDs, the run log, and the run state.** It also removes a migrated Question's `[?]` from its source line.
- **The migration-verifier writes nothing in the notes.** Its findings never set a status above what the writer's own tag, comment, or request gave.
- **`migrated-to` is written by the Run manager at the source of every migrated Idea Unit, after the migration-verifier approves the copy.** The migrator never writes it.
- **Migrated lines carry no link back to their source.**
- **The migrator gives its reason for where each Idea Unit went.** It goes in the run log, not in the notes.

#### 10.2 Nothing in the Brain Dump doc

- **The migrator writes nothing in the Brain Dump doc, unless a writer's comment asks it to** (migrator-rules.md 08.6).
- **The writer's words there are untouched.** Block IDs and `migrated-to` pointers there are the Run manager's.
- **Without such a comment, the migrator never writes status tags in the Brain Dump doc.** It reads the writer's tags there and acts on them.

#### 10.3 No Gaps, dependencies, or contradictions

- **It doesn't look for Gaps.** The writer: "The Intake run shouldn't be checking for gaps, since a gap requires context."
- **It doesn't look for dependencies.** The writer: "At the very least, spotting dependencies asks too much of it."
- **It doesn't flag contradictions, whether tentative or committed.** Two incompatible tentative ideas are alternatives under exploration. The incorrect read in migrator-rules.md 06.4 shows the false concern to avoid.
- **It only pays attention to the construction of the words as far as migrating needs.** See migrator-rules.md 06.4.

#### 10.4 Only tags and comments trigger migration

- **The writer triggers migration with a status tag or with a comment.** The writer: "#status/provisional in the brain dump is the instruction for the agent to migrate idea units into their own Idea Note. #status/committed in an Idea Note is the instruction for the agent to commit -- or 'migrate' -- the idea into an Area Note." In the Brain Dump doc, that holds for a tag the writer typed. There, a comment that asks only for a tag doesn't trigger migration, and neither does the tag the migrator adds for it (migrator-rules.md 08.8). In an Idea Note, a comment that asks only for a tag triggers migration as a typed tag does.
- **Plain prose doesn't trigger migration.** Only the writer's status tags and comments do. The writer: "Status tags and comments mentioning to migrate means bullets migrate." And: "Empty bullets with no tag means they don't migrate."
- **The writer tags each line, or writes a comment that says which bullets migrate.** The writer will "either tag every line or ensure that the comments scope the bullets that should migrate, with something from "migrate all the bullets between "- {first few words of first bullet}" to "{first few words of last bullet}""."
- **The untagged September 9 bullet is enough to pull out its ideas and their meaning.** It isn't enough to set their status, which needs the writer's tag or comment. Reading the writer's words recovers each idea. It doesn't recover status.

#### 10.5 Where the migrator sits in a migration run

- **The writer starts every run.**
- **A migration run works on whatever changed since the last successful migration run.** The Run manager finds the changes by scanning the notes for trigger lines (a line with a status tag or a writer's comment) that aren't on the run state's handled list. So a tag or comment added to an old line still counts.
- **A migration run goes in this order:** the migrator, the migration-verifier, the Run manager writing pointers for approved copies, then the Edit guard.
- **The writer doesn't edit notes during a run.**
