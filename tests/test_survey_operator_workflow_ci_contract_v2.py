from __future__ import annotations

import json
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


if __name__ == "__main__":
    unittest.main()
