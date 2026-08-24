from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts import survey_core_execution_bridge_v2 as bridge
from scripts import survey_discovery_v2 as discovery
from scripts import survey_period_v2 as period
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_x_intake_v2 as x_intake


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

    def retrospective_request(self) -> dict:
        return {
            "schema_version": "2.0-rc1",
            "request_id": "period-init-r1",
            "issue_id": "SP-2024-H1",
            "source_root": "sources/SP-2024-H1",
            "work_branch": "special/2024-H1-v2-work",
            "reviewed_main_sha": "c" * 40,
            "recorded_at": "2026-08-23T14:00:00Z",
            "operation": {
                "kind": "INITIALIZE_RETROSPECTIVE",
                "target_gate": "ARCHITECTURE_REVIEW",
                "special_slug": "2024-H1",
                "execution_record": {
                    "session_id": "period-postmerge-r1",
                    "reviewed_main_sha": "c" * 40,
                    "objective": "Run configured Retrospective Period production to Architecture Review.",
                    "requested_stop": "ARCHITECTURE_REVIEW",
                },
            },
        }

    def advance_request(self) -> dict:
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
            "agent_reviews": [],
            "summary": "Adopt validated Discovery.",
        }
        return payload

    def test_request_schema_accepts_bounded_weekly_initialization(self) -> None:
        schema_gate.validate_instance(self.weekly_request(), self.schema, label="Operator request")

    def test_request_schema_accepts_configured_retrospective_initialization(self) -> None:
        schema_gate.validate_instance(self.retrospective_request(), self.schema, label="Operator request")

    def test_retrospective_request_identity_matches_existing_period_builder(self) -> None:
        request = self.retrospective_request()
        cfg = core.load_json(self.root / core.DEFAULT_CONFIG)
        recorded_at = core.parse_instant(request["recorded_at"])
        spec = period.resolve_configured_period(
            self.root,
            request["operation"]["special_slug"],
            recorded_at,
        )
        profile = period.period_profile(self.root, cfg, spec)

        self.assertEqual(profile["research_profile"], "RETROSPECTIVE_PERIOD")
        self.assertEqual(profile["publication_profile"], "LONGFORM_SPECIAL")
        self.assertEqual(profile["issue_id"], request["issue_id"])
        self.assertEqual(profile["paths"]["source_root"], request["source_root"])
        self.assertEqual(profile["paths"]["work_branch"], request["work_branch"])

    def test_request_schema_requires_reviewed_main_for_every_operation(self) -> None:
        for payload in (self.weekly_request(), self.retrospective_request(), self.advance_request()):
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
        payload = self.advance_request()
        payload["operation"]["agent_reviews"] = [
            {
                "check_id": "FAKE_DETERMINISTIC_PASS",
                "kind": "DETERMINISTIC",
                "executor": "ChatGPT",
                "evidence": "not allowed",
            }
        ]
        with self.assertRaises(ValueError):
            schema_gate.validate_instance(payload, self.schema, label="Operator request")

    def test_operator_transport_has_default_branch_trust_root(self) -> None:
        workflow = (self.root / ".github/workflows/survey-production-v2-operator-bridge.yml").read_text(encoding="utf-8")
        contract_ci = (self.root / ".github/workflows/pipeline-contract-tests.yml").read_text(encoding="utf-8")

        # issue_comment is a default-branch event. No work-branch workflow is
        # needed to bootstrap trust, so untrusted branch YAML cannot grant
        # itself write authority before admission.
        self.assertIn("issue_comment:", workflow)
        self.assertIn("types:\n      - created", workflow)
        self.assertIn("OPERATOR_QUEUE_ISSUE: '448'", workflow)
        self.assertIn("/survey-core-execute ", workflow)
        self.assertIn("github.event.issue.number == 448", workflow)
        self.assertIn("author_association", workflow)
        self.assertNotIn("workflow_run:", workflow)
        self.assertNotIn("on:\n  push:", workflow)

        # Trusted preflight treats the supplied work-branch head as data,
        # proves it is the exact current branch head and a request-only commit,
        # resolves protected paths from reviewed main, and only then admits a
        # write-capable dependent job.
        self.assertIn("Parse exact operator command", workflow)
        self.assertIn("Operator request commit must contain only the immutable request file", workflow)
        self.assertIn("Operator request commit must be the exact current canonical work-branch head", workflow)
        self.assertIn("reviewed_main_sha is not an ancestor of current main", workflow)
        self.assertIn("Human Gate request must bind reviewed_repository_commit_sha to the request-only commit parent", workflow)
        self.assertIn('git", "show", f"{reviewed}:config/survey-production-v2.json"', workflow)
        self.assertIn("Shared Core or contract authority drifted from reviewed_main_sha", workflow)
        self.assertIn("needs: operator-preflight", workflow)
        self.assertIn("permissions:\n      contents: write", workflow)
        self.assertIn("Canonical work branch moved after trusted preflight", workflow)
        self.assertIn("survey_core_execution_bridge_v2.py", workflow)
        self.assertIn("Bridge attempted write outside edition source root", workflow)
        self.assertIn("Bridge must not mutate immutable request authority", workflow)
        self.assertIn("--force-with-lease", workflow)
        self.assertLess(workflow.index("operator-preflight:"), workflow.index("operator-execute:"))

        # Pipeline contract CI remains independent validation and is not the
        # production trust bootstrap or write-capable executor.
        self.assertNotIn("workflow_run:", contract_ci)
        self.assertNotIn("operator-preflight:", contract_ci)
        self.assertNotIn("operator-execute:", contract_ci)
        self.assertNotIn("contents: write", contract_ci)

    def test_bridge_has_no_request_driven_shell_or_subprocess_surface(self) -> None:
        text = (self.root / "scripts/survey_core_execution_bridge_v2.py").read_text(encoding="utf-8")
        self.assertNotIn("import subprocess", text)
        self.assertNotIn("os.system", text)
        self.assertNotIn("shell=True", text)
        self.assertIn('"INITIALIZE_WEEKLY"', text)
        self.assertIn('"INITIALIZE_RETROSPECTIVE"', text)
        self.assertIn('"INITIALIZE_THEMATIC"', text)
        self.assertIn('"ADVANCE_STAGE"', text)
        self.assertIn("period.resolve_configured_period", text)
        self.assertIn("period.period_profile", text)
        self.assertIn('ref_name == "main"', text)
        self.assertIn('paths.get("source_root") != request["source_root"]', text)
        self.assertNotIn("approve_architecture(", text)
        self.assertNotIn("approve_publication_preview(", text)

    def test_current_bridge_authority_names_all_initialization_profiles(self) -> None:
        inventory = (self.root / "docs/survey-production-core-v2-workflow-responsibility-inventory.md").read_text(encoding="utf-8")
        policy = (self.root / "docs/survey-production-core-v2-github-actions-policy.md").read_text(encoding="utf-8")

        self.assertIn("INITIALIZE_WEEKLY", inventory)
        self.assertIn("INITIALIZE_RETROSPECTIVE", inventory)
        self.assertIn("INITIALIZE_THEMATIC", inventory)
        self.assertIn("existing `survey_period_v2`", inventory)

        self.assertIn("Weekly", policy)
        self.assertIn("configured Retrospective", policy)
        self.assertIn("Thematic", policy)
        self.assertIn("existing `survey_period_v2`", policy)

    def test_bridge_executes_thematic_init_then_discovery_advance_end_to_end(self) -> None:
        cfg = core.load_json(self.root / core.DEFAULT_CONFIG)
        current_head = core.repository_commit_sha(self.root)
        branch = "test/bridge-e2e"
        issue_id = "BRIDGE-E2E"

        sources_root = self.root / "sources"
        sources_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=sources_root) as raw_temp:
            source_root = Path(raw_temp)
            source_rel = source_root.relative_to(self.root).as_posix()
            survey_rel = f"{source_rel}/survey"

            spec_path = source_root / "research-scope-v2.json"
            core.write_json(
                spec_path,
                {
                    "issue_id": issue_id,
                    "question": "Can the operator bridge execute canonical Core glue end to end?",
                    "temporal_mode": "OPEN_HISTORY_AS_OF",
                    "as_of": "2026-08-23T13:00:00Z",
                    "scope_dimensions": ["bridge execution"],
                    "source_root": source_rel,
                    "survey_root": survey_rel,
                    "work_branch": branch,
                },
            )

            init_request = {
                "schema_version": "2.0-rc1",
                "request_id": "bridge-e2e-init",
                "issue_id": issue_id,
                "source_root": source_rel,
                "work_branch": branch,
                "reviewed_main_sha": current_head,
                "recorded_at": "2026-08-23T14:00:00Z",
                "operation": {
                    "kind": "INITIALIZE_THEMATIC",
                    "target_gate": "ARCHITECTURE_REVIEW",
                    "spec_path": spec_path.relative_to(self.root).as_posix(),
                    "execution_record": {
                        "session_id": "bridge-e2e",
                        "reviewed_main_sha": current_head,
                        "objective": "Exercise bridge initialization and one lifecycle transition.",
                        "requested_stop": "ARCHITECTURE_REVIEW",
                    },
                },
            }
            init_path = source_root / "execution/requests/bridge-e2e-init.json"
            core.write_json(init_path, init_request)
            init_result = bridge.execute_request(
                self.root,
                init_path,
                event_sha=current_head,
                ref_name=branch,
            )
            self.assertEqual(init_result["lifecycle_state"], "ISSUE_INITIALIZED")

            profile_path = source_root / cfg["state_authority"]["profile_filename"]
            state_path = source_root / cfg["state_authority"]["authoritative_filename"]
            self.assertTrue(profile_path.is_file())
            self.assertTrue(state_path.is_file())
            self.assertTrue((source_root / "execution/index.md").is_file())
            self.assertTrue((source_root / "execution/bridge-runs/bridge-e2e-init/receipt.json").is_file())

            x_manifest = x_intake.build_manifest(
                self.root,
                cfg,
                profile_path,
                {
                    "decision": "NOT_REQUIRED",
                    "rationale": "The bridge glue fixture does not require community observation.",
                    "series_context": None,
                    "runs": [],
                },
            )
            raw_path = source_root / "raw/fixture.txt"
            raw_path.parent.mkdir(parents=True, exist_ok=True)
            raw_path.write_text("bridge fixture raw\n", encoding="utf-8")
            discovery_path = source_root / "discovery/discovery.jsonl"
            discovery_path.parent.mkdir(parents=True, exist_ok=True)
            discovery_record = {
                "schema_version": "2.0-rc1",
                "issue_id": issue_id,
                "discovery_id": "bridge-source",
                "provenance": {
                    "origin": "BASE",
                    "research_pass": 0,
                    "parent_refs": [],
                    "obligation_ids": ["scope:01"],
                    "reason": "End-to-end bridge fixture.",
                },
                "source": {
                    "source_type": "PRIMARY",
                    "collector_id": "bridge-fixture",
                    "collector_run_id": "bridge-fixture-r1",
                    "observed_at": "2026-08-23T14:05:00Z",
                    "title": "Bridge fixture",
                    "locator": "https://example.invalid/bridge-fixture",
                    "raw_paths": [raw_path.relative_to(self.root).as_posix()],
                    "published_at": "2026-08-23T12:00:00Z",
                    "summary_text": "Fixture source for deterministic bridge integration.",
                    "metadata": {},
                },
            }
            discovery_path.write_text(json.dumps(discovery_record) + "\n", encoding="utf-8")
            acceptance_path = source_root / "discovery/discovery-accepted-v2.json"
            discovery.build_acceptance(
                self.root,
                discovery_path,
                x_manifest,
                issue_id,
                acceptance_path,
            )

            advance_request = {
                "schema_version": "2.0-rc1",
                "request_id": "bridge-e2e-discovery",
                "issue_id": issue_id,
                "source_root": source_rel,
                "work_branch": branch,
                "reviewed_main_sha": current_head,
                "recorded_at": "2026-08-23T14:10:00Z",
                "operation": {
                    "kind": "ADVANCE_STAGE",
                    "expected_from_state": "ISSUE_INITIALIZED",
                    "state_path": state_path.relative_to(self.root).as_posix(),
                    "artifacts": [
                        {
                            "name": "discovery-acceptance",
                            "path": acceptance_path.relative_to(self.root).as_posix(),
                        }
                    ],
                    "agent_reviews": [],
                    "summary": "Adopt the validated Discovery fixture.",
                },
            }
            advance_path = source_root / "execution/requests/bridge-e2e-discovery.json"
            core.write_json(advance_path, advance_request)
            advance_result = bridge.execute_request(
                self.root,
                advance_path,
                event_sha=current_head,
                ref_name=branch,
            )
            self.assertEqual(advance_result["lifecycle_state"], "DISCOVERY_COLLECTED")
            self.assertIsNone(advance_result["terminal_reason"])

            state = core.load_json(state_path)
            self.assertEqual(state["lifecycle_state"], "DISCOVERY_COLLECTED")
            self.assertEqual(state["machine_checkpoints"]["discovery"], "passed")
            self.assertEqual(state["next_action"], "stage:screening")
            self.assertTrue((source_root / "orchestration/v2/checkpoints/ISSUE_INITIALIZED.json").is_file())
            self.assertTrue((source_root / "execution/bridge-runs/bridge-e2e-discovery/receipt.json").is_file())


if __name__ == "__main__":
    unittest.main()
