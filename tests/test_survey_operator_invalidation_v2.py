from __future__ import annotations

import unittest

from scripts import survey_human_gate_v2 as human_gate
from scripts import survey_production_v2 as core
from tests import test_survey_human_gate_v2 as human_fixture


class OperatorPendingGateInvalidationTests(unittest.TestCase):
    @staticmethod
    def _fixture() -> human_fixture.SurveyHumanGateV2Tests:
        human_fixture.SurveyHumanGateV2Tests.setUpClass()
        fixture = human_fixture.SurveyHumanGateV2Tests()
        fixture.setUp()
        operator_source = fixture.source_root / "operator-source"
        operator_survey = fixture.source_root / "operator-survey"
        profile = core.thematic_profile(
            fixture.root,
            fixture.cfg,
            {
                "issue_id": fixture.issue_id,
                "question": "Can a pending Architecture Gate be safely invalidated?",
                "temporal_mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-08-24T00:00:00Z",
                "scope_dimensions": ["operator invalidation"],
                "source_root": operator_source.relative_to(fixture.root).as_posix(),
                "survey_root": operator_survey.relative_to(fixture.root).as_posix(),
                "work_branch": fixture.branch,
            },
        )
        fixture.profile_path, fixture.state_path = core.initialize(
            fixture.root,
            fixture.cfg,
            profile,
            fixture.impl,
            "ARCHITECTURE_REVIEW",
            core.parse_instant("2026-08-24T00:00:00Z"),
        )
        fixture.source_root = operator_source
        fixture.source_rel = operator_source.relative_to(fixture.root).as_posix()
        fixture.survey_root = operator_survey
        fixture.survey_rel = operator_survey.relative_to(fixture.root).as_posix()
        return fixture

    def test_operator_invalidation_requires_the_exact_pending_gate_state(self) -> None:
        fixture = self._fixture()
        self.addCleanup(fixture.doCleanups)

        with self.assertRaisesRegex(ValueError, "requires pending ARCHITECTURE_ESTABLISHED"):
            human_gate.invalidate_pending_gate(
                fixture.root,
                fixture.cfg,
                fixture.state_path,
                "ARCHITECTURE_REVIEW",
                "CANDIDATES_NORMALIZED",
                "fixture precondition test",
                "operator-test",
                fixture.impl,
                invalidated_commit_sha=fixture.impl,
            )

    def test_operator_invalidation_rejects_boundary_outside_configured_safe_set(self) -> None:
        fixture = self._fixture()
        self.addCleanup(fixture.doCleanups)
        fixture._advance_to_selection()
        fixture._reach_architecture_gate("Architecture pending surface", "2026-08-24T00:05:00Z")
        before = core.load_json(fixture.state_path)

        with self.assertRaisesRegex(ValueError, "not allowed for ARCHITECTURE_REVIEW"):
            human_gate.invalidate_pending_gate(
                fixture.root,
                fixture.cfg,
                fixture.state_path,
                "ARCHITECTURE_REVIEW",
                "DRAFT_COMPLETE",
                "fixture invalid boundary",
                "operator-test",
                fixture.impl,
                invalidated_commit_sha=fixture.impl,
            )

        self.assertEqual(core.load_json(fixture.state_path), before)
        self.assertEqual(
            core.load_json(fixture.source_root / fixture.cfg["state_authority"]["human_review_index_path"])
            if (fixture.source_root / fixture.cfg["state_authority"]["human_review_index_path"]).exists()
            else {"reviews": []},
            {"reviews": []},
        )


if __name__ == "__main__":
    unittest.main()
