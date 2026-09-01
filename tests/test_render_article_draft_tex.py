from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import render_article_draft_tex as radt


class ArticleDraftRendererTests(unittest.TestCase):
    def _primary(self) -> dict:
        return {
            "issue_id": "2026-W32",
            "evidence_task_id": "feature",
            "card": {
                "evidence_task_id": "feature",
                "artifact": {"organization": "Example Org"},
                "temporal": {
                    "events": [
                        {
                            "event_id": "event-release",
                            "event_type": "MODEL_UPDATE",
                            "event_date": "2026-08-05",
                            "source_published_at": "2026-08-05",
                            "source_ids": ["s1"],
                        }
                    ]
                },
                "sources": [
                    {
                        "source_id": "s1",
                        "url": "https://example.com/release",
                        "source_class": "PRIMARY_OFFICIAL",
                        "title": "Example Release 50%",
                        "published_at": "2026-08-05",
                        "accessed_at": "2026-08-10T00:00:00Z",
                        "role": "official release note",
                    }
                ],
                "claims": [
                    {
                        "claim_id": "claim-main",
                        "text": "Release exists.",
                        "evidence_class": "PRIMARY_FACT",
                        "source_ids": ["s1"],
                        "context": None,
                    }
                ],
                "metrics": [
                    {
                        "metric_id": "metric-vendor",
                        "name": "speed",
                        "value": "50",
                        "unit": "%",
                        "context": "vendor setup",
                        "evidence_class": "VENDOR_CLAIM",
                        "source_ids": ["s1"],
                    }
                ],
                "limitations": [
                    {
                        "limitation_id": "limit-vendor",
                        "text": "Vendor benchmark only.",
                        "evidence_class": "INFERENCE",
                        "source_ids": ["s1"],
                    }
                ],
            },
        }

    def _social(self) -> dict:
        return {
            "issue_id": "2026-W32",
            "evidence_task_id": "social",
            "card": {
                "evidence_task_id": "social",
                "artifact": {"organization": "Community"},
                "temporal": {"events": []},
                "sources": [
                    {
                        "source_id": "x1",
                        "url": "https://example.com/social/post",
                        "source_class": "SOCIAL",
                        "title": "Community post",
                        "published_at": "2026-08-06",
                        "accessed_at": "2026-08-10T00:00:00Z",
                        "role": "community observation",
                    }
                ],
                "claims": [
                    {
                        "claim_id": "claim-social",
                        "text": "A community observation exists.",
                        "evidence_class": "SOCIAL_OBSERVATION",
                        "source_ids": ["x1"],
                        "context": None,
                    }
                ],
                "metrics": [],
                "limitations": [
                    {
                        "limitation_id": "limit-social",
                        "text": "Social observation only.",
                        "evidence_class": "INFERENCE",
                        "source_ids": ["x1"],
                    }
                ],
            },
        }

    def _package(self) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "package_id": "feature-package",
            "draft_source_mode": "EVIDENCE_PACKAGE",
            "execution_stage": "ARTICLE_DRAFTING",
            "basis": {
                "architecture_plan_sha256": "1" * 64,
                "architecture_input_sha256": "2" * 64,
                "evidence_reviewed_sha256": "3" * 64,
            },
            "package": {
                "title": "Feature",
                "package_type": "FEATURE",
                "page_target": 2,
                "editorial_angle": "Explain it.",
                "must_cover": ["Mechanics", "Comparison", "Community"],
                "boundaries": ["Vendor benchmark only.", "Social observation only."],
                "late_breaking": False,
                "drafting_order": 1,
            },
            "primary_evidence": [self._primary()],
            "supporting_evidence": [self._social()],
            "drafting_constraints": {
                "language": "ja",
                "raw_sources_forbidden": True,
                "unknowns_remain_unknown": True,
                "citation_granularity": "EVENT_CLAIM_METRIC_LIMITATION",
                "cover_headline_finalization_forbidden": True,
                "this_week_summary_forbidden": True,
            },
        }

    def _ref(self, task: str, kind: str, evidence_id: str) -> dict:
        return {"evidence_task_id": task, "kind": kind, "evidence_id": evidence_id}

    def _draft(self, package_path: Path, prompt_path: Path) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "package_id": "feature-package",
            "draft_version": "v0.1",
            "status": "DRAFT",
            "basis": {
                "draft_package_sha256": hashlib.sha256(package_path.read_bytes()).hexdigest(),
                "prompt_id": "article-drafting-v0.1",
                "prompt_sha256": hashlib.sha256(prompt_path.read_bytes()).hexdigest(),
            },
            "runner": {
                "provider": "test",
                "model": "test-model",
                "invocation": "unit-test",
                "generated_at": "2026-08-10T00:00:00Z",
                "run_reference": None,
            },
            "headline": "foo_barをどう読むか",
            "deck": "更新が公開された。",
            "deck_attribution_mode": "FACTUAL",
            "deck_evidence_refs": [self._ref("feature", "EVENT", "event-release")],
            "blocks": [
                {
                    "block_id": "heading",
                    "block_type": "HEADING",
                    "text": "技術的な意味",
                    "attribution_mode": "NONE",
                    "evidence_refs": [],
                },
                {
                    "block_id": "mechanics",
                    "block_type": "PARAGRAPH",
                    "text": "foo_barでは50%という表記もLaTeXへ安全に渡す。",
                    "attribution_mode": "FACTUAL",
                    "evidence_refs": [self._ref("feature", "EVENT", "event-release")],
                },
                {
                    "block_id": "comparison",
                    "block_type": "TABLE",
                    "text": "| 項目 | 値 |\n|---|---|\n| speed_1 | 50% |",
                    "attribution_mode": "ATTRIBUTED",
                    "evidence_refs": [self._ref("feature", "METRIC", "metric-vendor")],
                },
                {
                    "block_id": "vendor-boundary",
                    "block_type": "CLAIM_BOUNDARY",
                    "text": "性能値はベンダー報告であり、独立再現ではない。",
                    "attribution_mode": "MIXED",
                    "evidence_refs": [
                        self._ref("feature", "METRIC", "metric-vendor"),
                        self._ref("feature", "LIMITATION", "limit-vendor"),
                    ],
                },
                {
                    "block_id": "community",
                    "block_type": "COMMUNITY_NOTE",
                    "text": "コミュニティで観測された反応であり、技術検証ではない。",
                    "attribution_mode": "SOCIAL",
                    "evidence_refs": [self._ref("social", "CLAIM", "claim-social")],
                },
            ],
            "must_cover_coverage": [
                {"requirement": "Mechanics", "block_ids": ["mechanics"]},
                {"requirement": "Comparison", "block_ids": ["comparison"]},
                {"requirement": "Community", "block_ids": ["community"]},
            ],
            "boundary_coverage": [
                {"requirement": "Vendor benchmark only.", "block_ids": ["vendor-boundary"]},
                {"requirement": "Social observation only.", "block_ids": ["community"]},
            ],
            "late_breaking_acknowledged": False,
        }

    def test_renderer_generates_safe_tex_and_url_hash_bibliography(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package = root / "package.json"
            package.write_text(json.dumps(self._package()), encoding="utf-8")
            prompt = root / "prompt.md"
            prompt.write_text("prompt", encoding="utf-8")
            draft = root / "draft.json"
            draft.write_text(json.dumps(self._draft(package, prompt)), encoding="utf-8")
            tex = root / "article.tex"
            bib = root / "article.bib"
            manifest_path = root / "render.json"

            manifest, passed = radt.render(package, draft, prompt, tex, bib, manifest_path)
            self.assertTrue(passed, manifest)
            text = tex.read_text(encoding="utf-8")
            bibliography = bib.read_text(encoding="utf-8")
            self.assertIn(r"\section{foo\_barをどう読むか}", text)
            self.assertIn(r"50\%", text)
            self.assertIn(r"speed\_1", text)
            self.assertIn(r"\begin{claimboundary}", text)
            self.assertIn(r"\begin{communitynote}", text)
            self.assertIn(r"\begin{tabularx}{\columnwidth}", text)
            self.assertIn(r"\autocite{src-", text)
            self.assertEqual(manifest["bib"]["entry_count"], 2)
            self.assertIn("https://example.com/release", bibliography)
            self.assertIn("https://example.com/social/post", bibliography)
            self.assertIn(r"Example Release 50\%", bibliography)

    def test_citation_key_is_stable_per_url(self) -> None:
        self.assertEqual(
            radt.cite_key("https://example.com/release"),
            radt.cite_key("https://example.com/release"),
        )
        self.assertNotEqual(
            radt.cite_key("https://example.com/release"),
            radt.cite_key("https://example.com/other"),
        )


if __name__ == "__main__":
    unittest.main()
