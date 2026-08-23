from __future__ import annotations

import unittest
from pathlib import Path

from scripts import survey_schema_v2 as schema_gate


class SurveyCoreExecutionBridgeV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(".").resolve()
        cls.schema = cls.root / "schemas/operator-execution-request-v2.schema.json"

    def test_request_schema_accepts_bounded_weekly_initialization(self) -> None:
        payload = {
            "schema_version": "2.0-rc1",
            "request_id": "w33-init-r2",
            "issue_id": "2026-W33",
            "work_branch": "weekly/2026-W33-v2-work",
            "recorded_at": "2026-08-23T13:30:00Z",
            "operation": {
                "kind": "INITIALIZE_WEEKLY",
                "target_gate": "ARCHITECTURE_REVIEW",
                "execution_record": {
                    "session_id": "postmerge-r2",
                    "reviewed_main_sha": "a" * 40,
                    "objective": "Run clean W33 production validation to Architecture Review.",
                    "requested_stop": "ARCHITECTURE_REVIEW",
                },
            },
        }
        schema_gate.validate_instance(payload, self.schema, label="Operator request")

    def test_request_schema_rejects_arbitrary_command_surface(self) -> None:
        payload = {
            "schema_version": "2.0-rc1",
            "request_id": "bad-command",
            "issue_id": "2026-W33",
            "work_branch": "weekly/2026-W33-v2-work",
            "recorded_at": "2026-08-23T13:30:00Z",
            "operation": {
                "kind": "RUN_COMMAND",
                "command": "python -c 'print(1)'",
            },
        }
        with self.assertRaises(ValueError):
            schema_gate.validate_instance(payload, self.schema, label="Operator request")

    def test_advance_request_cannot_claim_deterministic_agent_review(self) -> None:
        payload = {
            "schema_version": "2.0-rc1",
            "request_id": "w33-discovery-r2",
            "issue_id": "2026-W33",
            "work_branch": "weekly/2026-W33-v2-work",
            "recorded_at": "2026-08-23T13:40:00Z",
            "operation": {
                "kind": "ADVANCE_STAGE",
                "expected_from_state": "ISSUE_INITIALIZED",
                "state_path": "sources/2026-W33/production-state.json",
                "artifacts": [
                    {
                        "name": "discovery-acceptance",
                        "path": "sources/2026-W33/discovery/discovery-accepted-v2.json",
                    }
                ],
                "agent_reviews": [
                    {
                        "check_id": "FAKE_DETERMINISTIC_PASS",
                        "kind": "DETERMINISTIC",
                        "executor": "ChatGPT",
                        "evidence": "not allowed",
                    }
                ],
                "summary": "Adopt validated Discovery.",
            },
        }
        with self.assertRaises(ValueError):
            schema_gate.validate_instance(payload, self.schema, label="Operator request")

    def test_workflow_requires_request_only_commit_and_edition_local_writes(self) -> None:
        text = (self.root / ".github/workflows/survey-production-v2-operator-bridge.yml").read_text(encoding="utf-8")
        self.assertIn("sources/*/execution/requests/*.json", text)
        self.assertIn("contents: write", text)
        self.assertIn("github.actor != 'github-actions[bot]'", text)
        self.assertIn("--diff-filter=A", text)
        self.assertIn("Operator request commit must contain only the immutable request file", text)
        self.assertIn("Bridge attempted write outside edition source root", text)
        self.assertIn("Bridge must not mutate immutable request authority", text)
        self.assertIn("survey_core_execution_bridge_v2.py", text)
        self.assertNotIn("workflow_dispatch", text)

    def test_bridge_has_no_request_driven_shell_or_subprocess_surface(self) -> None:
        text = (self.root / "scripts/survey_core_execution_bridge_v2.py").read_text(encoding="utf-8")
        self.assertNotIn("import subprocess", text)
        self.assertNotIn("os.system", text)
        self.assertNotIn("shell=True", text)
        self.assertIn('"INITIALIZE_WEEKLY"', text)
        self.assertIn('"INITIALIZE_THEMATIC"', text)
        self.assertIn('"ADVANCE_STAGE"', text)
        self.assertNotIn("approve_architecture(", text)
        self.assertNotIn("approve_publication_preview(", text)


if __name__ == "__main__":
    unittest.main()
