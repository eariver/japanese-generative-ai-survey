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
F & 主要資料 & SECURITY EVENT & 2026-01-28 (SECURITY\_ENGINEERING\_NOTE) \\
G & 主要資料 & PAPER & 2026-01-24 (PAPER\_SUBMISSION) \\
H & 主要資料 & MODEL & 2026-01-27 (MODEL\_STUDIO\_AVAILABILITY) \\
I & 主要資料 & FRAMEWORK & 2026-01-26 (PROJECT\_PRERELEASE) \\
'''
        result = translate_machine_labels(source)
        self.assertEqual(reader_taxonomy_findings(result), [])
        for label in (
            "API入力拡張",
            "APIライフサイクル機能",
            "APIツール公開",
            "技術解説",
            "モデル行動方針公開",
            "セキュリティ関連",
            "セキュリティ技術解説",
            "論文投稿",
            "Model Studio提供開始",
            "プロジェクトPre-release",
        ):
            self.assertIn(label, result)
        for leaked in (
            "API_INPUT_EXPANSION",
            "API_LIFECYCLE_FEATURE",
            "API_TOOL_RELEASE",
            "ENGINEERING_NOTE",
            "MODEL_BEHAVIOR_POLICY_RELEASE",
            "モデル_BEHAVIOR_POLICY_RELEASE",
            "SECURITY EVENT",
            "SECURITY_ENGINEERING_NOTE",
            "SECURITY_技術解説",
            "PAPER_SUBMISSION",
            "論文_SUBMISSION",
            "MODEL_STUDIO_AVAILABILITY",
            "モデル_STUDIO_AVAILABILITY",
            "PROJECT_PRERELEASE",
        ):
            self.assertNotIn(leaked, result.replace(r"\_", "_"))


if __name__ == "__main__":
    unittest.main()
