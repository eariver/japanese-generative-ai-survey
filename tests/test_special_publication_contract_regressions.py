from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.postprocess_special_reader_facing_notes import (
    reader_taxonomy_findings,
    transform_note,
)
from scripts.special_layout_text_normalization import (
    manual_item_marker_findings,
    normalize_itemize_manual_markers,
    split_leading_standfirst,
)
from scripts.special_publication_layout_check import (
    inspect_derived_layout_files,
    inspect_layout,
)


class SpecialPublicationContractRegressionTests(unittest.TestCase):
    def test_m02_composite_and_partial_event_labels_are_normalized(self):
        source = (
            r"A & 主要資料 & モデル & 2026-02-02 (Agent\_製品公開); "
            r"2026-02-05 (SYSTEM\_CARD\_PUBLICATION); "
            r"2026-02-12 (研究\_PREVIEW) \\" "\n"
            r"B & 補足資料 & Framework & 2026-02-24 (PROJECT\_RELEASE) \\" "\n"
            r"C & 主要資料 & モデル & 2026-02-16 (REGIONAL\_モデル公開); "
            r"2026-02-20 (INTERNATIONAL\_モデル公開) \\" "\n"
            r"D & 主要資料 & オープンウェイト & 2026-02-12 "
            r"(オープンウェイト\_モデル公開) \\" "\n"
            r"E & 主要資料 & Framework & 2026-02-13 "
            r"(TECHNICAL\_Framework公開) \\" "\n"
            r"F & 主要資料 & モデル & 2026-02-19 (API\_モデル公開) \\" "\n"
        )
        result = transform_note(source)
        for expected in (
            "Agent製品公開",
            "System Card公開",
            "研究Preview",
            "プロジェクト公開",
            "地域別モデル公開",
            "国際提供モデル公開",
            "オープンウェイトモデル公開",
            "技術Framework公開",
            "APIモデル公開",
        ):
            self.assertIn(expected, result)
        self.assertEqual(reader_taxonomy_findings(result), [])

    def test_generic_taxonomy_guard_rejects_unknown_forms(self):
        source = (
            r"A & 主要資料 & Framework & 2026-02-01 (FUTURE\_EVENT) \\" "\n"
            r"B & 主要資料 & Framework & 2026-02-02 (SECURITY EVENT) \\" "\n"
            r"C & 主要資料 & Framework & 2026-02-03 (研究\_UNKNOWN) \\" "\n"
        )
        findings = reader_taxonomy_findings(source)
        self.assertIn("FUTURE_EVENT", findings)
        self.assertIn("SECURITY EVENT", findings)
        self.assertIn("研究_UNKNOWN", findings)

    def test_balanced_local_multicols_passes(self):
        manifest = {
            "layout": {
                "body_mode": (
                    "mixed: narrative articles two-column via local balanced multicols"
                )
            },
            "frontmatter": {"path": "sections/00-frontmatter.tex"},
            "articles": [{"package_id": "a"}, {"package_id": "b"}],
        }
        main = (
            "\\input{sections/00-frontmatter}\n"
            "\\section{A}\n"
            "\\begin{multicols}{2}\n"
            "text\n"
            "\\end{multicols}\n"
            "\\input{technical-notes/a-notes}\n"
            "\\section{B}\n"
            "\\begin{multicols}{2}\n"
            "text\n"
            "\\end{multicols}\n"
            "\\input{technical-notes/b-notes}\n"
        )
        self.assertEqual(
            inspect_layout(manifest, main, {"status": "APPROVED"}),
            [],
        )


    def test_standfirst_and_manual_list_normalization(self):
        lines = [
            "% generated\n",
            r"\noindent\textbf{Lead sentence.}\autocite{x}" + "\n",
            "\n",
            "Narrative body.\n",
        ]
        standfirst, body = split_leading_standfirst(lines)
        self.assertIn(r"\noindent\textbf{Lead sentence.}", "".join(standfirst))
        self.assertEqual("".join(body), "Narrative body.\n")

        source = (
            r"\begin{itemize}" + "\n"
            r"  \item Lead sentence." + "\n"
            r"  \item ・agent execution: a" + "\n"
            r"  \item ・serving/runtime: b" + "\n"
            r"  \item ・safety/control: c" + "\n"
            r"  \item ・multimodal interaction: d" + "\n"
            r"  \item ・specialized reasoning: e" + "\n"
            r"  \item Trailing explanation." + "\n"
            r"\end{itemize}" + "\n"
        )
        normalized, removed, lifted = normalize_itemize_manual_markers(source)
        self.assertEqual(removed, 5)
        self.assertEqual(lifted, 2)
        self.assertEqual(manual_item_marker_findings(normalized), [])
        self.assertTrue(normalized.startswith("Lead sentence.\n\n"))
        self.assertIn(r"\item agent execution: a", normalized)
        self.assertIn("\\end{itemize}\n\nTrailing explanation.", normalized)

    def test_derived_layout_rejects_standfirst_and_manual_bullet_leaks(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            body = root / "layout-bodies/a-narrative.tex"
            body.parent.mkdir(parents=True)
            body.write_text(
                "% generated\n"
                r"\noindent\textbf{Lead still in columns.}" + "\n"
                r"\begin{itemize}" + "\n"
                r"\item ・duplicated bullet" + "\n"
                r"\end{itemize}" + "\n",
                encoding="utf-8",
            )
            manifest = {
                "articles": [
                    {
                        "package_id": "a",
                        "layout_body_path": "layout-bodies/a-narrative.tex",
                    }
                ]
            }
            errors = inspect_derived_layout_files(manifest, root)
            self.assertTrue(any("standfirst leaked" in error for error in errors))
            self.assertTrue(any("manual bullet marker" in error for error in errors))

    def test_full_width_standfirst_contract_passes(self):
        manifest = {
            "layout": {
                "body_mode": "mixed: narrative articles two-column via local balanced multicols"
            },
            "frontmatter": {"path": "sections/00-frontmatter.tex"},
            "articles": [
                {
                    "package_id": "a",
                    "layout_standfirst_present": True,
                    "layout_standfirst_path": "layout-bodies/a-standfirst.tex",
                    "layout_body_path": "layout-bodies/a-narrative.tex",
                }
            ],
        }
        main = (
            "\\input{sections/00-frontmatter}\n"
            "\\section{A}\n"
            "\\input{layout-bodies/a-standfirst}\n"
            "\\begin{multicols}{2}\n"
            "\\input{layout-bodies/a-narrative}\n"
            "\\end{multicols}\n"
            "\\input{technical-notes/a-notes}\n"
        )
        self.assertEqual(inspect_layout(manifest, main, {"status": "APPROVED"}), [])

    def test_single_column_regression_is_rejected(self):
        manifest = {
            "layout": {"body_mode": "single-column long-form"},
            "frontmatter": {"path": "sections/00-frontmatter.tex"},
            "articles": [{"package_id": "a"}],
        }
        main = (
            "\\input{sections/00-frontmatter}\n"
            "\\section{A}\n"
            "text\n"
            "\\input{technical-notes/a-notes}\n"
        )
        errors = inspect_layout(manifest, main, {"status": "APPROVED"})
        self.assertTrue(any("single-column" in e for e in errors))
        self.assertTrue(any("two-column" in e for e in errors))

    def test_explicit_approved_single_column_override_can_opt_out(self):
        manifest = {
            "layout": {"body_mode": "single-column long-form"},
            "articles": [{"package_id": "a"}],
        }
        architecture = {
            "status": "APPROVED",
            "layout_override": {
                "narrative_body_mode": "single-column",
                "approval_reference": (
                    "Human Gate explicitly approved single-column narrative"
                ),
            },
        }
        self.assertEqual(inspect_layout(manifest, "text", architecture), [])


if __name__ == "__main__":
    unittest.main()
