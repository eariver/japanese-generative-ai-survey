from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import revise_special_half_year_review_repairs_v13 as event
from scripts import revise_special_half_year_review_repairs_v28 as repair


class HalfYearRenderedNoteScopeV28Tests(unittest.TestCase):
    def _fixture(self, root: Path) -> dict[str, object]:
        issue_id = "SP-TEST-H2"
        source_dir = root / "surveys" / "special" / "test" / "revisions" / "v0.1"
        note_path = source_dir / "technical-notes" / "10-notes.tex"
        note_path.parent.mkdir(parents=True)
        note_path.write_text(
            "\\begin{technicalnote}{Rendered Model}{主要資料}\n"
            "\\item \\textbf{一次情報で確認できる事実}: placeholder\n"
            "\\end{technicalnote}\n",
            encoding="utf-8",
        )
        current_manifest = {
            "issue_id": issue_id,
            "articles": [
                {
                    "technical_notes_reader_facing": True,
                    "technical_notes_path": "technical-notes/10-notes.tex",
                }
            ],
        }
        manifest_path = source_dir / "source-manifest.json"
        manifest_path.write_text(json.dumps(current_manifest), encoding="utf-8")

        state_path = root / "sources" / issue_id / "pipeline-state.json"
        state_path.parent.mkdir(parents=True)
        state_path.write_text(
            json.dumps(
                {
                    "provenance": {
                        "validated_issue_source": {
                            "path": manifest_path.relative_to(root).as_posix()
                        }
                    }
                }
            ),
            encoding="utf-8",
        )
        return {"issue_id": issue_id, "articles": current_manifest["articles"]}

    def test_rendered_titles_come_from_state_pinned_reader_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = self._fixture(root)
            self.assertEqual(
                repair._rendered_technical_note_titles(root, manifest),
                {"rendered model"},
            )

    def test_chronology_only_selected_evidence_does_not_require_technical_note_detail(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = self._fixture(root)
            queue = root / "queue.jsonl"
            queue.write_text("{}\n", encoding="utf-8")

            rendered_url = "https://example.com/rendered"
            chronology_url = "https://example.com/chronology"
            rendered = {
                "canonical_title": "Rendered Model",
                "urls": [rendered_url],
                "events": [],
            }
            chronology = {
                "canonical_title": "Chronology Only",
                "urls": [chronology_url],
                "events": [],
            }
            index = {"Rendered Model": rendered, "Chronology Only": chronology}
            screening = {
                event.impl._normalize_url(rendered_url): {
                    "summary_text": "Rendered Model supports tool use.",
                    "screening_id": "rendered",
                },
                event.impl._normalize_url(chronology_url): {
                    "summary_text": "",
                    "screening_id": "chronology",
                },
            }

            old_overrides = event.impl._ACTIVE_OVERRIDES
            event.impl._ACTIVE_OVERRIDES = {}
            try:
                with patch.object(event.impl, "_ORIGINAL_MERGE", return_value=index), patch.object(
                    event,
                    "_screening_index_with_source_type",
                    return_value=(screening, queue),
                ), patch.object(
                    event,
                    "_safe_technical_signals",
                    side_effect=lambda summary, events, title="": ["tool use"] if title == "Rendered Model" else [],
                ):
                    merged = repair._merge_rendered_scope(root, manifest)
            finally:
                event.impl._ACTIVE_OVERRIDES = old_overrides

            self.assertEqual(
                merged["Rendered Model"]["technical_points"],
                ["対象event近傍の一次資料から tool use を確認できる。"],
            )
            self.assertNotIn("technical_points", merged["Chronology Only"])


if __name__ == "__main__":
    unittest.main()
