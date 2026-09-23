# TS-002 Discovery coverage accounting — first run (for Sol completeness review)

Collector run: `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`
Canonical JSONL: `discovery/discovery-v2.jsonl` (128 BASE records, pass 0)
Acceptance: `discovery/discovery-accepted-v2.json` (Core-built, graph validated)
X manifest: `external/x/x-source-intake-v2.json` (`CHATGPT_DECIDES / NOT_REQUIRED / COMPLETE`, zero runs)

## 1. Dimension coverage (D01–D12 as BT-O01–BT-O12; cross-tagged)

| Obligation | Dimension | Records | Primary/tech authorities | Historical anchors | Current-system coverage | Unresolved gaps |
|---|---|---|---|---|---|---|
| BT-O01 | representation/tokenization | 15 | 12 papers, 1 repo, 1 doc, 1 announcement | VAE/VQ-VAE/VQ-VAE-2/VQGAN/dVAE/SoundStream/EnCodec/DAC/AudioLM/MAGVIT/Wan2.2-VAE | Wan2.2-VAE, Stable Audio 3 (SAME), Lyria latents | FLUX-VAE internals (closed) |
| BT-O02 | paradigms/objectives | 34 | 30 papers, 1 repo, 2 announcements, 1 doc | GAN/DCGAN/StyleGAN(x2)/PixelRNN/ImageTransformer/DDPM/DDIM/ScoreSDE/EDM/LDM/DiT/SiT/FlowMatching/RectifiedFlow/Consistency/ADM | FLUX.2-klein, FLUX 3, Wan2.2-MoE | Closed-denoiser internals |
| BT-O03 | conditioning/alignment | 12 | 8 papers, 1 announcement, 2 docs, 1 card | CLIP/CFG/GLIDE/ADM/DALL-E/Imagen/eDiff-I/CLAP | Seedream 5.0, Nano Banana 2 | None blocking |
| BT-O04 | control/reference/identity | 17 | 11 papers, 4 announcements, 2 docs | ControlNet/T2I-Adapter/IP-Adapter/DreamBooth/LoRA/SPADE/MotionCtrl/MusicControlNet | Seedream, Seedance refs, Luma keyframe, FLUX.2 refs | Identity-metric depth |
| BT-O05 | editing/preservation | 21 | 11 papers, 7 announcements, 3 docs | SDEdit/RePaint/Blended/P2P/Imagic/InstructPix2Pix/Tune-A-Video/Voicebox | GPT Image 2.5, Seedream, Suno edit, Stable Audio edit, Runway Aleph, Seedance edit | Video-edit benchmarks |
| BT-O06 | temporal/long-horizon | 21 | cross-tagged speech/music/video/current | Phenaki/MovieGen/VDM/ImagenVideo via cross-tags | Seedance 30s+continuation, Suno long-form, Lyria structure, Seed Audio scene | AV-sync metrics (G08) |
| BT-O07 | speech/voice | 23 | 15 papers, 4 announcements/docs/cards | WaveNet/Tacotron(x2)/FastSpeech/HiFi-GAN/VITS/YourTTS/VALL-E(x2)/Voicebox/Seed-TTS/Seamless | GPT-Live, GPT-Realtime API, Gemini 3.8 Audio, Seed Audio 1.0 | Open-runtime evidence (G09), streaming methodology (G10) |
| BT-O08 | music/audio | 19 | 10 papers, 6 announcements/docs/cards | Jukebox/DiffWave/AudioLM/MusicLM/MusicGen/AudioLDM/StableAudioOpen/Mustango | Lyria 3.5, Stable Audio 3, Suno v6, ElevenLabs | Suno/ElevenLabs architecture (G02), structure metrics (G07) |
| BT-O09 | video | 26 | 10 papers/repos, 12 announcements/docs | VDM/ImagenVideo/Phenaki/MakeAVideo/AnimateDiff/SVD/MovieGen/Sora/MAGVIT/TuneAVideo | Seedance 2.5, Veo, FLUX 3, Kling 3.0, Runway 4.5, Luma Ray3(x2), Wan2.2, Sora lifecycle | Wan 3.0 closed (G05), Sora mechanism (G06) |
| BT-O10 | runtime/deployment | 25 | 9 papers, 10 announcements/docs/repos | DDIM/Consistency/LCM/LCM-LoRA/ADD/ProgressiveDistill/MobileDiffusion | FLUX.2-klein speed, GPT-Realtime latency, Wan2.2-TI2V-5B local, Stable Audio local | Independent measurements (G04, G10) |
| BT-O11 | evaluation/validity | 19 | 13 papers/spec, 3 cards/docs | FID/IS/GenEval/T2IComp/Pick-a-Pic/FAD/LibriSpeech/GE2E/MUSHRA/VBench(x2)/CLIP/CLAP | Lyria card, Gemini cards, Veo eval | AV-sync (G08), physics validity (G11) |
| BT-O12 | convergence/boundary | 13 | 4 papers, 7 announcements/docs, 2 specs | Unified-IO/AudioPaLM/AnyGPT/CoDi/C2PA/SynthID | Nano Banana 2, FLUX 3, Seedream, Seed Audio, Gemini audio, GPT-Live | None blocking; TS-003 leakage checked |

