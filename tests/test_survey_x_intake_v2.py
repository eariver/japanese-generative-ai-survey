from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts import survey_production_v2 as core
from scripts import survey_x_intake_v2 as xintake


class SurveyXIntakeV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.source_root = Path(".").resolve()
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for rel in (
            core.DEFAULT_CONFIG,
            xintake.MANIFEST_SCHEMA,
            xintake.BASE_PROMPT,
            xintake.WEEKLY_PROMPT,
            xintake.SPECIAL_PROMPT,
        ):
            src = self.source_root / rel
            dst = self.root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        self.cfg = core.load_json(self.root / core.DEFAULT_CONFIG)

    def write_profile(self, issue_id: str, research: str, publication: str, survey_root: str) -> Path:
        if research == "WEEKLY":
            temporal = {
                "mode": "ROLLING_WINDOW",
                "window_start": "2026-08-14T18:00:00-04:00",
                "window_end": "2026-08-21T18:00:00-04:00",
                "cutoff": "2026-08-21T18:00:00-04:00",
                "timezone": "America/New_York",
            }
        elif research == "RETROSPECTIVE_PERIOD":
            temporal = {
                "mode": "BOUNDED_PERIOD",
                "start": "2025-07-01T00:00:00+09:00",
                "end": "2025-12-31T23:59:59+09:00",
                "as_of": "2026-08-22T09:00:00Z",
                "timezone": "Asia/Tokyo",
            }
        else:
            temporal = {"mode": "OPEN_HISTORY_AS_OF", "as_of": "2026-08-22T09:00:00Z"}
        dummy = "a" * 64
        profile = {
            "schema_version": "2.0-rc1",
            "issue_id": issue_id,
            "research_profile": research,
            "publication_profile": publication,
            "research_scope": {
                "question": "Fixture research question",
                "inclusion": [],
                "exclusion": [],
                "scope_dimensions": ["coverage"],
                "initial_obligations": [
                    {
                        "obligation_id": "fixture:coverage",
                        "dimension": "coverage",
                        "description": "Establish fixture coverage.",
                    }
                ],
                "temporal_policy": temporal,
            },
            "paths": {
                "source_root": f"sources/{issue_id}",
                "survey_root": survey_root,
                "work_branch": f"test/{issue_id}",
            },
            "contract": {
                "pipeline_contract_version": "fixture",
                "pipeline_contract_sha256": dummy,
                "quality_contract_version": "fixture",
                "quality_contract_sha256": dummy,
                "research_profile_version": "fixture",
                "research_profile_sha256": dummy,
                "publication_profile_version": "fixture",
                "publication_profile_sha256": dummy,
            },
        }
        path = self.root / profile["paths"]["source_root"] / "production-profile.json"
        core.write_json(path, profile)
        return path

    @staticmethod
    def required_spec(run_id: str = "x-pass-01", *, series_context=None) -> dict:
        return {
            "decision": "REQUIRED",
            "rationale": "X observation is material to this fixture.",
            "series_context": series_context,
            "runs": [
                {
                    "run_id": run_id,
                    "purpose": "Observe material technical community signal.",
                    "research_questions": ["What became materially salient on X?"],
                    "coverage_focus": ["independent testing", "integration"],
                    "time_scope": "fixture time scope",
                    "expected_result_filename": "grok-x-result.md",
                }
            ],
        }

    def test_weekly_requires_x_intake_and_renders_one_self_contained_drive_task(self) -> None:
        profile = self.write_profile("2026-W35", "WEEKLY", "WEEKLY_MAGAZINE", "surveys/weekly/2026-W35")
        with self.assertRaisesRegex(ValueError, "requires Grok/X Source Intake"):
            xintake.build_manifest(
                self.root,
                self.cfg,
                profile,
                {
                    "decision": "NOT_REQUIRED",
                    "rationale": "invalid weekly bypass",
                    "series_context": None,
                    "runs": [],
                },
            )
        manifest_path = xintake.build_manifest(self.root, self.cfg, profile, self.required_spec("weekly-x-2026-W35"))
        payload = xintake.validate_manifest(self.root, self.cfg, manifest_path, require_complete=False)
        self.assertEqual(payload["policy"], "REQUIRED_BY_PROFILE")
        self.assertEqual(payload["status"], "AWAITING_GROK")
        self.assertEqual(payload["drive_handoff"]["category"], "Weekly")
        run = payload["runs"][0]
        self.assertEqual(
            run["run_folder"],
            "Grok_X_SourseIntake/Weekly/2026-W35/weekly-x-2026-W35",
        )
        self.assertEqual(run["task_file_name"], "grok-task.md")
        self.assertEqual(run["drive_task_path"], run["run_folder"] + "/grok-task.md")
        self.assertNotIn("instruction", run)
        self.assertNotIn("prompt", run)
        task_path = self.root / run["task"]["path"]
        self.assertEqual(task_path.name, "grok-task.md")
        task = task_path.read_text(encoding="utf-8")
        self.assertIn(run["drive_task_path"], task)
        self.assertIn(run["run_folder"], task)
        self.assertIn("Human handoff consists only", task)
        self.assertIn("final technical Evidence authority", task)
        self.assertIn("You are **not**", task)
        self.assertIn("Coverage scan", task)
        self.assertFalse((task_path.parent / "grok-instruction.md").exists())
        self.assertFalse((task_path.parent / "grok-prompt.md").exists())

    def test_task_authority_drift_fails_closed(self) -> None:
        profile = self.write_profile("2026-W35", "WEEKLY", "WEEKLY_MAGAZINE", "surveys/weekly/2026-W35")
        manifest_path = xintake.build_manifest(self.root, self.cfg, profile, self.required_spec("weekly-x-2026-W35"))
        payload = core.load_json(manifest_path)
        task_path = self.root / payload["runs"][0]["task"]["path"]
        task_path.write_text(task_path.read_text(encoding="utf-8") + "\nDRIFT\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "task authority drift"):
            xintake.validate_manifest(self.root, self.cfg, manifest_path, require_complete=False)

    def test_result_filename_cannot_overwrite_task_file(self) -> None:
        profile = self.write_profile("SP001", "THEMATIC", "LONGFORM_SPECIAL", "surveys/special/SP001")
        spec = self.required_spec()
        spec["runs"][0]["expected_result_filename"] = "grok-task.md"
        with self.assertRaisesRegex(ValueError, "expected_result_filename invalid"):
            xintake.build_manifest(self.root, self.cfg, profile, spec)

    def test_special_can_explicitly_record_not_required(self) -> None:
        profile = self.write_profile(
            "SP-2025-H2",
            "RETROSPECTIVE_PERIOD",
            "LONGFORM_SPECIAL",
            "surveys/special/2025-H2",
        )
        manifest_path = xintake.build_manifest(
            self.root,
            self.cfg,
            profile,
            {
                "decision": "NOT_REQUIRED",
                "rationale": "Primary/historical sources fully answer this bounded fixture question; X would not add material signal.",
                "series_context": None,
                "runs": [],
            },
        )
        payload = xintake.validate_manifest(self.root, self.cfg, manifest_path)
        self.assertEqual(payload["policy"], "CHATGPT_DECIDES")
        self.assertEqual(payload["decision"], "NOT_REQUIRED")
        self.assertEqual(payload["status"], "COMPLETE")
        self.assertEqual(payload["drive_handoff"]["category"], "Retrospective_Special")

    def test_foundations_uses_dedicated_drive_category(self) -> None:
        profile = self.write_profile(
            "SP-FOUNDATIONS-V02",
            "THEMATIC",
            "LONGFORM_SPECIAL",
            "surveys/special/foundations-v02",
        )
        manifest_path = xintake.build_manifest(
            self.root,
            self.cfg,
            profile,
            self.required_spec("historical-reception-pass", series_context="GENERATIVE_AI_FOUNDATIONS"),
        )
        payload = xintake.validate_manifest(self.root, self.cfg, manifest_path, require_complete=False)
        self.assertEqual(payload["drive_handoff"]["category"], "Generative_AI_Foundations")
        self.assertTrue(payload["runs"][0]["run_folder"].startswith("Grok_X_SourseIntake/Generative_AI_Foundations/"))
        self.assertTrue(payload["runs"][0]["drive_task_path"].endswith("/grok-task.md"))

    def test_record_result_binds_imported_raw_and_completes_manifest(self) -> None:
        profile = self.write_profile("SP001", "THEMATIC", "LONGFORM_SPECIAL", "surveys/special/SP001")
        manifest_path = xintake.build_manifest(self.root, self.cfg, profile, self.required_spec())
        raw = self.root / "sources/SP001/external/x/x-pass-01/raw/grok-x-result.md"
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_text("---\nsensor: grok-x-source-intake\n---\nNo material signal.\n", encoding="utf-8")
        xintake.record_result(
            self.root,
            self.cfg,
            manifest_path,
            "x-pass-01",
            raw,
            "grok-x-result.md",
            "2026-08-22T10:00:00Z",
            "2026-08-22T10:05:00Z",
            "NO_MATERIAL_SIGNAL",
            "NO_MATERIAL_DISCOVERY",
            [],
            "The targeted X pass found no material discovery for the fixture question.",
        )
        payload = xintake.validate_manifest(self.root, self.cfg, manifest_path)
        result = payload["runs"][0]["result"]
        self.assertEqual(payload["status"], "COMPLETE")
        self.assertEqual(result["raw"]["sha256"], core.sha256_file(raw))
        self.assertEqual(result["raw"]["byte_count"], raw.stat().st_size)

    def test_required_manifest_cannot_validate_complete_before_drive_result_import(self) -> None:
        profile = self.write_profile("SP001", "THEMATIC", "LONGFORM_SPECIAL", "surveys/special/SP001")
        manifest_path = xintake.build_manifest(self.root, self.cfg, profile, self.required_spec())
        with self.assertRaisesRegex(ValueError, "not complete"):
            xintake.validate_manifest(self.root, self.cfg, manifest_path)


if __name__ == "__main__":
    unittest.main()
