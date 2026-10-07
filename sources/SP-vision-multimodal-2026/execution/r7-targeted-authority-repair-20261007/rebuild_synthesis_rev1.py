#!/usr/bin/env python3
"""Rebuild synthesis input/result only (rev1 payload fix), then revalidate.

Used after targeted spec synthesis-payload edits that do not touch package prose.
Reuses regenerate_rev1 builders + validators. Frozen Core untouched.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECDIR = SRC / "execution/r7-targeted-authority-repair-20261007"


def main() -> int:
    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(EXECDIR))
    from scripts import survey_drafting_v2 as drafting
    from scripts import survey_production_v2 as core
    import regenerate_rev1 as regen
    import validate_overlay as oval

    root = ROOT
    up = regen._upstream(root, SRC / "production-state.json")
    spec = json.loads((EXECDIR / "compact-input-fresh-121-r7-rev1.json").read_text(encoding="utf-8"))
    assert spec.get("draft_version") == "fresh-121-r7-rev1"
    draft_root = up["source_root"] / "draft/v2"
    pairs = []
    for pid in ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B", "P08", "P09",
                "P10", "P11", "P12", "P13", "P14", "P15"]:
        pairs.append((draft_root / "packages" / pid / "draft-package.json",
                      draft_root / "packages" / pid / "draft-result.json"))
    synthesis_input = regen._build_synthesis_input_with_overlay(root, up, pairs)
    synthesis_input_path = draft_root / "profile-synthesis-input.json"
    core.write_json(synthesis_input_path, synthesis_input)
    fresh_syn = spec.get("synthesis", {}).get("profile_payload", {})
    assert fresh_syn and "VM-D114" in json.dumps(fresh_syn, ensure_ascii=False)
    cur = core.load_json(draft_root / "profile-synthesis-result.json")
    synthesis_result = {
        "schema_version": "2.0-rc1", "issue_id": up["state"]["issue_id"],
        "research_profile": up["state"]["research_profile"],
        "publication_profile": up["state"]["publication_profile"],
        "synthesis_version": "v1.0", "status": "ESTABLISHED",
        "basis": {"synthesis_input_sha256": core.sha256_file(synthesis_input_path),
                  "prompt_id": "profile-synthesis-v2",
                  "prompt_sha256": core.sha256_file(root / drafting.SYNTHESIS_PROMPT)},
        "runner": dict(spec["runner"], run_reference=None),
        "profile_payload": fresh_syn,
        "publication_payload": spec.get("synthesis", {}).get("publication_payload", {}),
    }
    errs = drafting.validate_synthesis_result(
        synthesis_result, synthesis_input_path, root / drafting.SYNTHESIS_PROMPT)
    assert not errs, errs
    core.write_json(draft_root / "profile-synthesis-result.json", synthesis_result)
    print("synthesis rebuilt: input",
          core.sha256_file(synthesis_input_path)[:12], "result",
          core.sha256_file(draft_root / "profile-synthesis-result.json")[:12])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