## 2. Modality coverage

| Modality | Records | Share | Note |
|---|---|---|---|
| image | 55 | 43% | legitimately largest historical lane; does not hide others (see below) |
| speech | 18 | 14% | dedicated WaveNet→native-realtime lineage |
| audio (general) | 10 | 8% | codec/diffusion shared with speech/music |
| music | 12 | 9% | dedicated Jukebox→Lyria/StableAudio/Suno lineage |
| video | 26 | 20% | dedicated VDM→Seedance/Veo/Wan lineage |
| crossmodal | 7 | 5% | CLIP/LoRA/convergence/provenance |

Speech+audio+music+video = 66 records (52%) vs image 55 (43%). No modality is a token appendix.

## 3. Historical transition coverage (bottleneck → mechanism → benefit → trade-off → inheritance)

- Raw pixels/waveforms/frames → VAE/VQ/codec compression → tractable sequences → reconstruction bound (BT-D001–D010).
- AR/GAN → DDPM/score → stable high-fidelity sampling → step cost (BT-D013–D022, D030).
- Pixel diffusion → latent diffusion → resolution scaling → autoencoder bound (BT-D023–D024).
- U-Net → DiT/transformer denoisers → scaling → compute cost (BT-D025–D026).
- Diffusion → flow/rectified/consistency → fewer steps → distillation drift (BT-D027–D029, D078–D082).
- No guidance → classifier/CFG → adherence → diversity cost (BT-D030–D034).
- No control → ControlNet/adapters/reference → fidelity → preservation conflicts (BT-D036–D043).
- De-novo only → inpaint/instruction/region/video-edit → workflows → boundary artifacts (BT-D044–D050).
- Waveform/pipeline TTS → parallel/end-to-end → latency/quality → duration-model limits (BT-D051–D057).
- TTS → codec-LM → zero-shot cloning → token-fidelity split (BT-D058–D062).
- Raw AR music → codec/staged/diffusion → minutes-long structure → structure-metric gap (BT-D063–D069).
- Image-only → space-time/cascade/tokenizer video → motion → short-clip ceiling (BT-D070–D077).
- Many-step → distill/consistency/adversarial/mobile → deployment → quality drift (BT-D078–D082).
- Single scores → decomposed/human/preference/AV → validity → condition-binding discipline (BT-D083–D093).
- Separate stacks → unified/native multimodal → shared surfaces → undisclosed-architecture caution (BT-D094–D099, capstones).

Each transition has enough authority to answer mechanism questions at Evidence stage; trade-off depth is marked per-record.

## 4. Current-capstone coverage summary

