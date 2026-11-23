# Rename Test on Almond, Milestone 17 Scan, 2026-10-25

The rename test of `2026-10-23-rename-test-almond.md`, rerun with the changed scan in `lib/runmanager/migration/scan.py` (spec-run-manager.md 11 items 102 to 104; `CONTRACT.md` 5.2 items 6, 8, 14 to 16). No model ran. The vault's Almond was not changed.

## Method

The method of 2026-10-23, unchanged:

1. Copied `Projects/Almond/` from the vault into the session scratchpad three times (`before/Almond`, `after/Almond`, `moved/Almond`).
2. **before:** left as it is, after the one migration run, `run-2026-10-16-0931-migration`.
3. **after:** renamed `Ideas/idea-almond.md` to `Ideas/idea-almond-renamed.md`, and rewrote every link to it outside `.runs/`: `Ideas/idea-almond|` and `Ideas/idea-almond]]` to the new name. Two files changed: `brain-dump.md` and `Runs/run-2026-10-16-0931-migration.md`.
4. **Almond2:** the folder renamed to `Almond2`, with every `Projects/Almond/` link prefix rewritten to `Projects/Almond2/` outside `.runs/`. Six files changed: `brain-dump.md`, `Research/research-light-anxiety-spread.md`, and four run logs in `Runs/`.
5. Ran the real `scan()` on each copy with the `handled` list from its `.runs/run-state.json` (57 entries in all three copies). `scan()` now returns three values, the batches data, the story note texts, and the carried-over matches `close` brings up to date.

As on 2026-10-23, Obsidian's own rewrite of a link may differ in form from step 3. The scan reads only the file name inside the link, so the result holds for a real rename.

## Results

| Copy | New lines, 2026-10-23 | New lines, now | Skipped, 2026-10-23 | Skipped, now | Renames found | Handled lines carried over to a new note |
| --- | --- | --- | --- | --- | --- | --- |
| before (unchanged) | 0 | 0 | 0 | 0 | none | 0 |
| after (note renamed) | 10 | 0 | 0 | 0 | 1 | 5 |
| Almond2 (folder moved) | 9 | 0 | 5 | 0 | none | 0 |

Lines handed back as new work: none, in any copy. Batches: 0 in all three.

- **after:** one rename, `{"from": "Ideas/idea-almond.md", "to": "Ideas/idea-almond-renamed.md"}`. The 5 lines carried over from the old note are lines 12, 13, 17, 25, and 29 of `Ideas/idea-almond-renamed.md`. `carried.json` (what `close` reads) holds 10 matches: those 5, and 5 more whose entry already names `brain-dump.md` and whose text only changed because the pointer's link target changed (`brain-dump.md` lines 61, 94, 105, 144, and 147). Those 5 move no note, so the run log's "Its {N} handled lines carried over" counts 5.
- **Almond2:** no rename. `carried.json` holds 14 matches, all `brain-dump.md` lines whose text changed only in the link prefix (lines 42, 60, 61, 94, 98, 105, 106, 107, 132, 138, 144, 147, 154, 156). Each keeps its entry and the scan skips nothing.

## One more check

`runmanager start --kind migration` on a fresh copy of the renamed project (with `RUNMANAGER_NOW="2026-10-25 10:00"`) exits 1 with "No new work since the last migration run." and makes no run.

## Commands

The scan, run on each copy by `scratchpad/m17/runscan.py <copy path>`:

```python
import sys, json
sys.path.insert(0, "/Users/mabbs/.claude/plugins/local/script-asst/lib")
from runmanager.migration import scan as sc
p = sys.argv[1]
handled = json.load(open(p + "/.runs/run-state.json"))["handled"]
out, _, carried = sc.scan(p, handled)
```

The copies and the link rewrite (`scratchpad/m17/rewrite.py <copy> note|folder`, which rewrites `.md` files outside `.runs/`):

```
cp -R Projects/Almond before/Almond; cp -R Projects/Almond after/Almond; cp -R Projects/Almond moved/Almond
mv after/Almond/Ideas/idea-almond.md after/Almond/Ideas/idea-almond-renamed.md
mv moved/Almond moved/Almond2
python3 rewrite.py after/Almond note
python3 rewrite.py moved/Almond2 folder
python3 -I runscan.py {before/Almond, after/Almond, moved/Almond2}
RUNMANAGER_NOW="2026-10-25 10:00" bin/runmanager start --project startcheck/Almond --kind migration
```
