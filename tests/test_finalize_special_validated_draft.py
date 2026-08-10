from __future__ import annotations

import unittest

from scripts import finalize_special_validated_draft as finalizer


class FinalizeSpecialValidatedDraftTests(unittest.TestCase):
    def test_split_bib_entries(self) -> None:
        text = "@online{a,\n  title={A}\n}\n\n@online{b,\n  title={B}\n}\n"
        entries = finalizer.split_bib_entries(text)
        self.assertEqual(len(entries), 2)
        self.assertTrue(entries[0].startswith("@online{a,"))
        self.assertTrue(entries[1].startswith("@online{b,"))

    def test_inject_package_label_after_section(self) -> None:
        source = "\\section{Title}\nBody\n"
        rendered = finalizer.inject_package_label(source, "pkg-one")
        self.assertIn("\\section{Title}\n\\label{pkg:pkg-one}\nBody", rendered)

    def test_parse_date_only_is_utc_midnight(self) -> None:
        parsed = finalizer.parse_instant("2026-07-31")
        self.assertEqual(parsed.isoformat(), "2026-07-31T00:00:00+00:00")


if __name__ == "__main__":
    unittest.main()
