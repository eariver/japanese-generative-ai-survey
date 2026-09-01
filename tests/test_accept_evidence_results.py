from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import accept_evidence_results as acceptor


class EvidenceAcceptanceTests(unittest.TestCase):
    ISSUE = "2026-W33"
    SCREENING_SHA = "a" * 64
    SOURCE_COMMIT = "1" * 40
    TASK_ID = "evidence:2026-W33:test-task-1234567890"

    def _json(self, path: Path, value: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")

    def _sha(self, path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def _task(self) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": self.ISSUE,
            "evidence_task_id": self.TASK_ID,
            "task_type": "VERIFY_ITEM",
            "grouping": {"basis": "single-screening-item", "duplicate_group": None, "requires_confirmation": False},
            "screening_ids": ["screening:test"],
            "screening_decisions": ["KEEP"],
            "source_types": ["official-feed-item"],
            "locators": ["https://example.com/release"],
            "topic_lanes": ["A"],
            "why_now": ["new release"],
            "verification_targets": ["Verify release date.", "Verify benchmark conditions."],
            "status": "PENDING_VERIFICATION",
        }

    def _card(self, task: dict, recommendation: str = "CANDIDATE") -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": self.ISSUE,
            "evidence_task_id": task["evidence_task_id"],
            "status": "VERIFIED",
            "grouping_resolution": {"accepted": True, "split_recommended": False, "note": None},
            "artifact": {
                "canonical_name": "Example Release",
                "artifact_type": "MODEL_UPDATE",
                "organization": "Example",
                "canonical_url": "https://example.com/release",
            },
            "temporal": {
                "artifact_first_announced": "2026-08-15",
                "observed_at": "2026-08-15T10:00:00Z",
                "events": [
                    {
                        "event_id": "event-release",
                        "event_type": "MODEL_UPDATE",
                        "event_date": "2026-08-15",
                        "source_published_at": "2026-08-15",
                        "source_ids": ["s1"],
                    }
                ],
            },
            "sources": [
                {
                    "source_id": "s1",
                    "url": "https://example.com/release",
                    "source_class": "PRIMARY_OFFICIAL",
                    "title": "Example Release",
                    "published_at": "2026-08-15",
                    "accessed_at": "2026-08-15T10:00:00Z",
                    "role": "official release note",
                }
            ],
            "claims": [
                {
                    "claim_id": "c1",
                    "text": "The update exists.",
                    "evidence_class": "PRIMARY_FACT",
                    "source_ids": ["s1"],
                    "context": None,
                }
            ],
            "metrics": [
                {
                    "metric_id": "m1",
                    "name": "benchmark",
                    "value": "42",
                    "unit": "points",
                    "context": "vendor benchmark setup",
                    "evidence_class": "VENDOR_CLAIM",
                    "source_ids": ["s1"],
                }
            ],
            "limitations": [
                {
                    "limitation_id": "l1",
                    "text": "No independent reproduction was verified.",
                    "evidence_class": "INFERENCE",
                    "source_ids": ["s1"],
                }
            ],
            "verification": {
                "targets": [
                    {
                        "target": "Verify release date.",
                        "status": "VERIFIED",
                        "finding": "Official release note is dated 2026-08-15.",
                        "source_ids": ["s1"],
                    },
                    {
                        "target": "Verify benchmark conditions.",
                        "status": "VERIFIED",
                        "finding": "Official note provides the benchmark setup.",
                        "source_ids": ["s1"],
                    },
                ],
                "unresolved_questions": [],
                "contradictions": [],
            },
            "editorial": {
                "why_now_confirmed": True,
                "why_now_note": "Official update is in-window.",
                "candidate_recommendation": recommendation,
                "rationale": "Primary source confirms a technical update.",
            },
        }

    def _fixture(self, root: Path, recommendation: str = "CANDIDATE") -> tuple[Path, Path, Path]:
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
        queue.write_text('{"screening_id":"screening:test"}\n', encoding="utf-8")

        package = root / "package"
        prompt = package / "contract" / "primary-source-verification-v0.1.md"
        prompt.parent.mkdir(parents=True, exist_ok=True)
        prompt.write_text("verify from primary sources only\n", encoding="utf-8")
        run_schema = package / "contract" / "evidence-run.schema.json"
        card_schema = package / "contract" / "evidence-card.schema.json"
        self._json(run_schema, {"type": "object"})
        self._json(card_schema, {"type": "object"})

        task_path = package / "input" / "tasks" / "task-001.json"
        self._json(task_path, self._task())
        task_manifest = package / "input" / "evidence-task-manifest.json"
        self._json(task_manifest, {"schema_version": "1.0", "issue_id": self.ISSUE, "evidence_task_count": 1})
        task_index = package / "input" / "evidence-task-index.jsonl"
        task_index.parent.mkdir(parents=True, exist_ok=True)
        task_index.write_text(json.dumps(self._task()) + "\n", encoding="utf-8")

        package_manifest = {
            "schema_version": "1.0",
            "issue_id": self.ISSUE,
            "source": {
                "ref": f"weekly/{self.ISSUE}-work",
                "commit_sha": self.SOURCE_COMMIT,
                "pipeline_state_sha256": self._sha(state),
            },
            "screening_basis": {
                "result_set_sha256": self.SCREENING_SHA,
                "acceptance_path": (screening / "acceptance.json").relative_to(repo).as_posix(),
                "acceptance_sha256": self._sha(screening / "acceptance.json"),
                "verification_queue_path": queue.relative_to(repo).as_posix(),
                "verification_queue_sha256": self._sha(queue),
            },
            "prompt": {
                "prompt_id": "primary-source-verification-v0.1",
                "path": "contract/primary-source-verification-v0.1.md",
                "sha256": self._sha(prompt),
            },
            "contracts": {
                "evidence_run": {"path": "contract/evidence-run.schema.json", "sha256": self._sha(run_schema)},
                "evidence_card": {"path": "contract/evidence-card.schema.json", "sha256": self._sha(card_schema)},
            },
            "evidence_tasks": {
                "manifest_path": "input/evidence-task-manifest.json",
                "manifest_sha256": self._sha(task_manifest),
                "index_path": "input/evidence-task-index.jsonl",
                "index_sha256": self._sha(task_index),
                "task_count": 1,
                "tasks": [
                    {
                        "evidence_task_id": self.TASK_ID,
                        "path": "input/tasks/task-001.json",
                        "sha256": self._sha(task_path),
                        "bytes": task_path.stat().st_size,
                    }
                ],
            },
            "expected_outputs": {"one_result_per_task": True, "schema_version": "1.0", "naming": "results/<input task filename>"},
            "rules": ["test fixture"],
        }
        self._json(package / "evidence-execution-package.json", package_manifest)

        results = root / "results"
        task = self._task()
        self._json(
            results / "task-001.json",
            {
                "schema_version": "1.0",
                "issue_id": self.ISSUE,
                "evidence_task_id": self.TASK_ID,
                "evidence_task_sha256": self._sha(task_path),
                "prompt_id": "primary-source-verification-v0.1",
                "prompt_sha256": self._sha(prompt),
                "runner": {
                    "provider": "test-provider",
                    "model": "test-model",
                    "invocation": "unit-test",
                    "generated_at": "2026-08-15T10:00:00Z",
                    "run_reference": "test-run-1",
                },
                "card": self._card(task, recommendation),
            },
        )
        return repo, package, results

    def _accept(self, repo: Path, package: Path, results: Path):
        return acceptor.accept(
            package_root=package,
            results_dir=results,
            repo_root=repo,
            issue_id=self.ISSUE,
            review_reference="assistant-review:evidence-complete",
        )

    def test_accepts_complete_validated_evidence_and_advances_state(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            result, passed = self._accept(repo, package, results)
            self.assertTrue(passed, result)
            self.assertEqual(result["status"], "ACCEPTED")
            self.assertEqual(result["evidence_task_count"], 1)
            self.assertEqual(result["candidate_ready_count"], 1)
            self.assertEqual(result["lifecycle_state"], "EVIDENCE_REVIEWED")
            accepted = repo / "sources" / self.ISSUE / "evidence" / "runs" / result["result_set_sha256"]
            self.assertTrue((accepted / "results" / "task-001.json").is_file())
            self.assertTrue((accepted / "evidence-reviewed.jsonl").is_file())
            self.assertTrue((accepted / "candidate-ready.jsonl").is_file())
            self.assertTrue((accepted / "validation").is_dir())
            manifest = json.loads((accepted / "acceptance.json").read_text())
            self.assertEqual(manifest["state_transition"]["to"], "EVIDENCE_REVIEWED")
            self.assertEqual(manifest["results"][0]["runner"]["model"], "test-model")
            state = json.loads((repo / "sources" / self.ISSUE / "pipeline-state.json").read_text())
            self.assertEqual(state["lifecycle_state"], "EVIDENCE_REVIEWED")
            self.assertEqual(state["gates"]["evidence_normalized"], "passed")
            self.assertEqual(state["gates"]["candidate_selection"], "pending")

    def test_exact_accepted_set_is_idempotent_after_later_progress(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            first, passed = self._accept(repo, package, results)
            self.assertTrue(passed, first)
            state_path = repo / "sources" / self.ISSUE / "pipeline-state.json"
            state = json.loads(state_path.read_text())
            state["lifecycle_state"] = "SELECTION_COMPLETE"
            state["gates"]["candidate_selection"] = "passed"
            state_path.write_text(json.dumps(state), encoding="utf-8")
            second, passed = self._accept(repo, package, results)
            self.assertTrue(passed, second)
            self.assertEqual(second["status"], "ALREADY_ACCEPTED")
            self.assertFalse(second["state_transition_recovered"])
            self.assertEqual(json.loads(state_path.read_text())["lifecycle_state"], "SELECTION_COMPLETE")

    def test_new_set_rejects_wrong_lifecycle_or_changed_screening_basis(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp), recommendation="HOLD")
            state_path = repo / "sources" / self.ISSUE / "pipeline-state.json"
            state = json.loads(state_path.read_text())
            state["lifecycle_state"] = "EVIDENCE_REVIEWED"
            state["gates"]["evidence_normalized"] = "passed"
            state_path.write_text(json.dumps(state), encoding="utf-8")
            package_path = package / "evidence-execution-package.json"
            manifest = json.loads(package_path.read_text())
            manifest["source"]["pipeline_state_sha256"] = self._sha(state_path)
            self._json(package_path, manifest)
            with self.assertRaisesRegex(ValueError, "may be accepted only in CANDIDATES_NORMALIZED"):
                self._accept(repo, package, results)

        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            queue = repo / "sources" / self.ISSUE / "screening" / "runs" / self.SCREENING_SHA / "verification-queue.jsonl"
            queue.write_text('{"changed":true}\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "verification queue bytes no longer match"):
                self._accept(repo, package, results)

    def test_incomplete_extra_or_invalid_result_set_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            (results / "task-001.json").unlink()
            with self.assertRaisesRegex(ValueError, "complete and exact"):
                self._accept(repo, package, results)

        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            self._json(results / "extra.json", {})
            with self.assertRaisesRegex(ValueError, "complete and exact"):
                self._accept(repo, package, results)

        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            result_path = results / "task-001.json"
            value = json.loads(result_path.read_text())
            value["evidence_task_sha256"] = "0" * 64
            self._json(result_path, value)
            with self.assertRaisesRegex(ValueError, "validation failed"):
                self._accept(repo, package, results)

    def test_interrupted_state_transition_is_recovered_for_exact_accepted_set(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            first, passed = self._accept(repo, package, results)
            self.assertTrue(passed, first)
            state_path = repo / "sources" / self.ISSUE / "pipeline-state.json"
            # Recreate the exact pre-accept state bytes referenced by the package.
            package_manifest = json.loads((package / "evidence-execution-package.json").read_text())
            pre_state = {
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
            }
            state_path.write_text(json.dumps(pre_state, ensure_ascii=False), encoding="utf-8")
            self.assertEqual(self._sha(state_path), package_manifest["source"]["pipeline_state_sha256"])
            second, passed = self._accept(repo, package, results)
            self.assertTrue(passed, second)
            self.assertTrue(second["state_transition_recovered"])
            self.assertEqual(json.loads(state_path.read_text())["lifecycle_state"], "EVIDENCE_REVIEWED")


if __name__ == "__main__":
    unittest.main()
