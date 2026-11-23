"""The research-run rules, and fingerprint-changed for both run kinds (spec-edit-guard.md 04).

link-line-invalid, close-invalid, and unexpected-research-note run on research runs only.
fingerprint-changed runs on both. The link line and close rules run only on changes explain.py
explained as a link line or a close (spec-edit-guard.md 05 item 3).
"""
import hashlib
import os
import re

from .compare import notes_under
from .flags import make_flag, note_flag

RESEARCH = "Research/"
# A close: the request's checkbox `[r]` changed to `[x]`, nothing else (spec-run-manager.md 08.4 item 2).
OPEN_REQUEST = re.compile(r"^(\s*- )\[r\]( .*)$")


def indent_of(text):
    return text[: len(text) - len(text.lstrip())]


def link_line_target(text, request_text, project_name):
    """Return the note a link line points to, as a path inside the project folder, when the line is in
    the settled form; otherwise None (spec-run-manager.md 08.4 item 1):

        {request's indent}    - [AGENT] [[Projects/{Project}/Research/{name}|{name}]]

    One indent level deeper than the request (four spaces or a tab), no colon after [AGENT], and the
    file name shown.
    """
    pattern = (re.escape(indent_of(request_text)) + r"(?:    |\t)- \[AGENT\] \[\[Projects/"
               + re.escape(project_name) + r"/(Research/[^\]|#]+)\|([^\]|]+)\]\]")
    m = re.fullmatch(pattern, text)
    if not m or m.group(2) != m.group(1).rsplit("/", 1)[-1]:
        return None
    return m.group(1) + ".md"


def _named_note(outcomes, request_id):
    """The note the outcomes file names for a request: its `note`, when the outcome is `passed`."""
    for o in outcomes:
        if o["request"] == request_id and o["outcome"] == "passed":
            return o["note"]
    return None


def _link_line_valid(e, ctx, project):
    """A link line is valid when it sits right under its request, is in the settled form, points to the
    note the outcomes file names for that request, and that note exists (spec-edit-guard.md 04 item 6)."""
    if not e.info["under"]:
        return False
    target = link_line_target(e.change.after, e.info["request_line"].text, ctx.project_name)
    return (target is not None
            and target == _named_note(ctx.outcomes, e.entry["id"])
            and os.path.isfile(os.path.join(project, target)))


def link_line_invalid(explained, ctx, project):
    return [make_flag("link-line-invalid", e.change)
            for e in explained if e.how == "link-line" and not _link_line_valid(e, ctx, project)]


def close_invalid(explained, ctx, project):
    """A close passes only with a valid link line right under it, and nothing else on the request line
    changed. The flag holds the request's snapshot text as before and its text now as after, so undoing
    the close puts the writer's words back (spec-edit-guard.md 05 item 6; spec-run-manager.md 08.4 item 3).
    """
    valid_under = {e.entry["id"] for e in explained
                   if e.how == "link-line" and e.info["under"] and _link_line_valid(e, ctx, project)}
    flags = []
    for e in explained:
        if e.how != "close":
            continue
        m = OPEN_REQUEST.match(e.change.before)
        only_closed = bool(m) and e.change.after == f"{m.group(1)}[x]{m.group(2)}"
        if not only_closed or e.entry["id"] not in valid_under:
            flags.append(make_flag("close-invalid", e.change))
    return flags


def _new_notes(ctx, project, snapshot_notes):
    """Notes in the project now that are in neither the snapshot nor the fingerprints file."""
    known = set(snapshot_notes) | set(ctx.fingerprints)
    return [n for n in sorted(notes_under(project)) if n not in known]


def unexpected_research_note(ctx, project, snapshot_notes):
    """A new note in Research/ passes only if the outcomes file names it (spec-edit-guard.md 04 item 7)."""
    named = {o["note"] for o in ctx.outcomes if o.get("note")}
    return [note_flag("unexpected-research-note", n) for n in _new_notes(ctx, project, snapshot_notes)
            if n.startswith(RESEARCH) and n not in named]


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 16), b""):
            h.update(block)
    return h.hexdigest()


def fingerprint_changed(ctx, project, snapshot_notes):
    """A fingerprinted note whose fingerprint changed, or that is gone. On a research run, also a new
    note outside Research/ (spec-edit-guard.md 04 table; 11 Decisions Log items 23, 27, and 28)."""
    flags = []
    for note, digest in sorted(ctx.fingerprints.items()):
        path = os.path.join(project, note)
        if not os.path.isfile(path) or _sha256(path) != digest:
            flags.append(note_flag("fingerprint-changed", note))
    if ctx.kind == "research":
        flags += [note_flag("fingerprint-changed", n) for n in _new_notes(ctx, project, snapshot_notes)
                  if not n.startswith(RESEARCH)]
    return flags
