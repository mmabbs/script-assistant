"""The before-snapshot: copies of the notes a run may edit, and a fingerprint of every other note
(spec-run-manager.md 04 items 8, 9, and 14). Pruning to the last 3 snapshots happens at `close`
(CONTRACT.md 4 item 2)."""
import hashlib
import json
import os
import re
import shutil

from .lines import write_note_whole

# The folders that hold only run output, never covered (spec-run-manager.md 04 item 9).
NEVER_COVERED = {"Runs", ".runs", "llm-files"}


def run_folder(project, run_id):
    return os.path.join(project, ".runs", run_id)


def covered_notes(project):
    """Map each covered note's path inside the project (with /) to its full path, sorted by path.
    Only .md files. Skips Runs/, .runs/, and llm-files/ at the project root (spec-run-manager.md 04
    item 9), and every folder whose name starts with a dot, which Obsidian hides."""
    found = {}
    for dirpath, dirnames, filenames in os.walk(project):
        at_root = os.path.samefile(dirpath, project)
        dirnames[:] = [d for d in dirnames
                       if not d.startswith(".") and not (at_root and d in NEVER_COVERED)]
        for name in filenames:
            if name.endswith(".md"):
                full = os.path.join(dirpath, name)
                found[os.path.relpath(full, project).replace(os.sep, "/")] = full
    return dict(sorted(found.items()))


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()


def write_json(path, data):
    write_note_whole(path, json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def save(project, run_id, copies):
    """Save the snapshot: each note in `copies` (path inside the project -> the text read when the run
    started) goes to `.runs/{run-id}/snapshot/`, and every other covered note gets a SHA-256 of the
    whole file in `fingerprints.json` (spec-run-manager.md 04 items 8, 9, and 14)."""
    folder = run_folder(project, run_id)
    for note, text in copies.items():
        dest = os.path.join(folder, "snapshot", *note.split("/"))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        write_note_whole(dest, text)
    prints = {note: sha256_of(full) for note, full in covered_notes(project).items() if note not in copies}
    os.makedirs(folder, exist_ok=True)
    write_json(os.path.join(folder, "fingerprints.json"), prints)


RUN_FOLDER = re.compile(r"run-(\d{4}-\d{2}-\d{2}-\d{4})-[a-z]+")


def prune(project, keep=3):
    """Every run folder except the `keep` newest by start time loses its snapshot/ folder; the rest of
    the folder stays (spec-run-manager.md 04 item 8; CONTRACT.md 4 item 2). Runs at `close`, after the
    history is written."""
    runs = os.path.join(project, ".runs")
    found = []
    for name in os.listdir(runs):
        m = RUN_FOLDER.fullmatch(name)
        if m and os.path.isdir(os.path.join(runs, name)):
            found.append((m.group(1), name))
    for _, name in sorted(found, reverse=True)[keep:]:
        shutil.rmtree(os.path.join(runs, name, "snapshot"), ignore_errors=True)
