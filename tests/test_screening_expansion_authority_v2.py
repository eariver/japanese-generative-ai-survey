from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import survey_discovery_v2 as discovery
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening
from tests import test_survey_screening_v2 as screening_tests


IMPLEMENTATION_SHA = "3" * 40


class SurveyScreeningExpansionAuthorityV2Tests(unittest.TestCase):
    def _source(self, raw_path: str, locator: str) -> dict:
        return {
            "source_type": "paper",
            "collector_id": "fixture-collector",
            "collector_run_id": "fixture-run-001",
            "observed_at": "2026-08-22T02:00:00+09:00",
            "title": locator,
            "locator": locator,
            "raw_paths": [raw_path],
            "published_at": "2025-01-01T00:00:00Z",
            "summary_text": "bounded source observation",
            "metadata": {},
        }

    def _record(
        self,
        discovery_id: str,
        origin: str,
        raw_path: str,
        locator: str,
        *,
        parent_refs: list[str] | None = None,
        obligation_ids: list[str] | None = None,
        research_pass: int = 0,
    ) -> dict:
        return {
            "schema_version": "2.0-rc1",
            "issue_id": "SP-EXPANSION",
            "discovery_id": discovery_id,
            "provenance": {
                "origin": origin,
                "research_pass": research_pass,
                "parent_refs": parent_refs or [],
                "obligation_ids": obligation_ids or [],
                "reason": f"fixture provenance for {discovery_id}",
            },
            "source": self._source(raw_path, locator),
        }

    def _root_and_children(self, root: Path) -> tuple[list[dict], list[dict]]:
        raw = root / "raw/shared.json"
        raw_b = root / "raw/root-b.json"
        raw.parent.mkdir(parents=True, exist_ok=True)
        raw.write_text('{"fixture":"shared"}\n', encoding="utf-8")
        raw_b.write_text('{"fixture":"root-b"}\n', encoding="utf-8")
        root_records = [
            self._record(
                "root-a", "BASE", "raw/shared.json", "https://example.invalid/root-a",
                obligation_ids=["obligation:scope"],
            ),
            self._record(
                "root-b", "BASE", "raw/root-b.json", "https://example.invalid/root-b",
                obligation_ids=["obligation:scope"],
            ),
        ]
        children = [
            self._record(
                "child-1", "REFERENCE_EXPANSION", "raw/shared.json", "https://example.invalid/root-a",
                parent_refs=["root-a"], obligation_ids=["obligation:scope"], research_pass=1,
            ),
            self._record(
                "child-2", "REFERENCE_EXPANSION", "raw/shared.json", "https://example.invalid/root-a",
                parent_refs=["root-a"], obligation_ids=["obligation:scope"], research_pass=1,
            ),
        ]
        return root_records, children

    def test_valid_one_to_many_expansion_is_rooted_and_surfaces_disjoint_roots(self) -> None:
        with self.subTest("one-to-many"):
            with tempfile.TemporaryDirectory() as raw_root:
                root = Path(raw_root)
                root_records, children = self._root_and_children(root)
                result = screening.validate_discovery_expansion(
                    root, root_records, children, "SP-EXPANSION"
                )
                self.assertEqual(result["accounted_root_ids"], ["root-a"])
                self.assertEqual(result["unaccounted_root_ids"], ["root-b"])

    def test_expansion_fail_close_cases(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            root_records, children = self._root_and_children(root)

            cases = {
                "orphan parent": (lambda row: row["provenance"].update({"parent_refs": ["missing-root"]}), "outside accepted root"),
                "other parent set": (lambda row: row["provenance"].update({"parent_refs": ["other-issue:root"]}), "outside accepted root"),
                "invented Raw": (lambda row: row["source"].update({"raw_paths": ["raw/invented.json"]}), "outside declared parent Raw union"),
                "unrelated source": (lambda row: row["source"].update({"locator": "https://example.invalid/unrelated"}), "source identity"),
                "silent root omission": (lambda row: row["provenance"].update({"parent_refs": ["root-a"]}), "silently omitted"),
                "unrelated BASE substitution": (lambda row: row.update({"discovery_id": "unrelated", "provenance": {
                    "origin": "BASE", "research_pass": 0, "parent_refs": [], "obligation_ids": [], "reason": "unrelated valid record"
                }}), "parent-requiring expansion origin"),
            }
            for label, (mutate, message) in cases.items():
                with self.subTest(label=label):
                    candidate = copy.deepcopy(children)
                    if label == "silent root omission":
                        root_for_case = copy.deepcopy(root_records)
                        root_for_case[1]["source"]["raw_paths"] = ["raw/shared.json"]
                        candidate[0]["source"]["locator"] = "https://example.invalid/root-a"
                        with self.assertRaisesRegex(ValueError, message):
                            screening.validate_discovery_expansion(root, root_for_case, candidate, "SP-EXPANSION")
                        continue
                    mutate(candidate[0])
                    if label == "invented Raw":
                        (root / "raw/invented.json").write_text('{"fixture":"invented"}\n', encoding="utf-8")
                    with self.assertRaisesRegex(ValueError, message):
                        screening.validate_discovery_expansion(root, root_records, candidate, "SP-EXPANSION")

    def test_derived_screening_and_evidence_use_event_ids(self) -> None:
        helper = screening_tests.SurveyScreeningV2Tests(
            methodName="test_discovery_set_rejects_duplicate_ids"
        )
        helper.setUp()
        temp, root, cfg = helper.sandbox()
        self.addCleanup(temp.cleanup)
        state_path = helper.init_thematic(root, cfg, "SP-EXPANSION")
        root_records, children = self._root_and_children(root)
        root_path = root / "sources/SP-EXPANSION/discovery/discovery.jsonl"
        derived_path = root / "sources/SP-EXPANSION/screening/input/event-discovery.jsonl"
        screening.write_jsonl(root_path, root_records)
        screening.write_jsonl(derived_path, children)
        acceptance_marker = root / "sources/SP-EXPANSION/discovery/discovery-accepted-v2.json"
        core.write_json(acceptance_marker, {"fixture": "patched authority"})
        normalized_root = [discovery._normalize_record(root, row, "SP-EXPANSION") for row in root_records]

        def fake_root_acceptance(repo_root: Path, acceptance_path: Path) -> dict:
            return {
                "issue_id": "SP-EXPANSION",
                "discovery_path": str(root_path.relative_to(root)),
                "discovery_sha256": core.sha256_file(root_path),
                "records": normalized_root,
            }

        with patch.object(discovery, "validate_acceptance", side_effect=fake_root_acceptance):
            package_path = screening.prepare_package(
                root,
                state_path,
                derived_path,
                root / "sources/SP-EXPANSION/screening/v2/package",
                IMPLEMENTATION_SHA,
            )
            package = core.load_json(package_path)
            results_dir = package_path.parent / "results"
            results_dir.mkdir()
            for batch in package["input"]["batches"]:
                rows = screening.read_jsonl(package_path.parent / batch["path"])
                core.write_json(
                    results_dir / f"{batch['batch_id']}.json",
                    {
                        "schema_version": "2.0-rc1",
                        "issue_id": package["issue_id"],
                        "batch_id": batch["batch_id"],
                        "basis": screening.expected_result_basis(root, package_path, package, batch),
                        "decisions": [
                            {
                                "discovery_id": row["discovery_id"],
                                "decision": "KEEP",
                                "reason": "screen independently",
                                "scope_tags": ["fixture"],
                                "duplicate_group": None,
                                "verification_targets": ["canonical source"],
                                "confidence": "high",
                            }
                            for row in rows
                        ],
                    },
                )
            accepted = screening.accept_results(
                root,
                package_path,
                results_dir,
                root / "sources/SP-EXPANSION/screening/v2/runs",
                IMPLEMENTATION_SHA,
            )
            resolved = screening.resolve_effective_discovery_basis(root, package_path)
            self.assertEqual(resolved["mode"], "DERIVED_EXPANSION")
            self.assertEqual(
                {row["discovery_id"] for row in resolved["records"]}, {"child-1", "child-2"}
            )
            evidence_package = evidence.prepare_evidence_package(
                root,
                state_path,
                derived_path,
                accepted,
                root / "sources/SP-EXPANSION/evidence/v2/package",
                IMPLEMENTATION_SHA,
            )
            evidence_payload = core.load_json(evidence_package)
            self.assertEqual(len(evidence_payload["tasks"]), 2)
            self.assertEqual(
                {row["discovery_ids"][0] for row in evidence_payload["tasks"]},
                {"child-1", "child-2"},
            )

            unrelated_path = root / "sources/SP-EXPANSION/screening/input/unrelated.jsonl"
            unrelated = self._record(
                "unrelated", "BASE", "raw/shared.json", "https://example.invalid/unrelated"
            )
            screening.write_jsonl(unrelated_path, [unrelated])
            bad_package = copy.deepcopy(package)
            bad_package["basis"]["discovery_path"] = str(unrelated_path.relative_to(root))
            bad_package["basis"]["discovery_sha256"] = core.sha256_file(unrelated_path)
            bad_package_path = root / "sources/SP-EXPANSION/screening/v2/bad-package.json"
            core.write_json(bad_package_path, bad_package)
            with self.assertRaisesRegex(ValueError, "parent-requiring expansion origin"):
                screening.resolve_effective_discovery_basis(root, bad_package_path)


if __name__ == "__main__":
    unittest.main()
