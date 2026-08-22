from __future__ import annotations

import copy
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening


IMPLEMENTATION_SHA = "4" * 40
BASE_FILES = [
    "config/survey-production-v2.json",
    "config/weekly-pipeline.json",
    "schemas/survey-production-profile.schema.json",
    "schemas/survey-production-state.schema.json",
]


class SurveyEvidenceV2Tests(unittest.TestCase):
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
            "raw_paths": ["raw/source.json"],
            "published_at": "2025-01-01T00:00:00Z",
            "summary_text": "bounded source summary",
            "metadata": {},
        }

    def discovery(self, issue_id: str, discovery_id: str, origin: str = "BASE") -> dict:
        return {
            "schema_version": "2.0-rc1",
            "issue_id": issue_id,
            "discovery_id": discovery_id,
            "provenance": {
                "origin": origin,
                "research_pass": 0,
                "parent_refs": ["2026-W32:carry"] if origin == "CARRY_OVER" else [],
                "obligation_ids": ["weekly-carry"] if origin == "CARRY_OVER" else [],
                "reason": f"test provenance for {origin}",
            },
            "source": self.source(f"https://example.invalid/{discovery_id}"),
        }

    def init_profile(self, root: Path, cfg: dict, research_profile: str) -> tuple[Path, Path]:
        if research_profile == "THEMATIC":
            profile = core.thematic_profile(
                root,
                cfg,
                {
                    "issue_id": "SP001",
                    "question": "How did a model lineage and its competing branch develop?",
                    "temporal_mode": "OPEN_HISTORY_AS_OF",
                    "as_of": "2026-08-22T02:00:00+09:00",
                    "scope_dimensions": ["lineage", "competition"],
                },
            )
        else:
            profile = core.weekly_profile(
                root,
                cfg,
                core.parse_instant("2026-08-22T02:00:00+09:00"),
                "2026-W33",
            )
        return core.initialize(
            root,
            cfg,
            profile,
            IMPLEMENTATION_SHA,
            "ARCHITECTURE_REVIEW",
            core.parse_instant("2026-08-22T02:05:00+09:00"),
        )

    def make_screening(
        self,
        root: Path,
        state_path: Path,
        records: list[dict],
        decisions: dict[str, str],
    ) -> tuple[Path, Path]:
        issue_id = records[0]["issue_id"]
        discovery_path = root / "sources" / issue_id / "discovery" / "discovery.jsonl"
        screening.write_jsonl(discovery_path, records)
        package_path = screening.prepare_package(
            root,
            state_path,
            discovery_path,
            root / "sources" / issue_id / "screening" / "v2" / "package",
            IMPLEMENTATION_SHA,
        )
        package = core.load_json(package_path)
        results_dir = package_path.parent / "results"
        results_dir.mkdir(parents=True)
        for batch in package["input"]["batches"]:
            batch_rows = screening.read_jsonl(package_path.parent / batch["path"])
            result = {
                "schema_version": "2.0-rc1",
                "issue_id": issue_id,
                "batch_id": batch["batch_id"],
                "basis": screening.expected_result_basis(root, package_path, package, batch),
                "decisions": [
                    {
                        "discovery_id": row["discovery_id"],
                        "decision": decisions[row["discovery_id"]],
                        "reason": "explicit test disposition",
                        "scope_tags": ["lineage"],
                        "duplicate_group": None,
                        "verification_targets": ["subject identity"],
                        "confidence": "high",
                    }
                    for row in batch_rows
                ],
            }
            core.write_json(results_dir / f"{batch['batch_id']}.json", result)
        accepted = screening.accept_results(
            root,
            package_path,
            results_dir,
            root / "sources" / issue_id / "screening" / "v2" / "runs",
            IMPLEMENTATION_SHA,
        )
        return discovery_path, accepted

    @staticmethod
    def card_for_task(root: Path, package_path: Path, task_meta: dict, *, status: str = "VERIFIED") -> dict:
        package = core.load_json(package_path)
        task = core.load_json(package_path.parent / task_meta["path"])
        locator = task["source_records"][0]["locator"]
        return {
            "schema_version": "2.0-rc1",
            "issue_id": package["issue_id"],
            "evidence_task_id": task["evidence_task_id"],
            "basis": {
                "task_sha256": task_meta["sha256"],
                "screening_acceptance_sha256": task["screening_basis"]["screening_acceptance_sha256"],
                "prompt_sha256": package["prompt"]["sha256"],
                "result_contract_sha256": package["contracts"]["card"]["sha256"],
            },
            "status": status,
            "entities": [
                {
                    "entity_id": "target",
                    "canonical_name": "Target Model",
                    "entity_type": "MODEL",
                    "organization": "Example",
                    "canonical_url": locator,
                },
                {
                    "entity_id": "comparator",
                    "canonical_name": "Comparator Model",
                    "entity_type": "MODEL",
                    "organization": "Other",
                    "canonical_url": "https://example.invalid/comparator",
                },
            ],
            "artifact": {
                "primary_subject_id": "target",
                "artifact_type": "MODEL",
                "canonical_name": "Target Model",
                "canonical_url": locator,
            },
            "temporal": {"observed_at": "2026-08-22T02:10:00+09:00", "events": []},
            "sources": [
                {
                    "source_id": "source-1",
                    "url": locator,
                    "source_class": "PRIMARY_PAPER",
                    "title": "Source",
                    "published_at": "2025-01-01T00:00:00Z",
                    "accessed_at": "2026-08-22T02:10:00+09:00",
                    "role": "verification source",
                }
            ],
            "claims": [
                {
                    "statement_id": "claim-1",
                    "text": "Target Model introduces the tested method.",
                    "subject_id": "target",
                    "subject_role": "PRIMARY_SUBJECT",
                    "evidence_class": "AUTHOR_CLAIM",
                    "source_ids": ["source-1"],
                    "context": "source-local claim",
                }
            ],
            "metrics": [],
            "limitations": [],
            "verification": {
                "targets": [
                    {
                        "target": "subject identity",
                        "status": "VERIFIED",
                        "finding": "target and comparator are distinct entities",
                        "subject_ids": ["target", "comparator"],
                        "source_ids": ["source-1"],
                    }
                ],
                "unresolved_questions": [],
                "contradictions": [],
            },
        }

    def make_evidence(
        self,
        root: Path,
        state_path: Path,
        discovery_path: Path,
        screening_acceptance_path: Path,
        *,
        status: str = "VERIFIED",
    ) -> tuple[Path, Path]:
        issue_id = core.load_json(state_path)["issue_id"]
        package_path = evidence.prepare_evidence_package(
            root,
            state_path,
            discovery_path,
            screening_acceptance_path,
            root / "sources" / issue_id / "evidence" / "v2" / "package",
            IMPLEMENTATION_SHA,
        )
        package = core.load_json(package_path)
        results_dir = package_path.parent / "results"
        results_dir.mkdir(parents=True)
        for meta in package["tasks"]:
            card = self.card_for_task(root, package_path, meta, status=status)
            core.write_json(results_dir / Path(meta["path"]).name, card)
        accepted = evidence.accept_evidence_results(
            root,
            package_path,
            results_dir,
            root / "sources" / issue_id / "evidence" / "v2" / "runs",
            IMPLEMENTATION_SHA,
        )
        return package_path, accepted

    def make_views(
        self,
        root: Path,
        profile_path: Path,
        evidence_acceptance_path: Path,
        *,
        materiality: str = "MATERIAL",
    ) -> Path:
        profile = core.load_json(profile_path)
        accepted = core.load_json(evidence_acceptance_path)
        views_dir = root / "views-input"
        views_dir.mkdir(parents=True, exist_ok=True)
        for row in accepted["results"]:
            if profile["research_profile"] == "THEMATIC":
                annotations = {
                    "lineage_role": "CORE",
                    "branch_ids": ["main"],
                    "transition_ids": [],
                    "inheritance_note": "directly relevant to the lineage question",
                    "historical_attribution_caveat": None,
                }
            elif profile["research_profile"] == "WEEKLY":
                annotations = {
                    "why_this_issue": "material within the completed editorial window",
                    "window_relation": "MAIN_EVENT",
                    "carry_over": False,
                }
            else:
                annotations = {"period_role": "chronology", "chronology_relevance": True}
            view = {
                "schema_version": "2.0-rc1",
                "issue_id": profile["issue_id"],
                "research_profile": profile["research_profile"],
                "evidence_task_id": row["evidence_task_id"],
                "evidence_sha256": row["sha256"],
                "materiality": {"status": materiality, "rationale": "explicit edition-level significance"},
                "scope_dimensions": list(profile["research_scope"]["scope_dimensions"][:1]),
                "profile_annotations": annotations,
            }
            core.write_json(views_dir / evidence.view_filename(row["evidence_task_id"]), view)
        return evidence.accept_edition_views(
            root,
            profile_path,
            evidence_acceptance_path,
            views_dir,
            root / "views-accepted",
            IMPLEMENTATION_SHA,
        )

    def make_chain(self, research_profile: str = "THEMATIC", *, include_drop: bool = False):
        temp, root, cfg = self.sandbox()
        self.addCleanup(temp.cleanup)
        profile_path, state_path = self.init_profile(root, cfg, research_profile)
        issue_id = core.load_json(state_path)["issue_id"]
        records = [self.discovery(issue_id, "target-source")]
        decisions = {"target-source": "KEEP"}
        if include_drop:
            records.append(self.discovery(issue_id, "irrelevant-source"))
            decisions["irrelevant-source"] = "DROP"
        discovery_path, screening_acceptance = self.make_screening(root, state_path, records, decisions)
        package_path, evidence_acceptance = self.make_evidence(
            root, state_path, discovery_path, screening_acceptance
        )
        views_acceptance = self.make_views(root, profile_path, evidence_acceptance)
        return root, profile_path, state_path, discovery_path, screening_acceptance, package_path, evidence_acceptance, views_acceptance

    def test_evidence_package_is_exact_and_preserves_task_bytes(self) -> None:
        root, _, _, _, _, package_path, accepted, _ = self.make_chain()
        package = core.load_json(package_path)
        self.assertEqual(package["expected_outputs"], {"one_result_per_task": True, "filename_rule": "same-basename-as-task"})
        self.assertTrue(package["tasks"])
        acceptance = core.load_json(accepted)
        for meta in package["tasks"]:
            name = Path(meta["path"]).name
            self.assertTrue((accepted.parent / "tasks" / name).is_file())
            self.assertTrue((accepted.parent / "results" / name).is_file())
        evidence.validate_evidence_acceptance(root, accepted, IMPLEMENTATION_SHA)
        self.assertEqual(acceptance["result_set_sha256"], accepted.parent.name)

    def test_evidence_result_set_rejects_extra_artifacts_and_detects_accepted_tampering(self) -> None:
        temp, root, cfg = self.sandbox()
        self.addCleanup(temp.cleanup)
        profile_path, state_path = self.init_profile(root, cfg, "THEMATIC")
        discovery_path, screening_acceptance = self.make_screening(
            root, state_path, [self.discovery("SP001", "target-source")], {"target-source": "KEEP"}
        )
        package_path = evidence.prepare_evidence_package(
            root, state_path, discovery_path, screening_acceptance,
            root / "sources/SP001/evidence/v2/package", IMPLEMENTATION_SHA
        )
        package = core.load_json(package_path)
        results_dir = package_path.parent / "results"
        results_dir.mkdir()
        meta = package["tasks"][0]
        card = self.card_for_task(root, package_path, meta)
        core.write_json(results_dir / Path(meta["path"]).name, card)
        (results_dir / "README.txt").write_text("unexpected", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "complete and exact"):
            evidence.accept_evidence_results(root, package_path, results_dir, root / "accepted-extra", IMPLEMENTATION_SHA)
        (results_dir / "README.txt").unlink()
        accepted = evidence.accept_evidence_results(root, package_path, results_dir, root / "accepted", IMPLEMENTATION_SHA)
        result_file = next((accepted.parent / "results").iterdir())
        result_file.write_text(result_file.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "accepted Evidence result changed"):
            evidence.validate_evidence_acceptance(root, accepted, IMPLEMENTATION_SHA)

    def test_factual_evidence_rejects_editorial_fields_and_unregistered_sources(self) -> None:
        root, _, _, _, _, package_path, _, _ = self.make_chain()
        package = core.load_json(package_path)
        meta = package["tasks"][0]
        task = core.load_json(package_path.parent / meta["path"])
        card = self.card_for_task(root, package_path, meta)
        card["editorial"] = {"why_now": "forbidden"}
        self.assertIn("editorial fields are forbidden", "; ".join(evidence.validate_evidence_card(card, task, meta["sha256"], package)))
        card = self.card_for_task(root, package_path, meta)
        card["sources"][0]["url"] = "https://example.invalid/hidden-new-source"
        self.assertIn("add it through Discovery/Screening first", "; ".join(evidence.validate_evidence_card(card, task, meta["sha256"], package)))

    def test_issue_191_comparator_owned_metric_cannot_bind_primary_subject(self) -> None:
        root, _, _, _, _, package_path, _, _ = self.make_chain()
        package = core.load_json(package_path)
        meta = package["tasks"][0]
        task = core.load_json(package_path.parent / meta["path"])
        card = self.card_for_task(root, package_path, meta)
        card["metrics"] = [
            {
                "metric_id": "parameters-405b",
                "name": "parameter scale",
                "value": "405",
                "unit": "B",
                "context": "comparison row adjacent to the target",
                "subject_id": "target",
                "subject_role": "COMPARATOR",
                "comparison_subject_ids": ["comparator"],
                "evidence_class": "PRIMARY_FACT",
                "source_ids": ["source-1"],
            }
        ]
        errors = evidence.validate_evidence_card(card, task, meta["sha256"], package)
        self.assertTrue(any("COMPARATOR cannot bind artifact.primary_subject_id" in error for error in errors))

        card["metrics"][0]["subject_id"] = "comparator"
        card["metrics"][0]["comparison_subject_ids"] = ["target"]
        self.assertEqual(evidence.validate_evidence_card(card, task, meta["sha256"], package), [])

    def test_materiality_ledger_prevents_issue_166_silent_drop_and_preserves_non_material_state(self) -> None:
        root, profile_path, _, discovery_path, screening_acceptance, _, evidence_acceptance, views_acceptance = self.make_chain(include_drop=True)
        ledger = evidence.build_materiality_ledger(
            root, profile_path, discovery_path, screening_acceptance, evidence_acceptance,
            views_acceptance, IMPLEMENTATION_SHA
        )
        self.assertEqual({row["discovery_id"] for row in ledger["rows"]}, {"target-source", "irrelevant-source"})
        dispositions = {row["discovery_id"]: row["downstream_disposition"] for row in ledger["rows"]}
        self.assertEqual(dispositions["target-source"], "MATERIAL")
        self.assertEqual(dispositions["irrelevant-source"], "EXCLUDED")

        missing = copy.deepcopy(ledger)
        missing["rows"] = missing["rows"][:-1]
        with self.assertRaisesRegex(ValueError, "exactly one row per Discovery"):
            evidence.validate_materiality_ledger(
                missing, root, profile_path, discovery_path, screening_acceptance,
                evidence_acceptance, views_acceptance, IMPLEMENTATION_SHA
            )
        extra = copy.deepcopy(ledger)
        extra["rows"].append(copy.deepcopy(extra["rows"][0]))
        extra["rows"][-1]["discovery_id"] = "invented"
        with self.assertRaisesRegex(ValueError, "exactly one row per Discovery"):
            evidence.validate_materiality_ledger(
                extra, root, profile_path, discovery_path, screening_acceptance,
                evidence_acceptance, views_acceptance, IMPLEMENTATION_SHA
            )

    def test_thematic_closure_requires_no_open_material_obligations_and_gap_fill(self) -> None:
        root, profile_path, _, discovery_path, screening_acceptance, _, evidence_acceptance, views_acceptance = self.make_chain()
        ledger = evidence.build_materiality_ledger(
            root, profile_path, discovery_path, screening_acceptance, evidence_acceptance,
            views_acceptance, IMPLEMENTATION_SHA
        )
        ledger_path = evidence.write_materiality_ledger(root / "materiality.json", ledger)
        basis = {
            "production_profile_sha256": core.sha256_file(profile_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
        }
        ready = {
            "schema_version": "2.0-rc1",
            "issue_id": "SP001",
            "research_profile": "THEMATIC",
            "basis": basis,
            "overall_status": "READY",
            "obligations": [
                {
                    "obligation_id": "lineage",
                    "dimension": "lineage",
                    "description": "trace the main lineage",
                    "status": "SATISFIED",
                    "discovery_ids": ["target-source"],
                    "evidence_task_ids": [ledger["rows"][0]["evidence_task_ids"][0]],
                    "rationale": "verified Evidence covers the lineage obligation",
                },
                {
                    "obligation_id": "competition",
                    "dimension": "competition",
                    "description": "check competing branches",
                    "status": "SATISFIED",
                    "discovery_ids": ["target-source"],
                    "evidence_task_ids": [ledger["rows"][0]["evidence_task_ids"][0]],
                    "rationale": "competing branch search was explicitly disposed",
                },
            ],
            "residual_limitations": [],
            "closure": {
                "expansion_passes": 2,
                "final_pass_new_sources": 0,
                "final_pass_new_material_obligations": 0,
                "final_pass_new_material_obligations_open": 0,
                "targeted_gap_fill_completed": True,
                "open_material_obligations": 0,
                "limitations": [],
                "status": "COMPLETE",
            },
        }
        self.assertEqual(
            evidence.validate_completeness(
                ready, root, profile_path, discovery_path, screening_acceptance,
                evidence_acceptance, views_acceptance, ledger_path, IMPLEMENTATION_SHA
            ),
            [],
        )
        open_gap = copy.deepcopy(ready)
        open_gap["obligations"][0]["status"] = "NEEDS_RESEARCH"
        open_gap["overall_status"] = "READY"
        open_gap["closure"]["open_material_obligations"] = 1
        open_gap["closure"]["final_pass_new_material_obligations"] = 1
        open_gap["closure"]["final_pass_new_material_obligations_open"] = 1
        open_gap["closure"]["targeted_gap_fill_completed"] = False
        open_gap["closure"]["status"] = "COMPLETE"
        errors = evidence.validate_completeness(
            open_gap, root, profile_path, discovery_path, screening_acceptance,
            evidence_acceptance, views_acceptance, ledger_path, IMPLEMENTATION_SHA
        )
        self.assertTrue(any("overall_status must be INCOMPLETE" in error for error in errors))
        self.assertTrue(any("Thematic closure status must be NEEDS_RESEARCH" in error for error in errors))

    def test_weekly_completeness_does_not_require_thematic_closure(self) -> None:
        root, profile_path, _, discovery_path, screening_acceptance, _, evidence_acceptance, views_acceptance = self.make_chain("WEEKLY")
        ledger = evidence.build_materiality_ledger(
            root, profile_path, discovery_path, screening_acceptance, evidence_acceptance,
            views_acceptance, IMPLEMENTATION_SHA
        )
        ledger_path = evidence.write_materiality_ledger(root / "weekly-materiality.json", ledger)
        profile = core.load_json(profile_path)
        obligations = [
            {
                "obligation_id": f"weekly-{dimension}",
                "dimension": dimension,
                "description": f"cover {dimension}",
                "status": "SATISFIED",
                "discovery_ids": ["target-source"],
                "evidence_task_ids": [ledger["rows"][0]["evidence_task_ids"][0]],
                "rationale": "weekly scope obligation disposed",
            }
            for dimension in profile["research_scope"]["scope_dimensions"]
        ]
        result = {
            "schema_version": "2.0-rc1",
            "issue_id": profile["issue_id"],
            "research_profile": "WEEKLY",
            "basis": {
                "production_profile_sha256": core.sha256_file(profile_path),
                "materiality_ledger_sha256": core.sha256_file(ledger_path),
            },
            "overall_status": "READY",
            "obligations": obligations,
            "residual_limitations": [],
            "closure": None,
        }
        self.assertEqual(
            evidence.validate_completeness(
                result, root, profile_path, discovery_path, screening_acceptance,
                evidence_acceptance, views_acceptance, ledger_path, IMPLEMENTATION_SHA
            ),
            [],
        )


if __name__ == "__main__":
    unittest.main()
