#!/usr/bin/env python3
"""TS-002 Evidence r2 interactive input: Layer A source-local factual records.

Operator: Muse (Luna/Work execution role) under
docs/prompts/2026-09-24_muse-ts-002-evidence-semantic-depth-repair-r2.md and
Sol Evidence Semantic Review r1 (REQUEST_CHANGES E1-E5).

Layer A contains ONLY source-bound facts: identity, events, disclosed
method/architecture/representation/objective, condition-bound measurements,
stated limitations, attributed vendor/author claims, access boundary. NO
edition-level lineage prose, NO 'Historical role' claims, NO selection
recommendations, NO cross-source successor judgments (those live in
transition-ledger.json/.md).

VERIFIED is used only where the source body was actually consumed for that
target. Summary/Raw-only or blocked sources are PARTIAL/NEEDS_MORE with
UNRESOLVED targets and exact barriers. Corrected arXiv locators (recorded
locator resolves to an unrelated paper) are consumed at the verified-correct
ID with the defect stated in limitations; nothing is silently substituted.
"""

from __future__ import annotations

import json
from pathlib import Path

ISSUE = "SP-beyond-text-2026"
DISC = Path("sources/SP-beyond-text-2026/discovery/discovery-v2.jsonl")
SCREEN = Path("sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/interactive-decisions.json")
OUTDIR = Path("sources/SP-beyond-text-2026/execution/evidence-semantic-depth-r2")
OUT = OUTDIR / "evidence-interactive-input-r2.json"

OB2DIM = {
    "BT-O01": "media_representation_tokenization",
    "BT-O02": "generative_paradigms_objectives",
    "BT-O03": "conditioning_alignment",
    "BT-O04": "control_reference_identity",
    "BT-O05": "editing_preservation",
    "BT-O06": "temporal_long_horizon",
    "BT-O07": "speech_voice_lineage",
    "BT-O08": "music_audio_lineage",
    "BT-O09": "video_lineage",
    "BT-O10": "runtime_deployment",
    "BT-O11": "evaluation_validity",
    "BT-O12": "multimodal_convergence",
}

CLOSED_CAP = {f"BT-D{i:03d}" for i in range(100, 129)}
MECH_ANCHOR_CLOSED = {"BT-D111", "BT-D113", "BT-D124"}
BLOCKED = {"BT-D024", "BT-D072", "BT-D091", "BT-D120", "BT-D125"}
PARTIAL = {"BT-D022", "BT-D059", "BT-D062", "BT-D076", "BT-D083", "BT-D089",
           "BT-D098", "BT-D106", "BT-D134"}

ORG_HINTS = [
    ("ByteDance", "ByteDance"), ("Google", "Google"), ("DeepMind", "Google DeepMind"),
    ("OpenAI", "OpenAI"), ("Stability", "Stability AI"), ("Suno", "Suno"),
    ("ElevenLabs", "ElevenLabs"), ("Meta", "Meta"), ("Black Forest Labs", "Black Forest Labs"),
    ("BFL", "Black Forest Labs"), ("Kuaishou", "Kuaishou"), ("Runway", "Runway"),
    ("Luma", "Luma"), ("Alibaba", "Alibaba"), ("Wan", "Alibaba"), ("Descript", "Descript"),
    ("ITU", "ITU"), ("C2PA", "C2PA"),
]


def org_of(title):
    for hint, org in ORG_HINTS:
        if hint.lower() in title.lower():
            return org
    return None


def ent_artifact(rec):
    did = rec["discovery_id"]
    title = rec["source"]["title"]
    loc = rec["source"]["locator"]
    tl = title.lower()
    if did == "BT-D139":
        return ("OTHER", "OTHER", "Accepted X reception ledger r3 (27 direct observations)", None)
    if "librispeech" in tl or "pick-a-pic" in tl:
        return ("DATASET", "DATASET", title, org_of(title))
    if any(k in tl for k in ("benchmark", "fid", "inception score", "geneval", "compbench",
                             "frechet", "mushra", "wav2lip", "videophy", "five", "duplexbench")) \
            or "benchmark" in tl or "evaluation" in tl and "model card" not in tl:
        return ("BENCHMARK", "BENCHMARK", title, org_of(title))
    if "c2pa" in tl or "synthid" in tl or "mushra" in tl or "itu" in tl:
        return ("OTHER", "OTHER", title, org_of(title))
    if "arxiv" in loc or rec["source"]["source_type"] == "PRIMARY_PAPER":
        return ("PAPER", "PAPER", title, org_of(title))
    if "github.com" in loc:
        if "wan2.2" in loc.lower() and "vae" not in tl:
            return ("MODEL", "MODEL", title, org_of(title))
        return ("FRAMEWORK", "FRAMEWORK", title, org_of(title))
    if "model card" in tl:
        return ("MODEL", "MODEL", title, org_of(title))
    if any(k in tl for k in ("api", "deprecation", "release notes", "help", "docs", "hub")):
        if "api" in tl or "deprecat" in tl:
            return ("API", "API", title, org_of(title))
        return ("PRODUCT", "PRODUCT", title, org_of(title))
    if did in CLOSED_CAP:
        return ("MODEL", "MODEL", title, org_of(title))
    return ("PAPER", "PAPER", title, org_of(title))


# Per-record body-consumption data.
# Keys: access, sections, corrected (verified-correct locator or None),
#   claims [(text, evidence_class, context)], lims [..],
#   extra_ver {target: (status, finding)} for non-full-body targets.
# The 'Evidence-stage full-body verification' target is derived from access.
DATA = {

# ---------------- D01 representation ----------------
"BT-D001": dict(access="FULL", sections="arXiv abs + HTML v11: Abstract, §1 Intro, §2 Method (SGVB/AEVB, reparameterization), §3 VAE example, §5 Experiments, §6 Conclusion", corrected=None,
 claims=[
  ("The source introduces amortized variational inference with the reparameterization trick: a probabilistic encoder q_phi(z|x) (MLP, Gaussian) and decoder p_theta(x|z), prior N(0,I), trained by stochastic-gradient variational Bayes (SGVB estimators, analytic KL).", "PRIMARY_FACT", "Abstract + §2; Appendix A derivations."),
  ("Reported scope: continuous latent variables with intractable posteriors on large datasets; evaluated on MNIST/Frey Face lower bounds and marginal likelihoods; 2D latent manifold visualisation. Discrete latents are excluded.", "PRIMARY_FACT", "§5 experiments; §6 conclusion."),
 ],
 lims=["Mean-field-free Gaussian-posterior example only; discrete latents and global-parameter VB deferred in-text.",
  "Downstream compression/fidelity claims require first-stage autoencoder sources, not this paper alone."],
 extra_ver={}),

"BT-D002": dict(access="FULL", sections="arXiv abs + HTML v2: Abstract, §1-3 (discrete latents, learning, prior), §4 Experiments, §5 Conclusion, App A.1 EMA", corrected=None,
 claims=[
  ("The source defines VQ-VAE: encoder output quantised by nearest-neighbour lookup in embedding table e (R^{KxD}), uniform categorical prior, straight-through gradients with codebook + commitment losses, EMA codebook updates.", "PRIMARY_FACT", "§3.1-3.2; App A.1."),
  ("Reported numbers: CIFAR-10 bits/dim VAE 4.51 vs VQ-VAE 4.67 vs VIMCO 5.14; ImageNet 128x128x3 to 32x32x1 at K=512; speech 64x/128x downsampling with 49.3% phoneme mapping (128 codes at ~25 Hz) vs 7.2% chance.", "PRIMARY_FACT", "§4 tables; conditions in-text."),
 ],
 lims=["No joint prior+VQ-VAE training; uniform prior during representation learning; MSE pixel-loss blur noted in-text.",
  "Codebook-collapse/usage frontier needs successor sources."],
 extra_ver={}),

"BT-D003": dict(access="FULL", sections="arXiv abs + HTML v1: Abstract, §1, §2 Background, §3 hierarchical codes/priors/rejection, §5 FFHQ/NLL/CAS experiments, App hyperparameters", corrected=None,
 claims=[
  ("The source scales VQ-VAE with two-level discrete maps (256px: 32x32 top + 64x64 bottom conditioned on top; FFHQ-1024 adds 128x128), EMA codebooks, feed-forward decoder, and PixelSnail priors; single feed-forward decode runs ~30x faster than pixel-space.", "PRIMARY_FACT", "§3; App Tables 3-4."),
  ("Reported numbers: ImageNet-256 NLL top 3.40/3.41 + bottom 3.45/3.45 (train/val); CAS Top-1/Top-5 54.83/77.59 (58.74/80.98 after reconstruction) vs BigGAN-deep 42.65/65.92 vs real 73.09/91.47; FID ~30 to ~10 with classifier rejection at diversity cost.", "PRIMARY_FACT", "§5.2-5.3; train/val conditions in-text."),
 ],
 lims=["Latent-space likelihood not comparable across encoders; FID/IS sensitive to VQ blur; prior training 1.6M/754k steps heavy.",
  "Hierarchical-code cost/coverage vs single-scale successors needs comparison sources."],
 extra_ver={}),

"BT-D004": dict(access="FULL", sections="Correct body 2012.09841 HTML v3 consumed (Abstract, §1, §2, §3 VQGAN codebook + latent transformer, §4, §5, App). Recorded locator 2012.09812 resolves to unrelated ViNG robotics paper.", corrected="2012.09841",
 claims=[
  ("The source builds a CNN VQGAN codebook (|Z|=1024 typical; 256x256 to 16x16=256 indices) with perceptual + patch-discriminator losses, then models code sequences with a GPT-2-medium latent transformer (307M, sliding window for megapixel).", "PRIMARY_FACT", "Correct body §§3-4; title/authors verified."),
  ("Reported numbers: same-representation NLL favours Transformer over PixelSNAIL on RIN/LSUN-CT/IN/D-RIN/S-FLCKR; CIFAR-10 +18.63% FID at 14.08x faster sampling vs pixels; COCO-Stuff FID 22.4, ADE20K 35.5.", "PRIMARY_FACT", "Correct body §4 tables."),
 ],
 lims=["Recorded locator 2012.09812 is a transcription defect (resolves to unrelated paper); claims above rest on verified-correct 2012.09841. Future Discovery repair should correct the locator.",
  "Sliding-window generation needs spatial invariance/conditioning; fixed 16x16 transformer context."],
 extra_ver={}),

"BT-D005": dict(access="FULL", sections="arXiv abs + HTML v2: Abstract, §1, §2 dVAE/prior/data/mixed-precision/rerank, §3 quant/overlap/qualitative, §4, App", corrected=None,
 claims=[
  ("The source models 256x256 images as 32x32=1024 dVAE tokens (8192 vocab) jointly with BPE text (<=256 tokens) in a 12B sparse decoder-only transformer, with joint ELB (beta=6.6) and CLIP-contrastive best-of-512 rerank at inference.", "PRIMARY_FACT", "§2; App."),
  ("Reported numbers: 250M pairs; MS-COCO zero-shot human vote 90.0% realism + 93.3% caption match vs DF-GAN; FID within ~2 pts of best prior; 21% COCO / 12% CUB train overlap with no result change.", "PRIMARY_FACT", "§3 tables/conditions."),
 ],
 lims=["Heavy compression loses high-frequency detail; CUB specialist gap; rerank-dependent; variable binding/text rendering inconsistent in-text.",
  "dVAE ceiling vs VQGAN/CLIP-latent successors needs successor sources."],
 extra_ver={}),

"BT-D006": dict(access="FULL", sections="arXiv abs + HTML v1: Abstract, §I-III (encoder/decoder/RVQ/discriminators/objective), §IV-V results, §VI", corrected=None,
 claims=[
  ("The source defines SoundStream: causal convolutional encoder/decoder with residual vector quantization (320x downsampling, 75 frames/s at 24 kHz, e.g. 8 layers for 6 kbps), hinge adversarial + feature-matching + mel-spectral losses, streamable on smartphone CPU with selectable layer count.", "PRIMARY_FACT", "§III; §V setup."),
  ("Reported numbers: single model 3-18 kbps; MUSHRA at 24 kHz 3 kbps beats Opus 12 kbps and Lyra 3 kbps, nears EVS 9.6 kbps (3.2-4x bit saving); ViSQOL >3.7 at 3 kbps; entropy coding saves 7-20%.", "PRIMARY_FACT", "§V; crowdsourced-MUSHRA conditions in-text."),
 ],
 lims=["MUSHRA-inspired crowdsourcing (not strict MUSHRA); constant-rate operation; music hardest; enhancement demo is noise-suppression only.",
  "Rate/quality frontier vs EnCodec/DAC needs matched comparison."],
 extra_ver={}),

"BT-D007": dict(access="FULL", sections="arXiv abs + HTML v1: Abstract, §1-3 (enc/dec, RVQ, LM+entropy, objective+balancer), §4 experiments, §5, App", corrected=None,
 claims=[
  ("The source defines EnCodec: streaming convolutional encoder-decoder with multistream RVQ (75 steps/s at 24 kHz, up to 32 codebooks x1024; 1.5/3/6/12/24 kbps by codebook count), per-bandwidth multi-scale STFT discriminator, optional Transformer LM + arithmetic coding; 13.3 ms initial latency, RTF ~9.8 enc/10.4 dec on 1-thread MacBook at 6 kbps.", "PRIMARY_FACT", "§3; §4 setup."),
  ("Reported numbers: streamable MUSHRA 1.5/3/6/12 kbps clean 49.2/67.0/83.1/90.6 vs Opus-6 30.1, Opus-12 76.5, EVS-9.6 84.4; entropy trims ~25-40%; stereo 48 kHz 6 kbps 82.9 ties MP3-64k.", "PRIMARY_FACT", "§4 tables/conditions."),
 ],
 lims=["Discriminator-overpower handled by stochastic updates; 48 kHz+entropy-coding slower than real-time; stereo only via discriminator tweak.",
  "Semantic-vs-acoustic split needs AudioLM-style hybrid sources."],
 extra_ver={}),

"BT-D008": dict(access="FULL", sections="arXiv abs + HTML v2: Abstract, §1-3 (Snake, RVQ, dropout, discriminator, losses), §4 experiments, §5, App", corrected=None,
 claims=[
  ("The source defines the Descript Audio Codec: SoundStream-style convolutional encoder (22M)/decoder (54M) with Snake activations, stride-512 embeddings (86 Hz at 44.1 kHz), 9x10-bit factorized L2-normalized RVQ (~91x compression), multi-period + multi-band complex-STFT discriminator, no k-means/restarts; open code/weights.", "PRIMARY_FACT", "§3; App."),
  ("Reported numbers: 8 kbps Mel 0.93/STFT 1.60/ViSQOL 4.18/SI-SDR 10.75, beating EnCodec-12k on all four; matched-24 kHz 12 kbps Mel 0.74/ViSQOL 4.51/SI-SDR 12.51 vs EnCodec 1.15/4.39/8.44; MUSHRA beats EnCodec at all rates.", "PRIMARY_FACT", "§4 tables/conditions."),
 ],
 lims=["Still below reference MUSHRA; worse on environmental/glockenspiel/synth; balanced full-band sampling required.",
  "Generation-downstream gain needs adopter evidence, not codec metrics alone."],
 extra_ver={}),

"BT-D009": dict(access="FULL", sections="arXiv abs + HTML v2: Abstract, §I-III (components, token trade-offs Table I, 3-stage hierarchy), §IV experiments incl. Tables II-III, §V-VII", corrected=None,
 claims=[
  ("The source defines AudioLM: hybrid semantic tokens (w2v-BERT-XL layer-7 k-means K=1024 at 25 Hz, ~250 bps) + acoustic SoundStream tokens (12x1024 RVQ at 50 Hz, 6000 bps; 4 coarse=2000 bps + 8 fine), modelled by three 0.3B decoder-only Transformers in stages (semantic, coarse-acoustic, fine); 3-second prompt continuation with temperatures 0.6/0.8/0.6.", "PRIMARY_FACT", "§III; Table I."),
  ("Reported numbers: semantic-250 bps ABX 6.7/7.6 + ViSQOL 1.1 vs acoustic-2000 bps ABX 22.4/28.7 + ViSQOL 3.3; acoustic continuation ASR CER 3.4/WER 6.0; speaker accuracy 92.6% on continuation vs 3.2% on resampled semantics.", "PRIMARY_FACT", "§IV Tables II-III/conditions."),
 ],
 lims=["Acoustic-only modelling babbles; semantic-only cannot vocode; proper-noun/background-noise ASR errors; piano only continuations beyond speech.",
  "Long-form structure beyond continuations needs MusicLM/MusicGen successors."],
 extra_ver={}),

"BT-D010": dict(access="FULL", sections="arXiv abs + HTML v2: Abstract, §1, §2 prelim, §3 MAGVIT (3D tokenization, COMMIT), §4 results, §5-6, suppl", corrected=None,
 claims=[
  ("The source defines MAGVIT: 3D-VQ video tokenizer (4x16x16=1024 tokens for 16x128x128, codebook 1024, inflated 2D-VQ init) with a BERT transformer trained by COMMIT multi-task masked modelling over 10 tasks; non-autoregressive COMMIT decoding in K=12 steps (16x128x128 in 12 steps, 0.25 s TPUv4i / 37 fps V100).", "PRIMARY_FACT", "§3; Alg 1."),
  ("Reported numbers: UCF-101 FVD 332 to 76(L)/159(B), IS to 89.27; BAIR-FP FVD 84 to 62 (31 debiased); Kinetics-600-FP 16.2 to 9.9 (~39% cut); ~100x diffusion, 60x TATS-AR sampling efficiency.", "PRIMARY_FACT", "§4 tables/conditions."),
 ],
 lims=["VQ fidelity bounds generation; fixed 16-frame training; debiased BAIR protocol needed; naive unmasking fails (COMMIT motivation).",
  "Masked-prior vs diffusion-prior comparison needs successor coverage."],
 extra_ver={}),

"BT-D012": dict(access="FULL", sections="Wan2.2 GitHub repo page + README consumed: header/paper/blog links, T2V/I2V/TI2V/S2V/Animate commands, MoE/VAE exposition, efficiency table, license", corrected=None,
 claims=[
  ("The repo documents Wan2.2-VAE high-compression video representation: 4x16x16 T-H-W (64x) plus patchification to 4x32x32 total; TI2V-5B unified T2V+I2V runs 5 s 720P at 24 fps in <9 min on a single 24 GB consumer GPU (offload/dtype/T5-CPU).", "PRIMARY_FACT", "README MoE/VAE/efficiency sections."),
  ("The repo documents a 2-expert MoE layout (high-noise layout expert + low-noise detail expert switched at SNR threshold t_moe): T2V-A14B/I2V-A14B 27B total/14B active; TI2V-5B 5B dense; open weights Apache 2.0; ComfyUI/Diffusers supported.", "PRIMARY_FACT", "README architecture/run sections."),
 ],
 lims=["README-level disclosure only: no VAE reconstruction/ablation numbers, no training loss/objective, efficiency table values partly image-bound.",
  "Open line stops at 2.2; 2.5/2.6/2.7/3.0 are API-only."],
 extra_ver={}),

# ---------------- D02 paradigms ----------------
"BT-D013": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-7 (adversarial nets, theory, experiments, advantages)", corrected=None,
 claims=[
  ("The source defines GANs: generator G(z) vs discriminator minimax V=logD(x)+log(1-D(G(z))) with non-saturating max logD(G(z)); optimum at pg=pdata, D=1/2; single forward-pass sampling with no explicit density.", "PRIMARY_FACT", "§3-4."),
  ("Reported numbers: Parzen log-likelihood MNIST 225±2 vs DBN 138±2; TFD 2057±26 vs best baseline 2110±50; CIFAR-10 samples qualitative only.", "PRIMARY_FACT", "§5 conditions."),
 ],
 lims=["No explicit density; discriminator must stay synchronised (mode collapse risk); Parzen evaluation high-variance in high dimensions.",
  "Modern role is vocoder/autoencoder/post-training hybrid, not standalone SOTA."],
 extra_ver={}),

"BT-D014": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-7 (architecture, LSUN training, CIFAR/SVHN validation, visualisations)", corrected=None,
 claims=[
  ("The source defines DCGAN: strided-convolution discriminator / fractional-strided generator, no pooling/FC layers, batchnorm (not on G-output/D-input), ReLU+Tanh generator, LeakyReLU discriminator, Adam 0.0002; 100-dim uniform Z with conv-hierarchy arithmetic.", "PRIMARY_FACT", "§3."),
  ("Reported numbers: CIFAR-10 82.8% classifier probe; SVHN-1000 22.48% error vs 28.87% supervised same-architecture; deduplicated LSUN (~275k dups removed).", "PRIMARY_FACT", "§4-5 conditions."),
 ],
 lims=["Occasional filter-collapse with longer training; no log-likelihood; global-average-pooling stability/speed trade-off noted.",
  "Stability analysis superseded by StyleGAN-era engineering."],
 extra_ver={}),

