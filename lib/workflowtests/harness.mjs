#!/usr/bin/env node
// Fake-agent test harness for Claude Code workflow scripts.
// Contract: lib/workflowtests/CONTRACT.md. Node standard library only.
//
// Usage (from the plugin root):
//   node lib/workflowtests/harness.mjs [--script FILE] [--cases DIR] [case-name ...]
// Defaults: --script lib/research.js, --cases lib/workflowtests/cases/

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { isDeepStrictEqual } from 'node:util';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PLUGIN_ROOT = path.resolve(HERE, '..', '..');
const DEFAULT_SCRIPT = path.join(PLUGIN_ROOT, 'lib', 'research.js');
const DEFAULT_CASES = path.join(HERE, 'cases');
const SHAPES_FILE = path.join(PLUGIN_ROOT, 'references', 'research-answer-shapes.json');
const CASE_TIMEOUT_MS = 10000;

const AsyncFunction = Object.getPrototypeOf(async function () {}).constructor;

// ---------------------------------------------------------------- labels (contract section 3)

const LABEL_TABLE = [
  { re: /^plan (\S+)$/, agentType: 'script-asst:research-planner', key: 'research-planner' },
  { re: /^topic (\S+) (\d+)$/, agentType: 'script-asst:researcher', key: 'researcher' },
  { re: /^write (\S+)$/, agentType: 'script-asst:research-writer', key: 'research-writer' },
  { re: /^check (\S+)$/, agentType: 'script-asst:research-evaluator', key: 'research-evaluator' },
  { re: /^fix (\S+)$/, agentType: 'script-asst:research-writer', key: 'research-writer' },
  { re: /^recheck (\S+)$/, agentType: 'script-asst:research-evaluator', key: 'research-evaluator' },
];

function stripUnderscoreKeys(v) {
  if (Array.isArray(v)) return v.map(stripUnderscoreKeys);
  if (v && typeof v === 'object') {
    const out = {};
    for (const [k, val] of Object.entries(v)) {
      if (!k.startsWith('_')) out[k] = stripUnderscoreKeys(val);
    }
    return out;
  }
  return v;
}

// ---------------------------------------------------------------- schema validator

const KNOWN_KEYWORDS = new Set([
  'type', 'properties', 'required', 'additionalProperties', 'items', 'enum',
  'minItems', 'minimum', 'pattern', 'description',
]);

function describe(v) {
  if (v === null) return 'null';
  if (Array.isArray(v)) return 'array';
  return typeof v;
}

function typeMatches(v, t) {
  switch (t) {
    case 'null': return v === null;
    case 'array': return Array.isArray(v);
    case 'object': return typeof v === 'object' && v !== null && !Array.isArray(v);
    case 'integer': return Number.isInteger(v);
    case 'number': return typeof v === 'number' && Number.isFinite(v);
    case 'string': return typeof v === 'string';
    case 'boolean': return typeof v === 'boolean';
    default: return false;
  }
}

export function validate(value, schema, at = '$') {
  const errors = [];
  for (const k of Object.keys(schema)) {
    if (!k.startsWith('_') && !KNOWN_KEYWORDS.has(k)) {
      errors.push(`${at}: harness validator does not support the schema keyword "${k}"`);
    }
  }
  if (schema.type !== undefined) {
    const types = Array.isArray(schema.type) ? schema.type : [schema.type];
    if (!types.some((t) => typeMatches(value, t))) {
      errors.push(`${at}: expected type ${types.join(' or ')}, got ${describe(value)}`);
      return errors;
    }
  }
  if (schema.enum !== undefined && !schema.enum.some((e) => isDeepStrictEqual(e, value))) {
    errors.push(`${at}: ${JSON.stringify(value)} is not one of ${JSON.stringify(schema.enum)}`);
  }
  if (schema.minimum !== undefined && typeof value === 'number' && value < schema.minimum) {
    errors.push(`${at}: ${value} is below the minimum ${schema.minimum}`);
  }
  if (schema.pattern !== undefined && typeof value === 'string' && !new RegExp(schema.pattern).test(value)) {
    errors.push(`${at}: ${JSON.stringify(value)} does not match the pattern ${schema.pattern}`);
  }
  if (Array.isArray(value)) {
    if (schema.minItems !== undefined && value.length < schema.minItems) {
      errors.push(`${at}: has ${value.length} items, needs at least ${schema.minItems}`);
    }
    if (schema.items !== undefined) {
      value.forEach((item, i) => errors.push(...validate(item, schema.items, `${at}[${i}]`)));
    }
  }
  if (typeMatches(value, 'object')) {
    for (const r of schema.required ?? []) {
      if (!Object.prototype.hasOwnProperty.call(value, r)) errors.push(`${at}: missing required key "${r}"`);
    }
    const props = schema.properties ?? {};
    for (const [k, sub] of Object.entries(props)) {
      if (Object.prototype.hasOwnProperty.call(value, k)) errors.push(...validate(value[k], sub, `${at}.${k}`));
    }
    if (schema.additionalProperties === false) {
      for (const k of Object.keys(value)) {
        if (!Object.prototype.hasOwnProperty.call(props, k)) errors.push(`${at}: unexpected key "${k}"`);
      }
    }
  }
  return errors;
}

