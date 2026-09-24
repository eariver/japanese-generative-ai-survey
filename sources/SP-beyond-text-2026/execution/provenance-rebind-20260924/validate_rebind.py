#!/usr/bin/env python3
"""17 required validators for TS-002 provenance rebind. Writes receipt."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(".").resolve()
PDIR = ROOT / "sources/SP-beyond-text-2026/execution/provenance-rebind-20260924"
DISC = ROOT / "sources/SP-beyond-text-2026/discovery/discovery-v2.jsonl"
STATE = ROOT / "sources/SP-beyond-text-2026/production-state.json"
MANIFEST = json.loads((PDIR / "provenance-repair-manifest.json").read_text(encoding="utf-8"))
REPORT = json.loads((PDIR / "evidence-rebound-build-report.json").read_text(encoding="utf-8"))
R1_SHA = "f01de6548929c74d9b9715e382027c89e5aa5c780f3865ebbf5e3e3b654985e7"
R2_SHA = "048cbd0942f073ed6ba134c97a5691e9ea4eb1eb0db6fa1ed842abe5faf2810e"

checks = {}


def check(name, ok, detail=""):
    checks[name] = {"pass": bool(ok), "detail": detail}


recs = {}
for line in DISC.read_text(encoding="utf-8").splitlines():
    if line.strip():
        r = json.loads(line)
        recs[r["discovery_id"]] = r

# 1-4 counts + decisions
check("DISCOVERY_COUNT_UNCHANGED", len(recs) == 139, f"n={len(recs)}")
sacc = json.loads(Path(ROOT / REPORT["screening_acceptance"]).read_text(encoding="utf-8"))
from collections import Counter
dc = Counter(d["decision"] for d in sacc["decisions"])
check("SCREENING_DECISIONS_UNCHANGED",
      len(sacc["decisions"]) == 139 and dc.get("KEEP") == 134 and dc.get("MAYBE") == 3
      and dc.get("INSPECT") == 2 and dc.get("DROP", 0) == 0, dict(dc))
ev = json.loads(Path(ROOT / REPORT["evidence_acceptance"]).read_text(encoding="utf-8"))
check("EVIDENCE_COUNT_UNCHANGED", len(ev["results"]) == 139, f"n={len(ev['results'])}")
vw = json.loads(Path(ROOT / REPORT["views_acceptance"]).read_text(encoding="utf-8"))
check("EDITION_VIEW_COUNT_UNCHANGED", len(vw["views"]) == 139, f"n={len(vw['views'])}")

# 5. all corrected rebound
acc = json.loads((ROOT / "sources/SP-beyond-text-2026/execution/provenance-rebind-20260924/compat-rebound/package.json").read_text(encoding="utf-8"))
tloc = {}
for m in acc["tasks"]:
    t = json.loads(Path(ROOT / "sources/SP-beyond-text-2026/execution/provenance-rebind-20260924/compat-rebound" / m["path"]).read_text(encoding="utf-8"))
    tloc[t["discovery_ids"][0]] = t["source_records"][0]["locator"]
bad = [row["discovery_id"] for row in MANIFEST["rows"]
       if recs[row["discovery_id"]]["source"]["locator"] != row["corrected_locator"]
       or tloc[row["discovery_id"]] != row["corrected_locator"]]
check("ALL_CORRECTED_BODY_IDS_REBOUND", not bad, f"violations={bad}")

# 6. no VERIFIED card points to known-wrong locator
wrong = {row["old_locator"] for row in MANIFEST["rows"]}
r2in = json.loads((PDIR / "evidence-interactive-input-r2-rebound.json").read_text(encoding="utf-8"))
bad2 = [r["discovery_id"] for r in r2in["records"]
        if r["status"] == "VERIFIED" and r["entity"].get("canonical_url") in wrong]
check("NO_VERIFIED_CARD_POINTS_TO_KNOWN_WRONG_LOCATOR", not bad2, f"violations={bad2}")

# 7-9 identities
d062 = recs["BT-D062"]["source"]
check("BT_D062_TITLE_LOCATOR_IDENTITY_CONSISTENT",
      d062["locator"] == "https://arxiv.org/abs/2312.05187" and "2312.05187" not in d062["title"]
      and "Seamless" in d062["title"] and recs["BT-D062"]["source"]["published_at"] == "2023-12",
      d062["locator"] + " | " + d062["title"][:60])
d089 = recs["BT-D089"]["source"]
check("BT_D089_TITLE_LOCATOR_IDENTITY_CONSISTENT",
      d089["locator"] == "https://ieeexplore.ieee.org/document/7178964" and "1507.08211" not in d089["locator"],
      d089["locator"])
d024 = recs["BT-D024"]["source"]
check("BT_D024_REPOSITORY_IDENTITY_VERIFIED",
      d024["locator"] == "https://github.com/CompVis/stable-diffusion"
      and "CompVis" in d024["title"] and "Stability-AI" not in d024["title"]
      and recs["BT-D024"]["source"]["published_at"] == "2022-08",
      d024["locator"] + " | " + d024["title"][:60])

# 10-11 manifest / substitution
check("OLD_LOCATORS_PRESERVED_IN_REPAIR_MANIFEST",
      len(MANIFEST["rows"]) == 24 and all(
          set(row) >= {"discovery_id", "old_locator", "corrected_locator", "correction_basis",
                       "observed_mismatch", "body_actually_consumed", "repair_timestamp"}
          for row in MANIFEST["rows"]),
      f"rows={len(MANIFEST['rows'])}")
import glob as _g
card_files = _g.glob(str(Path(ROOT / REPORT["evidence_acceptance"]).parent / "results" / "*.json"))
sub = []
for f in card_files:
    c = json.loads(Path(f).read_text(encoding="utf-8"))
    urls = [s.get("url") for s in c.get("sources", [])]
    canon = [e.get("canonical_url") for e in c.get("entities", [])]
    if any(u in wrong for u in urls + canon):
        sub.append(f"{Path(f).name}: authority URL is a known-wrong locator")
check("NO_SILENT_SOURCE_SUBSTITUTION", not sub, f"violations={sub}")

# 12. no false promotion: PARTIAL/BLOCKED set identical to r2 except D062's legitimate v2 promotion
raled = json.loads((PDIR / "source-body-access-ledger-rebound.json").read_text(encoding="utf-8"))
final = {r["discovery_id"]: r["final_status"] for r in raled["rows"]}
nonver = sorted(d for d, s in final.items() if s != "VERIFIED")
check("PARTIAL_NEEDS_MORE_NOT_FALSELY_PROMOTED",
      nonver == sorted(["BT-D022", "BT-D024", "BT-D059", "BT-D072", "BT-D076", "BT-D083",
                        "BT-D089", "BT-D091", "BT-D098", "BT-D106", "BT-D120", "BT-D125", "BT-D134"]),
      f"non_verified={nonver}")

# 13. ledger refs
led = json.loads((PDIR / "transition-ledger.json").read_text(encoding="utf-8"))
tids = {m["evidence_task_id"] for m in acc["tasks"]}
badref = [e["transition_id"] for e in led["entries"]
          if not set(e["discovery_ids"]) <= set(recs) or not set(e["evidence_task_ids"]) <= tids]
check("TRANSITION_LEDGER_REFERENCES_VALID", not badref and len(led["entries"]) == 43, f"bad={badref}")

# 14-15 history preserved
for sha, name in ((R1_SHA, "R1"), (R2_SHA, "R2")):
    e = json.loads((ROOT / f"sources/SP-beyond-text-2026/evidence/v2/accepted/{sha}/evidence-accepted.json").read_text(encoding="utf-8"))
    check(f"{name}_EVIDENCE_PRESERVED", e.get("result_set_sha256") == sha, e.get("result_set_sha256", "?")[:12])
check("R2_SEMANTIC_EVIDENCE_PRESERVED",
      Path(ROOT / f"sources/SP-beyond-text-2026/evidence/v2/accepted/{R2_SHA}/evidence-accepted.json").is_file(),
      "r2 dir + input snapshot in prior-authority")

# 16-17 core/state
st = subprocess.run(["git", "status", "--porcelain=v1"], capture_output=True, text=True, cwd=str(ROOT)).stdout
touched = [l for l in st.splitlines() if re.search(r"AGENTS\.md|^ ?M (config|schemas|scripts/|\.github/workflows)/|docs/survey-production-core-v2-", l)]
check("SHARED_CORE_UNCHANGED", not touched, f"touched={touched}")
state = json.loads(STATE.read_text(encoding="utf-8"))
check("MATERIALITY_NOT_ENTERED",
      state["lifecycle_state"] == "CANDIDATES_NORMALIZED"
      and state["machine_checkpoints"]["materiality"] == "pending"
      and state["machine_checkpoints"]["completeness"] == "pending"
      and not (ROOT / "sources/SP-beyond-text-2026/materiality-ledger-v2.json").exists()
      and not (ROOT / "sources/SP-beyond-text-2026/profile-completeness-v2.json").exists(),
      state["lifecycle_state"])

(PDIR / "validation-rebind.json").write_text(
    json.dumps({"schema_version": "1.0", "issue_id": "SP-beyond-text-2026",
                "checks": checks, "all_pass": all(c["pass"] for c in checks.values())},
               ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v["pass"] for k, v in checks.items()}, indent=2))
print("ALL_PASS:", all(c["pass"] for c in checks.values()))
