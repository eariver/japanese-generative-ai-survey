import unittest

from scripts.postprocess_special_reader_facing_notes import transform_note


class SpecialEventOnlyTailPolicyTests(unittest.TestCase):
    def test_single_verified_fact_and_source_are_grouped(self):
        source = r'''\begin{technicalnote}{Event X}{主要資料}
\begin{tabularx}{\linewidth}{@{}>{\bfseries}p{0.22\linewidth}X@{}}
組織 & Example \\
種別 & Model \\
時系列 & 2025-05-20 \\
\end{tabularx}
\smallskip
{\bfseries 一次資料から整理したtechnical points}
\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]
\item \textbf{一次情報で確認できる事実}: 一次資料で確認した事実。
\end{itemize}
{\bfseries 一次資料}
\begin{itemize}
\item \url{https://example.com/event}
\end{itemize}
\end{technicalnote}
'''
        result = transform_note(source)
        marker = "event-only fact/source tail group"
        self.assertIn(marker, result)
        self.assertIn(r"\begin{minipage}{\linewidth}", result)
        self.assertLess(
            result.index(r"\begin{minipage}{\linewidth}"),
            result.index(r"{\bfseries 一次資料から整理したtechnical points}"),
        )
        self.assertLess(
            result.index(r"\url{https://example.com/event}"),
            result.index(r"\end{minipage}"),
        )
        self.assertLess(
            result.index(r"\begin{technicalnote}"),
            result.index(r"\begin{minipage}{\linewidth}"),
        )

    def test_multi_fact_event_card_remains_breakable_without_large_group(self):
        source = r'''\begin{technicalnote}{Event Y}{主要資料}
{\bfseries 一次資料から整理したtechnical points}
\begin{itemize}
\item \textbf{一次情報で確認できる事実}: fact one.
\item \textbf{一次情報で確認できる事実}: fact two.
\end{itemize}
{\bfseries 一次資料}
\begin{itemize}
\item \url{https://example.com/y}
\end{itemize}
\end{technicalnote}
'''
        result = transform_note(source)
        self.assertNotIn("event-only fact/source tail group", result)
        self.assertIn(r"\begin{samepage}", result)


if __name__ == "__main__":
    unittest.main()
