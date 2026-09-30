#!/usr/bin/env python3
"""Build TS-003 Architecture r2 interactive input from the r1 input (Selection byte-identical).

Applies Human REQUEST_CHANGES A-D with regeneration boundary SELECTION_COMPLETE:
 A: page plan 112 target / 120 max (4 / 72 / 16 / 16 / 4)
 B: P15 SUPPORTING reuse of already-selected eval/limitation authorities + extension cross-synthesis map
 C: per-package page budgets + 3 depth classes in publication_extensions
 D: Human-requested reader title in architecture publication_extensions
"""
import copy
import json

IN = "sources/SP-vision-multimodal-2026/execution/selection-architecture-20261001/interactive-selection-architecture.json"
OUT = "sources/SP-vision-multimodal-2026/execution/architecture-r2-20261001/interactive-architecture-r2.json"

READER_TITLE = "Vision & Multimodal AI — 視覚表現から接地・推論・行動へ"
REJECTED_SUBTITLE = "検知・認識からVLM・World Modelへ"

PAGE_BUDGET = {
    "P01": 4, "P02": 6, "P03": 5, "P04": 4, "P05": 7, "P06": 5,
    "P07A": 4, "P07B": 11, "P08": 6, "P09": 10, "P10": 4, "P11": 6,
    "P12": 5, "P13": 6, "P14": 5, "P15": 16,
}

FULL = "FULL_MECHANISM_TREATMENT"
TRANS = "TRANSITION_NODE_TREATMENT"
BRIEF = "BRIEF_CONTEXT_OR_AUTHORITY"

# package_id -> (FULL ids, TRANSITION ids, BRIEF ids); must partition package placements exactly.
DEPTH = {
    "P01": (["VM-D003", "VM-D004"], [], ["VM-D001", "VM-D002"]),
    "P02": (["VM-D006", "VM-D010", "VM-D011", "VM-D012"], ["VM-D005", "VM-D007"], ["VM-D008", "VM-D009"]),
    "P03": (["VM-D013", "VM-D017"], ["VM-D015", "VM-D018"], ["VM-D014", "VM-D016"]),
    "P04": ([], ["VM-D019", "VM-D020", "VM-D021", "VM-D022"], []),
    "P05": (["VM-D026", "VM-D027", "VM-D028"], ["VM-D023", "VM-D024", "VM-D025"], ["VM-D029", "VM-D108", "VM-D109"]),
    "P06": (["VM-D030", "VM-D036"], ["VM-D033", "VM-D034", "VM-D035"], ["VM-D031", "VM-D032"]),
    "P07A": (["VM-D039"], [], ["VM-D037", "VM-D038", "VM-D040"]),
    "P07B": (["VM-D043", "VM-D047", "VM-D050", "VM-D051"],
             ["VM-D041", "VM-D042", "VM-D044", "VM-D045", "VM-D046", "VM-D048", "VM-D049", "VM-D052", "VM-D053", "VM-D056"],
             ["VM-D054", "VM-D055"]),
    "P08": (["VM-D059", "VM-D062"], ["VM-D058", "VM-D060"], ["VM-D057", "VM-D061", "VM-D063"]),
    "P09": (["VM-D065", "VM-D066", "VM-D070", "VM-D071"], ["VM-D067", "VM-D068", "VM-D069"],
            ["VM-D064", "VM-D072", "VM-D073", "VM-D074", "VM-D075", "VM-D076", "VM-D077"]),
    "P10": (["VM-D080"], ["VM-D078"], ["VM-D079", "VM-D081", "VM-D082"]),
    "P11": (["VM-D089"], ["VM-D085", "VM-D088"], ["VM-D083", "VM-D084", "VM-D086", "VM-D087", "VM-D111"]),
    "P12": (["VM-D090", "VM-D091"], ["VM-D092"], []),
    "P13": (["VM-D095", "VM-D097"], ["VM-D093", "VM-D094", "VM-D096", "VM-D098"], ["VM-D099", "VM-D100"]),
    "P14": (["VM-D103", "VM-D105"], ["VM-D101", "VM-D102", "VM-D104"], ["VM-D106", "VM-D107"]),
    # P15: D110 is the explicit PRIMARY; reused SUPPORTING eval/limitation authorities get
    # substantive synthesis treatment (TRANSITION class reads as per-contract synthesis depth in P15).
    "P15": (["VM-D110"],
            ["VM-D108", "VM-D109", "VM-D078", "VM-D079", "VM-D081", "VM-D086", "VM-D087",
             "VM-D072", "VM-D073", "VM-D099", "VM-D100", "VM-D106", "VM-D107"],
            []),
}

