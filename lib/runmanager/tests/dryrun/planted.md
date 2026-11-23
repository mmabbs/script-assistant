# Planted mistakes: Run manager dry run

Built by `build.py` from `source/`. The project is the Edit guard's realistic research case (`lib/editguard/tests/realistic/research/`) set back to before its run. The session runs `init`, `start --kind research --run-number 2`, copies `prepared/Lighthouse/` over the project, copies `prepared/outcomes.json` to `.runs/{run_id}/outcomes.json`, then `mark`, the Edit guard check, `act`, a second check, and `close`.

Request ids from `start` (path, then line):

| id | Note | Line | Outcome in `prepared/outcomes.json` |
| --- | --- | --- | --- |
| r1 | `Areas/area-mara.md` | 26 | failed, note written: `Research/research-light-keeper-refusal.md` |
| r2 | `Ideas/idea-harrow-point.md` | 29 | passed: `Research/research-light-tide-tables.md` |
| r3 | `brain-dump.md` | 66 | passed: `Research/research-light-relief-keeper-contracts.md` |

## The plants

1. **A changed line in a request note.** `Ideas/idea-harrow-point.md`, line 24, under `## Winters`. "It is the warmest room in the village." becomes "It is the warmest room in the whole village." The prepared note is the whole pre-run file with that one line changed. It is not a request line and not a comment. The Edit guard flags `unexplained-change`; `act` puts the line back.
   - Run log: `## Notes changed outside the run`, one entry naming `idea-harrow-point`, with the changed text quoted and the original shown.
2. **A stray new note in `Ideas/`.** `Ideas/idea-keeper-refusal.md` (the whole note is new, so there is no line). It is in neither the snapshot nor the fingerprints, and it is not in `Research/`. The Edit guard flags `fingerprint-changed`; `act` edits nothing, and the note stays in the project.
   - Run log: `## Notes changed outside the run`, one entry naming `idea-keeper-refusal`.
3. **A failed request whose note was written.** r1, `Areas/area-mara.md` line 26: `- [r] Could a lone keeper legally refuse a relief posting? #research/run-2`. The outcome is `failed` with `Research/research-light-keeper-refusal.md` named (spec 06 item 5). The request stays `- [r]`. The note sits in `Research/`, and the outcomes file names it, so the Edit guard does not flag it.
   - Run log: `## Requests still open`, one entry quoting the request with its note link `area-mara`, the reason "No source covered whether a lone keeper could refuse a posting.", and the failed note `research-light-keeper-refusal`.
4. **One request that passes cleanly.** r3, `brain-dump.md` line 66: `- [r] What did a relief keeper's contract look like in the 1950s? #research/run-2`, with the comment `%% Canadian lights if you can find them. %%` under it. `mark` closes it and writes the link line right under the request, above the comment. Nothing is flagged on it.
   - Run log: `## Done`, one entry for r3 pointing to `research-light-relief-keeper-contracts`.

r2 also passes, and its note holds plant 1. It is not a plant of its own, but its Done entry is expected too.

## The whole log, in order

First line: "Research run 2, started 2026-10-12 12:00." (with `RUNMANAGER_NOW="2026-10-12 12:00"`). Sections, in order:

1. `## Requests still open`: r1 only (plant 3).
2. `## Notes changed outside the run`: `idea-keeper-refusal` (plant 2) and `idea-harrow-point` with its line put back (plant 1).
3. `## Done`: r2 (tide tables) and r3 (relief keeper contracts, plant 4).

## What must NOT appear

1. **`## Closes undone`:** none of the plants breaks a close. The prepared notes hold no link line, so `mark` writes every link line itself. If this section appears, a link line or request line went wrong.
2. **`## Still flagged after the second check`:** the second check repeats `fingerprint-changed` on `Ideas/idea-keeper-refusal.md`, but CONTRACT.md section 4 item 13 drops it, because the first check already named that note. If this section appears, that rule broke.
3. **"Nothing needs you."** The first three sections are not empty.
4. **No entry for `Research/research-light-keeper-refusal.md` under Notes changed outside the run,** and none for the two passed notes. The outcomes file names them, so they are expected.
5. **No entry for `llm-files/`.** The pre-run project holds `llm-files/migrator-working-2026-10-02.md` only; this run's findings files are left out (the workflow's own output, not part of this return).
6. **No `Requests still open` entry for r2 or r3**, and no mention of the `#research/run-3` request in `Ideas/idea-fog-signal.md` or the `#research/run-1` requests, which are not part of the run.

## Not planted, and why

1. **The realistic case's link line below a comment** (its `planted.md` item 1) is not planted. The brief asked for the four plants above, and `mark` writes link lines, so a prepared note cannot carry that mistake without editing the request lines.
2. **The realistic case's `area-mara.md` word change** is not planted. Plant 1 is a different line in a different note (`idea-harrow-point.md`), chosen so that exactly one passed request is clean and exactly one note holds a stray change. `area-mara.md` is the pre-run file, unchanged.
