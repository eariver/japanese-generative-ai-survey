#!/usr/bin/env python3
"""TS-002 screening judgments: 139 explicit per-record dispositions.

Operator: Muse (Luna/Work execution role) applying the Core v2 screening
contract (config/prompts/source-screening-v2.md) against the THEMATIC
Production Profile research question. Preserves primary technical
authorities, the single accepted X reception record, negative-space /
LOW_SIGNAL markings, modality balance, and the TS-002/TS-003 boundary.
Does not discard old sources for age; does not let closed products crowd
out historical mechanism anchors. Not a Sol decision. Sol reviews the
Evidence outcome via a fresh Evidence Semantic Review (materiality,
completeness, selection, architecture not entered here).
"""

from __future__ import annotations

import json
from pathlib import Path

ISSUE_ID = "SP-beyond-text-2026"
OUT = Path("sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/interactive-decisions.json")

FULL = "Evidence-stage full-body verification"

# id: (decision, confidence, reason, scope_tags, verification_targets, duplicate_group)
J = {
# D01 representation / tokenization anchors
"BT-D001": ("KEEP", "high", "VAE origin for the latent-variable/thread that makes continuous media tractable; required D01/D02 anchor.", ["BT-O01", "BT-O02"], [FULL], None),
"BT-D002": ("KEEP", "high", "VQ-VAE discrete-latent origin; intentional discard/preserve tradeoff anchor for image/audio/video tokenizers.", ["BT-O01", "BT-O02"], [FULL], None),
"BT-D003": ("KEEP", "high", "VQ-VAE-2 hierarchy/scale anchor showing discrete latents reaching high-fidelity images.", ["BT-O01", "BT-O02"], [FULL], None),
"BT-D004": ("KEEP", "high", "VQGAN transformer-over-discrete-latents anchor; direct parent of latent-diffusion-era token practice.", ["BT-O01", "BT-O02"], [FULL], None),
"BT-D005": ("KEEP", "high", "dVAE text-to-image anchor binding discrete representation to text conditioning (D01/D03).", ["BT-O01", "BT-O03"], [FULL], None),
"BT-D006": ("KEEP", "high", "SoundStream end-to-end neural codec origin; RVQ/streamable-representation anchor for speech/audio.", ["BT-O01", "BT-O07"], [FULL], None),
"BT-D007": ("KEEP", "high", "EnCodec high-fidelity codec anchor; RVQ/latency/quality tradeoff reference for codec-LM era.", ["BT-O01", "BT-O07", "BT-O08"], [FULL], None),
"BT-D008": ("KEEP", "high", "Descript/DAC improved-RVQGAN anchor; reconstruction-quality bound on downstream generation.", ["BT-O01", "BT-O08"], [FULL], None),
"BT-D009": ("KEEP", "high", "AudioLM semantic+acoustic tokenization anchor; the split that structures codec-LM music/speech work.", ["BT-O01", "BT-O07", "BT-O08"], [FULL], None),
"BT-D010": ("KEEP", "high", "MAGVIT language-neutral video tokenizer anchor; compressed discrete variable-length video representation.", ["BT-O01", "BT-O06", "BT-O09"], [FULL], None),
"BT-D011": ("KEEP", "high", "Imagen T5-conditioning anchor; deep language understanding as generation conditioner (not TS-003 perception).", ["BT-O01", "BT-O03"], [FULL, "TS-002/TS-003 boundary: conditioning machinery only"], None),
"BT-D012": ("KEEP", "high", "Wan2.2-VAE high-compression video VAE anchor; latent-rate/compute consequence for open video.", ["BT-O01", "BT-O09", "BT-O10"], [FULL, "hardware/configuration binding at Evidence"], None),
# D02 paradigms / objectives
"BT-D013": ("KEEP", "high", "GAN origin; adversarial generation/thread retained for vocoders, autoencoders, post-training hybrids.", ["BT-O02"], [FULL], None),
"BT-D014": ("KEEP", "high", "DCGAN convolutional-GAN anchor for stable high-fidelity image generation practice.", ["BT-O02"], [FULL], None),
"BT-D015": ("KEEP", "high", "StyleGAN generator/control landmark; fidelity plus style/control separation for image lineage.", ["BT-O02", "BT-O04"], [FULL], None),
"BT-D016": ("KEEP", "high", "StyleGAN2 quality anchor; artifact/control refinement in the GAN image lineage.", ["BT-O02"], [FULL], None),
"BT-D017": ("KEEP", "high", "PixelRNN autoregressive-pixels origin; raw-sequence cost motivation for latent/token compression.", ["BT-O02"], [FULL], None),
"BT-D018": ("KEEP", "high", "Image Transformer autoregressive anchor; attention over pixels before latent-era scaling.", ["BT-O02"], [FULL], None),
"BT-D019": ("KEEP", "high", "DDPM diffusion origin; tractable training plus sequential-sampling-cost thread start.", ["BT-O02", "BT-O10"], [FULL], None),
"BT-D020": ("KEEP", "high", "DDIM deterministic/implicit sampling anchor; first major sampling-cost reduction on diffusion.", ["BT-O02", "BT-O10"], [FULL], None),
"BT-D021": ("KEEP", "high", "Score-SDE continuous-time anchor unifying diffusion/score modeling with solver implications.", ["BT-O02"], [FULL], None),
"BT-D022": ("KEEP", "high", "EDM design-space anchor; preconditioning/schedule/solver choices that later systems inherit.", ["BT-O02", "BT-O10"], [FULL], None),
"BT-D023": ("KEEP", "high", "Latent Diffusion anchor; compression plus diffusion composition that underpins SD lineage.", ["BT-O01", "BT-O02"], [FULL], None),
"BT-D024": ("KEEP", "high", "Stable Diffusion public implementation anchor; open reproduction/runtime half of latent diffusion.", ["BT-O02", "BT-O10"], [FULL, "version/content binding at Evidence"], None),
"BT-D025": ("KEEP", "high", "DiT transformer-denoiser anchor; backbone/objective separation (U-Net vs Transformer).", ["BT-O02"], [FULL], None),
"BT-D026": ("KEEP", "high", "SiT interpolant-transformer anchor; flow/interpolant view on transformer denoisers.", ["BT-O02"], [FULL], None),
"BT-D027": ("KEEP", "high", "Flow Matching anchor; continuous-flow objective distinct from score/diffusion.", ["BT-O02", "BT-O10"], [FULL], None),
"BT-D028": ("KEEP", "high", "Rectified Flow anchor; straight/fast transfer path reused by editing/video comparisons.", ["BT-O02", "BT-O10"], [FULL], None),
"BT-D029": ("KEEP", "high", "Consistency Models anchor; few-step/inference-acceleration thread distinct from training objective.", ["BT-O02", "BT-O10"], [FULL], None),
"BT-D030": ("KEEP", "high", "ADM diffusion-beats-GAN anchor with classifier guidance; quality/diversity/stability comparison point.", ["BT-O02", "BT-O03"], [FULL], None),
# D03 conditioning / alignment
"BT-D031": ("KEEP", "high", "CLIP conditioning/evaluation machinery anchor; semantic conditioning distinct from perception history.", ["BT-O03", "BT-O11"], [FULL, "TS-002/TS-003 boundary: conditioning/evaluation machinery only"], None),
"BT-D032": ("KEEP", "high", "Classifier-free guidance anchor; training-time conditioning plus inference-time guidance distinction.", ["BT-O03"], [FULL], None),
"BT-D033": ("KEEP", "high", "GLIDE text-guided diffusion anchor; text-conditioning plus editing precursor.", ["BT-O03", "BT-O05"], [FULL], None),
"BT-D034": ("KEEP", "high", "eDiff-I expert-denoiser ensemble anchor; conditioning capacity/specialization direction.", ["BT-O03"], [FULL], None),
"BT-D035": ("KEEP", "high", "CLAP text-audio alignment anchor; audio-side counterpart to CLIP for alignment metrics.", ["BT-O03", "BT-O08", "BT-O11"], [FULL], None),
# D04 control / reference / identity
"BT-D036": ("KEEP", "high", "ControlNet spatial-control transition anchor; generation-control separation landmark.", ["BT-O04"], [FULL], None),
"BT-D037": ("KEEP", "high", "T2I-Adapter lightweight-control anchor; adapter path distinct from full ControlNet.", ["BT-O04"], [FULL], None),
"BT-D038": ("KEEP", "high", "IP-Adapter image-prompt adapter anchor; reference conditioning plus editing bridge.", ["BT-O04", "BT-O05"], [FULL], None),
"BT-D039": ("KEEP", "high", "DreamBooth personalization anchor; subject/identity preservation problem start.", ["BT-O04", "BT-O05"], [FULL], None),
"BT-D040": ("KEEP", "high", "LoRA adapter anchor; efficient adaptation reused across image/video acceleration stacks.", ["BT-O04"], [FULL], None),
"BT-D041": ("KEEP", "high", "SPADE/GauGAN spatial-normalization anchor; segmentation-signal as generation control (not perception history).", ["BT-O04"], [FULL, "TS-002/TS-003 boundary: control signals only"], None),
"BT-D042": ("KEEP", "high", "MotionCtrl camera/object-motion control anchor for video; control-fidelity separation case.", ["BT-O04", "BT-O06", "BT-O09"], [FULL], None),
"BT-D043": ("KEEP", "high", "Music ControlNet anchor; melody/rhythm/timing control in the audio lane.", ["BT-O04", "BT-O08"], [FULL], None),
# D05 editing / preservation
"BT-D044": ("KEEP", "high", "SDEdit image-to-image/editing origin; de-novo vs edit distinction anchor.", ["BT-O05"], [FULL], None),
"BT-D045": ("KEEP", "high", "RePaint diffusion-inpainting anchor; masked preservation plus resampling mechanism.", ["BT-O05"], [FULL], None),
"BT-D046": ("KEEP", "high", "Blended Latent Diffusion anchor; locality/preservation handling in latent editing.", ["BT-O05"], [FULL], None),
"BT-D047": ("KEEP", "high", "Prompt-to-Prompt cross-attention editing anchor; attention-control edit locality mechanism.", ["BT-O03", "BT-O05"], [FULL], None),
"BT-D048": ("KEEP", "high", "Imagic real-image editing anchor; embedding-optimization edit path with preservation limits.", ["BT-O05"], [FULL], None),
"BT-D049": ("KEEP", "high", "InstructPix2Pix instruction-editing anchor; language-instruction edit lineage start.", ["BT-O05"], [FULL], None),
"BT-D050": ("KEEP", "high", "Tune-A-Video one-shot video-editing anchor; image-diffusion to video-edit transfer.", ["BT-O05", "BT-O06", "BT-O09"], [FULL], None),
# D07 speech lineage + vocoders
"BT-D051": ("KEEP", "high", "WaveNet raw-waveform autoregression origin; speech-history anchor never collapsed into music.", ["BT-O02", "BT-O07"], [FULL], None),
"BT-D052": ("KEEP", "high", "Tacotron end-to-end TTS decomposition-change anchor.", ["BT-O07"], [FULL], None),
"BT-D053": ("KEEP", "high", "Tacotron 2 mel-conditioning anchor; naturalness/intelligibility step in TTS lineage.", ["BT-O07"], [FULL], None),
"BT-D054": ("KEEP", "high", "FastSpeech parallel/controllable-TTS anchor; latency/control thread in speech.", ["BT-O07", "BT-O10"], [FULL], None),
"BT-D055": ("KEEP", "high", "HiFi-GAN efficient neural-vocoder anchor; GAN retained as vocoder/post-training mechanism.", ["BT-O07", "BT-O10"], [FULL], None),
"BT-D056": ("KEEP", "high", "VITS end-to-end latent+flow+adversarial TTS anchor; intelligibility/naturalness/speaker thread.", ["BT-O07"], [FULL], None),
"BT-D057": ("KEEP", "high", "YourTTS multispeaker-transfer anchor; speaker/identity preservation in TTS.", ["BT-O04", "BT-O07"], [FULL], None),
"BT-D058": ("KEEP", "high", "VALL-E codec-LM zero-shot TTS anchor; neural-codec plus language-modeling transition.", ["BT-O01", "BT-O07"], [FULL], None),
"BT-D059": ("KEEP", "high", "VALL-E 2 human-parity codec-LM anchor; vendor parity claim quarantined at Evidence.", ["BT-O07", "BT-O11"], [FULL, "vendor-claim quarantine"], None),
"BT-D060": ("KEEP", "high", "Voicebox flow-matching multilingual speech generation/editing anchor; non-autoregressive path.", ["BT-O02", "BT-O05", "BT-O07"], [FULL], None),
"BT-D061": ("KEEP", "high", "Seed-TTS versatile speech anchor; expressiveness/coverage in current speech lineage.", ["BT-O06", "BT-O07"], [FULL, "vendor-claim quarantine"], None),
"BT-D062": ("KEEP", "high", "SeamlessM4T-v2 expressive multilingual/streaming anchor; translation-adjacent speech kept to generation boundary.", ["BT-O06", "BT-O07"], [FULL], None),
# D08 music / audio lineage
"BT-D063": ("KEEP", "high", "Jukebox raw/discrete music-modeling origin; long-form structure problem start.", ["BT-O02", "BT-O06", "BT-O08"], [FULL], None),
"BT-D064": ("KEEP", "high", "DiffWave versatile diffusion-audio anchor; diffusion in the waveform lane.", ["BT-O02", "BT-O07", "BT-O08"], [FULL], None),
"BT-D065": ("KEEP", "high", "MusicLM text-to-music anchor; semantic/musical-structure thread.", ["BT-O06", "BT-O08"], [FULL], None),
"BT-D066": ("KEEP", "high", "MusicGen controllable-music anchor; melody/chroma/lyrics conditioning practice.", ["BT-O04", "BT-O08"], [FULL], None),
"BT-D067": ("KEEP", "high", "AudioLDM latent-diffusion text-to-audio anchor; DiT/latent path in general audio.", ["BT-O02", "BT-O08"], [FULL], None),
"BT-D068": ("KEEP", "high", "Stable Audio Open anchor; open-weight mechanism comparator for latent-diffusion audio.", ["BT-O08", "BT-O10"], [FULL, "license/version binding at Evidence"], None),
"BT-D069": ("KEEP", "high", "MuSTANGO controllable text-to-music anchor; control-fidelity case in music.", ["BT-O04", "BT-O08"], [FULL], None),
# D09 video lineage
"BT-D070": ("KEEP", "high", "Video Diffusion Models anchor; temporal diffusion problem start for video.", ["BT-O02", "BT-O06", "BT-O09"], [FULL], None),
"BT-D071": ("KEEP", "high", "Imagen Video cascaded spatial+temporal super-resolution anchor.", ["BT-O06", "BT-O09"], [FULL], None),
"BT-D072": ("KEEP", "high", "Phenaki variable-length discrete-video anchor; tokenizer plus temporal-structure thread.", ["BT-O01", "BT-O06", "BT-O09"], [FULL], None),
"BT-D073": ("KEEP", "high", "Make-A-Video text-video-data-free anchor; joint image-video training direction.", ["BT-O03", "BT-O09"], [FULL], None),
"BT-D074": ("KEEP", "high", "AnimateDiff personalized video anchor; reference/personalization transfer to video.", ["BT-O05", "BT-O09"], [FULL], None),
"BT-D075": ("KEEP", "high", "Stable Video Diffusion latent-video scaling anchor; open image-to-video reference.", ["BT-O09", "BT-O10"], [FULL], None),
"BT-D076": ("KEEP", "high", "Movie Gen media-foundation anchor; scaled video plus synchronized-audio direction.", ["BT-O06", "BT-O09"], [FULL, "vendor-claim quarantine"], None),
"BT-D077": ("KEEP", "high", "Sora historical turning-point anchor; research impact distinct from 2026 product longevity.", ["BT-O06", "BT-O09"], [FULL, "lifecycle dates verified 2026-09-23"], None),
# D10 runtime / acceleration
"BT-D078": ("KEEP", "high", "Progressive distillation anchor; few-step sampling thread start.", ["BT-O02", "BT-O10"], [FULL], None),
"BT-D079": ("KEEP", "high", "Latent Consistency Models anchor; consistency/distillation inference acceleration.", ["BT-O02", "BT-O10"], [FULL], None),
"BT-D080": ("KEEP", "high", "LCM-LoRA universal-acceleration anchor; adapter plus consistency composition.", ["BT-O04", "BT-O10"], [FULL], None),
"BT-D081": ("KEEP", "high", "SDXL-Turbo/ADD adversarial-distillation anchor; few-step quality/speed tradeoff case.", ["BT-O02", "BT-O10"], [FULL], None),
"BT-D082": ("KEEP", "high", "MobileDiffusion subsecond-mobile anchor; on-device deployability bound.", ["BT-O10"], [FULL, "hardware/configuration binding at Evidence"], None),
# D11 evaluation / metric validity
"BT-D083": ("KEEP", "high", "FID/TTUR distribution-metric origin; limitations must be preserved at Evidence.", ["BT-O11"], [FULL, "metric-validity context binding"], None),
"BT-D084": ("KEEP", "high", "Inception Score anchor; early quality/diversity metric with known limits.", ["BT-O11"], [FULL, "metric-validity context binding"], None),
"BT-D085": ("KEEP", "high", "GenEval compositional-alignment diagnostic anchor; prompt-adherence separation case.", ["BT-O03", "BT-O11"], [FULL, "metric-validity context binding"], None),
"BT-D086": ("KEEP", "high", "T2I-CompBench compositional benchmark anchor; binding/attribute diagnostic.", ["BT-O03", "BT-O11"], [FULL, "metric-validity context binding"], None),
"BT-D087": ("KEEP", "high", "Pick-a-Pic human-preference dataset anchor; preference-study methodology case.", ["BT-O11"], [FULL, "metric-validity context binding"], None),
"BT-D088": ("KEEP", "high", "Fréchet Audio Distance anchor; embedding-dependence limit must be preserved.", ["BT-O11"], [FULL, "metric-validity context binding"], None),
"BT-D089": ("KEEP", "high", "LibriSpeech corpus anchor; intelligibility/WER evaluation substrate.", ["BT-O07", "BT-O11"], [FULL], None),
"BT-D090": ("KEEP", "high", "GE2E speaker-verification loss anchor; speaker-similarity evaluation substrate.", ["BT-O07", "BT-O11"], [FULL], None),
"BT-D091": ("KEEP", "high", "MUSHRA listening-protocol anchor; human audio-evaluation methodology.", ["BT-O11"], [FULL, "metric-validity context binding"], None),
"BT-D092": ("KEEP", "high", "VBench multidimensional video-evaluation anchor; consistency/motion/adherence split.", ["BT-O09", "BT-O11"], [FULL, "metric-validity context binding"], None),
"BT-D093": ("KEEP", "high", "VBench-2.0 intrinsic-faithfulness anchor; physics/commonsense/human-fidelity extension.", ["BT-O09", "BT-O11"], [FULL, "metric-validity context binding"], None),
# D12 convergence / provenance boundary
"BT-D094": ("KEEP", "high", "Unified-IO unified vision-language anchor; convergence case kept to generation-relevant scope.", ["BT-O12"], [FULL, "TS-002/TS-003 boundary: generation-relevant only"], None),
"BT-D095": ("KEEP", "high", "AudioPaLM speak-and-listen anchor; native-audio multimodal boundary case.", ["BT-O07", "BT-O12"], [FULL, "TS-002/TS-003 boundary: generation-relevant only"], None),
"BT-D096": ("KEEP", "high", "AnyGPT discrete-multimodal anchor; unified-token convergence hypothesis case.", ["BT-O12"], [FULL, "TS-002/TS-003 boundary: generation-relevant only"], None),
"BT-D097": ("KEEP", "high", "CoDi any-to-any diffusion anchor; compositing-diffusion convergence mechanism.", ["BT-O02", "BT-O12"], [FULL], None),
"BT-D098": ("KEEP", "high", "C2PA provenance-specification anchor; watermark/credential deployment-trust mechanism.", ["BT-O11", "BT-O12"], [FULL], None),
"BT-D099": ("KEEP", "high", "SynthID watermarking anchor; generated-media verification mechanism.", ["BT-O12"], [FULL], None),
# Current capstones: capability/workflow cases, architecture non-inference
"BT-D100": ("KEEP", "high", "FLUX.2 [klein] interactive-visual-intelligence capstone; open/local plus few-step runtime case.", ["BT-O02", "BT-O05", "BT-O10"], [FULL, "vendor-claim quarantine; architecture non-inference; hardware/configuration binding"], None),
"BT-D101": ("KEEP", "high", "FLUX.2 product-surface authority; generation+editing feature availability case.", ["BT-O04", "BT-O05"], [FULL, "capability surface only; architecture non-inference"], None),
"BT-D102": ("KEEP", "high", "Seedream 5.0 Pro multimodal creation/editing capstone; design-task direction case.", ["BT-O04", "BT-O05", "BT-O12"], [FULL, "vendor evaluation quarantined; architecture non-inference"], None),
"BT-D103": ("KEEP", "high", "ChatGPT Images 2.5 generation+iterative-editing capstone; limited-disclosure capability case.", ["BT-O05", "BT-O06"], [FULL, "capability/workflow only; architecture non-inference"], None),
"BT-D104": ("KEEP", "high", "Nano Banana 2 reasoning+generation/editing boundary capstone; TS-002/TS-003 test case.", ["BT-O05", "BT-O12"], [FULL, "capability case; reasoning-architecture non-inference; TS-002/TS-003 boundary"], None),
"BT-D105": ("KEEP", "high", "Gemini 3.1 Flash Image model-card authority; limitations/evaluation for native image surface.", ["BT-O11", "BT-O12"], [FULL, "model-card limits preserved; architecture non-inference"], None),
"BT-D106": ("MAYBE", "medium", "Imagen dedicated-generator comparator retained solely as deprecation/lifecycle evidence for dedicated-to-multimodal convergence; not a current mechanism anchor.", ["BT-O02", "BT-O12"], [FULL, "lifecycle-only role; do not use for 2026 capability ranking"], None),
"BT-D107": ("KEEP", "high", "GPT-Live native realtime-speech capstone; reasoning+speech latency/streaming case.", ["BT-O06", "BT-O07", "BT-O10"], [FULL, "vendor-claim quarantine; latency/streaming binding"], None),
"BT-D108": ("KEEP", "high", "OpenAI voice-API model authority; realtime voice capability/availability case.", ["BT-O07", "BT-O10"], [FULL, "capability/availability only"], None),
"BT-D109": ("KEEP", "high", "Gemini 3.8 Audio model-card authority; native-audio limits/evaluation case.", ["BT-O07", "BT-O11", "BT-O12"], [FULL, "model-card limits preserved"], None),
"BT-D110": ("KEEP", "high", "Seed Audio 1.0 scene-level audio capstone; speech/SFX/ambience convergence test case.", ["BT-O06", "BT-O07", "BT-O08", "BT-O12"], [FULL, "vendor-claim quarantine; scene-continuity binding"], None),
"BT-D111": ("KEEP", "high", "Lyria 3.5 model-card authority; rare architecture/evaluation disclosure for closed music frontier.", ["BT-O06", "BT-O08", "BT-O11"], [FULL, "card-disclosed mechanism only; no beyond-card inference"], None),
"BT-D112": ("KEEP", "high", "Lyria model-page corroboration; closed music lineage context.", ["BT-O08"], [FULL, "capability context only"], None),
"BT-D113": ("KEEP", "high", "Stable Audio 3 open-weight mechanism anchor; autoencoder plus latent-diffusion plus editing/local case.", ["BT-O05", "BT-O08", "BT-O10"], [FULL, "mechanism anchor; version/license binding"], None),
"BT-D114": ("MAYBE", "medium", "Suno release-notes version/lifecycle authority; closed long-form workflow case with thin independent evaluation (G03 partial retained).", ["BT-O06", "BT-O08"], [FULL, "version-fluid; workflow case only; architecture non-inference"], None),
"BT-D115": ("KEEP", "high", "Suno v6 launch authority; local-editing/mashup/multimodal-input workflow direction case.", ["BT-O05", "BT-O08"], [FULL, "capability/ecosystem case; architecture non-inference"], None),
"BT-D116": ("MAYBE", "medium", "ElevenLabs Music docs secondary closed comparator; composition-plan/reference/inpainting case with thin authority.", ["BT-O06", "BT-O08"], [FULL, "secondary comparator only; corroboration needed at Evidence"], None),
"BT-D117": ("KEEP", "high", "Seedance 2.5 joint audio-video capstone; clip-to-storytelling transition case with continuation.", ["BT-O04", "BT-O05", "BT-O06", "BT-O09"], [FULL, "vendor-claim quarantine; duration vs coherence binding"], None),
"BT-D118": ("KEEP", "high", "Veo closed comparator with card/benchmark authority; adherence/physics evaluation case.", ["BT-O06", "BT-O09", "BT-O11"], [FULL, "vendor benchmark quarantined; architecture non-inference"], None),
"BT-D119": ("KEEP", "high", "FLUX 3 joint image/video/audio convergence case; shared-foundation hypothesis instance.", ["BT-O09", "BT-O12"], [FULL, "early-access claims quarantined; convergence question only"], None),
"BT-D120": ("KEEP", "high", "Kling 3.0 Omni launch authority; generation+editing+audio claim with disclosure-depth check at Evidence.", ["BT-O05", "BT-O09"], [FULL, "launch claims quarantined; mechanism role only if disclosed"], None),
"BT-D121": ("KEEP", "high", "Runway Gen-4.5 production T2V/I2V case; workflow/control/runtime comparator.", ["BT-O09", "BT-O10"], [FULL, "workflow/runtime case; architecture non-inference"], None),
"BT-D122": ("INSPECT", "medium", "Luma Ray3 production comparator; subversions changed during 2026 so exact version must be bound at Evidence before any comparison.", ["BT-O04", "BT-O09"], ["bind exact Ray3 subversion/version at Evidence", FULL], None),
"BT-D123": ("INSPECT", "medium", "Ray 3.2 dated subversion datapoint; version-discipline companion to BT-D122, not a standalone capability rank.", ["BT-O09"], ["bind exact version/date at Evidence", FULL], None),
"BT-D124": ("KEEP", "high", "Wan2.2 open-weight release anchor; mandatory open/runtime lane with local ecosystem.", ["BT-O06", "BT-O09", "BT-O10"], [FULL, "version/checkpoint currency binding; local-runtime binding"], None),
"BT-D125": ("KEEP", "high", "Wan open-source hub corroboration; current-release identification surface (do not freeze on 2.2 if superseded).", ["BT-O09", "BT-O10"], [FULL, "identify current official release at Evidence"], None),
"BT-D126": ("KEEP", "high", "Sora 2 historical record; lifecycle context for frontier-impact vs product-longevity distinction.", ["BT-O09"], [FULL, "historical/lifecycle role only; not a 2026 product capstone"], None),
"BT-D127": ("KEEP", "high", "Sora discontinuation help-center authority; exact lifecycle-date evidence.", ["BT-O09"], [FULL, "date/lifecycle fact only"], None),
"BT-D128": ("KEEP", "high", "OpenAI API deprecation authority; Sora 2 Videos API shutdown-date evidence (2026-09-24).", ["BT-O09", "BT-O10"], [FULL, "date/availability fact only"], None),
# R2 gap-fill
"BT-D129": ("KEEP", "high", "Wav2Lip lip-sync expert anchor; AV-synchronization evaluation lane (G08 partial).", ["BT-O11", "BT-O09"], [FULL, "metric-validity context binding"], None),
"BT-D130": ("KEEP", "high", "AV-HuBERT-style AV representation validity-critique anchor; lip-sync metric limits.", ["BT-O11"], [FULL, "metric-validity context binding"], None),
"BT-D131": ("KEEP", "high", "VideoPhy physical-commonsense evaluation anchor; video physics lane (G11).", ["BT-O11", "BT-O09"], [FULL, "metric-validity context binding"], None),
"BT-D132": ("KEEP", "high", "F5-TTS flow-matching TTS anchor; open/deployable speech lane (G09).", ["BT-O07", "BT-O10"], [FULL], None),
"BT-D133": ("KEEP", "high", "CosyVoice 2 streaming speech-LM anchor; deployable cloning/streaming lane (G09).", ["BT-O07", "BT-O10"], [FULL], None),
"BT-D134": ("KEEP", "high", "Moshi full-duplex speech-text foundation anchor; streaming methodology plus latency lane (G10).", ["BT-O07", "BT-O10"], [FULL], None),
"BT-D135": ("KEEP", "high", "DuplexBench full-duplex evaluation methodology anchor; interruption/overlap/latency measurement lane.", ["BT-O11", "BT-O07"], [FULL, "metric-validity context binding"], None),
"BT-D136": ("KEEP", "high", "Music human-preference benchmark anchor; FAD/CLAP correlation plus open judgments (G03 partial).", ["BT-O11", "BT-O08"], [FULL, "metric-validity context binding; era limitation preserved"], None),
"BT-D137": ("KEEP", "high", "FLUX.2-klein-4B independent H100 measurement anchor; vendor sub-second claim now independently anchored (G04 partial).", ["BT-O10"], [FULL, "hardware/configuration binding; single-lab limit preserved"], None),
"BT-D138": ("KEEP", "high", "FiVE diffusion-vs-rectified-flow video-editing benchmark anchor; RF speed/quality tradeoff in editing domain (G12 partial).", ["BT-O05", "BT-O09", "BT-O02"], [FULL, "editing-domain scope preserved; pure-generation ablations thin"], None),
# X-bound reception
"BT-D139": ("KEEP", "high", "Single accepted X reception/deployment/counter-signal record for 27 audited observations; preserves modality balance and LOW_SIGNAL lanes without creating 27 technical records.", ["BT-O04", "BT-O05", "BT-O06", "BT-O07", "BT-O08", "BT-O09", "BT-O10"], ["primary/independent rebinding for any technical follow-up; no popularity ranking", FULL], None),
}


