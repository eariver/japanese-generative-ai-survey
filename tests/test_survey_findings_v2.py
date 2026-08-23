from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import survey_findings_v2 as findings
from scripts import survey_production_v2 as core


class SurveyFindingsV2Tests(unittest.TestCase):
    def finding(self, *, finding_id: str = "AUD-900", status: str = "OPEN", requires_regression: bool = True) -> dict:
        return {
            "schema_version": "2.0-rc1",
            "finding_id": finding_id,
            "work_unit": "WU-TEST",
            "scope": "CORE",
            "source_commit_sha": "a" * 40,
            "found_by": "TEST",
            "summary": "fixture",
            "details": "fixture",
            "defect_kind": "CONTRACT",
            "confidence": "high",
            "requires_regression": requires_regression,
            "regression_fixture": "tests/test_fixture.py" if requires_regression else None,
            "status": status,
            "resolved_by_repair_set_id": "REPAIR-TEST" if status == "CLOSED" else None,
        }

    def repair(self, *, status: str = "IMPLEMENTED", finding_ids: list[str] | None = None) -> dict:
        ids = finding_ids or ["AUD-900"]
        return {
            "schema_version": "2.0-rc1",
            "repair_set_id": "REPAIR-TEST",
            "work_unit": "WU-TEST",
            "finding_ids": ids,
            "status": status,
            "repair_commit_sha": "b" * 40,
            "verification_editions": [],
            "verification_results": [],
        }

    def test_finding_taxonomy_keeps_scope_and_regression_orthogonal(self) -> None:
        payload = self.finding(requires_regression=False)
        self.assertEqual(findings.validate_finding(payload), [])
        payload["scope"] = "EDITION_LOCAL"
        payload["requires_regression"] = True
        payload["regression_fixture"] = "tests/test_issue_specific_regression.py"
        self.assertEqual(findings.validate_finding(payload), [])

    def test_fixed_regression_finding_requires_fixture_and_classification(self) -> None:
        payload = self.finding(status="FIXED_GENERIC")
        payload["regression_fixture"] = None
        errors = findings.validate_finding(payload)
        self.assertTrue(any("regression_fixture" in error for error in errors), errors)

    def test_closed_finding_cannot_exist_without_repair_set_authority(self) -> None:
        payload = self.finding(status="CLOSED")
        self.assertEqual(payload["resolved_by_repair_set_id"], "REPAIR-TEST")
        self.assertEqual(findings.validate_finding(payload), [])

        payload["resolved_by_repair_set_id"] = None
        errors = findings.validate_finding(payload)
        self.assertTrue(any("resolved_by_repair_set_id" in error for error in errors), errors)

    def test_validated_repair_requires_all_pass_and_verification_editions(self) -> None:
        closed = self.finding(status="CLOSED")
        repair = self.repair(status="VALIDATED")
        repair["verification_editions"] = ["2026-W34"]
        repair["verification_results"] = [{"edition_id": "2026-W34", "status": "FAIL", "evidence": "fixture"}]
        errors = findings.validate_repair_set(repair, [closed])
        self.assertTrue(any("all PASS" in error for error in errors), errors)

        repair["verification_results"][0]["status"] = "PASS"
        self.assertEqual(findings.validate_repair_set(repair, [closed]), [])

    def test_closed_repair_set_is_the_only_valid_finding_closure_authority(self) -> None:
        closed = self.finding(status="CLOSED")
        repair = self.repair(status="CLOSED")
        errors = findings.validate_repair_set(repair, [closed])
        self.assertEqual(errors, [])

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
        self.assertIn("run the complete six-point acceptance audit from zero", final_rule)
        self.assertIn("rerun all six acceptance points from point 1", final_rule)
        self.assertFalse(Path("sources/2026-W33/production-state.json").exists())
        self.assertFalse(Path("sources/SP001/production-state.json").exists())


if __name__ == "__main__":
    unittest.main()
