# SOURCE RECORD — Olmo-core 3 technical report retrieval (DOCUMENTED FAILURE + bounded fallback)

- artifact_class: CLAIM_LEVEL_DERIVED_NOTE__RETRIEVAL_FAILURE_LOG
- target_url: https://allenai.org/papers/olmocore3 (Tech Report link from https://allenai.org/blog/olmocore3)
- attempts (meaningful retries, both failed on size):
  1. 2026-10-10T05:27:24Z Muse webfetch markdown → `Response too large (exceeds 5MB limit)`
  2. 2026-10-10T05:27:24Z Muse webfetch text → `Response too large (exceeds 5MB limit)`
- No PDF URL guessed (URL fabrication prohibited); no further rendering available in-tool.

## Bounded fallback consumption (what WAS read instead)

- Ai2 blog Oct 1 (r2, full body READ): DDP resident experts, expert/pipeline parallelism, distributed optimizer, rowwise/grouped-GEMM, MXFP8; 8→128 experts <5% drop; 47B 52k vs 19.4k (~2.7x, 8×B300); 1.2T/58.36B-active/512GPU 858 TFLOP/s/GPU (random routing); 2.38T short-capacity test; token gerrymandering / expert-LR / overlap negative results.
- `https://github.com/allenai/olmo-core` repo page READ 2026-10-10T05:27:24Z: `PyTorch building blocks for the OLMo ecosystem`; 1.7k stars / 344 forks; `Apache-2.0 license`; PyPI `ai2-olmo-core`; docs/readthedocs; `src/scripts/official/` training scripts (OLMo2/OLMo3); inference (transformers/vLLM/Olmo-core beta). Repo confirms open code existence, NOT report prose.
- Search excerpt corroborates report dated 2026-10-01 (acknowledgments snippet) — date only, not content.

## Claim-level bound (honest)

- Blog-backed claims stay VERIFIED (blog fully read); report-body targets (`tech-report`, `github-repo`) stay UNRESOLVED with this explicit failure (NOT silent).
- Quantitative provenance (2.7x conditions, trillion-scale configs, ablations) remains reporter-level (Ai2 blog), NOT original-report-verified.
- Retry avenue for Sol/Selection depth: paginated report sections, docs site, or repo-cloned report file (none available in this execution).
