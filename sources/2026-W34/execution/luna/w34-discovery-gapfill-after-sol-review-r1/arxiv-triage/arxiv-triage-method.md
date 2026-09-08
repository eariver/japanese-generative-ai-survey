# Full collected arXiv triage method

This is a Discovery-only, provisional relevance triage. It does not perform Screening, Materiality, Selection, or Evidence acceptance. Sol must independently review the full ledger and shortlist.

- Source run: `arxiv-api-2026-W34-20260907T161121Z`; six Atom Raw files; raw rows before version/category deduplication: **3108**.
- Normalized unique corpus: **2296**; this matches the accepted collector summary's 2,296 entries.
- W34 boundary: `2026-08-14T22:00:00Z` inclusive through `2026-08-21T22:00:00Z` exclusive; boundary rows: **0**.
- Deterministic high-recall prefilter hits: **2026**.
- Provisional semantic shortlist: **314**; after merging IDs already represented in the prior Discovery graph: **311**.
- Existing-Discovery duplicate relationships: **3**; low-signal/irrelevant-or-out-of-scope signal: **270**; prefilter-hit background: **1712**.

## Vocabulary

- `language_models`: `\bllm\b|large language model|language model|foundation model|generative ai|genai`
- `agents_tools`: `\bagent(?:s|ic)?\b|tool use|function calling|computer use|autonomous agent`
- `retrieval_embeddings`: `\brag\b|retrieval[- ]augmented|retrieval|knowledge retrieval|embedding`
- `inference_serving`: `\binference\b|serving|quantization|speculative decoding|mixture[- ]of[- ]experts|\bmoe\b`
- `multimodal_media`: `multimodal|vision-language|vision language|\bvlm\b|text-to-video|video generation|image generation`
- `training_methods`: `transformer|diffusion|reasoning|pretraining|pre-training|fine[- ]tuning|post[- ]training|reinforcement learning|distillation|synthetic data`
- `safety_security`: `safety|alignment|security|cyber|adversarial|prompt injection|privacy|authorization|guardrail|robustness`
- `developer_systems`: `code generation|software engineering|program synthesis|code agent|developer|repository|debugging|refactoring`
- `evaluation`: `benchmark|evaluation|evaluating|test-time|assessment|measurement`
- `memory_context`: `\bmemory\b|long[- ]term|context window|context management`

## Provisional semantic rule

A row enters the provisional shortlist when the deterministic score is at least 9. Title term groups count twice, full title+abstract term groups count once, a title method marker adds 2, and a title that is domain-specific without a high-signal system group loses 2. The rule is designed to expose a broad, inspectable set of technical research leads; it is not a claim that every shortlisted paper is important or W34-material.

The full ledger records every entry, matched groups, score, bucket, lane, concise rationale, arXiv locator, and the Raw filename. Existing Discovery relationships are explicit rather than silently discarded. No target paper count or story quota was used.

