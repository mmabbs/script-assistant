# Stop dry run: steps

Built by `build.py DEST`. The project is `DEST/Lighthouse/`. It has three `- [r] ... #research/run-2` requests. A hook swaps the research workflow for a cheap stand-in. Agent 1 writes `Research/research-light-keeper-refusal.md` at once. Agent 2 waits 3 minutes, then would write `Research/research-light-tide-tables.md`. You stop the run in between.

## Build

1. In a terminal, run `python3 /Users/mabbs/.claude/plugins/local/script-asst/lib/runmanager/tests/dryrun-stop/build.py DEST`, with DEST a folder that doesn't hold a `Lighthouse` yet. It prints `built DEST/Lighthouse`.

## Run

2. Open a new terminal and run `cd DEST/Lighthouse` then `claude`.
3. When Claude Code asks whether to trust the folder, say yes.
4. Type `/reload-plugins`.
5. Type `/script-asst:run research 2`.
6. Open `DEST/Lighthouse/Research/` in Finder. Wait for `research-light-keeper-refusal.md` to appear. It takes a minute or so. Agent 2 is now waiting its 3 minutes.
7. As soon as the note appears, type `stop` in the Claude Code session. Do it within 3 minutes, before agent 2 finishes.
8. Wait for Claude to say the run closed and give a log link. Then open the run log, the newest file in `DEST/Lighthouse/Runs/`.

## Check

9. In `Research/`, check `research-light-tide-tables.md` is not there. Pass if it never appears. Look again a few minutes later, since agent 2 may still be running if the stop didn't hold.
10. Search `DEST/Lighthouse/` for `#research/run-2`. There are three requests: `Areas/area-mara.md`, `Ideas/idea-harrow-point.md`, `brain-dump.md`. Pass if every one still starts with `- [r]`, and none has a link line under it.
11. In the run log, find `## Requests still open`. Pass if all of these hold:
    1. Its first line is "You stopped this run. Every request stays open."
    2. It lists `research-light-keeper-refusal` exactly once, at its end, under "Written before you stopped the run:".
    3. `research-light-keeper-refusal` does not appear under `## Notes changed outside the run`.
12. With no run open, type `/script-asst:run recover`. Pass if it refuses.
13. Type `/script-asst:run abandon`. Pass if it refuses.

## If a check fails

14. Write down which numbered check failed. Paste the whole run log into the chat, plus the last 20 lines of the session if the run didn't close.
15. If agent 2 failed on a permission prompt or its `sleep 180` was refused (the log or `/workflows` shows it), say so, and paste what it showed.
16. If `research-light-keeper-refusal.md` never appeared and the workflow ran for a long time, the hook swap may not have fired. Check that `DEST/Lighthouse/.runs/research.js` starts with "Dry-run stand-in" in its description. If it holds the real workflow, the swap didn't run: say so.
