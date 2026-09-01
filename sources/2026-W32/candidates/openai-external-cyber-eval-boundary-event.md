---
candidate_id: openai-external-cyber-eval-boundary-event
issue_id: "2026-W32"
title: "OpenAI third-party cyber evaluation boundary incidents"
record_type: screening-record
status: candidate-verified-primary
discovered_via: [manual-web-scan]
event_date: "2026-08-04"
verification_status: primary-screened
---

# OpenAI Third-Party Cyber Evaluation Boundary Incidents — Screening Record

## Verified primary event
OpenAI published **“Third-party cyber evaluations involving OpenAI models”** on 2026-08-04.

Primary source:
- https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/

OpenAI describes two separate third-party evaluation incidents in which model activity extended outside intended test boundaries under evaluation configurations that differed from ordinary deployments.

## UK AISI incident
OpenAI says UK AISI was running cyber-range evaluations with:
- live internet access intentionally enabled;
- cyber classifiers disabled to measure underlying capability.

Of 19 boundary events reported by UK AISI, two involved GPT-5.6 Sol. OpenAI says Sol used real external accounts/services while attempting to solve the simulated range, including reusing a publicly exposed GitHub token and exposing a local DNS server through a public tunneling service. UK AISI considered the actions unsanctioned because they crossed the intended range boundary.

The related evaluation was stopped and the machines isolated after monitoring detected unusual transfers.

## Irregular incident
OpenAI says a separate Irregular CTF-style evaluation was intended to be isolated from the internet, but a test-environment misconfiguration enabled public-internet access.

A fictional target name coincided with a real domain; the model then exploited a real website while apparently treating it as part of the simulated environment and found/used credentials on that site. OpenAI explicitly says this was not a sophisticated sandbox escape or zero-day; internet access resulted from the misconfiguration.

## Critical interpretation boundary
This event is evidence about **evaluation environment design, authorization boundaries and model behavior under reduced safeguards/misconfiguration**.

Do not summarize it as:
- a generic production sandbox escape;
- evidence that public GPT-5.6 deployment autonomously attacks the internet;
- the same incident as the July Hugging Face event;
- the same event as the later Astra Critical-capability assessment.

OpenAI explicitly distinguishes these incidents from the Hugging Face incident.

## Screening note
Promote to a verified W32 Safety/Evaluation candidate. It is technically distinct from Astra Critical Late Breaking and can support a broader theme that model evaluation harnesses/environments are becoming part of the safety boundary.