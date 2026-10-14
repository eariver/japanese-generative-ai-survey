# Evidence collector run r3-C — open-weights + serving/decision bundle (2026-10-12, DELEGATED)

Capture: DELEGATED subagent webfetch excerpts (verbatim). Sol re-verifies directly. NO_BYTE_HTML.

## C1. Mistral Large 4 — 52B pins RETRIEVED, 49B absent from official bodies
- Blog https://mistral.ai/news/mistral-large-4 (Oct 6 2026): 52B active / 1T total; preview API today (Studio); weights end of month; pricing card Input $1.36 / Output $4.18 per M; vendor benchmarks (DeepSWE 61.7%, Coding Agent Index 49.8%...).
- Docs https://docs.mistral.ai/models/mistral-large-4: 52B active / 1.05T total + 1.6B vision encoder; 1M context; sale pricing Input $0.68/Output $2.09; version Openv26.10.
- 49B figure NOT on official blog/docs bodies; only third-party snippets. Disagreement preserved (Grok X states 49B).

## C2. Beam https://reflection.ai/blog/introducing-beam — RETRIEVED
- Date Oct 5 2026 (+update 10/8 results refresh). 501B/23B MoE; weights + report + card later this month (not downloadable); Apache-2.0 intent; vendor benches (DeepSWE 44.4, TB2.1 80.1, AIME 97.8...); 23.8T tokens; GB300 RL scale.

## C3. Liquid d1 https://www.liquid.ai/blog/d1-open — RETRIEVED
- Date OCT 7 2026. d1-3B + d1-omni-600M open weights, HF LiquidAI/d1-3b + d1-omni-600M available today (vendor); Decision Index 48.57/15.95; 8ms RTX4090; no pricing/license-SPDX in body.

## C4. Kolibri https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/ — RETRIEVED
- Date 03/10/2026. 78B/3B (table 78.1B/3.46B); 1M context; Apache-2.0; HF Aleph-Alpha/Kolibri-1 downloadable; 20T tokens, 768 B200; vendor benches.

## C5. Nova Sonic https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-nova-2.5-Sonic — RETRIEVED
- Posted Oct 5 2026. GA speech-to-speech; Bedrock us-east-1/us-west-2/eu-north-1/ap-northeast-1; same-as-Nova-2-Sonic pricing (no numerics); 256K context.

## C6. Perplexity forum https://community.perplexity.ai/c/announcements/9 — RETRIEVED
- /6286 (Oct 6 21:11Z): decider v1.1-27b open weights, HF Decision Index 0.3 top, $0.02/M input (half v1).
- /6296 (Oct 7 16:30Z): embed-v2-late pair, frontier, HF-public.
- /6312 (Oct 9 16:27Z): Decision Bench 94.5% / 1071 cases @ $0.017/1k decisions.
- Params/license/HF URLs beyond generic NOT in thread bodies.

## C7. Clef-omni https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ — RETRIEVED
- JSON-LD datePublished 2026-10-09T18:27:34.129Z (< cutoff, IN-WINDOW confirmed). Qwen3-Omni-30B-A3B MoE; latencies 130/150ms; pricing flash $0.038/M, Clef $0.24/M, omni $0.15/M; HF open weights; vendor benches.

## C8. StepFun Step 5 — official page NOT_ACCESSIBLE, provider listing snippet-only
- stepfun.com/step-5-preview direct fetch: JS shell only ("阶跃星辰"). Specs via search snippets (600B/27B, 1M, API live, open weights Oct 15, $1/$2.70) UNVERIFIED direct.
- OpenRouter page direct (llms.txt view): API guide only, no pricing table. Pricing/free-week (Oct 8-15)/license-Proprietary via snippets only.

## C9. MS Decision-1 https://commandline.microsoft.com/microsoft-decision-1-model-foundry/ — RETRIEVED (day-only)
- Date 2026.10.09, NO clock time in body -> TIME_UNRESOLVED stands. Qwen3.5-9B scorer; Foundry + OpenRouter; $0.042/M in, out free; vendor 36-bench claims.

## C10. Nace Drex/NDI — docs PARTIALLY RETRIEVED
- nace.ai/drex RETRIEVED: Drex 1.5 128K ctx, Decision Index 0.2.1 58.28 (+0.37 vs Jev), API drex-latest + GitHub open models.
- Blog introducing-drex: Sep 24 2026 GA + Sep 28 update (PRE-WINDOW origins; Oct 9 X post is in-window announcement).
- NDI docs (docs.ndi.nace.ai) RETRIEVED: platform API description; NO 1.0 version label/date/pricing/benchmarks/license found.
- ElevenLabs: Audio Detector + SynthID docs RETRIEVED; protocol WG charter/membership/spec NOT found (NOT_ACCESSIBLE docs).

## C11. Tencent Youtu-Parsing-Omni HF — RETRIEVED (month-only)
- Card: 5B, license youtu-parsing, vendor OmniDocBench 96.96 etc.; News bullets [2026-10] only; NO day-granular upload date in fetch -> HOLD stands.
