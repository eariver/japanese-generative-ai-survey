# TS-003 Vision & Multimodal — Human Architecture Review dossier (r2)

Status: `ARCHITECTURE_DOSSIER_R2 / HUMAN_REVIEW_SURFACE / NO_HUMAN_DECISION`

Date: `2026-10-01`

Issue: `SP-vision-multimodal-2026` — branch `special/vision-multimodal-2026-work`

Lifecycle: `ARCHITECTURE_ESTABLISHED` — selection `passed`, architecture `passed`,
Human Architecture Review `pending` (r2), draft `pending`, Publication Preview `pending`.

This dossier proposes Architecture r2. It records no Human decision.

## 1. Review identity

- Edition: TS-003 Vision & Multimodal (THEMATIC / LONGFORM_SPECIAL).
- Revision: Architecture r2 (regeneration from `SELECTION_COMPLETE` after Human r1 `REQUEST_CHANGES`).
- r1 review record: `gates/reviews/architecture-r1.json` (r1, `REQUEST_CHANGES`,
  reviewed commit `11616337817917df2da04daea2341202da376303`, boundary `SELECTION_COMPLETE`).
- r1 bytes preserved: commit `116163378…` + `execution/architecture-r1/` (architecture `7e112f84…`,
  summary `8b3cb666…`, attention `c5a19177…`, selection `378b818e…`) + dossier r1.
- r2 canonical artifacts (working tree at dossier time):
  - `candidate-matrix-v2.json` sha256 `1cb6f3a8b86f7e21f510a144baf8c3897f1661dca19739e292ee5cfe91c3a35a` (unchanged)
  - `candidate-selection-v2.json` sha256 `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef` (byte-identical)
  - `architecture-v2.json` sha256 `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38` (fresh r2)
  - `architecture-review-summary-v2.json` sha256 `151770365ec5b9facbbd8e2bcdfe3964f5201eb2dd9eaf2d4904a4dc0c1115da` (fresh r2)
  - `architecture-review-attention-v2.json` sha256 `c5a1917788b6da842997b076f46d220c541dba4a1ca4d09a68f7cd0d1d4ca07d` (identical: screening/ledger/selection inputs unchanged)
- Supervisory authority: Sol Architecture Review r1 (`execution/sol-architecture-review-r1.md`,
  advisory `REQUEST_CHANGES`, findings A/B blocking, C drafting-risk, D due-now).
- Execution authority: `execution/requests/sol-ts003-architecture-review-r1-request-changes-20261001.md`.
- Machine readiness: `READY_FOR_ARCHITECTURE_REVIEW` (deterministic only; not a recommendation).

## 2. What changed r1 → r2 (exactly the four requested changes; nothing else)

- **A. Page plan**: 104 (4/68/16/12/4) → **112 target / 120 max** (front 4, Parts I–III 72,
  Part IV 16, Part V 16, back 4). Body 104: I–III ≈69.2% (contract 65–72),
  IV ≈15.4% (13–18), V ≈15.4% (15–20). No lineage thinned to hold the old total.
- **B. P15 synthesis authority**: was PRIMARY-only (OCRBench v2). Now 1 PRIMARY + **13 reused
  SUPPORTING** synthesis authorities + architecture-level `p15_cross_package_synthesis_map`
  extension (P05/P09/P10/P11/P12/P13/P14 threads + X01–X04 anchors, all already-selected IDs).
  No new candidates, no new research, no catalogue, no ranking.
- **C. Package page/depth budgets**: every package carries `page_budget_body_pages`
  (4/6/5/4/7/5/4/11/6/10/4/6/5/6/5/16 = 104) and per-candidate depth classes
  (`FULL_MECHANISM_TREATMENT` / `TRANSITION_NODE_TREATMENT` / `BRIEF_CONTEXT_OR_AUTHORITY`).
  P07B 11pp, P09 10pp — mechanism/transition-grouped, not one-paragraph-per-paper.
- **D. Reader title**: `Vision & Multimodal AI — 視覚表現から接地・推論・行動へ`
  bound as `reader_title_human_requested_r2` in architecture `publication_extensions`
  (Human-requested, inherited by Draft). Backlog subtitle
  `検知・認識からVLM・World Modelへ` stays rejected. Machine identity untouched.

## 3. Preserved from r1 (acceptance checklist)

- Five-Part structure; 16 packages P01–P15 incl. P07A/P07B split; package order unchanged.
- Selection byte-identical: 111 SELECTED (72 PRIMARY / 39 SUPPORTING), same roles/placement.
- D04 four-node cap (MiDaS/OpenPose/VisualGenome/DUSt3R); P12–P14 bounded endpoints (~15.4%).
- Dreamer / JEPA-V-JEPA / Genie four-pole split + non-ancestry guard.
- G01–G06 unresolved/bounded; five PARTIAL records carried with barriers.
- Vendor/source-role discipline; no cross-task ranking; TS-001/TS-002 boundaries.
- Editorial thesis unchanged (problem-layer organization, representation-sufficiency question,
  convergence as open question in Part V).

## 4. P15 cross-synthesis authority map (r2)

Direct SUPPORTING reuse in P15 (publication role changes to synthesis evidence, not new transitions):
P05 VM-D108/VM-D109 (DocVQA/ChartQA); P10 VM-D078/VM-D079/VM-D081 (MMMU/POPE/MMBench);
P11 VM-D086/VM-D087 (Video-MME/LongVideoBench); P09 VM-D072/VM-D073 (Gemini-3.x vendor-vs-independent poles);
P13 VM-D099/VM-D100 (card-scoped limitation); P14 VM-D106/VM-D107 (Genie-3 limitation).
Extension map (already-selected IDs): P12 GUI eval VM-D090/D091/D092 (PRIMARY home stays P12);
X01 VM-D003/D035/D051/D062/D096; X02 VM-D010/D047/D092/D097/D104;
X03 VM-D059/D065/D089/D091/D100; X04 VM-D056/D080/D098/D099/D100/D110.
Bound in `architecture-v2.json` `publication_extensions.p15_cross_package_synthesis_map`
+ P15 `must_cover_requirements`; full table in dossier §2 source input
`execution/architecture-r2-20261001/interactive-architecture-r2.json`.

## 5. Research coverage / evidence quality (unchanged from r1)

Discovery 111 records; Screening 103/3/5/0; Evidence r5 106 VERIFIED / 5 PARTIAL;
Materiality 101/10; Completeness LIMITED (O06-G06, O14-G01, O15-G02).
No research rerun; upstream bytes untouched.

## 6. Risks for Human inspection (r2)

1. P15 at 16 pages with 14 bound authorities must stay synthesis-led, not catalogue-led — Draft contract carries the methodology-first rule.
2. Depth budgets are Architecture-level controls; Draft may still need Sol enforcement for P07B/P09 density.
3. r2 attention bytes equal r1 (correct: inputs unchanged) — not a regeneration defect.
4. Convergence verdict remains an open evidence-backed question for Draft, not a decided unity narrative.
5. Waymo driving pointer still pending a primary source (flagged, non-blocking).

## 7. Human decision options

After reviewing this dossier and the bound r2 artifacts, the Human may choose:

- `APPROVED`
- `REQUEST_CHANGES` (with requested changes and one allowed pre-Architecture regeneration boundary)

Silence is not a decision. Work has stopped at this Gate: `NO_DRAFT`, `NO_HUMAN_R2_DECISION`.
