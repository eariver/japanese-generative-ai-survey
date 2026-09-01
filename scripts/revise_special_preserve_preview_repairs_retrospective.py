#!/usr/bin/env python3
"""Run preserve-preview repairs while keeping the active edition's page budget metadata."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_preserve_preview_repairs as core


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    result = core.build(root, special_slug, issue_id, source_version)

    edition = load_json(root / "specials" / special_slug / "edition.json")
    budget = edition.get("page_budget") or {}
    soft_target = int(budget["target"])
    hard_max = int(budget["max"])

    state_path = root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    source = state["provenance"]["validated_issue_source"]
    manifest_path = root / source["path"]
    manifest = load_json(manifest_path)

    layout = manifest.setdefault("layout", {})
    layout["page_count_policy"] = (
        f"{soft_target}-page soft editorial target; {hard_max}-page hard ceiling from edition manifest; "
        "no padding solely to meet soft target"
    )
    revision = manifest.setdefault("layout_revision", {})
    revision["page_target_soft"] = soft_target
    revision["page_target_hard_max"] = hard_max
    revision["page_budget_source"] = f"specials/{special_slug}/edition.json"
    write_json(manifest_path, manifest)

    source["sha256"] = sha256(manifest_path)
    write_json(state_path, state)

    result["source_manifest_sha256"] = source["sha256"]
    result["page_target_soft"] = soft_target
    result["page_target_hard_max"] = hard_max
    result["page_budget_source"] = f"specials/{special_slug}/edition.json"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()

    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
