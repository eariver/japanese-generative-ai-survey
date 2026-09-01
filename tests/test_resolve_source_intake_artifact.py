from __future__ import annotations

import unittest

from scripts import resolve_source_intake_artifact as resolver


class ResolveSourceIntakeArtifactTests(unittest.TestCase):
    def _run(self) -> dict:
        return {
            "id": 12345,
            "status": "completed",
            "conclusion": "success",
            "repository": {"full_name": "eariver/japanese-generative-ai-survey"},
            "head_repository": {"full_name": "eariver/japanese-generative-ai-survey"},
            "path": ".github/workflows/weekly-pipeline.yml",
            "event": "workflow_dispatch",
            "head_branch": "main",
            "head_sha": "1" * 40,
            "html_url": "https://github.com/eariver/japanese-generative-ai-survey/actions/runs/12345",
        }

    def _artifact(self, **changes) -> dict:
        value = {
            "id": 67890,
            "name": "weekly-source-intake-2026-W33",
            "expired": False,
            "digest": "sha256:" + "a" * 64,
            "workflow_run": {"id": 12345},
            "archive_download_url": "https://api.github.com/repos/eariver/japanese-generative-ai-survey/actions/artifacts/67890/zip",
        }
        value.update(changes)
        return value

    def _resolve(self, *, run=None, artifacts=None):
        return resolver.resolve(
            run=run or self._run(),
            artifacts=artifacts or {"artifacts": [self._artifact()]},
            repository="eariver/japanese-generative-ai-survey",
            issue_id="2026-W33",
            source_run_id=12345,
        )

    def test_resolves_exact_successful_main_source_intake_artifact(self) -> None:
        value = self._resolve()
        self.assertEqual(value["status"], "VERIFIED")
        self.assertEqual(value["source_actions"]["workflow_run_id"], 12345)
        self.assertEqual(value["source_actions"]["head_sha"], "1" * 40)
        self.assertEqual(value["artifact"]["id"], 67890)
        self.assertEqual(value["artifact"]["digest"], "sha256:" + "a" * 64)

    def test_rejects_wrong_workflow_event_or_ref(self) -> None:
        cases = (
            ("path", ".github/workflows/other.yml", "must come from"),
            ("event", "push", "event must be"),
            ("head_branch", "feature", "head_branch must be"),
        )
        for key, bad_value, message in cases:
            with self.subTest(key=key):
                run = self._run()
                run[key] = bad_value
                with self.assertRaisesRegex(ValueError, message):
                    self._resolve(run=run)

    def test_rejects_duplicate_or_missing_expected_artifact(self) -> None:
        duplicate = {"artifacts": [self._artifact(), self._artifact(id=67891)]}
        with self.assertRaisesRegex(ValueError, "exactly one artifact"):
            self._resolve(artifacts=duplicate)
        with self.assertRaisesRegex(ValueError, "exactly one artifact"):
            self._resolve(artifacts={"artifacts": []})

    def test_rejects_expired_invalid_digest_or_wrong_run_artifact(self) -> None:
        cases = (
            ({"expired": True}, "expired"),
            ({"digest": "sha256:not-a-digest"}, "digest"),
            ({"workflow_run": {"id": 999}}, "workflow_run id mismatch"),
        )
        for changes, message in cases:
            with self.subTest(changes=changes):
                with self.assertRaisesRegex(ValueError, message):
                    self._resolve(artifacts={"artifacts": [self._artifact(**changes)]})

    def test_rejects_wrong_repository_or_run_identity(self) -> None:
        run = self._run()
        run["id"] = 111
        with self.assertRaisesRegex(ValueError, "run id mismatch"):
            self._resolve(run=run)

        run = self._run()
        run["head_repository"] = {"full_name": "someone/fork"}
        with self.assertRaisesRegex(ValueError, "head_repository mismatch"):
            self._resolve(run=run)


if __name__ == "__main__":
    unittest.main()
