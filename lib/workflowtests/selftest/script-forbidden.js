export const meta = {
  name: 'selftest-forbidden',
  description: 'Uses a call the Workflow tool throws on. The harness must refuse it.',
}

const started = Date.now()
return [{ request: 'r1', outcome: 'passed', note: null, reason: null, started }]
