#!/usr/bin/env python3
"""Build the VM-D075 omni license supplement (Core builder only) + stage the card.

Card: claim-1 tail resolved buckets; NEW claim-2 weights; limitation-2 (scoped
unresolved) DELETED as resolved; lim-1 + unresolved kept. VERIFIED kept.
"""
from __future__ import annotations
import copy
import datetime
import hashlib
import json
from pathlib import Path

from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

ISSUE_ID = "SP-vision-multimodal-2026"
ROOT0 = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
CURR = "3cd37179fe5c5a70d549dfabc9399864dea6a49ce79f1e85dcafd086ac61d412"
TID075 = "evidence:SP-vision-multimodal-2026:4b007409a575a02d"
NOW = "2026-10-05T00:00:00Z"
SNAP = f"{EDIR}/snapshots"
SUP_OUT = f"{EDIR}/evidence-authority-supplement-vm-d075-omni.json"
SUP_ID = "ts003-late-cutoff-supplement-vm-d075-omni-20261005"

SPECS = [
    ("qwen3-omni-LICENSE-main.txt", "https://raw.githubusercontent.com/QwenLM/Qwen3-Omni/main/LICENSE",
     "Qwen3-Omni repo-root LICENSE (current; Apache-2.0)",
     "Code license bucket: repo-root LICENSE full Apache-2.0 text as served today."),
    ("qwen3-omni-LICENSE-ae5dbf9.txt", "https://raw.githubusercontent.com/QwenLM/Qwen3-Omni/ae5dbf9e734b7c72c1a70805cfb321b5fa3e9615/LICENSE",
     "Qwen3-Omni repo-root LICENSE at commit ae5dbf9 (2025-09-22 inception)",
     "Code license pre-cutoff proof: byte-identical Apache-2.0 text since repo inception."),
    ("qwen3-omni-30b-readme-main.md", "https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct/raw/main/README.md",
     "Qwen3-Omni-30B-A3B-Instruct model-card README (current; license_name apache-2.0)",
     "Weight license bucket: current header license_name apache-2.0 for the released artifact."),
    ("qwen3-omni-30b-readme-302ffa9.md", "https://huggingface.co/Qwen/Qwen3-Omni-30B-A3B-Instruct/raw/302ffa9/README.md",
     "Qwen3-Omni-30B-A3B-Instruct model-card README at commit 302ffa9 (2025-09-20 initial)",
     "Weight license pre-cutoff proof: license apache-2.0 from release; bound artifact model-00001-of-00015.safetensors."),
]


def sid(url: str) -> str:
    return "supplement-src-" + hashlib.sha256(url.encode()).hexdigest()[:16]


