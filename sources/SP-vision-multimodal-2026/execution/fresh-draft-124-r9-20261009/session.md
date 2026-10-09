# Session — TS-003 Fresh Draft from Approved Architecture r9 / Evidence 124 (fresh-124-r9)

Run: `execution/fresh-draft-124-r9-20261009`. Human APPROVED r9 authority only; no Architecture/Evidence reopen; no Source Intake; no TeX/PDF/Preview/Freeze/Release; no shared-Core change; no new branch/fallback/force-push.

## Starting authority (read-only)

- Branch `special/vision-multimodal-2026-work`
- Remote HEAD `fbba4458412dd3fd3368af8231a7c846e963e4f2` — MATCH
- Remote Tree `e0bcc4f5d8a5c2ba3c52ee1f088de9307c391f2c` — MATCH
- Local HEAD `fbba4458412dd3fd3368af8231a7c846e963e4f2` — MATCH
- Local Tree `e0bcc4f5d8a5c2ba3c52ee1f088de9307c391f2c` — MATCH
- Working tree clean (porcelain empty; one pre-existing stash left untouched).
- Lifecycle `ARCHITECTURE_ESTABLISHED`, arch approved, draft pending, next `stage:drafting-synthesis`.
- Approved arch SHA `cd37a969fe4d49b54517cb5253bb283931d5bf9e5eb795315b74c0e40339a1af`, approval `385b390f5c0faae026f5447dafff737a3c635e6d973a3bd5ca2425753d35af02`.
- Discovery 125, Evidence 124 (119/5), Selection 124, Completeness 14/2, 16 pkgs, 40-map (40 unique/50 refs), page 112/120, draft pending.

## Required reads (all verified)

1. Production State, r9 approval/review/index — verified above.
2. Approved `architecture-v2.json` (cd37…, PROPOSED status preserved; approval via Human Gate).
3. Review summary/attention (READY_FOR_ARCHITECTURE_REVIEW basis; 124/124/125/14-2).
4. Candidate selection/matrix (124 SELECTED, 124 rows, SHAs 8075/c631).
5. Canonical Evidence acceptance `6b55033d…` (124 results) + 124 cards (VM-D011/D123-125 attribution closure verified at card level).
6. Cross-package synthesis authority (40 unique IDs via `publication_extensions.p15_cross_package_synthesis_map`).
7. `execution/drafting-language-policy-ja.md` (binding).
8. `execution/drafting-terminology-map-ja.md` (cumulative R9 binding; Pass A/B/C protocol).
9. `execution/r9-p12-cost-framing-20261008/deferred-fresh-draft-requirements.md` (all items consumed).
10. r9 P02 attribution closure records (D011 +1 lineage claim; D123 native; D124/D125 claim-3 removed).
11. Prior generation/validation precedent (rev5 scripts + validators referenced; rev5 prose used only as regression/negative reference; 0 blocks copied).

## Fresh generation (no bulk copy)

- Re-derived all 16 `draft-package.json` via `survey_drafting_v2.derive_draft_package` under `current_stage_basis_override` (stage-basis drift guard precedent). New basis: arch cd37, summary 1500, approval 385b, matrix 8075, selection c631, evidence 326e. P02 11 inputs (8 primary +3 supporting incl. D123/D124/D125); P15 14 inputs.
- Authored 16 packages anew (headline/deck/blocks/boundaries) via 4 parallel authoring passes with per-package binding rationale (inputs → prose → downstream state). Spec `compact-input-fresh-124-r9.json` (`fresh-124-r9`, 51,123 block chars; P01 7, P02 12, P03 8, P04 7, P05 10, P06 9, P07A 6, P07B 15, P08 8, P09 11, P10 7, P11 10, P12 8, P13 8, P14 7, P15 13). Zero blocks identical to `fresh-121-r8-rev5` (asserted).
- Built generation-time overlay `cross-package-map-fresh-124-r9.json` (33 entries: P06 1, P07A 1, P07B 2, P10 2, P11 1, P15 26; unique 30 incl. P15 40-map coverage; all rebound to r9 SHAs; SELECTED + byte binding verified; no placement change). P04/P05 need no overlay in fresh prose (all canonical).
- Regenerated via `regenerate_fresh_r9.py` (canonical `runner._draft_result` for 10; union-ref `_xresult` for 6; boundaries_text post-hoc override validation-neutral): 16/16 (10 canonical PASS + 6 overlay PASS; frozen generic P15 errors 111 documented as known Core limitation, edition-local overlay is established form). Synthesis input rebuilt overlay-aware; synthesis result (fresh profile_payload: branch/parallel/unresolved/attribution) validated.
- Naming: `fresh-124-r9` (unique vs `fresh-121-r8-rev5`; Core has no contrary naming contract; reason recorded here).

## Depth/volume

