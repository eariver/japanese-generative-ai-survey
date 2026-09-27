#!/usr/bin/env python3
"""Build the canonical interactive Selection/Architecture input for SP-beyond-text-2026.

Edition-local operator tooling (NOT shared Core). Emits the exact input JSON
consumed by scripts/run_selection_architecture_v2_interactive.py.

Semantic authority: Sol provenance readback PASS (rebound Evidence accepted:
126 VERIFIED / 8 PARTIAL / 5 NEEDS_MORE) plus the Materiality-through-Architecture
prompt §§5-9. Anti-thinness: all 134 non-HOLD records selected; the 43-entry
transition ledger maps to packages; closed products stay capability context;
X stays reception context; 5 body-blocked records HOLD (no fabrication).
"""

from __future__ import annotations

import json
from pathlib import Path

ISSUE_ID = "SP-beyond-text-2026"
OUT_REL = "sources/SP-beyond-text-2026/execution/progress-materiality-architecture-20260925/interactive-selection-architecture.json"

PUB = "LONGFORM_SPECIAL"
RES = "THEMATIC"


def sel(usage, pkg, lane, rationale):
    assert usage in ("PRIMARY", "SUPPORTING")
    kind = "primary" if usage == "PRIMARY" else "supporting"
    role = "anchor" if usage == "PRIMARY" else "context"
    return {
        "discovery_id": None,
        "disposition": "SELECTED",
        "rationale": rationale,
        "architecture_usage": usage,
        "publication_role": f"{PUB}:{pkg}-{kind}",
        "architecture_role": f"{RES}:{lane}-{role}",
        "profile_extensions": {"lane": lane},
    }


def hold(rationale):
    return {
        "discovery_id": None,
        "disposition": "HOLD",
        "rationale": rationale,
        "architecture_usage": "NONE",
        "publication_role": None,
        "architecture_role": None,
        "profile_extensions": {"lane": "unselected"},
    }


A = {}
# ---- representation ----
for did, lane, rat in [
    ("BT-D001", "media_representation_tokenization", "PRIMARY anchor: amortized VI/reparameterization origin of continuous media latents."),
    ("BT-D002", "media_representation_tokenization", "PRIMARY anchor: discrete codebook origin feeding VQGAN/codecs/video tokenizers."),
    ("BT-D006", "media_representation_tokenization", "PRIMARY anchor: RVQ neural codec origin (SoundStream) for speech/audio."),
    ("BT-D007", "media_representation_tokenization", "PRIMARY anchor: EnCodec token rate/quality reference for codec-LM audio."),
    ("BT-D009", "media_representation_tokenization", "PRIMARY anchor: semantic/acoustic tokenization separation thesis (AudioLM)."),
    ("BT-D010", "media_representation_tokenization", "PRIMARY anchor: 3D-VQ video tokenizer precedent (MAGVIT)."),
]:
    r = sel("PRIMARY", "rep-compression", lane, f"SELECTED PRIMARY {rat}")
    r["discovery_id"] = did
    A[did] = r
for did, lane, rat in [
    ("BT-D003", "media_representation_tokenization", "SUPPORTING hierarchical-code scale point (VQ-VAE-2)."),
    ("BT-D004", "media_representation_tokenization", "SUPPORTING perceptual-adversarial tokenizer bar (VQGAN)."),
    ("BT-D005", "media_representation_tokenization", "SUPPORTING text-conditioned discrete-token precedent (dVAE)."),
    ("BT-D008", "media_representation_tokenization", "SUPPORTING codec rate/quality successor datapoint (DAC)."),
    ("BT-D012", "media_representation_tokenization", "SUPPORTING open high-compression video VAE with consumer-GPU envelope (Wan2.2-VAE)."),
]:
    r = sel("SUPPORTING", "rep-compression", lane, f"SELECTED SUPPORTING {rat}")
    r["discovery_id"] = did
    A[did] = r
# ---- paradigms ----
for did, lane, rat in [
    ("BT-D013", "generative_paradigms_objectives", "PRIMARY anchor: adversarial formulation origin; quality/diversity/stability axis."),
    ("BT-D015", "generative_paradigms_objectives", "PRIMARY anchor: style-based generator/control landmark (StyleGAN)."),
    ("BT-D016", "generative_paradigms_objectives", "PRIMARY anchor: GAN quality ceiling diffusion had to beat (StyleGAN2)."),
    ("BT-D019", "generative_paradigms_objectives", "PRIMARY anchor: DDPM diffusion origin with score-matching equivalence."),
    ("BT-D020", "generative_paradigms_objectives", "PRIMARY anchor: first general sampling-efficiency transition (DDIM)."),
    ("BT-D021", "generative_paradigms_objectives", "PRIMARY anchor: score-SDE continuous-time unification."),
    ("BT-D023", "generative_paradigms_objectives", "PRIMARY anchor: latent-diffusion era transition."),
    ("BT-D025", "generative_paradigms_objectives", "PRIMARY anchor: transformer-denoiser backbone/objective separation (DiT)."),
    ("BT-D027", "generative_paradigms_objectives", "PRIMARY anchor: simulation-free flow training (Flow Matching)."),
    ("BT-D028", "generative_paradigms_objectives", "PRIMARY anchor: rectified straightening with reflow (Rectified Flow)."),
    ("BT-D029", "generative_paradigms_objectives", "PRIMARY anchor: few-step self-consistent generation (Consistency)."),
    ("BT-D030", "generative_paradigms_objectives", "PRIMARY anchor: diffusion-beats-GAN turning point with classifier guidance (ADM)."),
]:
    r = sel("PRIMARY", "paradigms", lane, f"SELECTED PRIMARY {rat}")
    r["discovery_id"] = did
    A[did] = r
