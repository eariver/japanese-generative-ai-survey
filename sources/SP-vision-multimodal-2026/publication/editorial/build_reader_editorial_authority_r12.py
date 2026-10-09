#!/usr/bin/env python3
"""Build TS-003 reader/editorial authority r12 (bounded content repair).

Chain: r11 (technical-depth restoration candidate) -> r12
(BOUNDED_CONTENT_REPAIR_CANDIDATE / FRESH_CONTENT_REVIEW_REQUIRED).
Basis: independent review REQUEST_CHANGES + approved Architecture + existing
Evidence + limited primary-source verification (reports/papers consulted for
verification only; no new evidence_task_ids).

Ops: r12-ops-a.json + r12-ops-b1.json + r12-ops-b2.json under the same dir.
- replacements: full new reader_text + evidence_refs (refs must be
  package-local evidence_task_ids, except the Architecture-sanctioned P15
  cross-package synthesis binding listed in CROSS_PACKAGE_ALLOW).
- edits: exact-once old->new sentence/phrase repairs.
- deletions: semantic-duplicate blocks whose every proposition is retained
  elsewhere (recorded in the repair report; never blanket deletion).
- ref_additions: P15 p15-b5 cross-package binding with provenance record.

Reproducible: re-run this script; r11 bytes + ops files only.
"""
import copy
import glob
import hashlib
import json
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = REPO / "sources/SP-vision-multimodal-2026"
ED = SRC / "publication/editorial"
R11 = ED / "reader-editorial-authority-r11.json"
OUT = ED / "reader-editorial-authority-r12.json"
OPS = [ED / "r12-ops-a.json", ED / "r12-ops-b1.json", ED / "r12-ops-b2.json"]

ISSUE = "SP-vision-multimodal-2026"

# Architecture-sanctioned cross-package synthesis binding (P15 must_cover:
# "P15 consumes P12 GUI/Computer-Use evaluation via the extension
# cross-synthesis map; PRIMARY single-destination rule keeps home in P12").
CROSS_PACKAGE_ALLOW = {
    "P15": {
        "evidence:SP-vision-multimodal-2026:85268ad1dbd5f285",
        "evidence:SP-vision-multimodal-2026:6852a5755398b866",
        "evidence:SP-vision-multimodal-2026:3d4f179a082773fd",
    }
}

# PARAGRAPH blocks legitimately carrying empty refs (pure editorial gap
# declaration with explicit scope delimiters, §7.2 option 2).
EMPTY_REF_ALLOW = {("P15", "p15-b9")}
P15_B9_DELIMITERS = ("以下は編集上の整理であり、資料由来の事実主張ではない",
                     "本段落は根拠の不在の宣言であり、新たな時系列の主張ではない")


def sha_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def load_evidence_index():
    idx = {}
    for f in glob.glob(str(SRC / "evidence/v2/accepted/*/results/*.json")):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        stmts = {c["statement_id"]: c["subject_id"] for c in d.get("claims", [])}
        stmts.update({l["statement_id"]: l["subject_id"]
                      for l in d.get("limitations", [])})
        idx[d["evidence_task_id"]] = stmts
    return idx


