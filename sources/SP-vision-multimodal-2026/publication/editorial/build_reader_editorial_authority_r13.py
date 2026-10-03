#!/usr/bin/env python3
"""Build TS-003 reader/editorial authority r13 (review follow-up bounded repair).

Chain: r12 -> r13 (BOUNDED_CONTENT_REPAIR_CANDIDATE / FRESH_CONTENT_REVIEW_REQUIRED).
Basis: independent review (HEAD 103df2866) priorities 4-7 at reader level +
Evidence r6 batch (priorities 1-3): OpenVLA/Genie micro-repair + P09 supplement.

Ops: r13-ops-a.json + r13-ops-b.json. Inserts supported (after_block_id).
Cross-package synthesis (Architecture-sanctioned): P15 p15-b5 <- P12 trio
(must_cover map) + P15 p15-b9 X01 timeline <- named already-selected
supervision evidence (X01-X04 synthesis clause). PRIMARY homes unchanged.
Evidence refs validated against the NEW r6 acceptance
(5b8d4ba62aa56465007f34782cc88e8f32ea4a9181c66cc9fa74785eb6ff07ab):
task IDs stable across repair; new claim-3/4/5 + 4/5/6 verified present.

Reproducible: re-run this script; r12 bytes + ops files only.
"""
import copy
import glob
import hashlib
import json
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = REPO / "sources/SP-vision-multimodal-2026"
ED = SRC / "publication/editorial"
R12 = ED / "reader-editorial-authority-r12.json"
OUT = ED / "reader-editorial-authority-r13.json"
OPS = [ED / "r13-ops-a.json", ED / "r13-ops-b.json"]
EV6 = "5b8d4ba62aa56465007f34782cc88e8f32ea4a9181c66cc9fa74785eb6ff07ab"

ISSUE = "SP-vision-multimodal-2026"

CROSS_PACKAGE_ALLOW = {
    "P15": {
        "evidence:SP-vision-multimodal-2026:85268ad1dbd5f285",
        "evidence:SP-vision-multimodal-2026:6852a5755398b866",
        "evidence:SP-vision-multimodal-2026:3d4f179a082773fd",
        "evidence:SP-vision-multimodal-2026:649b3797fd83a762",
        "evidence:SP-vision-multimodal-2026:20d1ebc2759ddd61",
        "evidence:SP-vision-multimodal-2026:48beece23bd3412f",
        "evidence:SP-vision-multimodal-2026:9dce7c29b30f2b61",
        "evidence:SP-vision-multimodal-2026:4e994d899261cc65",
        "evidence:SP-vision-multimodal-2026:b049264287440eba",
        "evidence:SP-vision-multimodal-2026:48f42e295f015ec1",
        "evidence:SP-vision-multimodal-2026:b57c9615772bd967",
    }
}


