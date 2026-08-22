from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening


IMPLEMENTATION_SHA = "3" * 40
BASE_FILES = [
    "config/survey-production-v2.json",
    "config/weekly-pipeline.json",
    "schemas/survey-production-profile.schema.json",
    "schemas/survey-production-state.schema.json",
]


class SurveyScreeningV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_root = Path(".").resolve()

    def sandbox(self) -> tuple[tempfile.TemporaryDirectory[str], Path, dict]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        source_cfg = core.load_json(self.repo_root / "config/survey-production-v2.json")
        required = [
            *BASE_FILES,
            *source_cfg["contract_files"]["pipeline"],
            *source_cfg["contract_files"]["quality"],
        ]
        for rel in dict.fromkeys(required):
            src = self.repo_root / rel
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        cfg = core.load_json(root / "config/survey-production-v2.json")
        return temp, root, cfg

    @staticmethod
    def source(locator: str) -> dict:
        return {
            "source_type": "paper",
            "collector_id": "test-collector",
            "collector_run_id": "run-001",
            "observed_at": "2026-08-22T02:00:00+09:00",
            "title": locator,
            "locator": locator,
            "raw_paths": [f"raw/{locator}.json"],
            "published_at": "2025-01-01T00:00:00Z",
            "summary_text": "bounded discovery summary",
            "metadata": {},
        }

    def discovery(
        self,
        issue_id: str,
        discovery_id: str,
        origin: str,
        *,
        parent_refs: list[str] | None = None,
        obligation_ids: list[str] | None = None,
        research_pass: int = 0,
    ) -> dict:
        return {
            "schema_version": "2.0-rc1",
            "issue_id": issue_id,
            "discovery_id": discovery_id,
            "provenance": {
                "origin": origin,
                "research_pass": research_pass,
                "parent_refs": parent_refs or [],
                "obligation_ids": obligation_ids or [],
                "reason": f"test provenance for {origin}",
            },
            "source": self.source(discovery_id),
        }

    def init_thematic(self, root: Path, cfg: dict, issue_id: str = "SP001") -> Path:
        profile = core.thematic_profile(
            root,
            cfg,
            {
                "issue_id": issue_id,
                "question": "How did a model ecosystem and its competing branches develop?",
                "temporal_mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-08-22T02:00:00+09:00",
                "scope_dimensions": ["lineage", "competition"],
            },
        )
        _, state_path = core.initialize(
            root,
            cfg,
            profile,
            IMPLEMENTATION_SHA,
            "ARCHITECTURE_REVIEW",
            core.parse_instant("2026-08-22T02:05:00+09:00"),
        )
        return state_path

    def test_thematic_expansion_origins_require_traceable_basis(self) -> None:
        valid = [
            self.discovery("SP001", "seed", "BASE"),
            self.discovery("SP001", "ref", "REFERENCE_EXPANSION", parent_refs=["seed"], research_pass=1),
            self.discovery("SP001", "successor", "SUCCESSOR_EXPANSION", parent_refs=["seed"], research_pass=1),
            self.discovery("SP001", "parallel", "PARALLEL_EXPANSION", parent_refs=["seed"], research_pass=1),
            self.discovery("SP001", "competing", "COMPETING_EXPANSION", parent_refs=["seed"], research_pass=1),
            self.discovery("SP001", "bridge", "BRIDGE_EXPANSION", parent_refs=["ref", "successor"], research_pass=2),
            self.discovery("SP001", "gap", "GAP_FILL", obligation_ids=["branch-coverage"], research_pass=2),
        ]
        screening.validate_discovery_set(valid, "SP001")

        invalid = self.discovery("SP001", "orphan", "REFERENCE_EXPANSION", research_pass=1)
        self.assertIn("requires at least one parent_ref", "; ".join(screening.validate_discovery(invalid, "SP001")))

        invalid_gap = self.discovery("SP001", "gap", "GAP_FILL", research_pass=1)
        self.assertIn("requires at least one obligation_id", "; ".join(screening.validate_discovery(invalid_gap, "SP001")))

    def test_weekly_carry_over_uses_same_discovery_contract_without_thematic_fields(self) -> None:
        record = self.discovery(
            "2026-W33",
            "carry-over-model-x",
            "CARRY_OVER",
            parent_refs=["2026-W32:model-x"],
            obligation_ids=["weekly-carry-over:model-x"],
            research_pass=0,
        )
        self.assertEqual(screening.validate_discovery(record, "2026-W33"), [])
        self.assertNotIn("why_now", record)
        self.assertNotIn("topic_lane", record)

    def test_discovery_set_rejects_duplicate_ids(self) -> None:
        records = [self.discovery("SP001", "same", "BASE"), self.discovery("SP001", "same", "BASE")]
        with self.assertRaisesRegex(ValueError, "duplicate discovery_id"):
            screening.validate_discovery_set(records, "SP001")

    def test_prepare_package_binds_profile_state_discovery_prompt_contract_and_batches(self) -> None:
        temp, root, cfg = self.sandbox()
        self.addCleanup(temp.cleanup)
        state_path = self.init_thematic(root, cfg)
        discovery_path = root / "sources/SP001/discovery/discovery.jsonl"
        records = [
            self.discovery("SP001", "seed", "BASE"),
            self.discovery("SP001", "ref", "REFERENCE_EXPANSION", parent_refs=["seed"], research_pass=1),
            self.discovery("SP001", "competing", "COMPETING_EXPANSION", parent_refs=["seed"], research_pass=1),
        ]
        screening.write_jsonl(discovery_path, records)
        package_path = screening.prepare_package(
            root,
            state_path,
            discovery_path,
            root / "sources/SP001/screening/v2/package",
            IMPLEMENTATION_SHA,
            max_records=2,
            max_json_chars=20000,
        )
        package = core.load_json(package_path)
        self.assertEqual(package["issue_id"], "SP001")
        self.assertEqual(package["research_profile"], "THEMATIC")
        self.assertEqual(package["input"]["record_count"], 3)
        self.assertEqual(len(package["input"]["batches"]), 2)
        self.assertEqual(package["basis"]["state_sha256"], core.sha256_file(state_path))
        self.assertEqual(package["prompt"]["sha256"], core.sha256_file(root / screening.PROMPT_PATH))
        self.assertEqual(package["result_contract"]["sha256"], core.sha256_file(root / screening.RESULT_SCHEMA))

    def _write_valid_results(self, root: Path, package_path: Path) -> Path:
        package = core.load_json(package_path)
        results_dir = package_path.parent / "results"
        results_dir.mkdir(parents=True, exist_ok=True)
        for batch in package["input"]["batches"]:
            batch_rows = screening.read_jsonl(package_path.parent / batch["path"])
            decisions = []
            for row in batch_rows:
                decisions.append(
                    {
                        "discovery_id": row["discovery_id"],
                        "decision": "KEEP",
                        "reason": "material to supplied research scope",
                        "scope_tags": ["model-ecosystem", "historical-lineage"],
                        "duplicate_group": None,
                        "verification_targets": ["canonical publication date", "subject identity"],
                        "confidence": "medium",
                    }
                )
            result = {
                "schema_version": "2.0-rc1",
                "issue_id": package["issue_id"],
                "batch_id": batch["batch_id"],
                "basis": screening.expected_result_basis(root, package_path, package, batch),
                "decisions": decisions,
            }
            core.write_json(results_dir / f"{batch['batch_id']}.json", result)
        return results_dir

    def test_complete_screening_accepts_arbitrary_scope_tags_without_why_now_or_lanes(self) -> None:
        temp, root, cfg = self.sandbox()
        self.addCleanup(temp.cleanup)
        state_path = self.init_thematic(root, cfg)
        discovery_path = root / "sources/SP001/discovery/discovery.jsonl"
        screening.write_jsonl(
            discovery_path,
            [
                self.discovery("SP001", "seed", "BASE"),
                self.discovery("SP001", "parallel", "PARALLEL_EXPANSION", parent_refs=["seed"], research_pass=1),
            ],
        )
        package_path = screening.prepare_package(
            root, state_path, discovery_path, root / "sources/SP001/screening/v2/package", IMPLEMENTATION_SHA
        )
        results_dir = self._write_valid_results(root, package_path)
        accepted = screening.accept_results(
            root,
            package_path,
            results_dir,
            root / "sources/SP001/screening/v2/runs",
            IMPLEMENTATION_SHA,
        )
        payload = core.load_json(accepted)
        self.assertEqual(payload["record_count"], 2)
        self.assertEqual({d["discovery_id"] for d in payload["decisions"]}, {"seed", "parallel"})
        self.assertTrue(all("why_now" not in d for d in payload["decisions"]))
        self.assertTrue(all("topic" not in d for d in payload["decisions"]))

    def test_screening_fails_closed_on_missing_extra_duplicate_or_weekly_only_fields(self) -> None:
        temp, root, cfg = self.sandbox()
        self.addCleanup(temp.cleanup)
        state_path = self.init_thematic(root, cfg)
        discovery_path = root / "sources/SP001/discovery/discovery.jsonl"
        screening.write_jsonl(
            discovery_path,
            [self.discovery("SP001", "a", "BASE"), self.discovery("SP001", "b", "BASE")],
        )
        package_path = screening.prepare_package(
            root, state_path, discovery_path, root / "sources/SP001/screening/v2/package", IMPLEMENTATION_SHA
        )
        results_dir = self._write_valid_results(root, package_path)
        package = core.load_json(package_path)
        result_path = results_dir / "batch-001.json"
        result = core.load_json(result_path)

        result["decisions"] = result["decisions"][:1]
        core.write_json(result_path, result)
        with self.assertRaisesRegex(ValueError, "cover exactly"):
            screening.accept_results(root, package_path, results_dir, root / "accepted-missing", IMPLEMENTATION_SHA)

        result = core.load_json(results_dir / "batch-001.json")
        result["decisions"] = [
            {
                "discovery_id": "a",
                "decision": "KEEP",
                "reason": "x",
                "scope_tags": [],
                "duplicate_group": None,
                "verification_targets": [],
                "confidence": "high",
                "why_now": "forbidden Weekly field",
            },
            {
                "discovery_id": "b",
                "decision": "DROP",
                "reason": "x",
                "scope_tags": [],
                "duplicate_group": None,
                "verification_targets": [],
                "confidence": "high",
            },
        ]
        result["basis"] = screening.expected_result_basis(root, package_path, package, package["input"]["batches"][0])
        core.write_json(result_path, result)
        with self.assertRaisesRegex(ValueError, "Weekly why_now/topic-lane fields are forbidden"):
            screening.accept_results(root, package_path, results_dir, root / "accepted-weekly-field", IMPLEMENTATION_SHA)

        self._write_valid_results(root, package_path)
        extra = core.load_json(results_dir / "batch-001.json")
        core.write_json(results_dir / "batch-999.json", extra)
        with self.assertRaisesRegex(ValueError, "complete and exact"):
            screening.accept_results(root, package_path, results_dir, root / "accepted-extra", IMPLEMENTATION_SHA)

    def test_package_basis_drift_fails_before_acceptance(self) -> None:
        temp, root, cfg = self.sandbox()
        self.addCleanup(temp.cleanup)
        state_path = self.init_thematic(root, cfg)
        discovery_path = root / "sources/SP001/discovery/discovery.jsonl"
        screening.write_jsonl(discovery_path, [self.discovery("SP001", "seed", "BASE")])
        package_path = screening.prepare_package(
            root, state_path, discovery_path, root / "sources/SP001/screening/v2/package", IMPLEMENTATION_SHA
        )
        results_dir = self._write_valid_results(root, package_path)
        discovery_path.write_text(discovery_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "discovery_sha256"):
            screening.accept_results(root, package_path, results_dir, root / "accepted", IMPLEMENTATION_SHA)


if __name__ == "__main__":
    unittest.main()
