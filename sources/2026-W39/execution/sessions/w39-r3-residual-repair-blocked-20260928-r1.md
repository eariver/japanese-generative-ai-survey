# Survey Production session — w39-r3-residual-repair-BLOCKED-core-representation-gap-20260928-r1

Issue: `2026-W39`
Started: `2026-09-28T14:0xZ` (remote preflight guards PASS; local fast-forwarded to remote `5c141a6e5c8d5c145dfab399d23987f42e4d0a43`)

## Starting authority

- Branch: `weekly/2026-W39-v2-work`; Exact Starting Remote SHA `5c141a6e5c8d5c145dfab399d23987f42e4d0a43` / tree `1bb3135c5db15a09dbb7de27fd0c2a88539faaf3` (all §2 guards PASS: main/frozen/ancestors verified)
- Execution contract: `execution/requests/sol-w39-publication-preview-r2-sol-review-residual-repair-through-r3-20260928.md`
- Human r2 decision: still `PENDING` (no new Human input in this run)
- No gate decision recorded, inferred, or mutated in this run.

## Actions actually performed

- Enumerated 3-file union corpus (BASE 178 + SUPPLEMENT 177 + R2_RESIDUAL 37 + request form 計り方 = 392 search forms).
- Searched r2 reviewed bytes: 192 forms with hits (424 instances), 200 ZERO_HIT_CHECKED.
- Adjudicated all Sol §5 residuals and repaired TeX (卓上版, 腕前, 貯めて使える制限の戻し, 発表側の手つき, 近来で最良, Claude Code tautology, 公式の場, 大規模A/Bテスト, 使る typo→使う, 読みの行番号, 出荷済み, 学びの長さ, 扱える投稿, 三つのモデルで寄せた, 測り/計り方, 速さの薦め, 量らない, スコアの比べ, プレプリントの記録, 四組織による作, 書きぶり, 場の声, 他所の確かめ, 請求の実相, 力の入れ方 re-decided per residual authority, 先代, 長い仕事, 作り手, 書き手, 各所, 使える日の目処, 次の一手, 調子).
- Seed-external final-byte scan: repaired 文脈資料→背景情報, カーネルの持ち込み→カーネル移植; reviewed-and-retained ordinary words logged (挑む者, 公開の場, 試し, 手ほどき, 用立て, 場→反応 after fix, 力の入れ方 n/a, 要約文の数え).
- New generic defects requiring successor supplement: 0. Typo corrections: 1.
- r3 occurrence ledger built (424 occurrences: 59 reader REPLACE / 49 reader RETAIN / 200 ZERO_HIT / 315 frozen+URL distinctly categorized incl. FROZEN_INTERNAL_NON_READER) + human companion.
- Rebuilt via CI (run 36440543369, artifact 10979260910); four-surface byte identity independently demonstrated (repo == sidecar == artifact == artifact-sidecar == 7fac4b5c, 329744 B, 12 pp).
- Regenerated manuscript/deterministic/bundle/surface-input (corrected blocks)/reviews/gate/candidate (READY, a1517f1e); caught and fixed stale surface-input blocks from r2 builder.

## Blocking defect (Core representation gap)

- After publication regen, `survey_stage_validation_v2` and `validate_agent_state` fail with 6× `Stage Checkpoint artifact drift` (r2 DRAFT_COMPLETE.json pins r2 bytes; r3 bytes differ).
- Returning state RELEASE_CANDIDATE→DRAFT_COMPLETE has NO canonical representation without a Human record:
  - `request-publication-preview-revision` would fabricate a non-existent Human decision (contract §3 forbids; governance forbids) — NOT USED.
  - `invalidate-pending-gate` is fail-closed twice over: (1) arch-approved + PUBLICATION_PREVIEW gate → "cannot cross an active Human Architecture approval"; (2) existing Human review records in index — both verified in code.
  - Manual state/checkpoint surgery would bypass fail-closed guards and violate the trust model — NOT DONE.
  - `revalidate-publication-surface` requires VALIDATED_DRAFT lifecycle — not our state.
- Per contract §11 ("canonical Human Gate/invalidation protocol cannot represent the requested boundary"), this is a legitimate BLOCKING STOP. No unauthorized workaround performed.

## Restoration (no history rewrite)

- To avoid leaving an invalid state, r3 publication bytes were restored to the canonical r2-pinned bytes (`git checkout 01724a7d -- publication/ main.pdf sha256`; r3 review-row stubs removed).
- State re-validated: `validate_agent_state` errors NONE; lifecycle `RELEASE_CANDIDATE`, next `PUBLICATION_PREVIEW`.
- All r3 repair work is preserved in commits `01724a7d` (TeX + r3 ledger) and CI run `36434164543`/artifact `10979260910` (7fac4b5c, independently verified) for a follow-up run once governance resolves (e.g., Human records r2 REQUEST_CHANGES, canonically invalidating to DRAFT_COMPLETE, after which the preserved r3 repair can be re-applied and re-validated).

## End state

- Lifecycle: `RELEASE_CANDIDATE`
- Terminal reason: `HUMAN_GATE_REACHED`
- Next action: `PUBLICATION_PREVIEW` (Human decision on r2 still pending)
- R3 Preview: NOT created (blocked before candidate binding)
- Session status: `BLOCKED_ON_CORE_REPRESENTATION_GAP`
