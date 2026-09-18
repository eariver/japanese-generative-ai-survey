# W37 Sol Discovery completeness review

Status: `SOL_DISCOVERY_COMPLETENESS_REVIEW / NON_BLOCKING_WITH_RESIDUAL_LIMITS`
Date: `2026-09-18T23:10:00Z`
Issue: `2026-W37`
Discovery acceptance: `sources/2026-W37/discovery/discovery-accepted-v2.json` (14 records, graph validated)
X manifest: `COMPLETE`, run `weekly-x-2026-W37`, discovery `w37-grok-r3-45-url-ledger` bound

## Surfaces exercised

- Grok/X r3 Raw (45 URLs: 24 ordinary / 1 pre-window / 20 late-breaking, Sol-corrected 12 ordinary INDEPENDENT) as one sensor, not universe
- Primary official: OpenAI FinServ Sep 10, GPT-Live-1 API Sep 10, Agents API Sep 10, DeepSeek news+API docs Sep 10, Cognition SWE-2 Sep 10, Fusion Sep 11, OpenBMB MiniCPM5-2B Sep 7, Cohere North Translate Sep 10, InclusionAI Ling VL Sep 10, Anthropic Threat Intel Sep 10
- Secondary: AP/PBS Coxon resignation Sep 9 (safety discourse only), CellCog GLM-5.5 tracker Sep 6 (rumor disposal)
- Web open-world sweep for Sep 4-11 window across foundation/agents/multimodal/open-weight/inference/eval/safety lanes

## Lane coverage (12 required)

- A Foundation/Reasoning: Astra FinServ, DeepSeek V4.1 Flash, MiniCPM5-2B, North (translation LM), GLM rumor disposed — COVERED
- B Agents/Coding/Harness: FinServ Work, GPT-Live delegation, Agents API, SWE-2, Fusion — COVERED (strong)
- C Multimodal: DeepSeek native vision, Ling VL — COVERED
- D Image Gen/Edit: examined (W36 Pics Nano Banana Sep 1 pre-window; no W37 ordinary-window material release found) — QUIET (legitimate)
- E Video Gen/Edit: examined (W36 fal H3 Max Sep 1 pre-window; no W37 ordinary material) — QUIET
- F Speech/Audio/Music: GPT-Live-1 voice — COVERED
- G Open Weight/Local/Quant: DeepSeek MIT, MiniCPM Apache-2.0, Ling MIT, North CC BY-NC research — COVERED
- H Inference/Serving/Systems: DeepSeek KV cache/pricing, MiniCPM vLLM/SGLang, Agents sandboxes — COVERED
- I Memory/Multi-Agent/Retrieval: Agents subagents/compaction, Fusion lead/sidekick — COVERED
- J Evaluation/Benchmarks: FrontierCode 50.0% (SWE-2), DeepSeek tables, MiniCPM 53.9 avg, WMT26 83.6, AA Index 42 — COVERED (vendor-reported bounds)
- K Safety/Security: Anthropic Threat Intel Sep 10, Coxon resignation context — COVERED (report + discourse, no technical promotion)
- L Other Emerging: FinServ vertical packaging, North translation vertical — COVERED

## Negative-space sweep

- Checked Anthropic (Fable 5.1 Sep 1 pre-window, no new W37 model; Threat Intel Sep 10 captured), Google (Gemini 3.8 Flash Sep 2 pre-window; 3.8 Live Sep 15 late-breaking, excluded), Meta, xAI, Mistral, Qwen, Kimi (K3 as SWE-2 base, no new W37 release), Z.ai (5.3 Aug, no 5.5 per tracker)
- Image/video/speech beyond GPT-Live: no material W37 ordinary-window releases located; quiet determination is defensible, not a gap-fill failure
- No silent drop of technically material alternatives detected at Discovery stage

## Duplicate/concentration

- DeepSeek news + API docs overlap intentionally (launch claims vs API operational binding); not misleading inflation
- OpenAI triple (FinServ / Live / Agents) are distinct Sep 10 products, not duplicates
- 14 records is not inflated by X ledger (1 record for 45 URLs)

## W36 carry-over

- Released W36 authority scanned fresh: 19 assignments (SELECTED/HOLD, no HOLD_OUT/WATCHLIST/LATE_BREAKING roles requiring continuation)
- All W36 SELECTED (Astra Sep 3, Fermat Sep 4 boundary, Fable Sep 1, Gemini Sep 2, K2, GLM-5.3 Aug 28, Atlas, Pics, H3 Max, FUSE, Copilot, Kilo, Muse Spark, NVIDIA-HF) are pre-window for W37 (before Sep 4 22Z) with no new W37 development
- Zero formal inherited obligations; recorded explicitly. No CARRY_OVER Discovery records required.

## Residual limitations

- OpenAI pages via webfetch (curl blocked); stored claim-relevant excerpts, full pages consumed via webfetch 2026-09-18
- DeepSeek HTML raw (92k/27k) contains full page; markdown excerpts in Discovery summary are faithful
- Ling VL repo exact hour Sep 4 unresolved; Sep 8/10 bindings establish ordinary-window materiality regardless
- Fusion Sep 11 assumed ordinary (daytime; no evidence of >=22Z late-breaking); cost/benchmark figures vendor-reported
- Image/video quiet is a finding, not proof of non-existence; completeness means space examined, not every lane filled

## Verdict

`NON_BLOCKING` — Discovery is sufficient basis for Screening/Evidence. Proceed to CANDIDATES_NORMALIZED via canonical Screening. No Exception Gate.
