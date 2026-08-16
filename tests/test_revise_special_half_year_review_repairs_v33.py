import json

import pytest

from scripts import revise_special_half_year_review_repairs_v33 as repair


QUEUE_SHA = "a" * 64
ISSUE_ID = "SP-2024-H1"
VERSION = "v0.14"


def _write_json(path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def _setup(tmp_path, *, overlay_entries):
    base_path = tmp_path / "sources" / ISSUE_ID / "editorial" / "base.json"
    overlay_path = tmp_path / "sources" / ISSUE_ID / "editorial" / "overlay.json"
    marker_path = tmp_path / "sources" / ISSUE_ID / "editorial" / f"layout-revision-{VERSION}.json"

    _write_json(
        base_path,
        {
            "issue_id": ISSUE_ID,
            "screening_verification_queue_sha256": QUEUE_SHA,
            "entries": {
                "Quiet-STaR": {
                    "source_urls": ["http://arxiv.org/abs/2403.09629v2"],
                    "technical_points": ["base point"],
                }
            },
        },
    )
    _write_json(
        overlay_path,
        {
            "issue_id": ISSUE_ID,
            "screening_verification_queue_sha256": QUEUE_SHA,
            "entries": overlay_entries,
        },
    )
    _write_json(
        marker_path,
        {
            "layout_changes": {
                "technical_note_detail_overrides_path": base_path.relative_to(tmp_path).as_posix(),
                "technical_note_detail_overrides_overlay_path": overlay_path.relative_to(tmp_path).as_posix(),
            }
        },
    )


def test_override_overlay_preserves_base_and_adds_revision_entries(tmp_path) -> None:
    _setup(
        tmp_path,
        overlay_entries={
            "DeepSeek-V2 / DeepSeek-Coder-V2": {
                "source_urls": ["https://example.com/deepseek"],
                "technical_points": ["overlay point"],
            }
        },
    )

    values = repair._load_overrides_with_overlay(tmp_path, ISSUE_ID, VERSION)

    assert set(values) == {"Quiet-STaR", "DeepSeek-V2 / DeepSeek-Coder-V2"}
    assert values["Quiet-STaR"]["technical_points"] == ["base point"]
    assert values["DeepSeek-V2 / DeepSeek-Coder-V2"]["technical_points"] == ["overlay point"]
    assert values["Quiet-STaR"]["_expected_queue_sha256"] == QUEUE_SHA
    assert values["DeepSeek-V2 / DeepSeek-Coder-V2"]["_expected_queue_sha256"] == QUEUE_SHA


def test_override_overlay_rejects_duplicate_base_title(tmp_path) -> None:
    _setup(
        tmp_path,
        overlay_entries={
            "Quiet-STaR": {
                "source_urls": ["http://arxiv.org/abs/2403.09629v2"],
                "technical_points": ["replacement must not be allowed"],
            }
        },
    )

    with pytest.raises(ValueError, match="must be additive"):
        repair._load_overrides_with_overlay(tmp_path, ISSUE_ID, VERSION)


def test_override_overlay_requires_hash_binding(tmp_path) -> None:
    _setup(tmp_path, overlay_entries={"DeepSeek": {"source_urls": [], "technical_points": ["point"]}})
    overlay_path = tmp_path / "sources" / ISSUE_ID / "editorial" / "overlay.json"
    payload = json.loads(overlay_path.read_text(encoding="utf-8"))
    payload["screening_verification_queue_sha256"] = ""
    _write_json(overlay_path, payload)

    with pytest.raises(ValueError, match="screening_verification_queue_sha256 is required"):
        repair._load_overrides_with_overlay(tmp_path, ISSUE_ID, VERSION)
