from __future__ import annotations

import unittest
from pathlib import Path

from scripts import survey_schema_v2 as schema_gate


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


if __name__ == "__main__":
    unittest.main()
