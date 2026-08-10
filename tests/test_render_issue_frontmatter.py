from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import render_issue_frontmatter as rif


class IssueFrontmatterRendererTests(unittest.TestCase):
    def _input(self) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "status": "post-draft-synthesis-input-ready",
            "basis": {"architecture_input_sha256": "1" * 64, "architecture_plan_sha256": "2" * 64, "article_prompt_sha256": "3" * 64, "article_drafts": []},
            "editorial_thesis": "test",
            "cover_anchor_candidates": ["feature"],
            "articles": [
                {"package_id": "feature", "package_type": "FEATURE", "drafting_order": 1, "page_target": 2, "late_breaking": False, "editorial_angle": "feature", "boundaries": [], "headline": "foo_bar", "deck": "feature deck", "blocks": []},
                {"package_id": "late", "package_type": "LATE_BREAKING", "drafting_order": 2, "page_target": 1, "late_breaking": True, "editorial_angle": "late", "boundaries": ["post-cutoff"], "headline": "Late", "deck": "late deck", "blocks": []},
            ],
            "constraints": {"language": "ja", "max_this_week_signals": 5, "no_new_external_facts": True, "summarize_only_validated_article_text": True, "late_breaking_boundary_required": True, "page_references_must_use_package_ids": True},
        }

    def _result(self, input_path: Path, prompt_path: Path) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "synthesis_version": "v0.1",
            "status": "DRAFT",
            "basis": {"synthesis_input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(), "prompt_id": "issue-synthesis-v0.1", "prompt_sha256": hashlib.sha256(prompt_path.read_bytes()).hexdigest()},
            "runner": {"provider": "test", "model": "test", "invocation": "unit", "generated_at": "2026-08-10T00:00:00Z", "run_reference": None},
            "cover": {"headline": "モデルの外側へ", "deck": "完成記事から見えた軸。", "anchor_package_ids": ["feature"]},
            "this_week_signals": [
                {"signal_id": "normal", "title": "通常", "summary": "通常記事を要約。", "package_ids": ["feature"], "late_breaking": False},
                {"signal_id": "late", "title": "締切後", "summary": "締切後情報として扱う。", "package_ids": ["late"], "late_breaking": True},
            ],
        }

    def test_frontmatter_uses_dynamic_pageref_and_semantic_late_box(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path = root / "input.json"
            input_path.write_text(json.dumps(self._input()), encoding="utf-8")
            prompt_path = root / "prompt.md"
            prompt_path.write_text("prompt", encoding="utf-8")
            result_path = root / "result.json"
            result_path.write_text(json.dumps(self._result(input_path, prompt_path)), encoding="utf-8")
            output = root / "frontmatter.tex"
            manifest_path = root / "manifest.json"
            manifest, passed = rif.render(input_path, result_path, prompt_path, output, manifest_path)
            self.assertTrue(passed, manifest)
            text = output.read_text(encoding="utf-8")
            self.assertIn(r"\surveycoverstory", text)
            self.assertIn(r"foo\_bar", text)
            self.assertIn(r"\pageref{pkg:feature}", text)
            self.assertIn(r"\pageref{pkg:late}", text)
            self.assertIn(r"\begin{latebreaking}", text)
            self.assertNotIn("p.3", text)
            self.assertEqual(manifest["signal_count"], 2)


if __name__ == "__main__":
    unittest.main()
