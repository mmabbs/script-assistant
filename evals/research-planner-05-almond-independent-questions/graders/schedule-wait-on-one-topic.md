---
type: regex
pattern: "\"waits_on\"\\s*:\\s*\\[\\s*\\d+\\s*,"
match: not_contains
target: { source: file, path: run/answer.json }
---
