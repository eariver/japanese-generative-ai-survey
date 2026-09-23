#!/usr/bin/env python3
"""Build the canonical interactive Selection/Architecture input for SP-efficient-llm-2026.

Edition-local operator tooling (NOT shared Core). Emits the exact input JSON
consumed by the frozen Core runner scripts/run_selection_architecture_v2_interactive.py.

Semantic authority: Sol Evidence Review PASS (execution/reviews/sol-evidence-review-pass-20260922.md)
plus the TS-001 reissue instruction §§6-16. Dispositions: 112 SELECTED / 12 HOLD / 33 REJECT / 3 INSPECT.
"""
from __future__ import annotations

import json
from pathlib import Path

ISSUE_ID = "SP-efficient-llm-2026"
OUT_REL = "sources/SP-efficient-llm-2026/execution/selection-architecture-input/interactive-selection-architecture.json"

PUB = "LONGFORM_SPECIAL"
RES = "THEMATIC"


def sel(usage, pkg, lane, rationale):
    assert usage in ("PRIMARY", "SUPPORTING")
    kind = "primary" if usage == "PRIMARY" else "supporting"
    role = "anchor" if usage == "PRIMARY" else "context"
    return {
        "disposition": "SELECTED",
        "rationale": rationale,
        "architecture_usage": usage,
        "publication_role": f"{PUB}:{pkg}-{kind}",
        "architecture_role": f"{RES}:{lane}-{role}",
        "profile_extensions": {"lane": lane},
    }


def out(disposition, rationale):
    assert disposition in ("HOLD", "REJECT", "INSPECT")
    return {
        "disposition": disposition,
        "rationale": rationale,
        "architecture_usage": "NONE",
        "publication_role": None,
        "architecture_role": None,
        "profile_extensions": {"lane": "unselected"},
    }


