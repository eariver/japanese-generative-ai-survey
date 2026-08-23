#!/usr/bin/env python3
"""Generic Grok/X Source Intake handoff for Survey Production Core v2.

ChatGPT owns the research decision and task specification. This helper renders one
self-contained Grok task file, binds the exact Google Drive task-file path, and
records the exact Raw bytes after ChatGPT imports the returned Markdown from
Drive. It never calls Grok or Google Drive itself.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate

MANIFEST_SCHEMA = Path("schemas/x-source-intake-v2.schema.json")
BASE_PROMPT = Path("config/prompts/grok/x-source-intake-base-v1.md")
WEEKLY_PROMPT = Path("config/prompts/grok/x-source-intake-weekly-v1.md")
SPECIAL_PROMPT = Path("config/prompts/grok/x-source-intake-special-v1.md")
DEFAULT_RELATIVE_MANIFEST = Path("external/x/x-source-intake-v2.json")
TASK_FILENAME = "grok-task.md"
RUN_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


class XIntakeError(ValueError):
    pass


def _rel(repo_root: Path, path: Path) -> str:
    root = repo_root.resolve()
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(root))
    except ValueError as exc:
        raise XIntakeError(f"X intake path must be repository-local: {path}") from exc


def _safe_file(repo_root: Path, path: Path, label: str) -> Path:
    rel = _rel(repo_root, path)
    resolved = core.repo_local_path(repo_root, rel, label)
    if resolved.is_symlink() or not resolved.is_file():
        raise XIntakeError(f"{label} missing or unsafe: {rel}")
    return resolved


def _authority(repo_root: Path, path: Path) -> dict[str, str]:
    file = _safe_file(repo_root, path, "X intake authority")
    return {"path": _rel(repo_root, file), "sha256": core.sha256_file(file)}


def _profile(repo_root: Path, cfg: dict[str, Any], profile_path: Path) -> tuple[Path, dict[str, Any]]:
    path = _safe_file(repo_root, profile_path, "Production Profile")
    profile = core.load_json(path)
    errors = core.validate_profile(profile, cfg)
    if errors:
        raise XIntakeError("Production Profile invalid for X Source Intake: " + "; ".join(errors))
    return path, profile


def _external_cfg(cfg: dict[str, Any]) -> dict[str, Any]:
    value = cfg.get("external_source_intake", {}).get("x_grok")
    if not isinstance(value, dict):
        raise XIntakeError("external_source_intake.x_grok contract missing")
    return value


def _nonempty_strings(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or not value or any(not isinstance(item, str) or not item.strip() for item in value):
        raise XIntakeError(f"{label} must be a non-empty string array")
    return list(value)


def _validate_spec(spec: dict[str, Any]) -> dict[str, Any]:
    expected = {"decision", "rationale", "series_context", "runs"}
    if set(spec) != expected:
        raise XIntakeError("X intake spec fields must be decision/rationale/series_context/runs")
    if spec.get("decision") not in {"REQUIRED", "NOT_REQUIRED"}:
        raise XIntakeError("X intake decision must be REQUIRED or NOT_REQUIRED")
    if not isinstance(spec.get("rationale"), str) or not spec["rationale"].strip():
        raise XIntakeError("X intake rationale must be non-empty")
    if spec.get("series_context") not in {None, "GENERATIVE_AI_FOUNDATIONS"}:
        raise XIntakeError("unsupported X intake series_context")
    runs = spec.get("runs")
    if not isinstance(runs, list):
        raise XIntakeError("X intake runs must be an array")
    if spec["decision"] == "REQUIRED" and not runs:
        raise XIntakeError("REQUIRED X intake needs at least one Grok run")
    if spec["decision"] == "NOT_REQUIRED" and runs:
        raise XIntakeError("NOT_REQUIRED X intake must not carry Grok runs")
    seen: set[str] = set()
    normalized: list[dict[str, Any]] = []
    fields = {
        "run_id",
        "purpose",
        "research_questions",
        "coverage_focus",
        "time_scope",
        "expected_result_filename",
    }
    for row in runs:
        if not isinstance(row, dict) or set(row) != fields:
            raise XIntakeError("each X intake run must exactly match the run-spec contract")
        run_id = row.get("run_id")
        if not isinstance(run_id, str) or not RUN_ID_RE.fullmatch(run_id) or run_id in seen:
            raise XIntakeError(f"X intake run_id invalid or duplicated: {run_id}")
        seen.add(run_id)
        purpose = row.get("purpose")
        time_scope = row.get("time_scope")
        filename = row.get("expected_result_filename")
        if not isinstance(purpose, str) or not purpose.strip():
            raise XIntakeError(f"X intake purpose missing: {run_id}")
        if not isinstance(time_scope, str) or not time_scope.strip():
            raise XIntakeError(f"X intake time_scope missing: {run_id}")
        if (
            not isinstance(filename, str)
            or not filename.strip()
            or "/" in filename
            or "\\" in filename
            or filename in {".", ".."}
            or filename == TASK_FILENAME
        ):
            raise XIntakeError(f"X intake expected_result_filename invalid: {run_id}")
        normalized.append(
            {
                "run_id": run_id,
                "purpose": purpose,
                "research_questions": _nonempty_strings(row.get("research_questions"), f"{run_id}.research_questions"),
                "coverage_focus": _nonempty_strings(row.get("coverage_focus"), f"{run_id}.coverage_focus"),
                "time_scope": time_scope,
                "expected_result_filename": filename,
            }
        )
    return {
        "decision": spec["decision"],
        "rationale": spec["rationale"],
        "series_context": spec["series_context"],
        "runs": normalized,
    }


def _policy_and_category(cfg: dict[str, Any], profile: dict[str, Any], series_context: str | None) -> tuple[str, str]:
    xcfg = _external_cfg(cfg)
    research = profile["research_profile"]
    policy = xcfg.get("profile_policy", {}).get(research)
    if policy not in {"REQUIRED_BY_PROFILE", "CHATGPT_DECIDES"}:
        raise XIntakeError(f"missing X intake profile policy: {research}")
    if series_context == "GENERATIVE_AI_FOUNDATIONS":
        if research != "THEMATIC":
            raise XIntakeError("Generative AI Foundations X intake requires THEMATIC Production Profile")
        category = xcfg.get("series_category", {}).get(series_context)
    else:
        category = xcfg.get("drive_categories", {}).get(research)
    if category not in {
        "Weekly",
        "Retrospective_Special",
        "Thematic_Special",
        "Generative_AI_Foundations",
    }:
        raise XIntakeError(f"missing/invalid Google Drive category for X intake: {category}")
    return policy, category


def _render_run(
    repo_root: Path,
    profile: dict[str, Any],
    category: str,
    root_name: str,
    run: dict[str, Any],
    run_dir: Path,
) -> tuple[Path, str, str]:
    run_dir.mkdir(parents=True, exist_ok=True)
    task_path = run_dir / TASK_FILENAME
    if task_path.exists():
        raise XIntakeError(f"refusing to overwrite existing Grok task: {run['run_id']}")
    edition = Path(profile["paths"]["survey_root"]).name
    drive_path = f"{root_name}/{category}/{edition}/{run['run_id']}"
    drive_task_path = f"{drive_path}/{TASK_FILENAME}"
    overlay_path = WEEKLY_PROMPT if profile["research_profile"] == "WEEKLY" else SPECIAL_PROMPT
    base = (repo_root / BASE_PROMPT).read_text(encoding="utf-8")
    overlay = (repo_root / overlay_path).read_text(encoding="utf-8")
    base = base.replace("<TASK_ID>", run["run_id"]).replace("<ISSUE_ID>", profile["issue_id"])
    questions = "\n".join(f"- {value}" for value in run["research_questions"])
    focus = "\n".join(f"- {value}" for value in run["coverage_focus"])
    task = f"""# Grok X Source Intake Task — {run['run_id']}

