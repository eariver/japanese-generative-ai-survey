# Retrieval provenance (edition-local collector raw, NOT exact HTTP bytes)
- source_url: https://devin.ai/blog/introducing-code-scans
- retrieved_at: 2026-09-19T00:00:00Z (worker webfetch markdown excerpt; exact HTTP bytes not captured)
- collector_id: primary-webfetch
- collector_run_id: w38-primary-20260919-r1
- published_date_on_page: September 16, 2026
- authority_class: PRIMARY_OFFICIAL (Cognition first-party product announcement)

# Introducing Code Scans (excerpt)

Code Scans: turn broad engineering goals into concrete codebase improvements. Tell Devin the goal; it investigates, evaluates findings, opens PRs. Entry: /scan in Devin webapp; docs: docs.devin.ai/work-with-devin/code-scans.

Architecture: Agentic MapReduce (from Devin Security Swarm): Plan (Devin studies repo, defines relevance rules) -> Shard (rules run, code divided into batches) -> Map (parallel agents investigate) -> Reduce (final agent combines, dedups, prioritizes). Completeness property: every selected batch must be processed.

Early results (vendor-stated, Philips Digital Computational Pathology): 96% PR merge rate; 700+ engineering hours saved (short testing timeframe).

Worked examples (vendor-reported): Dioxus Rust compile-time scan — clean debug build 58.6s -> 21.0s (-64%, 22 workspace crates); SEO scan devin.ai + cognition.com — Ahrefs health 87->92, slow pages -73%, missing alt text eliminated.

Scan catalog: performance, DB queries, test coverage, dead code, code quality, cleanup, telemetry, accessibility, compliance, migration planning, SEO, custom.

## Claim boundary notes (Sol consumption)
- VERIFIED from this page: feature existence/launch (Sep 16 2026); /scan entry; Agentic MapReduce 4-phase architecture as vendor-described design (NOT independently benchmarked); docs link.
- Vendor customer metrics (96%, 700h, Dioxus -64%, Ahrefs deltas) are first-party stated pilot outcomes, NOT independently reproduced — carry as stated-with-attribution, not verified fact.
