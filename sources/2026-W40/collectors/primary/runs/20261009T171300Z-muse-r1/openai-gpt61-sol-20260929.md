# Collector raw — OpenAI: Introducing GPT-6.1 Sol (Sep 29)

- collector_id: primary-webfetch
- collector_run_id: w40-primary-20261009-muse-r1
- retrieved_at: 2026-10-09T17:13:32Z (webfetch excerpt of live page)
- source_url: https://openai.com/index/introducing-gpt-6-1-sol/
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-29 (vendor page header)

## Consumed claims (claim-level)

1. EVENT: OpenAI launched GPT-6.1 Sol on Sep 29, 2026 as upgrade to GPT-6 Sol; near-Astra intelligence at one-fifth Astra standard prices. (PRIMARY_FACT: release occurred, identity, date)
2. PRICING: Standard $2 input / $10 output / $0.10 cached input per 1M tokens; cached input 95% below standard, 50% below GPT-6 Sol cached. Astra $10/$50/$1.00; Luna $0.10/$0.50/$0.01 shown on same page. (PRIMARY_FACT as vendor price card)
3. BENCHMARKS (vendor-run, attribution required): DeepSWE v1.1 matches Astra at ~1/5 cost, +6.4pp over GPT-6 Sol; GDP.pdf above Opus 5.5 with fallbacks at <1/2 cost; AutomationBench +2.2pp over Opus 5.5 medium at ~1/3 cost, +4.8pp over GPT-6 Sol; OSWorld 2.0 offline +7pp over GPT-6 Sol max at <1/2 cost, within 2.1pp of Astra at ~1/7 cost; Terminal-Bench Science 0.1 >2x GPT-6 Sol max at <1/2 cost ($5.47 vs $23.21 Opus 5.5 / $23.80 Astra); factuality error 11.4%->7.7% at low effort. (VENDOR_CLAIM)
4. AVAILABILITY: ChatGPT Work + Codex for Plus/Pro/Business/Enterprise/Edu from Sep 29; NOT in Chat; API `gpt-6.1-sol`; Ultrafast for 6.1 Sol coming soon (not yet). (PRIMARY_FACT as vendor availability statement)
5. SAFETY: Alignment evals improved over GPT-6 Sol, closer to Astra; broken-search disclosure 2.1% fail (vs 4.9% Sol, 1.5% Astra, 28.7% Luna); no reviewer-bypass attempts observed. (VENDOR_CLAIM as vendor eval)

## Boundaries / unresolved

- All benchmark deltas are vendor-run in research/API environment; competitor scores from public reports; do not present as independent reproduction.
- "Near-Astra" is vendor framing across selected evals; Astra remains highest on hardest science tasks (68.1% Terminal-Bench Science).
- Ultrafast pricing/availability for 6.1 Sol is separate DevDay item; do not conflate standard price with Ultrafast tier.
