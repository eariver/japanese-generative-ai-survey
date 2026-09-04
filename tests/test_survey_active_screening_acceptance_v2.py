from __future__ import annotations

import copy
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_discovery_v2 as discovery
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening
from scripts import survey_x_intake_v2 as x_intake


class SurveyActiveScreeningAcceptanceV2Tests(unittest.TestCase):
    """Regression coverage for checkpoint-bound active Screening authority."""

    def setUp(self) -> None:
        self.repo_root = Path(".").resolve()
        self.cfg = core.load_json(self.repo_root / core.DEFAULT_CONFIG)
        self.implementation = core.repository_commit_sha(self.repo_root)

    def _sandbox(self) -> tuple[tempfile.TemporaryDirectory[str], Path, dict, Path]:
        temp = tempfile.TemporaryDirectory(dir=self.repo_root)
        root = Path(temp.name)
        required = [
            "config/survey-production-v2.json",
            "config/weekly-pipeline.json",
            "schemas/survey-production-profile.schema.json",
            "schemas/survey-production-state.schema.json",
            *self.cfg["contract_files"]["pipeline"],
            *self.cfg["contract_files"]["quality"],
        ]
        for rel in dict.fromkeys(required):
            source = self.repo_root / rel
            target = root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        cfg = core.load_json(root / core.DEFAULT_CONFIG)
        source_root = root / "sources/SP-ACTIVE"
        profile = core.thematic_profile(
            root,
            cfg,
            {
                "issue_id": "SP-ACTIVE",
                "question": "Which immutable Screening run is active?",
                "temporal_mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-09-04T00:00:00Z",
                "scope_dimensions": ["authority"],
            },
        )
        _, state_path = core.initialize(
            root,
            cfg,
            profile,
            self.implementation,
            "ARCHITECTURE_REVIEW",
            core.parse_instant("2026-09-04T00:00:00Z"),
        )
        self.assertTrue(source_root.is_dir())
        return temp, root, cfg, state_path

    @staticmethod
    def _record(root: Path, discovery_id: str) -> dict:
        raw = root / "sources/SP-ACTIVE/raw/shared.json"
        raw.parent.mkdir(parents=True, exist_ok=True)
        if not raw.exists():
            raw.write_text('{"fixture":"active-screening"}\n', encoding="utf-8")
        return {
            "schema_version": "2.0-rc1",
            "issue_id": "SP-ACTIVE",
            "discovery_id": discovery_id,
            "provenance": {
                "origin": "BASE",
                "research_pass": 0,
                "parent_refs": [],
                "obligation_ids": [],
                "reason": "active Screening authority fixture",
            },
            "source": {
                "source_type": "paper",
                "collector_id": "active-fixture",
                "collector_run_id": "active-run-001",
                "observed_at": "2026-09-03T23:00:00Z",
                "title": discovery_id,
                "locator": f"https://example.invalid/{discovery_id}",
                "raw_paths": ["sources/SP-ACTIVE/raw/shared.json"],
                "published_at": "2026-09-03T00:00:00Z",
                "summary_text": "bounded active-authority fixture",
                "metadata": {},
            },
        }

    def _write_stage_reviews(
        self,
        root: Path,
        cfg: dict,
        state_path: Path,
        artifacts: dict[str, Path],
        name: str,
    ) -> Path:
        state = core.load_json(state_path)
        profile_path = root / state["profile"]["path"]
        profile = core.load_json(profile_path)
        stage = cfg["orchestration"]["stage_plan"][state["lifecycle_state"]]
        artifact_rows = [
            {
                "name": artifact_name,
                "path": str(path.relative_to(root)),
                "sha256": core.sha256_file(path),
            }
            for artifact_name, path in sorted(artifacts.items())
        ]
        result_path = root / profile["paths"]["source_root"] / "reviews" / f"{name}-core.json"
        core.write_json(
            result_path,
            {
                "schema_version": "2.0-rc1",
                "check_id": "CORE_STAGE_CONTRACT",
                "status": "PASS",
                "issue_id": state["issue_id"],
                "from_state": state["lifecycle_state"],
                "to_state": stage["next_state"],
                "production_state": {
                    "path": str(state_path.relative_to(root)),
                    "sha256": core.sha256_file(state_path),
                },
                "production_profile": {
                    "path": str(profile_path.relative_to(root)),
                    "sha256": core.sha256_file(profile_path),
                },
                "implementation_commit_sha": self.implementation,
                "contract": core.contract_identity(
                    root,
                    cfg,
                    state["research_profile"],
                    state["publication_profile"],
                ),
                "artifacts": artifact_rows,
                "recorded_at": "2026-09-04T00:05:00Z",
            },
        )
        review_path = root / profile["paths"]["source_root"] / "reviews" / f"{name}.json"
        core.write_json(
            review_path,
            {
                "reviews": [
                    {
                        "check_id": "CORE_STAGE_CONTRACT",
                        "kind": "DETERMINISTIC",
                        "executor": "active-acceptance-fixture",
                        "evidence": "exact State/Profile/checkpoint artifact contract passed",
                        "result_path": str(result_path.relative_to(root)),
                    }
                ]
            },
        )
        return review_path

    def _write_results(self, root: Path, package_path: Path, decision: str, label: str) -> Path:
        package = core.load_json(package_path)
        results_dir = package_path.parent / f"results-{label}"
        results_dir.mkdir(parents=True, exist_ok=True)
        for batch in package["input"]["batches"]:
            rows = screening.read_jsonl(package_path.parent / batch["path"])
            decisions = [
                {
                    "discovery_id": row["discovery_id"],
                    "decision": decision,
                    "reason": f"{label} immutable Screening fixture",
                    "scope_tags": ["fixture"],
                    "duplicate_group": None,
                    "verification_targets": [],
                    "confidence": "high",
                }
                for row in rows
            ]
            core.write_json(
                results_dir / f"{batch['batch_id']}.json",
                {
                    "schema_version": "2.0-rc1",
                    "issue_id": package["issue_id"],
                    "batch_id": batch["batch_id"],
                    "basis": screening.expected_result_basis(root, package_path, package, batch),
                    "decisions": decisions,
                },
            )
        return results_dir

    def _fixture(self, *, reverse_run_creation: bool = False) -> dict:
        temp, root, cfg, state_path = self._sandbox()
        self.addCleanup(temp.cleanup)
        source_root = root / "sources/SP-ACTIVE"
        discovery_path = source_root / "discovery/discovery-v2.jsonl"
        records = [self._record(root, "active-a"), self._record(root, "active-b")]
        screening.write_jsonl(discovery_path, records)

        spec_path = source_root / "external/x/spec.json"
        core.write_json(
            spec_path,
            {
                "decision": "NOT_REQUIRED",
                "rationale": "active-authority fixture does not require X intake",
                "series_context": None,
                "runs": [],
            },
        )
        profile_path = root / core.load_json(state_path)["profile"]["path"]
        x_manifest = x_intake.build_manifest(
            root,
            cfg,
            profile_path,
            core.load_json(spec_path),
            source_root / "external/x/x-source-intake-v2.json",
        )
        root_acceptance_path = source_root / "discovery/discovery-accepted-v2.json"
        discovery.build_acceptance(
            root,
            discovery_path,
            x_manifest,
            "SP-ACTIVE",
            root_acceptance_path,
        )

        package_path = screening.prepare_package(
            root,
            state_path,
            discovery_path,
            source_root / "screening/v2/package",
            self.implementation,
        )
        accepted_root = source_root / "screening/v2/accepted"
        creation = [
            ("corrected", "MAYBE"),
            ("historical", "KEEP"),
        ] if reverse_run_creation else [
            ("historical", "KEEP"),
            ("corrected", "MAYBE"),
        ]
        accepted: dict[str, Path] = {}
        for label, decision in creation:
            results = self._write_results(root, package_path, decision, label)
            accepted[label] = screening.accept_results(
                root, package_path, results, accepted_root, self.implementation
            )

        discovery_reviews = self._write_stage_reviews(
            root,
            cfg,
            state_path,
            {"discovery-acceptance": root_acceptance_path},
            "discovery",
        )
        discovery_checkpoint = agent.build_stage_checkpoint(
            root,
            cfg,
            state_path,
            {"discovery-acceptance": root_acceptance_path},
            discovery_reviews,
            "accepted root Discovery fixture is ready",
            core.parse_instant("2026-09-04T00:10:00Z"),
            self.implementation,
        )
        agent.advance_with_checkpoint(root, cfg, state_path, discovery_checkpoint)

        screening_reviews = self._write_stage_reviews(
            root,
            cfg,
            state_path,
            {"screening-acceptance": accepted["corrected"]},
            "screening",
        )
        screening_checkpoint = agent.build_stage_checkpoint(
            root,
            cfg,
            state_path,
            {"screening-acceptance": accepted["corrected"]},
            screening_reviews,
            "corrected Screening acceptance is adopted by checkpoint authority",
            core.parse_instant("2026-09-04T00:20:00Z"),
            self.implementation,
        )
        agent.advance_with_checkpoint(root, cfg, state_path, screening_checkpoint)
        return {
            "temp": temp,
            "root": root,
            "cfg": cfg,
            "state_path": state_path,
            "accepted": accepted,
            "checkpoint": screening_checkpoint,
        }

    def _alternate_state(self, fixture: dict, state: dict, name: str) -> Path:
        path = fixture["root"] / f"{name}.json"
        core.write_json(path, state)
        return path

    def test_two_immutable_runs_coexist_and_checkpoint_selects_corrected(self) -> None:
        fixture = self._fixture()
        root = fixture["root"]
        accepted_root = root / "sources/SP-ACTIVE/screening/v2/accepted"
        self.assertEqual(len(list(accepted_root.glob("*/screening-accepted.json"))), 2)
        self.assertNotEqual(fixture["accepted"]["historical"], fixture["accepted"]["corrected"])
        resolved = screening.resolve_active_screening_acceptance(
            root, fixture["state_path"], self.implementation
        )
        self.assertEqual(resolved["path"].resolve(), fixture["accepted"]["corrected"].resolve())
        self.assertNotEqual(resolved["path"].resolve(), fixture["accepted"]["historical"].resolve())
        self.assertEqual(resolved["acceptance"]["decisions"][0]["decision"], "MAYBE")

    def test_directory_creation_order_does_not_change_checkpoint_selection(self) -> None:
        fixture = self._fixture(reverse_run_creation=True)
        resolved = screening.resolve_active_screening_acceptance(
            fixture["root"], fixture["state_path"], self.implementation
        )
        self.assertEqual(resolved["path"].resolve(), fixture["accepted"]["corrected"].resolve())

    def test_explicit_historical_acceptance_remains_backward_compatible(self) -> None:
        fixture = self._fixture()
        from scripts import survey_agent_tool_v2 as runtime_tool

        with runtime_tool.current_stage_basis_override():
            historical = screening.validate_acceptance(
                fixture["root"], fixture["accepted"]["historical"], self.implementation
            )
        self.assertEqual(historical["record_count"], 2)
        self.assertEqual(
            {row["decision"] for row in historical["decisions"]}, {"KEEP"}
        )

    def test_active_resolver_requires_post_screening_passed_checkpoint(self) -> None:
        fixture = self._fixture()
        state = core.load_json(fixture["state_path"])
        state["machine_checkpoints"]["screening"] = "pending"
        state["checkpoint_provenance"]["screening"] = None
        with self.assertRaises(ValueError):
            screening.resolve_active_screening_acceptance(
                fixture["root"], self._alternate_state(fixture, state, "pending-state"), self.implementation
            )

        state = core.load_json(fixture["state_path"])
        state["checkpoint_provenance"]["screening"] = None
        with self.assertRaisesRegex(ValueError, "passed checkpoint lacks Stage Checkpoint provenance"):
            screening.resolve_active_screening_acceptance(
                fixture["root"], self._alternate_state(fixture, state, "missing-provenance-state"), self.implementation
            )

    def test_missing_checkpoint_artifact_row_fails_closed(self) -> None:
        fixture = self._fixture()
        state = core.load_json(fixture["state_path"])
        checkpoint = core.load_json(fixture["checkpoint"])
        checkpoint["artifacts"] = [
            {
                "name": "unrelated-artifact",
                "path": "sources/SP-ACTIVE/unrelated.json",
                "sha256": "0" * 64,
            }
        ]
        unrelated = fixture["root"] / "sources/SP-ACTIVE/unrelated.json"
        core.write_json(unrelated, {"fixture": "unrelated"})
        checkpoint["artifacts"][0]["sha256"] = core.sha256_file(unrelated)
        report_path = fixture["root"] / "sources/SP-ACTIVE/reviews/screening-core.json"
        report = core.load_json(report_path)
        report["artifacts"] = copy.deepcopy(checkpoint["artifacts"])
        core.write_json(report_path, report)
        checkpoint["reviews"][0]["result"]["sha256"] = core.sha256_file(report_path)
        checkpoint_path = fixture["root"] / "sources/SP-ACTIVE/orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json"
        core.write_json(checkpoint_path, checkpoint)
        state["checkpoint_provenance"]["screening"] = {
            "path": str(checkpoint_path.relative_to(fixture["root"])),
            "sha256": core.sha256_file(checkpoint_path),
        }
        with self.assertRaises(ValueError):
            screening.resolve_active_screening_acceptance(
                fixture["root"], self._alternate_state(fixture, state, "zero-artifact-state"), self.implementation
            )

    def test_duplicate_checkpoint_artifact_rows_fail_closed(self) -> None:
        fixture = self._fixture()
        state = core.load_json(fixture["state_path"])
        checkpoint = core.load_json(fixture["checkpoint"])
        checkpoint["artifacts"].append(copy.deepcopy(checkpoint["artifacts"][0]))
        report_path = fixture["root"] / "sources/SP-ACTIVE/reviews/screening-core.json"
        report = core.load_json(report_path)
        report["artifacts"] = copy.deepcopy(checkpoint["artifacts"])
        core.write_json(report_path, report)
        checkpoint["reviews"][0]["result"]["sha256"] = core.sha256_file(report_path)
        checkpoint_path = fixture["root"] / "sources/SP-ACTIVE/orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json"
        core.write_json(checkpoint_path, checkpoint)
        state["checkpoint_provenance"]["screening"] = {
            "path": str(checkpoint_path.relative_to(fixture["root"])),
            "sha256": core.sha256_file(checkpoint_path),
        }
        with self.assertRaises(ValueError):
            screening.resolve_active_screening_acceptance(
                fixture["root"], self._alternate_state(fixture, state, "duplicate-artifact-state"), self.implementation
            )

    def test_checkpoint_artifact_hash_drift_fails_closed(self) -> None:
        fixture = self._fixture()
        accepted_path = fixture["accepted"]["corrected"]
        original = accepted_path.read_bytes()
        accepted_path.write_bytes(original + b"\n")
        self.addCleanup(lambda: accepted_path.write_bytes(original))
        with self.assertRaisesRegex(ValueError, "Stage Checkpoint artifact drift"):
            screening.resolve_active_screening_acceptance(
                fixture["root"], fixture["state_path"], self.implementation
            )

    def test_checkpoint_authority_hash_drift_fails_closed(self) -> None:
        fixture = self._fixture()
        state = core.load_json(fixture["state_path"])
        state["checkpoint_provenance"]["screening"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "provenance SHA drift"):
            screening.resolve_active_screening_acceptance(
                fixture["root"], self._alternate_state(fixture, state, "drifted-checkpoint-state"), self.implementation
            )

    def test_active_api_rejects_pre_screening_state(self) -> None:
        fixture = self._fixture()
        state = core.load_json(fixture["state_path"])
        state["lifecycle_state"] = "DISCOVERY_COLLECTED"
        state["next_action"] = "stage:screening"
        state["terminal_reason"] = None
        with self.assertRaisesRegex(ValueError, "post-Screening Production State"):
            screening.resolve_active_screening_acceptance(
                fixture["root"], self._alternate_state(fixture, state, "pre-screening-state"), self.implementation
            )

    def test_required_downstream_runners_do_not_scan_screening_acceptance_directories(self) -> None:
        evidence_source = (self.repo_root / "scripts/run_evidence_v2_interactive.py").read_text(encoding="utf-8")
        selection_source = (self.repo_root / "scripts/run_selection_architecture_v2_interactive.py").read_text(encoding="utf-8")
        self.assertNotIn('screening/v2/accepted").glob', evidence_source)
        self.assertNotIn('screening/v2/accepted").glob', selection_source)
        self.assertIn("resolve_active_screening_acceptance", evidence_source)
        self.assertIn("resolve_active_screening_acceptance", selection_source)


if __name__ == "__main__":
    unittest.main()
