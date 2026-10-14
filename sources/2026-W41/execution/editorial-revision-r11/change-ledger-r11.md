# W41 r11 change ledger (BLOCKER / MAJOR / MINOR per audit item)

Status: `EDITION_LOCAL / PROPOSAL_LEDGER`
Date: 2026-10-13 JST
Old: canonical `draft/v2/packages/*/draft-result.json` (v10.1, DRAFT) — UNTOUCHED.
New: `execution/editorial-revision-r11/proposals/*/draft-result.json` (v11.0, REVISED).

## BLOCKER

### B-01 — P4 image output units (p1) — RESOLVED in proposal
- Before: 「出力は画像が4K」＋「どれだけの解像度」— 4K tokenを画素解像度と誤読させる記述。
- After: 「出力は画像が4K token、テキストが64K token」「画像の『4K token』は出力token数の上限であり、画素解像度や画像寸法の上限ではない」「画素数や寸法の上限は取得カード範囲から確認できない」。
- Evidence: supplement excerpt (Input up to 1M token context; Image 4K token output; Text 64K token output) via claim-1 ref; limitation refs for unknowns.
- Verdict: RESOLVED (validator PASS + guard grep clean).

### B-02 — P5 SynthID text support (p6, t1) — RESOLVED in proposal
- Before: 「テキストは対象に含まれていない」「テキスト除外」「検出精度のベンチマークも存在しない」。
- After: 「取得した公式ブログで検証対象として明示されているのは画像・映像・音声であり、テキストの対応状況はこの資料からは確認できない」「取得した資料の範囲内では、検出精度を示す評価数値は確認できなかった」。
- Evidence: synthid excerpt (images/video/audio enumeration; text NOT listed note) via claim-1; limitation-1 for benchmarks.
- Also: scale numbers added (1800億件以上 images/videos; 24万年分 audio) as申告規模 with non-transfer caveat (p9).
- Verdict: RESOLVED (validator PASS + old-phrasing grep 0).

## MAJOR (technical depth / claim precision)

- P1 p5/t1: billing-unit separation (cache-read $0.01/$0.05 as the only confirmed split; input/output unit basis unknown stated). RESOLVED (no fabrication; unknowns marked).
- P1 p7/t1: bench-object unknowns (GDPval/OSWorld/HLE/TB4 objects/conditions/scales unknown stated). RESOLVED.
- P2 p1: Decisions function description added (typed answers, v1/decisions, gpt-6-luna, beta; 10x/methodology caveat kept). RESOLVED.
- P3 p5: MRL truncation dims (128/256/512) + practical meaning + text-modality scoping. RESOLVED (vendor-attributed, claim-1 anchored).
- P3 p8: Mistral 52B/1.05T split, per-1M input/output price display, 49B secondary-record note. RESOLVED.
- P3 p13/p14/p16/t1: MoE total/active + memory/compute prose; process paragraph replaced with verification-guidance paragraph; download-verified phrasing removed (three-stage distinction). RESOLVED.
- P4 p2: Elo 1050±14 (Thinking) as vendor relative value, arena non-equivalence kept. RESOLVED.
- P5 p2/p3/t2: FPR-vs-detection split, psych/ELI5 + math caveat, same-record scope, synonym triple (92/66/17 @400-token) in new table, no cross-population claim. RESOLVED.
- P5 scale: 180B/240k-yr as申告規模 with accuracy-non-transfer note (p9). RESOLVED.
- P6 p5/p7/p8: 13.4pp vs ~32% split (+48% time), caveats consolidated, judged-scope sentence added. RESOLVED.

## MINOR (Japanese quality / Priority C)

- All 9 banned self-referential patterns removed from 6 proposals (grep 0): Muse自身/委託/到達点整備/バンドル/セル粒度/小品/手ずから/地平線/取得形態.
- Residual meta-adjacent lines rewritten (P2 p11 beta-meaning, P3 p14 verification steps, P4 p5, P5 p9/p12, P1 p4/p8/p9/p11).
- Reader-needed boundaries kept (vendor-measured, unconfirmed prices/downloads, PDF unread, clock/license gaps).
- Two post-build fixes revalidated: P2 typo (オープWェイト→オープンウェイト), version pattern (r10.1→v10.1 style → v11.0).

## must_cover (27, substantive mapping preserved)

- P1:4, P2:5, P3:7, P4:3, P5:5, P6:3 — each requirement mapped to explaining blocks only (no blanket assignment). Validator PASS 6/6 via official draft-check.

(End of file)
