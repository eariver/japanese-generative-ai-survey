# TS-002 Human Architecture Review dossier (fresh review, no decision)

Issue: `SP-beyond-text-2026` / GitHub Issue `#526`
Branch: `special/beyond-text-2026-work`
State: `ARCHITECTURE_ESTABLISHED`, next `ARCHITECTURE_REVIEW`,
  `human_gates.architecture_review = pending` (no approval fabricated or resolved).
Canonical inputs: `architecture-v2.json` (PROPOSED, 14 packages) +
  `architecture-review-summary-v2.json` (`READY_FOR_ARCHITECTURE_REVIEW`) +
  `architecture-review-attention-v2.json`, all Core-validated.

## 1. Proposed title / subtitle

Unchanged working title: **Beyond Text — 画像・音声・音楽・映像生成AIの技術史**.
No subtitle change proposed at this gate.

## 2. Central thesis / reader promise

高次元連続メディア（画素・波形・フレーム・動き・同期音）を生成可能にしたのは、
表現・予測/生成目的・条件づけ・制御/編集・時間構造・サンプリング/実行・評価の
選択の進化である。本Specialは有名製品のカタログではなく、画像・音声・音楽・映像の
各モダリティで「何がボトルネックで、何が変わり、何が改善し、何が悪化し、
何が継承されたか」を技術史として構成する。

Reader promise: after reading, the reader can explain for each modality which
representation made generation tractable, which objective/architecture/sampling
choices followed, how control and editing diverged from generation, where
long-horizon competence breaks, what deployment costs, and how evaluation
claims must be read.

## 3. Chapter and section outline (14 mechanism-led packages, drafting order)

1. `arch-representation` — 表現と圧縮：生成可能にする短縮の歴史 (6 primary / 5 supporting)
2. `arch-paradigms` — 生成パラダイムと目的関数 (12 / 5)
3. `arch-conditioning` — 条件づけとアライメント (4 / 3)
4. `arch-control` — 制御と参照：空間・参照・主体性の保存 (3 / 4)
5. `arch-editing` — 生成から編集へ (4 / 3)
6. `arch-speech` — 音声・声の系譜 (7 / 8)
7. `arch-music` — 音楽・一般音響の系譜 (4 / 4)
8. `arch-video` — 映像の系譜 (4 / 4)
9. `arch-temporal` — 長時間・同期・編集の一貫性 (1 / 3)
10. `arch-runtime` — 実行と配備の経済 (4 / 2)
11. `arch-evaluation` — 評価の方法論 (5 / 5)
12. `arch-convergence` — 収束問題：統合か連携か (3 / 3)
13. `arch-capstones` — 2025-2026 capstone群：能力・workflow・lifecycleの証拠 (0 / 27)
14. `arch-reception` — 受容と counter-signal (0 / 1)

Chronology runs inside semantic chapters. Chapters 1-12 are mechanism-led;
13-14 are evidence-bounded context chapters (no hidden-architecture inference).

## 4. Page-budget estimate by chapter (target 80 / max 96; guidance, not a hard cap)

representation 8 / paradigms 10 / conditioning 5 / control 5 / editing 5 /
speech 9 / music 7 / video 9 / temporal 4 / runtime 5 / evaluation 7 /
convergence 4 / capstones 8 / reception 2 / front+back matter 6 (sum 84 incl. rounding).
Depth is preferred over artificial compression; no padding to reach target.

## 5. Chapter → transition-ledger / Evidence mapping

All 43 ledger entries map to packages: representation T-REP-01..07 →
arch-representation; paradigms T-PAR-01..09 + runtime T-RT-01 →
arch-paradigms/arch-runtime; conditioning/control/editing T-COND/T-CTRL/T-EDIT →
arch-conditioning/control/editing; speech T-SP-01..04 → arch-speech;
music T-MU-01..03 → arch-music; video T-VI-01..05 → arch-video/arch-temporal;
evaluation T-EV-01/02 → arch-evaluation; convergence T-CV-01 → arch-convergence;
reception T-X-01 → arch-reception; lifecycle T-CLOSED-01 → arch-capstones.
Each retained transition keeps bottleneck → change → improvement →
trade-off → succession shape where sources support it.

## 6. Representation coverage map

Raw pixels/waveforms/frames (PixelRNN, WaveNet) → continuous latents (VAE, LDM
autoencoder, Stable Audio AE) → discrete codebooks (VQ-VAE/VQGAN/dVAE) →
RVQ neural codecs (SoundStream/EnCodec/DAC) → semantic/acoustic hierarchies
(AudioLM, MusicLM, VALL-E) → spatiotemporal video compression (MAGVIT,
Wan2.2-VAE). First-class axis with compression/fidelity/editability bounds.

## 7. Modality coverage map (Discovery 139)

image 56 / speech 22 / audio 10 / music 13 / video 30 / crossmodal 8.
Non-image modalities hold 83/139 records (60%) with their own representation,
mechanism, control/temporal, runtime, and evaluation stories in chapters 6-9.
Image does not collapse other lanes into appendices.

