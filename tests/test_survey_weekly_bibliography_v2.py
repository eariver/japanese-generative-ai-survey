import unittest

from scripts import survey_weekly_bibliography_v2 as bib


class SurveyWeeklyBibliographyV2Tests(unittest.TestCase):
    def test_bibliography_metadata_never_degrades_to_unknown_placeholder(self):
        record = {
            "title": "Expanding Daybreak as the Cyber Defense Window Narrows",
            "organization": "OpenAI",
            "published_date": "2026-08-10",
            "url": "https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows",
            "status": "VERIFIED",
            "materiality": "MATERIAL",
        }

        rendered = bib._bib_text("w2026w33example", record, "2026-08-14")

        self.assertNotIn("Unknown", rendered)
        self.assertIn("organization = {{OpenAI}}", rendered)
        self.assertIn("date = {2026-08-10}", rendered)
        self.assertIn("urldate = {2026-08-14}", rendered)
        self.assertIn("note = {[V/M]}", rendered)
        self.assertIn(record["url"], rendered)

    def test_unsupported_human_author_is_omitted_not_invented(self):
        record = {
            "title": "Example Paper",
            "organization": None,
            "published_date": "2026-08-09",
            "url": "http://arxiv.org/abs/2608.00000v1",
            "status": "PARTIAL",
            "materiality": "CONTEXT",
        }

        rendered = bib._bib_text("w2026w33paper", record, "2026-08-14")

        self.assertNotIn("Unknown", rendered)
        self.assertNotIn("author =", rendered)
        self.assertNotIn("organization =", rendered)
        self.assertIn("date = {2026-08-09}", rendered)
        self.assertIn("note = {[P/C]}", rendered)

    def test_evidence_tag_mapping_is_fail_closed_and_self_documented(self):
        self.assertEqual(bib._evidence_tag("VERIFIED", "MATERIAL"), "V/M")
        self.assertEqual(bib._evidence_tag("PARTIAL", "CONTEXT"), "P/C")
        self.assertIn("V=VERIFIED", bib.EVIDENCE_TAG_LEGEND)
        self.assertIn("C=CONTEXT", bib.EVIDENCE_TAG_LEGEND)
        with self.assertRaisesRegex(ValueError, "unsupported Weekly bibliography evidence tag"):
            bib._evidence_tag("UNKNOWN", "MATERIAL")

    def test_source_owner_fallbacks_are_deterministic(self):
        self.assertEqual(bib._source_organization("https://openai.com/index/example"), "OpenAI")
        self.assertEqual(bib._source_organization("https://github.com/sgl-project/sglang/releases/tag/v1"), "sgl-project")
        self.assertEqual(bib._source_organization("http://arxiv.org/abs/2608.00000v1"), "arXiv")
        self.assertEqual(
            bib._source_organization("Grok_X_SourseIntake/Weekly/2026-W33/run/result.md"),
            "Grok/X Source Intake",
        )

    def test_publication_date_normalization_accepts_iso_and_rfc_dates(self):
        self.assertEqual(bib._normalize_date("2026-08-09T11:54:09Z"), "2026-08-09")
        self.assertEqual(bib._normalize_date("Mon, 10 Aug 2026 10:00:00 GMT"), "2026-08-10")
        self.assertIsNone(bib._normalize_date(None))


if __name__ == "__main__":
    unittest.main()
