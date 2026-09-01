from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import survey_completeness_v2 as completeness
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening


class SurveyCompletenessV2NamedObligationTests(unittest.TestCase):
    @staticmethod
    def discovery(discovery_id: str, obligation_ids: list[str]) -> dict:
        return {
            "schema_version": "2.0-rc1",
            "issue_id": "SP001",
            "discovery_id": discovery_id,
            "provenance": {
                "origin": "GAP_FILL" if obligation_ids else "BASE",
                "research_pass": 1 if obligation_ids else 0,
                "parent_refs": [],
                "obligation_ids": obligation_ids,
                "reason": "named research obligation fixture",
            },
            "source": {
                "source_type": "paper",
                "collector_id": "fixture",
                "collector_run_id": "run-1",
                "observed_at": "2026-08-22T02:00:00+09:00",
                "title": discovery_id,
                "locator": f"https://example.invalid/{discovery_id}",
                "raw_paths": ["raw/source.json"],
                "published_at": None,
                "summary_text": None,
                "metadata": {},
            },
        }

    def call_guard(self, discovery_path: Path, result: dict) -> list[str]:
        root = discovery_path.parent
        profile_path = root / "profile.json"
        ledger_path = root / "ledger.json"
        dummy = root / "dummy.json"
        discoveries = screening.read_jsonl(discovery_path)
        named_ids = sorted(
            {
                obligation_id
                for row in discoveries
                for obligation_id in row["provenance"]["obligation_ids"]
            }
        )
        initial_obligations = [
            {
                "obligation_id": obligation_id,
                "dimension": "lineage",
                "description": f"fixture initial obligation {obligation_id}",
            }
            for obligation_id in named_ids
        ] or [
            {
                "obligation_id": "initial:lineage",
                "dimension": "lineage",
                "description": "fixture initial lineage obligation",
            }
        ]
        core.write_json(
            profile_path,
            {
                "research_scope": {
                    "scope_dimensions": ["lineage"],
                    "initial_obligations": initial_obligations,
                }
            },
        )
        core.write_json(
            ledger_path,
            {
                "rows": [
                    {
                        "discovery_id": row["discovery_id"],
                        "evidence_task_ids": [],
                    }
                    for row in discoveries
                ]
            },
        )
        with patch("scripts.survey_completeness_v2.evidence.validate_completeness", return_value=[]):
            return completeness.validate_profile_completeness(
                result,
                root,
                profile_path,
                discovery_path,
                dummy,
                dummy,
                dummy,
                ledger_path,
                "4" * 40,
            )

    def test_named_obligation_cannot_disappear_from_completeness(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            discovery_path = root / "discovery.jsonl"
            screening.write_jsonl(
                discovery_path,
                [
                    self.discovery("seed", []),
                    self.discovery("gap-source", ["gap:competing-branch"]),
                ],
            )
            result = {"obligations": []}
            errors = self.call_guard(discovery_path, result)
            self.assertTrue(any("silently dropped named Discovery obligations" in error for error in errors))
            self.assertTrue(any("silently dropped Profile initial obligation" in error for error in errors))

    def test_named_obligation_must_reference_every_declaring_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            discovery_path = root / "discovery.jsonl"
            screening.write_jsonl(
                discovery_path,
                [
                    self.discovery("gap-a", ["gap:shared"]),
                    self.discovery("gap-b", ["gap:shared"]),
                ],
            )
            result = {
                "obligations": [
                    {
                        "obligation_id": "gap:shared",
                        "dimension": "lineage",
                        "description": "dispose every Discovery declaring the shared obligation",
                        "status": "SATISFIED",
                        "discovery_ids": ["gap-a"],
                        "evidence_task_ids": [],
                        "rationale": "fixture obligation",
                    }
                ]
            }
            errors = self.call_guard(discovery_path, result)
            self.assertTrue(any("gap-b" in error and "does not trace back" in error for error in errors))

            result["obligations"][0]["discovery_ids"] = ["gap-a", "gap-b"]
            self.assertEqual(self.call_guard(discovery_path, result), [])


if __name__ == "__main__":
    unittest.main()
