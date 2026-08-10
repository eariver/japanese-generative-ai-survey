#!/usr/bin/env python3
"""Merge renderer-generated BibLaTeX files without silently resolving conflicts."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ENTRY_START = re.compile(r"^@online\{([A-Za-z0-9._:-]+),\s*$")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_generated_bib(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    entries: dict[str, str] = {}
    index = 0
    while index < len(lines):
        if not lines[index].strip():
            index += 1
            continue
        match = ENTRY_START.match(lines[index])
        if not match:
            raise ValueError(f"{path}:{index + 1}: expected generated @online entry")
        key = match.group(1)
        buffer = [lines[index]]
        index += 1
        while index < len(lines):
            buffer.append(lines[index])
            if lines[index].strip() == "}":
                break
            index += 1
        else:
            raise ValueError(f"{path}: unterminated entry {key}")
        text = "\n".join(buffer).rstrip() + "\n"
        if key in entries:
            raise ValueError(f"{path}: duplicate key inside file: {key}")
        entries[key] = text
        index += 1
    return entries


def merge(inputs: list[Path], output: Path, manifest_output: Path) -> tuple[dict[str, Any], bool]:
    if not inputs:
        raise ValueError("at least one generated bibliography is required")
    merged: dict[str, str] = {}
    origins: dict[str, list[str]] = {}
    conflicts: list[dict[str, Any]] = []
    input_records: list[dict[str, Any]] = []

    for path in sorted(inputs, key=lambda value: value.as_posix()):
        entries = parse_generated_bib(path)
        input_records.append({
            "path": path.as_posix(),
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
            "entry_count": len(entries),
        })
        for key, text in entries.items():
            if key not in merged:
                merged[key] = text
                origins[key] = [path.as_posix()]
            elif merged[key] == text:
                origins[key].append(path.as_posix())
            else:
                conflicts.append({
                    "key": key,
                    "first_origins": origins[key],
                    "conflicting_origin": path.as_posix(),
                })

    passed = not conflicts
    output.parent.mkdir(parents=True, exist_ok=True)
    if passed:
        output.write_text("\n".join(merged[key].rstrip() for key in sorted(merged)) + "\n", encoding="utf-8")
    elif output.exists():
        output.unlink()

    manifest = {
        "schema_version": "1.0",
        "passed": passed,
        "input_count": len(inputs),
        "entry_count": len(merged) if passed else 0,
        "inputs": input_records,
        "deduplicated_keys": sorted(key for key, values in origins.items() if len(values) > 1),
        "conflicts": conflicts,
        "output": (
            {"path": output.as_posix(), "sha256": sha256_file(output), "bytes": output.stat().st_size}
            if passed else None
        ),
        "note": "Identical URL-hash entries are deduplicated. Conflicting metadata for the same generated cite key is a hard failure and must be reconciled upstream in Evidence metadata.",
    }
    manifest_output.parent.mkdir(parents=True, exist_ok=True)
    manifest_output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest, passed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", action="append", required=True, dest="inputs")
    parser.add_argument("--output", required=True)
    parser.add_argument("--manifest-output", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, passed = merge(
        [Path(value) for value in args.inputs],
        Path(args.output),
        Path(args.manifest_output),
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
