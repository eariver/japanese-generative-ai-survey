from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts import survey_quality_v2 as quality


class SurveyQualityV2Tests(unittest.TestCase):
    def sandbox(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        schema = root / quality.QUALITY_SCHEMA
        schema.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(Path(quality.QUALITY_SCHEMA), schema)
        return temp, root

    @staticmethod
    def complete_checks() -> list[dict[str, str]]:
        return [
            {"check_id": check_id, "status": "PASS", "evidence": f"fixture evidence for {check_id}"}
            for check_id in sorted(quality.REQUIRED_CHECKS)
        ]

    def test_complete_coupled_regression_bundle_binds_exact_source_and_pdf_bytes(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        source = root / "survey/main.tex"
        pdf = root / "survey/main.pdf"
        source.parent.mkdir(parents=True)
        source.write_text("validated source\n", encoding="utf-8")
        pdf.write_bytes(b"%PDF-1.7\nfixture\n")
        output = root / "quality/regression.json"

        quality.build_bundle(root, "SP001", source, pdf, self.complete_checks(), output)
        payload = quality.validate_bundle(root, output, issue_id="SP001")

        self.assertEqual(payload["status"], "PASS")
        self.assertEqual({row["check_id"] for row in payload["checks"]}, quality.REQUIRED_CHECKS)
        self.assertEqual(payload["source"]["path"], "survey/main.tex")
        self.assertEqual(payload["pdf"]["path"], "survey/main.pdf")
        self.assertEqual(payload["pdf"]["storage"], "REPOSITORY_FILE")
        self.assertIsNone(payload["pdf"]["actions_artifact"])

    def test_actions_artifact_authority_survives_ephemeral_materialization_removal(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        source = root / "survey/main.tex"
        pdf = root / "out/materialized/main.pdf"
        source.parent.mkdir(parents=True)
        pdf.parent.mkdir(parents=True)
        source.write_text("validated source\n", encoding="utf-8")
        pdf.write_bytes(b"%PDF-1.7\nactions-fixture\n")
        authority = {
            "storage": "GITHUB_ACTIONS_ARTIFACT",
            "path": "main.pdf",
            "sha256": quality.core.sha256_file(pdf),
            "byte_count": pdf.stat().st_size,
            "actions_artifact": {
                "repository": "eariver/japanese-generative-ai-survey",
                "workflow_run_id": 32558585352,
                "artifact_id": 123456789,
                "artifact_name": "survey-SP001-v2",
                "artifact_digest": "sha256:" + "a" * 64,
            },
        }
        output = root / "quality/regression.json"
        quality.build_bundle(root, "SP001", source, pdf, self.complete_checks(), output, authority)
        pdf.unlink()

        payload = quality.validate_bundle(root, output, issue_id="SP001")
        self.assertEqual(payload["pdf"], authority)

    def test_actions_artifact_authority_must_match_inspected_pdf_bytes(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        source = root / "survey/main.tex"
        pdf = root / "out/materialized/main.pdf"
        source.parent.mkdir(parents=True)
        pdf.parent.mkdir(parents=True)
        source.write_text("validated source\n", encoding="utf-8")
        pdf.write_bytes(b"%PDF-1.7\nactions-fixture\n")
        authority = {
            "storage": "GITHUB_ACTIONS_ARTIFACT",
            "path": "main.pdf",
            "sha256": "0" * 64,
            "byte_count": pdf.stat().st_size,
            "actions_artifact": {
                "repository": "eariver/japanese-generative-ai-survey",
                "workflow_run_id": 1,
                "artifact_id": 2,
                "artifact_name": "fixture",
                "artifact_digest": "sha256:" + "b" * 64,
            },
        }
        with self.assertRaisesRegex(ValueError, "SHA does not match"):
            quality.build_bundle(root, "SP001", source, pdf, self.complete_checks(), root / "quality/regression.json", authority)

    def test_missing_member_of_coupled_family_fails_closed(self) -> None:
        checks = self.complete_checks()
        checks.pop()
        with self.assertRaisesRegex(ValueError, "coupled quality regression family incomplete"):
            quality.validate_checks(checks)

    def test_failed_check_and_duplicate_check_are_rejected(self) -> None:
        checks = self.complete_checks()
        checks[0] = dict(checks[0], status="FAIL")
        with self.assertRaisesRegex(ValueError, "quality check did not pass"):
            quality.validate_checks(checks)

        checks = self.complete_checks()
        checks.append(dict(checks[0]))
        with self.assertRaisesRegex(ValueError, "quality check IDs must be unique"):
            quality.validate_checks(checks)

    def test_post_validation_artifact_drift_invalidates_bundle(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        source = root / "survey/main.tex"
        pdf = root / "survey/main.pdf"
        source.parent.mkdir(parents=True)
        source.write_text("validated source\n", encoding="utf-8")
        pdf.write_bytes(b"%PDF-1.7\nfixture\n")
        output = root / "quality/regression.json"
        quality.build_bundle(root, "2026-W33", source, pdf, self.complete_checks(), output)

        pdf.write_bytes(pdf.read_bytes() + b"changed")
        with self.assertRaisesRegex(ValueError, "pdf bytes drifted"):
            quality.validate_bundle(root, output, issue_id="2026-W33")


if __name__ == "__main__":
    unittest.main()
