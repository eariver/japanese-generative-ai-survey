from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import revise_special_half_year_review_repairs_v5 as repair


class HalfYearCanonicalTechnicalNoteURLTests(unittest.TestCase):
    def test_mutated_historical_url_is_restored_from_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "notes.tex"
            path.write_text(
                "\\begin{technicalnote}{Llama 3.3 70B Instruct}{主要資料}\n"
                "\\begin{itemize}\n"
                "\\item {\\scriptsize\\url{https://example.com/モデル_CARD.md}}\n"
                "\\end{itemize}\n"
                "\\end{technicalnote}\n",
                encoding="utf-8",
            )
            count = repair.restore_note_urls_from_evidence(
                path,
                {
                    "Llama 3.3 70B Instruct": {
                        "urls": ["https://example.com/MODEL_CARD.md"]
                    }
                },
            )
            self.assertEqual(count, 1)
            text = path.read_text(encoding="utf-8")
            self.assertIn("https://example.com/MODEL_CARD.md", text)
            self.assertNotIn("モデル_CARD.md", text)

    def test_url_count_mismatch_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "notes.tex"
            path.write_text(
                "\\begin{technicalnote}{Artifact}{主要資料}\n"
                "\\url{https://example.com/one}\n"
                "\\end{technicalnote}\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "canonical URL restoration count mismatch"):
                repair.restore_note_urls_from_evidence(
                    path,
                    {"Artifact": {"urls": ["https://example.com/one", "https://example.com/two"]}},
                )


if __name__ == "__main__":
    unittest.main()
