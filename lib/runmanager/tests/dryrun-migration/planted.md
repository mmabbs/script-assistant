# Planted mistakes: Run manager migration dry run

Built by `build.py` from `source/`. The project is the Edit guard's realistic migration case (`lib/editguard/tests/realistic/migration/`) set back to before its run: the story notes are its `snapshot/`, every other note is its `Lighthouse/`. The session follows `steps.md`, copying `prepared/` files in place of the migrator and the migration-verifier.

Updated 2026-10-13 for spec-run-manager.md 11 items 81 and 83 (CONTRACT.md 5.3 item 1; 5.6 items 3 and 6): `record` now refuses a copy missing from its note, the log asks the writer only its questions, and the handled list keeps a piece's comments off when the piece holds an undone unit or a missed line.

## The project before the run

1. **The run state** (`source/Lighthouse/.runs/run-state.json`) has no open run, one history entry for `run-2026-10-02-2015-migration`, that run's 5 unit index entries, and 30 handled entries.
2. **The handled list keeps the realistic case's 6 entries** (the earlier run's pointer lines), with `pointer` added in the shape of spec-run-manager.md 04 item 20.
3. **24 handled entries are added for the earlier run, so the scan finds only the intended work.** Without them, every Rejected line, its reason comment, the writer-tagged lines in the Idea and Area Notes, and the earlier run's four `%% Agent, … %%` comments are new work. The added entries are `left in place` for tagged lines, `comment` for comments, and `written` for the harbour line the earlier run copied into `Ideas/idea-harrow-point.md`.
4. **The realistic `run-state.json` was in an older shape** (`open_run` with `run`, history with `finished`). The current `runmanager` refuses that shape, so the history entry is rewritten to spec-run-manager.md 04 item 17's fields.
5. **`brain-dump.md` holds `%% Agent, area-mara. %%` twice**, under 2026-09-26 and 2026-10-08. The handled list holds it once, so the older one is handled and the 2026-10-08 one is new work (CONTRACT.md 5.2 item 6).

## What `start` finds

Two batches (`batches: 2`), no skipped lines.

| Batch | Piece | Size | New trigger lines |
| --- | --- | --- | --- |
| b1 | `brain-dump.md` `### 2026-10-03` | 7 | 37, 39, 40, 46, 50 |
| b1 | `brain-dump.md` `### 2026-10-08` | 4 | 54, 55, 58, 61 |
| b2 | `Ideas/idea-mara-lighthouse.md` | 11 | 13 (the dog comment) |

b1 is 11 bullets; adding the Idea Note's 11 would make 22, over 20, so it starts b2.

## The units

| Unit | Action | Source | Where it ends |
| --- | --- | --- | --- |
| b1-u1 | migrate | brain-dump 37, sea glass | undone, round 2 (plant 5) |
| b1-u2 | migrate | brain-dump 39, causeway split | pointer written |
| b1-u3 | migrate | brain-dump 48 and 49, merge | pointer written, after plant 1's retry |
| b1-u4 | migrate | brain-dump 54, logbook | pointer written |
| b1-u5 | edit | brain-dump 57, storm line | approved (plant 3) |
| b2-u1 | reject | idea-mara-lighthouse 12, dog | approved |

The b1 record also holds one question (plant 4). The b1 round-0 findings hold one `missed` line (plant 6).

## The plants

1. **A copy whose words differ from its record, caught at `record`.** `prepared/b1-r0/notes/Ideas/idea-relief-keeper.md` holds `- The relief keeper could be someone from the mainland who has never seen the sea and is frightened of the water.`; unit u3's copy in `prepared/b1-r0/record.json` says `…is scared of the water.` `record` exits 1 with: "The record file P/.runs/units/{run-id}-b1.json was refused: unit u3's copy `…scared of the water.` isn't in Ideas/idea-relief-keeper.md as a line the run wrote." Nothing changes. The skill retries the migrator; `prepared/b1-r0-retry/` stands in for it, rewriting the note's line to the record's words (its record is the same as `b1-r0`'s). `record` then passes, u3 is approved and gets its pointer.
   - Log: **nothing.** The slip is fixed inside the run (spec-run-manager.md 11 item 81). No flag names it, and u3 is listed under Migrated as ordinary work.
2. **An unrecorded change to a writer's line in an Area Note.** `prepared/b1-r0/notes/Areas/area-mara.md` changes `- Mara is scared of deep water, though she has lived beside it all her life.` to `…afraid of deep water…`. No record covers it, and the retry leaves it. Flag `f1` `unexplained-change`, no unit; the flag findings judge it `not-asked`; `act` at `judged` puts it back.
   - Log, `## Changes put back`: "In [[…area-mara|area-mara]], a changed line was put back. It read `…afraid…`, and reads `…scared…` again."
