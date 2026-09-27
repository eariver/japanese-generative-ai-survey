# TS-002 semantic delta audit (r1 → r2)

r1 result-set: `f01de6548929c74d9b9715e382027c89e5aa5c780f3865ebbf5e3e3b654985e7` (139 results, all PARTIAL, preserved untouched).
r2 result-set: `048cbd0942f073ed6ba134c97a5691e9ea4eb1eb0db6fa1ed842abe5faf2810e` (139 results: 125 VERIFIED / 9 PARTIAL / 5 NEEDS_MORE).
Method: Layer A rebuilt from consumed source bodies (125 FULL) instead of Discovery summaries + Raw notes.
`Historical role (BT-Oxx)` prose removed from all cards; cross-source synthesis moved to `transition-ledger.json` (43 entries, 41 multi-task).

## Representative deltas

### VAE (BT-D001)
- r1: summary restatement of amortized VI/reparameterization + generic representation thread; limitation `full-text body verification reserved`.
- r2: body-consumed SGVB estimators (L^A/L^B, analytic KL eq7/10), MLP encoder (mu/sigma, M=100, L=1, Adagrad + MAP), ancestral sampling without MCMC; scope bound to continuous latents on MNIST/Frey Face; limitation now states Gaussian-posterior example only with discrete latents excluded. VERIFIED.

### SoundStream (BT-D006)
- r1: RVQ-lineage restatement, body reserved.
- r2: body-consumed causal conv embeddings (320x, 75 frames/s @24 kHz, Nq layers e.g. 8 for 6 kbps), SEANet-like encoder/decoder, hinge-adversarial + feature-matching + mel losses, FiLM denoising, streamable smartphone-CPU inference with selectable layers; numbers now bound (MUSHRA 3 kbps beats Opus 12 kbps, ViSQOL >3.7). VERIFIED.

### AudioLM (BT-D009)
- r1: semantic-plus-acoustic restatement, body reserved.
- r2: body-consumed hybrid token hierarchy (semantic 25 Hz ~250 bps + acoustic 50 Hz 6000 bps with 4-coarse/8-fine split), three 0.3B staged Transformers, staged temperatures, 3 s continuation; numbers now bound (ABX, CER/WER, 92.6% speaker accuracy). VERIFIED.

### DDPM (BT-D019)
- r1: forward/reverse restatement + generic runtime language, body reserved.
- r2: body-consumed epsilon-parameterisation with score-matching equivalence (§3.2, Eq 12-14), simplified Lsimple down-weighting small-t, U-Net + sinusoidal time + 16x16 attention, T=1000 linear schedule; numbers now bound (CIFAR-10 IS 9.46/FID 3.17 vs VLB 7.67/13.51; rate 1.78 + distortion 1.97 bits/dim). VERIFIED.

### Latent diffusion (BT-D023)
- r1: latent-diffusion restatement, body reserved.
- r2: body-consumed KL/VQ-regularised autoencoder reused once, time-conditional UNet + tau_theta(y) cross-attention, joint LDM + conditional objectives, DDIM 10-200 steps with 200-250-step guidance; numbers now bound (CelebA-HQ 5.11, COCO 12.63/IS 30.29). VERIFIED.

### Conditioning/control anchor (BT-D032 classifier-free guidance)
- r1: joint-training/guidance-scale restatement, body reserved.
- r2: body-consumed dropout rates (p_uncond 0.1-0.2), guidance equation, swept scales; numbers now bound (64px FID 1.55 at w=0.1; 128px 2.43 beating ADM-Guided 2.97; 2x NFE cost). VERIFIED.

### Speech anchor (BT-D060 Voicebox)
- r1: flow-matching infilling restatement, body reserved.
- r2: body-consumed non-AR CNF with optimal-transport conditional flow matching on 80-dim log-mel + phones, duration model, infill conditioning, guidance, <10-NFE ODE solver; numbers now bound (WER 5.9→1.9%, sim 0.580→0.681, 20x faster). VERIFIED.

### Music anchor (BT-D065 MusicLM)
- r1: staged-generation restatement, body reserved.
- r2: body-consumed frozen SoundStream + w2v-BERT + MuLan staging with train/inference token swap, three 430M Transformers, story-mode continuation; numbers now bound (FAD-VGG 4.0, MCC 0.51, human wins 312 vs 158/97, memorisation <0.2%). VERIFIED.

### Video anchors (BT-D070 Video Diffusion Models; BT-D071 Imagen Video)
- r1: both summary restatements, bodies reserved.
- r2 D070: body-consumed factorized 3D U-Net + reconstruction guidance with weight, joint image-video training; numbers now bound (UCF-101 FID 295/IS 57; BAIR FVD 68.19; extension FVD 136 vs 451 replacement). VERIFIED.
- r2 D071: body-consumed 7-model 11.6B cascade with temporal attention/conv split, v-prediction, oscillating guidance, 8-step distillation; numbers now bound (distilled CLIP 25.03 vs 25.19 at ~18x faster). VERIFIED.

### Evaluation sources (BT-D083 FID; BT-D092 VBench)
- r1: both summary restatements with `full-text reserved`.
- r2 D083: PARTIAL — abstract consumed + FAD §2 cross-description only (full-text HTML 404, ar5iv fatal); metric mechanism recorded at abstract level with embedding/sample-size limits explicitly unverified.
- r2 D092: VERIFIED — body-consumed 16 disentangled dims + 8 content categories with named backbones (DINO/CLIP/flicker/interpolation-prior/RAFT/LAION/MUSIQ/GRiT/UMT/Tag2Text/CLIP/ViCLIP) and human win-ratio alignment; numbers now bound (subject 86-92% vs spatial 18-37%). Validity limits (backbone bias, static-video cheating) explicit.

### Closed-system case (BT-D100 FLUX.2 klein)
- r1: vendor speed-claim restatement with independent-measurement-absent limit.
- r2: announcement body consumed (family 9B/4B/Base, FP8/NVFP4 variants, 4-step distillation, Jan 15 2026 date, Apache-2.0 4B) with vendor charts quarantined (GB200 bf16) and tokenizer/training explicitly UNDISCLOSED. Stays CONTEXT; no architecture inferred. VERIFIED (quarantine target).

### BT-D139 X-bound evidence
- r1: Sol-audited ledger restatement as one reception record (already adequate; the defect was elsewhere).
- r2: unchanged substance, tightened to observation-only classes (SOCIAL_OBSERVATION) with raw-recount verification (27 sections/URLs) and rebinding requirement; stays CONTEXT. VERIFIED.

## Structural deltas (all 139)
- Removed `Historical role (BT-Oxx)` + selection-recommendation prose from every card (validator `no_lineage_prose_in_cards` PASS).
- Removed all `full-text reserved` + `VERIFIED` contradictions (validator PASS; PARTIAL/BLOCKED use UNRESOLVED with barriers).
- 21 recorded-locator transcription defects documented in limitations with verified-correct body IDs (future Discovery repair listed, no silent substitution).
- 5 BLOCKED (D024 repo 404/API 404; D072 OpenReview wall; D091 ITU gated; D120 IR timeout; D125 JS shell) → NEEDS_MORE/HOLD.
- 9 PARTIAL (abstract/homepage/snippet/v1-family/unevaluated-section cases) with exact barriers.
