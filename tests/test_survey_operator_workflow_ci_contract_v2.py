from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class SurveyOperatorWorkflowCIContractV2Tests(unittest.TestCase):
    def test_operator_workflow_materializes_canonical_remote_work_branch_ref(self) -> None:
        workflow = Path(
            ".github/workflows/survey-production-v2-operator-bridge.yml"
        ).read_text(encoding="utf-8")

        self.assertIn("issue_comment:", workflow)
        self.assertIn('canonical_work_ref="refs/remotes/origin/$request_work_branch"', workflow)
        self.assertIn('canonical_work_ref="refs/remotes/origin/$REQUEST_HEAD_BRANCH"', workflow)
        self.assertGreaterEqual(workflow.count('"refs/heads/$'), 2)
        self.assertNotIn("refs/remotes/origin/operator-work", workflow)

    def test_both_regression_workflows_watch_operator_workflow_changes(self) -> None:
        core_ci = Path(".github/workflows/survey-production-v2-ci.yml").read_text(
            encoding="utf-8"
        )
        pipeline_ci = Path(".github/workflows/pipeline-contract-tests.yml").read_text(
            encoding="utf-8"
        )

        operator_path = ".github/workflows/survey-production-v2-operator-bridge.yml"
        self.assertGreaterEqual(core_ci.count(operator_path), 2)
        self.assertIn(".github/workflows/*.yml", pipeline_ci)
        self.assertNotIn("workflow_run:", pipeline_ci)
        self.assertNotIn("contents: write", pipeline_ci)

    def test_config_names_default_branch_operator_workflow_as_trusted_executor(self) -> None:
        cfg = json.loads(
            Path("config/survey-production-v2.json").read_text(encoding="utf-8")
        )
        control = cfg["workflow_control"]

        self.assertEqual(
            control["operator_execution_bridge_workflow"],
            "survey-production-v2-operator-bridge.yml",
        )
        self.assertEqual(
            control["operator_execution_trusted_workflow"],
            "survey-production-v2-operator-bridge.yml",
        )
        self.assertNotEqual(
            control["operator_execution_trusted_workflow"],
            "pipeline-contract-tests.yml",
        )

    def test_preflight_python_is_isolated_from_untrusted_checkout(self) -> None:
        workflow = Path(
            ".github/workflows/survey-production-v2-operator-bridge.yml"
        ).read_text(encoding="utf-8")

        self.assertIn("python3 -I -c 'import json,sys;", workflow)
        self.assertIn('python3 -I - "$reviewed_main_sha"', workflow)
        self.assertNotIn("python -c 'import json,sys;", workflow)
        self.assertNotIn('python - "$reviewed_main_sha"', workflow)

        with tempfile.TemporaryDirectory(prefix="survey-preflight-poison-") as tmp:
            root = Path(tmp)
            (root / "json.py").write_text(
                'raise RuntimeError("UNTRUSTED_JSON_IMPORTED")\n',
                encoding="utf-8",
            )
            request = root / "request.json"
            request.write_text(
                json.dumps({"reviewed_main_sha": "a" * 40}),
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable,
                    "-I",
                    "-c",
                    (
                        'import json,sys; '
                        'print(json.load(open(sys.argv[1], encoding="utf-8"))'
                        '["reviewed_main_sha"])'
                    ),
                    str(request),
                ],
                cwd=root,
                text=True,
                capture_output=True,
                check=False,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "a" * 40)
        self.assertNotIn("UNTRUSTED_JSON_IMPORTED", result.stderr)

    def test_executor_uses_reviewed_main_runtime_and_exact_module_cli_smoke(self) -> None:
        root = Path(".").resolve()
        workflow = (
            root / ".github/workflows/survey-production-v2-operator-bridge.yml"
        ).read_text(encoding="utf-8")

        self.assertIn(
            'git archive "$REVIEWED_MAIN_SHA" scripts | tar -x -C "$trusted_runtime"',
            workflow,
        )
        self.assertIn('cd "$TRUSTED_CORE_RUNTIME"', workflow)
        self.assertIn("python -m scripts.survey_core_execution_bridge_v2", workflow)
        self.assertIn('--repo-root "$GITHUB_WORKSPACE"', workflow)
        self.assertIn('--request "$GITHUB_WORKSPACE/$REQUEST_PATH"', workflow)
        self.assertIn(
            'python -I -m pip install -r "$GITHUB_WORKSPACE/config/survey-production-v2-requirements.txt"',
            workflow,
        )
        self.assertGreaterEqual(
            workflow.count("python -I -c 'import json,sys;"),
            3,
        )

        poison = root / "json.py"
        self.assertFalse(poison.exists(), "CLI smoke requires no pre-existing top-level json.py")
        sources = root / "sources"
        sources.mkdir(parents=True, exist_ok=True)

        with tempfile.TemporaryDirectory(prefix="survey-trusted-runtime-") as runtime_tmp, \
             tempfile.TemporaryDirectory(dir=sources, prefix="operator-cli-smoke-") as request_tmp:
            trusted_runtime = Path(runtime_tmp)
            shutil.copytree(root / "scripts", trusted_runtime / "scripts")
            request_path = Path(request_tmp) / "request.json"
            request_path.write_text(
                json.dumps(
                    {
                        "schema_version": "2.0-rc1",
                        "request_id": "cli-smoke",
                        "issue_id": "CLI-SMOKE",
                        "source_root": "sources/CLI-SMOKE",
                        "work_branch": "test/operator-cli-smoke",
                        "reviewed_main_sha": "a" * 40,
                        "recorded_at": "2026-08-24T00:00:00Z",
                        "operation": {
                            "kind": "INITIALIZE_WEEKLY",
                            "target_gate": "ARCHITECTURE_REVIEW",
                            "execution_record": {
                                "session_id": "cli-smoke",
                                "reviewed_main_sha": "a" * 40,
                                "objective": "Exercise exact workflow module startup.",
                                "requested_stop": "ARCHITECTURE_REVIEW",
                            },
                        },
                    }
                ),
                encoding="utf-8",
            )
            poison.write_text(
                'raise RuntimeError("UNTRUSTED_JSON_IMPORTED")\n',
                encoding="utf-8",
            )
            env = os.environ.copy()
            env.pop("PYTHONPATH", None)
            env.pop("PYTHONHOME", None)
            try:
                result = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "scripts.survey_core_execution_bridge_v2",
                        "--repo-root",
                        str(root),
                        "--request",
                        str(request_path),
                        "--event-sha",
                        "b" * 40,
                        "--ref-name",
                        "test/operator-cli-smoke",
                    ],
                    cwd=trusted_runtime,
                    env=env,
                    text=True,
                    capture_output=True,
                    check=False,
                )
            finally:
                poison.unlink(missing_ok=True)

        self.assertEqual(result.returncode, 2)
        self.assertIn("operator request must use canonical path", result.stderr)
        self.assertNotIn("UNTRUSTED_JSON_IMPORTED", result.stderr)
        self.assertNotIn("ModuleNotFoundError", result.stderr)


if __name__ == "__main__":
    unittest.main()
