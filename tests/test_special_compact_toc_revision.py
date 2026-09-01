from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.revise_special_compact_toc import build


def dump(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class CompactTocRevisionTests(unittest.TestCase):
    def test_validated_draft_can_receive_content_neutral_section_toc_revision(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            issue = "SP-2026-M04"
            slug = "2026-M04"
            current = root / "surveys" / "special" / slug / "revisions" / "v0.2"
            (current / "sections").mkdir(parents=True)
            (current / "technical-notes").mkdir(parents=True)
            front = current / "sections" / "00-frontmatter.tex"
            front.write_text("\\section*{Monthly Signals}\n\\tableofcontents\n", encoding="utf-8")
            article = current / "sections" / "10-a.tex"
            notes = current / "technical-notes" / "10-a-notes.tex"
            article.write_text("article body\n", encoding="utf-8")
            notes.write_text("notes body\n", encoding="utf-8")
            main = current / "main.tex"
            main.write_text("\\input{sections/00-frontmatter}\n", encoding="utf-8")
            manifest = current / "source-manifest.json"
            dump(manifest, {
                "source_version": "v0.2",
                "status": "VALIDATED_SOURCE",
                "frontmatter": {"path": "sections/00-frontmatter.tex", "sha256": digest(front)},
                "main_tex": {"path": "main.tex", "sha256": digest(main)},
                "articles": [{
                    "package_id": "a",
                    "article_section_path": "sections/10-a.tex",
                    "article_section_sha256": digest(article),
                    "technical_notes_path": "technical-notes/10-a-notes.tex",
                    "technical_notes_sha256": digest(notes),
                }],
                "theme_synthesis": [],
                "reader_facing_technical_notes": True,
            })
            state_path = root / "sources" / issue / "pipeline-state.json"
            dump(state_path, {
                "lifecycle_state": "VALIDATED_DRAFT",
                "gates": {
                    "claim_and_chronology_validation": "passed",
                    "latex_build": "pending",
                    "visual_review": "pending",
                    "freeze": "pending",
                },
                "provenance": {
                    "validated_issue_source": {
                        "path": manifest.relative_to(root).as_posix(),
                        "sha256": digest(manifest),
                        "source_version": "v0.2",
                        "reader_facing_technical_notes": True,
                    }
                },
            })
            marker = root / "sources" / issue / "editorial" / "layout-revision-v0.3.json"
            dump(marker, {
                "schema_version": "1.0",
                "issue_id": issue,
                "revision": "v0.3",
                "constraints": {
                    "new_external_evidence_allowed": False,
                    "selected_evidence_only": True,
                    "reader_content_changed": False,
                },
                "layout_changes": {"compact_toc_to_sections": True},
                "reason": "Over-budget preview caused by subsection-heavy TOC.",
            })

            report = build(root, slug, issue, "v0.3")
            self.assertEqual(report["toc_depth"], "section")
            revised = root / "surveys" / "special" / slug / "revisions" / "v0.3"
            revised_front = (revised / "sections" / "00-frontmatter.tex").read_text(encoding="utf-8")
            self.assertIn(r"\setcounter{tocdepth}{0}", revised_front)
            self.assertEqual((revised / "sections" / "10-a.tex").read_bytes(), article.read_bytes())
            self.assertEqual((revised / "technical-notes" / "10-a-notes.tex").read_bytes(), notes.read_bytes())
            new_state = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(new_state["lifecycle_state"], "VALIDATED_DRAFT")
            self.assertEqual(new_state["gates"]["latex_build"], "pending")
            self.assertEqual(new_state["provenance"]["validated_issue_source"]["source_version"], "v0.3")
            self.assertTrue(new_state["provenance"]["validated_issue_source"]["reader_facing_technical_notes"])


if __name__ == "__main__":
    unittest.main()
