#!/usr/bin/env python3
"""Index and verify immutable raw-source files for one weekly issue."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")


def load_index(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def discover_raw_files(repo_root: Path, issue_id: str) -> list[Path]:
    issue_root = repo_root / "sources" / issue_id
    if not issue_root.exists():
        return []
    files: list[Path] = []
    for path in issue_root.rglob("*"):
        if not path.is_file() or path.name.startswith("."):
            continue
        relative = path.relative_to(issue_root)
        if "raw" in relative.parts:
            files.append(path)
    return sorted(files)


def entry_for(repo_root: Path, path: Path) -> dict[str, Any]:
    return {
        "path": path.relative_to(repo_root).as_posix(),
        "sha256": sha256_file(path),
        "bytes": path.stat().st_size,
    }


def indexed_map(index: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    if index is None:
        return {}
    return {entry["path"]: entry for entry in index.get("entries", [])}


def check(repo_root: Path, issue_id: str, index_path: Path) -> tuple[dict[str, Any], bool]:
    index = load_index(index_path)
    current_files = discover_raw_files(repo_root, issue_id)
    current = {entry["path"]: entry for entry in (entry_for(repo_root, p) for p in current_files)}
    indexed = indexed_map(index)

    missing = sorted(set(indexed) - set(current))
    unindexed = sorted(set(current) - set(indexed))
    changed = []
    for path in sorted(set(indexed) & set(current)):
        if (
            indexed[path].get("sha256") != current[path]["sha256"]
            or indexed[path].get("bytes") != current[path]["bytes"]
        ):
            changed.append(
                {
                    "path": path,
                    "indexed_sha256": indexed[path].get("sha256"),
                    "current_sha256": current[path]["sha256"],
                    "indexed_bytes": indexed[path].get("bytes"),
                    "current_bytes": current[path]["bytes"],
                }
            )

    report = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "index_path": index_path.relative_to(repo_root).as_posix(),
        "index_exists": index is not None,
        "passed": index is not None and not missing and not unindexed and not changed,
        "indexed_count": len(indexed),
        "current_raw_count": len(current),
        "missing_indexed_files": missing,
        "unindexed_raw_files": unindexed,
        "modified_raw_files": changed,
    }
    return report, bool(report["passed"])


def update(repo_root: Path, issue_id: str, index_path: Path) -> tuple[dict[str, Any], bool]:
    existing = load_index(index_path)
    current_files = discover_raw_files(repo_root, issue_id)
    current = {entry["path"]: entry for entry in (entry_for(repo_root, p) for p in current_files)}
    indexed = indexed_map(existing)

    missing = sorted(set(indexed) - set(current))
    changed = []
    for path in sorted(set(indexed) & set(current)):
        if (
            indexed[path].get("sha256") != current[path]["sha256"]
            or indexed[path].get("bytes") != current[path]["bytes"]
        ):
            changed.append(path)

    if missing or changed:
        report = {
            "schema_version": "1.0",
            "issue_id": issue_id,
            "passed": False,
            "refused_update": True,
            "missing_indexed_files": missing,
            "modified_indexed_files": changed,
            "note": "Existing indexed raw files are immutable. Restore them before updating the index.",
        }
        return report, False

    merged = dict(indexed)
    added = []
    for path, entry in current.items():
        if path not in merged:
            merged[path] = entry
            added.append(path)

    if existing is None or added:
        index = {
            "schema_version": "1.0",
            "issue_id": issue_id,
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "entries": [merged[path] for path in sorted(merged)],
        }
        write_json(index_path, index)

    report = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "passed": True,
        "index_path": index_path.relative_to(repo_root).as_posix(),
        "added": added,
        "indexed_count": len(merged),
        "note": "No existing indexed raw file was modified or removed.",
    }
    return report, True


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--index")
    parser.add_argument("--report")
    parser.add_argument("mode", choices=["check", "update"])
    return parser


def main() -> int:
    args = build_parser().parse_args()
    repo_root = Path(args.repo_root).resolve()
    index_path = (
        Path(args.index).resolve()
        if args.index
        else repo_root / "sources" / args.issue_id / "raw-index.json"
    )

    if args.mode == "check":
        report, passed = check(repo_root, args.issue_id, index_path)
    else:
        report, passed = update(repo_root, args.issue_id, index_path)

    if args.report:
        write_json(Path(args.report), report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
