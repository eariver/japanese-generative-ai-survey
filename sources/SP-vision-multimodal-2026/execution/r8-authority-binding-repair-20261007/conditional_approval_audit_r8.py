#!/usr/bin/env python3
"""§8/§22 conditional-approval audit on the ACTUAL regenerated r7 Architecture.

Fail-closed: any FAIL -> no r7 APPROVED, STOP with r7 PENDING.
Writes conditional-approval-audit-r7.json.
"""
from __future__ import annotations
import json
import subprocess
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/r8-authority-binding-repair-20261007"


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
    new_mx = json.loads((SRC / "candidate-matrix-v2.json").read_text(encoding="utf-8"))
    ev_acc = max((SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                 key=lambda p: p.stat().st_mtime)
    ev = json.loads(ev_acc.read_text(encoding="utf-8"))
    import collections
    statuses = collections.Counter(r["status"] for r in ev["results"])

    check("16 packages", len(new_arch["packages"]) == 16, str(len(new_arch["packages"])))
    check("package order unchanged",
          [p["package_id"] for p in new_arch["packages"]] == [p["package_id"] for p in head_arch["packages"]])
    check("page plan unchanged", new_arch.get("page_plan") == head_arch.get("page_plan"))
    check("target/max unchanged",
          new_arch["page_plan"].get("target_pages") == 112 and new_arch["page_plan"].get("max_pages") == 120,
          f"{new_arch['page_plan'].get('target_pages')}/{new_arch['page_plan'].get('max_pages')}")
    check("Evidence 121", ev["result_count"] == 121, str(ev["result_count"]))
    check("116/5 split", dict(statuses) == {"VERIFIED": 116, "PARTIAL": 5}, str(dict(statuses)))
    check("Selection 121", len(new_sel["assignments"]) == 121)
    check("Completeness 14/2",
          collections.Counter(o["status"] for o in new_comp["obligations"]) == {"SATISFIED": 14, "LIMITATION": 2})
    pmap = new_arch["publication_extensions"]["p15_cross_package_synthesis_map"]
    ids40 = {i for v in pmap.values() for i in v}
    check("P15 40 IDs", len(ids40) == 40, str(len(ids40)))
    check("P15 40-ID set unchanged",
          ids40 == {i for v in head_arch["publication_extensions"]["p15_cross_package_synthesis_map"].values() for i in v})
    check("P15 map keys unchanged",
          list(pmap) == list(head_arch["publication_extensions"]["p15_cross_package_synthesis_map"]))
    disc_n = sum(1 for _ in open(SRC / "discovery/discovery-v2.jsonl", encoding="utf-8"))
    check("Coverage Freeze (122/121/121, no D122)",
          disc_n == 122 and ev["result_count"] == 121 and len(new_sel["assignments"]) == 121 and
          "VM-D122" not in json.dumps(new_arch, ensure_ascii=False),
          f"disc={disc_n}")

    # exactly two intended Evidence semantic changes
    old_acc = json.loads(_head(f"{SRC.relative_to(ROOT)}/evidence/v2/accepted/66c9932ebc23a3c04df6c1dd2ba65fb300c7e090343e5062487160f00682c77f/evidence-accepted.json"))
    old_by_task = {r["evidence_task_id"]: r["sha256"] for r in old_acc["results"]}
    new_by_task = {r["evidence_task_id"]: r["sha256"] for r in ev["results"]}
    changed = sorted(t for t in old_by_task if old_by_task[t] != new_by_task[t])
    check("exactly one Evidence change (VM-D039)",
          changed == ["evidence:SP-vision-multimodal-2026:20d1ebc2759ddd61"],
          str([t.split(':')[-1][:8] for t in changed]))

    blob_new = json.dumps(new_arch, ensure_ascii=False)
    check("CLIP unit corrected (no 1.28M labels)",
          "1.28M labels" not in blob_new)
    check("P11 SAM3 wording corrected",
          "concept-prompted video grounding and memory-based tracking are supporting" in blob_new and
          "stored-timeline on-demand navigation remains" in blob_new)
    check("P07B must-cover unchanged",
          "SigLIP 2 localization transfer and SAM 3 concept grounding extend" in blob_new)
    # r6 semantics preserved
    for needle in ("p09_measurement_provenance", "author/developer self-reported",
                   "VQA-family accuracy can exploit question/answer priors",
                   "not a paper-measured contamination rate"):
        check(f"r6/r7 semantic preserved: {needle[:30]}", needle in blob_new)
    pkgs_old = {p["package_id"]: p for p in head_arch["packages"]}
    pkgs_new = {p["package_id"]: p for p in new_arch["packages"]}
    changed_pkgs = sorted(pid for pid in pkgs_old if pkgs_old[pid] != pkgs_new[pid])
    check("changed packages exactly P11", changed_pkgs == ["P11"], str(changed_pkgs))
    check("no other thesis/purpose/lineage change",
          head_arch["editorial_thesis"] == new_arch["editorial_thesis"] and
          head_arch["architecture_goals"] == new_arch["architecture_goals"] and
          all(pkgs_old[pid]["title"] == pkgs_new[pid]["title"] and
              pkgs_old[pid]["purpose"] == pkgs_new[pid]["purpose"] and
              pkgs_old[pid]["primary_candidate_ids"] == pkgs_new[pid]["primary_candidate_ids"] and
              pkgs_old[pid]["supporting_candidate_ids"] == pkgs_new[pid]["supporting_candidate_ids"] and
              pkgs_old[pid]["drafting_order"] == pkgs_new[pid]["drafting_order"]
              for pid in pkgs_old))
    check("matrix 121 rows", new_mx["summary"]["candidate_count"] == 121)
    check("no disposition change",
          [(a["candidate_id"], a["disposition"]) for a in new_sel["assignments"]] ==
          [(a["candidate_id"], a["disposition"]) for a in head_sel["assignments"]])
    head_comp = json.loads(_head(f"{SRC.relative_to(ROOT)}/profile-completeness-v2.json"))
    check("completeness semantics identical to HEAD (obligations/residual/closure)",
          head_comp["obligations"] == new_comp["obligations"] and
          head_comp.get("residual_limitations") == new_comp.get("residual_limitations") and
          head_comp.get("closure") == new_comp.get("closure"))
    st = subprocess.run(["git", "status", "--porcelain=v1"], cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8")
    shared_touched = [l for l in st.splitlines() if l.strip() and
                      any(l.split(None, 1)[1].startswith(p) for p in
                          ("AGENTS.md", "config/", "schemas/", "scripts/", ".github/workflows/", "docs/survey-production-core-v2-"))]
    check("shared Core unchanged", not shared_touched, "; ".join(shared_touched))

    overall = all(v["pass"] for v in results.values())
    (EDIR / "conditional-approval-audit-r8.json").write_text(
        json.dumps({"audit": "conditional Human Architecture r8 (§8/§24)",
                    "overall_pass": overall,
                    "conditions": results,
                    "architecture_sha256": __import__("hashlib").sha256((SRC / "architecture-v2.json").read_bytes()).hexdigest()},
                   ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("OVERALL:", "PASS" if overall else "FAIL")
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())
