from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import special_pipeline


class SpecialPipelineTests(unittest.TestCase):
    def manifest(self) -> dict:
        return {
            "schema_version": "1.0",
            "special_id": "SP-2026-M07",
            "special_slug": "2026-M07",
            "display_label": "2026年7月 Retrospective",
            "series_title": "Japanese Generative AI Technical Survey Special",
            "edition_kind": "RETROSPECTIVE_PERIOD",
            "status": "ACTIVE",
            "coverage": {
                "start": "2026-07-01T00:00:00Z",
                "end": "2026-07-31T23:59:59Z",
                "timezone": "UTC",
                "retrospective_as_of": "2026-08-10T14:09:00Z",
            },
            "topic_scope": None,
            "community_research": {"mode": "DISABLED", "reason": "Historical X is unnecessary."},
            "editorial_policy": {
                "retrospective_method": "CURRENT_RECONSTRUCTION",
                "why_this_special_required": True,
                "primary_sources_required": True,
            },
            "page_budget": {"target": 24, "max": 36},
            "paths": {
                "survey_root": "surveys/special/2026-M07",
                "source_root": "sources/SP-2026-M07",
                "work_branch": "special/2026-M07-work",
            },
        }

    def test_july_manifest_builds_explicit_window_plan(self) -> None:
        manifest = self.manifest()
        self.assertEqual(special_pipeline.validate_manifest(manifest), [])
        plan = special_pipeline.build_plan(manifest)
        self.assertEqual(plan["issue_id"], "SP-2026-M07")
        self.assertEqual(plan["collection_window_start"], "2026-07-01T00:00:00Z")
        self.assertEqual(plan["collection_window_end"], "2026-07-31T23:59:59Z")
        self.assertEqual(plan["community_research"]["mode"], "DISABLED")
        self.assertIn("candidate_selection", plan["human_gates"])
        self.assertIn("public_release", plan["human_gates"])

    def test_retrospective_cannot_require_grok(self) -> None:
        manifest = self.manifest()
        manifest["community_research"]["mode"] = "ENABLED"
        errors = special_pipeline.validate_manifest(manifest)
        self.assertTrue(any("Grok/X" in error for error in errors))

    def test_initial_state_preserves_human_gates(self) -> None:
        state = special_pipeline.initial_state(self.manifest())
        self.assertEqual(state["lifecycle_state"], "ISSUE_INITIALIZED")
        self.assertEqual(state["gates"]["candidate_selection"], "pending")
        self.assertEqual(state["gates"]["issue_architecture"], "pending")
        self.assertEqual(state["gates"]["visual_review"], "pending")
        self.assertEqual(state["gates"]["freeze"], "pending")
        self.assertTrue(state["automation"]["human_gate_required_for_public_release"])

    def test_historical_granularity_matches_editorial_decision(self) -> None:
        config = json.loads(Path("config/special-pipeline.json").read_text(encoding="utf-8"))
        plan = special_pipeline.historical_plan(config)
        monthly = [x for x in plan["planned_period_specials"] if x["tier"] == "MONTHLY"]
        half_year = [x for x in plan["planned_period_specials"] if x["tier"] == "HALF_YEAR"]
        self.assertEqual(monthly[0]["special_slug"], "2025-M08")
        self.assertEqual(monthly[-1]["special_slug"], "2026-M07")
        self.assertEqual(len(monthly), 12)
        self.assertEqual(half_year[0]["start"], "2022-11-01T00:00:00Z")
        self.assertEqual(half_year[-1]["start"], "2025-05-01T00:00:00Z")
        self.assertEqual(half_year[-1]["end"], "2025-07-31T23:59:59Z")
        self.assertEqual(plan["annual_before"], "2022-11-01")

    def test_manifest_rejects_source_path_aliasing(self) -> None:
        manifest = self.manifest()
        manifest["paths"]["source_root"] = "sources/2026-W31"
        errors = special_pipeline.validate_manifest(manifest)
        self.assertTrue(any("source_root" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
