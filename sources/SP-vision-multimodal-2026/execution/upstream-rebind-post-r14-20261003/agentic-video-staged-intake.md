# Agentic Video Understanding (VM-D112) — STAGED intake specs (NOT canonical)

Status: staged for the Human-gated pipeline run. NOT admitted: no Discovery acceptance update to the canonical file, no screening acceptance, no Evidence task/card, no materiality/selection/architecture binding. Formal admission requires Human-gated return to DISCOVERY_COLLECTED and the canonical rebuild chain (see repair report §Agentic Video).

## Screening decision (staged)

- discovery_id: VM-D112
- decision: KEEP
- reason: Official Google release 2026-09-01 (in-cutoff): query-driven on-demand timeline navigation replacing static 1-FPS ingest; distinct token-acquisition mechanism (P09/VM-O10) and third video-processing contract distinct from offline ingest and streaming state (P11/VM-O12); non-duplicate of Flash-VStream (model-side streaming memory vs API-side server tool loop); figures vendor-reported ceilings requiring Evidence-stage benchmark binding.
- scope_tags: [VM-O10, VM-O12]
- verification_targets: Evidence-stage full-body verification of official docs pages (bind access date); benchmark list/split binding incl. LongVideoBench scope; static-vs-agentic token-math worked example.
- duplicate_group: null
- confidence: medium

## Evidence drafts (staged, ≤500 chars each; subject ev-vmd112; entity MODEL "Agentic Video Understanding (Google, 2026)")

- M1 static default (AUTHOR_CLAIM): "Static processing extracts video frames at a fixed rate (default 1 FPS, adjustable via API) and places them into context in a single pass; audio at 1Kbps mono with per-second timestamps. Custom FPS/clipping options apply in static mode only." [ai.google.dev video-understanding, Technical details]
- M2 agentic loop (AUTHOR_CLAIM): "Agentic understanding replaces upfront full-timeline ingest with a server-side Think→Act→Observe loop: a lightweight reference pointer (metadata only), prompt-based planning of what to inspect, and targeted tool calls fetching only needed video slices." [aistudio developer guide]
- M3 goal-directed acquisition (AUTHOR_CLAIM): "The model takes a goal-directed role deciding what to watch, at what speed, and through which modality (frames, audio, transcript), invoking an internal tool to load the relevant part of the video file per query." [blog post body, 2026-09-01]
- M4 adaptive rate/resolution (AUTHOR_CLAIM): "Agentic processing adaptively adjusts frame rates and resolution on the fly based on the prompt — e.g. 5–10 FPS for fast motion, 0.1 FPS to skim — and resamples interesting windows at higher FPS for rapid motion inspection." [docs + guide + blog]
- I1 input surface (AUTHOR_CLAIM): uploads + YouTube via Gemini API; processing='agentic'; modes mixable per video.
- I2 on-demand modalities (AUTHOR_CLAIM): timeline navigation requesting transcripts/frames/audio on demand.
- I3 multi-turn state (AUTHOR_CLAIM): explicit context preservation across turns required.
- E1 token reduction (AUTHOR_CLAIM): up to 88% fewer tokens, long-form condition, materialized-media billing.
- E2 cost reduction (AUTHOR_CLAIM, separate): up to 66% lower cost, benchmark scope, standard pricing.
- E3 quality change (AUTHOR_CLAIM, separate): up to ~7% higher quality, 3.7 Flash chart scope.
- E4 TTFT caveat (AUTHOR_CLAIM): navigation may increase TTFT on clips <5 min; static suits short clips.
- E5 token accounting (AUTHOR_CLAIM): thinking tokens + tool prompt tokens.
- B1 vendor ceiling (INFERENCE); B2a model scope 3.7/3.6/3.5-Lite + 3.8 in docs by 09-16 (AUTHOR_CLAIM); B2b binding requirement (INFERENCE); B3 NOT streaming (INFERENCE).

## Selection/Architecture placement (staged recommendation)

- Selection: new node, architecture_usage PRIMARY, transition-anchor, LONGFORM_SPECIAL primary-narrative (fallback: SUPPORTING cross-package evidence if review judges closed-vendor depth insufficient).
- Architecture: primary home P09 TRANSITION_NODE_TREATMENT; P11 contract-level touch (third-contract statement, no new depth class unless review requires).
- Depth budget: P09 TRANSITION 3→4; page budgets untouched.

## Discovery record (staged)

- discovery_id VM-D112, origin GAP_FILL, research_pass 1, parent_refs [], obligations [VM-O10, VM-O12]; locator blog.google introducing-agentic-video-in-gemini (2026-09); raw: raw/discovery-observations-currency-supplement-agentic-video.md.
- NOTE: schema-valid GAP_FILL staged at execution/upstream-rebind-post-r14-20261003/discovery-v2-supplement-112.jsonl + discovery/discovery-accepted-supplement-agentic-video-20261003.json. Canonical discovery-accepted-v2.json (111) untouched. A validator finding during screening staging (validate_discovery_expansion) confirmed NO bounded append path exists for genuinely-new-source records (derived expansion requires parent-rooted identity); formal admission needs Human-gated stage re-entry. Staged files retained as exact intake materials.
