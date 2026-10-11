# Collector excerpt — w41-primary-mistral-large4-20261006 (Muse r1, claim-level derived note)

Source URLs:
- https://mistral.ai/news/mistral-large-4/ (blog, dated October 6, 2026, day precision)
- https://docs.mistral.ai/models/mistral-large-4-0 (model page, dated October 6, 2026)
Retrieved: 2026-10-11 (UTC) via operator webfetch. Capture class: CLAIM_LEVEL_DERIVED_NOTE.

## 49B vs 52B reconciliation (per contract §B)

- Current blog body: "1 trillion-parameter natively multimodal model with 52 billion active parameters".
- Current docs model page: "52B active parameters and 1.05T total parameters" + 1.6B vision encoder.
- Both current sources agree on **52B active** (1T vs 1.05T total is rounding-level). The scout's 49B figure does not appear in either current page. Therefore: repeat **52B active / ~1–1.05T total** with both pins; treat any 49B repetition as superseded unless a versioned source is produced.

## Consumed claims

- Public preview API now (Mistral Studio); **weights promised end of October, NOT downloadable** → open-weight intention ≠ available bytes.
- Pricing (docs, sale): input $1.36→$0.68, cached $0.14→$0.07, output $4.18→$2.09 per 1M tokens. Context 1M.
- Vendor benchmarks (attributed): DeepSWE 61.7%, Terminal-Bench 28.3%, Coding Agent Index 49.8%, AutomationBench 59.9%, AA-Briefcase 1393 Elo, Cyber Index top-5 + Cybench 93%, Dense 200 42% vs GPT-6-Astra 41%, B3 93.3%, KORA 1.691. RL at scale: 3k GPUs, ~33B tokens/day.
- Trained 3,800 Grace Blackwell GPUs in Mistral EU datacenters; Series D €3B noted as corporate context.

## Boundaries

- Day-only dates; weights pending; all figures vendor-run; RL-preview model still training ("no saturation" is vendor claim).
