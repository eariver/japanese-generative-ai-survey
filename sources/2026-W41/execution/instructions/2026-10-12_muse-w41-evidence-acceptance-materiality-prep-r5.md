# J-GAS W41 — Muse r5 Evidence Acceptance + Materiality/Completeness Preparation

Status: `EXECUTION_AUTHORITY / SOL_EVIDENCE_R4_BINDING_CONDITIONAL_PASS / BOUNDED_ACCEPTANCE_AFTER_SC-E41-05_06 / CORE_V2_IMMUTABLE`
Date: 2026-10-12 JST
Repo: `eariver/japanese-generative-ai-survey`
Only existing branch: `weekly/2026-W41-v2-work`
Sol exact technical review: `sources/2026-W41/execution/reviews/sol-w41-evidence-authority-binding-r2-20261012.md`
Reviewed r4 HEAD: `241a1cd5a7d3809b6a052628509a35445ad57c83`; Tree `97818cb482c3f5a2b3d6abbea4bf3639eb51e7b7`.
Reviewed main SHA/Tree: `83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8` / `31c0adc5b57761e5073d100554279a8adc5a18f4`.
Frozen Core SHA/Tree: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

## 0. Strict read-only startup gate

Exact Starting HEAD/Tree for this instruction commit will be supplied by Sol at invocation. Check both against current remote branch. Check instruction commit parent == `cbcfbd4c421a00a1e46873e989f4b3f2ba5e6f0f`. Check reviewed Muse r4 HEAD/Tree is exact ancestor, remote main/Core match above, and canonical W41 State `CANDIDATES_NORMALIZED / stage:evidence-materiality-completeness` with Discovery/Screening PASSED, Evidence/Materiality/Completeness PENDING and both Human Gates PENDING. Accepted 37 Discovery/37 Screening immutable; no active concurrent worker commits or unowned dirty worktree.

Any mismatch → ZERO WRITES, exact expected/actual report, STOP. No new/fallback/review/repair branch; no reset/rebase/cherry-pick/force/history rewrite, no W40 or shared-Core/scripts/config/schema/workflow/main writes, no unauthorized Human Gate.

## 1. MANDATORY SC-E41-05 exact-nine regeneration fail-closed guard

- Before any official Evidence acceptance, inspect the actual r4 `build_r2_package.py` source: it remaps `SECONDARY_OBSERVATION` without checking the approved nine IDs. Fix by a narrowly constrained **edition-local builder guard** (in-place on r4 builder or new r5 builder under `execution/compat`; original r4 committed SHA remains in history). Exact allowlist is defined by r4 `projection-ledger.json`, nine IDs and stable task identities; enforce expected cardinality and exact original `source_type` values. Unexpected tenth, missing member, changed locator/other Task authority fields, or unrecognized source type MUST fail before any output authoritative write.
- Verify regenerated complete r2 derived Task+Package bytes remain exactly identical to the reviewed r4 version (36 exact task hashes and package hash), or, if a truly necessary change affects SHA, build a separate r3 candidate package and rebuild matching Cards/Views; do not silently reuse stale SHA/card bindings.
- Re-run deterministic two-build identical proof, unknown-type/tenth-item injection negative test, and real frozen Core `validate_evidence_package_basis`, `task_authority_sources` on ALL 36, and Supplement manifest validity, without monkeypatch or runtime source-class override. If a historical state-basis wrapper is required, document **exactly** which Core function is intercepted, why, and prove it cannot suppress source, accepted-Screening, or current-State SHA drift; otherwise STOP `CORE_ACCEPTANCE_BLOCKED`.

## 2. MANDATORY SC-E41-06 narrow editorial/provenance cleanup

- In new or revised reviewer input/Card, change absolute “no blog.google 2.1 rollout post exists” into scoped factual “no matching first-party announcement located among sources checked”; classify the exhaustive-negative-search inference appropriately, rather than citing the positive model card alone as proof of web-wide absence.
- For the eight supplement entries, preserve seven archived raw excerpts and exact proven bytes/SHA unless source-substance changes are essential. Existing timestamp precision is **bundle-level**, not exact individual HTTP retrieval. Reconcile `accessed_at` provenance to real logged collection instants; visibly label any schema-required estimate `BUNDLE_WINDOW_ESTIMATE / PER_PAGE_UNKNOWN` in a separate, task-ID keyed provenance ledger and downstream Card limitations. Never claim a per-page exact fetch clock without direct log proof.
- Distinguish literal issuer excerpts (bounded) from appended analyst NOTE statements; do not mark these as unmodified full HTML/PDF. No technical report methods, metrics, licensing or model weights can become VERIFIED merely because a URL or excerpt exists.
- Maintain StepFun/time-sensitive model HOLDs, W40 four carried HOLDs, Clef blog vs later X clock, Microsoft day-only and Tencent month-only, Nace original Sep24 release vs later X. No new news-window candidates or broad research rerun in this hygiene-only step.

