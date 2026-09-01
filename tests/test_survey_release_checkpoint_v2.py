from __future__ import annotations

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
        publication = source / "publication/v2"
        publication.mkdir(parents=True)
        verification = publication / "merge-verification-v2.json"
        release = publication / "release-record-v2.json"
        core.write_json(verification, {"fixture": "merge-verification"})
        core.write_json(release, {"fixture": "release-record"})
        state_path = source / "production-state.json"
        state = {
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "research_profile": "THEMATIC",
            "publication_profile": "LONGFORM_SPECIAL",
            "lifecycle_state": "FROZEN",
        }
        core.write_json(state_path, state)
        profile = {
            "paths": {
                "source_root": rel,
                "survey_root": f"{rel}/survey",
                "work_branch": "test/release-checkpoint",
            }
        }
        return source, profile, state_path, verification, release

    def test_release_boundary_uses_one_compact_checkpoint_with_current_tool_identity(self) -> None:
        source, profile, state_path, verification, release = self.fixture()
        release_payload = {
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "merge_verification_path": str(verification.relative_to(self.root)),
            "merge_verification_sha256": core.sha256_file(verification),
        }
        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(source / "production-profile.json", profile, source)),
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
        self.assertEqual(record["reviews"][0]["kind"], "DETERMINISTIC")
        self.assertEqual(record["reviews"][0]["result"]["sha256"], core.sha256_file(release))

    def test_release_checkpoint_rejects_release_record_bound_to_other_merge_verification(self) -> None:
        source, profile, state_path, verification, release = self.fixture()
        other = source / "publication/v2/other-merge-verification.json"
        core.write_json(other, {"fixture": "other"})
        release_payload = {
            "issue_id": "SP-RELEASE-CHECKPOINT",
            "merge_verification_path": str(other.relative_to(self.root)),
            "merge_verification_sha256": core.sha256_file(other),
        }
        with (
            mock.patch.object(agent, "verify_agent_state_basis"),
            mock.patch.object(agent, "_profile_and_source", return_value=(source / "production-profile.json", profile, source)),
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


if __name__ == "__main__":
    unittest.main()