# Already-selected SUPPORTING candidates reused by P15 as synthesis authorities (Change B).
P15_REUSE = DEPTH["P15"][1]

P15_EXTRA_REQUIREMENTS = [
    "P15 binds cross-package synthesis authority: P05 DocVQA/ChartQA, P10 MMMU/POPE/MMBench, "
    "P11 Video-MME/LongVideoBench, P09 Gemini-3.x vendor-vs-independent poles, P13 Gemini-Robotics-2/On-Device-2 "
    "limitation evidence, P14 Genie-3 limitation evidence (all reused SUPPORTING, no new candidates)",
    "P15 consumes P12 GUI/Computer-Use evaluation (OSWorld/OSWorld-2.0/SeeClick-ScreenSpot) via the "
    "extension cross-synthesis map; PRIMARY single-destination rule keeps their package home in P12",
    "X01-X04 synthesis threads bound via the extension cross-synthesis map to named already-selected evidence",
    "Methodology-first organizing principle holds: distinct evaluation contracts, no benchmark catalogue, no score ranking",
]

P15_EXTRA_BOUNDARIES = [
    "Reused SUPPORTING authorities change publication role to synthesis evidence; they are not new technical transitions",
    "P15 must not become an OCRBench-centered chapter; OCRBench v2 is one anchor among the bound synthesis set",
]

CROSS_SYNTHESIS_MAP = {
    "p05_document_chart_ocr": ["VM-D108", "VM-D109", "VM-D027", "VM-D028"],
    "p10_hallucination_evidence_use_reasoning": ["VM-D078", "VM-D079", "VM-D080", "VM-D081"],
    "p11_long_video_streaming": ["VM-D086", "VM-D087", "VM-D088", "VM-D089"],
    "p12_gui_computer_use": ["VM-D090", "VM-D091", "VM-D092"],
    "p13_vla_limitation": ["VM-D098", "VM-D099", "VM-D100"],
    "p14_world_model_limitation": ["VM-D103", "VM-D104", "VM-D105", "VM-D106", "VM-D107"],
    "p09_vendor_vs_independent": ["VM-D065", "VM-D070", "VM-D071", "VM-D072", "VM-D073"],
    "x01_data_supervision_post_training": ["VM-D003", "VM-D035", "VM-D051", "VM-D062", "VM-D096"],
    "x02_objective_interface_contracts": ["VM-D010", "VM-D047", "VM-D092", "VM-D097", "VM-D104"],
    "x03_token_context_memory_latency": ["VM-D059", "VM-D065", "VM-D089", "VM-D091", "VM-D100"],
    "x04_reliability_provenance_claim_strength": ["VM-D056", "VM-D080", "VM-D098", "VM-D099", "VM-D100", "VM-D110"],
}