// ---------------------------------------------------------------- forbidden-construct scan (contract section 1 item 4)

// Blank out comments, string contents and regex literals so the scan sees code only.
function stripCode(src) {
  let out = '';
  let i = 0;
  const n = src.length;
  let lastSig = '';
  const REGEX_AFTER = '(,=:[!&|?{};+-*%<>~^';
  function scan(stopAtBrace) {
    let depth = 0;
    while (i < n) {
      const c = src[i];
      const d = src[i + 1];
      if (c === '/' && d === '/') {
        while (i < n && src[i] !== '\n') i++;
        continue;
      }
      if (c === '/' && d === '*') {
        const e = src.indexOf('*/', i + 2);
        i = e < 0 ? n : e + 2;
        out += ' ';
        continue;
      }
      if (c === '"' || c === "'") {
        out += c;
        i++;
        while (i < n && src[i] !== c && src[i] !== '\n') {
          if (src[i] === '\\') i++;
          i++;
        }
        out += c;
        i++;
        lastSig = c;
        continue;
      }
      if (c === '`') {
        out += c;
        i++;
        while (i < n && src[i] !== '`') {
          if (src[i] === '\\') { i += 2; continue; }
          if (src[i] === '$' && src[i + 1] === '{') {
            i += 2;
            out += '${';
            scan(true);
            out += '}';
            continue;
          }
          i++;
        }
        out += '`';
        i++;
        lastSig = '`';
        continue;
      }
      if (c === '/' && (lastSig === '' || REGEX_AFTER.includes(lastSig))) {
        i++;
        let inClass = false;
        while (i < n && src[i] !== '\n') {
          if (src[i] === '\\') { i += 2; continue; }
          if (src[i] === '[') inClass = true;
          else if (src[i] === ']') inClass = false;
          else if (src[i] === '/' && !inClass) break;
          i++;
        }
        i++;
        while (i < n && /[a-z]/i.test(src[i])) i++;
        out += '/r/';
        lastSig = '/';
        continue;
      }
      if (stopAtBrace) {
        if (c === '{') depth++;
        else if (c === '}') {
          if (depth === 0) { i++; return; }
          depth--;
        }
      }
      out += c;
      i++;
      if (!/\s/.test(c)) lastSig = c;
    }
  }
  scan(false);
  return out;
}

