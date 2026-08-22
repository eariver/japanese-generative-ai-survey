from __future__ import annotations

import unittest
from pathlib import Path

from scripts import survey_orchestrator_v2 as orchestrator
from scripts import survey_production_v2 as core
from tests.test_survey_orchestrator_v2 import SurveyOrchestratorV2Tests


class SurveyControlGatePersistenceV2Tests(unittest.TestCase):
    def test_one_stage_adoption_then_terminal_persistence_reaches_gate_without_drafting(self) -> None:
        helper = SurveyOrchestratorV2Tests(methodName="test_advance_to_gate_executes_validated_stage_order_and_pins_attestations")
        helper.repo_root = Path(".").resolve()
        temp, root, cfg, state_path, _ = helper.sandbox()
        self.addCleanup(temp.cleanup)
        registry = helper.stage_registry(cfg)
        orchestration_dir = root / "sources/SP001/orchestration/v2"
        clock = lambda: core.parse_instant("2026-08-22T03:05:00+09:00")

        for _ in range(4):
            result = orchestrator.execute_current(root, cfg, state_path, orchestration_dir, registry, clock=clock)
            self.assertEqual(result["executed_actions"], 1)
        self.assertEqual(core.load_json(state_path)["lifecycle_state"], "SELECTION_COMPLETE")

        architecture = orchestrator.execute_current(root, cfg, state_path, orchestration_dir, registry, clock=clock)
        self.assertEqual(architecture["executed_actions"], 1)
        state = core.load_json(state_path)
        self.assertEqual(state["lifecycle_state"], "ARCHITECTURE_ESTABLISHED")
        self.assertEqual(state["terminal_reason"], "HUMAN_GATE_REACHED")
        self.assertEqual(state["machine_checkpoints"]["draft"], "pending")

        terminal = orchestrator.execute_current(root, cfg, state_path, orchestration_dir, registry, clock=clock)
        self.assertEqual(terminal["executed_actions"], 0)
        self.assertEqual(terminal["terminal_reason"], "HUMAN_GATE_REACHED")
        self.assertIsNone(terminal["action_result_path"])

        specs = sorted((orchestration_dir / "specs").glob("*.json"))
        results = sorted((orchestration_dir / "results").glob("*.json"))
        self.assertEqual(len(specs), 6)
        self.assertEqual(len(results), 5)
        terminal_spec = core.load_json(specs[-1])
        self.assertEqual(terminal_spec["action_kind"], "HUMAN_GATE")
        self.assertEqual(terminal_spec["handler"], "human:architecture-review")
        self.assertEqual(core.load_json(state_path)["machine_checkpoints"]["draft"], "pending")


if __name__ == "__main__":
    unittest.main()
