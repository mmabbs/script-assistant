export const meta = {
  name: 'research',
  description: 'Dry-run stand-in for the research workflow: two cheap agents in sequence. The first writes one light note at once. The second waits 3 minutes, then writes another. Returns no outcomes.',
  phases: [
    { title: 'First note', detail: 'one agent writes research-light-keeper-refusal.md' },
    { title: 'Wait, then second note', detail: 'one agent waits 3 minutes, then writes research-light-tide-tables.md' },
  ],
}

// Stand-in for lib/research.js, used only by the stop dry run (tests/dryrun-stop/).
// The hook swap-standin.py copies it over .runs/research.js right after runmanager start.
// It reads args the way lib/research.js does, and it never touches the filesystem itself.

const project = String(args.project ?? '').replace(/\/+$/, '')

const NOTE_SHAPE = `A light research note is a markdown file in this shape, in this order:
---
title: Research Light - {Title}
type: [research-light]
created: 2026-10-10
---

# {Title}

Request: {the request} (#research/run-2)

## Findings

- three to five short bullets

## Useful for the story

- two short bullets

## Open questions

- one short bullet

## Sources

- two short bullets`

await agent(
  `Write one file with the Write tool: ${project}/Research/research-light-keeper-refusal.md. ` +
  `It is a dry-run note, so invent plausible content about a 1950s lighthouse keeper. Do not search the web. ` +
  `Title "Keeper Refusal". Request: Could a lone keeper legally refuse a relief posting?\n\n${NOTE_SHAPE}\n\n` +
  `Write nothing else and run no command. Reply "done" when the file is written.`,
  { label: 'stand-in: first note', model: 'sonnet', effort: 'low' },
)

await agent(
  `Step 1. Run exactly this one command with the Bash tool, with run_in_background set to true: sleep 180\n` +
  `Do not change the command or run anything else first. Then wait for its completion notice, which comes in 3 minutes. Do nothing until it arrives.\n\n` +
  `Step 2. Then write one file with the Write tool: ${project}/Research/research-light-tide-tables.md. ` +
  `It is a dry-run note, so invent plausible content about printed tide tables in 1950s villages. Do not search the web. ` +
  `Title "Tide Tables". Request: How did printed tide tables reach small villages in the 1950s?\n\n${NOTE_SHAPE}\n\n` +
  `Write nothing else. Reply "done" when the file is written.`,
  { label: 'stand-in: wait, then second note', model: 'sonnet', effort: 'low' },
)

return []
