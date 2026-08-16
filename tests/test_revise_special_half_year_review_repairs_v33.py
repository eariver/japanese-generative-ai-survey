import json
import tempfile
import unittest
from pathlib import Path

from scripts import revise_special_half_year_review_repairs_v33 as repair


QUEUE_SHA = "a" * 64
ISSUE_ID = "SP-2024-H1"
VERSION = "v0.14"


def _write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def _setup(root: Path, *, overlay_entries) -> None:
    base_path = root / "sources" / ISSUE_ID / "editorial" / "base.json"
    overlay_path = root / "sources" / ISSUE_ID / "editorial" / "overlay.json"
    marker_path = root / "sources" / ISSUE_ID / "editorial" / f"layout-revision-{VERSION}.json"

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
                "technical_note_detail_overrides_path": base_path.relative_to(root).as_posix(),
                "technical_note_detail_overrides_overlay_path": overlay_path.relative_to(root).as_posix(),
            }
        },
    )


class HalfYearLayeredOverrideV33Tests(unittest.TestCase):
    def test_override_overlay_preserves_base_and_adds_revision_entries(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            _setup(
                root,
                overlay_entries={
                    "DeepSeek-V2 / DeepSeek-Coder-V2": {
                        "source_urls": ["https://example.com/deepseek"],
                        "technical_points": ["overlay point"],
                    }
                },
            )

            values = repair._load_overrides_with_overlay(root, ISSUE_ID, VERSION)

            self.assertEqual(set(values), {"Quiet-STaR", "DeepSeek-V2 / DeepSeek-Coder-V2"})
            self.assertEqual(values["Quiet-STaR"]["technical_points"], ["base point"])
            self.assertEqual(
                values["DeepSeek-V2 / DeepSeek-Coder-V2"]["technical_points"],
                ["overlay point"],
            )
            self.assertEqual(values["Quiet-STaR"]["_expected_queue_sha256"], QUEUE_SHA)
            self.assertEqual(
                values["DeepSeek-V2 / DeepSeek-Coder-V2"]["_expected_queue_sha256"],
                QUEUE_SHA,
            )

    def test_override_overlay_rejects_duplicate_base_title(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            _setup(
                root,
                overlay_entries={
                    "Quiet-STaR": {
                        "source_urls": ["http://arxiv.org/abs/2403.09629v2"],
                        "technical_points": ["replacement must not be allowed"],
                    }
                },
            )

            with self.assertRaisesRegex(ValueError, "must be additive"):
                repair._load_overrides_with_overlay(root, ISSUE_ID, VERSION)

    def test_override_overlay_requires_hash_binding(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            _setup(
                root,
                overlay_entries={
                    "DeepSeek": {"source_urls": [], "technical_points": ["point"]}
                },
            )
            overlay_path = root / "sources" / ISSUE_ID / "editorial" / "overlay.json"
            payload = json.loads(overlay_path.read_text(encoding="utf-8"))
            payload["screening_verification_queue_sha256"] = ""
            _write_json(overlay_path, payload)

            with self.assertRaisesRegex(ValueError, "screening_verification_queue_sha256 is required"):
                repair._load_overrides_with_overlay(root, ISSUE_ID, VERSION)


if __name__ == "__main__":
    unittest.main()
