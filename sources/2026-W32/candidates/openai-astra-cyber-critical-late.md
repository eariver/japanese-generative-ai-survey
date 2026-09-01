---
candidate_id: openai-astra-cyber-critical-late
issue_id: "2026-W32"
title: "OpenAI Astra — Critical cyber capability concern / strengthened controls"
record_type: screening-record
status: late-breaking-verified-primary
source_window: post-cutoff
discovered_via: [grok-v0.2]
event_date: "2026-08-07"
verification_status: primary-screened
---

# Astra Cyber Capability Concern — Screening Record

## Verified event
OpenAI published **“Responding to the next frontier of critical cyber capabilities”** on 2026-08-07.

Primary source:
- https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/

OpenAI states that recent internal evaluations of Astra, an upcoming model, showed significant advances in agentic coding and cybersecurity and led OpenAI to conclude that it **could not rule out Critical cyber capability** under the Preparedness Framework.

OpenAI defines the Critical cyber threshold in terms of autonomous zero-day exploit development against many hardened real-world critical systems, or end-to-end novel cyberattack strategies against hardened targets from a high-level goal. OpenAI says Astra had not been definitively classified Critical at publication time; rather, preliminary results were strong enough that Critical capability could not be ruled out while assessment continued.

## Verified response measures
OpenAI says it:
- strengthened isolated testing, network/tool restrictions, model-weight protections/encryption, monitoring/detection and sandboxing;
- **paused internal activities involving Astra that did not meet the strengthened control requirements**;
- implemented universal monitoring for risky actions and misalignment across Astra agentic applications, including training and evaluation;
- planned work with government agencies and selected AI-safety organizations for capability testing;
- planned recommended security controls for third-party testing partners.

## Important boundaries
- This does **not** establish that Astra has definitively reached the Preparedness `Critical` threshold.
- Astra was **not** the pre-release model involved in the July Hugging Face incident; OpenAI explicitly distinguishes them.
- GPT-5.6 Sol had previously been assessed at the High rather than Critical threshold.

## Relation to other W32 OpenAI cyber events
OpenAI also published on 2026-08-04 about third-party cyber evaluations involving boundary-crossing behavior under reduced-safeguard or misconfigured test environments. That is tracked separately from this Astra capability assessment.

## Relation to Astra mathematics candidate
The mathematics/reasoning results remain tracked in `openai-astra.md`. This record is a separate safety/cyber event concerning the same upcoming model.

## Screening note
Promote to a **verified Late Breaking candidate**. Any article wording must preserve the distinction between “cannot rule out Critical” and “classified as Critical.”