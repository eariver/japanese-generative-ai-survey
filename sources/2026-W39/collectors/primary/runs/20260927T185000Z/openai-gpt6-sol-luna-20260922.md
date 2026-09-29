# Collector raw — OpenAI: Introducing GPT-6 Sol and Luna (Sep 22)

- collector_id: primary-webfetch
- collector_run_id: w39-primary-20260927-r1
- retrieved_at: 2026-09-27T18:36:00Z (webfetch excerpt of live page)
- source_url: https://openai.com/index/introducing-gpt-6-sol-and-luna
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-22 (vendor page; "last verified: 2026-09-22" on availability)

## Consumed claims (claim-level)

1. EVENT: OpenAI expanded GPT-6 family with GPT-6 Sol and GPT-6 Luna on Sep 22, 2026. Positioned as cost-efficiency frontier; trained with similar methods as GPT-6 Astra. (PRIMARY_FACT: release occurred, identity, date)
2. PRICING: API prices cut 50% vs GPT-5.6 promotional pricing. Sol: $4→$2 input, $20→$10 output per 1M tokens. Luna: $0.20→$0.10 input, $1.20→$0.50 output. (PRIMARY_FACT as vendor price card; independent billing verification NOT performed)
3. AVAILABILITY: ChatGPT Work + Codex for Plus/Pro/Business/Enterprise/Edu from Sep 22; Luna also in desktop app for Free/Go; NOT in Chat (rolling out gradually). API names `gpt-6-sol`, `gpt-6-luna`. (PRIMARY_FACT as vendor availability statement; gradual-rollout caveat noted)
4. BENCHMARKS (vendor-run, attribution required): AutomationBench Sol xhigh 33.2% @ $0.27/task vs Opus 5 max 26.9% @ 11.1x cost; Agents' Last Exam Sol max 56.4%; FrontierCode Sol improved, matches Fable 5.1 xhigh at lower cost; DeepSWE v1.1 Sol max 68.8% vs Fable 5 max 69.9% xhigh at ~80% lower cost; OSWorld 2.0 offline Sol xhigh 60.5% vs Opus 5 medium 60.3% at ~80% lower cost. (VENDOR_CLAIM: vendor-run evals, competitor scores from public reports)
5. FACTUALITY (vendor internal eval): Sol makes ~half the mistakes of predecessor on flagged-conversation eval; approaching Astra-level reliability. (VENDOR_CLAIM: internal, non-representative sample disclosed)
6. CACHING: higher default hit rates; 90% cached-input-read discounts; GitHub reports >50% reduction in fresh-processing share across billions of requests (third-party operational observation cited by vendor). (VENDOR_CLAIM + cited third-party observation)
7. ALIGNMENT: Sol/Luna build on Astra alignment work; lower misleading-claims rates on coding; system card referenced. (VENDOR_CLAIM)
8. VOICE: page cross-links GPT-Live/Voice availability Sep 23 (Voice plugins per X C1 row 2102808325742322002). Voice availability detail NOT in this page body — separate verification needed.

## Boundaries / unresolved

- Long-context/long-task performance specifics (1M context per AWS Bedrock listing, seen in search excerpt only — NOT consumed from primary; do not assert from this raw).
- Competitor benchmark figures are vendor-reported; treat as vendor-bound.
- X-reported long-task stability complaints (xiaomovps) are community signal, neither confirmed nor refuted by this page.
