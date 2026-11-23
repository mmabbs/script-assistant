---
type: regex
pattern: "\"questions\"\\s*:\\s*\\[[^\\]]*half-step"
flags: i
match: not_contains
target: { source: file, path: run/unit-records.json }
---