def main() -> None:
    if set(J) != {f"BT-D{i:03d}" for i in range(1, 140)}:
        missing = sorted(set(f"BT-D{i:03d}" for i in range(1, 140)) - set(J))
        extra = sorted(set(J) - {f"BT-D{i:03d}" for i in range(1, 140)})
        raise ValueError(f"screening coverage must be exactly BT-D001..BT-D139: missing={missing} extra={extra}")
    decisions = []
    for did in sorted(J):
        decision, confidence, reason, tags, targets, dup = J[did]
        decisions.append({
            "discovery_id": did,
            "decision": decision,
            "reason": reason,
            "scope_tags": tags,
            "duplicate_group": dup,
            "verification_targets": targets,
            "confidence": confidence,
        })
    doc = {
        "schema_version": "2.0-rc1",
        "issue_id": ISSUE_ID,
        "runner": {
            "provider": "Muse",
            "model": "Spark (Luna/Work execution role)",
            "invocation": "Core v2 screening contract + THEMATIC Production Profile research question; preserves primary authorities, X reception, negative-space/LOW_SIGNAL, modality balance, TS-002/TS-003 boundary; Sol review via fresh Evidence Semantic Review, not a Sol decision",
            "generated_at": "2026-09-24T12:50:00Z",
        },
        "decisions": decisions,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from collections import Counter
    print(json.dumps({"out": str(OUT), "counts": dict(Counter(d["decision"] for d in decisions))}, indent=2))


if __name__ == "__main__":
    raise SystemExit(main())