for did, lane, rat in [
    ("BT-D014", "generative_paradigms_objectives", "SUPPORTING reproducible CNN-GAN baseline (DCGAN)."),
    ("BT-D017", "generative_paradigms_objectives", "SUPPORTING raw-sequence cost origin (PixelRNN)."),
    ("BT-D018", "generative_paradigms_objectives", "SUPPORTING transformer-prior precedent (Image Transformer)."),
    ("BT-D022", "generative_paradigms_objectives", "SUPPORTING design-space reference at abstract level (EDM; body barrier declared)."),
    ("BT-D026", "generative_paradigms_objectives", "SUPPORTING diffusion-to-flow bridge on transformer backbone (SiT)."),
]:
    r = sel("SUPPORTING", "paradigms", lane, f"SELECTED SUPPORTING {rat}")
    r["discovery_id"] = did
    A[did] = r
# ---- conditioning ----
for did, lane, rat in [
    ("BT-D011", "conditioning_alignment", "PRIMARY anchor: frozen-encoder conditioning with T5-vs-CLIP finding (Imagen)."),
    ("BT-D032", "conditioning_alignment", "PRIMARY anchor: dominant text-adherence control (classifier-free guidance)."),
    ("BT-D033", "conditioning_alignment", "PRIMARY anchor: text-guided diffusion with guidance comparison + editing extension (GLIDE)."),
    ("BT-D036", "conditioning_alignment", "PRIMARY anchor: spatial-control transition (ControlNet; also control lane)."),
]:
    r = sel("PRIMARY", "conditioning", lane, f"SELECTED PRIMARY {rat}")
    r["discovery_id"] = did
    A[did] = r
for did, lane, rat in [
    ("BT-D031", "conditioning_alignment", "SUPPORTING semantic-encoder precedent with generation-only boundary (CLIP)."),
    ("BT-D034", "conditioning_alignment", "SUPPORTING conditioning-encoder composition study (eDiff-I)."),
    ("BT-D035", "conditioning_alignment", "SUPPORTING text-audio joint embedding for conditioning/eval (CLAP)."),
]:
    r = sel("SUPPORTING", "conditioning", lane, f"SELECTED SUPPORTING {rat}")
    r["discovery_id"] = did
    A[did] = r
# ---- control ----
for did, lane, rat in [
    ("BT-D038", "control_reference_identity", "PRIMARY anchor: reference-conditioning mechanism (IP-Adapter)."),
    ("BT-D039", "control_reference_identity", "PRIMARY anchor: identity-preservation origin (DreamBooth)."),
    ("BT-D042", "control_reference_identity", "PRIMARY anchor: camera/object motion control for video (MotionCtrl)."),
]:
    r = sel("PRIMARY", "control", lane, f"SELECTED PRIMARY {rat}")
    r["discovery_id"] = did
    A[did] = r
for did, lane, rat in [
    ("BT-D037", "control_reference_identity", "SUPPORTING lightweight control alternative (T2I-Adapter)."),
    ("BT-D040", "control_reference_identity", "SUPPORTING parameter-efficient control surface (LoRA)."),
    ("BT-D041", "control_reference_identity", "SUPPORTING pre-diffusion spatial-control precursor (SPADE)."),
    ("BT-D043", "control_reference_identity", "SUPPORTING audio-domain control-signal study (Music ControlNet)."),
]:
    r = sel("SUPPORTING", "control", lane, f"SELECTED SUPPORTING {rat}")
    r["discovery_id"] = did
    A[did] = r
# ---- editing ----
for did, lane, rat in [
    ("BT-D044", "editing_preservation", "PRIMARY anchor: editing-as-partial-diffusion formulation (SDEdit)."),
    ("BT-D045", "editing_preservation", "PRIMARY anchor: preservation-of-unmasked-content mechanism (RePaint)."),
    ("BT-D049", "editing_preservation", "PRIMARY anchor: instruction-following editing origin (InstructPix2Pix)."),
    ("BT-D050", "editing_preservation", "PRIMARY anchor: image-diffusion to video-edit transfer (Tune-A-Video)."),
]:
    r = sel("PRIMARY", "editing", lane, f"SELECTED PRIMARY {rat}")
    r["discovery_id"] = did
    A[did] = r
