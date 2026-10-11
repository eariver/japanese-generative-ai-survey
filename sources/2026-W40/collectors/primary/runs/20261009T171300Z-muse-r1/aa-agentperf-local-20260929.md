# Collector raw — Artificial Analysis: AA-AgentPerf-Local (Sep 29)

- collector_id: primary-webfetch
- collector_run_id: w40-primary-20261009-muse-r1
- retrieved_at: 2026-10-09T17:13:32Z (webfetch excerpt of live article)
- source_url: https://artificialanalysis.ai/articles/aa-agentperf-local
- source_type: EVALUATOR_PUBLISHER
- published: 2026-09-29 (publisher article header)

## Consumed claims (claim-level)

1. EVENT: Artificial Analysis launched AA-AgentPerf-Local Sep 29, 2026: open-source local inference tool replaying real agent trajectories (8 tasks, 168 turns, ~56K growing context, identical token work; tool execution skipped by default). Code github.com/ArtificialAnalysis/aa-agentperf-local. (PRIMARY_FACT as publisher release record)
2. COVERAGE: Initial hardware DGX Spark 128GB / RTX 5090 32GB / Ryzen AI Halo 128GB / MacBook Pro M5 Pro 64GB; models Qwen3.5-9B, Qwen3.8-27B, Qwen3.6-35B-A3B, Ling 3.0 Flash 124B/5B-active at 4-bit; 14 configs with speculative decoding (MTP/DFlash/DSpark) published. (PRIMARY_FACT as publisher methodology description)
3. RESULTS (publisher-measured, attribution required): Active-params trend with exceptions; RTX 5090 fastest where fits (>3.5x); Spark 1.4-1.7x Halo on 3/4 models despite 7% bandwidth gap (compute/CUDA maturity); MacBook within 2-9% Halo on 2 models; prefill share 22-41% for Qwen3.8-27B despite 73-93% KV-cache hits; speculative +30-120% decode. Prices at MSRP vs inflated street noted. (EVALUATOR_CLAIM: publisher benchmark, not model-intelligence eval)
4. SCOPE: Tests inference serving, NOT autonomous task correctness or model intelligence. (EDITORIAL_BOUNDARY per Sol register; publisher states same)

## Boundaries / unresolved

- Single-agent full-system focus; multi-agent/shared-load pending per publisher.
- Hardware/software rapidly shifting; leaderboard is living, not frozen W40 authority without commit pin.
