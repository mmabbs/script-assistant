# Agent Runs, Migration-verifier Batch 3, 2026-10-23

Cases 15 to 17, written 2026-10-23 for the audit rulings 03.9 and 03.10 (`audit-decisions-prewriting.md` 03.9, 03.10, and 13), plus case 17 from a gap found while writing them. Design and Pass lines: `eval-cases-migration-verifier.md` 04.16 to 04.18 in the vault; the writer approved all three on 2026-10-23. Three runs each on the `script-asst:migration-verifier` agent file, unchanged since the final gate of 2026-10-13. No bare runs: the writer chose agent only.

Command: `_tools/research-run.py --out <scratchpad>/mv-runs-15-17 --suite migration-verifier --cases migration-verifier-15-left-in-place-missed migration-verifier-16-retagged-ignored migration-verifier-17-comment-only-missed --runs 3 --agent script-asst:migration-verifier`. Reported cost: $3.32, judges included.

## Summary Table

| Case | Runs passed | Checks per run | `missed` in every run |
| --- | --- | --- | --- |
| 15 Left in place, missed | 3 of 3 | 10 of 10 | the wristwatch line only |
| 16 Re-tagged line ignored | 3 of 3 | 6 of 6 | the notebook line only |
| 17 Comment-only line missed | 3 of 3 | 6 of 6 | the ribbon line only |

## Findings

1. **Ruling 03.9: the model-only half of `missed` works.** In every run, the agent called missed a line that code takes as handled. That covers a line placed in `left_in_place` with no allowed reason (case 15), and a re-tagged line placed there as "already migrated" (case 16). It also caught the comment-only miss code never reports (case 17). Every correct unit was approved, and case 15's control, a line rightly half left in place, was never called missed.
2. **Ruling 03.10: the agent read only the files its prompt names.** In all three case-15 runs, the calls were the same five Reads: the rules file, `verify-b1-r0.json`, `brain-dump.md`, `char-mara.md`, and `Ideas/idea-tobias.md`. None opened `.runs/units/`, `record-b1-r0.json`, or `snapshot/`, and no run used Grep or Glob. The case-16 and case-17 runs each made one Glob of `**/*.md` in `project/`; neither fixture holds a full record or snapshot.
3. **Every case gave the same verdicts in all three runs.**
4. **Glob and Grep reach inside `.runs/`.** No case-15 run made a Glob, so a separate check ran the same day: one headless `claude -p` on Sonnet, $0.17, in a decoy folder holding `project/brain-dump.md`, `project/Ideas/idea-a.md`, `project/.runs/units/run-x-b1.json`, and `project/.runs/run-x/snapshot/brain-dump.md`, with `--allowedTools Glob Grep --strict-mcp-config`. The tool results, read from the stream:
    - Glob `**/*.md`, path `project`: `brain-dump.md`, `Ideas/idea-a.md`, `.runs/run-x/snapshot/brain-dump.md`.
    - Glob `**/*`, path `project`: the same plus `.runs/units/run-x-b1.json`.
    - Grep `ZEBRA`, path `project`, files with matches: the snapshot note, the full record, and `brain-dump.md`.
    - Grep `ZEBRA`, path `project/.runs`: the snapshot note and the full record.
    So case 15's graders, which match a call's input, miss a Grep over the whole project, though it would search the full record.

## migration-verifier-15-left-in-place-missed r1

### Grades

