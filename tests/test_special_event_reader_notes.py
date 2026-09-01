from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import fill_special_reader_notes_ja as fill
from scripts import run_expand_special_validated_source as runner
from scripts import special_reader_notes_ja as notes


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SpecialEventReaderNotesTests(unittest.TestCase):
    def make_repo(self) -> tuple[tempfile.TemporaryDirectory, Path, str, str, dict]:
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        issue = "SP-TEST-H1"
        package_id = "feature-one"
        task_id = "event-only-one"
        record = {
            "issue_id": issue,
            "evidence_task_id": task_id,
            "card": {
                "artifact": {"organization": "Example Org"},
                "sources": [{
                    "source_id": "s",
                    "title": "Example Event Release",
                    "url": "https://example.com/release",
                    "published_at": "2025-01-20",
                }],
                "temporal": {"events": [{
                    "event_id": "e",
                    "source_ids": ["s"],
                    "occurred_at": "2025-01-20",
                    "description": "Example service became available through the API.",
                }]},
                "claims": [],
                "metrics": [],
                "limitations": [],
            },
        }
        package = {
            "schema_version": "1.0",
            "issue_id": issue,
            "package_id": package_id,
            "primary_evidence": [record],
            "supporting_evidence": [],
        }
        package_path = root / f"sources/{issue}/drafting/packages/v0.1/{package_id}.json"
        dump(package_path, package)
        dump(
            root / f"sources/{issue}/architecture/issue-architecture-v0.1.json",
            {"packages": [{"package_id": package_id, "package_type": "FEATURE"}]},
        )
        return td, root, issue, package_id, record

    def test_prepare_fill_apply_and_check_event_only_evidence(self) -> None:
        td, root, issue, package_id, record = self.make_repo(); self.addCleanup(td.cleanup)
        summary = root / f"sources/{issue}/editorial/technical-notes-ja-v0.1.json"
        report = notes.prepare(root, issue, summary)
        self.assertEqual(report["record_count"], 1)
        prepared = json.loads(summary.read_text(encoding="utf-8"))
        self.assertEqual(prepared["records"][0]["artifact_name"], "Example Event Release")
        self.assertEqual(len(prepared["records"][0]["event_facts"]), 1)
        event = prepared["records"][0]["event_facts"][0]
        self.assertEqual(event["item_id"], "e")
        self.assertEqual(event["evidence_class"], "PRIMARY_FACT")

        overrides = root / f"sources/{issue}/editorial/technical-notes-ja-overrides-v0.1"
        dump(overrides / "part-01.json", {
            "issue_id": issue,
            "translations": [{
                "evidence_task_id": "event-only-one",
                "kind": "event",
                "item_id": "e",
                "source_text_sha256": event["source_text_sha256"],
                "text_ja": "2025年1月20日、Example serviceはAPIで利用可能になった。",
            }],
        })
        fill_report = fill.run(root, issue, summary, overrides)
        self.assertEqual(fill_report["translation_override_count"], 1)
        self.assertEqual(json.loads(summary.read_text(encoding="utf-8"))["status"], "READY")

        original_card_name = runner.expansion.card_name
        original_event_dates = runner.expansion.event_dates
        self.addCleanup(setattr, runner.expansion, "card_name", original_card_name)
        self.addCleanup(setattr, runner.expansion, "event_dates", original_event_dates)
        runner.expansion.card_name = runner.compat_card_name
        runner.expansion.event_dates = runner.compat_event_dates
        note = runner.safe_note("PRIMARY", record)
        self.assertIn("Example Event Release", note)
        self.assertIn("2025-01-20", note)
        self.assertIn("Example service became available through the API.", note)
        self.assertNotIn("normalized claim", note)

        source = root / "surveys/special/TEST/revisions/v0.2"
        note_path = source / f"technical-notes/10-{package_id}-notes.tex"
        note_path.parent.mkdir(parents=True, exist_ok=True)
        note_path.write_text(note, encoding="utf-8")
        package_path = root / f"sources/{issue}/drafting/packages/v0.1/{package_id}.json"
        manifest_path = source / "source-manifest.json"
        dump(manifest_path, {
            "source_version": "v0.2",
            "articles": [{
                "package_id": package_id,
                "draft_package_path": package_path.relative_to(root).as_posix(),
                "technical_notes_path": note_path.relative_to(source).as_posix(),
                "technical_notes_sha256": sha(note_path),
            }],
        })
        dump(root / f"sources/{issue}/pipeline-state.json", {
            "provenance": {"validated_issue_source": {
                "path": manifest_path.relative_to(root).as_posix(),
                "sha256": sha(manifest_path),
                "source_version": "v0.2",
            }}
        })

        applied = notes.apply(root, issue, "TEST", summary)
        self.assertEqual(applied["summary_replacement_count"], 1)
        rendered = note_path.read_text(encoding="utf-8")
        self.assertIn("APIで利用可能になった", rendered)
        self.assertNotIn("became available through the API", rendered)
        checked = notes.check(root, issue)
        self.assertTrue(checked["passed"], checked["errors"])
        self.assertEqual(checked["generic_fallback_findings"], 0)


if __name__ == "__main__":
    unittest.main()
