---
candidate_id: minimax-h3
issue_id: "2026-W32"
title: "MiniMax H3"
record_type: screening-record
status: candidate
discovered_via: [grok-v0.4, primary-source-screening, reaction-pass]
event_date: "2026-07-31"
verification_status: primary-screened-plus-weight-artifact-confirmed
---

# MiniMax H3 — Screening Record

## Collected information
- MiniMax announced H3 on 2026-07-31 as a general omni-modal generative model.
- MiniMax describes multimodal context over text, image, video and audio; native stereo audio; up to 15-second / 2K video; and unified generation/editing/reference workflows.
- At launch, MiniMax said model weights were planned within the following few days, subject to applicable laws and regulations.
- MiniMax also documented remaining limitations in multimodal-context understanding, model scale and some image-detail cases.

## Primary sources
- MiniMax launch / technical overview: https://minimaxi.com/blog/minimax-h3
- SGLang H3 cookbook: https://github.com/sgl-project/sglang/blob/main/docs/cookbook/diffusion/MiniMax/MiniMax-H3.mdx
- SGLang v0.5.17 release: https://github.com/sgl-project/sglang/releases/tag/v0.5.17

## Weight / checkpoint verification update — 2026-08-10
The launch article only promised a future weight release; it must not be used to claim launch-day weight availability.

By the current compilation pass, SGLang's official H3 cookbook explicitly references the public model IDs:
- Hugging Face: `MiniMaxAI/MiniMax-H3`
- ModelScope: `MiniMax/MiniMax-H3`

The cookbook describes released checkpoint partitions `FL2VA` and `Ref2VA` and maps them to public task profiles:
- `t2va`: text to video and audio;
- `fl2va`: first/last-frame conditioning;
- `ref2va`: image/video/audio reference conditioning, including video-to-video use.

This is sufficient to move the evidence state from "weights planned" to "public weight/checkpoint artifact confirmed by a primary downstream serving source." The exact timestamp at which the repository first became public is still not pinned in the current evidence and should not be invented.

## Technical design claims from MiniMax
MiniMax names the following design elements:
- Contextual Omni Representation;
- H3-VAE;
- H3-Omni Transformer;
- In-context Regeneration.

MiniMax reports a 4x sequence-length benefit from the new tokenizer/VAE design and nearly 30% end-to-end training-throughput improvement from its heterogeneous understanding/generation training setup. These remain vendor-reported technical claims, not independently reproduced measurements.

## Existing evidence
- Technical: `sources/2026-W32/evidence/technical/verified-candidates-v0.1.md`
- Social: `sources/2026-W32/evidence/social/x-community-reaction-normalized-v0.1.md`

## Community reaction collected
- Before cutoff, MiniMax official activity emphasized open weights and a ComfyUI-oriented session.
- Immediately post-cutoff, independent posts showed RTX 5090 ComfyUI timing tests, distilled LoRA workflows, prompt-rewriter GGUF tooling and multi-shot + audio examples.

## Claim boundaries
- The collected GGUF evidence concerns `MiniMax-H3-Prompt-Rewriter-LoRA`, not proof that the H3 core model itself was distributed as GGUF.
- Community timing/VRAM/quality observations are not official hardware requirements or independent model-quality benchmarks.
- ComfyUI Partner Nodes are API-backed integration and should not automatically be equated with native local-weight execution; local execution claims need the specific workflow/repository evidence attached to them.

## Post-cutoff serving follow-through
SGLang v0.5.17 (2026-08-08) adds day-0 H3 support. Its cookbook documents H3 serving on B200/H100 and a verified 2x RTX 5090 (32 GB each) layerwise-offload recipe. This is Late Breaking for W32 and should remain visibly separated from the pre-cutoff model chronology.

## Unverified / pending
- Exact public-weight publication timestamp.
- Independent quality / consistency comparisons.
- Generalized consumer-hardware requirements beyond the specific serving/workflow configurations already evidenced.

## Screening note
Keep as a feature candidate. The strongest W32 angle is the chronology: 7/31 model announcement -> weight/checkpoint availability and workflow focus by the cutoff -> post-cutoff local/serving experimentation. Preserve the difference between artifact date and technical-community momentum date.