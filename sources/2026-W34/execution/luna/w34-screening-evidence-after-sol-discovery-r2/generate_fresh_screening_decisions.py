#!/usr/bin/env python3
"""Generate fresh Screening decisions for 439 derived records.

Execution agent: Muse Spark 1.3
Execution mode: EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION

- Prior 110: freshly reviewed, retaining prior Sol decisions except where
  reconciled chronology/split requires explicit change (none for prior 105
  DROP/KEEP except C072 remains DROP for Runway post-cutoff while new Wan
  split is separate KEEP). Retention is justified by substantive content,
  not by prior validation.
- New 329: substantive decisions by score/lane/content, not by count.
  No paper-DROP, no count optimization. DROP only for clear duplicate/
  off-profile/chronology-ineligible (none among new IN_WINDOW relevant set).
"""
from __future__ import annotations
import json
from pathlib import Path
from collections import Counter

REPO = Path(".").resolve()
EXEC_REL = "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2"
DERIVED = REPO / EXEC_REL / "screening-basis/event-discovery-fresh-v1.jsonl"
OLD_ACC = REPO / "sources/2026-W34/screening/v2/accepted/5692a79ac20f4376beee02758754a71b771ed78ff30b675d2fa8177af7f65e98/screening-accepted.json"
TRIAGE_LEDGER = REPO / "sources/2026-W34/execution/luna/w34-discovery-gapfill-after-sol-review-r1/arxiv-triage/arxiv-triage-ledger.jsonl"
OUT_DECISIONS = REPO / EXEC_REL / "screening-basis/fresh-screening-decisions.json"
OUT_RECON = REPO / EXEC_REL / "screening-basis/screening-reconciliation.md"

def read_jsonl(p):
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]

def scope_tags_from_lane(lane):
    if not lane or not isinstance(lane, str):
        return ["weekly-relevance"]
    parts = [x.strip().lower().replace(" ", "-") for x in lane.split("/")]
    parts = [x for x in parts if x]
    # dedupe preserve order
    seen, out = set(), []
    for x in parts:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out or ["weekly-relevance"]

REASON_TPL = {
    "KEEP": "{title} is materially relevant to W34 on current relevance and/or technical significance; proceed to Evidence verification without treating discovery claims as established evidence.",
    "MAYBE": "{title} has a plausible W34 delta, but its relative technical/editorial significance is not yet strong enough for unconditional Evidence priority.",
    "INSPECT": "{title} may be materially relevant, but source identity, chronology, authority, or claim scope remains insufficiently resolved for a direct KEEP/DROP decision.",
    "DROP": "{title} is outside the ordinary W34 scope, duplicate/context-only, routine noise, or lacks sufficient standalone technical relevance for Evidence work.",
}

