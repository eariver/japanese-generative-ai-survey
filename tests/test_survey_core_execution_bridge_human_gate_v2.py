from __future__ import annotations

import unittest
from pathlib import Path

from scripts import survey_core_execution_bridge_v2 as bridge
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate
from tests.test_survey_human_gate_v2 import SurveyHumanGateV2Tests


class SurveyCoreExecutionBridgeHumanGateV2Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(".").resolve()
        cls.schema = cls.root / "schemas/operator-execution-request-v2.schema.json"

    def request(self, operation: dict, request_id: str) -> dict:
        return {
            "schema_version": "2.0-rc1",
            "request_id": request_id,
            "issue_id": "SP001",
            "source_root": "sources/SP001",
            "work_branch": "special/SP001-v2-work",
            "reviewed_main_sha": "a" * 40,
            "recorded_at": "2026-08-24T00:30:00Z",
            "operation": operation,
        }

    def approval(self, kind: str) -> dict:
        return {
            "kind": kind,
            "state_path": "sources/SP001/production-state.json",
            "expected_revision": 1,
            "reviewed_by": "human-reviewer",
            "reviewed_at": "2026-08-24T00:29:00Z",
            "review_reference": "chat:human-gate:r1",
        }

    def revision(self, kind: str, boundary: str) -> dict:
        return {
            **self.approval(kind),
            "regeneration_boundary": boundary,
            "requested_changes": "Revise the reviewed candidate and present r2.",
        }

    def _fixture(self) -> SurveyHumanGateV2Tests:
        SurveyHumanGateV2Tests.setUpClass()
        fixture = SurveyHumanGateV2Tests(
            methodName="test_architecture_request_changes_regenerates_r2_then_approves"
        )
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        return fixture

    def _execute(
        self,
        fixture: SurveyHumanGateV2Tests,
        request_id: str,
        operation: dict,
        *,
        recorded_at: str,
    ) -> dict:
        request = {
            "schema_version": "2.0-rc1",
            "request_id": request_id,
            "issue_id": fixture.issue_id,
            "source_root": fixture.source_rel,
            "work_branch": fixture.branch,
            "reviewed_main_sha": fixture.impl,
            "recorded_at": recorded_at,
            "operation": operation,
        }
        path = fixture.source_root / "execution" / "requests" / f"{request_id}.json"
        core.write_json(path, request)
        return bridge.execute_request(
            fixture.root,
            path,
            event_sha=fixture.impl,
            ref_name=fixture.branch,
        )

    def test_schema_accepts_all_explicit_human_gate_operations(self) -> None:
        operations = [
            ("architecture-approve", self.approval("RECORD_ARCHITECTURE_APPROVAL")),
            (
                "architecture-revise",
                self.revision("REQUEST_ARCHITECTURE_REVISION", "SELECTION_COMPLETE"),
            ),
            (
                "publication-approve",
                self.approval("RECORD_PUBLICATION_PREVIEW_APPROVAL"),
            ),
            (
                "publication-revise",
                self.revision("REQUEST_PUBLICATION_PREVIEW_REVISION", "DRAFT_COMPLETE"),
            ),
        ]
        for request_id, operation in operations:
            with self.subTest(operation=operation["kind"]):
                schema_gate.validate_instance(
                    self.request(operation, request_id),
                    self.schema,
                    label="Human Gate operator request",
                )

    def test_schema_requires_explicit_human_provenance(self) -> None:
        for key in ("expected_revision", "reviewed_by", "reviewed_at", "review_reference"):
            operation = self.approval("RECORD_ARCHITECTURE_APPROVAL")
            del operation[key]
            with self.subTest(key=key), self.assertRaises(ValueError):
                schema_gate.validate_instance(
                    self.request(operation, f"missing-{key}"),
                    self.schema,
                    label="Human Gate operator request",
                )

    def test_schema_rejects_cross_gate_regeneration_boundaries(self) -> None:
        bad_arch = self.revision("REQUEST_ARCHITECTURE_REVISION", "DRAFT_COMPLETE")
        with self.assertRaises(ValueError):
            schema_gate.validate_instance(
                self.request(bad_arch, "bad-architecture-boundary"),
                self.schema,
                label="Human Gate operator request",
            )
        bad_pub = self.revision("REQUEST_PUBLICATION_PREVIEW_REVISION", "SELECTION_COMPLETE")
        with self.assertRaises(ValueError):
            schema_gate.validate_instance(
                self.request(bad_pub, "bad-publication-boundary"),
                self.schema,
                label="Human Gate operator request",
            )

    def test_schema_does_not_offer_generic_human_decision_or_rejection_surface(self) -> None:
        payload = self.request(
            {
                "kind": "EXECUTE_HUMAN_DECISION",
                "decision": "APPROVED",
                "state_path": "sources/SP001/production-state.json",
            },
            "generic-human-decision",
        )
        with self.assertRaises(ValueError):
            schema_gate.validate_instance(payload, self.schema, label="Human Gate operator request")

        payload = self.request(
            {
                "kind": "REJECT_ARCHITECTURE",
                "state_path": "sources/SP001/production-state.json",
            },
            "reject-architecture",
        )
        with self.assertRaises(ValueError):
            schema_gate.validate_instance(payload, self.schema, label="Human Gate operator request")

    def test_bridge_dispatches_only_to_canonical_human_gate_protocol(self) -> None:
        text = (self.root / "scripts/survey_core_execution_bridge_v2.py").read_text(encoding="utf-8")
        self.assertIn("from scripts import survey_human_gate_v2 as human_gate", text)
        for kind in (
            "RECORD_ARCHITECTURE_APPROVAL",
            "REQUEST_ARCHITECTURE_REVISION",
            "RECORD_PUBLICATION_PREVIEW_APPROVAL",
            "REQUEST_PUBLICATION_PREVIEW_REVISION",
        ):
            self.assertIn(f'"{kind}"', text)
        self.assertIn("human_gate.record_architecture_approval", text)
        self.assertIn("human_gate.request_architecture_revision", text)
        self.assertIn("human_gate.record_publication_preview_approval", text)
        self.assertIn("human_gate.request_publication_preview_revision", text)
        self.assertNotIn("import subprocess", text)
        self.assertNotIn("os.system", text)
        self.assertNotIn("shell=True", text)
        self.assertNotIn("EXECUTE_HUMAN_DECISION", text)

    def test_existing_workflow_remains_single_request_only_transport(self) -> None:
        text = (self.root / ".github/workflows/survey-production-v2-operator-bridge.yml").read_text(encoding="utf-8")
        self.assertIn("sources/**/execution/requests/*.json", text)
        self.assertIn("Operator request commit must contain only the immutable request file", text)
        self.assertIn("Verify reviewed-main Core baseline", text)
        self.assertIn("Bridge attempted write outside edition source root", text)
        self.assertIn("Bridge must not mutate immutable request authority", text)
        self.assertIn("github.actor != 'github-actions[bot]'", text)
        self.assertNotIn("workflow_dispatch", text)

    def test_bridge_executes_architecture_revision_then_r2_approval(self) -> None:
        fixture = self._fixture()
        fixture._advance_to_selection()
        fixture._reach_architecture_gate("Architecture bridge r1", "2026-08-24T00:05:00Z")
        checkpoint = (
            fixture.source_root
            / fixture.cfg["state_authority"]["agent_checkpoint_dir"]
            / "SELECTION_COMPLETE.json"
        )
        self.assertTrue(checkpoint.is_file())

        revised = self._execute(
            fixture,
            "bridge-architecture-r1-revise",
            {
                "kind": "REQUEST_ARCHITECTURE_REVISION",
                "state_path": fixture.state_path.relative_to(fixture.root).as_posix(),
                "expected_revision": 1,
                "regeneration_boundary": "SELECTION_COMPLETE",
                "requested_changes": "Clarify the Architecture thesis and present r2.",
                "reviewed_by": "human-reviewer",
                "reviewed_at": "2026-08-24T00:06:00Z",
                "review_reference": "bridge:architecture:r1",
            },
            recorded_at="2026-08-24T00:06:30Z",
        )
        self.assertEqual(revised["lifecycle_state"], "SELECTION_COMPLETE")
        self.assertFalse(checkpoint.exists())
        self.assertIn(checkpoint.relative_to(fixture.root).as_posix(), revised["removed_paths"])

        fixture._reach_architecture_gate("Architecture bridge r2", "2026-08-24T00:07:00Z")
        approved = self._execute(
            fixture,
            "bridge-architecture-r2-approve",
            {
                "kind": "RECORD_ARCHITECTURE_APPROVAL",
                "state_path": fixture.state_path.relative_to(fixture.root).as_posix(),
                "expected_revision": 2,
                "reviewed_by": "human-reviewer",
                "reviewed_at": "2026-08-24T00:08:00Z",
                "review_reference": "bridge:architecture:r2",
            },
            recorded_at="2026-08-24T00:08:30Z",
        )
        self.assertEqual(approved["lifecycle_state"], "ARCHITECTURE_ESTABLISHED")
        self.assertIsNone(approved["terminal_reason"])
        state = core.load_json(fixture.state_path)
        self.assertEqual(state["human_gates"]["architecture_review"], "approved")
        self.assertEqual(state["next_action"], "stage:drafting-synthesis")
        index = core.load_json(
            fixture.source_root / fixture.cfg["state_authority"]["human_review_index_path"]
        )
        rows = [
            (row["gate"], row["revision"], row["decision"])
            for row in index["reviews"]
        ]
        self.assertEqual(
            rows,
            [
                ("ARCHITECTURE_REVIEW", 1, "REQUEST_CHANGES"),
                ("ARCHITECTURE_REVIEW", 2, "APPROVED"),
            ],
        )

    def test_bridge_executes_publication_revision_then_r2_approval(self) -> None:
        fixture = self._fixture()
        fixture._advance_to_selection()
        fixture._reach_architecture_gate("Architecture for publication bridge", "2026-08-24T00:05:00Z")
        architecture_approved = self._execute(
            fixture,
            "bridge-publication-architecture-approve",
            {
                "kind": "RECORD_ARCHITECTURE_APPROVAL",
                "state_path": fixture.state_path.relative_to(fixture.root).as_posix(),
                "expected_revision": 1,
                "reviewed_by": "human-reviewer",
                "reviewed_at": "2026-08-24T00:06:00Z",
                "review_reference": "bridge:publication:architecture",
            },
            recorded_at="2026-08-24T00:06:30Z",
        )
        self.assertIsNone(architecture_approved["terminal_reason"])

        fixture._reach_publication_gate(1, 10)
        revised = self._execute(
            fixture,
            "bridge-publication-r1-revise",
            {
                "kind": "REQUEST_PUBLICATION_PREVIEW_REVISION",
                "state_path": fixture.state_path.relative_to(fixture.root).as_posix(),
                "expected_revision": 1,
                "regeneration_boundary": "DRAFT_COMPLETE",
                "requested_changes": "Repair the reviewed source/PDF and present r2.",
                "reviewed_by": "human-reviewer",
                "reviewed_at": "2026-08-24T00:14:00Z",
                "review_reference": "bridge:publication:r1",
            },
            recorded_at="2026-08-24T00:14:30Z",
        )
        self.assertEqual(revised["lifecycle_state"], "DRAFT_COMPLETE")
        state = core.load_json(fixture.state_path)
        self.assertEqual(state["human_gates"]["architecture_review"], "approved")
        self.assertEqual(state["human_gates"]["publication_preview"], "pending")
        self.assertEqual(state["machine_checkpoints"]["validation"], "pending")
        self.assertEqual(state["machine_checkpoints"]["publication_candidate"], "pending")

        candidate_r2 = fixture._build_publication_candidate(2)
        fixture._advance(
            {
                "reader-manuscript": candidate_r2["manifest"],
                "validated-source": candidate_r2["source"],
                "publication-pdf": candidate_r2["pdf"],
                "quality-regression-bundle": candidate_r2["bundle"],
                "semantic-review": candidate_r2["semantic"],
                "visual-review": candidate_r2["visual"],
            },
            "BRIDGE_VALIDATION_FIXTURE_R2",
            "2026-08-24T00:15:00Z",
        )
        gate_state = fixture._advance(
            {"publication-candidate": candidate_r2["candidate"]},
            "BRIDGE_CANDIDATE_FIXTURE_R2",
            "2026-08-24T00:16:00Z",
        )
        self.assertEqual(gate_state["lifecycle_state"], "RELEASE_CANDIDATE")
        self.assertEqual(gate_state["terminal_reason"], "HUMAN_GATE_REACHED")

        approved = self._execute(
            fixture,
            "bridge-publication-r2-approve",
            {
                "kind": "RECORD_PUBLICATION_PREVIEW_APPROVAL",
                "state_path": fixture.state_path.relative_to(fixture.root).as_posix(),
                "expected_revision": 2,
                "reviewed_by": "human-reviewer",
                "reviewed_at": "2026-08-24T00:17:00Z",
                "review_reference": "bridge:publication:r2",
            },
            recorded_at="2026-08-24T00:17:30Z",
        )
        self.assertEqual(approved["lifecycle_state"], "RELEASE_CANDIDATE")
        self.assertIsNone(approved["terminal_reason"])
        state = core.load_json(fixture.state_path)
        self.assertEqual(state["human_gates"]["publication_preview"], "approved")
        self.assertEqual(state["machine_checkpoints"]["publication_preview"], "passed")
        self.assertEqual(state["next_action"], "stage:freeze")
        index = core.load_json(
            fixture.source_root / fixture.cfg["state_authority"]["human_review_index_path"]
        )
        publication_rows = [
            (row["revision"], row["decision"])
            for row in index["reviews"]
            if row["gate"] == "PUBLICATION_PREVIEW"
        ]
        self.assertEqual(publication_rows, [(1, "REQUEST_CHANGES"), (2, "APPROVED")])


if __name__ == "__main__":
    unittest.main()
