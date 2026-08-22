#!/usr/bin/env python3
"""Foundation contracts and state authority for Survey Production Core v2.

WU-005 deliberately implements only the profile/state foundation. It does not
perform Source Intake, Screening, Evidence, drafting, or publication. Those
stages are registered by later work units.

Key invariants enforced here:
- research scope and temporal policy are separate;
- Weekly reuses the tested cutoff-to-cutoff calendar implementation;
- any named completed Weekly issue can be initialized without legacy state;
- Thematic profiles do not fabricate bounded coverage windows;
- Profile-defined initial research obligations are first-class;
- production-state.json is the sole v2 state authority;
- legacy pipeline-state.json is read-only compatibility evidence;
- semantic contract identity, executable commit identity, and artifact identity
  are distinct and checked before state transitions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

from scripts import weekly_pipeline

DEFAULT_CONFIG = Path("config/survey-production-v2.json")
PROFILE_SCHEMA = Path("schemas/survey-production-profile.schema.json")
STATE_SCHEMA = Path("schemas/survey-production-state.schema.json")
WEEKLY_ISSUE_RE = re.compile(r"^(?P<year>\d{4})-W(?P<week>\d{2})$")
ISSUE_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")

LIFECYCLE = (
    "ISSUE_INITIALIZED",
    "DISCOVERY_COLLECTED",
    "CANDIDATES_NORMALIZED",
    "EVIDENCE_REVIEWED",
    "SELECTION_COMPLETE",
    "ARCHITECTURE_ESTABLISHED",
    "DRAFT_COMPLETE",
    "VALIDATED_DRAFT",
    "RELEASE_CANDIDATE",
    "FROZEN",
)

CHECKPOINTS = (
    "discovery",
    "screening",
    "evidence",
    "materiality",
    "completeness",
    "selection",
    "architecture",
    "draft",
    "validation",
    "publication_preview",
    "freeze",
)

CONTRACT_KEYS = {
    "pipeline_contract_version",
    "pipeline_contract_sha256",
    "quality_contract_version",
    "quality_contract_sha256",
    "research_profile_version",
    "research_profile_sha256",
    "publication_profile_version",
    "publication_profile_sha256",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        value = json.load(fh)
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value


def json_bytes(data: dict[str, Any]) -> bytes:
    return (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(json_bytes(data))


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def sha256_object(value: Any) -> str:
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(payload)


def aggregate_file_hash(repo_root: Path, paths: list[str]) -> str:
    digest = hashlib.sha256()
    for rel in sorted(paths):
        path = repo_root / rel
        if not path.is_file():
            raise ValueError(f"contract file does not exist: {rel}")
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def parse_instant(value: str) -> datetime:
    return weekly_pipeline.parse_instant(value)


def iso_utc(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def repository_commit_sha(repo_root: Path, override: str | None = None) -> str:
    if override is not None:
        if len(override) != 40 or any(c not in "0123456789abcdef" for c in override):
            raise ValueError("implementation commit override must be a lowercase 40-hex SHA")
        return override
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise ValueError("cannot resolve implementation repository commit; pass --implementation-sha") from exc
    value = result.stdout.strip()
    if len(value) != 40:
        raise ValueError("git rev-parse HEAD did not return a 40-hex commit")
    return value


def contract_identity(repo_root: Path, cfg: dict[str, Any], research_profile: str, publication_profile: str) -> dict[str, str]:
    research = cfg["research_profiles"].get(research_profile)
    publication = cfg["publication_profiles"].get(publication_profile)
    if research is None:
        raise ValueError(f"unknown research profile: {research_profile}")
    if publication is None:
        raise ValueError(f"unknown publication profile: {publication_profile}")

    pipeline_files = list(cfg["contract_files"]["pipeline"])
    pipeline_files.extend([str(DEFAULT_CONFIG), str(PROFILE_SCHEMA), str(STATE_SCHEMA)])
    return {
        "pipeline_contract_version": cfg["pipeline_contract_version"],
        "pipeline_contract_sha256": aggregate_file_hash(repo_root, pipeline_files),
        "quality_contract_version": cfg["quality_contract_version"],
        "quality_contract_sha256": aggregate_file_hash(repo_root, list(cfg["contract_files"]["quality"])),
        "research_profile_version": research["version"],
        "research_profile_sha256": sha256_object({"name": research_profile, "contract": research}),
        "publication_profile_version": publication["version"],
        "publication_profile_sha256": sha256_object({"name": publication_profile, "contract": publication}),
    }


def validate_temporal_policy(research_profile: str, policy: dict[str, Any], cfg: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    mode = policy.get("mode")
    allowed = cfg["research_profiles"].get(research_profile, {}).get("temporal_policies", [])
    if mode not in allowed:
        errors.append(f"temporal policy {mode!r} is not allowed for research profile {research_profile}")
        return errors

    def required(*keys: str) -> None:
        for key in keys:
            if not policy.get(key):
                errors.append(f"temporal policy {mode} requires {key}")

    if mode == "ROLLING_WINDOW":
        required("window_start", "window_end", "cutoff", "timezone")
        forbidden = {"start", "end", "as_of"}
    elif mode == "BOUNDED_PERIOD":
        required("start", "end", "as_of", "timezone")
        forbidden = {"window_start", "window_end", "cutoff"}
    elif mode in {"OPEN_HISTORY_AS_OF", "CURRENT_STATE_AS_OF"}:
        required("as_of")
        forbidden = {"start", "end", "window_start", "window_end", "cutoff", "timezone"}
    else:
        errors.append(f"unsupported temporal policy: {mode}")
        return errors

    for key in forbidden:
        if key in policy:
            errors.append(f"temporal policy {mode} forbids {key}")
    for key, value in policy.items():
        if key == "mode" or key == "timezone":
            continue
        try:
            parse_instant(str(value))
        except ValueError:
            errors.append(f"temporal policy {mode} field {key} must be an offset-aware ISO-8601 instant")
    return errors


def _nonempty_string_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and len(value) == len(set(value))
        and all(isinstance(item, str) and bool(item.strip()) for item in value)
    )


def _safe_relative_repo_path(value: Any) -> bool:
    if not isinstance(value, str) or not value or "\\" in value:
        return False
    path = Path(value)
    return not path.is_absolute() and ".." not in path.parts


def repo_local_path(repo_root: Path, value: str, label: str) -> Path:
    if not _safe_relative_repo_path(value):
        raise ValueError(f"{label} must be a repository-relative path without traversal")
    root = repo_root.resolve()
    resolved = (root / value).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"{label} escapes repository root") from exc
    return resolved


def _validate_initial_obligations(scope: dict[str, Any], errors: list[str]) -> None:
    dimensions = scope.get("scope_dimensions")
    if not _nonempty_string_list(dimensions) or not dimensions:
        errors.append("research_scope.scope_dimensions must be a non-empty unique string array")
        dimensions = []
    allowed_dimensions = set(dimensions)
    obligations = scope.get("initial_obligations")
    if not isinstance(obligations, list) or not obligations:
        errors.append("research_scope.initial_obligations must contain at least one obligation")
        return
    seen_ids: set[str] = set()
    covered_dimensions: set[str] = set()
    expected_fields = {"obligation_id", "dimension", "description"}
    for index, obligation in enumerate(obligations):
        prefix = f"research_scope.initial_obligations[{index}]"
        if not isinstance(obligation, dict) or set(obligation) != expected_fields:
            errors.append(f"{prefix} fields must exactly match the v2 Profile contract")
            continue
        obligation_id = obligation.get("obligation_id")
        dimension = obligation.get("dimension")
        description = obligation.get("description")
        if not isinstance(obligation_id, str) or not obligation_id.strip():
            errors.append(f"{prefix}.obligation_id must be non-empty")
        elif obligation_id in seen_ids:
            errors.append(f"duplicate initial obligation_id: {obligation_id}")
        else:
            seen_ids.add(obligation_id)
        if dimension not in allowed_dimensions:
            errors.append(f"{prefix}.dimension must reference a declared scope dimension")
        else:
            covered_dimensions.add(dimension)
        if not isinstance(description, str) or not description.strip():
            errors.append(f"{prefix}.description must be non-empty")
    missing_dimensions = sorted(allowed_dimensions - covered_dimensions)
    if missing_dimensions:
        errors.append(f"initial obligations do not cover Profile dimensions: {missing_dimensions}")


def validate_profile(profile: dict[str, Any], cfg: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {"schema_version", "issue_id", "research_profile", "publication_profile", "research_scope", "paths", "contract"}
    if set(profile) != required:
        missing = sorted(required - set(profile))
        extra = sorted(set(profile) - required)
        if missing:
            errors.append(f"profile missing required fields: {', '.join(missing)}")
        if extra:
            errors.append(f"profile has unsupported fields: {', '.join(extra)}")
        return errors
    if profile["schema_version"] != cfg["schema_version"]:
        errors.append("profile schema_version does not match v2 contract manifest")
    if not isinstance(profile.get("issue_id"), str) or not ISSUE_ID_RE.fullmatch(profile["issue_id"]):
        errors.append("issue_id must be a path-safe identifier")
    research_profile = profile["research_profile"]
    publication_profile = profile["publication_profile"]
    if research_profile not in cfg["research_profiles"]:
        errors.append(f"unknown research profile: {research_profile}")
    if publication_profile not in cfg["publication_profiles"]:
        errors.append(f"unknown publication profile: {publication_profile}")
    if research_profile == "WEEKLY" and publication_profile != "WEEKLY_MAGAZINE":
        errors.append("WEEKLY research profile requires WEEKLY_MAGAZINE publication profile")
    if research_profile in {"RETROSPECTIVE_PERIOD", "THEMATIC"} and publication_profile != "LONGFORM_SPECIAL":
        errors.append(f"{research_profile} research profile requires LONGFORM_SPECIAL publication profile")

    scope = profile.get("research_scope")
    scope_keys = {"question", "inclusion", "exclusion", "scope_dimensions", "initial_obligations", "temporal_policy"}
    if not isinstance(scope, dict):
        errors.append("research_scope must be an object")
    elif set(scope) != scope_keys:
        errors.append("research_scope fields must exactly match the v2 Profile contract")
    else:
        if not isinstance(scope.get("question"), str) or not scope["question"].strip():
            errors.append("research_scope.question must be non-empty")
        for key in ("inclusion", "exclusion"):
            value = scope.get(key)
            if not isinstance(value, list) or any(not isinstance(item, str) or not item.strip() for item in value):
                errors.append(f"research_scope.{key} must be an array of non-empty strings")
        _validate_initial_obligations(scope, errors)
        policy = scope.get("temporal_policy")
        if isinstance(policy, dict) and research_profile in cfg["research_profiles"]:
            errors.extend(validate_temporal_policy(research_profile, policy, cfg))
        elif policy is not None:
            errors.append("research_scope.temporal_policy must be an object")

    paths = profile.get("paths")
    if not isinstance(paths, dict) or set(paths) != {"source_root", "survey_root", "work_branch"}:
        errors.append("paths fields must exactly match the v2 Profile contract")
    else:
        for key in ("source_root", "survey_root"):
            if not _safe_relative_repo_path(paths.get(key)):
                errors.append(f"paths.{key} must be a repository-relative path without traversal")
        branch = paths.get("work_branch")
        if not isinstance(branch, str) or not branch.strip() or branch.startswith("/") or ".." in branch.split("/"):
            errors.append("paths.work_branch must be a non-empty relative branch name without traversal segments")

    contract = profile.get("contract")
    if not isinstance(contract, dict) or set(contract) != CONTRACT_KEYS:
        errors.append("contract fields must exactly match the v2 Profile contract")
    else:
        for key in (
            "pipeline_contract_version",
            "quality_contract_version",
            "research_profile_version",
            "publication_profile_version",
        ):
            if not isinstance(contract.get(key), str) or not contract[key]:
                errors.append(f"contract.{key} must be non-empty")
        for key in (
            "pipeline_contract_sha256",
            "quality_contract_sha256",
            "research_profile_sha256",
            "publication_profile_sha256",
        ):
            value = contract.get(key)
            if not isinstance(value, str) or len(value) != 64 or any(ch not in "0123456789abcdef" for ch in value):
                errors.append(f"contract.{key} must be a lowercase SHA-256")
    return errors


def weekly_cutoff_for_issue(issue_id: str, weekly_cfg: dict[str, Any]) -> datetime:
    match = WEEKLY_ISSUE_RE.fullmatch(issue_id)
    if match is None:
        raise ValueError(f"invalid Weekly issue id: {issue_id}; expected YYYY-Www")
    year = int(match.group("year"))
    week = int(match.group("week"))
    editorial = weekly_cfg["editorial"]
    iso_weekday = weekly_pipeline.weekday_number(editorial["cutoff_weekday"]) + 1
    try:
        day = datetime.fromisocalendar(year, week, iso_weekday)
    except ValueError as exc:
        raise ValueError(f"invalid Weekly issue id: {issue_id}") from exc
    zone = ZoneInfo(editorial["cutoff_timezone"])
    cutoff = datetime(
        day.year,
        day.month,
        day.day,
        int(editorial["cutoff_hour"]),
        int(editorial.get("cutoff_minute", 0)),
        tzinfo=zone,
    )
    if weekly_pipeline.issue_id_from_cutoff(cutoff) != issue_id:
        raise ValueError(f"Weekly issue id does not map to configured cutoff calendar: {issue_id}")
    return cutoff


def weekly_profile(repo_root: Path, cfg: dict[str, Any], now: datetime, issue_id: str | None = None) -> dict[str, Any]:
    weekly_cfg = load_json(repo_root / "config/weekly-pipeline.json")
    now_utc = now.astimezone(timezone.utc)
    if issue_id is None:
        cutoff = weekly_pipeline.latest_cutoff(now_utc, weekly_cfg)
        resolved_issue = weekly_pipeline.issue_id_from_cutoff(cutoff)
    else:
        cutoff = weekly_cutoff_for_issue(issue_id, weekly_cfg)
        if cutoff.astimezone(timezone.utc) > now_utc:
            raise ValueError(f"requested Weekly issue {issue_id} has not completed its editorial cutoff yet")
        resolved_issue = issue_id
    start, end = weekly_pipeline.editorial_window(cutoff, weekly_cfg)
    dimensions = ["current relevance", "technical significance", "carry-over obligations"]
    initial_obligations = [
        {
            "obligation_id": "weekly:current-relevance",
            "dimension": "current relevance",
            "description": "Establish which developments materially belong in this completed Weekly issue and why they matter to the issue.",
        },
        {
            "obligation_id": "weekly:technical-significance",
            "dimension": "technical significance",
            "description": "Verify and prioritize the technical significance of candidate developments without relying on Weekly timing alone.",
        },
        {
            "obligation_id": "weekly:carry-over",
            "dimension": "carry-over obligations",
            "description": "Explicitly dispose every carry-over obligation inherited from prior Weekly work.",
        },
    ]
    profile = {
        "schema_version": cfg["schema_version"],
        "issue_id": resolved_issue,
        "research_profile": "WEEKLY",
        "publication_profile": "WEEKLY_MAGAZINE",
        "research_scope": {
            "question": f"What materially changed in generative AI for {resolved_issue}, and why does it matter now?",
            "inclusion": ["material generative-AI technical developments relevant to the issue window or explicit carry-over"],
            "exclusion": ["items without material technical/editorial relevance to the issue"],
            "scope_dimensions": dimensions,
            "initial_obligations": initial_obligations,
            "temporal_policy": {
                "mode": "ROLLING_WINDOW",
                "window_start": start.isoformat(timespec="seconds"),
                "window_end": end.isoformat(timespec="seconds"),
                "cutoff": cutoff.isoformat(timespec="seconds"),
                "timezone": weekly_cfg["editorial"]["cutoff_timezone"],
            },
        },
        "paths": {
            "source_root": f"sources/{resolved_issue}",
            "survey_root": f"surveys/weekly/{resolved_issue}",
            "work_branch": f"weekly/{resolved_issue}-v2-work",
        },
        "contract": contract_identity(repo_root, cfg, "WEEKLY", "WEEKLY_MAGAZINE"),
    }
    errors = validate_profile(profile, cfg)
    if errors:
        raise ValueError("invalid generated Weekly profile: " + "; ".join(errors))
    return profile


def _thematic_initial_obligations(spec: dict[str, Any], dimensions: list[str]) -> list[dict[str, str]]:
    supplied = spec.get("initial_obligations")
    if supplied is not None:
        if not isinstance(supplied, list):
            raise ValueError("thematic initial_obligations must be an array")
        return [dict(row) if isinstance(row, dict) else row for row in supplied]
    return [
        {
            "obligation_id": f"scope:{index:02d}",
            "dimension": dimension,
            "description": f"Establish evidence-backed coverage for the thematic scope dimension: {dimension}.",
        }
        for index, dimension in enumerate(dimensions, start=1)
    ]


def thematic_profile(repo_root: Path, cfg: dict[str, Any], spec: dict[str, Any]) -> dict[str, Any]:
    required = ("issue_id", "question", "temporal_mode", "as_of", "scope_dimensions")
    missing = [key for key in required if not spec.get(key)]
    if missing:
        raise ValueError("thematic spec missing required fields: " + ", ".join(missing))
    temporal_mode = spec["temporal_mode"]
    if temporal_mode not in {"OPEN_HISTORY_AS_OF", "CURRENT_STATE_AS_OF"}:
        raise ValueError("Thematic temporal_mode must be OPEN_HISTORY_AS_OF or CURRENT_STATE_AS_OF")
    policy = {"mode": temporal_mode, "as_of": iso_utc(parse_instant(spec["as_of"]))}
    issue_id = spec["issue_id"]
    dimensions = list(spec["scope_dimensions"])
    if not dimensions:
        raise ValueError("Thematic scope_dimensions must not be empty")
    initial_obligations = _thematic_initial_obligations(spec, dimensions)
    profile = {
        "schema_version": cfg["schema_version"],
        "issue_id": issue_id,
        "research_profile": "THEMATIC",
        "publication_profile": "LONGFORM_SPECIAL",
        "research_scope": {
            "question": spec["question"],
            "inclusion": list(spec.get("inclusion", [])),
            "exclusion": list(spec.get("exclusion", [])),
            "scope_dimensions": dimensions,
            "initial_obligations": initial_obligations,
            "temporal_policy": policy,
        },
        "paths": {
            "source_root": spec.get("source_root", f"sources/{issue_id}"),
            "survey_root": spec.get("survey_root", f"surveys/special/{issue_id}"),
            "work_branch": spec.get("work_branch", f"special/{issue_id}-v2-work"),
        },
        "contract": contract_identity(repo_root, cfg, "THEMATIC", "LONGFORM_SPECIAL"),
    }
    errors = validate_profile(profile, cfg)
    if errors:
        raise ValueError("invalid generated Thematic profile: " + "; ".join(errors))
    return profile


def initial_state(
    repo_root: Path,
    cfg: dict[str, Any],
    profile: dict[str, Any],
    profile_path: Path,
    implementation_sha: str,
    target_gate: str,
    recorded_at: datetime,
) -> dict[str, Any]:
    if target_gate not in cfg["human_gates"]:
        raise ValueError(f"unsupported target Human Gate: {target_gate}")
    source_root = repo_local_path(repo_root, profile["paths"]["source_root"], "paths.source_root")
    legacy_path = source_root / cfg["state_authority"]["legacy_filename"]
    legacy_present = legacy_path.is_file()
    legacy_sha = sha256_file(legacy_path) if legacy_present else None
    profile_sha = sha256_file(profile_path)
    state = {
        "schema_version": cfg["schema_version"],
        "issue_id": profile["issue_id"],
        "research_profile": profile["research_profile"],
        "publication_profile": profile["publication_profile"],
        "lifecycle_state": "ISSUE_INITIALIZED",
        "profile": {
            "path": str(profile_path.relative_to(repo_root.resolve())),
            "sha256": profile_sha,
        },
        "contract": dict(profile["contract"]),
        "implementation": {
            "repository_commit_sha": implementation_sha,
            "orchestrator_version": cfg["orchestrator_version"],
        },
        "human_gates": {
            "architecture_review": "pending",
            "publication_preview": "pending",
        },
        "target_gate": target_gate,
        "next_action": "DISCOVERY",
        "terminal_reason": None,
        "exception_gate": {"status": "inactive", "reason": None},
        "machine_checkpoints": {name: "pending" for name in CHECKPOINTS},
        "legacy_compatibility": {
            "mode": cfg["state_authority"]["legacy_mode"],
            "legacy_state_path": str(legacy_path.relative_to(repo_root.resolve())),
            "legacy_state_present": legacy_present,
            "legacy_state_sha256": legacy_sha,
        },
        "history": [
            {
                "from": None,
                "to": "ISSUE_INITIALIZED",
                "recorded_at": iso_utc(recorded_at),
                "repository_commit_sha": implementation_sha,
            }
        ],
    }
    return state


def verify_state_basis(
    repo_root: Path,
    cfg: dict[str, Any],
    state: dict[str, Any],
    implementation_sha: str,
) -> None:
    profile_path = repo_local_path(repo_root, state["profile"]["path"], "state.profile.path")
    if not profile_path.is_file():
        raise ValueError("production profile referenced by state does not exist")
    actual_profile_sha = sha256_file(profile_path)
    if actual_profile_sha != state["profile"]["sha256"]:
        raise ValueError("production profile bytes changed after state initialization")
    profile = load_json(profile_path)
    profile_errors = validate_profile(profile, cfg)
    if profile_errors:
        raise ValueError("production profile no longer satisfies v2 contract: " + "; ".join(profile_errors))
    if profile.get("issue_id") != state.get("issue_id"):
        raise ValueError("production profile/state issue_id divergence")
    if profile.get("contract") != state.get("contract"):
        raise ValueError("production profile/state contract divergence")

    expected_contract = contract_identity(repo_root, cfg, state["research_profile"], state["publication_profile"])
    if expected_contract != state["contract"]:
        raise ValueError("current semantic contract files differ from state contract identity")
    if state["implementation"]["repository_commit_sha"] != implementation_sha:
        raise ValueError("implementation commit differs from authoritative state; explicit rebase/reinitialization is required")
    if state["implementation"]["orchestrator_version"] != cfg["orchestrator_version"]:
        raise ValueError("orchestrator version differs from authoritative state")

    legacy = state["legacy_compatibility"]
    legacy_path = repo_local_path(repo_root, legacy["legacy_state_path"], "legacy_state_path")
    actual_present = legacy_path.is_file()
    actual_sha = sha256_file(legacy_path) if actual_present else None
    if actual_present != legacy["legacy_state_present"] or actual_sha != legacy["legacy_state_sha256"]:
        raise ValueError("legacy compatibility artifact changed after v2 initialization; it cannot silently affect v2 state")


def transition_state(
    repo_root: Path,
    cfg: dict[str, Any],
    state: dict[str, Any],
    to_state: str,
    implementation_sha: str,
    recorded_at: datetime,
) -> dict[str, Any]:
    verify_state_basis(repo_root, cfg, state, implementation_sha)
    if to_state not in LIFECYCLE:
        raise ValueError(f"unsupported lifecycle state: {to_state}")
    current = state["lifecycle_state"]
    current_index = LIFECYCLE.index(current)
    target_index = LIFECYCLE.index(to_state)
    if target_index != current_index + 1:
        raise ValueError(f"non-monotonic transition refused: {current} -> {to_state}; exactly one forward step is required")

    updated = json.loads(json.dumps(state))
    updated["lifecycle_state"] = to_state
    updated["history"].append(
        {
            "from": current,
            "to": to_state,
            "recorded_at": iso_utc(recorded_at),
            "repository_commit_sha": implementation_sha,
        }
    )
    return updated


def initialize(
    repo_root: Path,
    cfg: dict[str, Any],
    profile: dict[str, Any],
    implementation_sha: str,
    target_gate: str,
    recorded_at: datetime,
) -> tuple[Path, Path]:
    errors = validate_profile(profile, cfg)
    if errors:
        raise ValueError("invalid v2 Production Profile: " + "; ".join(errors))
    source_root = repo_local_path(repo_root, profile["paths"]["source_root"], "paths.source_root")
    profile_path = source_root / cfg["state_authority"]["profile_filename"]
    state_path = source_root / cfg["state_authority"]["authoritative_filename"]
    if profile_path.exists() or state_path.exists():
        raise ValueError(f"refusing destructive v2 initialization: {profile_path} or {state_path} already exists")
    source_root.mkdir(parents=True, exist_ok=True)
    write_json(profile_path, profile)
    state = initial_state(repo_root, cfg, profile, profile_path, implementation_sha, target_gate, recorded_at)
    write_json(state_path, state)
    return profile_path, state_path


def cmd_init_weekly(args: argparse.Namespace, repo_root: Path, cfg: dict[str, Any]) -> int:
    now = parse_instant(args.now) if args.now else datetime.now(timezone.utc)
    impl = repository_commit_sha(repo_root, args.implementation_sha)
    profile = weekly_profile(repo_root, cfg, now, args.issue_id)
    profile_path, state_path = initialize(repo_root, cfg, profile, impl, args.target_gate, now)
    print(json.dumps({"profile": str(profile_path.relative_to(repo_root)), "state": str(state_path.relative_to(repo_root))}, indent=2))
    return 0


def cmd_init_thematic(args: argparse.Namespace, repo_root: Path, cfg: dict[str, Any]) -> int:
    spec_path = Path(args.spec)
    if not spec_path.is_absolute():
        spec_path = repo_root / spec_path
    spec = load_json(spec_path)
    now = parse_instant(args.recorded_at) if args.recorded_at else datetime.now(timezone.utc)
    impl = repository_commit_sha(repo_root, args.implementation_sha)
    profile = thematic_profile(repo_root, cfg, spec)
    profile_path, state_path = initialize(repo_root, cfg, profile, impl, args.target_gate, now)
    print(json.dumps({"profile": str(profile_path.relative_to(repo_root)), "state": str(state_path.relative_to(repo_root))}, indent=2))
    return 0


def cmd_validate_profile(args: argparse.Namespace, repo_root: Path, cfg: dict[str, Any]) -> int:
    path = Path(args.profile)
    if not path.is_absolute():
        path = repo_root / path
    errors = validate_profile(load_json(path), cfg)
    print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


def cmd_transition(args: argparse.Namespace, repo_root: Path, cfg: dict[str, Any]) -> int:
    state_path = Path(args.state)
    if not state_path.is_absolute():
        state_path = repo_root / state_path
    state = load_json(state_path)
    impl = repository_commit_sha(repo_root, args.implementation_sha)
    now = parse_instant(args.recorded_at) if args.recorded_at else datetime.now(timezone.utc)
    updated = transition_state(repo_root, cfg, state, args.to_state, impl, now)
    write_json(state_path, updated)
    print(state_path)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--config", default=str(DEFAULT_CONFIG))
    sub = parser.add_subparsers(dest="command", required=True)

    weekly = sub.add_parser("init-weekly", help="initialize a v2 Weekly profile/state")
    weekly.add_argument("--now", help="offset-aware ISO-8601 instant")
    weekly.add_argument("--issue-id", help="optional named completed Weekly issue (YYYY-Www); defaults to latest completed cutoff")
    weekly.add_argument("--target-gate", choices=["ARCHITECTURE_REVIEW", "PUBLICATION_PREVIEW"], default="ARCHITECTURE_REVIEW")
    weekly.add_argument("--implementation-sha")

    thematic = sub.add_parser("init-thematic", help="initialize a v2 Thematic profile/state from a spec JSON")
    thematic.add_argument("--spec", required=True)
    thematic.add_argument("--recorded-at", help="offset-aware ISO-8601 state-record time")
    thematic.add_argument("--target-gate", choices=["ARCHITECTURE_REVIEW", "PUBLICATION_PREVIEW"], default="ARCHITECTURE_REVIEW")
    thematic.add_argument("--implementation-sha")

    validate_p = sub.add_parser("validate-profile", help="validate v2 profile semantics")
    validate_p.add_argument("--profile", required=True)

    transition = sub.add_parser("transition", help="perform one monotonic v2 lifecycle transition")
    transition.add_argument("--state", required=True)
    transition.add_argument("--to-state", choices=LIFECYCLE, required=True)
    transition.add_argument("--recorded-at", help="offset-aware ISO-8601 transition time")
    transition.add_argument("--implementation-sha")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = repo_root / config_path
    try:
        cfg = load_json(config_path)
        if args.command == "init-weekly":
            return cmd_init_weekly(args, repo_root, cfg)
        if args.command == "init-thematic":
            return cmd_init_thematic(args, repo_root, cfg)
        if args.command == "validate-profile":
            return cmd_validate_profile(args, repo_root, cfg)
        if args.command == "transition":
            return cmd_transition(args, repo_root, cfg)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    parser.error("unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
