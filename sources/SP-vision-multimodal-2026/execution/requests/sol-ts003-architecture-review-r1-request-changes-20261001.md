# TS-003 execution instruction — Human Architecture Review r1 REQUEST_CHANGES, bounded Architecture r2 regeneration

Status: `EXECUTION_AUTHORITY / HUMAN_ARCHITECTURE_REVIEW_R1_REQUEST_CHANGES / BOUNDED_TO_SELECTION_COMPLETE`

Date: `2026-10-01 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Human decision authority

Human Architecture Review r1 decision:

`REQUEST_CHANGES`

Reviewed Architecture production authority:

`11616337817917df2da04daea2341202da376303`

Reviewed Architecture tree:

`ef716103320347854740418d556cc71dd1e4a557`

Sol advisory review:

`sources/SP-vision-multimodal-2026/execution/sol-architecture-review-r1.md`

Sol advisory commit:

`1c9a7b75725fd9234f26fd21f247836eae6bd296`

Regeneration boundary:

`SELECTION_COMPLETE`

This is one bounded pre-Draft Architecture correction. The Human is not requesting new Discovery, Screening, Evidence, Materiality, Completeness, or Selection work.

The current Selection is accepted as the immutable upstream basis for Architecture r2. Do not reinterpret this Human `REQUEST_CHANGES` decision as permission to change candidate dispositions or rerun research.

## 2. Start guard authority

Do not hardcode the work-branch start SHA/tree in this file.

The exact work-branch HEAD/tree supplied in the Sol launch message are the sole start guard for the work branch.

Before any write, read-only verify:

- remote work branch HEAD/tree == launch-message Exact Starting SHA/tree;
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- issue == `SP-vision-multimodal-2026`;
- lifecycle == `ARCHITECTURE_ESTABLISHED`;
- `next_action == ARCHITECTURE_REVIEW`;
- `terminal_reason == HUMAN_GATE_REACHED`;
- Human Architecture Review is still pending before this decision is canonically recorded;
- Draft remains pending;
- Publication Preview remains pending;
- Selection checkpoint is passed;
- Architecture checkpoint is passed;
- `candidate-selection-v2.json` is the reviewed r1 Selection authority, with 111 SELECTED and the same PRIMARY/SUPPORTING role assignments.

If any guard differs, perform zero writes, report expected vs actual, and STOP.

No new branch, fallback branch, repair branch, review branch, reset, rebase, cherry-pick, force push, squash, or history rewrite is authorized.

## 3. Mandatory read order

After the guard passes, read at minimum:

1. `sources/SP-vision-multimodal-2026/execution/sol-architecture-review-r1.md`
2. `sources/SP-vision-multimodal-2026/execution/selection-architecture-20261001/architecture-review-dossier-r1.md`
3. this execution request
4. `sources/SP-vision-multimodal-2026/candidate-selection-v2.json`
5. `sources/SP-vision-multimodal-2026/architecture-v2.json`
6. `sources/SP-vision-multimodal-2026/architecture-review-summary-v2.json`
7. `sources/SP-vision-multimodal-2026/architecture-review-attention-v2.json`
8. `sources/SP-vision-multimodal-2026/execution/sol-materiality-completeness-review-r1.md`
9. `sources/SP-vision-multimodal-2026/execution/sol-evidence-semantic-review-r5.md`
10. Round E planning authority: `docs/research-plans/2026-09-30_ts-003-sol-round-e-scope-closure.md` from planning branch `planning/ts-003-vision-multimodal-preresearch-20260930`
11. current canonical Core CLI/help/schema for recording Human Architecture Review `REQUEST_CHANGES` and regenerating Architecture from `SELECTION_COMPLETE`.

Do not treat deterministic `READY_FOR_ARCHITECTURE_REVIEW` as a Human approval.

## 4. What is accepted and must be preserved

The Human `REQUEST_CHANGES` decision does not reject the overall structure.

Preserve:

- the five-Part reader architecture;
- the 16 Architecture packages P01–P15 including separate P07A/P07B;
- the current package order;
- the current 111-candidate Selection and PRIMARY/SUPPORTING role assignments;
- D04 four-node cap: MiDaS / OpenPose / Visual Genome / DUSt3R;
- D07A image-level alignment vs D07B grounding separation;
- TS-001 generic efficiency and TS-002 generic generation boundaries;
- P12–P14 as bounded convergence endpoints;
- World Model four-pole split and non-ancestry guard;
- G01–G06 and the five PARTIAL records as explicit limitations;
- vendor/model-report attribution boundaries;
- prohibition on cross-task/cross-protocol numeric ranking;
- current Evidence r5, Materiality and Completeness authority.

The requested changes concern Architecture depth control, synthesis binding, reader title, and page allocation only.

## 5. Required Change A — restore Part V to the accepted weight

Round E established the planning weight contract:

- Parts I–III: `65–72%`;
- Part IV / D12–D14: `13–18%`;
- Part V / D15 + X01–X04 synthesis: `15–20%`.

Architecture r1 allocated 96 body pages as 68 / 16 / 12, making Part V only 12.5%.

Architecture r2 must restore Part V to the accepted 15–20% range.

Preferred page plan for r2:

- front matter: 4 pages;
- Parts I–III / P01–P11: 72 pages;
- Part IV / P12–P14: 16 pages;
- Part V / P15: 16 pages;
- back matter: 4 pages;
- target total: 112 pages;
- maximum remains 120 pages.

This produces a 104-page body with approximately:

- Parts I–III: 69.2%;
- Part IV: 15.4%;
- Part V: 15.4%.

The exact total may vary modestly if the canonical schema treats the page plan differently, but the accepted percentage ranges and 120-page maximum are mandatory.

Do not restore Part V by compressing load-bearing lineages merely to keep the old 104-page total.

## 6. Required Change B — make P15's synthesis authority explicit

P15 `Measurement, limits and convergence` currently has only OCRBench v2 as an explicit PRIMARY candidate and no SUPPORTING candidates, while its thesis depends on D15 plus X01–X04 and cross-package evidence.

Architecture r2 must explicitly bind P15 to a representative synthesis authority set drawn only from already-selected candidates.

At minimum, P15's Architecture-level authority must make the following synthesis dependencies explicit:

- document/chart/OCR evaluation from P05;
- hallucination / visual-evidence-use / reasoning diagnostics from P10;
- long-video / streaming evaluation from P11;
- GUI / Computer Use evaluation from P12;
- VLA evidence limitation / independent-evaluation scarcity from P13;
- World Model evaluation/terminology limitation from P14;
- current-system vendor-vs-independent claim-strength discipline from P09;
- X01 supervision/data progression across earlier packages;
- X02 objective/interface progression across class/box/mask/text/region/coordinate/action/latent-state contracts;
- X03 visual token/context/memory/latency economics using TS-001 vocabulary without retelling TS-001;
- X04 source-role / reliability / claim-strength boundaries including G01–G06.

Use existing selected candidates only. No new research or candidate creation is authorized.

If the canonical Architecture schema permits the same selected candidate to support more than one package, add representative existing candidates to P15 as SUPPORTING synthesis authorities.

If duplicate package binding is schema-invalid, do not alter Selection. Instead create a schema-valid Architecture-level cross-reference/synthesis map using existing extension fields or an additive edition-local Architecture artifact, and bind that map explicitly from the r2 Human dossier.

Do not turn P15 into a benchmark catalogue. Distinct evaluation contracts are the organizing principle; bare score aggregation is prohibited.

## 7. Required Change C — package-level page/depth budget

Architecture r2 must add a package-level depth plan sufficient to prevent thin source-catalogue drafting.

Preferred starting page budget:

| Package | Pages |
|---|---:|
| P01 | 4 |
| P02 | 6 |
| P03 | 5 |
| P04 | 4 |
| P05 | 7 |
| P06 | 5 |
| P07A | 4 |
| P07B | 11 |
| P08 | 6 |
| P09 | 10 |
| P10 | 4 |
| P11 | 6 |
| P12 | 5 |
| P13 | 6 |
| P14 | 5 |
| P15 | 16 |

This is 104 body pages, matching the preferred 112-page total with 4-page front/back matter.

The Architecture must also distinguish at least three drafting-depth classes:

1. `FULL_MECHANISM_TREATMENT`
   - load-bearing transition or mechanism;
   - enough space to explain prior bottleneck, representation/interface change, mechanism, consequence, limitation, inheritance.

2. `TRANSITION_NODE_TREATMENT`
   - technically distinct lineage/bridge node;
   - concise but substantive comparison against predecessor/successor.

3. `BRIEF_CONTEXT_OR_AUTHORITY`
   - predecessor, benchmark, deployment, source-role, or limitation evidence;
   - cited where needed without forcing an equal-depth mini-section.

PRIMARY does not mechanically mean equal page allocation. SUPPORTING does not mean disposable.

P07B and P09 in particular must remain deep enough that their high source density does not collapse into one-paragraph-per-paper catalogue writing.

Do not solve density by merging P07A/P07B, removing D07B minimum lineage, collapsing omni/audio/video distinctions, or weakening P13/P14 branch distinctions.

## 8. Required Change D — reader-facing subtitle decision

Architecture r1 left the subtitle unresolved even though Round E deferred it specifically to Architecture Review.

The r2 reader-facing title is now:

`Vision & Multimodal AI — 視覚表現から接地・推論・行動へ`

This replaces the older backlog direction:

`Vision & Multimodal AI — 検知・認識からVLM・World Modelへ`

The old wording remains rejected because it implies an overly linear predetermined endpoint.

Do not rename the stable machine identity, issue ID, slug, branch, source root, or survey root.

If the current canonical Architecture schema has no reader-title field, record the title in a schema-valid publication extension or additive r2 Architecture dossier as the Human-requested reader-facing title to be inherited by Draft. Do not mutate immutable production-profile identity merely to carry this subtitle.

## 9. Upstream immutability

Do not rerun or substantively change:

- Discovery;
- Screening;
- Evidence r1–r5;
- active r5 Evidence/Views;
- Materiality;
- Completeness;
- Candidate Matrix;
- Candidate Selection;
- the 111 SELECTED decisions;
- PRIMARY/SUPPORTING role assignments;
- source bytes;
- `main`;
- `production/survey-core-v2`.

The Selection authority must remain byte-identical unless the current canonical Human-gate machinery requires provenance metadata outside the substantive Selection artifact.

If the four requested Architecture corrections cannot be made without changing Selection, stop fail-closed and report why. Do not silently reopen Selection.

## 10. Canonical Human decision recording

Record Human Architecture Review r1 through the current canonical Human-gate mechanism.

The decision must state:

- gate: `ARCHITECTURE_REVIEW`;
- reviewed revision: `r1`;
- decision: `REQUEST_CHANGES`;
- reviewed Architecture production authority: `11616337817917df2da04daea2341202da376303`;
- reviewed Architecture SHA-256: `7e112f84db8d56d23099a46825eebb50c8289219e11e38e042b58bf1e4df4201`;
- Sol advisory: `sources/SP-vision-multimodal-2026/execution/sol-architecture-review-r1.md`;
- regeneration boundary: `SELECTION_COMPLETE`;
- requested changes: A–D in this contract.

Use actual execution-time provenance/date through the canonical mechanism. Do not fabricate an earlier Human-review timestamp.

Do not mark Architecture r1 approved.

Preserve r1 and its dossier as immutable review history.

## 11. Architecture r2 regeneration

After recording r1 `REQUEST_CHANGES`, invalidate/regenerate only from `SELECTION_COMPLETE` using current canonical Core tooling.

Regenerate as required by the Core:

- `architecture-v2.json`;
- `architecture-review-summary-v2.json`;
- `architecture-review-attention-v2.json`;
- Architecture-stage validation/review artifacts;
- Architecture checkpoint/state transition;
- a fresh `architecture-review-dossier-r2.md` or current equivalent;
- additive package-depth/cross-synthesis artifact if required because the canonical schema lacks a native field.

Architecture r2 must remain `PROPOSED`, not Human-approved.

Machine validation may return `READY_FOR_ARCHITECTURE_REVIEW`; that is readiness only.

Stop again at a fresh Human Architecture Review.

## 12. r2 acceptance checks

Before committing, verify all of the following:

- Human r1 `REQUEST_CHANGES` is recorded canonically;
- regeneration boundary was exactly `SELECTION_COMPLETE`;
- Selection is unchanged and still 111 SELECTED with the same role assignments;
- 16 packages P01–P15 remain present;
- five-Part structure remains intact;
- P04 remains exactly the four-node hard-cap substrate;
- P07A/P07B remain separate;
- Part IV remains 13–18% of body;
- Part V is restored to 15–20% of body;
- target length is depth-supporting and <=120 pages;
- P15 has explicit cross-package synthesis authority for D15 + X01–X04;
- package-level page/depth budgets exist;
- P07B/P09 have sufficient explicit depth budget;
- reader-facing title is `Vision & Multimodal AI — 視覚表現から接地・推論・行動へ`;
- G01–G06 remain unresolved/bounded as before;
- no new research was run;
- Draft remains pending;
- Publication Preview remains pending;
- main unchanged;
- Production Core unchanged.

## 13. Final report

Report at least:

- startup guard results;
- Human r1 decision record path/revision/boundary;
- invalidation/regeneration path used;
- Selection byte/hash identity before/after;
- Architecture r1 hash and r2 hash;
- r2 page plan and Part percentages;
- per-package page/depth budget;
- P15 cross-synthesis authority map;
- subtitle disposition;
- validator/checkpoint results;
- final lifecycle;
- Human Architecture Review r2 status;
- final remote HEAD/tree;
- main unchanged;
- Core unchanged;
- no Draft.

Normal commit + non-force push only.

Normal terminal state:

`TS-003 HUMAN_ARCHITECTURE_REVIEW_R1_REQUEST_CHANGES_RECORDED`

`TS-003 ARCHITECTURE_R2_REGENERATED`

`ARCHITECTURE_ESTABLISHED`

`AWAITING_HUMAN_ARCHITECTURE_REVIEW_R2`

`NO_DRAFT`

`NO_HUMAN_R2_DECISION`
