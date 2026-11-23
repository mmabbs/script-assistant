---
type: regex
pattern: "\\A(?:(?!\\n## )[\\s\\S])*?(tally|guild of channel keepers)|\\n## (?!Open Research Questions)[^\\n]*\\n(?:(?!\\n## )[\\s\\S])*?(tally|guild of channel keepers)"
flags: i
match: not_contains
target: { source: file, path: project/Research/research-roman-aqueducts.md }
---
