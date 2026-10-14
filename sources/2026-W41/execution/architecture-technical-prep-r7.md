# W41 Architecture technical preparation / readiness r7 (per-package, Sol-facing)

Status: `EDITION_LOCAL / TECHNICAL_PREP / ARCHITECTURE_INPUT`
Date: 2026-10-12 JST
Architecture: `sources/2026-W41/architecture-v2.json` SHA `3554041e…` (6 packages, PROPOSED)
Exclusion: `execution/nanobanana-legacy-negative-exclusion-r6.md` binding; trace exception
`execution/architecture-trace-exception-r7.md`. Admissible blog language only in reader prose.

Conventions: [VENDOR] = publisher-measured, never independently reproduced. [READ] = consumed
excerpt level (DIRECT_READ full body only for textGrain blog and Decisions/Ultrafast changelog excerpts
via Muse; else delegated verbatim BOUNDED_EXCERPT). Claim/source IDs are Evidence task and supplement IDs.

## P1 — Frontier rollout week (PRIMARY GPT-6 UI + Haiku)

Thesis: rollout mechanics plus price cards carry the lead; benchmarks do not.
Mechanisms actually supported:
1. Tiered rollout mapping (GPT-6): paid tiers Oct 7 versus Free/Go Oct 8, Chat-tab scope, Sol-for-paid and
   Luna-for-Free/Go assignment [READ: page Vaughn, delegated verbatim; claim-1/2 VENDOR_CLAIM].
2. Start-latency definition (GPT-6): 44% sooner answering on web-search questions is time-to-start via
   interleaved thinking/answering [READ: distinction verified on page; vendor-measured denominator = GPT-6 Instant
   versus 5.6 Instant web-search subset; wall-time denominator absent].
3. Split price card (Haiku): at-or-below versus above 100k with cache-read rates plus Sonnet halving
   [READ: rates verified as stated; claim VENDOR_CLAIM].
4. Publisher bench table (Haiku): GDPval/OSWorld/HLE/TB4 values [VENDOR only; independent reproduction pending;
   system-card full evals unfetched].
Vendor-vs-reproduced: all numerics [VENDOR]; nothing independently reproduced. Denominators known only for the
44% subset (web-search questions) and Haiku table labels; no end-to-end latency denominator exists.
Uncertainty/negatives: system-card numbers not enumerated; pricing absent on GPT-6 page; delegated (not Muse
first-hand) GPT-6 read. Dedup: latency discussion lives here once; P2 Ultrafast box references back, does not
re-explain. JP relevance: tier timing and price cards directly affect JP Plus/Free and developer cost planning;
Sol/Luna naming kept in English with katakana gloss at first use (no over-kanji invention).
Downgrade check: no downgrade needed; both members support lead weight with stated boundaries.

## P2 — Agent and Decisions infrastructure (PRIMARY Decisions; SUPPORTING decider, embed, Ultrafast, Gemini stub)

Thesis: one verified changelog against forum observations and a stub; do not merge distribution channels.
Mechanisms:
1. Decision endpoint (Decisions beta): `v1/decisions` with gpt-6-luna binding, beta status [READ: changelog entry
   verified first-hand via Muse DIRECT_READ of excerpt; supplement-src-df537ff932f91343].
2. Beta performance framing: 10x versus Responses API [VENDOR, methodology absent on page; guides and pricing pages
   unfetched; r2 community $0.10/M input-only not on changelog].
3. Forum decision models (decider): updated open-weights multimodal decision model, HF Decision Index top claim,
   $0.02/M input and Decision Bench 94.5% on 1071 cases at $0.017/1k [VENDOR forum-stated; HF README unfetched;
   params beyond 27B title, license and repo URLs absent].
4. Service tier (Ultrafast): `service_tier: ultrafast` for gpt-6.1-sol on Responses API with rate-limit scope and
   global plus US/EU residency [READ: entry verified; supplement-src-ec5b609a5f24671e]; purpose is inter-token
   latency with no on-page numbers [no latency denominator exists].
