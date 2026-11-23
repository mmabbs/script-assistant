"""Tests for run-permissions.py: each approved kind, and each near miss that must get no answer.

Run: python3 -m unittest discover -s hooks/scripts -p 'test_*.py'   (from the plugin folder)
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

HOOK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "run-permissions.py")
PLUGIN = os.path.realpath(os.path.join(os.path.dirname(HOOK), "..", ".."))
RULES = os.path.join(PLUGIN, "references", "migrator-rules.md")


def answer(tool, tool_input, cwd, agent=None):
    d = {"hook_event_name": "PreToolUse", "tool_name": tool, "tool_input": tool_input, "cwd": cwd,
         "permission_mode": "default"}
    if agent:
        d["agent_type"], d["agent_id"] = agent, "a123"
    out = subprocess.run([sys.executable, HOOK], input=json.dumps(d), capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    if not out.stdout.strip():
        return None
    return json.loads(out.stdout)["hookSpecificOutput"]["permissionDecision"]


class RunPermissions(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.p = os.path.join(self.tmp.name, "Lighthouse")
        os.makedirs(os.path.join(self.p, "Ideas"))
        self.outside = os.path.join(self.tmp.name, "other.md")

    def tearDown(self):
        self.tmp.cleanup()

    def note(self, *parts):
        return os.path.join(self.p, *parts)

    # Approved
    def test_migrator_edits_a_note(self):
        self.assertEqual(answer("Edit", {"file_path": self.note("Ideas", "idea-tobias.md")}, self.p,
                                "script-asst:migrator"), "allow")

    def test_migrator_writes_a_new_note_at_the_root(self):
        self.assertEqual(answer("Write", {"file_path": self.note("area-new.md")}, self.p, "script-asst:migrator"),
                         "allow")

    def test_migrator_writes_its_record(self):
        rec = self.note(".runs", "units", "run-2026-10-13-2113-migration-b1.json")
        self.assertEqual(answer("Write", {"file_path": rec}, self.p, "script-asst:migrator"), "allow")

    def test_migrator_relative_path(self):
        self.assertEqual(answer("Edit", {"file_path": "Ideas/idea-tobias.md"}, self.p, "script-asst:migrator"),
                         "allow")

    def test_agent_reads_the_rules_file(self):
        self.assertEqual(answer("Read", {"file_path": RULES}, self.p, "script-asst:migration-verifier"), "allow")

    def test_runmanager_command(self):
        self.assertEqual(answer("Bash", {"command": f"runmanager status --project {self.p}"}, self.p), "allow")

    def test_editguard_command_with_a_glob(self):
        cmd = (f"editguard check --kind migration --project {self.p} --snapshot {self.p}/.runs/r/snapshot "
               f"--records {self.p}/.runs/units/run-b*.json --run-state {self.p}/.runs/run-state.json")
        self.assertEqual(answer("Bash", {"command": cmd}, self.p), "allow")

    def test_session_saves_findings(self):
        for name in ["findings-b1-r0.json", "findings-b12-r2.json", "findings-flags.json", "outcomes.json"]:
            path = self.note(".runs", "run-2026-10-13-2147-migration", name)
            self.assertEqual(answer("Write", {"file_path": path}, self.p), "allow", name)

    def test_research_agents_write_in_their_folders(self):
        cases = [("script-asst:research-planner", ("llm-files", "research-plans", "research-plan-fog.md")),
                 ("script-asst:researcher", ("llm-files", "research-findings", "run-2026-10-14-1600-research",
                                             "fog", "findings.md")),
                 ("script-asst:research-writer", ("Research", "research-fog.md"))]
        for agent, parts in cases:
            for tool in ("Write", "Edit"):
                self.assertEqual(answer(tool, {"file_path": self.note(*parts)}, self.p, agent), "allow", (agent, tool))

    def test_research_writer_writes_its_draft_copy(self):
        for tool in ("Write", "Edit"):
            path = self.note("llm-files", "research-findings", "run-2026-10-22-1000-research", "fog", "draft-1.md")
            self.assertEqual(answer(tool, {"file_path": path}, self.p, "script-asst:research-writer"), "allow", tool)

    def test_researcher_web_calls(self):
        for tool, inp in [("WebSearch", {"query": "lighthouse fog"}), ("WebFetch", {"url": "https://example.com",
                                                                                  "prompt": "summarise"})]:
            self.assertEqual(answer(tool, inp, self.p, "script-asst:researcher"), "allow", tool)

    # No answer
    def test_web_calls_from_anyone_but_the_researcher(self):
        for tool, inp in [("WebSearch", {"query": "lighthouse fog"}), ("WebFetch", {"url": "https://example.com",
                                                                                  "prompt": "summarise"})]:
            for agent in ["script-asst:research-writer", "script-asst:research-planner", "script-asst:migrator",
                          "script-asst-fake:researcher", None]:
                self.assertIsNone(answer(tool, inp, self.p, agent), (tool, agent))

    def test_research_writer_other_names_in_the_findings_folder(self):
        for name in ["topic-1.md", "draft-2.md", "draft-1.md.bak", "xdraft-1.md", "findings.md"]:
            path = self.note("llm-files", "research-findings", "run-2026-10-22-1000-research", "fog", name)
            self.assertIsNone(answer("Write", {"file_path": path}, self.p, "script-asst:research-writer"), name)
        # draft-1.md in the writer's own other folders, or outside the findings folder, gains nothing new
        for parts in [("llm-files", "research-plans", "draft-1.md"), ("llm-files", "draft-1.md"),
                      ("Ideas", "draft-1.md"), ("llm-files", "research-findings", ".hidden", "draft-1.md")]:
            self.assertIsNone(answer("Write", {"file_path": self.note(*parts)}, self.p, "script-asst:research-writer"),
                              parts)

    def test_other_agents_draft_copy_gains_nothing(self):
        path = self.note("llm-files", "research-findings", "run-2026-10-22-1000-research", "fog", "draft-1.md")
        # The researcher could already write any file in this folder, and the migrator any .md note outside the
        # dot-folders; both still can. No one else gets it.
        for agent in ["script-asst:researcher", "script-asst:migrator"]:
            self.assertEqual(answer("Write", {"file_path": path}, self.p, agent), "allow", agent)
        for agent in ["script-asst:research-planner", "script-asst:research-evaluator", None]:
            self.assertIsNone(answer("Write", {"file_path": path}, self.p, agent), agent)

    def test_research_near_misses(self):
        cases = [("script-asst:research-writer", ("Ideas", "x.md")),
                 ("script-asst:research-writer", ("llm-files", "research-plans", "x.md")),
                 ("script-asst:research-writer", ("Research", "x.sh")),
                 ("script-asst:research-writer", ("Research", ".hidden", "x.md")),
                 ("script-asst:research-planner", ("Research", "x.md")),
                 ("script-asst:research-planner", ("llm-files", "research-findings", "x.md")),
                 ("script-asst:researcher", ("Research", "x.md")),
                 ("script-asst:researcher", ("llm-files", "x.md")),
                 ("script-asst:research-evaluator", ("Research", "x.md")),
                 ("script-asst:migration-verifier", ("Research", "x.md")),
                 (None, ("Research", "x.md"))]
        for agent, parts in cases:
            self.assertIsNone(answer("Write", {"file_path": self.note(*parts)}, self.p, agent), (agent, parts))
        self.assertIsNone(answer("Write", {"file_path": self.note("Research")}, self.p, "script-asst:research-writer"))
        self.assertIsNone(answer("Write", {"file_path": os.path.join(self.tmp.name, "Research", "x.md")}, self.p,
                                 "script-asst:research-writer"))

    def test_session_save_near_misses(self):
        run = self.note(".runs", "run-2026-10-13-2147-migration")
        for path in [os.path.join(run, "run-state.json"), os.path.join(run, "batches.json"),
                     os.path.join(run, "findings-b1-r0.json.bak"), self.note(".runs", "findings-b1-r0.json"),
                     self.note(".runs", "units", "findings-b1-r0.json"), self.note("Ideas", "outcomes.json"),
                     os.path.join(run, "snapshot", "outcomes.json")]:
            self.assertIsNone(answer("Write", {"file_path": path}, self.p), path)

    def test_session_edit_of_findings(self):
        path = self.note(".runs", "run-2026-10-13-2147-migration", "findings-b1-r0.json")
        self.assertIsNone(answer("Edit", {"file_path": path}, self.p))

    def test_agent_write_of_findings(self):
        path = self.note(".runs", "run-2026-10-13-2147-migration", "findings-b1-r0.json")
        self.assertIsNone(answer("Write", {"file_path": path}, self.p, "script-asst:migration-verifier"))

    def test_main_session_edit(self):
        self.assertIsNone(answer("Edit", {"file_path": self.note("Ideas", "idea-tobias.md")}, self.p))

    def test_other_agent_edit(self):
        self.assertIsNone(answer("Edit", {"file_path": self.note("Ideas", "idea-tobias.md")}, self.p,
                                 "script-asst:migration-verifier"))

    def test_migrator_write_outside_the_project(self):
        self.assertIsNone(answer("Write", {"file_path": self.outside}, self.p, "script-asst:migrator"))

    def test_migrator_write_through_dotdot(self):
        self.assertIsNone(answer("Write", {"file_path": self.note("..", "other.md")}, self.p,
                                 "script-asst:migrator"))

    def test_migrator_write_to_settings(self):
        self.assertIsNone(answer("Write", {"file_path": self.note(".claude", "settings.json")}, self.p,
                                 "script-asst:migrator"))

    def test_migrator_write_to_a_dot_folder_note(self):
        self.assertIsNone(answer("Write", {"file_path": self.note(".obsidian", "x.md")}, self.p,
                                 "script-asst:migrator"))

    def test_migrator_write_to_run_state(self):
        self.assertIsNone(answer("Write", {"file_path": self.note(".runs", "run-state.json")}, self.p,
                                 "script-asst:migrator"))

    def test_migrator_write_non_note(self):
        self.assertIsNone(answer("Write", {"file_path": self.note("Ideas", "x.sh")}, self.p,
                                 "script-asst:migrator"))

    def test_migrator_write_through_a_link_out(self):
        os.symlink(self.tmp.name, self.note("Ideas", "out"))
        self.assertIsNone(answer("Write", {"file_path": self.note("Ideas", "out", "other.md")}, self.p,
                                 "script-asst:migrator"))

    def test_main_session_reads_the_rules_file(self):
        self.assertIsNone(answer("Read", {"file_path": RULES}, self.p))

    def test_agent_reads_elsewhere(self):
        self.assertIsNone(answer("Read", {"file_path": os.path.expanduser("~/.ssh/config")}, self.p,
                                 "script-asst:migrator"))

    def test_other_plugin_agent_named_like_ours(self):
        self.assertIsNone(answer("Edit", {"file_path": self.note("Ideas", "idea-tobias.md")}, self.p,
                                 "script-asst-fake:migrator"))

    def test_chained_commands(self):
        for cmd in ["runmanager status --project . ; rm -rf x", "runmanager status && echo hi",
                    "runmanager status | tee x", "runmanager status > x", "runmanager $(whoami)",
                    "runmanager `whoami`", "runmanager status\nrm x", "runmanager status & rm x",
                    "editguard check < x"]:
            self.assertIsNone(answer("Bash", {"command": cmd}, self.p), cmd)

    def test_other_commands(self):
        for cmd in ["runmanagerx status", "rm -rf x", "python3 runmanager", "/bin/runmanager status"]:
            self.assertIsNone(answer("Bash", {"command": cmd}, self.p), cmd)

    def test_bad_input(self):
        out = subprocess.run([sys.executable, HOOK], input="not json", capture_output=True, text=True)
        self.assertEqual((out.returncode, out.stdout), (0, ""))


if __name__ == "__main__":
    unittest.main()
