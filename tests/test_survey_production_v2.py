from __future__ import annotations

import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts import survey_production_v2 as v2


IMPLEMENTATION_SHA = "1" * 40
OTHER_IMPLEMENTATION_SHA = "2" * 40


class SurveyProductionV2FoundationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_root = Path(".").resolve()
        self.cfg = v2.load_json(self.repo_root / "config/survey-production-v2.json")

    def make_sandbox(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        source_cfg = v2.load_json(self.repo_root / "config/survey-production-v2.json")
        required = [
            "config/survey-production-v2.json",
            "config/weekly-pipeline.json",
            "schemas/survey-production-profile.schema.json",
            "schemas/survey-production-state.schema.json",
            *source_cfg["contract_files"]["pipeline"],
            *source_cfg["contract_files"]["quality"],
        ]
        for rel in dict.fromkeys(required):
            src = self.repo_root / rel
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        return temp, root

    @staticmethod
    def thematic_spec(**overrides: object) -> dict:
        spec = {
            "issue_id": "SP001",
            "question": "test thematic question",
            "temporal_mode": "OPEN_HISTORY_AS_OF",
            "as_of": "2026-08-22T02:00:00+09:00",
            "scope_dimensions": ["lineage", "competition"],
        }
        spec.update(overrides)
        return spec

    @staticmethod
    def write_checkpoint_attestation(root: Path, cfg: dict, state_path: Path, checkpoint: str) -> dict[str, str]:
        state = v2.load_json(state_path)
        profile_path = root / state["profile"]["path"]
        profile = v2.load_json(profile_path)
        source_root = root / profile["paths"]["source_root"]
        artifact = source_root / "generated" / f"{checkpoint}.json"
        v2.write_json(artifact, {"checkpoint": checkpoint, "issue_id": state["issue_id"]})
        attestation = source_root / cfg["state_authority"]["checkpoint_attestation_dir"] / f"{checkpoint}.json"
        v2.write_json(
            attestation,
            {
                "schema_version": "2.0-rc1",
                "issue_id": state["issue_id"],
                "checkpoint": checkpoint,
                "action_id": f"action:test:{checkpoint}",
                "action_spec_sha256": "a" * 64,
                "validator": f"validate:{checkpoint}",
                "validator_version": "2.0-rc1",
                "validated_at": "2026-08-21T17:09:00Z",
                "required_inputs": [
                    {
                        "name": "production-profile",
                        "path": str(profile_path.relative_to(root)),
                        "sha256": v2.sha256_file(profile_path),
                        "required": True,
                    }
                ],
                "outputs": [
                    {
                        "name": checkpoint,
                        "path": str(artifact.relative_to(root)),
                        "sha256": v2.sha256_file(artifact),
                        "required": True,
                    }
                ],
                "status": "PASSED",
            },
        )
        return {"path": str(attestation.relative_to(root)), "sha256": v2.sha256_file(attestation)}

    def test_contract_manifest_declares_two_human_gates_and_non_authoritative_legacy_state(self) -> None:
        self.assertEqual(self.cfg["human_gates"], ["ARCHITECTURE_REVIEW", "PUBLICATION_PREVIEW"])
        self.assertEqual(self.cfg["state_authority"]["authoritative_filename"], "production-state.json")
        self.assertEqual(self.cfg["state_authority"]["legacy_mode"], "NON_AUTHORITATIVE_READ_ONLY")
        self.assertFalse("CANDIDATE_SELECTION" in self.cfg["human_gates"])

    def test_weekly_profile_uses_existing_cutoff_logic_and_resolves_w33_before_cutoff(self) -> None:
        now = v2.parse_instant("2026-08-22T02:00:00+09:00")
        profile = v2.weekly_profile(self.repo_root, self.cfg, now, "2026-W33")
        policy = profile["research_scope"]["temporal_policy"]
        self.assertEqual(profile["research_profile"], "WEEKLY")
        self.assertEqual(profile["publication_profile"], "WEEKLY_MAGAZINE")
        self.assertEqual(policy["mode"], "ROLLING_WINDOW")
        self.assertEqual(policy["timezone"], "America/New_York")
        self.assertTrue(policy["window_start"].endswith("-04:00"))
        self.assertTrue(policy["window_end"].endswith("-04:00"))
        self.assertEqual(policy["window_end"], policy["cutoff"])
        self.assertEqual(len(profile["research_scope"]["initial_obligations"]), 3)

    def test_weekly_profile_can_initialize_w33_after_w34_cutoff_without_legacy_state(self) -> None:
        temp, root = self.make_sandbox()
        self.addCleanup(temp.cleanup)
        cfg = v2.load_json(root / "config/survey-production-v2.json")
        legacy = root / "sources/2026-W33/pipeline-state.json"
        self.assertFalse(legacy.exists())
        now = v2.parse_instant("2026-08-22T11:18:00+09:00")
        profile = v2.weekly_profile(root, cfg, now, "2026-W33")
        policy = profile["research_scope"]["temporal_policy"]
        self.assertEqual(profile["issue_id"], "2026-W33")
        self.assertEqual(policy["cutoff"], "2026-08-14T18:00:00-04:00")
        self.assertEqual(policy["window_start"], "2026-08-07T18:00:00-04:00")

    def test_weekly_profile_refuses_future_issue_before_cutoff(self) -> None:
        now = v2.parse_instant("2026-08-22T02:00:00+09:00")
        with self.assertRaisesRegex(ValueError, "has not completed its editorial cutoff"):
            v2.weekly_profile(self.repo_root, self.cfg, now, "2026-W34")
        after_w34 = v2.parse_instant("2026-08-22T11:18:00+09:00")
        with self.assertRaisesRegex(ValueError, "has not completed its editorial cutoff"):
            v2.weekly_profile(self.repo_root, self.cfg, after_w34, "2026-W35")

    def test_thematic_profile_has_no_fake_bounded_window_and_has_initial_obligations(self) -> None:
        spec = self.thematic_spec(
            question="How did Chinese generative AI ecosystems emerge and differentiate?",
            inclusion=["major model and developer ecosystems"],
            exclusion=["policy-only material without technical relevance"],
            scope_dimensions=["lineage", "distribution", "reasoning", "coding"],
            initial_obligations=[
                {"obligation_id": "initial:lineage", "dimension": "lineage", "description": "trace the core lineage"},
                {"obligation_id": "initial:distribution", "dimension": "distribution", "description": "cover distribution strategy"},
                {"obligation_id": "initial:reasoning", "dimension": "reasoning", "description": "cover reasoning systems"},
                {"obligation_id": "initial:coding", "dimension": "coding", "description": "cover coding systems"},
            ],
        )
        profile = v2.thematic_profile(self.repo_root, self.cfg, spec)
        policy = profile["research_scope"]["temporal_policy"]
        self.assertEqual(profile["research_profile"], "THEMATIC")
        self.assertEqual(policy["mode"], "OPEN_HISTORY_AS_OF")
        self.assertEqual(set(policy), {"mode", "as_of"})
        self.assertNotIn("start", policy)
        self.assertNotIn("end", policy)
        self.assertNotIn("window_start", policy)
        self.assertNotIn("window_end", policy)
        self.assertEqual(profile["research_scope"]["initial_obligations"][0]["obligation_id"], "initial:lineage")

    def test_thematic_profile_rejects_bounded_period_mode_and_empty_scope(self) -> None:
        with self.assertRaisesRegex(ValueError, "OPEN_HISTORY_AS_OF or CURRENT_STATE_AS_OF"):
            v2.thematic_profile(self.repo_root, self.cfg, self.thematic_spec(temporal_mode="BOUNDED_PERIOD"))
        with self.assertRaisesRegex(ValueError, "scope_dimensions"):
            v2.thematic_profile(self.repo_root, self.cfg, self.thematic_spec(scope_dimensions=[]))

    def test_thematic_profile_rejects_uncovered_initial_obligation_and_path_escape(self) -> None:
        bad = self.thematic_spec(
            initial_obligations=[{"obligation_id": "bad", "dimension": "not-declared", "description": "invalid dimension"}]
        )
        with self.assertRaisesRegex(ValueError, "declared scope dimension"):
            v2.thematic_profile(self.repo_root, self.cfg, bad)
        escaped = self.thematic_spec(source_root="../outside")
        with self.assertRaisesRegex(ValueError, "repository-relative path"):
            v2.thematic_profile(self.repo_root, self.cfg, escaped)

    def test_initialize_is_non_destructive_and_records_separate_identities(self) -> None:
        temp, root = self.make_sandbox()
        self.addCleanup(temp.cleanup)
        cfg = v2.load_json(root / "config/survey-production-v2.json")
        profile = v2.thematic_profile(root, cfg, self.thematic_spec(temporal_mode="CURRENT_STATE_AS_OF"))
        profile_path, state_path = v2.initialize(
            root, cfg, profile, IMPLEMENTATION_SHA, "ARCHITECTURE_REVIEW",
            v2.parse_instant("2026-08-22T02:05:00+09:00"),
        )
        state = v2.load_json(state_path)
        self.assertEqual(state["profile"]["sha256"], v2.sha256_file(profile_path))
        self.assertEqual(state["implementation"]["repository_commit_sha"], IMPLEMENTATION_SHA)
        self.assertEqual(state["contract"], profile["contract"])
        self.assertEqual(state["next_action"], "stage:discovery")
        self.assertIsNone(state["terminal_reason"])
        self.assertTrue(all(value is None for value in state["checkpoint_provenance"].values()))
        self.assertTrue(all(value is None for value in state["human_gate_provenance"].values()))
        self.assertEqual(v2.validate_state_semantics(root, cfg, state), [])
        with self.assertRaisesRegex(ValueError, "refusing destructive"):
            v2.initialize(
                root, cfg, profile, IMPLEMENTATION_SHA, "ARCHITECTURE_REVIEW",
                v2.parse_instant("2026-08-22T02:06:00+09:00"),
            )

    def test_transition_requires_exact_checkpoint_attestation_and_is_one_step(self) -> None:
        temp, root = self.make_sandbox()
        self.addCleanup(temp.cleanup)
        cfg = v2.load_json(root / "config/survey-production-v2.json")
        profile = v2.thematic_profile(root, cfg, self.thematic_spec())
        _, state_path = v2.initialize(
            root, cfg, profile, IMPLEMENTATION_SHA, "ARCHITECTURE_REVIEW",
            v2.parse_instant("2026-08-22T02:05:00+09:00"),
        )
        state = v2.load_json(state_path)
        with self.assertRaisesRegex(ValueError, "requires exact passed checkpoint updates"):
            v2.transition_state(
                root, cfg, state, "DISCOVERY_COLLECTED", IMPLEMENTATION_SHA,
                v2.parse_instant("2026-08-22T02:10:00+09:00"),
            )
        with self.assertRaisesRegex(ValueError, "requires exact checkpoint provenance updates"):
            v2.transition_state(
                root, cfg, state, "DISCOVERY_COLLECTED", IMPLEMENTATION_SHA,
                v2.parse_instant("2026-08-22T02:10:00+09:00"), {"discovery": "passed"},
            )
        authority = self.write_checkpoint_attestation(root, cfg, state_path, "discovery")
        advanced = v2.transition_state(
            root, cfg, state, "DISCOVERY_COLLECTED", IMPLEMENTATION_SHA,
            v2.parse_instant("2026-08-22T02:10:00+09:00"),
            {"discovery": "passed"}, {"discovery": authority},
        )
        self.assertEqual(advanced["lifecycle_state"], "DISCOVERY_COLLECTED")
        self.assertEqual(advanced["machine_checkpoints"]["discovery"], "passed")
        self.assertEqual(advanced["checkpoint_provenance"]["discovery"], authority)
        with self.assertRaisesRegex(ValueError, "exactly one forward step"):
            v2.transition_state(
                root, cfg, state, "EVIDENCE_REVIEWED", IMPLEMENTATION_SHA,
                v2.parse_instant("2026-08-22T02:11:00+09:00"), {}, {},
            )
        with self.assertRaisesRegex(ValueError, "implementation commit differs"):
            v2.transition_state(
                root, cfg, state, "DISCOVERY_COLLECTED", OTHER_IMPLEMENTATION_SHA,
                v2.parse_instant("2026-08-22T02:12:00+09:00"),
                {"discovery": "passed"}, {"discovery": authority},
            )

    def test_state_semantic_validation_rejects_forged_or_rewritten_authority(self) -> None:
        temp, root = self.make_sandbox()
        self.addCleanup(temp.cleanup)
        cfg = v2.load_json(root / "config/survey-production-v2.json")
        profile = v2.thematic_profile(root, cfg, self.thematic_spec())
        _, state_path = v2.initialize(
            root, cfg, profile, IMPLEMENTATION_SHA, "ARCHITECTURE_REVIEW",
            v2.parse_instant("2026-08-22T02:05:00+09:00"),
        )
        state = v2.load_json(state_path)

        forged = copy.deepcopy(state)
        forged["lifecycle_state"] = "DISCOVERY_COLLECTED"
        errors = v2.validate_state_semantics(root, cfg, forged)
        self.assertTrue(any("checkpoint discovery" in error or "history length" in error for error in errors), errors)

        forged = copy.deepcopy(state)
        forged["machine_checkpoints"]["architecture"] = "passed"
        errors = v2.validate_state_semantics(root, cfg, forged)
        self.assertTrue(any("checkpoint architecture" in error for error in errors), errors)

        forged = copy.deepcopy(state)
        forged["next_action"] = "ARCHITECTURE_REVIEW"
        errors = v2.validate_state_semantics(root, cfg, forged)
        self.assertTrue(any("next_action drift" in error for error in errors), errors)

        forged = copy.deepcopy(state)
        forged["history"][0]["to"] = "DISCOVERY_COLLECTED"
        errors = v2.validate_state_semantics(root, cfg, forged)
        self.assertTrue(any("history[0]" in error for error in errors), errors)

        authority = self.write_checkpoint_attestation(root, cfg, state_path, "discovery")
        advanced = v2.transition_state(
            root, cfg, state, "DISCOVERY_COLLECTED", IMPLEMENTATION_SHA,
            v2.parse_instant("2026-08-22T02:10:00+09:00"),
            {"discovery": "passed"}, {"discovery": authority},
        )
        attestation_path = root / authority["path"]
        tampered = v2.load_json(attestation_path)
        tampered["validator"] = "validate:forged"
        v2.write_json(attestation_path, tampered)
        errors = v2.validate_state_semantics(root, cfg, advanced)
        self.assertTrue(any("authority SHA drift" in error for error in errors), errors)

    def test_transition_rejects_profile_contract_and_legacy_drift(self) -> None:
        temp, root = self.make_sandbox()
        self.addCleanup(temp.cleanup)
        cfg = v2.load_json(root / "config/survey-production-v2.json")
        source_root = root / "sources/SP001"
        source_root.mkdir(parents=True, exist_ok=True)
        legacy_path = source_root / "pipeline-state.json"
        legacy_path.write_text('{"legacy": 1}\n', encoding="utf-8")
        profile = v2.thematic_profile(root, cfg, self.thematic_spec())
        profile_path, state_path = v2.initialize(
            root, cfg, profile, IMPLEMENTATION_SHA, "ARCHITECTURE_REVIEW",
            v2.parse_instant("2026-08-22T02:05:00+09:00"),
        )
        state = v2.load_json(state_path)
        self.assertTrue(state["legacy_compatibility"]["legacy_state_present"])

        legacy_path.write_text('{"legacy": 2}\n', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "legacy compatibility artifact changed"):
            v2.transition_state(
                root, cfg, state, "DISCOVERY_COLLECTED", IMPLEMENTATION_SHA,
                v2.parse_instant("2026-08-22T02:10:00+09:00"),
                {"discovery": "passed"}, {},
            )

        legacy_path.write_text('{"legacy": 1}\n', encoding="utf-8")
        changed_profile = json.loads(profile_path.read_text(encoding="utf-8"))
        changed_profile["research_scope"]["question"] = "changed after initialization"
        profile_path.write_text(json.dumps(changed_profile, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "profile bytes changed"):
            v2.transition_state(
                root, cfg, state, "DISCOVERY_COLLECTED", IMPLEMENTATION_SHA,
                v2.parse_instant("2026-08-22T02:11:00+09:00"),
                {"discovery": "passed"}, {},
            )

    def test_transition_rejects_contract_file_drift(self) -> None:
        temp, root = self.make_sandbox()
        self.addCleanup(temp.cleanup)
        cfg = v2.load_json(root / "config/survey-production-v2.json")
        profile = v2.thematic_profile(root, cfg, self.thematic_spec(temporal_mode="CURRENT_STATE_AS_OF"))
        _, state_path = v2.initialize(
            root, cfg, profile, IMPLEMENTATION_SHA, "ARCHITECTURE_REVIEW",
            v2.parse_instant("2026-08-22T02:05:00+09:00"),
        )
        state = v2.load_json(state_path)
        contract_path = root / "docs/survey-production-core-v2-authority.md"
        contract_path.write_text(contract_path.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "semantic contract files differ"):
            v2.transition_state(
                root, cfg, state, "DISCOVERY_COLLECTED", IMPLEMENTATION_SHA,
                v2.parse_instant("2026-08-22T02:10:00+09:00"),
                {"discovery": "passed"}, {},
            )


if __name__ == "__main__":
    unittest.main()
