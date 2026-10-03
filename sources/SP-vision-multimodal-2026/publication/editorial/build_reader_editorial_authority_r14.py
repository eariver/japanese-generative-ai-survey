#!/usr/bin/env python3
"""Build TS-003 reader/editorial authority r14 (content convergence).

Chain: r13 -> r14 (CONTENT_CONVERGENCE_CANDIDATE / FRESH_CONTENT_REVIEW_REQUIRED).
Ops: r14-ops-a.json + r14-ops-a2.json + r14-ops-b.json (replacements, edits,
deletions, ref_additions, inserts, metadata).
Cross-package synthesis (Architecture-sanctioned): P15 p15-b5 <- P12 trio
(carried), P15 p15-b9 X01 octet (carried), P15 p15-b3/b15 <- HallusionBench
ev-vmd080 (new; P10-home diagnostic authority, PRIMARY home unchanged).
Evidence refs validated against the r6 acceptance
(5b8d4ba62aa56465007f34782cc88e8f32ea4a9181c66cc9fa74785eb6ff07ab).

Reproducible: re-run this script; r13 bytes + ops files only.
"""
import copy
import glob
import hashlib
import json
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = REPO / "sources/SP-vision-multimodal-2026"
ED = SRC / "publication/editorial"
R13 = ED / "reader-editorial-authority-r13.json"
OUT = ED / "reader-editorial-authority-r14.json"
OPS = [ED / "r14-ops-a.json", ED / "r14-ops-a2.json", ED / "r14-ops-b.json", ED / "r14-ops-c.json"]
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
        "evidence:SP-vision-multimodal-2026:8843ba1fc533e700",
    }
}


