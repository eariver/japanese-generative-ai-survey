from __future__ import annotations

import json
import shutil
import unittest
from pathlib import Path

from scripts import survey_discovery_v2 as discovery
from scripts import survey_handoff_v2 as handoff
from scripts import survey_handlers_v2 as handlers
from scripts import survey_orchestrator_v2 as orchestrator
from scripts import survey_production_v2 as core
from tests import test_survey_orchestrator_v2 as orchestrator_tests


@unittest.skip("legacy Handoff control is retained for audit/compatibility but is not the canonical agent-first production path")
class SurveyHandoffV2Tests(unittest.TestCase):
    def sandbox(self):
        helper = orchestrator_tests.SurveyOrchestratorV2Tests(
            methodName="test_advance_to_gate_executes_validated_stage_order_and_pins_attestations"
        )
        helper.setUp()
        temp, root, cfg, state_path, pinned = helper.sandbox()
        self.addCleanup(temp.cleanup)
        repo_root = Path(".").resolve()
        for rel in (
            "schemas/stage-handoff-v2.schema.json",
            "schemas/stage-handoff-request-v2.schema.json",
        ):
            src = repo_root / rel
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        cfg["orchestration"]["stage_plan"]["ISSUE_INITIALIZED"]["handoff_required"] = True
        return root, cfg, state_path, pinned

    @staticmethod
    def record(raw_path: str) -> dict:
        return {
            "schema_version": "2.0-rc1",
            "issue_id": "SP001",
            "discovery_id": "seed",
            "provenance": {
                "origin": "BASE",
                "research_pass": 0,
                "parent_refs": [],
                "obligation_ids": [],
                "reason": "production-handoff fixture",
            },
            "source": {
                "source_type": "paper",
                "collector_id": "fixture-collector",
                "collector_run_id": "handoff-run-1",
                "observed_at": "2026-08-22T06:00:00+09:00",
                "title": "Fixture source",
                "locator": "https://example.invalid/fixture-source",
                "raw_paths": [raw_path],
                "published_at": None,
                "summary_text": None,
                "metadata": {},
            },
        }

    def discovery_artifacts(self, root: Path):
        raw_path = root / "sources/SP001/raw/source.json"
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        raw_path.write_text('{"fixture":true}\n', encoding="utf-8")
        discovery_path = root / "sources/SP001/discovery/discovery.jsonl"
        discovery_path.parent.mkdir(parents=True, exist_ok=True)
        relative_raw = str(raw_path.relative_to(root))
        discovery_path.write_text(
            json.dumps(self.record(relative_raw), ensure_ascii=False, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        acceptance_path = root / "sources/SP001/discovery/discovery-accepted-v2.json"
        discovery.build_acceptance(root, discovery_path, "SP001", acceptance_path)
        return discovery_path, acceptance_path

    def test_planner_fails_closed_when_required_handoff_is_missing(self) -> None:
        root, cfg, state_path, _ = self.sandbox()
        with self.assertRaisesRegex(ValueError, "required Stage Handoff missing"):
            orchestrator.plan_action(root, cfg, state_path)

    def test_builder_pins_explicit_paths_and_real_discovery_stage_executes(self) -> None:
        root, cfg, state_path, _ = self.sandbox()
        discovery_path, acceptance_path = self.discovery_artifacts(root)
        path = handoff.build_handoff(
            root,
            cfg,
            state_path,
            {"discovery-jsonl": discovery_path},
            {"discovery": acceptance_path, "discovery-acceptance": acceptance_path},
        )
        self.assertEqual(path, root / "sources/SP001/orchestration/v2/handoffs/ISSUE_INITIALIZED.json")
        spec = orchestrator.plan_action(root, cfg, state_path)
        handoff_inputs = [row for row in spec["required_inputs"] if row["name"] == "stage-handoff"]
        self.assertEqual(len(handoff_inputs), 1)
        self.assertEqual(handoff_inputs[0]["path"], str(path.relative_to(root)))
        self.assertEqual(handoff_inputs[0]["sha256"], core.sha256_file(path))
        orchestration_dir = root / "sources/SP001/orchestration/v2"
        spec_path = orchestration_dir / "specs/discovery.json"
        result_path = orchestration_dir / "results/discovery.json"
        orchestrator.write_action_spec(spec_path, spec)
        registry = {}
        handlers.register_handlers(registry)
        result = orchestrator.execute_action(
            root, cfg, state_path, spec_path, result_path, registry,
            clock=lambda: core.parse_instant("2026-08-22T06:05:00+09:00"),
        )
        self.assertEqual(result["status"], "SUCCEEDED")

    def test_handoff_output_drift_fails_before_checkpoint_transition(self) -> None:
        root, cfg, state_path, _ = self.sandbox()
        discovery_path, acceptance_path = self.discovery_artifacts(root)
        handoff.build_handoff(
            root, cfg, state_path,
            {"discovery-jsonl": discovery_path},
            {"discovery": acceptance_path, "discovery-acceptance": acceptance_path},
        )
        spec = orchestrator.plan_action(root, cfg, state_path)
        spec_path = root / "sources/SP001/orchestration/v2/specs/discovery-drift.json"
        result_path = root / "sources/SP001/orchestration/v2/results/discovery-drift.json"
        orchestrator.write_action_spec(spec_path, spec)
        acceptance_path.write_text(acceptance_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        registry = {}
        handlers.register_handlers(registry)
        result = orchestrator.execute_action(
            root, cfg, state_path, spec_path, result_path, registry,
            clock=lambda: core.parse_instant("2026-08-22T06:06:00+09:00"),
        )
        self.assertEqual(result["status"], "RETRYABLE_FAILURE")

    def test_builder_rejects_noncanonical_artifact_instead_of_selecting_a_latest_run(self) -> None:
        root, cfg, state_path, _ = self.sandbox()
        discovery_path, acceptance_path = self.discovery_artifacts(root)
        alternate = root / "sources/SP001/discovery/runs/latest/discovery-accepted-v2.json"
        alternate.parent.mkdir(parents=True, exist_ok=True)
        alternate.write_bytes(acceptance_path.read_bytes())
        with self.assertRaisesRegex(ValueError, "configured artifact output must use canonical path"):
            handoff.build_handoff(
                root, cfg, state_path,
                {"discovery-jsonl": discovery_path},
                {"discovery": alternate, "discovery-acceptance": alternate},
            )


if __name__ == "__main__":
    unittest.main()
