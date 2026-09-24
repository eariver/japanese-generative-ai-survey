# TS-002 Discovery negative space — 2026-09-24 (first run, primary-technical)

Collector run `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`.
Refresh `beyond-text-discovery-r2` observed `2026-09-24T09:43:32Z` (date repair + bounded gap-fill; r2 dispositions appended per gap).
Status: `SUMMARY_CAPTURED`; full-body consumption deferred to Evidence stage.
X/community pass explicitly NOT run (deferred per execution contract).

## G01 — Closed image capstone architecture (GPT Image 2.5, Nano Banana 2 internals)
Searched first-party release pages and model cards. No public architecture/mechanism authority found.
Disposition: capability/workflow cases only; no undisclosed-architecture inference permitted.

## G02 — Closed music capstone internals (Suno v6, ElevenLabs Music)
Release notes and capability docs captured. No model-card-grade architecture, training, or evaluation methodology found.
Disposition: capability/ecosystem cases; Lyria 3.5 card and Stable Audio 3 carry the mechanism weight.

## G03 — Suno/ElevenLabs independent evaluation
No independent measurement, reproduction, or listening-study authority located in the primary pass.
Disposition (r1): negative space for Evidence gap-fill or the later X/community reception pass.
Disposition (r2 2026-09-24, PARTIALLY_FILLED): BT-D136 (arXiv 2506.19085, 2025-06) adds an independent listening-study authority covering Suno v3/v3.5 (12 models, 6,000 songs, 15,600 pairwise comparisons, 2,500+ participants; Suno v3.5 top Elo; FAD-CLAP-MA best perception correlation). ElevenLabs independent evaluation remains thin; Suno v5/v6-era independent study still open.

## G04 — FLUX.2-klein sub-second runtime independent measurement
Vendor speed claim captured (BT-D100). No independent latency/VRAM measurement located.
Disposition (r1): vendor claim until independently reproduced; runtime gap-fill candidate.
Disposition (r2 2026-09-24, PARTIALLY_FILLED): BT-D137 (Inference Bench 2026-04-12) adds an independent klein-4B measurement with documented methodology (H100, Diffusers bf16: 1024px 4-step 0.57s, VRAM 16-18GB). Consumer-GPU replication and multi-config matrices remain for the Evidence/X passes.

## G05 — Wan flagship 2.5/2.6/2.7/3.0 technical authority
Verified at execution time (2026-09-23): last open-weights flagship is Wan2.2 (2025-07-28, Apache 2.0);
2.5-Preview/2.6/2.7/3.0-beta are API-only with no public weights (secondary corroboration only).
Disposition: Wan2.2 is the open mechanism anchor; Wan 3.0-class capability is closed-API negative space.

## G06 — Sora mechanism authority
Sora/Sora 2 pages captured as historical/lifecycle cases. No peer-reviewed architecture report published.
Disposition: lifecycle case with exact dates (product end 2026-04-26; Videos API removal 2026-09-24); not a mechanism anchor.

## G07 — Long-form music structure metrics
No widely adopted automatic metric for verse/chorus structure, motif persistence, or lyrics coherence found beyond
vendor model-card methodology (Lyria 3.5) and human-study protocols.
Disposition: methodology weakness to state explicitly; do not rank music systems by FAD alone.

## G08 — Audio-video synchronization metrics
VBench-family and model-card claims captured; no standalone widely adopted AV-sync benchmark with published validity
analysis located in this pass.
Disposition (r1): evaluation gap for Evidence gap-fill.
Disposition (r2 2026-09-24, PARTIALLY_FILLED): BT-D129 (Wav2Lip, ACM MM 2020: SyncNet LSE-C/LSE-D + ReSyncED benchmarks) grounds the lip-sync methodology lane, and BT-D130 (Yaman et al., CVPRW 2024: AV-HuBERT AVSu/AVSm/AVSv + documented SyncNet validity critique with user-study disagreement) bounds it — LSE scores must not be treated as comparable truth across conditions. Sound-event timing / semantic alignment for jointly generated AV content remains vendor-claim-only (Veo T2VA human preference); no standalone widely adopted event-timing benchmark found.

## G09 — Open-weight speech cloning runtime/measurement
YourTTS/Seed-TTS papers captured; current open speech-cloning deployment/runtime independent evidence thin.
Disposition (r1): candidate for the later X/community reception pass, not architecture authority.
Disposition (r2 2026-09-24, FILLED): BT-D132 (F5-TTS, ACL 2025: open flow-matching DiT zero-shot TTS, RTF 0.15, open code+checkpoints) plus BT-D133 (CosyVoice 2, 2024-12: open streaming zero-shot TTS with chunk-aware causal flow matching and documented deployment surfaces) give the open lane technically grounded mechanism + runtime authority. Community deployment-friction evidence remains for the later X pass.

## G10 — Streaming speech-to-speech latency methodology
Vendor API pages captured; comparable real-time-factor/time-to-first-audio methodology across vendors not found.
Disposition (r1): runtime comparison must not be constructed from incompatible vendor numbers.
Disposition (r2 2026-09-24, FILLED as methodology): BT-D134 (Moshi, 2024-09: full-duplex S2S framework, 160ms theoretical / ~200ms practical latency, turn/interruption modeling, open weights) provides the latency/architecture reference; BT-D133 defines first-package latency L_TTS for streaming TTS; BT-D135 (MTR-DuplexBench, 2025-11: stop/response latency + turn-taking/interruption/pause/background-speech success criteria) provides the vendor-neutral measurement vocabulary. Cross-vendor leaderboard construction remains prohibited.

## G11 — Video physics/commonsense evaluator validity
VBench-2.0 intrinsic-faithfulness dimensions captured; independent validity/reproducibility studies thin.
Disposition (r1): report vendor attribution; no cross-model ranking across conditions.
Disposition (r2 2026-09-24, FILLED): BT-D131 (VideoPhy, ICLR 2025: 688-caption physics-commonsense benchmark with SA/PC human judgments — best model 39.6% joint — plus VideoCon-Physics auto-evaluator with documented limits including near-random GPT-4-Vision judgments). Vendor physics scores must be read against this validity ceiling, not as comparable truth.

## G12 — Rectified-flow vs diffusion ablations in video/audio
Flow-matching/rectified-flow papers are image-domain; modality-transfer ablations for video/audio not located.
Disposition (r1): do not assert flow superiority outside evidenced domains.
Disposition (r2 2026-09-24, PARTIALLY_FILLED): BT-D138 (FiVE, arXiv 2503.13684: head-to-head diffusion vs rectified-flow video-editing benchmark, 15 metrics; RF 10-15x faster per frame with competitive quality) evidences the flow-vs-diffusion comparison inside the video-editing domain. Pure-generation ablations remain thin; no superiority claim outside evidenced domains.

## Non-gaps (explicitly covered, not negative space)
Representation/tokenization (VAE/VQ/codec/video-tokenizer), GAN lineage, AR lineage, DDPM/score/latent/DiT/flow,
guidance, spatial/reference control, editing lane, speech/music/video lineages, runtime distillation recipes,
image/audio/video evaluation methodology, convergence cases, provenance mechanisms.