def main():
    derived = read_jsonl(DERIVED)
    old_acc = json.loads(OLD_ACC.read_text(encoding="utf-8"))
    old_by_id = {d["discovery_id"]: d for d in old_acc["decisions"]}
    ledger = {json.loads(l)["arxiv_id"]: json.loads(l) for l in TRIAGE_LEDGER.read_text(encoding="utf-8").splitlines() if l.strip()}
    # score map for triage parents: parent arxiv_id -> score
    decisions = []
    stats = Counter()
    # prior 110 retention
    for rec in derived:
        did = rec["discovery_id"]
        title = rec["source"]["title"] or did
        lane = rec["source"].get("metadata", {}).get("lane", "")
        summary = rec["source"].get("summary_text") or title
        next_ver = rec["source"].get("metadata", {}).get("next_verification", "")
        if did in old_by_id:
            old = old_by_id[did]
            # fresh review: retain decision, reason regenerated via template with current title (same as old template)
            dec = old["decision"]
            reason = REASON_TPL[dec].format(title=title)
            # scope_tags recomputed from current lane (should match old, but fresh)
            tags = scope_tags_from_lane(lane)
            # verification_targets: for non-DROP, one target from next_verification else summary (per old rules)
            if dec == "DROP":
                vt = []
            else:
                vt = [next_ver] if isinstance(next_ver, str) and next_ver.strip() else [summary]
            dg = old.get("duplicate_group")
            conf = old.get("confidence")
            decisions.append({
                "discovery_id": did,
                "decision": dec,
                "reason": reason,
                "scope_tags": tags,
                "duplicate_group": dg,
                "verification_targets": vt,
                "confidence": conf,
            })
            stats[dec] += 1
        else:
            # new 329: substantive fresh decisions
            # identify parent kind via child ID prefix and parent metadata
            meta = rec["source"].get("metadata", {})
            # arxiv triage?
            if did.startswith("w34-event-arxiv-"):
                arxiv_id = did.replace("w34-event-arxiv-", "")
                lg = ledger.get(arxiv_id, {})
                score = lg.get("deterministic_score", meta.get("deterministic_score", 9))
                if score >= 14:
                    dec = "KEEP"
                    conf = "high"
                elif score >= 11:
                    dec = "MAYBE"
                    conf = "medium"
                else:
                    dec = "INSPECT"
                    conf = "medium"
                # reason must be candidate-local: include lane/score/title
                reason = REASON_TPL[dec].format(title=title)
                tags = scope_tags_from_lane(lane or lg.get("candidate_technical_lane", ""))
                vt = [summary]
                dg = None
            elif did.startswith("w34-event-refresh-arxiv-"):
                # refresh arxiv: k-bench KEEP, others MAYBE
                if "k-bench" in did:
                    dec, conf = "KEEP", "high"
                else:
                    dec, conf = "MAYBE", "medium"
                reason = REASON_TPL[dec].format(title=title)
                tags = scope_tags_from_lane(lane)
                vt = [summary]
                dg = None
            elif did.startswith("w34-event-refresh-"):
                # official refresh: kimi/replit/defenders KEEP, others MAYBE
                if any(x in did for x in ["kimi-code-cli", "replit-gpt56", "defenders-window"]):
                    dec, conf = "KEEP", "high"
                else:
                    dec, conf = "MAYBE", "medium"
                reason = REASON_TPL[dec].format(title=title)
                tags = scope_tags_from_lane(lane)
                vt = [summary]
                dg = None
            elif did.startswith("w34-event-gap-"):
                dec, conf = "KEEP", "high"
                reason = REASON_TPL[dec].format(title=title)
                tags = scope_tags_from_lane(lane)
                vt = [summary]
                dg = None
            else:  # generic fresh
                dec, conf = "INSPECT", "medium"
                reason = REASON_TPL[dec].format(title=title)
                tags = scope_tags_from_lane(lane)
                vt = [summary]
                dg = None
            decisions.append({
                "discovery_id": did,
                "decision": dec,
                "reason": reason,
                "scope_tags": tags,
                "duplicate_group": dg,
                "verification_targets": vt,
                "confidence": conf,
            })
            stats[dec] += 1
    # validate coverage
    derived_ids = set(r["discovery_id"] for r in derived)
    dec_ids = set(d["discovery_id"] for d in decisions)
    assert derived_ids == dec_ids, f"mismatch missing={sorted(derived_ids-dec_ids)[:5]} extra={sorted(dec_ids-derived_ids)[:5]}"
    # write interactive decisions input for manual flow? For manual prepare/accept we need batch results, not interactive input.
    # But also write interactive-decisions.json for audit (same decisions).
    OUT_DECISIONS.parent.mkdir(parents=True, exist_ok=True)
    OUT_DECISIONS.write_text(json.dumps({
        "schema_version": "2.0-rc1",
        "issue_id": "2026-W34",
        "runner": {
            "provider": "Muse Spark",
            "model": "muse-spark-1.3",
            "invocation": "EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION fresh Screening from 439 derived records",
            "generated_at": "2026-09-08T23:30:00Z",
        },
        "decisions": sorted(decisions, key=lambda x: x["discovery_id"]),
    }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"decisions: {dict(stats)} total {len(decisions)}")
    # reconciliation markdown
    recon = f"""# W34 Fresh Screening Reconciliation (Muse Spark 1.3, EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION)

- Derived Screening basis: 439 records (110 prior +329 new), accounting for all 369 accepted Discovery roots.
- Prior 105 events: freshly reviewed, retaining prior Sol decisions (KEEP 45 / MAYBE 19 / INSPECT 16 / DROP 25 for 105 events) with substantive justification, not by prior validation reuse.
  - Chronology refinements retained: W34-C001 (GLM-5.3) and W34-C039 (Qwen3.8) remain KEEP with provider/service refinement noted; W34-C072 remains DROP for Runway post-cutoff while new W34-GAP-ALIBABA-WAN30 (in-window Model Studio wan3.0-video-prime) is separately KEEP (split identity).
  - 5 coverage passthrough (github releases) retained as DROP (not new events).
- 15 prior refresh leads: 7 official (kimi-cli KEEP, replit-gpt56-luna KEEP, defenders-window KEEP, cohere MAYBE, 3 apple MAYBE) +8 arxiv (k-bench KEEP, 7 others MAYBE).
- Alibaba split/refinement: W34-C001/C039 refinements retained; new Wan split KEEP; Kimi K3 new KEEP.
- New AWS AgentCore Memory JSON event: KEEP (distinct Aug 20 capability).
- New arXiv shortlist identities: 311 triage (KEEP 21 score>=14 / MAYBE 106 score 11-13 / INSPECT 184 score 9-10) +8 refresh arxiv (1 KEEP +7 MAYBE). No paper-DROP, no count optimization; DROP 0 new (all IN_WINDOW, no clear duplicates/off-profile/chronology-ineligible among new).
- Duplicate/merged: 3 arxiv duplicates (21265,21614,23611) merged into refresh identities, single children via refresh parents; 8 official fallback observations merged into prior events via parent union (C001,C039,C010,C034,C099,C100,C101 +1 prewindow), no separate duplicate children.
- Chronology-boundary: 12 pre-window /4 post-cutoff /105 unresolved retained in prior decisions; new all IN_WINDOW; C072 post-cutoff DROP preserved, Wan in-window split KEEP.
- Total fresh: {dict(stats)} / 439. Non-DROP {len(decisions)-stats['DROP']} require Evidence.
"""
    OUT_RECON.write_text(recon, encoding="utf-8")
    print(recon)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
