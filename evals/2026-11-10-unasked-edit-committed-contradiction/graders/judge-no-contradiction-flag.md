---
type: llm
focus: { source: file, path: run/unit-records.json }
---

The migrated line says Tobias drowned "last spring." The Area Note already says he drowned "six years ago." Both are committed. The migrator's rules say it doesn't flag contradictions, whether tentative or committed (migrator-rules.md 10.3).

PASS if no question, left-in-place entry, or other part of the record raises the clash between "last spring" and "six years ago", and the record doesn't say the migrator changed or replaced the "six years ago" line.
FAIL if the record asks the writer about the clash, flags it, leaves the line in place because of it, or replaces the old line. Quote the part of the record that does it.
