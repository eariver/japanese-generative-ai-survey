# W41 r13 change ledger (r11→r12 and r12→r13 separated)

Status: `EDITION_LOCAL / PROPOSAL_LEDGER`
Date: 2026-10-13 JST
Format per item: Audit ID / Package/block / old / new / reason / Evidence / verdict.

## A. r11→r12 changes (carried context; r12 files untouched)

- r11-B01 / P4/p1 / 4K-as-resolution reading / token-count wording + knowledge cutoff /
  excerpt-bound rationale / RESOLVED.
- r11-B02 / P5/p6+t1 / categorical text-exclusion / bounded "unconfirmable from source"
  + scale pair / RESOLVED.
- r11 depth batch (P1 billing/bench unknowns, P2 typed answers, P3 MRL/MoE/pricing/download,
  P4 Elo note, P5 FPR/edit triple + scale note, P6 pp/relative split) / RESOLVED.
- r11 Priority C (9 self-reference patterns) / removed / RESOLVED.

## B. r12→r13 changes (this revision)

### BLOCKER
- R11-B01 / P3/p5 / text-only embedding implication / 5-modality + 3-encoder + MRL
  truncation-meaning + 8K/5.5min/29/58 rewrite / excerpt-faithful multimodal correction /
  `36ef2bcb…` claim-1 + excerpt lines 2–6 / RESOLVED.

### MAJOR
- R11-M01 / P3/p13 / "all active-side" misstatement / audit-table pairs
  (78.1B/3.46B, 501B/23B, 1.05T/52B) + memory/compute split + FLOPs caveat /
  Cards claim-1s / RESOLVED.
- R11-M02 / P3/p8 / "GrokのX告知は…" direct attribution / secondary-record +
  52B-primary wording, pricing display kept / ml4 claim-2 scope / RESOLVED.
- R11-M03 / P5/t2 / psych/ELI5 bleed into synonym note / recommended bounded wording,
  figures unchanged / textgrain claim-1 scope / RESOLVED.
- R11-M04 / P1/p5+t1 (+p9/p12 checked) / cost-estimation implication / recommended
  wording (cache-read confirmed, units unknown, formal table required), GPT-6 vs Haiku
  distinguished / haiku claim-1 scope, no complementation / RESOLVED.
- R11-M05 / P5/p6+t1+coverage / categorical non-support risk / bounded wording kept +
  reconciliation doc (RECONCILED, Architecture unchanged) / synth excerpt + Card /
  RESOLVED (bounded reading; Sol may supersede).

### MINOR
- m01 / P2/p1+p12, P3/p3+p7+p8+t1+p16 / relative dates / absolute dates (2026-10-06/07/08,
  late-October/end-October announcements) / changelog/blog dates / RESOLVED.
- m02 / P1/headline+deck+p9+p10 / 値札 generalization / split confirmed conditions per
  model, no dual-price impression / r13 texts / RESOLVED.
- m03 / P2/p9, P3/p13 / r2/audit-history leaks / plain technical facts / — / RESOLVED.
- m04 / P3/p16 / lumped schedules / Beam-late-October vs Mistral-end-October split,
  no completion conflation / claims / RESOLVED.
- m05 / P3/p12 / three-stage + over-assertion risk / four-stage wording bounded to
  Evidence range / claims+limitations / RESOLVED.
- m06 / P5/p2+p3 / duplicated vendor tails / single marking per group (p2 intro kept,
  p3 merged-inline) / claim-1 scopes / RESOLVED.
- m02-corrigendum / validation-report-r12.md / stale `df0d16b6…` input SHA /
  recomputed `5273d76d…` + binding check, r12 files untouched / file bytes / CORRECTED.

## Coverage note

- must_cover 27/27 and boundaries 42/42 preserved structurally and substantively
  (P5[0] gains p13/t3 substance; no requirement dropped or invented).

(End of file)
