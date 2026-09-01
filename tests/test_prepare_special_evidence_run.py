from __future__ import annotations

import unittest

from scripts import prepare_special_evidence_run


class PrepareSpecialEvidenceRunTests(unittest.TestCase):
    def test_rejects_weekly_issue_id_before_build(self):
        with self.assertRaisesRegex(ValueError, "SP-\\*"):
            prepare_special_evidence_run.build_package(
                repo_root=None, output_root=None, issue_id="2026-W33", screening_run_sha="a"*64,
                source_ref="weekly/2026-W33-work", source_commit="b"*40,
            )

    def test_special_issue_regex_accepts_canonical_id(self):
        self.assertIsNotNone(prepare_special_evidence_run.SPECIAL_ISSUE_RE.fullmatch("SP-2026-M07"))
        self.assertIsNone(prepare_special_evidence_run.SPECIAL_ISSUE_RE.fullmatch("2026-M07"))


if __name__ == "__main__":
    unittest.main()
