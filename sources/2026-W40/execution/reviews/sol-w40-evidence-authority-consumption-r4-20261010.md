# Sol W40 Evidence Authority-Consumption Review r4 — r7 technical PASS; precise chronology cleanup pre-acceptance

Status: **SOL_EVIDENCE_AUTHORITY_CONDITIONAL_PASS / AUTHORIZE_BOUNDED_ACCEPTANCE_AFTER_DETERMINISTIC_CHRONOLOGY_CLEANUP**  
Review: 2026-10-10 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Branch: `weekly/2026-W40-v2-work`  
Reviewed Muse r7 HEAD/Tree: `1e54815fd6f2b4ab1bd0597338219993cb463f0a` / `62dac8e51c9a6c7bba2b841bfb992707fc37ebf2`  
Reviewed main HEAD: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Editorial time window: `[2026-09-25T22:00:00Z, 2026-10-02T22:00:00Z)`.

This is a Sol technical/editorial authority decision; it **does not itself create** an accepted Evidence Card set, Core Stage Checkpoint, `EVIDENCE_REVIEWED` State or Human Gate. Only the **explicit narrowly specified** chronology/legacy-title correction below is authorized without a further intervening Sol review, because no new technical claim/source/Selection decision is allowed.

## 1. Execution-identity and provenance — PASS

- r7 direct-parent chain: `349644263bf63a19776f7a4ef23a9c5ee637a5e9` → `1e54815fd6f2b4ab1bd0597338219993cb463f0a` (one normal fast-forward commit). 82 files, all `sources/2026-W40/**`; no shared Core, main, W39, Human Gate, or Production State write.
- State `CANDIDATES_NORMALIZED`, next `stage:evidence-materiality-completeness`; Evidence/Materiality/Completeness all pending.
- Existing canonical Discovery 37 and Screening 37 unchanged; 35 r1 tasks, r5/r6 historical proposals, r6 supplement, Grok Raw and Daily X 64 ID ledger preserved.
- Frozen-Core-compatible r7 derived Task package: 35 tasks, approved 3 exact source-type projections (`PRIMARY_RESEARCH_ABSTRACT`→`PRIMARY_PAPER` 2; `EVALUATOR_PUBLISHER`→`PRIMARY_OFFICIAL` 1), 32 unmodified types, and three supplemented tasks.
- r7 Evidence Authority Supplement SHA256 `8012cec07cd70587709aa41e43dce44c2ff0601dabf9507167f1e2ba02eb6059`, four task-bound sources: ELYZA 33B/MoE pinned official model cards, Context Language Models v1 paper, ProvenanceGuard official paper v2.
- Muse r7 deterministic report: double-build identical, unknown-type and canonical unsupported-type fail-closed, `task_authority_sources` 35/35, `validate_evidence_card` 35/35 PASS, **29 VERIFIED / 6 PARTIAL**, 35 unique candidate/task IDs; no canonical Evidence acceptance.
- Direct diff of r6→r7 reviewer input: exactly **one** edited record `w40-primary-provenanceguard-20260929`; all other 34 records unchanged.

## 2. SC-E09 version/content identity — PASS

Source read independently by Sol: `https://arxiv.org/html/2606.18037v2`. Original arXiv header: `arXiv:2606.18037v2 [cs.AI] 26 Jul 2026`; **four authors** Ander Alvarez, Santhiya Rajan, Samuel Mugel, Román Orús.

First-party arXiv current submission history viewed during this review at `https://arxiv.org/abs/2606.18037`:
- v1: **2026-06-16 15:10:29 UTC**;
- v2: **2026-07-26 10:47:53 UTC**;
- **no v3 appears in the official submission history currently displayed**.

Sol independently checked v2 original body for 281 captured traces, 40/361 held-out claims, 260 source-eligible, reject F1 **0.802**, source ownership **0.858**, source+relation **0.681**, 59 questions/254 cases/2587 rows/263 claims in multi-source eval, F1 **0.846**, source **0.503**, source+relation **0.229**, and RF 400 trees/d5/leaf8/threshold 0.65. These match r7 field-by-field comparison and its accepted *source-bound interpretation*. They are original authors' evaluated metrics, not independent reproduction.

