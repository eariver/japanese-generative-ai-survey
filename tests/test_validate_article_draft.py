from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import validate_article_draft as vad


class ArticleDraftValidationTests(unittest.TestCase):
    def _evidence(self, task_id: str, *, social: bool = False) -> dict:
        evidence_class = "SOCIAL_OBSERVATION" if social else "PRIMARY_FACT"
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "evidence_task_id": task_id,
            "card": {
                "evidence_task_id": task_id,
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
                "claims": [
                    {
                        "claim_id": "claim-main",
                        "text": "Social reaction" if social else "Release exists",
                        "evidence_class": evidence_class,
                        "source_ids": ["s1"],
                        "context": None,
                    }
                ],
                "metrics": ([] if social else [
                    {
                        "metric_id": "metric-vendor",
                        "name": "benchmark",
                        "value": "42",
                        "unit": "points",
                        "context": "vendor benchmark",
                        "evidence_class": "VENDOR_CLAIM",
                        "source_ids": ["s1"],
                    }
                ]),
                "limitations": [
                    {
                        "limitation_id": "limit-main",
                        "text": "Social observation only." if social else "Vendor benchmark only.",
                        "evidence_class": "INFERENCE",
                        "source_ids": ["s1"],
                    }
                ],
            },
        }

    def _package(self, *, late: bool = False) -> dict:
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
                "package_type": "LATE_BREAKING" if late else "FEATURE",
                "page_target": 2,
                "editorial_angle": "Explain the update.",
                "must_cover": ["Mechanics", "Community reaction"],
                "boundaries": ["Vendor benchmark only.", "Social observation only."],
                "late_breaking": late,
                "drafting_order": 1,
            },
            "primary_evidence": [self._evidence("feature")],
            "supporting_evidence": [self._evidence("social", social=True)],
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

    def _draft(self, package_path: Path, prompt_path: Path, *, late: bool = False) -> dict:
        blocks = [
            {
                "block_id": "mechanics",
                "block_type": "PARAGRAPH",
                "text": "更新が公開された。",
                "attribution_mode": "FACTUAL",
                "evidence_refs": [self._ref("feature", "EVENT", "event-release")],
            },
            {
                "block_id": "vendor-boundary",
                "block_type": "CLAIM_BOUNDARY",
                "text": "性能値はベンダー報告である。",
                "attribution_mode": "ATTRIBUTED",
                "evidence_refs": [self._ref("feature", "METRIC", "metric-vendor")],
            },
            {
                "block_id": "community",
                "block_type": "COMMUNITY_NOTE",
                "text": "コミュニティでは反応が観測された。",
                "attribution_mode": "SOCIAL",
                "evidence_refs": [self._ref("social", "CLAIM", "claim-main")],
            },
        ]
        if late:
            blocks.append(
                {
                    "block_id": "late-note",
                    "block_type": "LATE_BREAKING_NOTE",
                    "text": "この更新は締切後情報として扱う。",
                    "attribution_mode": "FACTUAL",
                    "evidence_refs": [self._ref("feature", "EVENT", "event-release")],
                }
            )
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
            "headline": "更新をどう読むか",
            "deck": "更新が公開され、コミュニティ反応も観測された。",
            "deck_attribution_mode": "MIXED",
            "deck_evidence_refs": [
                self._ref("feature", "EVENT", "event-release"),
                self._ref("social", "CLAIM", "claim-main"),
            ],
            "blocks": blocks,
            "must_cover_coverage": [
                {"requirement": "Mechanics", "block_ids": ["mechanics"]},
                {"requirement": "Community reaction", "block_ids": ["community"]},
            ],
            "boundary_coverage": [
                {"requirement": "Vendor benchmark only.", "block_ids": ["vendor-boundary"]},
                {"requirement": "Social observation only.", "block_ids": ["community"]},
            ],
            "late_breaking_acknowledged": late,
        }

    def _write(self, root: Path, *, late: bool = False) -> tuple[Path, Path, Path]:
        package_path = root / "package.json"
        package_path.write_text(json.dumps(self._package(late=late)), encoding="utf-8")
        prompt_path = root / "prompt.md"
        prompt_path.write_text("prompt", encoding="utf-8")
        draft_path = root / "draft.json"
        draft_path.write_text(json.dumps(self._draft(package_path, prompt_path, late=late)), encoding="utf-8")
        return package_path, draft_path, prompt_path

    def test_valid_article_draft_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            package, draft, prompt = self._write(Path(tmp))
            report, passed = vad.validate(package, draft, prompt)
            self.assertTrue(passed, report)
            self.assertEqual(report["used_evidence_task_count"], 2)
            self.assertEqual(report["social_block_count"], 1)

    def test_vendor_claim_cannot_be_factual(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package, draft, prompt = self._write(root)
            value = json.loads(draft.read_text())
            value["blocks"][1]["attribution_mode"] = "FACTUAL"
            draft.write_text(json.dumps(value), encoding="utf-8")
            report, passed = vad.validate(package, draft, prompt)
            self.assertFalse(passed)
            self.assertTrue(any("FACTUAL block contains non-factual" in error for error in report["errors"]))

    def test_social_evidence_must_be_community_note(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package, draft, prompt = self._write(root)
            value = json.loads(draft.read_text())
            value["blocks"][2]["block_type"] = "PARAGRAPH"
            draft.write_text(json.dumps(value), encoding="utf-8")
            report, passed = vad.validate(package, draft, prompt)
            self.assertFalse(passed)
            self.assertTrue(any("COMMUNITY_NOTE" in error for error in report["errors"]))

    def test_all_architecture_included_evidence_must_be_used(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package, draft, prompt = self._write(root)
            value = json.loads(draft.read_text())
            value["deck_evidence_refs"] = [self._ref("feature", "EVENT", "event-release")]
            value["deck_attribution_mode"] = "FACTUAL"
            value["blocks"] = value["blocks"][:2]
            value["must_cover_coverage"][1]["block_ids"] = ["mechanics"]
            value["boundary_coverage"][1]["block_ids"] = ["mechanics"]
            draft.write_text(json.dumps(value), encoding="utf-8")
            report, passed = vad.validate(package, draft, prompt)
            self.assertFalse(passed)
            self.assertIn("social", report["missing_evidence_task_usage"])

    def test_requirement_coverage_must_match_package(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package, draft, prompt = self._write(root)
            value = json.loads(draft.read_text())
            value["must_cover_coverage"] = value["must_cover_coverage"][:1]
            draft.write_text(json.dumps(value), encoding="utf-8")
            report, passed = vad.validate(package, draft, prompt)
            self.assertFalse(passed)
            self.assertTrue(any("missing package requirements" in error for error in report["errors"]))

    def test_late_breaking_package_requires_acknowledged_note(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package, draft, prompt = self._write(root, late=True)
            value = json.loads(draft.read_text())
            value["late_breaking_acknowledged"] = False
            value["blocks"] = [block for block in value["blocks"] if block["block_type"] != "LATE_BREAKING_NOTE"]
            draft.write_text(json.dumps(value), encoding="utf-8")
            report, passed = vad.validate(package, draft, prompt)
            self.assertFalse(passed)
            self.assertTrue(any("Late Breaking package requires" in error for error in report["errors"]))

    def test_package_hash_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            package, draft, prompt = self._write(root)
            value = json.loads(draft.read_text())
            value["basis"]["draft_package_sha256"] = "0" * 64
            draft.write_text(json.dumps(value), encoding="utf-8")
            report, passed = vad.validate(package, draft, prompt)
            self.assertFalse(passed)
            self.assertTrue(any("draft_package_sha256" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
