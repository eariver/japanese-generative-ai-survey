from __future__ import annotations

import unittest
from pathlib import Path
from unittest import mock

from scripts import survey_handlers_v2 as handlers
from scripts import survey_pilot_bootstrap_v2 as bootstrap
from scripts import survey_production_v2 as core
from tests.test_survey_control_gate_persistence_v2 import SurveyControlGatePersistenceV2Tests
from tests.test_survey_state_publication_authority_v2 import SurveyStatePublicationAuthorityV2Tests


class SurveyPilotBootstrapV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(".").resolve()
        cls.cfg = core.load_json(cls.root / core.DEFAULT_CONFIG)

    def test_w33_and_sp001_profiles_bootstrap_from_registry_without_starting_pilot_state(self) -> None:
        recorded_at = core.parse_instant("2026-08-22T11:18:00+09:00")
        w33 = bootstrap.build_plan(self.root, "W33", recorded_at)
        sp001 = bootstrap.build_plan(self.root, "SP001", recorded_at)

        self.assertEqual(w33["next_operation"], "INITIALIZE")
        self.assertEqual(sp001["next_operation"], "INITIALIZE")
        self.assertEqual((w33["profile"]["research_profile"], w33["profile"]["publication_profile"]), ("WEEKLY", "WEEKLY_MAGAZINE"))
        self.assertEqual((sp001["profile"]["research_profile"], sp001["profile"]["publication_profile"]), ("THEMATIC", "LONGFORM_SPECIAL"))
        self.assertEqual(w33["profile"]["research_scope"]["temporal_policy"]["cutoff"], "2026-08-14T18:00:00-04:00")
        self.assertEqual(
            sp001["profile"]["research_scope"]["temporal_policy"],
            {"mode": "OPEN_HISTORY_AS_OF", "as_of": "2026-08-22T02:18:00Z"},
        )
        self.assertEqual(w33["profile"]["paths"]["work_branch"], "weekly/2026-W33-v2-work")
        self.assertEqual(sp001["profile"]["paths"]["work_branch"], "special/SP001-v2-work")
        self.assertFalse((self.root / "sources/2026-W33/production-state.json").exists())
        self.assertFalse((self.root / "sources/SP001/production-state.json").exists())

    def test_sp001_resume_preserves_initialization_as_of_instead_of_rematerializing_now(self) -> None:
        initial = bootstrap.build_plan(
            self.root,
            "SP001",
            core.parse_instant("2026-08-22T11:18:00+09:00"),
        )["profile"]
        status = {
            "status": "RESUME_EXISTING_STATE",
            "profile_path": "sources/SP001/production-profile.json",
            "state_path": "sources/SP001/production-state.json",
            "profile_exists": True,
            "state_exists": True,
            "lifecycle_state": "DISCOVERY_COLLECTED",
        }
        with mock.patch.object(bootstrap, "_repository_status", return_value=(status, initial)):
            resumed = bootstrap.build_plan(
                self.root,
                "SP001",
                core.parse_instant("2026-08-25T19:00:00+09:00"),
            )
        self.assertEqual(resumed["next_operation"], "RESUME")
        self.assertEqual(resumed["profile"]["research_scope"]["temporal_policy"]["as_of"], "2026-08-22T02:18:00Z")
        self.assertEqual(resumed["recorded_at"], "2026-08-25T10:00:00Z")

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
        self.assertIn("Persist terminal Action Spec reached by adopted stage", production)
        self.assertIn("HUMAN_GATE_REACHED|EXCEPTION_GATE_REQUIRED|COMPLETE", production)
        self.assertIn("cmp -s \"$active\" \"$pinned\"", production)
        self.assertIn("PYTHONPATH=worktree", production)
        self.assertIn("worktree/scripts/survey_orchestrator_v2.py", production)
        self.assertIn("worktree/config/survey-production-v2-requirements.txt", production)
        self.assertIn("verify_runtime_implementation", production)
        self.assertNotIn("PYTHONPATH=control-src", production)
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
        self.assertIn("verify_runtime_implementation", release)


if __name__ == "__main__":
    unittest.main()
