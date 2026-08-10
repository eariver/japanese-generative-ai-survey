from __future__ import annotations

import unittest

from scripts.resolve_special_source_intake_artifact import resolve


class ResolveSpecialSourceIntakeArtifactTests(unittest.TestCase):
    def sample_run(self):
        return {
            "id": 123,
            "status": "completed",
            "conclusion": "success",
            "repository": {"full_name": "eariver/japanese-generative-ai-survey"},
            "head_repository": {"full_name": "eariver/japanese-generative-ai-survey"},
            "path": ".github/workflows/special-pipeline.yml",
            "event": "workflow_dispatch",
            "head_branch": "main",
            "head_sha": "a" * 40,
            "html_url": "https://example.invalid/run/123",
        }

    def sample_artifacts(self):
        return {"artifacts": [{
            "id": 456,
            "name": "special-source-intake-2026-M07",
            "expired": False,
            "digest": "sha256:" + "b" * 64,
            "archive_download_url": "https://example.invalid/artifact.zip",
            "workflow_run": {"id": 123},
        }]}

    def test_exact_special_run_and_artifact_pass(self):
        result = resolve(
            run=self.sample_run(), artifacts=self.sample_artifacts(), repository="eariver/japanese-generative-ai-survey",
            special_id="SP-2026-M07", special_slug="2026-M07", source_run_id=123,
        )
        self.assertEqual(result["status"], "VERIFIED")
        self.assertEqual(result["artifact"]["id"], 456)

    def test_weekly_workflow_is_rejected(self):
        run = self.sample_run()
        run["path"] = ".github/workflows/weekly-pipeline.yml"
        with self.assertRaisesRegex(ValueError, "special-pipeline"):
            resolve(
                run=run, artifacts=self.sample_artifacts(), repository="eariver/japanese-generative-ai-survey",
                special_id="SP-2026-M07", special_slug="2026-M07", source_run_id=123,
            )

    def test_slug_id_mismatch_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "SP-<special_slug>"):
            resolve(
                run=self.sample_run(), artifacts=self.sample_artifacts(), repository="eariver/japanese-generative-ai-survey",
                special_id="SP-2026-M06", special_slug="2026-M07", source_run_id=123,
            )


if __name__ == "__main__":
    unittest.main()