const FORBIDDEN = [
  { name: 'Date.now()', re: /\bDate\s*\.\s*now\b/ },
  { name: 'Math.random()', re: /\bMath\s*\.\s*random\b/ },
  { name: 'new Date() with no argument', re: /\bnew\s+Date\s*\(\s*\)|\bnew\s+Date\b(?!\s*\()/ },
  { name: 'import', re: /\bimport\b/ },
  { name: 'require', re: /\brequire\b/ },
];

export function findForbidden(src) {
  const code = stripCode(src);
  return FORBIDDEN.filter((f) => f.re.test(code)).map((f) => f.name);
}

// ---------------------------------------------------------------- loading the script (contract section 1 item 3)

function compileScript(src) {
  const re = /^([ \t]*)export\s+const\s+meta\b/m;
  if (!re.test(src)) return { error: 'script has no "export const meta" line' };
  const body = src.replace(re, '$1const meta');
  try {
    return { fn: new AsyncFunction('agent', 'parallel', 'pipeline', 'phase', 'log', 'args', body) };
  } catch (e) {
    return { error: `script does not compile: ${e.message}` };
  }
}

// ---------------------------------------------------------------- one case

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function sortByRequest(list) {
  return [...list].sort((a, b) => {
    const x = String(a?.request);
    const y = String(b?.request);
    return x < y ? -1 : x > y ? 1 : 0;
  });
}

function compareResult(actual, expected, fail) {
  if (!Array.isArray(actual)) {
    fail(`result is not a list (got ${describe(actual)}: ${JSON.stringify(actual)})`);
    return;
  }
  if (!Array.isArray(expected)) {
    fail('broken case: expect.result must be a list');
    return;
  }
  const a = sortByRequest(actual);
  const e = sortByRequest(expected);
  if (a.length !== e.length) {
    fail(`result has ${a.length} entries, expected ${e.length}. Got ${JSON.stringify(a)}`);
    return;
  }
  e.forEach((exp, i) => {
    const act = a[i];
    const who = `result entry ${JSON.stringify(exp.request)}`;
    if (!act || typeof act !== 'object') {
      fail(`${who}: got ${JSON.stringify(act)}, expected an object`);
      return;
    }
    const { reason: expReason, reason_includes: includes, ...expRest } = exp;
    const { reason: actReason, ...actRest } = act;
    if (!isDeepStrictEqual(actRest, expRest)) {
      fail(`${who} differs (reason aside). Got ${JSON.stringify(actRest)}, expected ${JSON.stringify(expRest)}`);
    }
    if (!Object.prototype.hasOwnProperty.call(act, 'reason')) {
      fail(`${who}: the "reason" key is missing`);
    } else if (includes !== undefined) {
      if (typeof actReason !== 'string') {
        fail(`${who}: reason is ${JSON.stringify(actReason)}, expected text containing ${JSON.stringify(includes)}`);
      } else {
        for (const s of includes) {
          if (!actReason.includes(s)) fail(`${who}: reason ${JSON.stringify(actReason)} does not contain ${JSON.stringify(s)}`);
        }
      }
    } else if (expReason === null || expReason === undefined) {
      if (actReason !== null) fail(`${who}: reason is ${JSON.stringify(actReason)}, expected null`);
    } else if (typeof actReason !== 'string' || actReason === '') {
      fail(`${who}: reason is ${JSON.stringify(actReason)}, expected a reason string`);
    }
  });
}

async function runCase(caseDir, scriptPath, shapes) {
  const name = path.basename(caseDir);
  const reasons = [];
  const fail = (r) => { if (!reasons.includes(r)) reasons.push(r); };
  const result = { name, reasons, expectHarnessFail: false, expectFailIncludes: null };

  let spec;
  try {
    spec = JSON.parse(fs.readFileSync(path.join(caseDir, 'case.json'), 'utf8'));
  } catch (e) {
    fail(`case.json cannot be read: ${e.message}`);
    return result;
  }
  result.expectHarnessFail = spec.expect_harness_fail === true;
  result.expectFailIncludes = spec.expect_fail_includes ?? null;

  // Which script runs: the run's script, or this case's own (section 7).
  let scriptFile = scriptPath;
  if (typeof spec.script === 'string') scriptFile = path.resolve(caseDir, spec.script);
  let src;
  try {
    src = fs.readFileSync(scriptFile, 'utf8');
  } catch (e) {
    fail(`script cannot be read: ${scriptFile}`);
    return result;
  }

  for (const f of findForbidden(src)) fail(`script uses forbidden ${f}`);
  if (reasons.length) return result;

  const compiled = compileScript(src);
  if (compiled.error) {
    fail(compiled.error);
    return result;
  }

  // ---- state and stand-in globals
  const answers = {};
  for (const [label, list] of Object.entries(spec.answers ?? {})) answers[label] = structuredClone(list);
  const delays = spec.delay_ms ?? {};
  const calls = [];
  const events = []; // phase() and log() texts, in order
  let seq = 0;

  async function agent(prompt, opts) {
    // Everything up to the first await runs at call time, so start order is call order.
    const o = opts ?? {};
    const label = o.label;
    const call = {
      label,
      agentType: o.agentType,
      prompt,
      opts: o,
      start: ++seq,
      end: null,
      ended_before: calls.filter((c) => c.end !== null).map((c) => c.label),
    };
    calls.push(call);
    const finish = () => { call.end = ++seq; };

    if (typeof label !== 'string' || label === '') {
      fail('an agent() call has no opts.label');
      finish();
      throw new Error('agent() call with no label');
    }

    // Label and agentType form (section 3).
    let entry = null;
    for (const row of LABEL_TABLE) if (row.re.test(label)) { entry = row; break; }
    if (!entry) {
      fail(`label "${label}" is not one of the contract's label forms`);
    } else if (o.agentType !== entry.agentType) {
      fail(`${label}: agentType is ${JSON.stringify(o.agentType)}, expected ${JSON.stringify(entry.agentType)}`);
    }

    // Schema (section 3 item 2).
    const key = entry ? entry.key : String(o.agentType ?? '').replace(/^script-asst:/, '');
    if (o.schema === undefined) {
      fail(`${label}: opts.schema is missing`);
    } else if (!shapes[key]) {
      fail(`${label}: no schema on file for agent "${key}", cannot check opts.schema`);
    } else if (!isDeepStrictEqual(o.schema, stripUnderscoreKeys(shapes[key]))) {
      fail(`${label}: opts.schema does not equal the ${key} schema in references/research-answer-shapes.json (underscore keys removed)`);
    }

    // Answer (section 2 item 1).
    const queue = answers[label];
    if (!queue || queue.length === 0) {
      fail(`unexpected call ${label}`);
      finish();
      throw new Error(`unexpected call ${label}`);
    }
    const answer = queue.shift();

    const delay = delays[label] ?? 0;
    await sleep(delay);
    finish();

    if (answer === null) return null;
    if (typeof answer === 'object' && !Array.isArray(answer) && typeof answer.$throw === 'string') {
      throw new Error(answer.$throw);
    }
    if (o.schema !== undefined) {
      const errs = validate(answer, o.schema);
      if (errs.length) fail(`broken case: a set answer for ${label} fails the schema the call passed: ${errs.join('; ')}`);
    }
    return answer;
  }

  async function parallel(thunks) {
    return Promise.all(thunks.map(async (t) => {
      try { return await t(); } catch { return null; }
    }));
  }

  async function pipeline(items, ...stages) {
    return Promise.all(items.map(async (item, index) => {
      let prev = item;
      for (const stage of stages) {
        try { prev = await stage(prev, item, index); } catch { return null; }
      }
      return prev;
    }));
  }

  const phase = (title) => { events.push({ kind: 'phase', text: String(title) }); };
  const log = (message) => { events.push({ kind: 'log', text: String(message) }); };

  // ---- run
  let returned;
  let threw = null;
  let timedOut = false;
  let timer;
  const timeout = new Promise((_, reject) => {
    timer = setTimeout(() => { timedOut = true; reject(new Error(`timed out after ${CASE_TIMEOUT_MS} ms`)); }, CASE_TIMEOUT_MS);
  });
  try {
    const run = compiled.fn(agent, parallel, pipeline, phase, log, structuredClone(spec.args ?? {}));
    returned = await Promise.race([run, timeout]);
  } catch (e) {
    threw = e;
  } finally {
    clearTimeout(timer);
  }
  if (threw) fail(`script ${timedOut ? '' : 'threw: '}${threw.message}`);
  if (!threw) {
    for (const c of calls) if (c.end === null) fail(`script returned while the call ${c.label} was still running`);
  }

  // ---- checks (section 5)
  const expect = spec.expect ?? {};

  if (expect.result !== undefined && !threw) compareResult(returned, expect.result, fail);

  for (const [label, want] of Object.entries(expect.calls ?? {})) {
    const mine = calls.filter((c) => c.label === label);
    if (want.count !== undefined && mine.length !== want.count) {
      fail(`calls "${label}": ${mine.length} calls, expected ${want.count}`);
    }
    mine.forEach((c, i) => {
      for (const s of want.prompt_includes ?? []) {
        if (!String(c.prompt).includes(s)) fail(`calls "${label}": prompt of call ${i + 1} does not contain ${JSON.stringify(s)}`);
      }
      for (const s of want.prompt_excludes ?? []) {
        if (String(c.prompt).includes(s)) fail(`calls "${label}": prompt of call ${i + 1} contains ${JSON.stringify(s)}, which it must not`);
      }
    });
  }

  for (const label of expect.not_called ?? []) {
    const n = calls.filter((c) => c.label === label).length;
    if (n > 0) fail(`not_called "${label}": it was called ${n} time(s)`);
  }

  for (const [a, b] of expect.after ?? []) {
    const as = calls.filter((c) => c.label === a);
    const bs = calls.filter((c) => c.label === b);
    if (as.length === 0 || bs.length === 0) {
      fail(`after [${JSON.stringify(a)}, ${JSON.stringify(b)}]: ${as.length === 0 ? a : b} was never called, so the order cannot be checked`);
      continue;
    }
    const bad = as.some((ca) => bs.some((cb) => cb.end === null || ca.start < cb.end));
    if (bad) fail(`after [${JSON.stringify(a)}, ${JSON.stringify(b)}]: a "${a}" call started before a "${b}" call ended`);
  }

  for (const group of expect.together ?? []) {
    const firsts = group.map((label) => calls.find((c) => c.label === label));
    const missing = group.filter((_, i) => !firsts[i]);
    if (missing.length) {
      fail(`together ${JSON.stringify(group)}: never called: ${missing.join(', ')}`);
      continue;
    }
    const lastStart = Math.max(...firsts.map((c) => c.start));
    const firstEnd = Math.min(...firsts.map((c) => (c.end === null ? Infinity : c.end)));
    if (lastStart > firstEnd) fail(`together ${JSON.stringify(group)}: one call ended before all had started, so they did not run side by side`);
  }

  return result;
}

// ---------------------------------------------------------------- command line

function parseArgs(argv) {
  const opts = { script: DEFAULT_SCRIPT, cases: DEFAULT_CASES, names: [] };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === '--script' || a === '--cases') {
      const v = argv[++i];
      if (!v) throw new Error(`${a} needs a path`);
      opts[a.slice(2)] = path.resolve(process.cwd(), v);
    } else if (a.startsWith('--')) {
      throw new Error(`unknown flag ${a}`);
    } else {
      opts.names.push(a);
    }
  }
  return opts;
}