def main() -> int:
    import os
    with open(IN) as f:
        r1 = json.load(f)
    r2 = copy.deepcopy(r1)

    # --- assignments: Selection byte-identical (assert, do not touch) ---
    assert len(r2["assignments"]) == 111
    assert all(a["disposition"] == "SELECTED" for a in r2["assignments"])
    usage = {a["discovery_id"]: a["architecture_usage"] for a in r2["assignments"]}
    for did in P15_REUSE:
        assert usage[did] == "SUPPORTING", did

    # --- packages ---
    by_id = {p["package_id"]: p for p in r2["architecture"]["packages"]}
    assert sorted(usage) == sorted(
        d for p in by_id.values() for d in p["primary_discovery_ids"] + p["supporting_discovery_ids"]
    ), "r1 placement must cover all 111 exactly once"
    # Change B: add reuse set to P15 supporting
    p15 = by_id["P15"]
    assert p15["primary_discovery_ids"] == ["VM-D110"]
    assert p15["supporting_discovery_ids"] == []
    p15["supporting_discovery_ids"] = list(P15_REUSE)
    p15["must_cover_requirements"] = list(p15["must_cover_requirements"]) + P15_EXTRA_REQUIREMENTS
    p15["boundaries"] = list(p15["boundaries"]) + P15_EXTRA_BOUNDARIES

    # Change C: per-package depth budgets; assert partition == placement
    for pid, (full, trans, brief) in DEPTH.items():
        p = by_id[pid]
        placed = set(p["primary_discovery_ids"]) | set(p["supporting_discovery_ids"])
        if pid == "P15":
            placed |= set(P15_REUSE)
        assert set(full) | set(trans) | set(brief) == placed, pid
        assert not (set(full) & set(trans) or set(full) & set(brief) or set(trans) & set(brief)), pid
        p["publication_extensions"] = {
            "page_budget_body_pages": PAGE_BUDGET[pid],
            "depth_classes": {
                FULL: full,
                TRANS: trans,
                BRIEF: brief,
            },
        }
    assert sum(PAGE_BUDGET.values()) == 104, sum(PAGE_BUDGET.values())

    # Change A: page plan 112/120
    r2["architecture"]["page_plan"] = {
        "target_pages": 112,
        "max_pages": 120,
        "notes": ("Front matter 4; Parts I-III (P01-P11) 72 body pages (~69.2%); Part IV endpoints "
                  "(P12-P14) 16 (~15.4%); Part V evaluation/convergence (P15) 16 (~15.4%); back matter 4. "
                  "Body 104 pages; Round E contract holds (I-III 65-72% / IV 13-18% / V 15-20%). "
                  "Depth over brevity; endpoint packages capped regardless of recency; no lane compressed "
                  "to token paragraphs to meet a cap; Part V restored without thinning load-bearing lineages."),
    }

    # Change D + B-map + depth definitions at architecture level
    r2["architecture"]["publication_extensions"] = {
        "reader_title_human_requested_r2": READER_TITLE,
        "reader_title_status": "HUMAN_REQUESTED_R2 / inherited by Draft; machine identity unchanged",
        "rejected_subtitle": REJECTED_SUBTITLE + " (rejected: implies linear predetermined endpoint)",
        "round_e_part_weights": {
            "parts_I_III": "72 body pages, ~69.2% (contract 65-72%)",
            "part_IV": "16 body pages, ~15.4% (contract 13-18%)",
            "part_V": "16 body pages, ~15.4% (contract 15-20%)",
        },
        "depth_class_definitions": {
            FULL: "load-bearing transition or mechanism; prior bottleneck, representation/interface change, mechanism, consequence, limitation, inheritance",
            TRANS: "technically distinct lineage/bridge node; concise substantive comparison vs predecessor/successor (in P15: substantive per-contract synthesis treatment)",
            BRIEF: "predecessor, benchmark, deployment, source-role, or limitation evidence; cited where needed, no forced equal-depth mini-section",
        },
        "p15_cross_package_synthesis_map": CROSS_SYNTHESIS_MAP,
        "regeneration": "r2 from SELECTION_COMPLETE after Human Architecture Review r1 REQUEST_CHANGES; Selection byte-identical",
    }
    r2["architecture"]["architecture_goals"] = list(r2["architecture"]["architecture_goals"]) + [
        "Enforce package-level page/depth budgets so high-density packages (P07B, P09) never collapse into catalogues.",
    ]
    r2["runner"]["invocation"] = ("Architecture r2 regeneration from SELECTION_COMPLETE after Human r1 REQUEST_CHANGES "
                                  "(changes A-D); Selection assignments byte-identical to r1")
    from datetime import datetime, timezone
    r2["runner"]["generated_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    os.makedirs("sources/SP-vision-multimodal-2026/execution/architecture-r2-20261001", exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(r2, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("wrote:", OUT)
    print("P15 supporting reuse:", len(P15_REUSE))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
