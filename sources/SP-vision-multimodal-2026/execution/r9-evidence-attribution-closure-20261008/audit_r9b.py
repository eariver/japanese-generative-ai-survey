#!/usr/bin/env python3
"""TS-003 r9 attribution closure — terminal validation (§19 items 1-22).

Runs on FINAL worktree bytes. Exit 1 on any FAIL. Writes audit-r9b.json.
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
EDIR = SRC / "execution/r9-evidence-attribution-closure-20261008"
PREV_EDIR = SRC / "execution/p02-detr-bridge-intake-r9-20261008"


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

    disc = [json.loads(l) for l in open(SRC / "discovery/discovery-v2.jsonl", encoding="utf-8")]
    check("§19.1 Discovery count remains 125", len(disc) == 125, str(len(disc)))
    check("§19.2 no new Discovery IDs",
          max(r["discovery_id"] for r in disc) == "VM-D125")

    ev_acc = max(glob.glob(str(SRC / "evidence/v2/accepted/*/evidence-accepted.json")),
                 key=lambda p: os.stat(p).st_mtime)
    ev = json.load(open(ev_acc, encoding="utf-8"))
    check("§19.3 Evidence count remains 124", ev["result_count"] == 124)
    cards = {}
    for r in ev["results"]:
        for d in r["discovery_ids"]:
            cards[d] = json.load(open(Path(ev_acc).parent / "results" / r["filename"], encoding="utf-8"))

    d011 = cards["VM-D011"]
    d123 = cards["VM-D123"]
    d124 = cards["VM-D124"]
    d125 = cards["VM-D125"]
    check("§19.4 VM-D011 DINO-source-local predecessor claim",
          any(c["statement_id"] == "claim-3" and c["evidence_class"] == "AUTHOR_CLAIM"
              and c["source_ids"] == ["src-1"]
              and "based on DN-DETR" in c["text"] and "DAB-DETR" in c["text"]
              and "Deformable DETR" in c["text"] for c in d011["claims"])
          and d011["sources"][0]["url"] == "https://arxiv.org/abs/2203.03605")
    check("§19.5 VM-D123 mismatch eliminated",
          all("DINO" not in c["text"] and "DINO" not in c.get("context", "") for c in d123["claims"])
          and [c["statement_id"] for c in d123["claims"]] == ["claim-1", "claim-2", "claim-3"])
    check("§19.6 VM-D124 mismatch eliminated",
          all("DINO" not in c["text"] and "DINO" not in c.get("context", "") for c in d124["claims"])
          and [c["statement_id"] for c in d124["claims"]] == ["claim-1", "claim-2"])
    check("§19.7 VM-D125 mismatch eliminated",
          all("DINO" not in c["text"] and "DINO" not in c.get("context", "") for c in d125["claims"])
          and [c["statement_id"] for c in d125["claims"]] == ["claim-1", "claim-2"]
          and "diffusion" in json.dumps(d125["limitations"]).lower())
    # full-surface invalid-pattern scan
    bad_ctx = []
    for did, c in cards.items():
        for cl in c.get("claims", []):
            t = cl.get("text", "") + " " + cl.get("context", "")
            if "DINO §§" in t or "DINO abstract" in t or "DINO related-work" in t:
                bad_ctx.append(f"{did}/{cl['statement_id']}")
    check("§19.8 no AUTHOR_CLAIM context points to an absent source", not bad_ctx,
          "; ".join(bad_ctx[:6]))
    # every claim source_id resolves to a registered source
    bad_ref = []
    for did, c in cards.items():
        reg = {s["source_id"] for s in c.get("sources", [])}
        for cl in c.get("claims", []):
            for sid in cl.get("source_ids", []):
                if sid not in reg:
                    bad_ref.append(f"{did}/{cl['statement_id']}:{sid}")
    check("§19.8b all claim source_ids registered", not bad_ref, "; ".join(bad_ref[:6]))

    st = Counter(r["status"] for r in ev["results"])
    check("§19.9 VERIFIED/PARTIAL reported", dict(st) == {"VERIFIED": 119, "PARTIAL": 5},
          str(dict(st)))

    comp = json.load(open(SRC / "profile-completeness-v2.json", encoding="utf-8"))
    vmo02 = next(o for o in comp["obligations"] if o["obligation_id"] == "VM-O02")
    check("§19.10 VM-O02 SATISFIED", vmo02["status"] == "SATISFIED"
          and len(vmo02["discovery_ids"]) == 11)

    sel = json.load(open(SRC / "candidate-selection-v2.json", encoding="utf-8"))
    check("§19.11 Selection bounded (124/124, roles kept)",
          sel["summary"]["selected_count"] == 124
          and Counter(a["disposition"] for a in sel["assignments"]) == {"SELECTED": 124})

    arch = json.load(open(SRC / "architecture-v2.json", encoding="utf-8"))
    head_arch = json.loads(subprocess.run(["git", "show", "HEAD:sources/SP-vision-multimodal-2026/architecture-v2.json"],
                                          cwd=ROOT, check=True, capture_output=True).stdout.decode("utf-8"))
    check("§19.12 Architecture semantic P02 design unchanged",
          arch["packages"] == head_arch["packages"]
          and arch["editorial_thesis"] == head_arch["editorial_thesis"]
          and arch["page_plan"] == head_arch["page_plan"])
    hpkgs = {p["package_id"]: p for p in head_arch["packages"]}
    check("§19.13 other 15 packages unchanged",
          all(arch_pkgs == hpkgs[pid] for pid, arch_pkgs in
              ((p["package_id"], p) for p in arch["packages"])))

    check("§19.14 freeze exception limited to authorized bridge family",
          (EDIR / "coverage-freeze-exception.md").exists() is False
          and (PREV_EDIR / "coverage-freeze-exception.md").exists()
          and subprocess.run(["git", "status", "--porcelain=v1", "--", "specials/", "surveys/"],
                             capture_output=True, text=True, cwd=str(ROOT)).stdout.strip() == "")

    core_roots = ["AGENTS.md", "config/", "schemas/", "scripts/", ".github/workflows/",
                  "docs/survey-production-core-v2-session-bootstrap.md",
                  "docs/survey-production-core-v2-sol-luna-review-governance.md"]
    raw = subprocess.run(["git", "status", "--porcelain=v1", "--"] + core_roots,
                         capture_output=True, text=True, cwd=str(ROOT)).stdout.strip()
    dirty = "\n".join(l for l in raw.splitlines() if "__pycache__" not in l).strip()
    check("§19.15 Shared Core unchanged", dirty == "", dirty[:300])

    check("§19.16 fresh consumption review generated",
          (EDIR / "sol-evidence-consumption-review-r9b.md").exists())
    check("§19.17 fresh Human dossier generated",
          (EDIR / "architecture-review-dossier-r9-fresh.md").exists())
    # old incorrect PASS not active: lifecycle checkpoints bind the NEW validation;
    # old files untouched in worktree (immutable history only)
    state = json.load(open(SRC / "production-state.json", encoding="utf-8"))
    _cp_path = {k: (v or {}).get("path") for k, v in state.get("checkpoint_provenance", {}).items()}
    _cp_hit = False
    for _cp in _cp_path.values():
        if not _cp:
            continue
        try:
            _blob = open(ROOT / _cp, encoding="utf-8").read()
        except OSError:
            continue
        if "r9-evidence-attribution-closure-20261008" in _blob:
            _cp_hit = True
            break
    check("§19.18 old PASS not active authority",
          _cp_hit
          and subprocess.run(["git", "status", "--porcelain=v1", "--",
                              str(PREV_EDIR / "sol-evidence-consumption-review-r9.md"),
                              str(PREV_EDIR / "architecture-review-dossier-r9.md")],
                             capture_output=True, text=True, cwd=str(ROOT)).stdout.strip() == "")

    check("§19.19 Draft pending (checkpoint) + §19.20 no rev6",
          state["checkpoint_provenance"]["draft"] is None
          and json.load(open(SRC / "draft/v2/packages/P02/draft-result.json",
                             encoding="utf-8")).get("draft_version") == "fresh-121-r8-rev5")
    check("§19.21/22 no validation stage, no TeX/PDF/Preview/Freeze/Release",
          state["machine_checkpoints"]["validation"] == "pending"
          and subprocess.run(["git", "status", "--porcelain=v1", "--", str(SRC) + "/publication/"],
                             capture_output=True, text=True, cwd=str(ROOT)).stdout.strip() == "")

    check("terminal ARCHITECTURE_ESTABLISHED, review pending, next ARCHITECTURE_REVIEW",
          state["lifecycle_state"] == "ARCHITECTURE_ESTABLISHED"
          and state["human_gates"]["architecture_review"] == "pending"
          and state["human_gate_provenance"]["architecture_review"] is None
          and state.get("next_action") == "ARCHITECTURE_REVIEW")

    (EDIR / "audit-r9b.json").write_text(json.dumps(
        {"audit": "TS-003 r9 attribution closure terminal (§19)", "failures": fails},
        ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("OVERALL:", "PASS" if not fails else f"FAIL {fails}")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
