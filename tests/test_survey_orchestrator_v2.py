from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts import survey_orchestrator_v2 as orchestrator
from scripts import survey_production_v2 as core


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
        return temp, root, cfg, state_path, pinned

    @staticmethod
    def handler_for(expected_name: str):
        def handler(root: Path, cfg: dict, state: dict, spec: dict, pinned: str) -> list[dict]:
            rows: list[dict] = []
            for expected in spec["expected_outputs"]:
                name = expected["name"]
                artifact = root / "sources" / state["issue_id"] / "generated" / f"{spec['current_stage']}-{name}.json"
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
            if expected_name and expected_name not in {row["name"] for row in rows}:
                raise AssertionError(f"expected output was not planned: {expected_name}")
            return rows
        return handler

    def stage_registry(self, cfg: dict) -> orchestrator.HandlerRegistry:
        registry: orchestrator.HandlerRegistry = {}
        for stage in cfg["orchestration"]["stage_plan"].values():
            checkpoints = stage.get("checkpoints", [])
            expected_name = checkpoints[0] if checkpoints else (
                "publication-candidate" if stage["handler"] == "stage:publication-candidate" else ""
            )
            registry[stage["handler"]] = self.handler_for(expected_name)
        return registry

    def test_advance_to_gate_executes_registered_stage_order_without_chat_memory(self) -> None:
        temp, root, cfg, state_path, pinned = self.sandbox()
        self.addCleanup(temp.cleanup)
        result = orchestrator.advance_to_gate(
            root,
            cfg,
            state_path,
            root / "sources/SP001/orchestration/v2",
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
        for checkpoint in ("discovery", "screening", "evidence", "materiality", "completeness", "selection", "architecture"):
            self.assertEqual(state["machine_checkpoints"][checkpoint], "passed")
        specs = sorted((root / "sources/SP001/orchestration/v2/specs").glob("*.json"))
        results = sorted((root / "sources/SP001/orchestration/v2/results").glob("*.json"))
        self.assertEqual(len(specs), 6)
        self.assertEqual(len(results), 5)
        for path in results:
            payload = core.load_json(path)
            self.assertEqual(payload["status"], "SUCCEEDED")
            self.assertEqual(payload["implementation_commit_sha"], pinned)

    def test_architecture_approval_binds_exact_reviewed_bytes_and_promotes_target(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        terminal = orchestrator.advance_to_gate(
            root,
            cfg,
            state_path,
            root / "sources/SP001/orchestration/v2",
            self.stage_registry(cfg),
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        spec_path = root / terminal["action_spec_path"]
        architecture_path = root / "sources/SP001/architecture-v2.json"
        core.write_json(
            architecture_path,
            {"schema_version": "2.0-rc1", "issue_id": "SP001", "status": "PROPOSED"},
        )
        architecture_sha = core.sha256_file(architecture_path)
        review_path = root / "sources/SP001/architecture-review-summary-v2.json"
        core.write_json(
            review_path,
            {
                "schema_version": "2.0-rc1",
                "issue_id": "SP001",
                "readiness": {"status": "READY_FOR_ARCHITECTURE_REVIEW", "errors": []},
                "basis": {"architecture_sha256": architecture_sha},
            },
        )
        approval_path = root / "sources/SP001/gates/architecture-approval.json"
        action_result_path = root / "sources/SP001/orchestration/v2/results/architecture-human-review.json"
        before_bytes = architecture_path.read_bytes()
        result = orchestrator.apply_architecture_approval(
            root,
            cfg,
            state_path,
            spec_path,
            architecture_path,
            review_path,
            approval_path,
            action_result_path,
            "human-reviewer",
            core.parse_instant("2026-08-22T03:10:00+09:00"),
            "review:SP001:architecture:1",
        )
        self.assertEqual(result["status"], "SUCCEEDED")
        self.assertEqual(architecture_path.read_bytes(), before_bytes)
        approval = core.load_json(approval_path)
        self.assertEqual(approval["architecture_sha256"], architecture_sha)
        self.assertEqual(
            approval["architecture_review_summary_sha256"], core.sha256_file(review_path)
        )
        state = core.load_json(state_path)
        self.assertEqual(state["human_gates"]["architecture_review"], "approved")
        self.assertEqual(state["target_gate"], "PUBLICATION_PREVIEW")
        self.assertEqual(state["next_action"], "stage:drafting-synthesis")
        self.assertIsNone(state["terminal_reason"])
        next_spec = orchestrator.plan_action(root, cfg, state_path)
        self.assertEqual(next_spec["handler"], "stage:drafting-synthesis")
        self.assertEqual(next_spec["basis"]["implementation_commit_sha"], state["implementation"]["repository_commit_sha"])

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

    def test_stage_action_kind_is_contract_driven_and_supports_workflow_dispatch(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        cfg["orchestration"]["stage_plan"]["ISSUE_INITIALIZED"]["action_kind"] = "WORKFLOW_DISPATCH"
        spec = orchestrator.plan_action(root, cfg, state_path)
        self.assertEqual(spec["action_kind"], "WORKFLOW_DISPATCH")
        cfg["orchestration"]["stage_plan"]["ISSUE_INITIALIZED"]["action_kind"] = "CHAT_MAGIC"
        with self.assertRaisesRegex(ValueError, "invalid stage action_kind"):
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
        self.assertNotEqual(
            spec["basis"]["observed_repository_head_sha"],
            current["basis"]["observed_repository_head_sha"],
        )
        self.assertEqual(spec["action_id"], current["action_id"])
        result_path = root / "sources/SP001/orchestration/v2/results/preissued.json"
        result = orchestrator.execute_action(
            root,
            cfg,
            state_path,
            spec_path,
            result_path,
            {spec["handler"]: self.handler_for("discovery")},
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        self.assertEqual(result["status"], "SUCCEEDED")
        self.assertEqual(result["implementation_commit_sha"], pinned)
        self.assertEqual(core.load_json(state_path)["lifecycle_state"], "DISCOVERY_COLLECTED")

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
                    root,
                    cfg,
                    state_path,
                    spec_path,
                    result_path,
                    {spec["handler"]: self.handler_for("discovery")},
                    clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
                )

        pending_result, state_next = orchestrator._transaction_paths(result_path)
        self.assertFalse(result_path.exists())
        self.assertTrue(pending_result.exists())
        self.assertFalse(state_next.exists())
        self.assertEqual(core.load_json(state_path)["lifecycle_state"], "DISCOVERY_COLLECTED")
        self.assertTrue(orchestrator._recover_pending_transaction(state_path, result_path))
        self.assertTrue(result_path.exists())
        self.assertFalse(pending_result.exists())
        committed = core.load_json(result_path)
        self.assertEqual(committed["status"], "SUCCEEDED")
        self.assertEqual(committed["state_after_sha256"], core.sha256_file(state_path))

    def test_retryable_handler_failure_never_becomes_human_or_exception_gate(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        spec = orchestrator.plan_action(root, cfg, state_path)
        spec_path = root / "sources/SP001/orchestration/v2/specs/failure.json"
        orchestrator.write_action_spec(spec_path, spec)
        attempts = {"count": 0}

        def failing(*args, **kwargs):
            attempts["count"] += 1
            raise RuntimeError("transient collector failure")

        result_path = root / "sources/SP001/orchestration/v2/results/failure.json"
        before = state_path.read_bytes()
        result = orchestrator.execute_action(
            root,
            cfg,
            state_path,
            spec_path,
            result_path,
            {spec["handler"]: failing},
            clock=lambda: core.parse_instant("2026-08-22T03:05:00+09:00"),
        )
        self.assertEqual(result["status"], "RETRYABLE_FAILURE")
        self.assertEqual(result["attempts"], cfg["orchestration"]["retry_policy"]["max_attempts"])
        self.assertEqual(attempts["count"], result["attempts"])
        self.assertEqual(state_path.read_bytes(), before)
        state = core.load_json(state_path)
        self.assertEqual(state["exception_gate"]["status"], "inactive")
        self.assertEqual(state["human_gates"]["architecture_review"], "pending")
        self.assertEqual(state["lifecycle_state"], "ISSUE_INITIALIZED")


if __name__ == "__main__":
    unittest.main()
