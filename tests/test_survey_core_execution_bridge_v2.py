from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import survey_core_execution_bridge_v2 as bridge
from scripts import survey_schema_v2 as schema_gate


class SurveyCoreExecutionBridgeV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(".").resolve()
        cls.schema = cls.root / "schemas/operator-execution-request-v2.schema.json"

    def weekly_request(self) -> dict:
        return {
            "schema_version": "2.0-rc1",
            "request_id": "w33-init-r2",
            "issue_id": "2026-W33",
            "source_root": "sources/2026-W33",
            "work_branch": "weekly/2026-W33-v2-work",
            "reviewed_main_sha": "a" * 40,
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

    def test_request_schema_accepts_bounded_weekly_initialization(self) -> None:
        schema_gate.validate_instance(self.weekly_request(), self.schema, label="Operator request")

    def test_request_schema_requires_reviewed_main_for_every_operation(self) -> None:
        payload = self.weekly_request()
        del payload["reviewed_main_sha"]
        with self.assertRaises(ValueError):
            schema_gate.validate_instance(payload, self.schema, label="Operator request")

        payload = self.weekly_request()
        payload["reviewed_main_sha"] = "not-a-sha"
        with self.assertRaises(ValueError):
            schema_gate.validate_instance(payload, self.schema, label="Operator request")

    def test_request_schema_accepts_profile_bound_nested_source_root(self) -> None:
        payload = self.weekly_request()
        payload["request_id"] = "thematic-init-r2"
        payload["issue_id"] = "SP001"
        payload["source_root"] = "sources/specials/SP001"
        payload["work_branch"] = "production/thematic/SP001"
        payload["reviewed_main_sha"] = "b" * 40
        payload["operation"] = {
            "kind": "INITIALIZE_THEMATIC",
            "target_gate": "ARCHITECTURE_REVIEW",
            "spec_path": "sources/specials/SP001/research-scope-v2.json",
            "execution_record": {
                "session_id": "postmerge-r2",
                "reviewed_main_sha": "b" * 40,
                "objective": "Run Thematic production to Architecture Review.",
                "requested_stop": "ARCHITECTURE_REVIEW",
            },
        }
        schema_gate.validate_instance(payload, self.schema, label="Operator request")

    def test_source_root_must_stay_under_sources(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            request = {"source_root": "sources/specials/SP001"}
            self.assertEqual(
                bridge._source_root(root, request),
                root / "sources/specials/SP001",
            )
            with self.assertRaises(ValueError):
                bridge._source_root(root, {"source_root": "surveys/SP001"})

    def test_request_schema_rejects_arbitrary_command_surface(self) -> None:
        payload = self.weekly_request()
        payload["request_id"] = "bad-command"
        payload["operation"] = {
            "kind": "RUN_COMMAND",
            "command": "python -c 'print(1)'",
        }
        with self.assertRaises(ValueError):
            schema_gate.validate_instance(payload, self.schema, label="Operator request")

    def test_advance_request_cannot_claim_deterministic_agent_review(self) -> None:
        payload = self.weekly_request()
        payload["request_id"] = "w33-discovery-r2"
        payload["recorded_at"] = "2026-08-23T13:40:00Z"
        payload["operation"] = {
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
        }
        with self.assertRaises(ValueError):
            schema_gate.validate_instance(payload, self.schema, label="Operator request")

    def test_workflow_requires_request_only_commit_profile_bound_writes_and_reviewed_main_preflight(self) -> None:
        text = (self.root / ".github/workflows/survey-production-v2-operator-bridge.yml").read_text(encoding="utf-8")
        self.assertIn("sources/**/execution/requests/*.json", text)
        self.assertIn("- '!main'", text)
        self.assertIn("fetch-depth: 0", text)
        self.assertIn("contents: write", text)
        self.assertIn("github.actor != 'github-actions[bot]'", text)
        self.assertIn("--diff-filter=A", text)
        self.assertIn("Operator request commit must contain only the immutable request file", text)
        self.assertIn("Verify reviewed-main Core baseline", text)
        self.assertIn('reviewed_main_sha', text)
        self.assertIn("git merge-base --is-ancestor", text)
        self.assertIn("implementation_control_roots", text)
        self.assertIn("contract_files", text)
        self.assertIn("Shared Core or contract authority drifted from reviewed_main_sha", text)
        self.assertIn("Initialization execution record reviewed_main_sha must equal request reviewed_main_sha", text)
        self.assertIn("operator-bridge-result.json", text)
        self.assertIn("Bridge attempted write outside edition source root", text)
        self.assertIn("Bridge must not mutate immutable request authority", text)
        self.assertIn("survey_core_execution_bridge_v2.py", text)
        self.assertNotIn("workflow_dispatch", text)
        self.assertNotIn('source_root="sources/$issue_id"', text)

    def test_bridge_has_no_request_driven_shell_or_subprocess_surface(self) -> None:
        text = (self.root / "scripts/survey_core_execution_bridge_v2.py").read_text(encoding="utf-8")
        self.assertNotIn("import subprocess", text)
        self.assertNotIn("os.system", text)
        self.assertNotIn("shell=True", text)
        self.assertIn('"INITIALIZE_WEEKLY"', text)
        self.assertIn('"INITIALIZE_THEMATIC"', text)
        self.assertIn('"ADVANCE_STAGE"', text)
        self.assertIn('ref_name == "main"', text)
        self.assertIn('paths.get("source_root") != request["source_root"]', text)
        self.assertNotIn("approve_architecture(", text)
        self.assertNotIn("approve_publication_preview(", text)


if __name__ == "__main__":
    unittest.main()
