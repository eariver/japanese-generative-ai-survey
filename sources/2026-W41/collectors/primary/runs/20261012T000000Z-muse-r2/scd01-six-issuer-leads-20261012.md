# Collector excerpts r2-A — SC-D01 six issuer leads (Muse r2, bounded retrieval)

Retrieved: 2026-10-12 (UTC) via operator webfetch/websearch. Capture class varies per item below; NO_ORIGINAL_BYTES unless stated.

## 1. Liquid AI d1 (Oct 7) — full first-party page read

URL: https://www.liquid.ai/blog/d1-open (page header "OCT 7, 2026").
- d1-3B + d1-omni-600M open-weight decision models; HF repos LiquidAI/d1-3b, d1-omni-600M "available today".
- Decision Index v0.2.1 public split: d1-3B 48.57 (ahead of <10B, par Decider 35B-A3B); d1-omni-600M 15.95.
- Text bench mean: d1-3B 82.9 (top of vendor table), omni 78.4; Civil Comments omni 95.8; PAWS-X omni 79.5.
- Latency: 8ms RTX 4090 / 16ms Thor / 26ms Orin / 50ms Nano; llama.cpp day-one support.
- Backbones: d1-3B from LFM2.5-VL-3B (decoder-only); omni from LFM2.5-Encoder-350M + FastConformer audio + vision adapters.

## 2. AWS Nova 2.5 Sonic (Oct 5) — first-party changelog text confirmed via search render

URLs: https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-nova-2.5-Sonic/ (case-sensitive; lowercase variant 404s).
- "Posted on: Oct 5, 2026": GA speech-to-speech for real-time voice agents; improved reasoning/instruction-following/tool-call; lower latency; 4 regions (us-east-1, us-west-2, eu-north-1, ap-northeast-1); same pricing as Nova 2 Sonic. Service card exists (docs.aws.amazon.com responsible-ai/nova-2-5-sonic; not separately fetched).
- Audio lane: NOT QUIET (corrects r1).

## 3. Aleph Alpha Kolibri (Oct 3) — full first-party page read

URL: https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/ (dated 03/10/2026).
- 78B total / ~3B active MoE, EN/DE, 1M context; HF Aleph-Alpha/Kolibri-1 downloadable, Apache-2.0.
- Pretraining 20T tokens (21.3% German); 768 B200 GPUs; vendor benchmarks (AIME 2026 96.0, GPQA 84.3, AA-Omniscience non-hallucination 44.0, M/A grounding 0.23).

## 4. EmbeddingGemma 2 (Oct 6) — model card + secondary corroboration

URLs: https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2 (740M = 270M text + 170M vision + 300M audio; 768-d; Apache-2.0; HF+Kaggle weights) + Oct 6 secondary (Verge/TNW/Gigazine: 8K context, ~191MB RAM, on-device).
- Release-notes page timed out on fetch; date basis = model card + corroborating Oct 6 secondary. Weights downloadable → strong availability.

## 5. Perplexity (Oct 6/7) — issuer forum + X + HF README

- Forum https://community.perplexity.ai/c/announcements/9: pplx-decider-v1.1-27b thread + pplx-embed-v2-late thread (Oct 7, topic 6296).
- X @perplexity_ai Oct 7 4:09PM UTC: embed-v2-late pair, HF-public. IN-WINDOW timestamp.
- HF README perplexity-ai/pplx-decider-v1.1-27b: Decision Index 56.4 → 61.56 (+3.5 vs Jev), same backbone.
- Weights: decider downloadable (open weights per README); embed pair "publicly available on Hugging Face" per issuer X.

## 6. Decisions API first-party upgrade (Oct 6)

Source: official changelog render — "Oct 6 / Feature · Model: gpt-6-luna · API: v1/decisions / Released the Decisions API in beta with gpt-6-luna... 10x faster than the Responses API." + community post Oct 6 8:53pm UTC + pricing ($0.10/M input-only).
- Upgrades r1 row from secondary-only to FIRST-PARTY corroborated. No duplicate row created.
