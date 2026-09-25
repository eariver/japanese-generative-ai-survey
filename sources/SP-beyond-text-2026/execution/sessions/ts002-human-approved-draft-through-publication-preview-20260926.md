# Survey Production session — ts002-human-approved-draft-through-publication-preview-20260926

Issue: `SP-beyond-text-2026` / GitHub Issue `#526`
Branch: `special/beyond-text-2026-work` (existing only; no new/fallback/repair/review branches)
Execution authority: `docs/prompts/2026-09-25_muse-ts-002-human-approved-draft-through-publication-preview.md`
Human approval authority: `sources/SP-beyond-text-2026/execution/human-architecture-approval-20260925.md`
Sol review authority: `sources/SP-beyond-text-2026/execution/sol-architecture-review-r2-20260925.md`
Human decision: `ARCHITECTURE_REVIEW / APPROVED` (Human Owner「はい、承認します。進めてください」)

## Start guards (read-only, all PASS before any write)

- Remote work HEAD `87d51f30f8d9e1a877ff9c40dad1c00179f582f6` == Exact Starting SHA.
- Remote work tree `b72f54aad72a5907c2f8b21af42fdd4f28098f3c` == Expected Starting Tree.
- Remote main HEAD `0bbb02b3c5963403860897daec2feaf61e82589a` == Reviewed main SHA.
- Remote main tree `e4ddde5ed5059d303b818f54e27204369b256bcb` == Expected main Tree.
- Local checkout fast-forwarded to `87d51f30f` (no reset/rebase/force).

## Architecture approval materialization (canonical Human gate)

- Used `survey_human_gate_v2.record_architecture_approval` (current Core canonical mechanism).
- `reviewed_by = Human Owner`, `reviewed_at = 2026-09-25T14:07:26Z` (approval commit time),
  review_reference binds the ChatGPT Human Architecture Review for TS-002, the Human authority file
  (HEAD `36365ec65` / tree `6c197d7b`), Sol r2 PASS, and byte-identity of the r2 surface at `87d51f30`
  (architecture/summary/attention/state verified unchanged `36365ec` → `87d51f30`).
- Outputs:
  - `gates/architecture-approval.json` (`edd891999d7baf38`, binds arch `b496de50`, summary `00c7bc69`, attention `a206439c`)
  - `gates/reviews/architecture-r1.json` (revision 1: first Human review of this edition)
  - `gates/reviews/approvals/architecture-r1.json` (immutable snapshot)
  - `gates/review-index.json` (1 row, APPROVED)
- State: `ARCHITECTURE_ESTABLISHED`, `architecture_review = approved`, next `stage:drafting-synthesis`.

## Active Evidence/View/transition/Architecture hashes used for drafting

- Evidence `1fb07f81a2623f5a` (139: 126 VERIFIED / 8 PARTIAL / 5 NEEDS_MORE; sanitized `f8e273fd`)
- Views `e0c47bcf1b289f77` (139); transition ledger 43 entries; BT-D062 VERIFIED (not PARTIAL).
- Architecture `b496de50` (14 packages, page plan target 80 / max 96 guidance).
- Stage-basis override (`survey_agent_tool_v2.current_stage_basis_override`) used for post-approval
  derivation/validation only — the Core-canonical mechanism for content-addressed historical State-SHA
  drift (same precedent as `build_materiality_completeness.py`); all other basis checks rerun.

## Draft artifacts

- Interactive input: `execution/draft-through-preview-20260925/interactive-drafting-input.json`
  (14 packages, 71 PARAGRAPH blocks, all package discovery sets covered 1:1).
- `draft/v2/packages/<14 ids>/draft-package.json + draft-result.json` + `profile-synthesis-input.json`
  + `profile-synthesis-result.json` (ESTABLISHED) + archive.
- Lifecycle `ARCHITECTURE_ESTABLISHED` → `DRAFT_COMPLETE` (checkpoint `DRAFT_COMPLETE.json`).

## Manuscript section/chapter inventory (15 numbered sections)

1. 表現と圧縮 (BT-O01) — 2. 生成パラダイムと目的関数 (BT-O02) — 3. 条件づけ (BT-O03) —
4. 制御と参照 (BT-O04) — 5. 生成から編集へ (BT-O05) — 6. 音声・声 (BT-O07+BT-O06) —
7. 音楽・一般音響 (BT-O08+BT-O11) — 8. 映像 (BT-O09+BT-O06) — 9. 長時間・同期 (BT-O06+BT-O11) —
10. 実行と配備 (BT-O10) — 11. 評価 (BT-O11) — 12. 収束 (BT-O12) —
13. capstones (BT-O04/O05/O06/O07) — 14. 受容 (BT-O10/O06) — 15. 結び (FINAL_SYNTHESIS).
- 75 subsections, 23 commensurate tables, 139/139 bib keys cited and all 139 records cited,
  43 transition entries (120 bound discovery IDs) all cited.

## Actual PDF page count and allocation

- 68 pages (CI LuaLaTeX, audit PASS, 0 blocking + 0 layout findings).
- Allocation: s1 3.5 / s2 4 / s3 3 / s4 4 / s5 4 / s6 4 / s7 4 / s8 4 / s9 3 / s10 4 / s11 4 /
  s12 4 / s13 3 / s14 1 / s15 4 + front/back matter + references.
- Delta vs approved plan (8/10/5/5/5/9/7/9/4/5/7/4/8/2+6): prose density differs from planning
  assumption; representation/paradigms/speech/music/video each substantive (3.5–4pp);
  runtime/evaluation not collapsed; capstones compact and reception bounded by boundary design.
  Per execution authority §11, substance preferred over mechanical page restoration; no padding added.
  68 lies within the 64–96 planning envelope; below-target disposition recorded in
  LONGFORM_TECHNICAL_DEPTH (`page-plan:68/80`, `density-review:below-target-substantive`).

