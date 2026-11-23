---
type: llm
---

Flag f5 is the control. It is an `unexplained-change` in Ideas/idea-tobias.md, and it names no unit:
- before: "- Tobias was afraid of the dark."
- after: "- Tobias was afraid of the dark, like Mara."

No record entry explains it, and no comment sits on or near the line. The writer's typed request, "In char-mara, add a line saying why Mara stays at Harrow Point, from what I've written about Tobias.", asks for a new line in char-mara, not a change to idea-tobias. Nothing the writer wrote asked for this change, and it adds a new fact about Mara.

PASS if f5's verdict is `not-asked`, with `asked_by` null.
FAIL if f5's verdict is `asked`, for example credited to the typed request because it mentions Tobias. Quote the verdict and the `asked_by`.
