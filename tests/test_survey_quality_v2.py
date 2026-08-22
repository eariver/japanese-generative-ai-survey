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
        for rel in (quality.QUALITY_SCHEMA, quality.core.DEFAULT_CONFIG):
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(Path(rel), dst)
        return temp, root

    @staticmethod
    def profile(root: Path, issue_id: str, research_profile: str, publication_profile: str) -> Path:
        path = root / "profiles" / issue_id / "production-profile.json"
        quality.core.write_json(
            path,
            {
                "schema_version": "2.0-rc1",
                "issue_id": issue_id,
                "research_profile": research_profile,
                "publication_profile": publication_profile,
                "paths": {"survey_root": f"surveys/{issue_id}"},
            },
        )
        return path

    @staticmethod
    def complete_checks(root: Path, research_profile: str, publication_profile: str) -> list[dict[str, object]]:
        cfg = quality.core.load_json(root / quality.core.DEFAULT_CONFIG)
        expected = quality.expected_checks(cfg, research_profile, publication_profile)
        rows: list[dict[str, object]] = []
        for check_id, kind in sorted(expected.items()):
            result = None
            if kind == "DETERMINISTIC":
                result_path = root / "quality/results" / f"{check_id}.json"
                quality.core.write_json(result_path, {"check_id": check_id, "status": "PASS"})
                result = {
                    "path": str(result_path.relative_to(root)),
                    "sha256": quality.core.sha256_file(result_path),
                }
            rows.append({
                "check_id": check_id,
                "kind": kind,
                "status": "PASS",
                "executor": "fixture-tool" if kind == "DETERMINISTIC" else "ChatGPT",
                "evidence": f"fixture evidence for {check_id}",
                "recorded_at": "2026-08-22T09:00:00Z",
                "result": result,
            })
        return rows

    def test_profile_applicability_excludes_longform_and_period_checks_from_weekly(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        cfg = quality.core.load_json(root / quality.core.DEFAULT_CONFIG)
        weekly = quality.expected_checks(cfg, "WEEKLY", "WEEKLY_MAGAZINE")
        self.assertIn("WEEKLY_WHY_THIS_ISSUE", weekly)
        self.assertIn("WEEKLY_RENDERED_PAGE_REVIEW", weekly)
        self.assertNotIn("TECHNICAL_NOTES_TAIL_NEEDSPACE", weekly)
        self.assertNotIn("CHRONOLOGY_SOURCE_MAPPING", weekly)
        thematic = quality.expected_checks(cfg, "THEMATIC", "LONGFORM_SPECIAL")
        self.assertIn("THEMATIC_RESEARCH_CLOSURE", thematic)
        self.assertIn("TECHNICAL_NOTES_TAIL_NEEDSPACE", thematic)
        self.assertNotIn("WEEKLY_WHY_THIS_ISSUE", thematic)

    def test_complete_quality_bundle_binds_exact_profile_source_and_pdf_bytes(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        profile = self.profile(root, "SP001", "THEMATIC", "LONGFORM_SPECIAL")
        source = root / "survey/main.tex"
        pdf = root / "survey/main.pdf"
        source.parent.mkdir(parents=True)
        source.write_text("validated source\n", encoding="utf-8")
        pdf.write_bytes(b"%PDF-1.7\nfixture\n")
        output = root / "quality/regression.json"
        checks = self.complete_checks(root, "THEMATIC", "LONGFORM_SPECIAL")

        quality.build_bundle(
            root, "SP001", source, pdf, checks, output,
            production_profile_path=profile,
        )
        payload = quality.validate_bundle(root, output, issue_id="SP001")

        self.assertEqual(payload["status"], "PASS")
        self.assertEqual(payload["research_profile"], "THEMATIC")
        self.assertEqual(payload["publication_profile"], "LONGFORM_SPECIAL")
        self.assertEqual(payload["production_profile"]["path"], str(profile.relative_to(root)))
        self.assertEqual(payload["source"]["path"], "survey/main.tex")
        self.assertEqual(payload["pdf"]["path"], "survey/main.pdf")
        self.assertEqual(payload["pdf"]["storage"], "REPOSITORY_FILE")

    def test_retrospective_period_quality_is_derived_from_bound_profile(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        profile = self.profile(root, "SP-2025-H2", "RETROSPECTIVE_PERIOD", "LONGFORM_SPECIAL")
        source = root / "survey/period.tex"
        pdf = root / "survey/period.pdf"
        source.parent.mkdir(parents=True)
        source.write_text("period source\n", encoding="utf-8")
        pdf.write_bytes(b"%PDF-1.7\nperiod\n")
        checks = self.complete_checks(root, "RETROSPECTIVE_PERIOD", "LONGFORM_SPECIAL")
        output = root / "quality/period.json"
        quality.build_bundle(
            root, "SP-2025-H2", source, pdf, checks, output,
            production_profile_path=profile,
        )
        payload = quality.validate_bundle(root, output, issue_id="SP-2025-H2")
        ids = {row["check_id"] for row in payload["checks"]}
        self.assertIn("PERIOD_SCOPE_LABEL_IDENTITY", ids)
        self.assertIn("CHRONOLOGY_SOURCE_MAPPING", ids)
        self.assertNotIn("THEMATIC_RESEARCH_CLOSURE", ids)
        self.assertEqual(payload["research_profile"], "RETROSPECTIVE_PERIOD")

    def test_profile_drift_invalidates_quality_bundle(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        profile = self.profile(root, "SP001", "THEMATIC", "LONGFORM_SPECIAL")
        source = root / "survey/main.tex"
        pdf = root / "survey/main.pdf"
        source.parent.mkdir(parents=True)
        source.write_text("validated source\n", encoding="utf-8")
        pdf.write_bytes(b"%PDF-1.7\nfixture\n")
        output = root / "quality/regression.json"
        quality.build_bundle(
            root,
            "SP001",
            source,
            pdf,
            self.complete_checks(root, "THEMATIC", "LONGFORM_SPECIAL"),
            output,
            production_profile_path=profile,
        )
        data = quality.core.load_json(profile)
        data["research_profile"] = "RETROSPECTIVE_PERIOD"
        quality.core.write_json(profile, data)
        with self.assertRaisesRegex(ValueError, "Profile authority drift"):
            quality.validate_bundle(root, output, issue_id="SP001")

    def test_deterministic_requires_result_but_agent_review_does_not(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        checks = self.complete_checks(root, "WEEKLY", "WEEKLY_MAGAZINE")
        deterministic = next(row for row in checks if row["kind"] == "DETERMINISTIC")
        deterministic["result"] = None
        cfg = quality.core.load_json(root / quality.core.DEFAULT_CONFIG)
        with self.assertRaisesRegex(ValueError, "requires result authority"):
            quality.validate_checks(root, cfg, "WEEKLY", "WEEKLY_MAGAZINE", checks)

        checks = self.complete_checks(root, "WEEKLY", "WEEKLY_MAGAZINE")
        agent = next(row for row in checks if row["kind"] == "AGENT_SEMANTIC")
        self.assertIsNone(agent["result"])
        quality.validate_checks(root, cfg, "WEEKLY", "WEEKLY_MAGAZINE", checks)

    def test_actions_artifact_authority_survives_ephemeral_materialization_removal(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        profile = self.profile(root, "SP001", "THEMATIC", "LONGFORM_SPECIAL")
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
        checks = self.complete_checks(root, "THEMATIC", "LONGFORM_SPECIAL")
        quality.build_bundle(
            root, "SP001", source, pdf, checks, output, authority,
            production_profile_path=profile,
        )
        pdf.unlink()
        payload = quality.validate_bundle(root, output, issue_id="SP001")
        self.assertEqual(payload["pdf"], authority)

    def test_actions_artifact_authority_must_match_inspected_pdf_bytes(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        profile = self.profile(root, "SP001", "THEMATIC", "LONGFORM_SPECIAL")
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
        checks = self.complete_checks(root, "THEMATIC", "LONGFORM_SPECIAL")
        with self.assertRaisesRegex(ValueError, "SHA does not match"):
            quality.build_bundle(
                root, "SP001", source, pdf, checks, root / "quality/regression.json", authority,
                production_profile_path=profile,
            )

    def test_missing_applicable_check_and_duplicate_are_rejected(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        cfg = quality.core.load_json(root / quality.core.DEFAULT_CONFIG)
        checks = self.complete_checks(root, "WEEKLY", "WEEKLY_MAGAZINE")
        checks.pop()
        with self.assertRaisesRegex(ValueError, "applicable quality review family incomplete"):
            quality.validate_checks(root, cfg, "WEEKLY", "WEEKLY_MAGAZINE", checks)

        checks = self.complete_checks(root, "WEEKLY", "WEEKLY_MAGAZINE")
        checks.append(dict(checks[0]))
        with self.assertRaisesRegex(ValueError, "unique"):
            quality.validate_checks(root, cfg, "WEEKLY", "WEEKLY_MAGAZINE", checks)

    def test_post_validation_artifact_drift_invalidates_bundle(self) -> None:
        temp, root = self.sandbox()
        self.addCleanup(temp.cleanup)
        profile = self.profile(root, "2026-W33", "WEEKLY", "WEEKLY_MAGAZINE")
        source = root / "survey/main.tex"
        pdf = root / "survey/main.pdf"
        source.parent.mkdir(parents=True)
        source.write_text("validated source\n", encoding="utf-8")
        pdf.write_bytes(b"%PDF-1.7\nfixture\n")
        output = root / "quality/regression.json"
        checks = self.complete_checks(root, "WEEKLY", "WEEKLY_MAGAZINE")
        quality.build_bundle(
            root, "2026-W33", source, pdf, checks, output,
            production_profile_path=profile,
        )
        pdf.write_bytes(pdf.read_bytes() + b"changed")
        with self.assertRaisesRegex(ValueError, "pdf bytes drifted"):
            quality.validate_bundle(root, output, issue_id="2026-W33")


if __name__ == "__main__":
    unittest.main()