for did, lane, rat in [
    ("BT-D046", "editing_preservation", "SUPPORTING latent-space local editing (Blended LD)."),
    ("BT-D047", "editing_preservation", "SUPPORTING attention-as-editing-interface (Prompt-to-Prompt)."),
    ("BT-D048", "editing_preservation", "SUPPORTING optimisation-based real-image editing (Imagic)."),
]:
    r = sel("SUPPORTING", "editing", lane, f"SELECTED SUPPORTING {rat}")
    r["discovery_id"] = did
    A[did] = r
# ---- speech ----
for did, lane, rat in [
    ("BT-D051", "speech_voice_lineage", "PRIMARY anchor: waveform-modeling origin (WaveNet)."),
    ("BT-D056", "speech_voice_lineage", "PRIMARY anchor: latent/flow/adversarial hybrid TTS (VITS)."),
    ("BT-D058", "speech_voice_lineage", "PRIMARY anchor: codec-LM speech transition (VALL-E)."),
    ("BT-D060", "speech_voice_lineage", "PRIMARY anchor: non-autoregressive flow editing thesis (Voicebox)."),
    ("BT-D061", "speech_voice_lineage", "PRIMARY anchor: versatile controllable/deployable TTS (Seed-TTS)."),
    ("BT-D062", "speech_voice_lineage", "PRIMARY anchor: full-duplex/streaming v2 family reference (Seamless v2 body)."),
    ("BT-D134", "speech_voice_lineage", "PRIMARY anchor: full-duplex latency/architecture reference (Moshi, framework sections)."),
]:
    r = sel("PRIMARY", "speech", lane, f"SELECTED PRIMARY {rat}")
    r["discovery_id"] = did
    A[did] = r
for did, lane, rat in [
    ("BT-D052", "speech_voice_lineage", "SUPPORTING decomposition-change anchor (Tacotron)."),
    ("BT-D053", "speech_voice_lineage", "SUPPORTING human-parity MOS anchor (Tacotron 2)."),
    ("BT-D054", "speech_voice_lineage", "SUPPORTING parallelization/latency transition (FastSpeech)."),
    ("BT-D055", "speech_voice_lineage", "SUPPORTING adversarial vocoding standard (HiFi-GAN)."),
    ("BT-D057", "speech_voice_lineage", "SUPPORTING speaker-identity conditioning precedent (YourTTS)."),
    ("BT-D059", "speech_voice_lineage", "SUPPORTING decoding-stability study within consumed sections (VALL-E 2, partial)."),
    ("BT-D132", "speech_voice_lineage", "SUPPORTING open flow-matching DiT TTS with runtime (F5-TTS)."),
    ("BT-D133", "speech_voice_lineage", "SUPPORTING open streaming TTS with latency model (CosyVoice 2)."),
]:
    r = sel("SUPPORTING", "speech", lane, f"SELECTED SUPPORTING {rat}")
    r["discovery_id"] = did
    A[did] = r
# ---- music ----
for did, lane, rat in [
    ("BT-D063", "music_audio_lineage", "PRIMARY anchor: long-form raw-audio precedent (Jukebox)."),
    ("BT-D065", "music_audio_lineage", "PRIMARY anchor: semantic/musical-structure thread (MusicLM)."),
    ("BT-D066", "music_audio_lineage", "PRIMARY anchor: controllable baseline practice (MusicGen)."),
    ("BT-D068", "music_audio_lineage", "PRIMARY anchor: open-mechanism comparator (Stable Audio Open)."),
]:
    r = sel("PRIMARY", "music", lane, f"SELECTED PRIMARY {rat}")
    r["discovery_id"] = did
    A[did] = r
for did, lane, rat in [
    ("BT-D064", "music_audio_lineage", "SUPPORTING diffusion-in-audio transition (DiffWave)."),
    ("BT-D067", "music_audio_lineage", "SUPPORTING latent-diffusion-in-audio transition (AudioLDM)."),
    ("BT-D069", "music_audio_lineage", "SUPPORTING fine-grained musical-control study (MuSTANGO)."),
    ("BT-D136", "music_audio_lineage", "SUPPORTING human-preference metric validation (music benchmark)."),
]:
    r = sel("SUPPORTING", "music", lane, f"SELECTED SUPPORTING {rat}")
    r["discovery_id"] = did
    A[did] = r
# ---- video ----
for did, lane, rat in [
    ("BT-D070", "video_lineage", "PRIMARY anchor: diffusion-in-video transition (VDM)."),
    ("BT-D071", "video_lineage", "PRIMARY anchor: duration/resolution scaling design (Imagen Video)."),
    ("BT-D073", "video_lineage", "PRIMARY anchor: data-efficiency parallel invention (Make-A-Video)."),
    ("BT-D075", "video_lineage", "PRIMARY anchor: open image-to-video mechanism reference (SVD)."),
]:
    r = sel("PRIMARY", "video", lane, f"SELECTED PRIMARY {rat}")
    r["discovery_id"] = did
    A[did] = r
