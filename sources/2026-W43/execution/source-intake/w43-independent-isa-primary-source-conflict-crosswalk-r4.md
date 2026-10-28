# W43 ISA primary-source conflict crosswalk r4 (edition-local, noncanonical)

Status: `EDITION_LOCAL_SOURCE_NOTE / NO_CANONICAL_MUTATION`
Date: 2026-10-25. Starting HEAD `db78839bd7cb858a6cc5b1620bf6c574f064339f` / Tree `b1ee9c3e686e3f50cfabc9d679eff7e01937726e`.
Scope: versioned first-party passages actually read for W43-ISA-001…009. No new immutable raw source bytes were archived in this pass; canonical accepted r4 Evidence / Views / supplement raw are untouched. Where only a rendered page was read, no original-page HTML is claimed.

## 1. DeepInfer (ISA-001) — official README, live rendered read 2026-10-25

- URL: `https://github.com/deepseek-ai/DeepInfer` (rendered README observed 2026-10-25; mutable `main`, not a pinned release).
- Captured passages (rendered):
  - "DSpark and confidence-scheduled verification: accelerate decoding with draft tokens … Set `DEEPINFER_ENABLE_MTP_VARLEN=1`; `DEEPINFER_USE_NEXTN_DECODE` controls the maximum draft length (default: 5)."
  - "Batch-invariant inference: keep model results identical across different batch compositions. Enable with `DEEPINFER_BATCH_INVARIANT=1` (NVIDIA only)."
  - "Deterministic sampling: produce identical outputs for identical input tokens and sampling parameters. Set `DEEPINFER_BATCH_INVARIANT=1 DEEPINFER_ENABLE_MTP_VARLEN=0` and pass a fixed `seq_seed` to `SamplingParams` (NVIDIA only)."
- Pinned edition source already accepted: `supplement-src-d0805b13331ce793` (README, 2026-10-21T04:55:43Z, SHA prefix `b55624158ada4dc2`), `supplement-src-e20f1cffc1444d3a` (`deepinfer/environ.py`, 8738B, SHA prefix `fe2c531989c419f0`), pinned commit `9bd9cf24` cited in Architecture §2.2.
- Editorial binding: DSpark variable-length MTP (`MTP_VARLEN=1`, `NEXTN_DECODE` default 5 / 0 disables) and deterministic sampling (`MTP_VARLEN=0` + `BATCH_INVARIANT=1` + fixed `seq_seed`, NVIDIA only) are two DISTINCT illustrative setups, MUST NOT be shown as simultaneously enabled. No fake runnable command is asserted.

## 2. Voxtral (ISA-002) — three official documents contradict; UNRESOLVED 2026-10-25

- (a) Launch announcement `https://mistral.ai/news/voxtral-3/` (rendered, observed 2026-10-25): "The text-to-speech model, *Voxtral Mini TTS 3*, introduces new voices … with support for **35+ languages and 50+ dialects**." Highlights: "Natural speech … for **35+ languages and 50+ dialects**." Library section: "Voxtral TTS supports over **35 languages** and regional dialects." "Voice Presets are available in **18 languages**" (list: Arabic, Brazilian Portuguese, Catalan, Chinese Mandarin, Dutch, English US/UK, French, German, Greek, Hindi, Italian, Korean, Norwegian, Russian, Spanish, Vietnamese).
- (b) Model card `https://docs.mistral.ai/models/voxtral-mini-tts-3-0` (rendered, observed 2026-10-25): "Our state-of-the-art text-to-speech model … **Supports 9 languages**, streaming with ~90 ms time-to-first-audio, 5 output formats, 34 emotion tags, and 2 pace tags." Header: October 20, 2026, Public Preview, v3.0.
- (c) Language matrix `https://docs.mistral.ai/studio/audio/specs-and-limits/languages` (rendered, observed 2026-10-25): "Each model has its own list of supported languages"; table: `voxtral-mini-tts-3-0` / Speech generation / "**35 languages, 50+ dialects**"; TTS section: "Voxtral TTS 3 supports **35 languages with 50+ regional dialects**. Preset voices are available in the following languages" followed by a 22-row table (ar, ca, zh, nl, en_GB, en_us, fr, de, hi, hu, it, ja, ko, no, pl, pt, ro, ru, es, tr, uk, vi); note: "The model supports more languages than have preset voices. For languages without a preset, use voice cloning."
- Editorial binding: **UNRESOLVED_VENDOR_DOC_CONFLICT**. The three first-party pages do not agree on one universal TTS language number (35+ vs 9 vs 35/50+; presets 18 vs 22 rows). It is NOT established that "9 = preset voices" (preset lists are 18/22, not 9). Architecture P5 §5.1 therefore separates STT file transcription (50), realtime transcription (35+/45), TTS speech generation (announcement 35+/50+ vs model card 9 vs matrix 35/50+), presets, voice cloning, and the 11-language evaluation sample (capability ≠ support count). No universal TTS language number is asserted pending a versioned Mistral clarification.

