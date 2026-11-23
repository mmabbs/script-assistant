# Migrator, case 24, three runs

Run on 2026-10-23 with `_tools/research-run.py --suite migrator --agent script-asst:migrator --cases request-comment-24-carried-request --runs 3`, for the Run manager plan's Milestone 15. The agent file gained its sixth instruction the same day (spec-migrator.md 07 item 6), and the plugin's `references/migrator-rules.md` gained the 08.1 rule on a comment the run wrote to carry the writer's request (spec-migrator.md 13 item 23). `_fixtures/rules/migrator-rules.md` was recopied from it, which also brought in the 01.8 frontmatter rule of 2026-10-15 that the copy lacked.

| Case | Run | Checks passed | Pass line held, checked by hand |
| --- | --- | --- | --- |
| 24 | r1 | 6 of 6 | yes |
| 24 | r2 | 6 of 6 | yes |
| 24 | r3 | 6 of 6 | yes |

Cost: $1.14, judges included.

## Findings

1. **Every run followed the carried request for the line above it only.** One `migrate` unit, `trigger` kind `comment`, copied the drowning line into idea-lighthouse.
2. **Every run left the wedding-rings line in place and asked about it.** Each question quotes the request and asks whether it should cover the later line too. The Pass line allows a question.
3. **No run touched the Brain Dump doc.**

## request-comment-24-carried-request r1: 6 of 6 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  drowning-bell-in-lighthouse  found 'drowning'
PASS  judge-record-trigger-and-scope   1. Unit `u1` copies the drowning line into idea-lighthouse. Its `copies` has `"note": "Ideas/idea-lighthouse.md"`, and its `lines` include `"- The fog bell rings on its own the night before every drowning."`  2. The trigger is the comment. `u1` has `"kind": "comment"`, and its `text` reproduces the request comment's words: `"[AGENT] Your request from the migration run of 2026-10-21, for this line
PASS  no-wedding-rings-in-lighthouse  no match
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-lighthouse.md work/project/Ideas/idea-lighthouse.md
--- before/project/Ideas/idea-lighthouse.md	2026-10-23 15:14:28
+++ work/project/Ideas/idea-lighthouse.md	2026-10-23 15:14:50
@@ -8,3 +8,7 @@
 ## The lamp
 
 - The lamp uses whale oil, which the town can no longer afford.
+
+## The fog bell
+
+- The fog bell rings on its own the night before every drowning.
```

### Unit record

```json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "[AGENT] Your request from the migration run of 2026-10-21, for this line: \"everything about the fog bell goes into idea-lighthouse, tagged or not\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The fog bell rings on its own the night before every drowning."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-lighthouse.md",
          "under": "# Idea - Lighthouse",
          "lines": [
            "## The fog bell",
            "- The fog bell rings on its own the night before every drowning."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The carried-over request is the writer's own, and it routes the line above it to idea-lighthouse. The line is untagged, so it stays tentative, under a new fog bell heading beside the existing lamp cluster."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 12,
        "text": "- The fog bell was cast from melted wedding rings."
      },
      "why": "Untagged, with no comment of its own. The carried-over request covers only the line above it, so this line has no trigger."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 12,
        "text": "- The fog bell was cast from melted wedding rings."
      },
      "ask": "Your carried-over request said \"everything about the fog bell goes into idea-lighthouse, tagged or not\", but it is recorded for the line about the bell ringing only, so this line didn't move. Should it go into idea-lighthouse under The fog bell too?"
    }
  ],
  "could_not": []
}
```

### Reply

```text
Batch b1 is done: one unit migrated, one line left in place and one question for the writer.

- **Migrated (u1):** brain-dump.md line 10, "The fog bell rings on its own the night before every drowning.", went into `Ideas/idea-lighthouse.md` under a new `## The fog bell` heading. The trigger was the writer's request carried over from the 2026-10-21 run, which covers only the line above it. The line had no tag, so it stays tentative.
- **Left in place:** line 12, "The fog bell was cast from melted wedding rings." The writer's words say "everything about the fog bell", but the carried-over comment applies only to line 10, and line 12 has no tag or comment of its own.
- **Question:** should line 12 also go into idea-lighthouse under The fog bell?
- **Could not:** nothing.

Record file: `run/unit-records.json`
```

## request-comment-24-carried-request r2: 6 of 6 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  drowning-bell-in-lighthouse  found 'drowning'
PASS  judge-record-trigger-and-scope   1. Unit u1 copies the drowning line into idea-lighthouse. Its `copies` has `"note": "Ideas/idea-lighthouse.md"` with the line `"- The fog bell rings on its own the night before every drowning."`. 2. u1's trigger has `"kind": "comment"`. Its `text` holds the request comment's words: `"[AGENT] Your request from the migration run of 2026-10-21, for this line: \"everything about the fog bell goes int
PASS  no-wedding-rings-in-lighthouse  no match
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-lighthouse.md work/project/Ideas/idea-lighthouse.md
--- before/project/Ideas/idea-lighthouse.md	2026-10-23 15:14:28
+++ work/project/Ideas/idea-lighthouse.md	2026-10-23 15:14:56
@@ -8,3 +8,7 @@
 ## The lamp
 
 - The lamp uses whale oil, which the town can no longer afford.
