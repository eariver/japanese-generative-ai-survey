#!/usr/bin/env python3
"""TS-003 P02 bridge r9 — terminal validation (§15 items 1-14 + invariants).

Runs on FINAL worktree bytes. Exit 1 on any FAIL. Writes audit-r9.json.
"""
from __future__ import annotations
import glob
import hashlib
import json
import os
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/p02-detr-bridge-intake-r9-20261008"


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(65536), b""):
            h.update(c)
    return h.hexdigest()


def main() -> int:
    fails = []

    def check(name, ok, detail=""):
        print(("PASS" if ok else "FAIL"), "-", name, ("| " + detail if detail else ""))
        if not ok:
            fails.append(name)

    # ---- intake scope ----
    disc = [json.loads(l) for l in open(SRC / "discovery/discovery-v2.jsonl", encoding="utf-8")]
    new_recs = [r for r in disc if r["discovery_id"] in ("VM-D123", "VM-D124", "VM-D125")]
    check("§15.1 only bounded P02 family newly intaken",
          len(disc) == 125 and len(new_recs) == 3
          and all(r["provenance"]["obligation_ids"] == ["VM-O02"] for r in new_recs),
          f"discovery={len(disc)}")
    locs = {r["discovery_id"]: r["source"]["locator"] for r in new_recs}
    check("§15.1b exact locators",
          locs == {"VM-D123": "https://arxiv.org/abs/2010.04159",
                   "VM-D124": "https://arxiv.org/abs/2201.12329",
                   "VM-D125": "https://arxiv.org/abs/2203.01305"}, str(locs))
    check("§15.7 VM-D122 not reused",
          "VM-D122" not in {r["discovery_id"] for r in new_recs}
          and max(r["discovery_id"] for r in disc) == "VM-D125")

    # ---- evidence ----
    ev_acc = max(glob.glob(str(SRC / "evidence/v2/accepted/*/evidence-accepted.json")),
                 key=lambda p: os.stat(p).st_mtime)
    ev = json.load(open(ev_acc, encoding="utf-8"))
    by_did = {}
    for r in ev["results"]:
        for d in r["discovery_ids"]:
            by_did[d] = r
    for did, title_frag in (("VM-D123", "Deformable DETR"), ("VM-D124", "DAB-DETR"),
                            ("VM-D125", "DN-DETR")):
        r = by_did.get(did)
        _card_txt = ""
        if r is not None:
            _card_txt = Path(ev_acc).parent.joinpath("results", r["filename"]).read_text(encoding="utf-8")
        check(f"§15.{2 if did == 'VM-D123' else 3 if did == 'VM-D124' else 4} {did} primary Evidence",
              r is not None and r["status"] == "VERIFIED" and title_frag in _card_txt,
              (r["status"] if r else "missing") + "/" + (r["evidence_task_id"][-12:] if r else ""))
    st = Counter(r["status"] for r in ev["results"])
    check("evidence 124 = 119 VERIFIED / 5 PARTIAL",
          ev["result_count"] == 124 and dict(st) == {"VERIFIED": 119, "PARTIAL": 5},
          f"{ev['result_count']}/{dict(st)}")
    # DINO intact at claim level
    dino_new = by_did.get("VM-D011")
    dino_old = json.load(open(SRC / f"evidence/v2/accepted/1311b55593ecd4420193619bc60766828af0e2b9ebeffd45801e80080d93087d/results/task-73b035353dec1954a85d.json",
                               encoding="utf-8"))
    check("§15.5 DINO Evidence intact (claims byte-identical)",
          dino_new is not None and
          json.loads(subprocess.run(["git", "show", "HEAD:sources/SP-vision-multimodal-2026/evidence/v2/accepted/1311b55593ecd4420193619bc60766828af0e2b9ebeffd45801e80080d93087d/results/task-73b035353dec1954a85d.json"],
                                    cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8"))["claims"] ==
          json.loads(Path(ev_acc).parent.joinpath("results", dino_new["filename"]).read_text(encoding="utf-8"))["claims"])
    check("§15.6 no DINO-name collision (self-supervised DINO separate)",
          "self-supervised" in json.dumps(by_did.get("VM-D011"), ensure_ascii=False).lower()
          or "DINO detector" in json.dumps([c.get("text", "") for c in
                                            json.loads(Path(ev_acc).parent.joinpath("results", by_did["VM-D011"]["filename"]).read_text(encoding="utf-8"))["claims"]]))

    # ---- completeness ----
    comp = json.load(open(SRC / "profile-completeness-v2.json", encoding="utf-8"))
    ostat = Counter(o["status"] for o in comp["obligations"])
    check("completeness 14/2, obligations 16", dict(ostat) == {"SATISFIED": 14, "LIMITATION": 2}
          and len(comp["obligations"]) == 16, str(dict(ostat)))
    vmo02 = next(o for o in comp["obligations"] if o["obligation_id"] == "VM-O02")
    check("§15.7 VM-O02 recomputed (SATISFIED, 11 records, bridge rationale)",
          vmo02["status"] == "SATISFIED" and len(vmo02["discovery_ids"]) == 11
          and "DN-DETR" in vmo02["rationale"] and "DAB-DETR" in vmo02["rationale"]
          and "Deformable DETR" in vmo02["rationale"],
          f"{vmo02['status']}/{len(vmo02['discovery_ids'])}")
    others_same = True
    head_comp = json.loads(subprocess.run(["git", "show", "HEAD:sources/SP-vision-multimodal-2026/profile-completeness-v2.json"],
                                          cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8"))
    for o_new in comp["obligations"]:
        if o_new["obligation_id"] == "VM-O02":
            continue
        o_old = next(o for o in head_comp["obligations"] if o["obligation_id"] == o_new["obligation_id"])
        if o_new["status"] != o_old["status"] or o_new["rationale"] != o_old["rationale"]:
            others_same = False
    check("§15.8 unrelated obligations unchanged", others_same)

    # ---- architecture ----
    arch = json.load(open(SRC / "architecture-v2.json", encoding="utf-8"))
    check("architecture PROPOSED (not self-approved)",
          arch.get("status") == "PROPOSED"
          and arch.get("human_review", {}).get("reviewed_by") is None)
    check("architecture SHA differs from r8 (new candidate)",
          sha256_file(SRC / "architecture-v2.json") !=
          "56658960dff0269a89bf38d5b3027147dea7159f5c15337ff8a74d6ea7e4d773")
    pkgs = {p["package_id"]: p for p in arch["packages"]}
    head_arch = json.loads(subprocess.run(["git", "show", "HEAD:sources/SP-vision-multimodal-2026/architecture-v2.json"],
                                          cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8"))
    hpkgs = {p["package_id"]: p for p in head_arch["packages"]}
    others_arch_same = all(pkgs[pid] == hpkgs[pid] for pid in pkgs if pid != "P02")
    check("§15.9 other 15 packages architecturally unchanged", others_arch_same)
    p02 = pkgs["P02"]
    check("P02 placements",
          len(p02["primary_candidate_ids"]) == 8 and len(p02["supporting_candidate_ids"]) == 3)
    check("P02 must-cover explicit (7 requirements)",
          len(p02["must_cover_requirements"]) == 7
          and any("Deformable DETR bridge" in r for r in p02["must_cover_requirements"])
          and any("DAB-DETR bridge" in r for r in p02["must_cover_requirements"])
          and any("DN-DETR bridge" in r for r in p02["must_cover_requirements"])
          and any("convergence of DETR-successor" in r for r in p02["must_cover_requirements"]))

    # ---- selection ----
    sel = json.load(open(SRC / "candidate-selection-v2.json", encoding="utf-8"))
    check("selection 124/124 SELECTED",
          sel["summary"]["selected_count"] == 124 and len(sel["assignments"]) == 124)

    # ---- §15.10 no random expansion ----
    check("§15.10 no random Evidence expansion",
          ev["result_count"] == 124 and len(disc) == 125)

    # ---- §15.11 shared core ----
    core_roots = ["AGENTS.md", "config/", "schemas/", "scripts/", ".github/workflows/",
                  "docs/survey-production-core-v2-session-bootstrap.md",
                  "docs/survey-production-core-v2-sol-luna-review-governance.md"]
    raw = subprocess.run(["git", "status", "--porcelain=v1", "--"] + core_roots,
                         capture_output=True, text=True, cwd=str(ROOT)).stdout.strip()
    dirty = "\n".join(l for l in raw.splitlines() if "__pycache__" not in l).strip()
    check("§15.11 Shared Core unchanged", dirty == "", dirty[:300])

    # ---- §15.12 freeze ----
    cov = subprocess.run(["git", "status", "--porcelain=v1", "--", "specials/", "surveys/"],
                         capture_output=True, text=True, cwd=str(ROOT)).stdout.strip()
    check("§15.12 Coverage Freeze intact + exception recorded",
          cov == "" and (EDIR / "coverage-freeze-exception.md").exists(), cov[:200])

    # ---- §15.13/14 no draft rev6, no publication outputs ----
    check("§15.13 no Draft rev6 generated",
          not glob.glob(str(SRC / "draft/v2/packages/P02/draft-result.json")) or
          json.load(open(SRC / "draft/v2/packages/P02/draft-result.json", encoding="utf-8")).get("draft_version") == "fresh-121-r8-rev5")
    check("§15.14 no TeX/PDF/Preview/Freeze/Release started",
          subprocess.run(["git", "status", "--porcelain=v1", "--", str(SRC) + "/publication/"],
                         capture_output=True, text=True, cwd=str(ROOT)).stdout.strip() == "")

    # ---- lifecycle / gates ----
    state = json.load(open(SRC / "production-state.json", encoding="utf-8"))
    check("terminal: ARCHITECTURE_ESTABLISHED, gates pending, no approval",
          state["lifecycle_state"] == "ARCHITECTURE_ESTABLISHED"
          and state["human_gates"]["architecture_review"] == "pending"
          and state["human_gate_provenance"]["architecture_review"] is None)
    check("r8 history preserved (review + snapshot intact)",
          (SRC / "gates/reviews/architecture-r8.json").exists()
          and (SRC / "gates/reviews/approvals/architecture-r8.json").exists())
    check("active canonical approval superseded (file absent)",
          not (SRC / "gates/architecture-approval.json").exists())
    check("next_action is the pending Human Architecture Review",
          state.get("next_action") == "ARCHITECTURE_REVIEW",
          state.get("next_action"))

    (EDIR / "audit-r9.json").write_text(json.dumps(
        {"audit": "TS-003 P02 bridge r9 terminal (§15)", "failures": fails},
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("OVERALL:", "PASS" if not fails else f"FAIL {fails}")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
