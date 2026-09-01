from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import validate_issue_architecture as via


class IssueArchitecturePackagePageCapTests(unittest.TestCase):
    def _input(self) -> dict:
        item = {
            "evidence_task_id": "feature",
            "title": "Feature",
            "role": "FEATURE_CORE",
            "selection_rationale": "test",
            "artifact_type": "MODEL",
            "organization": "Example",
            "timing_relation": "MAIN_EVENT",
            "event_dates": ["2024-08-01"],
            "evidence_status": "VERIFIED",
            "comparison_readiness": "READY",
            "why_now_confirmed": True,
            "remaining_boundaries": [],
            "evidence_class_counts": {"PRIMARY_FACT": 1},
            "source_class_counts": {"PRIMARY_OFFICIAL": 1},
        }
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "status": "architecture-input-ready",
            "basis": {
                "selection_path": "selection.json",
                "selection_sha256": "1" * 64,
                "matrix_path": "matrix.json",
                "matrix_sha256": "2" * 64,
                "selection_version": "v0.1",
                "approval": {
                    "approved_by": "internal-editorial-checkpoint",
                    "approved_at": "2026-08-14T00:00:00Z",
                    "approval_reference": "test",
                },
            },
            "editorial_constraints": {
                "page_target": 64,
                "page_max": 96,
                "forced_section_balance": False,
                "cover_headline_deferred_until_drafts_stable": True,
                "this_week_summary_written_last": True,
                "late_breaking_must_remain_post_cutoff": True,
                "hold_or_excluded_items_must_not_be_drafted": True,
            },
            "selected_by_role": {
                "FEATURE_CORE": [item],
                "SECTION_CORE": [],
                "PAPER_WATCH": [],
                "SUPPORTING_EVIDENCE": [],
                "LATE_BREAKING": [],
                "CHRONOLOGY": [],
                "WATCHLIST": [],
            },
            "not_selected_for_architecture": [],
            "selected_item_count": 1,
            "excluded_item_count": 0,
            "rules": ["test"],
        }

    def _plan(self, input_path: Path, page_target: int) -> dict:
        architecture_input = json.loads(input_path.read_text(encoding="utf-8"))
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "architecture_version": "v0.1",
            "status": "PROPOSED",
            "basis": {
                "architecture_input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
                "selection_sha256": architecture_input["basis"]["selection_sha256"],
                "matrix_sha256": architecture_input["basis"]["matrix_sha256"],
            },
            "approval": {"approved_by": None, "approved_at": None, "approval_reference": None},
            "editorial_thesis": "Test thesis.",
            "architecture_goals": ["Keep package size bounded."],
            "page_budget": {"target": 64, "max": 96, "planned": page_target},
            "cover": {"headline_deferred": True, "headline": None, "anchor_candidates": ["feature"]},
            "packages": [{
                "package_id": "feature",
                "title": "Feature",
                "package_type": "FEATURE",
                "primary_evidence_task_ids": ["feature"],
                "supporting_evidence_task_ids": [],
                "page_target": page_target,
                "editorial_angle": "Test.",
                "must_cover": [],
                "boundaries": [],
                "late_breaking": False,
                "drafting_order": 1,
            }],
            "this_week_summary_written_last": True,
        }

    def test_eight_pages_is_allowed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path = root / "input.json"
            input_path.write_text(json.dumps(self._input()), encoding="utf-8")
            plan_path = root / "plan.json"
            plan_path.write_text(json.dumps(self._plan(input_path, 8)), encoding="utf-8")
            report, passed = via.validate(input_path, plan_path, require_approved=False)
            self.assertTrue(passed, report)

    def test_nine_pages_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path = root / "input.json"
            input_path.write_text(json.dumps(self._input()), encoding="utf-8")
            plan_path = root / "plan.json"
            plan_path.write_text(json.dumps(self._plan(input_path, 9)), encoding="utf-8")
            report, passed = via.validate(input_path, plan_path, require_approved=False)
            self.assertFalse(passed)
            self.assertTrue(any("exceeds package maximum 8" in error for error in report["errors"]), report)


if __name__ == "__main__":
    unittest.main()
