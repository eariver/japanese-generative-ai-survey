from __future__ import annotations

import unittest
from pathlib import Path

from scripts import survey_handlers_v2 as handlers
from scripts import survey_production_v2 as core


class SurveyPilotBootstrapV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(".").resolve()
        cls.cfg = core.load_json(cls.root / core.DEFAULT_CONFIG)

    def test_w33_and_sp001_profiles_bootstrap_without_starting_pilot_state(self) -> None:
        w33 = core.weekly_profile(
            self.root,
            self.cfg,
            core.parse_instant("2026-08-22T11:18:00+09:00"),
            "2026-W33",
        )
        sp001 = core.thematic_profile(
            self.root,
            self.cfg,
            {
                "issue_id": "SP001",
                "question": "How did Chinese generative AI ecosystems emerge and differentiate?",
                "temporal_mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-08-22T11:18:00+09:00",
                "scope_dimensions": ["lineage", "distribution", "reasoning", "coding"],
                "initial_obligations": [
                    {"obligation_id": "initial:lineage", "dimension": "lineage", "description": "trace core technical lineage"},
                    {"obligation_id": "initial:distribution", "dimension": "distribution", "description": "cover distribution and open-weight strategy"},
                    {"obligation_id": "initial:reasoning", "dimension": "reasoning", "description": "cover reasoning systems"},
                    {"obligation_id": "initial:coding", "dimension": "coding", "description": "cover coding systems"},
                ],
            },
        )

        self.assertEqual((w33["research_profile"], w33["publication_profile"]), ("WEEKLY", "WEEKLY_MAGAZINE"))
        self.assertEqual((sp001["research_profile"], sp001["publication_profile"]), ("THEMATIC", "LONGFORM_SPECIAL"))
        self.assertEqual(w33["research_scope"]["temporal_policy"]["cutoff"], "2026-08-14T18:00:00-04:00")
        self.assertEqual(set(sp001["research_scope"]["temporal_policy"]), {"mode", "as_of"})
        self.assertFalse((self.root / "sources/2026-W33/production-state.json").exists())
        self.assertFalse((self.root / "sources/SP001/production-state.json").exists())

    def test_all_stage_handlers_and_semantic_validators_have_one_settled_registry(self) -> None:
        registry: dict[str, object] = {}
        handlers.register_handlers(registry)
        for lifecycle, stage in self.cfg["orchestration"]["stage_plan"].items():
            self.assertIn(stage["handler"], registry, lifecycle)
            self.assertIn(stage["validator"], registry, lifecycle)
            self.assertEqual(stage.get("handoff_required"), True, lifecycle)
        frozen = self.cfg["orchestration"]["stage_plan"]["FROZEN"]
        self.assertEqual(frozen["action_kind"], "WORKFLOW_DISPATCH")
        self.assertEqual(frozen["retry_policy"], {"retryable": True, "max_attempts": 2})
        self.assertEqual(frozen["idempotency"], {"mode": "EXTERNAL_KEY", "key": "release_identity"})

    def test_workflow_and_assistant_control_authority_is_explicit_and_narrow(self) -> None:
        control = self.cfg["workflow_control"]
        self.assertEqual(control["dispatch_ref"], "main")
        self.assertEqual(control["handler_dispatch"], {"stage:release": "survey-production-v2-release.yml"})
        self.assertEqual(
            control["release_reconciliation"],
            {"external_key": "release_identity", "existing_release_policy": "VERIFY_EXACT_BYTES_THEN_RESUME"},
        )
        paths = {
            "assistant": self.root / ".github/workflows" / control["assistant_control_workflow"],
            "control": self.root / ".github/workflows" / control["production_control_workflow"],
            "release": self.root / ".github/workflows" / control["release_workflow"],
        }
        for label, path in paths.items():
            self.assertTrue(path.is_file(), f"missing {label} workflow: {path}")
        assistant = paths["assistant"].read_text(encoding="utf-8")
        self.assertIn("survey-production-v2-control", assistant)
        self.assertIn("survey-production-v2-release", assistant)
        self.assertIn("workflow not allowlisted by Core v2 assistant control", assistant)
        self.assertIn("Core v2 assistant dispatch ref must be main", assistant)
        self.assertIn("production_state_sha256", assistant)
        self.assertIn("release_manifest_sha256", assistant)
        production = paths["control"].read_text(encoding="utf-8")
        self.assertIn("survey_handoff_v2.py", production)
        self.assertIn("execute-current", production)
        self.assertIn("approve-architecture", production)
        self.assertIn("approve-publication-preview", production)
        self.assertIn("FROZEN is a WORKFLOW_DISPATCH stage", production)
        release = paths["release"].read_text(encoding="utf-8")
        self.assertIn("GITHUB_ACTIONS_ARTIFACT", release)
        self.assertIn("build_merge_verification", release)
        self.assertIn("build_release_record", release)
        self.assertIn("release-record/", release)
        self.assertIn("VERIFY_EXACT_BYTES_THEN_RESUME", release)
        self.assertIn("Create or reconcile exact-byte issue-only GitHub Release", release)
        self.assertIn("reconciled-existing-release", release)
        self.assertIn("gh release download", release)
        self.assertIn("actual_sha", release)
        self.assertIn("actual_bytes", release)


if __name__ == "__main__":
    unittest.main()
