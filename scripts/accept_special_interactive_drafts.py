#!/usr/bin/env python3
"""Accept a complete set of interactive Special article drafts and render them.

The submitted interactive draft bodies are preserved separately by the caller.
This script derives complete Article Draft Results by binding each body to the
exact immutable Draft Package and article-drafting prompt. It may only strengthen
attribution metadata when cited Evidence classes require a broader mode; prose,
Evidence refs, coverage declarations, and editorial requirements are not altered.

Only a complete six-package (or generally complete ARTICLE_DRAFTING package set)
acceptance advances the lifecycle to DRAFT_COMPLETE. Visual Review, Freeze, merge,
and public Release remain separate human gates.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

from scripts import render_article_draft_tex as renderer
from scripts import validate_article_draft as validator

ATTRIBUTED = {"VENDOR_CLAIM", "PROJECT_CLAIM", "AUTHOR_CLAIM"}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def valid_datetime(value: str) -> bool:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def classes_for_refs(refs: list[dict[str, Any]], evidence_index: dict[tuple[str, str, str], str]) -> set[str]:
    classes: set[str] = set()
    for ref in refs:
        key = (ref.get("evidence_task_id"), ref.get("kind"), ref.get("evidence_id"))
        evidence_class = evidence_index.get(key)
        if evidence_class:
            classes.add(evidence_class)
    return classes


def strengthened_mode(mode: str, classes: set[str]) -> str:
    """Return a validator-safe mode without weakening the submitted attribution."""
    if not classes:
        return mode
    has_attributed = bool(classes & ATTRIBUTED)
    has_social = "SOCIAL_OBSERVATION" in classes
    has_inference = "INFERENCE" in classes
    only_primary = classes <= {"PRIMARY_FACT"}

    if mode == "NONE":
        return mode
    if mode == "FACTUAL":
        if only_primary:
            return mode
        if has_social and not has_attributed and not has_inference and classes <= {"SOCIAL_OBSERVATION"}:
            return "SOCIAL"
        if has_attributed and not has_social and not has_inference:
            return "ATTRIBUTED"
        return "MIXED"
    if mode == "ATTRIBUTED" and (has_social or has_inference):
        return "MIXED"
    if mode == "SOCIAL" and classes != {"SOCIAL_OBSERVATION"}:
        return "MIXED"
    if mode == "INFERENCE" and (has_attributed or has_social):
        return "MIXED"
    return mode


def apply_attribution_strengthening(
    body: dict[str, Any], package: dict[str, Any]
) -> tuple[dict[str, Any], list[dict[str, str]]]:
    result = copy.deepcopy(body)
    evidence_index, _, _, evidence_errors = validator.build_evidence_index(package)
    if evidence_errors:
        raise ValueError(f"Draft Package Evidence index is invalid: {evidence_errors}")
    changes: list[dict[str, str]] = []

    def apply(location: str, obj: dict[str, Any], mode_key: str, refs_key: str) -> None:
        mode = obj.get(mode_key)
        refs = obj.get(refs_key)
        if not isinstance(mode, str) or not isinstance(refs, list):
            return
        new_mode = strengthened_mode(mode, classes_for_refs(refs, evidence_index))
        if new_mode != mode:
            obj[mode_key] = new_mode
            changes.append({"location": location, "from": mode, "to": new_mode})

    apply("deck", result, "deck_attribution_mode", "deck_evidence_refs")
    for index, block in enumerate(result.get("blocks") or []):
        if isinstance(block, dict):
            apply(f"blocks[{index}]/{block.get('block_id', 'UNKNOWN')}", block, "attribution_mode", "evidence_refs")
    return result, changes


def article_package_entries(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    entries = [
        entry for entry in manifest.get("package_files") or []
        if entry.get("execution_stage") == "ARTICLE_DRAFTING"
    ]
    return sorted(entries, key=lambda entry: (entry.get("drafting_order", 0), entry.get("package_id", "")))


def assemble_result(
    body: dict[str, Any],
    package_path: Path,
    prompt_path: Path,
    provider: str,
    model: str,
    invocation: str,
    generated_at: str,
    run_reference: str,
) -> tuple[dict[str, Any], list[dict[str, str]]]:
    package = load_json(package_path)
    if body.get("schema_version") != "1.0":
        raise ValueError("interactive body schema_version must be 1.0")
    if body.get("issue_id") != package.get("issue_id"):
        raise ValueError("interactive body issue_id does not match Draft Package")
    if body.get("package_id") != package.get("package_id"):
        raise ValueError("interactive body package_id does not match Draft Package")

    derived, attribution_changes = apply_attribution_strengthening(body, package)
    derived["basis"] = {
        "draft_package_sha256": sha256_file(package_path),
        "prompt_id": "article-drafting-v0.1",
        "prompt_sha256": sha256_file(prompt_path),
    }
    derived["runner"] = {
        "provider": provider,
        "model": model,
        "invocation": invocation,
        "generated_at": generated_at,
        "run_reference": run_reference,
    }

    # Stable top-level order for reviewability.
    order = [
        "schema_version", "issue_id", "package_id", "draft_version", "status",
        "basis", "runner", "headline", "deck", "deck_attribution_mode",
        "deck_evidence_refs", "blocks", "must_cover_coverage", "boundary_coverage",
        "late_breaking_acknowledged",
    ]
    return {key: derived[key] for key in order}, attribution_changes


def accept(
    repo_root: Path,
    issue_id: str,
    package_dir: Path,
    overrides_dir: Path,
    prompt_path: Path,
    provider: str,
    model: str,
    invocation: str,
    generated_at: str,
    run_reference: str,
) -> dict[str, Any]:
    if not valid_datetime(generated_at):
        raise ValueError("generated_at must be timezone-aware ISO-8601")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    if state.get("lifecycle_state") != "ARCHITECTURE_ESTABLISHED":
        raise ValueError(f"interactive drafting requires ARCHITECTURE_ESTABLISHED, got {state.get('lifecycle_state')}")
    gates = state.get("gates") or {}
    if gates.get("issue_architecture") != "passed" or gates.get("article_draft") != "pending":
        raise ValueError("interactive drafting requires issue_architecture=passed and article_draft=pending")

    package_manifest_path = package_dir / "draft-package-manifest.json"
    package_manifest = load_json(package_manifest_path)
    if package_manifest.get("issue_id") != issue_id or package_manifest.get("passed") is not True:
        raise ValueError("Draft Package manifest is not accepted for this issue")
    entries = article_package_entries(package_manifest)
    if not entries:
        raise ValueError("no ARTICLE_DRAFTING packages found")

    expected_body_names = {f"{entry['package_id']}.json" for entry in entries}
    actual_body_names = {path.name for path in overrides_dir.glob("*.json") if path.is_file()}
    if actual_body_names != expected_body_names:
        missing = sorted(expected_body_names - actual_body_names)
        extra = sorted(actual_body_names - expected_body_names)
        raise ValueError(f"interactive draft body set must be complete; missing={missing}, extra={extra}")

    staging = repo_root / ".tmp-special-draft-acceptance"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    accepted_dir = staging / "results"
    rendered_dir = staging / "rendered"
    validation_dir = staging / "validation"
    inputs_dir = staging / "submitted-bodies"
    for directory in (accepted_dir, rendered_dir, validation_dir, inputs_dir):
        directory.mkdir(parents=True, exist_ok=True)

    result_rows: list[dict[str, Any]] = []
    strengthening: list[dict[str, Any]] = []
    for entry in entries:
        package_id = entry["package_id"]
        package_path = package_dir / entry["path"]
        if sha256_file(package_path) != entry["sha256"]:
            raise ValueError(f"Draft Package digest mismatch: {package_id}")
        body_path = overrides_dir / f"{package_id}.json"
        body = load_json(body_path)
        shutil.copyfile(body_path, inputs_dir / body_path.name)
        draft, changes = assemble_result(
            body, package_path, prompt_path, provider, model, invocation, generated_at, run_reference
        )
        draft_path = accepted_dir / f"{package_id}.json"
        write_json(draft_path, draft)
        report, passed = validator.validate(package_path, draft_path, prompt_path)
        write_json(validation_dir / f"{package_id}.json", report)
        if not passed:
            raise ValueError(f"Article Draft validation failed for {package_id}: {report['errors']}")

        tex_path = rendered_dir / f"{package_id}.tex"
        bib_path = rendered_dir / f"{package_id}.bib"
        render_manifest_path = rendered_dir / f"{package_id}.render.json"
        render_manifest, _ = renderer.render(
            package_path, draft_path, prompt_path, tex_path, bib_path, render_manifest_path
        )
        result_rows.append({
            "package_id": package_id,
            "draft_path": f"results/{package_id}.json",
            "draft_sha256": sha256_file(draft_path),
            "validation_path": f"validation/{package_id}.json",
            "validation_sha256": sha256_file(validation_dir / f"{package_id}.json"),
            "tex_path": f"rendered/{package_id}.tex",
            "tex_sha256": render_manifest["tex"]["sha256"],
            "bib_path": f"rendered/{package_id}.bib",
            "bib_sha256": render_manifest["bib"]["sha256"],
        })
        for change in changes:
            strengthening.append({"package_id": package_id, **change})

    digest_material = "\n".join(
        f"{row['package_id']}\t{row['draft_sha256']}" for row in sorted(result_rows, key=lambda row: row["package_id"])
    ).encode("utf-8")
    result_set_sha = hashlib.sha256(digest_material).hexdigest()
    final_dir = repo_root / "sources" / issue_id / "drafting" / "runs" / result_set_sha
    if final_dir.exists():
        raise ValueError(f"draft result set already exists: {result_set_sha}")

    acceptance = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "ACCEPTED",
        "result_set_sha256": result_set_sha,
        "generated_at": generated_at,
        "basis": {
            "draft_package_manifest_path": package_manifest_path.relative_to(repo_root).as_posix(),
            "draft_package_manifest_sha256": sha256_file(package_manifest_path),
            "article_drafting_prompt_path": prompt_path.relative_to(repo_root).as_posix(),
            "article_drafting_prompt_sha256": sha256_file(prompt_path),
        },
        "article_draft_count": len(result_rows),
        "results": result_rows,
        "attribution_mode_strengthening": strengthening,
        "note": "Submitted interactive bodies are preserved byte-for-byte under submitted-bodies; accepted results are derived SHA-bound artifacts.",
    }
    write_json(staging / "acceptance.json", acceptance)
    shutil.move(staging.as_posix(), final_dir.as_posix())

    state["lifecycle_state"] = "DRAFT_COMPLETE"
    state["gates"]["article_draft"] = "passed"
    state.setdefault("provenance", {})["article_draft"] = {
        "result_set_path": final_dir.relative_to(repo_root).as_posix(),
        "result_set_sha256": result_set_sha,
        "acceptance_sha256": sha256_file(final_dir / "acceptance.json"),
        "article_draft_count": len(result_rows),
        "generated_at": generated_at,
    }
    write_json(state_path, state)
    return acceptance


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--package-dir", required=True)
    parser.add_argument("--overrides-dir", required=True)
    parser.add_argument("--prompt", default="config/prompts/editorial/article-drafting-v0.1.md")
    parser.add_argument("--provider", default="OpenAI")
    parser.add_argument("--model", default="GPT-5.6 Sol")
    parser.add_argument("--invocation", default="interactive ChatGPT project drafting; no paid inference-provider API")
    parser.add_argument("--generated-at", required=True)
    parser.add_argument("--run-reference", default="Interactive Special article drafting")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    root = Path(args.repo_root).resolve()
    acceptance = accept(
        root,
        args.issue_id,
        (root / args.package_dir).resolve(),
        (root / args.overrides_dir).resolve(),
        (root / args.prompt).resolve(),
        args.provider,
        args.model,
        args.invocation,
        args.generated_at,
        args.run_reference,
    )
    print(json.dumps(acceptance, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
