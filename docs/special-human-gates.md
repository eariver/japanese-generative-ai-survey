# Special Human Gate model

Status: canonical policy for future Special production from 2026-08-13 JST.

## Objective

Keep machine validation strict while minimizing unnecessary user interruptions. The pipeline may contain many deterministic state/validation gates, but normal production has only two user-interaction Human Gates.

## Gate 1 — Architecture Review

Timing: after source collection, Screening/Evidence review, Candidate Selection, clustering, and Architecture proposal generation.

The review surface should include enough information for one editorial decision:

- collection and Evidence counts / important limitations;
- major topic clusters and the proposed issue thesis;
- proposed FEATURE_CORE / SECTION_CORE / SUPPORTING_EVIDENCE / PAPER_WATCH / CHRONOLOGY / HOLD_OUT roles;
- section/package architecture and page allocation;
- important Claim Boundaries or chronology constraints that affect the issue structure.

Candidate Selection is preserved as a deterministic/auditable checkpoint and may still be stored as `APPROVED` internally, but it is **not a separate user stop**. The user approves Selection and Architecture together by approving the Architecture proposal.

Architecture approval authorizes drafting and all deterministic work necessary to reach a publication-ready PDF, including claim/chronology validation and layout-only repair.

## Gate 2 — Publication Preview

Timing: once the exact publication candidate PDF exists and all machine preflight checks pass.

The user is shown the exact PDF that will become the public release asset. Approval must be bound to its SHA-256 and approval reference.

A single Publication Preview approval authorizes, for those identical approved bytes:

1. Visual Review machine-checkpoint record;
2. Freeze record and release manifest;
3. work PR merge;
4. exact-artifact re-download and SHA verification;
5. GitHub Release publication.

Freeze and Public Release therefore remain auditable state transitions, but they are **not additional normal Human Gates**. `visual_review` is retained as a machine/provenance checkpoint name; it is not a third Human Gate. New pipeline state declares `human_gate_required_for_publication_preview=true` and `human_gate_required_for_visual_review=false`.

## Exception Gate — on demand only

An Exception Gate is not a fixed lifecycle stage. It is raised only when continuing requires a new editorial/publication decision that cannot be derived from the existing approvals.

Raise an Exception Gate when, for example:

- Evidence is materially insufficient for a reasonable Architecture;
- material sources conflict and the choice changes the story;
- the approved Architecture requires a material structural/editorial change;
- a semantic/content change is needed after Publication Preview approval;
- approved source/PDF provenance cannot be preserved;
- publication identity, scope, or correction handling must deviate from policy.

Do not raise an Exception Gate for deterministic technical recovery that preserves approved content and provenance, such as retryable CI/source collection failures, layout-only work before Publication Preview, merge-conflict resolution with byte-identical approved source/PDF, or re-running a failed publication step against the same frozen hashes.

## Machine checkpoints remain strict

The simplification applies only to user interaction. Existing machine checkpoints remain authoritative, including:

- raw source preservation;
- candidate inventory / Screening completeness;
- Evidence normalization and provenance;
- Candidate Selection validation;
- Issue Architecture validation;
- Article Draft validation;
- claim / chronology validation;
- LaTeX build and log/page-budget checks;
- exact PDF SHA binding;
- Visual Review record derived from Publication Preview approval;
- Freeze source/PDF integrity checks;
- release manifest / release asset SHA verification.

Internal state names are intentionally retained for backward-compatible provenance even where they no longer map one-to-one to a Human Gate.

## Normal flow

```text
Issue initialization
  -> Source Discovery
  -> Screening / Evidence
  -> Candidate Selection (internal checkpoint)
  -> Architecture Proposal
  -> HUMAN GATE 1: Architecture Review
  -> Drafting / Validation / Layout / Build
  -> Publication Preview PDF
  -> HUMAN GATE 2: Publication Preview
  -> Visual Review record (machine checkpoint)
  -> Freeze
  -> Merge
  -> Public Release
  -> Complete
```

At any point, a genuinely new editorial/publication choice branches to an on-demand Exception Gate and returns to the normal flow after the user decision is recorded.

## Workflow mapping

- Architecture preparation: `apply-special-selection-and-propose-architecture.yml` — internal editorial checkpoint; no standalone Human Gate.
- Architecture approval: `approve-special-architecture-and-prepare-drafts.yml` — **Human Gate 1**.
- Publication approval: `accept-special-publication-preview-issue-only.yml` — **Human Gate 2**, then deterministic Visual Review/Freeze/merge/Release.
- The historical standalone `accept-special-visual-review-issue-only.yml` workflow is removed so it cannot create a partial legacy approval path. The Python module `accept_special_visual_review_issue_only.py` is retained only as an internal implementation primitive used by the Publication Preview workflow.
- `accept-special-freeze-issue-only.yml` and `publish-special-frozen-release-issue-only.yml` remain verified recovery primitives after an already-recorded Publication Preview approval. They derive timestamp/reference authority from the committed Publication Preview record and accept no new Human approval parameters.
