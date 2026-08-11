import unittest

from scripts.postprocess_special_reader_facing_notes import transform_note


class SpecialReaderFacingNotesTests(unittest.TestCase):
    def test_pipeline_terms_ids_and_leading_clearpage_are_removed(self):
        source = r'''\clearpage
\sectionkicker{Source-backed technical notes}
\subsection*{Example: Technical Notes}
この欄は記事本文で圧縮した一次資料上の情報を、比較・再検証しやすい形へ展開したものである。新しい外部情報は追加せず、Selection済みEvidenceのchronology、normalized claim、limitations、source URLのみを再配置する。
Artifact & Role & Type & Objective chronology \\
X & PRIMARY & MODEL UPDATE & 2026-07-01 (MODEL_UPDATE) \\
\begin{technicalnote}{X}{PRIMARY}
Organization & Example \\
Artifact type & MODEL UPDATE \\
Chronology & 2026-07-01 (MODEL_UPDATE) \\
{\bfseries Primary source}
{\scriptsize\color{SurveyMuted}Source-bound record: \texttt{evidence:SP-TEST:item-1}.}
\end{technicalnote}
'''
        result = transform_note(source)
        self.assertFalse(result.lstrip().startswith(r"\clearpage"))
        for banned in ("Selection済みEvidence", "normalized claim", "Source-bound record:", "PRIMARY", "MODEL_UPDATE"):
            self.assertNotIn(banned, result)
        self.assertIn("比較・再検証しやすい形で整理", result)
        self.assertIn("主要資料", result)
        self.assertIn("モデル更新", result)
        self.assertIn("一次資料", result)


if __name__ == "__main__":
    unittest.main()
