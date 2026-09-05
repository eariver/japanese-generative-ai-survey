from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import survey_agent_control_v2 as agent


class ActiveEvidenceViewResolverTests(unittest.TestCase):
    def test_resolver_uses_checkpoint_bound_pair_when_historical_runs_coexist(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            evidence_path = root / "evidence-new.json"
            evidence_path.write_bytes(b"new evidence")
            views_path = root / "views-new.json"
            with views_path.open("w", encoding="utf-8") as handle:
                json.dump(
                    {"evidence_acceptance_sha256": hashlib.sha256(evidence_path.read_bytes()).hexdigest()},
                    handle,
                )
            (root / "evidence-old.json").write_bytes(b"old evidence")
            authority = {"path": "checkpoint.json", "sha256": "a" * 64}

            def fake_resolve(_root, _cfg, _state, _checkpoint, artifact_name):
                return {
                    "checkpoint_authority": authority,
                    "artifact_path": evidence_path if artifact_name == "evidence-acceptance" else views_path,
                }

            with patch.object(agent, "resolve_checkpoint_artifact", side_effect=fake_resolve):
                resolved = agent.resolve_active_evidence_views(root, {}, {})

            self.assertEqual(resolved["evidence_path"], evidence_path)
            self.assertEqual(resolved["views_path"], views_path)

    def test_resolver_rejects_cross_checkpoint_or_cross_run_view_binding(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            evidence_path = root / "evidence.json"
            evidence_path.write_bytes(b"evidence")
            views_path = root / "views.json"
            views_path.write_text(
                json.dumps({"evidence_acceptance_sha256": hashlib.sha256(evidence_path.read_bytes()).hexdigest()}),
                encoding="utf-8",
            )
            authorities = [
                {"path": "checkpoint-a.json", "sha256": "a" * 64},
                {"path": "checkpoint-b.json", "sha256": "b" * 64},
            ]

            def fake_resolve(_root, _cfg, _state, _checkpoint, artifact_name):
                return {
                    "checkpoint_authority": authorities[0 if artifact_name == "evidence-acceptance" else 1],
                    "artifact_path": evidence_path if artifact_name == "evidence-acceptance" else views_path,
                }

            with patch.object(agent, "resolve_checkpoint_artifact", side_effect=fake_resolve):
                with self.assertRaisesRegex(agent.AgentControlError, "same Stage Checkpoint"):
                    agent.resolve_active_evidence_views(root, {}, {})

            def fake_same_checkpoint(_root, _cfg, _state, _checkpoint, artifact_name):
                return {
                    "checkpoint_authority": authorities[0],
                    "artifact_path": evidence_path if artifact_name == "evidence-acceptance" else views_path,
                }

            views_path.write_text(
                json.dumps({"evidence_acceptance_sha256": "0" * 64}),
                encoding="utf-8",
            )
            with patch.object(agent, "resolve_checkpoint_artifact", side_effect=fake_same_checkpoint):
                with self.assertRaisesRegex(agent.AgentControlError, "does not bind"):
                    agent.resolve_active_evidence_views(root, {}, {})


if __name__ == "__main__":
    unittest.main()
