# W43 r2 consumption note 04 — speech/video + Ming (DC-07/DC-08, SUBSTANTIVELY_CONSUMED 2026-10-24)

## Mistral Voxtral 3 (Oct 20) — announcement + docs read
- Family: Small Transcribe 3 (flagship batch + diarization) + Mini 4B + Realtime + Speech 3 TTS + LiveKit SDK (listen→reason→speak single pipeline, turn <1s, barge-in). 50+ langs transcription, 35+ langs/50+ dialects speech; diarization, context biasing, end-of-turn (acoustic+semantic); Pro Voice 30min adaptation.
- Vendor evidence consumed: FLEURS 45 WER Small 4.1/4.0 (vs MS 4.6/4.5, Whisper large-v3 higher); diarization cpWER Small 18.4/Mini 18.6 (vs Pyannote 19.0); keyphrase recall 94.6/81.4; AA realtime WER; realtime sub-500ms 40+ langs; TTS internal evals (Voice Code Bench 300 prompts, pronunciation 300 sentences, multilingual 377 prompts/11 langs, expressive 237 prompts; judge gemini-3.8-flash; prices from vendor pages; generated 2026-10-20). Voice Code Bench hill-climb examples (email/phone, flight £1881, pregnancy name, passport) show v1→v3 error repair.
- Price: Mini $0.0035/min, Small $0.004, Realtime $0.008, Speech $13/M chars; agent API $0.04 (Small 4) / $0.08 (larger); EU/US/global + self-deploy (sovereignty). Distinct from Le Chonk grounding (W42 INSPECT c3439ff4 gap stands).

## ElevenLabs Eleven Realtime (Oct 20, Min Kim) — blog read
- v1 Mini (natural/low-cost) + v1 Max (reasoning/tool-use); single speech-to-speech; 90+ langs, 17k+ voices; ElevenAgents + Realtime API (OpenAI Realtime compat: endpoint+model swap; WebSocket only; migration guide).
- Independent AA (consumed as reported): BBA Max 98.8/Mini 75.9; TTFA 0.57/0.62s; Full-Duplex Mini 95.8/Max 94.1; Arena Max 998/Mini 988; tool-use Max 87.1/Mini 60.3 (Max for heavy tool-calling). Pareto accuracy-vs-speed framing is vendor's; AA is independent but unreproduced here.

## fal FLUX 3 Max (Oct 19) — PR + model page + X corroboration (secondary search)
- PR Oct 19 3:46pm ET (fal): with BFL on FLUX 3 foundation (post-train + RL + inference opt); text/image/keyframes-to-video; 10s video 10.95s vs Seedance 2.5 277.80s (22x) at same Elo + 11.5x vs FLUX 3 (126.44s); Elo 1139 tied #1 image-to-video (AA, 4868 votes per r1; preliminary snapshot).
- Discrepancy recorded: press release 10.95s vs model page/blog/X 12.45s average (10s 720p). Unite.AI repeats 10.95s/126.44s; flux3max.app notes 12.45s vs 10.95s + Elo 1138 Oct 20 board + pricing $0.0425/s 720p / $0.0725/s 1080p (Oct 15–Nov 7) → $0.17/$0.29. All vendor-reported; quality claim is image-to-video only; VB notes vendor timings.
- Event identity: Oct 19 platform availability is IN; Klein image weights Oct 15 OUT (separate). Never conflate.

## InclusionAI Ming-3.0-tts (Oct 2026 month precision + repo Oct 19 IN)
- Repo created Oct 19 07:03:25Z IN, pushed Oct 21; 197 stars/13 forks/10 commits; MIT license. Family: 0.5B dense + tiny MoE 7.9B-A1.3B (Ling V3); multilingual + voice cloning/design + NL control + 14 paralinguistic tags; 7 langs + Sichuanese/Cantonese; tasks (seed/multilingual/paralinguistic/podcast/basic/emotion/dialect/freeform/voice_design/ip).
- Independent AA consumed as reported: Controlled Voice 1069 (1st open-weights, 13th overall); Pronunciation Robustness 93.2% (1st overall; shorthand 96.5%, exact-seq 90.6%); Provider Voice 1188 (3rd open-weights, 17th overall). Vendor tables: NVBench single-tag SOTA (6/6 with tiny), dialect SOTAs, emotion splits; historical Ming-omni-tts retains some records (noted, no SOTA overclaim).
- Date precision: News says [2026.10] month-only; repo creation Oct 19 is the IN event anchor. Roadmap (vLLM-Omni, tech report) pending. Day-level model release date NOT proven — record month precision honestly.
