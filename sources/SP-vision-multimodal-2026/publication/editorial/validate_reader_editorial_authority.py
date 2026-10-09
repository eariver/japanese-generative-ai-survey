#!/usr/bin/env python3
"""Validate TS-003 reader/editorial authority r9 against canonical r1.

Independently re-checks (never assumes Sol read-only findings):
- 16 draft-package.json unchanged (r1 == r9 bytes, checkpoint-bound)
- For all packages: no newly introduced Evidence ref, no newly introduced
  source (evidence_task_id sets equal), no package identity change,
  CLAIM_BOUNDARY block present, limitation authority preserved
  (LIMITATION evidence_id sets equal), Architecture package order unchanged.
- For P07A/P07B/P15: unique Evidence authority sets unchanged despite
  paragraph consolidation / reference redistribution.
- All r9 reader projections in authority match immutable r9 commit bytes.

Deterministic structure/provenance only; semantic equivalence remains subject
to fresh semantic/editorial + Sol exact-PDF review.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = REPO / "sources/SP-vision-multimodal-2026"
AUTH = SRC / "publication/editorial/reader-editorial-authority-r9.json"

R1 = "d1053e957d92cddd9d2759ec9713db59c66263ad"
R9 = "79d2b3e291e10896ed616bd698abefc1e479ddbe"
PACKAGES = ["P01", "P02", "P03", "P04", "P05", "P06", "P07A", "P07B",
            "P08", "P09", "P10", "P11", "P12", "P13", "P14", "P15"]


def show(commit, rel):
    return subprocess.check_output(["git", "show", f"{commit}:{rel}"], cwd=REPO)


def ev_all(res):
    s = set()
    for ref in (res.get("deck_evidence_refs") or []):
        s.add((ref["evidence_task_id"], ref["evidence_id"], ref.get("kind")))
    for b in res["blocks"]:
        for ref in (b.get("evidence_refs") or []):
            s.add((ref["evidence_task_id"], ref["evidence_id"], ref.get("kind")))
    return s


def ev_task_set(res):
    s = set()
    for ref in (res.get("deck_evidence_refs") or []):
        s.add(ref["evidence_task_id"])
    for b in res["blocks"]:
        for ref in (b.get("evidence_refs") or []):
            s.add(ref["evidence_task_id"])
    return s


def lim_set(res):
    s = set()
    for b in res["blocks"]:
        if b["block_type"] == "CLAIM_BOUNDARY":
            for ref in (b.get("evidence_refs") or []):
                s.add((ref["evidence_task_id"], ref["evidence_id"]))
    return s


def main() -> int:
    auth = json.loads(AUTH.read_text(encoding="utf-8"))
    assert auth["issue_id"] == "SP-vision-multimodal-2026"
    assert auth["semantic_labels"]["CANONICAL_DRAFT_AUTHORITY"].startswith("checkpointed r1")
    assert "never claim r9 remains canonical" in auth["semantic_labels"]["warning"]
    checkpoint = json.loads((REPO / auth["canonical_draft_authority"]["checkpoint_path"]).read_text(encoding="utf-8"))
    failures = []

    # Packages unchanged.
    for pid in PACKAGES:
        rel = f"sources/SP-vision-multimodal-2026/draft/v2/packages/{pid}/draft-package.json"
        r1b = show(R1, rel)
        r9b = show(R9, rel)
        if r1b != r9b:
            failures.append(f"{pid} package bytes differ r1 vs r9")
        exp = auth["canonical_draft_authority"]["checkpointed_draft_package_sha256"][pid]
        if hashlib.sha256(r1b).hexdigest() != exp:
            failures.append(f"{pid} package r1 != checkpoint")

    # Per-package Evidence / identity / boundary checks.
    by_pid = {p["package_id"]: p for p in auth["reader_packages"]}
    for pid in PACKAGES:
        rel = f"sources/SP-vision-multimodal-2026/draft/v2/packages/{pid}/draft-result.json"
        r1 = json.loads(show(R1, rel).decode("utf-8"))
        r9 = json.loads(show(R9, rel).decode("utf-8"))
        # Authority capture fidelity.
        proj = by_pid[pid]
        if proj["headline"] != r9["headline"]:
            failures.append(f"{pid} headline not bound to r9")
        if proj["deck"] != r9["deck"]:
            failures.append(f"{pid} deck not bound to r9")
        if len(proj["ordered_blocks"]) != len(r9["blocks"]):
            failures.append(f"{pid} block count {len(proj['ordered_blocks'])} != r9 {len(r9['blocks'])}")
        for pb, rb in zip(proj["ordered_blocks"], r9["blocks"]):
            if pb["block_id"] != rb["block_id"] or pb["block_type"] != rb["block_type"] or pb["reader_text"] != rb["text"]:
                failures.append(f"{pid} {rb['block_id']} projection mismatch")
        # No package identity change.
        if r1["package_id"] != r9["package_id"]:
            failures.append(f"{pid} package_id changed")
        # No new Evidence ref / source.
        if ev_task_set(r9) != ev_task_set(r1):
            failures.append(f"{pid} evidence_task_id set changed: new={sorted(ev_task_set(r9)-ev_task_set(r1))} lost={sorted(ev_task_set(r1)-ev_task_set(r9))}")
        if ev_all(r9) != ev_all(r1):
            failures.append(f"{pid} full Evidence ref set changed")
        # CLAIM_BOUNDARY preserved (at least one, limitation refs preserved).
        b1 = [b for b in r1["blocks"] if b["block_type"] == "CLAIM_BOUNDARY"]
        b9 = [b for b in r9["blocks"] if b["block_type"] == "CLAIM_BOUNDARY"]
        if len(b1) == 0 or len(b9) == 0:
            failures.append(f"{pid} missing CLAIM_BOUNDARY")
        if lim_set(r9) != lim_set(r1):
            failures.append(f"{pid} LIMITATION authority changed")
        # must_cover requirements identical (Architecture coverage anchor).
        if [c["requirement"] for c in r1.get("must_cover_coverage", [])] != [c["requirement"] for c in r9.get("must_cover_coverage", [])]:
            failures.append(f"{pid} must_cover requirements changed")

    # Architecture order unchanged.
    arch = json.loads((SRC / "architecture-v2.json").read_text(encoding="utf-8"))
    ordered = sorted(arch["packages"], key=lambda r: (r["drafting_order"], r["package_id"]))
    if [p["package_id"] for p in ordered] != PACKAGES:
        failures.append("Architecture package order changed")
    if auth["architecture_package_order"] != PACKAGES:
        failures.append("authority Arch order wrong")

    # Synthesis capture fidelity.
    syn_r9 = json.loads(show(R9, "sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-result.json").decode("utf-8"))
    if auth["reader_synthesis"]["profile_payload"] != syn_r9["profile_payload"]:
        failures.append("synthesis payload not bound to r9")

    # Explicit P07A/P07B/P15 unique-set re-check (consolidation cases).
    for pid in ["P07A", "P07B", "P15"]:
        rel = f"sources/SP-vision-multimodal-2026/draft/v2/packages/{pid}/draft-result.json"
        r1 = json.loads(show(R1, rel).decode("utf-8"))
        r9 = json.loads(show(R9, rel).decode("utf-8"))
        if ev_task_set(r1) != ev_task_set(r9):
            failures.append(f"{pid} consolidation changed unique Evidence set")

    if failures:
        print("VALIDATION FAIL:")
        for f in failures:
            print(" -", f)
        return 1
    print(f"reader-editorial authority validation PASS: 16/16 packages unchanged; "
          f"16/16 Evidence sets bounded; limitations preserved; Arch order intact; "
          f"projections bind {R9[:7]} bytes; canonical remains r1 {R1[:7]}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
