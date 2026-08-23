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

### Runtime synchronization before code changes

The canonical redesign branch initially still represented the pre-pilot Core snapshot plus redesign documentation, while current `main` had accumulated 111 commits during W33/SP001 production. Those commits contained the exact runtime paths that failed in real production, including interactive Drafting/Synthesis, Selection/Architecture, semantic-publication/quality, work-branch control, Weekly publication rendering, LONGFORM renderer/style repairs and related tests.

Redesigning only the older snapshot would therefore have produced a false repair target.

The branch histories were reconciled explicitly:

- prior redesign head: `e4794648589d32bbffbaafa29fdb58e26b86f55e`;
- current production `main`: `198c69703dba7b4f2f7b1d914d88f72bf7d7d887`;
- merge base: `a009ad28c2c2ed61ab90022a93b23eb053cadb3b`;
- an explicit merge tree adopted current `main` runtime wholesale and overlaid only the audited redesign authority/plan/policy/worklog files;
- canonical redesign merge commit: `5812c5761ed5e94bda503bf522dba96299255250`.

This makes the failed real-production runtime the implementation baseline while preserving the redesign history as the other merge parent.

PR #445 records the synchronization operation. It is not an edition-production execution trigger.

### Initial workflow inventory observation

The synchronized `.github/workflows/` tree confirms extensive production mutation in Actions. Examples include `prepare-*`, `apply-*`, `revise-*`, interactive Drafting/Evidence/Selection/Semantic Publication/Semantic Quality, work-branch state control and numerous cadence-specific layout/pagination repair workflows.

Do not mass-delete these before the new hot path is established. First classify them and remove their authority from the redesigned Core hot path; then retire legacy mutation workflows only after replacement responsibility is explicit and regression-protected.

### Initial Publication Boundary observation from synchronized runtime

The real W33 renderer (`scripts/survey_weekly_semantic_publication_v2.py`) directly demonstrates the #433/#434 defect:

- it writes `Core v2 Evidence: ...; materiality: ...` into reader-facing bibliography notes;
- it requires internal `profile_synthesis.current_interpretation` to survive byte-for-byte inside the final reader summary;
- it renders accepted Draft Result blocks directly into publication TeX;
- it derives reader bibliography directly from internal Candidate Matrix / Materiality / Discovery authority.

The real LONGFORM semantic publication path similarly assembles reader source from Draft bytes plus a structured revision object. These are useful regression examples, but they must cease to be the authoritative publication-authoring boundary.

The next implementation step is to define the smallest cross-profile reader-facing source/QA/candidate contract that lets ChatGPT author publication bytes directly while keeping deterministic provenance and exact-byte verification.
