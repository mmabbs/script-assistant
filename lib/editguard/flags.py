"""Writes the flags file."""
import json
import os
import tempfile


def make_flag(rule, change, unit=""):
    """One flag, without its id (spec-edit-guard.md 05 item 2). `change` is an explain.Change."""
    return {"rule": rule, "note": change.note, "before": change.before, "after": change.after,
            "unit": unit, "_order": (change.note, change.seq)}


def note_flag(rule, note):
    """A flag on a whole note, with before, after, and unit empty (spec-edit-guard.md 05 item 5)."""
    return {"rule": rule, "note": note, "before": "", "after": "", "unit": "", "_order": (note, 0)}


def drop_asked(flags, judged, findings):
    """The second pass: drop each flag that matches one judged asked for, on rule, note, before, and
    after (spec-edit-guard.md 07 item 2). `judged` is the first pass's flags list; `findings` is
    findings-flags.json, whose entries name judged flags by id (spec-migration-verifier.md 05.3).
    Raises ValueError when an asked finding names a flag the judged file doesn't hold."""
    by_id = {f["id"]: f for f in judged}
    asked = set()
    for v in findings["flags"]:
        if v["verdict"] != "asked":
            continue
        if v["flag"] not in by_id:
            raise ValueError(f"findings names flag {v['flag']!r}, which the judged flags file doesn't hold")
        f = by_id[v["flag"]]
        asked.add((f["rule"], f["note"], f["before"], f["after"]))
    return [f for f in flags if (f["rule"], f["note"], f["before"], f["after"]) not in asked]


def number_flags(flags):
    """Sort flags by note, then by where the change sits, and number them f1, f2, ..."""
    out = []
    for i, f in enumerate(sorted(flags, key=lambda f: f["_order"]), 1):
        out.append({"id": f"f{i}", "rule": f["rule"], "note": f["note"],
                    "before": f["before"], "after": f["after"], "unit": f["unit"]})
    return out


def write_flags(path, flags):
    """Write the flags list to path through a temp file in the same folder, then swap it in."""
    folder = os.path.dirname(os.path.abspath(path))
    fd, tmp = tempfile.mkstemp(dir=folder, prefix=".flags-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(flags, f, indent=2)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