## 3. Canonical Evidence Acceptance (only after required proofs PASS)

Keep original r1 Evidence and original r4 proposal as historical evidence. Build/version r5 candidate files only as needed for corrected Card/Task/result SHA. Ensure:
- derived package holds 36 tasks for all 36 non-DROP accepted Discovery IDs;
- r4 `external/evidence-supplement/evidence-authority-supplement-r4.json` holds eight legally bound entries, seven raw files with full raw SHA/byte verification;
- Cards exactly 36, no dangling `source_ids`, all primary model-card/blog claims bind exact authoritative supplement source IDs when not already directly in accepted Discovery; no vendor benchmark presented as independently reproduced; author claims stay bounded to body actually consumed;
- Core `validate_evidence_card` **36/36 with repo_root and source authority** PASS and `validate_evidence_package_basis` PASS, no `task_source_ids=None` or unrecorded bypass;
- accurate statuses VERIFIED/PARTIAL/NEEDS_MORE and MATERIAL/HOLD/CONTEXT with all evidence not found explicit (do not force a target ratio).

ONLY THEN use frozen `scripts/survey_evidence_v2.py` `accept_evidence_results` + `validate_evidence_acceptance` to create real `evidence-accepted.json` and full immutable 36-card accepted result set (obtain actual CLI/API signature; no hand-engineered approval JSON). Read back exact accepted manifest paths and SHA/digests.

If legitimate frozen Core acceptance refuses the reviewed projection or source supplement, STOP with error and **do not mutate Core** or fake stage PASS.

## 4. Edition Views Acceptance and Materiality/Completeness proposals

After canonical Evidence acceptance, rebuild all 36 Edition Views with actual **accepted Evidence Card/result SHA** identities (not obsolete provisional r2 Card SHA or unaccepted package SHA). Validate all 36 via frozen `validate_edition_view`, accept via `accept_edition_views`, and validate accepted Views. Preserve source-to-claim role, temporal HOLD, 12 NEEDS_MORE, and reader-facing Japanese terminology hygiene; do not inflate X/Grok contextual entries into technical articles.

Prepare **nonaccepted**, schema-checked Materiality Ledger and Completeness Assessment as Sol review inputs with:
- 37 Discovery → 37 Screening → 36 Evidence and 36 Views (1 DROP Negative-space meta-row);
- explicit 21 provisional MATERIAL / 13 HOLD / 2 CONTEXT source-based justifications, or defensible updated grouping;
- coverage of required Weekly research dimensions, event dedup, tech depth, counterfactual high-material omissions (e.g. Nano Banana, d1, Nova Sonic, textGrain, Mistral, Haiku, embedding, decision and local/edge), no empty short issue due to unjustified holding;
- direct/delegated original material actually consumed vs only cited locator vs original-byte HTML/PDF not consumed, license/weight/version/vendor-benchmark bounds;
- four W40 carryover holds, ambiguous Oct9 cutoff, Daily X 7 originals/92 topics + 09:00 absence and weekly-Grok 14 links (12 in, 2 post) with no false independent verification;
- assessment of any gaps material enough to prevent formal Materiality/Completeness PASS and candidate preliminary ranking (but NO canonical Selection).

## 5. Mandatory stop and final report

**Do NOT** advance `CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED` (Core's combined Evidence+Materiality+Completeness transition), do NOT claim Materiality/Completeness checkpoints passed, do NOT run canonical Selection/Architecture/Draft/PDF or make Human Gate decisions.

Stop at `SOL_MATERIALITY_COMPLETENESS_REVIEW_READY` ONLY if all frozen Core acceptance+View validators truly pass; else `SOL_MATERIALITY_COMPLETENESS_REVIEW_BLOCKED` with exact failure. State stays `CANDIDATES_NORMALIZED`.

Create edition-local session, SC-E41-05/06 attestation + SHA crosswalk and `execution/SOL_MATERIALITY_COMPLETENESS_REVIEW_HANDOFF-r5.md` reporting final remote HEAD/Tree, main/Core exact identity, changed-path list, original/derived Task projection proofs, Source supplement hash/byte proof, exact Evidence+Views accepted manifests and 36 SHA-bound entries, provisional Materiality/Completeness inputs and unresolved primary-body/temporal constraints. Normal commits and non-force push, exact remote readback.
