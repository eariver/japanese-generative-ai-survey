from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import revise_special_adaptive_spacing as router


class PreservePreviewRouterTests(unittest.TestCase):
    def marker(self, root: Path, changes: dict) -> None:
        path = root / "sources/SP-TEST/editorial/layout-revision-v0.2.json"
        path.parent.mkdir(parents=True)
        path.write_text(
            json.dumps({"issue_id": "SP-TEST", "revision": "v0.2", "layout_changes": changes}),
            encoding="utf-8",
        )

    def test_preserve_preview_marker_routes_to_preserve_builder(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.marker(root, {"preserve_current_layout_visual_review_repairs": True})
            expected = {"mode": "preserve"}
            with patch(
                "scripts.revise_special_preserve_preview_repairs_retrospective.build",
                return_value=expected,
            ) as mocked:
                actual = router.build(root, "test", "SP-TEST", "v0.2")
            self.assertEqual(actual, expected)
            mocked.assert_called_once_with(root, "test", "SP-TEST", "v0.2")

    def test_other_markers_preserve_existing_adaptive_router(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.marker(root, {"visual_review_repairs": True})
            expected = {"mode": "legacy"}
            with patch.object(router.core, "build", return_value=expected) as mocked:
                actual = router.build(root, "test", "SP-TEST", "v0.2")
            self.assertEqual(actual, expected)
            mocked.assert_called_once_with(root, "test", "SP-TEST", "v0.2")


if __name__ == "__main__":
    unittest.main()
