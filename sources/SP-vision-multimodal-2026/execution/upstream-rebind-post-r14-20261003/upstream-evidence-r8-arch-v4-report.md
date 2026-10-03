# Upstream Evidence r8 + Architecture v4 — Execution Record (2026-10-03)

- starting HEAD: `e5c46494426e5bd549742949463786283c30caed`
- starting tree: `1b2c7ad76682925cdf3cac7c01ae3bed4f2bf863`
- Terminal: fresh Human Architecture Review PENDING (no approval, no gate mutation).

## Guard

- Remote HEAD/tree matched expected; clean tree; no new branch; no force/reset/rewrite.

## Evidence repair

- VM-D084: V1 identity VERIFIED preserved from r7 (entity V1, claim with 108,499, zero V2 strings). No further change.
- VM-D106: REPAIRED. Before: `SIMA-agent training use with goal-agnostic simulation` (overbroad, implied training). After: `recent SIMA version executed in Genie-3 worlds to test compatibility for future training (Genie 3 goal-unaware, simulates future from agent actions)`. Primary: DeepMind Genie 3 blog, Fueling embodied agent research (run + compatibility-test + goal-unaware + action-conditioned quotes verified; training reading refuted).
- VM-D010: re-verified against §5 spec (matching costs → assignment → matched-pair loss; aux as standard recipe) — r7 already compliant → UNCHANGED.
- VM-D091: REPAIRED. Before: floating `~318 vs ~30` adjacent to Opus 4.8-batched config (misattribution risk). After: 318.4 average explicitly bound to `Claude Opus 4.7 + maximum thinking + single-action over 108 tasks` vs ~30 (1.0); 20.6/54.8 bound to `Opus 4.8 + max thinking + batched + 500 steps` with its own 481.8-call figure. Primary: OSWorld 2.0 paper abstract/Table 3/§2.2.1/§3.1/§3.2 (4.7-vs-4.8 version split confirmed).
- Batch: r8 acceptance `d6338dc4...` (3f510fbb) + views `11fd09a0...` (227fc9b5); 111 cards (109 byte-identical hash-proven: D106+D091 rebuilt); all canonical validators PASS. Timestamps preserved.
- Affected downstream artifacts (recorded, machine files rewritten only where governed): matrix D091 row (new SHAs), selection basis, architecture basis; TeX/bib/drafts/r14 reader wording left for post-approval backlog.

## VM-D112 Discovery/Screening/Evidence disposition

- Discovery supplement (112-record acceptance) BUILT+VALIDATED as staged artifact; canonical 111 acceptance untouched.
- Formal screening acceptance BLOCKED at `validate_discovery_expansion` (derived records must be parent-rooted; genuinely-new-source records have no bounded append path). Proven by prior failing run + code inspection (unchanged shared code).
- Therefore: NO screening acceptance, NO evidence task/card, NO materiality/selection/architecture admission for VM-D112 in this pass. Staged specs retained (screening KEEP decision, 17 evidence drafts, placement recommendation). GOVERNED_PIPELINE_REENTRY_REQUIRED — HUMAN_GATE_NOT_BYPASSED. Requires Human-gated return to DISCOVERY_COLLECTED.

## New Evidence authority

- r8 acceptance d6338dc4 (file sha 3f510fbb) + views 11fd09a0 (file sha 227fc9b5). r7 superseded as latest (retained).

## New Materiality / Completeness

- materiality-ledger-v2-r8.json (111 rows; dispositions unchanged) / profile-completeness-v2-r8.json (LIMITED; judgments carried incl. VM-O06 SATISFIED). Validators PASS.

## New Selection

- candidate-selection-v2-r8.json (111 assignments carried byte-identical + refreshed basis). Validator PASS. No Agentic role admitted (blocked, staged recommendation retained).

## New Architecture

- architecture-v3.json PROPOSED retained; NEW architecture-v4.json PROPOSED (v3 content + refreshed basis only; P09 license precision, P12 condition binding, V1/DETR states already correct in v3 — verified, no further content change). status PROPOSED, human_review null. NO gate record created.
- Review package: architecture-review-summary-v4.json + architecture-review-attention-v4.json + architecture-v3-to-v4.diff (18 lines: basis SHAs only).

## Stale-binding audit

- ELIMINATED: D106/D091 evidence bytes+views; ledger/completeness/matrix/selection bases (r8 files); architecture basis (v4).
- REMAINING (by design): draft-package/checkpoint/production-state/gate pins; TeX/PDF/bib; r14 wording; P01 Option B (backlog above).

## Deferred reader backlog

- post-approval-reader-backlog.md (P11 V2→V1, P02 matching/loss, P12 318 binding, P13 ceilings, P14/P15 Genie sync, P09 living-repo identifiers, P01 Option B edits, future dedup + terminology batches).

## Final HEAD/tree

- (filled at commit time; two normal commits: Evidence r8 batch, then refresh chain + records)
