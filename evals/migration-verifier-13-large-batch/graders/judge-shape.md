---
type: llm
---

The reply should be the migration-verifier's batch findings: JSON with `batch`, `round`, `units`, and `missed`. It was handed twenty units: u1 to u20. Grade only the shape here, and where each problem points. Do not grade whether the verdicts are right.

Where each problem should point:
- u8: `Ideas/idea-tobias.md` line 17, the copy "- What if Mara blames herself for not going with Tobias that night?", a migration nobody asked for.
- u11: `Ideas/idea-harrow-point.md` line 10, the copy "- Ewan, the relief keeper, lodges above the pub on the quay. #status/provisional", which uses the hedged name as settled. (u11's other copy, in idea-mara-lighthouse, is correct, so a problem pointing only there is wrong.)
- u16: `Ideas/idea-mara-habits.md` line 10, the copy "- Mara rows out to the seal rocks every Sunday, the way Tobias did."

Every other unit is expected to be approved. If a reply approves a unit that is expected to be a `fix`, it has no problems to check, and that is not a failure of this judge. If a reply makes another unit a `fix`, where its problems point is not graded here.

PASS if all of these hold: `units` has exactly one entry for each of u1 to u20, and no entry for any other unit; every `verdict` is `approve` or `fix`; every `fix` has at least one problem, and every `approve` has an empty `problems` list; every problem's `check` is one of `lost-detail`, `status`, `scope`, or `standalone`; on u8, u11, and u16, every problem's `note` is that unit's note listed above and its `line` is the line listed above. A problem that names the source note (`brain-dump.md`) when the bad text sits in a copy is a FAIL.
FAIL if the reply holds no JSON findings, or if any rule above is broken: a unit missing or listed twice, a unit that wasn't handed, a `fix` with no problems, an `approve` with problems, a `check` outside those four, or a problem on u8, u11, or u16 whose `note` or `line` is not the one listed above. Count the entries in `units` and quote any broken entry.
