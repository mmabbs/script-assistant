---
type: regex
pattern: "\\A(?:(?!\\n## )[\\s\\S])*?(where (the )?evidence is (strong|weak))|\\n## (?!Open Research Questions)[^\\n]*\\n(?:(?!\\n## )[\\s\\S])*?(where (the )?evidence is (strong|weak))"
flags: i
match: not_contains
target: { source: file, path: project/Research/research-scurvy-remedies.md }
---
