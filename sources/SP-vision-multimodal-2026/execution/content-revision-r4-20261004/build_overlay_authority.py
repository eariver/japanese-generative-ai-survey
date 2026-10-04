#!/usr/bin/env python3
"""Build P15 cross-package synthesis overlay authority (deterministic, read-only upstream)."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
OUTDIR = SRC / "execution/content-revision-r4-20261004"


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    arch_path = SRC / "architecture-v2.json"
    arch = json.loads(arch_path.read_text(encoding="utf-8"))
    amap = arch["publication_extensions"]["p15_cross_package_synthesis_map"]
    matrix_path = SRC / "candidate-matrix-v2.json"
    matrix = json.loads(matrix_path.read_text(encoding="utf-8"))
    sel = json.loads((SRC / "candidate-selection-v2.json").read_text(encoding="utf-8"))
    sel_disp = {a["candidate_id"]: a["disposition"] for a in sel["assignments"]}
    arch_usage = {}
    home_pkg = {}
    for pkg in arch["packages"]:
        pid = pkg["package_id"]
        for cid in pkg.get("primary_candidate_ids", []):
            arch_usage.setdefault(cid, []).append((pid, "PRIMARY"))
        for cid in pkg.get("supporting_candidate_ids", []):
            arch_usage.setdefault(cid, []).append((pid, "SUPPORTING"))
    for cid, uses in arch_usage.items():
        non_p15 = [u for u in uses if u[0] != "P15"]
        home_pkg[cid] = non_p15[0] if non_p15 else uses[0]
    mrow = {}
    for r in matrix["rows"]:
        for d in r.get("discovery_ids", []):
            mrow[d] = r
    # Evidence acceptance path via checkpoint
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
    entries = []
    for axis in sorted(amap.keys()):
        for did in amap[axis]:
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
            for coll, _k in (("claims", None), ("metrics", None), ("limitations", None)):
                for item in card.get(coll, []):
                    subjects.add(item["subject_id"])
            hp, usage = home_pkg[cid]
            entries.append({
                "synthesis_axis": axis,
                "discovery_id": did,
                "candidate_id": cid,
                "canonical_home_package": hp,
                "home_architecture_usage": usage,
                "all_architecture_usages": [{"package_id": p, "usage": u} for p, u in arch_usage[cid]],
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
    # dedup by discovery id (multi-axis entries repeated per axis intentionally kept per axis)
    out = {
        "schema_version": "1.0",
        "issue_id": "SP-vision-multimodal-2026",
        "authority_kind": "edition-local P15 mixed-placement cross-package synthesis compatibility overlay",
        "allowlist_source": "architecture-v2.json publication_extensions.p15_cross_package_synthesis_map",
        "architecture_sha256": arch_sha,
        "architecture_approval_sha256": appr_sha,
        "candidate_matrix_sha256": matrix_sha,
        "evidence_acceptance_sha256": ev_acc_sha,
        "entry_count": len(entries),
        "unique_discovery_count": len({e["discovery_id"] for e in entries}),
        "entries": entries,
    }
    OUTDIR.mkdir(parents=True, exist_ok=True)
    (OUTDIR / "p15-cross-package-synthesis-authority.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"entries": len(entries), "unique": len({e['discovery_id'] for e in entries})}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
