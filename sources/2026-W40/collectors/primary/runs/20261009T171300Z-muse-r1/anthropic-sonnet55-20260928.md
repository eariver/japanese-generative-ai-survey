# Collector raw — Anthropic: Introducing Claude Sonnet 5.5 (Sep 28)

- collector_id: primary-webfetch
- collector_run_id: w40-primary-20261009-muse-r1
- retrieved_at: 2026-10-09T17:13:32Z (webfetch excerpt of live page)
- source_url: https://www.anthropic.com/claude-sonnet-5-5
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-28 (vendor page header; AWS Bedrock confirms launch Sep 28, 2026)

## Consumed claims (claim-level)

1. EVENT: Anthropic released Claude Sonnet 5.5 on Sep 28, 2026, second model in Claude 5.5 family; complement to Opus 5.5 (Sep 22, pre-window). (PRIMARY_FACT: release occurred, identity, date)
2. PRICING: Same nominal price as Sonnet 5: $2 input / $10 output / $0.20 cache-read per 1M tokens; vendor states up to 30% less per task via fewer tokens. (PRIMARY_FACT as vendor price card; per-task saving is vendor-measured)
3. SPEED: Vendor states 30%+ faster output than Sonnet 5; fastest Sonnet to date. (VENDOR_CLAIM)
4. BENCHMARKS (vendor-run, attribution required): Terminal-Bench 4.0 70.6% (Sonnet 5: 10.3%); FrontierCode 1.1 Main 46.2% Max; CursorBench 4.0 55.5% (Sonnet 5: 34.1%); GDPval-AA v2.1 1844 (Sonnet 5: 1449, Opus 5.5: 1846); AA-Briefcase v1.1 1811; HLE with tools 64.5%; OSWorld 2.1 partial 80.1%; Chartography 61.6% no tools. Effort-level/cost curves per page. (VENDOR_CLAIM: vendor-run evals; Artificial Analysis ran GDPval/Briefcase on pre-release build with structured-output bug caveat, footnote 3)
5. CONTEXT: 1M tokens context, 128K max output (Bedrock model card; third-party model pages consistent). (PRIMARY_FACT as distributor spec)
6. SAFETY: First Sonnet with Opus-5.5-class cyber safeguards/fallbacks; biology safeguards same as Sonnet 5; distillation defences (reasoning-extraction classifiers, preserved thinking). (VENDOR_CLAIM as vendor safeguard description)
7. AVAILABILITY: All platforms incl. AWS Bedrock, Google Cloud, Azure; API id `claude-sonnet-5-5`; zero data retention. (PRIMARY_FACT as vendor availability statement)

## Boundaries / unresolved

- Competitor figures (GPT-6 Sol etc.) are vendor-reported with footnotes on stale third-party scores; do not present as independent comparison.
- Max-effort FrontierCode dip vs Xhigh is vendor-explained (code-review skill timeouts); not independently reproduced.
- Opus 5.5 Sep 22 remains pre-window; do not merge Opus community adoption into Sonnet 5.5 freshness.
