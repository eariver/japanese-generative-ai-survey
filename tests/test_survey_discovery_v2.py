from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts import survey_discovery_v2 as discovery
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_x_intake_v2 as xintake


class SurveyDiscoveryV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.source_root = Path(".").resolve()
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for rel in (
            discovery.DISCOVERY_ACCEPTANCE_SCHEMA,
            xintake.MANIFEST_SCHEMA,
            core.DEFAULT_CONFIG,
            xintake.BASE_PROMPT,
            xintake.WEEKLY_PROMPT,
            xintake.SPECIAL_PROMPT,
        ):
            src = self.source_root / rel
            dst = self.root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        (self.root / "raw").mkdir()
        (self.root / "raw/source-a.json").write_text('{"a":1}\n', encoding="utf-8")
        (self.root / "raw/source-b.json").write_text('{"b":2}\n', encoding="utf-8")
        self.cfg = core.load_json(self.root / core.DEFAULT_CONFIG)
        self.profile_path = self.root / "sources/SP001/production-profile.json"
        dummy = "a" * 64
        core.write_json(
            self.profile_path,
            {
                "schema_version": "2.0-rc1",
                "issue_id": "SP001",
                "research_profile": "THEMATIC",
                "publication_profile": "LONGFORM_SPECIAL",
                "research_scope": {
                    "question": "Fixture thematic question",
                    "inclusion": [],
                    "exclusion": [],
                    "scope_dimensions": ["coverage"],
                    "initial_obligations": [
                        {
                            "obligation_id": "fixture:coverage",
                            "dimension": "coverage",
                            "description": "Establish fixture coverage.",
                        }
                    ],
                    "temporal_policy": {
                        "mode": "OPEN_HISTORY_AS_OF",
                        "as_of": "2026-08-22T09:00:00Z",
                    },
                },
                "paths": {
                    "source_root": "sources/SP001",
                    "survey_root": "surveys/special/SP001",
                    "work_branch": "test/SP001",
                },
                "contract": {
                    "pipeline_contract_version": "fixture",
                    "pipeline_contract_sha256": dummy,
                    "quality_contract_version": "fixture",
                    "quality_contract_sha256": dummy,
                    "research_profile_version": "fixture",
                    "research_profile_sha256": dummy,
                    "publication_profile_version": "fixture",
                    "publication_profile_sha256": dummy,
                },
            },
        )
        self.x_manifest = xintake.build_manifest(
            self.root,
            self.cfg,
            self.profile_path,
            {
                "decision": "NOT_REQUIRED",
                "rationale": "This Discovery unit fixture does not need X community signal.",
                "series_context": None,
                "runs": [],
            },
        )

    @staticmethod
    def _record(discovery_id: str, origin: str, *, research_pass: int, parents=None, obligations=None, raw="raw/source-a.json") -> dict:
        return {
            "schema_version": "2.0-rc1",
            "issue_id": "SP001",
            "discovery_id": discovery_id,
            "provenance": {
                "origin": origin,
                "research_pass": research_pass,
                "parent_refs": parents or [],
                "obligation_ids": obligations or [],
                "reason": f"fixture {origin}",
            },
            "source": {
                "source_type": "paper",
                "collector_id": "fixture-collector",
                "collector_run_id": "run-1",
                "observed_at": "2026-08-22T02:00:00+09:00",
                "title": discovery_id,
                "locator": f"https://example.invalid/{discovery_id}",
                "raw_paths": [raw],
                "published_at": None,
                "summary_text": None,
                "metadata": {},
            },
        }

    def _write_discovery(self, records: list[dict]) -> Path:
        path = self.root / "sources/SP001/discovery/discovery.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as fh:
            for record in records:
                fh.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
        return path

    def _accept(self, path: Path) -> Path:
        return discovery.build_acceptance(
            self.root,
            path,
            self.x_manifest,
            "SP001",
            path.parent / "discovery-accepted.json",
        )

    def test_acceptance_resolves_same_run_and_external_namespaces(self) -> None:
        path = self._write_discovery(
            [
                self._record("seed", "BASE", research_pass=0),
                self._record("ref", "REFERENCE_EXPANSION", research_pass=1, parents=["local:seed"]),
                self._record(
                    "carry",
                    "CARRY_OVER",
                    research_pass=0,
                    parents=["external:2026-W32:model-x"],
                    obligations=["weekly-carry-over:model-x"],
                    raw="raw/source-b.json",
                ),
                self._record("gap", "GAP_FILL", research_pass=2, obligations=["branch-gap"]),
            ]
        )
        accepted = self._accept(path)
        payload = discovery.validate_acceptance(self.root, accepted)
        by_id = {row["discovery_id"]: row for row in payload["records"]}
        self.assertEqual(by_id["ref"]["parent_edges"][0]["scope"], "SAME_RUN")
        self.assertEqual(by_id["carry"]["parent_edges"][0]["scope"], "EXTERNAL")
        self.assertEqual(by_id["gap"]["method"]["trigger"]["kind"], "OBLIGATION_GAP")
        self.assertEqual(by_id["seed"]["method"]["trigger"]["kind"], "PROFILE_SEED")
        self.assertEqual(by_id["seed"]["raw_refs"][0]["sha256"], core.sha256_file(self.root / "raw/source-a.json"))
        self.assertEqual(payload["x_source_intake"]["sha256"], core.sha256_file(self.x_manifest))

    def test_dangling_same_run_edge_fails_closed(self) -> None:
        path = self._write_discovery(
            [self._record("ref", "REFERENCE_EXPANSION", research_pass=1, parents=["local:missing"])]
        )
        with self.assertRaisesRegex(ValueError, "dangling same-run parent"):
            self._accept(path)

    def test_same_run_parent_must_be_from_earlier_research_pass(self) -> None:
        path = self._write_discovery(
            [
                self._record("seed", "BASE", research_pass=1),
                self._record("ref", "REFERENCE_EXPANSION", research_pass=1, parents=["local:seed"]),
            ]
        )
        with self.assertRaisesRegex(ValueError, "research_pass must be greater"):
            self._accept(path)

    def test_ambiguous_parent_namespace_is_rejected(self) -> None:
        path = self._write_discovery(
            [
                self._record("seed", "BASE", research_pass=0),
                self._record("ref", "REFERENCE_EXPANSION", research_pass=1, parents=["seed"]),
            ]
        )
        with self.assertRaisesRegex(ValueError, "explicit local"):
            self._accept(path)

    def test_raw_byte_drift_invalidates_accepted_discovery(self) -> None:
        path = self._write_discovery([self._record("seed", "BASE", research_pass=0)])
        accepted = self._accept(path)
        (self.root / "raw/source-a.json").write_text('{"a":999}\n', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "differs from current Discovery/Raw bytes"):
            discovery.validate_acceptance(self.root, accepted)

    def test_x_manifest_byte_drift_invalidates_accepted_discovery(self) -> None:
        path = self._write_discovery([self._record("seed", "BASE", research_pass=0)])
        accepted = self._accept(path)
        payload = core.load_json(self.x_manifest)
        payload["rationale"] = "Changed after Discovery acceptance."
        core.write_json(self.x_manifest, payload)
        with self.assertRaisesRegex(ValueError, "X Source Intake manifest SHA drift"):
            discovery.validate_acceptance(self.root, accepted)

    def test_schema_gate_rejects_structurally_invalid_acceptance_before_semantics(self) -> None:
        invalid = {
            "schema_version": "2.0-rc1",
            "issue_id": "SP001",
            "x_source_intake": {"path": "missing.json", "sha256": "f" * 64},
            "discovery_path": "sources/SP001/discovery/discovery.jsonl",
            "discovery_sha256": "0" * 64,
            "record_count": 1,
            "records": [],
            "graph_sha256": "1" * 64,
            "unexpected": True,
        }
        with self.assertRaises(schema_gate.SchemaConformanceError):
            schema_gate.validate_instance(invalid, self.root / discovery.DISCOVERY_ACCEPTANCE_SCHEMA, label="Discovery acceptance")


if __name__ == "__main__":
    unittest.main()
