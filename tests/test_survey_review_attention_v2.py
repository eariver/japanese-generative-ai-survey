from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts import survey_production_v2 as core
from scripts import survey_review_attention_v2 as attention


class SurveyReviewAttentionV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.source_root = Path(".").resolve()
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        src = self.source_root / attention.ATTENTION_SCHEMA
        dst = self.root / attention.ATTENTION_SCHEMA
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        (self.root / "sources/SP001").mkdir(parents=True)

    def _write_inputs(self) -> tuple[Path, Path, Path]:
        screening = self.root / "sources/SP001/screening-accepted.json"
        materiality = self.root / "sources/SP001/materiality-ledger.json"
        selection = self.root / "sources/SP001/candidate-selection.json"
        core.write_json(
            screening,
            {
                "issue_id": "SP001",
                "decisions": [
                    {"discovery_id": "drop-a", "decision": "DROP", "reason": "out of scope"},
                    {"discovery_id": "maybe-b", "decision": "MAYBE", "reason": "needs verification"},
                    {"discovery_id": "keep-c", "decision": "KEEP", "reason": "material"},
                ],
            },
        )
        core.write_json(
            materiality,
            {
                "issue_id": "SP001",
                "rows": [
                    {"discovery_id": "drop-a", "downstream_disposition": "EXCLUDED", "rationale": "confirmed out of scope"},
                    {"discovery_id": "dup-d", "downstream_disposition": "DUPLICATE", "rationale": "same canonical source"},
                    {"discovery_id": "keep-c", "downstream_disposition": "MATERIAL", "rationale": "material"},
                ],
            },
        )
        core.write_json(
            selection,
            {
                "issue_id": "SP001",
                "assignments": [
                    {"candidate_id": "cand-1", "disposition": "HOLD", "rationale": "awaiting boundary check"},
                    {"candidate_id": "cand-2", "disposition": "SELECTED", "rationale": "selected"},
                ],
            },
        )
        return screening, materiality, selection

    def test_attention_is_bounded_with_explicit_overflow(self) -> None:
        screening, materiality, selection = self._write_inputs()
        output = self.root / "sources/SP001/architecture-review-attention-v2.json"
        attention.build_attention(self.root, screening, materiality, selection, output, limit=3)
        payload = attention.validate_attention(self.root, output)
        self.assertEqual(payload["total_count"], 5)
        self.assertEqual(payload["shown_count"], 3)
        self.assertEqual(payload["overflow_count"], 2)
        self.assertTrue(payload["truncated"])
        self.assertTrue(all(row["item_id"] for row in payload["items"]))
        self.assertTrue(all(row["rationale"] for row in payload["items"]))

    def test_attention_basis_drift_fails_closed(self) -> None:
        screening, materiality, selection = self._write_inputs()
        output = self.root / "sources/SP001/architecture-review-attention-v2.json"
        attention.build_attention(self.root, screening, materiality, selection, output, limit=50)
        selection.write_text('{"issue_id":"SP001","assignments":[]}\n', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "basis drift"):
            attention.validate_attention(self.root, output)

    def test_attention_rejects_missing_rationale(self) -> None:
        screening, materiality, selection = self._write_inputs()
        payload = core.load_json(screening)
        payload["decisions"][0]["reason"] = ""
        core.write_json(screening, payload)
        with self.assertRaisesRegex(ValueError, "stable id/rationale"):
            attention.build_attention(
                self.root,
                screening,
                materiality,
                selection,
                self.root / "sources/SP001/architecture-review-attention-v2.json",
            )


if __name__ == "__main__":
    unittest.main()
