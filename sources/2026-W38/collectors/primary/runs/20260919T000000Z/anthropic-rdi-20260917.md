# Retrieval provenance (edition-local collector raw, NOT exact HTTP bytes)
- source_url: https://www.anthropic.com/institute/measuring-pace-of-ai-development
- retrieved_at: 2026-09-19T00:00:00Z (worker webfetch markdown excerpt; exact HTTP bytes not captured)
- collector_id: primary-webfetch
- collector_run_id: w38-primary-20260919-r1
- published_date: 2026-09-17 (per verification subagent fetch metadata 2026-09-17T20:27:12Z; page body undated in excerpt — date from fetch metadata, treat methodology/numbers as page content)
- authority_class: PRIMARY_OFFICIAL (Anthropic first-party research/institute post)

# Measurements for understanding the pace of AI development inside frontier labs (excerpt)

Three public measurements: (1) share of AI R&D performed by AI itself; (2) oversight/intervention of agent actions; (3) compute allocation.

## (1) AI-led R&D — Anthropic R&D Automation Index (prototype, Epoch AI AL scale AL0-AL5)
As of August 2026: Claude operates fully autonomously (AL5) for no measured subset; Claude "leads" (AL4) 26% of Anthropic AI R&D work; share at/above "AI collaborates" (AL3+) above 90%. Basket: ~15,000 granular tasks from July 2026 sampling, 542-node tree (378 leaves), frozen baseline; person-time weighting. Judge-model agreement checks vs staff reported (exact 59% model-vs-human, 97% within one level).

## (2) Oversight of agents
~30,000 agents doing research/engineering work at any one time (most-used internal platform, August 2026). Online monitors: 100% actions pass pre-execution (seconds); humans review blocked within a week; >1B decisions analyzed, 0.002% blocked (~1/47,000). Offline monitors: 100% ingested post-hoc; ~100k transcripts/week flagged then classifier-triaged; ~50/week escalated to humans; ~1-2/1000 flagged for review.

## (3) Compute allocation (snapshot July 13-20)
~6% of AI R&D compute to safety; ~12% of AI-driven AI R&D compute to safety (deliberately conservative; excludes safeguards-classifier compute). Single fungible pool snapshot, not fixed allocation.

## Claim boundary notes (Sol consumption)
- VERIFIED from this page: the three metrics and August-2026 snapshot values (26% AL4, >90% AL3+, 30k agents, 0.002%/1-per-47k blocked, 6%/12% compute) as first-party reported measurements with stated methodology/appendix.
- Methodology scope/limits explicitly stated on page (judge-model dependence, frozen basket, one-week compute snapshot) — do NOT generalize to industry-wide claims or to September-2026 current values.
- X ledger rows 1-4 (Aug-era R&D posts) + row-level "biomolecular optimization repo/report" technical implications remain UNVERIFIED here: no dedicated biomolecular-optimization repo URL on this page; closest GitHub refs (anthropics/life-sciences marketplace, bio-research plugin) are secondary-sourced, NOT evidenced from primary in this pass — record as PARTIAL/UNRESOLVED.
