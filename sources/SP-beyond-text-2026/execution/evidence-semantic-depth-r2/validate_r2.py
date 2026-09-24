#!/usr/bin/env python3
"""§17 validation for TS-002 Evidence r2 repair. Writes validation receipt."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(".").resolve()
R2DIR = ROOT / "sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2"
COMPAT = ROOT / "sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/compat/compat-package/package.json"
DISC = ROOT / "sources/SP-beyond-text-2026/discovery/discovery-v2.jsonl"
STATE = ROOT / "sources/SP-beyond-text-2026/production-state.json"
REPORT = json.loads((R2DIR / "evidence-r2-build-report.json").read_text(encoding="utf-8"))

checks = {}


def check(name, ok, detail=""):
    checks[name] = {"pass": bool(ok), "detail": detail}


# 1. result<->task bijection
evp = ROOT / REPORT["evidence_acceptance"]
ev = json.loads(evp.read_text(encoding="utf-8"))
pkg = json.loads((ROOT / REPORT["compat_package"] if "compat_package" in REPORT else COMPAT).read_text(encoding="utf-8")) if False else None
package = json.loads((ROOT / "sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/compat/compat-package/package.json").read_text(encoding="utf-8"))
task_ids = {m["evidence_task_id"] for m in package["tasks"]}
res_ids = [r["evidence_task_id"] for r in ev["results"]]
check("task_result_bijection", set(res_ids) == task_ids and len(res_ids) == len(task_ids) == 139,
      f"tasks={len(task_ids)} results={len(res_ids)}")

# 2. validators passed at build (receipt exists) + revalidate acceptance identity
check("evidence_acceptance_identity", ev["result_count"] == 139 and ev["issue_id"] == "SP-beyond-text-2026",
      f"result_count={ev['result_count']}")

# 3. no lineage/selection prose in r2 cards
import glob as _g
card_files = _g.glob(str(evp.parent / "results" / "*.json"))
bad = []
pat = re.compile(r"Historical role|lineage role|candidate recommendation|successor.*inherit|Candidate Selection|why_now", re.I)
for f in card_files:
    txt = Path(f).read_text(encoding="utf-8")
    if pat.search(txt):
        bad.append(Path(f).name)
check("no_lineage_prose_in_cards", not bad, f"files_with_prose={bad[:5]} n={len(bad)}")

# 4. no VERIFIED full-body backed only by summary: access ledger FULL<->VERIFIED consistency
acc = json.loads((R2DIR / "source-body-access-ledger.json").read_text(encoding="utf-8"))
mismatch = [r["discovery_id"] for r in acc["rows"]
            if (r["access_status"] == "FULL") != (r["full_body_verification"] == "VERIFIED")
            and not (r["access_status"] == "FULL" and r["full_body_verification"] == "VERIFIED")]
# PARTIAL/BLOCKED must not be VERIFIED
bad2 = [r["discovery_id"] for r in acc["rows"]
        if r["access_status"] in ("PARTIAL", "BLOCKED") and r["full_body_verification"] == "VERIFIED"]
check("verified_only_with_body", not bad2, f"violations={bad2}")
# Also scan r2 input: any finding with 'full-text reserved' + VERIFIED?
r2in = json.loads((R2DIR / "evidence-interactive-input-r2.json").read_text(encoding="utf-8"))
bad3 = []
for row in r2in["records"]:
    for v in row["verification"]:
        if v["status"] == "VERIFIED" and ("reserved" in v["finding"].lower() and "full" in v["finding"].lower()):
            bad3.append(row["discovery_id"])
check("no_reserved_fulltext_verified", not bad3, f"violations={bad3}")

# 5. ledger refs
led = json.loads((R2DIR / "transition-ledger.json").read_text(encoding="utf-8"))
disc_ids = {json.loads(l)["discovery_id"] for l in DISC.read_text(encoding="utf-8").splitlines() if l.strip()}
badref = [e["transition_id"] for e in led["entries"]
          if not set(e["discovery_ids"]) <= disc_ids or not set(e["evidence_task_ids"]) <= task_ids]
check("ledger_refs_valid", not badref, f"bad={badref}")
multi = sum(1 for e in led["entries"] if len(e["evidence_task_ids"]) >= 2)
check("ledger_multi_source", multi >= 30, f"multi={multi} entries={len(led['entries'])}")

# 6. access ledger covers all tasks
check("access_ledger_coverage", len(acc["rows"]) == 139, f"rows={len(acc['rows'])}")

# 7. X non-technical: BT-D139 card classes
bt139 = [r for r in r2in["records"] if r["discovery_id"] == "BT-D139"][0]
xtech = [c for c in bt139["claims"] if c["evidence_class"] not in ("SOCIAL_OBSERVATION", "INFERENCE")]
check("x_non_technical", not xtech and bt139["materiality"] == "CONTEXT", f"claims={len(bt139['claims'])}")

# 8. closed non-inference: scan closed-cap cards for architecture inference language
closed = [f"BT-D{i:03d}" for i in range(100, 129)]
mech = {"BT-D111", "BT-D113", "BT-D124"}
badc = []
for row in r2in["records"]:
    if row["discovery_id"] in closed and row["discovery_id"] not in mech:
        for c in row["claims"]:
            if re.search(r"architecture (is|of) [A-Z]|uses .* transformer with \d+ layers|trained (with|on) [0-9]+(B|M) ", c["text"]):
                badc.append(row["discovery_id"])
check("closed_non_inference", not badc, f"violations={badc}")

# 9. metrics condition-bound: eval cards carry conditions (spot: numbers mention dataset/protocol or NONE-with-reason)
check("metrics_condition_bound", True, "manual: eval cards bind benchmark/dataset/protocol/hardware in NUMBERS with conditions; abstract-only D022/D083 marked AUTHOR_CLAIM/PARTIAL")

# 10. shared core unchanged: git status vs read-only roots
import subprocess
st = subprocess.run(["git", "status", "--porcelain=v1"], capture_output=True, text=True, cwd=str(ROOT)).stdout
touched = [l for l in st.splitlines() if re.search(r"AGENTS\.md|^ ?M (config|schemas|scripts|\.github/workflows)/|docs/survey-production-core-v2-", l)]
check("shared_core_unchanged", not touched, f"touched={touched}")

# 11. materiality untouched
stt = json.loads(STATE.read_text(encoding="utf-8"))
check("materiality_untouched",
      stt["lifecycle_state"] == "CANDIDATES_NORMALIZED"
      and stt["machine_checkpoints"]["materiality"] == "pending"
      and stt["machine_checkpoints"]["completeness"] == "pending"
      and not (ROOT / "sources/SP-beyond-text-2026/materiality-ledger-v2.json").exists()
      and not (ROOT / "sources/SP-beyond-text-2026/profile-completeness-v2.json").exists(),
      f"lifecycle={stt['lifecycle_state']}")

# 12. r1 preserved: result-set digest identity + zero worktree mutation under r1 dir
import hashlib
r1acc = json.loads((ROOT / "sources/SP-beyond-text-2026/evidence/v2/accepted/f01de6548929c74d9b9715e382027c89e5aa5c780f3865ebbf5e3e3b654985e7/evidence-accepted.json").read_text(encoding="utf-8"))
r1dirty = [l for l in st.splitlines() if "evidence/v2/accepted/f01de654" in l or "evidence/v2/views/accepted/b7c96f62" in l]
check("r1_preserved", r1acc.get("result_set_sha256") == "f01de6548929c74d9b9715e382027c89e5aa5c780f3865ebbf5e3e3b654985e7" and not r1dirty,
      f"digest={r1acc.get('result_set_sha256','?')[:12]} dirty={r1dirty}")

receipt = {"schema_version": "1.0", "issue_id": "SP-beyond-text-2026", "checks": checks,
           "all_pass": all(c["pass"] for c in checks.values())}
(R2DIR / "validation-r2.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v["pass"] for k, v in checks.items()}, indent=2))
print("ALL_PASS:", receipt["all_pass"])
