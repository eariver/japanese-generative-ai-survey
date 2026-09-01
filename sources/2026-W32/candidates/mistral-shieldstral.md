---
candidate_id: mistral-shieldstral
issue_id: "2026-W32"
title: "Mistral Shieldstral"
record_type: screening-record
status: candidate-reviewed
discovered_via: [grok-v0.4, primary-source-screening, reaction-pass]
event_date: "2026-07-28"
verification_status: full-paper-reviewed
evidence_record: "../evidence/papers/shieldstral.md"
---

# Mistral Shieldstral — Screening Record

## Primary source
- arXiv: https://arxiv.org/abs/2607.25857

## Full-review resolution
Full-paper evidence is recorded in `../evidence/papers/shieldstral.md`.

Shieldstral is a 3B multimodal safety classifier designed to accept free-form natural-language policy queries at inference time. The authors train it on approximately 54.1M mixed public/synthetic samples and evaluate text, policy-adaptability and multimodal safety.

Important boundaries established by review:
- the reported 84.9 text F1, 91.3 adaptability F1 and 83.8 multimodal F1 are author-reported benchmark results;
- competing systems use different output/reasoning/threshold settings, so aggregate F1 does not imply identical inference conditions;
- training and evaluation taxonomies differ structurally, but most broad harm domains still overlap;
- millions of samples are LLM-generated or LLM-filtered;
- headline benchmark averages do not establish adaptive-adversary robustness or universal real-world moderation quality.

## Existing social evidence
- `../evidence/social/x-community-reaction-normalized-v0.1.md`
- Community reaction is modest; no representative independent adversarial test was captured in the Reaction Pass.

## Screening state
Retain as a reviewed Safety/Multimodal candidate. Its value is primarily technical—runtime policy specification in a compact model—rather than X momentum.