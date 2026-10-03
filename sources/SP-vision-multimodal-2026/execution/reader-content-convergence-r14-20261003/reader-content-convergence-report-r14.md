# TS-003 r14 Content Convergence and Evidence Alignment — Execution Report

- Date: 2026-10-03 JST
- Authority: `EXECUTION_AUTHORITY / R13_INDEPENDENT_REVIEW_REQUEST_CHANGES / CONTENT_CONVERGENCE / EVIDENCE_ALIGNMENT / STOP_BEFORE_TEX`
- Branch (existing only): `special/vision-multimodal-2026-work`
- Start guard: remote HEAD `afc0a184984262e58135225ee4e39402ab3cc211` + tree `3256b3d3b16c206f5bfbff0b5042f1a54a97ca6a` MATCH, clean tree, no new branch.
- Terminal: `FRESH_CONTENT_REVIEW_REQUIRED` (READER_JSON_ONLY, no TeX/PDF)
- r13: 139 blocks / 68,059 chars → r14: 139 blocks / 68,059 chars class (net small; convergence, not expansion)

## 1. Review findings addressed (§5–§16)

- **P09 stale-LIMIT contradictions (§6.1/6.2): RESOLVED.** p09-b9/b10/b11/b12 rewritten as pointer-established + per-axis LIMIT: confirmed axes (2×2→1 merger, DeepStack layer map, 448→256, V2PE δ, K-crops, connector layers, S0-S3/30k/36k recipes in b13–b16) stated as established by pointer; still-unconfirmed axes (measured KV-cache reduction, deployment memory, end-to-end latency improvement, undocumented internals) kept explicit. Old blanket-unknown sentences deleted. No contradiction within authority.
- **P09 license/openness (§6.3): RESOLVED with artifact matrix.** Official current sources re-verified read-only 2026-10-03 (repo LICENSE files, official HF org model pages; HF Qwen3-VL-8B-Instruct page confirms `License: apache-2.0`; no third-party blogs): Qwen3-VL code Apache-2.0 + weights Apache-2.0 (named artifacts only, date-bound in prose); Molmo2 model Apache-2.0 + code Apache-2.0 + Ai2 first-party/open data at collection scope + third-party academic/non-commercial limits fenced to training sources (never generalized to model license; Apache-2.0 never generalized to corpus). #559 Qwen3-Omni Apache-2.0 named scope untouched (p09-b6 byte-identical).
- **Agentic Video (§7/§8): GOVERNED_PIPELINE_REENTRY_REQUIRED — HUMAN_GATE_NOT_BYPASSED.** Governance determination (read-only): adding a NEW Discovery candidate post-Architecture-approval (Human `approved`) requires Discovery supplement → Screening → Evidence → Selection refresh → Architecture rebind → Architecture rN+1 → Human Architecture Review. No bounded append-only path exists for new candidates (r6 precedent covers in-scope repair only, explicitly not transferable). Therefore: NO Discovery, NO Evidence, NO reader admission for Agentic Video in this pass. Currency record stands (INSPECT referral). §8 integration does not trigger (condition unmet by design).
- **P07B non-redundant chain (§9): PASS.** b11–b15 converted to comparison/synthesis (teacher/distillation dependence, region pretraining, classifier-vs-matching, fusion depths, query formulation, self-training, annotation/vocabulary axes); b16 map kept; fronts untouched. Depth kept as comparison material.
- **Cross-package dedup (§10): PASS.** Mechanism-front + comparison-back roles enforced (P06 b7/b8, P08 b8, P11 b7/b8 conversions; P03/P05 keeps verified clean). Zero exact-duplicate sentences in r14 (machine-verified).
- **P02 (§11): PASS.** Aux loss = standard recipe, never 必須 (guards verbatim); RPN attention metaphor source-attributed with modern-confusion guard.
- **P01 (§12): PASS.** DeiT (recipe/distillation/data-efficiency) vs Swin (hierarchy/shifted-window/dense-prediction) split in p01-b3; cap kept.
- **P13 OpenVLA causality (§13): PASS.** Unattributed efficiency causality cut; ceiling enforced (7B-scale conditional outperformance reported, no cause assigned); embodiment fix + G01 + date binding kept.
- **P15 (§14): PASS.** No internal package IDs in reader prose (P12→画面操作の節 etc.); HallusionBench cross-bound with formal provenance #3 (PRIMARY home stays P10); production language purged (19 patterns verified absent, incl. P09 deferral fences converted).
- **Metadata (§15): PASS.** SigLIP2 unified CLOSED (unresolved question deleted); renderer_binding points to r14 authority; canonical-r1-provenance-only distinction kept.
- **Terminology (§16): PASS.** DUSt3R intrinsics/pose/pointmap gloss; dataset-vs-metric distinction; 36-pattern banned scan clean with contextual retains documented.

