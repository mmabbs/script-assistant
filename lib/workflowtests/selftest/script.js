export const meta = {
  name: 'selftest',
  description: 'Stand-in workflow for the harness self-test. Not part of the plugin.',
}

// Same schemas as references/research-answer-shapes.json, underscore keys removed.
const researcherSchema = {
  type: 'object',
  properties: {
    result: {
      type: 'string',
      enum: ['found', 'none', 'failed'],
      description: 'found: the findings file is written. none or failed: no file was written.',
    },
  },
  required: ['result'],
}
// args.bad_schema drops "additionalProperties", so the harness must catch the mismatch.
if (!args.bad_schema) researcherSchema.additionalProperties = false

const writerSchema = {
  type: 'object',
  properties: {
    note: {
      type: 'string',
      description: 'The note\'s path inside the project folder, such as Research/research-memory-extraction.md.',
    },
  },
  required: ['note'],
  additionalProperties: false,
}

phase('research')

const results = await pipeline(
  args.requests,
  // Stage 1: one researcher per topic, side by side. A null answer is retried once under the same label.
  async (_prev, req) => {
    const found = await parallel(args.topics.map((n) => async () => {
      const call = () => agent(`Research topic ${n}. Plan: ${args.project}/llm-files/research-plans/research-plan-x.md`, {
        label: `topic ${req.id} ${n}`,
        agentType: 'script-asst:researcher',
        schema: researcherSchema,
      })
      const first = await call()
      return first === null ? await call() : first
    }))
    log(`${req.id}: ${found.length} topics done`)
    return { req, ok: found.filter((a) => a && a.result === 'found').length }
  },
  // Stage 2: the writer runs only after every researcher for the request has finished.
  async (prev) => {
    const id = prev.req.id
    if (prev.ok === 0) return { request: id, outcome: 'failed', note: null, reason: 'no topic produced findings' }
    const w = await agent(`Write the note for ${id}.`, {
      label: `write ${id}`,
      agentType: 'script-asst:research-writer',
      schema: writerSchema,
    })
    if (w === null) return { request: id, outcome: 'failed', note: null, reason: 'the writer returned nothing' }
    return { request: id, outcome: 'passed', note: w.note, reason: null }
  },
)

return results
