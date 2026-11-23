---
type: llm
focus: { source: file, path: run/unit-records.json }
---

The run had three operations: a split (one bullet about Pell ringing the bell became two copies, one in idea-harrow-point and one in idea-tobias), a merge (two cat bullets became one copy in idea-mara-lighthouse), and a plain migration (the paraffin line went to idea-mara-lighthouse).

This file is the migrator's unit record. Each entry in `units` lists its source lines in `sources` and the blocks it adds in `copies`. Each copy names its `note`.

PASS if the record shows:
1. The bell bullet as one unit with one entry in `sources` and two entries in `copies` (one in idea-harrow-point, one in idea-tobias).
2. The cat as one unit with two entries in `sources` and one entry in `copies`, in idea-mara-lighthouse.
3. The paraffin line as one unit with one entry in `sources` and one entry in `copies`, in idea-mara-lighthouse.
FAIL if any copy is missing from the record, or if the merged unit lists only one source line instead of two.
