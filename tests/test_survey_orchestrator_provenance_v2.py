from __future__ import annotations

import unittest

from scripts import survey_orchestrator_v2 as orchestrator
from scripts import survey_production_v2 as core
from tests import test_survey_orchestrator_v2 as orchestrator_tests


class SurveyOrchestratorProvenanceV2Tests(unittest.TestCase):
    def test_attested_upstream_artifact_drift_invalidates_next_action_plan(self) -> None:
        helper = orchestrator_tests.SurveyOrchestratorV2Tests(
            methodName="test_advance_to_gate_executes_validated_stage_order_and_pins_attestations"
        )
        helper.setUp()
        temp, root, cfg, state_path, _ = helper.sandbox()
        self.addCleanup(temp.cleanup)

        spec = orchestrator.plan_action(root, cfg, state_path)
        spec_path = root / "sources/SP001/orchestration/v2/specs/discovery.json"
        orchestrator.write_action_spec(spec_path, spec)
        result_path = root / "sources/SP001/orchestration/v2/results/discovery.json"
        result = orchestrator.execute_action(
            root,
            cfg,
            state_path,
            spec_path,
            result_path,
            helper.stage_registry(cfg),
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        self.assertEqual(result["status"], "SUCCEEDED")

        state = core.load_json(state_path)
        discovery_authority = state["checkpoint_provenance"]["discovery"]
        self.assertIsInstance(discovery_authority, dict)
        next_spec = orchestrator.plan_action(root, cfg, state_path)
        inputs = {row["name"]: row for row in next_spec["required_inputs"]}
        self.assertIn("checkpoint-attestation:discovery", inputs)
        self.assertEqual(
            inputs["checkpoint-attestation:discovery"]["sha256"],
            discovery_authority["sha256"],
        )

        attestation = core.load_json(root / discovery_authority["path"])
        self.assertTrue(attestation["outputs"])
        output_ref = attestation["outputs"][0]
        output_path = root / output_ref["path"]
        payload = core.load_json(output_path)
        payload["tampered_after_attestation"] = True
        core.write_json(output_path, payload)

        with self.assertRaisesRegex(
            ValueError,
            "artifact SHA drift|checkpoint attestation|Production State semantic inconsistency",
        ):
            orchestrator.plan_action(root, cfg, state_path)


if __name__ == "__main__":
    unittest.main()
