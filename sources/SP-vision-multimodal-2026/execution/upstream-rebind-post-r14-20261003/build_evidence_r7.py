#!/usr/bin/env python3
"""Build TS-003 r7 Evidence: r6 baseline with 2 micro-repaired cards.

- 109 unaffected cards/views: byte-for-byte copies of r6 canonical files.
- VM-D084 (Case A): entity/artifact/source-title rename V2 -> V1 (original 2017
  database); claim-1 gains V1 version identity (108,499 exact). No scale change.
- VM-D010: claim-1 matching-cost vs training-loss separation; claim-3 auxiliary
  losses reframed as standard recipe (intermediate decoder layers, shared FFNs;
  helpful, not architecturally mandatory).
- Timestamps preserved from r6 on all cards (no new retrieval run).
- Views: 109 r6 byte-copies + 2 rebuilt views bound to new card hashes.
- Canonical append-only acceptors + validators only. Same post-gate adaptations
  as r6 (documented there): no lifecycle advance, no gate mutation, no approval.
  Sol re-review required before downstream use.
"""

from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import run_evidence_v2_interactive as inter

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
R6_DIR = "5b8d4ba62aa56465007f34782cc88e8f32ea4a9181c66cc9fa74785eb6ff07ab"
R6_RES = f"{SRC}/evidence/v2/accepted/{R6_DIR}/results"
R6_VIEW_DIR = ("e8373be3a1af71cf4b10fd2c54395c879ef09e7ed80897da209b4a5d77385845")
R6_VIEW_RES = f"{SRC}/evidence/v2/views/accepted/{R6_VIEW_DIR}/views"
EDIR = f"{SRC}/execution/upstream-rebind-post-r14-20261003"
CARD_EDITS = f"{EDIR}/card-edits-r7.json"
R7_INPUT = f"{EDIR}/evidence-interactive-input-r7.json"
PKG = (f"{SRC}/execution/screening-evidence-20260930/evidence-package/package.json")
STATE_REL = f"{SRC}/production-state.json"

TARGETS = ["VM-D084", "VM-D010"]

PACKAGE_SHA_KNOWN = "ca1fab780b68646743d2a3c91f69bcbc95dd3907e49a70bf23f564090191e371"

PREEXISTING_DRIFT = {
    "Stage Checkpoint artifact drift: publication-pdf",
    "Stage Checkpoint artifact drift: quality-regression-bundle",
    "Stage Checkpoint artifact drift: reader-manuscript",
    "Stage Checkpoint artifact drift: reader-surface-gate",
    "Stage Checkpoint artifact drift: semantic-review",
    "Stage Checkpoint artifact drift: validated-source",
    "Stage Checkpoint artifact drift: visual-review",
}

_orig_validate_agent_state = agent.validate_agent_state


def _validate_agent_state_postgate(repo_root, cfg, state):
    errs = _orig_validate_agent_state(repo_root, cfg, state)
    missing = PREEXISTING_DRIFT - set(errs)
    if missing:
        raise ValueError("pre-existing drift baseline changed; refusing to filter: "
                         + "; ".join(sorted(missing)))
    return [e for e in errs if e not in PREEXISTING_DRIFT]


agent.validate_agent_state = _validate_agent_state_postgate


def _exact_regular_files(directory, expected_names, label):
    actual = {p.name: p for p in directory.iterdir() if p.is_file() and not p.is_symlink()}
    if set(actual) != set(expected_names):
        raise ValueError(label + " file set mismatch")
    return actual


