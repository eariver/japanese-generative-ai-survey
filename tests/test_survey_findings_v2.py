from __future__ import annotations

import copy
import unittest

from scripts import survey_findings_v2 as findings


class SurveyFindingsV2Tests(unittest.TestCase):
    @staticmethod
    def finding(**overrides):
        value = {
            "schema_version": "2.0-rc1",
            "finding_id": "F-SP001-001",
            "edition": "SP001",
            "stage": "ARCHITECTURE_REVIEW",
            "observed_problem": "A material branch disappeared from the proposed structure.",
            "expected_behavior": "Every material branch remains selected, held, rejected with rationale, or explicitly limited.",
            "actual_behavior": "The branch had no visible destination.",
            "production_workaround": "Human reviewer restored the branch manually.",
            "classification": {
                "scope": "CORE",
                "defect_kind": "TRACEABILITY",
                "confidence": "high",
            },
            "requires_regression": True,
            "provenance": {
                "source_commit": "a" * 40,
                "relevant_artifacts": ["sources/SP001/materiality-ledger.json"],
                "human_review_reference": "review:SP001:architecture:1",
            },
            "improvement_action": "Fail closed when material candidates disappear before Architecture.",
            "regression_fixture": "tests/test_sp001_materiality_traceability.py",
            "status": "FIXED_GENERIC",
        }
        value.update(overrides)
        return value

    @staticmethod
    def repair(**overrides):
        value = {
            "schema_version": "2.0-rc1",
            "repair_set_id": "R-SP001-001",
            "finding_ids": ["F-SP001-001"],
            "affected_components": ["Candidate Matrix", "Architecture"],
            "actual_layers_changed": ["CORE"],
            "disposition": "CORE_FIX",
            "implementation_commits": ["b" * 40],
            "regression_fixtures": ["tests/test_sp001_materiality_traceability.py"],
            "compatibility_impact": "No frozen release is rewritten; future Core v2 editions fail closed.",
            "validation_results": [
                {"check": "dedicated regression", "status": "PASS", "reference": "ci:123"}
            ],
            "verification_editions": ["W33", "SP001"],
            "status": "VALIDATED",
        }
        value.update(overrides)
        return value

    def test_finding_taxonomy_keeps_scope_and_regression_orthogonal(self) -> None:
        value = self.finding()
        self.assertEqual(findings.validate_finding(value), [])
        self.assertEqual(value["classification"]["scope"], "CORE")
        self.assertTrue(value["requires_regression"])

        bad = copy.deepcopy(value)
        bad["classification"]["scope"] = "REGRESSION_REQUIRED"
        self.assertTrue(findings.validate_finding(bad))

    def test_fixed_regression_finding_requires_fixture_and_classification(self) -> None:
        missing_fixture = self.finding(regression_fixture=None)
        errors = findings.validate_finding(missing_fixture)
        self.assertTrue(any("regression_fixture" in error for error in errors), errors)

        unclassified = self.finding()
        unclassified["classification"]["scope"] = "UNCLASSIFIED"
        errors = findings.validate_finding(unclassified)
        self.assertTrue(any("classified scope" in error for error in errors), errors)

    def test_repair_set_must_resolve_exact_findings_and_required_regressions(self) -> None:
        finding = self.finding()
        repair = self.repair()
        self.assertEqual(findings.validate_repair_set(repair, [finding]), [])

        missing_fixture = copy.deepcopy(repair)
        missing_fixture["regression_fixtures"] = []
        errors = findings.validate_repair_set(missing_fixture, [finding])
        self.assertTrue(any("required regression fixture" in error for error in errors), errors)

        missing_finding = copy.deepcopy(repair)
        errors = findings.validate_repair_set(missing_finding, [])
        self.assertTrue(any("exactly the Findings" in error for error in errors), errors)

    def test_validated_repair_requires_all_pass_and_verification_editions(self) -> None:
        finding = self.finding()
        repair = self.repair()
        repair["validation_results"][0]["status"] = "PENDING"
        errors = findings.validate_repair_set(repair, [finding])
        self.assertTrue(any("all-PASS" in error for error in errors), errors)

        repair = self.repair(verification_editions=[])
        errors = findings.validate_repair_set(repair, [finding])
        self.assertTrue(any("verification_editions" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
