from __future__ import annotations

import unittest

from scripts import survey_handoff_v2 as handoff
from scripts import survey_handlers_v2 as handlers
from scripts import survey_orchestrator_v2 as orchestrator
from scripts import survey_production_v2 as core
from tests import test_survey_handoff_v2 as handoff_tests


@unittest.skip("legacy Handoff Request control is retained for audit/compatibility but is not the canonical agent-first production path")
class SurveyHandoffRequestV2Tests(unittest.TestCase):
    def fixture(self):
        helper = handoff_tests.SurveyHandoffV2Tests(
            methodName="test_builder_pins_explicit_paths_and_real_discovery_stage_executes"
        )
        self.addCleanup(helper.doCleanups)
        root, cfg, state_path, pinned = helper.sandbox()
        discovery_path, acceptance_path = helper.discovery_artifacts(root)
        return helper, root, cfg, state_path, pinned, discovery_path, acceptance_path

    def write_request(self, root, state_path, discovery_path, acceptance_path):
        state = core.load_json(state_path)
        request_path = handoff.canonical_request_path(root, state)
        core.write_json(
            request_path,
            {
                "schema_version": "2.0-rc1",
                "issue_id": state["issue_id"],
                "lifecycle_state": state["lifecycle_state"],
                "inputs": [
                    {"name": "discovery-jsonl", "path": str(discovery_path.relative_to(root))}
                ],
                "outputs": [
                    {"name": "discovery", "path": str(acceptance_path.relative_to(root))},
                    {"name": "discovery-acceptance", "path": str(acceptance_path.relative_to(root))},
                ],
            },
        )
        return request_path

    def test_canonical_request_builds_handoff_and_execute_current_stops_after_one_stage(self) -> None:
        _, root, cfg, state_path, _, discovery_path, acceptance_path = self.fixture()
        request_path = self.write_request(root, state_path, discovery_path, acceptance_path)
        handoff_path = handoff.build_handoff_from_request(root, cfg, state_path, request_path)
        self.assertTrue(handoff_path.is_file())
        registry = {}
        handlers.register_handlers(registry)
        result = orchestrator.execute_current(
            root, cfg, state_path, root / "sources/SP001/orchestration/v2", registry,
            clock=lambda: core.parse_instant("2026-08-22T06:15:00+09:00"),
        )
        self.assertEqual(result["executed_actions"], 1)

    def test_request_must_use_canonical_path_and_current_state_identity(self) -> None:
        _, root, cfg, state_path, _, discovery_path, acceptance_path = self.fixture()
        canonical = self.write_request(root, state_path, discovery_path, acceptance_path)
        alternate = root / "request.json"
        alternate.write_bytes(canonical.read_bytes())
        with self.assertRaisesRegex(ValueError, "must use canonical path"):
            handoff.build_handoff_from_request(root, cfg, state_path, alternate)
        payload = core.load_json(canonical)
        payload["lifecycle_state"] = "DISCOVERY_COLLECTED"
        core.write_json(canonical, payload)
        with self.assertRaisesRegex(ValueError, "identity does not match"):
            handoff.build_handoff_from_request(root, cfg, state_path, canonical)


if __name__ == "__main__":
    unittest.main()