# discovery_id -> assignment fields (without discovery_id key)
A = {
    # ---- P1 fundamentals ----
    "EFF-D001": sel("PRIMARY", "p1-bottleneck", "fundamentals",
        "SELECTED PRIMARY P1 anchor: Kaplan scaling-laws origin for the loss-scaling half of the bottleneck contract; revised by Chinchilla but required historical anchor."),
    "EFF-D002": sel("PRIMARY", "p1-bottleneck", "fundamentals",
        "SELECTED PRIMARY P1 anchor: Chinchilla compute-optimal allocation (~20 tok/param) that reframes training efficiency as data/model allocation, not just scale."),
    "EFF-D003": sel("PRIMARY", "p1-bottleneck", "fundamentals",
        "SELECTED PRIMARY P1 anchor: Orca iteration-level scheduling origin establishing the prefill/decode split every later package reasons about."),
    # ---- training / MoE ----
    "EFF-D004": sel("SUPPORTING", "p8-capstone", "capstone",
        "SELECTED SUPPORTING P8: Dynamo V4.1-Flash deployment recipe as the concrete 2026 serving instance of the P1 bottleneck model; release-level authority, body line-level detail outstanding per Card limitation."),
    "EFF-D005": sel("PRIMARY", "p4-precision", "precision",
        "SELECTED PRIMARY P4 anchor: FP8 formats paper grounding low-precision training; supplement-bound to verified true identity 2209.05433, abstract-scope."),
    "EFF-D006": sel("PRIMARY", "p2-scaling-moe", "moe-training",
        "SELECTED PRIMARY P2 anchor: DeepSeek-V3 report (FP8 training at scale + MTP objective) tying precision to training allocation and to the decode package."),
    "EFF-D007": sel("PRIMARY", "p2-scaling-moe", "moe-training",
        "SELECTED PRIMARY P2 anchor: Muon optimizer reference implementation for the optimizer-efficiency thread; implementation authority, convergence-theory detail per Card boundary."),
    "EFF-D008": sel("PRIMARY", "p8-capstone", "capstone",
        "SELECTED PRIMARY P8 anchor: Qwen3.8-Next architecture report, body-consumed (Tab.11, three-axis eval, GR, Muon/stability sections); comparative spine for Qwen alongside D127/D029/D081."),
    "EFF-D009": out("REJECT",
        "REJECT: Qwen3-Next launch announcement superseded for architecture purposes by first-party D008 (body-consumed report), D081 (official blog), and D127 (repo source of truth); announcement adds no distinct citable claim."),
    "EFF-D010": sel("PRIMARY", "p2-scaling-moe", "moe-training",
        "SELECTED PRIMARY P2 anchor: sparsely-gated MoE origin (Shazeer) opening the conditional-compute lineage."),
    "EFF-D011": sel("PRIMARY", "p2-scaling-moe", "moe-training",
        "SELECTED PRIMARY P2 anchor: GShard covering the Switch/GShard-class transition to scaled expert parallelism."),
    "EFF-D012": sel("PRIMARY", "p2-scaling-moe", "moe-training",
        "SELECTED PRIMARY P2 anchor: Switch Transformers (simplified routing at scale), paired with GShard for the transition narrative."),
    "EFF-D013": sel("SUPPORTING", "p2-scaling-moe", "moe-training",
        "SELECTED SUPPORTING P2: Mixtral as Western open-MoE corroboration that sparse experts reached production outside the DeepSeek line."),
    "EFF-D014": sel("PRIMARY", "p2-scaling-moe", "moe-training",
        "SELECTED PRIMARY P2 anchor: DeepSeekMoE fine-grained specialist lexicon bridging classic MoE to the modern DeepSeek line."),
    "EFF-D015": sel("PRIMARY", "p2-scaling-moe", "moe-training",
        "SELECTED PRIMARY P2 anchor: DeepSeek-V2 (strong, economical, efficient MoE) establishing MLA+MoE economics before V3/V4.1."),
    "EFF-D016": out("REJECT",
        "REJECT: Qwen3 family-breadth anchor superseded by D008 (Qwen3.8-Next design report, body-consumed) for every architecture claim this thesis needs; retained breadth narrative is an unnecessary editorial role."),
    "EFF-D017": out("REJECT",
        "REJECT: V4-Flash model card superseded by D030 (V4.1 card, same lineage identity fields) plus D123 (V4.1 report) for architecture claims; predecessor-card identity adds no distinct citable claim."),
    # ---- attention / memory ----
    "EFF-D018": sel("PRIMARY", "p3-attention", "attention-memory",
        "SELECTED PRIMARY P3 anchor: MQA origin (one write-head) for the MHA-to-shared-KV reduction thread."),
    "EFF-D019": sel("PRIMARY", "p3-attention", "attention-memory",
        "SELECTED PRIMARY P3 anchor: GQA generalizing MQA; the grouped-KV design deployed across the 2026 capstones."),
    "EFF-D020": sel("PRIMARY", "p3-attention", "attention-memory",
        "SELECTED PRIMARY P3 anchor: FlashAttention exact-attention-with-better-IO thesis; the contrast point for architectures that change computation/storage."),
    "EFF-D021": out("REJECT",
        "REJECT: FlashAttention-2 version intermediate superseded by D020 (exact-IO thesis origin) plus D056 (current MLA decode kernel) for deployed-kernel claims; version delta adds no distinct thesis claim."),
    "EFF-D022": out("REJECT",
        "REJECT: FlashAttention-3 version intermediate superseded by D020 plus D056 for the same reason as D021; Hopper-kernel detail is an unnecessary editorial role here."),
    "EFF-D023": out("REJECT",
        "REJECT: Mamba SSM-origin detail superseded for the linear-attention narrative by D024 (GDN, direct Kimi Linear lineage) plus D027; SSM taxonomy is beyond this thesis scope."),
    "EFF-D024": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3: Gated DeltaNet as the direct recurrent/linear lineage into Kimi Linear; abstract-scope."),
    "EFF-D025": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3: Mistral 7B sliding-window anchor for the sparse/local attention thread."),
    "EFF-D026": sel("PRIMARY", "p3-attention", "attention-memory",
        "SELECTED PRIMARY P3 anchor: Native Sparse Attention for learned sparse/local attention; abstract-scope, ablations outstanding."),
    "EFF-D027": sel("PRIMARY", "p3-attention", "attention-memory",
        "SELECTED PRIMARY P3 anchor: Kimi Linear report, body-consumed (3:1 interleave, DPLR, drop-in compat, license fact); linear-attention capstone mechanism."),
    "EFF-D028": sel("PRIMARY", "p8-capstone", "capstone",
        "SELECTED PRIMARY P8 anchor: Kimi-Linear repo (KDA kernel, vLLM path, checkpoints) as Kimi implementation ground complementing the D027 report anchor in P3."),
    "EFF-D029": sel("SUPPORTING", "p3-attention", "capstone",
        "SELECTED SUPPORTING P3+P8: Qwen README (QSA config, scores) binding QSA attention claims for the attention package and Qwen score conditions for the capstone comparison; vendor scores quarantined to stated conditions."),
    "EFF-D030": sel("PRIMARY", "p8-capstone", "capstone",
        "SELECTED PRIMARY P8 anchor: V4.1-Flash model card (CED, CSA2, Engram, DSpark identity) as the V4.1 checkpoint-identity authority."),
    "EFF-D031": out("REJECT",
        "REJECT: V4.1-Flash launch announcement superseded by D123 (body-consumed report), D030 (model card), and D126 (V-series launch lineage); announcement adds no distinct citable claim."),
    "EFF-D032": sel("PRIMARY", "p3-attention", "attention-memory",
        "SELECTED PRIMARY P3 anchor: DSA announcement trace, VERIFIED via launch Raw plus supplement; former INSPECT closed; DSA-debut authority with homepage-locator boundary resolved."),
    # ---- decoding / TTC ----
    "EFF-D033": sel("PRIMARY", "p5-decode", "decoding-ttc",
        "SELECTED PRIMARY P5 anchor: Leviathan speculative-decoding origin (draft/target framing) for the stop-waiting-serially arc."),
    "EFF-D034": sel("SUPPORTING", "p5-decode", "decoding-ttc",
        "SELECTED SUPPORTING P5: Chen speculative-sampling companion origin corroborating the draft/verify mechanism; D033 carries the primary framing."),
    "EFF-D035": sel("SUPPORTING", "p5-decode", "decoding-ttc",
        "SELECTED SUPPORTING P5: Medusa multi-head draft precedent bridging early speculation to EAGLE/MTP adoption."),
    "EFF-D036": sel("PRIMARY", "p5-decode", "decoding-ttc",
        "SELECTED PRIMARY P5 anchor: EAGLE, VERIFIED with speedups and guarantee scope consumed; current-adoption core of P5."),
    "EFF-D037": sel("SUPPORTING", "p5-decode", "decoding-ttc",
        "SELECTED SUPPORTING P5: EAGLE-2 dynamic draft trees corroborating EAGLE evolution; D036 carries primary claims."),
    "EFF-D038": sel("PRIMARY", "p5-decode", "decoding-ttc",
        "SELECTED PRIMARY P5 anchor: MTP paper (mechanism plus HumanEval/MBPP gains consumed) tying multi-token prediction to training and serving adoption."),
    "EFF-D039": sel("SUPPORTING", "p5-decode", "decoding-ttc",
        "SELECTED SUPPORTING P5: vLLM MTP speculative-decoding docs as implementation authority; release-level, line-level detail per Card boundary."),
    "EFF-D040": sel("SUPPORTING", "p6-serving", "serving",
        "SELECTED SUPPORTING P6+P8: DSpark evidence bundle (vLLM deepseek_v41 plus Dynamo recipe) as serving/runtime corroboration for V4.1; release-level."),
    # ---- precision / local ----
    "EFF-D041": sel("PRIMARY", "p4-precision", "precision",
        "SELECTED PRIMARY P4 anchor: LLM.int8() 8-bit matmul origin opening the bit-reduction thread."),
    "EFF-D042": sel("PRIMARY", "p4-precision", "precision",
        "SELECTED PRIMARY P4 anchor: GPTQ as the practical post-training quantization workhorse for local deployment."),
    "EFF-D043": sel("SUPPORTING", "p4-precision", "precision",
        "SELECTED SUPPORTING P4: SmoothQuant corroborating activation-aware scaling; AWQ/GPTQ carry primary practical claims."),
    "EFF-D044": sel("SUPPORTING", "p4-precision", "precision",
        "SELECTED SUPPORTING P4: AWQ activation-aware quantization corroboration; method detail abstract-scope."),
    "EFF-D045": sel("PRIMARY", "p4-precision", "precision",
        "SELECTED PRIMARY P4 anchor: QLoRA tying quantization to adaptation for hand-held fine-tuning economics."),
    "EFF-D046": out("REJECT",
        "REJECT: SparseGPT unstructured-sparsity claims superseded for this thesis by GPTQ/AWQ (practical quantization lane) plus D150 (pruning-as-efficiency via reasoning); no deployment path in the local-inference narrative needs it."),
    "EFF-D047": sel("SUPPORTING", "p4-precision", "precision",
        "SELECTED SUPPORTING P4: BitNet 1-bit origin for the low-bit/native-low-bit boundary discussion; full-body training detail outstanding, 40-target UNRESOLVED t2 noted."),
    "EFF-D048": sel("PRIMARY", "p4-precision", "precision",
        "SELECTED PRIMARY P4 anchor: GGUF specification authority with the mandatory boundary that GGUF is a representation format, not a quantization algorithm."),
    "EFF-D049": sel("SUPPORTING", "p4-precision", "precision",
        "SELECTED SUPPORTING P4: MXFP4/FP4-expert deployment evidence binding the FP4 story from V4-line training to vLLM dispatch; release-level."),
    "EFF-D050": sel("PRIMARY", "p4-precision", "precision",
        "SELECTED PRIMARY P4 anchor: llama.cpp (GGML history, GGUF runtime, k-quants, CPU/GPU split) as the local-inference runtime spine; body line-level detail outstanding."),
    "EFF-D051": sel("SUPPORTING", "p4-precision", "precision",
        "SELECTED SUPPORTING P4: KTransformers heterogeneous CPU/GPU MoE execution corroborating the weight-memory reality for MoE local runs; body outstanding."),
    "EFF-D052": out("REJECT",
        "REJECT: vLLM Ascend GLM tutorial superseded by D163 (vLLM deployment authority, VERIFIED) plus D129 (GLM deployment matrix) for serving claims; Ascend-specific tutorial is an unnecessary editorial role."),
    # ---- serving ----
    "EFF-D053": sel("PRIMARY", "p6-serving", "serving",
        "SELECTED PRIMARY P6 anchor: PagedAttention/vLLM (SOSP'23) origin; production efficiency does not follow from architecture efficiency alone."),
    "EFF-D054": out("REJECT",
        "REJECT: SGLang repo superseded by D055 (paper carrying RadixAttention mechanism) for architecture claims; living-repo artifact adds no distinct citable claim for this package."),
    "EFF-D055": sel("PRIMARY", "p6-serving", "serving",
        "SELECTED PRIMARY P6 anchor: SGLang paper (structured-program execution, RadixAttention) for prefix/KV-reuse systematization."),
    "EFF-D056": sel("SUPPORTING", "p3-attention", "serving",
        "SELECTED SUPPORTING P3+P6: FlashMLA decode kernel corroborating MLA inference reality; release-level, H20/ETAP detail excluded per D057 rejection."),
    "EFF-D057": out("REJECT",
        "REJECT: FlashMLA-ETAP H20-specific case superseded by D056 for MLA-kernel claims; export-constrained hardware detail is an unnecessary editorial role."),
    "EFF-D058": out("REJECT",
        "REJECT: TensorRT-LLM production stack detail superseded by D066 (FlashInfer kernels) plus vLLM/SGLang runtime anchors for the kernel/runtime lane; vendor-stack depth is unnecessary here."),
    "EFF-D059": sel("PRIMARY", "p6-serving", "serving",
        "SELECTED PRIMARY P6 anchor: Splitwise prefill/decode disaggregation origin for the disaggregation thread."),
    "EFF-D060": out("REJECT",
        "REJECT: DistServe disaggregated-SLO placement detail superseded by D059 (disaggregation origin) plus D061 (disaggregated store); placement nuance is an unnecessary editorial role."),
    "EFF-D061": sel("PRIMARY", "p6-serving", "serving",
        "SELECTED PRIMARY P6 anchor: Mooncake KV-cache-centric disaggregated store; supplement-bound to verified identity 2407.00079, abstract-scope."),
    "EFF-D062": sel("PRIMARY", "p6-serving", "serving",
        "SELECTED PRIMARY P6 anchor: SARATHI chunked-prefill lineage (2023 paper plus 2024 Sarathi-Serve follow-up bound additively); supplement-verified identities."),
    "EFF-D063": out("REJECT",
        "REJECT: Dynamo serving-lens recipe reading superseded by D004 (deployment recipe) plus D163 (VERIFIED vLLM recipe) for Dynamo serving claims; second Dynamo reading is redundant."),
    "EFF-D064": sel("SUPPORTING", "p6-serving", "serving",
        "SELECTED SUPPORTING P6: DeepEP expert-parallel communication library corroborating MoE communication cost; body outstanding."),
    "EFF-D065": sel("SUPPORTING", "p2-scaling-moe", "serving",
        "SELECTED SUPPORTING P2+P6: DeepGEMM FP8 GEMM library tying low-precision training substrate (P2) to serving kernels (P6); body outstanding."),
    "EFF-D066": sel("SUPPORTING", "p6-serving", "serving",
        "SELECTED SUPPORTING P6: FlashInfer AI serving kernels corroborating the production kernel stack; body outstanding."),
    "EFF-D067": sel("SUPPORTING", "p2-scaling-moe", "moe-training",
        "SELECTED SUPPORTING P2: Hinton distillation origin for the train-only-what-is-useful lineage; bounding role, not a deployment claim."),
    "EFF-D068": sel("SUPPORTING", "p2-scaling-moe", "moe-training",
        "SELECTED SUPPORTING P2: LoRA low-rank adaptation origin feeding the QLoRA adaptation story in P4; method detail abstract-scope."),
    "EFF-D069": sel("SUPPORTING", "p5-decode", "decoding-ttc",
        "SELECTED SUPPORTING P5: DeepSeek-R1 plus distilled models as reasoning-model context for the test-time-compute arc; distillation claims bounded."),
    # ---- Jev ----
    "EFF-D070": sel("PRIMARY", "p7-routing", "routing-kasane",
        "SELECTED PRIMARY P7 anchor: Jev TypeSafe launch, VERIFIED first-party pages consumed; mandatory specialization case, vendor claims bounded by thin independent reproduction."),
    "EFF-D071": sel("PRIMARY", "p7-routing", "routing-kasane",
        "SELECTED PRIMARY P7 anchor: TypeSafe System One concepts plus introduction docs, VERIFIED; suitability and task-class bounds documented."),
    "EFF-D072": sel("SUPPORTING", "p7-routing", "routing-kasane",
        "SELECTED SUPPORTING P7: Jev wiki dated model-card fact snapshot as timeline corroboration only; former MAYBE resolved as CONTEXT, explicitly not specification authority."),
    "EFF-D073": sel("SUPPORTING", "p7-routing", "routing-kasane",
        "SELECTED SUPPORTING P7: awesome-jev community reproduction hub documenting community attempt activity around Jev; corroboration only, KEEP-origin CONTEXT."),
    "EFF-D074": out("HOLD",
        "HOLD: DataCamp Jev access/pricing explainer held; access and pricing facts are covered by first-party D070/D141, so the secondary explainer adds no unique authority for this architecture. Former MAYBE with explicit park rationale."),
    "EFF-D075": out("REJECT",
        "REJECT: Lambda provider page superseded by first-party D030/D129 for specification facts; provider-measured throughput is quarantined per authority boundary and carries no unique deployment claim. Former MAYBE with explicit rationale."),
    "EFF-D076": out("HOLD",
        "HOLD: DeepInfra API pricing snapshot held; API-economics is not load-bearing for the mechanism-stack thesis and D153 effort-binding plus first-party pricing carry the cost discussion. Former MAYBE with explicit park rationale."),
    "EFF-D077": out("INSPECT",
        "INSPECT: AI-drafted UNEDITED V4.1 parameter study held for inspection; tensor derivations must be inspected before any architecture use. Former INSPECT retained as INSPECT with explicit reason, not silently promoted."),
    "EFF-D078": sel("SUPPORTING", "p6-serving", "serving",
        "SELECTED SUPPORTING P6+P8: vLLM deepseek_v41 model code docs as runtime-implementation corroboration; body outstanding."),
    "EFF-D079": out("HOLD",
        "HOLD: llm-stats Qwen launch analysis held; weights-vs-API split is useful but vendor comparisons need quarantine and first-party D008/D081/D127 cover launch facts. Former MAYBE with explicit park rationale."),
    "EFF-D080": sel("SUPPORTING", "p8-capstone", "capstone",
        "SELECTED SUPPORTING P8: NVIDIA GB300 Qwen deployment blog as deployment-existence evidence with explicit prefix-hit-conditioned boundary; vendor-adjacent numbers quarantined. Former MAYBE resolved as bounded SUPPORTING."),
    "EFF-D081": sel("SUPPORTING", "p8-capstone", "capstone",
        "SELECTED SUPPORTING P8: Qwen3.8-Flash-Next official blog as first-party launch-claim authority alongside D008/D127."),
    "EFF-D082": out("HOLD",
        "HOLD: llm-stats GLM launch analysis held for the same reason as D079; promo-vs-list pricing needs quarantine and first-party GLM authorities (D128-D131) cover launch facts. Former MAYBE with explicit park rationale."),
    "EFF-D083": out("REJECT",
        "REJECT: HF transformers GLM doc superseded by D131 (Z.ai developer docs) plus D130 (model card) for GLM-5.3 facts; integration-doc angle adds no distinct mechanism claim."),
    "EFF-D084": out("INSPECT",
        "INSPECT: LM Studio GLM page held for inspection; vendor benchmark table carries a harness warning and IndexPool-adjacent claims need inspection before use. Former MAYBE retained as INSPECT."),
    "EFF-D085": out("INSPECT",
        "INSPECT: NVIDIA NIM GLM card held for inspection; hybrid claims plus the KDA-label collision with Kimi KDA must be resolved before architecture use. Former MAYBE retained as INSPECT."),
    "EFF-D086": out("HOLD",
        "HOLD: MiniMax-M2.x materiality watch held; no distinct efficiency mechanism confirmed, so pursue/park remains a later materiality judgment, not an architecture placement. Former MAYBE with explicit watch rationale."),
    "EFF-D087": out("HOLD",
        "HOLD: gpt-oss open-weight watch held; distinct-mechanism contribution unverified and gap-fill-locator-only. Former MAYBE with explicit watch rationale."),
    # ---- benchmarks ----
    "EFF-D088": out("REJECT",
        "REJECT: MMLU-Pro benchmark-definition authority not selected; P9 teaches methodology through validity exhibits (D092/D093/D098/D118) and P8 compares mechanism stacks, not leaderboard ranks, so per-benchmark definition pages are unnecessary editorial roles. No headline number is load-bearing."),
    "EFF-D089": out("REJECT",
        "REJECT: GPQA Diamond not selected for the same reason as D088; reasoning-eval grounding travels with capstone Evidence Cards under stated conditions, not with standalone definition authority."),
    "EFF-D090": out("REJECT",
        "REJECT: Humanity's Last Exam not selected for the same reason as D088; saturation/version-drift claims cite P9 methodology exhibits, not each harness."),
    "EFF-D091": out("REJECT",
        "REJECT: LiveCodeBench not selected for the same reason as D088; code-eval validity is carried by D093/D094/D100 exhibits."),
    "EFF-D092": sel("PRIMARY", "p9-measure", "methodology",
        "SELECTED PRIMARY P9 anchor: SWE-bench grounding the Verified/Pro distinction the methodology package turns on."),
    "EFF-D093": sel("PRIMARY", "p9-measure", "methodology",
        "SELECTED PRIMARY P9 anchor: SWE-bench-Pro validity-evolution case; former INSPECT closed via supplement identity plus captured full text, section-level consumption outstanding as stated boundary."),
    "EFF-D094": sel("PRIMARY", "p9-measure", "methodology",
        "SELECTED PRIMARY P9 anchor: Terminal-Bench agentic/tool-access case; supplement-bound to verified 2.0 identity, v1-ID boundary noted."),
    "EFF-D095": out("REJECT",
        "REJECT: BFCL leaderboard repo not selected; function-calling/task-cost representation is carried by D096-class agentic exhibits plus D100 harness-dependence note, and per-harness authority is unnecessary here for the same D088 reason."),
    "EFF-D096": out("REJECT",
        "REJECT: tau-bench not selected; agentic task-cost argument is carried by D094 (Terminal-Bench) plus D100, so a second agent-harness authority is an unnecessary editorial role."),
    "EFF-D097": out("HOLD",
        "HOLD: BrowseComp announcement-grade record held; version/harness outstanding and RULER/T-Bench carry the agent/long-context validity exhibits. Former MAYBE with explicit park rationale."),
    "EFF-D098": sel("PRIMARY", "p9-measure", "methodology",
        "SELECTED PRIMARY P9 anchor: RULER long-context retrieval/reasoning validity case; supplement-bound to verified identity 2404.06654, abstract-scope."),
    "EFF-D099": out("HOLD",
        "HOLD: AIME/MAA competition authority held; generation/year/CI conditions outstanding and the reasoning-budget discussion does not need contest rules. Former MAYBE with explicit park rationale."),
    "EFF-D100": sel("SUPPORTING", "p9-measure", "methodology",
        "SELECTED SUPPORTING P9: DeepSWE methodology note as the harness-dependence cautionary exhibit; standalone primary outstanding per Card boundary. Former MAYBE resolved as bounded SUPPORTING."),
    # ---- training systems / KV cache ----
    "EFF-D101": sel("SUPPORTING", "p2-scaling-moe", "moe-training",
        "SELECTED SUPPORTING P2: Megatron-LM tensor model-parallelism origin for the training-allocation context; parallelism detail bounded."),
    "EFF-D102": out("REJECT",
        "REJECT: GPipe pipeline-parallelism detail superseded by D101 (tensor-parallel origin) plus D103 (memory sharding) for the training-allocation context this thesis needs."),
    "EFF-D103": sel("SUPPORTING", "p2-scaling-moe", "moe-training",
        "SELECTED SUPPORTING P2: ZeRO memory-sharding anchor for trillion-parameter training memory economics."),
    "EFF-D104": out("REJECT",
        "REJECT: ZeRO-Offload/Infinity heterogeneous-memory detail superseded by D103 for memory-sharding claims; offload depth is an unnecessary editorial role."),
    "EFF-D105": out("REJECT",
        "REJECT: Activation-checkpointing origin detail superseded by D103/D101 for the training-memory narrative; sublinear-memory technique depth is beyond this inference-efficiency thesis scope."),
    "EFF-D106": out("REJECT",
        "REJECT: FSDP productization detail superseded by D103 (ZeRO lineage) for sharding claims; PyTorch-packaging angle adds no distinct mechanism."),
    "EFF-D107": out("REJECT",
        "REJECT: DeepSpeed-Ulysses sequence-parallelism detail superseded by D108-class long-context parallelism framing, itself out of scope (see D108); training-time sequence detail unnecessary."),
    "EFF-D108": out("REJECT",
        "REJECT: Ring Attention training-time sequence parallelism out of inference-thesis scope; inference long-context is carried by D026/D027/D098, so this is an unnecessary editorial role."),
    "EFF-D109": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3: H2O heavy-hitter oracle for eviction-style KV budgeting; abstract-scope."),
    "EFF-D110": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3: StreamingLLM attention-sinks landmark for streaming KV retention; abstract-scope."),
    "EFF-D111": out("REJECT",
        "REJECT: SnapKV clustering-window detail superseded by H2O (heavy-hitter, D109) plus PyramidKV (layer-budgeting, D112) for the KV-budgeting narrative; fourth eviction method is an unnecessary editorial role."),
    "EFF-D112": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3: PyramidKV pyramidal layer-budgeting; supplement-bound to verified identity 2406.02069 with wrong-locator boundary preserved."),
    "EFF-D113": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3+P6: vLLM automatic prefix caching docs binding prefix/KV-reuse claims across memory and serving packages; release-level."),
    "EFF-D114": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3+P6: LMCache external KV-cache layer corroborating cache/offload practice; body outstanding."),
    "EFF-D115": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3: Mixture-of-Depths conditional-depth precedent for compute-that-adapts-per-token; abstract-scope."),
    "EFF-D116": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3: LayerSkip self-speculative early-exit bridging conditional compute to the P5 decode arc; abstract-scope."),
    "EFF-D117": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3: DeeBERT earliest early-exit lineage anchor, one-line bounding role only with no LLM-scale claim. Former MAYBE resolved as narrow SUPPORTING; supplement-bound to verified identity 2004.12993."),
    "EFF-D118": sel("PRIMARY", "p9-measure", "methodology",
        "SELECTED PRIMARY P9 anchor: MLPerf Inference methodology standard for TTFT/TPOT/throughput/concurrency binding; release-level, version pin per Card boundary."),
    "EFF-D119": sel("SUPPORTING", "p9-measure", "methodology",
        "SELECTED SUPPORTING P9: GenAI-Perf docs consumed and bound as LLM-benchmarking tooling authority; AIPerf-as-product remains open per stated limitation. Former INSPECT closed as bounded SUPPORTING."),
    "EFF-D120": sel("SUPPORTING", "p9-measure", "methodology",
        "SELECTED SUPPORTING P9: LLMPerf included for its caveats, teaching incomparability rather than ground truth. Former MAYBE resolved as cautionary SUPPORTING."),
    "EFF-D121": sel("SUPPORTING", "p9-measure", "methodology",
        "SELECTED SUPPORTING P9: lm-evaluation-harness as the standard open harness reference; version pin per Card boundary."),
    "EFF-D122": sel("SUPPORTING", "p9-measure", "methodology",
        "SELECTED SUPPORTING P9: HELM holistic-evaluation reference for beyond-accuracy methodology framing."),
    # ---- capstone line ----
    "EFF-D123": sel("PRIMARY", "p8-capstone", "capstone",
        "SELECTED PRIMARY P8 anchor: DeepSeek-V4.1-Flash technical report, body-consumed at section level (CSA2 modes, FP4-KV training, SWA replay, appendix map, post-training pipeline); per-figure pins open per Card boundary."),
    "EFF-D124": out("REJECT",
        "REJECT: DeepSeek-V4 report (section-structure-level only) superseded by D123 (body-consumed V4.1 report) plus D032/D126 for V-line lineage; predecessor structure adds no citable claim beyond the lineage pointer D123 already carries."),
    "EFF-D125": sel("PRIMARY", "p3-attention", "attention-memory",
        "SELECTED PRIMARY P3 anchor: DeepSeek-V3.2 report as the DSA mechanism primary (indexer equations, ReLU/FP8, MLA-MQA consumed); V3.2 lineage presence in P8 travels via D126."),
    "EFF-D126": sel("SUPPORTING", "p3-attention", "capstone",
        "SELECTED SUPPORTING P3+P8: V3.2-Exp launch plus API docs as DSA-debut lineage authority (50%+ price-cut debut framing); launch-page scope."),
    "EFF-D127": sel("SUPPORTING", "p8-capstone", "capstone",
        "SELECTED SUPPORTING P8: Qwen GitHub repo as report-plus-README source of truth complementing the D008 report anchor; body line-level detail outstanding."),
    "EFF-D128": sel("PRIMARY", "p8-capstone", "capstone",
        "SELECTED PRIMARY P8 anchor with MANDATORY scope boundary: GLM-5 technical report is PRIMARY but abstract-scope for the material claims presently consumed (abstract consumed; full-body DSA details, RL infrastructure, benchmark tables NOT consumed). Mixed-authority-depth lineage member; NEVER described as full-body verified. D128 remains usable as bounded primary authority."),
    "EFF-D129": sel("SUPPORTING", "p8-capstone", "capstone",
        "SELECTED SUPPORTING P8: GLM-5 GitHub repo (IndexShare, MTP, deployment matrix) corroborating GLM lineage depth beyond the D128 abstract; body outstanding."),
    "EFF-D130": sel("SUPPORTING", "p8-capstone", "capstone",
        "SELECTED SUPPORTING P8: GLM-5.3-Flash model card as first-party checkpoint-identity authority for the GLM capstone member."),
    "EFF-D131": sel("SUPPORTING", "p8-capstone", "capstone",
        "SELECTED SUPPORTING P8: Z.ai developer docs GLM overview as first-party capability-claim authority; vendor ratios quarantined."),
    "EFF-D132": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3+P8: KDA kernel implementation (FLA) plus vLLM path binding Kimi Linear kernel claims; body outstanding, KDA-label collision with D085 noted as unresolved."),
    "EFF-D133": sel("SUPPORTING", "p2-scaling-moe", "moe-training",
        "SELECTED SUPPORTING P2: Expert Choice Routing as the expert-choice routing variant bounding the token-choice routing narrative; abstract-scope."),
    "EFF-D134": out("REJECT",
        "REJECT: MegaBlocks MoE compute-substrate detail superseded by D064 (DeepEP communication library) plus D014 for expert-parallel narrative; historical substrate depth is an unnecessary editorial role."),
    "EFF-D135": sel("SUPPORTING", "p4-precision", "precision",
        "SELECTED SUPPORTING P4: BitNet b1.58 native-ternary lineage for the native-low-bit side of the boundary with D047; non-MSR industrial deployment remains not-found per limitation."),
    "EFF-D136": sel("SUPPORTING", "p4-precision", "precision",
        "SELECTED SUPPORTING P4: OCP Microscaling MX specification v1.0 as the normative FP4/MX standard behind D049 deployment evidence; spec-level, body outstanding."),
    "EFF-D137": out("REJECT",
        "REJECT: Microscaling data-formats paper superseded by D136 (normative OCP spec) for spec facts plus D005/D049 for training/deployment; paper-level retelling is redundant."),
    "EFF-D138": out("REJECT",
        "REJECT: Training-data dedup detail superseded by D139 (DoReMi mixture optimization) for the data-efficiency thread; preprocessing depth is beyond this thesis scope."),
    "EFF-D139": sel("SUPPORTING", "p2-scaling-moe", "moe-training",
        "SELECTED SUPPORTING P2: DoReMi data-mixture optimization for the train-only-useful-data thread; supplement-bound to verified identity 2305.10429, abstract-scope."),
    # ---- Jev execution / memory / TTC / routing ----
    "EFF-D141": sel("PRIMARY", "p7-routing", "routing-kasane",
        "SELECTED PRIMARY P7 anchor: Jev 1.13 official Models page, VERIFIED card-equivalent first-party model facts; vendor scope, independent reproduction thin."),
    "EFF-D142": sel("SUPPORTING", "p7-routing", "routing-kasane",
        "SELECTED SUPPORTING P7: TypeSafe API reference (contract plus confidence derivation) bounding how Jev probabilistic decisions are actually invoked; body outstanding."),
    "EFF-D143": sel("PRIMARY", "p3-attention", "attention-memory",
        "SELECTED PRIMARY P3 anchor: Engram conditional-memory paper (adaptations, delta table, LogitLens consumed) for memory-that-adapts-per-query."),
    "EFF-D144": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3: Engram official implementation repo corroborating the conditional-memory mechanism; body outstanding."),
    "EFF-D145": sel("SUPPORTING", "p3-attention", "attention-memory",
        "SELECTED SUPPORTING P3: Qwen N-gram vs Engram lineage assessment recorded as PARALLEL_OR_UNRESOLVED_LINEAGE; unresolved-lineage boundary preserved, not asserted."),
    "EFF-D146": out("HOLD",
        "HOLD: kNN-LM explicit-corpus retrieval precedent held; boundary-sharpening-only role versus static lookup, and the Engram/Kimi memory treatment carries the lane without a retrieval-architecture detour. Former MAYBE with explicit park rationale."),
    "EFF-D147": out("HOLD",
        "HOLD: RETRO chunked cross-attention precedent held for the same reason as D146; precedent sweep closed at Screening, editorial role unnecessary for this architecture. Former MAYBE with explicit park rationale."),
    "EFF-D148": sel("PRIMARY", "p5-decode", "decoding-ttc",
        "SELECTED PRIMARY P5 anchor: Snell test-time-compute scaling, VERIFIED with 4x/14x numbers consumed; the optimal-compute-allocation pole of the TTC thread."),
    "EFF-D149": sel("PRIMARY", "p5-decode", "decoding-ttc",
        "SELECTED PRIMARY P5 anchor: s1 simple test-time scaling, VERIFIED (curation, budget forcing, o1-preview comparison); budget-forcing origin."),
    "EFF-D150": sel("PRIMARY", "p5-decode", "decoding-ttc",
        "SELECTED PRIMARY P5 anchor: ThinkPrune RL pruning of long CoT, VERIFIED (results table plus protocol consumed); former INSPECT closed; weight-vs-substitute boundary per Card."),
    "EFF-D151": sel("PRIMARY", "p5-decode", "decoding-ttc",
        "SELECTED PRIMARY P5 anchor: overthinking cost-utility analysis, VERIFIED; the more-thinking-hurts pole bounding reasoning-budget waste claims."),
    "EFF-D152": out("HOLD",
        "HOLD: Reasoning-on-a-Budget adaptive-TTC survey held as deferred follow-up pool; secondary-by-design taxonomy and candidate-finder-only role, with Snell/s1/ThinkPrune primaries carrying TTC claims. Former MAYBE with explicit park rationale."),
    "EFF-D153": sel("PRIMARY", "p5-decode", "decoding-ttc",
        "SELECTED PRIMARY P5 anchor: current-model effort-control binding (V4.1 plus Qwen) grounding reasoning-budget claims in shipping behavior, not just papers."),
    "EFF-D154": sel("PRIMARY", "p7-routing", "routing-kasane",
        "SELECTED PRIMARY P7 anchor: FrugalGPT cascade, VERIFIED (Table 3 plus pricing analysis consumed); the avoid-calling-the-big-model origin."),
    "EFF-D155": sel("PRIMARY", "p7-routing", "routing-kasane",
        "SELECTED PRIMARY P7 anchor: RouteLLM preference-data router (data pipeline plus eval design consumed) for learned routing economics."),
    "EFF-D156": out("HOLD",
        "HOLD: 2026 routing/cascading survey held as deferred follow-up pool; secondary unifier, not primary authority, with FrugalGPT/RouteLLM/fragility primaries carrying routing claims. Former MAYBE with explicit park rationale."),
    "EFF-D157": sel("PRIMARY", "p7-routing", "routing-kasane",
        "SELECTED PRIMARY P7 anchor: router-LLM fragility analysis (EACL 2026) with MANDATORY summary-scope boundary; captured-but-unconsumed body detail constrains how far fragility generalizations may travel."),
    # ---- X / runtime follow-ups ----
    "EFF-D162": sel("SUPPORTING", "p4-precision", "capstone",
        "SELECTED SUPPORTING P4+P8 with MANDATORY boundary: accepted X reception ledger (27 observations, 24 accounts, 20 independent) usable ONLY as SUPPORTING reception/deployment evidence, never PRIMARY technical authority; self-reported measurements configuration-bound."),
    "EFF-D163": sel("SUPPORTING", "p6-serving", "serving",
        "SELECTED SUPPORTING P6+P8: vLLM V4.1-Flash recipe, VERIFIED deployment authority with AMD-verification-refusal and MTP-module-drop boundaries consumed; F1 runtime follow-up."),
    "EFF-D164": sel("SUPPORTING", "p4-precision", "precision",
        "SELECTED SUPPORTING P4+P8 with MANDATORY boundary: Unsloth GLM local-quantization authority supporting GGUF availability, local-memory feasibility, and packaging/runtime paths only; vendor-measured speed/quality figures quarantined. F2 runtime follow-up."),
    "EFF-D165": sel("SUPPORTING", "p4-precision", "precision",
        "SELECTED SUPPORTING P4+P8: llama.cpp Qwen port (merged PR 27742: converter, GDN, QSA, PLE), VERIFIED implementation authority for local-feasibility and Qwen runtime support. F3 runtime follow-up."),
}

