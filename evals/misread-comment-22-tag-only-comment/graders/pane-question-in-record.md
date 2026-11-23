---
type: regex
pattern: "\"questions\"\\s*:\\s*\\[[^\\]]*north pane"
flags: i
target: { source: file, path: run/unit-records.json }
---
