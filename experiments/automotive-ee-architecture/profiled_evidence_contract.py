#!/usr/bin/env python3
"""Build an experiment-only Evidence contract from the production contract shape.

The production Evidence schemas and prompt remain untouched. The adapter reuses the
existing Evidence Run/Card structure, replacing only the closed AI artifact_type enum
with the domain ontology declared by evidence-profile.json and packaging a
domain-specific prompt beside it.

This is an abstraction probe, not a proposal to weaken the production AI contract.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any

ARTIFACT_TYPE_RE = re.compile(r"^[A-Z][A-Z0-9_]{1,63}$")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_repo_path(repo_root: Path, configured: str, label: str) -> Path:
    value = Path(configured)
    path = value if value.is_absolute() else repo_root / value
    path = path.resolve()
    if not path.is_file():
        raise ValueError(f"{label} missing: {path}")
    return path


def validate_artifact_types(profile: dict[str, Any]) -> list[str]:
    raw = profile.get("artifact_types")
    if not isinstance(raw, list) or not raw:
        raise ValueError("profile.artifact_types must be a non-empty array")
    values: list[str] = []
    seen: set[str] = set()
    for item in raw:
        if not isinstance(item, str) or not ARTIFACT_TYPE_RE.fullmatch(item):
            raise ValueError(f"invalid artifact type: {item!r}")
        if item in seen:
            raise ValueError(f"duplicate artifact type: {item}")
        seen.add(item)
        values.append(item)
    if "OTHER" not in seen:
        raise ValueError("profile.artifact_types must include OTHER as an explicit escape hatch")
    return values


def generated_card_schema(base_card: dict[str, Any], artifact_types: list[str], profile_id: str) -> dict[str, Any]:
    # JSON round-trip provides a deterministic deep copy while ensuring the source
    # schema object cannot be mutated by accident.
    result = json.loads(json.dumps(base_card, ensure_ascii=False))
    try:
        artifact = result["properties"]["artifact"]["properties"]
        old_type = artifact["artifact_type"]
    except (KeyError, TypeError) as exc:
        raise ValueError("base Evidence Card schema does not expose artifact.artifact_type") from exc
    if not isinstance(old_type, dict) or not isinstance(old_type.get("enum"), list):
        raise ValueError("base artifact_type is no longer a closed enum; abstraction probe must be reviewed")
    artifact["artifact_type"] = {"enum": artifact_types}
    # Keep the generated contract relocatable inside an execution package. A
    # relative $id lets evidence-run.schema.json resolve evidence-card.schema.json
    # against the package retrieval location without reaching back to production.
    result["$id"] = "evidence-card.schema.json"
    result["title"] = f"Profiled Survey Evidence Card ({profile_id})"
    return result


def generated_run_schema(base_run: dict[str, Any], profile_id: str) -> dict[str, Any]:
    result = json.loads(json.dumps(base_run, ensure_ascii=False))
    try:
        card_ref = result["properties"]["card"]["$ref"]
    except (KeyError, TypeError) as exc:
        raise ValueError("base Evidence Run schema does not expose card.$ref") from exc
    if card_ref != "evidence-card.schema.json":
        raise ValueError(f"unexpected base Evidence Card ref: {card_ref!r}")
    result["$id"] = "evidence-run.schema.json"
    result["title"] = f"Profiled Survey Evidence Runner Output ({profile_id})"
    return result


def build(*, repo_root: Path, profile_path: Path, output_root: Path) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    profile_path = profile_path.resolve()
    output_root = output_root.resolve()
    profile = load_json(profile_path)
    profile_id = profile.get("profile_id")
    if not isinstance(profile_id, str) or not profile_id.strip():
        raise ValueError("profile_id must be non-empty")

    artifact_types = validate_artifact_types(profile)
    prompt_path = resolve_repo_path(repo_root, profile["prompt"], "Evidence prompt")
    base_run_path = resolve_repo_path(repo_root, profile["base_evidence_run_schema"], "base Evidence Run schema")
    base_card_path = resolve_repo_path(repo_root, profile["base_evidence_card_schema"], "base Evidence Card schema")
    base_run = load_json(base_run_path)
    base_card = load_json(base_card_path)

    contract = output_root / "contract"
    contract.mkdir(parents=True, exist_ok=True)
    prompt_target = contract / "primary-source-verification-v0.1.md"
    shutil.copyfile(prompt_path, prompt_target)
    run_target = contract / "evidence-run.schema.json"
    card_target = contract / "evidence-card.schema.json"
    write_json(run_target, generated_run_schema(base_run, profile_id))
    write_json(card_target, generated_card_schema(base_card, artifact_types, profile_id))

    # The production contract pins this prompt ID. Keep it unchanged so the probe
    # measures domain context/ontology separation rather than inventing a parallel
    # execution protocol.
    prompt_id = base_run.get("properties", {}).get("prompt_id", {}).get("const")
    if prompt_id != "primary-source-verification-v0.1":
        raise ValueError(f"unexpected production prompt_id contract: {prompt_id!r}")

    manifest = {
        "schema_version": "1.0",
        "experiment": "PROFILED_EVIDENCE_CONTRACT",
        "profile_id": profile_id,
        "issue_id": profile.get("issue_id"),
        "prompt_id": prompt_id,
        "artifact_types": artifact_types,
        "production_files_modified": [],
        "base": {
            "evidence_run_schema": {
                "path": base_run_path.relative_to(repo_root).as_posix(),
                "sha256": sha256_file(base_run_path),
            },
            "evidence_card_schema": {
                "path": base_card_path.relative_to(repo_root).as_posix(),
                "sha256": sha256_file(base_card_path),
            },
        },
        "generated": {
            "prompt": {"path": "contract/primary-source-verification-v0.1.md", "sha256": sha256_file(prompt_target)},
            "evidence_run_schema": {"path": "contract/evidence-run.schema.json", "sha256": sha256_file(run_target)},
            "evidence_card_schema": {"path": "contract/evidence-card.schema.json", "sha256": sha256_file(card_target)},
        },
        "abstraction_boundary": {
            "shared_unchanged_shape": [
                "runner provenance",
                "source classes",
                "evidence classes",
                "events",
                "claims",
                "metrics",
                "limitations",
                "verification targets",
                "editorial recommendation"
            ],
            "domain_profiled": ["Evidence prompt", "artifact.artifact_type enum"],
            "note": "Generated schemas are experiment artifacts. Production AI schemas remain authoritative for AI survey editions."
        },
    }
    write_json(output_root / "evidence-contract-manifest.json", manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--profile", required=True)
    parser.add_argument("--output-root", required=True)
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    profile_path = Path(args.profile)
    if not profile_path.is_absolute():
        profile_path = repo_root / profile_path
    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = repo_root / output_root
    manifest = build(repo_root=repo_root, profile_path=profile_path, output_root=output_root)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