This file is the complete execution authority for this Grok/X run. The Human handoff consists only of giving Grok the exact Google Drive path/reference to this file. Do not ask the Human to copy or restate the task body.

Issue: `{profile['issue_id']}`  
Research Profile: `{profile['research_profile']}`  
Purpose: {run['purpose']}  
Time scope: {run['time_scope']}  

## Research questions

{questions}

## Coverage focus

{focus}

## Google Drive handoff

Task file path:

`{drive_task_path}`

Result folder:

`{drive_path}`

Expected result filename:

`{run['expected_result_filename']}`

The run folder and this task file are prepared by ChatGPT before handoff. Read this exact task file, perform the requested X research, and save the final Markdown result into the result folder above and nowhere else.

Operational rules:

1. Use X as the observation/search surface described below.
2. Do not write to GitHub.
3. If this exact task file or result folder is unavailable, stop and report that condition instead of choosing another location.
4. Do not overwrite an existing result; use a revision suffix and report the actual filename.
5. The result remains Raw Observation. Downstream ChatGPT performs primary-source verification, repository import, and Discovery disposition.
6. Do not treat a missing ChatGPT-side Grok connector as relevant; this run is intentionally invoked by Human-mediated Drive task-file handoff.

---

{base.rstrip()}

---

{overlay.rstrip()}
"""
    task_path.write_text(task, encoding="utf-8")
    return task_path, drive_path, drive_task_path


def build_manifest(
    repo_root: Path,
    cfg: dict[str, Any],
    profile_path: Path,
    spec: dict[str, Any],
    output_path: Path | None = None,
) -> Path:
    profile_path, profile = _profile(repo_root, cfg, profile_path)
    normalized = _validate_spec(spec)
    policy, category = _policy_and_category(cfg, profile, normalized["series_context"])
    if policy == "REQUIRED_BY_PROFILE" and normalized["decision"] != "REQUIRED":
        raise XIntakeError(f"{profile['research_profile']} requires Grok/X Source Intake")
    xcfg = _external_cfg(cfg)
    root_name = xcfg.get("drive_root_name")
    if root_name != "Grok_X_SourseIntake":
        raise XIntakeError("Grok/X Google Drive root contract drift")
    source_root = core.repo_local_path(repo_root, profile["paths"]["source_root"], "X intake source_root")
    manifest_path = output_path or (source_root / DEFAULT_RELATIVE_MANIFEST)
    if not manifest_path.is_absolute():
        manifest_path = repo_root / manifest_path
    _rel(repo_root, manifest_path)
    if manifest_path.exists():
        raise XIntakeError(f"refusing to overwrite X Source Intake manifest: {manifest_path}")
    runs: list[dict[str, Any]] = []
    for run in normalized["runs"]:
        run_dir = manifest_path.parent / run["run_id"]
        task_path, drive_path, drive_task_path = _render_run(
            repo_root, profile, category, root_name, run, run_dir
        )
        runs.append(
            {
                **run,
                "run_folder": drive_path,
                "task_file_name": TASK_FILENAME,
                "drive_task_path": drive_task_path,
                "task": _authority(repo_root, task_path),
                "result": None,
            }
        )
    payload = {
        "schema_version": "2.0-rc1",
        "issue_id": profile["issue_id"],
        "production_profile": _authority(repo_root, profile_path),
        "research_profile": profile["research_profile"],
        "policy": policy,
        "series_context": normalized["series_context"],
        "decision": normalized["decision"],
        "rationale": normalized["rationale"],
        "drive_handoff": {
            "provider": "GOOGLE_DRIVE",
            "root_folder_name": root_name,
            "category": category,
            "edition_folder": Path(profile["paths"]["survey_root"]).name,
        },
        "runs": runs,
        "status": "COMPLETE" if normalized["decision"] == "NOT_REQUIRED" else "AWAITING_GROK",
    }
    schema_gate.validate_instance(payload, repo_root / MANIFEST_SCHEMA, label="X Source Intake manifest")
    core.write_json(manifest_path, payload)
    return manifest_path


def _validate_raw_ref(repo_root: Path, result: dict[str, Any], run_id: str) -> Path:
    raw = result["raw"]
    path = core.repo_local_path(repo_root, raw["path"], f"X Source Intake Raw {run_id}")
    if path.is_symlink() or not path.is_file():
        raise XIntakeError(f"X Source Intake Raw missing: {run_id}")
    if core.sha256_file(path) != raw["sha256"] or path.stat().st_size != raw["byte_count"]:
        raise XIntakeError(f"X Source Intake Raw authority drift: {run_id}")
    return path


def _validate_manifest_basis(
    repo_root: Path,
    cfg: dict[str, Any],
    payload: dict[str, Any],
) -> tuple[Path, dict[str, Any]]:
    profile_ref = payload["production_profile"]
    profile_path = core.repo_local_path(repo_root, profile_ref["path"], "X intake Production Profile")
    if profile_path.is_symlink() or not profile_path.is_file() or core.sha256_file(profile_path) != profile_ref["sha256"]:
        raise XIntakeError("X intake Production Profile authority drift")
    _, profile = _profile(repo_root, cfg, profile_path)
    if profile["issue_id"] != payload["issue_id"] or profile["research_profile"] != payload["research_profile"]:
        raise XIntakeError("X intake manifest/Profile identity mismatch")
    policy, category = _policy_and_category(cfg, profile, payload["series_context"])
    if payload["policy"] != policy:
        raise XIntakeError("X intake policy differs from current Profile contract")
    if policy == "REQUIRED_BY_PROFILE" and payload["decision"] != "REQUIRED":
        raise XIntakeError("Profile-required X intake was marked NOT_REQUIRED")
    xcfg = _external_cfg(cfg)
    expected_drive = {
        "provider": "GOOGLE_DRIVE",
        "root_folder_name": xcfg["drive_root_name"],
        "category": category,
        "edition_folder": Path(profile["paths"]["survey_root"]).name,
    }
    if payload["drive_handoff"] != expected_drive:
        raise XIntakeError("X intake Google Drive handoff identity drift")
    return profile_path, profile


def validate_manifest(
    repo_root: Path,
    cfg: dict[str, Any],
    manifest_path: Path,
    *,
    discovery_acceptance_path: Path | None = None,
    require_complete: bool = True,
) -> dict[str, Any]:
    payload = schema_gate.load_and_validate_json(
        manifest_path, repo_root / MANIFEST_SCHEMA, label="X Source Intake manifest"
    )
    _validate_manifest_basis(repo_root, cfg, payload)
    if require_complete and payload["status"] != "COMPLETE":
        raise XIntakeError("X Source Intake is not complete")
    accepted_by_id: dict[str, dict[str, Any]] | None = None
    if discovery_acceptance_path is not None:
        from scripts import survey_discovery_v2 as discovery

        accepted = discovery.validate_acceptance(repo_root, discovery_acceptance_path)
        if accepted["issue_id"] != payload["issue_id"]:
            raise XIntakeError("X intake/Discovery issue identity mismatch")
        accepted_by_id = {row["discovery_id"]: row for row in accepted["records"]}
    for run in payload["runs"]:
        task_ref = run["task"]
        task_path = core.repo_local_path(repo_root, task_ref["path"], f"X intake task {run['run_id']}")
        if task_path.is_symlink() or not task_path.is_file() or core.sha256_file(task_path) != task_ref["sha256"]:
            raise XIntakeError(f"X intake task authority drift: {run['run_id']}")
        expected_drive_task = f"{run['run_folder']}/{run['task_file_name']}"
        if run["task_file_name"] != TASK_FILENAME or run["drive_task_path"] != expected_drive_task:
            raise XIntakeError(f"X intake Drive task-file identity drift: {run['run_id']}")
        result = run["result"]
        if result is None:
            if require_complete:
                raise XIntakeError(f"X intake run has no imported result: {run['run_id']}")
            continue
        raw_path = _validate_raw_ref(repo_root, result, run["run_id"])
        if result["status"] == "NO_MATERIAL_SIGNAL" and result["discovery_disposition"] != "NO_MATERIAL_DISCOVERY":
            raise XIntakeError(f"NO_MATERIAL_SIGNAL run must use NO_MATERIAL_DISCOVERY: {run['run_id']}")
        if accepted_by_id is None:
            continue
        if result["discovery_disposition"] == "DISCOVERY_RECORDED":
            for discovery_id in result["discovery_ids"]:
                record = accepted_by_id.get(discovery_id)
                if record is None:
                    raise XIntakeError(f"X intake result references unknown Discovery: {discovery_id}")
                raw_paths = {ref["path"] for ref in record.get("raw_refs", [])}
                if _rel(repo_root, raw_path) not in raw_paths:
                    raise XIntakeError(
                        f"Discovery {discovery_id} does not bind the imported Grok Raw bytes for {run['run_id']}"
                    )
        elif result["discovery_ids"]:
            raise XIntakeError(f"NO_MATERIAL_DISCOVERY must not name Discovery IDs: {run['run_id']}")
    return payload


def record_result(
    repo_root: Path,
    cfg: dict[str, Any],
    manifest_path: Path,
    run_id: str,
    raw_path: Path,
    drive_file_name: str,
    observed_at: str,
    imported_at: str,
    result_status: str,
    discovery_disposition: str,
    discovery_ids: list[str],
    rationale: str,
) -> Path:
    payload = schema_gate.load_and_validate_json(
        manifest_path, repo_root / MANIFEST_SCHEMA, label="X Source Intake manifest"
    )
    _validate_manifest_basis(repo_root, cfg, payload)
    if payload["decision"] != "REQUIRED":
        raise XIntakeError("cannot record Grok result for NOT_REQUIRED X intake")
    if result_status not in {"SUCCESS", "PARTIAL", "INSUFFICIENT_EVIDENCE", "NO_MATERIAL_SIGNAL"}:
        raise XIntakeError("invalid X intake result status")
    if discovery_disposition not in {"DISCOVERY_RECORDED", "NO_MATERIAL_DISCOVERY"}:
        raise XIntakeError("invalid X intake discovery disposition")
    if not isinstance(drive_file_name, str) or not drive_file_name.strip() or "/" in drive_file_name or "\\" in drive_file_name:
        raise XIntakeError("drive_file_name must be one plain filename")
    if drive_file_name == TASK_FILENAME:
        raise XIntakeError("Grok result filename must not overwrite the task file")
    if not isinstance(rationale, str) or not rationale.strip():
        raise XIntakeError("X intake result rationale must be non-empty")
    core.parse_instant(observed_at)
    core.parse_instant(imported_at)
    if discovery_disposition == "DISCOVERY_RECORDED" and not discovery_ids:
        raise XIntakeError("DISCOVERY_RECORDED requires at least one Discovery ID")
    if discovery_disposition == "NO_MATERIAL_DISCOVERY" and discovery_ids:
        raise XIntakeError("NO_MATERIAL_DISCOVERY must not name Discovery IDs")
    raw = _safe_file(repo_root, raw_path, "imported Grok Raw")
    target: dict[str, Any] | None = None
    for run in payload["runs"]:
        if run["run_id"] == run_id:
            target = run
            break
    if target is None:
        raise XIntakeError(f"unknown X intake run_id: {run_id}")
    if target["result"] is not None:
        raise XIntakeError(f"refusing to overwrite recorded X intake result: {run_id}")
    target["result"] = {
        "status": result_status,
        "drive_file_name": drive_file_name,
        "observed_at": core.iso_utc(core.parse_instant(observed_at)),
        "imported_at": core.iso_utc(core.parse_instant(imported_at)),
        "raw": {
            "path": _rel(repo_root, raw),
            "sha256": core.sha256_file(raw),
            "byte_count": raw.stat().st_size,
        },
        "discovery_disposition": discovery_disposition,
        "discovery_ids": list(discovery_ids),
        "rationale": rationale,
    }
    payload["status"] = "COMPLETE" if all(run["result"] is not None for run in payload["runs"]) else "AWAITING_GROK"
    schema_gate.validate_instance(payload, repo_root / MANIFEST_SCHEMA, label="X Source Intake manifest")
    core.write_json(manifest_path, payload)
    return manifest_path


def _load_spec(path: Path) -> dict[str, Any]:
    value = core.load_json(path)
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    sub = parser.add_subparsers(dest="command", required=True)

    build = sub.add_parser("build")
    build.add_argument("--profile", required=True)
    build.add_argument("--spec", required=True)
    build.add_argument("--output")

    record = sub.add_parser("record-result")
    record.add_argument("--manifest", required=True)
    record.add_argument("--run-id", required=True)
    record.add_argument("--raw", required=True)
    record.add_argument("--drive-file-name", required=True)
    record.add_argument("--observed-at", required=True)
    record.add_argument("--imported-at", required=True)
    record.add_argument("--result-status", required=True)
    record.add_argument("--discovery-disposition", required=True)
    record.add_argument("--discovery-id", action="append", default=[])
    record.add_argument("--rationale", required=True)

    validate = sub.add_parser("validate")
    validate.add_argument("--manifest", required=True)
    validate.add_argument("--discovery-acceptance")
    validate.add_argument("--allow-awaiting", action="store_true")

    args = parser.parse_args()
    root = Path(args.repo_root).resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)

    def local(value: str) -> Path:
        path = Path(value)
        return path if path.is_absolute() else root / path

    try:
        if args.command == "build":
            output = local(args.output) if args.output else None
            path = build_manifest(root, cfg, local(args.profile), _load_spec(local(args.spec)), output)
        elif args.command == "record-result":
            path = record_result(
                root,
                cfg,
                local(args.manifest),
                args.run_id,
                local(args.raw),
                args.drive_file_name,
                args.observed_at,
                args.imported_at,
                args.result_status,
                args.discovery_disposition,
                list(args.discovery_id),
                args.rationale,
            )
        else:
            validate_manifest(
                root,
                cfg,
                local(args.manifest),
                discovery_acceptance_path=(local(args.discovery_acceptance) if args.discovery_acceptance else None),
                require_complete=not args.allow_awaiting,
            )
            path = local(args.manifest)
        print(path)
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
