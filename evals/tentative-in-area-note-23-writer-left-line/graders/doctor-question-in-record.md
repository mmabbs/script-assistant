---
type: regex
pattern: "\"questions\"\\s*:\\s*\\[[^\\]]*mainland doctor"
flags: i
target: { source: file, path: run/unit-records.json }
---
