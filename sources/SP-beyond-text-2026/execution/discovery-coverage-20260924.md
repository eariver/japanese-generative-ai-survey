# TS-002 Discovery coverage accounting — first run + r2 refresh (for Sol completeness review)

Collector run: `beyond-text-discovery-r1` observed `2026-09-23T17:30:00Z`
Refresh run: `beyond-text-discovery-r2` observed `2026-09-24T09:43:32Z` (Sol r1 bounded repair: date fixes + gap-fill)
Canonical JSONL: `discovery/discovery-v2.jsonl` (128 BASE records pass 0 + 10 GAP_FILL records pass 1 = 138)
Acceptance: `discovery/discovery-accepted-v2.json` (Core-built, graph validated)
X manifest: `external/x/x-source-intake-v2.json` (`CHATGPT_DECIDES / NOT_REQUIRED / COMPLETE`, zero runs)

## 1. Dimension coverage (D01–D12 as BT-O01–BT-O12; cross-tagged)

| Obligation | Dimension | Records | Primary/tech authorities | Historical anchors | Current-system coverage | Unresolved gaps |
|---|---|---|---|---|---|---|
| BT-O01 | representation/tokenization | 15 | 12 papers, 1 repo, 1 doc, 1 announcement | VAE/VQ-VAE/VQ-VAE-2/VQGAN/dVAE/SoundStream/EnCodec/DAC/AudioLM/MAGVIT/Wan2.2-VAE | Wan2.2-VAE, Stable Audio 3 (SAME), Lyria latents | FLUX-VAE internals (closed) |
| BT-O02 | paradigms/objectives | 35 (+1: FiVE diffusion-vs-RF editing) | 30 papers, 1 repo, 2 announcements, 1 doc | GAN/DCGAN/StyleGAN(x2)/PixelRNN/ImageTransformer/DDPM/DDIM/ScoreSDE/EDM/LDM/DiT/SiT/FlowMatching/RectifiedFlow/Consistency/ADM | FLUX.2-klein, FLUX 3, Wan2.2-MoE | Closed-denoiser internals |
| BT-O03 | conditioning/alignment | 12 | 8 papers, 1 announcement, 2 docs, 1 card | CLIP/CFG/GLIDE/ADM/DALL-E/Imagen/eDiff-I/CLAP | Seedream 5.0, Nano Banana 2 | None blocking |
| BT-O04 | control/reference/identity | 17 | 11 papers, 4 announcements, 2 docs | ControlNet/T2I-Adapter/IP-Adapter/DreamBooth/LoRA/SPADE/MotionCtrl/MusicControlNet | Seedream, Seedance refs, Luma keyframe, FLUX.2 refs | Identity-metric depth |
| BT-O05 | editing/preservation | 22 (+1: FiVE RF-vs-diffusion editing bench) | 11 papers, 7 announcements, 3 docs | SDEdit/RePaint/Blended/P2P/Imagic/InstructPix2Pix/Tune-A-Video/Voicebox | GPT Image 2.5, Seedream, Suno edit, Stable Audio edit, Runway Aleph, Seedance edit | RF-vs-diffusion editing now benchmarked (FiVE); pure-generation ablations thin |
| BT-O06 | temporal/long-horizon | 21 | cross-tagged speech/music/video/current | Phenaki/MovieGen/VDM/ImagenVideo via cross-tags | Seedance 30s+continuation, Suno long-form, Lyria structure, Seed Audio scene | AV-sync event-timing still vendor-claim (G08 partial) |
| BT-O07 | speech/voice | 27 (+4: F5-TTS, CosyVoice 2, Moshi, DuplexBench) | 15 papers, 4 announcements/docs/cards | WaveNet/Tacotron(x2)/FastSpeech/HiFi-GAN/VITS/YourTTS/VALL-E(x2)/Voicebox/Seed-TTS/Seamless | GPT-Live, GPT-Realtime API, Gemini 3.8 Audio, Seed Audio 1.0 | Open lane now grounded (F5-TTS/CosyVoice 2); streaming methodology via Moshi/DuplexBench |
| BT-O08 | music/audio | 20 (+1: Suno listening-study bench) | 10 papers, 6 announcements/docs/cards | Jukebox/DiffWave/AudioLM/MusicLM/MusicGen/AudioLDM/StableAudioOpen/Mustango | Lyria 3.5, Stable Audio 3, Suno v6, ElevenLabs | Suno v3-era independent study added; v5/v6 + ElevenLabs independent eval still thin |
| BT-O09 | video | 29 (+3: Wav2Lip, VideoPhy, FiVE) | 10 papers/repos, 12 announcements/docs | VDM/ImagenVideo/Phenaki/MakeAVideo/AnimateDiff/SVD/MovieGen/Sora/MAGVIT/TuneAVideo | Seedance 2.5, Veo, FLUX 3, Kling 3.0, Runway 4.5, Luma Ray3(x2), Wan2.2, Sora lifecycle | Physics validity now benchmarked (VideoPhy); Wan 3.0 closed (G05), Sora mechanism (G06) retained |
| BT-O10 | runtime/deployment | 29 (+4: F5-TTS RTF, CosyVoice 2 streaming, Moshi latency, klein-4B bench) | 9 papers, 10 announcements/docs/repos | DDIM/Consistency/LCM/LCM-LoRA/ADD/ProgressiveDistill/MobileDiffusion | FLUX.2-klein speed, GPT-Realtime latency, Wan2.2-TI2V-5B local, Stable Audio local | klein now independently measured (G04 partial); streaming latencies methodologically grounded, vendor leaderboard still prohibited |
| BT-O11 | evaluation/validity | 24 (+5: Wav2Lip, AV-HuBERT critique, VideoPhy, DuplexBench, Suno bench) | 13 papers/spec, 3 cards/docs | FID/IS/GenEval/T2IComp/Pick-a-Pic/FAD/LibriSpeech/GE2E/MUSHRA/VBench(x2)/CLIP/CLAP | Lyria card, Gemini cards, Veo eval | Lip-sync grounded + validity-bounded (G08 partial); physics benchmarked (G11 filled); duplex turn-taking measurable (G10) |
| BT-O12 | convergence/boundary | 13 | 4 papers, 7 announcements/docs, 2 specs | Unified-IO/AudioPaLM/AnyGPT/CoDi/C2PA/SynthID | Nano Banana 2, FLUX 3, Seedream, Seed Audio, Gemini audio, GPT-Live | None blocking; TS-003 leakage checked |

