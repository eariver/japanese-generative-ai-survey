#!/usr/bin/env python3
"""Contract tests for the Automotive E/E Evidence abstraction probe."""
from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import profiled_evidence_contract as probe

ROOT = Path(__file__).resolve().parents[2]
PROFILE_PATH = ROOT / "experiments" / "automotive-ee-architecture" / "evidence-profile.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class ProfiledEvidenceContractTest(unittest.TestCase):
    def test_generated_contract_changes_only_profiled_schema_fields(self) -> None:
        profile = probe.load_json(PROFILE_PATH)
        base_run_path = ROOT / profile["base_evidence_run_schema"]
        base_card_path = ROOT / profile["base_evidence_card_schema"]
        prompt_path = ROOT / profile["prompt"]
        before = {
            "run": sha256(base_run_path),
            "card": sha256(base_card_path),
            "prompt": sha256(prompt_path),
        }

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            manifest = probe.build(repo_root=ROOT, profile_path=PROFILE_PATH, output_root=output)
            generated_run = probe.load_json(output / "contract" / "evidence-run.schema.json")
            generated_card = probe.load_json(output / "contract" / "evidence-card.schema.json")
            base_run = probe.load_json(base_run_path)
            base_card = probe.load_json(base_card_path)

            self.assertEqual(manifest["production_files_modified"], [])
            self.assertEqual(generated_run["$id"], "evidence-run.schema.json")
            self.assertEqual(generated_card["$id"], "evidence-card.schema.json")
            self.assertEqual(generated_run["properties"]["card"]["$ref"], "evidence-card.schema.json")
            self.assertEqual(
                generated_card["properties"]["artifact"]["properties"]["artifact_type"]["enum"],
                profile["artifact_types"],
            )
            self.assertEqual(
                generated_run["properties"]["prompt_id"],
                base_run["properties"]["prompt_id"],
            )
            self.assertEqual(
                (output / "contract" / "primary-source-verification-v0.1.md").read_bytes(),
                prompt_path.read_bytes(),
            )

            # Normalize the three intentionally generated Card fields back to the
            # production values. The complete schema must then be byte-semantic
            # equivalent as a JSON object.
            normalized_card = json.loads(json.dumps(generated_card))
            normalized_card["$id"] = base_card["$id"]
            normalized_card["title"] = base_card["title"]
            normalized_card["properties"]["artifact"]["properties"]["artifact_type"] = (
                base_card["properties"]["artifact"]["properties"]["artifact_type"]
            )
            self.assertEqual(normalized_card, base_card)

            normalized_run = json.loads(json.dumps(generated_run))
            normalized_run["$id"] = base_run["$id"]
            normalized_run["title"] = base_run["title"]
            self.assertEqual(normalized_run, base_run)

        after = {
            "run": sha256(base_run_path),
            "card": sha256(base_card_path),
            "prompt": sha256(prompt_path),
        }
        self.assertEqual(before, after)

    def test_profile_ontology_is_closed_and_explicit(self) -> None:
        profile = probe.load_json(PROFILE_PATH)
        values = probe.validate_artifact_types(profile)
        self.assertEqual(values, profile["artifact_types"])
        self.assertEqual(len(values), len(set(values)))
        self.assertIn("OTHER", values)
        self.assertIn("STANDARD", values)
        self.assertIn("MIDDLEWARE", values)
        self.assertIn("PLATFORM", values)


if __name__ == "__main__":
    unittest.main()
