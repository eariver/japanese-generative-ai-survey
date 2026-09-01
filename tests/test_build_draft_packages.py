from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import build_draft_packages as bdp


class DraftPackageBuilderTests(unittest.TestCase):
    def _selected_item(self, task_id: str, role: str, boundaries: list[str]) -> dict:
        return {
            "evidence_task_id": task_id,
            "title": task_id,
            "role": role,
            "selection_rationale": "selected",
            "artifact_type": "MODEL_UPDATE",
            "organization": "Example",
            "timing_relation": "MAIN_EVENT",
            "event_dates": ["2026-08-05"],
            "evidence_status": "VERIFIED",
            "comparison_readiness": "READY_WITH_CAVEAT",
            "why_now_confirmed": True,
            "remaining_boundaries": boundaries,
            "evidence_class_counts": {"PRIMARY_FACT": 1},
            "source_class_counts": {"PRIMARY_OFFICIAL": 1},
        }

    def _input(self) -> dict:
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
                "approval": {"approved_by": "human", "approved_at": "2026-08-10T00:00:00Z", "approval_reference": "manual"},
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
                "FEATURE_CORE": [self._selected_item("feature", "FEATURE_CORE", ["Vendor claim must remain attributed."])],
                "SECTION_CORE": [],
                "PAPER_WATCH": [],
                "SUPPORTING_EVIDENCE": [self._selected_item("support", "SUPPORTING_EVIDENCE", ["Social observation only."])],
                "LATE_BREAKING": [],
                "CHRONOLOGY": [],
                "WATCHLIST": [],
            },
            "not_selected_for_architecture": [],
            "selected_item_count": 2,
            "excluded_item_count": 0,
            "rules": ["test"],
        }

    def _plan(self, input_path: Path) -> dict:
        architecture_input = json.loads(input_path.read_text())
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "architecture_version": "v0.1",
            "status": "APPROVED",
            "basis": {
                "architecture_input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
                "selection_sha256": architecture_input["basis"]["selection_sha256"],
                "matrix_sha256": architecture_input["basis"]["matrix_sha256"],
            },
            "approval": {"approved_by": "human", "approved_at": "2026-08-10T00:00:00Z", "approval_reference": "manual"},
            "editorial_thesis": "Test thesis.",
            "architecture_goals": ["test"],
            "page_budget": {"target": 16, "max": 24, "planned": 4},
            "cover": {"headline_deferred": True, "headline": None, "anchor_candidates": ["feature"]},
            "packages": [
                {
                    "package_id": "feature-package",
                    "title": "Feature",
                    "package_type": "FEATURE",
                    "primary_evidence_task_ids": ["feature"],
                    "supporting_evidence_task_ids": ["support"],
                    "page_target": 2,
                    "editorial_angle": "Explain it.",
                    "must_cover": ["Core mechanics."],
                    "boundaries": ["Vendor claim must remain attributed.", "Social observation only."],
                    "late_breaking": False,
                    "drafting_order": 1,
                },
                {
                    "package_id": "frontmatter",
                    "title": "Frontmatter",
                    "package_type": "FRONTMATTER",
                    "primary_evidence_task_ids": [],
                    "supporting_evidence_task_ids": [],
                    "page_target": 1,
                    "editorial_angle": "Written after drafts.",
                    "must_cover": [],
                    "boundaries": [],
                    "late_breaking": False,
                    "drafting_order": 2,
                },
                {
                    "package_id": "references",
                    "title": "References",
                    "package_type": "REFERENCES",
                    "primary_evidence_task_ids": [],
                    "supporting_evidence_task_ids": [],
                    "page_target": 1,
                    "editorial_angle": "Generated references.",
                    "must_cover": [],
                    "boundaries": [],
                    "late_breaking": False,
                    "drafting_order": 3,
                },
            ],
            "this_week_summary_written_last": True,
        }

    def _write(self, root: Path) -> tuple[Path, Path, Path]:
        input_path = root / "architecture-input.json"
        input_path.write_text(json.dumps(self._input()), encoding="utf-8")
        plan_path = root / "architecture-plan.json"
        plan_path.write_text(json.dumps(self._plan(input_path)), encoding="utf-8")
        evidence_path = root / "evidence-reviewed.jsonl"
        evidence_path.write_text(
            json.dumps({"issue_id": "2026-W32", "evidence_task_id": "feature", "card": {"artifact": {"canonical_name": "Feature"}}}) + "\n" +
            json.dumps({"issue_id": "2026-W32", "evidence_task_id": "support", "card": {"artifact": {"canonical_name": "Support"}}}) + "\n",
            encoding="utf-8",
        )
        return input_path, plan_path, evidence_path

    def test_builds_article_summary_and_reference_stages(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path, plan_path, evidence_path = self._write(root)
            out = root / "out"
            manifest, passed = bdp.build(input_path, plan_path, evidence_path, out)
            self.assertTrue(passed, manifest)
            self.assertEqual(manifest["materialized_package_count"], 3)
            self.assertEqual(manifest["article_drafting_count"], 1)
            self.assertEqual(manifest["post_draft_summary_count"], 1)
            self.assertEqual(manifest["reference_generation_count"], 1)

            feature = json.loads((out / "feature-package.json").read_text())
            self.assertEqual(feature["execution_stage"], "ARTICLE_DRAFTING")
            self.assertEqual([item["evidence_task_id"] for item in feature["primary_evidence"]], ["feature"])
            self.assertEqual([item["evidence_task_id"] for item in feature["supporting_evidence"]], ["support"])
            self.assertTrue(feature["drafting_constraints"]["this_week_summary_forbidden"])

            frontmatter = json.loads((out / "frontmatter.json").read_text())
            self.assertEqual(frontmatter["execution_stage"], "POST_DRAFT_SUMMARY")
            self.assertFalse(frontmatter["drafting_constraints"]["this_week_summary_forbidden"])

            references = json.loads((out / "references.json").read_text())
            self.assertEqual(references["execution_stage"], "REFERENCE_GENERATION")

            for entry in manifest["package_files"]:
                path = out / entry["path"]
                self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), entry["sha256"])
                self.assertEqual(path.stat().st_size, entry["bytes"])

    def test_missing_reviewed_evidence_fails_without_silent_drop(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path, plan_path, evidence_path = self._write(root)
            evidence_path.write_text(
                json.dumps({"issue_id": "2026-W32", "evidence_task_id": "feature", "card": {}}) + "\n",
                encoding="utf-8",
            )
            manifest, passed = bdp.build(input_path, plan_path, evidence_path, root / "out")
            self.assertFalse(passed)
            self.assertTrue(any("support" in error for error in manifest["errors"]))

    def test_proposed_architecture_is_not_drafting_ready(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path, plan_path, evidence_path = self._write(root)
            plan = json.loads(plan_path.read_text())
            plan["status"] = "PROPOSED"
            plan["approval"] = {"approved_by": None, "approved_at": None, "approval_reference": None}
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            with self.assertRaises(ValueError):
                bdp.build(input_path, plan_path, evidence_path, root / "out")


if __name__ == "__main__":
    unittest.main()