- Image/editing: FLUX.2-klein (runtime claim, vendor), FLUX.2 docs (workflow), Seedream 5.0 (multimodal design), GPT Image 2.5 (closed workflow), Nano Banana 2 + Gemini card (convergence), Imagen (lifecycle comparator). Architecture: closed except via historical inference — marked as such.
- Speech/native: GPT-Live + Realtime API docs (latency/streaming, version-bound), Gemini 3.8 Audio card (limitations/eval), Seed Audio 1.0 (scene-audio convergence). Independent eval: negative space.
- Music: Lyria 3.5 card (strong mechanism/eval authority), Stable Audio 3 (open mechanism), Suno v6 + release notes (closed workflow), ElevenLabs (secondary comparator). Architecture unknowns explicit.
- Video: Seedance 2.5 (joint AV, 30s+continuation), Veo (closed benchmark), FLUX 3 (early-access convergence), Kling 3.0 (disclosure pending), Runway 4.5 (workflow), Luma Ray3/3.2 (version-bound), Wan2.2 (open mechanism, last-open verified 2026-09-23), Sora (lifecycle: product end 2026-04-26, API removal 2026-09-24, no replacement).
- Open/closed balance: open anchors (Wan2.2, Stable Audio, SVD lineage, AnimateDiff, LDM/SD) plus closed capability cases. Sora correctly recorded as retired, not frontier.

## 5. Evaluation-methodology coverage

FID+limits, IS precursor, GenEval, T2I-CompBench, Pick-a-Pic preference, FAD+limits, WER/LibriSpeech, speaker-similarity/GE2E, MUSHRA method, VBench, VBench-2.0, CLIP/CLAP alignment, model-card methodologies. No leaderboard assembled; vendor attribution preserved.

## 6. Negative space / unresolved gaps

See `raw/discovery-negative-space-2026-09-24.md` (G01–G12). Headline items: closed-architecture unknowns (G01/G02/G06),
independent runtime/eval measurements (G03/G04/G10), Wan 3.0 closed line (G05), music-structure and AV-sync metrics
(G07/G08), open speech deployment evidence (G09), physics-evaluator validity (G11), flow ablations outside image (G12).

## 7. Anti-collapse checks (PASS/FAIL/UNKNOWN)

- [x] PASS — Image (43%) does not reduce speech/music/video to appendices (52% combined, each with own lineage).
- [x] PASS — Representation/tokenization spans image, audio, video modalities.
- [x] PASS — GAN/adversarial lineage retained (5 records) alongside diffusion/flow.
- [x] PASS — Diffusion, DiT, flow matching kept distinct (separate anchors + SiT bridge).
- [x] PASS — Speech has a real WaveNet→native-realtime lineage, not product releases only.
- [x] PASS — Music has structure/long-form sources (MusicLM, Lyria card, Suno workflow) beyond fidelity.
- [x] PASS — Video has temporal/identity/physics/multi-shot sources (VBench-2.0, Movie Gen, Seedance, MotionCtrl).
- [x] PASS — Editing is first-class across image + video + speech/audio (21 records).
- [x] PASS — Runtime has technical recipes (distillation/consistency/ADD/mobile/local), not adjectives.
- [x] PASS — Evaluation has methodology sources for image, audio/speech/music, video.
- [x] PASS — Capstones mix closed capability cases with open deployment lanes (Wan2.2, Stable Audio, AnimateDiff).
- [x] PASS — Sora recorded as retired lifecycle case with exact dates, not current product.
- [x] PASS — No demo used as proof of realism/coherence/superiority.
- [x] PASS — TS-003 perception history excluded except load-bearing conditioning/provenance (CLIP, C2PA).

## 8. Authority/type counts

92 PRIMARY_PAPER, 3 PRIMARY_REPO, 15 PRIMARY_DOC, 13 PRIMARY_ANNOUNCEMENT, 2 PRIMARY_SPEC, 3 PRIMARY_MODEL_CARD.
Unique locators: 127 (Wan2.2 github shared by BT-D012/BT-D124 by design: representation anchor + open-capstone roles).
All records BASE/pass 0; no X/community records (deferred).
