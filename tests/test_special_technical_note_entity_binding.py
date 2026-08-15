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


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SpecialTechnicalNoteEntityBindingTests(unittest.TestCase):
    def _fixture(
        self,
        root: Path,
        fact: str,
        rejected: list[str],
        *,
        accepted: list[str] | None = None,
    ) -> dict:
        note = root / "technical-notes" / "notes.tex"
        note.parent.mkdir(parents=True)
        note.write_text(
            "\\begin{technicalnote}{Jamba 1.5 Mini and Large}{MODEL}\n"
            "\\begin{itemize}\n"
            "\\item \\textbf{一次情報で確認できる事実}: " + fact + "\n"
            "\\end{itemize}\n"
            "\\end{technicalnote}\n",
            encoding="utf-8",
        )
        main = root / "main.tex"
        main.write_text("\\input{technical-notes/notes}\n", encoding="utf-8")
        audit = {
            "schema_version": "1.0",
            "contract": ENTITY_BINDING_CONTRACT,
            "artifact_count": 1,
            "artifacts": [
                {
                    "title": "Jamba 1.5 Mini and Large",
                    "anchor": "Jamba",
                    "extraction_calls": 1,
                    "accepted_entity_bound_signals": accepted if accepted is not None else ["Mamba"],
                    "rejected_entity_bound_signals": rejected,
                    "empty_window_calls": 0,
                }
            ],
        }
        audit_path = root / "technical-note-entity-binding-audit.json"
        audit_path.write_text(json.dumps(audit), encoding="utf-8")
        return {
            "status": "VALIDATED_HALF_YEAR_SOURCE_SPECIFIC_NOTES_REVISION",
            "main_tex": {"path": "main.tex", "sha256": sha(main)},
            "reader_facing_technical_notes": {
                "source_specific_detail_contract": "SCREENING_BACKED_FAIL_CLOSED",
                "source_specific_detail_visible_card_count": 1,
                "source_specific_detail_override_count": 0,
                "entity_binding_contract": ENTITY_BINDING_CONTRACT,
                "entity_binding_audit_path": audit_path.name,
                "entity_binding_audit_sha256": sha(audit_path),
                "entity_binding_audited_artifact_count": 1,
                "entity_binding_rejected_signal_count": len(rejected),
            },
            "articles": [
                {
                    "package_id": "open-deployment",
                    "technical_notes_reader_facing": True,
                    "technical_notes_path": "technical-notes/notes.tex",
                    "technical_notes_sha256": sha(note),
                }
            ],
        }

    def test_guard_accepts_rejected_signal_absent_from_primary_fact(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self._fixture(
                root,
                "JambaについてSSM-Transformer / Mambaを確認できる。",
                ["70B parameter scale", "405B parameter scale"],
            )
            self.assertEqual(inspect_entity_binding(manifest, root), [])

    def test_guard_rejects_rejected_signal_reintroduced_into_primary_fact(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self._fixture(
                root,
                "JambaについてMamba / 405B parameter scaleを確認できる。",
                ["405B parameter scale"],
            )
            errors = inspect_entity_binding(manifest, root)
            self.assertTrue(any("405B parameter scale" in error for error in errors))

    def test_guard_allows_signal_when_same_signal_is_also_target_bound(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self._fixture(
                root,
                "Jambaについて256K context / Mambaを確認できる。",
                ["256K context"],
                accepted=["256K context", "Mamba"],
            )
            self.assertEqual(inspect_entity_binding(manifest, root), [])

    def test_guard_uses_token_boundaries_for_numeric_model_sizes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self._fixture(
                root,
                "対象modelは11B parameter scale / 128K contextである。",
                ["1B parameter scale"],
                accepted=["11B parameter scale", "128K context"],
            )
            self.assertEqual(inspect_entity_binding(manifest, root), [])

    def test_guard_ignores_provenance_note_file_not_rendered_by_main_tex(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self._fixture(
                root,
                "JambaについてMambaを確認できる。",
                ["405B parameter scale"],
            )
            unused = root / "technical-notes" / "unused.tex"
            unused.write_text(
                "\\begin{technicalnote}{Jamba 1.5 Mini and Large}{MODEL}\n"
                "\\begin{itemize}\n"
                "\\item \\textbf{一次情報で確認できる事実}: 405B parameter scale\n"
                "\\end{itemize}\n"
                "\\end{technicalnote}\n",
                encoding="utf-8",
            )
            manifest["articles"].append(
                {
                    "package_id": "provenance-only-synthesis",
                    "technical_notes_reader_facing": True,
                    "technical_notes_path": "technical-notes/unused.tex",
                    "technical_notes_sha256": sha(unused),
                }
            )
            self.assertEqual(inspect_entity_binding(manifest, root), [])

    def test_guard_still_rejects_duplicate_title_when_both_files_are_rendered(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self._fixture(
                root,
                "JambaについてMambaを確認できる。",
                [],
            )
            duplicate = root / "technical-notes" / "duplicate.tex"
            duplicate.write_text(
                "\\begin{technicalnote}{Jamba 1.5 Mini and Large}{MODEL}\n"
                "\\begin{itemize}\n"
                "\\item \\textbf{一次情報で確認できる事実}: Mamba\n"
                "\\end{itemize}\n"
                "\\end{technicalnote}\n",
                encoding="utf-8",
            )
            manifest["articles"].append(
                {
                    "package_id": "duplicate-rendered",
                    "technical_notes_reader_facing": True,
                    "technical_notes_path": "technical-notes/duplicate.tex",
                    "technical_notes_sha256": sha(duplicate),
                }
            )
            main = root / "main.tex"
            main.write_text(
                "\\input{technical-notes/notes}\n\\input{technical-notes/duplicate}\n",
                encoding="utf-8",
            )
            manifest["main_tex"]["sha256"] = sha(main)
            errors = inspect_entity_binding(manifest, root)
            self.assertTrue(any("duplicate reader-facing Technical Note title" in error for error in errors))

    def test_guard_rejects_half_year_source_without_contract(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = {
                "status": "VALIDATED_HALF_YEAR_SOURCE_SPECIFIC_NOTES_REVISION",
                "reader_facing_technical_notes": {
                    "source_specific_detail_contract": "SCREENING_BACKED_FAIL_CLOSED"
                },
                "articles": [],
            }
            errors = inspect_entity_binding(manifest, root)
            self.assertTrue(any("lack the required subject/entity binding contract" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
