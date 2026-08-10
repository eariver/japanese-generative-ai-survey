from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import accept_source_intake_artifact as acceptor


class SourceIntakeAcceptanceTests(unittest.TestCase):
    def _json(self, path: Path, value) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def _plan(self, issue: str) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": issue,
            "generated_at": "2026-08-15T09:00:00+00:00",
            "generated_at_local": "2026-08-15T18:00:00+09:00",
            "editorial_cutoff": "2026-08-14T18:00:00-04:00",
            "editorial_cutoff_timezone": "America/New_York",
            "collection_window_start": "2026-08-09T23:40:00+09:00",
            "collection_window_end": "2026-08-15T18:00:00+09:00",
            "automation_mode": "plan-only",
            "unattended_public_release": False,
            "notes": [],
        }

    def _artifact(self, root: Path, issue: str = "2026-W33") -> Path:
        artifact = root / "artifact"
        source_intake = artifact / "source-intake"
        self._json(artifact / "source-intake-control" / "plan.json", self._plan(issue))
        self._json(
            source_intake / "source-intake-report.json",
            {
                "schema_version": "1.0",
                "issue_id": issue,
                "collector_count": 2,
                "runs": [
                    {"run_id": f"arxiv-api-{issue}-run", "collector": "arxiv-api", "status": "success"},
                    {"run_id": f"official-pages-{issue}-run", "collector": "official-pages", "status": "success"},
                ],
                "overall_status": "success",
            },
        )
        arxiv = source_intake / "sources" / issue / "collectors" / "arxiv" / "runs" / "20260815T000000Z"
        self._json(
            arxiv / "collector-run.json",
            {
                "issue_id": issue,
                "run_id": f"arxiv-api-{issue}-run",
                "collector": {"id": "arxiv-api"},
            },
        )
        self._json(arxiv / "summary.json", {"entries": []})
        raw = arxiv / "raw" / "cs-ai.atom"
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_bytes(b"<feed>raw-arxiv</feed>")

        official = source_intake / "sources" / issue / "collectors" / "official-pages" / "runs" / "20260815T000100Z"
        self._json(
            official / "collector-run.json",
            {
                "issue_id": issue,
                "run_id": f"official-pages-{issue}-run",
                "collector": {"id": "official-pages"},
            },
        )
        self._json(official / "summary.json", {"pages": []})
        official_raw = official / "raw" / "vendor.html"
        official_raw.parent.mkdir(parents=True, exist_ok=True)
        official_raw.write_bytes(b"<html>raw-official</html>")

        # Derived screening data may exist in the artifact, but acceptance must not commit it.
        screening = artifact / "source-intake-screening"
        self._json(screening / "screening-manifest.json", {"issue_id": issue, "record_count": 2})
        (screening / "batches").mkdir(parents=True)
        (screening / "batches" / "batch-001.jsonl").write_text('{"derived":true}\n', encoding="utf-8")
        return artifact

    def _accept(
        self,
        artifact: Path,
        repo: Path,
        issue: str = "2026-W33",
        workflow_run_id: int = 12345,
    ):
        return acceptor.accept(
            artifact_root=artifact,
            repo_root=repo,
            issue_id=issue,
            workflow_run_id=workflow_run_id,
            artifact_id=67890,
            artifact_name=f"weekly-source-intake-{issue}",
            artifact_digest="sha256:" + "a" * 64,
            review_reference=f"assistant-review:run-{workflow_run_id}",
        )

    def test_accepts_collector_tree_and_initializes_discovery_state(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = self._artifact(root)
            repo = root / "repo"
            repo.mkdir()
            result, passed = self._accept(artifact, repo)
            self.assertTrue(passed, result)
            self.assertEqual(result["status"], "ACCEPTED")
            self.assertEqual(result["raw_file_count"], 2)
            self.assertEqual(result["total_file_count"], 6)
            self.assertTrue(result["pipeline_state_created"])

            manifest_path = repo / result["acceptance_manifest"]
            manifest = json.loads(manifest_path.read_text())
            self.assertFalse(manifest["derived_screening_committed"])
            self.assertEqual(manifest["source_actions"]["workflow_run_id"], 12345)
            self.assertEqual(manifest["source_actions"]["artifact_id"], 67890)
            self.assertEqual(manifest["source_actions"]["artifact_digest"], "sha256:" + "a" * 64)
            self.assertEqual(manifest["source_actions"]["review_reference"], "assistant-review:run-12345")
            self.assertEqual(manifest["state_transition"]["target_lifecycle_state"], "DISCOVERY_COLLECTED")
            self.assertEqual(sum(item["kind"] == "RAW" for item in manifest["files"]), 2)
            self.assertFalse((repo / "source-intake-screening").exists())

            state = json.loads((repo / result["pipeline_state"]).read_text())
            self.assertEqual(state["lifecycle_state"], "DISCOVERY_COLLECTED")
            self.assertEqual(state["calendar"]["editorial_cutoff"], "2026-08-14T18:00:00-04:00")
            self.assertEqual(state["calendar"]["collection_window_start"], "2026-08-09T23:40:00+09:00")
            self.assertEqual(state["calendar"]["collection_anchor_at"], "2026-08-15T18:00:00+09:00")
            self.assertEqual(state["gates"]["raw_sources_preserved"], "passed")

    def test_existing_initialized_state_transitions_without_rewriting_calendar_basis(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = self._artifact(root)
            repo = root / "repo"
            state_path = repo / "sources" / "2026-W33" / "pipeline-state.json"
            initialized = acceptor.new_discovery_state(self._plan("2026-W33"))
            initialized["lifecycle_state"] = "ISSUE_INITIALIZED"
            initialized["calendar"]["collection_anchor_at"] = None
            initialized["gates"]["raw_sources_preserved"] = "pending"
            self._json(state_path, initialized)

            result, passed = self._accept(artifact, repo)
            self.assertTrue(passed, result)
            self.assertFalse(result["pipeline_state_created"])
            self.assertTrue(result["pipeline_state_updated"])
            state = json.loads(state_path.read_text())
            self.assertEqual(state["lifecycle_state"], "DISCOVERY_COLLECTED")
            self.assertEqual(state["calendar"]["collection_window_start"], initialized["calendar"]["collection_window_start"])
            self.assertEqual(state["calendar"]["collection_anchor_at"], self._plan("2026-W33")["collection_window_end"])

    def test_same_artifact_is_idempotent_even_after_later_lifecycle_progress(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = self._artifact(root)
            repo = root / "repo"
            repo.mkdir()
            first, passed = self._accept(artifact, repo)
            self.assertTrue(passed, first)
            state_path = repo / first["pipeline_state"]
            state = json.loads(state_path.read_text())
            state["lifecycle_state"] = "CANDIDATES_NORMALIZED"
            state_path.write_text(json.dumps(state), encoding="utf-8")

            second, passed = self._accept(artifact, repo)
            self.assertTrue(passed, second)
            self.assertEqual(second["status"], "ALREADY_ACCEPTED")
            self.assertEqual(second["new_file_count"], 0)
            self.assertEqual(json.loads(state_path.read_text())["lifecycle_state"], "CANDIDATES_NORMALIZED")

    def test_new_source_intake_is_rejected_after_downstream_work_or_freeze(self) -> None:
        for lifecycle in ("CANDIDATES_NORMALIZED", "EVIDENCE_REVIEWED", "FROZEN"):
            with self.subTest(lifecycle=lifecycle), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                artifact = self._artifact(root)
                repo = root / "repo"
                state = acceptor.new_discovery_state(self._plan("2026-W33"))
                state["lifecycle_state"] = lifecycle
                self._json(repo / "sources" / "2026-W33" / "pipeline-state.json", state)
                with self.assertRaisesRegex(ValueError, "downstream work has begun"):
                    self._accept(artifact, repo)
                self.assertFalse((repo / "sources" / "2026-W33" / "collectors").exists())

    def test_same_destination_path_with_changed_raw_bytes_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = self._artifact(root)
            repo = root / "repo"
            repo.mkdir()
            self._accept(artifact, repo)
            raw = next((artifact / "source-intake" / "sources" / "2026-W33" / "collectors").rglob("cs-ai.atom"))
            raw.write_bytes(b"changed")
            with self.assertRaisesRegex(ValueError, "append-only conflict"):
                self._accept(artifact, repo)

    def test_partial_or_report_collector_mismatch_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = self._artifact(root)
            repo = root / "repo"
            repo.mkdir()
            report_path = artifact / "source-intake" / "source-intake-report.json"
            report = json.loads(report_path.read_text())
            report["overall_status"] = "partial"
            report_path.write_text(json.dumps(report), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "overall_status=success"):
                self._accept(artifact, repo)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = self._artifact(root)
            repo = root / "repo"
            repo.mkdir()
            run = next((artifact / "source-intake" / "sources" / "2026-W33" / "collectors").rglob("collector-run.json"))
            value = json.loads(run.read_text())
            value["run_id"] = "different"
            run.write_text(json.dumps(value), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "collector-run files do not match"):
                self._accept(artifact, repo)

    def test_invalid_or_mismatched_source_plan_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = self._artifact(root)
            repo = root / "repo"
            plan_path = artifact / "source-intake-control" / "plan.json"
            plan = json.loads(plan_path.read_text())
            plan["issue_id"] = "2026-W32"
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "plan issue_id mismatch"):
                self._accept(artifact, repo)

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = self._artifact(root)
            repo = root / "repo"
            plan_path = artifact / "source-intake-control" / "plan.json"
            plan = json.loads(plan_path.read_text())
            plan["collection_window_end"] = "2026-08-08T00:00:00+09:00"
            plan_path.write_text(json.dumps(plan), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "end precedes start"):
                self._accept(artifact, repo)

    def test_unexpected_file_in_collector_tree_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = self._artifact(root)
            repo = root / "repo"
            repo.mkdir()
            collectors = artifact / "source-intake" / "sources" / "2026-W33" / "collectors"
            (collectors / "README.md").write_text("unexpected", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unexpected file"):
                self._accept(artifact, repo)

    def test_review_reference_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            artifact = self._artifact(root)
            repo = root / "repo"
            repo.mkdir()
            with self.assertRaisesRegex(ValueError, "review_reference"):
                acceptor.accept(
                    artifact_root=artifact,
                    repo_root=repo,
                    issue_id="2026-W33",
                    workflow_run_id=12345,
                    artifact_id=67890,
                    artifact_name="weekly-source-intake-2026-W33",
                    artifact_digest="sha256:" + "a" * 64,
                    review_reference="",
                )


if __name__ == "__main__":
    unittest.main()
