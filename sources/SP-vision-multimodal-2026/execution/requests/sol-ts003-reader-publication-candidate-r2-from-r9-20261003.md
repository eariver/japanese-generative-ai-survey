# TS-003 execution instruction — publication candidate r2 regeneration from accepted Draft r9

Status: `EXECUTION_AUTHORITY / SOL_DRAFT_R9_PASS / REGENERATE_READER_PUBLICATION_CANDIDATE_R2 / STOP_BEFORE_STAGE_VALIDATION`

Date: `2026-10-03 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Authorities

Sol Draft Review r9:

`sources/SP-vision-multimodal-2026/execution/sol-draft-review-r9.md`

Decision:

`PASS`

Accepted Draft r9 worker commit:

`79d2b3e291e10896ed616bd698abefc1e479ddbe`

Accepted Draft r9 tree:

`4d96d07db9147b3c9a973a6f3bdc6b4cd09d8b53`

Binding cumulative terminology authority:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

Expected terminology map blob:

`cf39a5860d64b5d85a3a382911680dcadaa954a1`

Expected terminology map status:

`DRAFT_R9_BINDING`

Frozen Core authority:

`production/survey-core-v2@774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Stale publication candidate r1 must not be reused as current reader authority.

## 2. Start guards

The Sol launch message supplies the sole exact current work-branch starting HEAD/tree.

Before any write, read-only verify:

