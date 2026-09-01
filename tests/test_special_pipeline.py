from __future__ import annotations

import json
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
            "page_budget": {"target": 32, "max": 40},
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
        self.assertEqual(plan["human_gates"], ["issue_architecture", "publication_preview"])
        self.assertNotIn("candidate_selection", plan["human_gates"])
        self.assertNotIn("freeze", plan["human_gates"])
        self.assertNotIn("public_release", plan["human_gates"])
        self.assertEqual(
            plan["publication_preview_authorizes"],
            ["visual_review", "freeze", "work_pr_merge", "public_release"],
        )
        self.assertEqual(plan["exception_gate"], "ON_DEMAND")

    def test_retrospective_cannot_require_grok(self) -> None:
        manifest = self.manifest()
        manifest["community_research"]["mode"] = "ENABLED"
        errors = special_pipeline.validate_manifest(manifest)
        self.assertTrue(any("Grok/X" in error for error in errors))

    def test_initial_state_preserves_machine_checkpoints_but_only_two_human_stops(self) -> None:
        state = special_pipeline.initial_state(self.manifest())
        self.assertEqual(state["lifecycle_state"], "ISSUE_INITIALIZED")
        self.assertEqual(state["gates"]["candidate_selection"], "pending")
        self.assertEqual(state["gates"]["issue_architecture"], "pending")
        self.assertEqual(state["gates"]["visual_review"], "pending")
        self.assertEqual(state["gates"]["freeze"], "pending")
        automation = state["automation"]
        self.assertFalse(automation["human_gate_required_for_selection"])
        self.assertTrue(automation["human_gate_required_for_architecture"])
        self.assertTrue(automation["human_gate_required_for_publication_preview"])
        self.assertFalse(automation["human_gate_required_for_visual_review"])
        self.assertFalse(automation["human_gate_required_for_freeze"])
        self.assertFalse(automation["human_gate_required_for_public_release"])
        self.assertEqual(automation["exception_gate"], "ON_DEMAND")

    def test_config_declares_architecture_preview_exception_model(self) -> None:
        config = json.loads(Path("config/special-pipeline.json").read_text(encoding="utf-8"))
        policy = config["policy"]
        self.assertEqual(policy["human_gate_model"], "ARCHITECTURE_PUBLICATION_PREVIEW_WITH_EXCEPTION")
        self.assertFalse(policy["human_gate_required_for_selection"])
        self.assertTrue(policy["human_gate_required_for_architecture"])
        self.assertTrue(policy["human_gate_required_for_publication_preview"])
        self.assertFalse(policy["human_gate_required_for_visual_review"])
        self.assertFalse(policy["human_gate_required_for_freeze"])
        self.assertFalse(policy["human_gate_required_for_public_release"])
        self.assertEqual(policy["exception_gate"]["mode"], "ON_DEMAND")

    def test_start_prompt_authorizes_deterministic_initialization(self) -> None:
        config = json.loads(Path("config/special-pipeline.json").read_text(encoding="utf-8"))
        policy = config["policy"]
        self.assertFalse(policy["human_gate_required_for_initialization"])
        self.assertTrue(policy["start_prompt_authorizes_initialization"])
        self.assertEqual(
            policy["initialization_actions_authorized"],
            [
                "create_init_branch",
                "write_edition_manifest",
                "write_initial_pipeline_state",
                "open_and_merge_init_pr",
                "create_work_branch",
            ],
        )

    def test_initial_state_matches_current_state_schema_automation_contract(self) -> None:
        state = special_pipeline.initial_state(self.manifest())
        schema = json.loads(Path("schemas/special-pipeline-state.schema.json").read_text(encoding="utf-8"))
        automation_schema = schema["properties"]["automation"]
        self.assertEqual(set(state["automation"]), set(automation_schema["required"]))
        for key, value in state["automation"].items():
            property_schema = automation_schema["properties"][key]
            if "const" in property_schema:
                self.assertEqual(value, property_schema["const"], key)
        self.assertEqual(
            state["automation"]["publication_preview_authorizes"],
            [item["const"] for item in automation_schema["properties"]["publication_preview_authorizes"]["prefixItems"]],
        )

    def test_historical_granularity_matches_editorial_decision(self) -> None:
        config = json.loads(Path("config/special-pipeline.json").read_text(encoding="utf-8"))
        plan = special_pipeline.historical_plan(config)
        monthly = [x for x in plan["planned_period_specials"] if x["tier"] == "MONTHLY"]
        half_year = [x for x in plan["planned_period_specials"] if x["tier"] == "HALF_YEAR"]
        annual = [x for x in plan["planned_period_specials"] if x["tier"] == "ANNUAL"]

        self.assertEqual([x["special_slug"] for x in monthly], [
            "2026-M01", "2026-M02", "2026-M03", "2026-M04", "2026-M05", "2026-M06", "2026-M07"
        ])
        self.assertEqual([x["special_slug"] for x in half_year], [
            "2024-H1", "2024-H2", "2025-H1", "2025-H2"
        ])
        self.assertEqual([x["special_slug"] for x in annual], [
            "2020-Y", "2021-Y", "2022-Y", "2023-Y"
        ])
        self.assertEqual(half_year[0]["start"], "2024-01-01T00:00:00Z")
        self.assertEqual(half_year[-1]["end"], "2025-12-31T23:59:59Z")
        self.assertEqual(monthly[0]["start"], "2026-01-01T00:00:00Z")
        self.assertEqual(monthly[-1]["end"], "2026-07-31T23:59:59Z")
        self.assertEqual(plan["deferred_history"]["before"], "2020-01-01")
        self.assertEqual(plan["deferred_history"]["status"], "DEFERRED")

    def test_historical_plan_has_no_overlaps(self) -> None:
        config = json.loads(Path("config/special-pipeline.json").read_text(encoding="utf-8"))
        periods = special_pipeline.historical_plan(config)["planned_period_specials"]
        for previous, current in zip(periods, periods[1:]):
            self.assertLess(
                special_pipeline.parse_instant(previous["end"]),
                special_pipeline.parse_instant(current["start"]),
            )

    def test_annual_backfill_bootstrap_plans_are_manifest_independent(self) -> None:
        config = json.loads(Path("config/special-pipeline.json").read_text(encoding="utf-8"))
        expected = {
            "2020-Y": ("2020-01-01T00:00:00Z", "2020-12-31T23:59:59Z"),
            "2021-Y": ("2021-01-01T00:00:00Z", "2021-12-31T23:59:59Z"),
            "2022-Y": ("2022-01-01T00:00:00Z", "2022-12-31T23:59:59Z"),
        }
        for slug, (start, end) in expected.items():
            with self.subTest(slug=slug):
                plan = special_pipeline.bootstrap_plan(config, slug)
                self.assertEqual(plan["tier"], "ANNUAL")
                self.assertEqual(plan["special_id"], f"SP-{slug}")
                self.assertEqual(plan["coverage"]["start"], start)
                self.assertEqual(plan["coverage"]["end"], end)
                self.assertEqual(plan["coverage"]["retrospective_as_of"], "SET_AT_INITIALIZATION")
                self.assertEqual(plan["branches"]["init"], f"special/{slug}-init")
                self.assertEqual(plan["branches"]["work"], f"special/{slug}-work")
                self.assertIn("docs/annual-retrospective-specials.md", plan["required_guides"])
                self.assertTrue(plan["initialization"]["authorized_by_start_prompt"])
                self.assertFalse(plan["initialization"]["human_gate_required"])
                self.assertEqual(plan["initialization"]["mode"], "RESUME_IF_PRESENT_ELSE_INITIALIZE")
                self.assertEqual(plan["community_research_default"], "DISABLED")
                self.assertEqual(plan["stop_gate"]["gate"], "issue_architecture")
                self.assertTrue(plan["stop_gate"]["human_gate"])
                execution = plan["architecture_review_execution"]
                self.assertEqual(execution["canonical_source_intake"], "ALL_ENABLED_BASE_COLLECTORS")
                self.assertTrue(execution["period_specific_coverage_audit"])
                self.assertTrue(execution["supplemental_primary_source_gap_fill"])
                self.assertEqual(execution["candidate_selection"], "INTERNAL_CHECKPOINT")
                self.assertFalse(execution["reader_facing_drafting_before_approval"])

    def test_bootstrap_plan_rejects_unconfigured_period(self) -> None:
        config = json.loads(Path("config/special-pipeline.json").read_text(encoding="utf-8"))
        with self.assertRaisesRegex(ValueError, "not configured"):
            special_pipeline.bootstrap_plan(config, "2019-Y")

    def test_annual_source_specific_repair_workflow_is_retired(self) -> None:
        workflow = Path(".github/workflows/revise-special-annual-source-specific-notes-v2.yml")
        self.assertFalse(workflow.exists())

    def test_manifest_rejects_source_path_aliasing(self) -> None:
        manifest = self.manifest()
        manifest["paths"]["source_root"] = "sources/2026-W31"
        errors = special_pipeline.validate_manifest(manifest)
        self.assertTrue(any("source_root" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
