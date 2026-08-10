from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import assemble_substantive_issue as assembly


class SubstantiveAssemblyTests(unittest.TestCase):
    def _sha(self, path: Path) -> str:
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def _write_render(self, root: Path, package_id: str, package_sha: str, tex_text: str, bib_text: str) -> Path:
        root.mkdir(parents=True, exist_ok=True)
        tex = root / f"{package_id}.tex"
        bib = root / f"{package_id}.bib"
        tex.write_text(tex_text, encoding="utf-8")
        bib.write_text(bib_text, encoding="utf-8")
        manifest = root / f"{package_id}.render.json"
        manifest.write_text(
            json.dumps(
                {
                    "schema_version": "1.0",
                    "issue_id": "2026-W33",
                    "package_id": package_id,
                    "passed": True,
                    "basis": {
                        "draft_package_sha256": package_sha,
                        "article_draft_sha256": "a" * 64,
                        "prompt_sha256": "b" * 64,
                    },
                    "tex": {"path": tex.name, "sha256": self._sha(tex), "bytes": tex.stat().st_size},
                    "bib": {"path": bib.name, "sha256": self._sha(bib), "bytes": bib.stat().st_size, "entry_count": 1},
                    "citation_keys": ["src-same"],
                    "note": "test",
                }
            ),
            encoding="utf-8",
        )
        return manifest

    def _package_manifest(self, path: Path) -> tuple[str, str]:
        first_sha = "1" * 64
        second_sha = "2" * 64
        path.write_text(
            json.dumps(
                {
                    "schema_version": "1.0",
                    "issue_id": "2026-W33",
                    "passed": True,
                    "package_count": 4,
                    "materialized_package_count": 4,
                    "article_drafting_count": 2,
                    "post_draft_summary_count": 1,
                    "reference_generation_count": 1,
                    "basis": {
                        "architecture_plan_sha256": "c" * 64,
                        "architecture_input_sha256": "d" * 64,
                        "evidence_reviewed_sha256": "e" * 64,
                    },
                    "package_files": [
                        {
                            "package_id": "frontmatter",
                            "package_type": "FRONTMATTER",
                            "draft_source_mode": "ISSUE_SYNTHESIS",
                            "execution_stage": "POST_DRAFT_SUMMARY",
                            "path": "frontmatter.json",
                            "sha256": "f" * 64,
                            "bytes": 1,
                            "drafting_order": 3,
                        },
                        {
                            "package_id": "second-story",
                            "package_type": "SECTION",
                            "draft_source_mode": "EVIDENCE_PACKAGE",
                            "execution_stage": "ARTICLE_DRAFTING",
                            "path": "second.json",
                            "sha256": second_sha,
                            "bytes": 1,
                            "drafting_order": 2,
                        },
                        {
                            "package_id": "first-story",
                            "package_type": "FEATURE",
                            "draft_source_mode": "EVIDENCE_PACKAGE",
                            "execution_stage": "ARTICLE_DRAFTING",
                            "path": "first.json",
                            "sha256": first_sha,
                            "bytes": 1,
                            "drafting_order": 1,
                        },
                        {
                            "package_id": "references",
                            "package_type": "REFERENCES",
                            "draft_source_mode": "REFERENCES_GENERATED",
                            "execution_stage": "REFERENCE_GENERATION",
                            "path": "references.json",
                            "sha256": "9" * 64,
                            "bytes": 1,
                            "drafting_order": 4,
                        },
                    ],
                    "errors": [],
                    "note": "test",
                }
            ),
            encoding="utf-8",
        )
        return first_sha, second_sha

    def test_orders_sections_and_deduplicates_generated_bibliography(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package_manifest = root / "draft-package-manifest.json"
            first_sha, second_sha = self._package_manifest(package_manifest)
            common_bib = "@online{src-same,\n  title = {Same},\n  url = {https://example.com/same}\n}\n"
            render1 = self._write_render(root / "r1", "first-story", first_sha, "\\section{First}\n", common_bib)
            render2 = self._write_render(root / "r2", "second-story", second_sha, "\\section{Second}\n", common_bib)

            out = root / "out"
            manifest, passed = assembly.assemble(package_manifest, [render2, render1], out)
            self.assertTrue(passed, manifest)
            self.assertEqual([item["package_id"] for item in manifest["sections"]], ["first-story", "second-story"])
            self.assertEqual([item["section_path"] for item in manifest["sections"]], ["sections/10-first-story.tex", "sections/20-second-story.tex"])
            inputs = (out / "substantive-inputs.tex").read_text(encoding="utf-8")
            self.assertEqual(inputs.splitlines(), ["\\input{sections/10-first-story}", "\\input{sections/20-second-story}"])
            merged = (out / "references.generated.bib").read_text(encoding="utf-8")
            self.assertEqual(merged.count("@online{src-same,"), 1)
            self.assertEqual(manifest["merged_bibliography"]["entry_count"], 1)
            self.assertEqual(manifest["merged_bibliography"]["deduplicated_keys"], ["src-same"])
            self.assertEqual({item["execution_stage"] for item in manifest["deferred_packages"]}, {"POST_DRAFT_SUMMARY", "REFERENCE_GENERATION"})

    def test_missing_render_manifest_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package_manifest = root / "draft-package-manifest.json"
            first_sha, _ = self._package_manifest(package_manifest)
            render1 = self._write_render(
                root / "r1",
                "first-story",
                first_sha,
                "\\section{First}\n",
                "@online{src-one,\n  title = {One},\n  url = {https://example.com/one}\n}\n",
            )
            manifest, passed = assembly.assemble(package_manifest, [render1], root / "out")
            self.assertFalse(passed)
            self.assertTrue(any("missing render manifests" in error for error in manifest["errors"]))
            self.assertIsNone(manifest["merged_bibliography"])

    def test_render_hash_or_package_basis_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package_manifest = root / "draft-package-manifest.json"
            first_sha, second_sha = self._package_manifest(package_manifest)
            render1 = self._write_render(root / "r1", "first-story", first_sha, "First", "@online{a,\n  title = {A},\n  url = {https://example.com/a}\n}\n")
            render2 = self._write_render(root / "r2", "second-story", second_sha, "Second", "@online{b,\n  title = {B},\n  url = {https://example.com/b}\n}\n")
            value = json.loads(render2.read_text())
            value["basis"]["draft_package_sha256"] = "0" * 64
            render2.write_text(json.dumps(value), encoding="utf-8")
            manifest, passed = assembly.assemble(package_manifest, [render1, render2], root / "out")
            self.assertFalse(passed)
            self.assertTrue(any("Draft Package SHA" in error for error in manifest["errors"]))


if __name__ == "__main__":
    unittest.main()
