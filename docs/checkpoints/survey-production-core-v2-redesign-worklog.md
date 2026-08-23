# Survey Production Core v2 — Redesign implementation worklog

Status: `ACTIVE / IMPLEMENTATION STARTED`  
Started: 2026-08-23 JST  
Working branch: `refactor/survey-production-core-v2`  
Authority: `docs/survey-production-core-v2-redesign-authority.md`  
Design audit: `docs/survey-production-core-v2-redesign-preimplementation-audit.md`

## Purpose

This log records the actual Core v2 redesign implementation work performed after the W33/SP001 production-validation failure and the subsequent pre-implementation design audit.

It is an implementation worklog, not production-edition provenance. W33/SP001 remain failed production-validation evidence and must not be rewritten to look like successful runs.

## Operating rules

- Follow the audited redesign authority and Actions responsibility policy.
- Keep shared Core, Research Profile, Publication Profile, and edition/series authority orthogonal.
- Do not overfit implementation to W33/SP001 topic structure.
- GitHub Actions may remain only for clearly advantageous deterministic/reproducible/security-sensitive work; authoring/editorial reasoning belongs to ChatGPT.
- Preserve exact provenance, Human Gates, Publication Candidate byte identity, Freeze/Release integrity, and historical Evidence rigor.
- Record material implementation decisions, changed responsibility boundaries, regression coverage, and validation results here. Do not record every tool call.

## Planned implementation workstreams

1. Responsibility / orchestration simplification
2. Reader-facing Publication Boundary
3. Editorial / semantic / visual QA separation
4. Publication Candidate atomic revision/finalization
5. Edition execution-record bootstrap support
6. Grok single-task-file / Drive-path handoff cleanup
7. Regression + cross-profile compatibility validation
8. Fixed-head final audit

## 2026-08-23 — implementation start

### Starting state

- W33 and SP001 real-production validation are treated as failed Core v2 acceptance evidence.
- Pre-implementation redesign audit completed and design-level inconsistencies were corrected before implementation.
- Normal Human Gates remain `ARCHITECTURE_REVIEW` and `PUBLICATION_PREVIEW`.
- `refactor/survey-production-core-v2` remains the canonical redesign branch.

### Immediate implementation sequence

Begin by inventorying current Core scripts/workflows and classifying production mutation paths. The first concrete goal is to remove the architectural dependency on GitHub Actions/PRs as routine production-stage authoring or state-mutation triggers, while retaining CI/build/release verification where GitHub-side execution has a clear benefit.

No production edition is resumed during this implementation phase.
