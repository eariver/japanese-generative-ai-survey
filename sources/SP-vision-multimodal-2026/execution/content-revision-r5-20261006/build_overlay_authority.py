#!/usr/bin/env python3
"""Build multi-consumer cross-package synthesis overlay authority (deterministic, read-only upstream).

Consumers (all Architecture-authorized, edition-local compatibility):
  P15: 26 non-canonical IDs from architecture-v2.json
       publication_extensions.p15_cross_package_synthesis_map
       (the other 14 of the 40 distinct IDs resolve inside P15's own package inputs).
  P10: VM-D111 (VSI-Bench scaffold effect, PARTIAL) + VM-D112 (Agentic Video
       Understanding tool-assisted perception) — named by P10 must_cover_requirements.
  P11: VM-D115 (SAM 3 supporting stored-timeline evidence) — named by P11 must_cover.
  P06: VM-D065 (SigLIP2 encoder reuse, claim-3) — named by P06 must_cover_requirements.

For each Discovery ID: Matrix row (candidate/evidence_task/sha) -> Selection
SELECTED -> Evidence Acceptance (task/sha/filename) -> exact accepted Card bytes
(sha256 verified) -> subject IDs. Canonical home package resolved from Architecture
placements (non-consumer preferred). No Selection/destination change; reference role is
CROSS_PACKAGE_SYNTHESIS_REFERENCE (Draft-time synthesis only).
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
OUTDIR = SRC / "execution/content-revision-r5-20261006"


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


P15_CANONICAL = {
    "VM-D108", "VM-D109", "VM-D110", "VM-D078", "VM-D079", "VM-D081",
    "VM-D086", "VM-D087", "VM-D072", "VM-D073", "VM-D099", "VM-D100",
    "VM-D106", "VM-D107",
}

CONSUMERS = {
    "P15": {
        "allowlist_kind": "architecture_map_noncanonical",
        "allowlist_source": ("architecture-v2.json "
                             "publication_extensions.p15_cross_package_synthesis_map "
                             "(40 distinct IDs; 14 resolve inside P15 package inputs)"),
    },
    "P10": {
        "allowlist_kind": "must_cover_named",
        "allowlist_source": ("P10 must_cover_requirements: scaffold effect (VSI-Bench, PARTIAL depth), "
                             "tool-assisted perception (Agentic Video Understanding)"),
        "discovery_ids": ["VM-D111", "VM-D112"],
    },
    "P11": {
        "allowlist_kind": "must_cover_named",
        "allowlist_source": "P11 must_cover_requirements: SAM 3 memory video tracking as supporting stored-timeline evidence",
        "discovery_ids": ["VM-D115"],
    },
    "P06": {
        "allowlist_kind": "must_cover_named",
        "allowlist_source": "P06 must_cover_requirements: VM-O06 lineage complete; SigLIP2 encoder reuse bound via VM-D065 claim-3",
        "discovery_ids": ["VM-D065"],
    },
}


def main() -> int:
    arch_path = SRC / "architecture-v2.json"
    arch = json.loads(arch_path.read_text(encoding="utf-8"))
    amap = arch["publication_extensions"]["p15_cross_package_synthesis_map"]
    p15_all = sorted({d for ids in amap.values() for d in ids})
    assert len(p15_all) == 40, f"expected 40 distinct map IDs, got {len(p15_all)}"
    p15_overlay = sorted(set(p15_all) - P15_CANONICAL)
    assert len(p15_overlay) == 26, f"expected 26 non-canonical, got {len(p15_overlay)}"

    matrix_path = SRC / "candidate-matrix-v2.json"
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    sel = json.loads((SRC / "candidate-selection-v2.json").read_text(encoding="utf-8"))
    sel_disp = {a["candidate_id"]: a["disposition"] for a in sel["assignments"]}

    arch_usage: dict[str, list] = {}
    for pkg in arch["packages"]:
        pid = pkg["package_id"]
        for cid in pkg.get("primary_candidate_ids", []):
            arch_usage.setdefault(cid, []).append((pid, "PRIMARY"))
        for cid in pkg.get("supporting_candidate_ids", []):
            arch_usage.setdefault(cid, []).append((pid, "SUPPORTING"))

    mrow = {}
    for r in matrix["rows"]:
        for d in r.get("discovery_ids", []):
            mrow[d] = r

    norm = json.loads((SRC / "orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json").read_text(encoding="utf-8"))
    by_name = {row["name"]: row for row in norm["artifacts"]}
    ev_acc_path = (ROOT / by_name["evidence-acceptance"]["path"]).resolve()
    ev_acc = json.loads(ev_acc_path.read_text(encoding="utf-8"))
    ev_by_task = {r["evidence_task_id"]: r for r in ev_acc["results"]}

    arch_sha = sha256_file(arch_path)
    appr_path = SRC / "gates/architecture-approval.json"
    appr_sha = sha256_file(appr_path)
    matrix_sha = sha256_file(matrix_path)
    ev_acc_sha = sha256_file(ev_acc_path)

    wanted: dict[str, set[str]] = {"P15": set(p15_overlay)}
    for pid, cfg in CONSUMERS.items():
        if pid == "P15":
            continue
        wanted[pid] = set(cfg["discovery_ids"])

    # axis label per discovery id (P15 map axes; named roles otherwise)
    axis_of: dict[str, list[str]] = {}
    for axis in sorted(amap.keys()):
        for did in amap[axis]:
            axis_of.setdefault(did, []).append(axis)

    entries = []
    for pid in sorted(wanted):
        for did in sorted(wanted[pid]):
            row = mrow.get(did)
            assert row is not None, f"Discovery {did} missing in matrix"
            cid = row["candidate_id"]
            tid = row["evidence_task_id"]
            esha = row["evidence_sha256"]
            disp = sel_disp.get(cid)
            assert disp == "SELECTED", f"{did} {cid} disposition {disp}"
            meta = ev_by_task.get(tid)
            assert meta is not None and meta["sha256"] == esha, f"acceptance mismatch {did}"
            card_path = ev_acc_path.parent / "results" / meta["filename"]
            raw = card_path.read_bytes()
            assert hashlib.sha256(raw).hexdigest() == esha, f"card bytes drift {did}"
            card = json.loads(raw.decode("utf-8"))
            subjects = set()
            for ev in card.get("temporal", {}).get("events", []):
                subjects.add(ev["subject_id"])
            for coll in ("claims", "metrics", "limitations"):
                for item in card.get(coll, []):
                    subjects.add(item["subject_id"])
            uses = arch_usage.get(cid, [])
            non_consumer = [u for u in uses if u[0] != pid]
            home = non_consumer[0] if non_consumer else (uses[0] if uses else (None, None))
            entries.append({
                "consumer_package": pid,
                "synthesis_axis": axis_of.get(did, ["must_cover_named_cross_package"]),
                "discovery_id": did,
                "candidate_id": cid,
                "canonical_home_package": home[0],
                "home_architecture_usage": home[1],
                "all_architecture_usages": [{"package_id": p, "usage": u} for p, u in uses],
                "evidence_task_id": tid,
                "evidence_sha256": esha,
                "evidence_filename": meta["filename"],
                "evidence_subject_ids": sorted(subjects),
                "selection_disposition": disp,
                "reference_role": "CROSS_PACKAGE_SYNTHESIS_REFERENCE",
                "architecture_sha256": arch_sha,
                "architecture_approval_sha256": appr_sha,
                "candidate_matrix_sha256": matrix_sha,
                "evidence_acceptance_sha256": ev_acc_sha,
            })
    out = {
        "schema_version": "1.0",
        "issue_id": "SP-vision-multimodal-2026",
        "authority_kind": "edition-local multi-consumer cross-package synthesis compatibility overlay",
        "consumers": {pid: {"allowlist_kind": cfg["allowlist_kind"],
                            "allowlist_source": cfg["allowlist_source"],
                            "discovery_ids": sorted(wanted[pid])}
                      for pid, cfg in CONSUMERS.items()
                      if pid == "P15" or True},
        "architecture_sha256": arch_sha,
        "architecture_approval_sha256": appr_sha,
        "candidate_matrix_sha256": matrix_sha,
        "evidence_acceptance_sha256": ev_acc_sha,
        "entry_count": len(entries),
        "unique_discovery_count": len({e["discovery_id"] for e in entries}),
        "entries": entries,
    }
    out["consumers"]["P15"]["discovery_ids"] = sorted(wanted["P15"])
    OUTDIR.mkdir(parents=True, exist_ok=True)
    (OUTDIR / "cross-package-synthesis-authority.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"entries": len(entries),
                      "unique": len({e['discovery_id'] for e in entries}),
                      "per_consumer": {pid: len(wanted[pid]) for pid in sorted(wanted)}}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
