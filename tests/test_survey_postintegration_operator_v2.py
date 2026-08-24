from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import survey_core_execution_bridge_v2 as bridge
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate


class SurveyPostIntegrationOperatorRegressionV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(".").resolve()
        cls.request_schema = cls.root / "schemas/operator-execution-request-v2.schema.json"

    def _canonical_scope_fixture(self, source_root: Path, issue_id: str) -> Path:
        planning = source_root / "planning-authority.md"
        planning.write_text(f"# Planning\n\n## {issue_id}-PLAN\nCanonical thematic scope.\n", encoding="utf-8")
        scope = source_root / "research-scope-v2.json"
        core.write_json(scope, {
            "schema_version": "2.0-rc1",
            "issue_id": issue_id,
            "planning_authority": {
                "path": planning.relative_to(self.root).as_posix(),
                "entry": f"{issue_id}-PLAN",
                "sha256": core.sha256_file(planning),
            },
            "question": "Can canonical thematic scope materialization initialize through the operator bridge?",
            "inclusion": ["canonical thematic scope"],
            "exclusion": ["unrelated material"],
            "scope_dimensions": ["lineage"],
            "initial_obligations": [{
                "obligation_id": "scope:lineage",
                "dimension": "lineage",
                "description": "Establish the thematic lineage from evidence.",
            }],
            "materialized_by": "ChatGPT fixture",
            "materialized_at": "2026-08-25T00:00:00+09:00",
        })
        return scope

    def test_canonical_thematic_scope_materialization_initializes_with_request_temporal_identity(self) -> None:
        cfg = core.load_json(self.root / core.DEFAULT_CONFIG)
        current_head = core.repository_commit_sha(self.root)
        sources = self.root / "sources"
        sources.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=sources, prefix="postintegration-thematic-") as temp:
            source_root = Path(temp)
            source_rel = source_root.relative_to(self.root).as_posix()
            issue_id = "POSTINT-THEMATIC"
            branch = "test/postintegration-thematic"
            scope = self._canonical_scope_fixture(source_root, issue_id)
            request = {
                "schema_version": "2.0-rc1",
                "request_id": "canonical-thematic-init",
                "issue_id": issue_id,
                "source_root": source_rel,
                "work_branch": branch,
                "reviewed_main_sha": current_head,
                "recorded_at": "2026-08-25T00:10:00+09:00",
                "operation": {
                    "kind": "INITIALIZE_THEMATIC",
                    "target_gate": "ARCHITECTURE_REVIEW",
                    "spec_path": scope.relative_to(self.root).as_posix(),
                    "temporal_mode": "OPEN_HISTORY_AS_OF",
                    "survey_root": f"surveys/special/{issue_id}",
                    "execution_record": {
                        "session_id": "postintegration-thematic",
                        "reviewed_main_sha": current_head,
                        "objective": "Exercise canonical thematic materialization through the trusted bridge contract.",
                        "requested_stop": "ARCHITECTURE_REVIEW",
                    },
                },
            }
            schema_gate.validate_instance(request, self.request_schema, label="Operator request")
            request_path = source_root / "execution/requests/canonical-thematic-init.json"
            core.write_json(request_path, request)
            result = bridge.execute_request(self.root, request_path, event_sha=current_head, ref_name=branch)
            self.assertEqual(result["lifecycle_state"], "ISSUE_INITIALIZED")
            profile = core.load_json(source_root / cfg["state_authority"]["profile_filename"])
            self.assertEqual(profile["research_profile"], "THEMATIC")
            self.assertEqual(profile["publication_profile"], "LONGFORM_SPECIAL")
            self.assertEqual(profile["research_scope"]["temporal_policy"], {
                "mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-08-24T15:10:00Z",
            })
            self.assertEqual(profile["research_scope"]["scope_dimensions"], ["lineage"])
            self.assertEqual(profile["research_scope"]["initial_obligations"][0]["obligation_id"], "scope:lineage")
            self.assertEqual(profile["paths"]["source_root"], source_rel)
            self.assertEqual(profile["paths"]["survey_root"], f"surveys/special/{issue_id}")
            self.assertEqual(profile["paths"]["work_branch"], branch)

    def test_canonical_thematic_scope_requires_explicit_temporal_mode(self) -> None:
        cfg = core.load_json(self.root / core.DEFAULT_CONFIG)
        current_head = core.repository_commit_sha(self.root)
        sources = self.root / "sources"
        sources.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=sources, prefix="postintegration-thematic-missing-mode-") as temp:
            source_root = Path(temp)
            source_rel = source_root.relative_to(self.root).as_posix()
            issue_id = "POSTINT-NO-MODE"
            branch = "test/postintegration-no-mode"
            scope = self._canonical_scope_fixture(source_root, issue_id)
            request = {
                "schema_version": "2.0-rc1",
                "request_id": "canonical-thematic-no-mode",
                "issue_id": issue_id,
                "source_root": source_rel,
                "work_branch": branch,
                "reviewed_main_sha": current_head,
                "recorded_at": "2026-08-25T00:20:00+09:00",
                "operation": {
                    "kind": "INITIALIZE_THEMATIC",
                    "target_gate": "ARCHITECTURE_REVIEW",
                    "spec_path": scope.relative_to(self.root).as_posix(),
                    "execution_record": {
                        "session_id": "postintegration-no-mode",
                        "reviewed_main_sha": current_head,
                        "objective": "Require explicit temporal identity for canonical scope materialization.",
                        "requested_stop": "ARCHITECTURE_REVIEW",
                    },
                },
            }
            schema_gate.validate_instance(request, self.request_schema, label="Operator request")
            request_path = source_root / "execution/requests/canonical-thematic-no-mode.json"
            core.write_json(request_path, request)
            with self.assertRaisesRegex(ValueError, "requires operation.temporal_mode"):
                bridge.execute_request(self.root, request_path, event_sha=current_head, ref_name=branch)
            self.assertFalse((source_root / cfg["state_authority"]["profile_filename"]).exists())

    def test_raw_thematic_spec_cannot_silently_ignore_request_survey_root(self) -> None:
        cfg = core.load_json(self.root / core.DEFAULT_CONFIG)
        current_head = core.repository_commit_sha(self.root)
        sources = self.root / "sources"
        sources.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=sources, prefix="postintegration-raw-root-") as temp:
            source_root = Path(temp)
            source_rel = source_root.relative_to(self.root).as_posix()
            issue_id = "POSTINT-RAW-ROOT"
            branch = "test/postintegration-raw-root"
            raw_spec = source_root / "raw-thematic-spec.json"
            core.write_json(raw_spec, {
                "issue_id": issue_id,
                "question": "Can raw thematic request identity fail closed?",
                "temporal_mode": "OPEN_HISTORY_AS_OF",
                "as_of": "2026-08-25T00:30:00+09:00",
                "scope_dimensions": ["identity"],
                "source_root": source_rel,
                "survey_root": f"surveys/special/{issue_id}",
                "work_branch": branch,
            })
            request = {
                "schema_version": "2.0-rc1",
                "request_id": "raw-thematic-root-drift",
                "issue_id": issue_id,
                "source_root": source_rel,
                "work_branch": branch,
                "reviewed_main_sha": current_head,
                "recorded_at": "2026-08-25T00:30:00+09:00",
                "operation": {
                    "kind": "INITIALIZE_THEMATIC",
                    "target_gate": "ARCHITECTURE_REVIEW",
                    "spec_path": raw_spec.relative_to(self.root).as_posix(),
                    "temporal_mode": "OPEN_HISTORY_AS_OF",
                    "survey_root": "surveys/special/DIFFERENT",
                    "execution_record": {
                        "session_id": "postintegration-raw-root",
                        "reviewed_main_sha": current_head,
                        "objective": "Reject request/raw survey-root disagreement.",
                        "requested_stop": "ARCHITECTURE_REVIEW",
                    },
                },
            }
            schema_gate.validate_instance(request, self.request_schema, label="Operator request")
            request_path = source_root / "execution/requests/raw-thematic-root-drift.json"
            core.write_json(request_path, request)
            with self.assertRaisesRegex(ValueError, "survey_root differs from request"):
                bridge.execute_request(self.root, request_path, event_sha=current_head, ref_name=branch)
            self.assertFalse((source_root / cfg["state_authority"]["profile_filename"]).exists())

    def test_default_branch_operator_workflow_has_connector_native_pr_transport_without_new_workflow(self) -> None:
        workflow = (self.root / ".github/workflows/survey-production-v2-operator-bridge.yml").read_text(encoding="utf-8")
        self.assertIn("issue_comment:", workflow)
        self.assertIn("pull_request_target:", workflow)
        self.assertIn("github.event.pull_request.base.ref == 'main'", workflow)
        self.assertIn("github.event.pull_request.head.repo.full_name == github.repository", workflow)
        self.assertIn("Survey Core operator transport:", workflow)
        self.assertIn("Operator transport PR head branch must equal request work_branch", workflow)
        self.assertIn("Operator request commit must contain only the immutable request file", workflow)
        self.assertIn("Shared Core or contract authority drifted from reviewed_main_sha", workflow)
        self.assertNotIn("workflow_run:", workflow)
        self.assertNotIn("on:\n  push:", workflow)
        workflows = sorted((self.root / ".github/workflows").glob("*.yml"))
        self.assertEqual(len(workflows), 7)

    def test_postintegration_amendment_is_bound_into_pipeline_contract(self) -> None:
        cfg = core.load_json(self.root / core.DEFAULT_CONFIG)
        self.assertEqual(
            cfg["orchestrator_version"],
            "survey-production-core-v2/0.15-postintegration-transport-thematic",
        )
        self.assertIn(
            "docs/survey-production-core-v2-postintegration-amendment.md",
            cfg["contract_files"]["pipeline"],
        )


if __name__ == "__main__":
    unittest.main()
