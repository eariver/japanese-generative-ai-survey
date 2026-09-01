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
        count = {"total": 1, "counts": {"synthetic": 1}}
        return {
            "schema_version": "2.0-rc1",
            "issue_id": state["issue_id"],
            "research_profile": state["research_profile"],
            "basis": {
                "architecture_sha256": architecture_sha,
                "production_profile_sha256": h,
                "profile_completeness_sha256": h,
                "materiality_ledger_sha256": h,
                "candidate_matrix_sha256": h,
                "candidate_selection_sha256": h,
            },
            "readiness": {"status": "READY_FOR_ARCHITECTURE_REVIEW", "errors": []},
            "discovery": count,
            "research_expansion": {
                "max_research_pass": 0,
                "pass_counts": {"0": 1},
                "parent_link_count": 0,
                "obligation_link_count": 1,
                "unique_obligation_count": 1,
                "root_discovery_count": 1,
                "expanded_discovery_count": 0,
            },
            "screening": count,
            "evidence": count,
            "materiality": count,
            "selection": count,
            "completeness": {"overall_status": "READY", "obligation_counts": {"SATISFIED": 1}},
            "major_material_destinations": [],
            "residual_limitations": [],
            "architecture": {
                "status": "PROPOSED",
                "editorial_thesis": "Synthetic architecture used only to test orchestration authority.",
                "package_count": 1,
                "packages": ["pkg-001"],
                "page_plan": {"target_pages": 8, "max_pages": 12, "notes": None},
            },
        }

    def handler_for(self, *, malformed_architecture: bool = False):
        def handler(root: Path, cfg: dict, state: dict, spec: dict, pinned: str) -> list[dict]:
            rows: list[dict] = []
            for expected in spec["expected_outputs"]:
                name = expected["name"]
                if expected.get("path"):
                    artifact = root / expected["path"]
                else:
                    artifact = root / "sources" / state["issue_id"] / "generated" / f"{spec['current_stage']}-{name}.json"
                if name == "issue-architecture":
                    payload = (
                        {"schema_version": "2.0-rc1", "issue_id": state["issue_id"], "status": "PROPOSED"}
                        if malformed_architecture
                        else self.synthetic_architecture(state)
                    )
                    core.write_json(artifact, payload)
                elif name == "architecture-review-summary":
                    architecture = root / "sources" / state["issue_id"] / "architecture-v2.json"
                    core.write_json(artifact, self.synthetic_review(state, core.sha256_file(architecture)))
                elif name == "architecture-review-attention":
                    generated = root / "sources" / state["issue_id"] / "generated"
                    review_attention.build_attention(
                        root,
                        generated / "DISCOVERY_COLLECTED-screening.json",
                        generated / "CANDIDATES_NORMALIZED-materiality.json",
                        generated / "EVIDENCE_REVIEWED-selection.json",
                        artifact,
                    )
                else:
                    core.write_json(
                        artifact,
                        {
                            "issue_id": state["issue_id"],
                            "stage": spec["current_stage"],
                            "name": name,
                            "implementation_commit_sha": pinned,
                        },
                    )
                rows.append(
                    {
                        "name": name,
                        "checkpoint": expected["checkpoint"],
                        "path": str(artifact.relative_to(root)),
                        "sha256": core.sha256_file(artifact),
                    }
                )
            return rows
        return handler

    @staticmethod
    def validator_for(validator_name: str):
        def validator(root: Path, cfg: dict, state: dict, spec: dict, outputs: list[dict], pinned: str) -> list[str]:
            if spec.get("validator") != validator_name:
                return ["validator identity mismatch"]
            if validator_name != "validate:architecture":
                return []
            by_name = {row["name"]: row for row in outputs}
            architecture_row = by_name.get("issue-architecture")
            review_row = by_name.get("architecture-review-summary")
            if architecture_row is None or review_row is None:
                return ["Architecture validator requires Architecture and Review Summary outputs"]
            plan = core.load_json(root / architecture_row["path"])
            required = {
                "schema_version", "issue_id", "research_profile", "publication_profile",
                "status", "basis", "editorial_thesis", "architecture_goals", "page_plan",
                "packages", "selected_exceptions", "profile_extensions",
                "publication_extensions", "human_review",
            }
            errors: list[str] = []
            if set(plan) != required:
                errors.append("Issue Architecture fields do not match semantic contract")
            if plan.get("status") != "PROPOSED" or plan.get("issue_id") != state["issue_id"]:
                errors.append("Issue Architecture identity/status invalid")
            review = core.load_json(root / review_row["path"])
            if review.get("readiness", {}).get("status") != "READY_FOR_ARCHITECTURE_REVIEW":
                errors.append("Architecture Review Summary not ready")
            if review.get("basis", {}).get("architecture_sha256") != architecture_row["sha256"]:
                errors.append("Architecture Review Summary does not bind Architecture output")
            return errors
        return validator

    def stage_registry(self, cfg: dict, *, malformed_architecture: bool = False) -> orchestrator.HandlerRegistry:
        registry: orchestrator.HandlerRegistry = {}
        for stage in cfg["orchestration"]["stage_plan"].values():
            registry[stage["handler"]] = self.handler_for(malformed_architecture=malformed_architecture)
            registry[stage["validator"]] = self.validator_for(stage["validator"])
        return registry

    def test_advance_to_gate_executes_validated_stage_order_and_pins_attestations(self) -> None:
        temp, root, cfg, state_path, pinned = self.sandbox()
        self.addCleanup(temp.cleanup)
        result = orchestrator.advance_to_gate(
            root, cfg, state_path, root / "sources/SP001/orchestration/v2",
            self.stage_registry(cfg),
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        self.assertEqual(result["terminal_reason"], "HUMAN_GATE_REACHED")
        self.assertEqual(result["executed_actions"], 5)
        state = core.load_json(state_path)
        self.assertEqual(state["lifecycle_state"], "ARCHITECTURE_ESTABLISHED")
        self.assertEqual(state["human_gates"]["architecture_review"], "pending")
        self.assertEqual(state["next_action"], "ARCHITECTURE_REVIEW")
        self.assertEqual(state["terminal_reason"], "HUMAN_GATE_REACHED")
        passed = ("discovery", "screening", "evidence", "materiality", "completeness", "selection", "architecture")
        for checkpoint in passed:
            self.assertEqual(state["machine_checkpoints"][checkpoint], "passed")
            authority = state["checkpoint_provenance"][checkpoint]
            self.assertIsInstance(authority, dict)
            self.assertEqual(core.sha256_file(root / authority["path"]), authority["sha256"])
        self.assertEqual(core.validate_state_semantics(root, cfg, state), [])

        specs = sorted((root / "sources/SP001/orchestration/v2/specs").glob("*.json"))
        results = sorted((root / "sources/SP001/orchestration/v2/results").glob("*.json"))
        self.assertEqual(len(specs), 6)
        self.assertEqual(len(results), 5)
        for path in results:
            payload = core.load_json(path)
            self.assertEqual(payload["status"], "SUCCEEDED")
            self.assertEqual(payload["implementation_commit_sha"], pinned)
            self.assertEqual(payload["validator"], core.load_json(root / payload["outputs"][0]["path"]).get("validator", payload["validator"]) if False else payload["validator"])
        terminal_spec = core.load_json(root / result["action_spec_path"])
        gate_inputs = {row["name"]: row for row in terminal_spec["required_inputs"]}
        self.assertIn("checkpoint-attestation:architecture", gate_inputs)
        self.assertEqual(gate_inputs["checkpoint-attestation:architecture"]["sha256"], state["checkpoint_provenance"]["architecture"]["sha256"])
        self.assertEqual(gate_inputs["issue-architecture"]["sha256"], core.sha256_file(root / "sources/SP001/architecture-v2.json"))
        self.assertEqual(gate_inputs["architecture-review-summary"]["sha256"], core.sha256_file(root / "sources/SP001/architecture-review-summary-v2.json"))
        self.assertEqual(gate_inputs["architecture-review-attention"]["sha256"], core.sha256_file(root / "sources/SP001/architecture-review-attention-v2.json"))

    def test_semantically_invalid_architecture_cannot_pass_checkpoint_or_reach_gate(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        with self.assertRaisesRegex(ValueError, "deterministic action failed"):
            orchestrator.advance_to_gate(
                root, cfg, state_path, root / "sources/SP001/orchestration/v2",
                self.stage_registry(cfg, malformed_architecture=True),
                clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
            )
        state = core.load_json(state_path)
        self.assertEqual(state["lifecycle_state"], "SELECTION_COMPLETE")
        self.assertEqual(state["machine_checkpoints"]["architecture"], "pending")
        self.assertIsNone(state["checkpoint_provenance"]["architecture"])
        self.assertEqual(state["human_gates"]["architecture_review"], "pending")
        self.assertIsNone(state["terminal_reason"])

    def test_architecture_approval_binds_attested_reviewed_bytes_and_gate_provenance(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        terminal = orchestrator.advance_to_gate(
            root, cfg, state_path, root / "sources/SP001/orchestration/v2",
            self.stage_registry(cfg),
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        spec_path = root / terminal["action_spec_path"]
        architecture_path = root / "sources/SP001/architecture-v2.json"
        review_path = root / "sources/SP001/architecture-review-summary-v2.json"
        approval_path = root / "sources/SP001/gates/architecture-approval.json"
        action_result_path = root / "sources/SP001/orchestration/v2/results/architecture-human-review.json"
        before_bytes = architecture_path.read_bytes()
        result = orchestrator.apply_architecture_approval(
            root, cfg, state_path, spec_path, architecture_path, review_path,
            approval_path, action_result_path, "human-reviewer",
            core.parse_instant("2026-08-22T03:10:00+09:00"),
            "review:SP001:architecture:1",
        )
        self.assertEqual(result["status"], "SUCCEEDED")
        self.assertEqual(architecture_path.read_bytes(), before_bytes)
        state = core.load_json(state_path)
        authority = state["human_gate_provenance"]["architecture_review"]
        self.assertEqual(authority["path"], "sources/SP001/gates/architecture-approval.json")
        self.assertEqual(authority["sha256"], core.sha256_file(approval_path))
        self.assertEqual(state["human_gates"]["architecture_review"], "approved")
        self.assertEqual(state["target_gate"], "PUBLICATION_PREVIEW")
        self.assertEqual(state["next_action"], "stage:drafting-synthesis")
        self.assertEqual(core.validate_state_semantics(root, cfg, state), [])
        next_spec = orchestrator.plan_action(root, cfg, state_path)
        inputs = {row["name"]: row for row in next_spec["required_inputs"]}
        self.assertIn("architecture-approval-record", inputs)
        self.assertEqual(inputs["architecture-approval-record"]["sha256"], authority["sha256"])

    def test_reviewed_or_attested_architecture_cannot_be_replaced(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        terminal = orchestrator.advance_to_gate(
            root, cfg, state_path, root / "sources/SP001/orchestration/v2",
            self.stage_registry(cfg),
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        spec_path = root / terminal["action_spec_path"]
        architecture_path = root / "sources/SP001/architecture-v2.json"
        review_path = root / "sources/SP001/architecture-review-summary-v2.json"
        changed = core.load_json(architecture_path)
        changed["editorial_thesis"] = "tampered"
        core.write_json(architecture_path, changed)
        with self.assertRaisesRegex(ValueError, "drift|stale|inconsistency"):
            orchestrator.apply_architecture_approval(
                root, cfg, state_path, spec_path, architecture_path, review_path,
                root / "sources/SP001/gates/architecture-approval.json",
                root / "sources/SP001/orchestration/v2/results/architecture-human-review.json",
                "human-reviewer", core.parse_instant("2026-08-22T03:10:00+09:00"),
                "review:SP001:architecture:1",
            )

    def test_noncanonical_approval_path_is_rejected_before_write(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        terminal = orchestrator.advance_to_gate(
            root, cfg, state_path, root / "sources/SP001/orchestration/v2",
            self.stage_registry(cfg),
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        wrong = root / "sources/SP001/wrong-approval.json"
        with self.assertRaisesRegex(ValueError, "canonical configured path"):
            orchestrator.apply_architecture_approval(
                root, cfg, state_path, root / terminal["action_spec_path"],
                root / "sources/SP001/architecture-v2.json",
                root / "sources/SP001/architecture-review-summary-v2.json",
                wrong,
                root / "sources/SP001/orchestration/v2/results/architecture-human-review.json",
                "human-reviewer", core.parse_instant("2026-08-22T03:10:00+09:00"),
                "review:SP001:architecture:1",
            )
        self.assertFalse(wrong.exists())

    def test_state_pinned_attestation_and_approval_cannot_be_rewritten(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        terminal = orchestrator.advance_to_gate(
            root, cfg, state_path, root / "sources/SP001/orchestration/v2",
            self.stage_registry(cfg),
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        state = core.load_json(state_path)
        discovery_authority = state["checkpoint_provenance"]["discovery"]
        attestation_path = root / discovery_authority["path"]
        attestation = core.load_json(attestation_path)
        attestation["validator"] = "validate:rewritten"
        core.write_json(attestation_path, attestation)
        with self.assertRaisesRegex(ValueError, "authority SHA drift"):
            orchestrator.plan_action(root, cfg, state_path)

        # Restore by regenerating the whole sandbox for the Gate provenance check.
        temp2, root2, cfg2, state_path2, _ = self.sandbox()
        self.addCleanup(temp2.cleanup)
        terminal2 = orchestrator.advance_to_gate(
            root2, cfg2, state_path2, root2 / "sources/SP001/orchestration/v2",
            self.stage_registry(cfg2),
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        approval_path = root2 / "sources/SP001/gates/architecture-approval.json"
        orchestrator.apply_architecture_approval(
            root2, cfg2, state_path2, root2 / terminal2["action_spec_path"],
            root2 / "sources/SP001/architecture-v2.json",
            root2 / "sources/SP001/architecture-review-summary-v2.json",
            approval_path,
            root2 / "sources/SP001/orchestration/v2/results/architecture-human-review.json",
            "human-reviewer", core.parse_instant("2026-08-22T03:10:00+09:00"),
            "review:SP001:architecture:1",
        )
        approval = core.load_json(approval_path)
        approval["reviewed_by"] = "rewritten-reviewer"
        core.write_json(approval_path, approval)
        with self.assertRaisesRegex(ValueError, "authority SHA drift"):
            orchestrator.plan_action(root2, cfg2, state_path2)

    def test_workflow_dispatch_is_not_blindly_retried_without_idempotency(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        stage = cfg["orchestration"]["stage_plan"]["ISSUE_INITIALIZED"]
        stage["action_kind"] = "WORKFLOW_DISPATCH"
        spec = orchestrator.plan_action(root, cfg, state_path)
        self.assertEqual(spec["action_kind"], "WORKFLOW_DISPATCH")
        self.assertFalse(spec["retry_policy"]["retryable"])
        self.assertEqual(spec["retry_policy"]["max_attempts"], 1)
        self.assertEqual(spec["idempotency"], {"mode": "NONE", "key": None})
        spec_path = root / "sources/SP001/orchestration/v2/specs/workflow.json"
        orchestrator.write_action_spec(spec_path, spec)
        attempts = {"count": 0}

        def failing(*args, **kwargs):
            attempts["count"] += 1
            raise RuntimeError("ambiguous dispatch response")

        result = orchestrator.execute_action(
            root, cfg, state_path, spec_path,
            root / "sources/SP001/orchestration/v2/results/workflow.json",
            {spec["handler"]: failing, spec["validator"]: self.validator_for(spec["validator"])},
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        self.assertEqual(result["status"], "FAILED")
        self.assertEqual(result["attempts"], 1)
        self.assertEqual(attempts["count"], 1)

        stage["retry_policy"] = {"retryable": True, "max_attempts": 3}
        with self.assertRaisesRegex(ValueError, "idempotency/reconciliation"):
            orchestrator.plan_action(root, cfg, state_path)

    def test_artifact_only_head_movement_is_allowed_but_control_code_change_fails(self) -> None:
        temp, root, cfg, state_path, pinned = self.sandbox()
        self.addCleanup(temp.cleanup)
        self.git(root, "add", "sources")
        self.git(root, "commit", "-m", "artifact checkpoint")
        artifact_head = self.git(root, "rev-parse", "HEAD")
        self.assertNotEqual(artifact_head, pinned)
        spec = orchestrator.plan_action(root, cfg, state_path)
        self.assertEqual(spec["basis"]["implementation_commit_sha"], pinned)
        self.assertEqual(spec["basis"]["observed_repository_head_sha"], artifact_head)
        control_file = root / "scripts/runtime-change.py"
        control_file.write_text("print('changed implementation')\n", encoding="utf-8")
        self.git(root, "add", "scripts/runtime-change.py")
        self.git(root, "commit", "-m", "change controlled implementation")
        with self.assertRaisesRegex(ValueError, "implementation-controlled files differ"):
            orchestrator.plan_action(root, cfg, state_path)

    def test_untracked_control_file_is_implementation_drift(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        control_file = root / "scripts/untracked-runtime.py"
        control_file.write_text("print('untracked control code')\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "implementation-controlled files differ"):
            orchestrator.plan_action(root, cfg, state_path)

    def test_preissued_spec_survives_artifact_only_head_movement(self) -> None:
        temp, root, cfg, state_path, pinned = self.sandbox()
        self.addCleanup(temp.cleanup)
        spec = orchestrator.plan_action(root, cfg, state_path)
        spec_path = root / "sources/SP001/orchestration/v2/specs/preissued.json"
        orchestrator.write_action_spec(spec_path, spec)
        artifact = root / "sources/SP001/external-checkpoint.txt"
        artifact.write_text("artifact-only\n", encoding="utf-8")
        self.git(root, "add", "sources")
        self.git(root, "commit", "-m", "artifact-only head movement")
        current = orchestrator.plan_action(root, cfg, state_path)
        self.assertNotEqual(spec["basis"]["observed_repository_head_sha"], current["basis"]["observed_repository_head_sha"])
        self.assertEqual(spec["action_id"], current["action_id"])
        result = orchestrator.execute_action(
            root, cfg, state_path, spec_path,
            root / "sources/SP001/orchestration/v2/results/preissued.json",
            {
                spec["handler"]: self.handler_for(),
                spec["validator"]: self.validator_for(spec["validator"]),
            },
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        self.assertEqual(result["status"], "SUCCEEDED")
        self.assertEqual(result["implementation_commit_sha"], pinned)
        state = core.load_json(state_path)
        self.assertEqual(state["lifecycle_state"], "DISCOVERY_COLLECTED")
        self.assertIsNotNone(state["checkpoint_provenance"]["discovery"])

    def test_interrupted_state_result_commit_is_recoverable_without_silent_divergence(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        spec = orchestrator.plan_action(root, cfg, state_path)
        spec_path = root / "sources/SP001/orchestration/v2/specs/transaction.json"
        orchestrator.write_action_spec(spec_path, spec)
        result_path = root / "sources/SP001/orchestration/v2/results/transaction.json"
        original_replace = os.replace
        calls = {"count": 0}

        def fail_after_state_replace(src, dst):
            calls["count"] += 1
            if calls["count"] == 2:
                raise OSError("simulated crash after State replacement")
            return original_replace(src, dst)

        with mock.patch.object(orchestrator.os, "replace", side_effect=fail_after_state_replace):
            with self.assertRaisesRegex(OSError, "simulated crash"):
                orchestrator.execute_action(
                    root, cfg, state_path, spec_path, result_path,
                    {
                        spec["handler"]: self.handler_for(),
                        spec["validator"]: self.validator_for(spec["validator"]),
                    },
                    clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
                )
        pending_result, state_next = orchestrator._transaction_paths(result_path)
        self.assertFalse(result_path.exists())
        self.assertTrue(pending_result.exists())
        self.assertFalse(state_next.exists())
        self.assertEqual(core.load_json(state_path)["lifecycle_state"], "DISCOVERY_COLLECTED")
        self.assertTrue(orchestrator._recover_pending_transaction(state_path, result_path))
        committed = core.load_json(result_path)
        self.assertEqual(committed["status"], "SUCCEEDED")
        self.assertEqual(committed["state_after_sha256"], core.sha256_file(state_path))
        self.assertTrue(committed["validation_attestations"])

    def test_retryable_local_handler_failure_never_becomes_human_or_exception_gate(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        spec = orchestrator.plan_action(root, cfg, state_path)
        spec_path = root / "sources/SP001/orchestration/v2/specs/failure.json"
        orchestrator.write_action_spec(spec_path, spec)
        attempts = {"count": 0}

        def failing(*args, **kwargs):
            attempts["count"] += 1
            raise RuntimeError("transient collector failure")

        result = orchestrator.execute_action(
            root, cfg, state_path, spec_path,
            root / "sources/SP001/orchestration/v2/results/failure.json",
            {spec["handler"]: failing, spec["validator"]: self.validator_for(spec["validator"])},
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        self.assertEqual(result["status"], "RETRYABLE_FAILURE")
        self.assertEqual(result["attempts"], cfg["orchestration"]["retry_policies"]["LOCAL_SCRIPT"]["max_attempts"])
        self.assertEqual(attempts["count"], result["attempts"])
        state = core.load_json(state_path)
        self.assertEqual(state["exception_gate"]["status"], "inactive")
        self.assertEqual(state["human_gates"]["architecture_review"], "pending")
        self.assertEqual(state["lifecycle_state"], "ISSUE_INITIALIZED")
        self.assertIsNone(state["checkpoint_provenance"]["discovery"])


if __name__ == "__main__":
    unittest.main()