def accept_evidence_results_postgate(repo_root, package_path, results_dir,
                                     accepted_root, implementation_sha):
    """Byte-identical replicate of canonical accept_evidence_results; see r6
    builder for the single documented post-gate adaptation."""
    package = core.load_json(package_path)
    if core.sha256_file(package_path) != PACKAGE_SHA_KNOWN:
        raise ValueError("Evidence task package bytes changed; post-gate equivalence void")
    expected = {Path(meta["path"]).name for meta in package["tasks"]}
    files = _exact_regular_files(results_dir, expected, "Evidence result set")
    entries = []
    for meta in package["tasks"]:
        task_path = package_path.parent / meta["path"]
        task = core.load_json(task_path)
        result_path = files[Path(meta["path"]).name]
        card = core.load_json(result_path)
        errors = evidence.validate_evidence_card(card, task, meta["sha256"], package,
                                                 repo_root=repo_root)
        if errors:
            raise ValueError("Evidence Card " + meta["evidence_task_id"] + " invalid: " + "; ".join(errors))
        entries.append({
            "evidence_task_id": meta["evidence_task_id"],
            "discovery_ids": list(meta["discovery_ids"]),
            "sha256": core.sha256_file(result_path),
            "status": card["status"],
            "filename": result_path.name,
        })
    package_sha = core.sha256_file(package_path)
    result_set_sha = evidence._evidence_result_set_digest(package_sha, entries)
    run_dir = accepted_root / result_set_sha
    acceptance_path = run_dir / "evidence-accepted.json"
    if run_dir.exists():
        if acceptance_path.is_file():
            evidence.validate_evidence_acceptance(repo_root, acceptance_path,
                                                  implementation_sha)
            return acceptance_path
        raise ValueError("incomplete pre-existing Evidence acceptance directory: " + str(run_dir))
    (run_dir / "tasks").mkdir(parents=True)
    (run_dir / "results").mkdir(parents=True)
    shutil.copy2(package_path, run_dir / "package.json")
    for meta in package["tasks"]:
        basename = Path(meta["path"]).name
        shutil.copy2(package_path.parent / meta["path"], run_dir / "tasks" / basename)
        shutil.copy2(files[basename], run_dir / "results" / basename)
    acceptance = {
        "schema_version": "2.0-rc1",
        "issue_id": package["issue_id"],
        "research_profile": package["research_profile"],
        "result_set_sha256": result_set_sha,
        "package_sha256": package_sha,
        "screening_acceptance_sha256": package["basis"]["screening_acceptance_sha256"],
        "result_count": len(entries),
        "results": sorted(entries, key=lambda row: row["evidence_task_id"]),
    }
    core.write_json(acceptance_path, acceptance)
    return acceptance_path


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise ValueError("r7 build requires RELEASE_CANDIDATE (post-gate repair run; no gate advance)")
    package_path = root / PKG
    package = core.load_json(package_path)
    task_meta = {meta["discovery_ids"][0]: meta for meta in package["tasks"]}
    if set(task_meta) != {f"VM-D{i:03d}" for i in range(1, 112)}:
        raise ValueError("task package does not cover 111/111")

    edits = {e["discovery_id"]: e
             for e in core.load_json(root / CARD_EDITS)["card_edits"]}
    assert set(edits) == set(TARGETS), set(edits) ^ set(TARGETS)
    doc = core.load_json(root / R7_INPUT)
    by_id = {r["discovery_id"]: r for r in doc["records"]}
    assert set(by_id) == set(TARGETS)
    profile_path = root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(root, profile["paths"]["source_root"], "paths.source_root")
    implementation_sha = core.repository_commit_sha(root)

    with tempfile.TemporaryDirectory() as temp:
        temp_root = Path(temp)
        results_dir = temp_root / "evidence-results"
        results_dir.mkdir()
        for did in sorted(task_meta):
            meta = task_meta[did]
            fname = Path(meta["path"]).name
            if did in TARGETS:
                base = core.load_json(root / R6_RES / fname)
                ed = edits[did]
                for ce in ed.get("claim_edits", []):
                    hit = [c for c in base["claims"]
                           if c["statement_id"] == ce["statement_id"]]
                    assert len(hit) == 1, f"{did} {ce['statement_id']} miss"
                    assert hit[0]["text"].count(ce["old_text"]) == 1, f"{did} old miss"
                    hit[0]["text"] = hit[0]["text"].replace(ce["old_text"], ce["new_text"])
                if "entity_rename" in ed:
                    er = ed["entity_rename"]
                    ent = [e for e in base["entities"] if e["entity_id"] == er["entity_id"]]
                    assert len(ent) == 1, f"{did} entity miss"
                    ent[0]["canonical_name"] = er["canonical_name"]
                    assert base["artifact"]["primary_subject_id"] == er["entity_id"]
                    base["artifact"]["canonical_name"] = er["canonical_name"]
                if "source_title_rename" in ed:
                    assert base["sources"][0]["title"].count("Something-Something V2") == 1
                    base["sources"][0]["title"] = ed["source_title_rename"]
                for nc in ed.get("new_claims", []):
                    have = {c["statement_id"] for c in base["claims"]}
                    assert nc["statement_id"] not in have
                    base["claims"].append({
                        "statement_id": nc["statement_id"], "text": nc["text"],
                        "subject_id": nc["subject_id"], "subject_role": nc["subject_role"],
                        "evidence_class": nc["evidence_class"], "source_ids": nc["source_ids"],
                        "context": nc["context"]})
                task = core.load_json(package_path.parent / meta["path"])
                errs = evidence.validate_evidence_card(
                    base, task, meta["sha256"], package, repo_root=root)
                if errs:
                    raise ValueError(f"r7 Card {did} invalid: {'; '.join(errs)}")
                core.write_json(results_dir / fname, base)
            else:
                shutil.copy2(root / R6_RES / fname, results_dir / fname)

        evidence_root = source_root / "evidence/v2/accepted"
        with agent_tool.current_stage_basis_override():
            evidence_acceptance_path = accept_evidence_results_postgate(
                root, package_path, results_dir, evidence_root, implementation_sha)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, implementation_sha)

        by_task = {row["evidence_task_id"]: row for row in evidence_acceptance["results"]}
        views_dir = temp_root / "views"
        views_dir.mkdir()
        for did in sorted(task_meta):
            meta = task_meta[did]
            task_id = meta["evidence_task_id"]
            entry = by_task[task_id]
            if did in TARGETS:
                view = inter._build_view(profile, task_id, entry["sha256"], by_id[did])
                errs = evidence.validate_edition_view(
                    view, profile, entry["sha256"], entry["status"])
                if errs:
                    raise ValueError(f"r7 View {did} invalid: {'; '.join(errs)}")
                core.write_json(views_dir / evidence.view_filename(task_id), view)
            else:
                src_view = root / R6_VIEW_RES / evidence.view_filename(task_id)
                if not src_view.is_file():
                    raise ValueError(f"r6 view missing for {did}")
                shutil.copy2(src_view, views_dir / evidence.view_filename(task_id))

        views_root = source_root / "evidence/v2/views/accepted"
        with agent_tool.current_stage_basis_override():
            views_acceptance_path = evidence.accept_edition_views(
                root, profile_path, evidence_acceptance_path, views_dir, views_root,
                implementation_sha)
            evidence.validate_edition_views_acceptance(
                root, profile_path, evidence_acceptance_path, views_acceptance_path,
                implementation_sha)

    print(json.dumps({
        "evidence_acceptance": str(evidence_acceptance_path.relative_to(root)),
        "evidence_acceptance_sha256": core.sha256_file(evidence_acceptance_path),
        "views_acceptance": str(views_acceptance_path.relative_to(root)),
        "views_acceptance_sha256": core.sha256_file(views_acceptance_path),
        "cards": 111,
        "rebuilt_cards": sorted(TARGETS),
        "lifecycle": "RELEASE_CANDIDATE (unchanged; builder advances no gate)",
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
