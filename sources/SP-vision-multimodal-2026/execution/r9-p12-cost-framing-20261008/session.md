# Session — TS-003 r9 Final Bounded Architecture Correction: P12 Evidence-Safe Cost Framing

Run: `execution/r9-p12-cost-framing-20261008`. Human-bounded single-package
correction (`bounded-revision-authorization.md`); no gate decisions fabricated;
no shared Core modification; no force push.

## Starting authority (read-only verified before any write)

- Branch `special/vision-multimodal-2026-work`, HEAD `ff2631f769627d244dbe49e0c5206f92b8d4712f`,
  tree `45092a6b076948b336c1ca6e94b8525d78b0048f` (local==remote; clean tree).
- Lifecycle `ARCHITECTURE_ESTABLISHED`, r9 PROPOSED pending review, Draft pending.

## Re-entry

1. Fail-closed probes (`probe_reentry_r9c.py` → `reentry-probes-r9c.md`):
   ARCHITECTURE_REVIEW path needs a Human decision (not fabricated);
   PUBLICATION_PREVIEW + operator invalidation FAIL-CLOSED; Draft advance
   closed for this run; shared-Core CLOSED. Zero writes.
2. Core-controlled rewind (`execute_rewind.py` → `rewind-execution.json`):
   ARCHITECTURE_ESTABLISHED → SELECTION_COMPLETE (gate ARCHITECTURE_REVIEW;
   no approval active, nothing to supersede). 4 Core-computed paths removed
   (architecture-v2, summary, attention, SELECTION_COMPLETE checkpoint);
   `validate_agent_state` CLEAN.

## Correction (Core canonical machinery, frozen Core)

3. Evidence pre-check: VM-D091 supports tool-call counts (318.4, exact conditions),
   long-horizon workflows, state-management bottleneck; measures NO token/KV/
   context/compute/latency field directly — the correction is Evidence-faithful.
4. P12 correction (`correct_p12_architecture.py` → `architecture-r9prev-to-r9p12.diff`,
   17 lines): must-cover `Screenshot-loop token costs…` REPLACED with the
   Evidence-safe cost-framing requirement; proxy-prohibition boundary ADDED.
   Delta guard enforced: only P12 differs (P02/P04/P15 and all others
   byte-identical; budgets/depth unchanged). Summary + attention rebuilt,
   canonical validation passed. → ARCHITECTURE_ESTABLISHED, gates pending. STOP.
5. Fresh dossier `architecture-review-dossier-r9-p12.md` (P12-only scope stated);
   deferred fresh-Draft list recorded, not executed
   (`deferred-fresh-draft-requirements.md`, incl. the DUSt3R editorial-synthesis guard).
6. Terminal audit (`audit_r9p12.py`): 25/25 PASS (§15 items 1–22 + terminal state).

## End state

`R9_P12_EVIDENCE_SAFE_COST_FRAMING_COMPLETE / ONLY_P12_ARCHITECTURE_DELTA /
FRESH_HUMAN_ARCHITECTURE_REVIEW_PENDING / NO_DRAFT_REGEN`. No Draft rev6.
No reader-publication-validation. No TeX/PDF/Preview/Freeze/Release.
No further Architecture repair initiated by this execution.
