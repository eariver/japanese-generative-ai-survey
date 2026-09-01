import unittest

from scripts.release_identity import special_release_identity, weekly_release_identity


class ReleaseIdentityTests(unittest.TestCase):
    def test_special_public_identity_has_no_version(self):
        value = special_release_identity("2026-M06")
        self.assertEqual(value["release_identity_mode"], "ISSUE_ONLY")
        self.assertEqual(value["release_tag"], "special/2026-M06")
        self.assertEqual(value["release_title"], "Japanese Generative AI Technical Survey Special — 2026-M06")
        self.assertEqual(value["asset_name"], "Japanese_Generative_AI_Technical_Survey_Special_2026-M06.pdf")
        self.assertNotIn("v0.", " ".join(value.values()))

    def test_weekly_public_identity_has_no_version(self):
        value = weekly_release_identity("2026-W33")
        self.assertEqual(value["release_identity_mode"], "ISSUE_ONLY")
        self.assertEqual(value["release_tag"], "weekly/2026-W33")
        self.assertEqual(value["release_title"], "Japanese Generative AI Technical Survey — 2026-W33")
        self.assertEqual(value["asset_name"], "Japanese_Generative_AI_Technical_Survey_2026-W33.pdf")

    def test_invalid_identifiers_are_rejected(self):
        with self.assertRaises(ValueError):
            weekly_release_identity("2026-W33/v0.1")
        with self.assertRaises(ValueError):
            special_release_identity("2026-M06/v0.1")


if __name__ == "__main__":
    unittest.main()
