# TS-003 execution instruction — Draft r1 reader-surface repair to Draft r2

Status: `EXECUTION_AUTHORITY / SOL_DRAFT_R1_REQUEST_CHANGES / DRAFT_R2_READER_SURFACE_REPAIR_ONLY`

Date: `2026-10-01 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Authority

Sol Draft Review r1:

`sources/SP-vision-multimodal-2026/execution/sol-draft-review-r1.md`

Sol review decision:

`REQUEST_CHANGES`

Reviewed Draft r1 authority commit:

`d1053e957d92cddd9d2759ec9713db59c66263ad`

Reviewed Draft r1 tree:

`d69fe46574d0d922e8a1e2c4c4a69e2719f4ddae`

Human Architecture Review r2 remains APPROVED.

This is not a new Human gate and does not reopen Architecture.

## 2. Start guards

Do not hard-code the work-branch launch SHA/tree in this committed file.

The Sol launch message supplies the sole exact work-branch start SHA/tree.

Before any write, read-only verify:

- remote work branch HEAD/tree == launch-message expected HEAD/tree;
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- issue == `SP-vision-multimodal-2026`;
- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- Draft checkpoint == passed;
- validation/publication_preview/freeze/release checkpoints == pending;
- current Architecture SHA-256 == `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- current Selection SHA-256 == `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`.

If any guard differs, perform zero writes and report expected vs actual.

No new branch, fallback branch, repair branch, review branch, reset, rebase, cherry-pick, squash, force push or history rewrite is authorized.

## 3. Mandatory read order

Read at minimum:

1. `sources/SP-vision-multimodal-2026/execution/sol-draft-review-r1.md`
2. `sources/SP-vision-multimodal-2026/execution/drafting-language-policy-ja.md`
3. `sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`
4. `sources/SP-vision-multimodal-2026/execution/draft-r1-20261001/draft-r1-review-report.md`
5. all 16 current Draft r1 Results
6. current profile synthesis result
7. approved Architecture r2
8. unchanged Draft Packages
9. frozen Core v2 Draft schema/prompt/validation CLI

Do not interpret Worker language-QA `PASS_WITH_NOTES` as Sol approval.

## 4. Mission

Produce Draft r2 by revising reader-facing prose only.

Upstream research and approved editorial structure are immutable.

Do not rerun:

- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture.

Do not add sources or facts from memory/web.

Keep all 16 Draft Package files byte-identical.

Revise all 16 Draft Results because the r1 prose defect is systemic, even where a package appears relatively clean.

Regenerate profile synthesis only as needed to remain consistent with revised Draft Results.

Use `draft_version=r2` and `status=REVISED` if that is the schema-valid Core mechanism. If the current schema requires another canonical revision representation, use that mechanism and document it. Do not invent schema fields.

## 5. Core principle — semantic depth, not character filling

Architecture page budgets are not character quotas.

The r1 statement that package output was held within a character tolerance must not be used as a drafting objective in r2.

A shorter result is acceptable when repetition is removed.

Never add:

- paraphrased restatements;
- rhetorical closings;
- slogan-like sentences;
- repeated boundary reminders;
- duplicate conclusions

merely to approximate a page count.

If the prose becomes materially shorter after deduplication, leave it shorter unless there is a distinct Evidence-supported mechanism, transition, limitation or comparison that should genuinely be explained.

Report any resulting page/depth risk to Sol instead of padding.

## 6. Full-volume prose rewrite requirements

Rewrite all reader-facing paragraphs using normal Japanese technical prose.

Prefer established terms and straightforward syntax.

Examples of preferred replacements when context supports them:

- neural network / CNN → `ニューラルネットワーク` / `CNN`, not recurrent `網`;
- training recipe → `学習レシピ` / `レシピ`, not recurrent `処方`;
- evidence/support → `根拠` / `裏付け`, not recurrent `証し`;
- methodology/constraint → `方法` / `制約` / `前提`, not `躾`;
- architecture/design → `アーキテクチャ` / `設計`, not generic `構え`;
- carry forward / preserve → `引き継ぐ` / `維持する`, not generic metaphorical `運ぶ`;
- evidentiary category → say the category explicitly, not `棚`;
- responsibility/purpose → state the purpose directly, not repeated `仕事` / `務め`.

