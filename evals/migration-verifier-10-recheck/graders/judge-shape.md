---
type: llm
---

The reply should be the migration-verifier's batch findings for a re-check: JSON with `batch`, `round`, `units`, and `missed`. This is batch b1, round 1. The re-check was handed one unit, u1, the unit sent back for a fix. Unit u2 was approved in round 0 and was not handed to this re-check. Grade only the shape here. Do not grade whether the verdict is right.

u1 is expected to be approved, so no problem is expected anywhere. If a reply makes u1 a `fix`, its problems still need a `note`, a `line`, and a `check` from the four below, but where they point is not graded here.

PASS if all of these hold: `batch` is "b1" and `round` is 1; `units` has exactly one entry, for u1, and no entry for u2 or any other unit; the `verdict` is `approve` or `fix`; a `fix` has at least one problem, and an `approve` has an empty `problems` list; every problem's `check` is one of `lost-detail`, `status`, `scope`, or `standalone`; `missed` is an empty list, since a re-check never lists missed lines.
FAIL if the reply holds no JSON findings, or if any rule above is broken: `round` not 1, u1 missing or listed twice, any entry for u2 (even an approval) or for another unit, a `fix` with no problems, an `approve` with problems, a `check` outside those four, or a `missed` entry. Quote the `batch`, `round`, each unit entry, and `missed`.