- remote work branch HEAD/tree == launch-message expected HEAD/tree;
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- Frozen Core HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Frozen Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- terminology map blob == `cf39a5860d64b5d85a3a382911680dcadaa954a1`;
- issue == `SP-vision-multimodal-2026`;
- publication profile == `LONGFORM_SPECIAL`;
- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- draft checkpoint == passed;
- validation/publication_preview/freeze/release == pending;
- Architecture SHA-256 == `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- Selection SHA-256 == `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`.

If any guard differs: perform zero writes, report expected vs actual, stop.

No new branch, fallback/repair/review branch, reset, rebase, squash, cherry-pick, force push, or history rewrite.

## 3. Mandatory read order

1. this request;
2. `execution/sol-draft-review-r9.md`;
3. `execution/drafting-language-policy-ja.md`;
4. `execution/drafting-terminology-map-ja.md`;
5. `execution/language-qa-ja-draft-r9.md`;
6. `execution/draft-r9-20261002/draft-r9-review-report.md`;
7. all 16 canonical Draft r9 Results;
8. canonical profile synthesis input/result;
9. approved Architecture r2;
10. production profile/state;
11. prior rejected/stale publication candidate r1 report only for historical build mechanics;
12. Frozen Core publication/reader scripts, schemas, validators, and LONGFORM_SPECIAL configuration.

Use accepted Draft r9 as the only current reader-prose authority.

## 4. Mission

Regenerate TS-003 reader/publication candidate r2 from accepted Draft r9.

This is a content-preserving publication regeneration.

Do not revise Draft r9 prose.

Allowed transformations:

- TeX escaping;
- deterministic section/chapter assembly;
- title/front matter;
- citation/bibliography binding from already accepted Evidence;
- source notes;
- line/page breaking;
- layout-only repairs;
- publication metadata required by Core;
- deterministic reader/publication artifact generation.

Not allowed:

- paraphrasing accepted r9;
- adding/removing substantive technical claims;
- new research;
- source additions;
- Evidence/Selection/Architecture changes;
- source-role changes;
- comparison-scope changes;
- weakening CLAIM_BOUNDARY or G/PARTIAL limitations;
- terminology substitutions outside r9 authority.

If publication generation requires a substantive prose change, STOP for Sol.

## 5. Stale candidate replacement

The existing candidate r1 under:

`surveys/special/vision-multimodal-2026`

and:

`sources/SP-vision-multimodal-2026/publication/v2`

is stale.

Regenerate canonical publication outputs from r9.

Do not preserve stale r1 bytes merely to minimize diff.

Record r1 -> r2 replacement explicitly in the report.

## 6. Required publication outputs

Canonical survey root:

`surveys/special/vision-multimodal-2026`

Canonical publication authority root:

`sources/SP-vision-multimodal-2026/publication/v2`

Build the canonical LONGFORM_SPECIAL publication artifacts supported by Frozen Core, including where applicable:

- `main.tex`;
- `references.bib`;
- `main.pdf`;
- exact PDF digest sidecar;
- `reader-manuscript-v2.json`;
- `reader-surface-gate-v2.json`;
- `reader-surface-semantic-review-v2.json`;
- `quality-regression-bundle-v2.json`;
- `semantic-editorial-review-v2.json`;
- `visual-review-v2.json`;
- deterministic subject/entity/property binding;
- identifier preservation;
- PDF preflight.

Do not create Freeze/Release artifacts.

Do not create Human approval records.

## 7. Reader fidelity

Require content preservation from accepted r9:

- all 16 package identities represented;
- P07A/P07B distinct;
- no package omitted or duplicated;
- headline/deck/body meaning preserved;
- P07B mechanism grouping/depth preserved;
- P09 comparison protocol/version/config constraints preserved;
- P15 remains synthesis-led;
- source/evaluator role attribution preserved;
- CLAIM_BOUNDARY limitations preserved;
- no internal workflow labels;
- cumulative Terminology Map blocking forms absent from final publication text;
- punctuation anomaly set `、、 / 。。 / ，， / ,,` absent.

The publication generator must not reintroduce stale r1/r6 wording.

## 8. Bibliography / provenance

Use only already bound source authority.

Require:

- every citation key referenced exists;
- no invented citation;
- no missing citation binding;
- no unused publication-only invented source;
- source roles preserved;
- unresolved/PARTIAL provenance remains a limitation.

No web research to fill gaps.

If source binding is missing, STOP.

## 9. PDF build

Build exact committed PDF.

Record:

- repository path;
- blob SHA;
- SHA-256;
- byte count;
- page count;
- build method/toolchain.

Require:

- non-encrypted PDF;
- no undefined citations/references;
- no missing glyphs;
- no blocking TeX/layout warning according to canonical checks;
- no clipped text;
- no broken tables/boxes;
- no malformed headings;
- readable bibliography/source notes;
- no artificial blank-page padding.

Architecture target remains approximately 112 pages, hard maximum 120. Do not delete technical content or pad content to hit a page target.

If page count >120, STOP for Sol.

A materially shorter candidate is not itself a failure if it preserves accepted r9 content and layout is readable; record page count honestly.

## 10. Exact-PDF operator visual review

Inspect every page of the exact committed r2 PDF.

Record by page/page range:

- clipping/overflow;
- missing glyphs;
- line collisions;
- broken tables/boxes;
- bad page breaks;
- stranded headings;
- bibliography/source-note readability;
- excessive blank space/pages;
- malformed punctuation or conspicuous copy artifacts.

Formatting-only fixes are allowed and must trigger rebuild/re-review.

Any substantive prose fix requires STOP for Sol.

The worker visual review is evidence only. Sol will independently review the exact PDF afterward.

## 11. Known Core checkpoint-staleness blocker

Do not run or claim successful `DRAFT_COMPLETE -> VALIDATED_DRAFT` stage validation in this execution.

Known blocker:

- historical `ARCHITECTURE_ESTABLISHED` Draft checkpoint binds r1 Draft Result/synthesis hashes;
- accepted r9 results are legitimate reviewed successors;
- Frozen Core has no sanctioned DRAFT_COMPLETE-side Draft supersession/rebind mechanism;
- stage validation therefore fail-closes on artifact drift.

Do not:

- rewrite historical Stage Checkpoints;
- modify production-state checkpoint provenance;
- fake stage PASS;
- run `advance-stage`;
- use VALIDATED_DRAFT-only publication revalidation as a workaround.

Instead record:

`CORE_STAGE_VALIDATION_DEFERRED_KNOWN_CHECKPOINT_STALENESS`

The shared-Core repair will be handled separately after exact r2 PDF review.

## 12. Required report

Create:

`sources/SP-vision-multimodal-2026/execution/reader-publication-validation-r2-20261003/reader-publication-validation-report.md`

Report:

- startup guards;
- accepted Draft r9 authority;
- Frozen Core identity;
- stale r1 candidate identity;
- exact changed-path inventory;
- reader fidelity result;
- terminology-map final scan;
- bibliography/citation binding;
- reader-surface gate status;
- semantic/editorial review;
- deterministic quality checks;
- exact PDF path/blob/SHA-256/size/page count;
- exact-PDF visual review;
- proof publication derives from r9;
- proof production state unchanged;
- explicit known Core stage blocker/defer status;
- main/Core unchanged;
- final HEAD/tree.

## 13. Stop boundary

Keep production state byte-identical at `DRAFT_COMPLETE`.

Do not:

- run stage validation as if it could PASS;
- advance lifecycle;
- create/approve Human Publication Preview;
- Freeze;
- Release.

Normal terminal:

`TS-003 READER_PUBLICATION_CANDIDATE_R2_COMPLETE`

`TS-003 EXACT_R9_DERIVED_PDF_READY_FOR_SOL_REVIEW`

`ALL_NON_STAGE_PUBLICATION_CHECKS_PASS`

`CORE_STAGE_VALIDATION_DEFERRED_KNOWN_CHECKPOINT_STALENESS`

`PRODUCTION_STATE_UNCHANGED_DRAFT_COMPLETE`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

STOP there.
