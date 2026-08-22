from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from scripts import survey_orchestrator_v2 as orchestrator
from scripts import survey_production_v2 as core


class SurveyOrchestratorHardeningV2Tests(unittest.TestCase):
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
    def handler(root: Path, cfg: dict, state: dict, spec: dict, pinned: str) -> list[dict]:
        rows: list[dict] = []
        for expected in spec["expected_outputs"]:
            artifact = root / "sources" / state["issue_id"] / "generated" / f"{expected['name']}.json"
            core.write_json(
                artifact,
                {
                    "issue_id": state["issue_id"],
                    "name": expected["name"],
                    "implementation_commit_sha": pinned,
                },
            )
            rows.append(
                {
                    "name": expected["name"],
                    "checkpoint": expected["checkpoint"],
                    "path": str(artifact.relative_to(root)),
                    "sha256": core.sha256_file(artifact),
                }
            )
        return rows

    def test_untracked_control_file_is_implementation_drift(self) -> None:
        temp, root, cfg, state_path, _ = self.sandbox()
        self.addCleanup(temp.cleanup)
        untracked = root / "scripts/untracked-runtime.py"
        untracked.write_text("print('untracked control code')\n", encoding="utf-8")
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
            {spec["handler"]: self.handler},
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
                    {spec["handler"]: self.handler},
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


if __name__ == "__main__":
    unittest.main()
