from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import finalize_weekly_issue as fwi


class FinalizeWeeklyIssueTests(unittest.TestCase):
    def _write_article_assembly(self, root: Path) -> Path:
        assembly = root / "article-assembly"
        section_dir = assembly / "sections" / "generated"
        section_dir.mkdir(parents=True)
        section = section_dir / "01-feature.tex"
        section.write_text("% generated\n\\section{Feature}\n本文。\n", encoding="utf-8")
        refs = assembly / "references.bib"
        refs.write_text("@online{src-test,\n  title = {Test},\n  url = {https://example.com}\n}\n", encoding="utf-8")
        bib_manifest = {
            "schema_version": "1.0",
            "passed": True,
            "entry_count": 1,
            "output": {"path": refs.as_posix(), "sha256": hashlib.sha256(refs.read_bytes()).hexdigest(), "bytes": refs.stat().st_size},
        }
        manifest = {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "status": "ARTICLE_ONLY_ASSEMBLED",
            "passed": True,
            "expected_article_package_count": 1,
            "assembled_article_package_count": 1,
            "article_packages": [
                {
                    "package_id": "feature",
                    "drafting_order": 1,
                    "section": {"path": "sections/generated/01-feature.tex", "sha256": hashlib.sha256(section.read_bytes()).hexdigest(), "bytes": section.stat().st_size},
                    "bibliography_source": {},
                    "render_manifest_sha256": "1" * 64,
                }
            ],
            "section_inputs": ["sections/generated/01-feature.tex"],
            "bibliography": bib_manifest,
            "main": {"path": "main.tex", "sha256": "2" * 64, "bytes": 1},
            "frontmatter_deferred": True,
            "cover_headline_deferred": True,
            "this_week_summary_deferred": True,
            "errors": [],
        }
        (assembly / "assembly-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        return assembly

    def _synthesis_files(self, root: Path) -> tuple[Path, Path, Path]:
        input_path = root / "synthesis-input.json"
        input_value = {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "status": "post-draft-synthesis-input-ready",
            "basis": {"architecture_input_sha256": "1" * 64, "architecture_plan_sha256": "2" * 64, "article_prompt_sha256": "3" * 64, "article_drafts": []},
            "editorial_thesis": "test",
            "cover_anchor_candidates": ["feature"],
            "articles": [
                {"package_id": "feature", "package_type": "FEATURE", "drafting_order": 1, "page_target": 2, "late_breaking": False, "editorial_angle": "test", "boundaries": [], "headline": "Feature", "deck": "Deck", "blocks": []}
            ],
            "constraints": {"language": "ja", "max_this_week_signals": 5, "no_new_external_facts": True, "summarize_only_validated_article_text": True, "late_breaking_boundary_required": True, "page_references_must_use_package_ids": True},
        }
        input_path.write_text(json.dumps(input_value), encoding="utf-8")
        prompt = root / "synthesis-prompt.md"
        prompt.write_text("prompt", encoding="utf-8")
        result = root / "synthesis-result.json"
        result_value = {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "synthesis_version": "v0.1",
            "status": "DRAFT",
            "basis": {"synthesis_input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(), "prompt_id": "issue-synthesis-v0.1", "prompt_sha256": hashlib.sha256(prompt.read_bytes()).hexdigest()},
            "runner": {"provider": "test", "model": "test", "invocation": "unit", "generated_at": "2026-08-10T00:00:00Z", "run_reference": None},
            "cover": {"headline": "モデルの外側へ", "deck": "完成記事から見えた軸。", "anchor_package_ids": ["feature"]},
            "this_week_signals": [
                {"signal_id": "feature-signal", "title": "Feature", "summary": "Featureを要約。", "package_ids": ["feature"], "late_breaking": False}
            ],
        }
        result.write_text(json.dumps(result_value), encoding="utf-8")
        return input_path, result, prompt

    def _template(self, root: Path) -> Path:
        path = root / "template.tex.in"
        path.write_text("\\begin{document}\n\\input{sections/00-frontmatter}\n@@SECTION_INPUTS@@\n\\end{document}\n", encoding="utf-8")
        return path

    def test_final_source_adds_dynamic_package_label_and_keeps_freeze_gate_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            assembly = self._write_article_assembly(root)
            synthesis_input, synthesis_result, prompt = self._synthesis_files(root)
            template = self._template(root)
            out = root / "final"
            manifest, passed = fwi.finalize(assembly, synthesis_input, synthesis_result, prompt, template, out)
            self.assertTrue(passed, manifest)
            section = (out / "sections" / "generated" / "01-feature.tex").read_text(encoding="utf-8")
            self.assertIn("\\section{Feature}\n\\label{pkg:feature}\n", section)
            frontmatter = (out / "sections" / "00-frontmatter.tex").read_text(encoding="utf-8")
            self.assertIn(r"\pageref{pkg:feature}", frontmatter)
            main = (out / "main.tex").read_text(encoding="utf-8")
            self.assertIn(r"\input{sections/generated/01-feature.tex}", main)
            self.assertFalse(manifest["freeze_allowed"])
            self.assertTrue(manifest["ready_for_pdf_build"])
            self.assertTrue((out / "references.bib").is_file())

    def test_tampered_article_section_blocks_finalization(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            assembly = self._write_article_assembly(root)
            (assembly / "sections" / "generated" / "01-feature.tex").write_text("tampered\n", encoding="utf-8")
            synthesis_input, synthesis_result, prompt = self._synthesis_files(root)
            out = root / "final"
            manifest, passed = fwi.finalize(assembly, synthesis_input, synthesis_result, prompt, self._template(root), out)
            self.assertFalse(passed)
            self.assertFalse((out / "main.tex").exists())
            self.assertTrue(any("SHA mismatch" in error for error in manifest["errors"]))

    def test_section_without_single_top_level_section_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            fwi.inject_package_label("No section here\n", "feature")
        with self.assertRaises(ValueError):
            fwi.inject_package_label("\\section{A}\n\\section{B}\n", "feature")


if __name__ == "__main__":
    unittest.main()