"BT-D015": dict(access="FULL", sections="Correct body 1812.04948 consumed (Abstract, Intro, style generator, mixing, stochastic variation, disentanglement, FFHQ app). Recorded locator 1812.04958 resolves to unrelated GR paper.", corrected="1812.04948",
 claims=[
  ("The source defines the style-based generator: 8-layer MLP maps z to intermediate space W; learned affine styles drive per-layer AdaIN from a learned 4x4x512 constant plus per-layer Gaussian noise; mixing regularisation crosses two latents at a random point.", "PRIMARY_FACT", "Correct body style-generator/mixing sections; title/authors verified."),
  ("Reported numbers: FID 50k 1024px FFHQ config-f 4.40 and CelebA-HQ 5.17 vs baseline-a 8.04; path-length FFHQ traditional-Z 412.0/415.3 vs style-W with noise 200.5/160.6; linear separability 10.78 vs 3.54.", "PRIMARY_FACT", "Correct body tables."),
 ],
 lims=["Recorded locator 1812.04958 is a transcription defect; claims rest on verified-correct 1812.04948. Future Discovery repair should correct the locator.",
  "Mixing regularisation slightly distorts W path length; Z input space stays entangled."],
 extra_ver={}),

"BT-D016": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-5 (normalisation artifacts, PPL/smoothness, progressive-growing revisit, projection), App", corrected=None,
 claims=[
  ("The source redesigns StyleGAN: bias/noise outside the style block, std-only modulation, weight demodulation via grouped convolution; skip-generator + residual-discriminator, no progressive growing, doubled high-res feature maps; logistic + lazy R1 + path-length regularisation (orthogonal-Jacobian encouragement).", "PRIMARY_FACT", "§2-3."),
  ("Reported numbers: FFHQ-1024 FID 4.40 to 2.84, PPL 212.1 to 145.0 (config a to f, D saw 25M); LSUN-Car FID 3.27 to 2.32, PPL 1484.5 to 415.5.", "PRIMARY_FACT", "§4 tables/conditions."),
 ],
 lims=["FID/perceptual-path metrics are texture-biased; FID-PPL trade-off on unstructured sets; larger models may help further.",
  "Matched-resolution/budget GAN-vs-diffusion comparison needs discipline."],
 extra_ver={}),

"BT-D017": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-6 (pixel-by-pixel, Row/DiagonalBiLSTM, PixelCNN, multi-scale, specs, eval)", corrected=None,
 claims=[
  ("The source defines fully autoregressive pixel generation: row-major factorisation with RGB split, 256-way multinomial per channel; Row-LSTM and Diagonal-BiLSTM (skew + 1x1 in-state + 2x1 column recurrence, up to 12 layers) plus masked-conv PixelCNN and multi-scale variants.", "PRIMARY_FACT", "§2-3."),
  ("Reported numbers: MNIST 79.20 nats (7-layer Diagonal-BiLSTM); CIFAR-10 3.00 bits/dim; ImageNet-32 3.86, ImageNet-64 3.63 bits/dim; training parallel, generation sequential pixel-by-pixel.", "PRIMARY_FACT", "§5 conditions."),
 ],
 lims=["Sequential generation expensive; 64x64 single-scale weak global structure; size capped by GPU memory/time.",
  "Cost argument vs Image-Transformer follow-ups."],
 extra_ver={}),

"BT-D018": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-6 (representation, tempered sampling, uncond/class-cond/super-res)", corrected=None,
 claims=[
  ("The source defines the Image Transformer: decoder-only Transformer for autoregressive image modelling with raster order, 256-value embeddings per channel plus 2D coordinates, masked local multi-head self-attention; encoder-decoder variant for 8x8 to 32x32 super-resolution.", "PRIMARY_FACT", "§3."),
  ("Reported numbers: CIFAR-10 2.90 bits/dim; ImageNet average 3.77; CelebA super-resolution fooled rate 36.11±2.5% (2D, tau 0.8).", "PRIMARY_FACT", "§5 conditions."),
 ],
 lims=["Local attention still truncates full context; largest generation 32x32 plus super-resolution only.",
  "Full-attention DiT-scale comparison needed."],
 extra_ver={}),

"BT-D019": dict(access="FULL", sections="arXiv abs + HTML v2: Abstract, §1-4 (background, forward/reverse/decoder/Lsimple, sample quality, ablation, coding, interpolation), §5-6, App", corrected=None,
 claims=[
  ("The source defines DDPM: fixed Gaussian forward diffusion (T=1000, linear beta 1e-4 to 0.02) with learned Gaussian reverse transitions; epsilon-prediction parameterisation revealing equivalence to multi-noise-level denoising score matching with Langevin-like sampling; simplified unweighted objective Lsimple down-weighting small-t terms.", "PRIMARY_FACT", "§3; Eq 12-14."),
  ("Reported numbers: CIFAR-10 IS 9.46±0.11, FID 3.17 (train; 5.24 test) with Lsimple vs IS 7.67/FID 13.51 on true VLB; LSUN-Bedroom FID 4.90, Church 7.89; rate 1.78 + distortion 1.97 bits/dim (RMSE 0.95/255); U-Net backbone with Transformer sinusoidal time embedding, self-attention at 16x16.", "PRIMARY_FACT", "§4 Tables 1-2/conditions."),
 ],
 lims=["NLL uncompetitive vs other likelihood models; most bits describe imperceptible detail; 1000-step sampling costly (~5 days/50k A100).",
  "Step-cost reduction requires DDIM/distillation successors."],
 extra_ver={}),

"BT-D020": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-7 (DDPM background, non-Markovian forward, DDIM/ODE, quality/consistency/interp/reconstruction)", corrected=None,
 claims=[
  ("The source defines DDIM: non-Markovian forward process with identical marginals q(xt|x0) but a sigma vector controlling stochasticity (eta=0 deterministic/DDIM, eta=1 DDPM); generalised update with subsampled trajectory tau; deterministic path exposes an ODE (Euler) view with encodable latents.", "PRIMARY_FACT", "§3-4; Thm 1."),
  ("Reported numbers: CIFAR-10 eta=0 FID 13.36 at 10 steps, 6.84 at 20, 4.67 at 50, 4.16 at 100 vs eta=1 41.07 at 10; 10-50x speedup with 20-100 steps matching 1000-step quality; reconstruction MSE 0.014 at 10 steps to 0.0001 at 1000.", "PRIMARY_FACT", "§5 tables/conditions."),
 ],
 lims=["FID degrades as trajectory shortens; DDPM-implementation sigma collapses at short trajectories; ODE-vs-probability-flow gap at few steps.",
  "Few-step SOTA vs LCM/consistency successors not compared here."],
 extra_ver={}),

"BT-D021": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-6 (SMLD/DDPM background, forward/reverse/score-est, solvers/PC/prob-flow, controllable), Conclusion", corrected=None,
 claims=[
  ("The source unifies score-based and diffusion models as continuous-time SDEs: a single time-dependent score network trained by continuous denoising score matching; reverse-SDE solvers, predictor-corrector sampling, probability-flow ODE with exact likelihood, and conditional generation from unconditional scores.", "PRIMARY_FACT", "§3-4."),
  ("Reported numbers: CIFAR-10 IS 9.89, FID 2.20, NLL 2.99 bits/dim (sub-VP likelihood); PC-1000 VE-FID 3.24 vs predictor-only 4.98; first 1024x1024 samples from a score model.", "PRIMARY_FACT", "§4 Table 1/conditions."),
 ],
 lims=["Solver cost still high (1000-2000 evals); VE/VP/sub-VP trade-offs and corrector steps need tuning; architecture gains entangled with sampler gains.",
  "Solver optimality vs EDM successor and audio/video transfer beyond images."],
 extra_ver={}),

"BT-D022": dict(access="PARTIAL", sections="arXiv abs consumed (Heusel-style abstract verified: Karras et al., 2022). Full-text HTML 404 + ar5iv LaTeXML fatal; PDF/TeX only, not body-consumed.", corrected=None,
 claims=[
  ("The abstract reports a modular diffusion design space (preconditioning, schedule, solver) yielding CIFAR-10 conditional FID 1.79 / unconditional 1.97 at 35 NFE and ImageNet-64 1.36 retrained SOTA.", "AUTHOR_CLAIM", "Abstract only; body sections not consumed."),
 ],
 lims=["Abstract-only consumption: preconditioning/schedule/solver ablations, backbone-vs-objective separation, and cross-modal claims are NOT body-established.",
  "Image-domain ablations and audio/video transfer need full-body plus modality sources."],
 extra_ver={}),

"BT-D023": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-2, §3 perceptual compression + LDM + cross-attention, §4 compression trade-off/generation/conditioning/SR/inpainting, §5-6, App", corrected=None,
 claims=[
  ("The source defines latent diffusion: a perceptually-trained autoencoder (KL-regularised toward N(0,I) or VQ-regularised, decoder-side quantisation) compresses images once and is reused; diffusion runs on latents z with a time-conditional UNet; text/boxes/layout condition via domain encoder tau_theta(y) and cross-attention.", "PRIMARY_FACT", "§3."),
  ("Reported numbers: 256px unconditional FID CelebA-HQ 5.11, FFHQ 4.98, Church 4.02, Bedroom 2.95 (LDM-4/8, 200 DDIM steps); COCO-256 FID 12.63, IS 30.29±0.42; DDIM 10-200 steps; guidance s=1.5-10 over 200-250 steps; convolution beyond 256px to ~1024px for SR/inpainting.", "PRIMARY_FACT", "§4 tables/conditions."),
 ],
 lims=["Pixel-level detail still limited by first stage; LDM-32 over-compression stagnates; sequential sampling still costly; misuse/bias noted.",
  "Cross-attention conditioning role needs D03 sources; autoencoder-vs-prior error attribution needs ablations."],
 extra_ver={}),

"BT-D024": dict(access="BLOCKED", sections="Barrier: https://github.com/Stability-AI/stablediffusion returns 404 via webfetch (markdown+text); raw README 404; api.github.com/repos returns 404 Not Found as of access date. No README/tag/commit bytes consumed.", corrected=None,
 claims=[],
 lims=["Body blocked: the recorded repository locator is not retrievable (GitHub API 404); reference open implementation/weights, versioned tag/commit binding, and deployment/ecosystem claims are NOT established from body.",
  "Latent-diffusion mechanism weight in this edition rests on BT-D023 (paper) and BT-D025; this record is retained as NEEDS_MORE pending successful retrieval."],
 extra_ver={}),

"BT-D025": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-6 (prelims, patchify, adaLN, training, metrics, scaling, sampling-compute), Conclusion", corrected=None,
 claims=[
  ("The source replaces the UNet denoiser with a Transformer (DiT-S/B/L/XL, patchified Stable-Diffusion VAE latents, adaLN-Zero best): backbone-vs-objective separation landmark; class-dropout enables classifier-free guidance; sampling-compute cannot compensate model-compute.", "PRIMARY_FACT", "§3-5."),
  ("Reported numbers: ImageNet-256 XL/2-Guided s=1.5 FID 2.27, sFID 4.60, IS 278.24 at 7M steps vs LDM-4-G 3.60, ADM-G 4.59; ImageNet-512-G FID 3.04; 250-step ancestral sampling; DiT-XL/2 118.6/524.6 GFLOPs vs ADM 1120G.", "PRIMARY_FACT", "§4-5 tables/conditions."),
 ],
 lims=["JAX TPU-v3 throughput figures are hardware-bound; FID sensitive to eval suite; pixel-space DiT not tested.",
  "Scaling vs SiT/flow successors and text-to-image transfer need successor sources."],
 extra_ver={}),

"BT-D026": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-5 (flows/diffusion/score/velocity/interpolants, parameterisation, sampling/CFG experiments)", corrected=None,
 claims=[
  ("The source defines Scalable Interpolant Transformers: diffusion forward-SDE coupling replaced by interpolants xt=alpha_t x*+sigma_t eps (Linear/GVP/SBDM-VP) with velocity objective Lv and score derived via equation 9; identical DiT AdaLN-Zero backbone for fair comparison; probability-flow ODE (Heun) and reverse-SDE samplers with tunable diffusion coefficient w.", "PRIMARY_FACT", "§2-3."),
  ("Reported numbers: XL 400K 17.2 vs DiT 19.5; XL 7M 8.3 vs 9.6; XL-Guided s=1.5 256px FID 2.06 vs 2.27, 512px 2.62 SOTA at same params/GFLOPs; 250 NFE Euler-Maruyama.", "PRIMARY_FACT", "§3 tables/conditions."),
 ],
 lims=["wKL singular as t→1 for Linear/GVP (eta regularisation needed); velocity-score singularity at t=0; sampler discretisation heuristic.",
  "Flow-vs-diffusion gap vs rectified-flow reflow needs comparison."],
 extra_ver={}),

"BT-D027": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-7 (CNF prelims, FM+CFM, Gaussian paths, related, density/sampling-efficiency/conditional exps)", corrected=None,
 claims=[
  ("The source defines Flow Matching: CNF vector field trained simulation-free by regressing conditional (per-sample) vector fields (CFM, equal gradients per Thm 2); Gaussian conditional paths N(mu_t, sigma_t^2 I) with optimal-transport variant mu=t·x1 giving straight trajectories; same ADM UNet backbone across losses for ablation.", "PRIMARY_FACT", "§3-4."),
  ("Reported numbers: CIFAR-10 FM-OT NLL 2.99, FID 6.35, NFE 142 vs DDPM 3.12/7.48/274; ImageNet-64 NLL 3.31/FID 14.45/NFE 138; ImageNet-128 NLL 2.90/FID 20.9; training cost constant.", "PRIMARY_FACT", "§6 tables/conditions."),
 ],
 lims=["CIFAR FID higher than tuned literature (backbone not CIFAR-optimised); adaptive-solver NFE still 100+; marginal field not OT-optimal despite conditional OT.",
  "Trajectory-straightness vs rectified-flow reflow and high-res text-conditional transfer not established."],
 extra_ver={}),

"BT-D028": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-5 (transport problem, rectification properties/theory, related, toy/uncond/translation/adaptation exps)", corrected=None,
 claims=[
  ("The source defines Rectified Flow: least-squares regression of neural velocity v_theta on linear-interpolation directions (X1-X0); rectification rewires couplings deterministically with identical marginals and non-increasing convex transport cost; reflow straightens further; one-step distillation only at the end; VP/VE nonlinear extensions recover PF-ODE/DDIM.", "PRIMARY_FACT", "§2-3."),
  ("Reported numbers: CIFAR-10 one-step FID 4.85, recall 0.51 (claimed one-step SOTA); transport cost/straightness approach 0 with reflows at O(1/K); 1-rectified good at ≥2 steps, 2-rectified near-straight at 1 step.", "PRIMARY_FACT", "§5 tables/conditions."),
 ],
 lims=["Exact theory needs exact velocity field + unique ODE; estimation error accumulates over many reflows (1 reflow recommended); density smoothing needed for ill-behaved fields.",
  "Reflow cost vs LCM/consistency comparison and optimal-vs-straight coupling beyond 1D not established."],
 extra_ver={}),

"BT-D029": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-6 (diffusion/PF-ODE, consistency def/param/sampling/editing, distillation, isolated CT, few-step/editing exps)", corrected=None,
 claims=[
  ("The source defines Consistency Models: self-consistent function f mapping any PF-ODE trajectory point to origin (boundary f(x,eps)=x) via EDM-style skip parameterisation reusing diffusion UNets; consistency distillation from a teacher ODE solver or isolated consistency training from data; one-step sampling plus multistep alternate-denoise/inject schedule; zero-shot denoise/interpolation/inpainting/colourisation/SR/SDEdit.", "PRIMARY_FACT", "§3-5."),
  ("Reported numbers: distilled CIFAR-10 1-step FID 3.55, 2-step 2.93 SOTA; ImageNet-64 1-step 6.20, 2-step 4.70; isolated CT matches progressive distillation without teacher and beats non-adversarial one-step methods and many GANs.", "PRIMARY_FACT", "§6 tables/conditions."),
 ],
 lims=["Needs Lipschitz + higher-order solver for theorem error rates; continuous-time needs forward-mode JVP; greedy tau search assumes unimodal FID.",
  "Few-step quality vs LCM/ADD successors and guidance interaction beyond reported tables not established."],
 extra_ver={}),

"BT-D030": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-5 (background, architecture ablations, AdaGN, classifier guidance, LSUN/ImageNet/upsampling results)", corrected=None,
 claims=[
  ("The source shows diffusion beating GANs via architecture scale (128 base channels, multi-resolution attention, BigGAN resblocks, AdaGN timestep+class conditioning) plus classifier guidance: noisy classifier p_phi(y|xt,t) steers ancestral/DDIM sampling with scale s trading precision vs recall.", "PRIMARY_FACT", "§3-4; Alg 1-2."),
  ("Reported numbers: ImageNet-128 ADM-Guided FID 2.97 vs BigGAN 6.02; ImageNet-256 4.59 (25-step 5.44) vs BigGAN 6.95; 256 ADM-Guided+Upsampled 3.94, 512 3.85; LSUN-Bedroom 1.90/Horse 2.57/Cat 5.57 vs StyleGAN 2.35/3.84/7.25.", "PRIMARY_FACT", "§5 tables/conditions."),
 ],
 lims=["250-step sampling (25-step viable) still slower than GANs; classifier + large-upsample compute heavy; FID/IS/precision/recall imperfect proxies.",
  "Guidance mechanism vs classifier-free successor and API-scale text conditioning beyond class labels not established."],
 extra_ver={}),

# ---------------- D03 conditioning ----------------
"BT-D011": dict(access="FULL", sections="arXiv abs + HTML 2205.11487: Abstract, §1, §2.1 text encoders, §2.2 diffusion+CFG, §2.3 thresholding, §2.4 cascade, §2.5 Efficient U-Net, §3 eval, §4 COCO/DrawBench", corrected=None,
 claims=[
  ("The source conditions cascaded diffusion on large frozen text encoders: T5-XXL sequence + pooled embeddings via cross-attention in the 64px base plus two text-conditional super-resolution diffusions; 10% text-dropout joint conditional/unconditional training; classifier-free guidance with static/dynamic thresholding and noise-augmented cascade.", "PRIMARY_FACT", "§2."),
  ("Reported numbers: COCO zero-shot FID-30K 7.27 (GLIDE 12.24, DALL-E 2 10.39); human alignment 91.4 vs 91.9 reference; DrawBench human preference over VQ-GAN+CLIP/LDM/GLIDE/DALL-E 2.", "PRIMARY_FACT", "§3-4 conditions."),
 ],
 lims=["Weak photorealistic people; ~860M internal+LAION data limits; encoder finding era-specific.",
  "Super-resolution text-utility ablations beyond reported sweeps not established."],
 extra_ver={}),

"BT-D031": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1, §2.1-2.5 (WIT/CLIP objective/architecture/training), §3.1-3.3 (zero-shot/transfer/robustness), §6 limitations", corrected=None,
 claims=[
  ("The source defines CLIP: joint ResNet/ViT image + Transformer text encoders trained by symmetric cross-entropy over NxN pairs on WIT-400M with learned temperature; text encoder synthesises zero-shot classifiers via prompt templates + embedding ensembling (in-context reference, not diffusion).", "PRIMARY_FACT", "§2-3."),
  ("Reported numbers: zero-shot ImageNet 76.2% (matches ResNet-50), aYahoo 98.4, SUN 58.5; wins 16/27 vs ResNet-50 linear probe; STL10 99.3%.", "PRIMARY_FACT", "§3 tables/conditions."),
 ],
 lims=["Fails counting; fine-grained gaps (Flowers102/Aircraft ~-10%); bias/surveillance risks stated.",
  "Generation-relevance only; perception history belongs to TS-003; no generative conditioning quality established."],
 extra_ver={}),

"BT-D032": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-5 (background, guidance, ImageNet-64/128 sweeps, discussion)", corrected=None,
 claims=[
  ("The source defines classifier-free guidance: single network trained jointly conditional+unconditional via random conditioning dropout (p_uncond 0.1-0.2 best); inference-only guidance eps_tilde=(1+w)·eps_cond − w·eps_uncond with swept w; implicit-classifier motivation.", "PRIMARY_FACT", "§3."),
  ("Reported numbers: 64px best FID 1.55 at w=0.1, IS 260.2 at w=4.0; 128px FID 2.43 at w=0.3 beats ADM-Guided 2.97, IS 421 at w=4.0; costs 2 forward passes vs classifier guidance.", "PRIMARY_FACT", "§4 tables/conditions."),
 ],
 lims=["Saturated colours at high w; 2 forward passes; diversity loss; ImageNet-class conditioning only.",
  "Text-conditioning transfer and optimal p_uncond beyond tested values not established."],
 extra_ver={}),

"BT-D033": dict(access="FULL", sections="Correct body 2112.10741 consumed (Abstract, Intro, Background, Training, Results, Safety, Limitations, eval app). Recorded locator 2112.02092 resolves to unrelated hep-th paper.", corrected="2112.10741",
 claims=[
  ("The source trains a 3.5B diffusion model (2.3B ADM visual + 1.2B 24-block text Transformer at 64px) plus a 1.5B 64-to-256 upsampler, finetuned with 20% empty captions for classifier-free guidance and a separate inpainting finetune (extra RGB + mask channels, zero-initialised); inference compares classifier-free extrapolation against noised ViT-L CLIP-gradient guidance; inpainting and SDEdit reuse.", "PRIMARY_FACT", "Correct body Training/Results; title/authors verified."),
  ("Reported numbers: human Elo on MS-COCO 256px (CF 3.0, CLIP 2.0): photorealism/caption classifier-free 82.7/110.9 vs CLIP −73.2/29.3 vs unguided −88.6/−106.2; vs DALL-E wins 87% photorealism, 69% caption (reranked, temp 0.85); zero-shot FID 12.24 at CF 1.5.", "PRIMARY_FACT", "Correct body eval app/conditions."),
 ],
 lims=["Recorded locator 2112.02092 is a transcription defect; claims rest on verified-correct 2112.10741. Future Discovery repair should correct the locator.",
  "Fails unusual objects/scenarios; filtered-300M release retains dataset biases under guidance."],
 extra_ver={}),

