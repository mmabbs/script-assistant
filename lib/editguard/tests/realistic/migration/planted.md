# Planted mistakes: migration run

Run id `run-2026-10-10-1530-migration`. Two batches, seven units. The notes under `Lighthouse/` are the project after the Run manager wrote its pointers. Four things in them are wrong, listed below. Everything else is built to match its record. Rule names are the ones in spec-edit-guard.md 04.

## The four planted mistakes

1. **A copy whose words differ from its record.** Note `Ideas/idea-relief-keeper.md`, under `# Idea - Relief Keeper`, the line
   `- The relief keeper could be someone from the mainland who has never seen the sea and is frightened of the water.`
   Record `runs/units/run-2026-10-10-1530-migration-b1.json`, unit `b1-u4`, `copies` line says `...and is scared of the water.` Expected: `copy-mismatch` on `Ideas/idea-relief-keeper.md` (before empty, after the record's text, unit `b1-u4`), spec-edit-guard.md 03.3 item 1 and 05 item 4. The written line matches no record entry, so by the reading in fixture `30-copy-mismatch` it is also an `unexplained-change` with no unit.

2. **An unrecorded change to a writer's line in an Area Note.** Note `Areas/area-mara.md`, under `# Mara`. The snapshot line
   `- Mara is scared of deep water, though she has lived beside it all her life.`
   now reads
   `- Mara is afraid of deep water, though she has lived beside it all her life.`
   No `edits` entry in either record file covers it. Expected: `unexplained-change` on `Areas/area-mara.md`, before and after as above, unit empty (spec-edit-guard.md 03.2, last sentence; 04 table).

3. **A pointer missing one of its destinations.** Note `brain-dump.md`, heading `### 2026-10-03`. The source line of `b1-u2`
   `- The causeway floods twice a month, and Mara times her supply runs around the tide table. #status/provisional`
   carries a pointer to `idea-harrow-point` only. The unit copied to both `Ideas/idea-harrow-point.md` and `Ideas/idea-mara-lighthouse.md`, so `idea-mara-lighthouse` is missing. `run-state.json` holds the line as written, with the short pointer. Expected: `pointer-mismatch` on `brain-dump.md`, before the snapshot line, after the line with its short pointer, unit `b1-u2` (spec-edit-guard.md 03.3 item 2; 04 table).

4. **A status tag added in the Brain Dump doc.** Note `brain-dump.md`, heading `### 2026-10-08`. The line
   `- Mara has never once left the light during a storm.`
   now ends with ` #status/provisional`. Unit `b2-u2` is an `edit` unit that records exactly this change, and the writer's comment under the line says "Agent, tag this provisional." Expected: `brain-dump-status-tag` on `brain-dump.md`, unit `b2-u2` (spec-edit-guard.md 04 item 2: always flagged, even when a comment asked). By spec-edit-guard.md 04 item 7 and fixture `37-brain-dump-status-tag`, the same change also carries `writer-line-edited`, so two flags with the same before, after, and unit.

Expected total: 6 flags if the fixture readings hold: `copy-mismatch`, `unexplained-change` (the copy line), `unexplained-change` (the Area Note line), `pointer-mismatch`, `brain-dump-status-tag`, and `writer-line-edited`.

## What else the checker might flag, and why

1. **Nothing else should flag.** If anything does, check these first.
2. **Earlier run's pointers.** The Brain Dump headings 2026-09-12, 2026-09-19 and 2026-09-26 carry pointers from `run-2026-10-02-2015-migration` that are identical in the snapshot. They are unchanged (spec-edit-guard.md 03.1 item 5).
3. **Old-run entries in `unit_index`.** `run-state.json` has five `pointer-written` entries for the earlier run, and no record file for that run is passed. A checker that looks up a record for every entry could fail or flag here. By spec-edit-guard.md 03.2 item 5 it should key on run and unit and ignore them.
4. **Unit `b1-u3` removes a `[?]`.** The pointer on `    - [?] Who teaches him, Mara or the logbook?` removes the `[?]`, and the copy keeps it. Both are correct (spec-run-manager.md 08.2 item 4).
5. **Unit `b2-u3` is a rejection** in `Ideas/idea-mara-lighthouse.md`. The dog line moves to `## Rejected` with `#status/rejected`, and the reason is a comment on the line below. The writer's instruction comment stays where it was. `rejected-move-changed` should not fire.
6. **A writer-typed tag in an Area Note.** `Areas/area-mara.md` has `- Mara is wary of the mainland doctor. #status/provisional`, unchanged. `area-note-status-tag` covers only lines the run added or changed (spec-edit-guard.md 04 item 3). The graduated copy `b2-u1` dropped its `#status/committed` tag.
7. **A question left in the Brain Dump.** The line about the ferry horn and the fog signal, with its "Agent, put this somewhere sensible." comment, has a `questions` entry in the `b2` record and no unit. It is unchanged and has no pointer.
8. **`Runs/` and `llm-files/`.** Both hold `.md` files that are in neither the snapshot nor the fingerprints file. spec-run-manager.md 04 item 9 says neither folder is ever covered, but spec-edit-guard.md 03.1 item 8 does not say the Edit guard skips them. Fixture `29-copies-two-batches-pass` shows `Runs/` skipped. If `llm-files/migrator-working-2026-10-02.md` is flagged, that is a gap between the two specs, not a planted mistake.
9. **The `b1-u2` heading.** The copy opens with a new heading, `## The causeway`, listed first in its `lines` (spec-migrator.md 05.5 item 6).
10. **Fingerprints.** `Plot/plot-outline.md` and the two `Research/` notes are fingerprinted and unchanged.
