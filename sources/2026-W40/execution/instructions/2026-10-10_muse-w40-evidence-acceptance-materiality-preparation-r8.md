# W40 Muse r8 — conditional Evidence Acceptance and Materiality/Completeness review-preparation

Status: `SOL_BOUNDED_EXECUTION_AUTHORITY / R7_TECHNICAL_PASS / SC-E10_CLEANUP_THEN_ACCEPT_EVIDENCE_VIEWS / STOP_AT_SOL_MATERIALITY_REVIEW`  
Authority: `sources/2026-W40/execution/reviews/sol-w40-evidence-authority-consumption-r4-20261010.md`  
Repository: `eariver/japanese-generative-ai-survey`  
**Only existing branch:** `weekly/2026-W40-v2-work`  
Reviewed main SHA: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Reviewed Muse r7 HEAD/Tree: `1e54815fd6f2b4ab1bd0597338219993cb463f0a` / `62dac8e51c9a6c7bba2b841bfb992707fc37ebf2`  
Exact Muse r8 Starting SHA/Tree: given in Sol outer invocation **after** this instruction is committed.

## 0. Zero-write admission and irreversible limits

Before ANY write, read-only verify remote W40 HEAD == invocation's Starting SHA, its commit Tree == invocation Starting Tree, remote main HEAD == `afdb3df3faa20af3bb5798be429bba8dbd2100b1`, starting SHA descends from reviewed r7 `1e54815fd6f2b4ab1bd0597338219993cb463f0a`, Production State `CANDIDATES_NORMALIZED` / next `stage:evidence-materiality-completeness`, Evidence/Materiality/Completeness checkpoints pending and both Human Gates pending. Any mismatch: STOP and report expected/actual, **ZERO WRITES**.

No new/fallback/review/repair branch; no reset, rebase, force push or history rewrite; no shared Core, schema, config, CI, `main`, W39/other edition or Human Gate edit. Use exclusively existing W40 edition-local files, normal commits and non-force push, remote read-back after each authoritative transition. Preserve immutable r1-r7 historical proposals.

## 1. SC-E10 mandatory source chronology sanitization — BEFORE Evidence acceptance

Original, directly verified official source:
- `https://arxiv.org/html/2606.18037v2` — v2 July 26, 2026, four authors; source of ProvenanceGuard equations/results;
- `https://arxiv.org/abs/2606.18037` — current official history shown to Sol: v1 June 16 15:10:29Z, v2 July 26 10:47:53Z, **not an official v3/Aug27 record**.
- Sep29 Multiverse team blog is the W40 ordinary event and may refer to earlier paper; do not convert any original paper revision into W40 publication.

Correct residual `v3 Aug 27 current` assertions from r7 reader-input claims, Card claims, chronology and any new Edition View prose. Remove claims about gpt-5.4/Gemma4 adjudicators absent from read v2; do not reintroduce them as factual provenance. Preserve source facts/method/metrics validated under official pinned v2, publisher-attributed. Leave r7 supplement with v2 locator/July date unchanged if it passes exact SHA/rights checks. **Avoid rewriting historical accepted Discovery/Screening** even though the legacy `src-1.title` includes an unverified Aug27 aside; author an immutable edition-local `LEGACY_UNVERIFIED_DO_NOT_CITE` provenance exception and ensure the View does not surface/endorse that historical string. If your Core Card generation makes the source title appear automatically, annotate its role as historical lineage/non-authoritative for paper chronology, while binding results only to `supplement-src-700ea3fb3655e466`.

Create diff/grep QA over all new reader-facing claim fields and new View prose (not over preserved raw historical files) proving that positive `v3`/Aug27 current-version claims have been removed. If a source title cannot be corrected while obeying Core validation, document it as immutable historical metadata and **fail closed** if it leaks into publication prose.

## 2. Official Evidence Acceptance (only if SC-E10 and frozen validators PASS)

R7 source basis: `external/evidence-supplement/evidence-authority-supplement-r7.json`, SHA256 `8012cec07cd70587709aa41e43dce44c2ff0601dabf9507167f1e2ba02eb6059`; approved 3/35 edition-local task `source_type` projections; original 37 Discovery and 37 Screening accepted unchanged.

Build a **new r8** 35-task Evidence package/Card set under the CURRENT exact approved Core `implementation_sha`, since frozen validators bind implementation identity and task SHA. Do not accept old r7 `PROPOSED` Cards by file copying or pretend a different implementation SHA is identical. Keep a deterministic provenance ledger r1→r5→r6→r7→r8; precise 3 projected task fields, all supplement source IDs and original source content hashes, no other source type or scientific claim drift. Double-build reproducibility and negative tests for unmapped types.

