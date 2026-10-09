#!/usr/bin/env python3
"""Build TS-003 edition-local reader/editorial authority r11 (technical-depth restoration).

Revision chain: r10 (Sol-accepted r9 + Issue #559 bounded repair) -> r11
(technical-depth restoration candidate, Sol review required).
Canonical Draft authority remains checkpointed r1 (immutable). r11 is
publication-layer only, never canonical Draft authority. No TeX/PDF/production-state
changes. New blocks reuse ONLY evidence_task_ids already in the package's
draft-result.json / r10 authority (verified verbatim); no new Evidence admission.

Reproducible: re-run this script; r10 bytes + r11-new-blocks-g{1,2,3}.json only.
"""
import copy
import hashlib
import json
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = REPO / "sources/SP-vision-multimodal-2026"
ED = SRC / "publication/editorial"
R10 = ED / "reader-editorial-authority-r10.json"
OUT = ED / "reader-editorial-authority-r11.json"
GFILES = [ED / "r11-new-blocks-g1.json", ED / "r11-new-blocks-g2.json",
          ED / "r11-new-blocks-g3.json"]

ISSUE = "SP-vision-multimodal-2026"


def sha_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main() -> int:
    r10 = json.loads(R10.read_text(encoding="utf-8"))
    assert r10["issue_id"] == ISSUE
    assert r10["reader_editorial_revision"] == "r10"
    r11 = copy.deepcopy(r10)
    by_pid = {p["package_id"]: p for p in r11["reader_packages"]}

    new_blocks = []
    for gf in GFILES:
        new_blocks.extend(json.loads(gf.read_text(encoding="utf-8"))["new_blocks"])

    # Validate: no duplicate block ids, anchors exist, refs are package-local.
    seen = set()
    for nb in new_blocks:
        key = (nb["package_id"], nb["block_id"])
        assert key not in seen, f"duplicate new block {key}"
        seen.add(key)
    # Package-local evidence allow-list from r10 (== draft-result sets, verified).
    allowed = {}
    for p in r10["reader_packages"]:
        s = set()
        for r in p.get("deck_evidence_refs", []) or []:
            s.add(r["evidence_task_id"])
        for b in p["ordered_blocks"]:
            for r in b.get("evidence_refs", []) or []:
                s.add(r["evidence_task_id"])
        allowed[p["package_id"]] = s

    inserted = []
    for nb in new_blocks:
        pid = nb["package_id"]
        assert pid in by_pid, pid
        pkg = by_pid[pid]
        ids = [b["block_id"] for b in pkg["ordered_blocks"]]
        assert nb["block_id"] not in ids, f"collision {pid} {nb['block_id']}"
        assert nb["after_block_id"] in ids, f"anchor miss {pid} {nb['after_block_id']}"
        for r in nb["evidence_refs"]:
            assert r["evidence_task_id"] in allowed[pid], \
                f"non-local ref {pid} {r['evidence_task_id']}"
            assert set(r.keys()) == {"evidence_task_id", "kind", "evidence_id",
                                      "subject_id", "subject_role"}, r
            assert r["kind"] == "CLAIM" and r["subject_role"] == "PRIMARY_SUBJECT", r
        blk = {"block_id": nb["block_id"], "block_type": nb["block_type"],
               "reader_text": nb["reader_text"],
               "reader_text_sha256": sha_text(nb["reader_text"]),
               "evidence_refs": nb["evidence_refs"]}
        idx = ids.index(nb["after_block_id"])
        pkg["ordered_blocks"].insert(idx + 1, blk)
        inserted.append({"package_id": pid, "block_id": nb["block_id"],
                         "after": nb["after_block_id"],
                         "serves_nodes": nb["serves_nodes"]})

    # Per-package: coverage + boundary entries for r11 additions; derived sha.
    for p in r11["reader_packages"]:
        pid = p["package_id"]
        added = [i["block_id"] for i in inserted if i["package_id"] == pid]
        if added:
            p["must_cover_coverage"].append({
                "requirement": "TS-003 technical-depth restoration r11: FULL/TRANSITION "
                               "mechanism depth complementary to r10 (candidate, pending Sol review)",
                "block_ids": added})
            p["boundary_dispositions"].append({
                "boundary": "r11 additions reuse package-local Evidence only; no new claims, "
                            "no cross-package refs, no TeX/PDF regeneration.",
                "handling": "EXPLICITLY_STATED",
                "block_ids": added,
                "rationale": "Review-candidate depth restoration; Sol review required."})
        payload = json.dumps({"package_id": p["package_id"], "headline": p["headline"],
                              "deck": p["deck"], "blocks": p["ordered_blocks"]},
                             ensure_ascii=False, sort_keys=True).encode("utf-8")
        p["r11_derived_sha256"] = hashlib.sha256(payload).hexdigest()

    # Labels / revision / provenance.
    r11["semantic_labels"] = {
        "CANONICAL_DRAFT_AUTHORITY": "checkpointed r1 via ARCHITECTURE_ESTABLISHED.json "
                                     "(DRAFT_COMPLETE checkpoint, immutable)",
        "READER_EDITORIAL_AUTHORITY": "r10 (Sol-accepted r9 + Issue #559 repair) + r11 "
                                      "technical-depth restoration candidate, publication layer only",
        "warning": "r11 is TECHNICAL_DEPTH_RESTORATION_CANDIDATE / SOL_REVIEW_REQUIRED; "
                   "never call r11 Sol-accepted, approved, or canonical. r9/r10/r11 wording "
                   "must be consumed only via reader/editorial authority after canonical "
                   "restore; never claim r10/r11 remains canonical Draft authority.",
    }
    r11["reader_editorial_revision"] = "r11"
    r11["parent_reader_revision"] = "r10"
    r11["parent_reader_sha256"] = hashlib.sha256(R10.read_bytes()).hexdigest()
    r11["technical_depth_restoration"] = {
        "revision": "r11",
        "status": "TECHNICAL_DEPTH_RESTORATION_CANDIDATE / SOL_REVIEW_REQUIRED",
        "scope": "reader JSON only; no TeX/PDF regeneration, no lifecycle advancement",
        "new_blocks": inserted,
        "traceability": "r10 -> r11 appends technical-depth blocks only; r10 headlines, "
                        "decks, pre-existing block order/text/refs unchanged; new refs are "
                        "package-local evidence_task_ids verified verbatim against "
                        "draft-result.json / r10 authority.",
    }
    r11["provenance"] = {
        "built_from": f"reader-editorial-authority-r10.json@{r11['parent_reader_sha256'][:12]} "
                      "+ r11-new-blocks-g1/g2/g3.json",
        "reproducible": "re-run this script; r10 bytes + explicit new-block files only",
        "generator": "sources/SP-vision-multimodal-2026/publication/editorial/"
                     "build_reader_editorial_authority_r11.py",
    }
    OUT.write_text(json.dumps(r11, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} new_blocks={len(inserted)}")

    # Verify: pre-existing text/refs/order untouched.
    r10_by = {(p["package_id"], b["block_id"]): b for p in r10["reader_packages"]
              for b in p["ordered_blocks"]}
    r11_by = {(p["package_id"], b["block_id"]): b for p in r11["reader_packages"]
              for b in p["ordered_blocks"]}
    for k, b10 in r10_by.items():
        b11 = r11_by.get(k)
        assert b11 is not None, f"lost {k}"
        assert b11["reader_text"] == b10["reader_text"], f"text changed {k}"
        assert b11["evidence_refs"] == b10["evidence_refs"], f"refs changed {k}"
        assert b11["block_type"] == b10["block_type"], f"type changed {k}"
    # Verify: old relative order preserved.
    for p10 in r10["reader_packages"]:
        old_ids = [b["block_id"] for b in p10["ordered_blocks"]]
        p11 = by_pid[p10["package_id"]]
        new_ids = [b["block_id"] for b in p11["ordered_blocks"] if b["block_id"] in old_ids]
        assert new_ids == old_ids, f"order changed {p10['package_id']}"
    # Verify: decks/headlines untouched.
    for p10 in r10["reader_packages"]:
        p11 = by_pid[p10["package_id"]]
        assert p11["deck"] == p10["deck"] and p11["headline"] == p10["headline"], \
            p10["package_id"]
    print(f"r11 integrity PASS: {len(r10_by)} pre-existing blocks byte-identical, "
          f"order preserved, decks/headlines untouched.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
