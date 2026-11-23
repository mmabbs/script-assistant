"""The note's kind is whichever of brain-dump, idea-note, or area-note its `type` list holds, in any
position (migrator-rules.md 01.8)."""
import pytest

from editguard.rules_migration import note_kind


@pytest.mark.parametrize("front, kind", [
    (["type: [area-note]"], "area-note"),
    (["type: [character-profile, area-note]"], "area-note"),
    (["type:", "  - relationship-profile", "  - area-note"], "area-note"),
    (["type: idea-note"], "idea-note"),
    (["type:", "  - brain-dump"], "brain-dump"),
    (["type: [scene-note, scene-outline]"], ""),
    (["title: x"], ""),
])
def test_note_kind(tmp_path, front, kind):
    note = tmp_path / "note.md"
    note.write_text("\n".join(["---", *front, "---", "- a line"]) + "\n", encoding="utf-8")
    assert note_kind(str(note)) == kind
