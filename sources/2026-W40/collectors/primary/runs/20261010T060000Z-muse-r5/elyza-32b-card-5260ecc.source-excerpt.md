# SOURCE EXCERPT (bounded) — ELYZA 32B-A3B MoE pinned card (commit 5260ecc, full README READ)

- artifact_class: COPYRIGHT_BOUNDED_EXCERPT
- source_url: https://huggingface.co/elyza/ELYZA-Thinking-1.0-llm-jp-4-32b-a3b/blob/5260ecc249f32ef5005ef940c78f41f130d9c468/README.md
- retrieved_at: 2026-10-10T05:27:24Z (Muse webfetch text; rendered markdown, NOT byte-identical raw)
- access_mode: webfetch-read full pinned README (36.5 kB); bounded excerpt archived
- redistribution: bounded quotation only

## Bounded quotes

> frontmatter: `license: apache-2.0 / language: [ja, en] / base_model: llm-jp/llm-jp-4-32b-a3b-base`
> `ELYZA-Thinking-1.0-llm-jp-4-32b-a3b is a reasoning model by ELYZA, Inc., mid-trained and post-trained on llm-jp/llm-jp-4-32b-a3b-base`
> MoE Benchmark Results (Overall): `ELYZA 58.46 / llm-jp-4-32b-a3b-thinking 46.38 / llm-jp-4.1-32b-a3b-thinking 53.89 / Qwen3-30B-A3B 56.31 / gpt-oss-20b 57.26 / Nemotron 3.5 Lightning 30B-A3B 64.52 / Qwen3.5-35B-A3B 66.37 / Gemma 4 26B-A4B 68.58`; Japanese `59.61`; English `55.94`
> Representative rows: `JMMLU (ja) 81.05 (base 81.32)`; `JMATH-500 (ja) 88.20`; `M-IFEval-ja (ja) 81.75 (base 63.05)`; `JHumanEval (ja) 95.37`; `Nejumi BFCL (ja) 41.89 (base 11.58)`; `LiveCodeBench v6 (en) 53.66 (base 26.86)`; `BFCL v4 (en) 36.31 (base 13.29)`; `MATH-500 (en) 95.20`; `AIME 2024+2025 (en) 62.29 (base 34.48)`
> Same footnotes as 33B (parallel-call exclusion, temp/top_p, effort, max output) + `vLLM ... --moe-backend triton` (MoE serving detail)
> Same 3-stage method (JA-localized mid-training; program-verified SFT; RLVR with closed loopholes); same Acknowledgements/Citations pattern (`llm-jp-4-32b-a3b-base`, April 2026)

## Explicitly unread portions

- `Average performance` MoE chart image: NOT machine-readable; tables only.
- Quickstart blocks read, not executed.

## Dense vs MoE distinction (consumed)

- 33B = Dense (llama-family per tags); 32B-A3B = MoE (qwen3_moe tag; active params implied by A3B name; triton MoE backend). Parameter-active counts beyond names NOT stated on cards.
