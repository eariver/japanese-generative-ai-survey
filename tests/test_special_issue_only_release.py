import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class SpecialIssueOnlyReleaseTests(unittest.TestCase):
    def test_visual_review_then_freeze_creates_versionless_public_identity(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            issue = "SP-TEST-M06"
            slug = "2026-M06"
            source_version = "v0.9"
            source = root / "surveys" / "special" / slug / "revisions" / source_version / "source-manifest.json"
            dump(source, {"schema_version": "1.0", "issue_id": issue, "source_version": source_version})
            top_main = root / "surveys" / "special" / slug / "main.tex"
            top_main.parent.mkdir(parents=True, exist_ok=True)
            top_main.write_text("\\documentclass{article}\n", encoding="utf-8")
            pdf = root / "main.pdf"
            pdf.write_bytes(b"%PDF-issue-only-test")
            pdf_sha = sha(pdf)

            state_path = root / "sources" / issue / "pipeline-state.json"
            state = {
                "schema_version": "1.0",
                "issue_id": issue,
                "lifecycle_state": "RELEASE_CANDIDATE",
                "revision": "internal-state-r1",
                "calendar": {"frozen_at": None},
                "gates": {
                    "latex_build": "passed",
                    "visual_review": "pending",
                    "freeze": "pending",
                },
                "automation": {
                    "unattended_public_release": False,
                    "human_gate_required_for_public_release": True,
                },
                "provenance": {
                    "validated_issue_source": {
                        "path": str(source.relative_to(root)),
                        "sha256": sha(source),
                        "source_version": source_version,
                    },
                    "latex_build": {
                        "pdf_sha256": pdf_sha,
                        "page_count": 34,
                        "workflow_run_id": 12345,
                        "source_version": source_version,
                    },
                },
            }
            dump(state_path, state)

            subprocess.run([
                sys.executable,
                str(ROOT / "scripts" / "accept_special_visual_review_issue_only.py"),
                "--repo-root", str(root),
                "--issue-id", issue,
                "--special-slug", slug,
                "--approved-pdf", str(pdf),
                "--approved-pdf-sha256", pdf_sha,
                "--approval-reference", "Visual Review test approval",
                "--approved-at", "2026-08-11T14:00:00+09:00",
                "--artifact-name", "special-test-v0.9",
                "--artifact-id", "999",
                "--artifact-digest", "sha256:" + "b" * 64,
            ], check=True, cwd=ROOT, capture_output=True, text=True)

            candidate_path = root / "sources" / issue / "freeze" / "freeze-candidate.json"
            candidate = json.loads(candidate_path.read_text(encoding="utf-8"))
            self.assertEqual(candidate["release_identity_mode"], "ISSUE_ONLY")
            self.assertEqual(candidate["release_tag"], "special/2026-M06")
            self.assertNotIn("proposed_release_revision", candidate)
            self.assertNotIn("v0.9", candidate["release_title"])
            self.assertNotIn("v0.9", candidate["asset_name"])

            subprocess.run([
                sys.executable,
                str(ROOT / "scripts" / "accept_special_freeze_issue_only.py"),
                "--repo-root", str(root),
                "--issue-id", issue,
                "--special-slug", slug,
                "--approved-at", "2026-08-11T14:10:00+09:00",
                "--approval-reference", "Freeze test approval",
            ], check=True, cwd=ROOT, capture_output=True, text=True)

            manifest = json.loads((root / "sources" / issue / "release-manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest["release_identity_mode"], "ISSUE_ONLY")
            self.assertEqual(manifest["release_tag"], "special/2026-M06")
            self.assertEqual(manifest["asset_name"], "Japanese_Generative_AI_Technical_Survey_Special_2026-M06.pdf")
            self.assertNotIn("revision", manifest)
            self.assertEqual(manifest["source_version"], source_version)
            self.assertTrue(manifest["public_release_authorized"])
            current = (root / "surveys" / "special" / slug / "CURRENT_RELEASE.md").read_text(encoding="utf-8")
            self.assertIn("Canonical source", current)
            self.assertIn("not a public Release version", current)
            self.assertTrue(top_main.read_text(encoding="utf-8").startswith("% WORKSPACE ENTRY POINT"))


if __name__ == "__main__":
    unittest.main()
