from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import accept_screening_results as acceptor


class ScreeningAcceptanceTests(unittest.TestCase):
    ISSUE = "2026-W33"
    SOURCE_COMMIT = "1" * 40

    def _json(self, path: Path, value: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")

    def _sha(self, path: Path) -> str:
        return acceptor.sha256_file(path)

    def _fixture(self, root: Path, decision: str = "KEEP") -> tuple[Path, Path, Path]:
        repo = root / "repo"
        state_path = repo / "sources" / self.ISSUE / "pipeline-state.json"
        raw_index_path = repo / "sources" / self.ISSUE / "raw-index.json"
        self._json(
            state_path,
            {
                "schema_version": "1.0",
                "issue_id": self.ISSUE,
                "lifecycle_state": "DISCOVERY_COLLECTED",
                "revision": "working",
                "gates": {
                    "raw_sources_preserved": "passed",
                    "candidate_inventory": "pending",
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
        self._json(raw_index_path, {"schema_version": "1.0", "issue_id": self.ISSUE, "entries": []})

        package = root / "package"
        prompt = package / "contract" / "source-screening-v0.1.md"
        prompt.parent.mkdir(parents=True, exist_ok=True)
        prompt.write_text("screen only supplied records\n", encoding="utf-8")
        contract = package / "contract" / "screening-batch-result.schema.json"
        self._json(contract, {"type": "object"})

        record = {
            "schema_version": "1.0",
            "issue_id": self.ISSUE,
            "screening_id": "official-feed:example",
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
        }
        batch = package / "input" / "batches" / "batch-001.jsonl"
        batch.parent.mkdir(parents=True, exist_ok=True)
        encoded = json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
        batch.write_text(encoded, encoding="utf-8")
        index = package / "input" / "screening-index.jsonl"
        index.write_text(encoded, encoding="utf-8")
        screening_manifest = package / "input" / "screening-manifest.json"
        self._json(
            screening_manifest,
            {
                "schema_version": "1.0",
                "issue_id": self.ISSUE,
                "record_count": 1,
                "batch_count": 1,
            },
        )
        package_manifest = {
            "schema_version": "1.0",
            "issue_id": self.ISSUE,
            "source": {"ref": f"weekly/{self.ISSUE}-work", "commit_sha": self.SOURCE_COMMIT},
            "provenance": {
                "pipeline_state_sha256": self._sha(state_path),
                "raw_index_sha256": self._sha(raw_index_path),
            },
            "prompt": {
                "prompt_id": "source-screening-v0.1",
                "path": "contract/source-screening-v0.1.md",
                "sha256": self._sha(prompt),
            },
            "result_contract": {
                "path": "contract/screening-batch-result.schema.json",
                "sha256": self._sha(contract),
            },
            "screening_input": {
                "manifest_path": "input/screening-manifest.json",
                "manifest_sha256": self._sha(screening_manifest),
                "index_path": "input/screening-index.jsonl",
                "index_sha256": self._sha(index),
                "record_count": 1,
                "batch_policy": {"max_records": 40, "max_json_chars": 80000},
                "batches": [
                    {
                        "batch_id": "batch-001",
                        "path": "input/batches/batch-001.jsonl",
                        "record_count": 1,
                        "sha256": self._sha(batch),
                        "bytes": batch.stat().st_size,
                    }
                ],
            },
            "expected_outputs": {
                "file_pattern": "results/batch-###.json",
                "one_result_per_batch": True,
                "schema_version": "1.0",
            },
            "rules": ["test fixture"],
        }
        self._json(package / "screening-run-package.json", package_manifest)

        results = root / "results"
        why_now = "new release" if decision != "DROP" else None
        targets = ["Verify release details."] if decision != "DROP" else []
        self._json(
            results / "batch-001.json",
            {
                "schema_version": "1.0",
                "issue_id": self.ISSUE,
                "batch_id": "batch-001",
                "input_batch_sha256": self._sha(batch),
                "prompt_id": "source-screening-v0.1",
                "prompt_sha256": self._sha(prompt),
                "runner": {
                    "provider": "test-provider",
                    "model": "test-model",
                    "invocation": "unit-test",
                    "generated_at": "2026-08-15T10:00:00Z",
                    "run_reference": "test-run-1",
                },
                "decisions": [
                    {
                        "screening_id": "official-feed:example",
                        "decision": decision,
                        "reason": "Relevant technical release." if decision != "DROP" else "Routine item.",
                        "why_now": why_now,
                        "topic_lanes": ["A"] if decision != "DROP" else [],
                        "duplicate_group": None,
                        "verification_targets": targets,
                        "confidence": "high",
                    }
                ],
            },
        )
        return repo, package, results

    def _accept(self, repo: Path, package: Path, results: Path):
        return acceptor.accept(
            package_root=package,
            results_dir=results,
            repo_root=repo,
            issue_id=self.ISSUE,
            review_reference="assistant-review:screening-complete",
        )

    def test_accepts_complete_validated_result_set_and_closes_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            result, passed = self._accept(repo, package, results)
            self.assertTrue(passed, result)
            self.assertEqual(result["status"], "ACCEPTED")
            self.assertEqual(result["batch_count"], 1)
            self.assertEqual(result["reviewed_record_count"], 1)
            self.assertEqual(result["verification_queue_count"], 1)
            self.assertEqual(result["lifecycle_state"], "CANDIDATES_NORMALIZED")
            self.assertEqual(result["candidate_inventory_gate"], "passed")

            accepted = repo / "sources" / self.ISSUE / "screening" / "runs" / result["result_set_sha256"]
            self.assertTrue((accepted / "results" / "batch-001.json").is_file())
            self.assertTrue((accepted / "screening-reviewed.jsonl").is_file())
            self.assertTrue((accepted / "verification-queue.jsonl").is_file())
            self.assertTrue((accepted / "validation" / "batch-001.json").is_file())
            manifest = json.loads((accepted / "acceptance.json").read_text())
            self.assertEqual(manifest["state_transition"]["from"], "DISCOVERY_COLLECTED")
            self.assertEqual(manifest["state_transition"]["to"], "CANDIDATES_NORMALIZED")
            self.assertEqual(manifest["results"][0]["runner"]["model"], "test-model")
            state = json.loads((repo / "sources" / self.ISSUE / "pipeline-state.json").read_text())
            self.assertEqual(state["lifecycle_state"], "CANDIDATES_NORMALIZED")
            self.assertEqual(state["gates"]["candidate_inventory"], "passed")
            self.assertEqual(state["gates"]["evidence_normalized"], "pending")

    def test_exact_result_set_is_idempotent_after_lifecycle_progress(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            first, passed = self._accept(repo, package, results)
            self.assertTrue(passed, first)
            state_path = repo / "sources" / self.ISSUE / "pipeline-state.json"
            state = json.loads(state_path.read_text())
            state["lifecycle_state"] = "EVIDENCE_REVIEWED"
            state["gates"]["evidence_normalized"] = "passed"
            state_path.write_text(json.dumps(state), encoding="utf-8")
            # Exact accepted bytes remain a stable audit lookup and must not mutate state.
            second, passed = self._accept(repo, package, results)
            self.assertTrue(passed, second)
            self.assertEqual(second["status"], "ALREADY_ACCEPTED")
            self.assertEqual(json.loads(state_path.read_text())["lifecycle_state"], "EVIDENCE_REVIEWED")

    def test_new_result_set_is_rejected_after_discovery_stage(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp), decision="DROP")
            state_path = repo / "sources" / self.ISSUE / "pipeline-state.json"
            state = json.loads(state_path.read_text())
            state["lifecycle_state"] = "CANDIDATES_NORMALIZED"
            state["gates"]["candidate_inventory"] = "passed"
            state_path.write_text(json.dumps(state), encoding="utf-8")
            # Package provenance must be updated to the exact state bytes before lifecycle policy is evaluated.
            package_manifest_path = package / "screening-run-package.json"
            package_manifest = json.loads(package_manifest_path.read_text())
            package_manifest["provenance"]["pipeline_state_sha256"] = self._sha(state_path)
            self._json(package_manifest_path, package_manifest)
            with self.assertRaisesRegex(ValueError, "may be accepted only in DISCOVERY_COLLECTED"):
                self._accept(repo, package, results)

    def test_incomplete_extra_or_invalid_results_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            (results / "batch-001.json").unlink()
            with self.assertRaisesRegex(ValueError, "complete and exact"):
                self._accept(repo, package, results)

        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            self._json(results / "extra.json", {})
            with self.assertRaisesRegex(ValueError, "complete and exact"):
                self._accept(repo, package, results)

        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            result_path = results / "batch-001.json"
            value = json.loads(result_path.read_text())
            value["input_batch_sha256"] = "0" * 64
            self._json(result_path, value)
            with self.assertRaisesRegex(ValueError, "validation failed"):
                self._accept(repo, package, results)

    def test_repo_basis_and_package_bytes_must_still_match(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            raw_index = repo / "sources" / self.ISSUE / "raw-index.json"
            self._json(raw_index, {"schema_version": "1.0", "issue_id": self.ISSUE, "entries": [{"changed": True}]})
            with self.assertRaisesRegex(ValueError, "raw-index bytes no longer match"):
                self._accept(repo, package, results)

        with tempfile.TemporaryDirectory() as tmp:
            repo, package, results = self._fixture(Path(tmp))
            prompt = package / "contract" / "source-screening-v0.1.md"
            prompt.write_text("mutated prompt\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "prompt bytes"):
                self._accept(repo, package, results)


if __name__ == "__main__":
    unittest.main()
