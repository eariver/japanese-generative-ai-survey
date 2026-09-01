---
candidate_id: deepseek-v4-flash-0731
issue_id: "2026-W32"
title: "DeepSeek-V4-Flash-0731"
record_type: screening-record
status: candidate
discovered_via: [grok-v0.4, primary-source-screening]
event_date: "2026-07-31"
verification_status: primary-screened
---

# DeepSeek-V4-Flash-0731 — Screening Record

## Collected information
- DeepSeek's official changelog records a 2026-07-31 update named `DeepSeek-V4-Flash-0731`.
- DeepSeek states it keeps the same architecture and size as the preview version and was re-post-trained, with the update applying to the Flash API.
- An official Hugging Face repository exists and documents local serving with vLLM / SGLang; the repository/model weights are licensed under MIT.
- Vendor benchmark claims need harness-aware interpretation.

## Primary sources
- https://api-docs.deepseek.com/updates/
- https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731

## Existing evidence
- Technical: `sources/2026-W32/evidence/technical/verified-candidates-v0.1.md`
- Social: `sources/2026-W32/evidence/social/x-community-reaction-normalized-v0.1.md`

## Community reaction collected
- All three representative technical-reaction posts collected by the Reaction Pass are post-cutoff.
- They discuss cost/performance, ARC-AGI/coding examples and relative capability ceilings.

## Unverified / pending
- Independent benchmark reproduction under comparable harness / reasoning-effort settings.
- Exact chronology if API update and public-weight publication need hour-level separation.

## Screening note
Keep as a candidate. Treat the 7/31 technical event separately from post-cutoff community reaction.