Do not ban ordinary Japanese uses of these words mechanically. The requirement is to eliminate systematic metaphor substitution where technical terminology is clearer.

Avoid literary phrases such as `凱歌`, `束ねの妙` and similar rhetorical decoration unless there is a compelling reader-facing reason. In normal technical exposition there usually is not.

## 7. Sentence-level density rule

Every substantive sentence should perform at least one identifiable function:

- state a source-supported fact;
- explain a mechanism;
- explain why a transition matters;
- compare compatible alternatives;
- state a limitation;
- establish attribution/source role;
- synthesize across packages.

Delete sentences that merely restate the previous sentence in new words.

Before terminalization, run an exact-sentence duplicate scan over headline/deck/PARAGRAPH/BULLET/TABLE reader-facing text.

Acceptance target:

- zero exact duplicate sentence within each package, excluding literal quotations/fixed labels where repetition is unavoidable;
- P15 must have zero exact duplicated prose sentence;
- any cross-package repeated sentence must be reviewed to confirm it is genuinely necessary rather than templated filler.

Include the scan result in the r2 review report.

## 8. Paragraph structure

Do not produce long blocks followed by dozens of aphoristic one-clause restatements.

Each paragraph should have a coherent technical arc.

For FULL_MECHANISM treatment, normally cover:

1. predecessor bottleneck;
2. representation/interface/mechanism change;
3. how it works;
4. what operation it enables;
5. limitation/trade-off;
6. successor relation where supported.

Do not satisfy these six functions by repeating the same conclusion six ways.

TRANSITION_NODE treatment must explain the transition but may be concise.

BRIEF_CONTEXT_OR_AUTHORITY should remain brief.

## 9. P01 specific repair

Rewrite P01 from scratch at the prose level while retaining its bound Evidence and approved coverage.

Eliminate recurrent:

- `網`;
- `処方`;
- `壁` metaphors;
- `運ぶ`;
- `凱歌`;
- `束ねの妙`.

Use technically direct phrasing for AlexNet and ResNet.

Be especially careful not to turn editorial interpretation into unsupported fact. Keep scaling-recipe interpretation explicitly framed as synthesis where required.

## 10. P07B / P09 / P15

### P07B

Retain its mechanism-grouped structure and D07B lineage depth.

Remove repetitive bridge sentences and repeated reminders that do not add a technical distinction.

Do not revert to one-paper-one-paragraph catalogue form.

### P09

Retain the three organizing questions: resolution, fusion depth, time/audio.

Same-source/same-protocol head-to-head values may remain only when they materially support the approved technical comparison and evaluator/source attribution is explicit.

Do not author a cross-task leaderboard.

Reduce benchmark numbers that do not change the technical argument.

### P15

P15 requires the strongest rewrite.

It must remain synthesis-led across D15 + X01-X04, but the r1 rhetorical repetition must be removed.

Do not use repeated `躾`, `構え`, `証し`, `棚`, `務め`, `仕事` as connective tissue.

Organize the section around distinct evaluation contracts and source-strength questions.

The convergence conclusion may remain open, but state that conclusion once, support it, and stop. Do not repeat the same “we cannot conclude yet” proposition in multiple formulations.

## 11. Source-role repair

Audit every sentence that uses generic `著者`, `作り手`, `独立`, `ベンダー`, `公式` around evaluation claims.

P15 r1 sentence:

`著者の手で測った分だけが、独立の証しになる。`

must not survive.

Use explicit evaluator class, as supported by Evidence:

- model vendor;
- model paper authors;
- benchmark paper authors evaluating third-party models;
- independent third-party reproduction.

An author-reported result is not automatically independent.

If the Evidence does not support independence, do not imply it.

## 12. CLAIM_BOUNDARY reader surface

Do not dump raw Architecture boundary strings into reader-facing text.

For every Architecture boundary:

