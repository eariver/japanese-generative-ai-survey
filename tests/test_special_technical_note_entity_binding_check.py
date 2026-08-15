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


class SpecialTechnicalNoteEntityBindingCheckTests(unittest.TestCase):
    def _note(self, title: str, fact: str, role: str = "主要資料") -> str:
        return (
            f"\\begin{{technicalnote}}{{{title}}}{{{role}}}\n"
            "\\begin{itemize}\n"
            f"\\item \\textbf{{一次情報で確認できる事実}}: {fact}\n"
            "\\end{itemize}\n"
            "\\end{technicalnote}\n"
        )

    def _fixture(
        self,
        root: Path,
        note_texts: list[str],
        *,
        accepted: list[str],
        rejected: list[str],
    ) -> tuple[dict[str, object], Path]:
        source_dir = root / "source"
        source_dir.mkdir(parents=True)
        articles: list[dict[str, object]] = []
        for index, text in enumerate(note_texts, start=1):
            rel = f"technical-notes/{index:02d}.tex"
            path = source_dir / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            articles.append(
                {
                    "technical_notes_reader_facing": True,
                    "technical_notes_path": rel,
                    "technical_notes_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                }
            )

        artifacts = [
            {
                "title": "Llama 3.1",
                "accepted_entity_bound_signals": accepted,
                "rejected_entity_bound_signals": rejected,
            }
        ]
        audit = {
            "contract": ENTITY_BINDING_CONTRACT,
            "artifact_count": len(artifacts),
            "artifacts": artifacts,
        }
        audit_path = source_dir / "technical-note-entity-binding-audit.json"
        audit_path.write_text(json.dumps(audit, ensure_ascii=False), encoding="utf-8")
        manifest: dict[str, object] = {
            "status": "VALIDATED_HALF_YEAR_SOURCE_SPECIFIC_NOTES_REVISION",
            "reader_facing_technical_notes": {
                "source_specific_detail_contract": "SCREENING_BACKED_FAIL_CLOSED",
                "source_specific_detail_visible_card_count": 1,
                "source_specific_detail_override_count": 0,
                "entity_binding_contract": ENTITY_BINDING_CONTRACT,
                "entity_binding_audit_path": audit_path.name,
                "entity_binding_audit_sha256": hashlib.sha256(audit_path.read_bytes()).hexdigest(),
                "entity_binding_audited_artifact_count": 1,
                "entity_binding_rejected_signal_count": len(rejected),
            },
            "articles": articles,
        }
        return manifest, source_dir

    def test_acceptance_wins_when_same_rendered_signal_has_accepted_and_rejected_occurrences(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fact = "対象event近傍の一次資料から 405B parameter scale を確認できる。"
            manifest, source_dir = self._fixture(
                root,
                [self._note("Llama 3.1", fact)],
                accepted=["405B parameter scale"],
                rejected=["405B parameter scale"],
            )
            self.assertEqual(inspect_entity_binding(manifest, source_dir), [])

    def test_identical_fact_may_be_repeated_across_article_placements(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fact = "同じEvidenceの一次情報で確認できる事実。"
            manifest, source_dir = self._fixture(
                root,
                [
                    self._note("Llama 3.1", fact, "主要資料"),
                    self._note("Llama 3.1", fact, "補足資料"),
                ],
                accepted=[],
                rejected=[],
            )
            self.assertEqual(inspect_entity_binding(manifest, source_dir), [])

    def test_conflicting_duplicate_fact_remains_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest, source_dir = self._fixture(
                root,
                [
                    self._note("Llama 3.1", "first fact"),
                    self._note("Llama 3.1", "different fact"),
                ],
                accepted=[],
                rejected=[],
            )
            errors = inspect_entity_binding(manifest, source_dir)
            self.assertTrue(any("conflicting reader-facing Technical Note fact" in error for error in errors))

    def test_rejected_only_signal_still_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fact = "対象event近傍の一次資料から 405B parameter scale を確認できる。"
            manifest, source_dir = self._fixture(
                root,
                [self._note("Llama 3.1", fact)],
                accepted=[],
                rejected=["405B parameter scale"],
            )
            errors = inspect_entity_binding(manifest, source_dir)
            self.assertTrue(any("405B parameter scale" in error for error in errors))

    def test_short_rejected_scale_does_not_match_longer_numeric_token(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fact = "対象event近傍の一次資料から 11B parameter scale / 13B parameter scale / 70B parameter scale を確認できる。"
            manifest, source_dir = self._fixture(
                root,
                [self._note("Llama 3.1", fact)],
                accepted=[],
                rejected=["1B parameter scale", "3B parameter scale", "7B parameter scale"],
            )
            self.assertEqual(inspect_entity_binding(manifest, source_dir), [])

    def test_state_pinned_main_limits_check_to_rendered_note_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest, source_dir = self._fixture(
                root,
                [
                    self._note("Llama 3.1", "rendered target-bound fact"),
                    self._note("Llama 3.1", "provenance-only conflicting fact"),
                ],
                accepted=[],
                rejected=[],
            )
            main = source_dir / "main.tex"
            main.write_text("\\input{technical-notes/01}\n", encoding="utf-8")
            manifest["main_tex"] = {
                "path": "main.tex",
                "sha256": hashlib.sha256(main.read_bytes()).hexdigest(),
            }
            self.assertEqual(inspect_entity_binding(manifest, source_dir), [])


if __name__ == "__main__":
    unittest.main()
