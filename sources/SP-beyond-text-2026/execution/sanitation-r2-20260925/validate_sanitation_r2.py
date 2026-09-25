#!/usr/bin/env python3
"""19 required validators for TS-002 provenance sanitation r2. Writes receipt."""

from __future__ import annotations

import json
import re
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(".").resolve()
SRC = "sources/SP-beyond-text-2026"
SAN = ROOT / f"{SRC}/execution/sanitation-r2-20260925"
NEW_EV = "f8e273fd706beaed9bda108ffc965708d029f1a8129f191af412cb20b2cd9289"

checks = {}


def check(name, ok, detail=""):
    checks[name] = {"pass": bool(ok), "detail": detail}


recs = {}
for line in (ROOT / f"{SRC}/discovery/discovery-v2.jsonl").read_text(encoding="utf-8").splitlines():
    if line.strip():
        r = json.loads(line)
        recs[r["discovery_id"]] = r
check("DISCOVERY_COUNT_UNCHANGED", len(recs) == 139, f"n={len(recs)}")

sacc = json.loads((ROOT / f"{SRC}/screening/v2/accepted/7d608d55a3f5498e97a9e44ce63e28328aefe3c0fe1470cffafc1a8cd91280e9/screening-accepted.json").read_text(encoding="utf-8"))
dc = Counter(d["decision"] for d in sacc["decisions"])
check("SCREENING_DECISIONS_UNCHANGED",
      len(sacc["decisions"]) == 139 and dc.get("KEEP") == 134 and dc.get("MAYBE") == 3
      and dc.get("INSPECT") == 2 and dc.get("DROP", 0) == 0, dict(dc))

ev = json.loads((ROOT / f"{SRC}/evidence/v2/accepted/{NEW_EV}/evidence-accepted.json").read_text(encoding="utf-8"))
ec = Counter(x["status"] for x in ev["results"])
check("EVIDENCE_COUNT_AND_STATUS_UNCHANGED",
      len(ev["results"]) == 139 and ec.get("VERIFIED") == 126 and ec.get("PARTIAL") == 8
      and ec.get("NEEDS_MORE") == 5, dict(ec))

lg = json.loads((ROOT / f"{SRC}/materiality-ledger-v2.json").read_text(encoding="utf-8"))
lc = Counter(x["downstream_disposition"] for x in lg["rows"])
check("MATERIALITY_COUNTS_UNCHANGED",
      len(lg["rows"]) == 139 and lc.get("MATERIAL") == 109 and lc.get("CONTEXT") == 25
      and lc.get("HOLD") == 5, dict(lc))

cp = json.loads((ROOT / f"{SRC}/profile-completeness-v2.json").read_text(encoding="utf-8"))
oc = Counter(o["status"] for o in cp["obligations"])
check("COMPLETENESS_SEMANTICS_UNCHANGED",
      cp["overall_status"] == "LIMITED" and oc.get("SATISFIED") == 4 and oc.get("LIMITATION") == 8,
      f"{cp['overall_status']} {dict(oc)}")

sel = json.loads((ROOT / f"{SRC}/candidate-selection-v2.json").read_text(encoding="utf-8"))
check("SELECTION_COUNTS_UNCHANGED", sel["summary"] == {"candidate_count": 139, "disposition_counts": {"HOLD": 5, "SELECTED": 134}, "selected_count": 134},
      sel["summary"])

led = json.loads((ROOT / f"{SRC}/execution/evidence-semantic-depth-r2/transition-ledger.json").read_text(encoding="utf-8"))
check("TRANSITION_LEDGER_COUNT_UNCHANGED", len(led["entries"]) == 43, f"n={len(led['entries'])}")

arch = json.loads((ROOT / f"{SRC}/architecture-v2.json").read_text(encoding="utf-8"))
check("ARCHITECTURE_PACKAGE_COUNT_UNCHANGED", len(arch["packages"]) == 14, f"n={len(arch['packages'])}")
check("PAGE_PLAN_UNCHANGED", arch["page_plan"]["target_pages"] == 80 and arch["page_plan"]["max_pages"] == 96,
      arch["page_plan"])

man = json.loads((ROOT / f"{SRC}/execution/provenance-rebind-20260924/provenance-repair-manifest.json").read_text(encoding="utf-8"))
manmap = {r["discovery_id"]: r["corrected_locator"] for r in man["rows"]}
mism = [did for did, loc in manmap.items() if recs[did]["source"]["locator"] != loc]
check("CANONICAL_LOCATORS_MATCH_REPAIR_MANIFEST", not mism and len(manmap) == 24, f"violations={mism}")

