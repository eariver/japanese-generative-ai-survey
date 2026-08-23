from __future__ import annotations

import copy
import unittest
from pathlib import Path

from scripts import survey_findings_v2 as findings
from scripts import survey_production_v2 as core


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
            "resolved_by_repair_set_id": None,
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

    def test_closed_finding_cannot_exist_without_repair_set_authority(self) -> None:
        closed = self.finding(status="CLOSED", resolved_by_repair_set_id="R-SP001-001")
        errors = findings.validate_finding(closed)
        self.assertTrue(any("Repair Set validation context" in error for error in errors), errors)

        unresolved = self.finding(status="CLOSED", resolved_by_repair_set_id=None)
        errors = findings.validate_finding(unresolved)
        self.assertTrue(any("Repair Set validation context" in error for error in errors), errors)

        premature = self.finding(status="FIXED_GENERIC", resolved_by_repair_set_id="R-SP001-001")
        errors = findings.validate_finding(premature)
        self.assertTrue(any("only CLOSED" in error for error in errors), errors)

    def test_closed_repair_set_is_the_only_valid_finding_closure_authority(self) -> None:
        repair = self.repair(status="CLOSED")
        closed = self.finding(status="CLOSED", resolved_by_repair_set_id=repair["repair_set_id"])
        self.assertEqual(findings.validate_repair_set(repair, [closed]), [])

        wrong_authority = self.finding(status="CLOSED", resolved_by_repair_set_id="R-OTHER")
        errors = findings.validate_repair_set(repair, [wrong_authority])
        self.assertTrue(any("resolved_by_repair_set_id" in error or "authority mismatch" in error for error in errors), errors)

        not_closed = self.finding(status="FIXED_GENERIC")
        errors = findings.validate_repair_set(repair, [not_closed])
        self.assertTrue(any("requires CLOSED Finding" in error for error in errors), errors)

        validated = self.repair(status="VALIDATED")
        errors = findings.validate_repair_set(validated, [closed])
        self.assertTrue(any("non-CLOSED Repair Set" in error or "Repair Set validation context" in error for error in errors), errors)

    def test_wu010r_audit_repair_set_is_machine_readable_and_not_prematurely_closed(self) -> None:
        root = Path("docs/checkpoints/survey-production-core-v2-audit-findings")
        finding_paths = [root / f"AUD-{number:03d}.json" for number in range(13, 19)]
        audit_findings = [core.load_json(path) for path in finding_paths]
        repair = core.load_json(root / "WU-010R-repair-set.json")
        self.assertEqual(repair["status"], "IMPLEMENTED")
        self.assertEqual(repair["verification_editions"], [])
        self.assertEqual(findings.validate_repair_set(repair, audit_findings), [])
        self.assertTrue(all(value["status"] == "FIXED_GENERIC" for value in audit_findings))
        self.assertTrue(all(value["resolved_by_repair_set_id"] is None for value in audit_findings))

    def test_wu011_repair_set_remains_historical_and_current_premerge_boundary_is_repository_owned(self) -> None:
        audit_root = Path("docs/checkpoints/survey-production-core-v2-audit-findings")
        audit_findings = [core.load_json(audit_root / f"AUD-{number:03d}.json") for number in range(19, 27)]
        repair = core.load_json(audit_root / "WU-011-repair-set.json")

        self.assertEqual(repair["repair_set_id"], "REPAIR-WU011-2026-08-22")
        self.assertEqual(repair["status"], "IMPLEMENTED")
        self.assertEqual(repair["verification_editions"], [])
        self.assertEqual(findings.validate_repair_set(repair, audit_findings), [])
        self.assertEqual(repair["finding_ids"], [f"AUD-{number:03d}" for number in range(19, 27)])
        self.assertTrue(all(value["status"] == "FIXED_GENERIC" for value in audit_findings))
        self.assertTrue(all(value["resolved_by_repair_set_id"] is None for value in audit_findings))

        authority = Path("docs/survey-production-core-v2-authority.md").read_text(encoding="utf-8")
        worklog = Path("docs/checkpoints/survey-production-core-v2-worklog.md").read_text(encoding="utf-8")
        closure = Path("docs/survey-production-core-v2-wu011-second-audit-closure.md").read_text(encoding="utf-8")
        bootstrap = Path("docs/survey-production-core-v2-session-bootstrap.md").read_text(encoding="utf-8")
        final_rule = Path("docs/survey-production-core-v2-final-audit-rule.md").read_text(encoding="utf-8")

        # WU-011 remains historical. The redesigned live bootstrap must not be
        # forced to preserve the W33/SP001 pilot-only CLI surface that existed
        # during the pre-merge validation campaign.
        self.assertIn("PRE-AUDIT CANDIDATE", authority)
        self.assertIn("AUD-046", authority)
        self.assertIn("AUD-047", authority)
        self.assertIn("68213aaca4ef6d47cf4c06dfe7ae501e3db78b6d", authority)
        self.assertIn("WU-011: historical `COMPLETE", worklog)
        self.assertIn("PRE-AUDIT", worklog)
        self.assertIn("Human full-candidate review of PR #310", closure)
        self.assertIn("Production versus Core-maintenance boundary", bootstrap)
        self.assertIn("Resolve targets without user ceremony", bootstrap)
        self.assertNotIn("survey_pilot_bootstrap_v2.py plan --pilot", bootstrap)
        self.assertIn("run the complete seven-point acceptance audit from zero", final_rule)
        self.assertIn("rerun all seven acceptance points from point 1", final_rule)
        self.assertIn("Human Gate round-trip viability", final_rule)
        self.assertFalse(Path("sources/2026-W33/production-state.json").exists())
        self.assertFalse(Path("sources/SP001/production-state.json").exists())


if __name__ == "__main__":
    unittest.main()