def sha_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main() -> int:
    r12 = json.loads(R12.read_text(encoding="utf-8"))
    assert r12["issue_id"] == ISSUE and r12["reader_editorial_revision"] == "r12"
    # Evidence index from the NEW r6 acceptance (task IDs stable; new claims present).
    evidx = {}
    for f in glob.glob(str(SRC / f"evidence/v2/accepted/{EV6}/results/*.json")):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        stmts = {c["statement_id"]: c["subject_id"] for c in d.get("claims", [])}
        stmts.update({m["statement_id"]: m["subject_id"] for m in d.get("metrics", [])})
        stmts.update({l["statement_id"]: l["subject_id"] for l in d.get("limitations", [])})
        evidx[d["evidence_task_id"]] = stmts
    assert len(evidx) == 111, len(evidx)
    r13 = copy.deepcopy(r12)
    by_pid = {p["package_id"]: p for p in r13["reader_packages"]}

    ops = {"replacements": [], "deletions": [], "edits": [], "ref_additions": [], "inserts": []}
    for f in OPS:
        d = json.loads(f.read_text(encoding="utf-8"))
        for k in ops:
            ops[k].extend(d.get(k, []))

    allowed = {}
    for p in r12["reader_packages"]:
        s = set()
        for r in p.get("deck_evidence_refs", []) or []:
            s.add(r["evidence_task_id"])
        for b in p["ordered_blocks"]:
            for r in b.get("evidence_refs", []) or []:
                s.add(r["evidence_task_id"])
        allowed[p["package_id"]] = s

    def check_refs(pid, refs):
        for r in refs:
            assert set(r.keys()) == {"evidence_task_id", "kind", "evidence_id",
                                      "subject_id", "subject_role"}, r
            assert r["subject_role"] == "PRIMARY_SUBJECT", r
            assert r["kind"] == "CLAIM", r
            ok = r["evidence_task_id"] in allowed[pid] or \
                r["evidence_task_id"] in CROSS_PACKAGE_ALLOW.get(pid, set())
            assert ok, f"non-local ref {pid} {r['evidence_task_id']}"
            assert r["evidence_task_id"] in evidx, f"unknown task {r['evidence_task_id']}"
            stmt = evidx[r["evidence_task_id"]].get(r["evidence_id"])
            assert stmt is not None, f"unknown statement {r['evidence_id']} in {r['evidence_task_id']}"
            assert stmt == r["subject_id"], f"subject mismatch {r['evidence_id']}"

    touched = {}
    for pid, bid in ops["deletions"]:
        pkg = by_pid[pid]
        ids = [b["block_id"] for b in pkg["ordered_blocks"]]
        assert bid in ids, f"del miss {pid} {bid}"
        assert not bid.endswith("-boundaries")
        pkg["ordered_blocks"] = [b for b in pkg["ordered_blocks"] if b["block_id"] != bid]
        touched.setdefault(pid, []).append(bid)
    for nb in ops["replacements"]:
        pkg = by_pid[nb["package_id"]]
        blk = [b for b in pkg["ordered_blocks"] if b["block_id"] == nb["block_id"]]
        assert len(blk) == 1, f"replace miss {nb['package_id']} {nb['block_id']}"
        check_refs(nb["package_id"], nb["evidence_refs"])
        blk[0]["reader_text"] = nb["reader_text"]
        blk[0]["reader_text_sha256"] = sha_text(nb["reader_text"])
        blk[0]["evidence_refs"] = nb["evidence_refs"]
        touched.setdefault(nb["package_id"], []).append(nb["block_id"])
    edited_ids = set()
    for e in ops["edits"]:
        pkg = by_pid[e["package_id"]]
        hit = [b for b in pkg["ordered_blocks"] if b["reader_text"].count(e["old"]) == 1]
        assert len(hit) == 1, f"edit miss {e['package_id']}: {e['old'][:50]}"
        hit[0]["reader_text"] = hit[0]["reader_text"].replace(e["old"], e["new"])
        hit[0]["reader_text_sha256"] = sha_text(hit[0]["reader_text"])
        edited_ids.add((e["package_id"], hit[0]["block_id"]))
        touched.setdefault(e["package_id"], []).append(hit[0]["block_id"])
    for nb in ops["inserts"]:
        pid = nb["package_id"]
        pkg = by_pid[pid]
        ids = [b["block_id"] for b in pkg["ordered_blocks"]]
        assert nb["block_id"] not in ids, f"collision {pid} {nb['block_id']}"
        assert nb["after_block_id"] in ids, f"anchor miss {pid} {nb['after_block_id']}"
        check_refs(pid, nb["evidence_refs"])
        blk = {"block_id": nb["block_id"], "block_type": nb["block_type"],
               "reader_text": nb["reader_text"],
               "reader_text_sha256": sha_text(nb["reader_text"]),
               "evidence_refs": nb["evidence_refs"]}
        pkg["ordered_blocks"].insert(ids.index(nb["after_block_id"]) + 1, blk)
        touched.setdefault(pid, []).append(nb["block_id"])
    for ra in ops["ref_additions"]:
        pkg = by_pid[ra["package_id"]]
        blk = [b for b in pkg["ordered_blocks"] if b["block_id"] == ra["block_id"]]
        assert len(blk) == 1
        check_refs(ra["package_id"], ra["add_refs"])
        blk[0]["evidence_refs"].extend(ra["add_refs"])
        touched.setdefault(ra["package_id"], []).append(ra["block_id"])

    # Empty-ref legitimacy: none allowed in r13 (p15-b9 now bound).
    for p in r13["reader_packages"]:
        for b in p["ordered_blocks"]:
            if b["block_type"] == "PARAGRAPH":
                assert b.get("evidence_refs"), f"empty refs {p['package_id']} {b['block_id']}"

    for p in r13["reader_packages"]:
        pid = p["package_id"]
        if pid in touched:
            p["must_cover_coverage"].append({
                "requirement": "TS-003 r13 review follow-up: residual dedup, terminology "
                               "standardization, X01 supervision timeline, P09 supplement "
                               "prose (candidate, pending fresh content review)",
                "block_ids": sorted(set(touched[pid]))})
            p["boundary_dispositions"].append({
                "boundary": "r13 repairs reuse package-local Evidence, r6-supplemented "
                            "P09 claims, or Architecture-sanctioned P15 cross-package "
                            "synthesis; no new claims, no TeX/PDF regeneration.",
                "handling": "EXPLICITLY_STATED",
                "block_ids": sorted(set(touched[pid])),
                "rationale": "Bounded repair of independent-review follow-up items."})
        payload = json.dumps({"package_id": p["package_id"], "headline": p["headline"],
                              "deck": p["deck"], "blocks": p["ordered_blocks"]},
                             ensure_ascii=False, sort_keys=True).encode("utf-8")
        p["r13_derived_sha256"] = hashlib.sha256(payload).hexdigest()

    r13["semantic_labels"] = {
        "CANONICAL_DRAFT_AUTHORITY": "checkpointed r1 via ARCHITECTURE_ESTABLISHED.json "
                                     "(DRAFT_COMPLETE checkpoint, immutable)",
        "READER_EDITORIAL_AUTHORITY": "r12 bounded repair + r13 review follow-up "
                                      "candidate, publication layer only",
        "warning": "r13 is BOUNDED_CONTENT_REPAIR_CANDIDATE / FRESH_CONTENT_REVIEW_REQUIRED; "
                   "never Sol-accepted, approved, or canonical. Evidence r6 batch "
                   "(OpenVLA/Genie micro-repair + P09 supplement) requires Sol re-review "
                   "before downstream use beyond this reader candidate.",
    }
    r13["reader_editorial_revision"] = "r13"
    r13["parent_reader_revision"] = "r12"
    r13["parent_reader_sha256"] = hashlib.sha256(R12.read_bytes()).hexdigest()
    r13["evidence_basis"] = {
        "acceptance": f"sources/SP-vision-multimodal-2026/evidence/v2/accepted/{EV6}/evidence-accepted.json",
        "result_set_sha256": EV6,
        "note": "r13 refs validated against r6 acceptance (task IDs stable; P09 new "
                "claims claim-3/4/5 + claim-4/5/6 present; D098/D105 micro-repairs present).",
    }
    cross = r12.get("cross_package_provenance", [])
    cross = cross + [{
        "consumer": "P15 p15-b9 (X01 supervision-timeline synthesis)",
        "authorities": [
            "evidence:SP-vision-multimodal-2026:649b3797fd83a762 (ev-vmd003 supervised labels)",
            "evidence:SP-vision-multimodal-2026:20d1ebc2759ddd61 (ev-vmd039 contrastive pairs)",
            "evidence:SP-vision-multimodal-2026:48beece23bd3412f (ev-vmd045 pseudo pairs)",
            "evidence:SP-vision-multimodal-2026:9dce7c29b30f2b61 (ev-vmd034 self-distillation)",
            "evidence:SP-vision-multimodal-2026:4e994d899261cc65 (ev-vmd033 masked objectives)",
            "evidence:SP-vision-multimodal-2026:b049264287440eba (ev-vmd060 instruction tuning)",
            "evidence:SP-vision-multimodal-2026:48f42e295f015ec1 (ev-vmd062 synthetic instruction)",
            "evidence:SP-vision-multimodal-2026:b57c9615772bd967 (ev-vmd094 robot demonstrations)"],
        "basis": "architecture-v2.json P15 must_cover X01-X04 synthesis clause: threads "
                 "bound via the extension cross-synthesis map to named already-selected "
                 "evidence. Each clause restates its home package's claim; PRIMARY homes "
                 "unchanged; P15-native training evidence explicitly disclaimed in prose.",
    }]
    r13["cross_package_provenance"] = cross
    r13["provenance"] = {
        "built_from": f"reader-editorial-authority-r12.json@{r13['parent_reader_sha256'][:12]} "
                      "+ r13-ops-a/b.json",
        "reproducible": "re-run this script; r12 bytes + explicit ops files only",
        "generator": "sources/SP-vision-multimodal-2026/publication/editorial/"
                     "build_reader_editorial_authority_r13.py",
    }
    OUT.write_text(json.dumps(r13, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    n_rep = len(ops["replacements"])
    n_ins = len(ops["inserts"])
    print(f"wrote {OUT.relative_to(REPO)} replaced={n_rep} inserted={n_ins} "
          f"deleted={len(ops['deletions'])} edits={len(ops['edits'])}")

    # Integrity vs r12.
    r12_by = {(p["package_id"], b["block_id"]): b for p in r12["reader_packages"]
              for b in p["ordered_blocks"]}
    r13_by = {(p["package_id"], b["block_id"]): b for p in r13["reader_packages"]
              for b in p["ordered_blocks"]}
    changed = {(nb["package_id"], nb["block_id"]) for nb in ops["replacements"]} | edited_ids
    for k, b12 in r12_by.items():
        b13 = r13_by.get(k)
        if b13 is None:
            assert [k[0], k[1]] in ops["deletions"], f"undeclared loss {k}"
            continue
        if k in changed:
            continue
        assert b13["reader_text"] == b12["reader_text"], f"text changed {k}"
        assert b13["evidence_refs"] == b12["evidence_refs"], f"refs changed {k}"
    for p12 in r12["reader_packages"]:
        p13 = by_pid[p12["package_id"]]
        assert p13["deck"] == p12["deck"] and p13["headline"] == p12["headline"]
    print("r13 integrity PASS.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
