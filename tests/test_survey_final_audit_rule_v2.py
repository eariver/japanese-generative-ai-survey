from __future__ import annotations

import unittest
from pathlib import Path


class SurveyFinalAuditRuleV2Tests(unittest.TestCase):
    def test_repository_owns_all_changes_first_fixed_head_six_point_audit(self) -> None:
        rule = Path("docs/survey-production-core-v2-final-audit-rule.md").read_text(encoding="utf-8")
        authority = Path("docs/survey-production-core-v2-authority.md").read_text(encoding="utf-8")
        agents = Path("AGENTS.md").read_text(encoding="utf-8")
        bootstrap = Path("docs/survey-production-core-v2-session-bootstrap.md").read_text(encoding="utf-8")

        for phrase in (
            "finish every intended candidate change",
            "freeze one candidate branch head SHA",
            "run the complete six-point acceptance audit from zero",
            "Autonomous progression / stop discipline",
            "mark the current final audit INVALIDATED",
            "rerun all six acceptance points from point 1",
        ):
            self.assertIn(phrase, rule)

        self.assertIn("survey-production-core-v2-final-audit-rule.md", authority)
        self.assertIn("2f3c9b10c031cf0d8e5cc114fb93e481e90fffac", authority)
        self.assertIn("68213aaca4ef6d47cf4c06dfe7ae501e3db78b6d", authority)
        self.assertIn("705937af2eb45d5ba361fe748d7a622110bcb27c", authority)
        self.assertIn("AUD-047", authority)
        self.assertIn("audit-stable pre-audit state", authority)
        self.assertIn("PR/Human-review metadata", authority)
        self.assertIn("invalidate the entire audit", agents)
        self.assertIn("rerun all six points from point 1", agents)
        self.assertIn("Do not stop for ordinary internal work", agents)
        self.assertIn("continue immediately unless a Human/Exception Gate is reached", bootstrap)
        self.assertIn("manual Grok", rule)
        self.assertIn("resumes automatically toward the requested Gate", rule)
        self.assertIn("must not search for a Grok connector", rule)

    def test_final_result_is_external_metadata_not_post_audit_candidate_commit(self) -> None:
        rule = Path("docs/survey-production-core-v2-final-audit-rule.md").read_text(encoding="utf-8")
        self.assertIn("recorded outside the candidate tree", rule)
        self.assertIn("PR/Human-review handoff", rule)
        self.assertIn("candidate SHA changes", rule)


if __name__ == "__main__":
    unittest.main()
