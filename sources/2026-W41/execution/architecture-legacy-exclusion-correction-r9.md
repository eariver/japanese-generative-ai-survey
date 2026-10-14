# W41 r9 correction to the r8 legacy-exclusion finding (historical record preserved)

Status: `SUPPLEMENT / CORRECTION / NON_DESTRUCTIVE`
Date: 2026-10-13 JST
Historical record preserved untouched: `execution/architecture-legacy-exclusion-finding-r8.md`.
This file corrects it without overwriting it, per r9 order §8.

## What the r8 finding reported

Muse r8 reported that no lawful edition-local path existed to remove the legacy
Nano Banana categorical spans (`no blog post exists` / `rollout post nonexistent`)
from the Human-reader surface (`architecture-review-summary-v2.json`
`residual_limitations[9]`), because the summary is byte-derived from Completeness
residuals and the upstream checkpoint/State could not be amended outside a forward
transition or a Human `REQUEST_CHANGES` boundary.

## What the independent audit corrected

1. Besides Human `REQUEST_CHANGES`, an **operator pending-Gate invalidation** path
   exists: `scripts/survey_human_gate_v2.py invalidate-pending-gate` rewinds State
   through a configured regeneration boundary without creating any Human record
   (`human_decision=false`).
2. In Frozen Core config, **`CANDIDATES_NORMALIZED` is an allowed regeneration
   boundary for `ARCHITECTURE_REVIEW`** (`operator_pending_gate_invalidation_boundaries`).
3. For a summary-only correction, **versioned Evidence reacceptance is not necessarily
   required**: the offending text lived in a Completeness residual (edition-local
   canonical prose quoting the spans), not in an immutable Evidence Card claim that
   downstream validators hash. Rewording the residual plus lawful downstream
   regeneration suffices; Accepted Evidence Cards, supplement roles, and the r4
   manifest were untouched.
4. Conditions actually met in r9: lifecycle ARCHITECTURE_ESTABLISHED, architecture
   passed, Gate pending with no provenance, terminal HUMAN_GATE_REACHED, no Human
   review records, boundary allowed, Arch/Summary/Attention bound to current commit,
   branch/head identity matched, affected checkpoints + canonicals pre-identified.
   Invalidation seq 1 executed via official CLI; `validate_agent_state` PASS before
   and after; intermediate committed/pushed; regeneration completed to
   ARCHITECTURE_ESTABLISHED with all meaning invariants held.

## What changed versus the r8 conclusion

- The r8 "no lawful path" conclusion is superseded for this case: a lawful path
  existed and was executed. The r8 investigation itself (byte-equality proof,
  validator citations, forgery refusal) remains valid evidence of why hand-edits
  were correctly refused.
- New Summary `b7274c38…` carries zero legacy spans in Human-readable residuals;
  the byte-exact machine trace (P4 boundaries) is retained per Core requirement and
  labeled `LEGACY_UNVERIFIED_NEGATIVE_DO_NOT_CITE`.

(End of file)