def main() -> int:
    root = Path(".").resolve()
    from scripts import survey_agent_tool_v2 as agent_tool
    state = core.load_json(root / STATE_REL)
    profile = core.load_json(root / state["profile"]["path"])
    source_root = root / profile["paths"]["source_root"]
    discovery_path = source_root / "discovery/discovery-v2.jsonl"
    scr_acc = max((source_root / "screening/v2/accepted").glob("*/screening-accepted.json"),
                  key=lambda p: p.stat().st_mtime)
    sources = []
    for fname, locator, title, relation in SPECS:
        raw = root / SNAP / fname
        assert raw.is_file(), fname
        data = raw.read_bytes()
        assert len(data) > 0, fname
        sources.append({
            "supplement_source_id": sid(locator), "discovery_id": "VM-D075",
            "evidence_task_id": TID075, "locator": locator,
            "source_type": "first_party_release_or_docs", "source_class": "PRIMARY_OFFICIAL",
            "title": title, "published_at": None, "accessed_at": NOW,
            "raw_path": f"{SNAP}/{fname}", "raw_sha256": hashlib.sha256(data).hexdigest(),
            "byte_count": len(data), "relation": relation,
        })
    assert len({s["supplement_source_id"] for s in sources}) == 4
    _outp = root / SUP_OUT
    if _outp.exists():
        from scripts import survey_agent_tool_v2 as _at
        _cur = core.load_json(_outp)
        assert [dict(s) for s in _cur["sources"]] == [dict(s) for s in sources], "supplement sources differ"
        with _at.current_stage_basis_override():
            evidence.validate_evidence_authority_supplement(
                root, _outp, core.repository_commit_sha(root), expected_issue_id=ISSUE_ID)
        out = _outp
        print("supplement reused:", out.relative_to(root), core.sha256_file(out)[:12])
    else:
        with agent_tool.current_stage_basis_override():
            out = evidence.build_evidence_authority_supplement(
                root, ISSUE_ID, source_root, discovery_path, scr_acc, sources,
                root / SUP_OUT, supplement_id=SUP_ID,
                implementation_sha=core.repository_commit_sha(root))
        print("supplement:", out.relative_to(root), core.sha256_file(out)[:12])
    om = [sid(loc) for _, loc, _, _ in SPECS]

    import sys
    sys.path.insert(0, str(root))
    from scripts import survey_evidence_v2 as ev
    acc = core.load_json(root / SRC / f"evidence/v2/accepted/{CURR}/evidence-accepted.json")
    meta = next(r for r in acc["results"] if r["evidence_task_id"] == TID075)
    card = core.load_json(root / SRC / "evidence/v2/accepted" / CURR / "results" / meta["filename"])
    assert card["status"] == "VERIFIED"
    claims = {c["statement_id"]: c for c in card["claims"]}
    assert set(claims) == {"claim-1"}, set(claims)
    lims = {l["statement_id"]: l for l in card["limitations"]}
    assert set(lims) == {"limitation-1", "limitation-2"}, set(lims)
    subj = "ev-vmd075"
    c1 = copy.deepcopy(claims["claim-1"])
    old_tail = "Weights license and code license remain unresolved in canonical Evidence."
    assert c1["text"].endswith(old_tail), c1["text"][-120:]
    c1["text"] = c1["text"][: -len(old_tail)] + ("Code license Apache 2.0 (repo LICENSE since "
          "2025-09-22 inception); selected weights Apache 2.0 within bound model-card scope "
          "(30B-A3B-Instruct).")
    c1["source_ids"] = ["src-1"] + om
    c1["context"] = "Deployment surface per repo; license buckets per supplement bytes."
    c2 = {"statement_id": "claim-2",
          "text": ("Selected released weights Apache 2.0 within bound model-card scope "
                   "(Qwen3-Omni-30B-A3B-Instruct card apache-2.0 since 2025-09-20 initial commits; "
                   "bound artifact model-00001-of-00015.safetensors; no generalization beyond the checked card)."),
          "subject_id": subj, "subject_role": "PRIMARY_SUBJECT",
          "evidence_class": "PROJECT_CLAIM", "source_ids": om[2:],
          "context": "Model-card frontmatter current + pinned initial bytes."}
    card["claims"] = [c1, c2]
    card["limitations"] = [lims["limitation-1"]]
    have = {s["source_id"] for s in card["sources"]}
    by_id = {s["supplement_source_id"]: s for s in core.load_json(out)["sources"]}
    for k in om:
        s = by_id[k]
        card["sources"].append({
            "source_id": s["supplement_source_id"], "url": s["locator"],
            "source_class": s["source_class"], "title": s["title"],
            "published_at": s["published_at"], "accessed_at": s["accessed_at"],
            "role": s["relation"],
        })
    card["verification"]["targets"].append(
        {"target": "License authority repair (code + selected weights)",
         "status": "VERIFIED",
         "finding": "First-party repo LICENSE (current + 2025-09-22 pinned) and model-card README (current + 2025-09-20 pinned) exact bytes bound; obsolete unresolved tail/limitation removed.",
         "subject_ids": [subj], "source_ids": ["src-1"]})

    pkg = core.load_json(root / SRC / f"evidence/v2/accepted/{CURR}/package.json")
    pkg = copy.deepcopy(pkg)
    pkg["authority_supplement"] = {"path": SUP_OUT,
                                   "sha256": core.sha256_file(out)}
    tm = next(m for m in pkg["tasks"] if m["evidence_task_id"] == TID075)
    task = core.load_json(root / SRC / "evidence/v2/accepted" / CURR / tm["path"])
    task = copy.deepcopy(task)
    task["authority_supplement_source_ids"] = sorted(om)
    errors = ev.validate_evidence_card(card, task, tm["sha256"], pkg, repo_root=root)
    assert not errors, errors
    (root / EDIR / "staged-vm-d075-license.json").write_text(
        json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("staged VM-D075 VALID | claims:", len(card["claims"]),
          "| limitations:", len(card["limitations"]), "| status:", card["status"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
