from __future__ import annotations

import unittest

from scripts import survey_evidence_v2 as evidence


class SurveyEvidenceSourceClassRegressionTests(unittest.TestCase):
    def test_canonical_discovery_collector_source_types_are_explicitly_classified(self) -> None:
        expected = {
            "arxiv_atom_snapshot": "PRIMARY_PAPER",
            "official_web_fallback_observation": "PRIMARY_OFFICIAL",
            "official_release_notes_snapshot": "PRIMARY_OFFICIAL",
            "official_rss_index_snapshot": "PRIMARY_OFFICIAL",
            "official_research_index_snapshot": "PRIMARY_OFFICIAL",
        }
        for source_type, source_class in expected.items():
            with self.subTest(source_type=source_type):
                self.assertEqual(evidence._source_class(source_type), source_class)

    def test_unknown_source_types_still_fail_closed(self) -> None:
        for source_type in (
            "arxiv_atom_snapshot_unreviewed",
            "official_web_fallback_observation_unreviewed",
            "totally-arbitrary-source",
        ):
            with self.subTest(source_type=source_type):
                with self.assertRaisesRegex(ValueError, "unsupported source_type"):
                    evidence._source_class(source_type)


if __name__ == "__main__":
    unittest.main()
