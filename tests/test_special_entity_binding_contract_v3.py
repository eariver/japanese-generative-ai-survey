from __future__ import annotations

import unittest

from scripts.special_technical_note_entity_binding_check import ENTITY_BINDING_CONTRACT


class EntityBindingContractV3Tests(unittest.TestCase):
    def test_publication_preflight_requires_v3(self) -> None:
        self.assertEqual(ENTITY_BINDING_CONTRACT, "SUBJECT_COMPONENT_VARIANT_PROPERTY_BINDING_V3")


if __name__ == "__main__":
    unittest.main()
