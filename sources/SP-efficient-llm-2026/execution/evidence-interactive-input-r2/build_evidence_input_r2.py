#!/usr/bin/env python3
"""Build fresh interactive Evidence input r2 (edition-local).

Derives from the preserved r1 input parts (execution/evidence-interactive-input/,
never overwritten) plus r2 overrides (deeper body consumption + supplement
bindings). Validates exact 160-ID coverage and exact per-task verification-
target match against the Core-built task package (with frozen supplement).
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

R1_DIR = Path(__file__).resolve().parent.parent / "evidence-interactive-input"
sys.path.insert(0, str(R1_DIR))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from part_a import PART_A  # noqa: E402
from part_b import PART_B  # noqa: E402
from part_c import PART_C  # noqa: E402
from part_d import PART_D  # noqa: E402
from part_e import PART_E  # noqa: E402
from overrides_r2 import OVERRIDES_R2  # noqa: E402

OB_TO_DIMS = {
 "EFF-O01": ["efficiency_fundamentals"],
 "EFF-O02": ["scaling_and_training_efficiency"],
 "EFF-O03": ["conditional_compute_moe"],
 "EFF-O04": ["attention_sequence_kv_cache"],
 "EFF-O05": ["decoding_acceleration"],
 "EFF-O06": ["precision_quantization_compression"],
 "EFF-O07": ["model_representation_local_inference"],
 "EFF-O08": ["inference_kernels_serving"],
 "EFF-O09": ["distillation_pruning_adaptation"],
 "EFF-O10": ["specialization_instead_of_generation"],
 "EFF-O11": ["capstone_2026_models"],
 "EFF-O12": ["benchmark_methodology"],
 "EFF-O13": ["attention_sequence_kv_cache", "conditional_compute_moe"],
 "EFF-O14": ["decoding_acceleration"],
 "EFF-O15": ["conditional_compute_moe", "inference_kernels_serving"],
}

REPO = Path(".").resolve()
SUPPLEMENT_SOURCES = {
    e["discovery_id"]: e["supplement_source_id"]
    for e in json.load(open(REPO / "sources/SP-efficient-llm-2026/external/evidence-supplement/evidence-authority-supplement-r1.json"))["sources"]
}
SUPP_BY_DID: dict[str, list[str]] = {}
for e in json.load(open(REPO / "sources/SP-efficient-llm-2026/external/evidence-supplement/evidence-authority-supplement-r1.json"))["sources"]:
    SUPP_BY_DID.setdefault(e["discovery_id"], []).append(e["supplement_source_id"])

COMPLETENESS_R2 = {
 "obligations": [
  {"obligation_id": "EFF-O01", "status": "SATISFIED", "rationale": "Bottleneck-model core bound by Kaplan/Chinchilla origins, Orca prefill/decode split, and the Dynamo 2026 instance; body-level tables outstanding but no structural gap."},
  {"obligation_id": "EFF-O02", "status": "LIMITATION", "rationale": "19 KEEP core intact; D005 (FP8) and D139 (DoReMi) now supplement-bound to verified true identities (bodies abstract-scope); D140 accepted DROP. Lane preserved with explicit scope."},
  {"obligation_id": "EFF-O03", "status": "LIMITATION", "rationale": "15 KEEP core intact through DeepSeekMoE/Mixtral/MoD/LayerSkip/Expert-Choice/MegaBlocks; D117 (DeeBERT) supplement-bound to verified identity (body outstanding)."},
  {"obligation_id": "EFF-O04", "status": "LIMITATION", "rationale": "31 KEEP core intact; V4.1/V3.2/Qwen/Kimi reports body-consumed at section level; D032 supplement-bound to consumed launch authority; D077 lead-only; D061/D062/D112 supplement-bound (bodies abstract-scope). Per-figure pins outstanding."},
  {"obligation_id": "EFF-O05", "status": "SATISFIED", "rationale": "Full decoding chain bound with body-consumed EAGLE/MTP results, Medusa/EAGLE-2/Snell-equivalent mechanisms, vLLM MTP path, and DSpark via consumed recipe; no structural gap."},
  {"obligation_id": "EFF-O06", "status": "LIMITATION", "rationale": "21 KEEP core intact (int8/GPTQ/SmoothQuant/AWQ/QLoRA/SparseGPT/BitNet/b1.58/MX/MXFP4/GGUF); D005 supplement-bound (body outstanding)."},
  {"obligation_id": "EFF-O07", "status": "SATISFIED", "rationale": "GGUF boundary, llama.cpp reference, KTransformers offload, Ascend tutorial, X reception, Unsloth packaging, llama.cpp Qwen port all bound with consumed authorities where load-bearing."},
  {"obligation_id": "EFF-O08", "status": "LIMITATION", "rationale": "30 KEEP core intact; D061 (Mooncake) and D062 (SARATHI + Sarathi-Serve) supplement-bound to verified identities (bodies abstract-scope)."},
  {"obligation_id": "EFF-O09", "status": "LIMITATION", "rationale": "Hinton/LoRA/QLoRA/SparseGPT/R1 core intact; D159-D161 accepted DROPs; no further gap."},
  {"obligation_id": "EFF-O10", "status": "LIMITATION", "rationale": "Jev first-party core consumed (launch/concepts/models) with vendor quarantine; independent reproduction/evaluation still thin (community leads, F4 unresolved, no calibration protocol) — stated limitation."},
  {"obligation_id": "EFF-O11", "status": "LIMITATION", "rationale": "32 KEEP + 9 MAYBE + 2 INSPECT, zero DROP; all four capstones with section-level body consumption; D032 resolved via supplement; D077 lead-only; MiniMax/gpt-oss watches held for Sol pursue/park."},
  {"obligation_id": "EFF-O12", "status": "LIMITATION", "rationale": "14 KEEP methodology core intact; SWE-Pro identity resolved and supplement-bound (section read outstanding); RULER + Terminal-Bench family supplement-bound; GenAI-Perf docs consumed; AIPerf product surface open; harness pins outstanding."},
 ],
 "residual_limitations": [
  "Canonical Discovery locators for D005/D061/D062/D093/D094/D098/D112/D117/D139 remain wrong-identity bytes; citing authority is the frozen-validated supplement (amendment deferred to Sol).",
  "Full-body section/ablation detail outstanding for most paper records as stated per-record; abstract-scope records retained only where claims are scoped accordingly.",
  "Jev independent reproduction/evaluation remains thin; vendor claims quarantined, not promoted.",
  "AIPerf standalone product surface unconsumed (successor named in captured docs); MiniMax/gpt-oss mechanism contributions unconfirmed (watches held).",
  "Per-figure benchmark pins (V4.1 appendix, Qwen ablations, Kimi tables, routing/TTC results) and version pins (kernels, repos, harnesses) outstanding as stated per-record limitations.",
 ],
 "closure": {
  "targeted_gap_fill_completed": True,
  "limitations": [
   "Canonical Discovery locators for D005/D061/D062/D093/D094/D098/D112/D117/D139 remain wrong-identity bytes; citing authority is the frozen-validated supplement (amendment deferred to Sol).",
   "Full-body section/ablation detail outstanding for most paper records as stated per-record; abstract-scope records retained only where claims are scoped accordingly.",
   "Jev independent reproduction/evaluation remains thin; vendor claims quarantined, not promoted.",
   "AIPerf standalone product surface unconsumed (successor named in captured docs); MiniMax/gpt-oss mechanism contributions unconfirmed (watches held).",
   "Per-figure benchmark pins (V4.1 appendix, Qwen ablations, Kimi tables, routing/TTC results) and version pins (kernels, repos, harnesses) outstanding as stated per-record limitations.",
  ],
  "status": "LIMITED",
 },
}


def main() -> int:
    root = Path(".").resolve()
    specs = {}
    for part in (PART_A, PART_B, PART_C, PART_D, PART_E):
        for k, v in part.items():
            kk = k if k.startswith("EFF-") else f"EFF-{k}"
            specs[kk] = v
    for k, v in OVERRIDES_R2.items():
        kk = k if k.startswith("EFF-") else f"EFF-{k}"
        if kk not in specs:
            raise ValueError(f"override targets unknown record: {kk}")
        specs[kk] = v

    disc = {}
    with open(root / "sources/SP-efficient-llm-2026/discovery/discovery-v2.jsonl") as f:
        for line in f:
            line = line.strip()
            if line:
                r = json.loads(line)
                disc[r["discovery_id"]] = r
    acc = json.load(open(root / "sources/SP-efficient-llm-2026/screening/v2/accepted/24bac6aa5c849eb2f6ac46f2162c7333137230cfec2610e908815a0e591b045d/screening-accepted.json"))
    dec = {x["discovery_id"]: x["decision"] for x in acc["decisions"]}
    non_drop = sorted(d for d, v in dec.items() if v != "DROP")
    assert len(non_drop) == 160
    assert set(specs) == set(non_drop), f"coverage drift: {set(non_drop)^set(specs)}"

    targets = json.load(open(root / "sources/SP-efficient-llm-2026/execution/compat/evidence-source-class-projection/task-targets.json"))
    records = []
    for did in non_drop:
        spec = specs[did]
        obs = disc[did]["provenance"].get("obligation_ids", [])
        dims = sorted({d for o in obs for d in OB_TO_DIMS.get(o, [])})
        assert dims, did
        ver_list = []
        for target, (st, finding) in spec["ver"].items():
            t = "Evidence-stage full-body verification" if target == "@FULL" else target
            ver_list.append({"target": t, "status": st, "finding": finding})
        expected = set(targets[did])
        got = {v["target"] for v in ver_list}
        assert got == expected, f"{did}: {sorted(got)} vs {sorted(expected)}"
        eid, cname, etype, org = spec["entity"]
        rec = {
            "discovery_id": did,
            "status": spec["status"],
            "entity": {"entity_id": eid, "canonical_name": cname, "entity_type": etype,
                       "organization": org, "canonical_url": None},
            "artifact_type": spec["artifact"],
            "claims": [{"text": t, "evidence_class": c, "context": ctx} for (t, c, ctx) in spec["claims"]],
            "limitations": spec["limits"],
            "verification": ver_list,
            "materiality": spec["mat"],
            "materiality_rationale": spec["mat_rationale"],
            "scope_dimensions": dims,
            "lineage_role": spec["lineage"],
            "branch_ids": spec["branches"],
            "transition_ids": spec["transitions"],
            "inheritance_note": spec["inherit"],
            "historical_attribution_caveat": spec["caveat"],
        }
        if spec.get("bind_supplement"):
            bindings = SUPP_BY_DID.get(did)
            assert bindings, f"no supplement binding for {did}"
            rec["source_bindings"] = bindings
        records.append(rec)

    print("status:", dict(Counter(r["status"] for r in records)))
    print("materiality:", dict(Counter(r["materiality"] for r in records)))
    print("supplement-bound records:", sum(1 for r in records if "source_bindings" in r))
    doc = {
        "schema_version": "2.0-rc1",
        "issue_id": "SP-efficient-llm-2026",
        "runner": {"provider": "opencode", "model": "muse-spark-luna-work",
                   "invocation": "TS-001 reissue evidence-materiality-completeness interactive records r2 (supplement-bound + body-consumed)",
                   "generated_at": "2026-09-22T15:00:00Z"},
        "records": records,
        "completeness": COMPLETENESS_R2,
    }
    out = root / "sources/SP-efficient-llm-2026/execution/evidence-interactive-input-r2/interactive-evidence-r2.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        raise ValueError(f"refusing to overwrite: {out}")
    json.dump(doc, open(out, "w"), indent=1, ensure_ascii=False)
    print("wrote", out.relative_to(root), len(records), "records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