async function main() {
  let opts;
  try {
    opts = parseArgs(process.argv.slice(2));
  } catch (e) {
    console.error(`harness: ${e.message}. Usage: node lib/workflowtests/harness.mjs [--script FILE] [--cases DIR] [case-name ...]`);
    return 2;
  }

  if (!fs.existsSync(opts.script)) {
    console.error(`harness: the script under test does not exist yet: ${opts.script}`);
    return 1;
  }
  let shapes;
  try {
    shapes = JSON.parse(fs.readFileSync(SHAPES_FILE, 'utf8'));
  } catch (e) {
    console.error(`harness: cannot read the schemas file ${SHAPES_FILE}: ${e.message}`);
    return 2;
  }
  if (!fs.existsSync(opts.cases) || !fs.statSync(opts.cases).isDirectory()) {
    console.error(`harness: no cases folder at ${opts.cases}`);
    return 1;
  }
  const all = fs.readdirSync(opts.cases, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .sort();
  if (all.length === 0) {
    console.error(`harness: no cases to run, the folder is empty: ${opts.cases}`);
    return 1;
  }

  const missingNames = opts.names.filter((n) => !all.includes(n));
  const names = opts.names.length ? opts.names.filter((n) => all.includes(n)) : all;

  let allPass = true;
  const detail = [];
  for (const n of missingNames) {
    console.log(`FAIL ${n}: no such case folder in ${opts.cases}`);
    allPass = false;
  }
  for (const n of names) {
    const r = await runCase(path.join(opts.cases, n), opts.script, shapes);
    const failed = r.reasons.length > 0;
    if (r.expectHarnessFail) {
      if (!failed) {
        console.log(`FAIL ${n}: expected the harness to fail this case, but it passed`);
        allPass = false;
      } else if (r.expectFailIncludes !== null && !r.reasons.some((x) => x.includes(r.expectFailIncludes))) {
        console.log(`FAIL ${n}: the case failed, but no reason contains ${JSON.stringify(r.expectFailIncludes)}`);
        detail.push(r);
        allPass = false;
      } else {
        console.log(`PASS ${n} (failed as expected: ${r.reasons[0]})`);
      }
    } else if (failed) {
      console.log(`FAIL ${n}: ${r.reasons[0]}`);
      detail.push(r);
      allPass = false;
    } else {
      console.log(`PASS ${n}`);
    }
  }
  for (const r of detail) {
    console.log(`\nReasons for ${r.name}:`);
    r.reasons.forEach((x, i) => console.log(`  ${i + 1}. ${x}`));
  }
  return allPass ? 0 : 1;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().then((code) => process.exit(code));
}
