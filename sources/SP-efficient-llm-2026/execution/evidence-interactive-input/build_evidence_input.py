"""Build interactive-evidence.json for SP-efficient-llm-2026 from part specs. Validates coverage + target match before writing."""
import json, sys
sys.path.insert(0, "/tmp/opencode/ev-gen")
from part_a import PART_A
from part_b import PART_B
from part_c import PART_C
from part_d import PART_D
from part_e import PART_E

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

SPECS = {}
for part in (PART_A, PART_B, PART_C, PART_D, PART_E):
    for k, v in part.items():
        kk = k if k.startswith("EFF-") else f"EFF-{k}"
        assert kk not in SPECS, f"duplicate {kk}"
        SPECS[kk] = v

disc = {}
with open("/home/eariver/git/japanese-generative-ai-survey/sources/SP-efficient-llm-2026/discovery/discovery-v2.jsonl") as f:
    for line in f:
        line = line.strip()
        if line:
            r = json.loads(line)
            disc[r["discovery_id"]] = r

acc = json.load(open("/home/eariver/git/japanese-generative-ai-survey/sources/SP-efficient-llm-2026/screening/v2/accepted/24bac6aa5c849eb2f6ac46f2162c7333137230cfec2610e908815a0e591b045d/screening-accepted.json"))
dec = {x["discovery_id"]: x["decision"] for x in acc["decisions"]}
non_drop = sorted([d for d, v in dec.items() if v != "DROP"])
print("non-DROP:", len(non_drop))
missing = [d for d in non_drop if d not in SPECS]
extra = [d for d in SPECS if d not in non_drop]
print("missing specs:", missing)
print("extra specs:", extra)
assert not missing and not extra

targets = json.load(open("/tmp/opencode/ev-sources/task-targets.json"))

records = []
for did in non_drop:
    spec = SPECS[did]
    drec = disc[did]
    obs = drec["provenance"].get("obligation_ids", [])
    dims = sorted({d for o in obs for d in OB_TO_DIMS.get(o, [])})
    assert dims, did
    # verification
    ver_list = []
    for target, (st, finding) in spec["ver"].items():
        t = "Evidence-stage full-body verification" if target == "@FULL" else target
        ver_list.append({"target": t, "status": st, "finding": finding})
    expected = set(targets[did])
    got = {v["target"] for v in ver_list}
    assert got == expected, f"{did}: got {sorted(got)} expected {sorted(expected)}"
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
    records.append(rec)

# status/materiality census
from collections import Counter
print(Counter(r["status"] for r in records))
print(Counter(r["materiality"] for r in records))

