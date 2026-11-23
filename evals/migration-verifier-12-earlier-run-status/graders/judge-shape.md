---
type: llm
---

The reply should be the migration-verifier's batch findings: JSON with `batch`, `round`, `units`, and `missed`. It was handed two units: u1 and u2. Grade only the shape here, and where each problem points. Do not grade whether the verdicts are right.

Where each problem should point: for u2, `Ideas/idea-mara-habits.md` line 11 (the copy "- Mara has stopped answering letters from the mainland.", written in this run without the writer's provisional tag). u1 is expected to be approved. If a reply approves a unit that is expected to be a `fix`, it has no problems to check, and that is not a failure of this judge. If a reply makes u1 a `fix`, where its problems point is not graded here.

PASS if all of these hold: `units` has exactly one entry for each of u1 and u2, and no entry for any other unit; every `verdict` is `approve` or `fix`; every `fix` has at least one problem, and every `approve` has an empty `problems` list; every problem's `check` is one of `lost-detail`, `status`, `scope`, or `standalone`; on u2, every problem's `note` is `Ideas/idea-mara-habits.md` and its `line` is 11. A problem on u2 that names the source note (`brain-dump.md`), or line 10 of idea-mara-habits (the earlier run's wreck-buoy copy), is a FAIL.
FAIL if the reply holds no JSON findings, or if any rule above is broken: a unit missing or listed twice, a unit that wasn't handed, a `fix` with no problems, an `approve` with problems, or a `check` outside those four, or a problem on u2 whose `note` or `line` is not the one listed above. Quote the verdict and the problems.
