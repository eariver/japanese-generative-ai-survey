from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import special_reader_notes_ja as notes


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SpecialReaderNotesJaTests(unittest.TestCase):
    def make_repo(self) -> tuple[tempfile.TemporaryDirectory, Path, str]:
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        issue = "SP-TEST-M01"
        package_id = "feature-one"
        task_id = "evidence:SP-TEST-M01:item-one"
        package = {
            "schema_version": "1.0",
            "issue_id": issue,
            "package_id": package_id,
            "primary_evidence": [
                {
                    "evidence_task_id": task_id,
                    "card": {
                        "artifact": {"canonical_name": "Example Model"},
                        "claims": [
                            {
                                "claim_id": "claim-1",
                                "text": "Vendor reports Example Model supports a 1M context window.",
                                "evidence_class": "VENDOR_CLAIM",
                            }
                        ],
                        "limitations": [
                            {
                                "limitation_id": "limitation-1",
                                "text": "The reported capability was not independently reproduced.",
                                "evidence_class": "INFERENCE",
                            }
                        ],
                    },
                }
            ],
            "supporting_evidence": [],
        }
        package_path = root / f"sources/{issue}/drafting/packages/v0.1/{package_id}.json"
        dump(package_path, package)
        dump(
            root / f"sources/{issue}/architecture/issue-architecture-v0.1.json",
            {
                "packages": [
                    {"package_id": package_id, "package_type": "FEATURE"},
                    {"package_id": "frontmatter", "package_type": "FRONTMATTER"},
                ]
            },
        )
        source = root / "surveys/special/TEST/revisions/v0.2"
        (source / "technical-notes").mkdir(parents=True)
        note_path = source / f"technical-notes/10-{package_id}-notes.tex"
        note_path.write_text(
            "\\begin{technicalnote}{Example Model}{PRIMARY}\n"
            "\\item \\textbf{Vendor claim}: Vendor reports Example Model supports a 1M context window.\n"
            "\\item \\textbf{分析上の留意点}: The reported capability was not independently reproduced.\n"
            "{\\scriptsize\\color{SurveyMuted}Source-bound record: \\texttt{evidence:SP-TEST-M01:item-one}.}\n"
            "\\end{technicalnote}\n",
            encoding="utf-8",
        )
        manifest_path = source / "source-manifest.json"
        dump(
            manifest_path,
            {
                "source_version": "v0.2",
                "articles": [
                    {
                        "package_id": package_id,
                        "draft_package_path": package_path.relative_to(root).as_posix(),
                        "technical_notes_path": note_path.relative_to(source).as_posix(),
                        "technical_notes_sha256": sha(note_path),
                    }
                ],
            },
        )
        dump(
            root / f"sources/{issue}/pipeline-state.json",
            {
                "provenance": {
                    "validated_issue_source": {
                        "path": manifest_path.relative_to(root).as_posix(),
                        "sha256": sha(manifest_path),
                        "source_version": "v0.2",
                    }
                }
            },
        )
        return td, root, issue

    def test_prepare_preserves_source_text_and_leaves_translation_blank(self) -> None:
        td, root, issue = self.make_repo()
        self.addCleanup(td.cleanup)
        output = root / f"sources/{issue}/editorial/technical-notes-ja-v0.1.json"
        report = notes.prepare(root, issue, output)
        self.assertEqual(report["record_count"], 1)
        data = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(data["status"], "DRAFT")
        self.assertEqual(data["records"][0]["claims"][0]["text_ja"], "")
        self.assertIn("1M context window", data["records"][0]["claims"][0]["source_text"])

    def test_apply_replaces_only_pdf_facing_text(self) -> None:
        td, root, issue = self.make_repo()
        self.addCleanup(td.cleanup)
        summary = root / f"sources/{issue}/editorial/technical-notes-ja-v0.1.json"
        notes.prepare(root, issue, summary)
        data = json.loads(summary.read_text(encoding="utf-8"))
        data["status"] = "READY"
        data["records"][0]["claims"][0]["text_ja"] = "VendorはExample Modelが1M context windowをサポートすると説明している。"
        data["records"][0]["limitations"][0]["text_ja"] = "このcapabilityは独立には再現確認されていない。"
        dump(summary, data)

        report = notes.apply(root, issue, "TEST", summary)
        self.assertEqual(report["summary_replacement_count"], 2)
        note_path = root / "surveys/special/TEST/revisions/v0.2/technical-notes/10-feature-one-notes.tex"
        rendered = note_path.read_text(encoding="utf-8")
        self.assertIn("VendorはExample Model", rendered)
        self.assertIn("独立には再現確認されていない", rendered)
        self.assertNotIn("Vendor reports Example Model", rendered)
        # Upstream Draft Package / Evidence text remains untouched.
        package = json.loads((root / f"sources/{issue}/drafting/packages/v0.1/feature-one.json").read_text(encoding="utf-8"))
        self.assertEqual(package["primary_evidence"][0]["card"]["claims"][0]["text"], "Vendor reports Example Model supports a 1M context window.")

    def test_apply_rejects_english_only_reader_summary(self) -> None:
        td, root, issue = self.make_repo()
        self.addCleanup(td.cleanup)
        summary = root / f"sources/{issue}/editorial/technical-notes-ja-v0.1.json"
        notes.prepare(root, issue, summary)
        data = json.loads(summary.read_text(encoding="utf-8"))
        data["status"] = "READY"
        data["records"][0]["claims"][0]["text_ja"] = "Still English only."
        data["records"][0]["limitations"][0]["text_ja"] = "これは日本語です。"
        dump(summary, data)
        with self.assertRaisesRegex(ValueError, "Japanese sentence structure"):
            notes.apply(root, issue, "TEST", summary)


if __name__ == "__main__":
    unittest.main()
