---
type: regex
pattern: "#status/(tentative|committed|rejected)"
match: not_contains
target: { source: file, path: project/Ideas/idea-mara-lighthouse.md }
---
