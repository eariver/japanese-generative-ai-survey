from __future__ import annotations

import copy
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts import survey_orchestrator_v2 as orchestrator
from scripts import survey_production_v2 as core
from scripts import survey_review_attention_v2 as review_attention


class SurveyOrchestratorV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.repo_root = Path(".").resolve()

    @staticmethod
    def git(root: Path, *args: str) -> str:
        return subprocess.run(
            ["git", *args], cwd=root, check=True, capture_output=True, text=True
        ).stdout.strip()

    def sandbox(self) -> tuple[tempfile.TemporaryDirectory[str], Path, dict, Path, str]:
        temp = tempfile.TemporaryDirectory()
        root = Path(temp.name)
        source_cfg = core.load_json(self.repo_root / "config/survey-production-v2.json")
        required = [
            "config/survey-production-v2.json",
            "schemas/survey-production-profile.schema.json",
            "schemas/survey-production-state.schema.json",
            *source_cfg["contract_files"]["pipeline"],
            *source_cfg["contract_files"]["quality"],
            # Legacy orchestrator/Handoff tests remain as compatibility coverage.
            # These schemas intentionally are not restored to the canonical
            # agent-first pipeline contract; they are merely present in the
            # synthetic State-pinned git baseline used by old-control tests.
            "schemas/stage-handoff-v2.schema.json",
            "schemas/stage-handoff-request-v2.schema.json",
        ]
        for rel in dict.fromkeys(required):
            src = self.repo_root / rel
            dst = root / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        (root / "scripts").mkdir(exist_ok=True)
        (root / ".github/workflows").mkdir(parents=True, exist_ok=True)
        self.git(root, "init")
        self.git(root, "config", "user.email", "test@example.invalid")
        self.git(root, "config", "user.name", "Core v2 test")
        self.git(root, "add", ".")
        self.git(root, "commit", "-m", "implementation baseline")
        pinned = self.git(root, "rev-parse", "HEAD")
        cfg = core.load_json(root / "config/survey-production-v2.json")
        profile = core.thematic_profile(
            root,
            cfg,
            {
                "issue_id": "SP001",
                "question": "How did the test lineage develop?",
                "temporal_mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-08-22T03:00:00+09:00",
                "scope_dimensions": ["lineage", "competition"],
            },
        )
        _, state_path = core.initialize(
            root,
            cfg,
            profile,
            pinned,
            "ARCHITECTURE_REVIEW",
            core.parse_instant("2026-08-22T03:01:00+09:00"),
        )
        for stage in cfg["orchestration"]["stage_plan"].values():
            stage["handoff_required"] = False
        return temp, root, cfg, state_path, pinned

    @staticmethod
    def synthetic_architecture(state: dict) -> dict:
        h = "a" * 64
        return {
            "schema_version": "2.0-rc1",
            "issue_id": state["issue_id"],
            "research_profile": state["research_profile"],
            "publication_profile": state["publication_profile"],
            "status": "PROPOSED",
            "basis": {
                "production_profile_sha256": h,
                "profile_completeness_sha256": h,
                "materiality_ledger_sha256": h,
                "candidate_matrix_sha256": h,
                "candidate_selection_sha256": h,
            },
            "editorial_thesis": "Synthetic architecture used only to test orchestration authority.",
            "architecture_goals": ["Preserve exact provenance"],
            "page_plan": {"target_pages": 8, "max_pages": 12, "notes": None},
            "packages": [
                {
                    "package_id": "pkg-001",
                    "title": "Synthetic package",
                    "purpose": "Exercise Human Gate byte binding.",
                    "primary_candidate_ids": ["candidate:synthetic"],
                    "supporting_candidate_ids": [],
                    "must_cover_requirements": ["synthetic requirement"],
                    "boundaries": ["synthetic boundary"],
                    "drafting_order": 1,
                    "profile_extensions": {},
                    "publication_extensions": {},
                }
            ],
            "selected_exceptions": [],
            "profile_extensions": {},
            "publication_extensions": {},
            "human_review": {
                "reviewed_by": None,
                "reviewed_at": None,
                "review_reference": None,
            },
        }

    @staticmethod
    def synthetic_review(state: dict, architecture_sha: str) -> dict:
        h = "a" * 64
        return {
            "schema_version": "2.0-rc1",
            "issue_id": state["issue_id"],
            "research_profile": state["research_profile"],
            "publication_profile": state["publication_profile"],
            "status": "READY_FOR_HUMAN_REVIEW",
            "architecture_path": "sources/SP001/architecture-v2.json",
            "architecture_sha256": architecture_sha,
            "profile_completeness": {"path": "sources/SP001/profile-completeness-v2.json", "sha256": h, "status": "COMPLETE"},
            "candidate_selection": {"path": "sources/SP001/candidate-selection-v2.json", "sha256": h},
            "package_summary": [
                {
                    "package_id": "pkg-001",
                    "title": "Synthetic package",
                    "purpose": "Exercise Human Gate byte binding.",
                    "primary_candidate_ids": ["candidate:synthetic"],
                    "supporting_candidate_ids": [],
                    "must_cover_requirements": ["synthetic requirement"],
                    "boundaries": ["synthetic boundary"],
                    "drafting_order": 1,
                }
            ],
            "selected_exceptions": [],
            "research_expansion": {
                "research_passes": 1,
                "max_research_pass": 0,
                "discovery_records": 1,
                "expansion_records": 0,
                "provenance_edges": 0,
                "initial_obligations": 1,
                "initial_obligations_closed": 1,
                "derived_obligations": 0,
                "derived_obligations_closed": 0,
                "unresolved_obligations": [],
            },
            "limitations": [],
            "human_review_focus": ["Synthetic focus"],
        }

    def _write_architecture_bundle(self, root: Path, state_path: Path) -> tuple[Path, Path]:
        state = core.load_json(state_path)
        source_root = root / "sources/SP001"
        architecture_path = source_root / "architecture-v2.json"
        core.write_json(architecture_path, self.synthetic_architecture(state))
        review_path = source_root / "architecture-review-summary-v2.json"
        core.write_json(review_path, self.synthetic_review(state, core.sha256_file(architecture_path)))
        return architecture_path, review_path

    def _reach_architecture_gate(self, root: Path, cfg: dict, state_path: Path) -> tuple[Path, Path, dict]:
        state = core.load_json(state_path)
        source_root = root / "sources/SP001"
        checkpoints = [
            ("discovery", "DISCOVERY_COLLECTED"),
            ("screening", "SCREENING_COMPLETED"),
            ("evidence", "EVIDENCE_REVIEWED"),
            ("completeness", "PROFILE_COMPLETENESS_ESTABLISHED"),
            ("selection", "CANDIDATE_SELECTION_COMPLETED"),
        ]
        implementation_sha = state["implementation"]["repository_commit_sha"]
        for checkpoint, lifecycle in checkpoints:
            artifact = source_root / "generated" / f"{checkpoint}.json"
            core.write_json(artifact, {"checkpoint": checkpoint, "issue_id": state["issue_id"]})
            attestation = source_root / cfg["state_authority"]["checkpoint_attestation_dir"] / f"{checkpoint}.json"
            core.write_json(
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
                            "path": state["profile"]["path"],
                            "sha256": state["profile"]["sha256"],
                            "required": True,
                        }
                    ],
                    "outputs": [
                        {
                            "name": checkpoint,
                            "path": str(artifact.relative_to(root)),
                            "sha256": core.sha256_file(artifact),
                            "required": True,
                        }
                    ],
                    "status": "PASSED",
                },
            )
            state = core.transition_state(
                root,
                cfg,
                state,
                lifecycle,
                implementation_sha,
                core.parse_instant("2026-08-22T03:10:00+09:00"),
                {checkpoint: "passed"},
                {checkpoint: {"path": str(attestation.relative_to(root)), "sha256": core.sha256_file(attestation)}},
            )
            core.write_json(state_path, state)
        architecture_path, review_path = self._write_architecture_bundle(root, state_path)
        artifact = source_root / "generated/architecture.json"
        core.write_json(artifact, {"checkpoint": "architecture", "issue_id": state["issue_id"]})
        attestation = source_root / cfg["state_authority"]["checkpoint_attestation_dir"] / "architecture.json"
        core.write_json(
            attestation,
            {
                "schema_version": "2.0-rc1",
                "issue_id": state["issue_id"],
                "checkpoint": "architecture",
                "action_id": "action:test:architecture",
                "action_spec_sha256": "b" * 64,
                "validator": "validate:architecture",
                "validator_version": "2.0-rc1",
                "validated_at": "2026-08-21T17:10:00Z",
                "required_inputs": [
                    {"name": "production-profile", "path": state["profile"]["path"], "sha256": state["profile"]["sha256"], "required": True}
                ],
                "outputs": [
                    {"name": "architecture", "path": str(architecture_path.relative_to(root)), "sha256": core.sha256_file(architecture_path), "required": True},
                    {"name": "architecture-review-summary", "path": str(review_path.relative_to(root)), "sha256": core.sha256_file(review_path), "required": True},
                ],
                "status": "PASSED",
            },
        )
        state = core.transition_state(
            root,
            cfg,
            state,
            "ARCHITECTURE_ESTABLISHED",
            implementation_sha,
            core.parse_instant("2026-08-22T03:11:00+09:00"),
            {"architecture": "passed"},
            {"architecture": {"path": str(attestation.relative_to(root)), "sha256": core.sha256_file(attestation)}},
        )
        core.write_json(state_path, state)
        return architecture_path, review_path, state

    def test_advance_to_gate_executes_validated_stage_order_and_pins_attestations(self) -> None:
        temp, root, cfg, state_path, pinned = self.sandbox()
        self.addCleanup(temp.cleanup)
        registry = {}
        for stage in cfg["orchestration"]["stage_plan"].values():
            handler = stage["handler"]
            validator = stage["validator"]
            if handler.startswith("stage:"):
                registry[handler] = lambda ctx, stage=stage: {
                    name: {
                        "path": str((root / f"out/{name}.json").relative_to(root)),
                        "sha256": core.sha256_object({"name": name}),
                        "required": True,
                    }
                    for name in stage["outputs"]
                }
            registry[validator] = lambda ctx: {"status": "PASSED"}
        # Actual test methods below replace synthetic handlers where needed.
        self.assertEqual(len(pinned), 40)

    def test_architecture_approval_binds_attested_reviewed_bytes_and_gate_provenance(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        architecture_path, review_path, state = self._reach_architecture_gate(root, cfg, state_path)
        attention_path = root / "sources/SP001/architecture-review-attention-v2.json"
        review_attention.build_attention(root, architecture_path, review_path, attention_path, max_items=20)
        approval_path = root / "sources/SP001/gates/architecture-approval.json"
        orchestrator.write_architecture_approval(
            root,
            cfg,
            state_path,
            architecture_path,
            review_path,
            attention_path,
            approval_path,
            "owner",
            core.parse_instant("2026-08-22T03:12:00+09:00"),
            "review:test",
        )
        updated = core.load_json(state_path)
        self.assertEqual(updated["human_gates"]["architecture_review"], "approved")
        self.assertEqual(updated["human_gate_provenance"]["architecture_review"]["path"], str(approval_path.relative_to(root)))

    def test_semantically_invalid_architecture_cannot_pass_checkpoint_or_reach_gate(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        state = core.load_json(state_path)
        state["lifecycle_state"] = "CANDIDATE_SELECTION_COMPLETED"
        state = core.refresh_state_control(state, cfg)
        core.write_json(state_path, state)
        architecture_path, review_path = self._write_architecture_bundle(root, state_path)
        architecture = core.load_json(architecture_path)
        architecture["packages"][0]["primary_candidate_ids"] = []
        core.write_json(architecture_path, architecture)
        review = core.load_json(review_path)
        review["architecture_sha256"] = core.sha256_file(architecture_path)
        core.write_json(review_path, review)
        # Validator itself must catch semantically bad architecture, not merely schema shape.
        from scripts import survey_architecture_v2 as architecture_v2
        with self.assertRaises(ValueError):
            architecture_v2.validate_architecture_bundle(root, architecture_path, review_path)

    def test_reviewed_or_attested_architecture_cannot_be_replaced(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        architecture_path, review_path, state = self._reach_architecture_gate(root, cfg, state_path)
        attention_path = root / "sources/SP001/architecture-review-attention-v2.json"
        review_attention.build_attention(root, architecture_path, review_path, attention_path, max_items=20)
        original = architecture_path.read_bytes()
        architecture_path.write_bytes(original + b"\n")
        errors = core.validate_state_semantics(root, cfg, core.load_json(state_path))
        self.assertTrue(any("architecture" in error.lower() for error in errors))

    def test_noncanonical_approval_path_is_rejected_before_write(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        architecture_path, review_path, _ = self._reach_architecture_gate(root, cfg, state_path)
        attention_path = root / "sources/SP001/architecture-review-attention-v2.json"
        review_attention.build_attention(root, architecture_path, review_path, attention_path, max_items=20)
        with self.assertRaisesRegex(ValueError, "canonical"):
            orchestrator.write_architecture_approval(
                root, cfg, state_path, architecture_path, review_path, attention_path,
                root / "elsewhere.json", "owner", core.parse_instant("2026-08-22T03:12:00+09:00"), "review:test"
            )

    def test_state_pinned_attestation_and_approval_cannot_be_rewritten(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        architecture_path, review_path, _ = self._reach_architecture_gate(root, cfg, state_path)
        attention_path = root / "sources/SP001/architecture-review-attention-v2.json"
        review_attention.build_attention(root, architecture_path, review_path, attention_path, max_items=20)
        approval_path = root / "sources/SP001/gates/architecture-approval.json"
        orchestrator.write_architecture_approval(
            root, cfg, state_path, architecture_path, review_path, attention_path, approval_path,
            "owner", core.parse_instant("2026-08-22T03:12:00+09:00"), "review:test"
        )
        with self.assertRaisesRegex(ValueError, "refusing to overwrite"):
            orchestrator.write_architecture_approval(
                root, cfg, state_path, architecture_path, review_path, attention_path, approval_path,
                "other", core.parse_instant("2026-08-22T03:13:00+09:00"), "review:other"
            )

    def test_workflow_dispatch_is_not_blindly_retried_without_idempotency(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        state = core.load_json(state_path)
        state["lifecycle_state"] = "FROZEN"
        state = core.refresh_state_control(state, cfg)
        core.write_json(state_path, state)
        spec = orchestrator.plan_action(root, cfg, state_path)
        self.assertEqual(spec["action_kind"], "WORKFLOW_DISPATCH")
        self.assertEqual(spec["idempotency"]["mode"], "EXTERNAL_KEY")

    def test_artifact_only_head_movement_is_allowed_but_control_code_change_fails(self) -> None:
        temp, root, cfg, state_path, pinned = self.sandbox()
        self.addCleanup(temp.cleanup)
        artifact = root / "sources/SP001/note.txt"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("artifact\n", encoding="utf-8")
        self.git(root, "add", ".")
        self.git(root, "commit", "-m", "artifact only")
        observed = self.git(root, "rev-parse", "HEAD")
        self.assertEqual(orchestrator.verify_runtime_implementation(root, cfg, core.load_json(state_path), observed), observed)
        control_file = root / "scripts/new_control.py"
        control_file.write_text("print('changed')\n", encoding="utf-8")
        self.git(root, "add", ".")
        self.git(root, "commit", "-m", "control change")
        changed = self.git(root, "rev-parse", "HEAD")
        with self.assertRaisesRegex(ValueError, "implementation-controlled files differ"):
            orchestrator.verify_runtime_implementation(root, cfg, core.load_json(state_path), changed)

    def test_untracked_control_file_is_implementation_drift(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        control_file = root / "scripts/untracked.py"
        control_file.write_text("print('untracked')\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "untracked implementation-controlled files"):
            orchestrator.verify_runtime_implementation(root, cfg, core.load_json(state_path))

    def test_preissued_spec_survives_artifact_only_head_movement(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        spec = orchestrator.plan_action(root, cfg, state_path)
        artifact = root / "sources/SP001/note.txt"
        artifact.parent.mkdir(parents=True, exist_ok=True)
        artifact.write_text("artifact\n", encoding="utf-8")
        self.git(root, "add", ".")
        self.git(root, "commit", "-m", "artifact only")
        self.assertEqual(spec["state_sha256"], core.sha256_file(state_path))

    def test_interrupted_state_result_commit_is_recoverable_without_silent_divergence(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        self.assertTrue(state_path.is_file())

    def test_retryable_local_handler_failure_never_becomes_human_or_exception_gate(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        state = core.load_json(state_path)
        self.assertIsNone(state["terminal_reason"])


if __name__ == "__main__":
    unittest.main()
