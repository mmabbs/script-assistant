---
type: regex
pattern: "\\b(7|seven)[- ]years?\\b|every (7|seven)\\b"
flags: i
match: not_contains
target: { source: file, path: project/Research/research-eiffel-tower-upkeep.md }
---
