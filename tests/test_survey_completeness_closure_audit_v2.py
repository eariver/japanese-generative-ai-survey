from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import survey_completeness_v2 as completeness
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening


class SurveyCompletenessClosureAuditV2Tests(unittest.TestCase):
    @staticmethod
    def discovery(discovery_id: str, research_pass: int, obligation_ids: list[str]) -> dict:
        return {
            "schema_version": "2.0-rc1",
            "issue_id": "SP001",
            "discovery_id": discovery_id,
            "provenance": {
                "origin": "GAP_FILL" if obligation_ids else "BASE",
                "research_pass": research_pass,
                "parent_refs": [],
                "obligation_ids": obligation_ids,
                "reason": "closure audit fixture",
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

    def fixture(self) -> tuple[tempfile.TemporaryDirectory[str], Path, Path, Path, dict]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        profile_path = root / "profile.json"
        ledger_path = root / "ledger.json"
        discovery_path = root / "discovery.jsonl"
        core.write_json(
            profile_path,
            {
                "research_scope": {
                    "scope_dimensions": ["lineage"],
                    "initial_obligations": [
                        {
                            "obligation_id": "gap:new-branch",
                            "dimension": "lineage",
                            "description": "dispose the branch discovered in the final pass",
                        }
                    ],
                },
            },
        )
        core.write_json(
            ledger_path,
            {
                "rows": [
                    {
                        "discovery_id": "seed",
                        "evidence_task_ids": ["evidence:seed"],
                    },
                    {
                        "discovery_id": "expanded",
                        "evidence_task_ids": ["evidence:expanded"],
                    },
                ]
            },
        )
        screening.write_jsonl(
            discovery_path,
            [
                self.discovery("seed", 0, []),
                self.discovery("expanded", 1, ["gap:new-branch"]),
            ],
        )
        result = {
            "research_profile": "THEMATIC",
            "obligations": [
                {
                    "obligation_id": "gap:new-branch",
                    "dimension": "lineage",
                    "description": "dispose the branch discovered in the final pass",
                    "status": "SATISFIED",
                    "discovery_ids": ["expanded"],
                    "evidence_task_ids": ["evidence:expanded"],
                    "rationale": "verified and incorporated",
                }
            ],
            "closure": {
                "expansion_passes": 1,
                "final_pass_new_sources": 1,
                "final_pass_new_material_obligations": 1,
                "final_pass_new_material_obligations_open": 0,
                "targeted_gap_fill_completed": True,
                "open_material_obligations": 0,
                "limitations": [],
                "status": "COMPLETE",
            },
        }
        return temp, profile_path, ledger_path, discovery_path, result

    def call_guard(self, profile_path: Path, ledger_path: Path, discovery_path: Path, result: dict) -> list[str]:
        dummy = profile_path.parent / "dummy.json"
        with patch("scripts.survey_completeness_v2.evidence.validate_completeness", return_value=[]):
            return completeness.validate_profile_completeness(
                result,
                profile_path.parent,
                profile_path,
                discovery_path,
                dummy,
                dummy,
                dummy,
                ledger_path,
                "4" * 40,
            )

    def test_closure_counters_are_derived_from_discovery_provenance(self) -> None:
        temp, profile_path, ledger_path, discovery_path, result = self.fixture()
        self.addCleanup(temp.cleanup)
        self.assertEqual(self.call_guard(profile_path, ledger_path, discovery_path, result), [])

        lied = {**result, "closure": {**result["closure"], "final_pass_new_sources": 0}}
        errors = self.call_guard(profile_path, ledger_path, discovery_path, lied)
        self.assertTrue(any("final_pass_new_sources must be derived" in error for error in errors))

        lied = {
            **result,
            "closure": {**result["closure"], "final_pass_new_material_obligations": 0},
        }
        errors = self.call_guard(profile_path, ledger_path, discovery_path, lied)
        self.assertTrue(any("final_pass_new_material_obligations must be derived" in error for error in errors))

    def test_completeness_obligation_shape_is_fail_closed(self) -> None:
        temp, profile_path, ledger_path, discovery_path, result = self.fixture()
        self.addCleanup(temp.cleanup)
        malformed = {**result, "obligations": [dict(result["obligations"][0], invented=True)]}
        errors = self.call_guard(profile_path, ledger_path, discovery_path, malformed)
        self.assertTrue(any("fields must exactly match v2 contract" in error for error in errors))

        wrong_dimension = {
            **result,
            "obligations": [dict(result["obligations"][0], dimension="not-in-profile")],
        }
        errors = self.call_guard(profile_path, ledger_path, discovery_path, wrong_dimension)
        self.assertTrue(any("dimension is not declared" in error for error in errors))

    def test_profile_initial_obligation_cannot_disappear(self) -> None:
        temp, profile_path, ledger_path, discovery_path, result = self.fixture()
        self.addCleanup(temp.cleanup)
        missing = {**result, "obligations": []}
        errors = self.call_guard(profile_path, ledger_path, discovery_path, missing)
        self.assertTrue(any("silently dropped Profile initial obligation" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
