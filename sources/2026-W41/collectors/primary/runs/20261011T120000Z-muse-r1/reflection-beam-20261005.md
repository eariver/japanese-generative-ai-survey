# Collector excerpt — w41-primary-reflection-beam-20261005 (Muse r1, claim-level derived note)

Source URL: https://reflection.ai/blog/introducing-beam (dated October 5, 2026; "Update 10/8/26" noted on results)
Retrieved: 2026-10-11 (UTC) via operator webfetch. Capture class: CLAIM_LEVEL_DERIVED_NOTE.

## Consumed claims

- Beam: sparse MoE, 501B total / 23B active; coding/reasoning/agentic focus; pretraining 23.8T tokens; RL 100M+ rollouts on 10.5K GB300 over 4 weeks.
- Vendor benchmarks (attributed, updated 10/8): DeepSWE 44.4, SWE-Pro v2-Hard 77.2, Terminal-Bench 2.1 80.1, AIME 2026 97.8, HLE 36.2 no-tools, GPQA Diamond 90.5, AutomationBench 37.0, MCP Atlas 78.7.
- **Weights NOT released**: early access waitlist; "will release weights under Apache 2.0 later this month" + technical report/model card → open-weight intention only.
- Pretraining infra: 6,144 GB300 NVL72, <4 weeks, goodput 92.3%; context 1M via midtraining.

## Boundaries

- Day-only date; weights/license unverifiable until release; figures vendor-run.
