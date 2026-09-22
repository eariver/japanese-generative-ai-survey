#!/usr/bin/env python3
"""TS-001 screening judgments: 165 explicit per-record dispositions.

Operator: Muse (Luna/Work execution role) applying the Core v2 screening
contract (config/prompts/source-screening-v2.md) against the Production
Profile research question. Not a Sol decision. Sol reviews the outcome via
the screening review package.
"""

from __future__ import annotations

import json
from pathlib import Path

TAG = {
    "EFF-O01": "efficiency-fundamentals", "EFF-O02": "scaling-training",
    "EFF-O03": "moe-routing", "EFF-O04": "attention-kv",
    "EFF-O05": "decoding", "EFF-O06": "quantization",
    "EFF-O07": "local-inference", "EFF-O08": "serving",
    "EFF-O09": "distillation-adaptation", "EFF-O10": "specialization-jev",
    "EFF-O11": "capstone-2026", "EFF-O12": "benchmark-methodology",
    "EFF-O13": "conditional-memory", "EFF-O14": "test-time-compute",
    "EFF-O15": "model-routing",
}

# id: (decision, confidence, reason, extra_targets, dup_group)
J = {
"D001": ("KEEP", "high", "Dense-scaling-era origin for the D01 bottleneck model; revised by Chinchilla but required anchor for loss-scaling claims.", [], None),
"D002": ("KEEP", "high", "Compute-optimal scaling anchor (~20 tok/param); motivates the training-token-reduction thread.", [], None),
"D003": ("KEEP", "high", "Iteration-level scheduling origin; prefill/decode split anchoring D01 and D08.", [], None),
"D004": ("KEEP", "high", "2026 instance of D01 distinctions on one model (FP8/FP4/FP8-KV, aggregated vs disaggregated, DSpark topology-conditionality).", ["topology/precision binding at Evidence"], "dynamo-v41-recipe-readings"),
"D005": ("KEEP", "high", "FP8 format/algorithm origin for mixed-precision training and inference.", [], None),
"D006": ("KEEP", "high", "671B MoE FP8 training + MTP objective; mechanism reused by 2026 capstones for speculative decoding.", [], None),
"D007": ("KEEP", "medium", "Muon optimizer reference implementation; adoption claimed by Qwen3.8-Flash-Next and V4-Flash pretraining needs verification.", ["adoption claims in capstone reports"], None),
"D008": ("KEEP", "high", "First-party Qwen3.8-Flash-Next architecture report (125B/6B + 51B host-offloaded n-gram, GDN/QSA, scaling refit).", ["vendor-claimed 1/3 tokens / 1/9 FLOPs quarantine"], None),
"D009": ("KEEP", "medium", "Qwen3-Next ancestor statement for the 3:1 hybrid lineage; announcement-grade, lineage role only.", ["lineage claims vs report"], None),
"D010": ("KEEP", "high", "Sparsely-gated MoE origin: top-k gating, load-balance loss, capacity/compute separation.", [], None),
"D011": ("KEEP", "high", "Production MoE mechanics: expert parallelism, sharded dispatch, capacity factor.", [], None),
"D012": ("KEEP", "high", "Top-1 routing simplification; routing-strategy quality/communication tradeoff.", [], None),
"D013": ("KEEP", "high", "Open-weight MoE adoption anchor outside Chinese labs.", [], None),
"D014": ("KEEP", "high", "Fine-grained + shared experts and device-limited routing; DeepSeek branch mechanism authority.", [], None),
"D015": ("KEEP", "high", "236B/21B MLA + DeepSeekMoE; efficiency as first-class architectural claim.", [], None),
"D016": ("KEEP", "medium", "Qwen dense/MoE breadth preceding efficiency generations; lineage adoption evidence.", [], None),
"D017": ("KEEP", "high", "V4-Flash first-party checkpoint identity (284B/13B, CSA+HCA, mHC, FP4 experts).", ["license/precision variant binding"], None),
"D018": ("KEEP", "high", "MQA origin; KV-footprint reduction thread start.", [], None),
"D019": ("KEEP", "high", "GQA via uptraining; pre-MLA industry-default KV saver.", [], None),
"D020": ("KEEP", "high", "IO-aware exact attention origin; implementation efficiency vs approximation distinction.", [], None),
"D021": ("KEEP", "high", "FA2 parallelism rework; exactness preserved, KV asymptotics unchanged.", [], None),
"D022": ("KEEP", "medium", "FA3 Hopper asynchrony/FP8; hardware-conditional gains instance for Evidence.", ["hardware conditions"], None),
"D023": ("KEEP", "high", "Selective SSM alternative; lineage anchor for GDN/KDA responses.", [], None),
"D024": ("KEEP", "high", "Scalar-gated delta rule; direct parent of KDA and recurrent half of 2026 hybrids.", [], None),
"D025": ("KEEP", "medium", "SWA + GQA local-attention baseline for sparse/retrieval comparisons.", [], None),
"D026": ("KEEP", "high", "Open-world NSA: compress-select-slide trained end-to-end; must be disambiguated vs DSA/CSA/QSA at Evidence.", ["disambiguation vs DSA/CSA/QSA"], None),
"D027": ("KEEP", "high", "Kimi Linear first-party paper (KDA + 3:1 MLA hybrid, NoPE, 48B/3B); vendor win claims quarantined.", ["fair-comparison and KV/decode claims"], None),
"D028": ("KEEP", "high", "Kimi deployment authority: open kernel + vLLM implementation + checkpoints.", ["kernel/runtime version binding"], None),
"D029": ("KEEP", "high", "Qwen Flash-Next first-party README (QSA config, host-offload, self-reported scores).", ["self-reported scores quarantine"], "hf-qwen-card-readings"),
"D030": ("KEEP", "high", "V4.1-Flash first-party card (552B + 196B Engram, CED 8B/16B, CSA2, FP4 KV, DSpark).", ["spec/precision binding"], "hf-v41-card-readings"),
"D031": ("KEEP", "medium", "Official V4.1-Flash launch (KV ratios, API live, pricing); paper URL outstanding at collection.", ["paper/benchmark identity"], None),
"D032": ("INSPECT", "low", "DSA announcement trace with homepage-only locator; dedicated primary URL unisolated, so source identity is insufficient for Evidence.", ["isolate dedicated DSA primary URL"], None),
"D033": ("KEEP", "high", "Speculative-decoding co-origin: draft/verify, lossless, acceptance-rate-governed speedup.", [], None),
"D034": ("KEEP", "high", "Co-origin with acceptance-criterion formalism; joint invention attribution.", [], None),
"D035": ("KEEP", "medium", "Medusa multi-head drafts + tree verification; non-greedy losslessness qualification needed.", ["losslessness scope"], None),
"D036": ("KEEP", "high", "EAGLE feature-level drafts + tree attention; inspired V3 MTP.", [], None),
"D037": ("KEEP", "high", "EAGLE-2 dynamic trees; acceptance-rate science core to decoding lane.", [], None),
"D038": ("KEEP", "high", "MTP training-objective vs decoding-use distinction; mechanism reused by 2026 capstones.", [], None),
"D039": ("KEEP", "high", "Target-native MTP deployment path (GLM-5.3-Flash/DeepSeek-style); no separate draft model.", ["runtime version binding"], None),
"D040": ("KEEP", "high", "DSpark in-checkpoint drafter evidence bundle; no standalone paper exists.", [], None),
"D041": ("KEEP", "high", "LLM.int8 outlier-aware decomposition; constrained-memory inference origin.", [], None),
"D042": ("KEEP", "high", "GPTQ one-shot weight-only PTQ; 3-4 bit perplexity-cost anchor.", [], None),
"D043": ("KEEP", "high", "SmoothQuant difficulty migration enabling W8A8; weight+activation class.", [], None),
"D044": ("KEEP", "high", "AWQ salient-weight protection; strong 4-bit with tiny calibration.", [], None),
"D045": ("KEEP", "high", "QLoRA 4-bit base + adapters; quantization/adaptation interaction.", [], None),
"D046": ("KEEP", "high", "SparseGPT one-shot 50-60% pruning; bounds the no-retraining half.", [], None),
"D047": ("KEEP", "medium", "Native 1-bit training direction; industrial adoption beyond MSR is an open gap for Evidence.", ["adoption status"], None),
"D048": ("KEEP", "high", "GGUF container/format/metadata/mmap authority; explicitly not a quantization algorithm.", [], None),
"D049": ("KEEP", "high", "MXFP4 expert serving evidence; B200-conditional expert_dtype dispatch.", ["hardware conditions"], None),
"D050": ("KEEP", "high", "Reference local-inference implementation for the D07 lane.", ["version/content binding at Evidence"], None),
"D051": ("KEEP", "high", "Heterogeneous CPU/GPU MoE execution; expert-offload answer to capacity-vs-compute.", ["version/content binding at Evidence"], None),
"D052": ("KEEP", "high", "Ascend GLM-5.3-Flash deployment tutorial (quantized serving, MTP config, parsers).", ["tutorial/model-version binding"], None),
"D053": ("KEEP", "high", "PagedAttention origin: paged KV blocks, fragmentation, continuous batching.", [], None),
"D054": ("KEEP", "high", "SGLang + RadixAttention; Day-0 runtime for Qwen Flash-Next and V4.1 recipes.", ["version binding at Evidence"], None),
"D055": ("KEEP", "high", "SGLang paper: RadixAttention + compressed FSM; multi-call agent serving waste.", [], None),
"D056": ("KEEP", "high", "FlashMLA decode kernel; kernel half of MLA story, sparse backend in vLLM V4.1.", [], None),
"D057": ("KEEP", "medium", "FlashMLA-ETAP 2.78x over FlashMLA; stability-accounted reporting standard to verify.", ["stability accounting"], None),
"D058": ("KEEP", "medium", "TensorRT-LLM production stack; Day-0 Qwen Flash-Next support claim needs version/precision binding.", ["version/precision binding"], None),
"D059": ("KEEP", "high", "Splitwise phase-split origin; KV-transfer-for-specialization tradeoff.", [], None),
"D060": ("KEEP", "high", "DistServe disaggregated prefill/decode with SLO-aware placement.", [], None),
"D061": ("KEEP", "high", "Mooncake pooled KV store; context for V4.1 SSD-cache economics.", [], None),
"D062": ("KEEP", "medium", "SARATHI chunked prefill; scheduler refinement between Orca and disaggregation.", [], None),
"D063": ("KEEP", "high", "Same Dynamo V4.1 recipe read through the serving lens: aggregated-vs-disaggregated experiment binding D04/D05/D06/D08.", ["experiment conditions"], "dynamo-v41-recipe-readings"),
"D064": ("KEEP", "high", "DeepEP MoE dispatch/combine; communication half of D03 story.", ["version binding at Evidence"], None),
"D065": ("KEEP", "high", "DeepGEMM fine-grained FP8 matmul; kernel half of FP8 training/inference.", [], None),
"D066": ("KEEP", "medium", "FlashInfer shared kernel substrate for paged/MLA/sparse/speculative paths.", ["version binding at Evidence"], None),
"D067": ("KEEP", "high", "Distillation origin: soft targets, quality/capacity tradeoff frame.", [], None),
"D068": ("KEEP", "high", "LoRA frozen-base adapter efficiency anchor.", [], None),
"D069": ("KEEP", "high", "R1 RL reasoning + distillation into dense students; post-training efficiency lever.", [], None),
"D070": ("KEEP", "high", "Jev launch: new arch + parallel sampler + RLCD, typed outputs; race claim quarantined as vendor claim.", ["race/accuracy claims quarantine"], None),
"D071": ("KEEP", "high", "TypeSafe concept docs: Choice/Score/Noul, parallel isolation, calibration; limits documented.", [], None),
"D072": ("MAYBE", "low", "Jev wiki dated fact snapshot; explicitly not specification authority — corroboration only.", ["fact snapshot vs official docs"], None),
"D073": ("KEEP", "medium", "awesome-jev community reproduction hub; community-grade leads where independent evidence is otherwise thin.", ["lead verification; no peer-reviewed reproduction this pass"], None),
"D074": ("MAYBE", "low", "DataCamp Jev explainer; secondary corroboration of access/pricing only.", ["vs official docs"], None),
"D075": ("MAYBE", "low", "Lambda provider page: specs + provider-measured throughput; secondary, rebind at Evidence.", ["provider measurement conditions"], None),
"D076": ("MAYBE", "low", "DeepInfra price sample for API-economics lane; not official DeepSeek pricing.", ["official pricing"], None),
"D077": ("INSPECT", "low", "Infra-oriented V4.1 parameter study is AI-drafted and UNEDITED; tensor derivations need inspection before Evidence use.", ["verify derivations against report/card"], None),
"D078": ("KEEP", "high", "vLLM deepseek_v41 model code docs; deployment evidence.", ["version binding"], None),
"D079": ("MAYBE", "low", "llm-stats Qwen launch analysis; weights-vs-API split useful but vendor comparisons need quarantine.", ["vendor comparison quarantine"], None),
"D080": ("MAYBE", "medium", "NVIDIA blog Qwen-on-GB300 numbers; condition-bound (prefix-hit) vendor-adjacent benchmark.", ["harness/prefix-hit conditions"], None),
"D081": ("KEEP", "medium", "Qwen Flash-Next official blog; four-aspect upgrade claims as vendor authority.", ["upgrade claims quarantine"], None),
"D082": ("MAYBE", "low", "llm-stats GLM launch analysis; promo-vs-list pricing and vendor comparisons need quarantine.", ["pricing/comparison quarantine"], None),
"D083": ("KEEP", "high", "HF transformers GLM5-next doc; hybrid sparse+linear claims with MTP-layer exclusion noted.", ["MTP exclusion; vendor ratios"], None),
"D084": ("MAYBE", "low", "LM Studio GLM page gloss + vendor benchmark table with harness warning.", ["harness binding"], None),
"D085": ("MAYBE", "low", "NVIDIA NIM GLM card; hybrid claims plus KDA-label collision with Kimi KDA to resolve.", ["KDA disambiguation"], None),
"D086": ("MAYBE", "low", "MiniMax-M2.x materiality watch: no distinct efficiency mechanism confirmed; pursue/park is a later materiality judgment.", ["mechanism confirmation"], None),
"D087": ("MAYBE", "low", "gpt-oss materiality watch: distinct-mechanism contribution unverified; gap-fill locator only.", ["mechanism contribution"], None),
"D088": ("KEEP", "high", "MMLU-Pro reasoning-focused set; version pin at Evidence.", ["version pin"], None),
"D089": ("KEEP", "high", "GPQA Diamond expert science; split/harness binding for capstone citations.", ["split/harness binding"], None),
"D090": ("KEEP", "medium", "HLE saturation-response design; no capstone HLE number this pass — design authority.", [], None),
"D091": ("KEEP", "high", "LiveCodeBench time-windowed anti-contamination code set; version pin mandatory.", ["version pin"], None),
"D092": ("KEEP", "high", "SWE-bench real-issue tasks; base of the Verified/Pro validity thread.", [], None),
"D093": ("INSPECT", "low", "SWE-bench-Pro Which-Pro normalization outstanding with body pending; identity insufficient.", ["isolate exact Pro variant + body"], None),
"D094": ("KEEP", "high", "Terminal-Bench containerized tasks; version suffix proves name-is-not-contract.", ["version suffix"], None),
"D095": ("KEEP", "medium", "BFCL tool-call harness; parser-dependence scaffold risk, paper counterpart at Evidence.", ["paper counterpart; parser dependence"], None),
"D096": ("KEEP", "high", "tau-bench tool-interaction with pass^k consistency semantics.", [], None),
"D097": ("MAYBE", "low", "BrowseComp announcement-grade record; hard browsing benchmark but version/harness outstanding.", ["version/harness"], None),
"D098": ("KEEP", "high", "RULER graded long-context suite; rare joint capability+efficiency datapoint class.", [], None),
"D099": ("MAYBE", "low", "AIME/MAA competition authority; generation/year/CI conditions outstanding.", ["generation/year conditions"], None),
"D100": ("MAYBE", "medium", "DeepSWE best-of-two-harness reporting note; cautionary validity exhibit, standalone primary outstanding.", ["standalone DeepSWE primary"], "hf-qwen-card-readings"),
"D101": ("KEEP", "high", "Megatron-LM tensor parallelism; SCALE/PLACE mechanism, not arithmetic reduction.", [], None),
"D102": ("KEEP", "high", "GPipe micro-batch pipeline + recompute; bubble/memory tradeoff origin.", [], None),
"D103": ("KEEP", "high", "ZeRO sharded states; FIT (memory) mechanism for trillion-parameter training.", [], None),
"D104": ("KEEP", "high", "ZeRO-Offload/Infinity heterogeneous memory; ancestor of host-offload inference thinking.", [], None),
"D105": ("KEEP", "high", "Activation checkpointing recompute-for-memory EXCHANGE; direction must stay explicit.", [], None),
"D106": ("KEEP", "high", "FSDP PyTorch-native ZeRO-3-class sharding; current-stack lineage.", [], None),
"D107": ("KEEP", "high", "DeepSpeed-Ulysses sequence parallelism; training-side context parallelism.", [], None),
"D108": ("KEEP", "high", "Ring Attention blockwise + ring KV exchange; closes r1 G08 absentee.", [], None),
"D109": ("KEEP", "high", "H2O score-driven eviction; category-(3) eviction anchor.", [], None),
"D110": ("KEEP", "high", "StreamingLLM sink + window policy; constrains all eviction claims.", [], None),
"D111": ("KEEP", "high", "SnapKV prompt observation-window voting; prompt-aware category (3).", [], None),
"D112": ("KEEP", "high", "PyramidKV layer-wise budgets; layer-heterogeneity relevant to CSA2 sharing.", [], None),
"D113": ("KEEP", "high", "vLLM automatic prefix caching; granularity contrast vs SGLang radix tree.", ["version binding"], None),
"D114": ("KEEP", "high", "LMCache engine-independent reuse/offload/disaggregation; Mooncake backend.", ["version binding"], None),
"D115": ("KEEP", "medium", "Mixture-of-Depths per-token depth routing; explicitly NOT MoE — precision matters to routing lane.", [], None),
"D116": ("KEEP", "high", "LayerSkip same-model draft + verify; bridges conditional depth and decoding.", [], None),
"D117": ("MAYBE", "low", "DeeBERT minimal early-exit precedent; no LLM-scale claim — bounding only.", [], None),
"D118": ("KEEP", "high", "MLPerf Inference scenario-bound comparability proof (arrival, latency bounds, SLO, audit).", [], None),
"D119": ("INSPECT", "low", "GenAI-Perf locator captured but AIPerf-as-product NOT located; product identity unresolved.", ["locate/confirm AIPerf product identity"], None),
"D120": ("MAYBE", "medium", "LLMPerf included for its caveats; teaches incomparability, not ground truth.", ["caveat scope"], None),
"D121": ("KEEP", "high", "lm-evaluation-harness accuracy-side standard; same-name/different-harness discipline.", [], None),
"D122": ("KEEP", "high", "HELM multi-metric transparency-first harness; reproducibility anchor.", [], None),
"D123": ("KEEP", "high", "V4.1-Flash technical report: CED 8B/16B, pure CSA2, FP4-KV in training, Engram, eval appendix with scaffolds.", ["scaffold/version binding"], None),
"D124": ("KEEP", "high", "V4 technical report: 1.6T/49B Pro + 284B/13B Flash first-party anchor with FLOPs/KV ratios.", ["ratio conditions"], None),
"D125": ("KEEP", "high", "V3.2 report: DSA lightning indexer under MLA with long-context signal; closes r1 G03.", [], None),
"D126": ("KEEP", "medium", "V3.2-Exp launch + API docs: efficiency-to-price transmission event with kernels + weights.", ["price/artifact identity"], None),
"D127": ("KEEP", "high", "Qwen Flash-Next GitHub source of truth: preview-vs-production BOUND, runtime matrix, SWE-Pro footnote normalization.", ["bound/footnote verification"], None),
"D128": ("KEEP", "high", "GLM-5 technical report: 744B/40B first-party ground with cross-lab DSA adoption evidence.", [], None),
"D129": ("KEEP", "high", "zai-org/GLM-5 GitHub: IndexShare FLOPs, MTP acceptance, deployment matrix; IndexPool unresolved.", ["IndexPool resolution"], None),
"D130": ("KEEP", "high", "GLM-5.3-Flash first-party checkpoint identity (MIT, fp8, glm5_next, BF16 sibling).", [], None),
"D131": ("KEEP", "medium", "Z.ai GLM-5.3-Flash docs overview; relative attention/KV ratios vendor-quarantined.", ["ratio quarantine"], None),
"D132": ("KEEP", "high", "KDA open kernel + vLLM path; deployability proof beyond paper.", ["numerics/perf at Evidence"], None),
"D133": ("KEEP", "high", "Expert Choice experts-choose-tokens; third routing point vs top-k vs aux-loss-free.", [], None),
"D134": ("KEEP", "high", "MegaBlocks block-sparse MoE GEMMs; compute twin to DeepEP communication twin.", [], None),
"D135": ("KEEP", "medium", "BitNet b1.58 ternary lineage; industrial deployment still open.", ["deployment status"], None),
"D136": ("KEEP", "high", "OCP MX v1.0 spec; format authority behind V4-line FP4 claims.", [], None),
"D137": ("KEEP", "high", "MX semantics paper; native-low-bit vs PTQ evidence-class distinction.", [], None),
"D138": ("KEEP", "high", "Training-data dedup: selection-driven token efficiency without architecture change.", [], None),
"D139": ("KEEP", "high", "DoReMi mixture optimization; allocation as composition, not just quantity.", [], None),
"D140": ("DROP", "medium", "Collector-flagged park-leaning: synthetic quality-over-quantity with indirect relevance to serving-cost thesis; no distinct efficiency mechanism for this Special.", [], None),
"D141": ("KEEP", "high", "Jev 1.13 Models page: versioned IDs, alias-drift warning, rate limits; card equivalent.", ["version/alias binding"], None),
"D142": ("KEEP", "high", "TypeSafe API reference: answer schema + distribution-derived confidence; records the NOT FOUND for calibration protocol as a finding.", ["calibration protocol gap"], None),
"D143": ("KEEP", "high", "Engram paper: O(1) n-gram lookup, deterministic host offload, U-shaped sparsity allocation; conditional-memory lane origin.", [], None),
"D144": ("KEEP", "high", "Official Engram implementation; addressing/offload implementation evidence.", [], None),
"D145": ("KEEP", "medium", "Qwen N-gram vs Engram lineage assessment with ancestry explicitly NOT inferred; boundary honesty is the contribution.", [], None),
"D146": ("MAYBE", "medium", "kNN-LM explicit-corpus retrieval precedent; boundary-sharpening only vs static lookup.", [], None),
"D147": ("MAYBE", "medium", "RETRO chunked cross-attention precedent; closes the precedent sweep, boundary role only.", [], None),
"D148": ("KEEP", "high", "Snell test-time scaling origin: test-time over parameters for reasoning, difficulty dependence.", [], None),
"D149": ("KEEP", "high", "s1 budget forcing + s1K SFT + sequential/parallel taxonomy; benchmark-specific claims to verify.", ["claim scope"], None),
"D150": ("INSPECT", "low", "ThinkPrune RL pruning record with body unread; weight vs substitute unresolved per collection note.", ["confirm body weight or substitute"], None),
"D151": ("KEEP", "high", "Overthinking peak-then-decline evidence with flip mechanism and cost arithmetic; adaptive-stopping case.", [], None),
"D152": ("MAYBE", "medium", "Reasoning-on-a-Budget survey is secondary-by-design taxonomy; candidate-finder only.", ["primary candidates"], None),
"D153": ("KEEP", "high", "Effort-control binding: V4.1 effort 1-100 + Qwen thinking controls; explicit-budget class evidence.", [], "hf-v41-card-readings"),
"D154": ("KEEP", "high", "FrugalGPT cascade origin: scoring + router + stop judge with sequential-latency limitation noted.", [], None),
"D155": ("KEEP", "high", "RouteLLM preference-data router with transfer limits and staleness bounds stated.", [], None),
"D156": ("MAYBE", "medium", "2026 routing/cascading survey as secondary unifier; follow-up pool, not primary authority.", ["primary follow-ups"], None),
"D157": ("KEEP", "high", "Router fragility under shift; limitation evidence conditioning routing gains.", [], None),
"D158": ("DROP", "medium", "Collector-flagged park-leaning boundary probe: collaboration, not selection; no routing-mechanism contribution.", [], None),
"D159": ("DROP", "medium", "Collector PARK_WITH_REASON: encoder-era bridge off the present decoder-reasoning thesis path.", [], None),
"D160": ("DROP", "medium", "Collector PARK_WITH_REASON: last distinct pre-LLM technique with TinyBERT intentionally not duplicated.", [], None),
"D161": ("DROP", "medium", "Collector PARK_WITH_REASON: training-free metric, not a recovery pipeline; pipeline claims stay thin.", [], None),
"D162": ("KEEP", "medium", "Sol-reviewed X reception ledger (27 obs / 24 accounts / 20 independent); valid reception/deployment/friction signal under X_OBSERVATION boundary — never spec authority.", ["X boundary into Evidence"], None),
"D163": ("KEEP", "high", "V4.1 vLLM recipe: version floor, DSpark-only (MTP-module drop), named AMD verification refusal; separates architecture efficiency from runtime maturity.", ["recipe/version conditions"], None),
"D164": ("KEEP", "high", "Unsloth GLM-5.3-Flash packaging authority: GGUF table + memory-fit guidance; 3.3x MTP claim stays vendor-quarantined.", ["MTP claim independence"], None),
"D165": ("KEEP", "high", "Merged llama.cpp qwen4exp port with vLLM-parity validation and documented gaps; exact implementation authority behind local Qwen signal.", [], None),
}


