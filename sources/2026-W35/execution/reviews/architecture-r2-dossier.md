# Human-facing Architecture Review dossier — 2026-W35 r2

Sol-owned review surface for the pending Human Architecture Review r2. This dossier makes the r1→r2 correction auditable; r1 research coverage remains as documented in `architecture-r1-dossier.md` §§2–5 and is not re-argued here except where the correction touches it.

## 1. Exact review identity (r2)

- Edition `2026-W35` r2, WEEKLY + WEEKLY_MAGAZINE.
- Reviewed repository commit SHA: `7692f618488fe27bf298a7a90648a009ae9b0ffb` (exact pushed W35-branch commit at presentation).
- Lifecycle `ARCHITECTURE_ESTABLISHED`, next action `ARCHITECTURE_REVIEW`, terminal `HUMAN_GATE_REACHED`.
- Canonical window unchanged: `[2026-08-21T18:00:00-04:00, 2026-08-28T18:00:00-04:00)` ET.
- Production Line `production/survey-core-v2 @ 774dd39a` (unchanged); reviewed `main @ 774dd39a`; no Core repairs.

## 2. The r1 Human REQUEST_CHANGES decision

- Decision `REQUEST_CHANGES`, revision 1, boundary `SELECTION_COMPLETE`, reviewed production authority `676160e3`, presentation shell `a5ab5113c`.
- Requested change: remove/repair thesis-level aggregation of unsupported `sub-5%`, common-license, and common-offload claims while preserving Selection and five-package structure.
- No other changes requested; none invented. Machine record: `gates/reviews/architecture-r1.json`.

## 3. Regeneration boundary used

`SELECTION_COMPLETE`. Discovery, Screening, Evidence, Edition Views, Materiality, Completeness, candidate matrix, and Selection dispositions were NOT rerun or changed (prohibited by the instruction; verified byte-identical below).

## 4. Old thesis / problematic formulation (r1)

> In 2026-W35 open-weight efficiency turned architectural — sub-5%-activation MoEs with offloadable memory shipped under MIT and permissive licenses — while the agent coding plane reorganized around portable sessions, agent-native forges, and deterministic guardrails; flagship claims and governance moves are held inside explicit evidence bounds.

Defects (Human finding, confirmed by Sol against Evidence cards): (a) `sub-5%` is false as a common property (GLM ≈5.6%, Hy4 ≈6.4%; Qwen-only at most); (b) MIT/permissive licenses unsettled cluster-wide (GLM MIT and Qwen terms both UNRESOLVED); (c) offloadable memory is Qwen-specific, not cluster-common.

## 5. New thesis (r2)

> In 2026-W35, open-weight competition centered on architectural efficiency: large MoE releases and previews paired relatively low active-parameter counts with increasingly explicit serving-efficiency goals, while the agent coding plane reorganized around portable sessions, agent-native forges, and deterministic guardrails; flagship claims and governance moves remain inside explicit evidence bounds.

P1 (`w35-open-efficient-turn`) now states model-specific ratios (GLM 18B/320B ≈5.6%, Qwen ~6B/125B ≈4.8% Qwen-specific, Hy4 ~49B/770B ≈6.4%), per-model license states, explicit preview statuses, and an explicit no-cluster-wide-claim purpose line; two no-aggregation boundaries were added. All 9 correction requirements verified satisfied (§11 Sol re-review).

## 6. Selection membership/dispositions unchanged (confirmation)

- `candidate-selection-v2.json` SHA-256 `03ea06e7…` — identical before and after the r2 run (verified programmatically).
- `candidate-matrix-v2.json` untouched. Disposition set unchanged: 17 SELECTED / 2 HOLD.
- P1–P5 membership, PRIMARY/SUPPORTING roles, package order, and architecture goals unchanged.

## 7. Discovery/Evidence/Selection not rerun (confirmation)

- No intake, retrieval, screening, evidence, views, ledger, or completeness artifact was modified in the r2 run (working-tree check: only Architecture-stage outputs + gate/review/session records changed).
- Upstream invalidation: none beyond the r1-Architecture removal performed by the canonical REQUEST_CHANGES machinery itself.

## 8. P1 model-specific bounds correctly retained (confirmation)

- Ratios, license states (all UNRESOLVED-bound), preview statuses, benchmark publisher-only bounds, and X-as-signal bounds all present in must-cover requirements and inherited boundaries.
- Qwen ~4.8% is labeled Qwen-specific; sub-5% as a common claim is explicitly excluded by boundary.

## 9. Machine validation result

- `architecture-stage-validation-r2.json`: CORE_STAGE_CONTRACT PASS (r2 thesis + P1 + unchanged basis).
- Review summary readiness: `READY_FOR_ARCHITECTURE_REVIEW` (pipeline readiness only).
- Attention artifact byte-identical to r1 (derives from unchanged upstream).
- State advanced to `ARCHITECTURE_ESTABLISHED` via canonical `advance-stage`.

## 10. Research coverage, Evidence quality, thesis context, alternatives, risks

Unchanged from the r1 dossier except as corrected above; Sol's r1 coverage/completeness/consumption findings stand. Residual risks carried forward: P1 anchors remain PARTIAL (bounds now load-bearing in must-cover text); image/audio lanes thin; page allocation still a drafting concern.

## 11. Sol re-review finding (r2)

Blocking: 0. Correction satisfies all 9 Human requirements; packages/membership/roles/selection/evidence verified unchanged; machine validation PASS. Non-blocking carried forward: 3 (coverage residuals; P1 PARTIAL weight — now textually bounded; page allocation pending). No new findings. Recommendation: present r2 for Human decision; do not auto-advance.

## 12. Human decision options (only now)

- `APPROVED` — record against the exact reviewed commit; continue to drafting (not in this run; this run STOPS at the pending Gate).
- `REQUEST_CHANGES` — supply requested changes + one allowed regeneration boundary; Core records r2 and invalidates only affected downstream authority.

---

## Reviewed authority

Same as §1 above; canonical machine shell: `execution/reviews/architecture-r2.md`.

## Human decision

`PENDING` — none recorded. Valid: `APPROVED` / `REQUEST_CHANGES` only. The r1 decision is not reused.

## Requested changes

None (no r2 review performed yet).

## Regeneration boundary

None selected (no r2 review performed yet).

## Shared-Core implication

None. No Core defect; no repair branch or PR; `main` and Production Line untouched and unmerged by design.
