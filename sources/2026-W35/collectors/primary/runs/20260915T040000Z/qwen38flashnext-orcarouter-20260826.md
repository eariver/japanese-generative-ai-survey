# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w35-primary-20260915-r1
- locator: https://www.orcarouter.ai/blog/qwen-4-leak-vllm-fuse-op
- observed_at: 2026-09-15T04:25:00Z
- published_at: 2026-08-26 (page date; article updated later — only pre-2026-08-28T22:00Z facts used)
- retrieval: webfetch text; boilerplate trimmed; W35-window facts preserved. Post-window
  additions in the article (Sept PRs, Sept model launches) are NOT relied upon.
- authority_class: SECONDARY_TECHNICAL (inference-provider engineering analysis; HF card +
  engine PRs are verification targets)

# Retrieved content (W35-window facts only)

Title: Qwen 4 Leak: What the vLLM & SGLang PRs Reveal. By Alistair Wren, Aug 26 2026.

- vLLM PR #53909 "Add qwen4 fuse op" (open, unmerged, awaiting review, from contributor fork):
  standalone Triton kernels for HyperConnection, Qwen Sparse Attention (QSA), PLE state ops.
  13 passing tests (dtype/shape guards, paging metadata, cache slots, MRoPE layout, strided
  state, null/duplicate indices, determinism). Fail-closed host guards.
- Operator mapping to Qwen3.8-Flash-Next architecture: HyperConnection = gated residuals
  (single stream widened to 4 branches, element-wise gating, FP8 residual storage); QSA =
  indexer compresses keys into micro-blocks (ratio 4), keeps best 512 blocks (~2051 logical
  positions), softmax/value aggregation on uncompressed K/V; 12 of 48 layers QSA, 36 GDN
  linear-attention layers with fixed recurrent state; PLE = 51B-param n-gram lookup table
  (Per-Layer Embeddings), hash-addressed, offloadable to host memory. MoE body: 125B total,
  ~6B active (<5%), 512 experts, top-10 routing.
- Qwen3.8-Flash-Next (released Aug 26 2026): open weights on HF + ModelScope under
  qwen-community-1.0, standard + FP8; card: 125B MoE, ~6B active, 51B n-gram table, 262K
  context (1M via YaRN), multimodal; "A Preview of the Qwen4 Architecture";
  model_type=qwen4_exp; reference implementation in huggingface/transformers models/qwen4_exp.
- Qwen3.8-Flash served variant: Qwen Cloud CNY 1/3 per M input/output tokens (~$0.16/$0.47),
  default 1M context, built-in tools (vendor-reported pricing).
- Card benchmarks vendor-reported, unreproduced: DeepSWE 1.1 58.7, SWE-bench Pro 62.5,
  LiveCodeBench v6 91.9.
- SGLang day-0 post Aug 26 (SGLang + Alibaba + NVIDIA + AMD collab): NVFP4 checkpoint, claimed
  540 tok/s decode TP4 B200 with speculative decoding (vendor-collab claim, unaudited).
- SGLang PR #36585 (Aug 27): native Qwen4ExpForConditionalGeneration support; non-maintainer
  contributor; credited to autonomous agent "Argus"; failing CI, awaiting review.
- vLLM companion PR #53899: PLE offload (SGLang measured: BF16 table to pinned host mem frees
  ~23 GiB/GPU on H200, +78% KV capacity, bit-identical outputs — community/vendor measured).
- Qwen 4 proper: NOT released as of W35 window (no date/card/weights). September roadmap leak
  is rumor, not schedule. Distinguish preview (released) from flagship (unreleased).
