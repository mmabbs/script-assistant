---
type: regex
pattern: "\"waits_on\"\\s*:\\s*\\[\\s*\\d"
match: not_contains
target: { source: file, path: run/answer.json }
---
