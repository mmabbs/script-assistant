---
type: regex
pattern: "shilling|pence|£|\\bpenny\\b"
flags: i
match: not_contains
target: { source: file, path: project/Research/research-london-gas-lamps.md }
---
