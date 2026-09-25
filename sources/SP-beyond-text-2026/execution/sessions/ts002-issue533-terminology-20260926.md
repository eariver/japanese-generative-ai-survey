# Survey Production session — ts002-issue533-terminology-20260926

Issue: `#533` — reader-facing terminology cleanup (Human Owner revision request)
Sol boundary: Issue #533 latest Sol execution-boundary comment (eariver/OWNER, 2026-09-25)
Branch: `special/beyond-text-2026-work` (existing only)
Prior Sol r3 PASS (`26fabad23`) superseded by Issue #533 while open (not final disposition).

## Starting guards (read-only, all PASS)

- Remote work HEAD `26fabad2335c09ddc7babe62cf703b1aa5cdbc00` == Exact Starting SHA.
- Remote work tree `86509d277592c2b4ddd879fb03d0c8b248d273f1` == Expected Starting Tree.
- Remote main `0bbb02b3c5963403860897daec2feaf61e82589a` / `e4ddde5ed5059d303b818f54e27204369b256bcb` == reviewed main.

## Main guard

- Current Human Gate Core: `survey_human_gate_v2` revision mechanism; Architecture approval preserved; no Freeze/Release.

## Human Publication Preview r3 REQUEST_CHANGES canonical record

- Human explicitly selected REQUEST_CHANGES @ DRAFT_COMPLETE (no inference).
- `gates/reviews/publication-r3.json` (expected_revision=3), lifecycle RELEASE_CANDIDATE → DRAFT_COMPLETE.
- Invalidated validation checkpoints removed by Core; Architecture approval intact; state revalidated clean.

## Changed files

- `surveys/special/beyond-text-2026/main.tex` (terminology-only replacements; see ledger)
- `surveys/special/beyond-text-2026/main.pdf` (rebuilt 75pp)
- `sources/SP-beyond-text-2026/publication/v2/*` (manuscript/deterministic/bundle/surface/semantic/visual/candidate rebuilt)
- `sources/SP-beyond-text-2026/orchestration/v2/checkpoints/{DRAFT_COMPLETE,VALIDATED_DRAFT}.json` (rebuilt)
- `sources/SP-beyond-text-2026/execution/terminology-issue533/terminology-decision-ledger.{json,md}` (new, 242 rows)
- `sources/SP-beyond-text-2026/execution/draft-through-preview-20260925/` (pdf-build-audit-issue533.json, build_validation_533.py, advance_*_533.py, validation receipts)
- `references.bib`: byte-identical (no new authority).

## Terminology decision ledger

- Canonical: `execution/terminology-issue533/terminology-decision-ledger.json` (+ `.md`), 242 rows:
  REPLACE 228 (+5 manual compositions), SUPERSEDED_BY_MANUAL_COMPOSE 7, DUPLICATE_ALREADY_APPLIED 1, ESCALATE 1.
- 4 subagent groups with Evidence read-back; cross-group nesting reconciled (5 manual compositions for overlapping sites; order B→C→D→A with exact-count application + residual verification).

## High-confidence term before/after counts (main.tex; bib untouched)

- 零射影 31→0; 声器 35→0; 符号言語 10→0; 無撞着 13→0; 抽出推論 28→0; 類別条件 5→0; 類別脱落 2→0; 変換器 57→0 (all verified Transformer-sense, named forms); ゼロショット素体 2→2 (ESCALATED); 流れ整合 14→0; 整流流れ 3→0; 模擬なし 4→0; 任意間 11→0; 多能模型 2→0; 話声 14→0; 標本化 51→0.
- Rendered-PDF scan confirms identical zeros; ゼロショット素体 2 remain explicitly.

## Additional candidate retain/replace/escalate decisions

- REPLACE: Flow Matching（フローマッチング）, Rectified Flow（整流フロー）, simulation-free + gloss, any-to-any/任意モダリティ間 (AnyGPT framing verified), Seed-TTS descriptor (title-bound, Sol-reviewable), 音声/発話音声/話者音声 per source, generative 標本化→サンプリング (51 individually verified).
- RETAIN: generic 変換器 common-noun uses — none found (all 57 Transformer-sense); signal-rate/statistical senses of sampling — none among the 51+28.
- ESCALATE: ゼロショット素体 ×2 (BT-D096 AnyGPT: card "zero-shot base" cannot distinguish base-model/baseline/setup) — unmodified, returned to Sol.

## Semantic invariants comparison (before r3-repair → after)

- `\autocite` blocks 1259→1259, citation-key multiset identical; number/unit tokens 1041→1041 identical.
- Section structure 15 sections, order + labels + kickers identical; §6/§7 headings updated by terminology (fidelity locations rebuilt with exact new titles).
- Evidence statuses, 139/139 coverage, PARTIAL/NEEDS_MORE boundaries, vendor attribution, closed-system boundary: unchanged.
- Only grammar-level adjustments accompanying term swaps; no semantic prose changes.

## Citation invariants

- 139/139 keys cited and all records cited; 0 undefined (CI); deterministic subject-entity binding rebuilt PASS.

## Exact PDF page count / SHA-256

- r3: 73pp `67cc6592` → current: 75pp `e05a88bc1574e978` (+2 from katakana/English widening; observation, not target). CI PASS, 0 blocking + 0 layout findings.

## Visual regression result

- All 75 pages text-verified (min 328 chars refs-tail p75; no systematic blanks); TOC, §2/§6/§8 openings, table pages, refs beginning/middle/end rendered and inspected; no clipping/overflow/broken glyphs; bibliography author rendering intact (r2 repair preserved); §6/§7 heading changes render cleanly.

## Unresolved terminology items

- ゼロショット素体 ×2 (ESCALATE) — pending Sol read-back verdict; everything else resolved.

## Final Core state / Human Gate

- RELEASE_CANDIDATE, architecture_review approved, publication_preview pending, HUMAN_GATE_REACHED.
- Review index: ARCH r1 APPROVED; PUB r1/r2/r3 REQUEST_CHANGES (all Human). Next Human decision records publication-r4.
- `PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`. No approval fabricated. Freeze/Release/merge/release-record: none, prohibited and not entered.

## Starting/final HEAD + tree

- Start: HEAD `26fabad2335c09ddc7babe62cf703b1aa5cdbc00`, tree `86509d277592c2b4ddd879fb03d0c8b248d273f1`.
- Final: HEAD `91e2a1fa7b0b6e513c4f9778ce9f2bba7c59200c`, tree `f2ca50629307accb4539148ba1a91540e3f8590a`
  (origin/special/beyond-text-2026-work fast-forward, non-force; no new/fallback branches;
  no force push/reset/rebase/history rewrite).
