# TS-003 execution instruction — Draft r2 to Draft r3 under cumulative terminology authority

Status: `EXECUTION_AUTHORITY / SOL_DRAFT_R2_REQUEST_CHANGES / CUMULATIVE_TERMINOLOGY_MAP_R3_REPAIR_ONLY`

Date: `2026-10-02 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

Supersedes the earlier unexecuted request:

`sources/SP-vision-multimodal-2026/execution/requests/sol-ts003-draft-r2-terminology-reader-surface-repair-20261002.md`

Use this file, not the superseded request, for the next Muse execution.

## 1. Authorities

Sol Draft Review r2:

`sources/SP-vision-multimodal-2026/execution/sol-draft-review-r2.md`

Decision:

`REQUEST_CHANGES`

Reviewed Draft r2 authority commit:

`4a553c33385cb245d7239c116812999560165188`

Reviewed Draft r2 tree:

`f1f6fdf5582d30d03a280aea00e872dcf026a30f`

### Binding cumulative terminology authority

Path:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

Authority commit:

`ebe9c5f7f41b1f0ffa278ec60a6f238ef676eaf1`

Authority tree:

`e4c00a619355c6f20c85f1b084de33808cb24640`

Expected map blob SHA:

`37bfd73c838bde51a170572989e73166df5dfb51`

Expected map terminal state:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R3_BINDING`

This cumulative map is authoritative for terminology, known-failure regression prevention, and terminology QA. If this request conflicts with the map on terminology handling, the cumulative map wins.

Human Architecture r2 remains APPROVED.

This is not a new Human gate and does not reopen Architecture.

## 2. Start guards

The Sol launch message supplies the sole exact work-branch starting HEAD/tree.

Before any write, read-only verify:

