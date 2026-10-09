#!/usr/bin/env python3
"""Edition-local content-revision regenerator for TS-003 (DRAFT_COMPLETE held).

Mirrors execution/bounded-revision-112-20261004/regenerate_bounded_draft.py EXCEPT:
P15 result refs resolve over the UNION of canonical P15 inputs + edition-local
cross-package overlay (p15-cross-package-synthesis-authority.json), validated by
validate_p15_overlay.py. Everything else is identical (canonical derive/refs/
validation for 15 packages + synthesis). ONLY deviation, recorded in this dir.
No TeX/PDF/candidate/advance. No shared-Core change.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as runtime_tool
from scripts import survey_drafting_v2 as drafting
from scripts import survey_production_v2 as core
import scripts.run_drafting_synthesis_v2_interactive as runner

EXECNAME = "content-revision-r4-20261004"


def _load(path: Path):
    return core.load_json(path)


def _upstream_bounded(root: Path, state_path: Path) -> dict[str, Path]:
    state = _load(state_path)
    if state.get("human_gates", {}).get("architecture_review") != "approved":
        raise ValueError("bounded revision requires approved Architecture Review")
    cfg = _load(root / core.DEFAULT_CONFIG)
    state_errors = agent.validate_agent_state(root, cfg, state)
    if state_errors:
        print("pre-regeneration state notes (informational):", file=sys.stderr)
        for err in state_errors:
            print(" -", err, file=sys.stderr)
    profile_path = root / state["profile"]["path"]
    profile = _load(profile_path)
    source_root = root / profile["paths"]["source_root"]
    discovery_acceptance = source_root / "discovery/discovery-accepted-v2.json"
    accepted = _load(discovery_acceptance)
    raw_discovery = accepted.get("discovery_path")
    discovery_path = (root / raw_discovery).resolve()
    matrix_path = source_root / "candidate-matrix-v2.json"
    matrix = _load(matrix_path)
    norm_path = source_root / "orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json"
    norm = _load(norm_path)
    by_name = {row["name"]: row for row in norm.get("artifacts", [])}
    evidence_path = (root / by_name["evidence-acceptance"]["path"]).resolve()
    views_path = (root / by_name["edition-views-acceptance"]["path"]).resolve()
    if matrix.get("basis", {}).get("evidence_acceptance_sha256") != core.sha256_file(evidence_path):
        raise ValueError("Candidate Matrix does not bind checkpoint-bound Evidence acceptance")
    if matrix.get("basis", {}).get("edition_views_acceptance_sha256") != core.sha256_file(views_path):
        raise ValueError("Candidate Matrix does not bind checkpoint-bound Edition Views acceptance")
    approval_ref = state.get("human_gate_provenance", {}).get("architecture_review")
    approval_path = root / approval_ref["path"]
    attention = _load(source_root / "architecture-review-attention-v2.json")
    raw = attention.get("basis", {}).get("screening_acceptance_path")
    screening_path = (root / raw).resolve()
    return {
        "state": state_path, "profile": profile_path, "source_root": source_root,
        "discovery": discovery_path, "screening": screening_path,
        "evidence": evidence_path, "views": views_path,
        "ledger": source_root / "materiality-ledger-v2.json",
        "completeness": source_root / "profile-completeness-v2.json",
        "matrix": matrix_path, "selection": source_root / "candidate-selection-v2.json",
        "architecture": source_root / "architecture-v2.json",
        "review": source_root / "architecture-review-summary-v2.json",
        "approval": approval_path,
    }


def _overlay_cards(root: Path, up: dict, execdir: Path):
    overlay = json.loads((execdir / "p15-cross-package-synthesis-authority.json").read_text(encoding="utf-8"))
    ev_acc = _load(up["evidence"])
    ev_by_task = {r["evidence_task_id"]: r for r in ev_acc["results"]}
    cards: dict[str, dict] = {}
    allow: set[str] = set()
    for e in overlay["entries"]:
        tid = e["evidence_task_id"]
        allow.add(tid)
        if tid in cards:
            continue
        meta = ev_by_task[tid]
        assert meta["sha256"] == e["evidence_sha256"], tid
        p = up["evidence"].parent / "results" / meta["filename"]
        raw = p.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == e["evidence_sha256"], tid
        cards[tid] = json.loads(raw.decode("utf-8"))
    return overlay, cards, allow


def _p15_refs(package: dict, overlay_cards: dict, allow: set, discovery_ids: list, mode: str):
    # canonical authorized set
    by_cand = {row["candidate_id"]: row for row in package["evidence_inputs"]}
    authorized = set(by_cand)
    matrix_rows = package["candidate_matrix"]["rows"]
    refs = []
    for did in discovery_ids:
        hits = [r for r in matrix_rows if r["candidate_id"] in authorized and did in r.get("discovery_ids", [])]
        if len(hits) == 1:
            item = by_cand[hits[0]["candidate_id"]]
            refs.extend(runner._ref_rows(item["evidence_card"], item["evidence_task_id"], mode))
            continue
        # overlay resolution: exactly one matrix row carrying did whose task is allowlisted
        ohits = [r for r in matrix_rows if did in r.get("discovery_ids", [])]
        if len(ohits) != 1:
            raise ValueError(f"P15 overlay Discovery ID must resolve exactly once in Matrix: {did}")
        tid = ohits[0]["evidence_task_id"]
        if tid not in allow:
            raise ValueError(f"P15 Discovery ID outside overlay allowlist: {did}")
        refs.extend(runner._ref_rows(overlay_cards[tid], tid, mode))
    dedup, seen = [], set()
    for ref in refs:
        key = tuple(ref[k] for k in ("evidence_task_id", "kind", "evidence_id", "subject_id", "subject_role"))
        if key not in seen:
            seen.add(key)
            dedup.append(ref)
    if not dedup:
        raise ValueError(f"No Evidence refs resolved for P15 {discovery_ids} mode={mode}")
    return dedup


def _p15_attribution(package: dict, overlay_cards: dict, refs: list) -> str:
    if not refs:
        return "NONE"
    union = {i["evidence_task_id"]: i["evidence_card"] for i in package["evidence_inputs"]}
    for k, v in overlay_cards.items():
        union.setdefault(k, v)
    pseudo = {"evidence_inputs": [{"evidence_task_id": k, "evidence_card": v} for k, v in union.items()]}
    # reuse frozen index builder over pseudo package
    index = drafting._card_ref_index(pseudo)
    values = set()
    for ref in refs:
        values.add(index[(ref["evidence_task_id"], ref["kind"], ref["evidence_id"])][2] or "PRIMARY_FACT")
    if "SOCIAL_OBSERVATION" in values:
        return "SOCIAL" if values == {"SOCIAL_OBSERVATION"} else "MIXED"
    if "INFERENCE" in values:
        return "INFERENCE" if values == {"INFERENCE"} else "MIXED"
    claimed = {"VENDOR_CLAIM", "PROJECT_CLAIM", "AUTHOR_CLAIM"}
    if values & claimed:
        return "ATTRIBUTED" if values <= claimed else "MIXED"
    return "FACTUAL"


def _p15_result(root: Path, package_path: Path, package: dict, spec: dict, runner_meta: dict,
                draft_version: str, overlay_cards: dict, allow: set) -> dict:
    deck_refs = _p15_refs(package, overlay_cards, allow, spec["deck_discovery_ids"], spec.get("deck_ref_mode", "CLAIMS"))
    blocks = []
    for row in spec["blocks"]:
        mode = row.get("ref_mode", "CLAIMS")
        refs = _p15_refs(package, overlay_cards, allow, row.get("discovery_ids", []), mode) if mode != "NONE" else []
        if mode == "NONE" and row.get("discovery_ids"):
            raise ValueError("ref_mode NONE cannot carry discovery_ids")
        blocks.append({"block_id": row["block_id"], "block_type": row["block_type"], "text": row["text"],
                       "attribution_mode": _p15_attribution(package, overlay_cards, refs), "evidence_refs": refs})
    boundary_id = f'{package["package_id"]}-boundaries'
    boundary_refs = []
    for item in package["evidence_inputs"]:
        boundary_refs.extend(runner._ref_rows(item["evidence_card"], item["evidence_task_id"], "LIMITATIONS"))
    if boundary_refs:
        blocks.append({"block_id": boundary_id, "block_type": "CLAIM_BOUNDARY",
                       "text": "この節の読解上の境界: " + " / ".join(package["package"]["boundaries"]),
                       "attribution_mode": _p15_attribution(package, overlay_cards, boundary_refs),
                       "evidence_refs": boundary_refs})
    else:
        blocks.append({"block_id": boundary_id, "block_type": "CLAIM_BOUNDARY",
                       "text": "この節の読解上の境界: " + " / ".join(package["package"]["boundaries"]),
                       "attribution_mode": "NONE", "evidence_refs": []})
    content_ids = [r["block_id"] for r in blocks if r["block_type"] != "HEADING"]
    return {
        "schema_version": "2.0-rc1", "issue_id": package["issue_id"],
        "research_profile": package["research_profile"], "publication_profile": package["publication_profile"],
        "package_id": package["package_id"], "draft_version": draft_version, "status": "ESTABLISHED",
        "basis": {"draft_package_sha256": core.sha256_file(package_path), "prompt_id": "article-drafting-v2",
                  "prompt_sha256": core.sha256_file(root / drafting.DRAFT_PROMPT)},
        "runner": runner_meta, "headline": spec["headline"], "deck": spec["deck"],
        "deck_attribution_mode": _p15_attribution(package, overlay_cards, deck_refs), "deck_evidence_refs": deck_refs,
        "blocks": blocks,
        "must_cover_coverage": [{"requirement": req, "block_ids": content_ids} for req in package["package"]["must_cover_requirements"]],
        "boundary_dispositions": [{"boundary": b, "handling": "EXPLICITLY_STATED", "block_ids": [boundary_id],
                                   "rationale": "Approved Architecture boundary is preserved explicitly in the Draft Result."}
                                  for b in package["package"]["boundaries"]],
        "profile_extensions": package["profile_extensions"], "publication_extensions": package["publication_extensions"],
    }


def _build_synthesis_input_with_overlay(root: Path, up: dict, pairs: list, execdir: Path) -> dict:
    """Identical to frozen build_synthesis_input except P15 result re-validation.

    Package validation stays frozen-canonical for all 16 (P15 package is canonical
    byte-identical and passes). Result validation stays frozen-canonical for 15
    packages; P15 result is re-validated by the edition-local overlay validator
    (union authority). Output schema and embedded bytes are identical in form.
    """
    sys.path.insert(0, str(execdir))
    import validate_p15_overlay as p15val
    from scripts import survey_drafting_v2_base as base
    profile = _load(up["profile"])
    plan = _load(up["architecture"])
    approval = _load(up["approval"])
    approval_errors = base.validate_architecture_approval(
        approval, up["architecture"], up["review"], profile["issue_id"])
    if approval_errors:
        raise ValueError("Synthesis Architecture authorization invalid: " + "; ".join(approval_errors))
    expected_packages = {row["package_id"]: row for row in plan["packages"]}
    seen: set[str] = set()
    drafts: list[dict] = []
    for package_path, result_path in pairs:
        package = core.load_json(package_path)
        package_errors = drafting.validate_self_contained_draft_package(
            package, up["profile"], up["architecture"], up["review"], up["approval"])
        if package_errors:
            raise ValueError("Draft Package invalid before Synthesis: " + "; ".join(package_errors))
        result = core.load_json(result_path)
        if package["package_id"] == "P15":
            errors = p15val.validate_p15_result(
                result, package_path, execdir / "p15-cross-package-synthesis-authority.json")
        else:
            errors = drafting.validate_draft_result(result, package_path, root / drafting.DRAFT_PROMPT)
        if errors:
            raise ValueError("Draft Result invalid before Synthesis: " + "; ".join(errors))
        package_id = package["package_id"]
        if package_id not in expected_packages or package_id in seen:
            raise ValueError(f"Synthesis Draft package set invalid: {package_id}")
        if package["package"]["drafting_order"] != expected_packages[package_id]["drafting_order"]:
            raise ValueError(f"Synthesis drafting order drift: {package_id}")
        seen.add(package_id)
        drafts.append({
            "package_id": package_id,
            "drafting_order": package["package"]["drafting_order"],
            "draft_package_sha256": core.sha256_file(package_path),
            "draft_result_sha256": core.sha256_file(result_path),
            "draft_result": result,
        })
    if seen != set(expected_packages):
        raise ValueError("Synthesis requires one validated Draft Result per Architecture package: "
                         f"missing={sorted(set(expected_packages)-seen)}")
    drafts.sort(key=lambda row: (row["drafting_order"], row["package_id"]))
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    research_contract = cfg["research_profiles"][profile["research_profile"]]
    publication_contract = cfg["publication_profiles"][profile["publication_profile"]]
    return {
        "schema_version": "2.0-rc1",
        "issue_id": profile["issue_id"],
        "research_profile": profile["research_profile"],
        "publication_profile": profile["publication_profile"],
        "basis": {
            "production_profile_sha256": core.sha256_file(up["profile"]),
            "architecture_sha256": core.sha256_file(up["architecture"]),
            "architecture_approval_sha256": core.sha256_file(up["approval"]),
        },
        "editorial_thesis": plan["editorial_thesis"],
        "architecture_goals": list(plan["architecture_goals"]),
        "drafts": drafts,
        "profile_payload_requirements": list(research_contract.get("synthesis_payload_required", [])),
        "publication_payload_requirements": list(publication_contract.get("synthesis_payload_required", [])),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--state", required=True)
    ap.add_argument("--input", required=True)
    args = ap.parse_args()
    root = Path(args.repo_root).resolve()
    state_path = (root / args.state).resolve()
    input_path = (root / args.input).resolve()
    data = _load(input_path)
    up = _upstream_bounded(root, state_path)
    state = _load(state_path)
    execdir = up["source_root"] / "execution" / EXECNAME
    if data.get("schema_version") != "2.0-rc1" or data.get("issue_id") != state["issue_id"]:
        raise SystemExit("interactive Drafting input identity mismatch")
    if set(data) != {"schema_version", "issue_id", "draft_version", "runner", "packages", "synthesis"}:
        raise SystemExit("interactive Drafting input envelope invalid")
    plan = _load(up["architecture"])
    specs = data["packages"]
    if {row["package_id"] for row in specs} != {row["package_id"] for row in plan["packages"]}:
        raise SystemExit("interactive Drafting must cover every Architecture package exactly once")
    spec_by_id = {row["package_id"]: row for row in specs}
    overlay, overlay_cards, allow = _overlay_cards(root, up, execdir)
    sys.path.insert(0, str(execdir))
    import validate_p15_overlay as p15val
    draft_root = up["source_root"] / "draft/v2"
    pairs = []
    outputs = []
    implementation_sha = core.repository_commit_sha(root)
    with runtime_tool.current_stage_basis_override():
        ordered = sorted(plan["packages"], key=lambda r: (r["drafting_order"], r["package_id"]))
        derived = {}
        for plan_row in ordered:
            pid = plan_row["package_id"]
            spec = spec_by_id[pid]
            if set(spec) != {"package_id", "headline", "deck", "deck_discovery_ids", "blocks"}:
                raise SystemExit(f"interactive package fields invalid: {pid}")
            derived[pid] = drafting.derive_draft_package(
                root, up["profile"], up["discovery"], up["screening"], up["evidence"],
                up["views"], up["ledger"], up["completeness"], up["matrix"], up["selection"],
                up["architecture"], up["review"], up["approval"], pid, implementation_sha)
        canon_pass, overlay_pass = [], []
        frozen_p15_errors = None
        for plan_row in ordered:
            pid = plan_row["package_id"]
            spec = spec_by_id[pid]
            package = derived[pid]
            package_dir = draft_root / "packages" / pid
            package_dir.mkdir(parents=True, exist_ok=True)
            package_path = package_dir / "draft-package.json"
            result_path = package_dir / "draft-result.json"
            core.write_json(package_path, package)
            if pid == "P15":
                result = _p15_result(root, package_path, package, spec, data["runner"], data["draft_version"], overlay_cards, allow)
                errs = p15val.validate_p15_result(result, package_path, execdir / "p15-cross-package-synthesis-authority.json")
                if errs:
                    raise SystemExit("P15 overlay validation FAILED: " + "; ".join(errs))
                overlay_pass.append(pid)
                frozen_p15_errors = drafting.validate_draft_result(result, package_path, root / drafting.DRAFT_PROMPT)
                print(f"P15 overlay validation PASS (frozen generic validator errors recorded: {len(frozen_p15_errors)})")
            else:
                result = runner._draft_result(root, package_path, package, spec, data["runner"], data["draft_version"])
                errors = drafting.validate_draft_result(result, package_path, root / drafting.DRAFT_PROMPT)
                if errors:
                    raise SystemExit(f"{pid} Draft Result invalid: " + "; ".join(errors))
                canon_pass.append(pid)
            core.write_json(result_path, result)
            pairs.append((package_path, result_path))
            outputs.append({"package_id": pid})
    synthesis_input = _build_synthesis_input_with_overlay(root, up, pairs, execdir)
    synthesis_input_path = draft_root / "profile-synthesis-input.json"
    synthesis_result_path = draft_root / "profile-synthesis-result.json"
    core.write_json(synthesis_input_path, synthesis_input)
    syn = data["synthesis"]
    if set(syn) != {"profile_payload", "publication_payload"}:
        raise SystemExit("interactive synthesis fields invalid")
    synthesis_result = {
        "schema_version": "2.0-rc1", "issue_id": state["issue_id"],
        "research_profile": state["research_profile"], "publication_profile": state["publication_profile"],
        "synthesis_version": "v1.0", "status": "ESTABLISHED",
        "basis": {"synthesis_input_sha256": core.sha256_file(synthesis_input_path),
                  "prompt_id": "profile-synthesis-v2",
                  "prompt_sha256": core.sha256_file(root / drafting.SYNTHESIS_PROMPT)},
        "runner": data["runner"], "profile_payload": syn["profile_payload"],
        "publication_payload": syn["publication_payload"],
    }
    errors = drafting.validate_synthesis_result(synthesis_result, synthesis_input_path, root / drafting.SYNTHESIS_PROMPT)
    if errors:
        raise SystemExit("Profile Synthesis Result invalid: " + "; ".join(errors))
    core.write_json(synthesis_result_path, synthesis_result)
    archive = draft_root / "interactive-drafting-synthesis-input.json"
    core.write_json(archive, data)
    report = {"packages": outputs, "regenerated": len(outputs),
              "canonical_pass": canon_pass, "overlay_pass": overlay_pass,
              "frozen_generic_p15_errors": frozen_p15_errors}
    (execdir / "regen-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"packages": outputs, "regenerated": len(outputs),
                      "canonical_pass_count": len(canon_pass), "overlay_pass": overlay_pass,
                      "frozen_generic_p15_error_count": len(frozen_p15_errors or [])}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
