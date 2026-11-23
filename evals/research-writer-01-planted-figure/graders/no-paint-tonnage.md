---
type: regex
pattern: "(tonnes?|tons?) of paint|\\b60 (tonnes|tons)\\b|sixty (tonnes|tons)"
flags: i
match: not_contains
target: { source: file, path: project/Research/research-eiffel-tower-upkeep.md }
---