+
+## The fog bell
+
+- The fog bell rings on its own the night before every drowning.
```

### Unit record

```json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "[AGENT] Your request from the migration run of 2026-10-21, for this line: \"everything about the fog bell goes into idea-lighthouse, tagged or not\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The fog bell rings on its own the night before every drowning."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-lighthouse.md",
          "under": "# Idea - Lighthouse",
          "lines": [
            "## The fog bell",
            "- The fog bell rings on its own the night before every drowning."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The writer's carried-over request routes the line above it to idea-lighthouse. The source is untagged, so the copy stays untagged (tentative) under a new fog bell heading beside the existing lamp cluster."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 12,
        "text": "- The fog bell was cast from melted wedding rings."
      },
      "why": "Untagged, and the carried-over request applies only to the line directly above it (line 10), so nothing triggers this line's migration."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 12,
        "text": "- The fog bell was cast from melted wedding rings."
      },
      "ask": "Your carried-over request said \"everything about the fog bell goes into idea-lighthouse, tagged or not\", but it was recorded for the line above only. Should this wedding-rings line go to idea-lighthouse under The fog bell too?"
    }
  ],
  "could_not": []
}
```

### Reply

```text
I moved one line in batch b1, left one in place, and have one question for you.

- **Moved (1):** "The fog bell rings on its own the night before every drowning." (`brain-dump.md`, line 10) is now in `Ideas/idea-lighthouse.md` under a new `## The fog bell` heading. Your request from the 2026-10-21 run sent it there. It had no tag, so it went across untagged, as tentative.
- **Left in place (1):** "The fog bell was cast from melted wedding rings." (line 12) has no tag. Your carried-over request covers only the line directly above it, so nothing told me to move this one.
- **Question (1):** Your request said "everything about the fog bell goes into idea-lighthouse, tagged or not," which sounds like it includes the wedding-rings line. Should that line go under The fog bell too?

Nothing was left undone, and I made no changes in `brain-dump.md`.

Record file: `run/unit-records.json`
```

## request-comment-24-carried-request r3: 6 of 6 checks

### Grades

```text
PASS  brain-dump-no-edit  0 Edit call(s) matching /brain-dump\.md/
PASS  brain-dump-no-write  0 Write call(s) matching /brain-dump\.md/
PASS  drowning-bell-in-lighthouse  found 'drowning'
PASS  judge-record-trigger-and-scope   1. Unit `u1` copies the drowning line into idea-lighthouse. Its `copies` entry has `"note": "Ideas/idea-lighthouse.md"`, and its `lines` include `"- The fog bell rings on its own the night before every drowning."`. 2. That unit's `trigger` has `"kind": "comment"`. Its `"text"` is `"[AGENT] Your request from the migration run of 2026-10-21, for this line: \"everything about the fog bell goes into 
PASS  no-wedding-rings-in-lighthouse  no match
PASS  record-check  all checks pass
```

### Note changes

```diff
diff -ru before/project/Ideas/idea-lighthouse.md work/project/Ideas/idea-lighthouse.md
--- before/project/Ideas/idea-lighthouse.md	2026-10-23 15:14:28
+++ work/project/Ideas/idea-lighthouse.md	2026-10-23 15:14:49
@@ -8,3 +8,7 @@
 ## The lamp
 
 - The lamp uses whale oil, which the town can no longer afford.
+
+## The fog bell
+
+- The fog bell rings on its own the night before every drowning.
```

### Unit record

```json
{
  "units": [
    {
      "id": "u1",
      "action": "migrate",
      "trigger": {
        "kind": "comment",
        "text": "[AGENT] Your request from the migration run of 2026-10-21, for this line: \"everything about the fog bell goes into idea-lighthouse, tagged or not\""
      },
      "sources": [
        {
          "note": "brain-dump.md",
          "line": 10,
          "text": "- The fog bell rings on its own the night before every drowning."
        }
      ],
      "copies": [
        {
          "note": "Ideas/idea-lighthouse.md",
          "under": "# Idea - Lighthouse",
          "lines": [
            "## The fog bell",
            "- The fog bell rings on its own the night before every drowning."
          ]
        }
      ],
      "edits": [],
      "status": "tentative",
      "status_from": "default",
      "why": "The carried-over request, which covers the line above it, routes the fog bell material to idea-lighthouse. The source is untagged, so the copy stays untagged and tentative, under a new fog bell heading beside the lamp cluster."
    }
  ],
  "left_in_place": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 12,
        "text": "- The fog bell was cast from melted wedding rings."
      },
      "why": "The carried-over request applies only to the line above it (line 10). This line has no tag or comment of its own, so nothing triggers its migration."
    }
  ],
  "questions": [
    {
      "source": {
        "note": "brain-dump.md",
        "line": 12,
        "text": "- The fog bell was cast from melted wedding rings."
      },
      "ask": "Your carried-over request said \"everything about the fog bell goes into idea-lighthouse\", but it applies only to the line it sits under. Should this wedding-rings line also go into idea-lighthouse, under The fog bell?"
    }
  ],
  "could_not": []
}
```

### Reply

```text
I finished batch b1, round 0: I migrated one line, left one line where it was, and have one question for you.

- **Migrated (u1):** "The fog bell rings on its own the night before every drowning." (`brain-dump.md` line 10) now sits in `Ideas/idea-lighthouse.md`, under a new `## The fog bell` heading after the lamp section. Your request carried over from the 2026-10-21 run sent it there. The line had no tag, so the copy has none either and stays tentative.
- **Left in place:** "The fog bell was cast from melted wedding rings." (line 12) did not move. Your request said "everything about the fog bell," but a carried-over request applies only to the line directly above it, and this line has no tag or comment of its own.
- **Question:** Should the wedding-rings line also go into `idea-lighthouse` under The fog bell? If yes, it can move on a later run.

I didn't write anything in `brain-dump.md`. The record is at `run/unit-records.json`.
```
