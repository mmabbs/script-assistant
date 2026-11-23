"""Direct tests for the skeleton: init, status, the missing run state, the lock, the step check,
the whole-note write, and the case runner itself (on the cases in runner_selftest/)."""
import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

from runmanager import lines, state
from runmanager.tests.test_cases import RUNMANAGER, run_case

SELFTEST = Path(__file__).parent / "runner_selftest"
EMPTY = {"open_run": None, "history": [], "handled": [], "unit_index": []}


@pytest.fixture
def project(tmp_path):
    p = tmp_path / "Demo"
    p.mkdir()
    return p


@pytest.fixture(autouse=True)
def clock(monkeypatch):
    monkeypatch.setenv("RUNMANAGER_NOW", "2026-10-10 16:00")


def cli(*args):
    return subprocess.run([str(RUNMANAGER), *map(str, args)], capture_output=True, text=True)


# ---- init

def test_init_creates_the_run_state(project):
    done = cli("init", "--project", project)
    assert done.returncode == 0
    assert json.loads((project / ".runs" / "run-state.json").read_text()) == EMPTY


def test_init_refuses_when_a_run_state_exists(project):
    cli("init", "--project", project)
    before = (project / ".runs" / "run-state.json").read_text()
    done = cli("init", "--project", project)
    assert done.returncode == 1
    assert "already exists" in done.stderr
    assert (project / ".runs" / "run-state.json").read_text() == before


def test_init_refuses_a_missing_project_folder(tmp_path):
    done = cli("init", "--project", tmp_path / "nope")
    assert done.returncode == 1
    assert "does not exist" in done.stderr
    assert not (tmp_path / "nope").exists()


def test_init_writes_no_settings(project):
    done = cli("init", "--project", project)
    assert done.returncode == 0
    assert "write rules" not in done.stdout
    assert not (project / ".claude").exists()


def test_init_leaves_the_writers_settings_alone(project):
    (project / ".claude").mkdir()
    text = json.dumps({"model": "opus", "permissions": {"allow": ["Bash(ls:*)"], "deny": ["Read(./secret)"]}})
    (project / ".claude" / "settings.json").write_text(text)
    done = cli("init", "--project", project)
    assert done.returncode == 0
    assert (project / ".claude" / "settings.json").read_text() == text


def test_init_ignores_unreadable_settings(project):
    (project / ".claude").mkdir()
    (project / ".claude" / "settings.json").write_text("{not json")
    done = cli("init", "--project", project)
    assert done.returncode == 0
    assert (project / ".claude" / "settings.json").read_text() == "{not json"
    assert (project / ".runs" / "run-state.json").exists()


# ---- status

def test_status_with_no_open_run(project):
    cli("init", "--project", project)
    done = cli("status", "--project", project)
    assert done.returncode == 0
    assert done.stdout.strip() == "no open run"


def test_status_with_an_open_run(project):
    state.init_state(str(project))
    run = state.claim_run(str(project), "research", 2)
    assert run["id"] == "run-2026-10-10-1600-research"
    done = cli("status", "--project", project)
    assert done.returncode == 0
    assert done.stdout.startswith("open run: run-2026-10-10-1600-research (research), step: started, next: ")


# ---- the missing run state

@pytest.mark.parametrize("command", ["status", "start", "mark", "act", "close", "recover"])
def test_missing_run_state_stops_every_command_but_init(project, command):
    extra = ["--kind", "research", "--run-number", "2"] if command == "start" else []
    done = cli(command, "--project", project, *extra)
    assert done.returncode == 1
    assert done.stderr.count("\n") == 1
    assert "/script-asst:run init" in done.stderr
    assert not (project / ".runs").exists()


def test_the_nonexistent_project_gives_the_init_line():
    done = cli("status", "--project", "/tmp/nonexistent")
    assert done.returncode == 1
    assert "/script-asst:run init" in done.stderr


@pytest.mark.parametrize("text", ["not json", "[]", '{"open_run": null}', '{"open_run": null, "history": 1, '
                                  '"handled": [], "unit_index": []}'])
def test_unreadable_run_state_gives_the_init_line(project, text):
    (project / ".runs").mkdir()
    (project / ".runs" / "run-state.json").write_text(text)
    done = cli("status", "--project", project)
    assert done.returncode == 1
    assert "/script-asst:run init" in done.stderr
    assert (project / ".runs" / "run-state.json").read_text() == text


def test_bad_arguments_exit_2(project):
    assert cli("start", "--project", project).returncode == 2


# ---- the lock and the step check

def test_claim_run_writes_the_open_run_in_one_step(project):
    state.init_state(str(project))
    run = state.claim_run(str(project), "research", 2)
    assert run == {"id": "run-2026-10-10-1600-research", "kind": "research", "run_number": 2, "request": None,
                   "step": "started", "next_check": None, "started": "2026-10-10 16:00"}
    assert state.load_state(str(project))["open_run"] == run


def test_claim_run_refuses_a_second_run(project):
    state.init_state(str(project))
    state.claim_run(str(project), "research", 2)
    on_disk = (project / ".runs" / "run-state.json").read_text()
    with pytest.raises(state.Refusal) as e:
        state.claim_run(str(project), "research", 3)
    assert "run-2026-10-10-1600-research" in str(e.value)
    assert "/script-asst:run recover" in str(e.value)
    assert (project / ".runs" / "run-state.json").read_text() == on_disk


def test_claim_run_refuses_without_a_run_state(project):
    with pytest.raises(state.Refusal, match="/script-asst:run init"):
        state.claim_run(str(project), "research", 2)


