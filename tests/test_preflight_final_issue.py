from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import preflight_final_issue as preflight


class FinalIssuePreflightTests(unittest.TestCase):
    def _sha(self, path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def _record(self, root: Path, path: Path) -> dict:
        return {
            "path": path.relative_to(root).as_posix(),
            "sha256": self._sha(path),
            "bytes": path.stat().st_size,
        }

    def _fixture(self, root: Path) -> Path:
        issue = root / "issue"
        sections = issue / "sections" / "generated"
        sections.mkdir(parents=True)
        frontmatter = issue / "sections" / "00-frontmatter.tex"
        frontmatter.write_text(
            "\\surveycoverstory{モデルの外側へ}{今号の軸}{Feature}\n"
            "\\section*{This Week in AI}\n"
            "\\textbf{Feature} 要約。p.~\\pageref{pkg:feature}\n"
            "\\tableofcontents\n",
            encoding="utf-8",
        )
        article = sections / "01-feature.tex"
        article.write_text(
            "\\section{Feature}\n\\label{pkg:feature}\n本文。\\autocite{src-test}\n",
            encoding="utf-8",
        )
        references = issue / "references.bib"
        references.write_text(
            "@online{src-test,\n"
            "  title = {Test},\n"
            "  url = {https://example.com/test}\n"
            "}\n",
            encoding="utf-8",
        )
        main = issue / "main.tex"
        main.write_text(
            "\\documentclass{jlreq}\n"
            "\\addbibresource{references.bib}\n"
            "\\begin{document}\n"
            "\\input{sections/00-frontmatter}\n"
            "\\input{sections/generated/01-feature.tex}\n"
            "\\printbibliography\n"
            "\\end{document}\n",
            encoding="utf-8",
        )
        manifest = {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "status": "FINAL_SOURCE_ASSEMBLED",
            "passed": True,
            "basis": {},
            "article_section_count": 1,
            "article_sections": [
                {
                    "package_id": "feature",
                    **self._record(issue, article),
                    "label": "pkg:feature",
                }
            ],
            "frontmatter": {
                "schema_version": "1.0",
                "issue_id": "2026-W33",
                "passed": True,
                "basis": {},
                "output": self._record(issue, frontmatter),
                "anchor_package_ids": ["feature"],
                "signal_count": 1,
                "note": "test",
            },
            "references": self._record(issue, references),
            "main": self._record(issue, main),
            "ready_for_pdf_build": True,
            "freeze_allowed": False,
            "remaining_gates": [],
            "errors": [],
        }
        manifest_path = issue / "final-source-manifest.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        return issue

    def _refresh_section_record(self, issue: Path) -> None:
        manifest_path = issue / "final-source-manifest.json"
        manifest = json.loads(manifest_path.read_text())
        article = issue / manifest["article_sections"][0]["path"]
        manifest["article_sections"][0]["sha256"] = self._sha(article)
        manifest["article_sections"][0]["bytes"] = article.stat().st_size
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    def _refresh_frontmatter_record(self, issue: Path) -> None:
        manifest_path = issue / "final-source-manifest.json"
        manifest = json.loads(manifest_path.read_text())
        frontmatter = issue / manifest["frontmatter"]["output"]["path"]
        manifest["frontmatter"]["output"]["sha256"] = self._sha(frontmatter)
        manifest["frontmatter"]["output"]["bytes"] = frontmatter.stat().st_size
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    def _refresh_references_record(self, issue: Path) -> None:
        manifest_path = issue / "final-source-manifest.json"
        manifest = json.loads(manifest_path.read_text())
        references = issue / manifest["references"]["path"]
        manifest["references"]["sha256"] = self._sha(references)
        manifest["references"]["bytes"] = references.stat().st_size
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    def _set_issue_id(self, issue: Path, issue_id: str) -> None:
        manifest_path = issue / "final-source-manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["issue_id"] = issue_id
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    def test_valid_final_source_passes_exact_citation_and_pageref_checks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            issue = self._fixture(Path(tmp))
            report, passed = preflight.preflight(issue)
            self.assertTrue(passed, report)
            self.assertEqual(report["package_labels"], ["feature"])
            self.assertEqual(report["page_reference_labels"], ["feature"])
            self.assertEqual(report["citation_keys"], ["src-test"])
            self.assertEqual(report["bibliography_keys"], ["src-test"])

    def test_missing_and_unused_bibliography_keys_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            issue = self._fixture(Path(tmp))
            article = issue / "sections" / "generated" / "01-feature.tex"
            article.write_text(
                "\\section{Feature}\n\\label{pkg:feature}\n本文。\\autocite{src-missing}\n",
                encoding="utf-8",
            )
            self._refresh_section_record(issue)
            report, passed = preflight.preflight(issue)
            self.assertFalse(passed)
            self.assertEqual(report["missing_bibliography_keys"], ["src-missing"])
            self.assertEqual(report["unused_bibliography_keys"], ["src-test"])

    def test_literal_page_reference_or_unknown_pageref_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            issue = self._fixture(Path(tmp))
            frontmatter = issue / "sections" / "00-frontmatter.tex"
            frontmatter.write_text(
                frontmatter.read_text(encoding="utf-8")
                + "今号 p.3 を参照。\\pageref{pkg:unknown}\n",
                encoding="utf-8",
            )
            self._refresh_frontmatter_record(issue)
            report, passed = preflight.preflight(issue)
            self.assertFalse(passed)
            self.assertTrue(any("literal internal page references" in error for error in report["errors"]))
            self.assertTrue(any("unknown package page refs" in error for error in report["errors"]))

    def test_unused_generated_bibliography_entry_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            issue = self._fixture(Path(tmp))
            references = issue / "references.bib"
            references.write_text(
                references.read_text(encoding="utf-8")
                + "\n@online{src-unused,\n  title = {Unused},\n  url = {https://example.com/unused}\n}\n",
                encoding="utf-8",
            )
            self._refresh_references_record(issue)
            report, passed = preflight.preflight(issue)
            self.assertFalse(passed)
            self.assertEqual(report["unused_bibliography_keys"], ["src-unused"])

    def test_internal_editorial_workflow_language_fails_reader_facing_preflight(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            issue = self._fixture(Path(tmp))
            article = issue / "sections" / "generated" / "01-feature.tex"
            article.write_text(
                "\\section{Feature}\n"
                "\\label{pkg:feature}\n"
                "Reaction Passでは有力だったため、次号で追跡する。\\autocite{src-test}\n",
                encoding="utf-8",
            )
            self._refresh_section_record(issue)
            report, passed = preflight.preflight(issue)
            self.assertFalse(passed)
            self.assertTrue(any("reader-facing prose violation [Reaction Pass]" in error for error in report["errors"]))
            self.assertTrue(any("reader-facing prose violation [future production TODO]" in error for error in report["errors"]))

    def test_tex_comments_do_not_trigger_reader_facing_prose_guard(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            issue = self._fixture(Path(tmp))
            article = issue / "sections" / "generated" / "01-feature.tex"
            article.write_text(
                "\\section{Feature}\n"
                "\\label{pkg:feature}\n"
                "% Reaction Pass and Candidate Inventory are internal provenance comments.\n"
                "X上ではlocal deploymentの検証が観測された。\\autocite{src-test}\n",
                encoding="utf-8",
            )
            self._refresh_section_record(issue)
            report, passed = preflight.preflight(issue)
            self.assertTrue(passed, report)

    def test_explicit_source_notes_marker_can_exempt_internal_metadata_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            issue = self._fixture(Path(tmp))
            article = issue / "sections" / "generated" / "01-feature.tex"
            article.write_text(
                preflight.PROSE_LINT_EXEMPT_MARKER
                + "\n\\section{Source Notes}\n"
                + "\\label{pkg:feature}\n"
                + "Reaction Pass provenance。\\autocite{src-test}\n",
                encoding="utf-8",
            )
            self._refresh_section_record(issue)
            report, passed = preflight.preflight(issue)
            self.assertTrue(passed, report)

    def test_frozen_w32_remains_legacy_exempt_from_new_prose_guard(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            issue = self._fixture(Path(tmp))
            self._set_issue_id(issue, "2026-W32")
            article = issue / "sections" / "generated" / "01-feature.tex"
            article.write_text(
                "\\section{Feature}\n\\label{pkg:feature}\nReaction Passでは観測した。\\autocite{src-test}\n",
                encoding="utf-8",
            )
            self._refresh_section_record(issue)
            report, passed = preflight.preflight(issue)
            self.assertTrue(passed, report)


if __name__ == "__main__":
    unittest.main()
