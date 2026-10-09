#!/usr/bin/env python3
"""Build the VM-D077-dedicated Evidence Authority Supplement (Core builder only).

10 first-party snapshots (exact bytes, hash-bound). Existing VM-D112 supplement
is NOT modified or reused. Staged under execution/vm-d077-authority-repair-20261004/.
"""
from __future__ import annotations
import datetime
import hashlib
from pathlib import Path

from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/vm-d077-authority-repair-20261004"
SNAP = f"{EDIR}/snapshots"
OUT = f"{EDIR}/evidence-authority-supplement-vm-d077.json"
SUPPLEMENT_ID = "ts003-narrow-repair-supplement-vm-d077-20261004"
TASK077 = "evidence:SP-vision-multimodal-2026:9193275622858906"

SPECS = [
    ("hf-molmo2-8b-model-card.html", "https://huggingface.co/allenai/Molmo2-8B",
     "Molmo2-8B model card (HF allenai, License apache-2.0 + License and Use)",
     "Model-weight license bucket: header License apache-2.0; License and Use section (research/educational use, third-party academic/non-commercial caveat)."),
    ("hf-molmo2-o-7b-model-card.html", "https://huggingface.co/allenai/Molmo2-O-7B",
     "Molmo2-O-7B model card (HF allenai, License apache-2.0 + License and Use)",
     "Model-weight license corroboration: header License apache-2.0; identical License and Use third-party caveat."),
    ("ai2-blog-molmo2.html", "https://allenai.org/blog/molmo2",
     "Ai2 Molmo 2 announcement publication/blog (Ai2, Dec 2025 + codebase update)",
     "Publication statement: 9-dataset table with scales; footer Apache 2.0 + third-party academic/non-commercial statement; full-codebase release note."),
    ("hf-molmo2-data-collection.html", "https://huggingface.co/collections/allenai/molmo2-data",
     "AllenAI Molmo2 Data collection (HF allenai, 13 items with live viewers)",
     "Dataset availability bucket: 13 collection items (9 family + eval splits) with live viewers; release scope boundary."),
    ("hf-dataset-molmo2-cap.html", "https://huggingface.co/datasets/allenai/Molmo2-Cap",
     "Molmo2-Cap dataset page (HF allenai, License odc-by + License section)",
     "Per-dataset terms: ODC-BY + research/educational use + GPT-4.1/GPT-5 output ToS + third-party academic/noncommercial + Source Attribution reference."),
    ("hf-dataset-askmodelanything.html", "https://huggingface.co/datasets/allenai/Molmo2-AskModelAnything",
     "Molmo2-AskModelAnything dataset page (HF allenai, License odc-by + License section)",
     "Per-dataset terms: ODC-BY + CC BY-4.0 video subset via GCS mapping + GPT output ToS + research/educational use."),
    ("hf-dataset-videocapqa.html", "https://huggingface.co/datasets/allenai/Molmo2-VideoCapQA",
     "Molmo2-VideoCapQA dataset page (HF allenai, License odc-by + License section)",
     "Per-dataset terms: ODC-BY + CC BY-4.0 video subset + GPT output ToS + research/educational use."),
    ("hf-dataset-synmultiimageqa.html", "https://huggingface.co/datasets/allenai/Molmo2-SynMultiImageQA",
     "Molmo2-SynMultiImageQA dataset page (HF allenai, License odc-by + License section)",
     "Per-dataset terms: ODC-BY + Claude-Sonnet-4.5 output Anthropic ToS + GPT-5 output ToU + research/educational use."),
    ("hf-dataset-videopoint-readme.md", "https://huggingface.co/datasets/allenai/Molmo2-VideoPoint/raw/main/README.md",
     "Molmo2-VideoPoint dataset README (HF allenai, license odc-by + License section)",
     "Per-dataset terms: ODC-BY + CC BY-4.0 video subset + GPT output ToS; human-annotated pointing data scope."),
    ("hf-dataset-videotrack-readme.md", "https://huggingface.co/datasets/allenai/Molmo2-VideoTrack/raw/main/README.md",
     "Molmo2-VideoTrack dataset README (HF allenai, license odc-by-1.0 + Video Sources table)",
     "Per-dataset terms: ODC-BY-1.0 + third-party Video Sources table (per-dataset licenses: CC BY-NC-SA, CC BY 4.0, non-commercial, Apache 2.0, MIT, BSD-3, CC0); videos NOT redistributed where restricted."),
]


def main() -> int:
    root = Path(".").resolve()
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    state = core.load_json(root / f"{SRC}/production-state.json")
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
        sid = "supplement-src-" + hashlib.sha256(locator.encode()).hexdigest()[:16]
        sources.append({
            "supplement_source_id": sid,
            "discovery_id": "VM-D077",
            "evidence_task_id": TASK077,
            "locator": locator,
            "source_type": "first_party_release_or_docs",
            "source_class": "PRIMARY_OFFICIAL",
            "title": title,
            "published_at": None,
            "accessed_at": now,
            "raw_path": f"{SNAP}/{fname}",
            "raw_sha256": hashlib.sha256(data).hexdigest(),
            "byte_count": len(data),
            "relation": relation,
        })
    assert len({s["supplement_source_id"] for s in sources}) == len(sources)
    from scripts import survey_agent_tool_v2 as agent_tool
    with agent_tool.current_stage_basis_override():
        out = evidence.build_evidence_authority_supplement(
            root, ISSUE_ID, source_root, discovery_path, scr_acc, sources,
            root / OUT, supplement_id=SUPPLEMENT_ID,
            implementation_sha=core.repository_commit_sha(root))
    print("supplement:", out.relative_to(root), core.sha256_file(out)[:12])
    print("sources:", len(sources))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