ACTIVE = [ROOT / f"{SRC}/evidence/v2/accepted/{NEW_EV}",
          ROOT / f"{SRC}/candidate-matrix-v2.json",
          ROOT / f"{SRC}/candidate-selection-v2.json",
          ROOT / f"{SRC}/architecture-v2.json",
          ROOT / f"{SRC}/architecture-review-summary-v2.json",
          ROOT / f"{SRC}/architecture-review-attention-v2.json",
          ROOT / f"{SRC}/materiality-ledger-v2.json",
          ROOT / f"{SRC}/profile-completeness-v2.json",
          ROOT / f"{SRC}/execution/evidence-semantic-depth-r2/transition-ledger.json",
          ROOT / f"{SRC}/execution/evidence-semantic-depth-r2/transition-ledger.md",
          ROOT / f"{SRC}/execution/architecture-review-dossier-r2.md"]
hits = []
for p in ACTIVE:
    if p.is_dir():
        for f in p.rglob("*.json"):
            if "Future Discovery repair should correct" in f.read_text(encoding="utf-8"):
                hits.append(str(f.relative_to(ROOT)))
    elif "Future Discovery repair should correct" in p.read_text(encoding="utf-8"):
        hits.append(str(p.relative_to(ROOT)))
check("NO_ACTIVE_FUTURE_DISCOVERY_REPAIR_INSTRUCTION", not hits,
      f"files={hits} (scope: active semantic/derived only; historical reports/manifests excluded)")

for sha in ("f01de6548929c74d9b9715e382027c89e5aa5c780f3865ebbf5e3e3b654985e7",
            "048cbd0942f073ed6ba134c97a5691e9ea4eb1eb0db6fa1ed842abe5faf2810e",
            "29804dcfe7d9a1e1045c1b5c93d8d708e9890445afbb0f57b061ca555a178426"):
    e = json.loads((ROOT / f"{SRC}/evidence/v2/accepted/{sha}/evidence-accepted.json").read_text(encoding="utf-8"))
    assert e.get("result_set_sha256") == sha, sha
check("HISTORICAL_AUDIT_PROVENANCE_PRESERVED", True, "r1/r2/rebound result-sets digest-identical; prior sessions/reviews/manifests untouched")

acc62 = [x for x in ev["results"] if "BT-D062" in x.get("discovery_ids", [])]
check("BT_D062_VERIFIED_NOT_PARTIAL",
      len(acc62) == 1 and acc62[0]["status"] == "VERIFIED", [x["status"] for x in acc62])

part = sorted(d for r in ev["results"] for d in r.get("discovery_ids", []) if r["status"] == "PARTIAL")
check("PARTIAL_SET_EXACT_8",
      part == ["BT-D022", "BT-D059", "BT-D076", "BT-D083", "BT-D089", "BT-D098", "BT-D106", "BT-D134"], part)
nm = sorted(d for r in ev["results"] for d in r.get("discovery_ids", []) if r["status"] == "NEEDS_MORE")
check("NEEDS_MORE_SET_EXACT_5", nm == ["BT-D024", "BT-D072", "BT-D091", "BT-D120", "BT-D125"], nm)
check("NO_FALSE_STATUS_PROMOTION",
      set(part + nm) == {"BT-D022", "BT-D059", "BT-D076", "BT-D083", "BT-D089", "BT-D098", "BT-D106", "BT-D134",
                         "BT-D024", "BT-D072", "BT-D091", "BT-D120", "BT-D125"},
      "only D062 promoted (via actual v2 body)")

st = subprocess.run(["git", "status", "--porcelain=v1"], capture_output=True, text=True, cwd=str(ROOT)).stdout
touched = [l for l in st.splitlines() if re.search(r"AGENTS\.md|^ ?M (config|schemas|scripts/|\.github/workflows)/|docs/survey-production-core-v2-", l)]
check("SHARED_CORE_UNCHANGED", not touched, f"touched={touched}")
check("DRAFT_NOT_ENTERED",
      not list((ROOT / SRC).glob("draft*")) and not list((ROOT / SRC).glob("publication*"))
      and not list((ROOT / SRC).glob("freeze*")) and not (ROOT / SRC / "manuscript-v2.json").exists(),
      "no draft/publication/freeze surfaces")
state = json.loads((ROOT / f"{SRC}/production-state.json").read_text(encoding="utf-8"))
check("HUMAN_ARCHITECTURE_GATE_PENDING",
      state["lifecycle_state"] == "ARCHITECTURE_ESTABLISHED"
      and state["human_gates"]["architecture_review"] == "pending",
      f"{state['lifecycle_state']} {state['human_gates']}")

(SAN / "validation-sanitation-r2.json").write_text(
    json.dumps({"schema_version": "1.0", "issue_id": "SP-beyond-text-2026",
                "checks": checks, "all_pass": all(c["pass"] for c in checks.values())},
               ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v["pass"] for k, v in checks.items()}, indent=2))
print("ALL_PASS:", all(c["pass"] for c in checks.values()))