def main() -> int:
    root = Path(".").resolve()
    recs = {}
    for line in (root / "sources/SP-efficient-llm-2026/discovery/discovery-v2.jsonl").read_text(encoding="utf-8").splitlines():
        if line.strip():
            r = json.loads(line)
            recs[r["discovery_id"]] = r
    assert len(recs) == 165, len(recs)
    decisions = []
    for did in sorted(recs):
        r = recs[did]
        key = did.split("-")[1]
        assert key in J, did
        dec, conf, reason, extra, dup = J[key]
        tags = sorted({TAG[o] for o in r["provenance"]["obligation_ids"] if o in TAG})
        targets = ["Evidence-stage full-body verification"] + extra
        decisions.append({
            "discovery_id": did, "decision": dec, "reason": reason,
            "scope_tags": tags, "duplicate_group": dup,
            "verification_targets": sorted(set(targets)), "confidence": conf,
        })
    doc = {
        "schema_version": "2.0-rc1", "issue_id": "SP-efficient-llm-2026",
        "runner": {"provider": "Muse", "model": "Spark (Luna/Work execution role)",
                   "invocation": "Core v2 screening contract + Production Profile research question; Sol review via screening review package, not a Sol decision",
                   "generated_at": "2026-09-22T02:00:00Z"},
        "decisions": decisions,
    }
    out = root / "sources/SP-efficient-llm-2026/execution/x-completion/interactive-decisions.json"
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from collections import Counter
    print(Counter(d["decision"] for d in decisions))
    print("wrote", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
