#!/usr/bin/env python3
"""Regenerate revised 16 draft-results + synthesis for TS-003 r7-rev1 (same r7 authority).

- derive_draft_package for all 16 (must be byte-identical to canonical files).
- frozen runner._draft_result for the 12 non-overlay packages.
- custom union-ref builder for overlay consumers P06/P10/P11/P15
  (canonical-first resolution, overlay fallback, optional per-discovery only_claims).
- post-hoc boundaries_text override (all 16) + must_cover_map override
  (P10/P11/P12/P15). Text-only changes are validation-neutral.
- canonical validate_draft_result for 12; overlay validator for 4.
- overlay-aware synthesis input rebuild + synthesis result (payloads preserved,
  basis/runner refreshed), validated.
No TeX/PDF/candidate/advance. No shared-Core change.
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as runtime_tool
from scripts import survey_drafting_v2 as drafting
from scripts import survey_production_v2 as core
import scripts.run_drafting_synthesis_v2_interactive as runner

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECNAME = "r8-draft-closure-rev3-20261007"
EXECDIR = SRC / "execution" / EXECNAME
OVERLAY_CONSUMERS = {"P04", "P05", "P06", "P07A", "P07B", "P10", "P11", "P15"}


def _load(path: Path):
    return core.load_json(path)


def _upstream(root: Path, state_path: Path) -> dict:
    state = _load(state_path)
    if state.get("human_gates", {}).get("architecture_review") != "approved":
        raise ValueError("revision requires approved Architecture Review")
    cfg = _load(root / core.DEFAULT_CONFIG)
    errs = agent.validate_agent_state(root, cfg, state)
    if errs:
        print("pre-regeneration state notes (informational):", file=sys.stderr)
        for e in errs:
            print(" -", e, file=sys.stderr)
    profile_path = root / state["profile"]["path"]
    profile = _load(profile_path)
    source_root = root / profile["paths"]["source_root"]
    accepted = _load(source_root / "discovery/discovery-accepted-v2.json")
    discovery_path = (root / accepted.get("discovery_path")).resolve()
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
    screening_path = (root / attention.get("basis", {}).get("screening_acceptance_path")).resolve()
    return {
        "state": state, "profile": profile_path, "source_root": source_root,
        "discovery": discovery_path, "screening": screening_path,
        "evidence": evidence_path, "views": views_path,
        "ledger": source_root / "materiality-ledger-v2.json",
        "completeness": source_root / "profile-completeness-v2.json",
        "matrix": matrix_path, "selection": source_root / "candidate-selection-v2.json",
        "architecture": source_root / "architecture-v2.json",
        "review": source_root / "architecture-review-summary-v2.json",
        "approval": approval_path,
    }


def _overlay_cards(up: dict):
    overlay = json.loads((SRC / "execution/r8-draft-closure-rev1-20261007/cross-package-map-r8-rev1.json").read_text(encoding="utf-8"))
    ev_acc = _load(up["evidence"])
    ev_by_task = {r["evidence_task_id"]: r for r in ev_acc["results"]}
    cards: dict[str, dict] = {}
    allow: dict[str, set] = {}
    for e in overlay["entries"]:
        pid, tid = e["consumer_package"], e["evidence_task_id"]
        allow.setdefault(pid, set()).add(tid)
        if tid in cards:
            continue
        meta = ev_by_task[tid]
        assert meta["sha256"] == e["evidence_sha256"], tid
        p = up["evidence"].parent / "results" / meta["filename"]
        raw = p.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == e["evidence_sha256"], tid
        cards[tid] = json.loads(raw.decode("utf-8"))
    disc_allow: dict[str, set] = {}
    for e in overlay["entries"]:
        disc_allow.setdefault(e["consumer_package"], set()).add(e["discovery_id"])
    return overlay, cards, allow, disc_allow


def _xrefs(package: dict, overlay_cards: dict, allow: set, disc_allow: set,
           discovery_ids: list, mode: str, only_claims: dict | None):
    by_cand = {row["candidate_id"]: row for row in package["evidence_inputs"]}
    authorized = set(by_cand)
    matrix_rows = package["candidate_matrix"]["rows"]
    refs = []
    for did in discovery_ids:
        hits = [r for r in matrix_rows if r["candidate_id"] in authorized and did in r.get("discovery_ids", [])]
        if len(hits) == 1:
            item = by_cand[hits[0]["candidate_id"]]
            rows = runner._ref_rows(item["evidence_card"], item["evidence_task_id"], mode)
        else:
            ohits = [r for r in matrix_rows if did in r.get("discovery_ids", [])]
            if len(ohits) != 1:
                raise ValueError(f"overlay Discovery ID must resolve exactly once in Matrix: {did}")
            tid = ohits[0]["evidence_task_id"]
            if tid not in allow or did not in disc_allow:
                raise ValueError(f"Discovery ID outside overlay allowlist: {did}")
            rows = runner._ref_rows(overlay_cards[tid], tid, mode)
        if only_claims and did in only_claims:
            keep = set(only_claims[did])
            rows = [r for r in rows if r["evidence_id"] in keep or r["kind"] != "CLAIM"]
            # NOTE: LIMITATION rows survive; claim restriction is the provenance point
        refs.extend(rows)
    dedup, seen = [], set()
    for ref in refs:
        key = tuple(ref[k] for k in ("evidence_task_id", "kind", "evidence_id", "subject_id", "subject_role"))
        if key not in seen:
            seen.add(key)
            dedup.append(ref)
    if not dedup:
        raise ValueError(f"No Evidence refs resolved for {discovery_ids} mode={mode}")
    return dedup


def _xattribution(package: dict, overlay_cards: dict, refs: list) -> str:
    if not refs:
        return "NONE"
    union = {i["evidence_task_id"]: i["evidence_card"] for i in package["evidence_inputs"]}
    for k, v in overlay_cards.items():
        union.setdefault(k, v)
    pseudo = {"evidence_inputs": [{"evidence_task_id": k, "evidence_card": v} for k, v in union.items()]}
    return runner._attribution(pseudo, refs)


def _xresult(root: Path, package_path: Path, package: dict, spec: dict,
             runner_meta: dict, draft_version: str, overlay_cards: dict,
             allow: set, disc_allow: set) -> dict:
    deck_refs = _xrefs(package, overlay_cards, allow, disc_allow,
                       spec["deck_discovery_ids"], spec.get("deck_ref_mode", "CLAIMS"),
                       spec.get("only_claims"))
    blocks = []
    for row in spec["blocks"]:
        mode = row.get("ref_mode", "CLAIMS")
        refs = _xrefs(package, overlay_cards, allow, disc_allow,
                      row.get("discovery_ids", []), mode,
                      row.get("only_claims")) if mode != "NONE" else []
        if mode == "NONE" and row.get("discovery_ids"):
            raise ValueError("ref_mode NONE cannot carry discovery_ids")
        blocks.append({"block_id": row["block_id"], "block_type": row["block_type"],
                       "text": row["text"],
                       "attribution_mode": _xattribution(package, overlay_cards, refs),
                       "evidence_refs": refs})
    boundary_id = f'{package["package_id"]}-boundaries'
    boundary_refs = []
    for item in package["evidence_inputs"]:
        boundary_refs.extend(runner._ref_rows(item["evidence_card"], item["evidence_task_id"], "LIMITATIONS"))
    blocks.append({"block_id": boundary_id, "block_type": "CLAIM_BOUNDARY",
                   "text": "BOUNDARIES_PLACEHOLDER",
                   "attribution_mode": _xattribution(package, overlay_cards, boundary_refs) if boundary_refs else "NONE",
                   "evidence_refs": boundary_refs})
    content_ids = [r["block_id"] for r in blocks if r["block_type"] != "HEADING"]
    return {
        "schema_version": "2.0-rc1", "issue_id": package["issue_id"],
        "research_profile": package["research_profile"], "publication_profile": package["publication_profile"],
        "package_id": package["package_id"], "draft_version": draft_version, "status": "ESTABLISHED",
        "basis": {"draft_package_sha256": core.sha256_file(package_path), "prompt_id": "article-drafting-v2",
                  "prompt_sha256": core.sha256_file(root / drafting.DRAFT_PROMPT)},
        "runner": runner_meta, "headline": spec["headline"], "deck": spec["deck"],
        "deck_attribution_mode": _xattribution(package, overlay_cards, deck_refs), "deck_evidence_refs": deck_refs,
        "blocks": blocks,
        "must_cover_coverage": [{"requirement": req, "block_ids": content_ids} for req in package["package"]["must_cover_requirements"]],
        "boundary_dispositions": [{"boundary": b, "handling": "EXPLICITLY_STATED", "block_ids": [boundary_id],
                                   "rationale": "Approved Architecture boundary is preserved explicitly in the Draft Result."}
                                  for b in package["package"]["boundaries"]],
        "profile_extensions": package["profile_extensions"], "publication_extensions": package["publication_extensions"],
    }


def _build_synthesis_input_with_overlay(root: Path, up: dict, pairs: list) -> dict:
    sys.path.insert(0, str(EXECDIR))
    import validate_overlay as oval
    from scripts import survey_drafting_v2_base as base
    profile = _load(up["profile"])
    plan = _load(up["architecture"])
    approval = _load(up["approval"])
    errs = base.validate_architecture_approval(approval, up["architecture"], up["review"], profile["issue_id"])
    if errs:
        raise ValueError("Synthesis Architecture authorization invalid: " + "; ".join(errs))
    overlay_cards_all = _overlay_cards(up)[1]
    expected_packages = {row["package_id"]: row for row in plan["packages"]}
    seen: set[str] = set()
    drafts: list[dict] = []
    for package_path, result_path in pairs:
        package = core.load_json(package_path)
        perrs = drafting.validate_self_contained_draft_package(
            package, up["profile"], up["architecture"], up["review"], up["approval"])
        if perrs:
            raise ValueError("Draft Package invalid before Synthesis: " + "; ".join(perrs))
        result = core.load_json(result_path)
        pid = package["package_id"]
        if pid in OVERLAY_CONSUMERS:
            errs = oval.validate_overlay_result(
                result, package_path, SRC / "execution/r8-draft-closure-rev1-20261007/cross-package-map-r8-rev1.json",
                pid, overlay_cards_all)
        else:
            errs = drafting.validate_draft_result(result, package_path, root / drafting.DRAFT_PROMPT)
        if errs:
            raise ValueError(f"Draft Result invalid before Synthesis ({pid}): " + "; ".join(errs))
        if pid not in expected_packages or pid in seen:
            raise ValueError(f"Synthesis Draft package set invalid: {pid}")
        if package["package"]["drafting_order"] != expected_packages[pid]["drafting_order"]:
            raise ValueError(f"Synthesis drafting order drift: {pid}")
        seen.add(pid)
        drafts.append({
            "package_id": pid,
            "drafting_order": package["package"]["drafting_order"],
            "draft_package_sha256": core.sha256_file(package_path),
            "draft_result_sha256": core.sha256_file(result_path),
            "draft_result": result,
        })
    if seen != set(expected_packages):
        raise ValueError("Synthesis requires one validated Draft Result per Architecture package")
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
    root = ROOT
    state_path = SRC / "production-state.json"
    up = _upstream(root, state_path)
    state = up["state"]
    spec_file = EXECDIR / "compact-input-fresh-121-r8-rev3.json"
    assert spec_file.exists(), "fresh r6 spec missing"
    spec = json.loads(spec_file.read_text(encoding="utf-8"))
    if spec.get("schema_version") != "2.0-rc1" or spec.get("issue_id") != state["issue_id"]:
        raise SystemExit("spec identity mismatch")
    plan = _load(up["architecture"])
    if {r["package_id"] for r in spec["packages"]} != {r["package_id"] for r in plan["packages"]}:
        raise SystemExit("spec must cover every Architecture package exactly once")
    spec_by_id = {r["package_id"]: r for r in spec["packages"]}
    overlay, overlay_cards, allow, disc_allow = _overlay_cards(up)
    sys.path.insert(0, str(EXECDIR))
    import validate_overlay as oval
    draft_root = up["source_root"] / "draft/v2"
    pairs = []
    outputs = []
    implementation_sha = core.repository_commit_sha(root)
    runner_meta = spec["runner"]
    draft_version = spec["draft_version"]
    with runtime_tool.current_stage_basis_override():
        ordered = sorted(plan["packages"], key=lambda r: (r["drafting_order"], r["package_id"]))
        derived = {}
        for plan_row in ordered:
            pid = plan_row["package_id"]
            s = spec_by_id[pid]
            allowed = {"package_id", "headline", "deck", "deck_discovery_ids", "deck_ref_mode",
                       "blocks", "must_cover_map", "boundaries_text"}
            if set(s) - allowed:
                raise SystemExit(f"spec fields invalid: {pid}: {sorted(set(s) - allowed)}")
            for b in s["blocks"]:
                bok = {"block_id", "block_type", "discovery_ids", "ref_mode", "text", "only_claims"}
                if set(b) - bok or "block_id" not in b or "text" not in b or "block_type" not in b:
                    raise SystemExit(f"spec block fields invalid: {pid}/{b.get('block_id')}")
            derived[pid] = drafting.derive_draft_package(
                root, up["profile"], up["discovery"], up["screening"], up["evidence"],
                up["views"], up["ledger"], up["completeness"], up["matrix"], up["selection"],
                up["architecture"], up["review"], up["approval"], pid, implementation_sha)
        canon_pass, overlay_pass = [], []
        frozen_p15_errors = None
        import shutil
        if (draft_root / "packages").exists():
            shutil.rmtree(draft_root / "packages")
        for stale in ("profile-synthesis-input.json", "profile-synthesis-result.json",
                      "interactive-drafting-synthesis-input.json"):
            if (draft_root / stale).exists():
                (draft_root / stale).unlink()
        for plan_row in ordered:
            pid = plan_row["package_id"]
            s = spec_by_id[pid]
            package = derived[pid]
            package_dir = draft_root / "packages" / pid
            package_dir.mkdir(parents=True, exist_ok=True)
            package_path = package_dir / "draft-package.json"
            result_path = package_dir / "draft-result.json"
            core.write_json(package_path, package)
            if pid in OVERLAY_CONSUMERS:
                result = _xresult(root, package_path, package, s, runner_meta,
                                  draft_version, overlay_cards, allow.get(pid, set()),
                                  disc_allow.get(pid, set()))
            else:
                result = runner._draft_result(root, package_path, package, s, runner_meta, draft_version)
            # post-hoc reader-facing overrides (validation-neutral: text + coverage mapping only)
            btext = s.get("boundaries_text")
            if btext:
                bid = f"{pid}-boundaries"
                hits = [b for b in result["blocks"] if b["block_id"] == bid]
                assert len(hits) == 1, pid
                assert btext and len(btext) > 20, pid
                hits[0]["text"] = btext
            mmap = s.get("must_cover_map")
            if mmap:
                reqs = package["package"]["must_cover_requirements"]
                if set(mmap) != set(reqs):
                    raise SystemExit(f"must_cover_map keys mismatch: {pid}")
                block_set = {b["block_id"] for b in result["blocks"]}
                for req, ids in mmap.items():
                    if not ids or len(set(ids)) != len(ids) or any(i not in block_set for i in ids):
                        raise SystemExit(f"must_cover_map block_ids invalid: {pid}/{req[:40]}")
                result["must_cover_coverage"] = [{"requirement": r, "block_ids": list(mmap[r])} for r in reqs]
            if pid in OVERLAY_CONSUMERS:
                errs = oval.validate_overlay_result(
                    result, package_path, SRC / "execution/r8-draft-closure-rev1-20261007/cross-package-map-r8-rev1.json",
                    pid, overlay_cards)
                if errs:
                    raise SystemExit(f"{pid} overlay validation FAILED: " + "; ".join(errs))
                overlay_pass.append(pid)
                if pid == "P15":
                    frozen_p15_errors = drafting.validate_draft_result(result, package_path, root / drafting.DRAFT_PROMPT)
            else:
                errs = drafting.validate_draft_result(result, package_path, root / drafting.DRAFT_PROMPT)
                if errs:
                    raise SystemExit(f"{pid} Draft Result invalid: " + "; ".join(errs))
                canon_pass.append(pid)
            core.write_json(result_path, result)
            pairs.append((package_path, result_path))
            outputs.append({"package_id": pid})
    synthesis_input = _build_synthesis_input_with_overlay(root, up, pairs)
    synthesis_input_path = draft_root / "profile-synthesis-input.json"
    synthesis_result_path = draft_root / "profile-synthesis-result.json"
    core.write_json(synthesis_input_path, synthesis_input)
    fresh_syn = spec.get("synthesis", {}).get("profile_payload", {})
    assert fresh_syn, "fresh synthesis profile_payload missing"
    synthesis_result = {
        "schema_version": "2.0-rc1", "issue_id": state["issue_id"],
        "research_profile": state["research_profile"], "publication_profile": state["publication_profile"],
        "synthesis_version": "v1.0", "status": "ESTABLISHED",
        "basis": {"synthesis_input_sha256": core.sha256_file(synthesis_input_path),
                  "prompt_id": "profile-synthesis-v2",
                  "prompt_sha256": core.sha256_file(root / drafting.SYNTHESIS_PROMPT)},
        "runner": dict(runner_meta, run_reference=None),
        "profile_payload": fresh_syn,
        "publication_payload": spec.get("synthesis", {}).get("publication_payload", {}),
    }
    errs = drafting.validate_synthesis_result(synthesis_result, synthesis_input_path, root / drafting.SYNTHESIS_PROMPT)
    if errs:
        raise SystemExit("Profile Synthesis Result invalid: " + "; ".join(errs))
    core.write_json(synthesis_result_path, synthesis_result)
    report = {"packages": outputs, "regenerated": len(outputs),
              "canonical_pass": canon_pass, "overlay_pass": overlay_pass,
              "frozen_generic_p15_errors": frozen_p15_errors}
    (EXECDIR / "regen-report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"regenerated": len(outputs), "canonical_pass_count": len(canon_pass),
                      "overlay_pass": overlay_pass,
                      "frozen_generic_p15_error_count": len(frozen_p15_errors or [])}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
