# W43 primary bundle 04 — speech, video and multimodal (claim-level, 2026-10-24)

Collector run: `20261024T120000Z-muse-r1` / collector_id `primary-webfetch`
Observed at: `2026-10-24T12:00:00Z`
Capture class: `CLAIM_LEVEL_DERIVED_NOTE__NO_ORIGINAL_BYTES`.

## 1. Mistral Voxtral 3 (Oct 20, 2026 12:00 UTC) — IN-WINDOW, BODY SEARCH-CONFIRMED
- URLs: https://mistral.ai/news/voxtral-3, https://docs.mistral.ai/models/voxtral-small-transcribe-3-0, .../voxtral-mini-transcribe-3-0, .../voxtral-mini-tts-3-0, CellCog 2026-10-20, MarkTechPost 2026-10-20.
- Claims (vendor, unvalidated):
  - 3 transcription (Small flagship, Mini 4B, Realtime) + Speech 3 TTS + LiveKit voice-agent SDK (listen/reason/speak one pipeline).
  - 50+ langs transcription, 35+ langs/50+ dialects speech; diarization, context biasing, turn detection (audio+semantic).
  - Pricing: Mini $0.0035/min, Small $0.004, Realtime $0.008, Speech $13/M chars; EU/US/global endpoints; public preview.
  - SOTA transcription claim vs Whisper-large-v3/Gemini 3.5/GPT-Transcribe/Scribe v2 (vendor).
- Status: CAPTURED_BUT_UNCONSUMED (announcement + docs not fully read). Evidence must fetch announcement + docs + eval details.
- Note: distinct from W42 INSPECT Le Chonk grounding (c3439ff42a96e600); Voxtral does NOT resolve Le Chonk weights/methods gap.

## 2. ElevenLabs Eleven Realtime (Oct 20, 2026) — IN-WINDOW, BODY SEARCH-CONFIRMED
- URLs: https://elevenlabs.io/blog/realtime (Oct 20), CXFoundation, i-scoop 2026-10-22, SoftPage 2026-10-22.
- Claims:
  - v1 Mini (natural/low-cost) + v1 Max (reasoning/tool-use); single speech-to-speech models; 90+ langs, 17k+ voices.
  - TTFA 0.57s Max / 0.62s Mini (vendor); AA independent: BBA spoken reasoning Max 98.8/Mini 75.9, tool-use Max 87.1/Mini 60.3, Full-Duplex Mini 95.8/Max 94.1 (AA via secondary, unvalidated here).
  - Speaks OpenAI realtime protocol (switching implication per i-scoop).
- Status: CAPTURED_BUT_UNCONSUMED. Evidence must fetch blog + AA pages + protocol docs.

## 3. fal FLUX 3 Max (Oct 19, 2026) — IN-WINDOW, BODY SEARCH-CONFIRMED
- URLs: PRNewswire 2026-10-19 15:46 ET (fal), VentureBeat 2026-10-19 15:29 PT, https://bfl.ai/models/flux-3-video.
- Claims (issuer + fal, unvalidated):
  - Post-trained by fal Research with BFL on FLUX 3 foundation (RL + inference optimization); text/image/keyframes-to-video; via fal inference platform (pay-go).
  - Speed: 10s clip 12.45s vs 277.80s Seedance 2.5 (fal comparison, 22x); 11.5x vs FLUX 3; quality: 1139 Elo / 4868 votes AA Video Arena (fal-reported), #1-tier image-to-video claim.
- Status: CAPTURED_BUT_UNCONSUMED. Evidence must fetch fal post + BFL model page + AA arena snapshot.

## 4. Room for Qwen/FLUX-Klein background
- FLUX 3 Image Klein weights Oct 15 (OUT, W42 SELECTED context); Qwen-Image-2.1 Pro/Turbo Oct 9 (OUT, background).
- Must not conflate Oct 19 FLUX 3 Max video with Oct 15 Klein image weights.

## Gaps
- Voxtral/ElevenLabs audio evals, FLUX arena methodology, license/availability terms: UNCONSUMED.
- No independent audio/video repro in this pass.
