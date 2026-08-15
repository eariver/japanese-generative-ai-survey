import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.initialize_weekly_carryover_ledger import initialize
from scripts.validate_weekly_carryover_ledger import validate


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class WeeklyCarryoverLedgerTests(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def test_legacy_seed_requires_complete_coverage(self) -> None:
        seed = self.root / "sources/2026-W33/carryover/carryover-seed-v0.1.json"
        write_json(seed, {
            "schema_version": "1.0",
            "source_issue_id": "2026-W32",
            "target_issue_id": "2026-W33",
            "entries": [
                {"prior_item_id": "legacy-a", "title": "Legacy A", "prior_role": "HOLD_OUT"},
                {"prior_item_id": "legacy-b", "title": "Legacy B", "prior_role": "LATE_BREAKING"},
            ],
        })
        digest = hashlib.sha256(seed.read_bytes()).hexdigest()
        ledger = self.root / "sources/2026-W33/carryover/carryover-ledger-v0.1.json"
        write_json(ledger, {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "source_issue_id": "2026-W32",
            "basis": {
                "legacy_seed_path": "sources/2026-W33/carryover/carryover-seed-v0.1.json",
                "legacy_seed_sha256": digest,
            },
            "entries": [
                {
                    "prior_item_id": "legacy-a",
                    "title": "Legacy A",
                    "prior_role": "HOLD_OUT",
                    "status": "RECHECKED_UNRESOLVED",
                    "resolution_note": "Still unresolved.",
                    "current_evidence_task_ids": [],
                },
            ],
        })
        report = validate(self.root, "2026-W33", ledger, "screening")
        self.assertFalse(report["passed"])
        self.assertTrue(any("legacy-b" in error for error in report["errors"]))

    def test_selection_stage_rejects_pending(self) -> None:
        previous = self.root / "sources/2026-W33/selection/candidate-selection-v0.1.json"
        write_json(previous, {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "status": "APPROVED",
            "assignments": [
                {"evidence_task_id": "task-a", "title": "A", "role": "HOLD_OUT"},
                {"evidence_task_id": "task-b", "title": "B", "role": "SECTION_CORE"},
            ],
        })
        ledger = self.root / "sources/2026-W34/carryover/carryover-ledger-v0.1.json"
        write_json(ledger, {
            "schema_version": "1.0",
            "issue_id": "2026-W34",
            "source_issue_id": "2026-W33",
            "entries": [
                {
                    "prior_evidence_task_id": "task-a",
                    "title": "A",
                    "prior_role": "HOLD_OUT",
                    "status": "PENDING_RECHECK",
                    "resolution_note": "Queued for W34 recheck.",
                    "current_evidence_task_ids": [],
                },
            ],
        })
        screening = validate(self.root, "2026-W34", ledger, "screening")
        selection = validate(self.root, "2026-W34", ledger, "selection")
        self.assertTrue(screening["passed"])
        self.assertFalse(selection["passed"])
        self.assertEqual(selection["pending_keys"], ["task-a"])

    def test_structured_selection_allows_resolved_entry(self) -> None:
        previous = self.root / "sources/2026-W33/selection/candidate-selection-v0.1.json"
        write_json(previous, {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "status": "APPROVED",
            "assignments": [
                {"evidence_task_id": "task-a", "title": "A", "role": "WATCHLIST"},
            ],
        })
        ledger = self.root / "sources/2026-W34/carryover/carryover-ledger-v0.1.json"
        write_json(ledger, {
            "schema_version": "1.0",
            "issue_id": "2026-W34",
            "source_issue_id": "2026-W33",
            "entries": [
                {
                    "prior_evidence_task_id": "task-a",
                    "title": "A",
                    "prior_role": "WATCHLIST",
                    "status": "RESOLVED_SUPPORT_CURRENT",
                    "resolution_note": "Mapped to current supporting evidence.",
                    "current_evidence_task_ids": ["current-task"],
                },
            ],
        })
        report = validate(self.root, "2026-W34", ledger, "selection")
        self.assertTrue(report["passed"])
        self.assertEqual(report["expected_count"], 1)
        self.assertEqual(report["pending_count"], 0)

    def test_initializer_creates_pending_entries_from_approved_selection(self) -> None:
        previous = self.root / "sources/2026-W33/selection/candidate-selection-v0.1.json"
        write_json(previous, {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "status": "APPROVED",
            "assignments": [
                {"evidence_task_id": "task-z", "title": "Z", "role": "LATE_BREAKING"},
                {"evidence_task_id": "task-a", "title": "A", "role": "HOLD_OUT"},
                {"evidence_task_id": "task-core", "title": "Core", "role": "FEATURE_CORE"},
            ],
        })
        ledger = self.root / "sources/2026-W34/carryover/carryover-ledger-v0.1.json"
        result = initialize(self.root, "2026-W34", ledger)
        self.assertEqual(result["status"], "INITIALIZED")
        doc = json.loads(ledger.read_text(encoding="utf-8"))
        self.assertEqual([entry["prior_evidence_task_id"] for entry in doc["entries"]], ["task-a", "task-z"])
        self.assertTrue(all(entry["status"] == "PENDING_RECHECK" for entry in doc["entries"]))
        self.assertTrue(validate(self.root, "2026-W34", ledger, "screening")["passed"])
        self.assertFalse(validate(self.root, "2026-W34", ledger, "selection")["passed"])

    def test_initializer_preserves_existing_legacy_ledger(self) -> None:
        ledger = self.root / "sources/2026-W33/carryover/carryover-ledger-v0.1.json"
        write_json(ledger, {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "source_issue_id": "2026-W32",
            "entries": [],
        })
        result = initialize(self.root, "2026-W33", ledger)
        self.assertEqual(result["status"], "EXISTING_LEDGER_PRESERVED")
        self.assertEqual(result["entry_count"], 0)

    def test_initializer_refuses_unapproved_previous_selection(self) -> None:
        previous = self.root / "sources/2026-W33/selection/candidate-selection-v0.1.json"
        write_json(previous, {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "status": "PENDING_APPROVAL",
            "assignments": [],
        })
        ledger = self.root / "sources/2026-W34/carryover/carryover-ledger-v0.1.json"
        with self.assertRaisesRegex(ValueError, "must be APPROVED"):
            initialize(self.root, "2026-W34", ledger)


if __name__ == "__main__":
    unittest.main()
