"""The note's kind is whichever of brain-dump, idea-note, or area-note its `type` list holds, in any
position (migrator-rules.md 01.8)."""
import pytest

from runmanager.migration.scan import note_kind


@pytest.mark.parametrize("front, kind", [
    (["type: [area-note]"], "area-note"),
    (["type: [character-profile, area-note]"], "area-note"),
    (["type:", "  - relationship-profile", "  - area-note"], "area-note"),
    (["type: idea-note"], "idea-note"),
    (["type:", "  - brain-dump"], "brain-dump"),
    (["type: [scene-note, scene-outline]"], None),
    (["title: x"], None),
])
def test_note_kind(front, kind):
    assert note_kind(["---", *front, "---", "- a line"]) == kind
