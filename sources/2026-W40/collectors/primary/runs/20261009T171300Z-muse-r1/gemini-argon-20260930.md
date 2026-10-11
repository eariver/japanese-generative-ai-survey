# Collector raw — Google: Gemini 4 Argon (Sep 30)

- collector_id: primary-webfetch
- collector_run_id: w40-primary-20261009-muse-r1
- retrieved_at: 2026-10-09T17:13:32Z (webfetch excerpt of live page)
- source_url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-30 (vendor page header; X post 2026-09-30T20:03:30Z is momentum, not first publication)

## Consumed claims (claim-level)

1. EVENT: Google announced Gemini 4 Argon frontier model Sep 30, 2026 for complex long-horizon workflows (coding, enterprise knowledge, cyber defence); rolling to trusted cyber defenders via Fairwind Program; phased release with US voluntary pre-release process; broader dev/enterprise/consumer later (paid API + AI Ultra first). (PRIMARY_FACT: announcement, date, staged rollout)
2. CONTEXT LIMIT: Page states "industry-leading 1 million token limit" and "expanding output token limit to 1M tokens, up from 64K". Grok's "1M output tokens" over-specifies: page does not cleanly separate input vs output vs trajectory budget in one line. Do NOT assert "1M output" without model-docs proof. (PRIMARY_FACT with exact-quoting boundary)
3. PRICING: Introductory $2 input / $10 output per 1M tokens, cached input 95% off; post-intro $4/$20. (PRIMARY_FACT as vendor price card)
4. BENCHMARKS (vendor-run, attribution required): DeepSWE v1.1 77.9% SOTA; Vals Index #1; Vals Finance Agent v2 + Harvey Legal leading; AutomationBench 51.3% #1; LVBench long-video 91.7% SOTA; CWE-bench v1 68% tied-first (with Astra/Grok 4.7 per third-party note); internal vuln/pen-test beats 3.8 Flash Cyber; Gray Swan IPI leading. Internal Google workload anecdotes (quantum 40%, 300TiB-1PiB memory, libgav1 Rust 2.7x, C++->Rust migrations). (VENDOR_CLAIM)
5. CYBER POSTURE: Trained for autonomous find-validate-patch; trusted-defender release WITHOUT cyber guardrails; broader release hardens misuse/CBRN refusal, prompt-injection, misalignment monitoring (CoT monitoring, sealed sandboxes). Wiz Scan-for-Good demo: critical healthcare vuln found. (VENDOR_CLAIM as vendor capability/safeguard description)

## Boundaries / unresolved

- Tester-only at announcement; no public GA date/price-beyond-intro timeline in this raw.
- Cross-vendor chart claims (vs Astra/Fable/Opus) are vendor-selected; independent reproduction pending.
- TechCrunch Sep 30 + Mashable Oct 1 corroborate date/staged rollout; not primary authority.
