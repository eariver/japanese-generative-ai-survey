from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.special_technical_note_entity_binding_check import (
    ENTITY_BINDING_CONTRACT,
    _coverage_population,
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

    def _annualize(self, manifest: dict[str, object]) -> None:
        reader = manifest["reader_facing_technical_notes"]
        assert isinstance(reader, dict)
        reader["annual_source_specific_detail_contract"] = "ANNUAL_SCREENING_BACKED_FAIL_CLOSED_V1"

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

    def test_annual_source_specific_contract_rejects_proximity_fallback(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest, source_dir = self._fixture(
                root,
                [self._note("GPT-4 / GPT-4V", "対象 event 近傍の一次資料から factuality evaluation を確認できる。")],
                accepted=[],
                rejected=[],
            )
            self._annualize(manifest)
            errors = inspect_entity_binding(manifest, source_dir)
            self.assertTrue(any("forbidden proximity fallback" in error for error in errors))

    def test_annual_multi_family_card_rejects_flat_parameter_scale_bucket(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest, source_dir = self._fixture(
                root,
                [self._note("LLaMA / Llama 2 / Code Llama", "7B parameter scale / 65B parameter scale / 13B parameter scale / 33B parameter scale")],
                accepted=[],
                rejected=[],
            )
            self._annualize(manifest)
            errors = inspect_entity_binding(manifest, source_dir)
            self.assertTrue(any("flattens scope-sensitive parameter scales" in error for error in errors))

    def test_declared_contract_is_enforced_for_review_repair_status(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            fact = "対象event近傍の一次資料から comparator-only-token を確認できる。"
            manifest, source_dir = self._fixture(
                root,
                [self._note("Llama 3.1", fact)],
                accepted=[],
                rejected=["comparator-only-token"],
            )
            manifest["status"] = "VALIDATED_HALF_YEAR_REVIEW_REPAIR_V3_REVISION"
            errors = inspect_entity_binding(manifest, source_dir)
            self.assertTrue(any("comparator-only-token" in error for error in errors))

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

    def test_unique_title_coverage_population_matches_v017_shape(self) -> None:
        reader = {
            "source_specific_detail_visible_card_count": 49,
            "source_specific_detail_override_count": 26,
            "entity_binding_coverage_population_count": 34,
            "entity_binding_coverage_basis": "UNIQUE_RENDERED_TITLE_COUNT",
            "entity_binding_visible_card_placement_count": 49,
        }
        population, visible, overrides, basis = _coverage_population(reader)
        self.assertEqual((population, visible, overrides), (34, 49, 26))
        self.assertEqual(basis, "UNIQUE_RENDERED_TITLE_COUNT")
        self.assertEqual(population - overrides, 8)

    def test_override_count_cannot_exceed_unique_title_population(self) -> None:
        reader = {
            "source_specific_detail_visible_card_count": 49,
            "source_specific_detail_override_count": 35,
            "entity_binding_coverage_population_count": 34,
            "entity_binding_coverage_basis": "UNIQUE_RENDERED_TITLE_COUNT",
            "entity_binding_visible_card_placement_count": 49,
        }
        with self.assertRaisesRegex(ValueError, "override count exceeds"):
            _coverage_population(reader)

    def test_unknown_declared_coverage_basis_fails_closed(self) -> None:
        reader = {
            "source_specific_detail_visible_card_count": 49,
            "source_specific_detail_override_count": 26,
            "entity_binding_coverage_population_count": 34,
            "entity_binding_coverage_basis": "CARD_PLACEMENTS",
        }
        with self.assertRaisesRegex(ValueError, "unsupported"):
            _coverage_population(reader)

    def test_legacy_manifest_uses_visible_card_fallback(self) -> None:
        reader = {
            "source_specific_detail_visible_card_count": 5,
            "source_specific_detail_override_count": 2,
        }
        population, visible, overrides, basis = _coverage_population(reader)
        self.assertEqual((population, visible, overrides), (5, 5, 2))
        self.assertEqual(basis, "VISIBLE_CARD_COUNT_LEGACY_FALLBACK")


if __name__ == "__main__":
    unittest.main()
