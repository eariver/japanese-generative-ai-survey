# Survey Production session — ts002-final-anygpt-cleanup-20260926

Authority: `docs/prompts/2026-09-26_muse-ts-002-issue533-final-anygpt-zero-shot-base-cleanup.md`
Sol: `sources/SP-beyond-text-2026/execution/sol-terminology-readback-issue533-r1-20260926.md` (REQUEST_CHANGES/ONE_RESIDUAL_SOURCE_BOUND_TERM)
Branch: `special/beyond-text-2026-work` (existing only)

## Starting guards (read-only, all PASS; zero writes until Human decision)

- Remote work HEAD `27a7611c3b6d363240758ea66cc0f23f9b918838` == Exact Starting SHA.
- Remote work tree `1625e1685b349b7c06f10ec901fd110febe83b72` == Expected Starting Tree.
- Remote main `0bbb02b3c5963403860897daec2feaf61e82589a` / `e4ddde5ed5059d303b818f54e27204369b256bcb` == reviewed main.

## Main guard

- `survey_human_gate_v2` revision mechanism; Architecture approval preserved; no Freeze/Release.

## Human decision (explicit, no inference)

- `REQUEST_CHANGES @ DRAFT_COMPLETE` on pending Publication Preview (lifecycle mechanics require it: validated-source is checkpoint-bound; rewind is the only canonical pre-Human repair path).
- Recorded as `gates/reviews/publication-r4.json` (expected_revision=4); lifecycle → DRAFT_COMPLETE; state revalidated clean.

## Exact files changed

- `surveys/special/beyond-text-2026/main.tex` (3 AnyGPT phrases only)
- `surveys/special/beyond-text-2026/main.pdf` (rebuilt)
- `sources/SP-beyond-text-2026/publication/v2/*` (manuscript/deterministic/bundle/surface/semantic/visual/candidate rebuilt)
- `sources/SP-beyond-text-2026/orchestration/v2/checkpoints/{DRAFT_COMPLETE,VALIDATED_DRAFT}.json` (rebuilt)
- `sources/SP-beyond-text-2026/execution/terminology-issue533/terminology-decision-ledger.json` (ESCALATE→REPLACE)
- `sources/SP-beyond-text-2026/execution/draft-through-preview-20260925/` (pdf-build-audit-final.json, build_validation_final.py, advance_*_final.py, validation receipts)
- `references.bib`: byte-identical.

## Three BT-D096 before/after phrases

1. `報告条件のゼロショット素体では画像説明CIDEr…` → `報告条件のベースモデルのゼロショット評価では画像説明CIDEr…`
2. `ゼロショット素体という条件も値と一体であり…` → `ベースモデルのゼロショット設定も値と一体であり…`
3. `素体のゼロショット値を調整後の姿と混同しない` → `ベースモデルのゼロショット結果を調整後の姿と混同しない`
- Meaning preserved: AnyGPT base model evaluated in a zero-shot setting (not baseline/chat/pretraining). Numbers, targets, citations, condition-bound boundary unchanged.

## Ledger decision/count update

- `ゼロショット素体`: ESCALATE → REPLACE, 2 → 0 (rationale bound to AnyGPT base-model terminology).
- All other 241 ledger rows unchanged.

## Invariant results

- `\autocite` blocks 1259 → 1259, sequence identical; citation-key multiset identical.
- Number/unit tokens 1041 → 1041 identical.
- Section/subsection order, labels, kickers identical; 139/139 coverage intact.
- Evidence statuses, PARTIAL/NEEDS_MORE, vendor/closed-system boundaries unchanged.
- All previously-cleaned Issue #533 terms remain zero in main.tex and rendered PDF.

## Exact PDF page count and SHA-256

- 75 pages, SHA-256 `31abcb35a4fd2c9354153d5d258efdb0d92006bc5aa2e9ce8613fa533df84bc4` (CI PASS, 0 blocking + 0 layout findings; commit `54463930d`).

## Visual regression result

- All 75 pages text-verified (min 328 chars refs-tail p75); terminology scan zeros incl. `ゼロショット素体`/`素体のゼロショット値`; TOC, AnyGPT region (p60), refs pages rendered and inspected; no clipping/overflow/broken glyphs/systematic blanks; bibliography rendering intact.

## Final terminology scan

- 16 scan terms all zero except none remaining (素体 fully gone from reader prose).

## Final Core state / Human Gate

- RELEASE_CANDIDATE, architecture_review approved, publication_preview pending, HUMAN_GATE_REACHED.
- Review index: ARCH r1 APPROVED; PUB r1/r2/r3/r4 REQUEST_CHANGES (all Human). Next Human decision records publication-r5.
- `PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`. No approval fabricated. Freeze/Release/merge/release-record: none, prohibited and not entered.

## Starting/final HEAD and tree

- Start: HEAD `27a7611c3b6d363240758ea66cc0f23f9b918838`, tree `1625e1685b349b7c06f10ec901fd110febe83b72`.
- Final: (recorded after push)