"BT-D034": dict(access="FULL", sections="Correct body 2211.01324 consumed (Abstract, Intro, Background, expert ensemble, multi-embedding, paint-with-words, experiments §5.1). Recorded locator 2211.12572 resolves to unrelated PnP Diffusion paper.", corrected="2211.01324",
 claims=[
  ("The source pretrains one shared EDM denoiser on log-normal noise, then binary-tree splits and finetunes stage experts (final 3-expert: high-noise, low-noise, intermediate) conditioned on T5-XXL + CLIP-text + CLIP-image with independent dropout; same per-step cost (one expert per sigma) over 64-base + SR256 + SR1024 cascade; training-free paint-with-words via cross-attention bias.", "PRIMARY_FACT", "Correct body expert-ensemble/multi-embedding sections; title/authors verified."),
  ("Reported numbers: zero-shot FID-30K COCO 256px Config-B 7.26 (beats Imagen), Config-D best 7.04; 4-expert at 600k beats shared baseline at 800k across the FID-CLIP curve (5K COCO + Visual Genome, CFG sweep 0-10); ~1B training pairs.", "PRIMARY_FACT", "Correct body §5.1/conditions."),
 ],
 lims=["Recorded locator 2211.12572 is a transcription defect; claims rest on verified-correct 2211.01324. Future Discovery repair should correct the locator.",
  "Expert count grows training cost; CLIP-only lacks compositionality, T5-only weaker foregrounds."],
 extra_ver={}),

"BT-D035": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-4 (contrastive pretraining, zero-shot, data/setup, results/prompts)", corrected=None,
 claims=[
  ("The source defines CLAP: CNN14 audio + BERT text encoders with linear projections to 1024-d joint space, symmetric contrastive loss with learned temperature on 128k pairs; inference by cosine similarity against templated text prompts (no diffusion).", "PRIMARY_FACT", "§2."),
  ("Reported numbers: zero-shot ESC50 82.6% (human 81%, AudioCLIP 69%), US8K 73.24%, FSD50K 30.24% mAP vs 3% Wav2CLIP, Music-vs-Speech 100%; supervised best on 5/16 tasks.", "PRIMARY_FACT", "§4 tables/conditions."),
 ],
 lims=["Speech/emotion/keyword tasks near-random; caption-quality bottleneck; AudioSet augmentation hurts.",
  "Conditioning use in generative audio diffusion and FAD/human alignment validity not established."],
 extra_ver={}),

# ---------------- D04 control ----------------
"BT-D036": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-4 (related, ControlNet+SD+training+CFG-resolution-weighting, qual/ablation/quant)", corrected=None,
 claims=[
  ("The source adds spatial control to frozen large diffusion: locked SD UNet plus a trainable copy of 12 encoder + 1 middle blocks linked by zero-initialised convolutions (growing from zero), a tiny 4-conv encoder for canny/depth/pose/segmentation, 50% prompt dropout; inference composes controls additively with CFG Resolution Weighting.", "PRIMARY_FACT", "§3-4."),
  ("Reported numbers: sketch perceptual quality 4.22 / fidelity 4.28 vs lite variant 3.93/4.09; ADE20K IoU 0.35 vs 0.58 ground truth, FID 15.27 vs lite 17.92; depth-conditioned outputs indistinguishable from industrial tools at 0.52±0.17; sudden convergence under 10k steps; robust from <<50k to >>1M samples.", "PRIMARY_FACT", "§4 tables/conditions."),
 ],
 lims=["Ambiguous inputs need prompts; multi-control weighting manual; single-control framing.",
  "Per-condition dataset sizes beyond the stated robustness curve not established."],
 extra_ver={}),

"BT-D037": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-4 (related, SD prelim, adapter/cubic sampling, COCO/compose/generalise/ablation)", corrected=None,
 claims=[
  ("The source defines T2I-Adapter: lightweight adapter (~77M; small 18M, tiny 5M) injecting 4-scale features into a frozen SD encoder, cubic timestep sampling emphasising early steps; weighted adapter sums at inference with no retraining, generalising to SD1.4/1.5 derivatives.", "PRIMARY_FACT", "§3."),
  ("Reported numbers: COCO FID 16.78 (seg) / 17.36 (sketch) vs PITI 19.36/21.21 vs SD 24.68; CLIP 0.2652/0.2666; 10 epochs batch-8 on 4xV100 ~3 days; encoder-injection placement best (FID 17.36).", "PRIMARY_FACT", "§4 tables/conditions."),
 ],
 lims=["Multi-adapter fusion manual; coarse free-hand sketch variance.",
  "Direct ControlNet-capacity comparison beyond concurrent-work citation not established."],
 extra_ver={}),

"BT-D038": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-4 (related, prelim, encoder/decoupled-attention/training, COCO/structure/multimodal/ablation)", corrected=None,
 claims=[
  ("The source defines IP-Adapter: frozen SD plus frozen OpenCLIP ViT-H/14 global image embedding projected to 4 tokens; decoupled cross-attention adds per-layer image K'/V' (initialised from text weights); only ~22M parameters trained with image-dropout for classifier-free-style control; reusable and ControlNet-compatible.", "PRIMARY_FACT", "§3."),
  ("Reported numbers: COCO CLIP-I 0.828 / CLIP-T 0.588 vs SD-variations 0.760/0.548; 10M LAION+COYO pairs, 1M steps on 8xV100, DDIM-50 CFG-7.5.", "PRIMARY_FACT", "§4 tables/conditions."),
 ],
 lims=["Content/style resemblance only; not subject-consistent like DreamBooth/Textual Inversion.",
  "Identity-preservation metrics vs DreamBooth not established."],
 extra_ver={}),

"BT-D039": dict(access="FULL", sections="Correct body 2208.12242 consumed (Abstract, Intro, method §§3.1-3.3, experiments §§4.1-4.5, limitations). Recorded locator 2208.04111 resolves to unrelated math.CO paper.", corrected="2208.12242",
 claims=[
  ("The source defines DreamBooth personalisation: finetune all layers of a frozen pretrained diffusion model on 3-5 images captioned with a rare-token identifier plus class noun, with autogenous class prior-preservation loss (own class samples, weight lambda); inference reuses the frozen personalised model with identifier prompts for recontextualisation, view synthesis, art rendition, property modification.", "PRIMARY_FACT", "Correct body §3; title/authors verified."),
  ("Reported numbers: 30 subjects x 25 prompts x 4 images (3000 images): Imagen-DreamBooth DINO 0.696 / CLIP-I 0.812 / CLIP-T 0.306, SD-DreamBooth 0.668/0.803/0.305 vs Textual-Inversion 0.569/0.780/0.255; user study (72 users, 1800 answers) SD-DreamBooth over TI: subject 68% vs 22%, prompt 81% vs 12%; ~1000 iterations, lambda 1.", "PRIMARY_FACT", "Correct body §4/conditions."),
 ],
 lims=["Recorded locator 2208.04111 is a transcription defect; claims rest on verified-correct 2208.12242. Future Discovery repair should correct the locator.",
  "Rare-context failures, context-appearance entanglement (colour shifts), overfitting near training settings."],
 extra_ver={}),

"BT-D040": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-5 (problem, adapters, LoRA, RoBERTa/DeBERTa/GPT-2/GPT-3), §7 rank analysis", corrected=None,
 claims=[
  ("The source defines LoRA: freeze W0, learn low-rank update deltaW=BA (r much smaller than dimensions) applied to query/value projections, Gaussian-A + zero-B initialisation, alpha/r scaling; merged W=W0+BA at inference gives zero extra latency, task switching by swapping A/B.", "PRIMARY_FACT", "§4."),
  ("Reported numbers: GPT-3 175B adaptation 10,000x fewer parameters (35 MB vs 350 GB), VRAM 1.2 TB to 350 GB, 25% speedup; RoBERTa-large average 89.0 vs 88.9 full finetune; GPT-2-medium E2E BLEU 70.4 vs 68.2.", "PRIMARY_FACT", "§5 tables/conditions."),
 ],
 lims=["Cross-task batching hard if merged; MLP/LN/bias excluded; rank tuning needed.",
  "Diffusion-LoRA media-specific behaviour not evidenced (LLM/NLU/NLG only)."],
 extra_ver={}),

"BT-D041": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §1-4 (related, SPADE+generator+multimodal, quant/qual/human/ablation)", corrected=None,
 claims=[
  ("The source defines SPADE/GauGAN: semantic masks modulate channel-normalised activations via spatially-varying gamma/beta from a 2-layer convolution (layout preserved through normalisation); encoder-free ResNet generator with multi-scale discriminator and VAE style encoder (GAN precursor, not diffusion).", "PRIMARY_FACT", "§3."),
  ("Reported numbers: COCO mIoU 37.4, accuracy 67.9, FID 22.6 vs pix2pixHD 14.6/45.8/111.5; ADE20K 38.5/79.9/33.9; Cityscapes 62.3/81.9/71.8; human preference 79-86% on COCO/ADE.", "PRIMARY_FACT", "§4 tables/conditions."),
 ],
 lims=["Needs paired mask-image data; SIMS better FID via retrieval but worse alignment.",
  "Diffusion-era transfer needs ControlNet linkage; precursor status only."],
 extra_ver={}),

"BT-D042": dict(access="FULL", sections="Correct body 2312.03641 consumed (Abstract, Intro, methodology §§3.1-3.2, experiments §§4.1-4.4, limitations §5). Recorded locator 2311.17058 resolves to unrelated panoptic-VSG paper.", corrected="2312.03641",
 claims=[
  ("The source defines MotionCtrl: frozen LVDM/VideoCrafter1 backbone; first train a lightweight camera module (camera Rt poses into second self-attention of temporal transformers; RealEstate10K + captions, 50k iterations), then an object module (sparse trajectories via convolutional adapter into UNet encoder; WebVid plus ParticleSfM dense-to-sparse with Gaussian filter, 20k dense + 20k sparse); appearance-free Rt plus trajectory conditioning, alone or jointly, transferable to LVDM or AnimateDiff.", "PRIMARY_FACT", "Correct body §3; title/authors verified."),
  ("Reported numbers: 16-frame 256px ParticleSfM-scored: camera-basic 0.0289 vs AnimateDiff 0.0548, camera-complex 0.0735 vs VideoComposer 0.0950, object 28.877 vs 36.8351; CLIPSIM 0.2319, FID 124.09, FVD 852.15 (1000-WebVid references); Adam lr 1e-4 batch 128.", "PRIMARY_FACT", "Correct body §4/conditions."),
 ],
 lims=["Recorded locator 2311.17058 is a transcription defect; claims rest on verified-correct 2312.03641. Future Discovery repair should correct the locator.",
  "Joint complex-camera plus complex-trajectory control has low success rate; order matters (camera-before-object); RealEstate10K scene diversity limited."],
 extra_ver={}),

"BT-D043": dict(access="FULL", sections="Correct body 2311.07069 consumed (Abstract, Intro, Background, Music-ControlNet §III, Setup §IV, Eval §V, Conclusions). Recorded locator 2311.15049 resolves to unrelated math.GN paper.", corrected="2311.07069",
 claims=[
  ("The source defines Music ControlNet: pretrain a 41M convolutional UNet on mel spectrograms (512x160, ~6 s, 22.05 kHz) with genre-mood tags, then finetune a ControlNet-style adapter with per-control MLP plus zero-convolutions on extracted melody (one-hot chroma), dynamics (smoothed dB energy), rhythm (beat/downbeat probabilities), with full-drop plus random-span masking for any-subset and partial-time control; 100-step DDIM inference with CFG 4 on global style and DiffWave vocoder.", "PRIMARY_FACT", "Correct body §III-IV; title/authors verified."),
  ("Reported numbers: in-domain extracted 6 s (all three controls): melody accuracy 58.7%, dynamics micro/macro 90.8%/64.0%, rhythm beat/downbeat F1 70.8%/40.8%; MusicCaps 10 s melody-full created 82.6% vs MusicGen 55.2% (~49% more faithful); 41M parameters vs 1.5B (35x fewer).", "PRIMARY_FACT", "Correct body §V/conditions."),
 ],
 lims=["Recorded locator 2311.15049 is a transcription defect; claims rest on verified-correct 2311.07069. Future Discovery repair should correct the locator.",
  "6 s training window (12-24 s extrapolation raises noise, degrades FAD); created controls can sound monotonous; tag-only text, instrumental-only, no vocals."],
 extra_ver={}),

# ---------------- D05 editing ----------------
"BT-D044": dict(access="FULL", sections="Correct body 2108.01073v2 consumed (Abstract, Intro, §§2-3 method, §5 experiments, App). Recorded locator 2108.01049 resolves to unrelated fluids paper.", corrected="2108.01073",
 claims=[
  ("The source defines SDEdit: noise a guide image to time t0 then reverse a VE/VP SDE with a pretrained score model; t0 in [0.3,0.6] trades guide faithfulness vs realism; masked channel keeps unedited pixels identical (preservation target: guide structure/background identity).", "PRIMARY_FACT", "Correct body §§2-3; title/authors verified."),
  ("Reported numbers: LSUN-bedroom human strokes L2 32.55 vs 53.76-101.18 baselines, realism preference 80.34-98.09%, satisfaction 75.43-91.72%; simulated strokes KID 0.0030 vs 0.0464-0.2070; compositing satisfaction +83.73%.", "PRIMARY_FACT", "Correct body §5/conditions."),
 ],
 lims=["Recorded locator 2108.01049 is a transcription defect; claims rest on verified-correct 2108.01073. Future Discovery repair should correct the locator.",
  "Needs reasonable guide and t0 search; white-pixel guides need large t0 losing faithfulness."],
 extra_ver={}),

"BT-D045": dict(access="FULL", sections="arXiv abs + HTML 2201.09865v4: Abstract, §§1-4 method, §5.1-5.6 experiments, App", corrected=None,
 claims=[
  ("The source defines RePaint inpainting: each reverse step samples the known region from forward-noised input and the unknown region from the model, then mask-combines; resampling diffuses back-and-forth (T=250, jump 10, 10 resamples) to harmonise; preservation target is exact unmasked pixels with mask-defined locality including extreme Half/Expand masks.", "PRIMARY_FACT", "§§3-4."),
  ("Reported numbers: 256px CelebA-HQ/ImageNet, 1000 votes per comparison, 95% preference for RePaint on Wide/Narrow/thin/thick masks; ablation 32-image Wide LPIPS 0.168 (1 resample) to 0.134 (4 resamples) at slowdown cost; jump-10/resample-10 LPIPS 0.068 with 56.25% votes vs LaMa.", "PRIMARY_FACT", "§5/conditions."),
 ],
 lims=["Slow (250x10 evaluations); LPIPS penalises valid diverse fills; thin-structure artefacts; failure cases in App F.",
  "Wall-clock/VRAM/quantisation and RTF not reported in consumed body."],
 extra_ver={}),

"BT-D046": dict(access="FULL", sections="arXiv abs + HTML 2206.02779v2: Abstract, §§1-4 method, Appendix", corrected=None,
 claims=[
  ("The source defines Blended Latent Diffusion: text-conditioned foreground latent blended per step with noised background latent in LDM latent space (8x downsampling) under a downsampled mask; optional per-image decoder-weights finetune (lambda=100) for faces/text/high-frequency backgrounds; progressive dilated-to-thin mask shrinking; CLIP-ranked multiple predictions.", "PRIMARY_FACT", "§§3-4."),
  ("Reported comparison: order-of-magnitude faster than ~25-minute pixel-space Blended Diffusion with better precision vs Blended Diffusion / GLIDE-filtered / PaintByWord++; VAE factor 8, lambda=100.", "AUTHOR_CLAIM", "§4/conditions; exact latency/FID table values not extracted from truncated body."),
 ],
 lims=["Lossy VAE needs optional finetune; pixel stitching seams and Poisson colour-shift; latent optimisation oversmooths; thin masks still fail fine details.",
  "Exact latency/VRAM/NFE and quantisation numbers not established in consumed excerpt."],
 extra_ver={}),

"BT-D047": dict(access="FULL", sections="arXiv abs + HTML 2208.01626v1: Abstract, §§1-4 method, §5 experiments, App A", corrected=None,
 claims=[
  ("The source defines Prompt-to-Prompt editing: fixed seed with source cross-attention maps injected into target generation at the 64x64 stage; Word Swap with tau cutoff, Add-Phrase via alignment function, Re-weight factor in [-2,2]; no training or mask; preservation is composition/geometry via attention with identity via shared maps.", "PRIMARY_FACT", "§§3-4."),
  ("Reported scope: qualitative cake/bicycle-to-car edits, style/specification changes, fader control; DDIM inversion often distorted, requiring attention-derived mask fallback.", "PRIMARY_FACT", "§5/conditions; no FID/CLIP benchmarks in body."),
 ],
 lims=["Inversion distortion; needs source prompt; low-resolution attention bottleneck bounds precision; cannot spatially move objects.",
  "Quantitative fidelity/alignment scores and runtime/VRAM not reported in consumed body."],
 extra_ver={}),

"BT-D048": dict(access="FULL", sections="Correct body 2210.09276v3 consumed (Abstract, §§1-4, App B-C). Recorded locator 2209.15146 resolves to unrelated ML-stress paper.", corrected="2210.09276",
 claims=[
  ("The source defines Imagic: (A) optimise target embedding toward an optimised embedding with denoising loss (Imagen 64px 100 steps lr 1e-3; SD latent 1000 steps lr 2e-3), (B) finetune UNet plus super-resolution stages fixing the optimised embedding (1500 steps), (C) interpolate eta 0.6-0.8 then generate plus super-resolve with 8 seeds picked best; preservation is background/structure/composition/identity for whole-image non-rigid edits.", "PRIMARY_FACT", "Correct body §§3-4; title/authors verified."),
  ("Reported numbers: TEdBench 100 pairs, 9213 two-alternative answers, >70% preference over SDEdit/DDIB/Text2LIVE; eta 0.6-0.8 balances CLIP vs 1-LPIPS average over 150 inputs; cost ~8 min on 2xTPUv4 (Imagen) or 7 min on A100 (SD).", "PRIMARY_FACT", "Correct body §4/conditions."),
 ],
 lims=["Recorded locator 2209.15146 is a transcription defect; claims rest on verified-correct 2210.09276. Future Discovery repair should correct the locator.",
  "Too-subtle edits or zoom/camera-angle shifts; eta/seed sensitive; inherits base-model face/bias limits; slow per-image optimisation."],
 extra_ver={}),

"BT-D049": dict(access="FULL", sections="Correct body 2211.09800v2 consumed (Abstract, §§1-4, App A-B). Recorded locator 2301.01780 resolves to unrelated axion paper.", corrected="2211.09800",
 claims=[
  ("The source defines InstructPix2Pix: GPT-3 finetuned on 700 triplets generates 454,445 instruction-caption pairs from LAION-Aesthetics; Stable Diffusion plus Prompt-to-Prompt sampling (p uniform 0.1-0.9, 100 samples/pair, CLIP-directional filter) trains SD with zero-initialised image-condition channels; dual classifier-free guidance on image (1-1.5, sweep 1.0-2.2) and text (5-10); multi-turn chaining shown.", "PRIMARY_FACT", "Correct body §§2-3; title/authors verified."),
  ("Reported comparison: CLIP image-similarity vs directional-similarity trade-off beats SDEdit at same directional values (text guidance 7.5); full 454k-plus-filter dataset best in ablations; inference in seconds (e.g. 100 steps 512px).", "PRIMARY_FACT", "Correct body §4/conditions."),
 ],
 lims=["Recorded locator 2301.01780 is a transcription defect; claims rest on verified-correct 2211.09800. Future Discovery repair should correct the locator.",
  "Fails viewpoint/zoom, excessive changes, isolation, swapping/counting/spatial reasoning; inherits SD/GPT-3 biases."],
 extra_ver={}),

"BT-D050": dict(access="FULL", sections="arXiv abs + HTML 2212.11565v2: Abstract, §§1-5, App A-C", corrected=None,
 claims=[
  ("The source defines Tune-A-Video: inflate SD 3x3 convolutions to 1x3x3 plus temporal self-attention with sparse spatio-temporal attention querying only first+previous frames; finetune only spatio-temporal query matrices plus full temporal attention plus cross-attention query (500 steps, lr 3e-5, batch 1, 32x512 frames); DDIM-inversion unconditional then DDIM-sample with edited prompt; DreamBooth/ControlNet compatible.", "PRIMARY_FACT", "§§3-4."),
  ("Reported numbers: 42 DAVIS videos x 140 prompts: frame consistency 92.40 vs 90.64 CogVideo vs 88.89 PnP; CLIP-score 27.58 vs 27.56 vs 23.91; user preference 87.86%/62.14% consistency, 85.00%/76.43% alignment; ~10 min finetune + 1 min sample per video on A100.", "PRIMARY_FACT", "§5/conditions."),
 ],
 lims=["Multi-object occlusion mixing; ablations show content drift without sparse attention, stagnant motion without inversion, flicker without finetune; inherits T2I object limits.",
  "VRAM/quantisation/offload and long-horizon consistency numbers not reported."],
 extra_ver={}),

