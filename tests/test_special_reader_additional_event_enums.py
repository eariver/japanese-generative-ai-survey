import unittest

from scripts.postprocess_special_reader_facing_notes import (
    reader_taxonomy_findings,
    translate_machine_labels,
)


class SpecialReaderAdditionalEventEnumTests(unittest.TestCase):
    def test_additional_event_enums_are_reader_facing(self):
        source = r'''\subsection*{Theme at a glance}
A & 主要資料 & API & 2026-01-08 (API\_INPUT\_EXPANSION) \\
B & 主要資料 & API & 2026-01-12 (API\_LIFECYCLE\_FEATURE) \\
C & 主要資料 & API & 2026-01-29 (API\_TOOL\_RELEASE) \\
D & 主要資料 & 公式情報 & 2026-01-28 (ENGINEERING\_NOTE) \\
E & 主要資料 & MODEL & 2026-01-22 (MODEL\_BEHAVIOR\_POLICY\_RELEASE) \\
'''
        result = translate_machine_labels(source)
        self.assertEqual(reader_taxonomy_findings(result), [])
        for label in (
            "API入力拡張",
            "APIライフサイクル機能",
            "APIツール公開",
            "技術解説",
            "モデル行動方針公開",
        ):
            self.assertIn(label, result)
        for leaked in (
            "API_INPUT_EXPANSION",
            "API_LIFECYCLE_FEATURE",
            "API_TOOL_RELEASE",
            "ENGINEERING_NOTE",
            "MODEL_BEHAVIOR_POLICY_RELEASE",
            "モデル_BEHAVIOR_POLICY_RELEASE",
        ):
            self.assertNotIn(leaked, result.replace(r"\_", "_"))


if __name__ == "__main__":
    unittest.main()
