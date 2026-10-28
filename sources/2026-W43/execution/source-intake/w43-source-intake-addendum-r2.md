# W43 r2 source-intake addendum (2026-10-24, DC-02..DC-09)

Supersedes nothing; appends to r1 (`w43-source-intake-summary-r1.md` preserved). Run `20261024T133000Z-muse-r2`.

## Newly acquired + substantively consumed (rendered-body level unless noted)
- OpenAI securing training (Oct 23): offline containment, defense in depth, Sep 20 DNS, hundreds of billions tokens red-team, Kata CVE-2026-24834/gVisor/Moby/kernel CVEs, Oct 1 resume, safety-case gating. Curl HTML 403 (failed raw); webfetch render consumed.
- OpenAI bio agents (Oct 21): GPT-Rosalind thousands agents, 32 min, CRISPR atlas, Tsc1/Tsc2 + DCTN1/cholesterol, 700 vs 11 refs, 75% preference, bioRxiv/HF/GitHub provenance. Consumed.
- OpenAI low-resource (Oct 19): MultiLangBench 20 langs (Astra 87.4 vs 26.8; COBOL 10.9→72.1), COBOL migration byte-parity (86.6 low / 97.9 high vs 5.4), GitHub eval open. Consumed.
- 1Password for Agents (Oct 22 blog + press): approve-on-device/autofill, Muse/Grok rolling out, Duet/ChatGPT/Townie + 9 coming soon, .com only, 1.6B/200k context. Consumed.
- MOSS-Image: README consumed (5B DiT, layout/text, 4K prompts, Base/SFT, ComfyUI/SGLang/vLLM day-0, community distills); repo meta raw (created Oct 16 01:18 OUT); Kohaku trainer consumed (LyCORIS, 6GB, sm70-120/Arc, err/LPIPS) + meta raw (created Oct 18 IN); report arXiv 2610.23374 submitted Oct 16 OUT (announce Oct 19 IN); MOSI API Oct 20 IN.
- MemT-1.0: abs consumed (GDN-2, MoS, 34B tokens, Nano/Flash, 1.86x@128K + 66x storage, 11 benches) + repo consumed (family table, SGLang, licenses split) + meta raw (created Oct 19 IN). v1 Oct 19 IN / v2 Oct 20 IN.
- Ming-3.0-tts: README consumed (0.5B + 7.9B-A1.3B, MIT, 7 langs+dialects, 14 tags, AA ranks, vendor tables, roadmap pending) + meta raw (created Oct 19 IN). News month-only [2026.10] — day unproven, recorded honestly.
- Duet (Oct 21): full announcement consumed (preview/waitlist/US Pro-Max, Opus 5.5, VM browser, checks-hours, approval gates, securities/money off-limits, 6000+ connectors, Link/Shop Pay, 1Password soon, classifier, work-first limits; Oct 22 Cloud + Oct 23 Cowork/Safety as related).
- DeepSeek 1017 (Oct 17): API docs consumed (wish-driven RL, examples, Search&Fetch $0.75/1k + free to Oct 31 16Z, HF/ModelScope, Harness ≥v0.2.1-rc.1, footnote harnesses).
- DeepInfer: README consumed (21.5k★/2.4k forks/4 commits, Apache-2.0, offline V4.1-only, kernels, DSpark defaults, SWA replay, async/batch-invariant/deterministic, structured outputs, SM100+Ascend, missing KV/disagg/LB explicit, build reqs, 4+64 GPU benches, vLLM credit) + meta raw (created Oct 16 OUT → repo OUT vs Oct 20 announce IN).
- Nemotron E4B (Oct 23): research page consumed (64K ctx corrected from r1 1M, 35 langs, 40%/80% fewer, full 5-capability tables incl. Tau2 55.1/RULER 87.0, RTX/Jetson AIPerf, RLVR/RLHF 2:1, DFlash +21%, checkpoints, deploy matrix, Reachy demo; OpenMDW-1.1 OSI-unproven).
- Voxtral 3 (Oct 20): announcement+docs consumed (50+ langs, Small SOTA FLEURS/diarization/keyphrase, realtime sub-500ms, TTS $13/M + evals, Pro Voice 30min, LiveKit SIP/WebRTC <1s, pricing, sovereign). Distinct from Le Chonk.
- Eleven Realtime (Oct 20): blog consumed (Mini/Max speech-to-speech, 90+ langs/17k voices, BBA 98.8/75.9, TTFA 0.57/0.62, Full-Duplex 95.8/94.1, Arena 998/988, tool-use 87.1/60.3, OpenAI-protocol compat).
- FLUX Max (Oct 19): PR + model page + X + VB consumed; discrepancy 10.95s (PR) vs 12.45s (page/blog/X) recorded; Elo 1139 (1138 Oct 20 board) tied #1 image-to-video only; pricing $0.0425/0.0725 → $0.17/0.29; vendor-only.
- TanStack 1.0 (Oct 23): blog consumed (stable core vs 0.x harness, 23 adapters, 8 UI, 143 contrib, codemod, threadId, sessions/steer, runCli non-sandbox, AG-UI).
- GitHub Teams/metrics (Oct 23): changelogs consumed (Teams @github flow + Nov 16 legacy retire; totals_by_client schema + server-side + additive).
- ARC Argon (Oct 13 OUT): page consumed (v1 98.5/v2 91.2 high, v3 49.8/97.5, incomplete Std coverage, $2/$10). OUT background; Qwen3.8 row ≠ identity proof.

## Raw-archived bytes (new in r2)
- X HTML Kimi status (208731B, SHA 0891bc1e, 2026-10-23T17:15:24.000Z embedded) + 5 GitHub API JSONs (~240B ea). 19 rendered bodies consumed without original HTML (honestly labeled). 0 independent repros.

## Chronology corrections applied (r2)
- Kimi: 13:15:24 EDT = 17:15:24Z (19-digit ID), 4h44m36s before cutoff — safely IN.
- AM-Bench v1 Oct 16 21:46:19Z OUT / v2 Oct 20 15:40:19Z IN (delta unchecked); OR-License Oct 16 18:13:25Z OUT; MOSS report Oct 16 12:27:37Z OUT (announce Oct 19 IN); MemT v1 Oct 19 IN / v2 Oct 20 IN.
- MOSS repo Oct 16 OUT vs trainer Oct 18 IN / report-announce Oct 19 IN / API Oct 20 IN; DeepInfer repo Oct 16 OUT vs announce Oct 20 IN.
- ARC Oct 13 OUT; Ming month-only precision; Step 5/Qwen/Wonder/Spark/Nemotron-Super-VL OUT preserved.

## Counts
- Discovery r2: 51 records (36 r1 preserved byte-identical + 15 new), 51/51 schema PASS, IDs unique.
- r1 0 consumed → r2 19 rendered bodies consumed + 6 byte-archived raw (1 X HTML + 5 API JSON). Independent repros still 0 (marked zero).
