# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w35-primary-20260915-r1
- locator: https://iapp.co.th/blog/openthai2p0-launch
- observed_at: 2026-09-15T05:10:00Z
- published_at: 2026-08-27 (page date)
- retrieval: webfetch text; nav/blogroll trimmed; launch claims preserved.
- authority_class: PRIMARY_OFFICIAL (vendor first-party launch post; vendor-measured numbers clearly marked)

# Retrieved content (substantive claims)

Title: OpenThai 2.0 — one open model that reads Thai documents, knows Thailand, and does agentic work. By Kobkrit Viriyayudhakorn (CEO, iApp Technology), with AIEAT.

Release: open-source Thai vision-language model, 27B params, Apache 2.0, weights free on HF (huggingface.co/iapp/openthai2.0-qwen3.8-27b — Qwen3.8-27B-based). Generalist sibling of OpenThai 2.0 Legal (30B specialist, released ~1 month earlier). Single model: Thai document/handwriting reading at specialist level + Thai knowledge QA in natural Thai + tool calling for agents; retains base general intelligence.

Vendor-measured numbers (same suite, identical serving, own prompts; repeatable per vendor):
- Thai reading CER (lower better): handwriting (n=916) 0.261 vs base 0.649; books/Royal Gazette (n=608) 0.126 vs 0.370; gov docs (n=906) 0.327 vs 0.530; printed (n=104) 0.077 vs 0.103.
- Knowledge/instruction: OpenThaiEval national exams 0.842 (base 0.820, Typhoon 2.5 0.742, Pathumma 3.0 0.660); IFEval-TH 0.795; HumanEval coding 0.957.
- BFCL tool use (3,841 cases): overall 0.820 (base 0.811, Typhoon 2.5 0.792); multi-turn agentic 0.775 (base 0.750, Typhoon 0.550). MMLU-Redux 0.916 vs base 0.924 (-0.008).
- Published losses: Typhoon-OCR 1.5 specialist still wins clean printed/isolated handwriting; scene text weakest; table extraction at parity with base.

Formats (all Apache 2.0): bf16 (vLLM/transformers, 1x80GB); GGUF Q4_K_M/Q8_0 (17/29GB); MLX 4-bit (Apple silicon 24GB+); INT8 W8A8 (~40GB); NVFP4 (Blackwell). MTP draft head: vLLM self-speculative 75.2 vs 50.1 tok/s (+50%, H100, token-identical).

Training: 3-stage LoRA on ~143K machine-verified rows (transcriptions vs human ground truth; knowledge leak-checked vs eval sets; instruction kept on programmatic-constraint pass). Handwriting bench text-disjoint. Compute: 8x H100 via Siam AI Corp.

Access: browser demo free; hosted OpenAI-compatible endpoint free until 2026-09-30 (30 req/min); self-host command documented.
