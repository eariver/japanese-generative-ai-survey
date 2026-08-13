from __future__ import annotations

import unittest

from scripts.postprocess_special_reader_facing_notes import (
    reader_taxonomy_findings,
    transform_note,
)
from scripts.special_publication_layout_check import inspect_layout


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