## Bibliography/citation counts

- `references.bib`: 139 `@online` records generated from sanitized Evidence acceptance
  (PARTIAL/NEEDS_MORE notes preserved; X ledger internal path noted).
- `\autocite`: 139/139 keys cited; 0 undefined (CI); 0 uncited records; 0 duplicated paragraphs.

## Transition coverage (43 entries)

- All 43 ledger entries mapped across the 14 packages (representation T-REP → paradigms →
  conditioning/control/editing → speech/music/video → temporal → runtime → evaluation →
  convergence → capstones → reception); bottleneck→change→improvement→tradeoff→succession
  preserved where sources support it; 120/120 bound discovery IDs cited.

## PARTIAL/NEEDS_MORE handling

- PARTIAL 8 (BT-D022/D059/D076/D083/D089/D098/D106/D134) used at stated levels only, fenced in
  front matter + section boundaries; NEEDS_MORE/HOLD 5 (BT-D024/D072/D091/D120/D125) excluded
  from packages, carried as barriers with sibling-authority coverage stated. Never upgraded.

## LOW_SIGNAL handling

- 11 lanes (duplex interruption, cross-lingual cloning, long-range music structure,
  metric-vs-preference, Nano Banana corpus, few-step ablations, flow-vs-diffusion,
  consumer klein replication, ElevenLabs independent eval, Wan 2.5+ authority, Sora mechanism)
  reported as open in capstones/reception/synthesis; never inflated or ranked.

## Closed-system and X boundary audit

- Closed products: capability/workflow/lifecycle only, vendor claims attributed, no hidden
  architecture/tokenizer/training inference, version/date binding (undated pages explicit).
- X (BT-D139): one bounded record (27 posts ≠ 27 authorities), reception/deployment/failure
  evidence only, no ranking, rebound-required rule stated.
- Reader-prose redaction pass: internal Discovery IDs removed from prose (BT-D059/BT-D134/
  btd076/btd106/locator list → neutral wording); citations via `\autocite` only. Verified in
  rendered PDF (p52) and by scan (0 residual IDs outside `\autocite`).

## Validation commands/receipts/results

- `build_validation.py`: manuscript manifest (`a472b183`) → 4 deterministic results →
  quality bundle → surface semantic review → surface gate → semantic review (9 checks PASS) →
  visual review (5 checks PASS). All Core validators PASS.
- `advance_validation.py`: `DRAFT_COMPLETE` → `VALIDATED_DRAFT` (checkpoint `VALIDATED_DRAFT.json`).
- `advance_candidate.py`: candidate `8416c5d90167a0fe` READY_FOR_PUBLICATION_PREVIEW →
  `VALIDATED_DRAFT` → `RELEASE_CANDIDATE` (publication_preview pending, HUMAN_GATE_REACHED).
- Edition checks: 15 sections; 120/120 transition discoveries cited; 0 stale-provenance phrases;
  0 TODO; 0 superlatives; 225/225 unique long paragraphs.

## PDF/typesetting QA findings and fixes

- r1 CI build (run 36164087589): FAIL on 171× missing glyph 绑 (U+7ED1, simplified 绑定 in prose).
  Fixed: 绑定 → バインド (30 occurrences).
- Visual QA of rendered r1 PDF (cover, front matter, TOC, s1, evaluation table p46, capstone p52):
  two-column flow, tables within margins, TOC hierarchy intact; found literal Discovery IDs in
  prose (p52) → redacted (7 replacements).
- Surface gate found `coverage を拡大` (RSG-LEX) → rephrased to domain language (3 replacements).
- r3 CI build (run 36165946276): PASS — 68 pages, 0 blocking, 0 layout findings.
- r4 CI build after redaction/rephrase (run 36166730605): PASS — 68 pages (`f7dd6f999f860e41`),
  0 blocking, 0 layout findings. All 68 pages text-verified (min 663 chars, no blanks);
  cover/TOC/capstone/synthesis/reference pages rendered and inspected.

## Remaining warnings/open issues for Human Publication Preview review

- 68 vs 80 target (within 64–96 envelope; disposition recorded; no padding by design).
- Completeness remains LIMITED (4 SATISFIED / 8 LIMITATION) with 13 barriers + LOW_SIGNAL lanes
  carried explicitly — the edition is honestly bounded, not artificially complete.
- Vendor evaluations remain vendor claims until independently reproduced.
- Wan open line frozen at 2.2; Sora mechanism undisclosed; C2PA spec homepage-only.

## Final production lifecycle state

- `RELEASE_CANDIDATE`, `architecture_review = approved`, `publication_preview = pending`,
  `next_action = PUBLICATION_PREVIEW`, `terminal_reason = HUMAN_GATE_REACHED`.
- Checkpoints: draft/validation passed; publication_preview/freeze/release pending.
- Semantics: `PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`.

## Freeze/Release confirmation

- NOT entered: no freeze-record, no release-manifest, no merge-verification, no release-record;
  no publication merge; no `publication-preview-approval.json` fabricated.

## Final remote HEAD/tree after non-force push

- HEAD `5524d73a891245935301fad7e077eec32a34a619`, tree `02e9891d86371f0ca867f6633f834bdd73888964`
  (origin/special/beyond-text-2026-work fast-forward, non-force; no new/fallback branches;
  no force push/reset/rebase/history rewrite).
