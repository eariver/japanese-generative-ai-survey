# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w37-primary-20260918-r1
- locator: https://huggingface.co/openbmb/MiniCPM5-2B
- observed_at: 2026-09-18T00:00:00Z
- published_at: 2026-09-07
- retrieval: webfetch markdown of OpenBMB MiniCPM5-2B model card; stored claim-relevant verbatim excerpts as returned. HF repo appeared Sep 6-7 2026 per secondary coverage (OrcaRouter Sep 6, vLLM recipe Sep 7, NYU Sep 8). Full card consumed via webfetch 2026-09-18.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (claim-relevant verbatim excerpts)

We are releasing MiniCPM5-2B, the second model in the MiniCPM5 series, following MiniCPM5-1B. It is a dense 2B Transformer that scales up the same training recipe, built for on-device, local deployment, and resource-constrained scenarios, reaching 2B-class open-source SOTA.

2B-class open-source SOTA: compared with strong open-source models of similar size, MiniCPM5-2B achieves SOTA performance within this comparison set. Average 53.9.

Model Information:

- Type: Causal Language Model
- Architecture: Standard LlamaForCausalLM
- Number of Parameters: 2,516,756,480
- Number of Non-Embedding Parameters: 1,981,982,720
- Number of Layers: 42
- Number of Attention Heads (GQA): 16 for Q and 2 for KV
- Context Length: 131,072

Evaluation: Within comparison set (LFM2.5-2.6B, Qwen3.5-2B, Gemma-4-E2B-it, plus larger Qwen3.5-4B etc.), MiniCPM5-2B average 53.9, exceeds larger models (highest 51.1). Advantages in code reasoning, math reasoning, long-context, tool use, agentic tasks.

Selected vendor figures:

- LiveCodeBench v6: 69.1
- AIME 2025: 86.5, AIME 2026: 86.5, MATH-500: 94.6
- SWE-bench Verified: 46.4
- GAIA Text-103: 88.7
- tau2-Bench Telecom: 97.1, BFCL v4: 66.6

Training: base + mid + post (SFT 400B deep-thinking, RL teachers, OPD merging 16 experts). Data released as UltraData family.

Quickstart: vLLM pip install vllm>=0.21, vllm serve openbmb/MiniCPM5-2B. SGLang, llama.cpp, Transformers supported. Tool calling via SGLang minicpm5 parser. Standard LlamaForCausalLM, no custom kernels, no model-code fork.

License: Apache-2.0.
