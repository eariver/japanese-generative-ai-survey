from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts import survey_pilot_bootstrap_v2 as bootstrap
from scripts import survey_production_v2 as core


class SurveyPilotBootstrapV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(".").resolve()
        cls.cfg = core.load_json(cls.root / core.DEFAULT_CONFIG)

    def write_sp001_scope(self, path: Path) -> None:
        registry = bootstrap._load_registry(self.root)
        pilot = bootstrap._pilot(registry, "SP001")
        _, authority = bootstrap._planning_authority(self.root, pilot)
        core.write_json(
            path,
            {
                "schema_version": "2.0-rc1",
                "issue_id": "SP001",
                "planning_authority": authority,
                "question": "How has China's generative-AI ecosystem developed across model families, open/reuse strategies, reasoning/coding, serving efficiency, long context and developer distribution?",
                "inclusion": ["major Chinese model families and developer ecosystems", "technical and distribution strategies that materially differentiate them"],
                "exclusion": ["policy-only material without technical/ecosystem relevance"],
                "scope_dimensions": ["model/ecosystem breadth", "open/reuse boundary", "reasoning/coding", "inference/serving", "long context", "cloud/developer ecosystem"],
                "initial_obligations": [
                    {"obligation_id": "ts001:breadth", "dimension": "model/ecosystem breadth", "description": "Map material model families, organizations and lineage relationships."},
                    {"obligation_id": "ts001:reuse", "dimension": "open/reuse boundary", "description": "Distinguish open-weight, licensing, redistribution and reuse boundaries."},
                    {"obligation_id": "ts001:reasoning", "dimension": "reasoning/coding", "description": "Compare reasoning and coding trajectories where material."},
                    {"obligation_id": "ts001:serving", "dimension": "inference/serving", "description": "Cover material inference and serving-efficiency strategies."},
                    {"obligation_id": "ts001:context", "dimension": "long context", "description": "Cover long-context strategies and boundaries where material."},
                    {"obligation_id": "ts001:developer", "dimension": "cloud/developer ecosystem", "description": "Cover cloud/API/developer distribution ecosystems where material."}
                ],
                "materialized_by": "ChatGPT",
                "materialized_at": "2026-08-22T02:18:00Z"
            },
        )

    def test_w33_initializes_but_sp001_first_requires_internal_scope_materialization(self) -> None:
        recorded_at = core.parse_instant("2026-08-22T11:18:00+09:00")
        w33 = bootstrap.build_plan(self.root, "W33", recorded_at)
        sp001 = bootstrap.build_plan(self.root, "SP001", recorded_at)

        self.assertEqual(w33["next_operation"], "INITIALIZE")
        self.assertEqual((w33["profile"]["research_profile"], w33["profile"]["publication_profile"]), ("WEEKLY", "WEEKLY_MAGAZINE"))
        self.assertEqual(w33["profile"]["research_scope"]["temporal_policy"]["cutoff"], "2026-08-14T18:00:00-04:00")
        self.assertEqual(sp001["next_operation"], "MATERIALIZE_SCOPE")
        self.assertIsNone(sp001["profile"])
        self.assertEqual(sp001["scope_materialization"]["planning_authority"]["entry"], "TS-001")
        self.assertEqual(sp001["scope_materialization"]["planning_authority"]["path"], "docs/thematic-special-backlog.md")
        self.assertIn("not a Human Gate", sp001["scope_materialization"]["instruction"])
        self.assertFalse((self.root / "sources/2026-W33/production-state.json").exists())
        self.assertFalse((self.root / "sources/SP001/production-state.json").exists())

    def test_sp001_profile_is_materialized_from_current_backlog_authority_not_registry_copy(self) -> None:
        recorded_at = core.parse_instant("2026-08-22T11:18:00+09:00")
        temp = tempfile.TemporaryDirectory(dir=self.root)
        self.addCleanup(temp.cleanup)
        scope_path = Path(temp.name) / "research-scope-v2.json"
        self.write_sp001_scope(scope_path)
        with mock.patch.object(bootstrap, "_scope_spec_path", return_value=scope_path):
            plan = bootstrap.build_plan(self.root, "SP001", recorded_at)
        self.assertEqual(plan["next_operation"], "INITIALIZE")
        profile = plan["profile"]
        self.assertEqual((profile["research_profile"], profile["publication_profile"]), ("THEMATIC", "LONGFORM_SPECIAL"))
        self.assertEqual(profile["research_scope"]["temporal_policy"], {"mode": "OPEN_HISTORY_AS_OF", "as_of": "2026-08-22T02:18:00Z"})
        self.assertEqual(profile["paths"]["work_branch"], "special/SP001-v2-work")
        self.assertEqual(len(profile["research_scope"]["scope_dimensions"]), 6)
        self.assertIn("inference/serving", profile["research_scope"]["scope_dimensions"])
        self.assertIn("cloud/developer ecosystem", profile["research_scope"]["scope_dimensions"])

    def test_sp001_resume_preserves_initialization_as_of_after_tool_upgrade(self) -> None:
        temp = tempfile.TemporaryDirectory(dir=self.root)
        self.addCleanup(temp.cleanup)
        scope_path = Path(temp.name) / "research-scope-v2.json"
        self.write_sp001_scope(scope_path)
        registry = bootstrap._load_registry(self.root)
        pilot = bootstrap._pilot(registry, "SP001")
        with mock.patch.object(bootstrap, "_scope_spec_path", return_value=scope_path):
            initial = bootstrap._materialize_profile(self.root, self.cfg, pilot, core.parse_instant("2026-08-22T11:18:00+09:00"))
        status = {
            "status": "RESUME_EXISTING_STATE",
            "profile_path": "sources/SP001/production-profile.json",
            "state_path": "sources/SP001/production-state.json",
            "profile_exists": True,
            "state_exists": True,
            "lifecycle_state": "DISCOVERY_COLLECTED",
        }
        with mock.patch.object(bootstrap, "_repository_status", return_value=(status, initial)):
            resumed = bootstrap.build_plan(self.root, "SP001", core.parse_instant("2026-08-25T19:00:00+09:00"))
        self.assertEqual(resumed["next_operation"], "RESUME")
        self.assertEqual(resumed["profile"]["research_scope"]["temporal_policy"]["as_of"], "2026-08-22T02:18:00Z")
        self.assertEqual(resumed["recorded_at"], "2026-08-25T10:00:00Z")

    def test_agent_first_control_is_canonical_and_legacy_handoff_is_not_contract_authority(self) -> None:
        operator = self.cfg["operator_model"]
        self.assertEqual(operator["primary_operator"], "CHATGPT")
        self.assertEqual(operator["local_stage_control"], "COMPACT_AGENT_CHECKPOINT")
        self.assertTrue(operator["autonomous_until_gate"])
        self.assertEqual(operator["normal_human_gates"], ["ARCHITECTURE_REVIEW", "PUBLICATION_PREVIEW"])
        pipeline_files = set(self.cfg["contract_files"]["pipeline"])
        self.assertIn("schemas/stage-checkpoint-v2.schema.json", pipeline_files)
        self.assertNotIn("schemas/action-spec-v2.schema.json", pipeline_files)
        self.assertNotIn("schemas/stage-handoff-v2.schema.json", pipeline_files)
        self.assertNotIn("schemas/stage-validation-attestation-v2.schema.json", pipeline_files)
        self.assertTrue(
            all(stage.get("handoff_required") is False for stage in self.cfg["orchestration"]["stage_plan"].values()),
            "canonical agent-first stage plan must not require legacy Stage Handoffs",
        )

    def test_workflow_authority_is_mechanical_and_release_is_the_only_stage_dispatch(self) -> None:
        control = self.cfg["workflow_control"]
        self.assertEqual(control["dispatch_ref"], "main")
        self.assertEqual(control["handler_dispatch"], {"stage:release": "survey-production-v2-release.yml"})
        self.assertEqual(control["release_reconciliation"], {"external_key": "release_identity", "existing_release_policy": "VERIFY_EXACT_BYTES_THEN_RESUME"})
        self.assertNotIn("assistant_control_workflow", control)
        self.assertNotIn("production_control_workflow", control)
        self.assertEqual(
            control["publication_preview_export_workflow"],
            "survey-production-v2-export-publication-preview.yml",
        )
        release_path = self.root / ".github/workflows" / control["release_workflow"]
        preview_path = self.root / ".github/workflows" / control["publication_preview_export_workflow"]
        self.assertTrue(release_path.is_file())
        self.assertTrue(preview_path.is_file())
        release = release_path.read_text(encoding="utf-8")
        self.assertIn("GITHUB_ACTIONS_ARTIFACT", release)
        self.assertIn("VERIFY_EXACT_BYTES_THEN_RESUME", release)
        self.assertIn("gh release download", release)
        self.assertIn("survey_release_checkpoint_v2.py", release)
        self.assertNotIn("survey_handoff_v2.py", release)
        self.assertNotIn("survey_orchestrator_v2.py", release)
        stage_plan = self.cfg["orchestration"]["stage_plan"]
        workflow_stages = [name for name, stage in stage_plan.items() if stage["action_kind"] == "WORKFLOW_DISPATCH"]
        self.assertEqual(workflow_stages, ["FROZEN"])
        self.assertEqual(stage_plan["FROZEN"]["handler"], "stage:release")

    def test_retired_core_v2_mutation_workflows_are_absent(self) -> None:
        retired = {
            "survey-production-v2-control.yml",
            "assistant-control-v2.yml",
            "survey-production-v2-work-branch-control.yml",
            "survey-production-v2-work-branch-human-gate.yml",
            "survey-production-v2-interactive-screening.yml",
            "survey-production-v2-interactive-evidence.yml",
            "survey-production-v2-interactive-selection-architecture.yml",
            "survey-production-v2-interactive-drafting-synthesis.yml",
            "survey-production-v2-interactive-semantic-publication.yml",
            "survey-production-v2-interactive-weekly-semantic-publication.yml",
            "survey-production-v2-interactive-semantic-quality.yml",
        }
        workflow_root = self.root / ".github/workflows"
        present = {path.name for path in workflow_root.glob("*.yml")}
        self.assertTrue(retired.isdisjoint(present), sorted(retired & present))
        contract_text = (self.root / "config/survey-production-v2.json").read_text(encoding="utf-8")
        for filename in retired:
            self.assertNotIn(filename, contract_text)

    def test_core_v2_cross_regression_wiring_preserves_current_weekly_production_controls(self) -> None:
        weekly = (self.root / ".github/workflows/weekly-pipeline.yml").read_text(encoding="utf-8")
        self.assertIn("scripts/survey_*_v2.py", weekly)
        self.assertIn("config/survey-production-v2-requirements.txt", weekly)
        self.assertIn("Install Survey Production Core v2 test dependencies", weekly)
        self.assertIn("Generate Grok Trend Sensor run instruction when collection anchor is available", weekly)
        self.assertIn("actions/upload-artifact@v7", weekly)
        self.assertIn("retention-days: 14", weekly)
        self.assertIn("--plan out/source-intake-control/plan.json", weekly)
        self.assertIn("scripts/build_screening_index.py", weekly)
        self.assertIn("out/weekly-pipeline/validation.json", weekly)
        self.assertIn("raw-provenance-report.json", weekly)
        self.assertIn("if: inputs.command == 'raw-index'", weekly)
        self.assertIn("if: inputs.command == 'raw-check'", weekly)


if __name__ == "__main__":
    unittest.main()
