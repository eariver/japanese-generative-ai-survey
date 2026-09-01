import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReleaseManifestTests(unittest.TestCase):
    def test_w32_release_manifest_contract(self):
        path = ROOT / "sources/2026-W32/release-manifest.json"
        data = json.loads(path.read_text(encoding="utf-8"))

        self.assertEqual(data["schema_version"], "1.0")
        self.assertEqual(data["issue_id"], "2026-W32")
        self.assertEqual(data["revision"], "v0.2")
        self.assertEqual(data["status"], "frozen")
        self.assertEqual(data["release_tag"], "weekly/2026-W32/v0.2")
        self.assertRegex(data["source_commit"], r"^[0-9a-f]{40}$")
        self.assertRegex(data["expected_pdf_sha256"], r"^[0-9a-f]{64}$")
        self.assertGreater(data["page_count"], 0)
        self.assertEqual(data["pdf_source"]["mode"], "actions-artifact")
        self.assertEqual(data["pdf_source"]["workflow_run_id"], 31350762039)
        self.assertEqual(data["pdf_source"]["artifact_id"], 9048888577)
        self.assertTrue((ROOT / data["freeze_record"]).is_file())

    def test_all_release_manifests_use_canonical_tag(self):
        manifests = list((ROOT / "sources").glob("*/release-manifest.json"))
        self.assertTrue(manifests)
        for path in manifests:
            data = json.loads(path.read_text(encoding="utf-8"))
            issue_id = data["issue_id"]
            if data.get("release_identity_mode") == "ISSUE_ONLY":
                self.assertNotIn("revision", data, path)
                if issue_id.startswith("SP-"):
                    self.assertIn("special_slug", data, path)
                    expected = f"special/{data['special_slug']}"
                else:
                    expected = f"weekly/{issue_id}"
            else:
                # Historical W32 and SP-2026-M07 were published before the
                # issue-only identity policy and retain their exact tags.
                self.assertIn("revision", data, path)
                if issue_id.startswith("SP-"):
                    self.assertIn("special_slug", data, path)
                    expected = f"special/{data['special_slug']}/{data['revision']}"
                else:
                    expected = f"weekly/{issue_id}/{data['revision']}"
            self.assertEqual(data["release_tag"], expected, path)
            self.assertTrue(re.fullmatch(r"[0-9a-f]{64}", data["expected_pdf_sha256"]), path)
            self.assertIn(data["pdf_source"]["mode"], {"actions-artifact", "rebuild"}, path)


if __name__ == "__main__":
    unittest.main()