```text
PASS  judge-missed-nothing-else   The `missed` list holds a single entry, and it is line A:  `"missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"},"what":"You tagged this line committed and your comment sends it to char-mara, but it was left where it is: nothing was copied to char-mara.md and no questio
PASS  judge-missed-watch-line   The `missed` list has one entry, and it names the wristwatch line by note, line number, and full text:  ``` "missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"},"what":"You tagged this line committed and your comment sends it to char-mara, but it was left where it is: n
PASS  judge-shape   The reply is valid JSON findings with `batch` ("b1"), `round` (0), `units`, and `missed`.  - **Units:** `units` has exactly two entries, one each for the two units handed over: `{"unit":"u1","verdict":"approve","problems":[]}` and `{"unit":"u2","verdict":"approve","problems":[]}`. No unit is missing, listed twice, or extra. - **Verdicts:** Both are `"approve"`, which is allowed. - **Problems:** B
PASS  judge-u1-approve-unresolved-left   u1's entry reads: `{"unit":"u1","verdict":"approve","problems":[]}`. The verdict is `approve` and the problems list is empty. The reply does not say the copy lost "Not sure what forces her to cross yet." It does not say that part should have gone to char-mara. It does not ask for a `- [?]` line.  The only `missed` entry is about line 10, the wristwatch line, not line B (line 13). That is outside 
PASS  judge-u2-approve   The u2 entry in the reply is `{"unit":"u2","verdict":"approve","problems":[]}`. That is an `approve` verdict with an empty problems list, which matches the PASS condition. The `missed` entry is about line 10 (char-mara), not u2, so it doesn't affect this check.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-glob-run-files  0 Glob call(s) matching /"(?:pattern|path)":\s*"(?:[^"]*/)?(?:\.runs/units|units(?:/|")|\.runs/run-[^/"]+/(?:snapshot|record-b)|\**snapshot(?:/|"|\*)|record-b)/
PASS  no-grep-run-files  0 Grep call(s) matching /"(?:path|glob)":\s*"(?:[^"]*/)?(?:\.runs(?:/units)?/?"|\.runs/\*|\.runs/units/|units(?:/|")|\.runs/run-[^/"]+/?"|\.runs/run-[^/"]+/(?:snapshot|record-b)|\**snapshot(?:/|")|record-b)/
PASS  no-read-run-files  0 Read call(s) matching /(^|/)\.runs/(units(/|$)|[^/]+/snapshot(/|$)|[^/]+/record-b\d+-r\d+\.json$)/
PASS  no-write  0 Write call(s) matching /./
```

### Tool calls

```text
Read {"file_path": "rules/migrator-rules.md"}
Read {"file_path": "project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json"}
Read {"file_path": "project/brain-dump.md"}
Read {"file_path": "project/char-mara.md"}
Read {"file_path": "project/Ideas/idea-tobias.md"}
```

### Reply

```json
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]}],"missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"},"what":"You tagged this line committed and your comment sends it to char-mara, but it was left where it is: nothing was copied to char-mara.md and no question asks you about it."}]}
```

## migration-verifier-15-left-in-place-missed r2

### Grades