Vendor-vs-reproduced: changelog entries [READ as stated]; all speed, price and bench figures [VENDOR].
Uncertainty: embed pair is title-only (two late-interaction models, specs and paths unfetched) kept as one-liner;
Gemini stub has no GA/SKU/price/region/split (Cloud blog unfetched, customer figures r2-stated unreverified).
Dedup: 44% start-latency (P1) versus inter-token purpose (P2 box) cross-referenced, not redefined. JP relevance:
beta API pin and residency matter to JP agent builders; forum prices in USD/M with JP-yen gloss only if sourced.
Downgrade applied: embed to one-liner, Gemini to comparator box (thin standalone explicitly rejected).

## P3 — Shipped versus promised weights plus speech (PRIMARY Kolibri; SUPPORTING Liquid, EGemma, Beam, Mistral, Clef, Nova)

Thesis: availability table is the article; promised weights are comparators with dates, never releases.
Mechanisms:
1. MoE scale and context (Kolibri 78B/3B, 1M; Beam 501B/23B preview; Mistral 52B active per docs with 1M;
   Qwen3-Omni-30B-A3B per Clef blog) [READ as stated; all VENDOR].
2. Availability states: Kolibri HF downloadable with Apache-2.0 stated-location; Liquid HF stated; EGemma HF plus
   Kaggle stated with card unfetched; Beam later-this-month intent; Mistral end-of-month with preview API today
   [READ as stated; downloads and SPDX unverified except stated locations].
3. Embedding specifics (EGemma): 740M split, 768-d MRL, 8K context, MTEB-Code vendor figure with full metrics
   deferred to unfetched card [VENDOR; architecture table snippet-only].
4. Speech GA versus omni claim (Nova GA Oct 5 with four regions and 256K versus Clef omni price and flash cut)
   [READ as stated; Nova pricing numerics absent; Clef HF/SPDX unverified; Clef timestamp pin JSON-LD 18:27:34Z
   in-window versus 23:11Z post-cutoff X].
Vendor-vs-reproduced: every scale, price, bench and availability cell [VENDOR]; download-verified column stays
honest (stated-location only, SPDX unverified). Denominators: Decision Index values without protocol; MTEB-Code
delta without full table; vendor benches (AIME/GPQA/DeepSWE/TB/AIME) without independent runs.
Uncertainty: Kolibri tables truncated; Mistral 49B-X versus 52B-docs unresolved by design; Beam/Reflection
weights not downloadable. Dedup: decision-model Index discussion points to P2 once; speech latency not claimed.
JP relevance: Apache-2.0 and HF paths matter to JP builders; ap-northeast-1 region noted for Nova; EU Kolibri
sovereignty angle glossed without overclaim. Comparison table (required): columns stated-license,
stated-location, download-status, weight-date; rows seven members in availability order.
Downgrade applied: Beam and Mistral to comparators; Nova and Clef to speech comparator boxes.

## P4 — Image brief (SUPPORTING Nano Banana 2.1)

Thesis: card spec box with one narrowed blog line; no ranking, no absence claim.
Mechanisms:
1. Card spec block: Gemini 3 series and 3.6 Flash base, 1M input, 4K image plus 64K text output, seven-channel
   distribution [READ: bounded excerpt supplement-src-360435193adc7df6; VENDOR_CLAIM].
2. Vendor Elo: side-by-side figure [VENDOR; arena basis unresolved per DailyX secondary].
Admissible blog line only: matching issuer blog post not found among pages checked on 2026-10-12 with explicit
not-proof-of-absence qualifier [READ: claim-2 PRIMARY_FACT]. Legacy categorical spans confined to machine
boundaries trace (trace exception r7) and absent from all reader prose (verified).
Uncertainty: pricing and license absent; docs page unfetched. Dedup: image-model discussion occurs only here.
JP relevance: creator-audience model note kept factual; no use-case invention. This package stays a small brief
by evidence boundary; expansion without a fetched docs page or arena basis would be padding.

