# Collector raw — DeepSeek official API docs: Models & Pricing (carry-over revalidation)

- collector_id: primary-webfetch
- collector_run_id: w39-primary-20260927-r1
- retrieved_at: 2026-09-27T18:42:00Z (webfetch excerpt of live page)
- source_url: https://api-docs.deepseek.com/quick_start/pricing/
- source_type: PRIMARY_OFFICIAL
- published: current pricing page (consumed 2026-09-27; model versions dated 0731/0813; V4.1 cutover rates effective 2026-09-10 per secondary calculator)

## Consumed claims (resolves W38 primary gap)

1. MODEL IDENTITY (PRIMARY_FACT): API models `deepseek-flash` (= DeepSeek-V4.1-Flash) and `deepseek-v4-pro` (= DeepSeek-V4-Pro-0813). Legacy names `deepseek-v4-flash`, `deepseek-v4-flash-vision-exp` still accepted but retired; requests served by V4.1-Flash and billed at Flash price. THIS IS THE ROUTING-CUTOVER PRIMARY EVIDENCE W38 lacked.
2. RATE CARD (PRIMARY_FACT as official card): flash cache-hit off-peak $0.003 / peak $0.006; cache-miss off-peak $0.15 / peak $0.3; output off-peak $0.6 / peak $1.2. Pro cache-hit off-peak $0.022 / peak $0.044; cache-miss off-peak $0.66 / peak $1.32; output off-peak $1.98 / peak $3.96. Off-peak = half of peak; peak windows 01:00–04:00 + 06:00–10:00 UTC Mon–Fri excl. Chinese holidays.
3. CAPABILITIES (PRIMARY_FACT): 1M context, 384K max output, thinking/non-thinking modes, JSON/tool/Responses/Anthropic-API support, FIM non-thinking only, Vision flash-only; concurrency 2500 flash / 500 pro.
4. No "V4.1-Pro launch" on this page — do NOT claim a V4.1-Pro model. Pro remains V4-Pro-0813. (W38 no-claim boundary preserved and now primary-backed)

## Boundaries

- Page is current-state (post-window); the cutover occurrence itself is corroborated as in-effect, but the exact in-window cutover instant is not established from this page alone.
- Late-only X rows (BenKoska eval note, agentschat2026 Cheepseek note, both Sep 25 23:5x UTC post-cutoff) remain late-only context; Cheepseek third-party shell pricing NOT verified against this card.
