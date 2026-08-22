#!/usr/bin/env python3
"""One-shot WU-011 fixture migration; removed after successful execution."""
from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: replacement count {count} != 1 for {old[:100]!r}")
    p.write_text(text.replace(old, new), encoding="utf-8")


# Drafting fixtures: create and bind canonical Architecture Review Attention.
replace_once(
    "tests/test_survey_drafting_v2.py",
    "from scripts import survey_production_v2 as core\n",
    "from scripts import survey_production_v2 as core\nfrom scripts import survey_review_attention_v2 as review_attention\n",
)
replace_once(
    "tests/test_survey_drafting_v2.py",
    '        summary_path = chain["root"] / "architecture-review-summary-v2.json"\n        core.write_json(summary_path, summary)\n        approval = {\n',
    '        summary_path = chain["root"] / "architecture-review-summary-v2.json"\n        core.write_json(summary_path, summary)\n        attention_path = chain["root"] / "architecture-review-attention-v2.json"\n        review_attention.build_attention(\n            chain["root"], chain["screening"], chain["ledger_path"], selection_path, attention_path\n        )\n        approval = {\n',
)
replace_once(
    "tests/test_survey_drafting_v2.py",
    '            "architecture_review_summary_sha256": core.sha256_file(summary_path),\n            "reviewed_by": "human-reviewer",\n',
    '            "architecture_review_summary_sha256": core.sha256_file(summary_path),\n            "architecture_review_attention_sha256": core.sha256_file(attention_path),\n            "reviewed_by": "human-reviewer",\n',
)
replace_once(
    "tests/test_survey_drafting_v2.py",
    '                "review_summary_path": summary_path,\n                "approval_path": approval_path,\n',
    '                "review_summary_path": summary_path,\n                "review_attention_path": attention_path,\n                "approval_path": approval_path,\n',
)

# Legacy orchestration-mechanics tests intentionally use synthetic handlers; production
# handoff semantics are tested separately. Keep production config strict and disable only
# the in-memory sandbox copy.
replace_once(
    "tests/test_survey_orchestrator_v2.py",
    "from scripts import survey_production_v2 as core\n",
    "from scripts import survey_production_v2 as core\nfrom scripts import survey_review_attention_v2 as review_attention\n",
)
replace_once(
    "tests/test_survey_orchestrator_v2.py",
    '        _, state_path = core.initialize(\n            root,\n            cfg,\n            profile,\n            pinned,\n            "ARCHITECTURE_REVIEW",\n            core.parse_instant("2026-08-22T03:01:00+09:00"),\n        )\n        return temp, root, cfg, state_path, pinned\n',
    '        _, state_path = core.initialize(\n            root,\n            cfg,\n            profile,\n            pinned,\n            "ARCHITECTURE_REVIEW",\n            core.parse_instant("2026-08-22T03:01:00+09:00"),\n        )\n        for stage in cfg["orchestration"]["stage_plan"].values():\n            stage["handoff_required"] = False\n        return temp, root, cfg, state_path, pinned\n',
)
replace_once(
    "tests/test_survey_orchestrator_v2.py",
    '                elif name == "architecture-review-summary":\n                    architecture = root / "sources" / state["issue_id"] / "architecture-v2.json"\n                    core.write_json(artifact, self.synthetic_review(state, core.sha256_file(architecture)))\n                else:\n',
    '                elif name == "architecture-review-summary":\n                    architecture = root / "sources" / state["issue_id"] / "architecture-v2.json"\n                    core.write_json(artifact, self.synthetic_review(state, core.sha256_file(architecture)))\n                elif name == "architecture-review-attention":\n                    generated = root / "sources" / state["issue_id"] / "generated"\n                    review_attention.build_attention(\n                        root,\n                        generated / "DISCOVERY_COLLECTED-screening.json",\n                        generated / "CANDIDATES_NORMALIZED-materiality.json",\n                        generated / "EVIDENCE_REVIEWED-selection.json",\n                        artifact,\n                    )\n                else:\n',
)
replace_once(
    "tests/test_survey_orchestrator_v2.py",
    '        self.assertEqual(gate_inputs["architecture-review-summary"]["sha256"], core.sha256_file(root / "sources/SP001/architecture-review-summary-v2.json"))\n',
    '        self.assertEqual(gate_inputs["architecture-review-summary"]["sha256"], core.sha256_file(root / "sources/SP001/architecture-review-summary-v2.json"))\n        self.assertEqual(gate_inputs["architecture-review-attention"]["sha256"], core.sha256_file(root / "sources/SP001/architecture-review-attention-v2.json"))\n',
)
