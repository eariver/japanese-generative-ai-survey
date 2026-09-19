# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w37-primary-20260918-r1
- locator: https://huggingface.co/inclusionAI/Ling-3.0-flash-VL
- observed_at: 2026-09-18T00:00:00Z
- published_at: 2026-09-10
- retrieval: webfetch markdown of inclusionAI Ling-3.0-flash-VL model card; stored claim-relevant verbatim excerpts as returned. HF repo created Sep 4 2026, FP8 Sep 8, OpenRouter listing Sep 10 per secondary coverage. Full card consumed via webfetch 2026-09-18.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (claim-relevant verbatim excerpts)

We are introducing Ling-3.0-flash-VL, our next-generation native multimodal model. Built upon Ling-3.0-flash, it brings visual information into the complete process of understanding, reasoning, acting, and verification. With 124B total parameters, only 5.5B activated parameters per token, support for image and video inputs, and a context window of up to 256K tokens.

Model Overview: inherits language, reasoning, long-context of Ling-3.0-flash, extending with native image and video understanding. 124B total, 5.5B active per token, up to 256K context.

Architecture:

- ViT visual encoder + two-layer MLP projector
- VideoRoPE for spatial + temporal
- 42-layer hybrid backbone alternates KDA and Gated MLA at 5:1
- Sparse MoE 124B total, 5.5B active per token

Evaluation: achieves 42 on Artificial Analysis Intelligence Index v4.1.1, +4 over Ling-3.0-flash 38.

Three capability dimensions: Understand (counting, layouts, charts, docs), Reason (calculation, multi-step, verification), Act (web/software interfaces to action sequences).

Quickstart: SGLang cookbook, vLLM with trust-remote-code, ling3 parsers. License MIT per HF header.

Note: Thinking mode enabled by default. Terminal-Bench 2.1 evaluated under AA protocol.
