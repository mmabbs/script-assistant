# Planted mistakes: research run

Run id `run-2026-10-10-1600-research`, run number 2. Three requests tagged `#research/run-2`: `r1` in `brain-dump.md` and `r2` in `Ideas/idea-harrow-point.md` passed, `r3` in `Areas/area-mara.md` failed and stays `- [r]`. The notes under `Lighthouse/` are the project after `runmanager mark`. Three things in them are wrong, listed below. Everything else is built correctly. Rule names are the ones in spec-edit-guard.md 04.

## The three planted mistakes

1. **A link line placed below the request's comment.** Note `Ideas/idea-harrow-point.md`, under `## Questions`. The request `r2` now reads, in order:
   `- [x] How did printed tide tables reach small villages in the 1950s? #research/run-2`
   `%% Look for printed almanacs. %%`
   `    - [AGENT] [[Projects/Lighthouse/Research/research-light-tide-tables|research-light-tide-tables]]`
   The link line is in the settled form and points to the note the outcomes file names, but it must sit on the line right under the request, above the comment (spec-run-manager.md 08.4 item 1; spec-edit-guard.md 04 item 6). Expected: `link-line-invalid` on `Ideas/idea-harrow-point.md` (before empty, after the link line, unit empty). By fixture `18-link-line-below-comment`, the close then has no valid link line under it, so `close-invalid` also fires (before `- [r] How did printed tide tables reach small villages in the 1950s? #research/run-2`, after the `- [x]` version, unit empty).

2. **A stray note written into `Ideas/`.** New note `Ideas/idea-keeper-refusal.md`, written by whatever worked on the failed request `r3`. It is not in the fingerprints file, not in the snapshot, and not in `Research/`. Expected: `fingerprint-changed` on `Ideas/idea-keeper-refusal.md`, with before, after, and unit empty (spec-edit-guard.md 04 table: on a research run, a new note outside `Research/`; 05 item 5; fixture `27-research-fingerprints-changed`). Its lines should not also raise `unexplained-change`, since a new note on a research run is judged by the research rules (03.1 item 8).

3. **A word changed in a request note outside the request line.** Note `Areas/area-mara.md`, under `# Mara`. The snapshot line
   `- Mara has not left the headland for a night in eleven years.`
   now reads
   `- Mara has not left the headland overnight in eleven years.`
   Expected: `unexplained-change` on `Areas/area-mara.md`, before and after as above, unit empty (spec-edit-guard.md 11 Decisions Log item 11; fixture `28-request-note-other-change`). No link-line or close rule fires on it.

Expected total: 4 flags: `link-line-invalid`, `close-invalid`, `fingerprint-changed`, `unexplained-change`.

## What else the checker might flag, and why

1. **Nothing else should flag.** If anything does, check these first.
2. **`r1` is correct.** In `brain-dump.md` under `### 2026-10-10`, the link line sits right under the closed request and above its comment. It must pass, and so must the close.
3. **`r3` stays open.** `- [r] Could a lone keeper legally refuse a relief posting? #research/run-2` in `Areas/area-mara.md` is unchanged. A failed request is not a change.
4. **An earlier run's closed request.** `Ideas/idea-harrow-point.md` holds `- [x] How did the ferry to Harrow Point run in the 1950s? #research/run-1`, its link line, and its comment, all identical in the snapshot. Unchanged lines are not stripped or flagged (spec-edit-guard.md 03.1 item 5).
5. **An open request for another run.** `Ideas/idea-fog-signal.md` holds `- [r] ... #research/run-3`. That note is fingerprinted and unchanged.
6. **The two new research notes.** `Research/research-light-relief-keeper-contracts.md` and `Research/research-light-tide-tables.md` are named in `outcomes.json`, so `unexpected-research-note` should not fire. Their link lines point to them, so the targets exist.
7. **`Runs/` and `llm-files/`.** Both hold `.md` files that are in neither the snapshot nor the fingerprints file, and `llm-files/research/run-2026-10-10-1600-research/` holds this run's three findings files. spec-run-manager.md 04 item 9 says neither folder is ever covered, but spec-edit-guard.md 03.1 item 8 does not say the Edit guard skips them. Fixture `29-copies-two-batches-pass` shows `Runs/` skipped. If anything in `llm-files/` is flagged, that is a gap between the two specs, not a planted mistake.
8. **Migration pointers in the notes.** The Brain Dump and Idea Notes carry pointers and copies from earlier migration runs. They are identical in the snapshot or the fingerprints, so nothing about them should flag.
