from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import prepare_evidence_run as prepare


class PrepareEvidenceRunTests(unittest.TestCase):
    ISSUE = "2026-W33"
    SCREENING_SHA = "a" * 64
    SOURCE_COMMIT = "1" * 40

    def _json(self, path: Path, value: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")

    def _queue_item(self, screening_id: str = "official-feed:example") -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": self.ISSUE,
            "batch_id": "batch-001",
            "screening_id": screening_id,
            "record": {
                "schema_version": "1.0",
                "issue_id": self.ISSUE,
                "screening_id": screening_id,
                "source_type": "official-feed-item",
                "collector_id": "official-pages",
                "collector_run_id": "official-pages:run",
                "observed_at": "2026-08-15T09:00:00Z",
                "title": "Example model release",
                "locator": "https://example.com/release",
                "raw_paths": ["sources/2026-W33/collectors/official/raw/example.xml"],
                "published_at": "2026-08-15T00:30:00Z",
                "summary_text": "Technical release details.",
                "metadata": {},
            },
            "screening": {
                "screening_id": screening_id,
                "decision": "KEEP",
                "reason": "Technically relevant.",
                "why_now": "New release.",
                "topic_lanes": ["A"],
                "duplicate_group": None,
                "verification_targets": ["Verify the release and technical details."],
                "confidence": "high",
            },
        }

    def _fixture(self, root: Path) -> Path:
        repo = root / "repo"
        state = repo / "sources" / self.ISSUE / "pipeline-state.json"
        self._json(
            state,
            {
                "schema_version": "1.0",
                "issue_id": self.ISSUE,
                "lifecycle_state": "CANDIDATES_NORMALIZED",
                "revision": "working",
                "gates": {
                    "raw_sources_preserved": "passed",
                    "candidate_inventory": "passed",
                    "evidence_normalized": "pending",
                    "candidate_selection": "pending",
                    "issue_architecture": "pending",
                    "article_draft": "pending",
                    "claim_and_chronology_validation": "pending",
                    "latex_build": "pending",
                    "visual_review": "pending",
                    "freeze": "pending",
                },
            },
        )

        screening = repo / "sources" / self.ISSUE / "screening" / "runs" / self.SCREENING_SHA
        self._json(
            screening / "acceptance.json",
            {
                "schema_version": "1.0",
                "issue_id": self.ISSUE,
                "status": "ACCEPTED",
                "result_set_sha256": self.SCREENING_SHA,
            },
        )
        queue = screening / "verification-queue.jsonl"
        queue.parent.mkdir(parents=True, exist_ok=True)
        queue.write_text(json.dumps(self._queue_item(), ensure_ascii=False) + "\n", encoding="utf-8")

        prompt = repo / "config" / "prompts" / "evidence" / "primary-source-verification-v0.1.md"
        prompt.parent.mkdir(parents=True, exist_ok=True)
        prompt.write_text("verify from primary sources only\n", encoding="utf-8")
        self._json(repo / "schemas" / "evidence-run.schema.json", {"type": "object"})
        self._json(repo / "schemas" / "evidence-card.schema.json", {"type": "object"})
        return repo

    def _build(self, repo: Path, output: Path):
        return prepare.build_package(
            repo_root=repo,
            output_root=output,
            issue_id=self.ISSUE,
            screening_run_sha=self.SCREENING_SHA,
            source_ref=f"weekly/{self.ISSUE}-work",
            source_commit=self.SOURCE_COMMIT,
        )

    def test_builds_deterministic_commit_pinned_evidence_package(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = self._fixture(root)
            first = self._build(repo, root / "out1")
            second = self._build(repo, root / "out2")
            self.assertEqual(first, second)
            self.assertEqual(first["source"]["commit_sha"], self.SOURCE_COMMIT)
            self.assertEqual(first["screening_basis"]["result_set_sha256"], self.SCREENING_SHA)
            self.assertEqual(first["evidence_tasks"]["task_count"], 1)
            self.assertEqual(len(first["evidence_tasks"]["tasks"]), 1)
            task = first["evidence_tasks"]["tasks"][0]
            self.assertTrue((root / "out1" / task["path"]).is_file())
            self.assertTrue((root / "out1" / first["prompt"]["path"]).is_file())
            self.assertTrue((root / "out1" / first["contracts"]["evidence_run"]["path"]).is_file())
            self.assertTrue((root / "out1" / first["contracts"]["evidence_card"]["path"]).is_file())
            self.assertFalse((root / "out1" / "task-build").exists())

    def test_requires_candidate_normalized_state_and_pending_evidence_gate(self) -> None:
        for lifecycle, evidence_gate, message in (
            ("DISCOVERY_COLLECTED", "pending", "CANDIDATES_NORMALIZED"),
            ("EVIDENCE_REVIEWED", "passed", "CANDIDATES_NORMALIZED"),
            ("CANDIDATES_NORMALIZED", "passed", "evidence_normalized gate=pending"),
        ):
            with self.subTest(lifecycle=lifecycle, evidence_gate=evidence_gate), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                repo = self._fixture(root)
                state_path = repo / "sources" / self.ISSUE / "pipeline-state.json"
                state = json.loads(state_path.read_text())
                state["lifecycle_state"] = lifecycle
                state["gates"]["evidence_normalized"] = evidence_gate
                state_path.write_text(json.dumps(state), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, message):
                    self._build(repo, root / "out")

    def test_requires_exact_accepted_screening_identity(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = self._fixture(root)
            acceptance = repo / "sources" / self.ISSUE / "screening" / "runs" / self.SCREENING_SHA / "acceptance.json"
            value = json.loads(acceptance.read_text())
            value["result_set_sha256"] = "b" * 64
            acceptance.write_text(json.dumps(value), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "result_set_sha256 mismatch"):
                self._build(repo, root / "out")

    def test_empty_verification_queue_is_explicitly_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = self._fixture(root)
            queue = repo / "sources" / self.ISSUE / "screening" / "runs" / self.SCREENING_SHA / "verification-queue.jsonl"
            queue.write_text("", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "zero-Evidence issue handling"):
                self._build(repo, root / "out")

    def test_task_manifest_identity_is_derived_from_queue_issue(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = self._fixture(root)
            queue = repo / "sources" / self.ISSUE / "screening" / "runs" / self.SCREENING_SHA / "verification-queue.jsonl"
            item = self._queue_item()
            item["record"]["issue_id"] = "2026-W32"
            queue.write_text(json.dumps(item) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Evidence Task manifest issue_id mismatch"):
                self._build(repo, root / "out")


if __name__ == "__main__":
    unittest.main()
