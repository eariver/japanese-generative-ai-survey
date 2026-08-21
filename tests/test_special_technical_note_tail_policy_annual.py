import unittest

from scripts.special_technical_note_tail_policy import (
    EVENT_ONLY_TAIL_GROUP_MARKER,
    GENERIC_TAIL_GROUP_MARKER,
    apply_generic_tail_policy,
    unprotected_tail_titles,
)


def annual_note(title: str, urls: list[str]) -> str:
    url_items = "\n".join(
        rf"\item {{\scriptsize\url{{{url}}}}}" for url in urls
    )
    return f"""\\begin{{technicalnote}}{{{title}}}{{主要資料}}
\\begingroup
% reader-facing Technical Notes break policy
\\widowpenalty=10000
\\clubpenalty=10000
\\displaywidowpenalty=10000
{{\\bfseries 一次資料から整理したtechnical points}}
\\begin{{itemize}}[leftmargin=1.5em,itemsep=0.35em]
\\item \\textbf{{一次情報で確認できる事実}}: source-specific annual technical detail.
\\end{{itemize}}
\\begin{{minipage}}{{\\linewidth}}
{GENERIC_TAIL_GROUP_MARKER}
\\begin{{samepage}}
{{\\bfseries 一次資料}}
\\begingroup\\sloppy
\\begin{{itemize}}[leftmargin=1.5em,itemsep=0.25em]
{url_items}
\\end{{itemize}}
\\endgroup
\\end{{samepage}}
\\end{{minipage}}
\\endgroup
\\end{{technicalnote}}
"""


class AnnualTailPolicyTests(unittest.TestCase):
    def test_expands_existing_source_only_group_to_fact_and_source(self) -> None:
        source = annual_note("REALM", ["http://arxiv.org/abs/2002.08909v1"])
        result = apply_generic_tail_policy(source)

        self.assertEqual(result.groups_added, 1)
        self.assertEqual(result.card_count, 1)
        self.assertEqual(result.protected_card_count, 1)
        self.assertEqual(unprotected_tail_titles(result.text), [])
        self.assertEqual(result.text.count(EVENT_ONLY_TAIL_GROUP_MARKER), 1)
        self.assertEqual(result.text.count(GENERIC_TAIL_GROUP_MARKER), 0)
        self.assertEqual(result.text.count(r"\begin{minipage}{\linewidth}"), 1)
        self.assertLess(
            result.text.index(EVENT_ONLY_TAIL_GROUP_MARKER),
            result.text.index(r"{\bfseries 一次資料から整理したtechnical points}"),
        )
        self.assertLess(
            result.text.index(r"{\bfseries 一次資料から整理したtechnical points}"),
            result.text.index(r"{\bfseries 一次資料}"),
        )

    def test_preserves_multiple_source_urls_inside_expanded_group(self) -> None:
        source = annual_note(
            "Learning to Summarize from Human Feedback",
            [
                "http://arxiv.org/abs/2009.01325v3",
                "https://openai.com/index/learning-to-summarize-with-human-feedback",
            ],
        )
        result = apply_generic_tail_policy(source)

        self.assertEqual(result.groups_added, 1)
        self.assertEqual(result.protected_card_count, 1)
        self.assertIn("http://arxiv.org/abs/2009.01325v3", result.text)
        self.assertIn("https://openai.com/index/learning-to-summarize-with-human-feedback", result.text)
        self.assertEqual(result.text.count(r"\begin{minipage}{\linewidth}"), 1)
        self.assertEqual(unprotected_tail_titles(result.text), [])


if __name__ == "__main__":
    unittest.main()
