"""Regression: Human Gate revision vs State-bound publication revalidation pointer.

Covers the generic lifecycle-integration defect where Publication Preview
REQUEST_CHANGES to DRAFT_COMPLETE (or any boundary invalidating the
validation checkpoint) left an orphaned active
publication_revalidation_provenance pointer, making legitimate rollback
impossible. The repair clears only the active State pointer when the
revision invalidates its validation basis, preserving the immutable
historical rN record.

No edition-specific conditionals; all fixtures are generic synthetic
WEEKLY editions. R1-R7 map to the maintenance mission.
"""
from __future__ import annotations

import os
import subprocess
import tempfile
import unittest
from datetime import timedelta
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_human_gate_v2 as human_gate
from scripts import survey_production_v2 as core
from scripts import survey_publication_v2 as publication
from scripts import survey_stage_validation_v2 as stage_validation
from tests.test_survey_publication_revalidation_v2 import (
    EXECUTOR,
    ISSUE,
    T0,
    Fixture,
)

BRANCH = "test/revalidation"
REMOTE_REF = f"refs/remotes/origin/{BRANCH}"


class RevalidationRevisionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(".").resolve()
        self.cfg = core.load_json(self.root / core.DEFAULT_CONFIG)
        self.impl = core.repository_commit_sha(self.root)
        subprocess.run(["git", "update-ref", "-d", REMOTE_REF], cwd=self.root, check=False, capture_output=True)
        subprocess.run(["git", "update-ref", REMOTE_REF, self.impl], cwd=self.root, check=True, capture_output=True)
        self.addCleanup(lambda: subprocess.run(["git", "update-ref", "-d", REMOTE_REF], cwd=self.root, check=False, capture_output=True))
        self._review_tip = self.impl

    def make_fixture(self) -> tuple[tempfile.TemporaryDirectory[str], Fixture]:
        temp = tempfile.TemporaryDirectory(dir=str(self.root))
        self.addCleanup(temp.cleanup)
        fix = Fixture(self.root, Path(temp.name))
        return temp, fix

    def _snapshot_review_commit(self, fix: Fixture) -> str:
        import tempfile as _tf

        fd, index_name = _tf.mkstemp(prefix="survey-reval-revision-index-")
        os.close(fd)
        index_path = Path(index_name)
        index_path.unlink()
        env = os.environ.copy()
        env["GIT_INDEX_FILE"] = str(index_path)
        try:
            subprocess.run(["git", "read-tree", self.impl], cwd=self.root, env=env, check=True, capture_output=True)
            for path in sorted(p for p in fix.base.rglob("*") if p.is_file()):
                rel = path.relative_to(self.root).as_posix()
                blob = subprocess.run(
                    ["git", "hash-object", "-w", str(path)],
                    cwd=self.root, check=True, capture_output=True, text=True,
                ).stdout.strip()
                subprocess.run(
                    ["git", "update-index", "--add", "--cacheinfo", f"100644,{blob},{rel}"],
                    cwd=self.root, env=env, check=True, capture_output=True,
                )
            tree = subprocess.run(["git", "write-tree"], cwd=self.root, env=env, check=True, capture_output=True, text=True).stdout.strip()
            commit = subprocess.run(
                ["git", "-c", "user.name=Survey Revalidation Revision Fixture",
                 "-c", "user.email=reval-revision@example.invalid",
                 "commit-tree", tree, "-p", self._review_tip, "-m", "Revalidation revision reviewed fixture snapshot"],
                cwd=self.root, check=True, capture_output=True, text=True,
            ).stdout.strip()
        finally:
            index_path.unlink(missing_ok=True)
        subprocess.run(["git", "update-ref", REMOTE_REF, commit], cwd=self.root, check=True, capture_output=True)
        self._review_tip = commit
        return commit

    def _regenerate(self, fix: Fixture, version: int = 2) -> None:
        for name in ("reader-manuscript-v2.json", "quality-regression-bundle-v2.json",
                     "semantic-editorial-review-v2.json", "visual-review-v2.json",
                     "reader-surface-input-v2.json", "reader-surface-semantic-review-v2.json",
                     "reader-surface-gate-v2.json"):
            (fix.src / "publication" / "v2" / name).unlink(missing_ok=True)
        fix._publication_files(version=version)
        fix._publication_authority()

    def _to_release_candidate(self, fix: Fixture):
        self._regenerate(fix, version=2)
        r1_path = agent.revalidate_publication_surface(
            self.root, self.cfg, fix.src / "production-state.json", "REVIEWED_CORE_CHANGE",
            "fixture reviewed core change", EXECUTOR, T0 + timedelta(hours=1), None,
        )
        r1_bytes = r1_path.read_bytes()
        r1_sha = core.sha256_file(r1_path)
        cand_path = fix.src / "publication" / "v2" / "publication-candidate-v2.json"
        publication.build_candidate(
            self.root, ISSUE, "WEEKLY_MAGAZINE",
            fix.src / "publication" / "v2" / "reader-manuscript-v2.json",
            fix.survey / "main.tex", fix.survey / "main.pdf", 1,
            fix.src / "publication" / "v2" / "quality-regression-bundle-v2.json",
            fix.src / "publication" / "v2" / "semantic-editorial-review-v2.json",
            fix.src / "publication" / "v2" / "visual-review-v2.json",
            cand_path,
        )
        report_path = fix.src / "execution" / "stage-report.json"
        stage_validation.validate_stage(
            self.root, self.cfg, fix.src / "production-state.json",
            {"publication-candidate": cand_path}, report_path, T0 + timedelta(hours=2),
        )
        reviews_path = fix.src / "execution" / "reviews.json"
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "fixture", "evidence": "revalidation revision advance",
            "result_path": str(report_path.relative_to(self.root)),
        }]})
        checkpoint = agent.build_stage_checkpoint(
            self.root, self.cfg, fix.src / "production-state.json",
            {"publication-candidate": cand_path}, reviews_path,
            "advance to RELEASE_CANDIDATE", T0 + timedelta(hours=3), None,
        )
        updated = agent.advance_with_checkpoint(self.root, self.cfg, fix.src / "production-state.json", checkpoint)
        return updated, cand_path, r1_path, r1_bytes, r1_sha

    def _request(self, fix: Fixture, boundary: str, revision: int = 1):
        commit = self._snapshot_review_commit(fix)
        return human_gate.request_publication_preview_revision(
            self.root, self.cfg, fix.src / "production-state.json", boundary,
            f"Fixture Human correction to {boundary}.", "fixture-human",
            T0 + timedelta(hours=4), f"review:publication:r{revision}-{boundary.lower()}",
            expected_revision=revision, reviewed_commit_sha=commit,
        ) + (commit,)

    def test_r1_draft_complete_clears_pointer(self) -> None:
        _, fix = self.make_fixture()
        updated, _, r1_path, r1_bytes, _ = self._to_release_candidate(fix)
        self.assertEqual(updated["lifecycle_state"], "RELEASE_CANDIDATE")
        self.assertIsNotNone(updated.get("publication_revalidation_provenance"))
        self.assertEqual(agent.validate_agent_state(self.root, self.cfg, updated), [])
        state, record_path, index_path, _, commit = self._request(fix, "DRAFT_COMPLETE")
        self.assertEqual(state["lifecycle_state"], "DRAFT_COMPLETE")
        self.assertEqual(state["human_gates"]["architecture_review"], "approved")
        self.assertEqual(state["human_gates"]["publication_preview"], "pending")
        self.assertEqual(state["machine_checkpoints"]["validation"], "pending")
        self.assertIsNone(state["checkpoint_provenance"]["validation"])
        self.assertIsNone(state.get("publication_revalidation_provenance"))
        self.assertEqual(agent.validate_agent_state(self.root, self.cfg, state), [])
        record = core.load_json(record_path)
        self.assertEqual(record["decision"], "REQUEST_CHANGES")
        self.assertEqual(record["revision"], 1)
        self.assertEqual(record["regeneration_boundary"], "DRAFT_COMPLETE")
        self.assertEqual(record["reviewed_repository_commit_sha"], commit)
        self.assertIsNone(record["approval"])
        index = core.load_json(index_path)
        self.assertEqual([(r["revision"], r["decision"]) for r in index["reviews"] if r["gate"] == "PUBLICATION_PREVIEW"], [(1, "REQUEST_CHANGES")])
        self.assertTrue(r1_path.is_file())
        self.assertEqual(r1_path.read_bytes(), r1_bytes)

    def test_r2_validated_draft_preserves_pointer(self) -> None:
        _, fix = self.make_fixture()
        updated, _, _, _, _ = self._to_release_candidate(fix)
        before_pointer = dict(updated["publication_revalidation_provenance"])
        state, _, _, _, _ = self._request(fix, "VALIDATED_DRAFT")
        self.assertEqual(state["lifecycle_state"], "VALIDATED_DRAFT")
        self.assertEqual(state["machine_checkpoints"]["validation"], "passed")
        self.assertIsNotNone(state["checkpoint_provenance"]["validation"])
        self.assertEqual(state.get("publication_revalidation_provenance"), before_pointer)
        self.assertEqual(agent.validate_agent_state(self.root, self.cfg, state), [])

    def test_r3_earlier_boundary_clears_pointer(self) -> None:
        _, fix = self.make_fixture()
        self._to_release_candidate(fix)
        state, _, _, _, _ = self._request(fix, "ARCHITECTURE_ESTABLISHED")
        self.assertEqual(state["lifecycle_state"], "ARCHITECTURE_ESTABLISHED")
        self.assertEqual(state["machine_checkpoints"]["validation"], "pending")
        self.assertIsNone(state.get("publication_revalidation_provenance"))
        self.assertEqual(agent.validate_agent_state(self.root, self.cfg, state), [])

    def test_r4_corrupt_pointer_fails_preflight(self) -> None:
        import json as _json

        _, fix = self.make_fixture()
        self._to_release_candidate(fix)
        state_path = fix.src / "production-state.json"
        before_bytes = state_path.read_bytes()
        state = _json.loads(before_bytes.decode("utf-8"))
        pointer = dict(state["publication_revalidation_provenance"])
        pointer["sha256"] = "0" * 64
        state["publication_revalidation_provenance"] = pointer
        state_path.write_text(_json.dumps(state), encoding="utf-8")
        corrupt_state_bytes = state_path.read_bytes()
        review_record_path = fix.src / "gates" / "reviews" / "publication-r1.json"
        review_index_path = fix.src / "gates" / "review-index.json"
        self.assertFalse(review_record_path.exists())
        self.assertFalse(review_index_path.exists())
        validation_checkpoint = fix.src / "orchestration" / "v2" / "checkpoints" / "DRAFT_COMPLETE.json"
        candidate_checkpoint = fix.src / "orchestration" / "v2" / "checkpoints" / "VALIDATED_DRAFT.json"
        self.assertTrue(validation_checkpoint.is_file())
        self.assertTrue(candidate_checkpoint.is_file())
        commit = self._snapshot_review_commit(fix)
        with self.assertRaises((human_gate.HumanGateError, agent.AgentControlError)):
            human_gate.request_publication_preview_revision(
                self.root, self.cfg, state_path, "DRAFT_COMPLETE",
                "Corrupt pointer must fail closed.", "fixture-human",
                T0 + timedelta(hours=4), "review:publication:corrupt",
                expected_revision=1, reviewed_commit_sha=commit,
            )
        self.assertEqual(state_path.read_bytes(), corrupt_state_bytes)
        # No review record must have been created.
        self.assertFalse(review_record_path.exists())
        # No review index must have been created as a side effect.
        self.assertFalse(review_index_path.exists())
        # No other canonical Human Gate output may have been written.
        self.assertFalse((fix.src / "gates" / "reviews" / "approvals" / "publication-r1.json").exists())
        self.assertTrue(validation_checkpoint.is_file())
        self.assertTrue(candidate_checkpoint.is_file())

    def test_r5_historical_record_retained_byte_identical(self) -> None:
        _, fix = self.make_fixture()
        _, _, r1_path, r1_bytes, r1_sha = self._to_release_candidate(fix)
        self._request(fix, "DRAFT_COMPLETE")
        self.assertTrue(r1_path.is_file())
        self.assertEqual(r1_path.read_bytes(), r1_bytes)
        self.assertEqual(core.sha256_file(r1_path), r1_sha)

    def _recover_to_release_candidate(self, fix: Fixture, version: int = 3):
        # From rolled-back DRAFT_COMPLETE through the normal pipeline.
        self._regenerate(fix, version=version)
        state_path = fix.src / "production-state.json"
        validation_artifacts = {
            "reader-manuscript": fix.src / "publication" / "v2" / "reader-manuscript-v2.json",
            "validated-source": fix.survey / "main.tex",
            "publication-pdf": fix.survey / "main.pdf",
            "quality-regression-bundle": fix.src / "publication" / "v2" / "quality-regression-bundle-v2.json",
            "semantic-review": fix.src / "publication" / "v2" / "semantic-editorial-review-v2.json",
            "visual-review": fix.src / "publication" / "v2" / "visual-review-v2.json",
            "reader-surface-gate": fix.src / "publication" / "v2" / "reader-surface-gate-v2.json",
        }
        report_path = fix.src / "execution" / "stage-report-r2.json"
        stage_validation.validate_stage(
            self.root, self.cfg, state_path, validation_artifacts, report_path, T0 + timedelta(hours=5),
        )
        reviews_path = fix.src / "execution" / "reviews-r2.json"
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "fixture", "evidence": "r6 recovery validation",
            "result_path": str(report_path.relative_to(self.root)),
        }]})
        checkpoint = agent.build_stage_checkpoint(
            self.root, self.cfg, state_path, validation_artifacts, reviews_path,
            "r6 recovery validation", T0 + timedelta(hours=6), None,
        )
        updated = agent.advance_with_checkpoint(self.root, self.cfg, state_path, checkpoint)
        self.assertEqual(updated["lifecycle_state"], "VALIDATED_DRAFT")
        cand_path = fix.src / "publication" / "v2" / "publication-candidate-v2.json"
        if cand_path.exists():
            cand_path.unlink()
        publication.build_candidate(
            self.root, ISSUE, "WEEKLY_MAGAZINE",
            fix.src / "publication" / "v2" / "reader-manuscript-v2.json",
            fix.survey / "main.tex", fix.survey / "main.pdf", 1,
            fix.src / "publication" / "v2" / "quality-regression-bundle-v2.json",
            fix.src / "publication" / "v2" / "semantic-editorial-review-v2.json",
            fix.src / "publication" / "v2" / "visual-review-v2.json",
            cand_path,
        )
        report2 = fix.src / "execution" / "stage-report-r2b.json"
        stage_validation.validate_stage(self.root, self.cfg, state_path, {"publication-candidate": cand_path}, report2, T0 + timedelta(hours=7))
        reviews2 = fix.src / "execution" / "reviews-r2b.json"
        core.write_json(reviews2, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "fixture", "evidence": "r6 recovery candidate",
            "result_path": str(report2.relative_to(self.root)),
        }]})
        checkpoint2 = agent.build_stage_checkpoint(
            self.root, self.cfg, state_path, {"publication-candidate": cand_path}, reviews2,
            "r6 recovery candidate", T0 + timedelta(hours=8), None,
        )
        final = agent.advance_with_checkpoint(self.root, self.cfg, state_path, checkpoint2)
        return final

    def test_r6_forward_recovery_roundtrip(self) -> None:
        _, fix = self.make_fixture()
        _, _, r1_path, r1_bytes, _ = self._to_release_candidate(fix)
        rolled, _, _, _, _ = self._request(fix, "DRAFT_COMPLETE")
        self.assertEqual(rolled["lifecycle_state"], "DRAFT_COMPLETE")
        self.assertIsNone(rolled.get("publication_revalidation_provenance"))
        final = self._recover_to_release_candidate(fix, version=3)
        self.assertEqual(final["lifecycle_state"], "RELEASE_CANDIDATE")
        self.assertEqual(final["human_gates"]["publication_preview"], "pending")
        self.assertEqual(final["human_gates"]["architecture_review"], "approved")
        self.assertIsNone(final.get("publication_revalidation_provenance"))
        self.assertEqual(agent.validate_agent_state(self.root, self.cfg, final), [])
        self.assertEqual(r1_path.read_bytes(), r1_bytes)

    def test_r7_later_revalidation_sequence_usable(self) -> None:
        _, fix = self.make_fixture()
        _, _, r1_path, r1_bytes, _ = self._to_release_candidate(fix)
        self._request(fix, "DRAFT_COMPLETE")
        # Recover only to VALIDATED_DRAFT, then exercise a later revalidation.
        self._regenerate(fix, version=3)
        state_path = fix.src / "production-state.json"
        validation_artifacts = {
            "reader-manuscript": fix.src / "publication" / "v2" / "reader-manuscript-v2.json",
            "validated-source": fix.survey / "main.tex",
            "publication-pdf": fix.survey / "main.pdf",
            "quality-regression-bundle": fix.src / "publication" / "v2" / "quality-regression-bundle-v2.json",
            "semantic-review": fix.src / "publication" / "v2" / "semantic-editorial-review-v2.json",
            "visual-review": fix.src / "publication" / "v2" / "visual-review-v2.json",
            "reader-surface-gate": fix.src / "publication" / "v2" / "reader-surface-gate-v2.json",
        }
        report_path = fix.src / "execution" / "stage-report-r7.json"
        stage_validation.validate_stage(self.root, self.cfg, state_path, validation_artifacts, report_path, T0 + timedelta(hours=5))
        reviews_path = fix.src / "execution" / "reviews-r7.json"
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "fixture", "evidence": "r7 recovery validation",
            "result_path": str(report_path.relative_to(self.root)),
        }]})
        checkpoint = agent.build_stage_checkpoint(
            self.root, self.cfg, state_path, validation_artifacts, reviews_path,
            "r7 recovery validation", T0 + timedelta(hours=6), None,
        )
        updated = agent.advance_with_checkpoint(self.root, self.cfg, state_path, checkpoint)
        self.assertEqual(updated["lifecycle_state"], "VALIDATED_DRAFT")
        self.assertIsNone(updated.get("publication_revalidation_provenance"))
        # Historical r1 must not break sequence discovery.
        seqs_before = agent._revalidation_existing_sequences(self.root, self.cfg, updated)
        self.assertIn(1, seqs_before)
        # A later legitimate regeneration + revalidation must succeed.
        self._regenerate(fix, version=4)
        r2_path = agent.revalidate_publication_surface(
            self.root, self.cfg, state_path, "REVIEWED_CORE_CHANGE",
            "later fixture change", EXECUTOR, T0 + timedelta(hours=7), None,
        )
        self.assertTrue(r2_path.is_file())
        self.assertNotEqual(r2_path, r1_path)
        self.assertEqual(r1_path.read_bytes(), r1_bytes)
        after = core.load_json(state_path)
        self.assertIsNotNone(after.get("publication_revalidation_provenance"))
        self.assertEqual(agent.validate_agent_state(self.root, self.cfg, after), [])
        record, errors = agent.resolve_active_publication_revalidation(self.root, self.cfg, after)
        self.assertIsNotNone(record)
        self.assertEqual(errors, [])

    def test_no_edition_conditionals_in_revision_pointer(self) -> None:
        source = (self.root / "scripts" / "survey_human_gate_v2.py").read_text(encoding="utf-8")
        start = source.index("def _revised_state")
        end = source.index("def _validate_pending_gate_surface")
        block = source[start:end]
        for token in ("2026-W34", "W34", "WEEKLY", "LONGFORM", "Special", "special", "retrospective", "thematic", "weekly/"):
            self.assertNotIn(token, block, token)


if __name__ == "__main__":
    unittest.main()