for did, lane, rat in [
    ("BT-D074", "video_lineage", "SUPPORTING open-ecosystem motion adapter (AnimateDiff)."),
    ("BT-D077", "video_lineage", "SUPPORTING historical turning-point with lifecycle discipline (Sora)."),
    ("BT-D124", "video_lineage", "SUPPORTING mandatory open/runtime lane (Wan2.2)."),
    ("BT-D138", "video_lineage", "SUPPORTING flow-vs-diffusion comparison in editing domain (FiVE)."),
]:
    r = sel("SUPPORTING", "video", lane, f"SELECTED SUPPORTING {rat}")
    r["discovery_id"] = did
    A[did] = r
# ---- runtime ----
for did, lane, rat in [
    ("BT-D078", "runtime_deployment", "PRIMARY anchor: distillation-for-few-step origin."),
    ("BT-D081", "runtime_deployment", "PRIMARY anchor: hybrid adversarial-distillation thesis (ADD)."),
    ("BT-D082", "runtime_deployment", "PRIMARY anchor: on-device deployment-envelope study (MobileDiffusion)."),
    ("BT-D137", "runtime_deployment", "PRIMARY anchor: independent klein measurement (vendor claim anchored)."),
]:
    r = sel("PRIMARY", "runtime", lane, f"SELECTED PRIMARY {rat}")
    r["discovery_id"] = did
    A[did] = r
for did, lane, rat in [
    ("BT-D079", "runtime_deployment", "SUPPORTING open few-step recipe (LCM)."),
    ("BT-D080", "runtime_deployment", "SUPPORTING portable few-step module (LCM-LoRA)."),
]:
    r = sel("SUPPORTING", "runtime", lane, f"SELECTED SUPPORTING {rat}")
    r["discovery_id"] = did
    A[did] = r
# ---- evaluation ----
for did, lane, rat in [
    ("BT-D085", "evaluation_validity", "PRIMARY anchor: compositional-alignment diagnostic (GenEval)."),
    ("BT-D087", "evaluation_validity", "PRIMARY anchor: preference-methodology anchor (Pick-a-Pic)."),
    ("BT-D088", "evaluation_validity", "PRIMARY anchor: FAD-limits anchor for audio/music."),
    ("BT-D092", "evaluation_validity", "PRIMARY anchor: decomposed video-quality dimensions (VBench)."),
    ("BT-D093", "evaluation_validity", "PRIMARY anchor: intrinsic-faithfulness extension (VBench-2.0)."),
    ("BT-D131", "evaluation_validity", "PRIMARY anchor: physics-commonsense benchmark with validity ceiling (VideoPhy)."),
]:
    r = sel("PRIMARY", "evaluation", lane, f"SELECTED PRIMARY {rat}")
    r["discovery_id"] = did
    A[did] = r
for did, lane, rat in [
    ("BT-D083", "evaluation_validity", "SUPPORTING interpretation-limits anchor at abstract level (FID; body barrier declared)."),
    ("BT-D084", "evaluation_validity", "SUPPORTING metric-validity caution (Inception Score)."),
    ("BT-D086", "evaluation_validity", "SUPPORTING binding-failure measurement (T2I-CompBench)."),
    ("BT-D089", "evaluation_validity", "SUPPORTING intelligibility substrate at snippet level (LibriSpeech; barrier declared)."),
    ("BT-D090", "evaluation_validity", "SUPPORTING similarity-evaluation substrate (GE2E)."),
    ("BT-D129", "evaluation_validity", "SUPPORTING lip-sync methodology lane (Wav2Lip)."),
    ("BT-D130", "evaluation_validity", "SUPPORTING validity-critique bound (AV-HuBERT metrics)."),
    ("BT-D135", "evaluation_validity", "SUPPORTING vendor-neutral measurement vocabulary (DuplexBench)."),
]:
    r = sel("SUPPORTING", "evaluation", lane, f"SELECTED SUPPORTING {rat}")
    r["discovery_id"] = did
    A[did] = r
# ---- convergence ----
for did, lane, rat in [
    ("BT-D095", "multimodal_convergence", "PRIMARY anchor: unified text+speech modelling case (AudioPaLM)."),
    ("BT-D096", "multimodal_convergence", "PRIMARY anchor: unified-token convergence probe (AnyGPT)."),
    ("BT-D097", "multimodal_convergence", "PRIMARY anchor: modality-composition mechanism (CoDi)."),
]:
    r = sel("PRIMARY", "convergence", lane, f"SELECTED PRIMARY {rat}")
    r["discovery_id"] = did
    A[did] = r