## 3. Nemotron / Flint counting (ISA-003)

- Nemotron BF16 card `https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16` (rendered, observed 2026-10-25): "Model Summary: **Total Parameters 8B (4B effective)**"; "Architecture: Gemma-4-E4B"; "Network Architecture: Gemma-4-E4B"; "Number of model parameters: 8B (4B effective parameters)"; "License: OpenMDW-1.1"; "This model has been post-trained on the Google Gemma 4 model, and use of the Google Gemma 4 model is governed by Apache License, Version 2.0."
- Flint card `https://huggingface.co/RecursiveSI/flint` (rendered, observed 2026-10-25): "Flint is Recursive's mixture-of-experts language model for coding agents, with **39.8 billion total parameters and approximately 2.5 billion active per token**." Specifications table: "Total parameters 39.8B; Active parameters per token Approximately 2.5B, **including the output head**"; footnote: "The active-parameter convention **includes the output head and excludes the full input embedding matrix**. The active body alone is approximately 2.2B parameters. '40B-A2.5B' is the rounded model-size designation."
- Editorial binding: 8B total / 4B effective (Nemotron) and 39.8B total / ~2.5B active per token (Flint, output-head-in / input-embedding-out) use NON-EQUIVALENT counting conventions and are shown in separate columns with the convention in the header. OpenMDW-1.1 (weights terms) and Gemma-4 base Apache-2.0 are never conflated; OSI approval is UNVERIFIED.

## 4. FLUX arithmetic (ISA-004)

- Vendor blog `https://fal.ai/blog/introducing-flux-3-max-by-fal` (rendered, observed 2026-10-25): "FLUX 3 Max generates a 10-second video in **12.45 seconds**, compared with **277.80 seconds for Seedance 2.5**. That's **26.5× faster, with 96.2% lower latency**."
- Independent recomputation (this pass, no new measurement): `277.80/10.95=25.3699→≈25.37x`; `277.80/12.45=22.3133→≈22.31x`; `(277.80-12.45)/277.80×100=95.5184%→≈95.52%`. The vendor's 26.5x/96.2% pair is arithmetically incompatible with its own 12.45s/277.80s table (12.45s yields 22.31x/95.52%, not 26.5x/96.2%). The 10.95s PR origin raw is still not archived in edition sources.
- Editorial binding: Architecture §4.2 labels the three quotients as *independent recomputation of vendor figures, not independently measured performance*; resolution / 10-second generation length / GPU / batch / quality / cold-vs-warm comparability remain UNKNOWN; the fastest-headline prohibition stands.

## 5. Decisions billing (ISA-005)

- Guide `https://developers.openai.com/api/docs/guides/decisions` (rendered, observed 2026-10-25): model `gpt-6-luna` only; "Ask up to **400 questions per request**, up from 200 during the public beta."; caching: "Check `usage.input_tokens_details.cached_tokens` for cache reads and `usage.input_tokens_details.cache_write_tokens` for cache writes. Both counts are included in `usage.input_tokens`."; "Pricing and availability: With `gpt-6-luna`, uncached input costs **$0.10 per 1M tokens**. Prompt cache hits receive discounted input pricing; **cache writes are charged**. … **Output tokens are not charged**."; "Regional processing premiums and long-context input pricing multipliers apply."
- Editorial binding: $0.10/M = uncached input only; $0.01/M = cached reads; **cache writes billed separately**; regional + long-context multipliers apply; **zero output-token charge ≠ zero total bill**; 400 questions = **per request**, not per account/quota. General API pricing is not conflated with special processing tiers.

## 6. Temporal / availability anchors (ISA-009)

- Kimi: X announcement `2026-10-23T17:15:24Z` IN (API first), weights Nov4 FUTURE — announcement / weights distribution / reproducibility kept as separate status columns.
- 1Password/Duet: "coming soon" / waitlist (US Pro/Max first) at cutoff — never rendered as live.
- TanStack: GH release `2026-10-22T15:18:14Z` / registry `15:21:49Z` IN as product proxy; Oct23 blog is day-only (UNRESOLVED clock) and is never cited as the product timestamp.
- GitHub Metrics: published `2026-10-23T23:42:03Z` = 1h42m03s AFTER the exclusive cutoff → POST_CUTOFF / NON_MATERIAL / OUT, never W43-selected. Grok X ledger: audit/provenance binder, NEVER_STORY.

## 7. What was NOT newly archived

- No new `evidence/v2/*`, `supplement-raw/*`, Discovery, Screening, Materiality, Completeness, Production State, Checkpoint, or Human Gate bytes were created or mutated. Supplement IDs cited above are the pre-existing accepted r4 authorities. This crosswalk is an edition-local reading note only.
