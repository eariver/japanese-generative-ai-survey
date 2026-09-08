#!/usr/bin/env python3
"""Build fresh event-level Screening Discovery expansion for W34 after Sol Discovery r2.

Execution agent: Muse Spark 1.3
Execution mode: EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION

Strategy (Core-valid derived expansion):
- Reuse 110 prior event-level records verbatim (105 prior events +5 coverage passthrough).
  Their 40 parents are subset of fresh 369 roots, so they remain valid.
- For each of the 329 new roots (new_ids - old_parents), create one 1:1 REFERENCE_EXPANSION
  child with identical source identity/raw/obligations and a fresh event-level ID.
  New roots = 15 refresh +3 official fallback new +311 triage arxiv =329.
- Total derived = 110 +329 =439 records, accounting for all 369 roots.
- Inventory is semantic cross-check, not input replacement. Reconciliation summary
  maps prior 105, refresh 15, fallback splits, AWS Memory, arxiv identities.
"""
from __future__ import annotations
import json
from pathlib import Path

REPO = Path(".").resolve()
EXEC_REL = "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2"
OLD_INPUT = REPO / "sources/2026-W34/screening/input/event-discovery-v2.jsonl"
NEW_DISCOVERY = REPO / "sources/2026-W34/discovery/discovery-v2.jsonl"
OUT_DERIVED = REPO / EXEC_REL / "screening-basis/event-discovery-fresh-v1.jsonl"
OUT_MAP = REPO / EXEC_REL / "screening-basis/derived-mapping.json"
OUT_SUMMARY = REPO / EXEC_REL / "screening-basis/reconciliation-summary.json"

def read_jsonl(p: Path):
    rows = []
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows

def write_jsonl(p: Path, rows):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="\n") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")

def child_id_for_parent(pid: str) -> str:
    # Deterministic fresh event-level IDs, avoiding collision with old w34-event-c* / w34-coverage-*
    if pid.startswith("w34-gapfill-arxiv-triage-"):
        suffix = pid.replace("w34-gapfill-arxiv-triage-", "")
        return f"w34-event-arxiv-{suffix}"
    if pid.startswith("w34-refresh-arxiv-"):
        suffix = pid.replace("w34-refresh-", "")
        return f"w34-event-refresh-arxiv-{suffix}"
    if pid.startswith("w34-refresh-"):
        suffix = pid.replace("w34-refresh-", "")
        return f"w34-event-refresh-{suffix}"
    if pid.startswith("w34-gapfill-alibaba-"):
        suffix = pid.replace("w34-gapfill-", "")
        return f"w34-event-gap-{suffix}"
    if pid.startswith("w34-gapfill-aws-"):
        suffix = pid.replace("w34-gapfill-", "")
        return f"w34-event-gap-{suffix}"
    # fallback generic
    return f"w34-event-fresh-{pid}"

def main() -> int:
    old_recs = read_jsonl(OLD_INPUT)
    new_roots = read_jsonl(NEW_DISCOVERY)
    new_by_id = {r["discovery_id"]: r for r in new_roots}
    old_parents = set()
    for r in old_recs:
        old_parents.update(r["provenance"]["parent_refs"])
    new_ids = set(new_by_id)
    assert old_parents.issubset(new_ids), f"old parents missing in new: {sorted(old_parents - new_ids)}"
    new_only = sorted(new_ids - old_parents)
    print(f"old records: {len(old_recs)}, old parents: {len(old_parents)}, new roots: {len(new_ids)}, new-only: {len(new_only)}")
    # Expect 329 new-only
    # Build children for new-only
    children = []
    mapping = []
    seen_child_ids = set(r["discovery_id"] for r in old_recs)
    for pid in new_only:
        parent = new_by_id[pid]
        cid = child_id_for_parent(pid)
        if cid in seen_child_ids or cid in new_ids:
            # collision guard: append suffix
            cid = f"{cid}-e1"
        assert cid not in seen_child_ids and cid not in new_ids, f"collision {cid}"
        seen_child_ids.add(cid)
        src = parent["source"]
        prov = parent["provenance"]
        meta = dict(src.get("metadata", {}))
        # enrich with event-level trace, preserving parent identity
        meta.update({
            "event_level_discovery_id": cid,
            "event_level_expansion": True,
            "selected_source_parent": pid,
            "fresh_expansion": "w34-screening-evidence-after-sol-discovery-r2",
            "screening_decision_present": False,
        })
        child = {
            "schema_version": "2.0-rc1",
            "issue_id": parent["issue_id"],
            "discovery_id": cid,
            "provenance": {
                "origin": "REFERENCE_EXPANSION",
                "research_pass": 1,
                "parent_refs": [pid],
                "obligation_ids": list(prov["obligation_ids"]),
                "reason": (
                    f"Create one independently screenable event-level record for fresh Discovery {pid} "
                    f"by 1:1 expansion of the accepted 369-record graph; retain source identity, Raw bindings, "
                    f"and obligations without Screening disposition. Inventory cross-check preserves split/duplicate/chronology semantics."
                ),
            },
            "source": {
                "source_type": src["source_type"],
                "collector_id": src["collector_id"],
                "collector_run_id": src["collector_run_id"],
                "observed_at": src["observed_at"],
                "title": src["title"],
                "locator": src["locator"],
                "raw_paths": list(src["raw_paths"]),
                "published_at": src.get("published_at"),
                "summary_text": src.get("summary_text"),
                "metadata": meta,
            },
        }
        children.append(child)
        mapping.append({"parent": pid, "child": cid, "title": src["title"][:120]})
    # Combine: old verbatim + new children sorted by child ID for determinism
    children_sorted = sorted(children, key=lambda r: r["discovery_id"])
    combined = list(old_recs) + children_sorted
    # Ensure unique IDs and no overlap with roots
    cids = [r["discovery_id"] for r in combined]
    assert len(cids) == len(set(cids)), "duplicate child IDs"
    overlap = set(cids) & new_ids
    assert not overlap, f"derived reuses root IDs: {sorted(overlap)}"
    OUT_DERIVED.parent.mkdir(parents=True, exist_ok=True)
    write_jsonl(OUT_DERIVED, combined)
    OUT_MAP.parent.mkdir(parents=True, exist_ok=True)
    OUT_MAP.write_text(json.dumps({"new_only_count": len(new_only), "children": len(children), "mapping": mapping}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Reconciliation summary counts
    summary = {
        "old_records_reused": len(old_recs),
        "old_parents": len(old_parents),
        "new_roots_total": len(new_ids),
        "new_only": len(new_only),
        "new_children": len(children),
        "total_derived": len(combined),
        "expected_breakdown": {
            "prior_105_events": 105,
            "coverage_passthrough": 5,
            "refresh_leads": 15,
            "official_fallback_new": 3,
            "arxiv_shortlist_new": 311,
            "total_unique_event_identities": 434,
            "total_derived_with_passthrough": 439,
        },
    }
    OUT_SUMMARY.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    print(f"wrote {OUT_DERIVED} ({len(combined)} records)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