THESIS = (
    "LLM efficiency has evolved from optimizing a single axis such as parameter count or FLOPs "
    "into a layered systems problem: training only what is useful, activating only part of the model, "
    "moving less memory, retaining less state, decoding fewer serial steps, routing requests to the "
    "cheapest adequate computation, and sometimes replacing free-form generation with specialized "
    "probabilistic decisions. No single technique makes a model efficient; the relevant bottleneck moves "
    "across training, prefill, decode, memory capacity, bandwidth, communication and serving conditions."
)

GOALS = [
    "establish-bottleneck-contract",
    "trace-conditional-compute-lineage",
    "separate-exact-io-from-architecture-change",
    "compare-2026-stacks-by-mechanism",
    "teach-benchmark-literacy",
]

PACKAGES = [
    {
        "package_id": "p1-bottleneck",
        "title": "「効率」とは何を減らすことなのか",
        "purpose": "Establish the bottleneck model as the conceptual contract: training vs inference, prefill vs decode, compute vs memory capacity vs bandwidth vs communication, latency vs throughput, total vs active parameters, weights vs KV-cache, token cost vs task cost. Later comparisons are meaningless without it.",
        "primary_discovery_ids": ["EFF-D001", "EFF-D002", "EFF-D003"],
        "supporting_discovery_ids": [],
        "must_cover_requirements": ["EFF-O01"],
        "boundaries": ["Abstract-scope paper sections retained only where claims are scoped accordingly; no naked cross-condition comparison."],
        "drafting_order": 1,
    },
    {
        "package_id": "p2-scaling-moe",
        "title": "ScalingからConditional Computeへ",
        "purpose": "Trace scaling laws and Chinchilla allocation into sparse MoE history (Shazeer through Switch/GShard) and modern fine-grained MoE economics, ending at active-vs-total parameter economics with expert memory/communication consequences. Contemporary Qwen/GLM stacks are compared in P8; P2 carries the lineage and training-allocation mechanics.",
        "primary_discovery_ids": ["EFF-D006", "EFF-D007", "EFF-D010", "EFF-D011", "EFF-D012", "EFF-D014", "EFF-D015"],
        "supporting_discovery_ids": ["EFF-D013", "EFF-D065", "EFF-D067", "EFF-D068", "EFF-D101", "EFF-D103", "EFF-D133", "EFF-D139"],
        "must_cover_requirements": ["EFF-O02", "EFF-O03", "EFF-O09"],
        "boundaries": ["D005/D139 supplement-bound identities, abstract-scope; training-parallelism detail bounded to allocation context; contemporary Qwen/GLM comparison deferred to P8."],
        "drafting_order": 2,
    },
    {
        "package_id": "p3-attention",
        "title": "AttentionとMemoryを減らす",
        "purpose": "Reduce attention and memory: MHA to MQA/GQA, FlashAttention exact-IO, sparse/local attention, DSA/QSA, recurrent/linear attention through Kimi Linear, KV-cache reduction, and conditional memory via Engram. Central distinction: exact computation with better IO versus architecture that changes computation/storage.",
        "primary_discovery_ids": ["EFF-D018", "EFF-D019", "EFF-D020", "EFF-D026", "EFF-D027", "EFF-D032", "EFF-D125", "EFF-D143"],
        "supporting_discovery_ids": ["EFF-D024", "EFF-D025", "EFF-D029", "EFF-D056", "EFF-D109", "EFF-D110", "EFF-D112", "EFF-D113", "EFF-D114", "EFF-D115", "EFF-D116", "EFF-D117", "EFF-D126", "EFF-D132", "EFF-D144", "EFF-D145"],
        "must_cover_requirements": ["EFF-O04", "EFF-O13"],
        "boundaries": ["D032 VERIFIED launch scope; D125 V3.2 body sections as consumed; D145 parallel-or-unresolved lineage never asserted; KDA-label collision (D085) unresolved and excluded; paper ablation detail outstanding as stated per-record."],
        "drafting_order": 3,
    },
    {
        "package_id": "p4-precision",
        "title": "Bitを減らし、巨大モデルを手元で動かす",
        "purpose": "Reduce bits and run giant models locally: int8/GPTQ/SmoothQuant/AWQ, FP8/FP4/MX, QLoRA, low-bit/native-low-bit boundary, GGUF as format (never as algorithm), llama.cpp, heterogeneous CPU/GPU reality, MoE weight-memory. Community/X material is supporting evidence only.",
        "primary_discovery_ids": ["EFF-D005", "EFF-D041", "EFF-D042", "EFF-D045", "EFF-D048", "EFF-D050"],
        "supporting_discovery_ids": ["EFF-D043", "EFF-D044", "EFF-D047", "EFF-D049", "EFF-D051", "EFF-D135", "EFF-D136", "EFF-D162", "EFF-D164", "EFF-D165"],
        "must_cover_requirements": ["EFF-O06", "EFF-O07", "EFF-O09"],
        "boundaries": ["GGUF is a representation format, not a quantization algorithm; D164 vendor speed/quality figures quarantined; D162 X ledger SUPPORTING-only, configuration-bound; D005 supplement-bound identity, abstract-scope; non-MSR native-1-bit deployment not found."],
        "drafting_order": 4,
    },
    {
        "package_id": "p5-decode",
        "title": "1 tokenずつ待たない",
        "purpose": "Stop waiting one token at a time: speculative decoding (draft/target), EAGLE, MTP with current adoption, then test-time compute, budget forcing, ThinkPrune and overthinking. Tie decode seriality and reasoning-budget waste into one arc without claiming they are the same mechanism.",
        "primary_discovery_ids": ["EFF-D033", "EFF-D036", "EFF-D038", "EFF-D148", "EFF-D149", "EFF-D150", "EFF-D151", "EFF-D153"],
        "supporting_discovery_ids": ["EFF-D034", "EFF-D035", "EFF-D037", "EFF-D039", "EFF-D069"],
        "must_cover_requirements": ["EFF-O05", "EFF-O14", "EFF-O09"],
        "boundaries": ["Decode seriality and reasoning-budget waste are adjacent, not identical; D150 weight-vs-substitute boundary preserved; D069 distillation claims bounded."],
        "drafting_order": 5,
    },
    {
        "package_id": "p6-serving",
        "title": "Servingで消える無駄",
        "purpose": "Eliminate waste in serving: Orca-style scheduling, continuous batching, PagedAttention/vLLM, prefix/KV reuse, disaggregation, Mooncake, Sarathi, cache/offload, SLO/concurrency. Architecture efficiency alone does not determine production efficiency.",
        "primary_discovery_ids": ["EFF-D053", "EFF-D055", "EFF-D059", "EFF-D061", "EFF-D062"],
        "supporting_discovery_ids": ["EFF-D040", "EFF-D056", "EFF-D064", "EFF-D065", "EFF-D066", "EFF-D078", "EFF-D113", "EFF-D114", "EFF-D163"],
        "must_cover_requirements": ["EFF-O08", "EFF-O15"],
        "boundaries": ["D061/D062 supplement-bound identities, abstract-scope; D163 AMD-refusal and MTP-module-drop boundaries preserved; release-level recipe authority, line-level detail outstanding."],
        "drafting_order": 6,
    },
    {
        "package_id": "p7-routing",
        "title": "「大きなモデルを毎回呼ぶ」必要はあるか",
        "purpose": "Ask whether the big model must be called every time: FrugalGPT cascades, RouteLLM learned routing, router fragility, and Jev/System One as a current specialization case with explicitly bounded vendor claims and thin independent reproduction stated as a limitation.",
        "primary_discovery_ids": ["EFF-D070", "EFF-D071", "EFF-D141", "EFF-D154", "EFF-D155", "EFF-D157"],
        "supporting_discovery_ids": ["EFF-D072", "EFF-D073", "EFF-D142"],
        "must_cover_requirements": ["EFF-O10"],
        "boundaries": ["Jev presented as a current specialization case, never as an established generative-LLM replacement; vendor claims bounded by missing independent reproduction and unresolved public calibration protocol; D157 summary-scope constrains fragility generalizations; D072 explicitly not specification authority."],
        "drafting_order": 7,
    },
    {
        "package_id": "p8-capstone",
        "title": "2026年の実装点",
        "purpose": "Compare the four 2026 implementation points by mechanism stack, not leaderboard rank: DeepSeek V4.1 Flash, Qwen3.8-Flash-Next, Kimi Linear, GLM-5.3-Flash, plus the Jev current-case pointer. Dimensions: total/active parameters, attention/memory design, precision, decoding, serving/runtime support, local feasibility, documented trade-offs, evidence quality. GLM D128 abstract-scope limitation is visible.",
        "primary_discovery_ids": ["EFF-D008", "EFF-D028", "EFF-D030", "EFF-D123", "EFF-D128"],
        "supporting_discovery_ids": ["EFF-D004", "EFF-D029", "EFF-D040", "EFF-D078", "EFF-D080", "EFF-D081", "EFF-D126", "EFF-D127", "EFF-D129", "EFF-D130", "EFF-D131", "EFF-D132", "EFF-D162", "EFF-D163", "EFF-D164", "EFF-D165"],
        "must_cover_requirements": ["EFF-O11"],
        "boundaries": ["D128 PRIMARY-but-abstract-scope: report abstract consumed; full-body DSA adoption details, RL infrastructure, benchmark tables NOT consumed; mixed GLM authority depth (D128 plus first-party model/docs/runtime); vendor ratios quarantined; no full-body-verified language for GLM; per-figure pins open across capstones; D162 SUPPORTING-only."],
        "drafting_order": 8,
    },
    {
        "package_id": "p9-measure",
        "title": "数字をどう読むか",
        "purpose": "Teach how to read numbers: TTFT, TPOT/ITL, tokens/sec, aggregate throughput, concurrency, context length, hardware, reasoning budget, benchmark version, scaffold/tool access, contamination, task-completion cost. SWE-bench Pro and validity exhibits show why apparently simple model comparisons fail.",
        "primary_discovery_ids": ["EFF-D092", "EFF-D093", "EFF-D094", "EFF-D098", "EFF-D118"],
        "supporting_discovery_ids": ["EFF-D100", "EFF-D119", "EFF-D120", "EFF-D121", "EFF-D122"],
        "must_cover_requirements": ["EFF-O12"],
        "boundaries": ["No headline number travels without methodology and conditions; D093 section-level consumption outstanding; AIPerf product authority unresolved; tooling version pins per-record; D120 teaches incomparability, not ground truth."],
        "drafting_order": 9,
    },
]


