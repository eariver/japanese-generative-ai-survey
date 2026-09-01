from __future__ import annotations

import unittest

from scripts.revise_special_dense_theme_table import densify_theme_tables


def _theme(rows: int, size: str = r"\footnotesize") -> str:
    row_end = chr(92) * 2
    lines = [
        r"\sectionkicker{Source-backed technical notes}",
        r"\subsection*{Theme at a glance}",
        r"\addcontentsline{toc}{subsection}{Theme at a glance}",
        r"\begin{center}",
        size,
        r"\begin{tabularx}{\linewidth}{@{}p{0.20\linewidth}p{0.10\linewidth}p{0.14\linewidth}X@{}}",
        r"\toprule",
        "資料 & 位置づけ & 種別 & 時系列 " + row_end,
        r"\midrule",
    ]
    lines.extend(
        f"Artifact {index} & 主要資料 & モデル & 2024-10-{index:02d} {row_end}"
        for index in range(1, rows + 1)
    )
    lines.extend([r"\bottomrule", r"\end{tabularx}", r"\end{center}", r"\normalsize", ""])
    return "\n".join(lines)


class SpecialDenseThemeTableTests(unittest.TestCase):
    def test_dense_table_switches_to_scriptsize_without_content_change(self) -> None:
        before = _theme(22)
        after, changed, row_counts = densify_theme_tables(before, 20)
        self.assertEqual(changed, 1)
        self.assertEqual(row_counts, [22])
        self.assertIn(r"\scriptsize", after)
        self.assertNotIn(r"\footnotesize", after)
        self.assertEqual(
            after.replace(r"\scriptsize", r"\footnotesize"),
            before,
        )

    def test_short_table_preserves_footnotesize(self) -> None:
        before = _theme(19)
        after, changed, row_counts = densify_theme_tables(before, 20)
        self.assertEqual(changed, 0)
        self.assertEqual(row_counts, [19])
        self.assertEqual(after, before)

    def test_already_dense_table_is_idempotent(self) -> None:
        before = _theme(22, r"\scriptsize")
        after, changed, row_counts = densify_theme_tables(before, 20)
        self.assertEqual(changed, 0)
        self.assertEqual(row_counts, [22])
        self.assertEqual(after, before)

    def test_multiple_theme_blocks_are_counted_independently(self) -> None:
        before = _theme(5) + "\n" + _theme(20)
        after, changed, row_counts = densify_theme_tables(before, 20)
        self.assertEqual(changed, 1)
        self.assertEqual(row_counts, [5, 20])
        self.assertEqual(after.count(r"\scriptsize"), 1)
        self.assertEqual(after.count(r"\footnotesize"), 1)


if __name__ == "__main__":
    unittest.main()
