#!/usr/bin/env python3
"""TS-003 formal Discovery re-execution (112 records): canonical corpus +
acceptance rebuilt under Human-gated re-entry to DISCOVERY_COLLECTED.

- Appends the staged VM-D112 record (byte-identical) to discovery-v2.jsonl.
- Supersedes discovery-accepted-v2.json IN PLACE: the 111-record file is a
  superseded stage output under re-entry (bytes survive in git history); the
  builder refuses overwrite, so the old file is removed first, then rebuilt
  + validated via canonical builders. No history rewrite (git retains all).
- Frozen Core only; no Core change. Post-gate adaptation: none needed here
  (build_acceptance takes no implementation SHA).
"""

from __future__ import annotations

import shutil
from pathlib import Path

from scripts import survey_discovery_v2 as discovery
from scripts import survey_production_v2 as core

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
JSONL_REL = f"{SRC}/discovery/discovery-v2.jsonl"
ACC_REL = f"{SRC}/discovery/discovery-accepted-v2.json"
X_REL = f"{SRC}/external/x/x-source-intake-v2.json"
STAGED_REL = (f"{SRC}/execution/upstream-rebind-post-r14-20261003/"
              "vm-d112-discovery-record.jsonl")


def main() -> int:
    root = Path(".").resolve()
    jsonl = root / JSONL_REL
    lines = jsonl.read_text(encoding="utf-8").strip().split("\n")
    assert len(lines) == 111, len(lines)
    staged = (root / STAGED_REL).read_text(encoding="utf-8").strip()
    assert staged.count("\n") == 0, "staged record must be one line"
    import json as _json
    rec = _json.loads(staged)
    assert rec["discovery_id"] == "VM-D112", rec["discovery_id"]
    assert all(_json.loads(line)["discovery_id"] != "VM-D112" for line in lines)
    jsonl.write_text("\n".join(lines + [staged]) + "\n", encoding="utf-8")

    acc = root / ACC_REL
    old_sha = core.sha256_file(acc)
    acc.unlink()  # superseded stage output under Human-gated re-entry; history retains bytes
    out = discovery.build_acceptance(root, jsonl, root / X_REL, ISSUE_ID, acc)
    accepted = discovery.validate_acceptance(root, out)
    assert accepted["record_count"] == 112, accepted["record_count"]
    print(f"discovery records: {accepted['record_count']}")
    print(f"old acceptance sha: {old_sha[:12]} -> new: {core.sha256_file(acc)[:12]}")
    print(f"graph sha: {accepted['graph_sha256'][:12]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
