from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import materialize_article_draft as mat


class ArticleMaterializationTests(unittest.TestCase):
    def _package(self, *, late: bool = False, social: bool = False) -> dict:
        primary_claim_class = "SOCIAL_OBSERVATION" if social else "PRIMARY_FACT"
        source_class = "SOCIAL" if social else "PRIMARY_OFFICIAL"
        block_boundary = ["Community observation only."] if social else ["Vendor benchmark only."]
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "package_id": "test-package",
            "draft_source_mode": "EVIDENCE_PACKAGE",
            "execution_stage": "ARTICLE_DRAFTING",
            "basis": {
                "architecture_plan_sha256": "1" * 64,
                "architecture_input_sha256": "2" * 64,
                "evidence_reviewed_sha256": "3" * 64,
            },
            "package": {
                "title": "Test package",
                "package_type": "LATE_BREAKING" if late else "FEATURE",
                "page_target": 1,
                "editorial_angle": "test",
                "must_cover": ["Release mechanics"],
                "boundaries": block_boundary,
                "late_breaking": late,
                "drafting_order": 1,
            },
            "primary_evidence": [
                {
                    "schema_version": "1.0",
                    "issue_id": "2026-W33",
                    "evidence_task_id": "task-main",
                    "card": {
                        "evidence_task_id": "task-main",
                        "temporal": {
                            "events": [
                                {
                                    "event_id": "event-release",
                                    "event_type": "MODEL_UPDATE",
                                    "event_date": "2026-08-14",
                                    "source_published_at": "2026-08-14",
                                    "source_ids": ["s1"],
                                }
                            ]
                        },
                        "sources": [
                            {
                                "source_id": "s1",
                                "url": "https://example.com/release",
                                "source_class": source_class,
                                "title": "Example Release & Notes",
                                "published_at": "2026-08-14",
                                "accessed_at": "2026-08-16T00:00:00Z",
                                "role": "primary",
                            }
                        ],
                        "claims": [
                            {
                                "claim_id": "claim-main",
                                "text": "Observation" if social else "Release exists",
                                "evidence_class": primary_claim_class,
                                "source_ids": ["s1"],
                                "context": None,
                            }
                        ],
                        "metrics": [
                            {
                                "metric_id": "metric-vendor",
                                "name": "benchmark",
                                "value": "42",
                                "unit": "points",
                                "context": "vendor benchmark",
                                "evidence_class": "VENDOR_CLAIM",
                                "source_ids": ["s1"],
                            }
                        ] if not social else [],
                        "limitations": [
                            {
                                "limitation_id": "limit-main",
                                "text": block_boundary[0],
                                "evidence_class": "INFERENCE",
                                "source_ids": ["s1"],
                            }
                        ],
                    },
                }
            ],
            "supporting_evidence": [],
            "drafting_constraints": {
                "language": "ja",
                "raw_sources_forbidden": True,
                "unknowns_remain_unknown": True,
                "citation_granularity": "EVENT_CLAIM_METRIC_LIMITATION",
                "cover_headline_finalization_forbidden": True,
                "this_week_summary_forbidden": True,
            },
        }

    def _draft(self, package_path: Path, prompt_path: Path, *, late: bool = False, social: bool = False) -> dict:
        if social:
            body_block = {
                "block_id": "community",
                "block_type": "COMMUNITY_NOTE",
                "text": "コミュニティ観測である。",
                "attribution_mode": "SOCIAL",
                "evidence_refs": [{"evidence_task_id": "task-main", "kind": "CLAIM", "evidence_id": "claim-main"}],
            }
            deck_mode = "SOCIAL"
            deck_refs = [{"evidence_task_id": "task-main", "kind": "CLAIM", "evidence_id": "claim-main"}]
        else:
            body_block = {
                "block_id": "mechanics",
                "block_type": "PARAGRAPH",
                "text": "更新が公開された。",
                "attribution_mode": "FACTUAL",
                "evidence_refs": [
                    {"evidence_task_id": "task-main", "kind": "EVENT", "evidence_id": "event-release"},
                    {"evidence_task_id": "task-main", "kind": "CLAIM", "evidence_id": "claim-main"},
                ],
            }
            deck_mode = "FACTUAL"
            deck_refs = [{"evidence_task_id": "task-main", "kind": "EVENT", "evidence_id": "event-release"}]

        blocks = [body_block]
        if not social:
            blocks.append(
                {
                    "block_id": "boundary",
                    "block_type": "CLAIM_BOUNDARY",
                    "text": "42 pointsはベンダー報告である。",
                    "attribution_mode": "ATTRIBUTED",
                    "evidence_refs": [{"evidence_task_id": "task-main", "kind": "METRIC", "evidence_id": "metric-vendor"}],
                }
            )
        if late:
            blocks.append(
                {
                    "block_id": "late-note",
                    "block_type": "LATE_BREAKING_NOTE",
                    "text": "締切後情報として扱う。",
                    "attribution_mode": "FACTUAL",
                    "evidence_refs": [{"evidence_task_id": "task-main", "kind": "EVENT", "evidence_id": "event-release"}],
                }
            )

        coverage_block = body_block["block_id"]
        boundary_block = body_block["block_id"] if social else "boundary"
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W33",
            "package_id": "test-package",
            "draft_version": "v0.1",
            "status": "DRAFT",
            "basis": {
                "draft_package_sha256": hashlib.sha256(package_path.read_bytes()).hexdigest(),
                "prompt_id": "article-drafting-v0.1",
                "prompt_sha256": hashlib.sha256(prompt_path.read_bytes()).hexdigest(),
            },
            "runner": {
                "provider": "test",
                "model": "model",
                "invocation": "unit-test",
                "generated_at": "2026-08-16T00:00:00Z",
                "run_reference": None,
            },
            "headline": "構造化Draft",
            "deck": "今週の更新をEvidenceに沿って読む。",
            "deck_attribution_mode": deck_mode,
            "deck_evidence_refs": deck_refs,
            "blocks": blocks,
            "must_cover_coverage": [{"requirement": "Release mechanics", "block_ids": [coverage_block]}],
            "boundary_coverage": [{"requirement": self._package(late=late, social=social)["package"]["boundaries"][0], "block_ids": [boundary_block]}],
            "late_breaking_acknowledged": late,
        }

    def _write_fixture(self, root: Path, *, late: bool = False, social: bool = False):
        package_path = root / "package.json"
        package_path.write_text(json.dumps(self._package(late=late, social=social)), encoding="utf-8")
        prompt_path = root / "prompt.md"
        prompt_path.write_bytes(Path("config/prompts/editorial/article-drafting-v0.1.md").read_bytes())
        draft_path = root / "draft.json"
        draft_path.write_text(json.dumps(self._draft(package_path, prompt_path, late=late, social=social)), encoding="utf-8")
        return package_path, draft_path, prompt_path

    def test_materializes_deduplicated_citations_and_claim_box(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package, draft, prompt = self._write_fixture(root)
            out = root / "out"
            manifest, passed = mat.materialize(package, draft, prompt, out)
            self.assertTrue(passed, manifest)
            self.assertEqual(manifest["citation_count"], 1)
            key = mat.citation_key("https://example.com/release")
            tex = (out / "test-package.tex").read_text(encoding="utf-8")
            bib = (out / "test-package.bib").read_text(encoding="utf-8")
            self.assertIn("\\section{構造化Draft}", tex)
            self.assertIn(f"\\autocite{{{key}}}", tex)
            self.assertIn("\\begin{claimboundary}", tex)
            self.assertIn(f"@online{{{key},", bib)
            self.assertEqual(bib.count(f"@online{{{key},"), 1)

    def test_social_and_late_blocks_map_to_shared_survey_boxes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package, draft, prompt = self._write_fixture(root, social=True)
            out = root / "social"
            mat.materialize(package, draft, prompt, out)
            tex = (out / "test-package.tex").read_text(encoding="utf-8")
            self.assertIn("\\begin{communitynote}", tex)

            package, draft, prompt = self._write_fixture(root / "late", late=True)
            out = root / "late-out"
            mat.materialize(package, draft, prompt, out)
            tex = (out / "test-package.tex").read_text(encoding="utf-8")
            self.assertIn("\\begin{latebreaking}", tex)

    def test_table_block_requires_consistent_pipe_rows(self) -> None:
        with self.assertRaises(ValueError):
            mat.parse_table("A | B\n1 | 2 | 3")
        rows = mat.parse_table("A | B\n--- | ---\n1 | 2")
        self.assertEqual(rows, [["A", "B"], ["1", "2"]])


if __name__ == "__main__":
    unittest.main()
