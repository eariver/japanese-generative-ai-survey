from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import assemble_weekly_issue as awi


class WeeklyIssueAssemblyTests(unittest.TestCase):
    def _selected(self, task_id: str) -> dict:
        return {
            "evidence_task_id": task_id,
            "title": task_id,
            "role": "FEATURE_CORE",
            "selection_rationale": "selected",
            "artifact_type": "MODEL_UPDATE",
            "organization": "Example",
            "timing_relation": "MAIN_EVENT",
            "event_dates": ["2026-08-05"],
            "evidence_status": "VERIFIED",
            "comparison_readiness": "READY",
            "why_now_confirmed": True,
            "remaining_boundaries": [],
            "evidence_class_counts": {"PRIMARY_FACT": 1},
            "source_class_counts": {"PRIMARY_OFFICIAL": 1},
        }

    def _architecture_input(self, task_ids: list[str]) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "status": "architecture-input-ready",
            "basis": {
                "selection_path": "selection.json",
                "selection_sha256": "1" * 64,
                "matrix_path": "matrix.json",
                "matrix_sha256": "2" * 64,
                "selection_version": "v0.1",
                "approval": {"approved_by": "human", "approved_at": "2026-08-10T00:00:00Z", "approval_reference": "manual"},
            },
            "editorial_constraints": {
                "page_target": 16,
                "page_max": 24,
                "forced_section_balance": False,
                "cover_headline_deferred_until_drafts_stable": True,
                "this_week_summary_written_last": True,
                "late_breaking_must_remain_post_cutoff": True,
                "hold_or_excluded_items_must_not_be_drafted": True,
            },
            "selected_by_role": {
                "FEATURE_CORE": [self._selected(task_id) for task_id in task_ids],
                "SECTION_CORE": [], "PAPER_WATCH": [], "SUPPORTING_EVIDENCE": [],
                "LATE_BREAKING": [], "CHRONOLOGY": [], "WATCHLIST": [],
            },
            "not_selected_for_architecture": [],
            "selected_item_count": len(task_ids),
            "excluded_item_count": 0,
            "rules": ["test"],
        }

    def _plan(self, input_path: Path, task_ids: list[str]) -> dict:
        architecture_input = json.loads(input_path.read_text())
        packages = []
        for order, task_id in enumerate(task_ids, start=1):
            packages.append({
                "package_id": f"package-{order}",
                "title": f"Package {order}",
                "package_type": "FEATURE",
                "primary_evidence_task_ids": [task_id],
                "supporting_evidence_task_ids": [],
                "page_target": 1,
                "editorial_angle": "Explain it.",
                "must_cover": [],
                "boundaries": [],
                "late_breaking": False,
                "drafting_order": order,
            })
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "architecture_version": "v0.1",
            "status": "APPROVED",
            "basis": {
                "architecture_input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
                "selection_sha256": architecture_input["basis"]["selection_sha256"],
                "matrix_sha256": architecture_input["basis"]["matrix_sha256"],
            },
            "approval": {"approved_by": "human", "approved_at": "2026-08-10T00:00:00Z", "approval_reference": "manual"},
            "editorial_thesis": "test",
            "architecture_goals": ["test"],
            "page_budget": {"target": 16, "max": 24, "planned": len(packages)},
            "cover": {"headline_deferred": True, "headline": None, "anchor_candidates": task_ids[:1]},
            "packages": packages,
            "this_week_summary_written_last": True,
        }

    def _bib(self, key: str, title: str = "Title") -> str:
        return f"@online{{{key},\n  title = {{{title}}},\n  url = {{https://example.com/{key}}}\n}}\n"

    def _write_fixture(self, root: Path, task_ids: list[str]) -> tuple[Path, Path, Path, Path, Path]:
        architecture_input = root / "architecture-input.json"
        architecture_input.write_text(json.dumps(self._architecture_input(task_ids)), encoding="utf-8")
        architecture_plan = root / "architecture-plan.json"
        architecture_plan.write_text(json.dumps(self._plan(architecture_input, task_ids)), encoding="utf-8")

        draft_manifest = {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "passed": True,
            "basis": {
                "architecture_plan_sha256": hashlib.sha256(architecture_plan.read_bytes()).hexdigest(),
                "architecture_input_sha256": hashlib.sha256(architecture_input.read_bytes()).hexdigest(),
                "evidence_reviewed_sha256": "3" * 64,
            },
            "package_files": [],
        }
        render_dir = root / "renders"
        render_dir.mkdir()
        for order, task_id in enumerate(task_ids, start=1):
            package_id = f"package-{order}"
            draft_sha = hashlib.sha256(f"draft-{package_id}".encode()).hexdigest()
            draft_manifest["package_files"].append({
                "package_id": package_id,
                "package_type": "FEATURE",
                "draft_source_mode": "EVIDENCE_PACKAGE",
                "execution_stage": "ARTICLE_DRAFTING",
                "path": f"{package_id}.json",
                "sha256": draft_sha,
                "bytes": 1,
                "drafting_order": order,
            })
            package_render_dir = render_dir / package_id
            package_render_dir.mkdir()
            tex = package_render_dir / "article.tex"
            tex.write_text(f"\\section{{Package {order}}}\n", encoding="utf-8")
            bib = package_render_dir / "article.bib"
            bib.write_text(self._bib(f"src-{order}"), encoding="utf-8")
            render_manifest = {
                "schema_version": "1.0",
                "issue_id": "2026-W32",
                "package_id": package_id,
                "passed": True,
                "basis": {"draft_package_sha256": draft_sha, "article_draft_sha256": "4" * 64, "prompt_sha256": "5" * 64},
                "tex": {"path": "article.tex", "sha256": hashlib.sha256(tex.read_bytes()).hexdigest(), "bytes": tex.stat().st_size},
                "bib": {"path": "article.bib", "sha256": hashlib.sha256(bib.read_bytes()).hexdigest(), "bytes": bib.stat().st_size, "entry_count": 1},
                "citation_keys": [f"src-{order}"],
            }
            (package_render_dir / "render-manifest.json").write_text(json.dumps(render_manifest), encoding="utf-8")

        draft_manifest_path = root / "draft-package-manifest.json"
        draft_manifest_path.write_text(json.dumps(draft_manifest), encoding="utf-8")
        template = root / "template.tex.in"
        template.write_text("ISSUE @@ISSUE_ID@@\n@@SECTION_INPUTS@@\nBIB", encoding="utf-8")
        return architecture_input, architecture_plan, draft_manifest_path, render_dir, template

    def test_complete_article_set_assembles_in_drafting_order(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = self._write_fixture(root, ["feature-a", "feature-b"])
            out = root / "assembled"
            manifest, passed = awi.assemble(*paths, out)
            self.assertTrue(passed, manifest)
            self.assertEqual(manifest["status"], "ARTICLE_ONLY_ASSEMBLED")
            self.assertEqual(manifest["assembled_article_package_count"], 2)
            self.assertEqual(manifest["section_inputs"], [
                "sections/generated/01-package-1.tex",
                "sections/generated/02-package-2.tex",
            ])
            main = (out / "main.tex").read_text(encoding="utf-8")
            self.assertLess(main.index("01-package-1"), main.index("02-package-2"))
            self.assertEqual((out / "references.bib").read_text().count("@online{"), 2)
            self.assertTrue(manifest["frontmatter_deferred"])

    def test_missing_render_manifest_blocks_assembly(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            architecture_input, architecture_plan, draft_manifest, render_dir, template = self._write_fixture(root, ["feature-a"])
            (render_dir / "package-1" / "render-manifest.json").unlink()
            out = root / "assembled"
            manifest, passed = awi.assemble(architecture_input, architecture_plan, draft_manifest, render_dir, template, out)
            self.assertFalse(passed)
            self.assertFalse((out / "main.tex").exists())
            self.assertTrue(any("missing render manifest" in error for error in manifest["errors"]))

    def test_render_sha_mismatch_blocks_assembly(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            architecture_input, architecture_plan, draft_manifest, render_dir, template = self._write_fixture(root, ["feature-a"])
            tex = render_dir / "package-1" / "article.tex"
            tex.write_text("tampered\n", encoding="utf-8")
            manifest, passed = awi.assemble(architecture_input, architecture_plan, draft_manifest, render_dir, template, root / "assembled")
            self.assertFalse(passed)
            self.assertTrue(any("SHA mismatch" in error for error in manifest["errors"]))

    def test_bibliography_conflict_blocks_final_main(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            architecture_input, architecture_plan, draft_manifest, render_dir, template = self._write_fixture(root, ["feature-a", "feature-b"])
            first_bib = render_dir / "package-1" / "article.bib"
            second_bib = render_dir / "package-2" / "article.bib"
            first_bib.write_text(self._bib("src-shared", "Title A"), encoding="utf-8")
            second_bib.write_text(self._bib("src-shared", "Title B"), encoding="utf-8")
            for order in (1, 2):
                package_dir = render_dir / f"package-{order}"
                manifest_path = package_dir / "render-manifest.json"
                value = json.loads(manifest_path.read_text())
                bib = package_dir / "article.bib"
                value["bib"] = {"path": "article.bib", "sha256": hashlib.sha256(bib.read_bytes()).hexdigest(), "bytes": bib.stat().st_size, "entry_count": 1}
                manifest_path.write_text(json.dumps(value), encoding="utf-8")
            manifest, passed = awi.assemble(architecture_input, architecture_plan, draft_manifest, render_dir, template, root / "assembled")
            self.assertFalse(passed)
            self.assertFalse((root / "assembled" / "main.tex").exists())
            self.assertTrue(any("bibliography merge failed" in error for error in manifest["errors"]))


if __name__ == "__main__":
    unittest.main()
