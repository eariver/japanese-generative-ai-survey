from __future__ import annotations

import unittest

from scripts.normalize_special_legacy_partial_enums import normalize_text


class NormalizeSpecialLegacyPartialEnumsTests(unittest.TestCase):
    def test_normalizes_escaped_and_unescaped_partial_event_labels(self) -> None:
        source = (
            r"2026-05-01 (モデル\_RELEASE); 2026-05-02 (研究\_RELEASE); "
            r"2026-05-03 (論文\_RELEASE); 2026-05-04 (API\_UPDATE); "
            "2026-05-05 (Agent_RELEASE)"
        )
        result, count = normalize_text(source)
        self.assertEqual(count, 5)
        self.assertIn("モデル公開", result)
        self.assertIn("研究公開", result)
        self.assertIn("論文公開", result)
        self.assertIn("API更新", result)
        self.assertIn("Agent公開", result)
        self.assertNotIn("_RELEASE", result)
        self.assertNotIn(r"\_RELEASE", result)
        self.assertNotIn(r"\_UPDATE", result)

    def test_does_not_touch_already_reader_facing_labels(self) -> None:
        source = "2026-05-01 (モデル公開); 2026-05-02 (論文公開)"
        result, count = normalize_text(source)
        self.assertEqual(count, 0)
        self.assertEqual(result, source)


if __name__ == "__main__":
    unittest.main()