- remote work branch HEAD/tree == launch-message expected HEAD/tree;
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- cumulative terminology map blob SHA == `37bfd73c838bde51a170572989e73166df5dfb51`;
- cumulative terminology map status == `DRAFT_R3_BINDING`;
- issue == `SP-vision-multimodal-2026`;
- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- draft checkpoint == passed;
- validation/publication_preview/freeze/release == pending;
- current Architecture SHA-256 == `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- current Selection SHA-256 == `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`.

If any guard differs, perform zero writes and report expected vs actual.

No new branch, fallback branch, repair branch, review branch, reset, rebase, cherry-pick, squash, force push or history rewrite is authorized.

## 3. Mandatory read order

Read in this order before editing:

1. this execution request;
2. `sources/SP-vision-multimodal-2026/execution/sol-draft-review-r2.md`;
3. `sources/SP-vision-multimodal-2026/execution/drafting-language-policy-ja.md`;
4. `sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`;
5. `sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r2.md`;
6. `sources/SP-vision-multimodal-2026/execution/draft-r2-20261001/draft-r2-review-report.md`;
7. all 16 canonical Draft r2 Results;
8. current profile synthesis;
9. approved Architecture r2;
10. unchanged Draft Packages;
11. frozen Core Draft schema/prompt/non-mutating validators.

The r2 Worker claims `F1-F5_CLOSED` and `PASS_WITH_NOTES` are not Sol approval and must not be used to skip repair.

## 4. Mission

Produce Draft r3 by applying the cumulative terminology authority to the entire reader surface and repairing every known or newly discovered terminology/over-domestication regression.

This is a Draft-only editorial repair.

Do not rerun or modify:

- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture;
- Human Architecture approval.

Do not add new research, sources, facts from memory, or web-derived facts.

Keep all 16 Draft Package files byte-identical.

Preserve Draft r1 and r2 as immutable Git history.

## 5. The cumulative map is the repair specification

Do not maintain a separate ad hoc bad-word list.

Apply Sections 1–7 of the cumulative terminology map as the authoritative repair and QA specification.

In particular:

- preserve load-bearing distinctions;
- use preferred technical forms;
- remove all `TECHNICAL_SUBSTITUTION_BLOCKING` uses from the known-failure registry;
- do not blindly replace ordinary Japanese uses;
- do not replace one bad expression with a new invented synonym;
- when a newly discovered terminology failure appears during r3 review, first add it to the cumulative map, then repair the prose, then rerun the terminology audit.

The cumulative update rule is mandatory.

## 6. Mandatory semantic terminology audit

Run the exact three-pass audit required by the cumulative map.

### Pass A — preferred/avoid conformance

Inspect every terminology row in the map across:

- headline;
- deck;
- PARAGRAPH;
- BULLET;
- TABLE;
- CLAIM_BOUNDARY;
- profile synthesis / reader-facing synthesis.

Do not omit CLAIM_BOUNDARY from the scan.

### Pass B — known-failure regression scan

Inspect every entry in the cumulative known-failure registry.

For every hit, classify it as exactly one of:

- `TECHNICAL_SUBSTITUTION_BLOCKING`;
- `ORDINARY_JAPANESE_ALLOWED`;
- `SOURCE_QUOTE_OR_FIXED_NAME`;
- `NOT_APPLICABLE`.

All `TECHNICAL_SUBSTITUTION_BLOCKING` hits must be repaired.

Any intentionally retained Avoid-form must be quoted with its sentence and classification in the QA report.

### Pass C — manual semantic full-text review

Read all 16 package reader surfaces, synthesis, and CLAIM_BOUNDARY blocks.

Look for new equivalents not already listed in the map:

- invented translations;
- over-domestication;
- school/human-role personification for model components;
- everyday-object metaphors replacing technical terms;
- literary connective tissue replacing mechanism/metric/source-role language;
- code/encoding ambiguity;
- segmentation euphemisms;
- multimodal euphemisms;
- evaluation/benchmark/metric conflation.

If a new failure is found:

1. update the cumulative terminology map in the same execution;
2. record the new entry and rationale;
3. repair all occurrences;
4. rerun Pass A/B/C;
5. report the map's new blob SHA in the final review report.

Do not silently fix a new failure without adding it to the cumulative map.

## 7. Preserve r2 improvements

Do not undo the following r2 gains:

- `網` removed as a neural-network substitute;
- zero exact duplicate sentences;
- removal of r1 padding;
- natural Japanese CLAIM_BOUNDARY blocks instead of raw Architecture strings;
- explicit source/evaluator roles;
- P07B mechanism grouping;
- P09 protocol-bound comparisons rather than cross-task ranking;
- P15's reduced repetition and higher information density.

Do not re-pad prose to restore r1 character count.

If removal of bad wording exposes genuine technical thinness, deepen only from already-bound Evidence and approved Architecture coverage. If that is insufficient, report the shortage rather than inventing prose or researching.

## 8. Evidence and structure integrity

Preserve all required Evidence references and must-cover content.

Do not weaken attribution.

Preserve boundary dispositions unless reader-facing wording alone is being repaired.

Preserve G01–G06 and all five PARTIAL limitations semantically without exposing internal labels unnecessarily.

Do not change Architecture to make wording easier.

If a correction would require new Evidence, do not research; flag it for Sol.

No cross-task authored ranking.

## 9. Draft r3 language QA

Create:

`sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r3.md`

The report must contain at least:

- terminology-map authority path/blob SHA/status;
- exact duplicate sentence count by package;
- full preferred/avoid terminology conformance table;
- full known-failure registry audit;
- every retained Avoid-form with exact sentence + semantic classification;
- teacher/student terminology audit;
- neural-network `網` audit;
- multimodal terminology audit;
- post-training terminology audit;
- hallucination terminology audit;
- segmentation-specific `切り分け/塗り分け` audit;
- source/software-code `符号` audit separated from legitimate encoding uses;
- residual metaphor audit;
- CLAIM_BOUNDARY audit;
- internal production-jargon audit;
- P07B/P09/P15 manual qualitative review;
- newly discovered terminology failures, if any, and the corresponding cumulative-map update.

Regex zero counts alone are not sufficient for PASS.

A `PASS_WITH_NOTES` is acceptable only when all notes are genuinely non-blocking and every known technical-substitution failure has been dispositioned.

## 10. Deterministic validation

Run canonical non-mutating schema/runner validation available for all revised Draft Results and synthesis while lifecycle remains `DRAFT_COMPLETE`.

Do not fake a rollback.

Do not call reader-publication validation.

If the frozen Core cannot perform a particular Draft-stage validation at `DRAFT_COMPLETE`, document the limitation exactly as in r2 and stop at the Sol-review boundary.

## 11. Required Draft r3 review report

Create:

`sources/SP-vision-multimodal-2026/execution/draft-r3-20261002/draft-r3-review-report.md`

Report at least:

- startup guards;
- reviewed r2 commit/tree;
- Sol Draft Review r2 authority;
- cumulative terminology map starting path/blob/status;
- whether the map changed during r3 and, if so, its final blob/hash;
- unchanged Draft Package hashes;
- all revised Draft Result hashes;
- synthesis hashes;
- exact duplicate scan;
- terminology-map conformance result;
- known-failure regression result;
- any newly discovered failure and map update;
- source-role preservation;
- CLAIM_BOUNDARY status;
- G01–G06 / PARTIAL preservation;
- P07B/P09/P15 review;
- language-QA r3 path/hash/status;
- deterministic validation results;
- actual lifecycle/next_action;
- Publication Preview pending;
- main/Core unchanged;
- final HEAD/tree.

## 12. Lifecycle boundary

Current `DRAFT_COMPLETE` remains valid.

Do not:

- call reader-publication validation;
- create Publication Preview;
- record Human Publication Preview decision;
- Freeze;
- Release.

## 13. Terminal condition

Normal terminal labels:

`TS-003 DRAFT_R3_CUMULATIVE_TERMINOLOGY_REPAIR_COMPLETE`

`TS-003 LANGUAGE_QA_R3_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW_R3`

`NO_READER_PUBLICATION_VALIDATION`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

STOP there.
