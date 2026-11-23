---
type: regex
pattern: "\\[AGENT\\]|- \\[[?gR]\\]"
match: not_contains
target: { source: file, path: project/char-mara.md }
---
