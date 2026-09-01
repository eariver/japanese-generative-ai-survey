from __future__ import annotations

import unittest

from scripts import survey_production_v2 as core
from tests import test_survey_production_v2 as production_tests


IMPLEMENTATION_SHA = "1" * 40


class SurveyWU008ContractIdentityTests(unittest.TestCase):
    def test_architecture_schema_drift_invalidates_initialized_state(self) -> None:
        helper = production_tests.SurveyProductionV2FoundationTests(
            methodName="test_contract_manifest_declares_two_human_gates_and_non_authoritative_legacy_state"
        )
        helper.setUp()
        temp, root = helper.make_sandbox()
        self.addCleanup(temp.cleanup)
        cfg = core.load_json(root / "config/survey-production-v2.json")
        profile = core.thematic_profile(
            root,
            cfg,
            {
                "issue_id": "SP001",
                "question": "explicit WU-008 contract identity fixture",
                "temporal_mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-08-22T02:00:00+09:00",
                "scope_dimensions": ["lineage"],
            },
        )
        _, state_path = core.initialize(
            root,
            cfg,
            profile,
            IMPLEMENTATION_SHA,
            "ARCHITECTURE_REVIEW",
            core.parse_instant("2026-08-22T02:05:00+09:00"),
        )
        state = core.load_json(state_path)
        contract_path = root / "schemas/issue-architecture-v2.schema.json"
        contract_path.write_text(
            contract_path.read_text(encoding="utf-8") + "\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValueError, "semantic contract files differ"):
            core.transition_state(
                root,
                cfg,
                state,
                "DISCOVERY_COLLECTED",
                IMPLEMENTATION_SHA,
                core.parse_instant("2026-08-22T02:10:00+09:00"),
            )


if __name__ == "__main__":
    unittest.main()
