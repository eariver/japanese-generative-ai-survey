# TS-003 execution instruction — reader/publication validation candidate from accepted Draft r6

Status: `EXECUTION_AUTHORITY / SOL_DRAFT_R6_PASS / BUILD_VALIDATED_READER_PDF / STOP_BEFORE_ADVANCE_STAGE`

Date: `2026-10-02 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Authorities

Sol Draft Review r6:

`sources/SP-vision-multimodal-2026/execution/sol-draft-review-r6.md`

Decision:

`PASS`

Accepted Draft r6 authority commit:

`a345358f568e5ab7b55798c1f8469378abbd5783`

Accepted Draft r6 tree:

`572ad64a59c1274c5b035facd2fa36c0eb4ffb6b`

Binding cumulative terminology map:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

Expected map blob:

`bad61f051146b0ec0c3fd25d72d816b2de41c53b`

Expected terminal:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R6_BINDING`

Frozen Core authority:

`production/survey-core-v2@774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Human Architecture r2 remains APPROVED.

No Human Publication Preview decision exists.

## 2. Start guards

The Sol launch message supplies the sole exact work-branch starting HEAD/tree.

Before any write, read-only verify:

- remote work branch HEAD/tree == launch-message expected HEAD/tree;
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- Frozen Core HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Frozen Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- map blob == `bad61f051146b0ec0c3fd25d72d816b2de41c53b`;
- issue == `SP-vision-multimodal-2026`;
- publication profile == `LONGFORM_SPECIAL`;
- source_root == `sources/SP-vision-multimodal-2026`;
- survey_root == `surveys/special/vision-multimodal-2026`;
- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- draft checkpoint == passed;
- validation/publication_preview/freeze/release == pending;
- Architecture SHA-256 == `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- Selection SHA-256 == `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`.

If any guard differs: zero writes, report expected vs actual, stop.

No new branch, fallback/repair/review branch, force push, rebase, reset, squash, cherry-pick, or history rewrite.

## 3. Mandatory read order

1. this request;
2. `execution/sol-draft-review-r6.md`;
3. `execution/drafting-language-policy-ja.md`;
4. `execution/drafting-terminology-map-ja.md`;
5. `execution/language-qa-ja-draft-r6.md`;
6. `execution/draft-r6-20261002/draft-r6-review-report.md`;
7. all 16 accepted canonical Draft r6 Results;
8. profile synthesis input/result;
9. approved Architecture r2;
10. production profile/state;
11. Frozen Core publication/reader scripts, schemas, and validators relevant to LONGFORM_SPECIAL, including:
   - `scripts/survey_longform_publication_v2.py`
   - `scripts/survey_reader_publication_v2.py`
   - `scripts/survey_reader_surface_gate_v2.py`
   - `scripts/survey_reader_fidelity_v2.py`
   - `scripts/survey_stage_validation_v2.py`
   - `scripts/special_publication_layout_check.py`
   - reader/publication schemas and config.

Use Frozen Core behavior as authoritative. Do not copy historical edition-specific hacks.

## 4. Mission

Build the exact TS-003 reader/publication validation candidate and exact PDF from accepted Draft r6.

The accepted Draft r6 prose is editorial authority.

Publication construction must be content-preserving.

Allowed transformations:

- TeX escaping and line breaking;
- section/chapter assembly;
- title/front matter;
- bibliography/source-note materialization from already-bound Evidence;
- citation-key binding;
- deterministic formatting;
- layout-only fixes;
- page breaking;
- publication metadata required by Core.

Not allowed without stopping for Sol:

- substantive paraphrasing of accepted r6;
- adding/removing technical claims;
- new research;
- new sources;
- altering Evidence/Selection/Architecture;
- changing source/evaluator attribution;
- weakening CLAIM_BOUNDARY or G/PARTIAL semantics;
- reintroducing terminology-map failures;
- padding to hit a page target.

If publication generation reveals a substantive prose defect, STOP and report it. Do not silently edit Draft r6.

## 5. Expected publication surface

Canonical survey root:

`surveys/special/vision-multimodal-2026`

Expected principal outputs include, as supported by canonical LONGFORM_SPECIAL tooling:

- `main.tex`;
- `references.bib`;
- `main.pdf`;
- PDF digest sidecar if the canonical path uses one;
- any canonical special-longform ancillary TeX/source files required by Core.

Canonical publication authority root:

`sources/SP-vision-multimodal-2026/publication/v2`

Build the canonical reader-validation artifact family required by Frozen Core, including where applicable:

- `reader-manuscript-v2.json`;
- `reader-surface-gate-v2.json`;
- `reader-surface-semantic-review-v2.json`;
- `quality-regression-bundle-v2.json`;
- `semantic-editorial-review-v2.json`;
- `visual-review-v2.json`;
- `deterministic/subject-entity-property-binding.json`;
- `deterministic/identifier-preservation.json`;
- `deterministic/pdf-preflight.json`.

Do not create Freeze/Release artifacts.

