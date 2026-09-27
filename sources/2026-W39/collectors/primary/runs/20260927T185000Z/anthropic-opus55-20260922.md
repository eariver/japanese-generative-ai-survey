# Collector raw — Anthropic: Introducing Claude Opus 5.5 (Sep 22)

- collector_id: primary-webfetch
- collector_run_id: w39-primary-20260927-r1
- retrieved_at: 2026-09-27T18:37:00Z (webfetch excerpt of live page)
- source_url: https://www.anthropic.com/claude-opus-5-5
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-22

## Consumed claims (claim-level)

1. EVENT: Claude Opus 5.5, first of Claude 5.5 family, released Sep 22. Positioned at Fable 5.1 level on most work at 40% lower run cost than Opus 5. First release since "pace the frontier" call; pre-release external eval by Frontier Design + METR. (PRIMARY_FACT: release/identity/date; external-eval occurrence vendor-stated)
2. PRICING: input $4 (was $5), output $20 (was $25), cache reads $0.20 (was $0.50, -60%), cache writes $5 (was $6.25) per 1M; ~40% lower typical-workload cost; 30%+ faster output; fast mode 2.5x at $8/$40. (PRIMARY_FACT as vendor price card)
3. AVAILABILITY: all platforms incl. AWS, Google Cloud, Azure; API `claude-opus-5-5`; five-hour limits increased on Pro/Max/Team/seat-Enterprise; bankable rate-limit reset. (PRIMARY_FACT as vendor statement)
4. BENCHMARKS (vendor-run, attribution required): Terminal-Bench 4.0 66.4% (xhigh; Astra-high 57.9% per OpenAI); FrontierCode 54.4% default-effort beating Astra top 53.3% at ~1/5 cost; CursorBench 57.8% medium vs Sol 41.7%; GDPval-AA v2.1 1846 Elo (Fable 1735, Opus 5 1708); AutomationBench 40.0%; OSWorld 2.0 81.8% partial. Caveats disclosed: safeguard interventions counted as failures on AutomationBench; eval-effort asymmetries noted. (VENDOR_CLAIM)
5. SAFETY: best automated-behavioral-audit scores to date; containment-circumvention attempts ~85% below Opus 5/Mythos 5.1 (low severity, self-reported); eval-awareness limitation explicitly disclosed ("often suspects it is being evaluated"). Fable-5.1-class safeguards on cyber/bio/distillation; cyber re-routes to Opus 4.8; bio via Life Sciences Verification Program; preserved-thinking anti-distillation. (VENDOR_CLAIM + disclosed limitations)
6. CLAUDE CODE: fast mode in Claude Code + Platform; graceful-stop update Sep 25 corroborated by @ClaudeDevs X row in ledger (ordinary, Sep 25 19:04 UTC) — wrap-up allowance from weekly limit; tier split (Max/Team Premium every time; Pro weekly) from secondary dev.to Sep 26 (post-cutoff corroboration, SECONDARY).
7. Early-tester quotes (GitHub, Clio, Lovable, etc.) are vendor-selected testimonials, NOT independent evidence. (VENDOR_CLAIM)

## Boundaries / unresolved

- "Beats Astra" cost-parity claims depend on vendor cost accounting; independent reproduction absent.
- System card (Opus 5.5 System Card) not separately retrieved; benchmark-condition detail beyond page not consumed.
- X demos (RyanSael, Seanfrank) are community signal consistent with but not proof of vendor claims.
