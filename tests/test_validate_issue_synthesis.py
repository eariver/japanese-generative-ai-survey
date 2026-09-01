from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts import validate_issue_synthesis as vis


class IssueSynthesisValidationTests(unittest.TestCase):
    def _input(self) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "status": "post-draft-synthesis-input-ready",
            "basis": {
                "architecture_input_sha256": "1" * 64,
                "architecture_plan_sha256": "2" * 64,
                "article_prompt_sha256": "3" * 64,
                "article_drafts": [],
            },
            "editorial_thesis": "Models move beyond checkpoints.",
            "cover_anchor_candidates": ["feature"],
            "articles": [
                {
                    "package_id": "feature",
                    "package_type": "FEATURE",
                    "drafting_order": 1,
                    "page_target": 2,
                    "late_breaking": False,
                    "editorial_angle": "Feature angle.",
                    "boundaries": ["Vendor claim only."],
                    "headline": "Feature headline",
                    "deck": "Feature deck",
                    "blocks": [{"block_id": "b1", "block_type": "PARAGRAPH", "text": "Feature text", "attribution_mode": "FACTUAL"}],
                },
                {
                    "package_id": "late",
                    "package_type": "LATE_BREAKING",
                    "drafting_order": 2,
                    "page_target": 1,
                    "late_breaking": True,
                    "editorial_angle": "Late angle.",
                    "boundaries": ["Post-cutoff event."],
                    "headline": "Late headline",
                    "deck": "Late deck",
                    "blocks": [{"block_id": "b2", "block_type": "LATE_BREAKING_NOTE", "text": "Post-cutoff text", "attribution_mode": "FACTUAL"}],
                },
            ],
            "constraints": {
                "language": "ja",
                "max_this_week_signals": 5,
                "no_new_external_facts": True,
                "summarize_only_validated_article_text": True,
                "late_breaking_boundary_required": True,
                "page_references_must_use_package_ids": True,
            },
        }

    def _result(self, input_path: Path, prompt_path: Path) -> dict:
        return {
            "schema_version": "1.0",
            "issue_id": "2026-W32",
            "synthesis_version": "v0.1",
            "status": "DRAFT",
            "basis": {
                "synthesis_input_sha256": hashlib.sha256(input_path.read_bytes()).hexdigest(),
                "prompt_id": "issue-synthesis-v0.1",
                "prompt_sha256": hashlib.sha256(prompt_path.read_bytes()).hexdigest(),
            },
            "runner": {
                "provider": "test",
                "model": "test-model",
                "invocation": "unit-test",
                "generated_at": "2026-08-10T00:00:00Z",
                "run_reference": None,
            },
            "cover": {
                "headline": "モデルの外側へ",
                "deck": "今号で見えた共通軸を読む。",
                "anchor_package_ids": ["feature"],
            },
            "this_week_signals": [
                {
                    "signal_id": "feature-signal",
                    "title": "Feature",
                    "summary": "Feature articleを要約する。",
                    "package_ids": ["feature"],
                    "late_breaking": False,
                },
                {
                    "signal_id": "late-signal",
                    "title": "Late Breaking",
                    "summary": "締切後情報としてLate articleを要約する。",
                    "package_ids": ["late"],
                    "late_breaking": True,
                },
            ],
        }

    def _write(self, root: Path) -> tuple[Path, Path, Path]:
        input_path = root / "input.json"
        input_path.write_text(json.dumps(self._input()), encoding="utf-8")
        prompt_path = root / "prompt.md"
        prompt_path.write_text("prompt", encoding="utf-8")
        result_path = root / "result.json"
        result_path.write_text(json.dumps(self._result(input_path, prompt_path)), encoding="utf-8")
        return input_path, result_path, prompt_path

    def test_valid_synthesis_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            input_path, result_path, prompt_path = self._write(Path(tmp))
            report, passed = vis.validate(input_path, result_path, prompt_path)
            self.assertTrue(passed, report)
            self.assertEqual(report["signal_count"], 2)

    def test_late_package_requires_late_signal_flag(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path, result_path, prompt_path = self._write(root)
            result = json.loads(result_path.read_text())
            result["this_week_signals"][1]["late_breaking"] = False
            result_path.write_text(json.dumps(result), encoding="utf-8")
            report, passed = vis.validate(input_path, result_path, prompt_path)
            self.assertFalse(passed)
            self.assertTrue(any("Late Breaking package" in error for error in report["errors"]))

    def test_late_signal_requires_explicit_post_cutoff_wording(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path, result_path, prompt_path = self._write(root)
            result = json.loads(result_path.read_text())
            result["this_week_signals"][1]["summary"] = "Late articleを要約する。"
            result_path.write_text(json.dumps(result), encoding="utf-8")
            report, passed = vis.validate(input_path, result_path, prompt_path)
            self.assertFalse(passed)
            self.assertTrue(any("post-cutoff wording" in error for error in report["errors"]))

    def test_unknown_package_reference_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path, result_path, prompt_path = self._write(root)
            result = json.loads(result_path.read_text())
            result["cover"]["anchor_package_ids"] = ["unknown"]
            result_path.write_text(json.dumps(result), encoding="utf-8")
            report, passed = vis.validate(input_path, result_path, prompt_path)
            self.assertFalse(passed)
            self.assertTrue(any("cover references unknown" in error for error in report["errors"]))

    def test_cover_anchor_must_come_from_architecture_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path, result_path, prompt_path = self._write(root)
            result = json.loads(result_path.read_text())
            result["cover"]["anchor_package_ids"] = ["late"]
            result["cover"]["headline"] = "後発情報を見る"
            result["cover"]["deck"] = "Late deckから考える。"
            result_path.write_text(json.dumps(result), encoding="utf-8")
            report, passed = vis.validate(input_path, result_path, prompt_path)
            self.assertFalse(passed)
            self.assertTrue(any("cover_anchor_candidates" in error for error in report["errors"]))

    def test_new_concrete_identifier_or_number_in_signal_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path, result_path, prompt_path = self._write(root)
            result = json.loads(result_path.read_text())
            result["this_week_signals"][0]["summary"] = "Feature articleはGPT-99で42%改善した。"
            result_path.write_text(json.dumps(result), encoding="utf-8")
            report, passed = vis.validate(input_path, result_path, prompt_path)
            self.assertFalse(passed)
            self.assertTrue(any("concrete ASCII identifiers/numbers" in error for error in report["errors"]))

    def test_input_sha_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path, result_path, prompt_path = self._write(root)
            result = json.loads(result_path.read_text())
            result["basis"]["synthesis_input_sha256"] = "0" * 64
            result_path.write_text(json.dumps(result), encoding="utf-8")
            report, passed = vis.validate(input_path, result_path, prompt_path)
            self.assertFalse(passed)
            self.assertTrue(any("synthesis_input_sha256" in error for error in report["errors"]))


if __name__ == "__main__":
    unittest.main()