def sha_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main() -> int:
    r13 = json.loads(R13.read_text(encoding="utf-8"))
    assert r13["issue_id"] == ISSUE and r13["reader_editorial_revision"] == "r13"
    evidx = {}
    for f in glob.glob(str(SRC / f"evidence/v2/accepted/{EV6}/results/*.json")):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        stmts = {c["statement_id"]: c["subject_id"] for c in d.get("claims", [])}
        stmts.update({m["statement_id"]: m["subject_id"] for m in d.get("metrics", [])})
        stmts.update({l["statement_id"]: l["subject_id"] for l in d.get("limitations", [])})
        evidx[d["evidence_task_id"]] = stmts
    assert len(evidx) == 111, len(evidx)
    r14 = copy.deepcopy(r13)
    by_pid = {p["package_id"]: p for p in r14["reader_packages"]}

    ops = {"replacements": [], "deletions": [], "edits": [], "ref_additions": [],
           "inserts": [], "metadata": []}
    for f in OPS:
        d = json.loads(f.read_text(encoding="utf-8"))
        for k in ops:
            ops[k].extend(d.get(k, []))

    allowed = {}
    for p in r13["reader_packages"]:
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
            assert r["kind"] in ("CLAIM", "LIMITATION"), r
            ok = r["evidence_task_id"] in allowed[pid] or \
                r["evidence_task_id"] in CROSS_PACKAGE_ALLOW.get(pid, set())
            assert ok, f"non-local ref {pid} {r['evidence_task_id']}"
            assert r["evidence_task_id"] in evidx, f"unknown task {r['evidence_task_id']}"
            stmt = evidx[r["evidence_task_id"]].get(r["evidence_id"])
            assert stmt is not None, f"unknown statement {r['evidence_id']}"
            assert stmt == r["subject_id"], "subject mismatch"

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
        pkg = by_pid[nb["package_id"]]
        ids = [b["block_id"] for b in pkg["ordered_blocks"]]
        assert nb["block_id"] not in ids and nb["after_block_id"] in ids
        check_refs(nb["package_id"], nb["evidence_refs"])
        blk = {"block_id": nb["block_id"], "block_type": nb["block_type"],
               "reader_text": nb["reader_text"],
               "reader_text_sha256": sha_text(nb["reader_text"]),
               "evidence_refs": nb["evidence_refs"]}
        pkg["ordered_blocks"].insert(ids.index(nb["after_block_id"]) + 1, blk)
        touched.setdefault(nb["package_id"], []).append(nb["block_id"])
    for ra in ops["ref_additions"]:
        pkg = by_pid[ra["package_id"]]
        blk = [b for b in pkg["ordered_blocks"] if b["block_id"] == ra["block_id"]]
        assert len(blk) == 1
        check_refs(ra["package_id"], ra["add_refs"])
        blk[0]["evidence_refs"].extend(ra["add_refs"])
        touched.setdefault(ra["package_id"], []).append(ra["block_id"])
    for md in ops["metadata"]:
        if md["kind"] == "unresolved_lineage_questions":
            r14["reader_synthesis"]["profile_payload"]["unresolved_lineage_questions"] = md["text"]
        elif md["kind"] == "reader_wording_source":
            r14["renderer_binding"]["reader_wording_source"] = md["text"]
        else:
            raise ValueError(f"unknown metadata kind {md['kind']}")
        touched.setdefault("_metadata", []).append(md["kind"])

    for p in r14["reader_packages"]:
        for b in p["ordered_blocks"]:
            if b["block_type"] == "PARAGRAPH":
                assert b.get("evidence_refs"), f"empty refs {p['package_id']} {b['block_id']}"

    for p in r14["reader_packages"]:
        pid = p["package_id"]
        if pid in touched:
            p["must_cover_coverage"].append({
                "requirement": "TS-003 r14 content convergence: stale-LIMIT reconciliation, "
                               "license refresh, comparison-role dedup, causality/terminology "
                               "fixes, P15 provenance cleanup (candidate, pending fresh review)",
                "block_ids": sorted(set(touched[pid]))})
            p["boundary_dispositions"].append({
                "boundary": "r14 repairs reuse package-local Evidence, r6-supplemented "
                            "claims, official current license sources (date-bound), or "
                            "Architecture-sanctioned P15 cross-package synthesis.",
                "handling": "EXPLICITLY_STATED",
                "block_ids": sorted(set(touched[pid])),
                "rationale": "Convergence repair of independent-review follow-up items."})
        payload = json.dumps({"package_id": p["package_id"], "headline": p["headline"],
                              "deck": p["deck"], "blocks": p["ordered_blocks"]},
                             ensure_ascii=False, sort_keys=True).encode("utf-8")
        p["r14_derived_sha256"] = hashlib.sha256(payload).hexdigest()

    r14["semantic_labels"] = {
        "CANONICAL_DRAFT_AUTHORITY": "checkpointed r1 via ARCHITECTURE_ESTABLISHED.json "
                                     "(DRAFT_COMPLETE checkpoint, immutable)",
        "READER_EDITORIAL_AUTHORITY": "r13 review follow-up + r14 content convergence "
                                      "candidate, publication layer only",
        "warning": "r14 is CONTENT_CONVERGENCE_CANDIDATE / FRESH_CONTENT_REVIEW_REQUIRED; "
                   "never Sol-accepted, approved, or canonical.",
    }
    r14["reader_editorial_revision"] = "r14"
    r14["parent_reader_revision"] = "r13"
    r14["parent_reader_sha256"] = hashlib.sha256(R13.read_bytes()).hexdigest()
    cross = r13.get("cross_package_provenance", [])
    cross = cross + [{
        "consumer": "P15 p15-b3 / p15-b15 (failure-attribution synthesis)",
        "authorities": ["evidence:SP-vision-multimodal-2026:8843ba1fc533e700 "
                        "(ev-vmd080 HallusionBench, claim-1)"],
        "basis": "architecture-v2.json P15 must_cover failure-attribution clause: bound "
                 "via the extension cross-synthesis map to the already-selected P10-home "
                 "diagnostic authority. Each P15 clause restates its home package's claim "
                 "(346-image control-pair structure, language-hallucination vs "
                 "visual-illusion separation, pair-accuracy as strict diagnostic, small "
                 "handcrafted scale); PRIMARY home unchanged in P10. Reused SUPPORTING "
                 "authority changes publication role to synthesis evidence; no new "
                 "technical transitions.",
    }]
    r14["cross_package_provenance"] = cross
    r14["provenance"] = {
        "built_from": f"reader-editorial-authority-r13.json@{r14['parent_reader_sha256'][:12]} "
                      "+ r14-ops-a/a2/b.json",
        "reproducible": "re-run this script; r13 bytes + explicit ops files only",
        "generator": "sources/SP-vision-multimodal-2026/publication/editorial/"
                     "build_reader_editorial_authority_r14.py",
    }
    OUT.write_text(json.dumps(r14, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} replaced={len(ops['replacements'])} "
          f"edits={len(ops['edits'])} metadata={len(ops['metadata'])}")

    r13_by = {(p["package_id"], b["block_id"]): b for p in r13["reader_packages"]
              for b in p["ordered_blocks"]}
    r14_by = {(p["package_id"], b["block_id"]): b for p in r14["reader_packages"]
              for b in p["ordered_blocks"]}
    changed = {(nb["package_id"], nb["block_id"]) for nb in ops["replacements"]} | edited_ids
    ref_added = {(ra["package_id"], ra["block_id"]) for ra in ops["ref_additions"]}
    for k, b13 in r13_by.items():
        b14 = r14_by.get(k)
        if b14 is None:
            assert [k[0], k[1]] in ops["deletions"], f"undeclared loss {k}"
            continue
        if k in changed:
            continue
        assert b14["reader_text"] == b13["reader_text"], f"text changed {k}"
        if k in ref_added:
            old = {(r["evidence_task_id"], r["evidence_id"]) for r in b13["evidence_refs"]}
            new = {(r["evidence_task_id"], r["evidence_id"]) for r in b14["evidence_refs"]}
            assert new > old, f"refs not extended {k}"
            continue
        assert b14["evidence_refs"] == b13["evidence_refs"], f"refs changed {k}"
    for p13 in r13["reader_packages"]:
        p14 = by_pid[p13["package_id"]]
        assert p14["deck"] == p13["deck"] and p14["headline"] == p13["headline"]
    # metadata assertions
    assert "reader-editorial-authority-r14.json" in r14["renderer_binding"]["reader_wording_source"]
    assert "SigLIP2" not in r14["reader_synthesis"]["profile_payload"]["unresolved_lineage_questions"]
    print("r14 integrity PASS.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