Do not create a Human approval record.

Do not create a Publication Preview approval.

Do not create or advance a Release Candidate merely because the PDF exists.

## 6. Reader-fidelity requirements

The publication surface must preserve the accepted Draft r6 content.

Mandatory checks:

- all 16 package identities represented;
- no package omitted;
- no synthetic package/candidate introduced;
- headline/deck/body meaning preserved;
- P07A and P07B remain distinct;
- P07B remains technically deep/mechanism-grouped;
- P09 sanctioned comparisons remain same-source/same-protocol/version-config bound;
- P15 remains synthesis-led;
- source/evaluator role attribution preserved;
- all explicit reader-facing limitations preserved;
- no internal production labels exposed;
- cumulative terminology-map blocking forms absent in final TeX/PDF text;
- bare self-supervised `自己教師` absent;
- established forms such as `ニューラルネットワーク`, `教師モデル`, `マルチモーダル`, `セグメンテーション`, `ポストトレーニング`, `ハルシネーション`, `デプロイ` preserved.

Use the reader-surface gate/fidelity tooling. Machine PASS does not substitute for the later Sol PDF review.

## 7. Bibliography / provenance

Materialize bibliography only from already-bound source authority.

Require:

- every citation key used by publication source exists in bibliography;
- no unused publication-only invented citation;
- no citation silently changes source role;
- bibliography identity/source provenance remains traceable to accepted Evidence;
- unresolved/partial provenance remains represented as a limitation rather than invented certainty.

Do not browse or research to fill bibliography gaps. If a required source binding is genuinely absent, STOP and report.

## 8. PDF build and deterministic checks

Build the exact publication PDF using the canonical special-longform path.

Require:

- non-encrypted PDF;
- page count recorded;
- PDF SHA-256 recorded;
- committed repository PDF bytes correspond exactly to the reviewed build artifact;
- no undefined citations/references;
- no missing glyph failures;
- no blocking overfull/underfull/layout failure according to the canonical gate;
- no clipped text, broken tables/boxes, unreadable source notes, or malformed headings;
- no page padding.

Architecture target is approximately 112 pages with maximum 120. Treat 120 as a hard stop for this edition. Do not shrink content by substantive deletion or pad content to reach 112.

If page count exceeds 120, stop for Sol with the cause; do not silently remove technical content.

## 9. Exact-PDF visual review

Perform a machine/operator visual review of the exact committed PDF.

Inspect every page.

Record:

- page count;
- clipping/overflow;
- missing glyphs;
- broken tables;
- line collisions;
- bad page breaks;
- headings stranded from content;
- bibliography/source-note readability;
- excessive blank pages/space;
- any figure/table artifact if present.

Formatting-only repairs may be made and rebuilt.

Any repair that would change accepted Draft r6 meaning requires STOP for Sol.

The visual review generated here is worker/operator evidence only. It is not Human Publication Preview approval and not Sol's independent PDF review.

## 10. Stage validation boundary

After all reader/publication artifacts and the exact PDF are stable, run canonical `DRAFT_COMPLETE -> VALIDATED_DRAFT` stage-contract validation against the final candidate bytes.

Require:

`CORE_STAGE_CONTRACT = PASS`

Record the validation output under the r6 publication-validation execution directory or another edition-local execution path. If Core convention keeps the validation file outside the canonical publication authority, record its exact hash/path in the session report.

Do NOT execute `advance-stage`.

Production State must remain byte-identical and lifecycle must remain `DRAFT_COMPLETE`.

This is intentionally a candidate for Sol review, not a state transition.

## 11. Required execution report

Create:

`sources/SP-vision-multimodal-2026/execution/reader-publication-validation-r1-20261002/reader-publication-validation-report.md`

Report at least:

- startup guards;
- accepted Draft r6 authority;
- Frozen Core identity;
- exact changed-path inventory;
- reader fidelity checks;
- terminology-map final scan;
- bibliography/citation binding;
- reader-surface gate status;
- semantic/editorial review status;
- deterministic quality checks;
- PDF build method;
- exact PDF path/blob/SHA-256/byte count/page count;
- visual review summary for every page/range;
- layout-check result;
- stage-contract validation result;
- production-state before/after hash proving no state mutation;
- main/Core unchanged;
- final HEAD/tree after normal non-force push.

## 12. Stop boundary

Do NOT:

- execute `advance-stage`;
- move lifecycle to `VALIDATED_DRAFT`;
- build/approve Human Publication Preview;
- infer Human approval;
- Freeze;
- Release.

Normal terminal:

`TS-003 READER_PUBLICATION_VALIDATION_CANDIDATE_COMPLETE`

`TS-003 EXACT_PDF_READY_FOR_SOL_REVIEW`

`CORE_STAGE_CONTRACT_PASS_DRAFT_COMPLETE_TO_VALIDATED_DRAFT`

`PRODUCTION_STATE_UNCHANGED_DRAFT_COMPLETE`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

STOP there.
