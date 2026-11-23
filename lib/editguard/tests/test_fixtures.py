"""Runs `editguard check` on every fixture folder and compares its flags with expected-flags.json.

The fixtures and their expected flags were written from spec-edit-guard.md alone, not from the code.
Each expected-flags.json lists every flag the full spec would raise, for all 12 rules. The test keeps
only the rules built so far, so the expected files stay valid as later milestones add rules.
"""
import json
import subprocess
from collections import Counter
from pathlib import Path

import pytest

# Each milestone adds the rules it builds. Milestone 3: compare and explain.
IMPLEMENTED_RULES = {"unexplained-change", "link-line-invalid", "close-invalid", "unexpected-research-note",
                     "fingerprint-changed", "copy-mismatch", "pointer-mismatch", "writer-line-edited",
                     "brain-dump-status-tag", "area-note-status-tag", "rejected-move-changed", "agent-line-added"}
# Features beyond single rules. "second-pass": cases with "pass": 2 in case.json (Milestone 6).
IMPLEMENTED_FEATURES = {"second-pass"}

TESTS_DIR = Path(__file__).resolve().parent
FIXTURES_DIR = TESTS_DIR / "fixtures"
PLUGIN_ROOT = TESTS_DIR.parents[2]
EDITGUARD = PLUGIN_ROOT / "bin" / "editguard"

CASES = sorted(p for p in FIXTURES_DIR.iterdir() if p.is_dir()) if FIXTURES_DIR.is_dir() else []


def build_args(case_dir: Path, out: Path) -> list[str]:
    case = json.loads((case_dir / "case.json").read_text())
    runs = case_dir / "runs"
    args = [
        str(EDITGUARD), "check",
        "--kind", case["kind"],
        "--project", str(case_dir / "Lighthouse"),
        "--snapshot", str(case_dir / "snapshot"),
    ]
    if case["kind"] == "migration":
        records = sorted((runs / "units").glob("*.json"))
        args += ["--records", *[str(r) for r in records]]
        args += ["--run-state", str(runs / "run-state.json"), "--run-id", case["run_id"]]
        args += ["--fingerprints", str(runs / "fingerprints.json")]
    else:
        args += [
            "--requests", str(runs / "requests.json"),
            "--outcomes", str(runs / "outcomes.json"),
            "--fingerprints", str(runs / "fingerprints.json"),
        ]
    if case.get("pass") == 2:
        args += [
            "--judged", str(runs / "flags-judged.json"),
            "--findings", str(runs / "findings-flags.json"),
        ]
    args += ["--out", str(out)]
    return args


def key(flag: dict) -> tuple:
    return (flag["rule"], flag["note"], flag["before"], flag["after"], flag["unit"])


def readable(flags) -> str:
    if not flags:
        return "    (none)"
    return "\n".join(
        f"    {f['rule']} | {f['note']} | unit={f['unit']!r}\n"
        f"        before: {f['before']!r}\n"
        f"        after:  {f['after']!r}"
        for f in sorted(flags, key=key)
    )


@pytest.mark.parametrize("case_dir", CASES, ids=[c.name for c in CASES])
def test_fixture(case_dir: Path, tmp_path: Path):
    case = json.loads((case_dir / "case.json").read_text())
    if case.get("pass") == 2 and "second-pass" not in IMPLEMENTED_FEATURES:
        pytest.skip("second pass not built yet (IMPLEMENTED_FEATURES)")
    out = tmp_path / "flags-1.json"
    result = subprocess.run(build_args(case_dir, out), capture_output=True, text=True)
    assert result.returncode == 0, (
        f"editguard exited {result.returncode}\nstdout: {result.stdout}\nstderr: {result.stderr}"
    )

    actual = [f for f in json.loads(out.read_text()) if f["rule"] in IMPLEMENTED_RULES]
    expected = [
        f for f in json.loads((case_dir / "expected-flags.json").read_text())
        if f["rule"] in IMPLEMENTED_RULES
    ]

    if Counter(map(key, actual)) != Counter(map(key, expected)):
        about = json.loads((case_dir / "case.json").read_text())["about"]
        pytest.fail(
            f"{case_dir.name}: flags differ (rules compared: {sorted(IMPLEMENTED_RULES)})\n"
            f"  about: {about}\n"
            f"  expected:\n{readable(expected)}\n"
            f"  actual:\n{readable(actual)}",
            pytrace=False,
        )
