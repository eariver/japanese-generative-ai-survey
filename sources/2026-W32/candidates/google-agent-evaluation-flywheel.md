---
candidate_id: google-agent-evaluation-flywheel
issue_id: "2026-W32"
title: "Google Agent Quality Flywheel / evaluation skill methodology"
record_type: screening-record
status: candidate
discovered_via: [manual-web-scan]
event_date: "2026-08-04?"
verification_status: primary-source-captured-date-needs-normalization
---

# Google Agent Quality Flywheel — Screening Record

## Collected information
Google Developers published a developer-facing agent-evaluation workflow that can be driven from a coding agent as a skill. The described loop is:
1. Prepare evaluation data.
2. Run inference / collect traces.
3. Grade with adaptive AutoRaters or custom metrics.
4. Analyze failures, including Automatic Loss Analysis for larger failure sets.
5. Optimize, rerun and compare against the previous baseline.

A notable design rule is that the optimizer does not grade its own work; evaluation is kept decoupled to reduce metric gaming.

## Primary source
- https://developers.googleblog.com/driving-the-agent-quality-flywheel-from-your-coding-agent/

## Related primary context
- Google Developers' earlier Agent Skills / evaluation material documents skill-driven evaluation and progressive-disclosure patterns.

## Unverified / pending
- Normalize the exact publication timestamp against the W32 window.
- Capture exact service/product naming and any preview/GA status needed for publication.

## Screening note
Keep as a methodological candidate. It is relevant even if the exact post date lands outside W32 because it may represent a broader agent-evaluation trend; chronology must be resolved before editorial selection.