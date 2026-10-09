#!/usr/bin/env python3
"""Build TS-003 edition-local reader/editorial authority r9.

CANONICAL_DRAFT_AUTHORITY = checkpointed r1 (ARCHITECTURE_ESTABLISHED.json).
READER_EDITORIAL_AUTHORITY = Sol-accepted r9 refinement (79d2b3e...), derived
from Sol-reviewed r2-r9 history + DRAFT_R9_BINDING terminology authority.

This authority is publication-layer only. It does NOT claim r9 remains
canonical Draft authority. Canonical Draft authority returns to checkpointed r1.
Reader wording is captured here for deterministic renderer use after restore.

Reproducible from exact Git history: r9 bytes are read via `git show
<commit>:<path>`, never from mutable workdir prose. Checkpoint SHAs are
cross-checked against r1 commit bytes.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = REPO / "sources/SP-vision-multimodal-2026"
EDITORIAL_DIR = SRC / "publication/editorial"
OUT = EDITORIAL_DIR / "reader-editorial-authority-r9.json"

ISSUE = "SP-vision-multimodal-2026"
CHECKPOINT_PATH = "sources/SP-vision-multimodal-2026/orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json"
CHECKPOINT_GIT_BLOB = "3c8024311d911f4e3a44e29859fc5cf481e0073e"
R1_COMMIT = "d1053e957d92cddd9d2759ec9713db59c66263ad"
R1_TREE = "d69fe46574d0d922e8a1e2c4c4a69e2719f4ddae"
R9_COMMIT = "79d2b3e291e10896ed616bd698abefc1e479ddbe"
R9_TREE = "4d96d07db9147b3c9a973a6f3bdc6b4cd09d8b53"
PUB_R3_COMMIT = "78b770fbabd4af29afe8a0342b747b01ae4b952b"
SOL_R3_COMMIT = "4d541ee6d8f3886f7bb6ef5e7d75e1ce13811633"
R3_PDF_SHA = "637877b879def1dc491b1b3d40a852cd209e22f02d57794697079a722f949795"
TERMINOLOGY_PATH = "sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md"
TERMINOLOGY_BLOB = "cf39a5860d64b5d85a3a382911680dcadaa954a1"
SOL_R9_PATH = "sources/SP-vision-multimodal-2026/execution/sol-draft-review-r9.md"

PACKAGES = ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B",
            "P08", "P09", "P10", "P11", "P12", "P13", "P14", "P15"]


def git_show(commit: str, rel: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{rel}"], cwd=REPO)


def git_rev(ref: str) -> str:
    return subprocess.check_output(["git", "rev-parse", ref], cwd=REPO, text=True).strip()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    # 1. Verify immutable checkpoint not rewritten.
    blob = subprocess.check_output(
        ["git", "hash-object", str(REPO / CHECKPOINT_PATH)], text=True).strip()
    assert blob == CHECKPOINT_GIT_BLOB, f"checkpoint blob drift: {blob}"
    checkpoint = json.loads((REPO / CHECKPOINT_PATH).read_text(encoding="utf-8"))
    assert checkpoint["issue_id"] == ISSUE
    assert checkpoint["implementation"]["repository_commit_sha"] == "1a588ff12384b4d5236d7e3860ee1cec937c14df", \
        "checkpoint implementation commit must remain 1a588ff (execution-contract authority, not restore source)"
    assert git_rev(R1_COMMIT) == R1_COMMIT
    assert git_rev(f"{R1_COMMIT}^{{tree}}") == R1_TREE
    assert git_rev(R9_COMMIT) == R9_COMMIT
    assert git_rev(f"{R9_COMMIT}^{{tree}}") == R9_TREE
    checkpoint_sha256 = sha256_bytes((REPO / CHECKPOINT_PATH).read_bytes())

    # 2. Extract checkpointed canonical SHAs.
    art_by_name = {a["name"]: a for a in checkpoint["artifacts"]}
    checkpoint_results = {}
    checkpoint_packages = {}
    for pid in PACKAGES:
        checkpoint_results[pid] = art_by_name[f"draft-result:{pid}"]["sha256"]
        checkpoint_packages[pid] = art_by_name[f"draft-package:{pid}"]["sha256"]
    checkpoint_synth_in = art_by_name["synthesis-input"]["sha256"]
    checkpoint_synth_out = art_by_name["synthesis-result"]["sha256"]

    # 3. Verify r1 commit bytes match checkpoint (canonical authority binding).
    for pid in PACKAGES:
        rel = f"sources/SP-vision-multimodal-2026/draft/v2/packages/{pid}/draft-result.json"
        b = git_show(R1_COMMIT, rel)
        assert sha256_bytes(b) == checkpoint_results[pid], f"r1 {pid} mismatch checkpoint"
        rel_pkg = f"sources/SP-vision-multimodal-2026/draft/v2/packages/{pid}/draft-package.json"
        b_pkg = git_show(R1_COMMIT, rel_pkg)
        assert sha256_bytes(b_pkg) == checkpoint_packages[pid], f"r1 package {pid} mismatch"
    for rel, exp in [
        ("sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-input.json", checkpoint_synth_in),
        ("sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-result.json", checkpoint_synth_out),
    ]:
        assert sha256_bytes(git_show(R1_COMMIT, rel)) == exp, f"r1 {rel} mismatch"

    # 4. Capture accepted r9 reader projections from immutable history.
    reader_packages = []
    for pid in PACKAGES:
        rel = f"sources/SP-vision-multimodal-2026/draft/v2/packages/{pid}/draft-result.json"
        raw = git_show(R9_COMMIT, rel)
        r9 = json.loads(raw.decode("utf-8"))
        assert r9["package_id"] == pid, pid
        assert r9["issue_id"] == ISSUE
        blocks = []
        for blk in r9["blocks"]:
            blocks.append({
                "block_id": blk["block_id"],
                "block_type": blk["block_type"],
                "reader_text": blk["text"],
                "reader_text_sha256": sha256_bytes(blk["text"].encode("utf-8")),
                "evidence_refs": blk.get("evidence_refs") or [],
            })
        reader_packages.append({
            "package_id": pid,
            "headline": r9["headline"],
            "headline_sha256": sha256_bytes(r9["headline"].encode("utf-8")),
            "deck": r9["deck"],
            "deck_sha256": sha256_bytes(r9["deck"].encode("utf-8")),
            "deck_evidence_refs": r9.get("deck_evidence_refs") or [],
            "ordered_blocks": blocks,
            "r9_file_sha256": sha256_bytes(raw),
            "r9_git_blob": subprocess.check_output(
                ["git", "rev-parse", f"{R9_COMMIT}:{rel}"], cwd=REPO, text=True).strip(),
            "canonical_r1_file_sha256": checkpoint_results[pid],
            "must_cover_coverage": r9.get("must_cover_coverage") or [],
            "boundary_dispositions": r9.get("boundary_dispositions") or [],
        })

    # 5. Accepted r9 synthesis for renderer.
    syn_raw = git_show(R9_COMMIT, "sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-result.json")
    syn = json.loads(syn_raw.decode("utf-8"))
    synth_in_raw = git_show(R9_COMMIT, "sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-input.json")
    reader_synthesis = {
        "r9_file_sha256": sha256_bytes(syn_raw),
        "r9_git_blob": subprocess.check_output(
            ["git", "rev-parse", f"{R9_COMMIT}:sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-result.json"],
            cwd=REPO, text=True).strip(),
        "canonical_r1_file_sha256": checkpoint_synth_out,
        "profile_payload": syn["profile_payload"],
        "synthesis_input_r9_sha256": sha256_bytes(synth_in_raw),
        "synthesis_input_canonical_r1_sha256": checkpoint_synth_in,
    }

    # 6. Terminology + Sol r9 + editorial history + publication r3.
    term_bytes = (REPO / TERMINOLOGY_PATH).read_bytes()
    term_blob_now = subprocess.check_output(["git", "hash-object", str(REPO / TERMINOLOGY_PATH)], text=True).strip()
    assert term_blob_now == TERMINOLOGY_BLOB, f"terminology blob drift: {term_blob_now}"
    sol_r9_bytes = (REPO / SOL_R9_PATH).read_bytes()
    # Editorial history: draft r1..r9 worker commits + Sol reviews r1..r9.
    draft_history = [
        {"version": "r1", "commit": "d1053e957d92cddd9d2759ec9713db59c66263ad",
         "subject": "TS-003 Draft r1: Human r2 APPROVED recorded, 16 packages drafted, language QA PASS_WITH_NOTES, DRAFT_COMPLETE"},
        {"version": "r2", "commit": "4a553c33385cb245d7239c116812999560165188",
         "subject": "TS-003 Draft r2: reader-surface repair (F1-F5), language QA PASS_WITH_NOTES, DRAFT_COMPLETE held"},
        {"version": "r3", "commit": "12f98c5945c1b2c049b52a1c7f64a78ccdd77512",
         "subject": "TS-003 Draft r3: cumulative terminology repair (Sol r2 F1-F5), map \u00a73.3 added, QA PASS_WITH_NOTES"},
        {"version": "r4", "commit": "f90f6000538437985b683edb1b2c4c33e2d067c5",
         "subject": "TS-003 Draft r4: cumulative terminology repair (Sol r3 F1-F6), QA PASS_WITH_NOTES"},
        {"version": "r5", "commit": "2979026987e11cd52cf278432d111e83a64c573b",
         "subject": "TS-003 Draft r5: final reader-surface cleanup (Sol r4 F1-F5), QA PASS_WITH_NOTES"},
        {"version": "r6", "commit": "a345358f568e5ab7b55798c1f8469378abbd5783",
         "subject": "TS-003 Draft r6: P09 terminology closure (Sol r5 F1-F4), QA PASS_WITH_NOTES"},
        {"version": "r7", "commit": "59f841121271d68154f9173d0826791215b261d4",
         "subject": "TS-003 Draft r7: preferred-terminology conformance (Sol pub-review r1), QA PASS_WITH_NOTES"},
        {"version": "r8", "commit": "45e1aae18883983bfb852ac95bfd78d6a4d2fcf1",
         "subject": "TS-003 Draft r8: bidirectional terminology repair (Sol r7 F1-F6), QA PASS_WITH_NOTES"},
        {"version": "r9", "commit": R9_COMMIT,
         "subject": "TS-003 Draft r9: final micro-cleanup (Sol r8, 4 edits), QA PASS_WITH_NOTES"},
    ]
    for row in draft_history:
        assert git_rev(row["commit"]) == row["commit"], row
        row["tree"] = git_rev(f"{row['commit']}^{{tree}}")
    sol_history = []
    for v in ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9"]:
        p = f"sources/SP-vision-multimodal-2026/execution/sol-draft-review-{v}.md"
        blob_now = subprocess.check_output(["git", "hash-object", str(REPO / p)], text=True).strip()
        sol_history.append({
            "version": v,
            "path": p,
            "git_blob_sha": blob_now,
            "sha256": sha256_bytes((REPO / p).read_bytes()),
        })
    arch = json.loads((SRC / "architecture-v2.json").read_text(encoding="utf-8"))
    ordered = sorted(arch["packages"], key=lambda r: (r["drafting_order"], r["package_id"]))
    arch_order = [p["package_id"] for p in ordered]
    assert arch_order == PACKAGES, arch_order

    authority = {
        "schema_version": "1.0",
        "issue_id": ISSUE,
        "semantic_labels": {
            "CANONICAL_DRAFT_AUTHORITY": "checkpointed r1 via ARCHITECTURE_ESTABLISHED.json (DRAFT_COMPLETE checkpoint, immutable)",
            "READER_EDITORIAL_AUTHORITY": "Sol-accepted r9 refinement as edition-local publication-layer transform (NOT canonical Draft authority)",
            "warning": "r9 wording must be consumed only via this reader/editorial authority after canonical restore; never claim r9 remains canonical Draft authority.",
        },
        "canonical_draft_authority": {
            "label": "CANONICAL_DRAFT_AUTHORITY = checkpointed r1",
            "checkpoint_path": CHECKPOINT_PATH,
            "checkpoint_git_blob": CHECKPOINT_GIT_BLOB,
            "checkpoint_sha256": checkpoint_sha256,
            "source_commit": R1_COMMIT,
            "source_tree": R1_TREE,
            "source_message": "TS-003 Draft r1: Human r2 APPROVED recorded, 16 packages drafted, language QA PASS_WITH_NOTES, DRAFT_COMPLETE",
            "implementation_commit_note": "ARCHITECTURE_ESTABLISHED.json implementation 1a588ff... is execution-contract authority, not Draft-bytes restore source; restore source is d1053e957...",
            "checkpointed_draft_result_sha256": checkpoint_results,
            "checkpointed_draft_package_sha256": checkpoint_packages,
            "checkpointed_synthesis_input_sha256": checkpoint_synth_in,
            "checkpointed_synthesis_result_sha256": checkpoint_synth_out,
        },
        "reader_editorial_authority": {
            "label": "READER_EDITORIAL_AUTHORITY = Sol-accepted r9 refinement",
            "accepted_r9_commit": R9_COMMIT,
            "accepted_r9_tree": R9_TREE,
            "formal_sol_review": {
                "path": SOL_R9_PATH,
                "sha256": sha256_bytes(sol_r9_bytes),
                "decision": "PASS",
                "terminal": "TS-003 SOL_DRAFT_REVIEW_R9_PASS / READER_PROSE_AUTHORITY_ACCEPTED",
            },
            "terminology_authority": {
                "path": TERMINOLOGY_PATH,
                "git_blob": TERMINOLOGY_BLOB,
                "sha256": sha256_bytes(term_bytes),
                "status": "DRAFT_R9_BINDING",
            },
            "editorial_history": {
                "draft_commits_r1_r9": draft_history,
                "sol_reviews_r1_r9": sol_history,
                "note": "r2-r9 transforms are Sol-reviewed editorial refinements; paragraph consolidation / reference redistribution in P07A/P07B/P15 preserved unique Evidence authority sets (validator re-checks, never assumes).",
            },
            "accepted_publication_r3": {
                "worker_commit": PUB_R3_COMMIT,
                "worker_tree": git_rev(f"{PUB_R3_COMMIT}^{{tree}}"),
                "sol_review_commit": SOL_R3_COMMIT,
                "sol_review_tree": git_rev(f"{SOL_R3_COMMIT}^{{tree}}"),
                "target_pdf_sha256": R3_PDF_SHA,
                "target_pdf_path": "surveys/special/vision-multimodal-2026/main.pdf",
                "target_pdf_bytes": 684804,
                "target_pdf_pages": 38,
            },
        },
        "architecture_package_order": arch_order,
        "reader_packages": reader_packages,
        "reader_synthesis": reader_synthesis,
        "renderer_binding": {
            "canonical_provenance_source": "checkpointed r1 bytes (integrity/provenance only, never reader wording)",
            "reader_wording_source": "this authority (reader-editorial-authority-r9.json) + accepted Evidence for bibliography/citation resolution + approved Architecture/Profile",
            "forbidden": "must not read restored r1 Draft Result prose as final reader wording; must not claim TeX identical to canonical Draft r9",
        },
        "provenance": {
            "built_from": f"git history {R9_COMMIT} + {CHECKPOINT_PATH}@{CHECKPOINT_GIT_BLOB} + {TERMINOLOGY_PATH}@{TERMINOLOGY_BLOB}",
            "reproducible": "re-run this script from exact Git history; workdir prose never used as capture source",
            "generator": "sources/SP-vision-multimodal-2026/publication/editorial/build_reader_editorial_authority_r9.py",
        },
    }
    EDITORIAL_DIR.mkdir(parents=True, exist_ok=True)
    (OUT).write_text(json.dumps(authority, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO)} packages={len(reader_packages)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
