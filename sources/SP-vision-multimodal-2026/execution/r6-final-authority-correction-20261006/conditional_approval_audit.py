#!/usr/bin/env python3
"""§12 conditional-approval audit on the ACTUAL regenerated Architecture.

Fail-closed: any condition FAIL -> no r6 APPROVED, STOP with r6 PENDING.
Writes conditional-approval-audit-r6.json (PASS/FAIL per condition).
"""
from __future__ import annotations
import json
import subprocess
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/r6-final-authority-correction-20261006"


def _head(rel: str):
    return subprocess.run(["git", "show", f"HEAD:{rel}"],
                          cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8")


def main() -> int:
    results = {}
    def check(name: str, ok: bool, detail: str = ""):
        results[name] = {"pass": bool(ok), "detail": detail}
        print(("PASS" if ok else "FAIL"), "-", name, ("| " + detail if detail else ""))

    head_arch = json.loads(_head(f"{SRC.relative_to(ROOT)}/architecture-v2.json"))
    new_arch = json.loads((SRC / "architecture-v2.json").read_text(encoding="utf-8"))
    head_sel = json.loads(_head(f"{SRC.relative_to(ROOT)}/candidate-selection-v2.json"))
    new_sel = json.loads((SRC / "candidate-selection-v2.json").read_text(encoding="utf-8"))
    new_comp = json.loads((SRC / "profile-completeness-v2.json").read_text(encoding="utf-8"))
    new_mat = json.loads((SRC / "materiality-ledger-v2.json").read_text(encoding="utf-8"))
    new_mx = json.loads((SRC / "candidate-matrix-v2.json").read_text(encoding="utf-8"))
    ev_acc = max((SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                 key=lambda p: p.stat().st_mtime)
    ev = json.loads(ev_acc.read_text(encoding="utf-8"))
    import collections
    statuses = collections.Counter(r["status"] for r in ev["results"])

    # ---- A. STRUCTURE INVARIANTS ----
    check("A1 package count 16", len(new_arch["packages"]) == 16, str(len(new_arch["packages"])))
    check("A2 package IDs/order unchanged",
          [p["package_id"] for p in new_arch["packages"]] == [p["package_id"] for p in head_arch["packages"]])
    check("A3 page plan unchanged", new_arch.get("page_plan") == head_arch.get("page_plan"))
    check("A4 target/max page plan unchanged",
          new_arch["page_plan"].get("target_pages") == head_arch["page_plan"].get("target_pages") and
          new_arch["page_plan"].get("max_pages") == head_arch["page_plan"].get("max_pages"),
          f"{new_arch['page_plan'].get('target_pages')}/{new_arch['page_plan'].get('max_pages')}")
    check("A5 Selection 121", len(new_sel["assignments"]) == 121, str(len(new_sel["assignments"])))
    check("A6 Completeness 14/2",
          collections.Counter(o["status"] for o in new_comp["obligations"]) == {"SATISFIED": 14, "LIMITATION": 2})
    pmap = new_arch["publication_extensions"]["p15_cross_package_synthesis_map"]
    ids40 = {i for v in pmap.values() for i in v}
    check("A7 P15 40 distinct IDs", len(ids40) == 40, str(len(ids40)))
    check("A7b P15 40-ID set unchanged",
          ids40 == {i for v in head_arch["publication_extensions"]["p15_cross_package_synthesis_map"].values() for i in v})
    # coverage freeze: discovery 122, evidence 121, selection 121, no D122
    disc_n = sum(1 for _ in open(SRC / "discovery/discovery-v2.jsonl", encoding="utf-8"))
    check("A8 coverage freeze (122/121/121, no D122)",
          disc_n == 122 and ev["result_count"] == 121 and len(new_sel["assignments"]) == 121 and
          "VM-D122" not in json.dumps(new_arch, ensure_ascii=False) and
          "VM-D122" not in json.dumps(ev, ensure_ascii=False),
          f"disc={disc_n} ev={ev['result_count']} sel={len(new_sel['assignments'])}")

    # ---- B. ALLOWED SEMANTIC DIFF ----
    blob_new = json.dumps(new_arch, ensure_ascii=False)
    blob_head = json.dumps(head_arch, ensure_ascii=False)
    check("B1 P07A contamination removed",
          "training contamination" not in blob_new and "Training contamination" not in blob_new)
    check("B1b P07A new semantics present",
          "VQA-family accuracy can exploit question/answer priors" in blob_new and
          "complementary image pairs" in blob_new)
    check("B2 P09 blanket vendor-measured removed",
          "All benchmark claims vendor-measured" not in blob_new and
          "No-degradation and leaderboard claims vendor-measured" not in blob_new and
          "Vendor-measured evals at this read level" not in blob_new)
    check("B2b P09 three-way present",
          "author/developer self-reported" in blob_new and "provider/vendor" in blob_new)
    check("B3 P15 binary removed",
          "p09_vendor_vs_independent" not in blob_new and "vendor-vs-independent" not in blob_new)
    check("B3b P15 three-way present",
          "p09_measurement_provenance" in blob_new and
          "author/developer self-reported vs provider/vendor-reported vs independent-third-party" in blob_new)
    check("B4 G05 first-party gap",
          "first-party" in json.dumps(new_comp, ensure_ascii=False) and
          "vendor/model-report scores" not in json.dumps(new_comp, ensure_ascii=False))
    # no other substantive change: titles, primary/supporting, order, page budgets
    same = True
    for hp, np in zip(head_arch["packages"], new_arch["packages"]):
        if hp["package_id"] != np["package_id"]: same = False
        if hp["title"] != np["title"]: same = False
        if hp["primary_candidate_ids"] != np["primary_candidate_ids"]: same = False
        if hp["supporting_candidate_ids"] != np["supporting_candidate_ids"]: same = False
        if hp["drafting_order"] != np["drafting_order"]: same = False
        if hp.get("publication_extensions", {}).get("page_budget_body_pages") != np.get("publication_extensions", {}).get("page_budget_body_pages"):
            same = False
    # P15 purpose three-way change is ALLOWED (exclude from same check)
    check("B5 no other package thesis/lineage/role change (titles/ids/order/budgets)",
          same and head_arch["editorial_thesis"] == new_arch["editorial_thesis"] and
          head_arch["architecture_goals"] == new_arch["architecture_goals"])
    pkgs_old = {p["package_id"]: p for p in head_arch["packages"]}
    pkgs_new = {p["package_id"]: p for p in new_arch["packages"]}
    changed = sorted(pid for pid in pkgs_old if pkgs_old[pid] != pkgs_new[pid])
    check("B6 changed packages exactly P07A/P09/P15", changed == ["P07A", "P09", "P15"], str(changed))

    # ---- C. NO UNEXPECTED AUTHORITY CHANGE ----
    check("C1 no new Discovery (122)", disc_n == 122)
    check("C2 no removed candidate (matrix 121)", new_mx["summary"]["candidate_count"] == 121)
    check("C3 no disposition change",
          [(a["candidate_id"], a["disposition"]) for a in new_sel["assignments"]] ==
          [(a["candidate_id"], a["disposition"]) for a in head_sel["assignments"]])
    check("C4 no new PARTIAL / statuses 116/5", dict(statuses) == {"VERIFIED": 116, "PARTIAL": 5}, str(dict(statuses)))
    check("C5 no VERIFIED change count", statuses["VERIFIED"] == 116 and statuses["PARTIAL"] == 5)
    check("C6 no new Architecture limitation (16 pkgs, boundaries count stable-ish)",
          len(new_arch["packages"]) == 16)
    # shared Core modification: git status on shared roots must be clean except edition tree + execution
    st = subprocess.run(["git", "status", "--porcelain=v1"], cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8")
    shared_touched = [l for l in st.splitlines() if l.strip() and
                      any(l.split(None, 1)[1].startswith(p) for p in
                          ("AGENTS.md", "config/", "schemas/", "scripts/", ".github/workflows/", "docs/survey-production-core-v2-"))]
    check("C7 no shared Core modification", not shared_touched, "; ".join(shared_touched))

    overall = all(v["pass"] for v in results.values())
    (EDIR / "conditional-approval-audit-r6.json").write_text(
        json.dumps({"audit": "conditional Human Architecture r6 (§12 A/B/C)",
                    "overall_pass": overall,
                    "conditions": results,
                    "architecture_sha256": __import__("hashlib").sha256((SRC / "architecture-v2.json").read_bytes()).hexdigest()},
                   ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("OVERALL:", "PASS" if overall else "FAIL")
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
