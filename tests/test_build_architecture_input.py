from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import build_architecture_input as bai


class ArchitectureInputBuilderTests(unittest.TestCase):
    def _matrix(self) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "rows": [
                {
                    "evidence_task_id": "feature",
                    "title": "Feature",
                    "artifact_type": "MODEL_UPDATE",
                    "organization": "Example",
                    "timing_relation": "MAIN_EVENT",
                    "event_dates": ["2026-08-05"],
                    "evidence_status": "VERIFIED",
                    "recommendation": "CANDIDATE",
                    "why_now_confirmed": True,
                    "comparison_readiness": "READY_WITH_CAVEAT",
                    "source_class_counts": {"PRIMARY_OFFICIAL": 1},
                    "evidence_class_counts": {"PRIMARY_FACT": 1, "VENDOR_CLAIM": 1},
                    "remaining_boundaries": ["Vendor benchmark only."],
                },
                {
                    "evidence_task_id": "late",
                    "title": "Late",
                    "artifact_type": "FRAMEWORK",
                    "organization": "Example",
                    "timing_relation": "POST_CUTOFF",
                    "event_dates": ["2026-08-08"],
                    "evidence_status": "VERIFIED",
                    "recommendation": "CANDIDATE",
                    "why_now_confirmed": True,
                    "comparison_readiness": "READY",
                    "source_class_counts": {"PRIMARY_REPOSITORY": 1},
                    "evidence_class_counts": {"PRIMARY_FACT": 1},
                    "remaining_boundaries": ["Post-cutoff event."],
                },
                {
                    "evidence_task_id": "hold",
                    "title": "Hold",
                    "artifact_type": "MODEL",
                    "organization": "Example",
                    "timing_relation": "MAIN_EVENT",
                    "event_dates": ["2026-08-05"],
                    "evidence_status": "PARTIAL",
                    "recommendation": "HOLD",
                    "why_now_confirmed": False,
                    "comparison_readiness": "HOLD",
                    "source_class_counts": {},
                    "evidence_class_counts": {},
                    "remaining_boundaries": ["Verification incomplete."],
                },
            ],
        }

    def _selection(self, matrix_path: Path, *, approved: bool) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "selection_version": "v0.1",
            "status": "APPROVED" if approved else "PENDING_APPROVAL",
            "basis": {
                "matrix_path": matrix_path.as_posix(),
                "matrix_sha256": hashlib.sha256(matrix_path.read_bytes()).hexdigest(),
            },
            "approval": (
                {
                    "approved_by": "human",
                    "approved_at": "2026-08-10T00:00:00Z",
                    "approval_reference": "manual",
                }
                if approved
                else {"approved_by": None, "approved_at": None, "approval_reference": None}
            ),
            "assignments": [
                {"evidence_task_id": "feature", "title": "Feature", "role": "FEATURE_CORE", "rationale": "Main story."},
                {"evidence_task_id": "late", "title": "Late", "role": "LATE_BREAKING", "rationale": "Post-cutoff."},
                {"evidence_task_id": "hold", "title": "Hold", "role": "HOLD_OUT", "rationale": "Needs verification."},
            ],
            "rules": ["test"],
        }

    def _write(self, root: Path, *, approved: bool) -> tuple[Path, Path]:
        matrix_path = root / "matrix.json"
        matrix_path.write_text(json.dumps(self._matrix()), encoding="utf-8")
        selection_path = root / "selection.json"
        selection_path.write_text(json.dumps(self._selection(matrix_path, approved=approved)), encoding="utf-8")
        return selection_path, matrix_path

    def test_approved_selection_builds_architecture_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            selection_path, matrix_path = self._write(root, approved=True)
            value = bai.build(selection_path, matrix_path)
            self.assertEqual(value["status"], "architecture-input-ready")
            self.assertEqual(value["selected_item_count"], 2)
            self.assertEqual(value["excluded_item_count"], 1)
            self.assertEqual(value["selected_by_role"]["FEATURE_CORE"][0]["evidence_task_id"], "feature")
            self.assertEqual(value["selected_by_role"]["LATE_BREAKING"][0]["timing_relation"], "POST_CUTOFF")
            self.assertEqual(value["not_selected_for_architecture"][0]["evidence_task_id"], "hold")
            self.assertEqual(value["basis"]["selection_sha256"], hashlib.sha256(selection_path.read_bytes()).hexdigest())
            self.assertEqual(value["basis"]["matrix_sha256"], hashlib.sha256(matrix_path.read_bytes()).hexdigest())

    def test_pending_selection_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            selection_path, matrix_path = self._write(root, approved=False)
            with self.assertRaises(ValueError):
                bai.build(selection_path, matrix_path)


if __name__ == "__main__":
    unittest.main()