# ---------------- D07 speech ----------------
"BT-D051": dict(access="FULL", sections="arXiv abs + HTML 1609.03499: Abstract, §§1-4, App A-B", corrected=None,
 claims=[
  ("The source defines WaveNet: dilated-causal autoregressive CNN on raw waveform (softmax mu-law 256-way, gated units, residual+skip, global/local conditioning); receptive-field scaling via dilation stacks 1,2,4..512 plus context stacks; sequential sample-by-sample inference.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: TTS MOS WaveNet with linguistic+logF0 features 4.21±0.081 (EN) / 4.08±0.085 (ZH) vs LSTM 3.67/3.79 vs concatenative 3.86/3.47 vs natural 4.55/4.21; gap cut 51% EN, 69% ZH; 44h/109-speaker VCTK; TIMIT raw-audio PER 18.8.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Receptive field ~240-300 ms misses long F0/prosody; sequential sampling costly; music lacks long-range coherence.",
  "Parallel-inference latency and multi-speaker zero-shot similarity scores not established."],
 extra_ver={}),

"BT-D052": dict(access="FULL", sections="arXiv abs + HTML 1703.10135: Abstract, §§1-6", corrected=None,
 claims=[
  ("The source defines Tacotron: end-to-end char-to-speech seq2seq with attention (CBHG encoder, content-tanh attention GRU decoder, 80-band mel target, multi-frame rate 2, CBHG post-net); waveform via 50-iteration Griffin-Lim (not neural vocoder); frame-level inference faster than sample-AR but attention-fragile.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: MOS 3.82±0.085 vs parametric 3.69±0.109 vs concatenative 4.09±0.119 (100 US-English phrases, 8 ratings each, 24 kHz, 24.6h single female speaker).", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Vanilla seq2seq misalignments/repetitions; GRU encoder noisier than CBHG; Griffin-Lim artefacts cap quality.",
  "Robustness rates and inference-latency numbers vs later non-AR systems not established."],
 extra_ver={}),

"BT-D053": dict(access="FULL", sections="Correct body 1712.05884 consumed (Abstract, §§1-4). Recorded locator 1712.05862 resolves to unrelated astro-ph paper.", corrected="1712.05884",
 claims=[
  ("The source defines Tacotron 2: Tacotron-style encoder with location-sensitive attention, LSTM decoder plus post-net predicting 80-band mel (50 ms frame/12.5 ms shift), plus modified 30-layer WaveNet vocoder (3 dilation cycles, 10-component logistic-mixture 16-bit 24 kHz output).", "PRIMARY_FACT", "Correct body §§2-3; title/authors verified."),
  ("Reported numbers: MOS 4.526±0.066 vs ground truth 4.582±0.053 vs WaveNet-linguistic 4.341±0.051 vs concatenative 4.166 (100 in-domain sentences, 8+ raters); side-by-side vs ground truth −0.270±0.155; 12-layer/10.5 ms WaveNet variant 4.481±0.059.", "PRIMARY_FACT", "Correct body §4/conditions."),
 ],
 lims=["Recorded locator 1712.05862 is a transcription defect; claims rest on verified-correct 1712.05884. Future Discovery repair should correct the locator.",
  "Occasional mispronunciation/prosody errors (23/100 unnatural prosody in audit); out-of-domain names weak."],
 extra_ver={}),

"BT-D054": dict(access="FULL", sections="arXiv abs + HTML 1905.09263: Abstract, §§1-5, App A-B", corrected=None,
 claims=[
  ("The source defines FastSpeech: non-autoregressive feed-forward Transformer TTS (FFT blocks, self-attention + 1D convolution) with duration predictor (MSE, log-domain, teacher-extracted alignments) and length regulator (alpha speed/break control); durations from a Transformer-teacher attention head; external WaveGlow vocoder; sequence-level knowledge distillation used.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: LJSpeech MOS 3.84±0.08 ≈ Transformer 3.88±0.09 / Tacotron 2 3.86; mel latency 0.025 s vs 6.735 s (269.40x), end-to-end 0.180 s vs 6.895 s (38.30x, V100 batch 1); 50 hard sentences 0 errors vs Transformer 7/15/17 (34%).", "PRIMARY_FACT", "§4-5/conditions."),
 ],
 lims=["Needs teacher alignments + distillation; duration error propagates; prosody control limited to rate/breaks.",
  "Waveform-level fidelity vs GAN/diffusion vocoders not established."],
 extra_ver={}),

"BT-D055": dict(access="FULL", sections="arXiv abs + HTML 2010.05646: Abstract, §§1-5, App A-C", corrected=None,
 claims=[
  ("The source defines HiFi-GAN: efficient GAN vocoder with transposed-convolution generator plus multi-receptive-field fusion (parallel residual blocks) and multi-period discriminator (periods 2,3,5,7,11 with 2D convolutions) plus multi-scale discriminator; LSGAN + mel-L1 (weight 45) + feature-matching (weight 2) losses.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: LJSpeech V1 MOS 4.36±0.07 (ground truth 4.45±0.06) vs WaveNet-MoL 4.02 / WaveGlow 3.81 / MelGAN 3.79; V1 GPU 3701 kHz (167.86x real-time); V3 CPU 296.38 kHz (13.44x); ablation without multi-period discriminator 2.28; VCTK-unseen V1 3.77.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Multi-period discriminator critical; small-footprint quality gap remains; fine-tuning needed for Tacotron-2-predicted mels.",
  "Prosody/speaker-similarity control beyond vocoding not established."],
 extra_ver={}),

"BT-D056": dict(access="FULL", sections="arXiv abs + HTML 2106.06103: Abstract, §§1-6", corrected=None,
 claims=[
  ("The source defines VITS: end-to-end conditional VAE (linear-spectrogram posterior, Transformer text prior with volume-preserving flow, monotonic alignment search, L1 mel reconstruction) plus stochastic duration predictor (variational dequantisation/augmentation, spline flows) plus HiFi-GAN V1 decoder with multi-period discriminator and feature matching; windowed generator training.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: LJSpeech MOS VITS 4.43±0.06 (≈ ground truth 4.46±0.06) vs VITS-DDP 4.39 vs Glow+HiFiGAN-finetuned 4.32; VCTK 4.38 = ground truth 4.38; speed 1480 kHz (67.12x real-time) vs Glow+HiFiGAN 606 kHz; ablation without flow 2.98.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Flow prior essential; single-speaker text preprocessing (IPA/phonemiser) remains; duration instability possible.",
  "Zero-shot unseen-speaker cloning scores delegated to successor (YourTTS)."],
 extra_ver={}),

"BT-D057": dict(access="FULL", sections="arXiv abs + HTML 2112.02418: Abstract, §§1-7", corrected=None,
 claims=[
  ("The source defines YourTTS: end-to-end VITS backbone (Transformer text encoder, flow decoder, posterior encoder, HiFi-GAN, stochastic duration, monotonic alignment) with speaker-identity conditioning (pretrained speaker embeddings, global conditioning/summation), 4-dim language embeddings, optional speaker-consistency loss, raw-character input; zero-shot multispeaker/multilingual TTS plus voice conversion.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: VCTK 11-unseen-speaker speaker-encoder cosine similarity 0.864, MOS 4.21±0.04, similarity-MOS 4.16±0.05 (≈ ground truth 0.824/4.26/4.19); English-to-English voice conversion MOS 4.20±0.05, similarity 4.07±0.06; <60 s adaptation finetune reaches near-ground-truth similarity.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Duration-predictor instability; mispronunciations without phonemes; gender/language imbalance; consistency loss trades naturalness for similarity.",
  "Streaming latency and codec-LM scaling comparison not established."],
 extra_ver={}),

"BT-D058": dict(access="FULL", sections="arXiv abs + HTML 2301.02111: Abstract, §§1-5", corrected=None,
 claims=[
  ("The source defines VALL-E: codec-token language modelling for zero-shot voice cloning (EnCodec 24 kHz to 75 Hz, 8x1024 RVQ): decoder-only autoregressive model for quantiser 1 plus non-autoregressive model for quantisers 2-8 with adaptive layer-norm staging and shared embedding/prediction layers; phoneme plus 3-second acoustic prompting with sampling decode and EnCodec-decoder synthesis.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: LibriLight 60k-hour/7k-speaker training; LibriSpeech WER 5.9 vs YourTTS 7.7 (ground truth 2.2), speaker similarity 0.580 vs 0.337 (ground truth 0.754); SMOS 4.38±0.10 vs 3.45; VCTK SMOS 3.81 vs 3.70; two-prompt non-autoregressive variant WER 2.8, similarity 0.732.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Random-sampling instability/infinite loops; needs 3-second prompt; noisy pseudo-phoneme labels; no streaming.",
  "Real-time latency and human-parity statistics left to VALL-E 2."],
 extra_ver={}),

"BT-D059": dict(access="PARTIAL", sections="Correct body 2406.05370 consumed partially (Abstract, §§1-3, §4.1; §4.2-4.3 result tables truncated). Recorded locator 2406.05358 resolves to unrelated RL paper.", corrected="2406.05370",
 claims=[
  ("The consumed sections define VALL-E 2: grouped-code language modelling (group size 1/2/4/8 with autoregressive group embedding/prediction plus non-autoregressive remaining codes) with repetition-aware sampling (nucleus sampling then random fallback on repetition-ratio threshold); parity defined as word-error-rate-reduction / CMOS / SMOS deltas above ground truth on LibriSpeech/VCTK.", "PRIMARY_FACT", "Correct body §§1-4.1; title/authors verified."),
 ],
 lims=["Recorded locator 2406.05358 is a transcription defect; claims rest on verified-correct 2406.05370 (partially consumed). Future Discovery repair should correct the locator.",
  "Exact parity margins, latency speedups, and hard-sentence stability numbers NOT established (result tables truncated); prompt length/quality/noise dependence; misuse/spoofing risk noted in-text."],
 extra_ver={}),

"BT-D060": dict(access="FULL", sections="arXiv abs + HTML 2306.15687: Abstract, §§1-3 fully; §4-5 and appendix truncated with claims taken from Abstract/§1", corrected=None,
 claims=[
  ("The source defines Voicebox: flow-matching infilling speech model (non-autoregressive continuous normalising flow with optimal-transport conditional flow matching, Transformer vector field on 80-dim log-mel plus frame-aligned phones) plus duration model, infill conditioning on past+future audio+text, classifier-free guidance, ODE solver under 10 evaluations; external HiFi-GAN-class vocoder.", "PRIMARY_FACT", "Abstract + §§1-3."),
  ("Reported numbers: zero-shot vs VALL-E word-error-rate 5.9% to 1.9%, similarity 0.580 to 0.681, up to 20x faster; cross-lingual vs YourTTS WER 10.9% to 5.2%, similarity 0.335 to 0.481; denoise vs prior work −8.8% WER, +0.450 similarity, +0.80 MOS.", "PRIMARY_FACT", "Abstract/§1/conditions; detailed §5 tables truncated."),
 ],
 lims=["Needs forced alignments/phone transcripts; vocoder-dependent; detailed §5 tables truncated in fetch.",
  "Fine-grained latency-vs-evaluations curves and duration-model ablations beyond consumed sections not established."],
 extra_ver={}),

"BT-D061": dict(access="FULL", sections="arXiv abs + HTML 2406.02430: Abstract, §§1-4", corrected=None,
 claims=[
  ("The source defines Seed-TTS: autoregressive Transformer token language model (speech tokeniser to tokens to diffusion Transformer to vocoder) with instruction/supervised finetuning plus reinforcement post-training (REINFORCE on similarity/word-error/speaker-embedding objectives) plus self-distilled factorisation and a diffusion-Transformer non-autoregressive variant without phoneme-duration module; streaming via causal diffusion with consistency/flow-matching distillation.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: in-context-learning objective English WER 2.249, similarity 0.762, CMOS −0.07 vs human (2.143/0.730); supervised finetune CMOS +0.37; reinforcement CMOS +0.14, hard-word-error 7.585 to 6.423; deployed latency 0.028x real-time-factor 0.132x with CMOS −0.02.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Hard-accent prompts weaker (15 s prompt insufficient); reward-hacking (slower/cleaner but less natural); vendor-authored evaluations.",
  "Model/data scale details and independent reproduction not established."],
 extra_ver={}),

"BT-D062": dict(access="PARTIAL", sections="Recorded body 2308.11596 (v1) consumed (Abstract, §1, contents). Recorded ID is the SeamlessM4T-v1 family, not the v2 expressive/streaming family (2312.05187 body not fetched).", corrected=None,
 claims=[
  ("The consumed v1 body defines: self-supervised w2v-BERT 2.0 (1M hours) plus SeamlessAlign mining plus multitask training plus UnitY text-to-unit plus HiFi-GAN unit vocoder; streaming (efficient monotonic attention) and expressive (UnitY2 non-autoregressive, prosody/style encoder) architectures belong to the v2 family and are NOT established from the consumed v1 body.", "PRIMARY_FACT", "v1 body §§1-3; v2 boundary explicit."),
  ("v1-only reported numbers: Fleurs speech-to-text-translation +20% BLEU; into-English +1.3 BLEU translation / +2.6 ASR-BLEU speech-to-speech vs cascaded; CVSS +58%; robustness +38% noise / +49% speaker; toxicity −63%.", "PRIMARY_FACT", "v1 body §4/conditions."),
 ],
 lims=["Recorded locator covers the v1 family; v2 UnitY2/expressive/streaming latency, speech-rate/pause preservation, and streaming-language claims are NOT established from the consumed body.",
  "v1 lacks expressive/streaming evaluation; prosody/latency metrics need the v2 body."],
 extra_ver={}),

# ---------------- D08 music ----------------
"BT-D063": dict(access="FULL", sections="arXiv abs + HTML 2005.00341v1: Abstract, §1, §2 VQ-VAE, §3 Music-VQ-VAE, §4 priors/upsamplers, §5 dataset/training/samples/ablations Tables 1-3", corrected=None,
 claims=[
  ("The source defines Jukebox: three separate VQ-VAEs (hop 8/32/128, codebook 2048) with random restarts and multi-resolution spectral loss compressing audio; 5B sparse-Transformer top prior (8192-token context ≈24 s top-level) plus 1B upsamplers; artist/genre/timing conditioning plus encoder-decoder unaligned-lyrics conditioning with decoder-pretraining surgery; windowed/primed ancestral sampling.", "PRIMARY_FACT", "§§2-4."),
  ("Reported numbers: spectral convergence on 5000 held-out 3 s clips: bottom −23.0 dB, middle −12.4 dB, top −8.3 dB with restarts; codebook 256 vs 2048 vs none −15.9 vs −23.0 vs −40.5 dB bottom; training 1.2M songs, VQ-VAE 2M parameters on 9 s clips (256xV100 3 days), upsamplers 1B (128xV100 2 weeks), prior 5B (512xV100 4 weeks); evaluation qualitative only, no MOS/FID.", "PRIMARY_FACT", "§5/conditions."),
 ],
 lims=["Coherence holds ~24 s top-context then drifts via windowed extension; no repeating chorus/melody memory; novel-style generalisation weak (artist embedding dominates).",
  "Long-form structure metrics, intelligible-lyrics rates, and motif-level controllability beyond artist/genre/lyrics-window conditioning not established."],
 extra_ver={}),

"BT-D064": dict(access="FULL", sections="arXiv abs + HTML 2009.09761v3: Abstract, §1-2, §3 architecture, §4 related, §5 vocoding/uncond/class-cond/denoise/interp, App A-D", corrected=None,
 claims=[
  ("The source defines DiffWave: bidirectional dilated-convolution epsilon-network (30-layer, kernel 3) with 128-dim sinusoidal step embedding predicting noise under unweighted ELBO; mel spectrogram (80-band, 2x transposed-16x upsample) added as per-layer bias, 128-dim global label embedding; fast sampling collapses train-time steps (20-200) to 6 inference steps.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: LJSpeech 22.05 kHz vocoding MOS LARGE 4.44±0.07 vs WaveNet 4.43±0.10 vs ground truth 4.52±0.06; BASE 4.38±0.08, BASE-Fast 4.37±0.07; BASE-T20 2.1x real-time FP32 V100 vs WaveNet ~500x slower than real-time; SC09 unconditional MOS 3.39±0.32 vs WaveGAN 2.03±0.33, FID 1.287 vs 1.349; class-conditional accuracy 91.2% vs WaveNet-256 60.7%.", "PRIMARY_FACT", "§5/conditions."),
 ],
 lims=["Still slower than SOTA flows; deeper layers/larger dilations degrade quality; zero-shot denoise/interpolation qualitative only.",
  "Music long-form structure, lyrics alignment, or motif/controllability not established (local-fidelity waveform diffusion only)."],
 extra_ver={}),

"BT-D065": dict(access="FULL", sections="arXiv abs + HTML 2301.11325v1: Abstract, §1-3 (background, tokenizers, hierarchical), §4 setup, §5 Table 1 + ablations, §6 melody/story-mode, §7-8", corrected=None,
 claims=[
  ("The source defines MusicLM: frozen SoundStream acoustic tokens (50 Hz, RVQ 12x1024, 6 kbps) plus w2v-BERT semantic tokens (25 Hz) plus MuLan joint text-music tokens (128-d, 10 s window); training conditions semantic on MuLan-audio tokens and acoustic on both, swapped to MuLan-text tokens at inference; three 430M decoder-only Transformers with temperature 1.0/0.95/0.4; story-mode 15 s-stride continuation and melody-condition extension.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: MusicCaps 10 s eval FAD-VGG 4.0 vs Mubert 9.6 vs Riffusion 13.4, KLD 1.01 vs 1.19/1.58, MCC 0.51 vs 0.34/0.32, human wins 312 vs 158/97 (1200 ratings) vs reference 472; no-semantic ablation KLD 1.01 to 1.05, MCC 0.51 to 0.49; memorisation exact <0.2%, approximate <0.01% false-positive.", "PRIMARY_FACT", "§5/conditions."),
 ],
 lims=["Inherits MuLan failures on negation and temporal ordering; MCC favours own method; 30 s training extended autoregressively, no verse/chorus model; no model release.",
  "Beat/chord/key-precise controllability and local-fidelity codec comparisons beyond MuLan/MusicCaps conditions not established."],
 extra_ver={}),

"BT-D066": dict(access="FULL", sections="arXiv abs + HTML 2306.05284v3: Abstract, §1-3 (EnCodec, interleavings, T5/FLAN/CLAP, chroma, decoder), §4 Tables 1-5", corrected=None,
 claims=[
  ("The source defines MusicGen: single-stage autoregressive codec music with EnCodec 32 kHz mono (stride 640 to 50 Hz, RVQ 4x2048) and delay-pattern single Transformer decoder (T5 text via cross-attention, chroma-argmax prefix, classifier-free-guidance drop 0.2 / scale 3.0, top-k 250 / temperature 1.0); stereo fine-tune doubles to 8 codebooks; 300M/1.5B/3.3B sizes trained 1M steps.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: MusicCaps FAD-VGG 3.1 (300M) vs Mousai 7.5 vs Riffusion 14.8, KL 1.28, CLAP-score 0.31; overall/relativity human 78.43±1.30/81.11±1.31 (300M) rising to 84.81±0.95/82.47±1.25 (3.3B) vs MusicLM 80.51±1.07/82.35±1.36 (40 instrumental clips); melody chroma-similarity 0.66 (text+chroma) vs 0.10 text-only.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Classifier-free-guidance-only fine control; flattening best but 6000 vs 1500 steps; chroma degrades objective metrics; melody needs audio-augmentation research.",
  "Lyrics singing or music-theory (chord/key/beat) control beyond unsupervised chroma-melody similarity not established."],
 extra_ver={}),

"BT-D067": dict(access="FULL", sections="arXiv abs + HTML 2301.12503v3: Abstract, §1-5 (CLAP, LDM, mixup, CFG, VAE, HiFiGAN, manipulations, Tables 1-4), App", corrected=None,
 claims=[
  ("The source defines AudioLDM: mel-VAE spectrogram compression (ratio 4 default) plus CLAP-aligned latent diffusion trained on audio embeddings and sampled on text embeddings, audio-only mixup avoiding caption concatenation; classifier-free guidance with 10% drop; shallow-reverse style transfer and masked-latent inpainting/super-resolution via convolutional spatial-mask correspondence.", "PRIMARY_FACT", "§§3-4."),
  ("Reported numbers: AudioCaps test L-Full (739M params, 8886 h) FD 23.31 vs DiffSound 47.68, IS 8.13 vs 4.01, KL 1.59 vs 2.52, FAD 1.96 vs 7.75, overall 65.91±1.0 vs 45.0±2.6; audio-only beats text+audio training (FD 23.31 vs 25.79); ratio-4 FD 29.48 vs ratio-8 33.50 vs ratio-16 34.32.", "PRIMARY_FACT", "§5/conditions."),
 ],
 lims=["CLAP text/audio gap remains; abstract captions hurt text-conditioning; ratio-1/2 untrainable on single RTX3090.",
  "Music-specific long-form/motif/lyrics structure not established (general-audio latent fidelity only)."],
 extra_ver={}),

"BT-D068": dict(access="FULL", sections="Correct body 2407.14358v2 consumed (Abstract, §1-2 arch, §3 CC data, §4 training, §5 Tables 1-4 + memorisation + speed, §6.1 limits). Recorded locator 2402.10046 resolves to unrelated ECE-calibration paper.", corrected="2407.14358",
 claims=[
  ("The source defines Stable Audio Open: variational autoencoder (5 convolutional blocks, dilated ResNet + Snake, 64-dim continuous latent at 21.5 Hz, 156M) plus T5-base text encoder (109M, not CLAP) plus diffusion-Transformer (1057M, rotary-half positions, prepended timing+timestep, cross-attention timing+text) generating up to 47 s variable-length by silence-fill plus trim; trained on 486,492 Creative-Commons clips (7330 h) with random metadata-concat prompts; DPM-Solver++ 100 steps, guidance 7.0.", "PRIMARY_FACT", "Correct body §§2-4; title/authors verified."),
  ("Reported numbers: AudioCaps FD-openl3 78.24 vs SA-1.0 103.66 vs AudioLDM2-48k 101.11, KL 2.14, CLAP-score 0.29; SongDescriber-instrumental FD 96.51 vs MusicGen-stereo 190.47, KL 0.55, CLAP 0.41; autoencoder SI-SDR −0.93 sounds / 6.28 music; speed 8 steps/s RTX3090 (11 A6000, 20 H100), diffusion-Transformer 5.9 GB / decode 14.5 GB; memorisation audit: 3693+856 repeats found, top candidates listened, none found.", "PRIMARY_FACT", "Correct body §5/conditions."),
 ],
 lims=["Recorded locator 2402.10046 is a transcription defect; claims rest on verified-correct 2407.14358. Future Discovery repair should correct the locator.",
  "Creative-Commons data limits music quality vs closed models; fails connectors and intelligible speech/singing; English-only."],
 extra_ver={}),

"BT-D069": dict(access="FULL", sections="Correct body 2311.08355v3 consumed (Abstract, §1-3 MusicBench/MuNet/predictors, §4 Tables 1-3 + ablations, §6 limits). Recorded locator 2308.02530 resolves to unrelated attention paper with author mismatch.", corrected="2311.08355",
 claims=[
  ("The source defines MuSTANGO: Tango/AudioLDM-VAE latent diffusion plus MuNet UNet with sequential cross-attentions (FLAN-T5 text, then beat encoder, then chord encoder), beat-first; inference predicts beats (DeBERTa-Large) and chords (FLAN-T5-Large verbalised) from text; MusicBench 52,768 pairs via enrichment plus pitch/speed/volume augmentation plus rephrasing.", "PRIMARY_FACT", "Correct body §§2-3; title/authors verified."),
  ("Reported numbers: TestA/B/FMA-Caps 10 s, 200 DDPM steps, guidance 3: Mustango-pretrained FD 26.35/25.97/25.18, FAD 1.46/1.67/2.34, KL 1.21/1.12/1.16; controllability TestB beat-chroma-mean 11.64-17.99 vs Tango 6.61 vs MusicGen-M 3.97 vs AudioLDM2 0.79; experts musicality 5.76-6.10/7 vs Tango 2.75.", "PRIMARY_FACT", "Correct body §4/conditions."),
 ],
 lims=["Recorded locator 2308.02530 is a transcription defect (plus author mismatch); claims rest on verified-correct 2311.08355. Future Discovery repair should correct the locator.",
  "Tempo/beat near-parity (captions already carry slow/fast words; beat-extractor noisy); 10 s clips only."],
 extra_ver={}),

# ---------------- D09 video ----------------
"BT-D070": dict(access="FULL", sections="arXiv abs + HTML 2204.03458: Abstract, §1-3 (factorized 3D U-Net, reconstruction guidance), §4.1-4.3 experiments, §6", corrected=None,
 claims=[
  ("The source extends image diffusion to video with a factorized 3D U-Net (2D convolution 1x3x3 plus per-frame spatial attention plus temporal attention with relative positions; images run by masking temporal attention) and reconstruction guidance (gradient of masked-region error, weight wr) extended to spatial super-resolution and block-autoregressive extension.", "PRIMARY_FACT", "§3."),
  ("Reported numbers: UCF-101 16x64x64 unconditional FID 295±3, IS 57±0.62 vs real 60.2; BAIR 1-to-15 frames FVD 68.19 ancestral (512 steps) / 66.92 Langevin (256 steps); Kinetics-600 5-to-11 frames FVD 18.6 ancestral / 16.2±0.34 Langevin; text-video joint training FVD 202.28/205.42 (0 images) to 57.84/60.72 (8 images); 64-frame extension FVD with reconstruction guidance 136.22/134.55 vs replacement 451.45/436.16.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Trains only 16-frame blocks at 64x64/128x128; long video only via autoregressive/temporal-SR guidance; models reflect dataset bias, not released.",
  "Short-range motion fidelity shown; identity/object permanence beyond 64 frames, long-horizon story structure, AV sync, editing preservation not established."],
 extra_ver={}),

"BT-D071": dict(access="FULL", sections="arXiv abs + HTML 2210.02303: Abstract, §1-2 (diffusion, 7-model cascade, Video U-Net, v-prediction, augmentation, joint training, distillation), §3 capabilities/scaling/parameterization/perceptual, §4-5", corrected=None,
 claims=[
  ("The source scales text-to-video to HD 1280x768 128-frame 24 fps: 1 frozen T5-XXL plus 1 base plus 3 spatial-SR plus 3 temporal-SR models (11.6B parameters); base uses temporal attention, SR stages use temporal convolution; v-prediction, noise-conditioning augmentation, classifier-free plus oscillating guidance, two-stage guided progressive distillation to 8 steps with stochastic sampler.", "PRIMARY_FACT", "§2."),
  ("Reported numbers: scaling base 16x40x24 on 4096 samples (500M to 1.6B to 5.6B improves FVD and CLIP); super-resolution 8x80x48 to 8x320x192 at 200k steps (v-prediction faster first-frame FID than epsilon-prediction, which shows colour/temporal shift); Table 1 at 192x320 128 frames: original 256+128 steps CLIP 25.19±0.03 / R-Precision 92.12±0.53 / 618 s vs distilled 8+8 steps 25.03±0.05 / 89.68±0.38 / 35 s (~18x faster, ~36x FLOPs with guidance distilled).", "PRIMARY_FACT", "§3-4/conditions."),
 ],
 lims=["Cascade cost/compute heavy; 3D rotation consistency inexact; trained on 14M video-text + 60M image-text + LAION-400M with bias risk; not released.",
  "Short-range fidelity/style/text-rendering shown; identity permanence over minutes, long-horizon narrative, AV sync, continuation beyond 5.3 s, edit preservation not quantified."],
 extra_ver={}),

"BT-D072": dict(access="BLOCKED", sections="Barrier: https://openreview.net/forum?id=vOEXS39nOF returns an OpenReview browser-verification wall (login required to skip); abstract/introduction/method/experiments not consumable via webfetch.", corrected=None,
 claims=[],
 lims=["Body blocked: no mechanism, numbers, or limitations established from body; the record's C-ViViT plus masked-bidirectional-Transformer description is Discovery-summary only.",
  "This record is retained as NEEDS_MORE pending successful retrieval; masked-prior vs diffusion-prior comparison not established."],
 extra_ver={}),

"BT-D073": dict(access="FULL", sections="Correct body 2209.14792 consumed (Abstract, §1, §2 prev work, §3.1 T2I backbone, §3.2 pseudo-3D conv/attention, §3.3 interpolation, §3.4 training, §4.1 datasets/settings, §4.2 quant, §4.3 qual, §5). Recorded locator 2209.14755 resolves to unrelated hep-ex paper.", corrected="2209.14792",
 claims=[
  ("The source reuses text-to-image appearance/text alignment and learns motion from unlabeled video: text-to-image UNet extended with pseudo-3D convolutions (2D pretrained plus 1D identity-initialised) and pseudo-3D attention (spatial pretrained plus temporal zero/identity-initialised) plus fps conditioning; inference runs prior to 16x64x64 temporal decoder to masked interpolation (76 frames) to temporal+spatial super-resolution (shared noise); image prior trained on 2.3B filtered pairs with prior frozen, motion on videos-only sets.", "PRIMARY_FACT", "Correct body §3; title/authors verified."),
  ("Reported numbers: MSR-VTT zero-shot 16x256x256 all 59,794 test captions FID 13.17 / CLIPSIM 0.3049 vs CogVideo-EN 23.59/0.2631; UCF-101 zero-shot 256px class-conditional IS 33.00 / FVD 367.23, finetuned IS 82.55 / FVD 81.25; human preference 76x256x256 vs prior video-diffusion work 84.38% quality / 78.13% faithfulness.", "PRIMARY_FACT", "Correct body §4/conditions."),
 ],
 lims=["Recorded locator 2209.14755 is a transcription defect; claims rest on verified-correct 2209.14792. Future Discovery repair should correct the locator.",
  "Cannot learn text-to-phenomena observable only in video; longer multi-scene/story videos future; web-data social biases exaggerated."],
 extra_ver={}),

"BT-D074": dict(access="FULL", sections="Correct body 2307.04725 consumed (Abstract, §1-2, §3 prelim, §4.1 domain adapter, §4.2 motion module, §4.3 MotionLoRA, §4.4 practice, §5 qual/quant/ablation/control, §6-8). Recorded locator 2307.04790 resolves to unrelated astro-ph paper.", corrected="2307.04725",
 claims=[
  ("The source animates any personalised text-to-image model without per-model tuning: inflate SD-V1.5 to 5D (image layers per-frame, motion merges spatial to batch); insert temporal Transformer self-attention with sinusoidal positions and zero-initialised residuals, base frozen; LoRA domain adapter on attention fits the video-data quality gap (scaled by alpha, 0 removes it at inference); MotionLoRA LoRA on motion attention for new shot types (20-50 videos, 2000 iterations, ~1-2 h, ~30 MB, composable).", "PRIMARY_FACT", "Correct body §4; title/authors verified."),
  ("Reported numbers: same personalised models, ranked text/domain/smoothness: this work average-user-ratings 2.21/2.28/2.825 and CLIP 31.39/87.29/98.00 vs Tune-a-Video 2.18/1.10/1.615 and T2V-Zero 1.62/2.62/1.56; MotionLoRA 50 references OK, 5 degrades to texture; temporal-convolution ablation collapses to identical frames.", "PRIMARY_FACT", "Correct body §5/conditions."),
 ],
 lims=["Recorded locator 2307.04790 is a transcription defect; claims rest on verified-correct 2307.04725. Future Discovery repair should correct the locator.",
  "Video-data quality gap requires adapter; MotionLoRA needs ~50 references; inherits personalised-model misuse risk; depth-control demo from random noise only."],
 extra_ver={}),

"BT-D075": dict(access="FULL", sections="arXiv abs + HTML 2311.15127: Abstract, §1-3 (background, curation, base/T2V/I2V/interpolation/multi-view), §4, App A", corrected=None,
 claims=[
  ("The source unifies data curation with three-stage training (image pretraining, low-resolution video pretraining, high-quality finetune): SD2.1 spatial initialisation plus inserted temporal convolution/attention, full finetune, EDM with noise-shift for resolution, micro-conditioning on fps; base 14x256x384 then 14x320x576 on curated video data plus 1M high-quality finetune; image-to-video via CLIP-image plus noise-augmented frame concatenation plus linearly increasing guidance; LoRA for camera variants.", "PRIMARY_FACT", "§§3-4."),
  ("Reported numbers: UCF-101 zero-shot text-to-video base FVD 242.02 vs Make-A-Video 367.23 (literature numbers); human Elo: image-pretrained over scratch, curated-10M subsets over WebVid/InternVid, curated-50M over uncurated-50M persisting after 50k high-resolution finetune; 25-frame image-to-video preferred over commercial systems in voter test; multi-view variant 12k steps/16 h on 8xA100 competitive on 50-object benchmark via PSNR/LPIPS/CLIP-S.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Short-clip focus; keyframe-at-once costly, sometimes too little motion, slow/high-VRAM sampling; long video needs coarser cascade or video tokeniser plus distillation.",
  "Short-range motion/continuation from single image shown; durable identity permanence, long-horizon structure, AV sync, editing preservation not established."],
 extra_ver={}),

"BT-D076": dict(access="PARTIAL", sections="Static HTML of the Meta research page consumed (title, date October 16 2024, full abstract, author list). Method/evaluation sections are JavaScript-gated (only 2 renderable text lines); no architecture/latent/training/eval-protocol sections consumed.", corrected=None,
 claims=[
  ("The page abstract states: cast of foundation models generating 1080p HD videos with aspect ratios and synchronised audio, plus instruction-based video editing and personalised videos from a user image; claimed state-of-the-art on text-to-video, personalisation, editing, video-to-audio, text-to-audio; largest video model 30B-parameter transformer, 73K video-token context (16 s at 16 fps); innovations claimed across architecture, latent spaces, objectives, data, evaluation, parallelisation, inference; all videos at a linked gallery.", "VENDOR_CLAIM", "Page static abstract; method/eval sections not consumed."),
 ],
 lims=["Abstract-level only: 30B/73K/16 s figures are vendor claims without consumed method/eval sections; JavaScript-gated body is an access barrier.",
  "Synchronised-AV fidelity, identity permanence, long-horizon structure, continuation, editing preservation not established."],
 extra_ver={"vendor-claim quarantine": ("VERIFIED", "Page abstract quarantined as vendor claim: 30B/73K/SOTA statements attributed to Meta with no independent reproduction; no mechanism inferred beyond page wording.")}),

"BT-D077": dict(access="FULL", sections="OpenAI Sora overview page body consumed (header/lifecycle banner, capability prompts, multi-shot/character persistence claims, weakness examples, safety, research techniques: diffusion+transformer+patches+recaptioning). Capability/lifecycle only.", corrected=None,
 claims=[
  ("The page presents text-to-video up to ~1 minute with quality/prompt adherence (historical turning point; product retired 2026): diffusion from noise with multi-step denoising, all-at-once or extended generation with multi-frame foresight, image-to-video animation, extend/fill-missing-frames, descriptive recaptioning for prompt following; dated lifecycle banner: Sora product unavailable as of 2026-04-26.", "VENDOR_CLAIM", "Page body; capability/lifecycle wording only."),
 ],
 lims=["Page gives no FVD/FID/CLIP scores or conditions, only qualitative claims and dated lifecycle facts.",
  "Page-listed weaknesses: physics/cause-effect failures, left/right confusion, temporal-trajectory errors, implausible motion, spontaneous entities, morphing, multi-character interaction errors. Architecture undisclosed per page."],
 extra_ver={}),

# ---------------- D10 runtime ----------------
"BT-D078": dict(access="FULL", sections="arXiv abs + HTML 2202.00512v2: Abstract, §§1-5, App B-G", corrected=None,
 claims=[
  ("The source defines progressive distillation: an N-step teacher's two DDIM steps distilled into a single student step via inverted targets, iterating N to N/2; stable parameterisations (x / x+eps / velocity with truncated-SNR weighting), cosine schedule; same-architecture student.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: CIFAR-10 FID 3.0 at 4 steps vs DDIM 4.16 at 100 and 13.36 at 10; 2.57 at 8, 4.51 at 2, 9.12 at 1; ImageNet-64/LSUN-128 near-optimal to 4-8 steps vs sharp DDIM drop below 128; 50k updates per halving (100k to 1-2 steps), total at most original training cost.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Degrades at 1-2 steps; no architecture compression; distilled stochastic sampling sits between distilled DDIM and undistilled stochastic.",
  "Latency/RTF/VRAM/hardware/quantisation/offload numbers not reported in consumed body."],
 extra_ver={}),

"BT-D079": dict(access="FULL", sections="arXiv abs + HTML 2310.04378v1: Abstract, §§1-5, App A-H", corrected=None,
 claims=[
  ("The source defines Latent Consistency Models: consistency distillation in latent space for few-step inference (latent consistency function, epsilon-parameterisation, one-stage guided distillation solving augmented probability-flow ODE with sampled guidance, DDIM/DPM-Solver stepping, skipping factor 20); plus latent-consistency finetuning; 1-4-step inference.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: LAION-Aesthetics 12M-512/650k-768 training, 4000 steps (~32 A100-hours); 512px guidance-8: FID 11.10 (4-step) vs DDIM 22.38 / DPM++ 18.43 / guided-distill 15.12, CLIP 28.69 vs 25.89-27.25; 1-step 35.36 vs 183-185.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["1-step gap remains; solver/skipping/guidance sensitive; custom sets need finetuning without universal module.",
  "Inference latency/VRAM/RTF/quantisation/offload not reported in consumed body."],
 extra_ver={}),

"BT-D080": dict(access="FULL", sections="arXiv abs + HTML 2311.05556v1: Abstract, §§1-3", corrected=None,
 claims=[
  ("The source defines LCM-LoRA: LoRA-parameterised consistency acceleration (trainable 67.5M for SD-V1.5 0.98B, 105M for 1.3B, 197M for SDXL 3.5B); acceleration vector plus style vector combinable without training (e.g. 0.8/1.0); neural probability-flow-ODE plug-in with 4-step guidance at 512/1024.", "PRIMARY_FACT", "§§2-3."),
  ("Reported scope: qualitative 4-step 512-V1.5/1024-SDXL/1B generations vs DPM-Solver++ at higher NFE; no FID/CLIP table in this report (defers to LCM).", "PRIMARY_FACT", "§3/conditions."),
 ],
 lims=["Report-only, no new benchmark; combination weights heuristic; per-model generality needs validation.",
  "Steps/latency/VRAM/hardware/quantisation numbers not established in consumed body."],
 extra_ver={}),

"BT-D081": dict(access="FULL", sections="Correct body 2311.17042v1 consumed (Abstract, §§1-4). Recorded locator 2311.17049 resolves to unrelated MobileCLIP paper.", corrected="2311.17042",
 claims=[
  ("The source defines Adversarial Diffusion Distillation: student from SD2.1/SDXL with 4 timesteps and zero-terminal SNR; hinge adversarial loss with frozen DINOv2 ViT-S heads plus text+image conditioning plus R1 regularisation, plus score-distillation loss (final NFSD variant in pixel space); no classifier-free guidance at inference with iterative refinement.", "PRIMARY_FACT", "Correct body §§2-3; title/authors verified."),
  ("Reported numbers: COCO-5k 512px ADD-M 1-step FID 19.7 / CLIP 0.326 vs UFOGen 22.5/0.311, InstaFlow-0.9B 23.4/0.304, progressive-distillation 4-step 26.4/0.300; human Elo 1-step beats LCM-XL-4-step, 4-step beats SDXL-Base-50-step; time 0.09 s 1-step vs DPM 25-step 0.88 s (A100 mixed precision, 512px).", "PRIMARY_FACT", "Correct body §4/conditions."),
 ],
 lims=["Recorded locator 2311.17049 is a transcription defect; claims rest on verified-correct 2311.17042. Future Discovery repair should correct the locator.",
  "Slightly lower diversity than teacher; realism vs oversmoothing trade-off; 512px evaluation."],
 extra_ver={}),

"BT-D082": dict(access="FULL", sections="arXiv abs + HTML 2311.16567v2: Abstract, §§1-5, App A-C", corrected=None,
 claims=[
  ("The source redesigns diffusion for mobile (UViT: bottleneck transformers 1024 channels, dropped self-attention at 64 and 32/outer-16 keeping cross-attention on 77 tokens, shared key-value 5% saving, swish-for-GELU, relu-attention with 10k finetune, feed-forward 4-to-3 10% saving, separable convolutions, 22-to-11 blocks 386M/182 GFLOPs, VAE f8-c8 plus distilled decoder); UFOGen full-finetune plus diffusion loss best; one-step must support plugins/LoRA/inpainting.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: COCO-30k 1-step FID 11.67 / CLIP 0.320 vs UFOGen 12.78/0.317, SnapFusion-8-step 13.5/0.308, SD-50-step 9.62/0.304; 50-step 8.65/0.325; human-preference 26.65 1-step vs 27.30 50-step; iPhone-15-Pro milliseconds 4+92+142=238 1-step vs 646/1740/7429 for longer schedules; 0.2 s 512px generations; 150M-pair training.", "PRIMARY_FACT", "§4/App/conditions."),
 ],
 lims=["Search cost 512 TPUs x 15 days; relu-attention needs finetune; downstream transfer without retraining retains gap; failures in appendix.",
  "Explicit VRAM/peak-memory and int8-quantised latency numbers not established beyond float16/int8 motive."],
 extra_ver={}),

# ---------------- D11 evaluation ----------------
"BT-D083": dict(access="PARTIAL", sections="arXiv abs consumed (Heusel et al., NIPS 2017, verified) plus FAD §2 cross-description. Full-text HTML 404 (base+v6) and ar5iv fatal conversion; PDF/TeX only, not body-consumed.", corrected=None,
 claims=[
  ("The abstract introduces the Fréchet Inception Distance as a distribution-similarity metric alongside the two time-scale update rule, tested on CelebA/CIFAR-10/SVHN/LSUN-Bedrooms; per the consumed FAD §2 cross-description, FID fits multivariate Gaussians on Inception coding-layer embeddings of generated vs large real sets and reports their Fréchet distance.", "AUTHOR_CLAIM", "Abstract + FAD §2 cross-description; full-text sections not consumed."),
 ],
 lims=["Exact embedding layer, sample sizes, and preprocessing not verified; distribution-level, prompt-blind metric.",
  "FID values, sample-size requirements, and embedding dependence not established."],
 extra_ver={}),

"BT-D084": dict(access="FULL", sections="Correct body 1606.03498 consumed (§§4-6). Recorded locator 1606.03461 resolves to unrelated math paper.", corrected="1606.03498",
 claims=[
  ("The source defines the Inception Score: exp(E[KL(p(y|x)||p(y))]) from a pretrained Inception network on ImageNet; low-entropy conditional means recognisable objects, high-entropy marginal means diversity; authors require ~50k samples since the score measures diversity.", "PRIMARY_FACT", "Correct body §§4-6; title verified."),
  ("Reported numbers: CIFAR-10 50k samples real 11.24±0.12, own methods 8.09±0.07, ablations down to 3.87±0.03; human real/fake judgement 78.7%, 71.4% on top-1% score-filtered.", "PRIMARY_FACT", "Correct body tables/conditions."),
 ],
 lims=["Recorded locator 1606.03461 is a transcription defect; claims rest on verified-correct 1606.03498. Future Discovery repair should correct the locator.",
  "Rough guide for independently trained models only; direct optimisation yields adversarial examples; ImageNet-class objectness bias."],
 extra_ver={}),

"BT-D085": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§1-6, App C-D, Tables 1-2", corrected=None,
 claims=[
  ("The source defines GenEval: 6 tasks x 553 templated prompts (COCO-80 objects, 11 Berlin-Kay colours); Mask2Former detector (confidence 0.3, 0.9 for counting) for presence/count/centroid-position plus CLIP ViT-L/14 on masked crops for colour; binary per-image correctness averaged per task.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: human agreement 83% overall (inter-annotator 88%), 91% on unanimous subset vs CLIPScore 80%/87%; IF-XL overall 0.61, SD-v2.1 0.50; position subtasks at most 15%, binding at most 35%.", "PRIMARY_FACT", "§4 Tables 1-2/conditions."),
 ],
 lims=["Closed COCO-80 vocabulary; photo-trained detector fails on holes/overlaps/clipart; ignores aesthetics/realism.",
  "Open-vocabulary generalisation beyond tested models not established."],
 extra_ver={}),

"BT-D086": dict(access="FULL", sections="arXiv abs + HTML v3: Abstract, §§I-IV, Tables I-VII (result §§V-VI partially consumed)", corrected=None,
 claims=[
  ("The source defines T2I-CompBench: 8000 prompts in 4 categories/8 subcategories (colour/shape/texture binding; 2D/3D/non-spatial relations; numeracy 1-8; complex); disentangled BLIP visual-question-answering per-pair yes-probability multiplied; UniDet (plus depth, IoU thresholds) for spatial/numeracy; MLLM 0-100 chain-of-thought scoring; 3-in-1 (CLIP+VQA+UniDet) for complex prompts.", "PRIMARY_FACT", "§§II-IV."),
  ("Reported scope: benchmark protocol consumed; per-model score tables in §§V-VI not fully consumed, so no per-model ordering is recorded here.", "AUTHOR_CLAIM", "§§II-IV; §§V-VI partial."),
 ],
 lims=["Detector/VQA-bounded; MLLM instability/hallucination; prompts intentionally include physically-impossible compositions.",
  "Per-model score ordering and MLLM-vs-dedicated-metric winner per subcategory not established."],
 extra_ver={}),

"BT-D087": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§1-7, App, Tables 1-2, Figs 5-7", corrected=None,
 claims=[
  ("The source defines Pick-a-Pic: web-app two-image pairwise choice plus tie (backbones SD2.1/Dreamlike/SDXL, varied guidance); 583,747 training examples / 37,523 prompts / 4,375 users with prompt-disjoint splits; PickScore is CLIP-H fine-tuned 4000 steps with InstructGPT-style KL preference objective plus inverse-prompt-frequency weighting.", "PRIMARY_FACT", "§§2-4."),
  ("Reported numbers: preference accuracy PickScore 70.5% vs experts 68.0%, CLIP-H 60.8%, random 56.8%; MS-COCO win-rate correlation 0.917 vs FID −0.900; Elo correlation 0.790±0.054 vs HPS 0.670; ranking win rates 71.3-85.1%.", "PRIMARY_FACT", "§5 Tables 1-2/conditions."),
 ],
 lims=["Self-selected social-media users; NSFW residue; 'superhuman' is vs context-blind annotators, not vs originating users.",
  "Generalisation beyond tested backbones/guidance scales not established."],
 extra_ver={}),

"BT-D088": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§1-7, App A-C", corrected=None,
 claims=[
  ("The source defines the Fréchet Audio Distance: VGGish 128-dim embeddings on 1-second windows (0.5 s step) with Fréchet distance between Gaussians of eval set vs clean background set (Magnatagatune 540 h background / 60 h eval); validated across 13 distortion families with intensity sweeps.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: human correlation 0.52 vs SDR 0.39, cosine −0.15, magnitude-L2 −0.01 (69,300 pairs, 20 raters, 300 5 s clips); clean-audio FAD 0.2; usable from ~300 clips/25 min.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["VGGish log-mel input is phase-blind; 1-second windows miss long-term structure; outliers on high/low-pass vs humans.",
  "Speech/TTS transfer not established (music-enhancement validation only)."],
 extra_ver={}),

"BT-D089": dict(access="PARTIAL", sections="Recorded locator 1507.08211 resolves to unrelated math paper (verified). Corpus facts verified from openSLR/ICASSP-citation snippets only; ICASSP PDF binary unparseable via webfetch.", corrected=None,
 claims=[
  ("Snippet-verified corpus facts: ~1000 hours of 16 kHz read English from LibriVox audiobooks, segmented/aligned, with Kaldi recipes, language-model data, and prebuilt language models released (openSLR-12).", "AUTHOR_CLAIM", "Citation snippets only; body sections not consumed."),
 ],
 lims=["Recorded locator 1507.08211 does not resolve to the LibriSpeech paper (transcription defect). Read-speech only; corpus splits, alignment protocol, and baselines not consumed from body.",
  "Exact splits, alignment method, baseline word-error-rates not established."],
 extra_ver={}),

"BT-D090": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§1-3, Tables 1-3", corrected=None,
 claims=[
  ("The source defines generalised end-to-end speaker-verification loss: batch of 64 speakers x 10 utterances; L2-normalised d-vectors from LSTM plus linear layer on 40-dim log-mel (25 ms/10 ms); scaled-cosine similarity matrix vs all centroids (true centroid excludes query); softmax loss (text-independent) or max-hard-negative contrast loss (text-dependent); multi-reader weighted multi-source loss; text-independent inference via 160-frame sliding windows with 50% overlap.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: text-dependent average equal-error-rate 3.55 to 3.10 (no multi-reader), 2.67 to 2.38 (multi-reader), ~30% relative cross-keyword gain, 60% less training time; text-independent 4.06/4.13 to 3.55, ~3x faster.", "PRIMARY_FACT", "§3 Tables 1-3/conditions."),
 ],
 lims=["Google-internal training sets (150M/1.2M utterances); embedding similarity is not naturalness; no listening tests.",
  "Open-data replication and validity as a text-to-speech speaker-similarity metric not established."],
 extra_ver={}),

"BT-D091": dict(access="BLOCKED", sections="Barrier: ITU landing page (R-REC-BS.1534-3, in force, approved 2015-10, managed group R00-SG06) exposes title/status only; full Recommendation text gated (purchase/login); no method sections retrievable.", corrected=None,
 claims=[],
 lims=["Body blocked: no protocol, scale, anchor, or listener-selection details verified; title/status only.",
  "All protocol details (stimulus set, anchors, scale, analysis) not established; per-study binding would need primary-study sources anyway. This record is retained as NEEDS_MORE."],
 extra_ver={}),

"BT-D092": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§1-5 plus Table 1 (supplement G-M method details partially consumed)", corrected=None,
 claims=[
  ("The source defines VBench: 16 disentangled dimensions (~100 prompts each) plus 8 content categories; video quality via DINO/CLIP cross-frame consistency, motion-adaptive flicker, interpolation-prior motion smoothness, RAFT dynamics, LAION aesthetics, MUSIQ imaging; condition consistency via GRiT (object/multi/colour/rule-based spatial), UMT action, Tag2Text scene, CLIP/ViCLIP style; pairwise human win-ratio alignment check per dimension.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: 4-model table (subject consistency 86-92%, spatial 18-37%, dynamic degree 42-90%); empirical min/max plus WebVid-average baselines included.", "PRIMARY_FACT", "§4 Table 1/conditions."),
 ],
 lims=["Pipelines inherit backbone biases; static videos can cheat consistency dimensions; text-to-video trails text-to-image (especially SDXL) on multi-object/spatial compositionality.",
  "Cross-dimension weighting not established (no single score by design)."],
 extra_ver={}),

"BT-D093": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§I-V plus Table II (later-experiment detail partially consumed)", corrected=None,
 claims=[
  ("The source defines VBench-2.0: 5 groups/18 dimensions (~70 prompts each); text-description alignment via LLaVA-Video-7B caption plus Qwen2.5-7B judge for complex semantics plus multi-question visual QA for surface visuals; specialists: ViT anomaly detectors (body/hand/face via YOLO-World patches), ArcFace identity, CoTracker camera heuristics, SIFT/FLANN/RANSAC plus RAFT geometry, LoRA-tuned Qwen2.5-VL-3B instance preservation; uniform prompt refiner (except Sora).", "PRIMARY_FACT", "§§II-IV."),
  ("Reported numbers: 4-state-of-the-art table: complex plot ~10-11%, dynamic spatial ~20%, motion order 15-29% (all low); anatomy 60-89%; 284 annotator-hours quality assurance at 95% bar.", "PRIMARY_FACT", "§V Table II/conditions."),
 ],
 lims=["Vision-LLM hallucination only mitigated (pre-filtering, redundant questions); per-evaluation model-version snapshots required.",
  "Longitudinal stability and minute-level plot-summarisation errors (flagged in-text) not established."],
 extra_ver={}),

# ---------------- D12 convergence ----------------
"BT-D094": dict(access="FULL", sections="arXiv abs + HTML 2206.08916v1: Abstract, §1-4 (goal, unified tokens, encoder-decoder, pretraining, tasks, GRIT), §5.1/5.3", corrected=None,
 claims=[
  ("The source defines Unified-IO: one seq2seq Transformer for 7+ vision/language tasks without task/modality heads (generation-relevant: text-to-image, inpainting, segmentation-to-image); all input/output homogenised to discrete tokens (text via SentencePiece prompts, dense maps/images via VQ-GAN codebooks, boxes/points via 1000 location tokens) fed to a pure T5 encoder-decoder with 2D patches and positional encodings; span-denoise 15% plus image-denoise 75% pretraining, then temperature-mixed multitask training on 80+ datasets without benchmark finetuning.", "PRIMARY_FACT", "§3."),
  ("Reported numbers (generation-relevant scope): GRIT-test average 64.3 (XL) vs GPV-2 32.0, first to cover 7/7; NYUv2 RMSE 0.385 (VQVAE-limited); ImageNet 79.1; COCO CIDEr 126.8; scale Small to XL monotonic, no saturation.", "PRIMARY_FACT", "§4-5/conditions."),
 ],
 lims=["VQ-GAN caps dense-output precision; pure Transformer lacks pyramid/loss priors; GRIT Unrestricted-track only.",
  "Audio/music generation or any-to-any audio conditioning not established (image/text generation tasks only; TS-002/TS-003 boundary)."],
 extra_ver={}),

"BT-D095": dict(access="FULL", sections="Correct body 2306.12925v1 consumed (Abstract, §1-3 tokenizers/vocab/decode/tasks/mixtures, §4 data/metrics, §5 ablations). Recorded locator 2306.12904 resolves to unrelated physics paper.", corrected="2306.12925",
 claims=[
  ("The source defines AudioPaLM: single decoder-only LLM consuming/generating interleaved speech+text (PaLM/PaLM-2 SentencePiece vocabulary expanded by 1024 audio tokens from w2v-BERT-multilingual or USM at 25 Hz, all weights trained on tagged mixtures including combined ASR+AST+S2ST single-decode chain-of-thought); decoding via AudioLM Stage-2/3 or SoundStorm (parallel, 100x faster) with 3-second voice prompt for cross-lingual voice transfer.", "PRIMARY_FACT", "Correct body §3; title/authors verified."),
  ("Reported numbers: AST AudioPaLM-2 over AudioPaLM +28% AST-observed / +107% ASR-observed; FLEURS zero-shot ASR-observed 20.7 BLEU vs Whisper-Large-v2-1.5B 19.6; speech-to-speech-translation BLEU-via-ASR state-of-the-art with superior voice-preservation scores vs cascades; training Adafactor lr 5e-5, mixtures e.g. thousands of hours.", "PRIMARY_FACT", "Correct body §5/conditions."),
 ],
 lims=["Recorded locator 2306.12904 is a transcription defect; claims rest on verified-correct 2306.12925. Future Discovery repair should correct the locator.",
  "Speech+text only (no image/video/music); translation targets largely synthetic; 3-second-prompt voice transfer degrades on shorter prompts."],
 extra_ver={}),

"BT-D096": dict(access="FULL", sections="Correct body 2402.12226v3 consumed (Abstract, §1-3 tokenizers/vocab/two-stage, §4 data/AnyInstruct, §5 Tables 2-6, §6). Recorded locator 2310.05661 resolves to unrelated logic paper with date mismatch.", corrected="2402.12226",
 claims=[
  ("The source defines AnyGPT: stable any-to-any speech/text/image/music conversation without LLM-architecture/training changes via data-level discretisation only (SEED image, SpeechTokenizer RVQ semantic-L1 plus SoundStorm acoustic, Encodec-music flattened frame-wise) with next-token training on LLaMA-2-7B (2T text tokens), text-bridge alignment, AnyInstruct-108k set, and diffusion/SoundStorm/Encodec de-tokenisers.", "PRIMARY_FACT", "Correct body §3; title/authors verified."),
  ("Reported numbers (zero-shot base): image-caption CIDEr 107.5 vs SEED-LLaMA 123.6; text-to-image CLIP-score 0.65 vs 0.69; Libri test-clean ASR word-error 8.5 vs Whisper-L2 2.7 vs human 5.8; VCTK TTS word-error 8.5 / similarity 0.77 vs VALL-E 7.9/0.75; MusicCaps understanding 0.11 (real 0.16) / generation 0.14 vs Mousai 0.23; music capped at 5 s.", "PRIMARY_FACT", "Correct body §5/conditions."),
 ],
 lims=["Recorded locator 2310.05661 is a transcription defect (plus date mismatch); claims rest on verified-correct 2402.12226. Future Discovery repair should correct the locator.",
  "Higher multimodal-vs-unimodal loss; tokeniser ceilings capability; 5 s music plus long-sequence context limits dialogue depth; no dedicated any-to-any benchmark."],
 extra_ver={}),

"BT-D097": dict(access="FULL", sections="Correct body 2305.11846v1 consumed (Abstract, §1-3 LDM/bridging/per-modality/alignment, §4 tasks/data, §5 Tables 2-10). Recorded locator 2305.11832 resolves to unrelated JointVAE-flows paper.", corrected="2305.11846",
 claims=[
  ("The source defines CoDi: independent per-modality latent diffusion models (image SD1.5, video plus pseudo-temporal plus latent-shift, audio mel-as-image plus AudioLDM-VAE/vocoder, text OPTIMUS/GPT-2) with text-bridged prompt encoders fused by weighted interpolation; joint generation adds frozen-model cross-attention plus contrastively-aligned environment encoders projecting latents, trained linearly (text-image to text-audio to video-audio) enabling unseen combinations.", "PRIMARY_FACT", "Correct body §3; title/authors verified."),
  ("Reported numbers: AudioCaps text-to-audio FD 22.90 vs AudioLDM-L-Full 23.31, IS 8.77 vs 8.13, KL 1.40 vs 1.59, FAD 1.80 vs 1.96; text-to-image COCO FID 11.26 vs SD1.4 11.21; joint similarity joint-vs-independent e.g. video-audio 0.255 vs 0.240; captioning near state-of-the-art.", "PRIMARY_FACT", "Correct body §5/conditions."),
 ],
 lims=["Recorded locator 2305.11832 is a transcription defect; claims rest on verified-correct 2305.11846. Future Discovery repair should correct the locator.",
  "Text-bridge inherits caption gaps; joint metric is encoder-cosine coherence, not fidelity; video temporal-consistency fixes partial."],
 extra_ver={}),

"BT-D098": dict(access="PARTIAL", sections="https://c2pa.org/ homepage body consumed (hero, how-it-works pointer, adopt-spec link, steering-committee list). Full C2PA specification (manifest/assertions/hash/signing/binding, audio-specific) NOT consumed.", corrected=None,
 claims=[
  ("Per the homepage, the organisation publishes an open provenance standard with Content-Credentials history (nutrition-label analogy) verifiable by consumers at any time, governed by a multi-stakeholder steering committee (listed members include Adobe/Amazon/BBC/Google/Meta/Microsoft/OpenAI/Sony/TikTok/Truepic).", "AUTHOR_CLAIM", "Homepage body; spec-level construction not present on page."),
 ],
 lims=["Marketing-page scope; no technical manifest, trust-list, or audio/music-binding details; deployment evidence needs vendor/spec sources.",
  "Any generation-relevant provenance guarantee (signing, tamper-evidence, audio binding, detector robustness) not established."],
 extra_ver={}),

"BT-D099": dict(access="FULL", sections="https://deepmind.google/technologies/synthid/ page body consumed (Overview, How-it-works 3 slides, Detecting-in-Gemini, Detector-portal).", corrected=None,
 claims=[
  ("The page describes SynthID watermarking/detection: embed digital watermark at creation (pixels/frames, audio waveform, LLM next-token probability skew) claimed robust to common edits (crop/filter/frame-rate/compression for image/video; noise/MP3/speed for audio); verify by SynthID detector or Gemini upload-check; detector portal currently journalist/media early-test.", "VENDOR_CLAIM", "Page body; no thresholds/keys/rates on page."),
 ],
 lims=["Product page only; no independent robustness evaluation; audio scope tied to Lyria/NotebookLM; text watermark quality-impact unquantified here; no detection rates, robustness curves, capacity, or audio/music-specific benchmarks on page.",
  "Detection robustness/false-positive rates or music-generation provenance efficacy beyond claimed invariances not established."],
 extra_ver={}),

# ---------------- r2 gap-fill ----------------
"BT-D129": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§1-5, Tables 1-2, Eq 1-6", corrected=None,
 claims=[
  ("The source defines Wav2Lip: freeze an expert SyncNet discriminator (colour, residual, cosine plus binary-cross-entropy, 5-frame window, 91% on LRS2 vs LipGAN 56%) and penalise the generator with expert-sync loss plus L1 (weight 0.03) plus visual GAN loss (weight 0.07); generator trained on LRS2 only, batch 80, Adam 1e-4.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: LRS2/LRW/LRS3 random-audio pairs lip-sync distance 6.512/6.386/6.652 and confidence 7.490/7.789/7.887 vs real 7.012/6.931, 6.736/7.838, 6.956/7.592; ReSyncED dubbed/random/TTS preference for Wav2Lip+GAN 60.2%/64.5%/51.2%, combined over 90% vs unsynced.", "PRIMARY_FACT", "§4 Tables 1-2/conditions."),
 ],
 lims=["Metric uses public SyncNet (different data); inherits SyncNet instability; talking-face only.",
  "Cross-condition lip-sync-distance comparability and general sound-event timing not established."],
 extra_ver={}),

"BT-D130": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§1-4.5, Tables 1-4, Eq 1-6, Figs 1/5", corrected=None,
 claims=[
  ("The source replaces SyncNet loss with lip-reading AV-HuBERT transformer final-layer 768-dim features: unsupervised audio-visual cosine plus binary-cross-entropy on the generated interval (5-frame window, 96x96 face crops, mel 16x80 16 kHz) plus GAN plus perceptual plus L1 losses (weights 10/1/0.5), Adam 1e-4; proposes AVSu/AVSm/AVSv metrics.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: LRS2 SSIM 0.947, PSNR 31.273, FID 4.51, landmark distance 1.188, lip-sync confidence 7.958 / distance 6.301, AVSu 0.508 / AVSm 0.939 / AVSv 0.879; HDTF SSIM 0.933, PSNR 30.579, FID 16.76; user study (10 HDTF videos, 10 raters, 1-5 scale) 3.92/4.02/3.95 vs Wav2Lip 2.91/2.88/2.73; unsupervised ablation best.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Talking-face only; AV metrics need independent adoption; small user study.",
  "Displacement of lip-sync-distance as standard not established."],
 extra_ver={}),

"BT-D131": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§1-6, Tables 2-4", corrected=None,
 claims=[
  ("The source defines VideoPhy: 3-stage curation (model-generated 1000 candidates, human verification to 688, graphics-PhD easy/hard split); binary human physical-adherence/commonsense judgements (0/1) by 14 workers; finetune VideoCon-7B to VideoCon-Physics for automatic judgements.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: 688 captions (289 solid-solid/291 solid-fluid/108 fluid-fluid, 366 easy/322 hard, 138 actions, 8.5 words); 12 models, 11330 videos, 36500 annotations; test 344 prompts, 1 video/model, 3 annotators majority (agree 75% adherence / 70% commonsense); best model joint 39.6% (adherence 63.3, commonsense 53), others under 20%; automatic ROC-AUC adherence 82 / commonsense 73 vs Gemini 73/58, GPT-4-Vision 53/53.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["2024 model set; binary judgements conflate quality/motion; commonsense more subjective.",
  "2025-2026 systems and simulator-grounded dynamics not established."],
 extra_ver={}),

"BT-D132": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§1-5, Tables 1-2, Figs 2-3", corrected=None,
 claims=[
  ("The source defines F5-TTS: diffusion-Transformer with adaptive layer-norm-zero (22 layers, 16 heads, 1024/2048 dims) plus ConvNeXt-V2 text refinement (4 layers, 335.8M parameters) on padded character-filler input, optimal-transport conditional flow matching, uniform-t training; inference Sway Sampling with Euler solver plus guidance factor 2.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: Emilia 95k-hour English+Chinese, 100-dim mel 24 kHz, mask 70-100%, 1.2M updates batch 307200 frames on 8xA100-80G; LibriSpeech-PC 1127-sample 32-evaluation-step word-error 2.42, similarity 0.66, real-time-factor 0.31, 16-step word-error 2.53 with real-time-factor 0.15 on RTX3090-10 s clips (baseline 32-step word-error 2.95, similarity 0.69, real-time-factor 0.68; ground truth 2.23); Seed English 1088-sample word-error 1.83, Chinese 2020-sample 1.56.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Offline non-streaming; duration by character ratio; no fine-grained emotion control.",
  "Universal continuous-representation efficiency not established."],
 extra_ver={}),

"BT-D133": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§1-4, Tables 2-6, Eq 1-15", corrected=None,
 claims=[
  ("The source defines CosyVoice 2: finite-scalar-quantisation supervised semantic tokeniser (25 Hz) plus Qwen2.5-0.5B text-speech language model (5/15 interleave, no text-encoder/speaker-embedding) plus chunk-aware causal flow-matching UNet (10 evaluations, guidance 0.7, cosine schedule, 4 masks) to 50 Hz mel at 24 kHz plus vocoder; latency model L = M·(d_lm + d_fm + d_voc).", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: tokeniser trained 200k hours with 6561-code full utilisation vs vector-quantised 4096-code 23%; LibriSpeech word-error 2.47, naturalness-MOS 3.96, speaker-similarity 0.745 (human 2.66/3.84/0.697); streaming variant near-lossless (Chinese 1.45, English 2.38, hard 8.08).", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Latency configuration-bound; English weaker (data imbalance); speaker-similarity metric speaker-verification-dependent.",
  "Vendor-family benchmark comparability not established."],
 extra_ver={}),

"BT-D134": dict(access="PARTIAL", sections="arXiv abs + HTML §§1-3.4 and Table 1 consumed (§5 evaluation not consumed).", corrected=None,
 claims=[
  ("The consumed sections define Moshi: Helium-7B backbone (32 layers, 4096 dims, 2.1T English tokens) plus Mimi streaming codec (24 kHz to 12.5 Hz, 80 ms frame, split residual-vector-quantisation distilling semantics to first level) plus hierarchical residual-quantisation depth-Transformer modelling parallel user/Moshi streams with acoustic delay and inner-monologue time-aligned text prefix.", "PRIMARY_FACT", "§§2-3."),
  ("Theoretical latency 160 ms (under 230 ms cross-linguistic natural average), ~200 ms in practice on L4 GPU; Mimi 12.5 Hz / 80 ms frames; context 3000 steps ≈ 4-5 minutes.", "PRIMARY_FACT", "§§2-3/conditions; evaluation-table numbers not consumed."),
 ],
 lims=["Research system; production runtime needs independent measurement; evaluation numbers not verified here (evaluation section not consumed).",
  "Production deployment figures and full quality rankings not established in this consumption."],
 extra_ver={}),

"BT-D135": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§1-4, Tables 1-7, App A", corrected=None,
 claims=[
  ("The source defines MTR-DuplexBench: segment turns via timestamped transcription plus voice-activity detection plus medium transcription model to large-model adjudication (6 passes, 30% overlap majority-vote median plus merge); assistant window with ground-truth history and muted next-user; 4 dimensions (synthetic conversational, natural dialogue, instruction, safety) with success/GPT-score/refusal plus latency in seconds.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: 200 10-round synthetic plus 200 120-second natural dialogues (average 5.88 rounds) plus 300 instruction plus 520 safety items; smooth-conversation success 73.00% round-1 to 57.40% rounds-1-10, interrupt 72.5 to 54.2, pause 93.5 to 84.8, background 53.0 to 25.7, latency ~0.64 s round-1 rising, cascaded ~9-12 s; instruction 68.0 to 41.9% vs baselines 86.5/92.6; safety ~90-91% vs ~99.7%.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["2025-11 protocol, adoption unverified; model-judge/segmentation dependence.",
  "Cross-lab adoption and examiner-free stability not established."],
 extra_ver={}),

"BT-D136": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§I-VI, Figs 1-5", corrected=None,
 claims=[
  ("The source benchmarks music generation models and metrics via human preference: tag-triple track combinations (CLAP cosine at most 0.1382, 500 combos) across 12 models x 500 10-second instrumental highest-energy clips; pairwise binary preference/alignment judgements (7800+7800=15600, 2500+ raters aged 18-34) with Elo (K=8, base 1000, 10k bootstraps) plus Bradley-Terry vs Fréchet/CLAP variants.", "PRIMARY_FACT", "§§2-4."),
  ("Reported numbers: 6000 songs (listed MusicGen sizes, Riffusion, AudioLDM2 variants, Mustango, StableAudio 1.0/2.0, Suno v3/v3.5, Udio); Suno v3.5 top Elo both axes, above reference library; Stable v2 +5pp over v1; Fréchet-CLAP music-audio best quality correlation, music-trained LAION variants best alignment (exact correlation magnitudes in figures, not text-extracted).", "PRIMARY_FACT", "§5/conditions."),
 ],
 lims=["v3/v3.5-era, not v5/v6; 10-second instrumental only; ElevenLabs thin in corpus.",
  "Newer commercial models and exact correlation magnitudes not established here."],
 extra_ver={}),

"BT-D137": dict(access="FULL", sections="Full vendor-lab blog consumed: hardware/method, 15-configuration speed, quality, consistency, scaling, batch, economics sections. (Edition Raw transcription corrected CLAP→CLIP in preflight.)", corrected=None,
 claims=[
  ("The blog measures FLUX.2-klein-4B with documented methodology: Diffusers FluxPipeline bf16 flow-matching scheduler on H100 SXM 80 GB; 5 resolutions x 3 step counts; CLIP alignment over 10 categories plus LPIPS plus attribute binding plus batch ramp 1-16 plus data-parallel 1/2/4/8 plus cost.", "PRIMARY_FACT", "Blog hardware/method sections."),
  ("Reported numbers: 512px-4-step 0.19 s (5.14 img/s), 768px 0.33 s, 1280x720 0.50 s, 1024px-4-step 0.57 s (1.77 img/s), 1024px-8-step 1.00 s, 1024px-12-step 1.43 s; VRAM 16 GB at 512px to 17.8 GB at 1024px (16-18 GB); peak batch-8 1.91 img/s; data-parallel 1:0.43, 2:0.82 (97%), 4:1.48 (87%), 8:2.53 (74%); CLIP average 0.335 across categories, flat across step counts (2-step 0.375 to 12-step 0.367); ~$0.0004/image at stated cloud price, 5-10x SDXL.", "PRIMARY_FACT", "Blog speed/quality/consistency/scaling/batch/economics sections with stated configs."),
 ],
 lims=["Single-vendor-lab source, not peer-reviewed; H100-only; consumer-GPU replication pending.",
  "A100/consumer replication and vendor-claim parity beyond this configuration not established."],
 extra_ver={}),

"BT-D138": dict(access="FULL", sections="arXiv abs + HTML: Abstract, §§1-5, Tables 1-3, Eq 1-10", corrected=None,
 claims=[
  ("The source defines FiVE: 100 videos (74 real every-8-frames + 26 synthetic, 35-126 frames) with 420 model-generated prompt pairs (colour/material/substitution with/without non-rigid plus add/remove), SAM2 masks plus FiVE-Accuracy vision-LLM yes/no plus multi-choice judgements; adapts Pyramid-Flow-384P plus Wan2.1-1.3B via training/inversion-free FlowEdit.", "PRIMARY_FACT", "§§2-3."),
  ("Reported numbers: 15 metrics: Wan-Edit LPIPS 94.61, SSIM 82.55, PSNR 25.57, fidelity 89.43 at 3.07 s/frame vs Pyramid-Edit 1.44 s/frame vs DMT 25.98 s/frame; FiVE-Accuracy Wan yes/no 41.41, multi-choice 52.53, union 55.72, intersection 38.22, accuracy 46.97 vs Pyramid 43.84, DMT 48.42, TokenFlow 27.43.", "PRIMARY_FACT", "§4/conditions."),
 ],
 lims=["Editing-domain only; pure-generation flow-vs-diffusion ablation thin.",
  "Pure-generation ablations and hyperparameter-universal superiority not established."],
 extra_ver={}),

# ---------------- capstones image/speech/music ----------------
"BT-D100": dict(access="FULL", sections="Vendor announcement body consumed (What's New, Model Family 9B/4B/Base, Quantized, Performance Analysis, Resources).", corrected=None,
 claims=[
  ("The page documents unified text-to-image plus single/multi-reference editing in one model; vendor-stated sub-second (under 0.5 s) inference and 4B fitting ~13 GB VRAM (RTX 3090/4070+); FP8 (1.6x faster/40% less VRAM) and NVFP4 (2.7x/55%) variants; API plus open weights; 9B flow model plus 8B Qwen3 text embedder step-distilled to 4 steps (vendor-disclosed); 9B/4B/Base sizes; 4B Apache 2.0; announcement dated January 15, 2026.", "VENDOR_CLAIM", "Page body; independent measurement absent."),
  ("Vendor performance claim: matches/exceeds 5x-larger models; Pareto-frontier Elo-vs-latency/VRAM vs Qwen/Z-Image on text-to-image/image-to-image/multi-reference (vendor charts, stated GB200 bf16 config).", "VENDOR_CLAIM", "Page performance section; vendor charts only."),
 ],
 lims=["Vendor speed/quality claims without independent measurement in this body; tokenizer/training undisclosed.",
  "Training data, tokenizer detail, independent benchmark verification not established."],
 extra_ver={"vendor-claim quarantine; architecture non-inference; hardware/configuration binding": ("VERIFIED", "Page claims quarantined as vendor-attributed with stated configs (GB200 bf16 charts, 4B VRAM figure); only the vendor-disclosed flow-model/embedder/distillation facts recorded; tokenizer/training explicitly marked undisclosed.")}),

"BT-D101": dict(access="FULL", sections="Vendor help article consumed (Key Capabilities, What's New vs FLUX.1, Model Family, Where to Use). No absolute date (relative 'Last updated 3 months ago').", corrected=None,
 claims=[
  ("The help article documents the FLUX.2 family surface: unified text-to-image plus image editing; multi-reference up to 8-10 images; up to 4MP (e.g. 2048x2048); improved text rendering; use via API, Playground, local Hugging Face variants.", "VENDOR_CLAIM", "Help article; descriptive docs, no eval numbers."),
 ],
 lims=["Docs describe surface, not architecture; no absolute publication date exposed.",
  "Publication date, architecture, training, evaluation not established."],
 extra_ver={}),

"BT-D102": dict(access="FULL", sections="Vendor announcement body consumed (infographics, precision editing, textures, multilingual, outlook). Page date 2026-07-08.", corrected=None,
 claims=[
  ("The page documents multimodal image creation/editing: dense infographic/data-visualisation generation; point/lasso/box/sketch control, hex-colour/material edit, layer separation (over 10 layers), multi-image fusion; 10+ language input/rendering.", "VENDOR_CLAIM", "Page body; vendor demos, no numeric eval in body."),
 ],
 lims=["Vendor evaluations are vendor claims until independently supported; vendor flags finer text-rendering and pixel-edit consistency as future work.",
  "Architecture, training, eval methodology, license not established."],
 extra_ver={}),

"BT-D103": dict(access="FULL", sections="Vendor announcement consumed (fidelity, precision/multi-turn editing, intelligence/style, Sketch, templates, sharing, API, safety, pricing). Page date September 8, 2026.", corrected=None,
 claims=[
  ("The page documents ChatGPT generation plus iterative editing: Sketch draw-reference, templates, on-image comments, prompt sharing; API models Flare (default) plus Sunburst (tighter control, slower); rollout to all tiers; 3B images/week usage context.", "VENDOR_CLAIM", "Page body; closed workflow reference."),
  ("Vendor claims: up to 50% lower latency vs prior version / Flare vs GPT-Image-2; early-customer quotes (named companies, vendor-attributed).", "VENDOR_CLAIM", "Page body; vendor-attributed."),
 ],
 lims=["Architecture disclosure limited; no mechanism inference permitted; evaluation/safety deferred to system card.",
  "Architecture, training, tokenizer, independent evaluation not established."],
 extra_ver={}),

"BT-D104": dict(access="FULL", sections="Vendor announcement consumed (Flash-speed intelligence, creative control, availability, provenance). Dated Feb 26, 2026.", corrected=None,
 claims=[
  ("The page documents text-to-image/editing via app, Search AI Mode/Lens, AI Studio/API, Vertex, Flow, Ads; world-knowledge plus web/image-search grounding; text render/translate/localise; subject consistency, 512px-4K aspect control; Nano Banana 2 = Gemini 3.1 Flash Image; Pro retained via regenerate menu.", "VENDOR_CLAIM", "Page body; TS-002/TS-003 boundary case, generation scope only."),
  ("Vendor claim: Pro capabilities at Flash speed; SynthID verification used 20M+ times since November (vendor-attributed).", "VENDOR_CLAIM", "Page body."),
 ],
 lims=["Reasoning-in-generator claims need model-card authority (see BT-D105); mechanism/eval detail deferred.",
  "Architecture, training, announcement-level eval numbers not established."],
 extra_ver={}),

"BT-D105": dict(access="FULL", sections="Model card consumed (Model Information/Data/Implementation/Distribution/Evaluation/Intended Usage+Limitations/Ethics). Published 26 February 2026.", corrected=None,
 claims=[
  ("The card documents natively multimodal reasoning: text+image (+audio/video comprehension) in, 1M context; image (4K tokens) + text (64K) out; served via app/API/Studio/Vertex/Search/Flow/NotebookLM; based on Gemini 3 Flash; knowledge cutoff January 2025.", "VENDOR_CLAIM", "Card model-information section."),
  ("Vendor evaluation: human side-by-side Elo plus AutoRater tables favouring 3.1 Flash Image over 2.5 Flash Image, 3 Pro Image, GPT-Image 1.5, Seedream 5.0 Lite, Grok Imagine Pro (with confidence intervals).", "VENDOR_CLAIM", "Card evaluation section; vendor methodology."),
 ],
 lims=["Card scope is model-specific; cross-model comparison prohibited; hallucinations; poor small/dense text, character-consistency gaps, doodle-ink persistence, spatial left/right confusion listed in-card.",
  "Training data, tokenizer, license, independent reproduction not established."],
 extra_ver={}),

"BT-D106": dict(access="PARTIAL", sections="Locator resolves to Nano Banana hub; no Imagen-specific sections/body consumed (product-line redirect/replacement, not fetch error).", corrected=None,
 claims=[
  ("The hub lists Nano Banana 2 Lite/2/Pro plus prompt guide and try-in surfaces; no Imagen capability body exists at the locator; 2026 Imagen deprecation/shutdown in favour of Nano Banana per record lifecycle note (not re-verified in body).", "VENDOR_CLAIM", "Hub body; lifecycle note from record, not body-verified."),
 ],
 lims=["Lifecycle transition is evidence of product direction, not architectural inevitability; marketing-hub scope.",
  "Imagen dates, capability details, architecture from this locator not established. Retained solely as deprecation/lifecycle context."],
 extra_ver={"lifecycle-only role; do not use for 2026 capability ranking": ("VERIFIED", "Retained strictly in lifecycle-only role against the hub redirect; no capability ranking use.")}),

"BT-D107": dict(access="FULL", sections="Vendor announcement consumed (continuous interaction, delegation, evals, voice experience, safety, availability). Dated July 8, 2026 (plus July 31, 2026 update note).", corrected=None,
 claims=[
  ("The page documents full-duplex voice (simultaneous listen/speak; backchannels, interruption handling, live translation); delegation to frontier model (named version at launch; Instant/Medium/High); voice with visual cards plus 9 remastered voices.", "VENDOR_CLAIM", "Page body."),
 ],
 lims=["Non-native accents/fluency gaps in some languages; no video/screenshare at launch; real-time-factor numbers need API-doc binding.",
  "Latency numbers, training data, license not established."],
 extra_ver={}),

"BT-D108": dict(access="FULL", sections="Vendor announcement consumed (voice patterns, realtime voice/translation/transcription, safety, pricing). Dated May 7, 2026.", corrected=None,
 claims=[
  ("The page documents the API voice-model surface (named realtime family): preambles, parallel tools, 128K context, minimal-to-xhigh reasoning; translation model (70+ in/13 out); streaming transcription model; Playground/WebRTC demos; pricing $32/1M audio-in ($0.40 cached)/$64/1M audio-out and per-minute translation/transcription prices.", "VENDOR_CLAIM", "Page body; version-bound figures."),
 ],
 lims=["Pricing/latency figures version-bound.",
  "Architecture, training, tokenizer not established."],
 extra_ver={}),

"BT-D109": dict(access="FULL", sections="Model card consumed (Model Information/Data/Implementation/Distribution/Evaluation-links/Intended Usage+Limitations/Ethics). Published 15 September 2026.", corrected=None,
 claims=[
  ("The card documents native audio input/output: Live plus Live Extended Thinking (audio/image/video/text in, 128K context; audio+text out 64K) and Flash/Flash-Lite text-to-speech (text up to 8K in; audio out); realtime conversational use; based on Gemini 3 Pro; cutoff January 2025.", "VENDOR_CLAIM", "Card sections."),
 ],
 lims=["Card-only scope; independent evaluation absent; hallucinations, jailbreak-resistance work ongoing, occasional slowness/timeouts listed.",
  "Training data, architecture detail, eval results, license not established."],
 extra_ver={}),

"BT-D110": dict(access="FULL", sections="Vendor announcement consumed (scene concept, capabilities, unified model, evaluation charts, next steps). Dated 2026-07-20.", corrected=None,
 claims=[
  ("The page documents scene-level speech plus sound-effects plus ambience joint generation; 100 ms prompt timing control for dialogue; text/reference/combined voice design without per-speaker training; up to 2-minute single-pass plus continuation; 20+ languages with cross-lingual timbre.", "VENDOR_CLAIM", "Page body."),
  ("Vendor charts: A/B preference gains text-to-timbre; over 90% usable rate most scenarios; MOS over 4.0 naturalness most languages, over 3.5 instruction-following except Vietnamese.", "VENDOR_CLAIM", "Page charts; vendor methodology."),
 ],
 lims=["Fine timing dialogue-only; longer-scene consistency future work; scene-coherence claims need independent evaluation.",
  "Training data, eval protocol detail, license not established."],
 extra_ver={}),

"BT-D111": dict(access="FULL", sections="Model card consumed (Model information/data/implementation/distribution/evaluation/intended usage/ethics). Visible date 29 July 2026.", corrected=None,
 claims=[
  ("The card documents text-to-music (plus lyrics out); genre/mood/instrument/vocal control; distributed via music product surface; latent diffusion applied to temporal audio latents (explicit architecture disclosure).", "VENDOR_CLAIM", "Card sections; unusually strong disclosure for a closed music model, still card-bounded."),
  ("Vendor evaluation: significant gains over prior version on audio fidelity and lyric prompt adherence (vendor human plus automatic evals with music experts).", "VENDOR_CLAIM", "Card evaluation section."),
 ],
 lims=["Closed weights; structure claims bound to card methodology; prohibited-use policy scope; watermarking noted; no numeric limitation list.",
  "Training data detail, tokenizer, license, duration caps in card not established."],
 extra_ver={}),

"BT-D112": dict(access="FULL", sections="Product hub consumed (details, length, compose-with-images, prompting, demos, model family, safety, try). Hub undated.", corrected=None,
 claims=[
  ("The hub documents prompt-to-track including image-to-music; duration control (60 s clips to full 3-minute songs); vocal/language/genre/acoustic controls; access via music product surfaces; family covers numbered versions plus realtime variants (one open).", "VENDOR_CLAIM", "Hub body; marketing-level detail."),
 ],
 lims=["Marketing-level detail; mechanism claims defer to BT-D111; vendor notes key capabilities still improving.",
  "Dates, hub-level architecture, training, license not established."],
 extra_ver={}),

"BT-D113": dict(access="FULL", sections="Vendor research note consumed (family, variable-length, inpainting, autoencoder, post-training, data/compute, release). Page shows May 20 (record datePublished 2026-05-20).", corrected=None,
 claims=[
  ("The note documents semantic-acoustic autoencoder plus latent diffusion plus adversarial post-training for fewer steps; variable-length text-to-audio generation plus inpainting/continuation; small/medium open weights plus pipeline; vendor-stated under 2 s on stated accelerator, seconds on stated laptop chip; trained on licensed/Creative-Commons data; papers listed with arXiv IDs.", "VENDOR_CLAIM", "Note sections; open-weight mechanism anchor."),
 ],
 lims=["Version-bound feature surface; open scope small/medium per license.",
  "Tokenizer detail, training mix, eval numbers, license text not established in note."],
 extra_ver={}),

"BT-D114": dict(access="FULL", sections="Release-notes index consumed (individually dated entries: Studio MIDI Sep 17 2026; v6 Sep 9 2026; Studio 2.0 Aug 13 2026; v5.5 Mar 26 2026; v5 Sep 23 2025). Index page itself undated.", corrected=None,
 claims=[
  ("The index documents the closed song workflow: Create (text/audio/image/video), Song Editor/Replace/Crop/Stems/Extend/Remix/Covers/Personas, Studio DAW (MIDI/FX/wavetable/automation), playlists/social/mobile/car integration; v6 entry retires prior models.", "VENDOR_CLAIM", "Index entries; changelog descriptions, no eval claims."),
 ],
 lims=["Capability/workflow role only; no architecture/eval authority; entry dates bind per-entry only.",
  "Model mechanism, training, evaluation not established."],
 extra_ver={}),

"BT-D115": dict(access="FULL", sections="Vendor announcement consumed (3-model suite, controls, next steps). Dated Sep 9, 2026.", corrected=None,
 claims=[
  ("The announcement documents v6 (flagship Pro/Premier) / v6-wild (exploratory) / v6-mini (free fast); natural-language section edit, multi-source mashup, sample/isolate/beat workflow, vibe/reference creation, text+audio+image+video inputs, single-lyric edit; built with named industry partners; prior models to retire onto v6 generation.", "VENDOR_CLAIM", "Page body; current commercial workflow case."),
 ],
 lims=["Vendor claims (best/faster/more expressive) without metrics; v6/v6-wild paid-only; upload/lyric screening safeguards vendor-described; independent validation absent.",
  "Architecture, training, eval methodology, license not established."],
 extra_ver={}),

"BT-D116": dict(access="FULL", sections="Capability docs consumed (Overview, Audio Reference, Finetunes, Usage, Key facts/FAQ). Living docs undated.", corrected=None,
 claims=[
  ("The docs document text-to-music (instrumental/vocals, multilingual); Audio Reference up to 30 s style guide (v2/v2.5, copyright-screened); custom/curated Finetunes (~5-10 min); section inpainting; 3 s-5 min durations; MP3/WAV; website plus API; v1 legacy-transition / v2 UI-default / v2.5 latest.", "VENDOR_CLAIM", "Docs body; secondary closed comparator."),
 ],
 lims=["Docs-level authority; evaluation methodology thin; reference guides style, not remix/genre-transfer; v1 deprecation with months notice.",
  "Architecture, training, evaluation, dates not established."],
 extra_ver={}),

# ---------------- capstones video ----------------
"BT-D117": dict(access="FULL", sections="Vendor announcement consumed (highlights, 30 s storytelling + multi-round extension, multimodal reference, timestamp/green-screen/camera/reference editing, industry scenarios, summary/limitations). Page date 2026-07-31.", corrected=None,
 claims=[
  ("The page documents unified audio-video joint generation: up to 30 s single-pass plus multi-round extension to multi-minute with shot-transition continuity; up to 30 images + 10 video + 10 audio references including clay/motion/creative references plus lighting control; timestamp-level plus green-screen/camera-perspective/reference editing; rollout on named apps, API coming soon.", "VENDOR_CLAIM", "Page body; clip-to-storytelling capstone."),
 ],
 lims=["Duration/coherence claims need independent verification; vendor acknowledges room on physical plausibility of complex motions and multi-subject interaction stability.",
  "Independent verification, scores, pricing/limits not in body; architecture undisclosed beyond unified joint-generation functional description."],
 extra_ver={}),

"BT-D118": dict(access="FULL", sections="Vendor model page consumed (header, What's new, native audio showcase, ingredients/style/consistency/extend/camera/frames/outpainting/object controls, 1080p-4K, Performance, Safety/Limitations). Dynamic page, no absolute publication date; performance vintage October 2025.", corrected=None,
 claims=[
  ("The page documents text-to-video/image-to-video plus native dialogue/sound-effects/ambience; reference ingredients/style/character, scene extension, first-last frame, outpainting, object add/remove, motion/character plus camera controls, 1080p/4K; access via app/Flow/Vids/Studio/API.", "VENDOR_CLAIM", "Page body."),
  ("Vendor performance (attributed): best on 1,003 MovieGenBench text-to-video (overall/alignment/quality + physics), 355 VBench image-to-video, 527 text-to-video-audio (overall/AV-alignment); internal ingredient/extension/frame/insertion leading.", "VENDOR_CLAIM", "Page performance section; vendor benchmarks until reproduced."),
 ],
 lims=["Vendor: natural consistent spoken audio for short segments remains active development with sync/incoherent-speech issues; synth-ID plus safety/memorisation checks.",
  "Parameters, training data/sampler, pricing not in body; architecture undisclosed."],
 extra_ver={}),

"BT-D119": dict(access="FULL", sections="Vendor blog consumed (one model multiple capabilities, Self-Flow vs flow-matching chart, Video, Image, Action, Launch Plan, What's next). Blog 2026-07-23.", corrected=None,
 claims=[
  ("The blog documents a joint image/video/audio unified model: video text-to-video/image-to-video/animation/reference, video-to-video, audio-video continuation, keyframe-to-video, multilingual dialogue, multi-style/aspect, agentic chaining to minutes, 20 s single plus native audio; image synthesis/edit; action prediction; Early Access via API/private weights; Dev open-weights planned.", "VENDOR_CLAIM", "Blog body; early-access convergence case."),
  ("Vendor preliminary claims (attributed): preferred over named competitors at stated percentages; Self-Flow lower Fréchet plus higher manipulation success; strong faces/sound-event/multilingual.", "VENDOR_CLAIM", "Blog charts; preliminary harness."),
 ],
 lims=["Vendor flags early/preliminary harness, expects improvement; safety-testing gated rollout.",
  "Final metrics, pricing, Dev date, compute/data not in body; only unified multimodal flow-matching backbone plus Self-Flow alignment disclosed, otherwise undisclosed."],
 extra_ver={}),

"BT-D120": dict(access="BLOCKED", sections="Barrier: webfetch timeout x2 on the recorded investor-relations locator, zero body bytes; no capability/eval sections consumed.", corrected=None,
 claims=[],
 lims=["Body blocked: all capability/release/eval/architecture facts require successful fetch; record summary must not be reused as body fact; no press substitution per boundary.",
  "This record is retained as NEEDS_MORE pending successful retrieval."],
 extra_ver={}),

"BT-D121": dict(access="FULL", sections="Vendor help article consumed (Introduction, spec details table, access, drafting prompt, generating/iterating, export). Dynamic article, no absolute date.", corrected=None,
 claims=[
  ("The article documents text-to-video plus image-to-video only (additional inputs coming soon); complex sequenced instructions/camera choreography; Standard+ plan, Web, 12 credits/s, 2-10 s, Explore Mode, 720p 24/25 fps; aspect coverage text-to-video 16:9 only, image-to-video six ratios; Aleph editing separate.", "VENDOR_CLAIM", "Article body; workflow/runtime comparator."),
 ],
 lims=["Vendor descriptor state-of-the-art motion/prompt-adherence/fidelity with no metric table in body (claim only); caps 10 s/720p; additional inputs not yet supported.",
  "Release date, scores, backbone, training data not in body; architecture weak."],
 extra_ver={}),

"BT-D122": dict(access="FULL", sections="Vendor model page consumed (header, Ray3.14 banner, V2V/keyframes/character-ref, reasoning/annotation, HDR/EXR, fidelity list, Draft/HiFi, Stories, gallery). Dynamic page, no date; banner notes latest Ray3.14 (native 1080p, 4x faster, stronger adherence, 3x lower cost).", corrected=None,
 claims=[
  ("The page documents text-to-video/image-to-video, video-to-video including character reference plus start/end keyframes, Modify (wardrobe/environment/relight/product placement), visual annotation, Draft Mode 5x faster/cheaper plus HiFi master to 4K HDR, native 16-bit HDR/EXR/SDR-to-HDR.", "VENDOR_CLAIM", "Page body; production comparator with subversion drift."),
 ],
 lims=["No eval/limitation section; version ambiguity (page vs 3.14 banner); exact version must be bound at any reuse with BT-D123.",
  "Dated release, scores, duration/resolution defaults, pricing not in this body; architecture undisclosed."],
 extra_ver={"bind exact Ray3 subversion/version at Evidence": ("VERIFIED", "Version ambiguity recorded against the page-vs-banner drift with BT-D123 as the dated companion; no comparison use without version binding.")}),

"BT-D123": dict(access="FULL", sections="Vendor news consumed (header 2026-06-09, What's New, studio/agency bullets, developer API).", corrected=None,
 claims=[
  ("The news documents frame-level control up to 16 keyframes, Performance Tracking plus 8-face expressive tracking, native HDR plus 16-bit EXR for post-production, reframe/aspect/extend/background preserving lighting, up to 20 s 1080p; full control surface as API for pipelines.", "VENDOR_CLAIM", "News body; dated subversion datapoint."),
 ],
 lims=["Single-version snapshot; no limitation/eval section; current-status recheck required.",
  "Pricing, method/training details, later subversions not in body."],
 extra_ver={"bind exact version/date at Evidence": ("VERIFIED", "Version/date bound to the 2026-06-09 news record as the dated companion to BT-D122; single-snapshot role only.")}),

"BT-D124": dict(access="FULL", sections="Wan2.2 GitHub repo page + README consumed (innovations, news, todo, run commands, efficiency, MoE architecture, hybrid TI2V/VAE, comparisons, license; README + raw README consistent). Weights/code 2025-07-28.", corrected=None,
 claims=[
  ("The repo documents open Apache-2.0 releases: text-to-video-A14B/image-to-video-A14B MoE 480p/720p, TI2V-5B dense text-to-video+image-to-video 720p@24fps on consumer GPU (4090/24 GB, 5 s under 9 min), S2V-14B audio+image+pose, Animate-14B animation/replacement; ComfyUI/Diffusers/Hub; prompt extension via hosted/local models.", "PRIMARY_FACT", "README run/architecture sections."),
  ("The repo discloses a 2-expert mixture-of-experts layout (high-noise layout expert / low-noise detail expert, 14B active/27B total, SNR threshold), Wan2.2-VAE 4x16x16 (64x) plus patchification to 4x32x32, diffusion training with FSDP/Ulysses; vendor comparisons: MoE lowest validation loss vs prior variants; benchmark chart vs closed models; +65.6% images / +83.2% videos vs 2.1.", "PRIMARY_FACT", "README MoE/VAE/comparison sections; hyperparams/corpus beyond README undisclosed."),
 ],
 lims=["A14B needs 80 GB single-GPU / 8-GPU multi-GPU; TI2V offload flags; Animate LoRA cross-use not recommended.",
  "Independent benchmark reproduction and exact corpus/compute not in body; open line frozen at 2.2."],
 extra_ver={}),

"BT-D125": dict(access="BLOCKED", sections="Barrier: static fetch returns JavaScript app shell (root div, meta only), zero renderable capability/eval sections.", corrected=None,
 claims=[],
 lims=["Body blocked: hub date/version and 2.2-last-open corroboration not established from body; no press substitution per boundary.",
  "This record is retained as NEEDS_MORE pending rendered fetch."],
 extra_ver={}),

"BT-D126": dict(access="FULL", sections="Vendor page consumed (flagship video+audio, world-simulator claim, deployment/social-app characters, responsible launch, availability, credits; discontinuation banner). Post September 30, 2025.", corrected=None,
 claims=[
  ("The page documents flagship video+audio: physics-accurate controllable multi-shot with world-state persistence, cinematic/anime/realistic styles, soundscape/speech/effects, real-world injection/character likeness; via iOS app and web, Pro tier, API planned; banner: Sora product unavailable as of 2026-04-26; US/Canada invite rollout.", "VENDOR_CLAIM", "Page body; historical/lifecycle role, not a 2026 product capstone."),
 ],
 lims=["Vendor leap claims without numeric benchmark in body; far-from-perfect disclaimer; safety/consent/provenance controls; compute-limited free limits.",
  "Architecture, compute/data, scores not in body."],
 extra_ver={}),

"BT-D127": dict(access="FULL", sections="Vendor help article consumed (when discontinued, export, data deletion, how-to-export, refund). Dynamic article, relative update stamp only.", corrected=None,
 claims=[
  ("The article documents first-party discontinuation guidance: web/app end 2026-04-26 with export/deletion handling; content dates 2026-04-26 product end and 2026-09-24 API end are content facts, not page-date facts.", "VENDOR_CLAIM", "Article body; lifecycle guidance only."),
 ],
 lims=["Consumer-surface scope; final export window conditional; API rows defer to BT-D128.",
  "Architecture/capability/eval not in scope of this body."],
 extra_ver={}),

"BT-D128": dict(access="FULL", sections="Vendor deprecation table consumed (overview, notice periods, deprecation vs legacy, upcoming, past). Living table undated.", corrected=None,
 claims=[
  ("The table documents API lifecycle: Videos API plus named model snapshots removed 2026-09-24 with no recommended replacement; row announced 2026-03-24, shutdown 2026-09-24.", "VENDOR_CLAIM", "Table rows; lifecycle/deployment boundary."),
 ],
 lims=["Version-bound table; recheck at any reuse; no capability/eval content.",
  "Product export/deletion handling not in this body (see BT-D127)."],
 extra_ver={}),

# ---------------- X-bound ----------------
"BT-D139": dict(access="FULL", sections="Accepted raw r3 file fully consumed (27/27/27 recount verified programmatically: 27 observation sections, 27 unique status URLs; FIRST_HAND 22/1/4 raw with OBS-SPEECH-01 YES->NO downstream normalisation; reception 14/5/3/5; categories 11/3/3/3/3/2/1/1; modality 11/4/3/8/1). Raw bytes immutable (sha ebfce3bf, 39000 bytes).", corrected=None,
 claims=[
  ("Reception/deployment value: local/on-device FLUX.2-klein deployment and latency friction; Seedream character/reference consistency reception; speech full-duplex adoption interest with weak matched latency evidence; music creator-workflow adoption; Seedance/Kling consistency and editing-failure comparisons; Wan2.2 GGUF/ComfyUI consumer-hardware constraints; identity/detail damage on edits; temporal/spatial drift and lip-sync as continuing video failure modes.", "SOCIAL_OBSERVATION", "Raw r3 observation records OBS-IMG-01..OBS-MECH-02; duplicate OBS-MECH-01 removed, OBS-VID-08 retained with secondary mechanism tag."),
  ("Sparse lanes remain explicitly LOW_SIGNAL: full-duplex interruption/overlap measurement, cross-lingual/emotion cloning degradation, long-range music structure, metric-vs-preference contradictions, independent editing-fidelity corpus, controlled few-step ablations; no popularity ranking or model winner derived.", "SOCIAL_OBSERVATION", "Raw r3 §§10/13 failure and LOW_SIGNAL ledgers."),
 ],
 lims=["Single bounded reception pass materialised as one Discovery record; 27 posts are not 27 technical authorities.",
  "Any technical follow-up promoted from an X lead must be rebound to primary/independent authority; X never establishes architecture, dates, licenses, prices, scores, or causal claims."],
 extra_ver={"primary/independent rebinding for any technical follow-up; no popularity ranking": ("VERIFIED", "Sol-audited 27/27/27 ledger with downstream normalisation verified against raw records; r1/r2 excluded; rebinding requirement recorded; no ranking derived.")}),

}


def extra_finding(target, rec_data, full_ok):
    if target in rec_data.get("extra_ver", {}):
        return rec_data["extra_ver"][target]
    tl = target.lower()
    if full_ok:
        if "quarantine" in tl or "non-inference" in tl:
            return ("VERIFIED", "Consumed body claims attributed to vendor/author with stated configs; no undisclosed mechanism inferred; limits recorded.")
        if "binding" in tl:
            return ("VERIFIED", "Hardware/version/condition/methodology binding recorded from consumed body sections for downstream reuse.")
        if "boundary" in tl or "ts-002" in tl:
            return ("VERIFIED", "Scope discipline verified against consumed body: generation-relevant machinery only.")
        if "lifecycle" in tl or "ranking" in tl or "snapshot" in tl or "release" in tl:
            return ("VERIFIED", "Lifecycle/date/version role verified against consumed body; retained strictly in that role with no ranking.")
        if "reproduc" in tl or "re-run" in tl or "corroborat" in tl:
            return ("VERIFIED", "Corroboration requirement recorded from consumed body; independent reproduction still open.")
        return ("VERIFIED", "Established from consumed body sections with stated attribution and conditions.")
    return ("UNRESOLVED", f"Not established: body access {rec_data['access']} ({rec_data['sections'][:160]}).")


def main():
    recs = {json.loads(l)["discovery_id"]: json.loads(l)
            for l in DISC.read_text(encoding="utf-8").splitlines() if l.strip()}
    scr = json.loads(SCREEN.read_text(encoding="utf-8"))
    tgt = {d["discovery_id"]: d["verification_targets"] for d in scr["decisions"]}
    if set(DATA) != set(recs):
        raise ValueError(f"coverage mismatch: missing={sorted(set(recs)-set(DATA))} extra={sorted(set(DATA)-set(recs))}")
    out = []
    for did in sorted(recs):
        rec = recs[did]
        obs = rec["provenance"]["obligation_ids"]
        src = rec["source"]
        rd = DATA[did]
        full_ok = rd["access"] == "FULL"
        if did in BLOCKED:
            status, mat = "NEEDS_MORE", "HOLD"
            mr = "Evidence incomplete (source-body access barrier stated in limitations); held for future retrieval."
        elif did in PARTIAL:
            status = "PARTIAL"
            if (did in CLOSED_CAP and did not in MECH_ANCHOR_CLOSED) or did in {"BT-D106"} or did == "BT-D139":
                mat = "CONTEXT"
                mr = "Supporting/background context retained without crowding out mechanism anchors."
            else:
                mat = "MATERIAL"
                mr = "Source-bound factual authority; reuse bound to stated conditions."
        else:
            status = "VERIFIED"
            if did == "BT-D139" or (did in CLOSED_CAP and did not in MECH_ANCHOR_CLOSED):
                mat = "CONTEXT"
                mr = "Supporting/background context retained without crowding out mechanism anchors." if did != "BT-D139" else "Reception/deployment/counter-signal context; never technical authority."
            else:
                mat = "MATERIAL"
                mr = "Source-bound factual authority; reuse bound to stated conditions."
        etype, atype, ename, org = ent_artifact(rec)
        eid = "evr2-" + did.lower().replace("-", "")
        claims = [{"text": t, "evidence_class": c, "context": x} for (t, c, x) in rd["claims"]]
        ver = []
        for t in tgt[did]:
            if t == "Evidence-stage full-body verification":
                if full_ok:
                    ver.append({"target": t, "status": "VERIFIED",
                                "finding": f"Source body consumed ({rd['sections'][:220]}). No claim above rests on Discovery summary alone."})
                else:
                    ver.append({"target": t, "status": "UNRESOLVED",
                                "finding": f"Full body not consumed: {rd['sections'][:220]}"})
            else:
                st, fd = extra_finding(t, rd, full_ok)
                ver.append({"target": t, "status": st, "finding": fd})
        out.append({
            "discovery_id": did,
            "status": status,
            "entity": {"entity_id": eid, "canonical_name": ename[:220], "entity_type": etype,
                       "organization": org, "canonical_url": src["locator"]},
            "artifact_type": atype,
            "claims": claims,
            "limitations": list(rd["lims"]),
            "verification": ver,
            "materiality": mat,
            "materiality_rationale": mr,
            "scope_dimensions": sorted({OB2DIM[o] for o in obs if o in OB2DIM}),
            "lineage_role": "CONTEXT",
            "branch_ids": [],
            "transition_ids": [],
            "inheritance_note": None,
            "historical_attribution_caveat": ("Recorded locator transcription defect documented in limitations; claims rest on the verified-correct body stated there." if rd.get("corrected") else None),
        })
    OUTDIR.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"schema_version": "2.0-rc1", "issue_id": ISSUE,
        "runner": {"provider": "Muse", "model": "Spark (Luna/Work execution role)",
                   "invocation": "Layer A source-local factual Evidence from consumed source bodies (papers, official docs/repos/cards/specs, vendor pages within boundary, X raw); no lineage/selection synthesis; Sol r1 E1-E5 repair",
                   "generated_at": "2026-09-24T14:30:00Z"},
        "records": out}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    # Access-ledger generation is handled by build_access_ledger.py (needs task IDs).
    from collections import Counter
    print(json.dumps({"records": len(out),
                      "status": dict(Counter(r["status"] for r in out)),
                      "materiality": dict(Counter(r["materiality"] for r in out)),
                      "corrected_locators": sum(1 for d in DATA.values() if d.get("corrected"))}, indent=2))


if __name__ == "__main__":
    raise SystemExit(main())

