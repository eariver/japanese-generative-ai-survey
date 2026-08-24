from __future__ import annotations

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts import survey_human_gate_v2 as human_gate
from scripts import survey_production_v2 as core
from tests.test_survey_human_gate_v2 import SurveyHumanGateV2Tests


class SurveyHumanGateAuditMatrixV2Tests(unittest.TestCase):
    """Fixed-head audit coverage for Human Gate requirements that span a matrix."""

    @staticmethod
    def _fixture() -> SurveyHumanGateV2Tests:
        SurveyHumanGateV2Tests.setUpClass()
        fixture = SurveyHumanGateV2Tests(
            methodName="test_architecture_request_changes_regenerates_r2_then_approves"
        )
        fixture.setUp()
        return fixture

    @staticmethod
    def _advance_from_current_to_selection(fixture: SurveyHumanGateV2Tests) -> None:
        while True:
            state = core.load_json(fixture.state_path)
            lifecycle = state["lifecycle_state"]
            if lifecycle == "SELECTION_COMPLETE":
                return
            if lifecycle == "ISSUE_INITIALIZED":
                fixture._advance(
                    fixture._artifacts(
                        {"discovery-acceptance": "discovery/discovery-accepted-v2.json"}
                    ),
                    "AUDIT_DISCOVERY_REPLAY",
                    "2026-08-24T01:01:00Z",
                )
            elif lifecycle == "DISCOVERY_COLLECTED":
                fixture._advance(
                    fixture._artifacts(
                        {
                            "screening-acceptance":
                            "screening/v2/accepted-fixture/screening-accepted.json"
                        }
                    ),
                    "AUDIT_SCREENING_REPLAY",
                    "2026-08-24T01:02:00Z",
                )
            elif lifecycle == "CANDIDATES_NORMALIZED":
                fixture._advance(
                    fixture._artifacts(
                        {
                            "evidence-acceptance": "evidence/v2/evidence-accepted.json",
                            "edition-views-acceptance":
                            "evidence/v2/edition-views-accepted.json",
                            "materiality-ledger": "materiality-ledger-v2.json",
                            "profile-completeness": "profile-completeness-v2.json",
                        }
                    ),
                    "AUDIT_EVIDENCE_REPLAY",
                    "2026-08-24T01:03:00Z",
                )
            elif lifecycle == "EVIDENCE_REVIEWED":
                fixture._advance(
                    fixture._artifacts(
                        {
                            "candidate-matrix": "candidate-matrix-v2.json",
                            "candidate-selection": "candidate-selection-v2.json",
                        }
                    ),
                    "AUDIT_SELECTION_REPLAY",
                    "2026-08-24T01:04:00Z",
                )
            else:
                raise AssertionError(f"unexpected rollback lifecycle: {lifecycle}")

    @staticmethod
    def _publish_nonregular_review_path_commit(
        fixture: SurveyHumanGateV2Tests,
        rel: str,
    ) -> str:
        valid_parent = fixture._snapshot_review_commit()
        fd, index_name = tempfile.mkstemp(prefix="survey-human-review-nonregular-index-")
        os.close(fd)
        index_path = Path(index_name)
        index_path.unlink()
        env = os.environ.copy()
        env["GIT_INDEX_FILE"] = str(index_path)
        try:
            subprocess.run(
                ["git", "read-tree", valid_parent],
                cwd=fixture.root,
                env=env,
                check=True,
                capture_output=True,
            )
            blob = subprocess.run(
                ["git", "hash-object", "-w", "--stdin"],
                cwd=fixture.root,
                input="non-regular-review-target\n",
                text=True,
                check=True,
                capture_output=True,
            ).stdout.strip()
            subprocess.run(
                [
                    "git",
                    "update-index",
                    "--add",
                    "--cacheinfo",
                    f"120000,{blob},{rel}",
                ],
                cwd=fixture.root,
                env=env,
                check=True,
                capture_output=True,
            )
            tree = subprocess.run(
                ["git", "write-tree"],
                cwd=fixture.root,
                env=env,
                text=True,
                check=True,
                capture_output=True,
            ).stdout.strip()
            commit = subprocess.run(
                [
                    "git",
                    "-c",
                    "user.name=Survey Human Gate Audit Fixture",
                    "-c",
                    "user.email=survey-human-gate-audit@example.invalid",
                    "commit-tree",
                    tree,
                    "-p",
                    valid_parent,
                    "-m",
                    "Human Gate non-regular reviewed-path fixture",
                ],
                cwd=fixture.root,
                text=True,
                check=True,
                capture_output=True,
            ).stdout.strip()
        finally:
            index_path.unlink(missing_ok=True)
        subprocess.run(
            ["git", "update-ref", fixture.remote_ref, commit],
            cwd=fixture.root,
            check=True,
            capture_output=True,
        )
        fixture._review_tip = commit
        return commit

    def test_architecture_request_changes_round_trips_from_every_allowed_boundary(self) -> None:
        expected = [
            "ISSUE_INITIALIZED",
            "DISCOVERY_COLLECTED",
            "CANDIDATES_NORMALIZED",
            "EVIDENCE_REVIEWED",
            "SELECTION_COMPLETE",
        ]
        cfg = core.load_json(Path(core.DEFAULT_CONFIG))
        self.assertEqual(
            cfg["orchestration"]["human_gate_revision_boundaries"]["ARCHITECTURE_REVIEW"],
            expected,
        )

        for index, boundary in enumerate(expected, start=1):
            with self.subTest(boundary=boundary):
                fixture = self._fixture()
                try:
                    fixture._advance_to_selection()
                    fixture._reach_architecture_gate(
                        f"Architecture audit r1 {boundary}",
                        "2026-08-24T00:05:00Z",
                    )
                    state, record_r1, _, _ = human_gate.request_architecture_revision(
                        fixture.root,
                        fixture.cfg,
                        fixture.state_path,
                        boundary,
                        f"Repair Architecture dependency class {boundary}.",
                        "human-reviewer",
                        core.parse_instant("2026-08-24T00:06:00Z"),
                        f"review:architecture:audit-boundary:{index}",
                        expected_revision=1,
                        reviewed_commit_sha=fixture._snapshot_review_commit(),
                    )
                    self.assertEqual(state["lifecycle_state"], boundary)
                    self.assertEqual(core.load_json(record_r1)["decision"], "REQUEST_CHANGES")
                    self.assertEqual(state["human_gates"]["architecture_review"], "pending")

                    self._advance_from_current_to_selection(fixture)
                    fixture._reach_architecture_gate(
                        f"Architecture audit r2 {boundary}",
                        "2026-08-24T01:05:00Z",
                    )
                    state, record_r2, review_index = human_gate.record_architecture_approval(
                        fixture.root,
                        fixture.cfg,
                        fixture.state_path,
                        "human-reviewer",
                        core.parse_instant("2026-08-24T01:06:00Z"),
                        f"review:architecture:audit-r2:{index}",
                        expected_revision=2,
                        reviewed_commit_sha=fixture._snapshot_review_commit(),
                    )
                    self.assertEqual(state["human_gates"]["architecture_review"], "approved")
                    self.assertEqual(state["next_action"], "stage:drafting-synthesis")
                    self.assertIsNone(state["terminal_reason"])
                    self.assertEqual(core.load_json(record_r2)["decision"], "APPROVED")
                    rows = [
                        (row["revision"], row["decision"])
                        for row in core.load_json(review_index)["reviews"]
                        if row["gate"] == "ARCHITECTURE_REVIEW"
                    ]
                    self.assertEqual(rows, [(1, "REQUEST_CHANGES"), (2, "APPROVED")])
                finally:
                    fixture.doCleanups()

    def test_r1_approvals_resume_drafting_and_freeze(self) -> None:
        fixture = self._fixture()
        self.addCleanup(fixture.doCleanups)
        fixture._advance_to_selection()
        fixture._reach_architecture_gate("Architecture audit direct approve r1", "2026-08-24T00:05:00Z")
        state, _, _ = human_gate.record_architecture_approval(
            fixture.root,
            fixture.cfg,
            fixture.state_path,
            "human-reviewer",
            core.parse_instant("2026-08-24T00:06:00Z"),
            "review:architecture:audit-direct-r1",
            expected_revision=1,
            reviewed_commit_sha=fixture._snapshot_review_commit(),
        )
        self.assertEqual(state["next_action"], "stage:drafting-synthesis")
        self.assertIsNone(state["terminal_reason"])

        fixture._reach_publication_gate(1, 10)
        state, _, _ = human_gate.record_publication_preview_approval(
            fixture.root,
            fixture.cfg,
            fixture.state_path,
            "human-reviewer",
            core.parse_instant("2026-08-24T00:14:00Z"),
            "review:publication:audit-direct-r1",
            expected_revision=1,
            reviewed_commit_sha=fixture._snapshot_review_commit(),
        )
        self.assertEqual(state["next_action"], "stage:freeze")
        self.assertIsNone(state["terminal_reason"])

    def test_reviewed_commit_rejects_non_regular_gate_input_path(self) -> None:
        fixture = self._fixture()
        self.addCleanup(fixture.doCleanups)
        fixture._advance_to_selection()
        fixture._reach_architecture_gate("Architecture non-regular provenance", "2026-08-24T00:05:00Z")
        architecture_rel = (fixture.source_root / "architecture-v2.json").relative_to(
            fixture.root
        ).as_posix()
        reviewed_commit = self._publish_nonregular_review_path_commit(
            fixture,
            architecture_rel,
        )
        with self.assertRaisesRegex(ValueError, "reviewed repository path is not a regular file"):
            human_gate.record_architecture_approval(
                fixture.root,
                fixture.cfg,
                fixture.state_path,
                "human-reviewer",
                core.parse_instant("2026-08-24T00:06:00Z"),
                "review:architecture:non-regular-path",
                expected_revision=1,
                reviewed_commit_sha=reviewed_commit,
            )


if __name__ == "__main__":
    unittest.main()
