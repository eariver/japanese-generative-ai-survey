from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import revise_special_half_year_review_repairs_v3 as repair


class HalfYearReviewRepairV3Tests(unittest.TestCase):
    def test_source_specific_fact_uses_structured_event(self) -> None:
        text = repair.source_specific_fact(
            "Llama 3.1",
            {
                "organization": "Meta",
                "events": [("2024-07-23", "MODEL_RELEASE")],
                "urls": ["https://ai.meta.com/blog/meta-llama-3-1/"],
            },
        )
        self.assertIn("Metaの一次資料", text)
        self.assertIn("Llama 3.1", text)
        self.assertIn("2024-07-23", text)
        self.assertIn("モデル公開", text)

    def test_repair_note_removes_generic_copy_and_preserves_url(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "notes.tex"
            url = "https://github.com/meta-llama/llama-models/blob/main/models/llama3_3/MODEL_CARD.md"
            path.write_text(
                "\\sectionkicker{Source-backed technical notes}\n"
                "intro\n"
                "\\medskip\n"
                "\\begin{technicalnote}{Llama 3.3 70B Instruct}{主要資料}\n"
                "\\begin{tabularx}{\\linewidth}{@{}>{\\bfseries}p{0.22\\linewidth}X@{}}\n"
                "組織 & Meta \\\\\n"
                "種別 & MODEL \\\\\n"
                "時系列 & 2024-12-06 (MODEL_RELEASE) \\\\\n"
                "\\end{tabularx}\n"
                "{\\bfseries 一次資料から整理したtechnical points}\n"
                "\\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]\n"
                "\\item \\textbf{一次情報で確認できる事実}: 一次資料で「Llama 3.3 70B Instruct」を確認できる。数値や能力に関する評価は、提供元・プロジェクト・著者の主張として扱う。\n"
                "\\end{itemize}\n"
                "{\\bfseries 読む際の境界}\n"
                "\\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]\n"
                "\\item \\textbf{分析上の留意点}: " + repair.GENERIC_LIMITATION + "\n"
                "\\end{itemize}\n"
                "{\\bfseries 一次資料}\n"
                "\\begin{itemize}\n"
                f"\\item {{\\scriptsize\\url{{{url}}}}}\n"
                "\\end{itemize}\n"
                "\\end{technicalnote}\n",
                encoding="utf-8",
            )
            facts, limitations, checked = repair.repair_note_file(
                path,
                {
                    "Llama 3.3 70B Instruct": {
                        "organization": "Meta",
                        "artifact_type": "MODEL",
                        "events": [("2024-12-06", "MODEL_RELEASE")],
                        "urls": [url],
                    }
                },
            )
            self.assertEqual(facts, 1)
            self.assertEqual(limitations, 1)
            self.assertEqual(checked, 1)
            text = path.read_text(encoding="utf-8")
            self.assertIn("2024-12-06にモデル公開", text)
            self.assertNotIn('一次資料で「Llama 3.3', text)
            self.assertNotIn(repair.GENERIC_LIMITATION, text)
            self.assertIn(url, text)
            self.assertNotIn("モデル_CARD.md", text)

    def test_chronology_is_compact_dated_list_with_citations(self) -> None:
        text = repair.render_chronology(
            [
                {
                    "date": "2024-08-13",
                    "title": "Introducing SWE-bench Verified",
                    "organization": "OpenAI",
                    "event_label": "評価ベンチマーク公開",
                    "bib_key": "src-example",
                }
            ]
        )
        self.assertIn("2024-08-13", text)
        self.assertIn("Introducing SWE-bench Verified", text)
        self.assertIn(r"\autocite{src-example}", text)
        self.assertNotIn("technicalnote", text)


if __name__ == "__main__":
    unittest.main()
