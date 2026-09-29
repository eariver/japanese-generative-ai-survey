# Collector raw — OpenAI: Better prompt caching for GPT-6 (Sep 22)

- collector_id: primary-webfetch
- collector_run_id: w39-primary-20260927-r1
- retrieved_at: 2026-09-27T18:38:00Z (search-excerpt consumption; full page body partially retrieved)
- source_url: https://openai.com/index/better-prompt-caching-for-gpt-6/
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-22

## Consumed claims

1. EVENT: Improved prompt caching system for GPT-6 family launched Sep 22: higher default hit rates; cache discounts for shared prefixes reused within 30-minute window. (PRIMARY_FACT)
2. TOOLS: Prompt Caching Dashboard (hit-rate monitoring), diagnostics tool for cache misses, explicit breakpoints for prefix control, reasoning-effort change mid-conversation without cache invalidation. (PRIMARY_FACT as vendor feature statements)
3. QUANT: cached-input-read discounts up to 90%; GitHub operational observation (>50% fresh-processing reduction) same as Sol/Luna page. (VENDOR_CLAIM)
4. Availability mechanism detail (minimum lengths, write multipliers) comes from API docs, NOT this page — not asserted here.

## Boundaries

- Cost/latency implications for persistent agents are vendor projections; independent measurement absent.
- Distinct from Cursor's harness-side cache work (separate vendor).