## 2. Reverse audit (§5)

New Evidence (r6) → old LIMIT statements swept across all packages: stale blanket-unknowns in P09 replaced by per-axis confirmed/LIMIT split; all other packages' LIMITs re-checked against r6 (only P09 + D098/D105 claims changed; no other LIMIT invalidated). New Evidence never over-claimed beyond its axes.

## 3. Comparison report (§20, r13 → r14 per package)

- P01: 4blk, micro-edit (DeiT/Swin split).
- P02: 7blk, b2 attention-metaphor guard + b4 aux-loss fix.
- P03–P06: counts unchanged; P04 DUSt3R/トークン列 edits; P06 b7/b8 comparison conversion.
- P07A: metric-split sentences untouched (verified).
- P07B: 16blk, b11–b15 comparison conversion + b1/eval + b16 discipline edits.
- P08: 8blk, b8 comparison conversion.
- P09: 16blk, b2/b7 license refresh + b9–b12 pointer reconciliation + boundaries artifact matrix.
- P10/P12: unchanged (r13 merges stand).
- P11: 8blk, b5/boundaries production-language fences.
- P13: 10blk, b6 causality cut.
- P14: unchanged (r13 separation + terminology stand).
- P15: 16blk, b3/b15 HallusionBench binding, b9/b13 ID cleanup.
- Merged blocks: comparison conversions listed above (no block deletions; 139→139).
- Removed semantic duplicates: back-block mechanism/number/limitation recitals replaced by pointers (see per-block cut logs in agent returns, retained in execution record inputs).
- New evidence-derived propositions: P09 supplement prose already in r13 b13–b16 (r6 claims); r14 adds none (convergence only).
- Stale LIMITs removed: P09 blanket-unknowns (4) + production fences (7).
- Remaining unresolved: axis-level LIMITs (measured KV/latency, undisclosed internals), RT-1 specifics, agentic-video admission, stale downstream SHA pins (Human-gated path owed).

## 4. Claim-by-claim QA (§21)

- Forward (reader→Evidence): builder validates every ref (task + statement + subject) against r6 acceptance; 124/124 nodes bound; p15-b3/b15 ev-vmd080 verified present.
- Reverse (Evidence→LIMIT): §2 above.
- Cross-block: 0 exact dups; flagged n-gram pairs re-measured low (0.018–0.045 class).
- Cross-package: P09/P11/P15 model/benchmark descriptions consistent (80ms, 234ms-theoretical, フレーム/入力フレーム, POPE, ベースライン, DETR split verified identical across packages).
- #559: 9 forbidden absent, 16 required + 5 retains present.

## 5. Lifecycle guard (§24) / protected artifacts (§25)

- publication_preview/freeze/release remain pending; production-state.json untouched; no gate transitioned; no approval fabricated.
- Historical authorities (r10–r13, Evidence r1–r5, checkpoints, approvals, main.tex/pdf) untouched — zero tracked modifications; only new files added.
- Agentic Video re-entry: RECORDED, not bypassed.

## 6. Remaining CONTENT blockers

1. Sol/independent re-review of r6 Evidence batch + r14 reader (requested with this review).
2. Human-gated downstream rebind (candidate-matrix/draft-package SHA pins stale by design) via Architecture rN+1 — for Human to disposition.
3. Agentic Video formal admission via governed pipeline re-entry — for Human to disposition.
