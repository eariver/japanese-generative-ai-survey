# SOL_MATERIALITY_SELECTION_REVIEW_HANDOFF r8 — 2026-W42 (Muse r8)

To: Sol. From: Muse. Date: 2026-10-17 JST.
Terminal: `SOL_MATERIALITY_SELECTION_REVIEW_READY` (candidate; Sol owns materiality/selection semantics).
Core: `EVIDENCE_REVIEWED` (discovery + screening + evidence + materiality + completeness passed; next `stage:selection`). Gates pending. NO Selection acceptance / Architecture / Draft / PDF.

## 1. Compat execution (Human-authorized, Core-immutable)
- Native frozen `current_stage_basis_override()` ONLY (restores on exit); no Core edits (verified: shared-tree diff vs frozen shows no scripts/schemas/config change in r8).
- DM-016 projection ledger: 17 SOCIAL/SECONDARY projections + 33 passthroughs; invariant (only source_type differs) enforced per task; unknown → fail-closed (proven N5).
- Supplement r8: 91 raw excerpts + manifest, frozen-validated (raw sha/bytes + basis SHAs).
- Interactive input 50 records validated (PARTIAL 43 / NEEDS_MORE 7; materiality 28/14/7/1 with substantive r7-view rationales).
- Chain (all frozen validators): 50 Core cards + 50 views accepted (`f2429e27…`, `4296ffd0…`), materiality ledger, LIMITED completeness (2 SATISFIED / 1 LIMITATION).
- Bridge ADVANCE → EVIDENCE_REVIEWED (event-bound receipt + checkpoint + stage contract). Accepted Discovery/Screening bytes untouched throughout.
- Negative matrix N1–N6: agent-state clean before/after; default-path failure distinct (impl-mismatch at this HEAD; semantic variant at r7 HEAD — same fail-closed family); tamper/wrong-SHA/unknown-type refuse. Full log: compat `validation-report.md`.

## 2. E42-R7-P1 + r7-audit closures inside r8
- 8 editorial bundle-09 misbindings: ELIMINATED by construction — Core cards cite only task-bound URLs (discovery locator or supplement entries); no bundle paths appear in any accepted card source.
- Materiality rationales: substantive r7 views (not boilerplate counts).
- Selection sketch revised → `selection-proposal-r8.PROPOSED.md` (per-candidate positive/negative rationale, P2/P6 overlap fixed, 20–24pp sensitivity plan, compression note). PROPOSED only.
- Ledger: 1-claim provenance receipt (PARTIAL + NON_MATERIAL + OTHER relation); 50th card counted, never storied.

## 3. Counts
- Discovery 50 / Screening 50 (KEEP 29 incl. binder / INSPECT 16 / MAYBE 5) / Evidence 50 (PARTIAL 43 / NEEDS_MORE 7) / Views 50 / Materiality 28-14-7-1 / Completeness LIMITED.
- Claims: 151 draft strings + 1 ledger receipt claim = 152 accepted claims (PARTIAL 43 / NEEDS_MORE 7 cards); every claim URL+class bound via task authority or supplement.

## 4. Residual gaps (unchanged standing)
- License FILE bytes (Muse/Super-VL; MiniCPM/Granite files absent upstream); PDF deep audits; bench methodologies; 13 THIN + 1 NOT_FOUND + 7 HOLD; security-X uncorroborated; JP/audio thin; Grok authorship unvalidated.
- Core Issues #568/#569 + DM-016/DM-023 remain OPEN_CORE (edition compat succeeded; generic defects untouched).

## 5. Sol next
- Materiality + positive/negative selection review of the r8 proposal; Architecture only after that independent approval. No Gate requested.