## 8. Architecture-vs-objective separation check

U-Net vs Transformer/DiT (architecture) kept distinct from AR vs adversarial vs
diffusion/score vs flow matching (objective/process) and from DDIM/solver/
distillation (inference/sampling) in packages arch-paradigms/arch-runtime;
validator `validate_architecture` PASS confirms separation is structurally held.

## 9. Generation-vs-editing separation check

De-novo generation vs inpainting/local/instruction/reference editing with
preservation targets is a dedicated package (arch-editing, 4/3) plus video
editing benchmark (FiVE) and audio continuation/inpainting in modality chapters.

## 10. Temporal/long-horizon coverage check

Local fidelity vs short-range coherence vs long-range structure vs
identity/object permanence vs AV/lip sync vs continuation vs edit consistency
vs multi-round behavior are separated in arch-temporal plus modality chapters;
one-sample claims never stand for long-horizon competence.

## 11. Runtime/deployment coverage check

Steps/NFE, latency/RTF/first-package latency, VRAM/memory, quantization/offload,
local/open vs closed deployment, hardware binding preserved where disclosed;
unbound numbers never compared; single-lab limits stated.

## 12. Evaluation-validity coverage check

FID/IS, FAD/CLAP-audio, WER/speaker-similarity/listening, music preference
studies, VBench/VBench-2.0, AV/lip-sync metrics with critiques,
physics/commonsense ceilings, automatic-vs-human validation — each with
modality/protocol context; no cross-condition leaderboard.

## 13. Closed-system boundary check

27 closed records are SUPPORTING capability/workflow/lifecycle context only.
Only vendor-disclosed fragments recorded (D100 flow+distill, D111 latent
diffusion over temporal latents, D113 autoencoder+diffusion+adversarial,
D124 MoE+VAE). No hidden architecture/training/tokenizer inference anywhere
(validator `closed_non_inference` PASS at Evidence; boundary rechecked here).

## 14. TS-002 / TS-003 boundary check

CLIP/T5 encoders, unified vision-language models, and audio LLMs appear only as
conditioning/evaluation/convergence machinery for generation; perception-side
histories (detection, segmentation, OCR, VQA, embodied reasoning) excluded.

## 15. Unresolved / PARTIAL / NEEDS_MORE handling plan

8 PARTIAL (EDM abstract, VALL-E 2 tables, Seamless v1/v2 boundary documented,
Movie Gen methods, FID full text, LibriSpeech protocol, C2PA spec, Imagen hub,
Moshi eval) and 5 NEEDS_MORE/HOLD (SD repo, Phenaki, ITU text, Kling IR, Wan hub)
are carried explicitly: draft must state barriers, use abstract/snippet-level
facts only at their level, and never upgrade them by narrative confidence.
Completeness LIMITED (4 SATISFIED / 8 LIMITATION) with residual limitations.

## 16. LOW_SIGNAL handling plan

Duplex interruption measurement, cross-lingual cloning degradation, long-range
music structure, metric-vs-preference contradictions, Nano Banana editing corpus,
few-step ablations, pure-generation flow-vs-diffusion, consumer klein
replication, ElevenLabs independent eval, Wan 2.5+ authority, Sora mechanism:
reported as LOW_SIGNAL/open, never inflated, never ranked.

## 17. Explicit anti-thinness check

SELECTED 134/139 (57 PRIMARY / 77 SUPPORTING), HOLD 5, REJECT 0 — coverage
optimized for explanation, not minimum count. All 43 ledger transitions mapped
to packages; Model cards, benchmarks, runtime, provenance, and reception lanes
retained. Compression audit: SELECTED (134) >> 1 with non-DROP 139 — no audit
trigger; depth preserved by construction.

## 18. Expected bibliography / evidence density

139 Discovery authorities → 139 Evidence Cards (126 VERIFIED / 8 PARTIAL /
5 NEEDS_MORE) + 139 Views + 43 transition entries. Draft chapters inherit
condition-bound numbers, validity limits, and barriers without returning to
Discovery summaries.

## 19. Intentional omissions and reasons

- Phenaki masked-prior comparison: body blocked (OpenReview wall) — omitted from
  mechanism claims, retained as HOLD with barrier.
- SD repository version binding: repo 404 — mechanism weight carried by LDM paper.
- ITU MUSHRA protocol text: gated — listening claims cite study-level sources.
- Kling 3.0 mechanism: IR page blocked — capability role only, no press substitution.
- Wan hub corroboration: JS-gated — open-line claims rest on repo README.
- Music long-form structure metrics, duplex interruption metrics: no adequate
  authority found — stated as open, not filled by speculation.

## 20. Review mechanics

- Reviewed commit for this gate: the pushed work-branch HEAD recorded in the
  session report (exact SHA/tree), containing State + canonical gate inputs.
- This dossier requests a Human decision: `APPROVED` or `REQUEST_CHANGES`
  (with requested changes + regeneration boundary). Silence is not a decision.
- No drafting, validation, publication, freeze, or release work is included.
