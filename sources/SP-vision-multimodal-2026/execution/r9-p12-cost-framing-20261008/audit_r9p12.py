#!/usr/bin/env python3
"""TS-003 r9 P12 correction — terminal validation (§15 items 1-22).

Runs on FINAL worktree bytes. Exit 1 on any FAIL. Writes audit-r9p12.json.
"""
from __future__ import annotations
import glob
import hashlib
import json
import os
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/r9-p12-cost-framing-20261008"

MC_OLD = "Screenshot-loop token costs via TS-001 vocabulary; safety audits as eval metadata only"


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

    arch = json.load(open(SRC / "architecture-v2.json", encoding="utf-8"))
    head_arch = json.loads(subprocess.run(["git", "show", "HEAD:sources/SP-vision-multimodal-2026/architecture-v2.json"],
                                          cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8"))
    pkgs = {p["package_id"]: p for p in arch["packages"]}
    hpkgs = {p["package_id"]: p for p in head_arch["packages"]}
    p12 = pkgs["P12"]

    check("§15.1 old Screenshot-loop requirement gone",
          MC_OLD not in p12["must_cover_requirements"]
          and MC_OLD not in json.dumps(arch, ensure_ascii=False))
    mc = [r for r in p12["must_cover_requirements"] if "state-management burden" in r]
    check("§15.2 proxy interpretation preserved", len(mc) == 1
          and "interaction-horizon/state-management proxy" in mc[0]
          and "measured tool-call counts" in mc[0])
    check("§15.3 explicit proxy boundary exists",
          any("not itself a direct measurement" in b and "proxy for interaction horizon" in b
              for b in p12["boundaries"]))
    blob12 = json.dumps(p12, ensure_ascii=False)
    check("§15.4 tool-call not equated with token cost",
          "token" in blob12 and "only where directly measured" in blob12
          and "token costs via TS-001" not in blob12)
    check("§15.5 tool-call not equated with context/KV/memory cost",
          "KV-cache/memory footprint" in blob12 and "context-window utilization" in blob12)
    check("§15.6 direct efficiency claims require direct Evidence",
          "directly measured by bound Evidence" in blob12)
    check("§15.5b long-horizon thesis + OSWorld distinction + condition binding kept",
          any("OSWorld 1.0 vs 2.0" in r for r in p12["must_cover_requirements"])
          and any("strictest binding" in b for b in p12["boundaries"]))

    p02_same = pkgs["P02"] == hpkgs["P02"]
    check("§15.7 P02 unchanged", p02_same)
    check("§15.8 P15 unchanged", pkgs["P15"] == hpkgs["P15"])
    check("§15.9 P04 unchanged", pkgs["P04"] == hpkgs["P04"])
    others_same = all(pkgs[pid] == hpkgs[pid] for pid in pkgs if pid not in ("P12",))
    check("§15.10 all other packages unchanged (only P12 delta)", others_same)
    check("§15.10b page budgets + depth classes unchanged",
          all(pkgs[pid]["publication_extensions"] == hpkgs[pid]["publication_extensions"] for pid in pkgs))

    disc = [json.loads(l) for l in open(SRC / "discovery/discovery-v2.jsonl", encoding="utf-8")]
    check("§15.11 Discovery 125", len(disc) == 125, str(len(disc)))
    ev_acc = max(glob.glob(str(SRC / "evidence/v2/accepted/*/evidence-accepted.json")),
                 key=lambda p: os.stat(p).st_mtime)
    ev = json.load(open(ev_acc, encoding="utf-8"))
    st = Counter(r["status"] for r in ev["results"])
    check("§15.12/13 Evidence 124, 119/5",
          ev["result_count"] == 124 and dict(st) == {"VERIFIED": 119, "PARTIAL": 5},
          f"{ev['result_count']}/{dict(st)}")
    sel = json.load(open(SRC / "candidate-selection-v2.json", encoding="utf-8"))
    check("§15.14 Selection 124", sel["summary"]["selected_count"] == 124)
    comp = json.load(open(SRC / "profile-completeness-v2.json", encoding="utf-8"))
    head_comp = json.loads(subprocess.run(["git", "show", "HEAD:sources/SP-vision-multimodal-2026/profile-completeness-v2.json"],
                                          cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8"))
    check("§15.15 Completeness judgments unchanged", comp["obligations"] == head_comp["obligations"])
    mx = json.load(open(SRC / "candidate-matrix-v2.json", encoding="utf-8"))
    head_mx = json.loads(subprocess.run(["git", "show", "HEAD:sources/SP-vision-multimodal-2026/candidate-matrix-v2.json"],
                                        cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8"))
    check("§15.15b matrix content unchanged", mx == head_mx)
    pe = arch["publication_extensions"]
    hpe = head_arch["publication_extensions"]
    check("§15.16 cross-package map unchanged",
          pe["p15_cross_package_synthesis_map"] == hpe["p15_cross_package_synthesis_map"])

    core_roots = ["AGENTS.md", "config/", "schemas/", "scripts/", ".github/workflows/",
                  "docs/survey-production-core-v2-session-bootstrap.md",
                  "docs/survey-production-core-v2-sol-luna-review-governance.md"]
    raw = subprocess.run(["git", "status", "--porcelain=v1", "--"] + core_roots,
                         capture_output=True, text=True, cwd=str(ROOT)).stdout.strip()
    dirty = "\n".join(l for l in raw.splitlines() if "__pycache__" not in l).strip()
    check("§15.17 Shared Core unchanged", dirty == "", dirty[:300])
    cov = subprocess.run(["git", "status", "--porcelain=v1", "--", "specials/", "surveys/"],
                         capture_output=True, text=True, cwd=str(ROOT)).stdout.strip()
    check("§15.18 Coverage Freeze unchanged", cov == "", cov[:200])

    state = json.load(open(SRC / "production-state.json", encoding="utf-8"))
    check("§15.19 Draft pending + §15.20 no rev6",
          state["checkpoint_provenance"]["draft"] is None
          and json.load(open(SRC / "draft/v2/packages/P12/draft-result.json",
                             encoding="utf-8")).get("draft_version") == "fresh-121-r8-rev5")
    check("§15.21/22 no validation, no TeX/PDF/Preview/Freeze/Release",
          state["machine_checkpoints"]["validation"] == "pending"
          and subprocess.run(["git", "status", "--porcelain=v1", "--", str(SRC) + "/publication/"],
                             capture_output=True, text=True, cwd=str(ROOT)).stdout.strip() == "")
    check("terminal ARCHITECTURE_ESTABLISHED, review pending",
          state["lifecycle_state"] == "ARCHITECTURE_ESTABLISHED"
          and state["human_gates"]["architecture_review"] == "pending"
          and state["human_gate_provenance"]["architecture_review"] is None
          and state.get("next_action") == "ARCHITECTURE_REVIEW")
    check("architecture PROPOSED, not approved, SHA renewed",
          arch.get("status") == "PROPOSED"
          and sha256_file(SRC / "architecture-v2.json") ==
          "cd37a969fe4d49b54517cb5253bb283931d5bf9e5eb795315b74c0e40339a1af")
    check("fresh dossier generated", (EDIR / "architecture-review-dossier-r9-p12.md").exists())

    (EDIR / "audit-r9p12.json").write_text(json.dumps(
        {"audit": "TS-003 r9 P12 correction terminal (§15)", "failures": fails},
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("OVERALL:", "PASS" if not fails else f"FAIL {fails}")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
