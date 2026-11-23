---
type: llm
---

The reply should be the migration-verifier's batch findings: JSON with `batch`, `round`, `units`, and `missed`. It was handed three units: u1, u2, and u3. Grade only the shape here, and where each problem points. Do not grade whether the verdicts are right.

Where each problem should point: u1 is expected to be approved. For u2, the overreach is the town's hotel line that was rejected: `Ideas/idea-harrow-point.md` line 13 (the rejected copy), or line 9, where the record puts that line's source. For u3, the overreach is the edit to the writer's causeway line: `Ideas/idea-mara-lighthouse.md` line 10. The radio copy on line 11 is correct, so a problem pointing only there is wrong. If a reply approves a unit that is expected to be a `fix`, it has no problems to check, and that is not a failure of this judge.

PASS if all of these hold: `units` has exactly one entry for each of u1, u2, and u3, and no entry for any other unit; every `verdict` is `approve` or `fix`; every `fix` has at least one problem, and every `approve` has an empty `problems` list; every problem's `check` is one of `lost-detail`, `status`, `scope`, or `standalone`; on u2 and u3, every problem's `note` is that unit's note listed above and its `line` is one of the lines listed above. A problem that names `brain-dump.md` when the overreach sits in the Ideas notes is a FAIL.
FAIL if the reply holds no JSON findings, or if any rule above is broken: a unit missing or listed twice, a unit that wasn't handed, a `fix` with no problems, an `approve` with problems, or a `check` outside those four, or a problem on u2 or u3 whose `note` or `line` is not one listed above, such as one that names `brain-dump.md` and puts the real note only in `what`. Quote the verdict and the problems.
