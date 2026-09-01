#!/usr/bin/env python3
"""Temporary compatibility bridge for the SP-2021-Y repair runner.

The one-shot runner originally referenced this historical verifier name. Current
main uses ``special_period_consistency.py check``. This bridge verifies that the
requested source manifest is exactly the state-pinned source and then delegates
to the canonical checker. It is removed together with the temporary runner after
the SP-2021-Y Publication Preview repair is persisted.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-manifest", required=True)
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    state_path = root / "sources" / args.issue_id / "pipeline-state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    pinned = str(state["provenance"]["validated_issue_source"]["path"])
    requested = Path(args.source_manifest).as_posix()
    if pinned != requested:
        raise SystemExit(f"state-pinned source mismatch: pinned={pinned!r}, requested={requested!r}")

    if not args.issue_id.startswith("SP-"):
        raise SystemExit(f"unsupported issue id: {args.issue_id!r}")
    special_slug = args.issue_id.removeprefix("SP-")
    canonical = Path(__file__).with_name("special_period_consistency.py")
    control_root = canonical.parent.parent
    command = [
        sys.executable,
        str(canonical),
        "check",
        "--repo-root",
        str(root),
        "--special-slug",
        special_slug,
        "--issue-id",
        args.issue_id,
    ]
    env = os.environ.copy()
    existing = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = str(control_root) if not existing else str(control_root) + os.pathsep + existing
    return subprocess.call(command, env=env)


if __name__ == "__main__":
    raise SystemExit(main())