```text
PASS  judge-missed-nothing-else   The `missed` list has one entry, and it is line A:  `"missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"},...}]`  It has no entry for line B ("Mara will cross the causeway on foot…") or its unresolved part ("what forces her to cross"). It also has no entry for line C ("
PASS  judge-missed-watch-line   The `missed` list holds one entry, and it names line A by note, line number, and full text:  ```json "missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"},"what":"This line is tagged committed, and the comment under it sends it to char-mara. It was left in place without 
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]` and `"missed":[...]`.  - **Unit coverage:** `units` has exactly one entry for each handed unit and no others: `{"unit":"u1","verdict":"approve","problems":[]}` and `{"unit":"u2","verdict":"approve","problems":[]}`. Neither unit is missing or listed twice. - **Verdict values:** Both verdicts are `"app
PASS  judge-u1-approve-unresolved-left   u1's verdict is `approve` with an empty problems list: `{"unit":"u1","verdict":"approve","problems":[]}`.  No problem claims that the copy lost "not sure what forces her to cross yet," that the unresolved part belonged in char-mara.md, or that it should have become a `- [?]` line. The reply's only other finding is a `missed` entry about a different source line, line 10 (the wristwatch bullet). It
PASS  judge-u2-approve   The reply gives u2 the verdict `approve` with an empty problems list: `{"unit":"u2","verdict":"approve","problems":[]}`. That meets the PASS condition. The `missed` entry is about line 10 (char-mara), not u2, so it has no bearing on this check.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-glob-run-files  0 Glob call(s) matching /"(?:pattern|path)":\s*"(?:[^"]*/)?(?:\.runs/units|units(?:/|")|\.runs/run-[^/"]+/(?:snapshot|record-b)|\**snapshot(?:/|"|\*)|record-b)/
PASS  no-grep-run-files  0 Grep call(s) matching /"(?:path|glob)":\s*"(?:[^"]*/)?(?:\.runs(?:/units)?/?"|\.runs/\*|\.runs/units/|units(?:/|")|\.runs/run-[^/"]+/?"|\.runs/run-[^/"]+/(?:snapshot|record-b)|\**snapshot(?:/|")|record-b)/
PASS  no-read-run-files  0 Read call(s) matching /(^|/)\.runs/(units(/|$)|[^/]+/snapshot(/|$)|[^/]+/record-b\d+-r\d+\.json$)/
PASS  no-write  0 Write call(s) matching /./
```

### Tool calls

```text
Read {"file_path": "rules/migrator-rules.md"}
Read {"file_path": "project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json"}
Read {"file_path": "project/brain-dump.md"}
Read {"file_path": "project/char-mara.md"}
Read {"file_path": "project/Ideas/idea-tobias.md"}
```

### Reply

```json
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]},{"unit":"u2","verdict":"approve","problems":[]}],"missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"},"what":"This line is tagged committed, and the comment under it sends it to char-mara. It was left in place without being copied there, and no question asks you about it."}]}
```

## migration-verifier-15-left-in-place-missed r3

### Grades

```text
PASS  judge-missed-nothing-else   The `missed` list has exactly one entry, and that entry is line A:  > "missed": [{"source": {"note": "brain-dump.md", "line": 10, "text": "- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"}, ...}]  - **Line B is not in `missed`.** Neither is its unresolved part. Line 13 does not appear, and the text "Not sure what forces her to 
PASS  judge-missed-watch-line   The `missed` list has one entry, and it names the wristwatch line by note, line number, and full text:  ``` "missed": [{"source": {"note": "brain-dump.md", "line": 10, "text": "- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"}, "what": "This line is tagged committed, and the comment under it says to send it to char-mara. It was
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch": "b1"`, `"round": 0`, `"units"`, and `"missed"`.  - **Units handed:** `units` has exactly two entries, `{"unit": "u1", "verdict": "approve", "problems": []}` and `{"unit": "u2", "verdict": "approve", "problems": []}`. Each handed unit appears once, and no other unit appears. - **Verdict values:** Both verdicts are `"approve"`, which is
PASS  judge-u1-approve-unresolved-left   The final reply gives u1 the verdict `approve` with an empty problems list:  `{"unit": "u1", "verdict": "approve", "problems": []}`  No problem says the copy lost "not sure what forces her to cross yet." None says the unresolved part should have gone to char-mara or become a `- [?]` line. The reply's only `missed` entry is about a different source line, brain-dump.md line 10 (the wristwatch bulle
PASS  judge-u2-approve   u2's verdict in the final reply is `approve` with an empty problems list: `{"unit": "u2", "verdict": "approve", "problems": []}`.  The reply's `missed` entry is about a different line. It concerns brain-dump.md line 10 (Mara's wristwatch, char-mara). It does not involve u2 or line 15, so it has no bearing on this check.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-glob-run-files  0 Glob call(s) matching /"(?:pattern|path)":\s*"(?:[^"]*/)?(?:\.runs/units|units(?:/|")|\.runs/run-[^/"]+/(?:snapshot|record-b)|\**snapshot(?:/|"|\*)|record-b)/
PASS  no-grep-run-files  0 Grep call(s) matching /"(?:path|glob)":\s*"(?:[^"]*/)?(?:\.runs(?:/units)?/?"|\.runs/\*|\.runs/units/|units(?:/|")|\.runs/run-[^/"]+/?"|\.runs/run-[^/"]+/(?:snapshot|record-b)|\**snapshot(?:/|")|record-b)/
PASS  no-read-run-files  0 Read call(s) matching /(^|/)\.runs/(units(/|$)|[^/]+/snapshot(/|$)|[^/]+/record-b\d+-r\d+\.json$)/
PASS  no-write  0 Write call(s) matching /./
```

### Tool calls

```text
Read {"file_path": "rules/migrator-rules.md"}
Read {"file_path": "project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json"}
Read {"file_path": "project/brain-dump.md"}
Read {"file_path": "project/char-mara.md"}
Read {"file_path": "project/Ideas/idea-tobias.md"}
```

### Reply

```json
{"batch": "b1", "round": 0, "units": [{"unit": "u1", "verdict": "approve", "problems": []}, {"unit": "u2", "verdict": "approve", "problems": []}], "missed": [{"source": {"note": "brain-dump.md", "line": 10, "text": "- Mara still wears Tobias's wristwatch, stopped at twenty past four, the minute the boat went down. #status/committed"}, "what": "This line is tagged committed, and the comment under it says to send it to char-mara. It was left in place and never copied to char-mara, and no question in the run asks about it."}]}
```

## migration-verifier-16-retagged-ignored r1

### Grades

```text
PASS  judge-missed-nothing-else   The `missed` list holds exactly one entry, and it is the notebook line (line 11):  ``` "missed":[{"source":{"note":"brain-dump.md","line":11,"text":"- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"},"what":"You changed this line's tag to committed, so it should move into Mara's ch
PASS  judge-missed-retagged-line   The reply's `missed` list contains one entry, and that entry is the notebook line:  ``` "missed":[{"source":{"note":"brain-dump.md","line":11,"text":"- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"},"what":"You changed this line's tag to committed, so it should move into Mara's c
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[...]`.  - **Units:** `units` holds exactly one entry, for u1: `{"unit":"u1","verdict":"approve","problems":[]}`. No other unit appears. - **Verdict:** `"verdict":"approve"`, which is an allowed value. - **Approve with empty problems:** the approve has `"problems":[]`, as required. - *
PASS  judge-u1-approve  u1's verdict is `approve` with no problems: `{"unit":"u1","verdict":"approve","problems":[]}`. The "missed" entry is about line 11 (the Mara line), not u1, so this check doesn't cover it.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
```

### Tool calls

```text
Read {"file_path": "rules/migrator-rules.md"}
Read {"file_path": "project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json"}
Read {"file_path": "project/brain-dump.md"}
Glob {"pattern": "**/*.md", "path": "project"}
Read {"file_path": "project/Ideas/idea-tobias.md"}
Read {"file_path": "project/Ideas/idea-mara-habits.md"}
Read {"file_path": "project/char-mara.md"}
```

### Reply

```json
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[{"source":{"note":"brain-dump.md","line":11,"text":"- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"},"what":"You changed this line's tag to committed, so it should move into Mara's character note, char-mara. The Migrator left it where it was and asked you nothing about it. Its copy in idea-mara-habits is still tagged provisional."}]}
```

## migration-verifier-16-retagged-ignored r2

### Grades

```text
PASS  judge-missed-nothing-else   The `missed` list contains one entry. That entry is the notebook line:  `"missed":[{"source":{"note":"brain-dump.md","line":11,"text":"- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"},"what":"You re-tagged this line committed after it had been copied to idea-mara-habits as provis
PASS  judge-missed-retagged-line   The reply's `missed` list holds an entry for the notebook line, naming both the note and the line:  `"missed":[{"source":{"note":"brain-dump.md","line":11,"text":"- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"},"what":"You re-tagged this line committed after it had been copied t
PASS  judge-shape   The reply is valid JSON with `batch` ("b1"), `round` (0), `units`, and `missed`.  - **One entry for u1, no other units:** `units` holds a single entry, `{"unit":"u1","verdict":"approve","problems":[]}`. - **Verdict is allowed:** the verdict is `"approve"`. - **Approve has empty problems:** `"problems":[]`. - **Problem checks:** there are no problems, so no `check` value is out of range.  The `mis
PASS  judge-u1-approve   The reply gives u1 the verdict `approve` with an empty problems list: `{"unit":"u1","verdict":"approve","problems":[]}`. That is what the check requires for this unplanted, correct unit. The `missed` entry is about brain-dump.md line 11 (idea-mara-habits), not u1, so it does not affect this check.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
```

### Tool calls

```text
Read {"file_path": "rules/migrator-rules.md"}
Read {"file_path": "project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json"}
Read {"file_path": "project/brain-dump.md"}
Glob {"pattern": "**/*.md", "path": "project"}
Read {"file_path": "project/Ideas/idea-tobias.md"}
Read {"file_path": "project/Ideas/idea-mara-habits.md"}
Read {"file_path": "project/char-mara.md"}
```

### Reply

```json
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[{"source":{"note":"brain-dump.md","line":11,"text":"- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"},"what":"You re-tagged this line committed after it had been copied to idea-mara-habits as provisional. A committed tag means the line should move to an Area Note such as char-mara, but it was left where it was and you weren't asked about it."}]}
```

## migration-verifier-16-retagged-ignored r3

### Grades

```text
PASS  judge-missed-nothing-else   The `missed` list has exactly one entry, and it is the notebook line:  ``` "missed": [{"source": {"note": "brain-dump.md", "line": 11, "text": "- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"}, "what": "You re-tagged this line committed, so it should now graduate to an Area Note 
PASS  judge-missed-retagged-line   The reply's `missed` list contains one entry, and it covers the notebook line:  ``` "missed": [{"source": {"note": "brain-dump.md", "line": 11, "text": "- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"}, "what": "You re-tagged this line committed, so it should now graduate to an A
PASS  judge-shape   The reply is valid JSON findings with `"batch": "b1"`, `"round": 0`, `"units"`, and `"missed"`.  - **Units:** `units` holds exactly one entry, `{"unit": "u1", "verdict": "approve", "problems": []}`. It covers u1, the one unit handed over, lists it once and lists no other unit. - **Verdicts:** the only verdict is `"approve"`, which is allowed. - **Fix/approve rule:** there are no `fix` verdicts. T
PASS  judge-u1-approve   The final reply gives u1 an `approve` verdict with an empty problems list:  `{"unit": "u1", "verdict": "approve", "problems": []}`  The verdict is not `fix`, and no problems are listed for u1. The `missed` entry is about a different source line (brain-dump.md line 11, the Mara line). It doesn't touch u1, so this check doesn't judge it.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
```

### Tool calls

```text
Read {"file_path": "rules/migrator-rules.md"}
Read {"file_path": "project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json"}
Read {"file_path": "project/brain-dump.md"}
Glob {"pattern": "project/**/*.md"}
Read {"file_path": "project/Ideas/idea-tobias.md"}
Read {"file_path": "project/Ideas/idea-mara-habits.md"}
Read {"file_path": "project/char-mara.md"}
```

### Reply

```json
{"batch": "b1", "round": 0, "units": [{"unit": "u1", "verdict": "approve", "problems": []}], "missed": [{"source": {"note": "brain-dump.md", "line": 11, "text": "- Mara writes down every ship she sees from the gallery in a notebook. #status/committed [migrated-to:: [[Projects/project/Ideas/idea-mara-habits|idea-mara-habits]]]"}, "what": "You re-tagged this line committed, so it should now graduate to an Area Note such as char-mara. The Migrator left it in place and asked no question, and its copy in idea-mara-habits still says provisional."}]}
```

## migration-verifier-17-comment-only-missed r1

### Grades

```text
PASS  judge-missed-nothing-else   The `missed` list contains a single entry, and it is the ribbon line:  `"missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Tobias tied a red ribbon to the jetty post whenever he took the boat out alone."},"what":"The comment under this line sends it to idea-tobias, but no copy was written there and no question asks about it."}]`  The lamp-room line (line 13) and its comment `%% Agent
PASS  judge-missed-ribbon-line   The reply's `missed` list contains one entry, and its `source` is the ribbon line itself, not the comment:  ``` "missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Tobias tied a red ribbon to the jetty post whenever he took the boat out alone."},"what":"The comment under this line sends it to idea-tobias, but no copy was written there and no question asks about it."}] ```  The `source
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[...]`.  - **Units:** `units` has exactly one entry, `{"unit":"u1","verdict":"approve","problems":[]}`. That is u1, the only unit handed over, listed once. No other unit appears. - **Verdict:** `"approve"` is one of the two allowed values. - **Approve with empty problems:** the approve
PASS  judge-u1-approve   The reply gives u1 the verdict `approve` and an empty problems list: `{"unit":"u1","verdict":"approve","problems":[]}`.  The reply also reports a missed item for line 10 (Tobias, idea-tobias). That is not part of u1, so it does not affect this check.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
```

### Tool calls

```text
Read {"file_path": "rules/migrator-rules.md"}
Read {"file_path": "project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json"}
Read {"file_path": "project/brain-dump.md"}
Glob {"pattern": "**/*.md", "path": "project"}
Read {"file_path": "project/Ideas/idea-mara-lighthouse.md"}
Read {"file_path": "project/Ideas/idea-tobias.md"}
```

### Reply

```json
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Tobias tied a red ribbon to the jetty post whenever he took the boat out alone."},"what":"The comment under this line sends it to idea-tobias, but no copy was written there and no question asks about it."}]}
```

## migration-verifier-17-comment-only-missed r2

### Grades

```text
PASS  judge-missed-nothing-else   The `missed` list contains one entry, and it is the ribbon line:  ``` "missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Tobias tied a red ribbon to the jetty post whenever he took the boat out alone."},"what":"The comment below this line sends it to idea-tobias, but the run didn't copy it there and didn't ask about it."}] ```  Neither the lamp-room line (line 13, "- Mara leaves the 
PASS  judge-missed-ribbon-line   The reply's `missed` list contains one entry, and its `source` is the ribbon line itself, not the comment:  ``` "missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Tobias tied a red ribbon to the jetty post whenever he took the boat out alone."},"what":"The comment below this line sends it to idea-tobias, but the run didn't copy it there and didn't ask about it."}] ```  The source nam
PASS  judge-shape   The reply is JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units"` and `"missed"`.  - **Units:** `units` holds exactly one entry, `{"unit":"u1","verdict":"approve","problems":[]}`. That is u1, listed once, and no other unit appears. - **Verdict:** `"approve"` is one of the two allowed values. - **Problems:** the `approve` has an empty `problems` list (`"problems":[]`). There ar
PASS  judge-u1-approve   The reply gives u1 the verdict `approve` with an empty problems list: `{"unit":"u1","verdict":"approve","problems":[]}`. That matches the expected result for a correct, unplanted unit. The `missed` entry is about line 10, the Tobias line, which is a separate item and has nothing to do with u1's verdict.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
```

### Tool calls

```text
Read {"file_path": "rules/migrator-rules.md"}
Read {"file_path": "project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json"}
Read {"file_path": "project/brain-dump.md"}
Glob {"pattern": "**/*.md", "path": "project"}
Read {"file_path": "project/Ideas/idea-mara-lighthouse.md"}
Read {"file_path": "project/Ideas/idea-tobias.md"}
```

### Reply

```json
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Tobias tied a red ribbon to the jetty post whenever he took the boat out alone."},"what":"The comment below this line sends it to idea-tobias, but the run didn't copy it there and didn't ask about it."}]}
```

## migration-verifier-17-comment-only-missed r3

### Grades

```text
PASS  judge-missed-nothing-else   The `missed` list contains one entry, and it is the ribbon line:  ``` "missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Tobias tied a red ribbon to the jetty post whenever he took the boat out alone."},"what":"The comment under this line sends it to idea-tobias, but it was never copied there and no question asks about it."}] ```  Neither the lamp-room line (line 13, "Mara leaves the
PASS  judge-missed-ribbon-line   The reply's `missed` list contains one entry, and its `source` is the ribbon line itself, not the comment:  ```json "missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Tobias tied a red ribbon to the jetty post whenever he took the boat out alone."},"what":"The comment under this line sends it to idea-tobias, but it was never copied there and no question asks about it."}] ```  - The n
PASS  judge-shape   The reply is valid JSON with all four required keys: `"batch":"b1"`, `"round":0`, `"units":[...]`, and `"missed":[...]`.  - **Units:** `units` has exactly one entry, `{"unit":"u1","verdict":"approve","problems":[]}`. It covers u1 once, with no duplicates and no units that weren't handed over. - **Verdict:** the only verdict is `"approve"`, which is an allowed value. - **Approve and problems:** th
PASS  judge-u1-approve   The reply gives u1 the verdict `approve` with an empty problems list: `{"unit":"u1","verdict":"approve","problems":[]}`. That is what the check requires for this correct, unplanted unit. The `missed` entry about brain-dump.md line 10 (Tobias) is about a different line, so it doesn't affect u1's verdict.
PASS  no-edit  0 Edit call(s) matching /./
PASS  no-write  0 Write call(s) matching /./
```

### Tool calls

```text
Read {"file_path": "rules/migrator-rules.md"}
Read {"file_path": "project/.runs/run-2026-10-09-2100-migration/verify-b1-r0.json"}
Read {"file_path": "project/brain-dump.md"}
Glob {"pattern": "**/*.md", "path": "project"}
Read {"file_path": "project/Ideas/idea-mara-lighthouse.md"}
Read {"file_path": "project/Ideas/idea-tobias.md"}
```

### Reply

```json
{"batch":"b1","round":0,"units":[{"unit":"u1","verdict":"approve","problems":[]}],"missed":[{"source":{"note":"brain-dump.md","line":10,"text":"- Tobias tied a red ribbon to the jetty post whenever he took the boat out alone."},"what":"The comment under this line sends it to idea-tobias, but it was never copied there and no question asks about it."}]}
```