## P5 — Provenance week (PRIMARY textGrain; SUPPORTING SynthID)

Thesis: read numbers versus stated scope; no efficacy transfer between modalities.
Mechanisms:
1. Watermark operating points (textGrain): 1% false-positive rate near 80% at 200 tokens and near 95% at 400
   tokens [READ first-hand blog; vendor-run, not independently reproduced].
2. Edit robustness and quality: edit-weakening numbers plus Astra quality table [READ blog; VENDOR].
3. Rollout and gating: API opt-in now, EU ChatGPT/Codex coming weeks, researcher-gated detector [READ blog].
4. Portal scope (SynthID): English-global from Oct 7, image/video/audio from Google or partners including soon-Apple,
   scale counts, text excluded [READ blog excerpt; VENDOR for partner coverage and scale].
Vendor-vs-reproduced: all figures [VENDOR]; textGrain is first-hand-read vendor-run, SynthID is excerpt-read
vendor-stated scope. Denominators known for textGrain token points; no detection-accuracy denominator exists for
the portal (benchmarks absent, body JS-shell unfetchable). Uncertainty: tech-report PDF binary-unparsed (no method
beyond blog facts); select-model list, pricing and license absent; partner claims unverified via fetch.
Dedup: FPR discussion lives here once; P4 image model does not borrow watermark numbers. JP relevance: EU precedent
and researcher gating directly relevant to JP policy and research readers; Kakao partnership noted as Asia signal.
Comparison table (required): artifact, modality scope, gating/availability, verification-status limits.
Downgrade check: no downgrade; textGrain supports deep-dive weight on blog facts, SynthID supports scope brief.

## P6 — Safety and science briefs (SUPPORTING Cyber, Math, Ironclad)

Thesis: three bounded briefs with explicit non-claims.
Mechanisms:
1. Program terms (Cyber): eleven founding partners, opt-in free scanner, model-generated proof-of-concept reports
   without human review, greater-than-90% true-positive expected [READ as stated; VENDOR for efficacy; scanner post
   and form internals unfetched; no measured outcomes].
2. Results listing (Math): unnamed-model mathematical results with repository, partial Lean formalizations, ten
   reasoning summaries and average compute stat [READ as listed; VENDOR; file counts and licenses unenumerated;
   model not released with no date].
3. Simulated eval (Ironclad): eleven EDGAR-simulated contracting tasks with vendor accuracy and time deltas as
   simulated estimates [READ as stated; VENDOR; rubric, per-task and training details absent; provisional only;
   product launches separate].
Uncertainty: no deployment measurement anywhere in this package. Dedup: agent-eval commentary points to P2 once;
no safety-performance synthesis across Cyber and provenance. JP relevance: security-audience program note, Lean
hook for science readers, contracting-eval design note for enterprise automation; all kept boundary-explicit.
All three stay briefs; promotion to deep-dives would require fetched scanner post, enumerated repo, or released
rubric respectively.

## Cross-package controls

Duplication control: latency (P1 versus P2 box), Decision Index (P2 versus P3 pointer), watermark numbers (P5 only),
speech (P3 only), image (P4 only), simulation (P6 only with P2 pointer). No HOLD imported for padding; 13 HOLD,
2 INSPECT and Grok REJECT appear only in attention and methods, never as article placements.
Japanese terminology discipline: model and product names in English with katakana gloss at first use; tier, price,
license and residency terms translated literally from pages without over-kanji invention; machine-readable editorial
JSON (this prep plus dossier) reserved for translator and claim validation before TeX.
Comparative tables required in P1, P3, P5 are specified above with columns; figure sourcing is first-party pages and
bounded excerpts only; no rendered pagination is fixed.

(End of file)
