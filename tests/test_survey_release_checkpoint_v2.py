from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts import survey_agent_control_v2 as agent
from scripts import survey_production_v2 as core
from scripts import survey_release_checkpoint_v2 as release_checkpoint


class SurveyReleaseCheckpointV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(".").resolve()
        self.cfg = core.load_json(self.root / core.DEFAULT_CONFIG)

    def fixture(self):
        temp = tempfile.TemporaryDirectory(dir=self.root)
        self.addCleanup(temp.cleanup)
        source = Path(temp.name)
        rel = str(source.relative_to(self.root))
        profile_path = source / "production-profile.json"
        profile = {
            "schema_version": "2.0-rc1",
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "research_profile": "THEMATIC",
            "publication_profile": "LONGFORM_SPECIAL",
            "thematic_id": "SP-RELEASE-CHECKPOINT",
            "thematic_title": "Release Checkpoint Test",
            "paths": {
                "source_root": rel,
                "survey_root": f"{rel}/survey",
                "work_branch": "test/release-checkpoint",
            },
        }
        core.write_json(profile_path, profile)

        publication = source / "publication/v2"
        publication.mkdir(parents=True)
        verification = publication / "merge-verification-v2.json"
        release = publication / "release-record-v2.json"
        core.write_json(verification, {"fixture": "merge-verification"})
        core.write_json(release, {"fixture": "release-record"})
        state_path = source / "production-state.json"
        state = {
            "schema_version": "2.0-rc1",
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "research_profile": "THEMATIC",
            "publication_profile": "LONGFORM_SPECIAL",
            "lifecycle_state": "FROZEN",
            "profile": {"path": str(profile_path.relative_to(self.root)), "sha256": core.sha256_file(profile_path)},
            "contract": core.contract_identity(self.root, self.cfg, "THEMATIC", "LONGFORM_SPECIAL"),
            "implementation": {
                "repository_commit_sha": core.repository_commit_sha(self.root),
                "orchestrator_version": self.cfg["orchestrator_version"],
            },
            "history": [],
            "human_gates": {"architecture_review": "approved", "publication_preview": "approved"},
            "human_gate_provenance": {},
            "target_gate": "ARCHITECTURE_REVIEW",
            "next_action": "stage:release",
            "terminal_reason": None,
            "exception_gate": {"status": "inactive", "reason": None},
            "machine_checkpoints": {},
            "checkpoint_provenance": {},
            "legacy_compatibility": {
                "mode": "NON_AUTHORITATIVE_READ_ONLY",
                "legacy_state_present": False,
                "legacy_state_path": f"{rel}/pipeline-state.json",
                "legacy_state_sha256": None,
            },
            "publication_revalidation_provenance": None,
        }
        core.write_json(state_path, state)
        return source, profile, state_path, verification, release

    def test_release_boundary_uses_one_compact_checkpoint_with_current_tool_identity(self) -> None:
        source, profile, state_path, verification, release = self.fixture()
        profile_path = source / "production-profile.json"
        release_payload = {
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "merge_verification_path": str(verification.relative_to(self.root)),
            "merge_verification_sha256": core.sha256_file(verification),
        }
        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(profile_path, profile, source)),
            mock.patch("scripts.survey_release_checkpoint_v2.publication.validate_release_record", return_value=release_payload),
        ):
            checkpoint = release_checkpoint.build_release_checkpoint(
                self.root,
                self.cfg,
                state_path,
                verification,
                release,
                core.parse_instant("2026-08-22T10:30:00Z"),
            )
        record = core.load_json(checkpoint)
        self.assertEqual(checkpoint, source / "orchestration/v2/checkpoints/FROZEN.json")
        self.assertEqual(record["from_state"], "FROZEN")
        self.assertEqual(record["to_state"], "RELEASED")
        self.assertEqual(record["checkpoints"], ["release"])
        self.assertEqual(record["implementation"]["repository_commit_sha"], core.repository_commit_sha(self.root))
        self.assertEqual(record["implementation"]["orchestrator_version"], self.cfg["orchestrator_version"])
        self.assertEqual([row["name"] for row in record["artifacts"]], ["merge-verification", "release-record"])
        self.assertEqual(len(record["reviews"]), 2)
        # Review 0: CORE_STAGE_CONTRACT
        self.assertEqual(record["reviews"][0]["check_id"], "CORE_STAGE_CONTRACT")
        self.assertEqual(record["reviews"][0]["kind"], "DETERMINISTIC")
        self.assertEqual(record["reviews"][0]["status"], "PASS")
        core_stage_path = self.root / record["reviews"][0]["result"]["path"]
        self.assertTrue(core_stage_path.is_file())
        self.assertEqual(record["reviews"][0]["result"]["sha256"], core.sha256_file(core_stage_path))
        # Review 1: RELEASE_EXACT_BYTE_RECONCILIATION
        self.assertEqual(record["reviews"][1]["check_id"], "RELEASE_EXACT_BYTE_RECONCILIATION")
        self.assertEqual(record["reviews"][1]["kind"], "DETERMINISTIC")
        self.assertEqual(record["reviews"][1]["status"], "PASS")
        self.assertEqual(record["reviews"][1]["result"]["sha256"], core.sha256_file(release))

    def test_release_checkpoint_rejects_release_record_bound_to_other_merge_verification(self) -> None:
        source, profile, state_path, verification, release = self.fixture()
        profile_path = source / "production-profile.json"
        other = source / "publication/v2/other-merge-verification.json"
        core.write_json(other, {"fixture": "other"})
        release_payload = {
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "merge_verification_path": str(other.relative_to(self.root)),
            "merge_verification_sha256": core.sha256_file(other),
        }
        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(profile_path, profile, source)),
            mock.patch("scripts.survey_release_checkpoint_v2.publication.validate_release_record", return_value=release_payload),
        ):
            with self.assertRaisesRegex(ValueError, "does not bind supplied Merge Verification path"):
                release_checkpoint.build_release_checkpoint(
                    self.root,
                    self.cfg,
                    state_path,
                    verification,
                    release,
                    core.parse_instant("2026-08-22T10:30:00Z"),
                )

    def test_release_checkpoint_requires_frozen_state(self) -> None:
        source, profile, state_path, verification, release = self.fixture()
        state = core.load_json(state_path)
        state["lifecycle_state"] = "RELEASE_CANDIDATE"
        core.write_json(state_path, state)
        with mock.patch.object(agent, "verify_agent_state_basis"):
            with self.assertRaisesRegex(ValueError, "requires FROZEN"):
                release_checkpoint.build_release_checkpoint(
                    self.root,
                    self.cfg,
                    state_path,
                    verification,
                    release,
                    core.parse_instant("2026-08-22T10:30:00Z"),
                )

    def test_success_path_advances_to_released_and_terminal_complete(self) -> None:
        source, profile, state_path, verification, release = self.fixture()
        profile_path = source / "production-profile.json"
        release_payload = {
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "merge_verification_path": str(verification.relative_to(self.root)),
            "merge_verification_sha256": core.sha256_file(verification),
        }
        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(profile_path, profile, source)),
            mock.patch("scripts.survey_release_checkpoint_v2.publication.validate_release_record", return_value=release_payload),
            mock.patch("scripts.survey_agent_control_v2.publication.validate_release_record", return_value=release_payload),
            mock.patch.object(agent, "validate_agent_state", return_value=[]),
        ):
            when = core.parse_instant("2026-08-22T10:30:00Z")
            checkpoint = release_checkpoint.build_release_checkpoint(
                self.root, self.cfg, state_path, verification, release, when
            )
            updated = agent.advance_with_checkpoint(self.root, self.cfg, state_path, checkpoint)

        self.assertEqual(updated["lifecycle_state"], "RELEASED")
        self.assertEqual(updated["machine_checkpoints"]["release"], "passed")
        self.assertIsNone(updated["next_action"])
        self.assertEqual(updated["terminal_reason"], "COMPLETE")
        authority = updated["checkpoint_provenance"]["release"]
        self.assertEqual(authority["path"], str(checkpoint.relative_to(self.root)))
        self.assertEqual(authority["sha256"], core.sha256_file(checkpoint))
        # Ensure disk state was updated
        on_disk = core.load_json(state_path)
        self.assertEqual(on_disk["lifecycle_state"], "RELEASED")
        self.assertEqual(on_disk["terminal_reason"], "COMPLETE")

    def test_missing_core_authority_fails_before_state_mutation(self) -> None:
        source, profile, state_path, verification, release = self.fixture()
        profile_path = source / "production-profile.json"
        release_payload = {
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "merge_verification_path": str(verification.relative_to(self.root)),
            "merge_verification_sha256": core.sha256_file(verification),
        }
        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(profile_path, profile, source)),
            mock.patch("scripts.survey_release_checkpoint_v2.publication.validate_release_record", return_value=release_payload),
        ):
            checkpoint = release_checkpoint.build_release_checkpoint(
                self.root, self.cfg, state_path, verification, release, core.parse_instant("2026-08-22T10:30:00Z")
            )

        # Case 1: Removing CORE_STAGE_CONTRACT review fails schema/contract validation before state mutation
        tampered_ckpt = source / "orchestration/v2/checkpoints/TAMPERED.json"
        payload = core.load_json(checkpoint)
        payload["reviews"] = [r for r in payload["reviews"] if r["check_id"] != "CORE_STAGE_CONTRACT"]
        core.write_json(tampered_ckpt, payload)

        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(profile_path, profile, source)),
            mock.patch("scripts.survey_agent_control_v2.publication.validate_release_record", return_value=release_payload),
            mock.patch("scripts.survey_agent_control_v2.canonical_checkpoint_path", return_value=tampered_ckpt),
        ):
            with self.assertRaises(ValueError):
                agent.advance_with_checkpoint(self.root, self.cfg, state_path, tampered_ckpt)

        # Case 2: Deleting the CORE_STAGE_CONTRACT report file fails agent control before state mutation
        core_stage_path = source / "publication/v2/core-stage-contract-v2.json"
        core_stage_path.unlink()

        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(profile_path, profile, source)),
            mock.patch("scripts.survey_agent_control_v2.publication.validate_release_record", return_value=release_payload),
        ):
            with self.assertRaises(agent.AgentControlError):
                agent.advance_with_checkpoint(self.root, self.cfg, state_path, checkpoint)

        # State must remain FROZEN
        on_disk = core.load_json(state_path)
        self.assertEqual(on_disk["lifecycle_state"], "FROZEN")

    def test_drifted_core_authority_fails_before_state_mutation(self) -> None:
        source, profile, state_path, verification, release = self.fixture()
        profile_path = source / "production-profile.json"
        release_payload = {
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "merge_verification_path": str(verification.relative_to(self.root)),
            "merge_verification_sha256": core.sha256_file(verification),
        }
        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(profile_path, profile, source)),
            mock.patch("scripts.survey_release_checkpoint_v2.publication.validate_release_record", return_value=release_payload),
        ):
            checkpoint = release_checkpoint.build_release_checkpoint(
                self.root, self.cfg, state_path, verification, release, core.parse_instant("2026-08-22T10:30:00Z")
            )

        # Tamper the CORE_STAGE_CONTRACT report file so its sha drifts from the review ref
        core_stage_path = source / "publication/v2/core-stage-contract-v2.json"
        report = core.load_json(core_stage_path)
        report["contract"]["pipeline_contract_sha256"] = "f" * 64
        core.write_json(core_stage_path, report)

        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(profile_path, profile, source)),
            mock.patch("scripts.survey_agent_control_v2.publication.validate_release_record", return_value=release_payload),
        ):
            with self.assertRaisesRegex(agent.AgentControlError, "CORE_STAGE_CONTRACT result authority drift"):
                agent.advance_with_checkpoint(self.root, self.cfg, state_path, checkpoint)

        # State must remain FROZEN
        on_disk = core.load_json(state_path)
        self.assertEqual(on_disk["lifecycle_state"], "FROZEN")

    def test_release_authority_failure_fails_before_state_mutation(self) -> None:
        source, profile, state_path, verification, release = self.fixture()
        profile_path = source / "production-profile.json"
        release_payload = {
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "merge_verification_path": str(verification.relative_to(self.root)),
            "merge_verification_sha256": core.sha256_file(verification),
        }
        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(profile_path, profile, source)),
            mock.patch("scripts.survey_release_checkpoint_v2.publication.validate_release_record", return_value=release_payload),
        ):
            checkpoint = release_checkpoint.build_release_checkpoint(
                self.root, self.cfg, state_path, verification, release, core.parse_instant("2026-08-22T10:30:00Z")
            )

        # Tamper release record file so its sha drifts from the review reference
        core.write_json(release, {"fixture": "tampered-release-record"})

        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(profile_path, profile, source)),
            mock.patch("scripts.survey_agent_control_v2.publication.validate_release_record", return_value=release_payload),
        ):
            with self.assertRaisesRegex(agent.AgentControlError, "RELEASE_EXACT_BYTE_RECONCILIATION result authority drift"):
                agent.advance_with_checkpoint(self.root, self.cfg, state_path, checkpoint)

        # State must remain FROZEN
        on_disk = core.load_json(state_path)
        self.assertEqual(on_disk["lifecycle_state"], "FROZEN")

    def test_idempotent_reexecution(self) -> None:
        source, profile, state_path, verification, release = self.fixture()
        profile_path = source / "production-profile.json"
        release_payload = {
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "merge_verification_path": str(verification.relative_to(self.root)),
            "merge_verification_sha256": core.sha256_file(verification),
        }
        when = core.parse_instant("2026-08-22T10:30:00Z")
        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(profile_path, profile, source)),
            mock.patch("scripts.survey_release_checkpoint_v2.publication.validate_release_record", return_value=release_payload),
        ):
            ckpt1 = release_checkpoint.build_release_checkpoint(self.root, self.cfg, state_path, verification, release, when)
            ckpt2 = release_checkpoint.build_release_checkpoint(self.root, self.cfg, state_path, verification, release, when)
            self.assertEqual(ckpt1, ckpt2)

            # Divergent checkpoint payload rejection
            core.write_json(ckpt1, {"divergent": True})
            with self.assertRaisesRegex(ValueError, "refusing divergent Release Stage Checkpoint overwrite"):
                release_checkpoint.build_release_checkpoint(self.root, self.cfg, state_path, verification, release, when)

    def test_cli_main_success_and_error(self) -> None:
        source, profile, state_path, verification, release = self.fixture()
        profile_path = source / "production-profile.json"
        release_payload = {
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "merge_verification_path": str(verification.relative_to(self.root)),
            "merge_verification_sha256": core.sha256_file(verification),
        }
        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(profile_path, profile, source)),
            mock.patch("scripts.survey_release_checkpoint_v2.publication.validate_release_record", return_value=release_payload),
            mock.patch("scripts.survey_agent_control_v2.publication.validate_release_record", return_value=release_payload),
            mock.patch.object(agent, "validate_agent_state", return_value=[]),
            mock.patch("sys.argv", [
                "survey_release_checkpoint_v2.py",
                "--repo-root", str(self.root),
                "--state", str(state_path),
                "--merge-verification", str(verification),
                "--release-record", str(release),
                "--recorded-at", "2026-08-22T10:30:00Z",
            ]),
        ):
            ret = release_checkpoint.main()
            self.assertEqual(ret, 0)
            on_disk = core.load_json(state_path)
            self.assertEqual(on_disk["lifecycle_state"], "RELEASED")
            self.assertEqual(on_disk["terminal_reason"], "COMPLETE")

        # Calling on already-RELEASED state returns 2
        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch("sys.argv", [
                "survey_release_checkpoint_v2.py",
                "--repo-root", str(self.root),
                "--state", str(state_path),
                "--merge-verification", str(verification),
                "--release-record", str(release),
            ]),
        ):
            ret = release_checkpoint.main()
            self.assertEqual(ret, 2)


if __name__ == "__main__":
    unittest.main()
