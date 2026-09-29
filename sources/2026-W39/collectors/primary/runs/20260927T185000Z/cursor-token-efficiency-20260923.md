# Collector raw — Cursor: Improved token efficiency for longer agent runs (Sep 23)

- collector_id: primary-webfetch
- collector_run_id: w39-primary-20260927-r1
- retrieved_at: 2026-09-27T18:39:00Z (webfetch excerpt of live page)
- source_url: https://cursor.com/blog/improved-token-efficiency
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-23; authors Jediah Katz, Connor O'Keefe, Calvin Yee

## Consumed claims

1. EVENT: Harness-efficiency program results published: -7% user token costs without quality reduction (production A/B measured). (VENDOR_CLAIM: vendor-measured production observation)
2. LEVERS (measured): system prompt trimmed ~66%; built-in tool defs offloaded to dynamic context (-60% static-context description tokens; MCP precedent -46.9% in MCP-tool sessions); explicit cache breakpoints + phantom-user-message stabilization → -20% cold cache misses; line numbers every 10th line → -1.6% cache-read tokens; subagent prompting rebalanced + model-selection tightening. (VENDOR_CLAIM: vendor production measurements)
3. METHOD NOTE: A/B on large user base; evals acknowledged as unrepresentative proxy. (vendor-disclosed method boundary)

## Boundaries

- 7% is Cursor-production-specific; not transferable to other harnesses.
- Quality-neutrality is vendor-measured; independent reproduction absent.
