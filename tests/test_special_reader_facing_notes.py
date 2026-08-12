import unittest

from scripts.postprocess_special_reader_facing_notes import transform_note


class SpecialReaderFacingNotesTests(unittest.TestCase):
    def test_pipeline_terms_ids_enums_and_leading_clearpage_are_removed(self):
        source = r'''\clearpage
\sectionkicker{Source-backed technical notes}
\subsection*{Example: Technical Notes}
この欄は記事本文で圧縮した一次資料上の情報を、比較・再検証しやすい形へ展開したものである。新しい外部情報は追加せず、Selection済みEvidenceのchronology、normalized claim、limitations、source URLのみを再配置する。
Artifact & Role & Type & Objective chronology \\
X & PRIMARY & OTHER & 2026-07-01 (OFFICIAL\_PUBLICATION); 2026-07-02 (PRODUCT\_UPDATE) \\
\begin{technicalnote}{X}{PRIMARY}
Organization & Example \\
Artifact type & AGENT \\
Chronology & 2026-07-01 (MODEL\_RELEASE) \\
{\bfseries Primary source}
\begingroup\sloppy
\begin{itemize}
\item \url{https://example.com}
\end{itemize}
\endgroup
{\scriptsize\color{SurveyMuted}Source-bound record: \texttt{evidence:SP-TEST:item-1}.}
\end{technicalnote}
'''
        result = transform_note(source)
        self.assertFalse(result.lstrip().startswith(r"\clearpage"))
        for banned in (
            "Selection済みEvidence", "normalized claim", "Source-bound record:",
            "PRIMARY", "OTHER", r"OFFICIAL\_PUBLICATION", r"PRODUCT\_UPDATE",
            r"MODEL\_RELEASE", r"モデル\_RELEASE",
        ):
            self.assertNotIn(banned, result)
        self.assertIn("比較・再検証しやすい形で整理", result)
        self.assertIn("主要資料", result)
        self.assertIn("公式情報", result)
        self.assertIn("公式公開", result)
        self.assertIn("製品更新", result)
        self.assertIn("モデル公開", result)
        self.assertIn("種別 & Agent", result)
        self.assertIn(r"\begin{samepage}", result)
        self.assertIn(r"\widowpenalty=10000", result)
        self.assertIn(r"\clubpenalty=10000", result)
        self.assertLess(result.index(r"\begin{samepage}"), result.index(r"\url{https://example.com}"))
        self.assertLess(result.index(r"\url{https://example.com}"), result.index(r"\end{samepage}"))

    def test_legacy_partially_translated_event_labels_are_normalized(self):
        source = r'''\subsection*{Theme at a glance}
A & 主要資料 & モデル & 2026-05-01 (モデル\_RELEASE) \\
B & 主要資料 & 研究 & 2026-05-02 (研究\_RELEASE) \\
C & 主要資料 & 論文 & 2026-05-03 (論文\_RELEASE) \\
\begin{technicalnote}{A}{主要資料}
種別 & モデル \\
時系列 & 2026-05-01 (モデル\_RELEASE) \\
{\bfseries 一次資料}
\begin{itemize}
\item \url{https://example.com/a}
\end{itemize}
\end{technicalnote}
'''
        result = transform_note(source)
        self.assertEqual(result.count("モデル公開"), 2)
        self.assertIn("研究公開", result)
        self.assertIn("論文公開", result)
        for banned in (r"モデル\_RELEASE", r"研究\_RELEASE", r"論文\_RELEASE"):
            self.assertNotIn(banned, result)

    def test_evaluation_playbook_gets_semantic_reader_label(self):
        source = r'''\subsection*{Theme at a glance}
A shared playbook for trustworthy third party evaluations & 補足資料 & SAFETY EVENT & 2026-05-29 (OFFICIAL\_PUBLICATION) \\
\begin{technicalnote}{A shared playbook for trustworthy third party evaluations}{補足資料}
種別 & SAFETY EVENT \\
時系列 & 2026-05-29 (OFFICIAL\_PUBLICATION) \\
{\bfseries 一次資料}
\begin{itemize}
\item \url{https://example.com/playbook}
\end{itemize}
\end{technicalnote}
'''
        result = transform_note(source)
        self.assertEqual(result.count("評価ガイダンス"), 2)
        self.assertNotIn("安全性事象", result)
        self.assertNotIn("SAFETY EVENT", result)
        self.assertNotIn(r"OFFICIAL\_PUBLICATION", result)
        # Only the compact source block is rigid; the whole technicalnote remains breakable.
        begin = result.index(r"\begin{technicalnote}")
        same = result.index(r"\begin{samepage}")
        self.assertLess(begin, same)


if __name__ == "__main__":
    unittest.main()
