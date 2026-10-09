# TS-003 execution instruction — Draft r4 to Draft r5 final reader-surface cleanup

Status: `EXECUTION_AUTHORITY / SOL_DRAFT_R4_REQUEST_CHANGES / FINAL_READER_SURFACE_CLEANUP_ONLY`

Date: `2026-10-02 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Authorities

Sol Draft Review r4:

`sources/SP-vision-multimodal-2026/execution/sol-draft-review-r4.md`

Decision:

`REQUEST_CHANGES`

Reviewed Draft r4 authority commit:

`f90f6000538437985b683edb1b2c4c33e2d067c5`

Reviewed tree:

`8807609dd8755cfdb7df6dc7b558c54822e5489e`

Binding cumulative terminology authority:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

Authority update commit:

`1b5184fda07afe4f8ffaff6124d09cfbfb364a1f`

Expected map blob SHA:

`45d8eb53a14ab9a50dd6eab7b74326ad7108dc5e`

Expected map terminal state:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R5_BINDING`

Human Architecture r2 remains APPROVED.

This request does not reopen Architecture and is not a new Human gate.

## 2. Start guards

The Sol launch message supplies the sole exact work-branch starting HEAD/tree.

Before any write, read-only verify:

- remote work branch HEAD/tree == launch-message expected HEAD/tree;
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- cumulative terminology map blob == `45d8eb53a14ab9a50dd6eab7b74326ad7108dc5e`;
- cumulative terminology map terminal state == `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R5_BINDING`;
- issue == `SP-vision-multimodal-2026`;
- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- draft checkpoint == passed;
- validation/publication_preview/freeze/release == pending;
- current Architecture SHA-256 == `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- current Selection SHA-256 == `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`.

If any guard differs, perform zero writes and report expected vs actual.

No new branch, fallback branch, repair branch, review branch, reset, rebase, cherry-pick, squash, force push, or history rewrite is authorized.

## 3. Mandatory read order

Read:

1. this request;
2. `execution/sol-draft-review-r4.md`;
3. `execution/drafting-language-policy-ja.md`;
4. `execution/drafting-terminology-map-ja.md`;
5. `execution/language-qa-ja-draft-r4.md`;
6. `execution/draft-r4-20261002/draft-r4-review-report.md`;
7. all 16 canonical Draft r4 Results;
8. current profile synthesis;
9. approved Architecture r2;
10. unchanged Draft Packages;
11. frozen Core Draft schema/prompt/non-mutating validators.

Do not treat Worker r4 `PASS_WITH_NOTES` as Sol approval.

## 4. Mission

Produce Draft r5 as a final bounded reader-surface cleanup.

The purpose is not to rewrite the volume again. Repair only residual terminology/shorthand defects identified by Sol r4 review plus any genuinely new equivalent found during the mandatory full-text pass.

Do not rerun or modify:

- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture;
- Human Architecture approval.

Do not add sources or factual claims from memory/web.

Keep all 16 Draft Package files byte-identical.

Preserve r1-r4 as immutable Git history.

## 5. Mandatory targeted repairs

### 5.1 P06 headline

Current:

`Transformerと自己教師の土台`

Repair both issues:

- self-supervised concept -> `自己教師あり` / `自己教師あり学習`;
- technical foundation/base sense -> `基盤`, `基盤表現`, or another established Architecture-consistent term.

Do not keep either `自己教師` or technical `土台` in the headline.

### 5.2 P06 technical mechanism wording

Repair:

- `言葉側だけを締める調整`;
- `一対の判定に還す`.

State exactly which component is adjusted/frozen and how the sigmoid objective operates, using only bound Evidence.

### 5.3 P06 source/citation boundary wording

Repair:

- `引用の結び`;
- `典拠の結び`;
- `手順の借り`;
- `仕組みの消費`;
- `結びの節`;
- `結びの話`.

In particular, the CLAIM_BOUNDARY must state directly:

- DeiT mitigates data dependence through its training procedure/recipe;
- SigLIP mechanism support is limited to the evidence level actually bound;
- precise source/citation correspondence remains unresolved if that is the preserved limitation.

No production-side “consumption” language may appear in reader text.

### 5.4 P07A contrastive-learning wording

Repair:

- `文と絵の組を大量に当て`;
- `決まった範疇の表引き`;
- `4億ペアの当て`;
- `30超の束`.

Use explicit terms such as:

- image-text pairs;
- contrastive learning/alignment;
- fixed-class classification;
- 30+ datasets/evaluation tasks;
- zero-shot transfer.

Preserve Evidence scope and attribution.

### 5.5 Other residual shorthand

Audit and repair as needed:

- P07B `ODinWを野外の補いとして添える`;
- P09 sequence-representation sense of `列に変える契約`;
- P11 evaluation-separation sense of `別の列に置く`;
- P06 technical `Transformerを渡す役割`;
- P07A `次の節への渡し`.

Name the actual mechanism/role/evaluation axis directly.

## 6. Full cumulative-map Pass A/B/C remains mandatory

Apply the entire cumulative R5 map, not only §3.5 examples.

Pass A:
- preferred/avoid conformance across headline/deck/PARAGRAPH/BULLET/TABLE/CLAIM_BOUNDARY/synthesis.

Pass B:
- every known-failure registry entry with semantic classification.

Pass C:
- full manual read of all 16 packages + synthesis + boundaries.

If a genuinely new failure is found:

1. add it to the cumulative map first;
2. repair every occurrence;
3. rerun Pass A/B/C;
4. report final map blob SHA.

Do not silently fix a new failure without recording it.

## 7. Preserve prior gains

Preserve:

- zero exact duplicates;
- no padding;
- all r1-r4 terminology repairs;
- technical segmentation correctness;
- code/encoding distinction;
- source/evaluator attribution;
- Japanese CLAIM_BOUNDARY wording;
- P07B mechanism grouping;
- P09 protocol-bound comparisons;
- P15 synthesis density;
- G01-G06/PARTIAL semantics.

Do not restore r1 length.

## 8. Integrity

Preserve all required Evidence references and must-cover content.

Do not change Architecture.

Do not add research.

If a wording repair cannot be made without new Evidence, leave the factual scope unchanged and flag the issue for Sol.

## 9. Language QA r5

Create:

`sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r5.md`

It must include:

- map authority path/blob/status;
- exact duplicate scan by package and cross-package;
- full preferred/avoid conformance;
- full registry audit;
- P06 headline audit;
- P06 mechanism wording audit;
- P06 CLAIM_BOUNDARY/source-linkage audit;
- P07A contrastive-learning terminology audit;
- P07B ODinW wording audit;
- P09 token/sequence wording audit;
- P11 evaluation-axis wording audit;
- all retained context-sensitive hits with exact sentence + classification;
- P06/P07A/P07B/P09/P11/P15 qualitative review;
- any newly discovered failure and map update.

Regex counts alone are insufficient.

## 10. Deterministic validation

Run available canonical non-mutating Draft Result and synthesis validators at `DRAFT_COMPLETE`.

Do not fake lifecycle rollback.

Do not call reader-publication validation.

## 11. Required r5 review report

Create:

`sources/SP-vision-multimodal-2026/execution/draft-r5-20261002/draft-r5-review-report.md`

Report:

- startup guards;
- reviewed r4 commit/tree;
- Sol r4 review authority;
- map starting blob/status;
- map changes if any + final blob;
- unchanged Draft Package hashes;
- revised Draft Result hashes;
- synthesis hashes;
- duplicate scan;
- terminology conformance;
- registry audit;
- targeted r4 residual closure;
- source-role preservation;
- CLAIM_BOUNDARY status;
- G01-G06/PARTIAL preservation;
- P06/P07A/P07B/P09/P11/P15 manual review;
- QA r5 path/hash/status;
- deterministic validation result;
- lifecycle/next_action;
- Publication Preview pending;
- main/Core unchanged;
- final HEAD/tree.

## 12. Lifecycle boundary

Keep `DRAFT_COMPLETE`.

Do not:

- call reader-publication validation;
- create Publication Preview;
- record Human Publication Preview decision;
- Freeze;
- Release.

## 13. Terminal condition

`TS-003 DRAFT_R5_FINAL_READER_SURFACE_CLEANUP_COMPLETE`

`TS-003 LANGUAGE_QA_R5_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW_R5`

`NO_READER_PUBLICATION_VALIDATION`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

STOP there.
