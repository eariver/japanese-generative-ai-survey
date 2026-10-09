# TS-003 execution instruction — Human Architecture Review r2 APPROVED, Draft r1 through Sol Draft Review

Status: `EXECUTION_AUTHORITY / HUMAN_ARCHITECTURE_REVIEW_R2_APPROVED / DRAFT_R1_ONLY / STOP_FOR_SOL_REVIEW`

Date: `2026-10-01 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Human decision authority

Human Architecture Review r2 decision:

`APPROVED`

The Human explicitly approved Architecture r2 after receiving the Sol r2 review and Human review summary.

Reviewed Architecture r2 production authority commit:

`61443a929c42de0c6669a3f5fbe4ac4dd5b2c55e`

Reviewed Architecture r2 tree:

`7d79584a1a32a5ccfe14a326983a58da40c4fa10`

Reviewed Architecture SHA-256:

`d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`

Reviewed Architecture Review summary SHA-256:

`151770365ec5b9facbbd8e2bcdfe3964f5201eb2dd9eaf2d4904a4dc0c1115da`

Reviewed Architecture Review attention SHA-256:

`c5a1917788b6da842997b076f46d220c541dba4a1ca4d09a68f7cd0d1d4ca07d`

Reviewed Selection SHA-256:

`378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`

Sol supervisory review:

`sources/SP-vision-multimodal-2026/execution/sol-architecture-review-r2.md`

Sol recommendation: `APPROVE`.

The earlier Human Architecture Review r1 `REQUEST_CHANGES` record remains immutable history and must not be overwritten.

## 2. Additional Human drafting instruction

At approval, the Human added a mandatory Drafting requirement:

> 現状のCore v2では拾えない問題、特に過度な漢語訳に気をつける。

This is a binding edition-local requirement.

Read and apply:

`sources/SP-vision-multimodal-2026/execution/drafting-language-policy-ja.md`

A Core validator PASS does not constitute a Japanese-language-quality PASS.

The Human instruction is not optional editorial advice. It is part of this execution contract.

## 3. Start guard authority

Do not hardcode the work-branch start SHA/tree in this committed execution file.

The exact work-branch HEAD/tree supplied by the Sol launch message are the sole work-branch start guard.

Before any write, read-only verify:

- remote work branch HEAD/tree == launch-message Exact Starting SHA/tree;
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- issue == `SP-vision-multimodal-2026`;
- lifecycle == `ARCHITECTURE_ESTABLISHED`;
- current Human Architecture Review r2 is still pending before the approval is canonically recorded;
- Draft is pending;
- Publication Preview is pending;
- Architecture checkpoint is passed;
- current `architecture-v2.json` SHA-256 == `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- current `candidate-selection-v2.json` SHA-256 == `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`;
- current Selection remains 111 SELECTED / 72 PRIMARY / 39 SUPPORTING.

If any guard differs, perform zero writes and report expected vs actual.

No new branch, fallback/repair/review branch, reset, rebase, cherry-pick, force push, squash, or history rewrite is authorized.

## 4. Mandatory read order

After guards pass, read at minimum:

1. `sources/SP-vision-multimodal-2026/execution/sol-architecture-review-r2.md`
2. `sources/SP-vision-multimodal-2026/execution/architecture-r2-20261001/architecture-review-dossier-r2.md`
3. `sources/SP-vision-multimodal-2026/architecture-v2.json`
4. `sources/SP-vision-multimodal-2026/architecture-review-summary-v2.json`
5. `sources/SP-vision-multimodal-2026/architecture-review-attention-v2.json`
6. `sources/SP-vision-multimodal-2026/candidate-selection-v2.json`
7. active Evidence r5 / Edition Views authority and their coverage reports
8. `sources/SP-vision-multimodal-2026/execution/drafting-language-policy-ja.md`
9. this execution request
10. frozen Core v2 Draft schema/prompt/CLI and current Human-gate mechanism
11. the older frozen editorial drafting prompt `config/prompts/editorial/article-drafting-v0.1.md` only for its reader-prose principle that technical English may remain where precision improves and translation for translation's sake should be avoided; it does not replace the active Core v2 schema/prompt.

## 5. Canonical Human r2 approval recording

Use the current frozen Core canonical Human-gate mechanism to record:

