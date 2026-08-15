import hashlib
import json
from pathlib import Path

from scripts.validate_weekly_carryover_ledger import validate


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def test_legacy_seed_requires_complete_coverage(tmp_path: Path) -> None:
    seed = tmp_path / "sources/2026-W33/carryover/carryover-seed-v0.1.json"
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
    ledger = tmp_path / "sources/2026-W33/carryover/carryover-ledger-v0.1.json"
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
    report = validate(tmp_path, "2026-W33", ledger, "screening")
    assert not report["passed"]
    assert any("legacy-b" in error for error in report["errors"])


def test_selection_stage_rejects_pending(tmp_path: Path) -> None:
    previous = tmp_path / "sources/2026-W33/selection/candidate-selection-v0.1.json"
    write_json(previous, {
        "schema_version": "1.0",
        "issue_id": "2026-W33",
        "status": "APPROVED",
        "assignments": [
            {"evidence_task_id": "task-a", "title": "A", "role": "HOLD_OUT"},
            {"evidence_task_id": "task-b", "title": "B", "role": "SECTION_CORE"},
        ],
    })
    ledger = tmp_path / "sources/2026-W34/carryover/carryover-ledger-v0.1.json"
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
    screening = validate(tmp_path, "2026-W34", ledger, "screening")
    selection = validate(tmp_path, "2026-W34", ledger, "selection")
    assert screening["passed"]
    assert not selection["passed"]
    assert selection["pending_keys"] == ["task-a"]


def test_structured_selection_allows_resolved_entry(tmp_path: Path) -> None:
    previous = tmp_path / "sources/2026-W33/selection/candidate-selection-v0.1.json"
    write_json(previous, {
        "schema_version": "1.0",
        "issue_id": "2026-W33",
        "status": "APPROVED",
        "assignments": [
            {"evidence_task_id": "task-a", "title": "A", "role": "WATCHLIST"},
        ],
    })
    ledger = tmp_path / "sources/2026-W34/carryover/carryover-ledger-v0.1.json"
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
    report = validate(tmp_path, "2026-W34", ledger, "selection")
    assert report["passed"]
    assert report["expected_count"] == 1
    assert report["pending_count"] == 0
