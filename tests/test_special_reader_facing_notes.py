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

    def test_attributed_claim_and_card_tail_are_grouped_without_unbreakable_whole_card(self):
        source = r'''\begin{technicalnote}{X}{主要資料}
\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]
\item \textbf{一次情報で確認できる事実}: 保存済み一次資料で確認できる。
% reader-facing Technical Notes late-card tail guard
\Needspace{12\baselineskip}
\item \textbf{Author claim}: 著者は結果を報告している。
\end{itemize}
{\bfseries 読む際の境界}
\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]
\item \textbf{分析上の留意点}: 本号では独立再現していない。
\end{itemize}
\begin{samepage}
{\bfseries 一次資料}
\begin{itemize}
\item \url{https://example.com/paper}
\end{itemize}
\end{samepage}
\end{technicalnote}
'''
        result = transform_note(source, selected_titles={"X"})
        claim = r"\item \textbf{Author claim}: 著者は結果を報告している。"
        self.assertNotIn(r"\Needspace{12\baselineskip}", result)
        self.assertNotIn("late-card tail guard", result)
        self.assertIn(r"\begin{minipage}{\linewidth}", result)
        self.assertIn("coherent tail group", result)
        self.assertLess(result.index(r"\begin{minipage}{\linewidth}"), result.index(claim))
        self.assertLess(result.index(claim), result.index(r"{\bfseries 読む際の境界}"))
        self.assertLess(result.index(r"\url{https://example.com/paper}"), result.index(r"\end{minipage}"))
        self.assertLess(result.index(r"\begin{technicalnote}"), result.index(r"\begin{minipage}{\linewidth}"))
        primary = r"\item \textbf{一次情報で確認できる事実}: 保存済み一次資料で確認できる。"
        self.assertLess(result.index(primary), result.index(r"\begin{minipage}{\linewidth}"))

    def test_generic_boundary_source_tail_is_grouped_without_visual_qa_opt_in(self):
        source = r'''\begin{technicalnote}{X}{主要資料}
\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]
\item \textbf{一次情報で確認できる事実}: 保存済み一次資料で確認できる。
\item \textbf{Author claim}: 著者は結果を報告している。
\end{itemize}
{\bfseries 読む際の境界}
\begin{itemize}
\item \textbf{分析上の留意点}: 本号では独立再現していない。
\end{itemize}
\begin{samepage}
{\bfseries 一次資料}
\begin{itemize}
\item \url{https://example.com/paper}
\end{itemize}
\end{samepage}
\end{technicalnote}
'''
        result = transform_note(source)
        claim = r"\item \textbf{Author claim}: 著者は結果を報告している。"
        minipage = r"\begin{minipage}{\linewidth}"
        boundary = r"{\bfseries 読む際の境界}"
        self.assertIn(minipage, result)
        self.assertIn("generic boundary/source tail group", result)
        self.assertNotIn("coherent tail group", result)
        self.assertLess(result.index(claim), result.index(minipage))
        self.assertLess(result.index(minipage), result.index(boundary))
        self.assertLess(result.index(r"\url{https://example.com/paper}"), result.index(r"\end{minipage}"))

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

    def test_update_event_enums_are_normalized_even_outside_parentheses(self):
        source = r'''\subsection*{Theme at a glance}
A & 主要資料 & MODEL\_RELEASE & 2026-04-01 (MODEL\_RELEASE) \\
B & 主要資料 & Agent\_UPDATE & 2026-04-16 (AGENT\_UPDATE) \\
C & 主要資料 & Framework\_UPDATE & 2026-04-15 (FRAMEWORK\_UPDATE) \\
'''
        result = transform_note(source)
        for banned in (
            r"MODEL\_RELEASE", r"モデル\_RELEASE",
            r"AGENT\_UPDATE", r"Agent\_UPDATE",
            r"FRAMEWORK\_UPDATE", r"Framework\_UPDATE",
        ):
            self.assertNotIn(banned, result)
        self.assertEqual(result.count("モデル公開"), 2)
        self.assertEqual(result.count("Agent更新"), 2)
        self.assertEqual(result.count("Framework更新"), 2)

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
        begin = result.index(r"\begin{technicalnote}")
        same = result.index(r"\begin{samepage}")
        self.assertLess(begin, same)


if __name__ == "__main__":
    unittest.main()
