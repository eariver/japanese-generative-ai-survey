# Collector raw — Hugging Face: Transformers now runs llama.cpp quants (Sep 22)

- collector_id: primary-webfetch
- collector_run_id: w39-primary-20260927-r1
- retrieved_at: 2026-09-27T18:38:00Z (webfetch excerpt of live page)
- source_url: https://huggingface.co/blog/transformers-llama-cpp-quants
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-22

## Consumed claims

1. EVENT: Transformers supports efficient GGUF execution via `from_pretrained(..., gguf_file=)` + `transformers serve` OpenAI-compatible endpoint; ggml Metal kernels reused through `kernels` library; `generate` loop optimizations (mask drop #48814, deferred stopping #47975). Initial focus Apple Silicon, Qwen3.5 dense/MoE (+compatible Qwen3.8). (PRIMARY_FACT)
2. BENCHMARKS (vendor-run, disclosed method): close to llama.cpp across 3 checkpoints on M2 Max/32GB (llama-bench tg128 vs generate incl. prefill — non-identical conditions explicitly disclosed). (VENDOR_CLAIM with disclosed method asymmetry)
3. SCOPE/CAVEATS (explicit): packed path MPS-only; padded batches lower perf; limited arch coverage (Qwen3.5 dense/MoE); llama.cpp REMAINS recommended engine for pure efficient local inference. (PRIMARY_FACT — vendor-stated limitations)
4. Use cases: Python/PyTorch experimentation, eval of GGUF quality, conversion validation, custom decoding, fine-tune-from-GGUF via GgufConfig(dequantize=True). (PRIMARY_FACT)

## Boundaries

- Performance parity is approximate and hardware-bound (M2 Max only); no cross-platform claim.
- X walkthroughs (markfenner INDEPENDENT; EfemeraTt/viralai_jp COMMUNITY) consistent with but not proof of vendor benchmarks.
