# W42 r2 bundle — IBM Granite Switch 4.1 (blog + model card bodies consumed, 2026-10-17)

Collector run: `20261017T071000Z-muse-r2` / collector_id `primary-webfetch`
Observed at: `2026-10-17T07:20:00Z`
Capture class: `CLAIM_LEVEL_DERIVED_NOTE__NO_ORIGINAL_BYTES`.

## Official blog (huggingface.co/blog/ibm-granite/granite-switch-4-1, published Oct 15, 2026) — BODY CONSUMED
- 8B + 30B Switch 4.1: Decision aLoRA (general decisions, e.g. v1/systemone) + Guardian aLoRA (safety decisions) + Granite-Speech-5.0-Turbo-CTC (470M, fastest ASR on OpenASR leaderboard, vendor) on ONE endpoint at ~base-model VRAM via cache-efficient Activated LoRAs (shared KV cache) + vLLM kernels + co-located ASR encoder.
- Guardian comparison (vendor): beats Jev 1.13, Microsoft-Decision-1, GPT-Luna-Decisions, Clef-Flash on safety decision tasks on average — explicitly names W41 HOLD Microsoft-Decision-1 WITHOUT rewriting its chronology (comparison claim, not fresh Decision-1 evidence; carry-over HOLD stands).
- Granite Libraries context (prior release): specialists beat generalists on specialized classification; Race demo vs Jev-27B (5-step RAG faster); Doom 3B at 60–100 decisions/s vs Jev 10/s (vendor demos).
- Access: vLLM plug-in, llama.cpp native, /v1/systemone swap-in, shared prefix cache; Adapter SDK/Mellea planned.

## Model card (huggingface.co/ibm-granite/granite-switch-4.1-8b — release Oct 14, 2026) — BODY CONSUMED
- Base granite-4.1-8b (8B dense, 128K ctx, 12 langs incl. Japanese); adapters decision + guardian-core; audio cascade (English-only, lowercase/unpunctuated, no joint training — limitation stated).
- Decision Index v0.3 fast subset (1,068 rows): overall 42.9 (Knowledge 29.1 / Language 48.9 / Retrieval 49.8 / Tools 59.8 / Arts 18.0); local-vs-hosted agree ±0.6 (serving-faithfulness check, vendor).
- License: Apache 2.0 (card header + LICENSE file) — VERIFIED available weights (HF page live, 278 downloads last month, Transformers/vLLM/SGLang/Docker snippets, safetensors). 30B sibling same config; preview variants (-8b/-30b/-3b-preview) with full Libraries bundle (no audio).
- Ethics: guardian-core is an extra layer, NOT a substitute for app-level safety testing; decision probs are priors, not certified classifications; mistranscription can silently alter adapter responses.
- Do NOT infer: 30B card not individually opened (same-config claim from 8B card + blog); preview-variant weights not verified beyond listing.

## Chronology
- Card release Oct 14 (IN) + blog Oct 15 (IN) → event IN-WINDOW on both. Compared-against Microsoft-Decision-1 remains W41 HOLD (no new Decision-1 clock/license/weights from this comparison).