COMPLETENESS = {
 "obligations": [
  {"obligation_id": "EFF-O01", "status": "SATISFIED", "rationale": "Bottleneck-model core bound by Kaplan/Chinchilla origins, Orca prefill/decode split, and the Dynamo 2026 instance; full-body tables outstanding but no structural gap."},
  {"obligation_id": "EFF-O02", "status": "LIMITATION", "rationale": "19 KEEP core intact (Chinchilla, FP8-training, Muon, distributed-training systems, dedup) but D005 (FP8) and D139 (DoReMi) carry wrong-identity bound locators (gap-fill true IDs recorded) and D140 is an accepted DROP; lane preserved, locator amendment pending Sol."},
  {"obligation_id": "EFF-O03", "status": "LIMITATION", "rationale": "15 KEEP core intact from Shazeer through DeepSeekMoE/Mixtral/MoD/LayerSkip/Expert-Choice/MegaBlocks; D117 (DeeBERT) carries a wrong-identity bound locator (true 2004.12993 recorded); precedent bounding preserved."},
  {"obligation_id": "EFF-O04", "status": "LIMITATION", "rationale": "31 KEEP core intact across MQA/GQA/FA1-3/Mamba/GDN/SWA/NSA/KDA/QSA/MLA-history plus eviction taxonomy; D032 and D077 INSPECT held with partial resolution (DSA URLs isolated; ezyang derivations traced but lead-only); D061/D062/D112 carry wrong-identity locators with true IDs recorded."},
  {"obligation_id": "EFF-O05", "status": "SATISFIED", "rationale": "Full decoding chain bound: speculative co-origins, Medusa, EAGLE/2, MTP objective/use, vLLM MTP path, DSpark bundle with D163-consumed recipe; no structural gap."},
  {"obligation_id": "EFF-O06", "status": "LIMITATION", "rationale": "21 KEEP core intact (LLM.int8/GPTQ/SmoothQuant/AWQ/QLoRA/SparseGPT/BitNet/b1.58/MX/MXFP4 deployment/GGUF boundary); D005 (FP8 origin) carries a wrong-identity bound locator with true ID recorded."},
  {"obligation_id": "EFF-O07", "status": "SATISFIED", "rationale": "GGUF boundary, llama.cpp reference role, KTransformers offload, Ascend tutorial, X local-deployment reception, Unsloth packaging, and llama.cpp Qwen port all bound; no structural gap."},
  {"obligation_id": "EFF-O08", "status": "LIMITATION", "rationale": "30 KEEP core intact (Orca/PagedAttention/SGLang/FlashMLA/serving papers/prefix-cache/LMCache/Dynamo/vLLM recipe); D061 (Mooncake) and D062 (SARATHI) carry wrong-identity bound locators with true IDs recorded."},
  {"obligation_id": "EFF-O09", "status": "LIMITATION", "rationale": "Hinton/LoRA/QLoRA/SparseGPT/R1-distillation core intact; D159-D161 are accepted Screening DROPs (rationale in Sol review); no further gap."},
  {"obligation_id": "EFF-O10", "status": "LIMITATION", "rationale": "Jev first-party core consumed (launch, concepts, models page) with vendor-claim quarantine; independent reproduction/evaluation remains thin (community leads only, F4 unresolved, no calibration protocol located) — stated as the central Jev limitation, not a coverage gap in intake."},
  {"obligation_id": "EFF-O11", "status": "LIMITATION", "rationale": "32 KEEP + 9 MAYBE + 2 INSPECT, zero DROP: all four 2026 capstones bound with first-party reports/cards/repos/recipes; D032/D077 INSPECT partially resolved (DSA URLs isolated; study traced); MiniMax/gpt-oss watches held for Sol pursue/park."},
  {"obligation_id": "EFF-O12", "status": "LIMITATION", "rationale": "14 KEEP methodology core intact (MMLU-Pro/GPQA/HLE/LiveCodeBench/SWE-bench/tau/RULER-role/MLPerf/harness standards) plus GenAI-Perf tooling consumed and AIPerf successor named; D093/D094/D098 carry wrong-identity locators with true identities recorded; D093/D119/D100 held for Sol binding judgment."},
 ],
 "residual_limitations": [
  "Nine bound Discovery locators are wrong-identity arXiv IDs (D005, D061, D062, D093, D094, D098, D112, D117, D139); true identities recorded as gap-fill triggers G-EV-01/03/04/05/06/07/08/09/11, locator amendment deferred to Sol.",
  "Full-body consumption outstanding for most paper records (abstract-level Evidence with explicit scope); captured-but-unconsumed primary bodies listed in the authority-consumption package.",
  "Jev independent reproduction/evaluation remains thin; vendor claims quarantined, not promoted.",
  "AIPerf standalone product surface unconsumed (successor named in NVIDIA docs); MiniMax/gpt-oss mechanism contributions unconfirmed (watches held).",
  "SWE-Pro footnote normalization (D127), version pins (benchmarks, kernels, repos), and per-condition measurement matrices outstanding as stated per-record limitations.",
 ],
 "closure": {
  "targeted_gap_fill_completed": True,
  "limitations": [
   "Nine wrong-identity locators recorded with true identities; amendment deferred to Sol (see residual).",
   "Abstract-level Evidence scope for most papers; full-body tables/proofs outstanding (see residual).",
   "Jev independent evidence thin; AIPerf product surface open; watch items unconfirmed (see residual).",
  ],
  "status": "LIMITED",
 },
}

doc = {
 "schema_version": "2.0-rc1",
 "issue_id": "SP-efficient-llm-2026",
 "runner": {"provider": "opencode", "model": "muse-spark-luna-work",
             "invocation": "TS-001 reissue evidence-materiality-completeness interactive records",
             "generated_at": "2026-09-22T12:00:00Z"},
 "records": records,
 "completeness": COMPLETENESS,
}
out = "/tmp/opencode/ev-gen/interactive-evidence.json"
json.dump(doc, open(out, "w"), indent=1, ensure_ascii=False)
print("wrote", out, len(records), "records")
