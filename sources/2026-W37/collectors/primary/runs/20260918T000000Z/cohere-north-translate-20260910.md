# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w37-primary-20260918-r1
- locator: https://cohere.com/blog/north-small-translate
- observed_at: 2026-09-18T00:00:00Z
- published_at: 2026-09-10
- retrieval: webfetch markdown of Cohere North Small Translate announcement; stored claim-relevant verbatim excerpts as returned. Page header shows Sep 10, 2026. Full page consumed via webfetch 2026-09-18.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (claim-relevant verbatim excerpts)

Sep 10, 2026

# Introducing North Small Translate: A leading sovereign open-weight machine translation model

Today, we're releasing North Small Translate, a mixture-of-experts machine translation model with strong performance across 50+ languages. Across WMT26 benchmarks, North Small Translate achieves an 83.6 score across all languages, outperforming proprietary models like DeepL and Google Translate, as well as open-weight alternatives such as Gemma 4 31B (off), GLM 5.2, and Mistral Large 3.

Snapshot:

- Model: North-Small-Translate-1.0
- License: Open-weights, non-commercial (CC BY-NC 4.0)
- Architecture: MoE
- Model size: 218B total; 25B active
- Context length: 16k input, 16k output
- Input/output modalities: Text
- Languages: Supports 50+ languages
- Optimized for: Machine translation
- Hardware minimum: 1x B200 @ W4A4, 2x H100s @ W4A4

Leading translation quality: WMT26 All Languages 83.60 vs Qwen 3.5 397B A17B 81.56, GLM 5.2 FP8 76.50, DeepL NextGen 81.37, Gemma 4 31B (on) 79.46, Google Translate 68.20. North Small Translate (Agentic) 84.36.

WMT26 benchmarked for WMT 2026 using GPT-5.6-Sol as a judge.

Throughput: up to 1.4x higher output throughput than Gemma 4 31B TP1 under identical concurrency – 112 vs 81 TOPS low concurrency, 39 vs 30 TOPS high concurrency.

Long-context: scores 48.9 on long-context evaluation (two book chapters single call, xComet-XL), vs Google Translate 21.3, Gemma 4 31B 19.4.

Cost: 80.1 score at $0.000676 per task, 661 tokens avg. Gemini 3.1 Pro Preview high $0.038928 per task cited as comparator.

Developed in partnership with RWS / Language Weaver.

Available today on Hugging Face for non-commercial and research use. Documentation at docs.cohere.com. Technical report at cohere.com/north-small-translate-tech-report.
