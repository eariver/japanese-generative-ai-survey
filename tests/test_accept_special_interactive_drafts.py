from __future__ import annotations

import unittest

from scripts import accept_special_interactive_drafts as asid


class SpecialInteractiveDraftAcceptanceTests(unittest.TestCase):
    def test_inference_with_author_claim_is_strengthened_to_mixed(self) -> None:
        self.assertEqual(asid.strengthened_mode("INFERENCE", {"AUTHOR_CLAIM", "INFERENCE"}), "MIXED")

    def test_inference_with_primary_fact_remains_inference(self) -> None:
        self.assertEqual(asid.strengthened_mode("INFERENCE", {"PRIMARY_FACT"}), "INFERENCE")

    def test_factual_vendor_claim_is_strengthened(self) -> None:
        self.assertEqual(asid.strengthened_mode("FACTUAL", {"VENDOR_CLAIM"}), "ATTRIBUTED")

    def test_social_mixed_with_primary_is_strengthened_to_mixed(self) -> None:
        self.assertEqual(asid.strengthened_mode("SOCIAL", {"SOCIAL_OBSERVATION", "PRIMARY_FACT"}), "MIXED")


if __name__ == "__main__":
    unittest.main()