- gate: `ARCHITECTURE_REVIEW`;
- revision: r2 / current next revision after r1;
- decision: `APPROVED`;
- reviewed repository commit: `61443a929c42de0c6669a3f5fbe4ac4dd5b2c55e`;
- reviewed Architecture SHA-256: `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- reviewed summary SHA-256: `151770365ec5b9facbbd8e2bcdfe3964f5201eb2dd9eaf2d4904a4dc0c1115da`;
- reviewed attention SHA-256: `c5a1917788b6da842997b076f46d220c541dba4a1ca4d09a68f7cd0d1d4ca07d`;
- reviewed_by: Human Owner;
- review reference: Human explicit approval in the supervising Sol chat after reviewing the r2 decision material;
- actual execution-time timestamp only.

Do not fabricate an earlier approval timestamp.

Preserve r1 `REQUEST_CHANGES` review history.

If the current Core gate mechanism cannot record this approval without changing the reviewed Architecture/Selection bytes, fail closed and report the limitation.

## 6. Draft mission

After canonical Human Architecture r2 approval is successfully recorded, build Draft r1 from the approved r2 Architecture.

This execution is authorized for Drafting only.

Do not perform new Discovery, Screening, Evidence, Materiality, Completeness, Selection, or Architecture work.

Do not add new sources or use outside remembered/web facts to fill gaps.

If Drafting exposes a genuinely blocking unsupported fact, preserve the unknown and flag it for Sol. Do not silently research around the approved Evidence boundary.

## 7. Binding reader identity and length

Reader-facing title:

`Vision & Multimodal AI — 視覚表現から接地・推論・行動へ`

Do not restore the rejected subtitle `検知・認識からVLM・World Modelへ`.

Architecture r2 page contract remains binding:

- target total: 112 pages;
- maximum: 120 pages;
- front matter: 4;
- body: 104;
- back matter: 4;
- Parts I–III: 72 body pages (~69.2%);
- Part IV: 16 (~15.4%);
- Part V: 16 (~15.4%).

Package body budgets:

- P01 4
- P02 6
- P03 5
- P04 4
- P05 7
- P06 5
- P07A 4
- P07B 11
- P08 6
- P09 10
- P10 4
- P11 6
- P12 5
- P13 6
- P14 5
- P15 16

Do not hit the page target by flattening technical depth.

## 8. Architecture depth classes are binding

Respect every package's r2 depth assignment:

- `FULL_MECHANISM_TREATMENT`
- `TRANSITION_NODE_TREATMENT`
- `BRIEF_CONTEXT_OR_AUTHORITY`

`FULL_MECHANISM_TREATMENT` must explain, where supported:

- predecessor bottleneck;
- representation/interface change;
- mechanism;
- newly enabled operation;
- limitation/trade-off;
- successor/inheritance relation.

`TRANSITION_NODE_TREATMENT` must be substantive enough to explain why the node changes the lineage; it is not merely a citation sentence.

`BRIEF_CONTEXT_OR_AUTHORITY` may remain concise and should not be inflated into an equal-depth mini-section.

P07B and P09 require special anti-catalogue enforcement. Do not write one-paper-one-paragraph release-note sequences.

## 9. P15 drafting contract

P15 must remain synthesis-led.

Use its explicit direct SUPPORTING authorities and `publication_extensions.p15_cross_package_synthesis_map` to synthesize:

- document/chart/OCR evaluation;
- multimodal reasoning/hallucination/evidence use;
- long-video vs streaming evaluation;
- GUI/Computer Use evaluation;
- VLA independent-evaluation scarcity;
- World Model evaluation/terminology limits;
- vendor-vs-independent claim-strength;
- X01 data/supervision/post-training progression;
- X02 interface/output-contract progression;
- X03 token/context/memory/latency economics;
- X04 reliability/provenance/claim strength.

Do not turn P15 into fourteen benchmark summaries.

Do not aggregate incompatible scores or create a cross-task ranking.

Convergence remains an Evidence-backed open question, not a predetermined unified-model conclusion.

## 10. Known limitations remain visible

Preserve G01–G06 as unresolved/bounded limitations unless already resolved in the approved Evidence authority. Do not repair them by prose inference:

- G01 independent/non-vendor VLA evaluation scarcity;
- G02 transferable control-oriented World Model benchmark absent;
- G03 same-protocol document specialist/generalist comparison absent;
- G04 real-deployment latency/VRAM evidence gap;
- G05 independent reproduction of current vendor/model-report claims lacking;
- G06 SigLIP2 exact citation binding limitation.

Preserve all five PARTIAL Evidence records and their barriers.

Vendor/project/author claims remain attributed. Product/demo pages do not become architecture authority.

## 11. Mandatory Japanese-language preflight

Before producing the full reader-facing Draft, create:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

Follow `drafting-language-policy-ja.md`.

At minimum establish preferred handling for load-bearing terms such as:

- alignment;
- grounding;
- detection;
- recognition;
- segmentation;
- multimodal;
- VLM;
- open-vocabulary;
- reasoning;
- streaming;
- Computer Use;
- Vision-Language-Action / VLA;
- World Model;
- predictive representation;
- benchmark;
- evaluation;
- deployment;
- architecture;
- capability;
- evidence/provenance where reader-facing.

The correct disposition may be established Japanese, katakana, or English. Do not force a kanji translation.

## 12. Mandatory Japanese-language QA after Drafting

After Draft r1 is materialized, conduct a full reader-facing Japanese-language QA and create:

`sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r1.md`

Audit at least:

- excessive kanji/Sino-Japanese translation;
- invented/nonstandard translations;
- literal-translation artifacts;
- noun stacking / over-nominalization;
- meaning drift between English source terminology and Japanese prose;
- inconsistent terminology across packages;
- repeated/unnecessary English parenthetical glosses;
- machine-translated-sounding syntax;
- production/internal jargon leakage;
- semantic distinctions blurred by translation.

This is an edition-local manual gate independent of Core validation.

If the QA finds obvious prose-only defects that can be corrected without changing factual meaning, Evidence refs, package coverage, or Architecture boundaries, correct them within this execution and rerun the QA.

If a correction would alter factual meaning, Evidence classification, source binding, or Architecture coverage, do not self-repair semantically. Record it as a Sol-review finding and stop.

Final language-QA status may be `PASS` or `PASS_WITH_NOTES`; a material language defect must be `REQUEST_SOL_REVIEW` rather than falsely passing.

## 13. Core Draft validation

Use the current frozen Core v2 Draft Package / Draft Result / validation machinery exactly as implemented.

Do not invent lifecycle-state names or manually edit `production-state.json`.

Run the canonical deterministic checks required for the Draft artifacts that are authorized at this stage.

If the current Core couples successful Draft construction to a canonical lifecycle transition, use that canonical transition. However:

- do not record any Human Publication Preview decision;
- do not freeze or release;
- do not infer Publication approval;
- do not perform a later-stage action merely because Draft validation passes.

The operational stopping point for this execution is a **fresh Sol Draft Review**.

If reaching a Publication Preview gate is an unavoidable mechanical consequence of canonical Draft validation, reaching the gate is allowed, but no Human decision or release action is allowed. Report the exact canonical state and stop for Sol.

## 14. Required Draft review package

Before stopping, produce an edition-local Draft r1 review report containing at least:

- Human r2 approval record path/hash;
- approved Architecture r2 hash;
- active Evidence r5/Views bindings;
- Draft Package/result counts and hashes;
- package-by-package page/depth realization;
- actual handling of P07B/P09/P15;
- must-cover/boundary coverage status;
- G01–G06 disposition;
- PARTIAL record disposition;
- source-role/vendor attribution checks;
- terminology-map path/hash;
- language-QA path/hash and status;
- examples/counts of language corrections made, if any;
- deterministic Core validation results;
- final canonical lifecycle/next_action/terminal_reason;
- Publication Preview decision status;
- main/Core unchanged checks;
- final work-branch HEAD/tree.

The report must distinguish deterministic validator PASS from Sol/Human editorial approval.

## 15. Prohibited actions

Do not:

- change Selection or Architecture;
- rerun research stages;
- add evidence from memory or web;
- weaken an Evidence limitation to make prose smoother;
- over-translate technical terms into invented kanji compounds;
- treat vendor claims as independent facts;
- create cross-task benchmark rankings;
- change main;
- change frozen Production Core;
- create new branches;
- force push/rewrite history;
- freeze/release;
- create or infer a Human Publication Preview approval.

## 16. Terminal condition

Normal terminal labels for this execution:

`TS-003 HUMAN_ARCHITECTURE_REVIEW_R2_APPROVED`

`TS-003 DRAFT_R1_BUILT`

`TS-003 JAPANESE_LANGUAGE_QA_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

Use the actual frozen-Core canonical lifecycle/state names in the repository report rather than inventing a lifecycle value from these operational labels.

STOP there.
