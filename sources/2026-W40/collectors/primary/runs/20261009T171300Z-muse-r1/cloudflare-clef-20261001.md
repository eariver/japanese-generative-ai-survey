# Collector raw — Cloudflare: Clef + Clef-flash decision models (Oct 1)

- collector_id: primary-webfetch
- collector_run_id: w40-primary-20261009-muse-r1
- retrieved_at: 2026-10-09T17:13:32Z (webfetch excerpt of live page)
- source_url: https://blog.cloudflare.com/clef-decision-models/
- source_type: PRIMARY_OFFICIAL
- published: 2026-10-01 (page JSON-LD datePublished 2026-10-01T15:34:02Z; changelog mirror same date)

## Consumed claims (claim-level)

1. EVENT: Cloudflare released Clef + Clef-flash Oct 1, 2026: first Cloudflare-trained open-source decision models on Workers AI; Apache-2.0 weights on Hugging Face; Jev-API compatible; RL fine-tuning platform (FDE now, self-serve later). (PRIMARY_FACT: release, date, license, hosting)
2. ARCHITECTURE: Qwen torso (27B Clef / 9B Clef-flash per third-party docs; vendor page states Qwen3.8-27B frozen + Qwen3.5-9B frozen with rank-256 LoRA + routing head); prefill-only pass, parallel schema-choice scoring (non-autoregressive); 64K context (vs Jev 32K); vision encoder (images) unlike text-only Jev. (PRIMARY_FACT as vendor architecture description; exact base IDs cross-checked with Workers AI docs)
3. INTERFACE: Typed questions (noul/choice/score etc.) with per-option probabilities + reliability scores; Workers AI binding env.AI.run() / REST / AI Gateway; pricing $0.24 (Clef) / $0.09 (Clef-flash) per 1M input tokens, no output price; 10K neurons/day free. (PRIMARY_FACT as vendor API/pricing description)
4. BENCHMARKS (vendor-run, attribution required): Jev Decision Index lead claimed (live demo); table: BFCL 98.47/98.76, ToolRet 69.19/66.43, API-Bank 91.93/93.11, When2Call 72.37/65.58 (Jev 80.97 wins), BANKING77 94.20/90.93, CLINC150+OOS 97.43/66.77, BRIGHT 45.91/39.26 (Jev 47.52 wins), ESCI 57.48/57.39, PhishNChips 79.60/75.05; Typesafe WorkflowEvals 3/4 wins; latency median 209.3ms / 38.8ms vs Jev 524.1ms (vendor-measured, edge GPUs). (VENDOR_CLAIM)
5. USE (vendor example): Threat-intel domain classification 2.2s vs 4.7s gpt-oss-120b with more labels. (VENDOR_CLAIM as illustrative run)

## Boundaries / unresolved

- Jev Decision Index is vendor-hosted benchmark, not independent cross-vendor reproduction; do not conflate with Strands Decider 2B numbers.
- Distinct from Strands Decider 2B (Oct 1, different vendor/architecture/license path) and Ollama /v1/systemone (Sep 29 serving interface); do not merge.
- RL platform is service announcement; no self-serve reproducibility in this raw.
