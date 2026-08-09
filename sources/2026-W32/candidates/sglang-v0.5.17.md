---
candidate_id: sglang-v0.5.17
issue_id: "2026-W32"
title: "SGLang v0.5.17"
record_type: screening-record
status: late-breaking-verified-primary
discovered_via: [manual-oss-scan]
event_date: "2026-08-08"
verification_status: primary-screened
---

# SGLang v0.5.17 — Screening Record

## Verified primary event
The official SGLang GitHub Releases page records **v0.5.17 released on 2026-08-08**.

Primary source:
- https://github.com/sgl-project/sglang/releases

The release highlights 582 PRs from 194 contributors and includes day-0 support for both Kimi K3 and MiniMax H3.

## Kimi K3 support
The release documents native Kimi K3 serving support including DCP, DSpark speculative decoding, chunked-prefill PP with TP decode, KDA-aware prefix caching, HiCache L2, LoRA on quantized weights, reasoning/tool-call support and OpenAI-compatible serving.

SGLang states this path was verified on NVIDIA GB300 and AMD MI35x.

## MiniMax H3 support
SGLang-Diffusion supports H3 task profiles including:
- text-to-video-and-audio (`t2va`);
- first/last-frame conditioning (`fl2va`);
- image/video/audio reference conditioning (`ref2va`, including video-to-video).

The release states H3 serving was verified on:
- B200 (TP2 + Ulysses4);
- H100 (TP2 + Ulysses2);
- 2× RTX 5090 with layerwise offload.

## Additional systems significance
v0.5.17 also introduces an initial native Rust frontend and multiple serving/runtime changes, but those should only be expanded if the issue later selects the release as a broader systems story.

## Timing boundary
This is **post-cutoff Late Breaking** for W32. It is especially useful because it independently connects two model candidates already in the pool—Kimi K3 and MiniMax H3—to a concrete serving ecosystem event.

## Screening note
Promote to a verified Late Breaking OSS candidate. The strongest W32 value is not merely the version number, but the rapid translation of new frontier/open models into production-oriented serving paths.