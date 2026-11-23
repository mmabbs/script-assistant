export const meta = {
  name: 'research',
  description:
    'Research for the writer\'s - [r] requests: a research-planner per request, researchers per topic in rounds, then a research-writer and a research-evaluator with one fix round. Returns one outcome per request.',
  whenToUse:
    'Called by the Run manager from the copy runmanager start writes to .runs/research.js, never by the writer directly. Requires args {project, run_id, requests: [{id, note, line, text, comment}]}, as runmanager start writes them to requests.json. Returns [{request, outcome, note, reason, failed_topics}].',
  phases: [
    { title: 'Plan', detail: 'one research-planner per request, one after another' },
    { title: 'Research', detail: 'one researcher per topic, in rounds; requests side by side; at most 15 per request' },
    { title: 'Write', detail: 'the research-writer turns the findings into the research note, and fixes it once if it fails' },
    { title: 'Check', detail: 'the research-evaluator checks each draft against the plan and findings' },
  ],
}

// The Research workflow. Design: spec-research-workflow.md.
// Fake-agent tests: lib/workflowtests/ (CONTRACT.md and cases/).
// The script passes paths and short answers only. It can't read files.

// The four answer shapes, copied from references/research-answer-shapes.json
// with every "_" key removed. Keep them in step with that file.