3. **A status tag added in the Brain Dump doc by an `edit` unit, which a comment asked for.** Unit b1-u5 changes `- Mara has never once left the light during a storm.` to end with ` #status/provisional`; the comment under it, line 58, is `%% Agent, tag this provisional. %%`. Flags `f2` `writer-line-edited` and `f3` `brain-dump-status-tag`, both unit b1-u5. b1-u5 is approved and that comment started it, so both flags skip the flags call and the change stands (spec-migration-verifier.md 06 item 7). The second check drops both.
   - Log, `## Other edits you asked for`: "In [[…brain-dump|brain-dump]], `- Mara has never once left the light during a storm.` now reads `- Mara has never once left the light during a storm. #status/provisional`, as your comment `%% Agent, tag this provisional. %%` in [[…brain-dump|brain-dump]] asked."
4. **A migrator question about a line.** The b1 record's `questions` entry: source line 60, `- The ferry horn and the fog signal sit a half-step apart, so on foggy mornings nobody can tell which is which.`, ask "Which note should the horn and fog signal line go in: idea-fog-signal or idea-harrow-point?"
   - Log, `## Questions for you`: the line quoted with its note link, the ask, then "Answer with a comment on the source line, then start another migration run." Because there is a question, the log has no "Nothing needs you."
5. **A unit fixed on rounds 0, 1, and 2, then undone.** b1-u1, sea glass, to `Ideas/idea-tobias.md`. Each round the migrator rewrites its copy and the record (`prepared/b1-r{0,1,2}/`); every other unit stays as it was.
   - Round 0: `- Tobias kept sea glass under his bed.`, tentative. Findings: `status` (no tag, though the writer tagged it provisional) and `lost-detail` (the tin is gone).
   - Round 1: `- Tobias kept sea glass in a tin. #status/provisional`. Findings: `lost-detail` (where the tin was is gone).
   - Round 2: `- Tobias kept a tin of sea glass, maybe under his bed. #status/provisional`. Findings: `lost-detail` (an added "maybe"). `findings` undoes the unit; `Ideas/idea-tobias.md` is back to its run-start text.
   - Log, `## Units undone`: `- Tobias kept a tin of sea glass under his bed. #status/provisional`, "Its copies went to [[…idea-tobias|idea-tobias]].", "It was undone because the migration-verifier still found problems after 2 fix rounds:", nested "lost-detail: The copy adds a "maybe" your line doesn't have. You wrote that the tin was under his bed, as a fact.", then "The next migration run tries this again." Only round 2's problem appears.
6. **A `missed` line in a batch's round-0 findings.** `prepared/b1-r0/findings.json`: source line 44, `- The relief keeper has never worked a hand-wound lamp.`, what "Your comment asks to move this line and the question under it to idea-relief-keeper. Nothing moved them." The migrator made no unit for that comment (`%% Agent, idea-relief-keeper. %%`, line 46).
   - Log, `## Lines the checker says were missed`: the line quoted, the what, then "The next migration run tries this again."

## The flags

First check (`flags-1.json`), as the real Edit guard writes them after `pointers`:

| Id | Rule | Note | Unit | Plant | Flag findings |
| --- | --- | --- | --- | --- | --- |
| f1 | `unexplained-change` | `Areas/area-mara.md` | none | 2 | `not-asked` |
| f2 | `writer-line-edited` | `brain-dump.md` | b1-u5 | 3 | stands; not handed to the call |
| f3 | `brain-dump-status-tag` | `brain-dump.md` | b1-u5 | 3 | stands; not handed to the call |

No `copy-mismatch` and no flag on the relief-keeper copy: the retry made record and note agree. Second check (`flags-2.json`): `[]`.

## The whole log, in order

File `Runs/{run-id}.md`. First line "Migration run, started {start time}." No request line. No "Nothing needs you." (there is a question). Sections, in order:

1. `## Questions for you`: plant 4.
2. `## Migrated`: b1-u2 (causeway), b1-u3 (the relief-keeper merge), b1-u4 (logbook). Not plants.
3. `## Rejected`: b2-u1 (the dog). Not a plant.
4. `## Other edits you asked for`: plant 3.
5. `## Units undone`: b1-u1 only (plant 5).
6. `## Lines the checker says were missed`: plant 6.
7. `## Changes put back`: `area-mara` only (plant 2).

## The handled list at close

14 new entries for this run. The `### 2026-10-03` piece holds an undone unit's source (line 37, b1-u1) and a missed line (line 44), so all three of its comments stay off: lines 40, 46, and 50. Lines 37 and 44 stay off too. The next migration run finds one batch: that piece, with lines 37, 40, 46, and 50. Its migrated lines (39, 48, 49) go on as `migrated`; their pointers keep the retried piece from copying them again (spec-run-manager.md 11 item 81, third bullet).

The `### 2026-10-08` piece and `Ideas/idea-mara-lighthouse.md` have no undone unit and no missed line, so their comments go on as `comment`: lines 55, 58, 61, and the dog comment.

## What must NOT appear

1. Anything about plant 1: no Units undone entry for b1-u3, no Changes put back entry for `idea-relief-keeper`, no undo miss.
2. `## Other notes`, `## Left in place, and why`, and `## Could not do`: all empty, so left out.
3. Any "still flagged after the second check" line: the second check is empty.
4. Any `fingerprint-changed` line: `Plot/` and `Research/` are untouched; `Runs/` and `llm-files/` are never covered.
5. "Answer with a comment on the source line…" anywhere but under Questions for you.
