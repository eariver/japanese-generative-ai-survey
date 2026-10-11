# SOURCE EXCERPT (bounded) — ProvenanceGuard original paper via ar5iv (paper body READ)

- artifact_class: COPYRIGHT_BOUNDED_EXCERPT
- source_url: https://ar5iv.org/html/2606.18037 (HTML rendering of arXiv 2606.18037; team blog pointed here as `[HF-PAPER-LINK]`/arXiv meantime)
- retrieved_at: 2026-10-10T05:27:24Z (Muse webfetch text; ar5iv rendering, NOT PDF bytes)
- access_mode: webfetch-read §§I–V (abstract through RQ2 ablations; output truncated ~40KB); bounded excerpt archived
- redistribution: bounded quotation only
- claim_location_anchors: authors/affiliations; Abstract (corpus counts); Fig.1–2; Eq trace/claims/routing/calibration; Table 1 RF config; Table 2 constants; §IV corpus/labels/benchmark/adjudication; Tables 3–11 (results/ablations/latency)

## Bounded quotes (methods/conditions)

> Authors: Ander Alvarez, Santhiya Rajan, Samuel Mugel, Román Orús (Multiverse Computing, Donostia/San Sebastián + Toronto; Orús also DIPC/Ikerbasque)
> `e_i = (tool_i, source_i, text_i)` (trace interface §III.1; stable tool/source IDs; fallback to tool name)
> Router: `ŝ_j = argmax_s cos(q_j, r_s)` centroid routing; premise cap 1,500 chars / 512-token NLI pair budget (historical 256-token runs labeled historical)
> NLI: MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli; alignment proxy τ=0.35, min supported-token ratio 0.70; literal protected-value strict check; lexical rescue 0.55/0.85
> RF calibrator: 400 trees, max depth 5, min leaf 8, balanced weights, Gini, seed 20260607; 1,597 train / 367 val / 361 held-out claims; threshold 0.65 (val block F1 0.841)
> Corpus: 281 frozen captured medical MCP traces (synthetic/de-identified, no PHI); 266-trace subset → 2,325 LLM-assisted labels (train/val/test by trace); 40-trace 361-claim held-out (human-expert verified); labels LLM-assisted (2 Gemma 4 E4B judge prompts + adjudication)
> Table 3 held-out: block F1 0.802 (P 0.673 / R 0.993), source acc 0.858 / 260 source-eligible, src+rel 0.681; verdict macro F1 0.406 (imbalanced); trace-bootstrap CI [0.664, 0.900]
> Multi-source benchmark: 59 test questions, 254 claim cases, 2,587 pairwise rows, 263 frozen extracted claims; block F1 0.846, source acc 0.503, src+rel 0.229 (same-topic wrong-chart 0.127, count-summary 0.179 stress slices)
> Baselines (same packet, support-only, no source IDs): MiniCheck 0.783 / RAGAS 0.758 / AlignScore 0.662 / SummaC-ZS 0.436
> Repair: 173 blocked → all resolved (144 fallback); multi-source rerun 59 → 59 (2 fallback); 50 injected attribution swaps → 50/50 detected; RQ2 raw-verdict head 0.839 acc
> Scope bound: `The central claim is limited to source-attribution factuality in MCP-grounded answers; we do not claim to solve open-domain factuality detection, clinical safety validation, or parametric-knowledge correction.`

## Reporter-vs-original provenance (corrections to team-blog relay)

- Held-out source accuracy 0.858/260 (matches relay); src+rel 0.681 (relay omitted).
- Harder-benchmark exact-source numbers are 0.503 / 0.229 (NOT the relay's 50.3% on a different test framing — same value, different unit: frozen extracted claims vs pairwise rows; units distinguished).
- Adjudication is LLM-assisted (2-judge + priority), human-expert ONLY on 361 held-out packet (relay under-specified this).
- 256-token runs are historical-labeled; retained config is 512-token.

## Explicitly unread portions

- Output truncated during §§V.3-rest/VI+ (conclusion/limitations/appendices incl. JSON trace schema App.A); figures render as text placeholders; Table 7–10 latency values partially captured.
- PDF bytes not consumed (ar5iv rendering only); code/poster/NVFlow PR not opened.
