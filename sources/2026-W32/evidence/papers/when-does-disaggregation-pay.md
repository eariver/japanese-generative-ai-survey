---
issue_id: "2026-W32"
candidate_id: paper-when-does-disaggregation-pay
evidence_type: full-paper-review
review_status: full-reviewed
primary_source: "https://arxiv.org/abs/2608.03741"
publication_date: "2026-08-04"
claim_authority: author-reported-simulation-results
---

# When Does Disaggregation Pay? — Full Paper Evidence Review

## Paper
**When Does Disaggregation Pay? Simulating Prefill–Decode–Attention–FFN Specialization for Agentic LLM Inference**  
arXiv:2608.03741

## Research question
The paper asks when increasingly fine-grained disaggregation of LLM inference is actually worthwhile. It compares:
- ND: no disaggregation;
- PD: prefill/decode split;
- AF: attention/FFN split;
- PDAF: four-way prefill/decode × attention/FFN split.

The central thesis is conditional: disaggregation benefit depends jointly on workload shape, model architecture, hardware characteristics, interconnect, parallelism and numeric precision.

## HeteroPanacea simulator
The authors introduce an event-driven simulator that searches system designs across:
- DP/TP/PP/EP parallelism;
- PD disaggregation;
- attention/FFN disaggregation;
- per-stage heterogeneous NPU design;
- mixed-precision quantization.

Each of prefill-attention, prefill-FFN, decode-attention and decode-FFN can be independently provisioned.

## Validation basis
Component measurements are collected on one server with:
- 8× NVIDIA B200;
- Intel Xeon 6960P;
- CUDA 12.8;
- PyTorch 2.10.0+cu128;
- NCCL 2.27.5.

The paper validates simulator **components** against this platform, but explicitly does not claim end-to-end serving validation.

Primary locator: §IV-A and §VII.

## Evaluation design
The main sweep spans eight model configurations across dense and MoE architectures. The paper's listed set includes Llama-3.1-405B, DeepSeek V4 variants, GPT-OSS, Llama 4 Scout/Maverick, Qwen3-235B-A22B and GLM-4.6.

Workload is parameterized by prefill/output token ratio:
- output length fixed at 1,000 tokens;
- input length scaled by the ratio;
- per-request lengths sampled around these targets;
- 500 requests simulated per configuration at 125 requests/s.

This synthetic workload parameterization is crucial when interpreting throughput gains.

Primary locator: §VI-A.

## Main author-reported findings
### Disaggregation is not always beneficial
At low/balanced prefill-to-output ratios, the paper reports that ND remains strongest for every model in the custom-NPU sweep: the overhead of disaggregation can exceed its benefit.

The authors state that disaggregation crosses parity only when workloads become sufficiently prefill-heavy.

### PD and PDAF benefit from hardware specialization
The paper reports up to **2.06× throughput** over traditional serving on agentic workloads in the specialized custom-NPU design space.

However, the four-way PDAF split only consistently exceeds simpler PD when the hardware space allows attention and FFN stages to receive genuinely different devices. On commercial GPUs, that extra split does not consistently pay off.

### Commercial-GPU gains are narrower and environment-dependent
The paper reports meaningful PD gains on prefill-heavy/agentic profiles, but explicitly notes that GPU experiment conclusions depend on the chosen provider/pricing assumptions.

## Quantization result: stage sensitivity depends on workload
A Qwen 32B study evaluates stage-wise precision assignments on BFCL and GSM8K.

Table VII reports:
- baseline: BFCL 18%, GSM8K 78%
- 8/8/8/8: 21%, 75%
- 4/4/4/4: 6%, 11%
- 8/4/8/8: 20%, 47%
- 8/8/4/8: 11%, 79%
- 4/8/8/8: 12%, 80%
- 8/8/8/4: 20%, 15%

The authors interpret the reversal as evidence that which stage tolerates reduced precision is a **workload property**, not merely a fixed model property.

## Critical limitations stated by the paper
The conclusion explicitly bounds the results:

- validation covers simulator components rather than an end-to-end deployed serving stack;
- scheduling and batching effects therefore remain unverified;
- the quantization accuracy study covers one model and two tasks without repeated runs;
- stage-wise quantization asymmetry should be read as directional, not a calibrated universal magnitude;
- commercial-GPU economic results use one provider offer and can change under other pricing models.

## Evidence assessment
### Supported by the paper
- HeteroPanacea explores fine-grained disaggregated inference under heterogeneous hardware and workload assumptions.
- The simulation predicts that disaggregation is workload-dependent and can lose to unified serving for decode-heavy/balanced workloads.
- The simulated custom-NPU design space produces larger benefits than commercially available GPU choices because stages can be more independently specialized.
- Precision sensitivity differs by task in the paper's Qwen 32B experiment.

### Author-reported / simulation-only
All throughput-improvement factors are simulation results. They are not end-to-end production measurements.

## Safe editorial statements
- This paper argues against treating disaggregation as universally beneficial: in its simulations, workload shape determines whether specialization clears its own overhead.
- The strongest reported PDAF gains require a rich custom-hardware design space; four-way splitting is not automatically advantageous on today's GPU catalogues.
- The study's stage-wise quantization experiment suggests attention/FFN precision sensitivity can invert across tasks, but the authors explicitly call the result directional because it covers one model and two tasks.

## Do not claim
- “PDAF gives 2.06× in production.”
- “Agentic workloads always benefit from disaggregation.”
- “The simulator has been validated as a complete serving stack.”
- “A specific stage can always be safely quantized to 4-bit.”

## Editorial significance before selection
A strong systems paper because it provides a conditional design rule rather than a simple benchmark win. It pairs naturally with SGLang/serving ecosystem material, but its numbers must remain clearly labeled as simulator results.