def test_the_clock_falls_back_to_the_system_clock(monkeypatch):
    monkeypatch.delenv("RUNMANAGER_NOW")
    assert state.now().year >= 2026


def test_a_bad_clock_value_is_refused(monkeypatch):
    monkeypatch.setenv("RUNMANAGER_NOW", "tomorrow")
    with pytest.raises(state.Refusal, match="RUNMANAGER_NOW"):
        state.now()


def test_require_step_returns_the_run_at_that_step():
    run = {"id": "run-x", "kind": "research", "step": "marked"}
    assert state.require_step({"open_run": run}, "marked") is run


def test_require_step_refuses_the_wrong_step_by_name():
    run = {"id": "run-x", "kind": "research", "step": "started"}
    with pytest.raises(state.Refusal) as e:
        state.require_step({"open_run": run}, "marked")
    assert "'started'" in str(e.value) and "'marked'" in str(e.value)
    assert "\n" not in str(e.value)


def test_require_step_refuses_when_no_run_is_open():
    with pytest.raises(state.Refusal, match="no open run"):
        state.require_step({"open_run": None}, "started")


# ---- the whole-note write

def test_write_note_whole_replaces_the_note(tmp_path):
    note = tmp_path / "idea.md"
    note.write_bytes(b"old\r\n")
    note.chmod(0o640)
    lines.write_note_whole(note, "new\r\nline two\n")
    assert note.read_bytes() == b"new\r\nline two\n"
    assert note.stat().st_mode & 0o777 == 0o640
    assert os.listdir(tmp_path) == ["idea.md"]


def test_write_note_whole_creates_a_new_note(tmp_path):
    lines.write_note_whole(tmp_path / "new.md", "héllo\n")
    assert (tmp_path / "new.md").read_text(encoding="utf-8") == "héllo\n"


def test_write_note_whole_leaves_the_note_alone_when_the_swap_fails(tmp_path, monkeypatch):
    note = tmp_path / "idea.md"
    note.write_text("old\n")

    def boom(src, dst):
        raise OSError("disk went away")
    monkeypatch.setattr(lines.os, "replace", boom)
    with pytest.raises(OSError):
        lines.write_note_whole(note, "new\n")
    assert note.read_text() == "old\n"
    assert os.listdir(tmp_path) == ["idea.md"]


# ---- the case runner, on its own self-test cases

@pytest.mark.parametrize("name", sorted(p.name for p in SELFTEST.iterdir() if p.is_dir()))
def test_runner_passes_its_selftest_cases(name, tmp_path):
    run_case(SELFTEST / name, tmp_path)


def copy_case(name, tmp_path):
    case = tmp_path / "case"
    shutil.copytree(SELFTEST / name, case)
    return case


def test_runner_fails_on_a_tree_difference(tmp_path):
    case = copy_case("01-copy-tree-delete", tmp_path)
    (case / "expected" / "tree" / "Demo" / "Ideas" / "new.md").write_text("different\n")
    with pytest.raises(AssertionError, match="new.md differs"):
        run_case(case, tmp_path / "work")


def test_runner_fails_on_a_missing_and_an_extra_file(tmp_path):
    case = copy_case("01-copy-tree-delete", tmp_path)
    shutil.move(case / "expected" / "tree" / "Demo" / "Ideas" / "new.md",
                case / "expected" / "tree" / "Demo" / "Ideas" / "other.md")
    with pytest.raises(AssertionError) as e:
        run_case(case, tmp_path / "work")
    assert "missing file Ideas/other.md" in str(e.value) and "extra file Ideas/new.md" in str(e.value)


def test_runner_fails_on_a_wrong_exit_code(tmp_path):
    case = copy_case("01-copy-tree-delete", tmp_path)
    (case / "steps.json").write_text(json.dumps([{"run": ["init"], "exit": 0}]))
    with pytest.raises(AssertionError, match="exit 1, wanted 0"):
        run_case(case, tmp_path / "work")


def test_runner_fails_on_wrong_stderr_text(tmp_path):
    case = copy_case("01-copy-tree-delete", tmp_path)
    (case / "steps.json").write_text(json.dumps([{"run": ["init"], "exit": 1, "stderr": "no such words"}]))
    with pytest.raises(AssertionError, match="stderr should contain"):
        run_case(case, tmp_path / "work")


def test_runner_fails_when_a_snapshot_should_be_gone(tmp_path):
    case = copy_case("02-log-snapshot-editguard", tmp_path)
    (case / "steps.json").write_text(json.dumps([{"editguard": True}]))
    with pytest.raises(AssertionError, match="snapshot/ should be gone"):
        run_case(case, tmp_path / "work")


@pytest.mark.parametrize("change, message", [
    ({"first_line": "Research run 9."}, "first line is"),
    ({"sections": [{"heading": "Done", "contains": ["nope"]}]}, "lacks 'nope'"),
    ({"sections": [{"heading": "Done"}, {"heading": "Requests still open"}]}, "out of order"),
    ({"absent": ["Done"]}, "should not appear"),
    ({"nothing_needs_you": True}, "Nothing needs you"),
])
def test_runner_fails_on_log_differences(tmp_path, change, message):
    case = copy_case("02-log-snapshot-editguard", tmp_path)
    log = json.loads((case / "expected" / "log.json").read_text())
    log.update(change)
    (case / "expected" / "log.json").write_text(json.dumps([log]))
    with pytest.raises(AssertionError, match=message):
        run_case(case, tmp_path / "work")
