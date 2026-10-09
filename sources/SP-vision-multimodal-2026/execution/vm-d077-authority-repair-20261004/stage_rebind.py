#!/usr/bin/env python3
"""Stage the rebound VM-D077 card (STAGED ONLY - no acceptance, no state change).

- claim-1/claim-2 carried (src-1 repo-level).
- claim-3 -> supplement model-card/blog IDs (verified Apache-2.0 + caveat).
- claim-4 -> supplement collection/dataset IDs, wording tightened to verified scope
  (unverified per-dataset specifics removed; individual texts stay unbound).
- PARTIAL kept; limitation-1 kept.
- Validated with canonical validate_evidence_card against an in-memory package/task
  carrying the new supplement binding (mirrors replay mechanics; canonical files
  untouched).
"""
from __future__ import annotations
import copy
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EDIR = SRC / "execution/vm-d077-authority-repair-20261004"
CURR = "4e77d1c6f8bf52ccd7b6e64a1787012c325ade49304884e7d92a44e7305deb22"
TID077 = "evidence:SP-vision-multimodal-2026:9193275622858906"


def sid(url: str) -> str:
    import hashlib
    return "supplement-src-" + hashlib.sha256(url.encode()).hexdigest()[:16]


SUP_8B = sid("https://huggingface.co/allenai/Molmo2-8B")
SUP_O7B = sid("https://huggingface.co/allenai/Molmo2-O-7B")
SUP_BLOG = sid("https://allenai.org/blog/molmo2")
SUP_COLLECTION = sid("https://huggingface.co/collections/allenai/molmo2-data")
SUP_CAP = sid("https://huggingface.co/datasets/allenai/Molmo2-Cap")
SUP_ASK = sid("https://huggingface.co/datasets/allenai/Molmo2-AskModelAnything")
SUP_VQA = sid("https://huggingface.co/datasets/allenai/Molmo2-VideoCapQA")
SUP_SYN = sid("https://huggingface.co/datasets/allenai/Molmo2-SynMultiImageQA")
SUP_VP = sid("https://huggingface.co/datasets/allenai/Molmo2-VideoPoint/raw/main/README.md")
SUP_VT = sid("https://huggingface.co/datasets/allenai/Molmo2-VideoTrack/raw/main/README.md")


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_evidence_v2 as ev
    from scripts import survey_production_v2 as core

    meta = None
    acc = core.load_json(SRC / f"evidence/v2/accepted/{CURR}/evidence-accepted.json")
    for r in acc["results"]:
        if r["evidence_task_id"] == TID077:
            meta = r
    assert meta is not None
    card = core.load_json(SRC / "evidence/v2/accepted" / CURR / "results" / meta["filename"])
    supp_path = EDIR / "evidence-authority-supplement-vm-d077.json"
    supp = core.load_json(supp_path)
    assert len(supp["sources"]) == 10
    assert card["status"] == "PARTIAL"
    by_id = {c["statement_id"]: c for c in card["claims"]}
    assert set(by_id) == {"claim-1", "claim-2", "claim-3", "claim-4"}, set(by_id)

    subj = "ev-vmd077"
    c3 = copy.deepcopy(by_id["claim-3"])
    assert "Apache-2.0 on HuggingFace model cards" in c3["text"]
    c3["source_ids"] = [SUP_8B, SUP_O7B, SUP_BLOG]
    c4 = copy.deepcopy(by_id["claim-4"])
    c4["text"] = ("Released-dataset availability bucket (first-party collection): 9-dataset family "
                   "plus eval splits served with live viewers (collection-verified availability); "
                   "per-dataset ODC-BY-family terms with model-output Terms (OpenAI/Anthropic) and "
                   "CC BY-4.0 video-subset provisions as verified on the checked license sections "
                   "(Cap/AskModelAnything/VideoCapQA/SynMultiImageQA/VideoPoint/VideoTrack); videos "
                   "stored as YouTube IDs requiring separate download; Source Attribution contents unbound.")
    c4["source_ids"] = [SUP_COLLECTION, SUP_CAP, SUP_ASK, SUP_VQA, SUP_SYN, SUP_VP, SUP_VT]
    c4["context"] = "Supplement-bound availability + license pattern (checked sections only)."
    card["claims"] = [by_id["claim-1"], by_id["claim-2"], c3, c4]
    # Narrow the stale unresolved question to the individual-texts level so it no
    # longer contradicts the bucket-bound limitation (same bucket logic, §6).
    # This is part of the VM-D077 correction itself, not a new target.
    vuq = card.get("verification", {}).get("unresolved_questions", [])
    assert vuq == ["data license mix binding: Training-data license mix not bound; carried as INSPECT item for later stages."], vuq
    card["verification"]["unresolved_questions"] = [
        "individual third-party dataset license texts and Source Attribution contents unbound; carried as INSPECT item for later stages."]
    # claim-1/claim-2 keep src-1 (repo-level statements verified 2026-09-30)
    assert by_id["claim-1"]["source_ids"] == ["src-1"] and by_id["claim-2"]["source_ids"] == ["src-1"]
    assert card["status"] == "PARTIAL" and len(card["limitations"]) == 1
    # register supplement sources in the card's own sources array (exact manifest mirror)
    have = {s["source_id"] for s in card["sources"]}
    assert have == {"src-1"}, have
    for s in supp["sources"]:
        card["sources"].append({
            "source_id": s["supplement_source_id"],
            "url": s["locator"],
            "source_class": s["source_class"],
            "title": s["title"],
            "published_at": s["published_at"],
            "accessed_at": s["accessed_at"],
            "role": s["relation"],
        })
    card["verification"]["targets"].append(
        {"target": "Narrow authority repair: claim-3/4 rebound to dedicated supplement",
         "status": "VERIFIED",
         "finding": "Model-card/blog/dataset-collection surfaces re-verified 2026-10-04 (exact bytes, hash-bound supplement); repo-root src-1 attribution removed from HF/publication/collection facts; PARTIAL kept (individual third-party texts unbound).",
         "subject_ids": [subj], "source_ids": ["src-1"]})

    # In-memory supplement binding mirrors replay mechanics (canonical files untouched)
    supp_ids = sorted(s["supplement_source_id"] for s in supp["sources"])
    pkg = core.load_json(SRC / f"evidence/v2/accepted/{CURR}/package.json")
    pkg = copy.deepcopy(pkg)
    pkg["authority_supplement"] = {"path": str(supp_path.relative_to(ROOT)),
                                   "sha256": core.sha256_file(supp_path)}
    task = None
    task_sha = None
    for m in pkg["tasks"]:
        if m["evidence_task_id"] == TID077:
            task = core.load_json(ROOT / SRC / "evidence/v2/accepted" / CURR / m["path"])
            task_sha = m["sha256"]
    assert task is not None
    task = copy.deepcopy(task)
    task["authority_supplement_source_ids"] = supp_ids
    errors = ev.validate_evidence_card(card, task, task_sha, pkg, repo_root=ROOT)
    assert not errors, errors

    outp = EDIR / "staged-vm-d077-rebound.json"
    outp.write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("staged rebound card VALID:", outp.relative_to(ROOT),
          "| claims:", len(card["claims"]), "| status:", card["status"])
    print("claim-3 src:", c3["source_ids"])
    print("claim-4 src:", c4["source_ids"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