- keep the exact boundary string in structured `boundary_dispositions.boundary`;
- choose `RESPECTED_BY_OMISSION` when the correct reader-facing behavior is simply to avoid an unsupported claim;
- choose `EXPLICITLY_STATED` only when the limitation materially helps the reader;
- when explicit, write the visible block in concise natural Japanese rather than copying English/internal wording.

Do not expose internal identifiers such as G01-G06, PARTIAL, candidate IDs, stage names or Core workflow jargon in ordinary prose.

If frozen Core validation structurally requires raw English boundary strings in visible block text, stop fail-closed and report the tooling limitation. Do not alter approved Architecture to work around it without Sol authorization.

## 13. Terminology map revision

Update the edition-local terminology map only if needed for the r2 prose repair.

The map itself is editorial guidance; do not use its preferred terms mechanically if normal Japanese is clearer in a specific sentence.

Add explicit anti-metaphor guidance for the r1 failure modes:

- 網;
- 処方;
- 証し;
- 躾;
- 構え;
- 運ぶ;
- 棚;
- rhetorical 仕事/務め.

Keep the Human requirement against excessive kanji translation.

The repair goal is neither “more English” nor “more Japanese”; it is precise, natural technical Japanese.

## 14. Language QA r2

Create:

`sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r2.md`

Audit the full 16-package reader surface plus synthesis.

At minimum report:

- exact sentence duplicate counts by package;
- count/spot review for r1 failure lexicon;
- literal translation artifacts;
- excessive kanji translation;
- invented terms;
- over-nominalization;
- source-role ambiguity;
- internal jargon leakage;
- raw English boundary leakage;
- terminology consistency;
- P07B/P09/P15 qualitative review.

Do not self-grade `PASS` solely from regex counts. Include manual full-text review.

A `PASS_WITH_NOTES` is acceptable only if notes are genuinely non-blocking and none of F1-F5 from Sol Draft Review r1 remains materially present.

## 15. Technical and Evidence integrity

Preserve all Evidence references required by the Draft Packages.

Do not weaken attribution.

Do not silently delete a fact merely because its Japanese is difficult; rewrite it naturally.

If a current r1 sentence is not supportable from its bound Evidence, remove or correct it within the existing Evidence boundary and record the repair.

If correction would require new Evidence/research, do not research; flag it for Sol.

G01-G06 and five PARTIAL limitations remain semantically present where relevant, but internal labels need not be reader-facing.

## 16. Validation and lifecycle

Run schema/runner validation for every revised Draft Result and revised synthesis.

Run the canonical deterministic Draft validation available at current `DRAFT_COMPLETE` state without manually changing lifecycle.

Do not call reader-publication validation.

Do not create Publication Preview.

Do not record any Human Publication Preview decision.

Do not freeze or release.

If Core only supports Draft validation as part of `ARCHITECTURE_ESTABLISHED -> DRAFT_COMPLETE` and cannot validate an r2 revision while already at `DRAFT_COMPLETE`, do not fake a rollback. Run all non-mutating validators available, document the limitation, and stop for Sol.

## 17. Required r2 review report

Create:

`sources/SP-vision-multimodal-2026/execution/draft-r2-20261001/draft-r2-review-report.md`

Report at least:

- startup guard results;
- reviewed r1 commit/tree;
- r1 Sol review authority;
- unchanged Draft Package hashes;
- all 16 r2 Draft Result hashes;
- synthesis hashes;
- exact duplicate-sentence scan;
- r1 failure-lexicon counts before/after;
- source-role repair summary;
- CLAIM_BOUNDARY disposition summary;
- G01-G06 / PARTIAL preservation;
- P07B/P09/P15 review;
- language-QA r2 path/hash/status;
- deterministic validation results;
- actual lifecycle/next_action;
- Publication Preview pending;
- main/Core unchanged;
- final HEAD/tree.

## 18. Terminal condition

Normal terminal labels:

`TS-003 DRAFT_R2_READER_SURFACE_REPAIR_COMPLETE`

`TS-003 LANGUAGE_QA_R2_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW_R2`

`NO_READER_PUBLICATION_VALIDATION`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

STOP there.
