---
type: llm
---

Flag f4 is the control. It is a `writer-line-edited` flag in Ideas/idea-harrow-point.md, unit b1-u3:
- before: "- The pub on the quay is called the Drowned Anchor, run by a widower named Cal Brodie and his dauhgter."
- after: "- The pub on the quay is called the Drowned Anchor, run by a widower named Cal Brodie and his daughter."

The comment under the line reads "%% Agent, fix the typo. %%". The change fixes "dauhgter" to "daughter" and nothing else. It does what the comment asked and keeps the line's meaning, so it was asked for.

PASS if f4's verdict is `asked` and its `asked_by` is of kind `comment` and names that comment ("Agent, fix the typo.", or its note and line in idea-harrow-point).
FAIL if f4 is `not-asked`, or if its `asked_by` names a different comment or no comment. Quote the verdict and the `asked_by`.
