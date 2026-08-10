from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import candidate_selection_gate as csg


class CandidateSelectionGateTests(unittest.TestCase):
    def _matrix(self) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "status": "pre-selection-comparison",
            "ranking": None,
            "rows": [
                {
                    "evidence_task_id": "candidate",
                    "title": "Candidate",
                    "recommendation": "CANDIDATE",
                    "timing_relation": "MAIN_EVENT",
                },
                {
                    "evidence_task_id": "late",
                    "title": "Late",
                    "recommendation": "CANDIDATE",
                    "timing_relation": "POST_CUTOFF",
                },
                {
                    "evidence_task_id": "hold",
                    "title": "Hold",
                    "recommendation": "HOLD",
                    "timing_relation": "MAIN_EVENT",
                },
                {
                    "evidence_task_id": "reject",
                    "title": "Reject",
                    "recommendation": "REJECT",
                    "timing_relation": "MAIN_EVENT",
                },
            ],
        }

    def _write_matrix(self, root: Path) -> Path:
        path = root / "matrix.json"
        path.write_text(json.dumps(self._matrix()), encoding="utf-8")
        return path

    def test_init_preserves_human_choice_and_sets_only_boundary_suggestions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            matrix = self._write_matrix(root)
            selection_path = root / "selection.json"
            selection = csg.initialize(matrix, selection_path, "v0.1")
            roles = {item["evidence_task_id"]: item["role"] for item in selection["assignments"]}
            self.assertEqual(roles["candidate"], "UNASSIGNED")
            self.assertEqual(roles["late"], "LATE_BREAKING")
            self.assertEqual(roles["hold"], "HOLD_OUT")
            self.assertEqual(roles["reject"], "EXCLUDE")
            self.assertEqual(selection["status"], "PENDING_APPROVAL")

    def test_approved_complete_selection_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            matrix = self._write_matrix(root)
            selection_path = root / "selection.json"
            selection = csg.initialize(matrix, selection_path, "v0.1")
            for item in selection["assignments"]:
                if item["evidence_task_id"] == "candidate":
                    item["role"] = "FEATURE_CORE"
                    item["rationale"] = "Lead technical story."
            selection["status"] = "APPROVED"
            selection["approval"] = {
                "approved_by": "human-reviewer",
                "approved_at": "2026-08-10T08:00:00Z",
                "approval_reference": "manual-review",
            }
            selection_path.write_text(json.dumps(selection), encoding="utf-8")
            report, passed = csg.validate(selection_path, matrix, require_approved=True)
            self.assertTrue(passed, report)
            self.assertEqual(report["unassigned_count"], 0)

    def test_hold_and_post_cutoff_cannot_be_promoted_to_feature(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            matrix = self._write_matrix(root)
            selection_path = root / "selection.json"
            selection = csg.initialize(matrix, selection_path, "v0.1")
            for item in selection["assignments"]:
                if item["evidence_task_id"] in {"late", "hold"}:
                    item["role"] = "FEATURE_CORE"
                    item["rationale"] = "invalid promotion"
            selection_path.write_text(json.dumps(selection), encoding="utf-8")
            report, passed = csg.validate(selection_path, matrix, require_approved=False)
            self.assertFalse(passed)
            self.assertTrue(any("POST_CUTOFF" in error for error in report["errors"]))
            self.assertTrue(any("HOLD Evidence" in error for error in report["errors"]))

    def test_matrix_change_invalidates_selection_basis(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            matrix = self._write_matrix(root)
            selection_path = root / "selection.json"
            csg.initialize(matrix, selection_path, "v0.1")
            changed = self._matrix()
            changed["rows"][0]["title"] = "Changed"
            matrix.write_text(json.dumps(changed), encoding="utf-8")
            report, passed = csg.validate(selection_path, matrix, require_approved=False)
            self.assertFalse(passed)
            self.assertTrue(any("matrix_sha256" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
