# Rename Fix Prototype on Almond, 2026-10-24

A prototype of `spec-run-manager.md` 11 items 102 and 104, run before the spec amendment was written. No model ran, and the vault's Almond was not changed. It follows the method of `2026-10-23-rename-test-almond.md`: three scratchpad copies of `Projects/Almond/` (unchanged, `Ideas/idea-almond.md` renamed to `Ideas/idea-almond-renamed.md`, and the project folder renamed to `Almond2`), with links rewritten outside `.runs/` as Obsidian does.

## What the prototype did

1. Ran the real `scan()` with an empty handled list, to get every trigger line.
2. Matched each story note's trigger lines against the handled entries that name that story note, with every wikilink's contents left out of both texts (`[[…]]` read as `[[]]`), counting repeats.
3. Matched the lines still unmatched against the handled entries whose story note no longer exists, the same way.

Script: `proto.py` in that session's scratchpad (not kept). It left comments' link targets out too. The spec's item 103 instead reads a comment's link targets through the renames the scan found, which this prototype didn't build.

## Results

| Copy | New lines, current scan | New lines, prototype | Carried over from a story note that no longer exists |
| --- | --- | --- | --- |
| unchanged | 0 | 0 | 0 |
| idea-almond.md renamed | 10 | 0 | 5 |
| folder moved to Almond2 | 9 (5 skipped) | 0 | 0 |

The 5 carried over are the tagged copies inside the renamed Idea Note.
