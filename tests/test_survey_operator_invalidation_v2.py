from __future__ import annotations

import copy
import shutil
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock

from scripts import survey_human_gate_v2 as human_gate
from scripts import survey_production_v2 as core
from tests import test_survey_human_gate_v2 as human_fixture


class OperatorPendingGateInvalidationTests(unittest.TestCase):
    @staticmethod
    def _fixture(
        target_gate: str = "ARCHITECTURE_REVIEW",
    ) -> human_fixture.SurveyHumanGateV2Tests:
        human_fixture.SurveyHumanGateV2Tests.setUpClass()
        fixture = human_fixture.SurveyHumanGateV2Tests()
        fixture.setUp()
        operator_source = fixture.source_root / "operator-source"
        operator_survey = fixture.source_root / "operator-survey"
        profile = core.thematic_profile(
            fixture.root,
            fixture.cfg,
            {
                "issue_id": fixture.issue_id,
                "question": "Can a pending Architecture Gate be safely invalidated?",
                "temporal_mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-08-24T00:00:00Z",
                "scope_dimensions": ["operator invalidation"],
                "source_root": operator_source.relative_to(fixture.root).as_posix(),
                "survey_root": operator_survey.relative_to(fixture.root).as_posix(),
                "work_branch": fixture.branch,
            },
        )
        fixture.profile_path, fixture.state_path = core.initialize(
            fixture.root,
            fixture.cfg,
            profile,
            fixture.impl,
            target_gate,
            core.parse_instant("2026-08-24T00:00:00Z"),
        )
        fixture.source_root = operator_source
        fixture.source_rel = operator_source.relative_to(fixture.root).as_posix()
        fixture.survey_root = operator_survey
        fixture.survey_rel = operator_survey.relative_to(fixture.root).as_posix()
        return fixture

    def _pending_architecture_fixture(
        self,
        target_gate: str = "ARCHITECTURE_REVIEW",
    ) -> human_fixture.SurveyHumanGateV2Tests:
        fixture = self._fixture(target_gate)
        fixture._advance_to_selection()
        fixture._reach_architecture_gate("Architecture pending surface", "2026-08-24T00:05:00Z")
        self._make_architecture_summary_schema_valid(fixture)
        return fixture

    @staticmethod
    def _make_architecture_summary_schema_valid(fixture) -> None:
        architecture = fixture.source_root / "architecture-v2.json"
        summary = fixture.source_root / "architecture-review-summary-v2.json"
        core.write_json(
            summary,
            {
                "schema_version": "2.0-rc1",
                "issue_id": fixture.issue_id,
                "research_profile": "THEMATIC",
                "basis": {
                    "architecture_sha256": core.sha256_file(architecture),
                    "production_profile_sha256": core.sha256_file(fixture.profile_path),
                    "profile_completeness_sha256": "0" * 64,
                    "materiality_ledger_sha256": "0" * 64,
                    "candidate_matrix_sha256": "0" * 64,
                    "candidate_selection_sha256": "0" * 64,
                },
                "readiness": {"status": "READY_FOR_ARCHITECTURE_REVIEW", "errors": []},
                "discovery": {"total": 0, "counts": {}},
                "research_expansion": {
                    "max_research_pass": 0,
                    "pass_counts": {},
                    "parent_link_count": 0,
                    "obligation_link_count": 0,
                    "unique_obligation_count": 0,
                    "root_discovery_count": 0,
                    "expanded_discovery_count": 0,
                },
                "screening": {"total": 0, "counts": {}},
                "evidence": {"total": 0, "counts": {}},
                "materiality": {"total": 0, "counts": {}},
                "selection": {"total": 0, "counts": {}},
                "completeness": {"overall_status": "LIMITED", "obligation_counts": {}},
                "major_material_destinations": [],
                "residual_limitations": ["operator invalidation fixture"],
                "architecture": {
                    "status": "PROPOSED",
                    "editorial_thesis": "Architecture Gate operator invalidation fixture.",
                    "package_count": 1,
                    "packages": ["Round-trip package"],
                    "page_plan": {},
                },
            },
        )
        state = core.load_json(fixture.state_path)
        checkpoint_path = core.repo_local_path(
            fixture.root,
            state["checkpoint_provenance"]["architecture"]["path"],
            "architecture checkpoint",
        )
        checkpoint = core.load_json(checkpoint_path)
        for artifact in checkpoint["artifacts"]:
            if artifact["name"] == "architecture-review-summary":
                artifact["sha256"] = core.sha256_file(summary)
        for review in checkpoint["reviews"]:
            if review.get("check_id") != human_gate.agent.CORE_STAGE_REVIEW_ID:
                continue
            result_path = core.repo_local_path(
                fixture.root,
                review["result"]["path"],
                "architecture contract result",
            )
            report = core.load_json(result_path)
            for artifact in report["artifacts"]:
                if artifact["name"] == "architecture-review-summary":
                    artifact["sha256"] = core.sha256_file(summary)
            core.write_json(result_path, report)
            review["result"]["sha256"] = core.sha256_file(result_path)
        core.write_json(checkpoint_path, checkpoint)
        state["checkpoint_provenance"]["architecture"]["sha256"] = core.sha256_file(checkpoint_path)
        core.write_json(fixture.state_path, state)

    @staticmethod
    def _invalidate(fixture, *, expected_head=None, invalidated_commit=None, boundary="CANDIDATES_NORMALIZED"):
        return human_gate.invalidate_pending_gate(
            fixture.root,
            fixture.cfg,
            fixture.state_path,
            "ARCHITECTURE_REVIEW",
            boundary,
            "operator negative-test fixture",
            "operator-test",
            expected_head or fixture.impl,
            invalidated_commit_sha=invalidated_commit or fixture.impl,
        )

    def _successful_invalidation(self):
        fixture = self._pending_architecture_fixture()
        reviewed_commit = fixture._snapshot_review_commit()
        with mock.patch.object(core, "repository_commit_sha", return_value=reviewed_commit):
            result = self._invalidate(
                fixture,
                expected_head=reviewed_commit,
                invalidated_commit=reviewed_commit,
            )
        return fixture, reviewed_commit, result[1]

    def _write_existing_review_row(self, fixture) -> None:
        state = core.load_json(fixture.state_path)
        profile = core.load_json(fixture.profile_path)
        artifacts = human_gate._reviewed_artifacts(
            fixture.root, fixture.cfg, state, profile, "ARCHITECTURE_REVIEW"
        )
        record = human_gate._review_record_payload(
            issue_id=fixture.issue_id,
            gate="ARCHITECTURE_REVIEW",
            revision=1,
            decision="REQUEST_CHANGES",
            reviewed_state=human_gate._authority(fixture.root, fixture.state_path),
            reviewed_artifacts=artifacts,
            reviewed_repository_commit_sha=fixture.impl,
            reviewed_by="human-fixture",
            reviewed_at=datetime(2026, 8, 24, 0, 6, tzinfo=timezone.utc),
            review_reference="review:architecture:existing-row",
            requested_changes="Existing Human review row for fail-closed testing.",
            regeneration_boundary="SELECTION_COMPLETE",
            approval=None,
        )
        human_gate._write_review_record(
            fixture.root,
            fixture.cfg,
            fixture.source_root,
            {"schema_version": "2.0-rc1", "issue_id": fixture.issue_id, "reviews": []},
            record,
        )

    def test_operator_invalidation_requires_the_exact_pending_gate_state(self) -> None:
        fixture = self._fixture()
        self.addCleanup(fixture.doCleanups)

        with self.assertRaisesRegex(ValueError, "requires pending ARCHITECTURE_ESTABLISHED"):
            human_gate.invalidate_pending_gate(
                fixture.root,
                fixture.cfg,
                fixture.state_path,
                "ARCHITECTURE_REVIEW",
                "CANDIDATES_NORMALIZED",
                "fixture precondition test",
                "operator-test",
                fixture.impl,
                invalidated_commit_sha=fixture.impl,
            )

    def test_operator_invalidation_rejects_boundary_outside_configured_safe_set(self) -> None:
        fixture = self._fixture()
        self.addCleanup(fixture.doCleanups)
        fixture._advance_to_selection()
        fixture._reach_architecture_gate("Architecture pending surface", "2026-08-24T00:05:00Z")
        before = core.load_json(fixture.state_path)

        with self.assertRaisesRegex(ValueError, "not allowed for ARCHITECTURE_REVIEW"):
            human_gate.invalidate_pending_gate(
                fixture.root,
                fixture.cfg,
                fixture.state_path,
                "ARCHITECTURE_REVIEW",
                "DRAFT_COMPLETE",
                "fixture invalid boundary",
                "operator-test",
                fixture.impl,
                invalidated_commit_sha=fixture.impl,
            )

        self.assertEqual(core.load_json(fixture.state_path), before)
        self.assertEqual(
            core.load_json(fixture.source_root / fixture.cfg["state_authority"]["human_review_index_path"])
            if (fixture.source_root / fixture.cfg["state_authority"]["human_review_index_path"]).exists()
            else {"reviews": []},
            {"reviews": []},
        )

    def test_gate_not_pending_is_rejected(self) -> None:
        fixture = self._pending_architecture_fixture()
        self.addCleanup(fixture.doCleanups)
        reviewed = fixture._snapshot_review_commit()
        with mock.patch.object(core, "repository_commit_sha", return_value=reviewed):
            human_gate.record_architecture_approval(
                fixture.root,
                fixture.cfg,
                fixture.state_path,
                "human-reviewer",
                datetime(2026, 8, 24, 0, 6, tzinfo=timezone.utc),
                "review:architecture:operator-negative",
                expected_revision=1,
                reviewed_commit_sha=reviewed,
            )
            with self.assertRaisesRegex(ValueError, "not pending"):
                self._invalidate(fixture, expected_head=reviewed, invalidated_commit=reviewed)

    def test_lifecycle_mismatch_is_rejected(self) -> None:
        fixture = self._fixture()
        self.addCleanup(fixture.doCleanups)
        fixture._advance_to_selection()
        with self.assertRaisesRegex(ValueError, "requires pending ARCHITECTURE_ESTABLISHED"):
            self._invalidate(fixture)

    def test_requested_gate_must_match_configured_current_gate_not_eventual_target(self) -> None:
        fixture = self._pending_architecture_fixture("PUBLICATION_PREVIEW")
        self.addCleanup(fixture.doCleanups)
        with self.assertRaisesRegex(ValueError, "current Gate mismatch"):
            human_gate.invalidate_pending_gate(
                fixture.root,
                fixture.cfg,
                fixture.state_path,
                "PUBLICATION_PREVIEW",
                "CANDIDATES_NORMALIZED",
                "requested eventual gate must not override current Architecture Gate",
                "operator-test",
                fixture.impl,
                invalidated_commit_sha=fixture.impl,
            )

    def test_architecture_pending_invalidation_preserves_eventual_publication_target(self) -> None:
        fixture = self._pending_architecture_fixture("PUBLICATION_PREVIEW")
        self.addCleanup(fixture.doCleanups)
        prior_state = core.load_json(fixture.state_path)
        reviewed = fixture._snapshot_review_commit()
        with mock.patch.object(core, "repository_commit_sha", return_value=reviewed):
            state, record_path, _ = human_gate.invalidate_pending_gate(
                fixture.root,
                fixture.cfg,
                fixture.state_path,
                "ARCHITECTURE_REVIEW",
                "CANDIDATES_NORMALIZED",
                "regenerate before presenting the current Architecture Gate",
                "operator-test",
                reviewed,
                invalidated_commit_sha=reviewed,
            )

        self.assertEqual(state["lifecycle_state"], "CANDIDATES_NORMALIZED")
        self.assertEqual(state["target_gate"], "PUBLICATION_PREVIEW")
        self.assertEqual(state["human_gates"]["architecture_review"], "pending")
        self.assertIsNone(state["human_gate_provenance"]["architecture_review"])
        self.assertEqual(core.load_json(record_path)["gate"], "ARCHITECTURE_REVIEW")
        self.assertEqual(prior_state["target_gate"], "PUBLICATION_PREVIEW")
        validated = human_gate.validate_operator_invalidation_record(
            fixture.root, record_path, expected_issue_id=fixture.issue_id
        )
        self.assertEqual(validated["gate"], "ARCHITECTURE_REVIEW")
        review_index = fixture.source_root / fixture.cfg["state_authority"]["human_review_index_path"]
        self.assertEqual(
            core.load_json(review_index)["reviews"] if review_index.exists() else [],
            [],
        )

    def test_terminal_reason_mismatch_is_rejected(self) -> None:
        fixture = self._pending_architecture_fixture()
        self.addCleanup(fixture.doCleanups)
        state = core.load_json(fixture.state_path)
        state["terminal_reason"] = None
        core.write_json(fixture.state_path, state)
        with self.assertRaises(ValueError):
            self._invalidate(fixture)

    def test_stale_invalidated_commit_is_rejected(self) -> None:
        fixture = self._pending_architecture_fixture()
        self.addCleanup(fixture.doCleanups)
        before = fixture.state_path.read_bytes()
        with self.assertRaisesRegex(ValueError, "stale pending Gate surface"):
            self._invalidate(fixture, invalidated_commit="0" * 40)
        self.assertEqual(fixture.state_path.read_bytes(), before)

    def test_expected_work_branch_head_mismatch_is_rejected(self) -> None:
        fixture = self._pending_architecture_fixture()
        self.addCleanup(fixture.doCleanups)
        with self.assertRaisesRegex(ValueError, "stale pending Gate surface"):
            self._invalidate(fixture, expected_head="1" * 40)

    def test_current_state_bytes_must_match_invalidated_commit(self) -> None:
        fixture = self._pending_architecture_fixture()
        self.addCleanup(fixture.doCleanups)
        reviewed = fixture._snapshot_review_commit()
        original = fixture.state_path.read_bytes()
        fixture.state_path.write_bytes(original + b"\n")
        try:
            with mock.patch.object(core, "repository_commit_sha", return_value=reviewed):
                with self.assertRaisesRegex(ValueError, "reviewed repository commit bytes differ for Production State"):
                    self._invalidate(fixture, expected_head=reviewed, invalidated_commit=reviewed)
        finally:
            fixture.state_path.write_bytes(original)

    def test_gate_input_bytes_must_match_invalidated_commit(self) -> None:
        fixture = self._pending_architecture_fixture()
        self.addCleanup(fixture.doCleanups)
        reviewed = fixture._snapshot_review_commit()
        architecture = fixture.source_root / "architecture-v2.json"
        summary = fixture.source_root / "architecture-review-summary-v2.json"
        architecture.write_bytes(architecture.read_bytes() + b"\n")
        summary_payload = core.load_json(summary)
        summary_payload["basis"]["architecture_sha256"] = core.sha256_file(architecture)
        core.write_json(summary, summary_payload)
        with mock.patch.object(human_gate.agent, "verify_agent_state_basis", return_value=None):
            with mock.patch.object(core, "repository_commit_sha", return_value=reviewed):
                with self.assertRaisesRegex(ValueError, "reviewed repository commit bytes differ for Human Gate artifact issue-architecture"):
                    self._invalidate(fixture, expected_head=reviewed, invalidated_commit=reviewed)

    def test_missing_gate_input_is_rejected(self) -> None:
        fixture = self._pending_architecture_fixture()
        self.addCleanup(fixture.doCleanups)
        reviewed = fixture._snapshot_review_commit()
        (fixture.source_root / "architecture-v2.json").unlink()
        with mock.patch.object(human_gate.agent, "verify_agent_state_basis", return_value=None):
            with mock.patch.object(core, "repository_commit_sha", return_value=reviewed):
                with self.assertRaisesRegex(ValueError, "Human Gate input issue-architecture missing or unsafe"):
                    self._invalidate(fixture, expected_head=reviewed, invalidated_commit=reviewed)

    def test_gate_input_symlink_and_symlink_traversal_are_rejected(self) -> None:
        fixture = self._pending_architecture_fixture()
        self.addCleanup(fixture.doCleanups)
        reviewed = fixture._snapshot_review_commit()
        architecture = fixture.source_root / "architecture-v2.json"
        target = fixture.source_root / "architecture-target.json"
        target.write_bytes(architecture.read_bytes())
        architecture.unlink()
        architecture.symlink_to(target)
        with mock.patch.object(human_gate.agent, "verify_agent_state_basis", return_value=None):
            with mock.patch.object(core, "repository_commit_sha", return_value=reviewed):
                with self.assertRaisesRegex(ValueError, "symlink"):
                    self._invalidate(fixture, expected_head=reviewed, invalidated_commit=reviewed)

        architecture.unlink()
        architecture.write_bytes(target.read_bytes())
        linked_dir = fixture.source_root / "linked-gate-inputs"
        linked_dir.symlink_to(fixture.source_root, target_is_directory=True)
        fixture.cfg["orchestration"]["gate_inputs"]["ARCHITECTURE_REVIEW"][0]["path"] = (
            "{source_root}/linked-gate-inputs/architecture-v2.json"
        )
        with mock.patch.object(human_gate.agent, "verify_agent_state_basis", return_value=None):
            with mock.patch.object(core, "repository_commit_sha", return_value=reviewed):
                with self.assertRaisesRegex(ValueError, "symlink"):
                    self._invalidate(fixture, expected_head=reviewed, invalidated_commit=reviewed)

    def test_active_human_gate_provenance_is_rejected(self) -> None:
        fixture = self._pending_architecture_fixture()
        self.addCleanup(fixture.doCleanups)
        state = core.load_json(fixture.state_path)
        state["human_gate_provenance"]["architecture_review"] = {
            "path": "sources/fake-approval.json",
            "sha256": "0" * 64,
        }
        core.write_json(fixture.state_path, state)
        with self.assertRaises(ValueError):
            self._invalidate(fixture)

    def test_existing_human_review_index_row_is_rejected(self) -> None:
        fixture = self._pending_architecture_fixture()
        self.addCleanup(fixture.doCleanups)
        self._write_existing_review_row(fixture)
        with self.assertRaisesRegex(ValueError, "requires no Human review records"):
            self._invalidate(fixture)

    def test_publication_preview_cannot_cross_approved_architecture(self) -> None:
        fixture = self._pending_architecture_fixture("PUBLICATION_PREVIEW")
        self.addCleanup(fixture.doCleanups)
        reviewed = fixture._snapshot_review_commit()
        with mock.patch.object(core, "repository_commit_sha", return_value=reviewed):
            human_gate.record_architecture_approval(
                fixture.root,
                fixture.cfg,
                fixture.state_path,
                "human-reviewer",
                datetime(2026, 8, 24, 0, 6, tzinfo=timezone.utc),
                "review:architecture:publication-negative",
                expected_revision=1,
                reviewed_commit_sha=reviewed,
            )
        fixture._reach_publication_gate(1, 10)
        with self.assertRaisesRegex(ValueError, "cannot cross an active Human Architecture approval"):
            human_gate.invalidate_pending_gate(
                fixture.root,
                fixture.cfg,
                fixture.state_path,
                "PUBLICATION_PREVIEW",
                "SELECTION_COMPLETE",
                "operator must not cross approved Architecture",
                "operator-test",
                reviewed,
                invalidated_commit_sha=reviewed,
            )

    def test_partial_cleanup_failure_rolls_back_state_artifacts_and_record(self) -> None:
        fixture = self._pending_architecture_fixture()
        self.addCleanup(fixture.doCleanups)
        reviewed = fixture._snapshot_review_commit()
        state_before = fixture.state_path.read_bytes()
        cleanup_paths, _ = human_gate._superseded_paths_for_regeneration(
            fixture.root,
            fixture.cfg,
            core.load_json(fixture.state_path),
            core.load_json(fixture.profile_path),
            fixture.source_root,
            "CANDIDATES_NORMALIZED",
            "ARCHITECTURE_REVIEW",
        )
        snapshots = {path: path.read_bytes() for path in cleanup_paths if path.exists()}
        self.assertGreaterEqual(len(snapshots), 2)
        original_unlink = Path.unlink
        calls = {"count": 0}

        def fail_on_second_cleanup(path, *args, **kwargs):
            if path in snapshots:
                calls["count"] += 1
                if calls["count"] == 2:
                    raise OSError("injected partial cleanup failure")
            return original_unlink(path, *args, **kwargs)

        with mock.patch.object(core, "repository_commit_sha", return_value=reviewed):
            with mock.patch.object(Path, "unlink", side_effect=fail_on_second_cleanup):
                with self.assertRaisesRegex(ValueError, "rolled back"):
                    self._invalidate(fixture, expected_head=reviewed, invalidated_commit=reviewed)

        self.assertEqual(fixture.state_path.read_bytes(), state_before)
        for path, raw in snapshots.items():
            self.assertTrue(path.is_file(), path)
            self.assertEqual(path.read_bytes(), raw)
        record_dir = human_gate._operator_record_dir(fixture.source_root, fixture.cfg)
        self.assertFalse(record_dir.exists())

    def test_operator_record_prior_state_drift_is_rejected(self) -> None:
        fixture, _, record_path = self._successful_invalidation()
        self.addCleanup(fixture.doCleanups)
        payload = core.load_json(record_path)
        payload["prior_state"]["sha256"] = "0" * 64
        core.write_json(record_path, payload)
        with self.assertRaisesRegex(ValueError, "prior State SHA does not match"):
            human_gate.validate_operator_invalidation_record(
                fixture.root, record_path, expected_issue_id=fixture.issue_id
            )

    def test_operator_record_prior_gate_input_drift_is_rejected(self) -> None:
        fixture, _, record_path = self._successful_invalidation()
        self.addCleanup(fixture.doCleanups)
        payload = core.load_json(record_path)
        payload["prior_gate_inputs"][0]["sha256"] = "0" * 64
        core.write_json(record_path, payload)
        with self.assertRaisesRegex(ValueError, "Gate input issue-architecture SHA does not match"):
            human_gate.validate_operator_invalidation_record(
                fixture.root, record_path, expected_issue_id=fixture.issue_id
            )

    def test_operator_record_checkpoint_authority_drift_is_rejected(self) -> None:
        fixture, _, record_path = self._successful_invalidation()
        self.addCleanup(fixture.doCleanups)
        payload = core.load_json(record_path)
        self.assertTrue(payload["invalidated_checkpoint_authority"])
        payload["invalidated_checkpoint_authority"][0]["sha256"] = "0" * 64
        core.write_json(record_path, payload)
        with self.assertRaisesRegex(ValueError, "checkpoint .* SHA does not match"):
            human_gate.validate_operator_invalidation_record(
                fixture.root, record_path, expected_issue_id=fixture.issue_id
            )

    def test_operator_record_canonical_authority_drift_is_rejected(self) -> None:
        fixture, _, record_path = self._successful_invalidation()
        self.addCleanup(fixture.doCleanups)
        payload = core.load_json(record_path)
        self.assertTrue(payload["superseded_canonical_paths"])
        payload["superseded_canonical_paths"][0]["sha256"] = "0" * 64
        core.write_json(record_path, payload)
        with self.assertRaisesRegex(ValueError, "canonical artifact .* SHA does not match"):
            human_gate.validate_operator_invalidation_record(
                fixture.root, record_path, expected_issue_id=fixture.issue_id
            )

    def test_operator_invalidation_sequence_gap_and_duplicate_are_rejected(self) -> None:
        fixture, _, record_path = self._successful_invalidation()
        self.addCleanup(fixture.doCleanups)
        record_dir = record_path.parent
        duplicate = record_dir / "architecture-invalidation-0002.json"
        shutil.copy2(record_path, duplicate)
        with self.assertRaisesRegex(ValueError, "sequences must be contiguous"):
            human_gate._load_operator_invalidation_records(
                fixture.root, fixture.cfg, fixture.source_root, fixture.issue_id
            )
        duplicate.unlink()

        gap = record_dir / "architecture-invalidation-0003.json"
        gap_payload = copy.deepcopy(core.load_json(record_path))
        gap_payload["sequence"] = 3
        core.write_json(gap, gap_payload)
        with self.assertRaisesRegex(ValueError, "sequences must be contiguous"):
            human_gate._load_operator_invalidation_records(
                fixture.root, fixture.cfg, fixture.source_root, fixture.issue_id
            )
        gap.unlink()


if __name__ == "__main__":
    unittest.main()
