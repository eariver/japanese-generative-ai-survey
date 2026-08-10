from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import build_article_drafting_packages as builder
from scripts import validate_article_draft_run as validator


class ArticleDraftingPipelineTests(unittest.TestCase):
    def _write_json(self, path: Path, value) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding="utf-8")

    def _architecture_item(self, task_id: str, role: str, *, timing: str = "MAIN_EVENT", boundaries=None) -> dict:
        return {
            "evidence_task_id": task_id,
            "title": task_id,
            "role": role,
            "selection_rationale": "selected",
            "artifact_type": "MODEL_UPDATE",
            "organization": "Example",
            "timing_relation": timing,
            "event_dates": ["2026-08-05"],
            "evidence_status": "VERIFIED",
            "comparison_readiness": "READY_WITH_CAVEAT" if boundaries else "READY",
            "why_now_confirmed": True,
            "remaining_boundaries": boundaries or [],
            "evidence_class_counts": {"PRIMARY_FACT": 1},
            "source_class_counts": {"PRIMARY_OFFICIAL": 1},
        }

    def _architecture_input(self) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "status": "architecture-input-ready",
            "basis": {
                "selection_path": "selection.json",
                "selection_sha256": "1" * 64,
                "matrix_path": "matrix.json",
                "matrix_sha256": "2" * 64,
                "selection_version": "v0.1",
                "approval": {
                    "approved_by": "human",
                    "approved_at": "2026-08-16T00:00:00Z",
                    "approval_reference": "selection-review",
                },
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
                "FEATURE_CORE": [self._architecture_item("feature", "FEATURE_CORE", boundaries=["Vendor benchmark only."])],
                "SECTION_CORE": [],
                "PAPER_WATCH": [],
                "SUPPORTING_EVIDENCE": [self._architecture_item("support", "SUPPORTING_EVIDENCE", boundaries=["Social observation only."])],
                "LATE_BREAKING": [self._architecture_item("late", "LATE_BREAKING", timing="POST_CUTOFF", boundaries=["Post-cutoff event."])],
                "CHRONOLOGY": [],
                "WATCHLIST": [],
            },
            "not_selected_for_architecture": [],
            "selected_item_count": 3,
            "excluded_item_count": 0,
            "rules": ["test"],
        }

    def _plan(self, input_path: Path, approved: bool = True) -> dict:
        architecture_input = json.loads(input_path.read_text())
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "architecture_version": "v0.1",
            "status": "APPROVED" if approved else "PROPOSED",
            "basis": {
                "architecture_input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
                "selection_sha256": architecture_input["basis"]["selection_sha256"],
                "matrix_sha256": architecture_input["basis"]["matrix_sha256"],
            },
            "approval": {
                "approved_by": "human" if approved else None,
                "approved_at": "2026-08-16T00:30:00Z" if approved else None,
                "approval_reference": "architecture-review" if approved else None,
            },
            "editorial_thesis": "Evidence first.",
            "architecture_goals": ["Preserve boundaries."],
            "page_budget": {"target": 16, "max": 24, "planned": 5},
            "cover": {"headline_deferred": True, "headline": None, "anchor_candidates": ["feature"]},
            "packages": [
                {
                    "package_id": "frontmatter",
                    "title": "Frontmatter",
                    "package_type": "FRONTMATTER",
                    "primary_evidence_task_ids": [],
                    "supporting_evidence_task_ids": [],
                    "page_target": 1,
                    "editorial_angle": "Defer summary.",
                    "must_cover": ["Contents."],
                    "boundaries": [],
                    "late_breaking": False,
                    "drafting_order": 3,
                },
                {
                    "package_id": "feature",
                    "title": "Feature",
                    "package_type": "FEATURE",
                    "primary_evidence_task_ids": ["feature"],
                    "supporting_evidence_task_ids": ["support"],
                    "page_target": 2,
                    "editorial_angle": "Explain verified core and claim boundary.",
                    "must_cover": ["Evidence boundaries."],
                    "boundaries": ["Vendor benchmark only.", "Social observation only."],
                    "late_breaking": False,
                    "drafting_order": 1,
                },
                {
                    "package_id": "late-breaking",
                    "title": "Late Breaking",
                    "package_type": "LATE_BREAKING",
                    "primary_evidence_task_ids": ["late"],
                    "supporting_evidence_task_ids": [],
                    "page_target": 1,
                    "editorial_angle": "Keep post-cutoff separate.",
                    "must_cover": ["Post-cutoff chronology."],
                    "boundaries": ["Post-cutoff event."],
                    "late_breaking": True,
                    "drafting_order": 2,
                },
                {
                    "package_id": "references",
                    "title": "References",
                    "package_type": "REFERENCES",
                    "primary_evidence_task_ids": [],
                    "supporting_evidence_task_ids": [],
                    "page_target": 1,
                    "editorial_angle": "Render references.",
                    "must_cover": ["Sources."],
                    "boundaries": [],
                    "late_breaking": False,
                    "drafting_order": 4,
                },
            ],
            "this_week_summary_written_last": True,
        }

    def _card(self, task_id: str, *, social: bool = False) -> dict:
        source_class = "SOCIAL" if social else "PRIMARY_OFFICIAL"
        evidence_class = "SOCIAL_OBSERVATION" if social else "PRIMARY_FACT"
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "evidence_task_id": task_id,
            "status": "VERIFIED",
            "grouping_resolution": {"accepted": True, "split_recommended": False, "note": None},
            "artifact": {"canonical_name": task_id, "artifact_type": "MODEL_UPDATE", "organization": "Example", "canonical_url": f"https://example.com/{task_id}"},
            "temporal": {
                "artifact_first_announced": "2026-08-05",
                "observed_at": "2026-08-16T00:00:00Z",
                "events": [
                    {"event_type": "MODEL_UPDATE", "event_date": "2026-08-05", "source_published_at": "2026-08-05", "source_ids": ["s1"]}
                ],
            },
            "sources": [
                {"source_id": "s1", "url": f"https://example.com/{task_id}/source", "source_class": source_class, "title": f"{task_id} source", "published_at": "2026-08-05", "accessed_at": "2026-08-16T00:00:00Z", "role": "primary"}
            ],
            "claims": [
                {"claim_id": "c1", "text": "Artifact exists.", "evidence_class": evidence_class, "source_ids": ["s1"], "context": None},
                {"claim_id": "c2", "text": "Vendor says benchmark improved.", "evidence_class": "VENDOR_CLAIM" if not social else "SOCIAL_OBSERVATION", "source_ids": ["s1"], "context": "claim context"},
            ],
            "metrics": [],
            "limitations": [
                {"limitation_id": "l1", "text": "No independent reproduction.", "evidence_class": "INFERENCE", "source_ids": ["s1"]}
            ],
            "verification": {"targets": [], "unresolved_questions": [], "contradictions": []},
            "editorial": {"why_now_confirmed": True, "why_now_note": "test", "candidate_recommendation": "CANDIDATE", "rationale": "test"},
        }

    def _write_fixture(self, root: Path, *, approved: bool = True):
        architecture_input = root / "architecture-input.json"
        self._write_json(architecture_input, self._architecture_input())
        plan = root / "architecture-plan.json"
        self._write_json(plan, self._plan(architecture_input, approved=approved))
        evidence = root / "evidence-reviewed.jsonl"
        items = []
        for task_id, social in (("feature", False), ("support", True), ("late", False)):
            items.append({
                "schema_version": "1.0",
                "issue_id": "2026-W33",
                "evidence_task_id": task_id,
                "task_file": f"{task_id}.json",
                "run_file": f"{task_id}.json",
                "runner": {"provider": "test", "model": "model", "invocation": "unit"},
                "evidence_task_sha256": "0" * 64,
                "prompt_id": "primary-source-verification-v0.1",
                "prompt_sha256": "1" * 64,
                "card": self._card(task_id, social=social),
            })
        evidence.write_text("".join(json.dumps(item) + "\n" for item in items), encoding="utf-8")
        style = root / "style.md"
        style.write_text("Editorial style", encoding="utf-8")
        prompt = root / "draft-prompt.md"
        prompt.write_bytes(Path("config/prompts/editorial/article-drafting-v0.1.md").read_bytes())
        return architecture_input, plan, evidence, style, prompt

    def test_builder_requires_approved_architecture_and_sets_runner_modes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            architecture_input, plan, evidence, style, _ = self._write_fixture(root)
            out = root / "packages"
            manifest, passed = builder.build(architecture_input, plan, evidence, style, out)
            self.assertTrue(passed, manifest)
            self.assertEqual(manifest["package_count"], 4)
            modes = {item["package_id"]: item["runner_mode"] for item in manifest["packages"]}
            self.assertEqual(modes["feature"], "LLM_DRAFT")
            self.assertEqual(modes["late-breaking"], "LLM_DRAFT")
            self.assertEqual(modes["frontmatter"], "DEFERRED_FRONTMATTER")
            self.assertEqual(modes["references"], "DETERMINISTIC_REFERENCES")
            feature = json.loads((out / "01-feature.json").read_text())
            self.assertEqual(len(feature["primary_evidence"]), 1)
            self.assertEqual(len(feature["supporting_evidence"]), 1)
            self.assertEqual(len(feature["source_catalog"]), 2)
            self.assertTrue(all(item["citation_key"].startswith("ev-") for item in feature["source_catalog"]))

    def test_builder_rejects_proposed_architecture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            architecture_input, plan, evidence, style, _ = self._write_fixture(root, approved=False)
            with self.assertRaises(ValueError):
                builder.build(architecture_input, plan, evidence, style, root / "packages")

    def _valid_feature_run(self, package: Path, prompt: Path) -> dict:
        pkg = json.loads(package.read_text())
        primary_key = next(item["citation_key"] for item in pkg["source_catalog"] if item["evidence_task_id"] == "feature")
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "package_id": "feature",
            "drafting_package_sha256": hashlib.sha256(package.read_bytes()).hexdigest(),
            "prompt_id": "article-drafting-v0.1",
            "prompt_sha256": hashlib.sha256(prompt.read_bytes()).hexdigest(),
            "runner": {"provider": "test", "model": "model", "invocation": "unit", "generated_at": "2026-08-16T01:00:00Z", "run_reference": None},
            "draft": {
                "status": "DRAFTED",
                "title": "Feature draft",
                "dek": None,
                "latex_body": f"Artifact exists. \\autocite{{{primary_key}}}",
                "evidence_task_ids_used": ["feature"],
                "claim_ledger": [
                    {
                        "draft_claim_id": "d1",
                        "text": "Artifact exists.",
                        "evidence_class": "PRIMARY_FACT",
                        "assertion_mode": "FACT",
                        "evidence_refs": [
                            {"evidence_task_id": "feature", "claim_ids": ["c1"], "metric_ids": [], "limitation_ids": [], "event_indices": [], "source_ids": ["s1"]}
                        ],
                        "citation_keys": [primary_key],
                        "boundary_note": None,
                    }
                ],
                "must_cover_coverage": [
                    {"requirement": "Evidence boundaries.", "status": "COVERED", "note": "Handled in prose."}
                ],
                "boundary_coverage": [
                    {"boundary": "Vendor benchmark only.", "status": "PRESERVED", "note": "Not stated as independent fact."},
                    {"boundary": "Social observation only.", "status": "PRESERVED", "note": "Not used as technical fact."},
                ],
                "open_questions": [],
            },
        }

    def test_valid_draft_run_passes_and_vendor_laundering_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            architecture_input, plan, evidence, style, prompt = self._write_fixture(root)
            out = root / "packages"
            builder.build(architecture_input, plan, evidence, style, out)
            package = out / "01-feature.json"
            run_path = root / "run.json"
            run = self._valid_feature_run(package, prompt)
            self._write_json(run_path, run)
            report, passed = validator.validate(package, run_path, prompt)
            self.assertTrue(passed, report)

            run["draft"]["claim_ledger"][0]["evidence_refs"][0]["claim_ids"] = ["c2"]
            self._write_json(run_path, run)
            report, passed = validator.validate(package, run_path, prompt)
            self.assertFalse(passed)
            self.assertTrue(any("does not match referenced Evidence classes" in error for error in report["errors"]))

    def test_unknown_body_citation_and_missing_latebreaking_treatment_fail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            architecture_input, plan, evidence, style, prompt = self._write_fixture(root)
            out = root / "packages"
            builder.build(architecture_input, plan, evidence, style, out)
            package = out / "01-feature.json"
            run = self._valid_feature_run(package, prompt)
            run["draft"]["latex_body"] += " \\autocite{unknown-key}"
            run_path = root / "run.json"
            self._write_json(run_path, run)
            report, passed = validator.validate(package, run_path, prompt)
            self.assertFalse(passed)
            self.assertTrue(any("package-external keys" in error for error in report["errors"]))

            late_package = out / "02-late-breaking.json"
            pkg = json.loads(late_package.read_text())
            key = pkg["source_catalog"][0]["citation_key"]
            late_run = {
                "schema_version": "1.0",
                "issue_id": "2026-W33",
                "package_id": "late-breaking",
                "drafting_package_sha256": hashlib.sha256(late_package.read_bytes()).hexdigest(),
                "prompt_id": "article-drafting-v0.1",
                "prompt_sha256": hashlib.sha256(prompt.read_bytes()).hexdigest(),
                "runner": {"provider": "test", "model": "model", "invocation": "unit", "generated_at": "2026-08-16T01:00:00Z", "run_reference": None},
                "draft": {
                    "status": "DRAFTED",
                    "title": "Late",
                    "dek": None,
                    "latex_body": f"Post-cutoff event. \\autocite{{{key}}}",
                    "evidence_task_ids_used": ["late"],
                    "claim_ledger": [
                        {
                            "draft_claim_id": "d1",
                            "text": "Post-cutoff event.",
                            "evidence_class": "PRIMARY_FACT",
                            "assertion_mode": "FACT",
                            "evidence_refs": [{"evidence_task_id": "late", "claim_ids": ["c1"], "metric_ids": [], "limitation_ids": [], "event_indices": [], "source_ids": ["s1"]}],
                            "citation_keys": [key],
                            "boundary_note": None,
                        }
                    ],
                    "must_cover_coverage": [{"requirement": "Post-cutoff chronology.", "status": "COVERED", "note": None}],
                    "boundary_coverage": [{"boundary": "Post-cutoff event.", "status": "PRESERVED", "note": None}],
                    "open_questions": [],
                },
            }
            self._write_json(run_path, late_run)
            report, passed = validator.validate(late_package, run_path, prompt)
            self.assertFalse(passed)
            self.assertTrue(any("latebreaking LaTeX treatment" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
