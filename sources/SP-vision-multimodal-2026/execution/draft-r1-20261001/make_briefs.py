#!/usr/bin/env python3
"""Generate per-package authoring briefs for TS-003 Draft r1 subagents."""
import json
import os

REPO = "/home/eariver/git/japanese-generative-ai-survey"
SRC = "sources/SP-vision-multimodal-2026"
arch = json.load(open(f"{REPO}/{SRC}/architecture-v2.json"))
mat = json.load(open(f"{REPO}/{SRC}/candidate-matrix-v2.json"))
sel = json.load(open(f"{REPO}/{SRC}/candidate-selection-v2.json"))

mi = {}
for row in mat["rows"]:
    did = row["discovery_ids"][0]
    mi[did] = {
        "title": row.get("title"),
        "type": row.get("artifact_type"),
        "ev": row.get("evidence_status"),
        "mat": row.get("materiality"),
    }
sel_by_cid = {a["candidate_id"]: a for a in sel["assignments"]}
cid2did = {}
for row in mat["rows"]:
    cid2did[row["candidate_id"]] = row["discovery_ids"][0]

acc = json.load(open(
    f"{REPO}/{SRC}/evidence/v2/accepted/4182d7d5848d7aa1506a6428f7284c0991320234cfe87d8a51ef8ce1e784de34/evidence-accepted.json"))
resdir = (f"{REPO}/{SRC}/evidence/v2/accepted/4182d7d5848d7aa1506a6428f7284c0991320234cfe87d8a51ef8ce1e784de34/results")
cards = {}
for row in acc["results"]:
    c = json.load(open(os.path.join(resdir, row["filename"])))
    for did in row["discovery_ids"]:
        cards[did] = c

outdir = f"{REPO}/{SRC}/execution/draft-r1-20261001/briefs"
os.makedirs(outdir, exist_ok=True)
for p in arch["packages"]:
    pid = p["package_id"]
    pub = p.get("publication_extensions", {})
    depth = pub.get("depth_classes", {})
    lines = []
    lines.append(f"# Brief {pid}: {p['title']}")
    lines.append(f"purpose: {p['purpose']}")
    lines.append(f"page_budget: {pub.get('page_budget_body_pages')} body pages")
    lines.append(f"must_cover: {p['must_cover_requirements']}")
    lines.append(f"boundaries({len(p['boundaries'])}):")
    for b in p["boundaries"]:
        lines.append(f"  - {b[:200]}")
    lines.append("depth classes:")
    for cls, ids in depth.items():
        lines.append(f"  {cls}: {ids}")
    lines.append("")
    lines.append("placements (did | usage | selection-rationale | card claims/limitations):")
    for cid in p["primary_candidate_ids"] + p["supporting_candidate_ids"]:
        did = cid2did[cid]
        a = sel_by_cid[cid]
        m = mi[did]
        c = cards[did]
        lines.append(f"== {did} [{a['architecture_usage']}] {m['type']}/{m['ev']}/{m['mat']}: {m['title']}")
        lines.append(f"   rationale: {a['rationale']}")
        for cl in c.get("claims", []):
            lines.append(f"   CLAIM {cl.get('statement_id')} [{cl.get('subject_role')}]: {(cl.get('text') or '')[:500]}")
        for ev2 in c.get("temporal", {}).get("events", []):
            lines.append(f"   EVENT {ev2.get('event_id')}: {(ev2.get('text') or '')[:300]}")
        for li in c.get("limitations", []):
            lines.append(f"   LIMIT {(li.get('statement_id'))}: {(li.get('text') or '')[:400]}")
    # P15 cross-synthesis map
    if pid == "P15":
        lines.append("")
        lines.append("CROSS-SYNTHESIS MAP (already-selected IDs, grouped):")
        for k, v in arch["publication_extensions"]["p15_cross_package_synthesis_map"].items():
            lines.append(f"  {k}: {v}")
    open(f"{outdir}/{pid}.md", "w").write("\n".join(lines) + "\n")
    print(pid, len("\n".join(lines)), "chars")
