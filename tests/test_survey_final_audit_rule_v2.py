from __future__ import annotations

import unittest
from pathlib import Path


class SurveyFinalAuditRuleV2Tests(unittest.TestCase):
    def test_repository_owns_fixed_head_seven_point_audit_contract(self) -> None:
        rule = Path("docs/survey-production-core-v2-final-audit-rule.md").read_text(encoding="utf-8")
        agents = Path("AGENTS.md").read_text(encoding="utf-8")
        bootstrap = Path("docs/survey-production-core-v2-session-bootstrap.md").read_text(encoding="utf-8")

        for phrase in (
            "finish all candidate changes",
            "freeze one candidate head SHA",
            "run all seven acceptance points from zero",
            "Weekly viability",
            "Special viability",
            "Generality",
            "Historical/clarified recurrence prevention",
            "Control proportionality",
            "Autonomous progression / stop discipline",
            "Human Gate round-trip viability",
            "No PASS verdict may be carried forward after mutation",
        ):
            self.assertIn(phrase, rule)

        self.assertIn("recorded outside the candidate tree", rule)
        self.assertIn("rerun Points 1–7 from Point 1", rule)
        self.assertIn("invalidate", rule.lower())
        self.assertIn("invalidates the entire audit", agents)
        self.assertIn("Do not stop for ordinary internal work", agents)
        self.assertIn("Routine search refinement", bootstrap)
        self.assertIn("are not extra Human Gates", bootstrap)
        self.assertIn("A formal production-validation run that hits a shared-Core defect is failed evidence", bootstrap)

    def test_point7_owns_trust_durability_cross_gate_and_runtime_isolation(self) -> None:
        rule = Path("docs/survey-production-core-v2-final-audit-rule.md").read_text(encoding="utf-8")

        # Direct-local durable review provenance.
        self.assertIn("dangling/unreachable reviewed commit", rule)
        self.assertIn("canonical `work_branch`", rule)
        self.assertIn("Candidate-bound PDF", rule)

        # Publication feedback may legitimately reopen Architecture.
        self.assertIn("Publication Preview — upstream/cross-gate repair", rule)
        self.assertIn("Architecture Review becomes pending", rule)
        self.assertIn("Architecture rN+1", rule)
        self.assertIn("cross-gate reopen is normal revision", rule)

        # Connector trust remains default-branch authority with two bounded transports.
        self.assertIn("single `survey-production-v2-operator-bridge.yml` workflow loaded from default-branch authority", rule)
        self.assertIn("Issue `#448`", rule)
        self.assertIn("/survey-core-execute <lowercase-40-hex-request-commit>", rule)
        self.assertIn("`pull_request_target`", rule)
        self.assertIn("same-repository PRs targeting `main`", rule)
        self.assertIn("Survey Core operator transport:", rule)
        self.assertIn("exact current canonical work-branch head", rule)
        self.assertIn("protected-path configuration is read from the named reviewed-main commit", rule)
        self.assertIn("only a dependent post-preflight job receives `contents: write`", rule)
        self.assertIn("lease-bound", rule)
        self.assertIn("there is no work-branch signal workflow and no `workflow_run` trust hop", rule)
        self.assertIn("exactly seven workflows", rule)

        # RVF-026 extends the trust root through Python startup/import behavior.
        self.assertIn("isolated Python startup", rule)
        self.assertIn("cannot import repository-local work-branch code", rule)
        self.assertIn("separately materialized reviewed-main runtime", rule)
        self.assertIn("not from the admitted worktree import root", rule)
        self.assertIn("poisoning top-level `json.py`", rule)
        self.assertIn("exact package-module subprocess startup smoke", rule)
        self.assertIn("RVF-026 import-poisoning regression", rule)

        # Canonical Thematic materialization is part of current special viability.
        self.assertIn("Canonical Thematic initialization", rule)
        self.assertIn("thematic-scope-spec-v2", rule)
        self.assertIn("planning-authority entry and SHA-256 are revalidated", rule)
        self.assertIn("`as_of` is derived from immutable request `recorded_at`", rule)

    def test_actions_surface_remains_seven_and_pipeline_ci_only(self) -> None:
        rule = Path("docs/survey-production-core-v2-final-audit-rule.md").read_text(encoding="utf-8")
        for workflow in (
            "pipeline-contract-tests.yml",
            "survey-production-v2-ci.yml",
            "build-weekly-survey.yml",
            "build-special-pdf.yml",
            "survey-production-v2-export-publication-preview.yml",
            "survey-production-v2-release.yml",
            "survey-production-v2-operator-bridge.yml",
        ):
            self.assertIn(workflow, rule)
        self.assertIn("`pipeline-contract-tests.yml` = independent read-only CI only", rule)
        self.assertIn("trusted default-branch dual activation", rule)
        self.assertIn("An eighth workflow is prima facie regression", rule)

    def test_current_rule_does_not_retain_superseded_acceptance_or_transport(self) -> None:
        rule = Path("docs/survey-production-core-v2-final-audit-rule.md").read_text(encoding="utf-8")
        self.assertNotIn("complete six-point acceptance audit", rule)
        self.assertNotIn("rerun all six acceptance points", rule)
        self.assertNotIn("six fresh verdicts", rule)
        self.assertNotIn("operator-bridge workflow = read-only work-branch signal", rule)
        self.assertNotIn("pipeline-contract workflow = normal CI plus trusted", rule)
        self.assertIn("109579e0f9b2988b62074165b28f144ac3b1ad55", rule)
        self.assertIn("historical evidence", rule)
        self.assertIn("no earlier 7/7 verdict may be reused", rule)


if __name__ == "__main__":
    unittest.main()