for did, lane, rat in [
    ("BT-D094", "multimodal_convergence", "SUPPORTING convergence-architecture precedent (Unified-IO, generation scope)."),
    ("BT-D098", "multimodal_convergence", "SUPPORTING provenance standard at homepage level (C2PA; spec barrier declared)."),
    ("BT-D099", "multimodal_convergence", "SUPPORTING provenance-mechanism comparator (SynthID)."),
]:
    r = sel("SUPPORTING", "convergence", lane, f"SELECTED SUPPORTING {rat}")
    r["discovery_id"] = did
    A[did] = r
# ---- closed capstones: all SUPPORTING capability/workflow context ----
CAPSTONES = {
    "BT-D100": ("capstone-image", "Open/local few-step runtime case (FLUX.2 klein; vendor claims quarantined)."),
    "BT-D101": ("capstone-image", "Documented generation/editing/reference surface (FLUX.2 help)."),
    "BT-D102": ("capstone-image", "Spatial/design grounding direction (Seedream 5.0 Pro)."),
    "BT-D103": ("capstone-image", "Iterative-editing closed workflow (ChatGPT Images 2.5)."),
    "BT-D104": ("capstone-image", "Reasoning+generation boundary case (Nano Banana 2)."),
    "BT-D105": ("capstone-image", "Native image surface limits/eval (Gemini 3.1 Flash Image card)."),
    "BT-D106": ("capstone-image", "Lifecycle-only comparator (Imagen deprecation; MAYBE screening)."),
    "BT-D107": ("capstone-speech", "Native realtime-speech case (GPT-Live)."),
    "BT-D108": ("capstone-speech", "API voice-model surface (deployment/latency authority)."),
    "BT-D109": ("capstone-speech", "Native-audio limits/eval card (Gemini 3.8 Audio)."),
    "BT-D110": ("capstone-audio", "Scene-level audio convergence probe (Seed Audio 1.0)."),
    "BT-D111": ("capstone-music", "Closed music card with architecture/eval disclosure (Lyria 3.5)."),
    "BT-D112": ("capstone-music", "Product-line context (Lyria hub; mechanism defers to card)."),
    "BT-D113": ("capstone-music", "Open-weight mechanism anchor (Stable Audio 3)."),
    "BT-D114": ("capstone-music", "Version/lifecycle authority (Suno notes; MAYBE screening)."),
    "BT-D115": ("capstone-music", "Commercial workflow direction (Suno v6)."),
    "BT-D116": ("capstone-music", "Secondary closed comparator (ElevenLabs; MAYBE screening)."),
    "BT-D117": ("capstone-video", "Clip-to-storytelling transition case (Seedance 2.5)."),
    "BT-D118": ("capstone-video", "Closed comparator with benchmark authority (Veo)."),
    "BT-D119": ("capstone-video", "Shared-foundation convergence case (FLUX 3)."),
    "BT-D120": ("capstone-video", "UNUSED (HOLD below: body blocked; excluded from packages)."),
    "BT-D076": ("capstone-video", "Joint-AV foundation claim at abstract level (Movie Gen; method sections gated)."),
    "BT-D121": ("capstone-video", "Workflow/control/runtime comparator (Runway Gen-4.5)."),
    "BT-D122": ("capstone-video", "Production comparator with version binding (Luma Ray3; INSPECT screening)."),
    "BT-D123": ("capstone-video", "Dated subversion datapoint (Ray 3.2; INSPECT screening)."),
    "BT-D125": ("capstone-video", "UNUSED (HOLD below: body blocked; excluded from packages)."),
    "BT-D126": ("capstone-video", "Historical/lifecycle record (Sora 2)."),
    "BT-D127": ("capstone-video", "Discontinuation guidance (lifecycle dates)."),
    "BT-D128": ("capstone-video", "API deprecation boundary (lifecycle dates)."),
}
for did, (lane, rat) in CAPSTONES.items():
    if did in ("BT-D120", "BT-D125"):
        continue
    if "UNUSED" in rat:
        raise ValueError(f"stale capstone entry: {did}")
    r = sel("SUPPORTING", "capstones", lane, f"SELECTED SUPPORTING closed capability/workflow case, architecture non-inference: {rat}")
    r["discovery_id"] = did
    A[did] = r
# ---- X reception ----
r = sel("SUPPORTING", "reception", "x-reception", "SELECTED SUPPORTING reception/deployment/counter-signal record only (27 audited observations, LOW_SIGNAL preserved, no technical authority, no ranking).")
r["discovery_id"] = "BT-D139"
A["BT-D139"] = r
# ---- HOLD: body-blocked, no fabrication ----
for did, rat in [
    ("BT-D024", "HOLD pending successful repository-body retrieval (identity rebound to CompVis; no version binding yet)."),
    ("BT-D072", "HOLD pending Phenaki body access (OpenReview wall); masked-prior comparison unresolved."),
    ("BT-D091", "HOLD pending ITU Recommendation text access (gated)."),
    ("BT-D120", "HOLD pending Kling IR body fetch (timeouts); no press substitution."),
    ("BT-D125", "HOLD pending rendered Wan-hub fetch (JS shell)."),
]:
    r = hold(f"{rat}")
    r["discovery_id"] = did
    A[did] = r


