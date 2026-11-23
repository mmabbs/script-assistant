# Rename Test on Almond, 2026-10-23

The test the writer ruled for audit ruling 03.12 (`audit-decisions-prewriting.md` 03.12 and 13): rename `idea-almond.md` and see which lines a migration run hands back as new work. No model ran. What a run hands the Migrator is decided by the Run manager's scan, `lib/runmanager/migration/scan.py` `scan()`, which only reads, so the test called it directly.

## Method

1. Copied `Projects/Almond/` from the vault into the session scratchpad three times. The vault's Almond was not changed.
2. **before:** left as it is, after the one migration run, `run-2026-10-16-0931-migration`.
3. **after:** renamed `Ideas/idea-almond.md` to `Ideas/idea-almond-renamed.md`, and rewrote every link to it outside `.runs/`, as Obsidian does on a rename: `Ideas/idea-almond|` and `Ideas/idea-almond]]` to the new name. Two files changed: `brain-dump.md` and `Runs/run-2026-10-16-0931-migration.md`.
4. **Almond2:** the whole project folder moved: renamed to `Almond2`, with every `Projects/Almond/` link prefix rewritten to `Projects/Almond2/` outside `.runs/`.
5. Ran `scan()` on each copy with the `handled` list from its `.runs/run-state.json`.

Obsidian's own rewrite of a link may differ from step 3 in form. It can't differ in the file name inside the link, which is all the scan reads, so the result holds for a real rename.

```python
import sys, json
sys.path.insert(0, "/Users/mabbs/.claude/plugins/local/script-asst/lib")
from runmanager.migration import scan as sc
p = sys.argv[1]
handled = json.load(open(p + "/.runs/run-state.json"))["handled"]
out, _ = sc.scan(p, handled)
```

## Results

| Copy | Batches | New lines | Skipped |
| --- | --- | --- | --- |
| before | 0 | 0 | 0 |
| after (note renamed) | 1 | 10 | 0 |
| Almond2 (folder moved) | 1 | 9 | 5 |

### Note renamed: 10 lines come back

1. **5 Brain Dump lines whose pointer names the renamed note:** lines 61, 94, 105, 144, and 147 of `brain-dump.md`. Their text no longer matches their handled entry, since the pointer changed. The pointer match in `CONTRACT.md` 5.2 item 8 then looks for an entry with the same destinations, and the destination is new, so none fits.
2. **5 tagged copies inside the renamed note:** lines 12, 13, 17, 25, and 29 of `Ideas/idea-almond-renamed.md`. Each handled entry for them is stored under the note `Ideas/idea-almond.md`, a path that no longer exists, so the copies look like new trigger lines. The audit didn't predict this.

### Folder moved: 9 of 14 tagged pointer lines come back

The audit's 03.12 said a folder move only changes the link prefix, so those lines would be skipped. The scan drops the prefix, so destinations do still match. But item 8 accepts a match only when exactly one handled entry has the same note and destinations and its text is gone from the note. After a move, every pointer line's text is gone, and lines that share a destination have several candidates. Almond's 14 tagged pointer lines name 8 destinations; 5 point to `idea-almond`, 3 to `concept-almonds`. Only 5 lines had a single candidate and were skipped. The `idea-ali-anxiety` line had one tagged neighbour but several untagged ones, since the candidates aren't limited to tagged entries.

## What limits the damage, and what doesn't

1. **The 03.11 guard doesn't fire after a rename.** `runmanager record` refuses a `migrate` copy into a note the source line's pointer already names, when an earlier run sent that line there for the same trigger (`CONTRACT.md` 5.3 item 15). But `record.py` `_sent` asks whether the earlier unit's copy went to the same note path. The earlier record says `Ideas/idea-almond.md`, and a new copy would go to `Ideas/idea-almond-renamed.md`, so the guard finds no earlier send. Read from the code, not run.
2. **What's left is the Migrator's own rule:** it leaves a line alone when the line's pointer already names the note (`spec-migrator.md` 07 item 5). Migrator case 21, `retry-21-no-second-copy`, tests that rule. So after a rename, a second copy of the 5 Brain Dump lines is stopped by an instruction only.
3. **What the Migrator would do with the 5 copies handed back from inside the Idea Note was not tested.**
