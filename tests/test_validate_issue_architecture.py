from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import validate_issue_architecture as via


class IssueArchitectureValidationTests(unittest.TestCase):
    def _item(self, task_id: str, role: str, *, timing: str = "MAIN_EVENT", boundaries: list[str] | None = None) -> dict:
        return {
            "evidence_task_id": task_id,
            "title": task_id,
            "role": role,
            "selection_rationale": "selected for test",
            "artifact_type": "MODEL_UPDATE",
            "organization": "Example",
            "timing_relation": timing,
            "event_dates": ["2026-08-05"],
            "evidence_status": "VERIFIED",
            "comparison_readiness": "READY_WITH_CAVEAT" if boundaries else "READY",
            "why_now_confirmed": True,
            "remaining_boundaries": boundaries or [],
            "evidence_class_counts": {"PRIMARY_FACT": 1},
            "source_class_counts": {"PRIMARY_OFFICIAL": 1},
        }

    def _architecture_input(self) -> dict:
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
                    "approved_by": "human",
                    "approved_at": "2026-08-10T00:00:00Z",
                    "approval_reference": "manual",
                },
            },
            "editorial_constraints": {
                "page_target": 16,
                "page_max": 24,
                "forced_section_balance": False,
                "cover_headline_deferred_until_drafts_stable": True,
                "this_week_summary_written_last": True,
                "late_breaking_must_remain_post_cutoff": True,
                "hold_or_excluded_items_must_not_be_drafted": True,
            },
            "selected_by_role": {
                "FEATURE_CORE": [self._item("feature", "FEATURE_CORE", boundaries=["Vendor benchmark only."])],
                "SECTION_CORE": [],
                "PAPER_WATCH": [],
                "SUPPORTING_EVIDENCE": [self._item("support", "SUPPORTING_EVIDENCE", boundaries=["Social observation only."])],
                "LATE_BREAKING": [self._item("late", "LATE_BREAKING", timing="POST_CUTOFF", boundaries=["Post-cutoff event."])],
                "CHRONOLOGY": [],
                "WATCHLIST": [],
            },
            "not_selected_for_architecture": [
                self._item("excluded", "HOLD_OUT", boundaries=["Not selected."])
            ],
            "selected_item_count": 3,
            "excluded_item_count": 1,
            "rules": ["test"],
        }

    def _plan(self, input_path: Path) -> dict:
        architecture_input = json.loads(input_path.read_text())
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
            "approval": {
                "approved_by": None,
                "approved_at": None,
                "approval_reference": None,
            },
            "editorial_thesis": "A coherent issue thesis.",
            "architecture_goals": ["Preserve evidence boundaries."],
            "page_budget": {"target": 16, "max": 24, "planned": 3},
            "cover": {
                "headline_deferred": True,
                "headline": None,
                "anchor_candidates": ["feature"],
            },
            "packages": [
                {
                    "package_id": "lead-feature",
                    "title": "Feature",
                    "package_type": "FEATURE",
                    "primary_evidence_task_ids": ["feature"],
                    "supporting_evidence_task_ids": ["support"],
                    "page_target": 2,
                    "editorial_angle": "Explain the feature.",
                    "must_cover": ["Evidence boundaries."],
                    "boundaries": ["Vendor benchmark only.", "Social observation only."],
                    "late_breaking": False,
                    "drafting_order": 1,
                },
                {
                    "package_id": "late-breaking",
                    "title": "Late Breaking",
                    "package_type": "LATE_BREAKING",
                    "primary_evidence_task_ids": ["late"],
                    "supporting_evidence_task_ids": [],
                    "page_target": 1,
                    "editorial_angle": "Keep the post-cutoff event separate.",
                    "must_cover": ["Post-cutoff chronology."],
                    "boundaries": ["Post-cutoff event."],
                    "late_breaking": True,
                    "drafting_order": 2,
                },
            ],
            "this_week_summary_written_last": True,
        }

    def _write(self, root: Path) -> tuple[Path, Path]:
        input_path = root / "architecture-input.json"
        input_path.write_text(json.dumps(self._architecture_input()), encoding="utf-8")
        plan_path = root / "architecture-plan.json"
        plan_path.write_text(json.dumps(self._plan(input_path)), encoding="utf-8")
        return input_path, plan_path

    def test_valid_proposed_architecture_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            input_path, plan_path = self._write(Path(tmp))
            report, passed = via.validate(input_path, plan_path, require_approved=False)
            self.assertTrue(passed, report)
            self.assertEqual(report["primary_required_count"], 2)
            self.assertEqual(report["primary_covered_count"], 2)
            self.assertEqual(report["planned_page_sum"], 3.0)

    def test_missing_selected_primary_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            input_path, plan_path = self._write(Path(tmp))
            plan = json.loads(plan_path.read_text())
            plan["packages"] = plan["packages"][:1]
            plan["page_budget"]["planned"] = 2
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            report, passed = via.validate(input_path, plan_path, require_approved=False)
            self.assertFalse(passed)
            self.assertEqual(report["missing_primary_items"], ["late"])

    def test_hold_or_excluded_intrusion_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            input_path, plan_path = self._write(Path(tmp))
            plan = json.loads(plan_path.read_text())
            plan["packages"][0]["supporting_evidence_task_ids"].append("excluded")
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            report, passed = via.validate(input_path, plan_path, require_approved=False)
            self.assertFalse(passed)
            self.assertTrue(any("excluded/HOLD" in error for error in report["errors"]))

    def test_late_breaking_in_normal_feature_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            input_path, plan_path = self._write(Path(tmp))
            plan = json.loads(plan_path.read_text())
            plan["packages"][1]["package_type"] = "FEATURE"
            plan["packages"][1]["late_breaking"] = False
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            report, passed = via.validate(input_path, plan_path, require_approved=False)
            self.assertFalse(passed)
            self.assertTrue(any("Late Breaking/Post-Cutoff primary" in error for error in report["errors"]))

    def test_missing_evidence_boundary_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            input_path, plan_path = self._write(Path(tmp))
            plan = json.loads(plan_path.read_text())
            plan["packages"][0]["boundaries"].remove("Social observation only.")
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            report, passed = via.validate(input_path, plan_path, require_approved=False)
            self.assertFalse(passed)
            self.assertTrue(any("missing Evidence boundaries" in error for error in report["errors"]))

    def test_page_sum_and_maximum_are_enforced(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            input_path, plan_path = self._write(Path(tmp))
            plan = json.loads(plan_path.read_text())
            plan["page_budget"]["planned"] = 25
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            report, passed = via.validate(input_path, plan_path, require_approved=False)
            self.assertFalse(passed)
            self.assertTrue(any("exceeds maximum" in error for error in report["errors"]))
            self.assertTrue(any("does not equal page_budget.planned" in error for error in report["errors"]))

    def test_approved_architecture_requires_approval_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            input_path, plan_path = self._write(Path(tmp))
            plan = json.loads(plan_path.read_text())
            plan["status"] = "APPROVED"
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            report, passed = via.validate(input_path, plan_path, require_approved=True)
            self.assertFalse(passed)
            self.assertTrue(any("APPROVED Architecture requires" in error for error in report["errors"]))

    def test_require_approved_blocks_proposed_plan(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            input_path, plan_path = self._write(Path(tmp))
            report, passed = via.validate(input_path, plan_path, require_approved=True)
            self.assertFalse(passed)
            self.assertTrue(any("must be APPROVED" in error for error in report["errors"]))

    def test_supporting_role_cannot_be_primary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            input_path, plan_path = self._write(Path(tmp))
            plan = json.loads(plan_path.read_text())
            plan["packages"][0]["supporting_evidence_task_ids"] = []
            plan["packages"][0]["primary_evidence_task_ids"].append("support")
            plan["packages"][0]["boundaries"] = ["Vendor benchmark only.", "Social observation only."]
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            report, passed = via.validate(input_path, plan_path, require_approved=False)
            self.assertFalse(passed)
            self.assertTrue(any("SUPPORTING_EVIDENCE role cannot be promoted" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