- Body 104 pages (P01-P11 72, P12-P14 16, P15 16) + front/back 4+4 =112 target (max 120). No PDF; density checked per-package (chars/page 339-749; P15 339 with 13 blocks/40 IDs; surgical dedup only, no padding, no mechanism deletion).
- FULL_MECHANISM 6 aspects covered within evidence bounds; TRANSITION bridges explicit; BRIEF capped.

## Mandatory corrections (all applied, audit-verified)

- P02: Deformable (reference-point sparse attention, multi-scale, 10x epochs, small-object), DAB (dynamic anchor queries, layer updates, positional priors, brief), DN (query denoising vs bipartite instability, NOT diffusion), DINO convergence (DN-improved + DAB-anchors + deformable-attention + own refinements), parallel/convergent (not single-hop), VM-D011-only predecessor basis (no retroattribution). Arch unchanged.
- P15: four roles explicit (1 self, 2 vendor, 3 benchmark-third-party, 4 independent repro; OpenVLA=1, Video-MME/Gemini=3; bare author-reported ≠ independent); 40-map consumed; X01-X04 integrated; no mini-catalogue.
- P04: DUSt3R downstream as `Survey/editorial synthesis` (`比較判断`), no direct causal lineage; 4-node cap held.
- P12/P15: tool-call only as horizon/state proxy (318.4 Opus 4.7 max-thinking single-action + 481.8 Opus 4.8 500-step + GPT-5.5 ~13% all model+thinking+tool+steps+release bound); no token/context/KV/latency/compute direct reading; 1.0 grounding vs 2.0 state-management distinct.
- P08: Molmo/PixMo scoped to paper academic set + large human eval; code/weights/data/license separated; no general superiority.
- P01: ResNet only controlled backbone-swap comparison; no strong general causal.
- P14: no Ha2018→Dreamer/Genie direct ancestry; 4-pole held; conceptual vs source-supported inheritance separated.
- Video: P09 mechanism/token/vendor, P10 diagnostic, P11 stored-timeline vs offline/online; surgical dedup only; SAM3 vs VM-D112 not collapsed.
- P07A/B: alignment (アライメント) vs grounding (グラウンディング/語句グラウンディング/GUI要素のグラウンディング) separated; metrics/I-O/milestones distinct. P07A repaired to 9× アライメント (rev5 had 0; fresh fixes defect).

## Japanese QA (binding map; no parallel map)

- Bad forms 0: 除去検証/思考の連鎖/頁面/一級の要素/ablation変形/完全オープン変形/文用言語モデル/使い回せる基盤 absent; correct アブレーション/CoT/ページ上/明示的な構成要素/アブレーション条件/バリアント/完全オープン版/バリアント/テキストLLM/再利用可能な基盤表現 present naturally (no blind replace).
- Pass A (preferred-form + bidirectional + first-use), Pass B (§3 registry), Pass C (residual + synthesis) via `audit_fresh_r9.py` 58/58 PASS (incl. P07A アライメント repair). No Sino-calque excess, no drift, no production leakage, no depth reduction.

## Validation

- `regen-report.json`: 16 regenerated, 10 canonical +6 overlay PASS, frozen P15 111 (documented Core limitation).
- `audit-fresh-124-r9.json`: 58/58 PASS (S structural 17, T technical 20, J Japanese 13 incl. banned 8, R regression 8 incl. 0-identical + no-Core).
- Canonical `validate_draft_result` 10/10; edition-local `validate_overlay_result` 6/6 (cause/target explicit; unconfirmed errors never PASS; no records fabricated).
- `validate_agent_state` CLEAN pre/post; checkpoint `ARCHITECTURE_ESTABLISHED.json` built; `draft-stage-validation-fresh-124-r9.json` + reviews recorded (34 artifacts).

## Advancement (checkpoint mechanism only)

- `ARCHITECTURE_ESTABLISHED → DRAFT_COMPLETE` via `advance_draft_r9.py` (`build_stage_checkpoint` + `advance_with_checkpoint`). Arch Gate stays `approved`; draft `passed` with fresh provenance; next `stage:reader-publication-validation` (NOT started). Validation pending, Preview/Freeze/Release untouched.

## Scope/stop boundary (held)

- Allowed only: fresh input/result, synthesis, edition-local QA, checkpoint validation, DRAFT_COMPLETE advance, logs/audit, normal commit/non-force push/read-back.
- No arch/evidence/intake/reader-validation/TeX/PDF/Preview/Freeze/Release. Shared roots untouched (git status: only `sources/SP-vision-multimodal-2026/draft/v2/*`, `production-state.json`, `orchestration/.../ARCHITECTURE_ESTABLISHED.json`, `execution/fresh-draft-124-r9-20261009/`).

## Terminal

`FRESH_124_R9_DRAFT_COMPLETE` / `MANDATORY_DRAFT_CORRECTIONS_APPLIED` / `APPROVED_ARCHITECTURE_PRESERVED` / `INDEPENDENT_CONTENT_REVIEW_PENDING`. STOP.
