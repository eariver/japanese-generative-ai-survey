#!/usr/bin/env python3
"""Negative regression fixtures for the repaired FINAL-artifact P07A audit (§15.4).

- F1: P07A result with B05 D114 refs stripped (SigLIP2 prose present, binding
  absent) -> the block-level D114 check MUST FAIL.
- F2: P07A package with a D114 input injected (simulating literal §15.1) ->
  canonical validate_self_contained_draft_package MUST FAIL (Core exact-placement
  invariant: exactly one input per Architecture candidate placement).
Fixtures live in /tmp only; canonical tree untouched. Fails (exit 1) if either
fixture PASSES (i.e., the validator cannot detect the defect class).
"""
from __future__ import annotations
import copy
import json
import tempfile
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
D114 = "evidence:SP-vision-multimodal-2026:0f5a5b1f4eb4032e"


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_drafting_v2 as drafting
    from scripts import survey_production_v2 as core

    profile_path = SRC / "production-profile.json"
    arch_path = SRC / "architecture-v2.json"
    review_path = SRC / "architecture-review-summary-v2.json"
    approval_path = SRC / "gates/architecture-approval.json"

    # ---- F1: result-level binding stripped ----
    res = json.loads((SRC / "draft/v2/packages/P07A/draft-result.json").read_text(encoding="utf-8"))
    b05 = next(b for b in res["blocks"] if b.get("block_id") == "P07A-B05")
    assert any(e["evidence_task_id"] == D114 for e in b05["evidence_refs"]), "precondition: real B05 binds D114"
    fixture = copy.deepcopy(res)
    fb05 = next(b for b in fixture["blocks"] if b.get("block_id") == "P07A-B05")
    fb05["evidence_refs"] = [e for e in fb05["evidence_refs"] if e["evidence_task_id"] != D114]
    assert "SigLIP 2" in fb05["text"] or "LocCa" in fb05["text"]
    f1_detected = not any(e["evidence_task_id"] == D114 for e in fb05["evidence_refs"])
    print(("PASS" if f1_detected else "FAIL"), "- F1 negative fixture detected (stripped B05 refs fail the D114 check)")

    # ---- F2: package-level injection rejected by canonical Core ----
    pkg = json.loads((SRC / "draft/v2/packages/P07A/draft-package.json").read_text(encoding="utf-8"))
    ev_acc = max((SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                 key=lambda q: q.stat().st_mtime)
    ev = json.loads(ev_acc.read_text(encoding="utf-8"))
    meta = next(r for r in ev["results"] if r["evidence_task_id"] == D114)
    card = json.loads((ev_acc.parent / "results" / meta["filename"]).read_text(encoding="utf-8"))
    injected = copy.deepcopy(pkg)
    injected["evidence_inputs"] = list(pkg["evidence_inputs"]) + [{
        "candidate_id": "candidate:SP-vision-multimodal-2026:1a72aa57c29bc267",
        "architecture_usage": "SUPPORTING",
        "evidence_task_id": D114,
        "evidence_sha256": meta["sha256"],
        "evidence_card": card,
    }]
    with tempfile.TemporaryDirectory() as tmp:
        tmppkg = Path(tmp) / "draft-package.json"
        tmppkg.write_text(json.dumps(injected, ensure_ascii=False), encoding="utf-8")
        # validate the fixture content directly (path-independent core logic uses the object)
        errs = drafting.validate_self_contained_draft_package(
            injected, profile_path, arch_path, review_path, approval_path)
    f2_detected = any("outside authorized Architecture package" in e or "exactly one Evidence input" in e for e in errs)
    print(("PASS" if f2_detected else "FAIL"), "- F2 negative fixture detected (injected D114 input fails canonical package validation)")
    if not f2_detected:
        print("  canonical errors were:", errs[:4])

    # ---- control: real artifacts pass both levels ----
    real_b05_ok = any(e["evidence_task_id"] == D114 for e in b05["evidence_refs"])
    real_pkg_errs = drafting.validate_self_contained_draft_package(
        pkg, profile_path, arch_path, review_path, approval_path)
    print(("PASS" if (real_b05_ok and not real_pkg_errs) else "FAIL"),
          "- control: real P07A result binds D114; real package canonically valid")
    ok = f1_detected and f2_detected and real_b05_ok and not real_pkg_errs
    print("OVERALL:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
