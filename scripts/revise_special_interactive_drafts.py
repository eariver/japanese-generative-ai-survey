#!/usr/bin/env python3
"""Re-open validated Special article drafting before Publication Preview.

This recovery path is intentionally narrow. It is allowed only before the
Publication Preview human gate, keeps the already approved Architecture and
immutable Draft Packages, archives all downstream provenance, removes any stale
preview-transfer copy, and re-runs the canonical evidence-linked Article Draft
validator/renderer against a complete revised override set.

It does not change Candidate Selection, Architecture, Evidence, Raw provenance,
or Draft Packages. Revised prose must therefore remain within the exact
Evidence surface previously authorized by Architecture.
"""
from __future__ import annotations

import argparse
import copy
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

from scripts import accept_special_interactive_drafts

DOWNSTREAM_PROVENANCE_KEYS = (
    "article_draft",
    "issue_synthesis",
    "claim_and_chronology_validation",
    "validated_issue_source",
    "annual_chronology",
    "latex_build",
    "publication_preview",
    "visual_review",
    "freeze",
)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def valid_datetime(value: str) -> bool:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def reset_for_redraft(repo_root: Path, issue_id: str, revision_reference: str, reset_at: str) -> dict[str, Any]:
    if not valid_datetime(reset_at):
        raise ValueError("reset_at must be timezone-aware ISO-8601")
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    if state.get("lifecycle_state") not in {"VALIDATED_DRAFT", "RELEASE_CANDIDATE"}:
        raise ValueError(
            "pre-publication redraft requires VALIDATED_DRAFT or RELEASE_CANDIDATE; "
            f"got {state.get('lifecycle_state')!r}"
        )
    gates = state.get("gates") or {}
    if gates.get("issue_architecture") != "passed":
        raise ValueError("approved Architecture is required")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("redraft is forbidden after Visual Review or Freeze has begun")
    automation = state.get("automation") or {}
    if automation.get("human_gate_required_for_publication_preview") is not True:
        raise ValueError("pipeline does not expose the expected Publication Preview boundary")
    if "publication_preview" in (state.get("provenance") or {}):
        raise ValueError("redraft is forbidden after Publication Preview approval has been recorded")

    provenance = state.setdefault("provenance", {})
    snapshot = {
        "reset_at": reset_at,
        "revision_reference": revision_reference,
        "prior_lifecycle_state": state.get("lifecycle_state"),
        "prior_gates": copy.deepcopy(gates),
        "prior_downstream_provenance": {
            key: copy.deepcopy(provenance[key]) for key in DOWNSTREAM_PROVENANCE_KEYS if key in provenance
        },
    }
    history = state.setdefault("provenance_history", {})
    history.setdefault("pre_publication_redraft", []).append(snapshot)

    for key in DOWNSTREAM_PROVENANCE_KEYS:
        provenance.pop(key, None)
    state["lifecycle_state"] = "ARCHITECTURE_ESTABLISHED"
    state["gates"]["article_draft"] = "pending"
    state["gates"]["claim_and_chronology_validation"] = "pending"
    state["gates"]["latex_build"] = "pending"
    state["gates"]["visual_review"] = "pending"
    state["gates"]["freeze"] = "pending"
    write_json(state_path, state)

    preview_dir = repo_root / "sources" / issue_id / "preview-transfer"
    if preview_dir.exists():
        shutil.rmtree(preview_dir)
    return snapshot


def run(
    *, repo_root: Path, issue_id: str, package_dir: Path, overrides_dir: Path,
    prompt_path: Path, provider: str, model: str, invocation: str,
    generated_at: str, run_reference: str,
) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    prior_state = load_json(state_path)
    prior_article = copy.deepcopy((prior_state.get("provenance") or {}).get("article_draft"))
    snapshot = reset_for_redraft(repo_root, issue_id, run_reference, generated_at)
    acceptance = accept_special_interactive_drafts.accept(
        repo_root,
        issue_id,
        package_dir.resolve(),
        overrides_dir.resolve(),
        prompt_path.resolve(),
        provider,
        model,
        invocation,
        generated_at,
        run_reference,
    )
    state = load_json(state_path)
    if state.get("lifecycle_state") != "DRAFT_COMPLETE":
        raise ValueError("canonical Article Draft acceptance did not reach DRAFT_COMPLETE")
    if state.get("gates", {}).get("article_draft") != "passed":
        raise ValueError("canonical Article Draft acceptance did not pass article_draft gate")
    if state.get("gates", {}).get("issue_architecture") != "passed":
        raise ValueError("redraft unexpectedly changed the approved Architecture gate")
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "REDRAFT_ACCEPTED",
        "prior_article_draft": prior_article,
        "archived_snapshot": snapshot,
        "new_article_draft_result_set_sha256": acceptance["result_set_sha256"],
        "new_article_draft_count": acceptance["article_draft_count"],
        "run_reference": run_reference,
        "generated_at": generated_at,
        "architecture_reopened": False,
        "selection_reopened": False,
        "evidence_reopened": False,
        "publication_preview_approval_recorded": False,
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root", default=".")
    p.add_argument("--issue-id", required=True)
    p.add_argument("--package-dir", required=True)
    p.add_argument("--overrides-dir", required=True)
    p.add_argument("--prompt", default="config/prompts/editorial/article-drafting-v0.1.md")
    p.add_argument("--provider", default="OpenAI")
    p.add_argument("--model", default="GPT-5.6 Sol")
    p.add_argument("--invocation", default="interactive ChatGPT pre-publication redraft; no paid inference-provider API")
    p.add_argument("--generated-at", required=True)
    p.add_argument("--run-reference", required=True)
    p.add_argument("--audit-output")
    a = p.parse_args()
    root = Path(a.repo_root).resolve()
    result = run(
        repo_root=root,
        issue_id=a.issue_id,
        package_dir=root / a.package_dir,
        overrides_dir=root / a.overrides_dir,
        prompt_path=root / a.prompt,
        provider=a.provider,
        model=a.model,
        invocation=a.invocation,
        generated_at=a.generated_at,
        run_reference=a.run_reference,
    )
    if a.audit_output:
        write_json(Path(a.audit_output), result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
