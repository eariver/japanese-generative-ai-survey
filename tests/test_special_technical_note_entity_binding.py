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
        accepted: list[str] | None = None,
        duplicate_fact: str | None = None,
    ) -> dict:
        note_dir = root / "technical-notes"
        note_dir.mkdir(parents=True)

        def write_note(path: Path, value: str) -> None:
            path.write_text(
                "\\begin{technicalnote}{Jamba 1.5 Mini and Large}{MODEL}\n"
                "\\begin{itemize}\n"
                "\\item \\textbf{一次情報で確認できる事実}: " + value + "\n"
                "\\end{itemize}\n"
                "\\end{technicalnote}\n",
                encoding="utf-8",
            )

        note = note_dir / "notes.tex"
        write_note(note, fact)
        articles = [
            {
                "package_id": "open-deployment",
                "technical_notes_reader_facing": True,
                "technical_notes_path": "technical-notes/notes.tex",
                "technical_notes_sha256": sha(note),
            }
        ]
        if duplicate_fact is not None:
            duplicate = note_dir / "supporting.tex"
            write_note(duplicate, duplicate_fact)
            articles.append(
                {
                    "package_id": "efficiency-serving",
                    "technical_notes_reader_facing": True,
                    "technical_notes_path": "technical-notes/supporting.tex",
                    "technical_notes_sha256": sha(duplicate),
                }
            )

        accepted = accepted if accepted is not None else ["Mamba"]
        audit = {
            "schema_version": "1.0",
            "contract": ENTITY_BINDING_CONTRACT,
            "artifact_count": 1,
            "artifacts": [
                {
                    "title": "Jamba 1.5 Mini and Large",
                    "anchor": "Jamba 1.5 Large",
                    "extraction_calls": 1,
                    "accepted_entity_bound_signals": accepted,
                    "rejected_entity_bound_signals": rejected,
                    "empty_window_calls": 0,
                }
            ],
        }
        audit_path = root / "technical-note-entity-binding-audit.json"
        audit_path.write_text(json.dumps(audit), encoding="utf-8")
        return {
            "status": "VALIDATED_HALF_YEAR_SOURCE_SPECIFIC_NOTES_REVISION",
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
            "articles": articles,
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

    def test_guard_allows_signal_with_both_accepted_and_rejected_occurrences(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self._fixture(
                root,
                "Jambaについて256K contextを確認できる。",
                ["70B parameter scale", "256K context"],
                accepted=["256K context"],
            )
            self.assertEqual(inspect_entity_binding(manifest, root), [])

    def test_guard_rejects_rejected_only_signal_reintroduced_into_primary_fact(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self._fixture(
                root,
                "JambaについてMamba / 405B parameter scaleを確認できる。",
                ["405B parameter scale"],
            )
            errors = inspect_entity_binding(manifest, root)
            self.assertTrue(any("rejected-only" in error and "405B parameter scale" in error for error in errors))

    def test_guard_allows_identical_duplicate_supporting_cards(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fact = "Jambaについて256K contextを確認できる。"
            manifest = self._fixture(
                root,
                fact,
                ["405B parameter scale"],
                accepted=["256K context"],
                duplicate_fact=fact,
            )
            self.assertEqual(inspect_entity_binding(manifest, root), [])

    def test_guard_rejects_inconsistent_duplicate_supporting_cards(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            manifest = self._fixture(
                root,
                "Jambaについて256K contextを確認できる。",
                ["405B parameter scale"],
                accepted=["256K context"],
                duplicate_fact="Jambaについて別のfactを確認できる。",
            )
            errors = inspect_entity_binding(manifest, root)
            self.assertTrue(any("inconsistent primary facts" in error for error in errors))

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
