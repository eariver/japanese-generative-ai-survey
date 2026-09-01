from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.special_technical_note_entity_binding_check import (
    ENTITY_BINDING_CONTRACT,
    inspect_entity_binding,
)


class SpecialTechnicalNoteEntityBindingZeroCountTests(unittest.TestCase):
    def _fixture(self, root: Path, *, include_count: bool = True) -> tuple[dict[str, object], Path]:
        source_dir = root / "source"
        source_dir.mkdir(parents=True)
        main = source_dir / "main.tex"
        main.write_text("% no reader-facing Technical Notes in this descendant\n", encoding="utf-8")

        audit: dict[str, object] = {
            "contract": ENTITY_BINDING_CONTRACT,
            "artifacts": [],
        }
        if include_count:
            audit["artifact_count"] = 0
        audit_path = source_dir / "technical-note-entity-binding-audit.json"
        audit_path.write_text(json.dumps(audit, ensure_ascii=False), encoding="utf-8")

        manifest: dict[str, object] = {
            "status": "VALIDATED_ANNUAL_ORDERED_REVIEW_REPAIR",
            "main_tex": {
                "path": "main.tex",
                "sha256": hashlib.sha256(main.read_bytes()).hexdigest(),
            },
            "reader_facing_technical_notes": {
                "source_specific_detail_contract": "SCREENING_BACKED_FAIL_CLOSED",
                "source_specific_detail_visible_card_count": 0,
                "source_specific_detail_override_count": 0,
                "entity_binding_contract": ENTITY_BINDING_CONTRACT,
                "entity_binding_audit_path": audit_path.name,
                "entity_binding_audit_sha256": hashlib.sha256(audit_path.read_bytes()).hexdigest(),
                "entity_binding_audited_artifact_count": 0,
                "entity_binding_rejected_signal_count": 0,
            },
            "articles": [],
        }
        return manifest, source_dir

    def test_explicit_zero_artifact_count_is_valid(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            manifest, source_dir = self._fixture(Path(tmp))
            self.assertEqual(inspect_entity_binding(manifest, source_dir), [])

    def test_missing_artifact_count_remains_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            manifest, source_dir = self._fixture(Path(tmp), include_count=False)
            errors = inspect_entity_binding(manifest, source_dir)
            self.assertTrue(any("audit count mismatch" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
