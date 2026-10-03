# TS-003 Architecture r3 Intake (112) — Execution Record (2026-10-03)

- Starting HEAD: `bc5d19922ace4a6e6ac319a0d6685be3eacc87b9` (r3 REQUEST_CHANGES
  bridge result at ISSUE_INITIALIZED)
- Authority: Human Architecture r3 REQUEST_CHANGES (boundary ISSUE_INITIALIZED)
  for VM-D112 formal intake. VM-D112 staged material used as input only, never
  as authority.
- Terminal: ARCHITECTURE_ESTABLISHED, both Human Gates pending (expected
  Architecture Review r4). STOP — no approval, no gate decision inferred.

## Chain (all canonical validators PASS)

1. Discovery: 111 carried + VM-D112 as normal BASE root record
   (`research_pass: 0`, `parent_refs: []`); acceptance 112 records; advanced
   ISSUE_INITIALIZED → DISCOVERY_COLLECTED.
2. Screening: fresh package over 112 records (111 carried byte-identical +
   VM-D112 formal §8 KEEP, VM-O10/VM-O12); acceptance
   `0b09cde03485a852df7ca5ff84b7eff768ecc0efae9c3615ea2662f71dc4d6bf`
   (KEEP 104 / MAYBE 3 / INSPECT 5); advanced → CANDIDATES_NORMALIZED.
3. Evidence (`phase_c_evidence.py`): package rebuilt WITH exact Evidence
   Authority Supplement `evidence-authority-supplement-112.json`
   (`15f5b2279c64`; two post-Screening docs sources bound to the VM-D112 task
   under `supplement-src-*` keys; raw captures byte-pinned under `raw/`).
   VM-D112 card: 15 claims + 2 limitations + 1 unresolved question, every claim
   re-verified against fetched official bytes 2026-10-03 (unverifiable staged
   specifics — numeric FPS schedule, reference-pointer/loop labels, billing
   phrasing — dropped or reworded to verified text). 111 cards carried from r8
   with deterministic basis rebinding only (D106/D091/D010/D084 repairs intact).
   Fresh acceptance `33ec63cbd5bbe776fb106f57fa64ca448061dfe92cbbfe3684848ddb17010b69`.
4. Views/Materiality/Completeness (`phase_d_views_materiality.py`): views
   acceptance `be9b7a50b1214113c6dd0a87d7092a574d8498d1bf2bb9ce0798a1d20f1231b5`;
   ledger 112 rows, VM-D112 MATERIAL (P09 economics + P11 third-contract
   rationales); completeness LIMITED with carried judgments + VM-O10/VM-O12
   VM-D112 disposition notes. SSv2 purge clean (V1 entity; profile-echo only).
   Advanced → EVIDENCE_REVIEWED.
5. Selection (`phase_e_selection.py`): matrix re-derived, 112 rows (D084 title
   `Something-Something V1`; VM-D112 MATERIAL row
   `candidate:...:69b72bb7fcd308ec`); 111 assignments carried + VM-D112
   SELECTED/SUPPORTING (`THEMATIC:lineage-context`,
   `LONGFORM_SPECIAL:supporting-context`). Advanced → SELECTION_COMPLETE.
6. Architecture (`phase_f_architecture.py`): v4 packages + refreshed basis +
   carried P02 cost/loss/recipe boundary + VM-D112 SUPPORTING dual placement
   (P09 economics axis, P11 third contract; full remaining-boundaries verbatim
   in both; TRANSITION_NODE treatment in both; must_cover both). Status
   PROPOSED, human_review null. Summary + attention recreated. Diff vs v4:
   `architecture-v4-to-v2-112.diff` (99 lines). Advanced →
   ARCHITECTURE_ESTABLISHED. STOP.

## Deltas vs r8/r14 authority (all prior repairs preserved)

- r8 Evidence repairs intact (V1 108,499×174; DETR cost/loss/recipe split;
  Opus 4.7/4.8 condition splits; SIMA executed-scope). SSv2-free generated texts.
- r13/r14 reader authorities untouched (no r15, no TeX/PDF).
- r2 approval snapshot preserved; no approval reused or fabricated; no r4
  decision record created (Human decision owed).

## Core Freeze / lifecycle safety

- Shared Core files changed: NO. Canonical builders/validators only
  (`build_evidence_authority_supplement`, `prepare_evidence_package`,
  stage validation, checkpoints/advance). Post-gate adaptation via
  Core-provided `current_stage_basis_override` + implementation_sha == HEAD.
- production-state.json advanced only via frozen checkpoint/advance helpers.
  No manual state imitation, no gate mutation. Sol re-review owed.
