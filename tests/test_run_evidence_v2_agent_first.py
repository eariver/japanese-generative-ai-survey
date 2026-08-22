from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import run_evidence_v2_agent_first as adapter
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening


class RunEvidenceV2AgentFirstTests(unittest.TestCase):
    def test_adapter_replaces_normalized_summary_with_hash_pinned_canonical_records(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            discovery_path = root / "sources/SP001/discovery/discovery-v2.jsonl"
            record = {
                "schema_version": "2.0-rc1",
                "issue_id": "SP001",
                "discovery_id": "SP001-D001",
                "provenance": {
                    "origin": "BASE",
                    "research_pass": 0,
                    "parent_refs": [],
                    "obligation_ids": ["SP001-O01"],
                    "reason": "seed",
                },
                "source": {
                    "source_type": "paper",
                    "collector_id": "test",
                    "collector_run_id": "run",
                    "observed_at": "2026-08-22T00:00:00Z",
                    "title": "source",
                    "locator": "https://example.invalid/source",
                    "raw_paths": ["raw/source.json"],
                    "published_at": None,
                    "summary_text": "summary",
                    "metadata": {},
                },
            }
            screening.write_jsonl(discovery_path, [record])
            accepted = {
                "schema_version": "2.0-rc1",
                "issue_id": "SP001",
                "discovery_path": "sources/SP001/discovery/discovery-v2.jsonl",
                "discovery_sha256": core.sha256_file(discovery_path),
                "record_count": 1,
                "records": [{"discovery_id": "SP001-D001", "research_pass": 0}],
            }

            def original(repo_root: Path, acceptance_path: Path) -> dict:
                return accepted

            result = adapter.acceptance_with_canonical_discovery_records(
                original,
                root,
                root / "sources/SP001/discovery/discovery-accepted-v2.json",
            )
            self.assertEqual(result["records"], [record])
            self.assertEqual(
                result["records"][0]["provenance"]["obligation_ids"],
                ["SP001-O01"],
            )

    def test_adapter_fails_if_canonical_discovery_bytes_drift(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = root / "discovery.jsonl"
            path.write_text("{}\n", encoding="utf-8")
            accepted = {
                "issue_id": "SP001",
                "discovery_path": "discovery.jsonl",
                "discovery_sha256": "0" * 64,
                "record_count": 1,
                "records": [],
            }

            def original(repo_root: Path, acceptance_path: Path) -> dict:
                return accepted

            with self.assertRaisesRegex(ValueError, "bytes changed"):
                adapter.acceptance_with_canonical_discovery_records(
                    original, root, root / "acceptance.json"
                )

    def test_thematic_closure_includes_every_residual_limitation_without_duplicates(self) -> None:
        original_result = {
            "research_profile": "THEMATIC",
            "residual_limitations": ["A", "B"],
            "closure": {"limitations": ["A", "closure-only"]},
        }

        def original(*args, **kwargs) -> dict:
            return original_result

        result = adapter.completeness_with_preserved_residual_limitations(original)
        self.assertEqual(result["closure"]["limitations"], ["A", "closure-only", "B"])
        self.assertEqual(original_result["closure"]["limitations"], ["A", "closure-only"])

    def test_non_thematic_completeness_is_unchanged(self) -> None:
        original_result = {
            "research_profile": "WEEKLY",
            "residual_limitations": ["A"],
            "closure": None,
        }

        def original(*args, **kwargs) -> dict:
            return original_result

        self.assertIs(
            adapter.completeness_with_preserved_residual_limitations(original),
            original_result,
        )


if __name__ == "__main__":
    unittest.main()
