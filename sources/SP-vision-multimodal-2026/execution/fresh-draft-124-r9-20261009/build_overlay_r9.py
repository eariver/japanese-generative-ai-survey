#!/usr/bin/env python3
"""Build cross-package-map-fresh-124-r9.json rebound to r9 authority.

33 entries (P06 1, P07A 1, P07B 2, P10 2, P11 1, P15 26) re-derived from
current matrix/evidence/selection. No new candidates; synthesis refs only.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/fresh-draft-124-r9-20261009"
OUT = EDIR / "cross-package-map-fresh-124-r9.json"

CONSUMERS = {
    "P06": ["VM-D065"],
    "P07A": ["VM-D114"],
    "P07B": ["VM-D114", "VM-D115"],
    "P10": ["VM-D111", "VM-D112"],
    "P11": ["VM-D115"],
    "P15": ["VM-D003","VM-D010","VM-D027","VM-D028","VM-D035","VM-D047","VM-D051","VM-D056",
            "VM-D059","VM-D062","VM-D065","VM-D070","VM-D071","VM-D080","VM-D088","VM-D089",
            "VM-D090","VM-D091","VM-D092","VM-D096","VM-D097","VM-D098","VM-D103","VM-D104",
            "VM-D105","VM-D120"],
}

def sha_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main() -> int:
    from scripts import survey_production_v2 as core
    arch = core.load_json(SRC / "architecture-v2.json")
    matrix = core.load_json(SRC / "candidate-matrix-v2.json")
    sel = core.load_json(SRC / "candidate-selection-v2.json")
    acc_path = SRC / "evidence/v2/accepted/6b55033d02efecf69d784ebe8af534058222f84e37668b16c6341f8cc2deacd5/evidence-accepted.json"
    acc = core.load_json(acc_path)
    by_task = {r["evidence_task_id"]: r for r in acc["results"]}
    # discovery -> matrix row
    d2row = {}
    for r in matrix["rows"]:
        for did in r.get("discovery_ids", []):
            assert did not in d2row, did
            d2row[did] = r
    # selection disposition
    sel_by_cand = {a["candidate_id"]: a["disposition"] for a in sel["assignments"]}
    # arch home packages per candidate
    c2pkgs = {}
    for p in arch["packages"]:
        for cid in p.get("primary_candidate_ids", []) + p.get("supporting_candidate_ids", []):
            c2pkgs.setdefault(cid, []).append(p["package_id"])
    entries = []
    for consumer, dids in CONSUMERS.items():
        for did in dids:
            row = d2row.get(did)
            assert row, did
            cand = row["candidate_id"]
            tid = row["evidence_task_id"]
            meta = by_task.get(tid)
            assert meta and meta["sha256"] == row["evidence_sha256"], (did, tid)
            assert sel_by_cand.get(cand) == "SELECTED", (did, cand)
            # canonical home must not be the consumer (overlay only)
            homes = c2pkgs.get(cand, [])
            assert consumer not in homes, (consumer, did, homes)
            card_path = acc_path.parent / "results" / meta["filename"]
            assert card_path.is_file(), did
            assert sha_file(card_path) == meta["sha256"], did
            card = core.load_json(card_path)
            assert card.get("evidence_task_id") == tid, did
            entries.append({
                "consumer_package": consumer,
                "discovery_id": did,
                "candidate_id": cand,
                "canonical_home_package": homes[0] if len(homes) == 1 else "|".join(sorted(homes)),
                "home_architecture_usage": "PRIMARY_OR_SUPPORTING",
                "evidence_task_id": tid,
                "evidence_sha256": meta["sha256"],
                "evidence_filename": meta["filename"],
                "selection_disposition": "SELECTED",
                "reference_role": "CROSS_PACKAGE_SYNTHESIS_REFERENCE",
            })
    # sort for determinism
    entries.sort(key=lambda e: (e["consumer_package"], e["discovery_id"]))
    payload = {
        "schema_version": "2.0-rc1",
        "issue_id": "SP-vision-multimodal-2026",
        "authority_kind": "EDITION_LOCAL_OVERLAY_SYNTHESIS_REFERENCE",
        "consumers": sorted(CONSUMERS),
        "architecture_sha256": sha_file(SRC / "architecture-v2.json"),
        "architecture_approval_sha256": sha_file(SRC / "gates/architecture-approval.json"),
        "candidate_matrix_sha256": sha_file(SRC / "candidate-matrix-v2.json"),
        "evidence_acceptance_sha256": sha_file(acc_path),
        "entry_count": len(entries),
        "unique_discovery_count": len({e["discovery_id"] for e in entries}),
        "entries": entries,
        "provenance": ("Fresh-124-r9 generation-time overlay: 33 entries re-derived from r9 authority "
                       "(arch cd37a969, matrix 80754cca, evidence 326e7a7b, approval 385b390f); "
                       "P04/P05 need no overlay in fresh prose (all canonical); "
                       "P15 26 + P06/P07A/P07B/P10/P11 7 = 33. No placement change; synthesis refs only."),
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"overlay: {OUT.relative_to(ROOT)} | entries {len(entries)} | unique {len({e['discovery_id'] for e in entries})}")
    from collections import Counter
    print(Counter(e["consumer_package"] for e in entries))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