r7 source entry `supplement-src-700ea3fb3655e466` is now `PRIMARY_PAPER`, locator `https://arxiv.org/html/2606.18037v2`, published `2026-07-26T10:47:53Z`, original r5 excerpt with unchanged SHA `9cf1f9735f57c27af65b8bf4551d1d831c8e6ecb8f2f8eaf1752e31b956a37ed`, and exact task identity. Card's sole `SOURCE_PUBLICATION_OR_RELEASE` event is v2 July 26 (pre-window). The W40 new event is **2026-09-29 team-blog explanation**, not the arXiv paper.

r7 appropriately withdrew unverified Gemma-4-E4B and gpt-5.4 judge-path claims. v3 paper body was never consumed; PDF bytes and some appendices remain unconsumed and are bounded appropriately.

## 3. SC-E10 minor but mandatory acceptance hygiene: residual unsupported v3 metadata

Despite SC-E09 source pin PASS, r7 Proposed Card and reviewer input still state `v3 Aug 27 2026 (current)` in claim-1/claim-2 and contextual role, plus the inherited legacy `src-1.title` says `paper Aug 27 pre-window`.

The **first-party currently displayed arXiv History lists only v1/v2**. W40 must not publish/accept editorial metadata asserting a v3 date or current status based solely on a secondary catalog. This does **not** invalidate the proven v2 equations/table and requires **no new research sweep**.

Before formal acceptance:

1. Produce new versioned preacceptance reviewer input/Card generation, **replace/remove positive v3 existence/current/2026-08-27 assertions** in editorial claim text, source-role summaries, item-level publication chronology and future reader-facing View prose; retain only v1 June16 and v2 July26 pinned facts, plus Sept29 team blog.
2. Preserve any historical canonical Discovery/Screening `src-1.title` if frozen Core requires byte identity, but explicitly tag its Aug27 bibliographic aside as `LEGACY_UNVERIFIED_DO_NOT_CITE` in a new edition-local override/exclusion/readme entry. It cannot be used as authority for paper publication timing. Cite supplement v2 when discussing paper results.
3. Revalidate 35 new Core Cards under the **exact current implementation and revised result-package SHA**; do not simply copy r7 Cards and claim their old SHA remains valid. No new scientific claims, changed numbers, or expanded materiality decisions are authorized as this cleanup.
4. If removal affects frozen Core task-source identity or cannot be represented without mutating canonical Discovery/Screening, STOP `ACCEPTANCE_BLOCKED` and ask Sol; do not change canonical source authority.
5. A short correction attestation with diff/grep proof must be included in next Muse handoff, including how downstream Views avoid resurrecting `v3`.

This is a **deterministic, content-constrained approval** of technical Evidence basis; it is not permission for Muse to invent a new Sol PASS on unrelated Evidence.

## 4. Authorized next unit and hard semantic boundary

Sol authorizes the next Muse bounded execution unit, **subject to SC-E10 cleanup first**, to:

A. regenerate official frozen-Core-valid derived 35-task package (using approved W40 projection and r7 4-entry supplement) and 35 vetted Card source bindings, and formally accept **Evidence 35** if all authentic validators pass;

B. rebuild exactly 35 Edition Views binding **accepted Evidence result SHAs**, with corrected scientific/source titles and sensible 30 MATERIAL / 4 HOLD / 1 CONTEXT *proposals* as independent editorial inputs, and formally validate/accept Views if legitimate;

C. draft Materiality Ledger and Completeness assessment with profiles, source-consumption states, temporal holds, counterfactuals and residual limitations; **stop before asserting Sol final Materiality/Selection PASS**;

D. **Do not advance** `CANDIDATES_NORMALIZED → EVIDENCE_REVIEWED` or declare materiality/completeness checkpoints passed in this unit, because the reviewed Core stage is a combined Evidence+Materiality+Completeness transition; Sol must first independently inspect materiality, omissions, and completeness against the newly accepted Evidence/View pair.

Frozen Core `CV2-DM-016` remains OPEN; the local approved 3-type mapping is not a general Core fix. Model releases and benchmark reports should not be conflated; archive genuine limitations. W39 rumors remain HOLD; AstaBrief/AutoSynthData cutoff unresolved; Olmo-core 3 technical report >5MB not consumed.

Terminal Sol decision: **`EVIDENCE_R7_TECHNICAL_PASS / CHRONOLOGY_CLEANUP_REQUIRED_BEFORE_ACCEPTANCE`**. Proceed only under next contract at `sources/2026-W40/execution/instructions/2026-10-10_muse-w40-evidence-acceptance-materiality-preparation-r8.md`. Next Sol boundary: independent Materiality+Completeness+Selection-input review. No Human approval or Architecture authorization.
