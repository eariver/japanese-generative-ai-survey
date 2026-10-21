# W42 Core Evidence compatibility recovery — Sol decision proposal (NOT execution authority)

Date: 2026-10-17 JST. Frozen Core production/survey-core-v2 `774dd39a951c9ac3818e83dfffd4c7666efb0a20`. W42 accepted up to `CANDIDATES_NORMALIZED`.
Review source: `sources/2026-W42/execution/reviews/sol-w42-r7-core-blocker-and-editorial-authority-audit-20261017.md`.

## Recommended decision

**Request explicit Human approval for a narrow, separate Core v2 maintenance exception.** Do not change the frozen Core in the W42 production branch. The maintenance revision must be independently tested and reviewed before deliberately integrating a pinned new Core version to W42. Without this authorization, W42 remains blocked; do not bypass validation, forge acceptance, or invalidate canonical upstream records.

## Isolation and proposed technical scope (for review, not yet permission to edit)

1. Fix the legacy `prepare_evidence_package` State-basis check to recognize canonical agent-first bridge checkpoint provenance and per-transition implementation SHAs while preserving all agent State integrity checks. Prefer reusing `survey_agent_control_v2.verify_agent_state_basis` in a specifically tested adapter, **not** globally relaxing `validate_state_semantics`. Verify all downstream Core APIs which consume Evidence use a compatible trust basis.
2. Reconcile Discovery source_type and Evidence `SOURCE_CLASS_MAP` at the formal contract boundary. 17/50 current W42 source records have 10 unsupported labels. Adopt minimal, provenance-based classes with unit tests: community/X-originated reports remain SOCIAL observations even when mentioning an official blog/paper; direct first-party body joins via exact authority supplement as appropriate; explicit secondary claims remain SECONDARY. Do NOT promote X evidence to PRIMARY_PAPER just from a `PAPER_LEAD` name, and do not map all `COMMUNITY_*` blindly.
3. Establish a lawful Evidence task/neutral view for the `w42-grok-x-ledger-20261017` non-editorial binder: Core requires one result per non-DROP Discovery, hence 50 Evidence tasks/Views. The binder must never inflate substantive article or Materiality counts and no fabricated model claim may be emitted.
4. Account for additional potential downstream gates: W42 r7's 49 local cards are **not** Core schema; all claim/sources must be represented by Core Evidence Card entity-role, source binding and verification structures. Where new first-party bodies are needed, obtain exact raw content and create a valid `Evidence Authority Supplement` rather than pretending derived bundles are original source bytes. Repair 8 editorial claims mislinked to unrelated bundle-09.
5. Materiality and Completeness must be built using exact accepted Evidence+Views bases; then independently substantiate each of 28 proposed MATERIAL rationales and every nonselected high-signal candidate. 16-page sketch is not accepted; compare an evidence-appropriate 20–24 page scope with explicit per-package depth.

## Regression and safety acceptance tests

- **Read-only old-state cases:** W41 RELEASED (published record), W42 CANDIDATES_NORMALIZED. A production prior issue must not require rewriting any historical State.
- **State tamper cases:** modified checkpoint bytes/hash, source-root escape, history rewrite, incorrect implementation or contract identity all fail closed. No global bypass of State validators.
- **Source map:** enumerate all 50 W42 source_types and representative W33/W34/W41 historical types, assert correct authority class and fail-closed on genuinely unknown/malicious values.
- **Evidence cardinality:** 50 tasks, 50 card results, 50 views; 49 editorial candidates + 1 neutral provenance binder; no silent DROP, no binder article.
- **Formal Core process:** prepare → card schema/evidence acceptance → views → Materiality/Completeness → genuine stage validation; exact SHA/checkpoint chains. W42 Production State and Core must not advance until these tests pass on an authorized reviewed Core integration.
- Independent post-fix reviewer review required; no architecting/publishing before Sol Materiality/Selection review.

## Alternatives / decision impact

A. **Narrow Core maintenance exception (RECOMMENDED)**: shared compatibility repair prevents repeating the fault in later weeks; costs explicit Core exception, review and integration. A Core revision would be new pinned authority and must be represented as such, NOT falsely called unchanged old Core.
B. **Maintain absolute immutable Core**: no currently validated end-to-end path. W42 pauses at CANDIDATES_NORMALIZED until a lawful non-Core workaround is demonstrated under all guards. Upstream 17-type normalization alone does not fix State-basis defect.

## Pending Human authorization

This document is a proposal and does NOT approve Core changes, creation of maintenance branches, stage invalidations, human review gates or draft publication.
