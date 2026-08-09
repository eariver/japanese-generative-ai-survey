---
candidate_id: anthropic-skill-plugin-security-scanning
issue_id: "2026-W32"
title: "Claude Code Automated Security Reviews"
record_type: screening-record
status: rejected-as-new-w32-event-context-only
original_discovered_via: [manual-web-scan]
event_date: "2026-03-16"
verification_status: primary-screened-corrected
---

# Claude Code Automated Security Reviews — Screening Record

## Initial collected note
The preliminary W32 pool contained a 2026-08-06 candidate described as security scanning for Claude Skills / Plugins.

## Primary-source resolution
Anthropic does provide **Automated Security Reviews in Claude Code**, but the durable primary documentation dates the feature to **2026-03-16**, not W32:
- https://support.claude.com/en/articles/11932705-automated-security-reviews-in-claude-code

Anthropic documents two modes:
- `/security-review` for on-demand terminal review;
- GitHub Actions for automated pull-request security review.

The documented checks include SQL injection, XSS, authentication/authorization flaws, insecure data handling and dependency vulnerabilities. Anthropic explicitly says automated reviews should complement rather than replace existing security practices and manual review.

## Correction boundary
The primary source does **not** support the collected shorthand `Skill / Plugin Security Scanning` or a new 2026-08-06 launch. Do not reinterpret the March feature as a W32 product event.

## Resolution
Preserve this record as provenance/context, but remove it from the pool of new W32 events. It may be cited as background if another W32 Agent Security story makes the feature relevant.