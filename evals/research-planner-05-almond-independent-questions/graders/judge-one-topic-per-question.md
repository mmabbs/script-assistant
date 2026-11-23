---
type: llm
focus: { source: file, path: project/llm-files/research-plans/research-plan-anxiety-contagion.md }
also: [run/answer.json]
---

The request was: - [r] Is anxiety "contagious"? It came with no comment. The text under test is the research-planner's plan for it, then its schedule, run/answer.json, which lists each topic's number and the topics it waits on.

In the first live run on this request, the plan had one topic holding these five questions:
1. what psychology calls the effect and how it is defined;
2. how anxiety passes from one person to another;
3. what studies show in different settings, such as watching someone under stress, parents and children, couples, coworkers, and crowds;
4. who catches it more easily;
5. whether "contagious" is an accurate word, and where the evidence is strong or weak.
Its one researcher could not cover them all. That plan fails this check.

How to count: for each topic, count how many of these five questions it holds, in any wording. A sub-question that only narrows or restates one of the five counts as part of that one, not as another. A topic's own "how strong is the evidence?" for its own question counts as narrowing that question, not as question 5. Question 5 counts only where a topic asks whether "contagious" is an accurate word, or where the evidence on the subject as a whole is strong or weak. Question marks are never counted.

Waiting: no topic may wait on another, with one exception. The topic that holds question 5 may wait on the topic that holds question 3, the studies, and on that topic only. A topic waits when its schedule entry lists another topic under waits_on, or when the plan tells its researcher to build on or use another topic's findings.

PASS if both hold:
1. No topic holds more than two of the five questions.
2. Either no topic waits on another, or the only wait is the question-5 topic waiting on the studies topic.

FAIL if any topic holds three or more of the five questions, or if any other wait appears: a different topic waits, the question-5 topic waits on a topic other than the studies topic, or it waits on more than one. List each topic heading with which of the five questions it holds and what it waits on, and name the topic that fails.