def build():
    assignments = []
    for did in sorted(A, key=lambda x: int(x.split("-D")[1])):
        row = {"discovery_id": did}
        row.update(A[did])
        assignments.append(row)
    doc = {
        "schema_version": "2.0-rc1",
        "issue_id": ISSUE_ID,
        "runner": {
            "provider": "luna-work",
            "model": "muse-spark",
            "invocation": "ts001-reissue-selection-architecture",
            "generated_at": "2026-09-22T17:00:00Z",
        },
        "assignments": assignments,
        "architecture": {
            "editorial_thesis": THESIS,
            "architecture_goals": GOALS,
            "page_plan": {
                "target_pages": 76,
                "max_pages": 96,
                "notes": "Package targets P1 7 / P2 9 / P3 11 / P4 9 / P5 8 / P6 9 / P7 7 / P8 11 / P9 6 (sum 77 incl. rounding); soft minimum ~64; do not pad to reach target.",
            },
            "packages": [
                {
                    "package_id": p["package_id"],
                    "title": p["title"],
                    "purpose": p["purpose"],
                    "primary_discovery_ids": p["primary_discovery_ids"],
                    "supporting_discovery_ids": p["supporting_discovery_ids"],
                    "must_cover_requirements": p["must_cover_requirements"],
                    "boundaries": p["boundaries"],
                    "drafting_order": p["drafting_order"],
                    "profile_extensions": {},
                    "publication_extensions": {},
                }
                for p in PACKAGES
            ],
            "selected_exceptions": [],
            "profile_extensions": {},
            "publication_extensions": {},
        },
    }
    return doc


def main() -> int:
    root = Path(".").resolve()
    doc = build()
    out_path = root / OUT_REL
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        raise ValueError(f"refusing to overwrite: {out_path}")
    out_path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    counts: dict[str, int] = {}
    for row in doc["assignments"]:
        counts[row["disposition"]] = counts.get(row["disposition"], 0) + 1
    print(json.dumps({"path": OUT_REL, "candidate_count": len(doc["assignments"]), "counts": counts}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