## 2. Modality coverage

| Modality | Records | Share | Note |
|---|---|---|---|
| image | 56 | 41% | legitimately largest historical lane; does not hide others (see below) |
| speech | 22 | 16% | dedicated WaveNet→native-realtime lineage + open/streaming/methodology lanes (r2) |
| audio (general) | 10 | 7% | codec/diffusion shared with speech/music |
| music | 13 | 9% | dedicated Jukebox→Lyria/StableAudio/Suno lineage + independent listening study (r2) |
| video | 30 | 22% | dedicated VDM→Seedance/Veo/Wan lineage + lip-sync/physics/editing benchmarks (r2) |
| crossmodal | 7 | 5% | CLIP/LoRA/convergence/provenance |

Speech+audio+music+video = 75 records (54%) vs image 56 (41%). No modality is a token appendix.

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

FID+limits, IS precursor, GenEval, T2I-CompBench, Pick-a-Pic preference, FAD+limits, WER/LibriSpeech, speaker-similarity/GE2E, MUSHRA method, VBench, VBench-2.0, CLIP/CLAP alignment, model-card methodologies, plus r2 additions: Wav2Lip LSE-C/D + ReSyncED, AV-HuBERT AVSu/AVSm/AVSv validity critique, VideoPhy SA/PC + VideoCon-Physics, DuplexBench turn-taking/latency criteria, Suno 12-model listening study + metric correlation, FiVE diffusion-vs-RF editing bench. No leaderboard assembled; vendor attribution preserved.

## 6. Negative space / unresolved gaps

See `raw/discovery-negative-space-2026-09-24.md` (G01–G12, r2 dispositions appended). Headline after r2: closed-architecture unknowns retained (G01/G02/G06), Wan 3.0 closed line (G05), music-structure metrics (G07); G09/G10/G11 filled as methodology, G03/G04/G08/G12 partially filled with explicit residual negative space; capstone chronology repaired (26 fixed, 3 verified-unchanged, 10 dynamic pages recorded unknown).

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

r2 re-check (2026-09-24): all 14 checks remain PASS after gap-fill (image share 43%→41%; speech/music/video methodology lanes strengthened, not diluted; no rankings constructed; no undisclosed-architecture inference added).

## 8. Authority/type counts

101 PRIMARY_PAPER, 3 PRIMARY_REPO, 16 PRIMARY_DOC, 13 PRIMARY_ANNOUNCEMENT, 2 PRIMARY_SPEC, 3 PRIMARY_MODEL_CARD.
Unique locators: 137 (Wan2.2 github shared by BT-D012/BT-D124 by design: representation anchor + open-capstone roles).
128 records BASE/pass 0 + 10 records GAP_FILL/pass 1 (BT-D129–D138); no X/community records (deferred).
