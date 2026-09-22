#!/usr/bin/env python3
"""Reproducibility test for the compat package builder (§15): build twice from
identical canonical inputs in clean temp dirs; require identical projected
task bytes/hashes, identical package bytes/hash, identical ledger semantics.
"""
from __future__ import annotations

import filecmp
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_compat_evidence_package import build_once

from scripts import survey_production_v2 as core


def snapshot(out_dir: Path) -> dict:
    pkg = out_dir / "package.json"
    tasks = sorted((out_dir / "tasks").iterdir())
    return {
        "package_sha256": core.sha256_file(pkg),
        "package_bytes": pkg.read_bytes(),
        "task_shas": {p.name: core.sha256_file(p) for p in tasks},
    }


def main() -> int:
    root = Path(".").resolve()
    impl = core.repository_commit_sha(root)
    with tempfile.TemporaryDirectory() as t1, tempfile.TemporaryDirectory() as t2:
        d1 = Path(t1) / "compat-a"
        d2 = Path(t2) / "compat-b"
        ledger1 = build_once(root, d1, impl)
        ledger2 = build_once(root, d2, impl)
        s1, s2 = snapshot(d1), snapshot(d2)
        assert s1["package_sha256"] == s2["package_sha256"], "package hash differs"
        assert s1["package_bytes"] == s2["package_bytes"], "package bytes differ"
        assert s1["task_shas"] == s2["task_shas"], "task hashes differ"
        for name in s1["task_shas"]:
            assert filecmp.cmp(d1 / "tasks" / name, d2 / "tasks" / name, shallow=False), name
        rows1 = ledger1["rows"]
        rows2 = ledger2["rows"]
        assert rows1 == rows2, "ledger semantic content differs"
        assert ledger1["task_count"] == ledger2["task_count"] == 160
        assert ledger1["projected_count"] == ledger2["projected_count"] == 67
    print(json.dumps({
        "COMPATIBILITY_REPRODUCIBILITY": "PASS",
        "package_sha256": s1["package_sha256"],
        "task_count": 160,
        "projected_count": 67,
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