const PLANNER_SCHEMA = {
  "type": "object",
  "properties": {
    "research_topic": {
      "type": "string",
      "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$",
      "description": "The {research-topic} slug. The plan file and the note use the same one."
    },
    "topics": {
      "type": "array",
      "minItems": 1,
      "description": "One entry per topic, in plan order. No maximum here: the script enforces the cap of 15.",
      "items": {
        "type": "object",
        "properties": {
          "n": {
            "type": "integer",
            "minimum": 1
          },
          "waits_on": {
            "type": "array",
            "items": {
              "type": "integer",
              "minimum": 1
            },
            "description": "Topic numbers this topic waits on. Empty when it waits on nothing."
          }
        },
        "required": [
          "n",
          "waits_on"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "research_topic",
    "topics"
  ],
  "additionalProperties": false
}

const RESEARCHER_SCHEMA = {
  "type": "object",
  "properties": {
    "result": {
      "type": "string",
      "enum": [
        "found",
        "none",
        "failed"
      ],
      "description": "found: the findings file is written. none or failed: no file was written."
    }
  },
  "required": [
    "result"
  ],
  "additionalProperties": false
}

const WRITER_SCHEMA = {
  "type": "object",
  "properties": {
    "note": {
      "type": "string",
      "description": "The note's path inside the project folder, such as Research/research-memory-extraction.md."
    }
  },
  "required": [
    "note"
  ],
  "additionalProperties": false
}

const EVALUATOR_SCHEMA = {
  "type": "object",
  "properties": {
    "verdict": {
      "type": "string",
      "enum": [
        "pass",
        "fail"
      ]
    },
    "problems": {
      "type": "array",
      "description": "Empty on a pass.",
      "items": {
        "type": "object",
        "properties": {
          "check": {
            "type": "string",
            "enum": [
              "matches findings",
              "coverage",
              "nothing dropped"
            ],
            "description": "matches findings: a claim or footnote doesn't match the findings. coverage: a plan question is neither answered nor listed under Open Research Questions. nothing dropped: a finding that answers a plan question is missing from the note."
          },
          "where": {
            "type": "string"
          },
          "detail": {
            "type": "string"
          }
        },
        "required": [
          "check",
          "where",
          "detail"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "verdict",
    "problems"
  ],
  "additionalProperties": false
}

// ---------------------------------------------------------------- settings

const CAP = 15 // researchers per request (spec 09)
const TRIES = 3 // each agent: the first try and two retries (spec 04 item 13)

const project = String(args.project ?? '').replace(/\/+$/, '')
const runId = String(args.run_id ?? '')
const requests = Array.isArray(args.requests) ? args.requests : []

// The script lives outside the plugin's workflows/ folder, so it is no slash
// command. If it's ever run without the Run manager's args, it stops here and
// starts no agent: nothing would be marked, linked, or checked.
if (!project || !runId || requests.length === 0) {
  log('The Research workflow runs only inside a research run. Start one with /script-asst:run research N.')
  return []
}

const dateMatch = runId.match(/^run-(\d{4}-\d{2}-\d{2})/)
const runDate = dateMatch ? dateMatch[1] : runId
if (!dateMatch) log(`Could not read a run date from the run id "${runId}". Handing the run id itself as the run date.`)

// ---------------------------------------------------------------- paths (CONTRACT.md 6 item 1)

const abs = (rel) => (String(rel).startsWith('/') ? String(rel) : `${project}/${rel}`)
const planPath = (topic) => `${project}/llm-files/research-plans/research-plan-${topic}.md`
const findingsPath = (topic, n) => `${project}/llm-files/research-findings/${runId}/${topic}/topic-${n}.md`
const draftPath = (topic) => `${project}/llm-files/research-findings/${runId}/${topic}/draft-1.md`
const templatePath = `${project}/Research/research-{research-topic}.md`

// ---------------------------------------------------------------- tries

// Calls one agent up to TRIES times. A null return, a thrown error, or an
// answer isFailedTry() rejects is a failed try. Returns the first good
// answer, or null when every try failed.
async function withTries(prompt, opts, isFailedTry) {
  for (let i = 1; i <= TRIES; i++) {
    let answer = null
    try {
      answer = await agent(prompt, opts)
    } catch (e) {
      log(`${opts.label}: try ${i} of ${TRIES} threw: ${e && e.message ? e.message : e}`)
      continue
    }
    if (answer === null || answer === undefined) {
      log(`${opts.label}: try ${i} of ${TRIES} returned nothing`)
      continue
    }
    const why = isFailedTry ? isFailedTry(answer) : null
    if (why) {
      log(`${opts.label}: try ${i} of ${TRIES} failed: ${why}`)
      continue
    }
    return answer
  }
  return null
}

const outcome = (request, kind, note, reason, failedTopics) => ({
  request,
  outcome: kind,
  note: note ?? null,
  reason: kind === 'failed' ? reason : null,
  failed_topics: failedTopics,
})

// ---------------------------------------------------------------- planning

function plannerPrompt(req, taken) {
  return [
    'Plan the research for one request.',
    '',
    `Run id: ${runId}`,
    `Project folder: ${project}`,
    `Request id: ${req.id}`,
    `The note it sits in: ${abs(req.note)}`,
    `Line: ${req.line}`,
    `Request line: ${req.text}`,
    `Writer's comment: ${req.comment ?? 'none'}`,
    `Research topics already taken in this run: ${taken.length ? taken.join(', ') : 'none'}`,
    '',
    `Save the plan as ${project}/llm-files/research-plans/research-plan-{research-topic}.md. Answer with the schedule.`,
  ].join('\n')
}

// Runs one request's research-planner. Returns { schedule } or { reason }.
async function plan(req, taken) {
  const label = `plan ${req.id}`
  const schedule = await withTries(
    plannerPrompt(req, taken),
    { label, agentType: 'script-asst:research-planner', phase: 'Plan', schema: PLANNER_SCHEMA },
    (a) => {
      if (typeof a.research_topic !== 'string' || !Array.isArray(a.topics) || a.topics.length === 0) return 'the schedule is incomplete'
      if (taken.includes(a.research_topic)) return `research topic "${a.research_topic}" is already taken in this run`
      return null
    },
  )
  if (!schedule) return { reason: `The research-planner gave no usable schedule after ${TRIES} tries.` }
  return { schedule }
}

// ---------------------------------------------------------------- research rounds

function researcherPrompt(topic, n, waitsOnPaths) {
  const lines = [
    `Research topic ${n} of the plan.`,
    '',
    `Plan: ${planPath(topic)}`,
    `Your topic number: ${n}`,
    `Write your findings file to: ${findingsPath(topic, n)}`,
    `Run date: ${runDate}`,
  ]
  if (waitsOnPaths.length) {
    lines.push('', 'Findings files of the topics yours waits on:')
    for (const p of waitsOnPaths) lines.push(`- ${p}`)
  }
  return lines.join('\n')
}

// One researcher with its tries. Returns 'found', 'none', or 'failed'.
async function research(req, topic, n, waitsOn) {
  const answer = await withTries(
    researcherPrompt(topic, n, waitsOn.map((w) => findingsPath(topic, w))),
    { label: `topic ${req.id} ${n}`, agentType: 'script-asst:researcher', phase: 'Research', schema: RESEARCHER_SCHEMA },
    (a) => {
      if (a.result === 'failed') return 'it answered failed'
      if (a.result !== 'found' && a.result !== 'none') return `unknown answer ${JSON.stringify(a.result)}`
      return null
    },
  )
  return answer ? answer.result : 'failed'
}

// Runs every topic of one schedule in rounds. Returns a map n -> status:
// found, none, failed, skipped-none (skipped only because of a none),
// skipped (any other cause), or over-cap.
async function runTopics(req, schedule) {
  const topic = schedule.research_topic
  const status = new Map()
  const waits = new Map()
  const order = []
  for (const t of schedule.topics) {
    if (waits.has(t.n)) {
      log(`${req.id}: the schedule lists topic ${t.n} twice. Using its first entry.`)
      continue
    }
    waits.set(t.n, [...new Set(t.waits_on ?? [])])
    order.push(t.n)
  }

  // The cap (spec 09): the first 15 in plan order run; the rest never start.
  for (const n of order.slice(CAP)) {
    status.set(n, 'over-cap')
    log(`${req.id}: topic ${n} is over the cap of ${CAP} researchers and will not run.`)
  }

  const settled = (n) => status.has(n) || !waits.has(n)
  const hasFile = (n) => status.get(n) === 'found'
  let round = 0
  for (;;) {
    const pending = order.filter((n) => !status.has(n))
    if (pending.length === 0) break

    // A topic whose prerequisite has no findings file is skipped (spec 04 item 15).
    // Skips can chain, so repeat until nothing more is skipped.
    let skippedSome = true
    while (skippedSome) {
      skippedSome = false
      for (const n of order) {
        if (status.has(n)) continue
        const pre = waits.get(n)
        if (pre.every(settled) && !pre.every(hasFile)) {
          // A skip caused only by a none, directly or down a chain of such skips,
          // counts like a none (writer's ruling, 2026-10-12).
          const missing = pre.filter((w) => !hasFile(w))
          const onlyNone = missing.every((w) => status.get(w) === 'none' || status.get(w) === 'skipped-none')
          status.set(n, onlyNone ? 'skipped-none' : 'skipped')
          skippedSome = true
          log(`${req.id}: topic ${n} is skipped: a topic it waits on has no findings file.`)
        }
      }
    }

    const ready = order.filter((n) => !status.has(n) && waits.get(n).every(hasFile))
    if (ready.length === 0) {
      // Whatever is left waits on itself or on a loop of topics, so it can never run.
      for (const n of order) {
        if (!status.has(n)) {
          status.set(n, 'skipped')
          log(`${req.id}: topic ${n} is skipped: what it waits on can never finish.`)
        }
      }
      break
    }

    round++
    log(`${req.id}: research round ${round}: topic${ready.length > 1 ? 's' : ''} ${ready.join(', ')}.`)
    const results = await parallel(ready.map((n) => () => research(req, topic, n, waits.get(n))))
    ready.forEach((n, i) => status.set(n, results[i] ?? 'failed'))
  }
  return { status, order }
}

// ---------------------------------------------------------------- the note

function writerPrompt(topic, found) {
  return [
    'Write the research note for one request.',
    '',
    `Run date: ${runDate}`,
    `Project folder: ${project}`,
    `Plan: ${planPath(topic)}`,
    `Template copy: ${templatePath}`,
    'Findings files:',
    ...found.map((n) => `- ${findingsPath(topic, n)}`),
  ].join('\n')
}

const problemLines = (problems) =>
  problems.length
    ? problems.map((p, i) => `${i + 1}. [${p.check}] Where: ${p.where}. What is wrong: ${p.detail}`)
    : ['(The research-evaluator listed none.)']

function fixPrompt(topic, found, note, problems) {
  return [
    'Fix round. The research-evaluator failed the note.',
    'Before you change anything, copy the note unchanged to the draft-1.md path below. Then fix each problem below in the note, in place.',
    '',
    `Note: ${abs(note)}`,
    `Copy the note to: ${draftPath(topic)}`,
    `Run date: ${runDate}`,
    `Project folder: ${project}`,
    `Plan: ${planPath(topic)}`,
    `Template copy: ${templatePath}`,
    'Findings files:',
    ...found.map((n) => `- ${findingsPath(topic, n)}`),
    '',
    'Problems:',
    ...problemLines(problems),
  ].join('\n')
}

function evaluatorPrompt(topic, found, note) {
  return [
    'Check one research note against its plan and findings files.',
    '',
    `Plan: ${planPath(topic)}`,
    'Findings files:',
    ...found.map((n) => `- ${findingsPath(topic, n)}`),
    `Note: ${abs(note)}`,
  ].join('\n')
}

// The scoped re-check (spec 04 item 5).
function recheckPrompt(topic, found, note, problems) {
  return [
    'Re-check one research note after its fix round.',
    'Judge only what the fix round changed, found by comparing the note with draft-1.md, plus whether each of the first check\'s problems below was fixed.',
    '',
    `Plan: ${planPath(topic)}`,
    'Findings files:',
    ...found.map((n) => `- ${findingsPath(topic, n)}`),
    `Note: ${abs(note)}`,
    `draft-1.md, the note before the fix round: ${draftPath(topic)}`,
    '',
    'First check\'s problems:',
    ...problemLines(problems),
  ].join('\n')
}

const writerOpts = (label) => ({ label, agentType: 'script-asst:research-writer', phase: 'Write', schema: WRITER_SCHEMA })
const evaluatorOpts = (label) => ({ label, agentType: 'script-asst:research-evaluator', phase: 'Check', schema: EVALUATOR_SCHEMA })

// ---------------------------------------------------------------- one request, after planning

async function finishRequest(req, schedule) {
  const r = req.id
  const topic = schedule.research_topic
  const { status, order } = await runTopics(req, schedule)

  const failed = new Map() // n -> failed_topics text
  for (const n of order) {
    const s = status.get(n)
    if (s === 'failed') failed.set(n, `topic ${n} (failed after retries)`)
    else if (s === 'over-cap') failed.set(n, `topic ${n} (over the cap)`)
    else if (s === 'skipped' || s === 'skipped-none') failed.set(n, `topic ${n} (skipped: a topic it waits on found nothing)`)
  }
  // Topics that really failed: every failed_topics entry except a skip caused only by a none.
  const realFailures = order.filter((n) => failed.has(n) && status.get(n) !== 'skipped-none').length
  const failedTopics = () => [...failed.keys()].sort((a, b) => a - b).map((n) => failed.get(n))
  const found = order.filter((n) => status.get(n) === 'found').sort((a, b) => a - b)

  if (found.length === 0) {
    if (realFailures === 0) {
      log(`${r}: every topic came back with nothing. No note.`)
      return outcome(r, 'no findings', null, null, failedTopics())
    }
    log(`${r}: nothing was found, and ${realFailures} topic${realFailures > 1 ? 's' : ''} failed. No note.`)
    return outcome(r, 'failed', null, `Nothing was found, and ${realFailures} topic${realFailures > 1 ? 's' : ''} failed.`, failedTopics())
  }

  // First draft.
  log(`${r}: writing the note from topic${found.length > 1 ? 's' : ''} ${found.join(', ')}.`)
  const draft = await withTries(writerPrompt(topic, found), writerOpts(`write ${r}`))
  if (!draft) return outcome(r, 'failed', null, `The research-writer gave no answer after ${TRIES} tries.`, failedTopics())
  let note = draft.note
  if (!note) return outcome(r, 'failed', null, 'The research-writer wrote no note.', failedTopics())

  // First check.
  const check = await withTries(evaluatorPrompt(topic, found, note), evaluatorOpts(`check ${r}`))
  if (!check) return outcome(r, 'failed', note, `The research-evaluator gave no answer after ${TRIES} tries.`, failedTopics())
  if (check.verdict === 'pass') {
    log(`${r}: the note passed.`)
    return outcome(r, 'passed', note, null, failedTopics())
  }

  // One fix round (spec 04 item 5).
  const problems = check.problems ?? []
  log(`${r}: the note failed the check with ${problems.length} problem${problems.length === 1 ? '' : 's'}. One fix round.`)
  const fix = await withTries(fixPrompt(topic, found, note, problems), writerOpts(`fix ${r}`))
  if (!fix) return outcome(r, 'failed', note, `The research-writer's fix round gave no answer after ${TRIES} tries.`, failedTopics())
  if (fix.note) note = fix.note

  const recheck = await withTries(recheckPrompt(topic, found, note, problems), evaluatorOpts(`recheck ${r}`))
  if (!recheck) return outcome(r, 'failed', note, `The research-evaluator's second check gave no answer after ${TRIES} tries.`, failedTopics())
  if (recheck.verdict === 'pass') {
    log(`${r}: the note passed after the fix round.`)
    return outcome(r, 'passed', note, null, failedTopics())
  }
  // The first line is the plain cause; the run log turns each later line into a nested bullet.
  const left = (recheck.problems ?? []).map((p) => `${p.check}, at ${p.where}: ${p.detail}`.replace(/\s*\n\s*/g, " "))
  log(`${r}: the note failed again after the fix round.`)
  return outcome(r, 'failed', note, ['The note failed the second check after the fix round.', ...left].join('\n'), failedTopics())
}

// ---------------------------------------------------------------- the run

if (requests.length === 0) {
  log('No requests were handed in. Nothing to do.')
  return []
}

// Planners run one after another, each handed the names already taken.
phase('Plan')
const taken = []
const planned = []
for (const req of requests) {
  log(`${req.id}: planning.`)
  const p = await plan(req, taken)
  if (p.schedule) {
    taken.push(p.schedule.research_topic)
    log(`${req.id}: research topic "${p.schedule.research_topic}", ${p.schedule.topics.length} topic${p.schedule.topics.length === 1 ? '' : 's'}.`)
  } else {
    log(`${req.id}: ${p.reason}`)
  }
  planned.push({ req, ...p })
}

// Then each request researches, writes, and checks, side by side.
phase('Research')
const results = await parallel(
  planned.map(({ req, schedule, reason }) => async () => {
    if (!schedule) return outcome(req.id, 'failed', null, reason, [])
    try {
      return await finishRequest(req, schedule)
    } catch (e) {
      return outcome(req.id, 'failed', null, `The workflow script hit an error: ${e && e.message ? e.message : e}`, [])
    }
  }),
)

return planned.map(({ req }, i) =>
  results[i] ?? outcome(req.id, 'failed', null, 'The workflow script lost this request\'s outcome.', []),
)