PACKAGES = [
    dict(package_id="arch-representation", title="表現と圧縮：生成可能にする短縮の歴史",
         purpose="Establish representation as the first-class axis: why raw pixels/waveforms/frames are expensive sequences and how continuous latents, discrete codebooks, RVQ neural codecs, semantic/acoustic hierarchies, and spatiotemporal tokenizers made media tractable, with compression/fidelity/editability bounds.",
         primary=["BT-D001", "BT-D002", "BT-D006", "BT-D007", "BT-D009", "BT-D010"],
         supporting=["BT-D003", "BT-D004", "BT-D005", "BT-D008", "BT-D012"],
         req=["BT-O01"], order=1,
         bounds=["Compression-ratio/token-rate claims bind stated configs only; semantic-vs-acoustic split preserved."]),
    dict(package_id="arch-paradigms", title="生成パラダイムと目的関数：AR・GAN・拡散・フローの分岐",
         purpose="Trace generative paradigms with architecture kept distinct from objective: autoregressive pixels/transformers, adversarial generation and its retained hybrid roles, DDPM/score-SDE/EDM, latent diffusion, DiT/SiT, flow matching/rectified flow, consistency/distillation; each transition answers bottleneck/mechanism/improvement/trade-off/inheritance.",
         primary=["BT-D013", "BT-D015", "BT-D016", "BT-D019", "BT-D020", "BT-D021", "BT-D023", "BT-D025", "BT-D027", "BT-D028", "BT-D029", "BT-D030"],
         supporting=["BT-D014", "BT-D017", "BT-D018", "BT-D022", "BT-D026"],
         req=["BT-O02"], order=2,
         bounds=["U-Net vs Transformer is architecture; diffusion vs flow is objective; solver/distillation is inference. No cross-condition ranking."]),
    dict(package_id="arch-conditioning", title="条件づけとアライメント：テキスト・ガイダンス・参照",
         purpose="Cover text conditioning, frozen-encoder findings, classifier and classifier-free guidance with scale trade-offs, expert ensembles, and audio alignment; distinguish training-time conditioning, inference-time guidance, adapters, and in-context reference.",
         primary=["BT-D011", "BT-D032", "BT-D033", "BT-D036"],
         supporting=["BT-D031", "BT-D034", "BT-D035"],
         req=["BT-O03"], order=3,
         bounds=["Prompt adherence is not perceptual or distribution quality; encoder findings are era-specific."]),
    dict(package_id="arch-control", title="制御と参照：空間・参照・主体性の保存",
         purpose="Cover spatial control (ControlNet lineage, adapters), reference/image-prompt conditioning, few-shot identity preservation, efficient adaptation, and time-varying audio/video control; separate control-signal fidelity from sample quality.",
         primary=["BT-D038", "BT-D039", "BT-D042"],
         supporting=["BT-D037", "BT-D040", "BT-D041", "BT-D043"],
         req=["BT-O04"], order=4,
         bounds=["Control signals as generation controls only (no perception-history retelling); identity claims bind stated protocols."]),
    dict(package_id="arch-editing", title="生成から編集へ：保存を伴う改変の系譜",
         purpose="Treat editing as distinct from de-novo generation: stroke guidance, mask-conditioned inpainting, latent local editing, attention-map editing, optimisation editing, instruction editing, and one-shot video editing; capture preservation target, locality, reference constraints, failure modes.",
         primary=["BT-D044", "BT-D045", "BT-D049", "BT-D050"],
         supporting=["BT-D046", "BT-D047", "BT-D048"],
         req=["BT-O05"], order=5,
         bounds=["Preservation claims bind mask/region definitions; per-image optimisation costs stated."]),
    dict(package_id="arch-speech", title="音声・声の系譜：波形からEnd-to-End、Codec LM、全二重へ",
         purpose="Trace speech from WaveNet raw autoregression through Tacotron/VITS end-to-end, neural vocoders, codec language models, flow-matching generation/editing, versatile controllable TTS, unified translation-task speech, open streaming TTS, and full-duplex dialogue with latency methodology; modality-specific evaluation throughout.",
         primary=["BT-D051", "BT-D056", "BT-D058", "BT-D060", "BT-D061", "BT-D062", "BT-D134"],
         supporting=["BT-D052", "BT-D053", "BT-D054", "BT-D055", "BT-D057", "BT-D059", "BT-D132", "BT-D133"],
         req=["BT-O07", "BT-O06"], order=6,
         bounds=["WER/intelligibility, naturalness, speaker similarity, prosody, latency/streaming kept distinct; vendor evals quarantined."]),
    dict(package_id="arch-music", title="音楽・一般音響の系譜：Codec LMと潜在拡散、二つの道",
         purpose="Trace music from hierarchical autoregression through semantic/acoustic staging to controllable single-stage codec music and latent-diffusion audio with theory-attribute control; separate acoustic fidelity, text/music alignment, long-horizon form, lyrics coherence, and continuation/inpainting; validate metrics against human preference.",
         primary=["BT-D063", "BT-D065", "BT-D066", "BT-D068"],
         supporting=["BT-D064", "BT-D067", "BT-D069", "BT-D136"],
         req=["BT-O08", "BT-O11"], order=7,
         bounds=["No ranking across incompatible durations/protocols; FAD/CLAP limits preserved."]),
    dict(package_id="arch-video", title="映像の系譜：時間的一貫性からメディア基盤へ",
         purpose="Trace video from factorized diffusion and cascaded super-resolution through variable-length tokenizers (barrier noted), data-efficient transfer, motion adapters, staged open models, and open-weight MoE deployment; separate local fidelity, short-range coherence, long-range structure, identity permanence, and continuation.",
         primary=["BT-D070", "BT-D071", "BT-D073", "BT-D075"],
         supporting=["BT-D074", "BT-D077", "BT-D124", "BT-D138"],
         req=["BT-O09", "BT-O06"], order=8,
         bounds=["Maximum supported duration is not demonstrated coherence; version/checkpoint currency binding required."]),
    dict(package_id="arch-temporal", title="長時間・同期・編集： fidelity を超える評価軸",
         purpose="Consolidate temporal/long-horizon structure across modalities: identity/object permanence, lip/AV synchronization with validity critique, physics/commonsense evaluation with ceilings, multi-round dialogue measurement, and edit preservation; single-sample claims never stand for long-horizon competence.",
         primary=["BT-D131"],
         supporting=["BT-D129", "BT-D130", "BT-D135"],
         req=["BT-O06", "BT-O11"], order=9,
         bounds=["Lip-sync scores are not comparable truth across conditions; physics scores read against validity ceilings."]),
    dict(package_id="arch-runtime", title="実行と配備：サンプリング・遅延・VRAM・公開性",
         purpose="Cover runtime economics: distillation/consistency/adversarial few-step lineages, mobile one-step with device timings, independent klein measurement anchoring vendor claims, and open vs closed deployment boundaries; never compare unbound numbers as a leaderboard.",
         primary=["BT-D078", "BT-D081", "BT-D082", "BT-D137"],
         supporting=["BT-D079", "BT-D080"],
         req=["BT-O10"], order=10,
         bounds=["All runtime numbers bind hardware/config/sampling budget; single-lab limits stated."]),
    dict(package_id="arch-evaluation", title="評価の方法論：指標は交換可能ではない",
         purpose="Establish evaluation as a full package: distribution metrics with limits, compositional diagnostics, human-preference methodology, audio distances with embedding dependence, speech corpora/similarity substrates, video multidimensional suites, and preference-vs-automatic validation; bind version/condition/population for every score.",
         primary=["BT-D085", "BT-D087", "BT-D088", "BT-D092", "BT-D093"],
         supporting=["BT-D083", "BT-D084", "BT-D086", "BT-D089", "BT-D090"],
         req=["BT-O11"], order=11,
         bounds=["No cross-condition leaderboard; vendor benchmarks quarantined until reproduced."]),
    dict(package_id="arch-convergence", title="収束問題：統合モデルか連携する専門家群か",
         purpose="Keep the convergence question evidence-backed: unified encoder-decoder multitask, speech-text LLMs, discrete any-to-any probes, composable diffusion, provenance mechanisms (C2PA/SynthID at stated authority), with TS-002/TS-003 boundary discipline; no predetermined conclusion.",
         primary=["BT-D095", "BT-D096", "BT-D097"],
         supporting=["BT-D094", "BT-D098", "BT-D099"],
         req=["BT-O12"], order=12,
         bounds=["Perception/VLM history excluded; convergence claims stay question-framed."]),
    dict(package_id="arch-capstones", title="2025-2026 capstone群：能力・workflow・lifecycleの証拠",
         purpose="Retain current systems strictly as capability/workflow/availability/lifecycle cases with vendor claims attributed and undisclosed architecture never inferred; lifecycle transitions (Imagen deprecation, Sora shutdown, Wan open-freeze) as convergence evidence; open-weight anchors carry mechanism weight.",
         primary=[],
         supporting=["BT-D076", "BT-D100", "BT-D101", "BT-D102", "BT-D103", "BT-D104", "BT-D105", "BT-D106", "BT-D107", "BT-D108", "BT-D109", "BT-D110", "BT-D111", "BT-D112", "BT-D113", "BT-D114", "BT-D115", "BT-D116", "BT-D117", "BT-D118", "BT-D119", "BT-D121", "BT-D122", "BT-D123", "BT-D126", "BT-D127", "BT-D128"],
         req=["BT-O04", "BT-O05", "BT-O06", "BT-O07", "BT-DUMMY-NONE"], order=13,
         bounds=["No architecture/training/tokenizer inference from product behavior; version/date binding required."]),
    dict(package_id="arch-reception", title="受容と counter-signal：現場の証拠",
         purpose="Preserve community reception/deployment/counter-signal evidence (local friction, consistency reception, side-by-side comparisons, runtime constraints, edit damage, drift/lip-sync failures) with LOW_SIGNAL lanes intact; any technical follow-up must be rebound to primary authority.",
         primary=[],
         supporting=["BT-D139"],
         req=["BT-O10", "BT-O06"], order=14,
         bounds=["No popularity ranking; X never establishes architecture, dates, licenses, prices, scores, or causal claims."]),
]