def main() -> int:
    r11 = json.loads(R11.read_text(encoding="utf-8"))
    assert r11["issue_id"] == ISSUE and r11["reader_editorial_revision"] == "r11"
    evidx = load_evidence_index()
    r12 = copy.deepcopy(r11)
    by_pid = {p["package_id"]: p for p in r12["reader_packages"]}

    ops = {"replacements": [], "deletions": [], "edits": [], "ref_additions": []}
    for f in OPS:
        d = json.loads(f.read_text(encoding="utf-8"))
        for k in ops:
            ops[k].extend(d.get(k, []))

    # Package-local allow-list from r11.
    allowed = {}
    for p in r11["reader_packages"]:
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
            assert stmt is not None, f"unknown statement {r['evidence_id']} in {r['evidence_task_id']}"
            assert stmt == r["subject_id"], \
                f"subject mismatch {r['evidence_id']}: {stmt} vs {r['subject_id']}"

    touched = {}
    # Deletions.
    deleted = []
    for pid, bid in ops["deletions"]:
        pkg = by_pid[pid]
        ids = [b["block_id"] for b in pkg["ordered_blocks"]]
        assert bid in ids, f"del miss {pid} {bid}"
        assert not bid.endswith("-boundaries"), f"refuse boundary delete {pid} {bid}"
        pkg["ordered_blocks"] = [b for b in pkg["ordered_blocks"] if b["block_id"] != bid]
        deleted.append({"package_id": pid, "block_id": bid})
        touched.setdefault(pid, []).append(bid)
    # Replacements.
    replaced = []
    for nb in ops["replacements"]:
        pid, bid = nb["package_id"], nb["block_id"]
        pkg = by_pid[pid]
        blk = [b for b in pkg["ordered_blocks"] if b["block_id"] == bid]
        assert len(blk) == 1, f"replace miss {pid} {bid}"
        b = blk[0]
        if bid.endswith("-boundaries"):
            assert nb["block_type"] == "CLAIM_BOUNDARY", (pid, bid)
        else:
            assert nb["block_type"] == "PARAGRAPH", (pid, bid)
        check_refs(pid, nb["evidence_refs"])
        b["reader_text"] = nb["reader_text"]
        b["reader_text_sha256"] = sha_text(nb["reader_text"])
        b["evidence_refs"] = nb["evidence_refs"]
        replaced.append({"package_id": pid, "block_id": bid,
                         "serves_nodes": nb.get("serves_nodes", [])})
        touched.setdefault(pid, []).append(bid)
    # Edits.
    n_edit = 0
    edited_ids = set()
    for e in ops["edits"]:
        pkg = by_pid[e["package_id"]]
        hit = [b for b in pkg["ordered_blocks"]
               if b["reader_text"].count(e["old"]) == 1]
        assert len(hit) == 1, f"edit miss {e['package_id']}: {e['old'][:50]}"
        hit[0]["reader_text"] = hit[0]["reader_text"].replace(e["old"], e["new"])
        hit[0]["reader_text_sha256"] = sha_text(hit[0]["reader_text"])
        n_edit += 1
        edited_ids.add((e["package_id"], hit[0]["block_id"]))
        touched.setdefault(e["package_id"], []).append(hit[0]["block_id"])
    # Ref additions.
    for ra in ops["ref_additions"]:
        pkg = by_pid[ra["package_id"]]
        blk = [b for b in pkg["ordered_blocks"] if b["block_id"] == ra["block_id"]]
        assert len(blk) == 1
        check_refs(ra["package_id"], ra["add_refs"])
        have = {(r["evidence_task_id"], r["evidence_id"]) for r in blk[0]["evidence_refs"]}
        for r in ra["add_refs"]:
            assert (r["evidence_task_id"], r["evidence_id"]) not in have, f"dup ref {ra}"
            blk[0]["evidence_refs"].append(r)
        touched.setdefault(ra["package_id"], []).append(ra["block_id"])

    # Empty-ref legitimacy.
    for p in r12["reader_packages"]:
        for b in p["ordered_blocks"]:
            if b["block_type"] == "PARAGRAPH" and not b.get("evidence_refs"):
                assert (p["package_id"], b["block_id"]) in EMPTY_REF_ALLOW, \
                    f"empty refs {p['package_id']} {b['block_id']}"
    b9 = [b for b in by_pid["P15"]["ordered_blocks"] if b["block_id"] == "p15-b9"][0]
    for s in P15_B9_DELIMITERS:
        assert s in b9["reader_text"], "p15-b9 delimiter missing"

    # Per-package coverage/boundary entries + derived sha.
    for p in r12["reader_packages"]:
        pid = p["package_id"]
        if pid in touched:
            p["must_cover_coverage"].append({
                "requirement": "TS-003 r12 bounded content repair: technical corrections, "
                               "semantic-dedup integration, provenance repair (candidate, "
                               "pending fresh content review)",
                "block_ids": sorted(set(touched[pid]))})
            p["boundary_dispositions"].append({
                "boundary": "r12 repairs reuse package-local Evidence only (plus the "
                            "Architecture-sanctioned P15<-P12 synthesis binding); no new "
                            "claims, no TeX/PDF regeneration.",
                "handling": "EXPLICITLY_STATED",
                "block_ids": sorted(set(touched[pid])),
                "rationale": "Bounded repair of independent-review REQUEST_CHANGES."})
        payload = json.dumps({"package_id": p["package_id"], "headline": p["headline"],
                              "deck": p["deck"], "blocks": p["ordered_blocks"]},
                             ensure_ascii=False, sort_keys=True).encode("utf-8")
        p["r12_derived_sha256"] = hashlib.sha256(payload).hexdigest()

    r12["semantic_labels"] = {
        "CANONICAL_DRAFT_AUTHORITY": "checkpointed r1 via ARCHITECTURE_ESTABLISHED.json "
                                     "(DRAFT_COMPLETE checkpoint, immutable)",
        "READER_EDITORIAL_AUTHORITY": "r11 technical-depth candidate + r12 bounded content "
                                      "repair candidate, publication layer only",
        "warning": "r12 is BOUNDED_CONTENT_REPAIR_CANDIDATE / FRESH_CONTENT_REVIEW_REQUIRED; "
                   "never Sol-accepted, approved, or canonical. Never claim r12 remains "
                   "canonical Draft authority.",
    }
    r12["reader_editorial_revision"] = "r12"
    r12["parent_reader_revision"] = "r11"
    r12["parent_reader_sha256"] = hashlib.sha256(R11.read_bytes()).hexdigest()
    r12["independent_review_basis"] = {
        "decision": "REQUEST_CHANGES on r11 technical-depth restoration",
        "repair_scope": "bounded content repair: semantic-dedup integration, technical "
                        "corrections (CLIP/LLaVA/DINO/RT-1/RT-2/OpenVLA/DreamerV3/Genie/"
                        "RPN/DETR), P15 supervision/eval separation + provenance, P09 "
                        "disclosure limits, P06 attribution confirmation, Japanese repair",
    }
    r12["cross_package_provenance"] = [{
        "consumer": "P15 p15-b5 (screen-operation layer-separation synthesis)",
        "authorities": [
            "evidence:SP-vision-multimodal-2026:85268ad1dbd5f285 (ev-vmd090 OSWorld)",
            "evidence:SP-vision-multimodal-2026:6852a5755398b866 (ev-vmd091 OSWorld 2.0)",
            "evidence:SP-vision-multimodal-2026:3d4f179a082773fd (ev-vmd092 SeeClick/ScreenSpot)"],
        "basis": "architecture-v2.json P15 must_cover: P15 consumes P12 GUI/Computer-Use "
                 "evaluation via the extension cross-synthesis map; PRIMARY "
                 "single-destination rule keeps their package home in P12. Reused "
                 "SUPPORTING authorities change publication role to synthesis evidence; "
                 "no new technical transitions; no P12 numbers imported beyond contract "
                 "separation already in p15-b5 prose.",
    }]
    r12["provenance"] = {
        "built_from": f"reader-editorial-authority-r11.json@{r12['parent_reader_sha256'][:12]} "
                      "+ r12-ops-a/b1/b2.json",
        "reproducible": "re-run this script; r11 bytes + explicit ops files only",
        "generator": "sources/SP-vision-multimodal-2026/publication/editorial/"
                     "build_reader_editorial_authority_r12.py",
    }
    r12["bounded_repair"] = {
        "revision": "r12",
        "status": "BOUNDED_CONTENT_REPAIR_CANDIDATE / FRESH_CONTENT_REVIEW_REQUIRED",
        "replaced_blocks": replaced,
        "deleted_blocks": deleted,
        "sentence_edits": n_edit,
    }
    OUT.write_text(json.dumps(r12, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} replaced={len(replaced)} "
          f"deleted={len(deleted)} edits={n_edit}")

    # Integrity: non-touched blocks byte-identical; decks/headlines untouched.
    r11_by = {(p["package_id"], b["block_id"]): b for p in r11["reader_packages"]
              for b in p["ordered_blocks"]}
    r12_by = {(p["package_id"], b["block_id"]): b for p in r12["reader_packages"]
              for b in p["ordered_blocks"]}
    changed_ids = {(nb["package_id"], nb["block_id"]) for nb in ops["replacements"]}
    changed_ids |= edited_ids
    edit_touched = set()
    # re-derive edited block ids by diff
    for k, b11 in r11_by.items():
        b12 = r12_by.get(k)
        if b12 is None:
            assert [k[0], k[1]] in ops["deletions"], f"undeclared loss {k}"
            continue
        if k in changed_ids:
            continue
        assert b12["reader_text"] == b11["reader_text"], f"text changed {k}"
        assert b12["evidence_refs"] == b11["evidence_refs"], f"refs changed {k}"
    for p11 in r11["reader_packages"]:
        p12 = by_pid[p11["package_id"]]
        assert p12["deck"] == p11["deck"] and p11["headline"] == p12["headline"]
        old_ids = [b["block_id"] for b in p11["ordered_blocks"]
                   if [p11["package_id"], b["block_id"]] not in ops["deletions"]]
        new_ids = [b["block_id"] for b in p12["ordered_blocks"]]
        assert new_ids == old_ids, f"order changed {p11['package_id']}"
    print(f"r12 integrity PASS: untouched blocks identical, decks/headlines intact, "
          f"order preserved modulo {len(deleted)} declared deletions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
