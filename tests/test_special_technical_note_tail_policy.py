import unittest

from scripts import postprocess_special_reader_facing_notes as reader_notes
from scripts.special_technical_note_tail_policy import (
    GENERIC_TAIL_GROUP_MARKER,
    apply_generic_tail_policy,
    unprotected_tail_titles,
)


def note(title: str, point_label: str = "Vendor claim") -> str:
    return f"""\\begin{{technicalnote}}{{{title}}}{{主要資料}}
\\begingroup
% reader-facing Technical Notes break policy
\\widowpenalty=10000
\\clubpenalty=10000
\\displaywidowpenalty=10000
{{\\bfseries 一次資料から整理したtechnical points}}
\\begin{{itemize}}[leftmargin=1.5em,itemsep=0.35em]
\\item \\textbf{{{point_label}}}: test point.
\\end{{itemize}}
{{\\bfseries 読む際の境界}}
\\begin{{itemize}}[leftmargin=1.5em,itemsep=0.35em]
\\item \\textbf{{分析上の留意点}}: limitation text that must not leave a source-only page-top remainder.
\\end{{itemize}}
\\begin{{samepage}}
{{\\bfseries 一次資料}}
\\begingroup\\sloppy
\\begin{{itemize}}[leftmargin=1.5em,itemsep=0.25em]
\\item {{\\scriptsize\\url{{https://example.com/{title}}}}}
\\end{{itemize}}
\\endgroup
\\end{{samepage}}
\\endgroup
\\end{{technicalnote}}
"""


class GenericTailPolicyTests(unittest.TestCase):
    def test_groups_every_unprotected_card_without_title_allowlist(self) -> None:
        source = note("Workspace agents", "一次情報で確認できる事実") + note("Claw-Eval-Live", "Author claim")
        result = apply_generic_tail_policy(source)
        self.assertEqual(result.groups_added, 2)
        self.assertEqual(result.card_count, 2)
        self.assertEqual(result.protected_card_count, 2)
        self.assertEqual(result.text.count(GENERIC_TAIL_GROUP_MARKER), 2)
        self.assertEqual(unprotected_tail_titles(result.text), [])
        self.assertIn(r"\end{minipage}\n\endgroup\n\end{technicalnote}".replace("\\n", "\n"), result.text)

    def test_preserves_existing_larger_coherent_group(self) -> None:
        source = note("Already protected").replace(
            r"\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]\n\item \textbf{Vendor claim}: test point.".replace("\\n", "\n"),
            r"\begin{minipage}{\linewidth}\n% reader-facing Technical Notes coherent tail group\n\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]\n\item \textbf{Vendor claim}: test point.".replace("\\n", "\n"),
            1,
        ).replace(
            r"\end{samepage}\n\endgroup\n\end{technicalnote}".replace("\\n", "\n"),
            r"\end{samepage}\n\end{minipage}\n\endgroup\n\end{technicalnote}".replace("\\n", "\n"),
            1,
        )
        result = apply_generic_tail_policy(source)
        self.assertEqual(result.groups_added, 0)
        self.assertEqual(result.protected_card_count, 1)
        self.assertEqual(unprotected_tail_titles(result.text), [])

    def test_reader_facing_transform_applies_generic_policy(self) -> None:
        source = note("Workspace agents", "一次情報で確認できる事実")
        revised = reader_notes.transform_note(source, selected_titles=set())
        self.assertIn(GENERIC_TAIL_GROUP_MARKER, revised)
        self.assertEqual(unprotected_tail_titles(revised), [])
        self.assertIn(r"\begin{technicalnote}{Workspace agents}{主要資料}", revised)


if __name__ == "__main__":
    unittest.main()