def main() -> None:
    import re
    expected = {f"BT-D{i:03d}" for i in range(1, 140)}
    assert set(A) == expected, sorted(expected - set(A))[:10]
    sel_count = sum(1 for v in A.values() if v["disposition"] == "SELECTED")
    assert sel_count == 134, sel_count
    # package coverage: every SELECTED in exactly one package as primary xor supporting
    covered = {}
    for p in PACKAGES:
        for did in p["primary"] + p["supporting"]:
            assert did not in covered, f"double-homed: {did}"
            covered[did] = p["package_id"]
        assert not (set(p["primary"]) & set(p["supporting"])), p["package_id"]
        for did in p["primary"] + p["supporting"]:
            assert A[did]["disposition"] == "SELECTED", did
    selected = {d for d, v in A.items() if v["disposition"] == "SELECTED"}
    assert set(covered) == selected, sorted(selected - set(covered))[:10]
    assert len(PACKAGES) == 14
    # fix placeholder requirement tag
    for p in PACKAGES:
        p["req"] = [r for r in p["req"] if r != "BT-DUMMY-NONE"]
    arch = {
        "editorial_thesis": ("高次元連続メディア（画素・波形・フレーム・動き・同期音）を生成可能にしたのは、表現・予測/生成目的・条件づけ・制御/編集・時間構造・サンプリング/実行・評価の選択の進化である。"
                              "本Specialは有名製品のカタログではなく、画像・音声・音楽・映像の各モダリティで「何がボトルネックで、何が変わり、何が改善し、何が悪化し、何が継承されたか」を技術史として構成する。"),
        "architecture_goals": [
            "Representation-first: raw/media compression/tokenization to be a first-class historical axis.",
            "Keep architecture, objective, and sampling/inference procedure distinct in every chapter.",
            "Treat editing/preservation as a separate technical problem from de-novo generation.",
            "Give speech, music, and video their own mechanism/runtime/evaluation stories (no image-appendix).",
            "Preserve metric-validity boundaries; never rank across incompatible conditions.",
            "Keep closed products as capability/workflow/lifecycle cases with attribution; no hidden-architecture inference.",
            "Keep the convergence question evidence-backed and open; enforce the TS-002/TS-003 boundary.",
        ],
        "page_plan": {"target_pages": 80, "max_pages": 96,
                      "notes": "Planning envelope 64-96 pages (guidance, not hard cap): representation 8 / paradigms 10 / conditioning 5 / control 5 / editing 5 / speech 9 / music 7 / video 9 / temporal 4 / runtime 5 / evaluation 7 / convergence 4 / capstones 8 / reception 2 / front+back matter 6 (sum 84 incl. rounding); prefer justified depth over artificial compression; do not pad to reach target."},
        "packages": [{
            "package_id": p["package_id"], "title": p["title"], "purpose": p["purpose"],
            "primary_discovery_ids": p["primary"], "supporting_discovery_ids": p["supporting"],
            "must_cover_requirements": p["req"], "boundaries": p["bounds"],
            "drafting_order": p["order"], "profile_extensions": {}, "publication_extensions": {},
        } for p in PACKAGES],
        "selected_exceptions": [],
        "profile_extensions": {},
        "publication_extensions": {},
    }
    doc = {"schema_version": "2.0-rc1", "issue_id": ISSUE_ID,
           "runner": {"provider": "Muse", "model": "Spark (Luna/Work execution role)",
                      "invocation": "Anti-thinness selection over rebound Evidence + 43-entry transition ledger; closed products as capability context; X as reception context; 5 blocked HOLD; Sol readback authority",
                      "generated_at": "2026-09-25T01:30:00Z"},
           "assignments": [{**v, "discovery_id": k} for k, v in sorted(A.items())],
           "architecture": arch}
    out = Path(OUT_REL)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from collections import Counter
    print(json.dumps({"assignments": len(doc["assignments"]),
                      "dispositions": dict(Counter(v["disposition"] for v in A.values())),
                      "packages": len(PACKAGES)}, indent=2))


if __name__ == "__main__":
    raise SystemExit(main())

