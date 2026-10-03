# Fresh Human Architecture Review — package supplement (v4 basis)

This file completes the §12/§20 review package alongside `architecture-v4.json`,
`architecture-review-summary-v4.json`, `architecture-review-attention-v4.json`,
and `execution/upstream-rebind-post-r14-20261003/architecture-v3-to-v4.diff`.
No Human decision is recorded or inferred here.

## 1. Evidence diff r7 → r8 (only 2 of 111 cards changed; 109 byte-identical)

- VM-D106 claim-1: `SIMA-agent training use with goal-agnostic simulation`
  → `recent SIMA version executed in Genie-3 worlds to test compatibility for
  future training (Genie 3 goal-unaware, simulates future from agent actions)`.
  Primary: DeepMind Genie 3 blog, Fueling embodied agent research (run +
  compatibility-test + goal-unaware + action-conditioned quotes verified;
  training reading refuted). Training-use extension prohibited and absent.
- VM-D091 claim-1: floating `~318 vs ~30` + adjacent Opus 4.8-batched config
  → split: `318.4 average` explicitly bound to `Claude Opus 4.7 + maximum
  thinking + single-action over 108 tasks` vs `~30 (OSWorld 1.0)`; `20.6/54.8`
  bound to `Opus 4.8 + max thinking + batched + 500 steps` with its own
  `481.8-call` figure. Primary: OSWorld 2.0 paper abstract/Table 3/§2.2.1/§3.1/§3.2
  (4.7-vs-4.8 version split confirmed; generic-complexity reading refused).
- VM-D084: no r7→r8 change (V1 identity already canonical in r7).
- VM-D010: no r7→r8 change (cost/loss split + recipe framing already compliant).

## 2. Selection diff r7-file → r8-file

- 111/111 assignments byte-identical (verified by comparison).
- Only `basis` SHAs refreshed (matrix/completeness/ledger r8 pins).
- No Agentic role admitted (VM-D112 not selected; staged recommendation retained separately).

## 3. VM-D112 disposition summary

- Substance evaluation (genuine, not reverse-engineered): cutoff ✓ (2026-09-01 release within 2026-09-30); TS-003 relevance ✓; P09 token-acquisition-economics materiality ✓; P11 third-contract materiality ✓; non-duplicate vs Flash-VStream (model-side streaming memory vs API-side server tool loop) ✓; official-docs authority with vendor-ceiling boundaries ✓.
- Recommendation (NOT a decision): KEEP, PRIMARY transition-anchor (P09 TRANSITION home, P11 contract touch), scope_tags VM-O10/VM-O12.
- Formal status: NOT admitted. Canonical screening acceptance structurally admits no genuinely-new-source records under frozen Core (proven by validator rejection + code inspection; shared code untouched). Staged specs retained for the Human-gated pipeline run. GOVERNED_PIPELINE_REENTRY_REQUIRED — HUMAN_GATE_NOT_BYPASSED.

## 4. Binding changes v3 → v4 (beyond basis SHAs)

- None. v3→v4 diff = basis SHAs only (18 lines). P09 license precision, P12 condition binding, V1 identity, DETR precision, P01 scope — all already correct in v3 content; r8 evidence refresh required no architecture-text change (verified by scan).
