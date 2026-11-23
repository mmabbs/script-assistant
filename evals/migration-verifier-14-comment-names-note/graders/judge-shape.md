---
type: llm
---

The reply should be the migration-verifier's batch findings: JSON with `batch`, `round`, `units`, and `missed`. It was handed three units: u1, u2, and u3. Grade only the shape here, and where each problem points. Do not grade whether the verdicts are right.

Where each problem should point: for u1, `Ideas/idea-mara-lighthouse.md` line 10, where the misplaced copy sits ("- Fenwick's chandlery on the quay is the only place left that sells lamp paraffin."). The bad text is that copy. It is not in `Ideas/idea-harrow-point.md`, the note where it should have gone, and not in `brain-dump.md`. u1's other copy, in idea-mara-habits, is correct, so a problem pointing only there is wrong. u2 and u3 are expected to be approved. If a reply approves a unit that is expected to be a `fix`, it has no problems to check, and that is not a failure of this judge. If a reply makes u2 or u3 a `fix`, where its problems point is not graded here.

PASS if all of these hold: `units` has exactly one entry for each of u1, u2, and u3, and no entry for any other unit; every `verdict` is `approve` or `fix`; every `fix` has at least one problem, and every `approve` has an empty `problems` list; every problem's `check` is one of `lost-detail`, `status`, `scope`, or `standalone`; on u1, every problem's `note` is `Ideas/idea-mara-lighthouse.md` and its `line` is 10.
FAIL if the reply holds no JSON findings, or if any rule above is broken: a unit missing or listed twice, a unit that wasn't handed, a `fix` with no problems, an `approve` with problems, or a `check` outside those four, or a problem on u1 whose `note` or `line` is not the one listed above, such as one that names `Ideas/idea-harrow-point.md` or `brain-dump.md` and puts idea-mara-lighthouse only in `what`. Quote the verdict and the problems.
