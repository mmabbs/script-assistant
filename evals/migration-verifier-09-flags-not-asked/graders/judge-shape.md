---
type: llm
---

The reply should be the migration-verifier's flag findings: JSON with a `flags` list. It was handed four flags: f1, f2, f3, and f4. Grade only the shape here, not whether the verdicts are right.

PASS if all of these hold: `flags` has exactly one entry for each of f1, f2, f3, and f4, and no entry for any other flag; every `verdict` is `asked` or `not-asked`; every `asked` verdict has an `asked_by` object; every `not-asked` verdict has `asked_by` set to null.
FAIL if the reply holds no JSON findings, or if any rule above is broken: a flag missing or listed twice, a flag that wasn't handed, an `asked` with no `asked_by`, or a `not-asked` whose `asked_by` isn't null. Quote the verdicts and the `asked_by` values.