Run actual `survey_evidence_v2.validate_evidence_package_basis`, `task_authority_sources` on ALL 35 with task-source binding ON, `validate_evidence_card` on EVERY Card with its exact r8 Task SHA/Package and `repo_root`. Require correct supplemented sources for ELYZA 33B/MoE, ProvenanceGuard v2 and Context Language Models v1. Status 29 VERIFIED / 6 PARTIAL and 35 task coverage, unless a concrete validator/source contradiction forces fail-closed STOP.

Then use frozen Core **`accept_evidence_results` and `validate_evidence_acceptance`** (not manual acceptance JSON) to materialize immutable, exact-SHA `evidence-accepted.json` and accepted 35-task/result copies. Audit acceptance list and result_set digest, source_role and version chronology, and record actual Core output/exit codes. **If Core will not legally accept derived projection+supplement, STOP CORE_ACCEPTANCE_BLOCKED; do not skip source binding or monkey-patch Core.** Stage state must remain `CANDIDATES_NORMALIZED` until later Sol materiality review.

## 3. Edition Views acceptance and Materiality/Completeness proposal

Reconstruct all **35 Edition Views** from the *accepted Evidence Card result SHAs*, not from the r7 task/package SHAs or the historical draft Views. Keep technical scope and hold distinctions; do not auto-promote a social/rumor source into verified authority. Review ELYZA as a provisional important Japanese-model MATERIAL candidate with both independently pinned model-card citations and benchmark caveats; preserve W39 carryover HOLDs, AstaBrief/AutoSynthData cutoff unknown, LIFT pre-window, source-limited Olmo report and TG performance claims.

Use frozen `validate_edition_view`, `accept_edition_views` and `validate_edition_views_acceptance` on 35 exact view↔accepted Evidence result SHA links; preserve immutable accepted Views/run authority. Use class/version-safe summaries and explicit caveats, especially ProvenanceGuard paper v2 vs W40 team blog.

Based on accepted Evidence+Views, generate schema-valid **proposed/draft** Materiality Ledger and Completeness Assessment with:
- 37 Discovery records -> 37 Screening -> 35 non-DROP Evidence Card/View pairs;
- rationales for 30 provisional MATERIAL / 4 HOLD / 1 CONTEXT (recompute if legitimate evidence changes), plus alternative grouping by substantive theme and why strong candidates omitted;
- coverage across 12 A–L research lanes, important omitted-type counterfactual and overshort issue prevention;
- material primary-source-consumed vs absent/retrieval-failed/captured-but-unconsumed distinctions (not automatic VERIFIED based on locator);
- timestamp ambiguity (AstaBrief/AutoSynthData) and licensing/version/publication distinctions;
- residual limitations for unconsumed report/code/quantitative vendor claims, no false `READY` if material obligations unresolved.

**DO NOT** mark Materiality or Completeness accepted or create canonical Stage Checkpoint, since Core `CANDIDATES_NORMALIZED` transition sets **Evidence+Materiality+Completeness** all passed together. Sol must inspect final Materiality/Completeness and proposed Selection judgment first. Do not start actual Selection/Architecture/Draft or Human Gate.

## 4. Validation logs, stop and dossier

Write `sources/2026-W40/execution/SOL_MATERIALITY_COMPLETENESS_REVIEW_HANDOFF-r8.md` with:
1. Starting/Final HEAD/Tree, reviewed main, exact ancestry/changed file allowlist, nonforce push/readback and State/Gate invariants;
2. SC-E10 positive false-version claim cleanup diff/grep and original-version source proof, with any immutable legacy title explicitly excluded from editorial authority;
3. r8 compat projection + supplement Sha, 35 task/card SHA chain, actual frozen Core exit codes, negative tests;
4. exact canonical Evidence accepted path/SHA, 35 accepted cards and source map, canonical Edition Views accepted path/SHA and 35 bound evidence-result SHA links;
5. provisional 37/37/35 materiality + completeness, source-consumption and counterfactual review, high-signal HOLD reasoning;
6. all unresolved actual first-party authority gaps and never-downgraded provenance warnings, CV2-DM-016 still OPEN_CORE;
7. explicit next Sol review questions and terminal decision `SOL_MATERIALITY_COMPLETENESS_REVIEW_READY` or `SOL_MATERIALITY_COMPLETENESS_REVIEW_BLOCKED`.

If any Evidence/View acceptance cannot be canonicalized due to frozen Core basis constraints, STOP `SOL_MATERIALITY_COMPLETENESS_REVIEW_BLOCKED` with precise failure, preserving edition-local validated work; do not manufacture stage/acceptance PASS. Do not alter existing accepted Discovery/Screening, any Shared Core, Production State, Human Gate or Selection/Architecture authority.

**Bounded terminal State expected `CANDIDATES_NORMALIZED`.** After Sol independently approves Materiality/Completeness, a separate instruction can call normal Core stage checkpoint/transition and then advance Selection.
