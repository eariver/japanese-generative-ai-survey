# Survey Production session — w37-sol-r1-request-changes-regenerate-r2-20260919

Issue: `2026-W37`
Started: `2026-09-19` (local ff from `8fb3960f6` to Exact Starting SHA `fb2733d5bf5646afad362691570fa8616fe42057`)

## Starting authority

- Branch: `weekly/2026-W37-v2-work`; Exact Starting SHA `fb2733d5b` (remote HEAD/tree verified read-only pre-write; parent `3a7dae19`/tree `6f10819c`; main `6aa385cb`/tree `62cf5dfb` plus Production Line `774dd39a`/tree `cd46a6f7a` guards PASS)
- Execution contract: `execution/requests/sol-w37-architecture-r1-request-changes-regenerate-from-discovery-20260919.md` (prior independent review verdict `REQUEST_CHANGES`, Human still `PENDING`)
- Lifecycle at start: `ARCHITECTURE_ESTABLISHED`; r1 surface unpresented; no Human review records
- Local HEAD was `8fb3960f6` (2 behind); fast-forwarded to `fb2733d5b` (no rewrite)

## Actions actually performed

- Invalidated the unpresented r1 Gate to `DISCOVERY_COLLECTED` via canonical `survey_human_gate_v2.py invalidate-pending-gate` (operator record `architecture-invalidation-0001.json`; no Human decision created). Preserved Grok r3 Raw/manifest, 14-record Discovery, all primary/secondary Raws, archived r3 correction review, W36 material.
- Verified Fusion publication time from first-party page metadata (`article:published_time` plus JSON-LD `datePublished` = `2026-09-11T10:00:00-07:00` = `2026-09-11T17:00:00Z`, ordinary with 5h margin); stored verification record under `collectors/primary/runs/20260919T000000Z/`; withdrew the date-only assumption.
- Regenerated Screening r2 (13 KEEP / 1 DROP) with neutral worker provenance (runner `muse-spark`); validated and advanced to CANDIDATES_NORMALIZED.
- Regenerated Evidence r2 (11 VERIFIED plus 2 PARTIAL with views/ledger/completeness LIMITED 3/3 SATISFIED); validated and advanced to EVIDENCE_REVIEWED.
- Regenerated Selection r2 (12 SELECTED / 1 HOLD, resignation HOLD/NONE with no Architecture weight) and Architecture r2 (7 packages, RC-1..RC-5 repairs, READY_FOR_ARCHITECTURE_REVIEW); validated and advanced to SELECTION_COMPLETE then ARCHITECTURE_ESTABLISHED (HUMAN_GATE_REACHED).
- Generated fresh r2 review shell (`architecture-r2.md`, PENDING) plus worker dossier (`architecture-r2-dossier.md`); r2 claims no independent review; prior r1 `REQUEST_CHANGES` cited as authority; historical r1 worker files classified `WORKER_SELF_REVIEW / NON_AUTHORITATIVE_AS_SOL`.
- No Draft generated (not authorized). No Core changes. No Drive access; no Grok rerun; no broad Discovery rerun.

## Deviations / failures

- None blocking. Old r1 accepted dirs remain on disk as history alongside new r2 content-addressed dirs.

## End state

- Lifecycle: `ARCHITECTURE_ESTABLISHED`
- Terminal reason: `HUMAN_GATE_REACHED`
- Next action: `ARCHITECTURE_REVIEW` (independent review first, then Human decision)
- Review target: r2 Gate triple plus dossier at the exact pushed commit recorded in `architecture-r2.md`
- Session status: `COMPLETE_AT_GATE`
