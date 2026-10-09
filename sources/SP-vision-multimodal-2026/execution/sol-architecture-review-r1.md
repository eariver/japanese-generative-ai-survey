# TS-003 Vision & Multimodal AI — Sol Architecture Review r1

Status: `SOL_ARCHITECTURE_REVIEW_R1 / ADVISORY_REQUEST_CHANGES / NO_HUMAN_DECISION`

Date: `2026-10-01 JST`

Repository: `eariver/japanese-generative-ai-survey`

Edition: `SP-vision-multimodal-2026`

Reviewed branch: `special/vision-multimodal-2026-work`

Reviewed HEAD: `11616337817917df2da04daea2341202da376303`

Reviewed tree: `ef716103320347854740418d556cc71dd1e4a557`

Reviewed main: `d6381568cc897a47d6de992189e20339350342b7`

Reviewed main tree: `83ce3a216d852a1c32d0138f9c56fadefa800666`

Reviewed Production Core: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Reviewed Core tree: `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

Human Architecture Review remains `pending`. This file is a Sol supervisory recommendation only and records no Human decision.

## 1. What passes

The Architecture has substantial strengths and preserves the central pre-production design:

- it rejects a single famous-model chronology and instead uses interacting technical problem layers;
- D04 remains exactly the four-node support substrate (MiDaS / OpenPose / Visual Genome / DUSt3R);
- D07A image-level alignment and D07B grounding remain separate packages with separate metric contracts;
- TS-001 generic efficiency and TS-002 generic generation remain cross-reference territory rather than being retold;
- P12–P14 remain bounded modern endpoints rather than the historical spine;
- Dreamer / JEPA-V-JEPA / Genie remain distinct predictive/world-model poles with the non-ancestry guard intact;
- G01–G06 and the five PARTIAL records remain explicit;
- current closed/vendor systems are capability/deployment comparators, not silently promoted to architecture authority;
- machine Selection and Architecture validation passed and Production State correctly stopped at `ARCHITECTURE_ESTABLISHED / HUMAN_GATE_REACHED` with Draft still pending.

These are strong foundations and should be retained in any revision.

## 2. Finding A — Part V weight drift from Round E (`BLOCKING`)

Round E explicitly defined the planning weight/depth contract:

- Parts I–III: 65–72%;
- Part IV / D12–D14: 13–18%;
- Part V / evaluation+synthesis: 15–20%.

The proposed Architecture allocates the 96 body pages as:

- Parts I–III: 68 pages = 70.8%;
- Part IV: 16 pages = 16.7%;
- Part V: 12 pages = 12.5%.

Parts I–IV therefore satisfy the accepted ranges, but Part V does not. The discrepancy is not merely cosmetic because Part V is where D15 plus X01–X04 are supposed to synthesize supervision/data history, interface contracts, efficiency/context economics, reliability/source fidelity, evaluation-contract limits and the unified-vs-modular convergence question.

Required correction before Draft:

- restore Part V to the accepted 15–20% planning range, or
- provide an explicit evidence-based Architecture Review justification for revising the Round E weight contract.

Given the user preference for semantic depth over arbitrary page economy, increasing the body/page target within the already-authorized 80–120 page envelope is preferable to compressing Parts I–IV merely to hit the old 104-page target.

## 3. Finding B — P15 synthesis is under-bound (`BLOCKING`)

P15 is titled `Measurement, limits and convergence` and is assigned responsibility for:

- D15 methodology-first synthesis;
- X01 supervision/data timeline;
- X02 interface/objective synthesis;
- X03 efficiency/token/memory/latency synthesis;
- X04 reliability/source-fidelity synthesis;
- the final convergence verdict.

However the canonical Architecture binds only one explicit PRIMARY candidate to P15: OCRBench v2, with no SUPPORTING candidates.

That is insufficiently explicit for a 12+ page cross-volume synthesis. The intended content clearly depends on authorities currently housed in P05/P09/P10/P11/P12/P13/P14 and earlier historical packages. Leaving those relations implicit creates two risks during Draft:

1. P15 becomes a thin OCRBench-centered methodology chapter despite its much broader thesis; or
2. Drafting pulls cross-package evidence opportunistically without an Architecture-level binding, weakening provenance and making convergence claims harder to audit.

Required correction before Draft:

- bind P15 explicitly to a representative cross-package synthesis set, reusing already-selected candidates where appropriate;
- include distinct evaluation/failure authorities (for example document/chart, hallucination/evidence-use, GUI/computer-use, long-video/streaming, spatial reasoning, VLA/world-model limitation evidence) without turning P15 into a benchmark catalogue;
- include explicit X01–X04 synthesis anchors and identify which prior-package evidence each synthesis thread consumes;
- preserve all existing no-ranking/vendor-attribution rules.

Candidate reuse across packages is acceptable where the publication role changes from local mechanism evidence to synthesis evidence; it should not be counted as a new technical transition.

## 4. Finding C — no per-package depth budget for high-density packages (`DRAFTING_RISK`)

Selection keeps all 111 accepted candidates: 72 PRIMARY and 39 SUPPORTING. This is not automatically a defect because SUPPORTING includes context, evaluation and deployment authorities. The risk appears at package density:

- P07B: 14 PRIMARY + 2 SUPPORTING;
- P09: 7 PRIMARY + 7 SUPPORTING;
- P05: 6 PRIMARY + 3 SUPPORTING;
- P13: 6 PRIMARY + 2 SUPPORTING;
- P14: 5 PRIMARY + 2 SUPPORTING.

The Architecture gives only Part-level page allocations, not package-level depth budgets. That makes the anti-thinness rule difficult to enforce deterministically during Draft.

Required correction or explicit drafting contract:

- add a package-level page/depth plan, at least for the high-density packages;
- distinguish `full mechanism treatment`, `transition-node treatment`, and `brief lineage/context citation` so PRIMARY does not mechanically imply equal paragraphs/pages;
- allow total length to rise within the 120-page maximum if required by evidence density;
- do not solve density by collapsing D07B, D09 or the VLA/world-model branch distinctions already accepted.

This finding is subordinate to Findings A/B: it can be resolved in the same Architecture regeneration rather than by changing Selection.

## 5. Title remains unresolved at the Architecture gate (`NON_BLOCKING_BUT_DUE_NOW`)

Round E explicitly deferred the final subtitle to Architecture Review and rejected the backlog wording `検知・認識からVLM・World Modelへ` as too linear.

The current Architecture/dossier uses only `TS-003 Vision & Multimodal` / `Vision & Multimodal AI` and does not freeze the reader-facing subtitle.

The Architecture Review should therefore choose or explicitly defer with a reason among directions such as:

- `Vision & Multimodal AI — 視覚表現から接地・推論・行動へ`
- `Vision & Multimodal AI — 世界を読むAIの技術史`

A title that makes World Model the predetermined endpoint should remain rejected unless the revised Architecture changes materially.

## 6. Selection assessment

`SELECTED 111/111` is acceptable only under the current role split:

- PRIMARY = 72
- SUPPORTING = 39

No Selection rollback is required at this time. The ten CONTEXT records are mapped to bounded SUPPORTING roles rather than being promoted as equal-depth historical nodes. The issue is therefore Architecture depth control, not the mere selection count.

If the Architecture revision cannot produce credible package-level depth within the 120-page maximum, Selection may then need a bounded secondary pass. That is not currently required.

## 7. Sol recommendation to Human

Recommendation: **REQUEST_CHANGES**, limited to one bounded pre-Draft Architecture regeneration.

The revision should preserve the existing Selection/Evidence authority and change only what is necessary to:

1. restore or formally re-justify the Round E Part V 15–20% weight;
2. explicitly bind P15 to the cross-package evidence needed for D15 + X01–X04 synthesis;
3. add package-level page/depth controls sufficient to prevent thin source-catalogue drafting;
4. present the final subtitle decision (or an explicit justified deferral) at the renewed Human Architecture Review.

No new research is required for these findings. Discovery, Screening, Evidence, Materiality and Completeness should remain unchanged unless the Architecture revision itself uncovers a genuinely blocking evidence gap.

Do not enter Draft before a fresh Human Architecture Review decision.

Terminal advisory state:

`SOL_ARCHITECTURE_REVIEW_R1_COMPLETE`

`RECOMMEND_HUMAN_REQUEST_CHANGES`

`NO_HUMAN_DECISION`

`NO_DRAFT`
