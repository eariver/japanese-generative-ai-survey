# Sol W40 Evidence Authority-Consumption Review r3 — VERSION-PIN CORRECTION REQUIRED

Decision: **`SOL_EVIDENCE_AUTHORITY_BINDING_STRUCTURAL_PASS / SCIENTIFIC_VERSION_PIN_CORRECTION_REQUIRED`**  
Date: 2026-10-10 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Existing branch: `weekly/2026-W40-v2-work`  
Reviewed Muse r6 HEAD: `b33f6aae45605ebf17792f4bd588252d76bfb860`  
Reviewed Muse r6 Tree: `6498ea6560778c4d1cd261eb93529f58e26ce7c8`  
Reviewed main HEAD: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Scope: W40, Evidence preacceptance only. State `CANDIDATES_NORMALIZED`; Human Gates pending/pending.

## 1. Execution guard — PASS

Read-only remote verification: r6 starting HEAD `edaa67d3684c878221f071a5da327b7d1f8faf77` is the sole immediate parent of r6 Final HEAD `b33f6aae45605ebf17792f4bd588252d76bfb860`. Exactly one fast-forward commit; 80 changed/added paths confined to `sources/2026-W40/`. Reviewed main identical; original 37 Discovery and accepted Screening unchanged, Core unchanged. Canonical state remains `CANDIDATES_NORMALIZED`; no Evidence Acceptance/checkpoint nor Selection/Human Gate.

## 2. Core compatibility and authority binding — SUBSTANTIAL PASS

- 35 tasks in `execution/compat/evidence-supplement-card-binding-r6/compat-package/package.json`. Sol-approved three `source_type` changes retained from r5 and original tasks not overwritten. Frozen Core builder used to bind four explicit Evidence Authority Supplement sources to three tasks; report logs 35/35 recognized task classes, double-build identical and unknown-type fail-closed.
- Evidence Supplement: `external/evidence-supplement/evidence-authority-supplement-r6.json` SHA256 `8872acfd2bebcc6b01907be9a219e33b1ce86dc39d023e585893f917e23e9c88`. Four items with exact task binding / excerpt SHA: ELYZA 33B, ELYZA 32B-A3B (both PRIMARY_REPOSITORY), ProvenanceGuard paper and Context Language Models full-text (PRIMARY_PAPER).
- 35 complete proposed Cards built and frozen `validate_evidence_card(...,repo_root=...)` reported 35/35 PASS; 29 VERIFIED + 6 PARTIAL; 127 claims and explicit supplement citations. No canonical acceptance created. Schema PASS is evidence of structural correctness, **not** proof that every claimed paper revision was consumed.
- ELYZA benchmark/Apache license claims now bind both pinned original issuer model cards rather than relying solely on legacy SECONDARY/UNVERIFIED Discovery source. ProvenanceGuard methods and CLM fulltext also supplement-bound. Other candidate status and previous semantic caveats preserved.

## 3. SC-E09 [BLOCKER] — Consumed ProvenanceGuard edition does not substantiate v3-specific source metadata

The r6 Supplement currently states:
- title `ProvenanceGuard original paper ... v3 current at access`;
- `published_at=2026-08-27T16:15:34Z`;
- locator `https://arxiv.org/abs/2606.18037` (unversioned);
- relation: ar5iv latest rendering **ASSUMED v3**.

Muse r5 bounded excerpt `collectors/primary/runs/20261010T060000Z-muse-r5/provenanceguard-paper-ar5iv-260618037.source-excerpt.md` names **four** authors: Ander Alvarez, Santhiya Rajan, Samuel Mugel and Román Orús. The primary version-pinned arXiv `https://arxiv.org/html/2606.18037v2` explicitly identifies **v2, July 26**, and these four authors, with the consumed method/evaluation text, 281 traces, 0.802 / 0.858 / 0.846 / 0.229 metrics. The unversioned primary arXiv abstract view available to Sol displays v1 Jun 16 and v2 Jul 26; more recent third-party catalogs mention Aug 27/v3 (some with additional authors), which means **v3 existence or later catalog metadata must not be inferred as the exact edition Muse consumed** without a version-pinned original-body comparison.

This is not a claim that v3 categorically does not exist. It is a concrete **consumed-content-to-publication-version mismatch**. Existing r6 Card also emits an `event` on Aug 27, semantically stronger than the evidence of the consumed v2. It may be safely corrected without changing the W40 event: **the Sep 29 team-blog exposition remains the W40 event; either v2 or later manuscript revisions are pre-window**.

### Required correction

1. Fetch or use the official **version-pinned v2 HTML** `https://arxiv.org/html/2606.18037v2`, explicitly match the reused first-party method/metrics and record limits. If independently shown that r5 excerpt actually derives from v3, provide exact v3 primary URL and evidence/field-by-field differences. Otherwise pin v2, with `published_at=2026-07-26T10:47:53Z`, and remove `v3 consumed`/Aug 27 event from actual Card/supporting reviewer input.
2. Reissue a **new r7 Evidence Authority Supplement identity**, preserve the other three accepted mappings/entries; rewrite only ProvenanceGuard supplement source/relation/publication version and, where appropriate, use exact version-qualified locator. Preserve the r6 supplement as historical PROPOSAL (not an accepted authority).
3. A supplement SHA change propagates to derived package and all 35 Card basis SHAs, so deterministically regenerate proposed 35 package tasks/Cards in a **new r7 directory** and validate all 35 with frozen Core binding enabled. No card acceptance or stage transition until Sol review.
4. Keep ELYZA, CLM, Gemini and other scientific content unchanged unless a concrete corresponding source-version mismatch is proven. No reopening broad Source Intake/Discovery.

## 4. Remaining non-blocking limitations / no new authority

- Dataset/rate/reproduction limitations from r5/r6: Olmo-core 3 report body >5 MB and unread; CLM paper appendix and PDF bytes unconsumed; honest ELYZA vendor benchmarks; unresolved AstaBrief/AutoSynthData cutoff times, W39 Pixel Canary/TBC HOLD. These are explicit Evidence/Selection limitations, **not global evidence completeness failure**.
- r6 marked DGX Spark 64GB `MATERIAL` with publisher metadata time 2026-10-02 13:00:39Z, whereas earlier Discovery had `TIME_UNRESOLVED`; this is candidate-level Evidence update, **not a retrospective change to accepted Discovery**. Selection must still examine the primary timestamp/price before inclusion. No broad new validation authorized in r7.
- r6 `src-1` lineage references can legitimately coexist with explicit supplement sources; card authoring should avoid interpreting all cited sources as equally authoritative for every metric. One-card source-role precision takes precedence over merely accumulating IDs.
- Frozen Core bug CV2-DM-016 remains OPEN. No Core patch/Schema edit or implicit approval of a general source classifier has occurred.

**Terminal decision:** `SOL_EVIDENCE_AUTHORITY_VERSION_PIN_CORRECTION_REQUIRED`. Authorize bounded Muse r7 consumed-source version pin plus 35-card regeneration; STOP again for Sol independent formal Acceptance review. No `EVIDENCE_REVIEWED`, Materiality/Completeness, Selection or Architecture stage advance.
