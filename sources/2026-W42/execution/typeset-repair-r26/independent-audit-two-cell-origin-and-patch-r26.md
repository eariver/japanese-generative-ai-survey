# W42 r26 — independent-audit two-cell origin and patch (NONCANONICAL)

Status: `SOL_W42_R26_FOCUSED / NONCANONICAL` evidence (not a Gate, not Publication).

## 1. Authority strings (r18 master, blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`)

Reader `reader-preview-r18.PROPOSED.json`:

- P2 / `t2-11` TABLE, LFM2.5 row, disclosure cell (full row):
  `LFM2.5｜実体：24B/2B推論専用CoT・131K文脈・33T事前学習・総36T訓練予算・能動24.5億｜効率主張：16種ベンチ表（温度つき、発行者計測）・スタック依存スループット｜開示：報酬ハッキング自己開示（独立検証ではない）・商用上限1000万米ドル（法主体の年商）`
  Required cell tail: `開示：報酬ハッキング自己開示（独立検証ではない）・商用上限1000万米ドル（法主体の年商）`
- P3 / `t3-18` TABLE, Nemotron 3.5 row, license cell (full row):
  `Nemotron 3.5｜120B/12B Mamba-2＋視覚｜MOPD/MTP/QAD開示（発行者）｜Bolt 74B今・E4B未来｜OpenMDW：Super VLファイル未確認、OSI主張不可、EXO不採用`
  Required cell tail: `OpenMDW：Super VLファイル未確認、OSI主張不可、EXO不採用`

Citations attached in print TeX (unchanged): `B11,B69,B12` (LFM2.5) and `B21,B72,B22,B20` (Nemotron 3.5) — both verified present in r18 ledger rows for these TABLE_ROW blocks.

## 2. Variant history (byte-verified, read-only)

| revision | TeX blob | T2 LFM2.5 cell | T3 Nemotron cell | verdict |
|---|---|---|---|---|
| r18 Reader (master) | `fc4fd9f2…` (JSON) | `…商用上限1000万米ドル（法主体の年商）` | `…Super VLファイル未確認、OSI主張不可、EXO不採用` | authority |
| r22 diagnostic TeX | `6099efb0…` (line 179 / 319) | `…商用上限1000万ドル` | `…Super VL未開封、OSI主張不可、EXO不採用` | WRONG (both) |
| r25 diagnostic TeX | `54aca5f2…` (line 190 / 335) | `…商用上限1000万ドル` | `…Super VL未開封、OSI主張不可、EXO不採用` | WRONG (both, inherited) |
| r26 diagnostic TeX | `ffdd4574…` (line 191 / 336) | `…商用上限1000万米ドル（法主体の年商）` | `…Super VLファイル未確認、OSI主張不可、EXO不採用` | RESTORED |

Key point (Sol disposition confirmed, re-verified here): both shortened strings already occur in **r22** (`diagnostic-r22/main.tex` blob `6099efb0…`, lines 179/319). They therefore **predate** the r25 MULTICOL-V2 redesign. Any claim that the r25 multicol work introduced — or that wrapper-only diffing could have detected — these content differences is false. This is a **Reader→TeX cell-fidelity defect inherited since r22**, not a layout regression, and the r26 fix is a content restoration, not a geometry change.

## 3. r26 patch (exact, minimal)

Base: r25 `main.tex` blob `54aca5f2…`. `diff r25 r26` yields exactly 4 hunks:

1. Line 1: header marker `r25-MULTICOL-V2` → `r26-MULTICOL-V2` (revision identity only).
2. Line 3 (new): provenance note `r26: r25 MULTICOL-V2 geometry kept; exact two-cell Reader restores ONLY (t2-11 LFM2.5 + t3-18 Nemotron3.5). No other prose/cell/geometry change.`
3. T2 row: `商用上限1000万ドル \cite{B11,B69,B12}` → `商用上限1000万米ドル（法主体の年商） \cite{B11,B69,B12}`.
4. T3 row: `OpenMDW：Super VL未開封、OSI主張不可、EXO不採用 \cite{B21,B72,B22,B20}` → `OpenMDW：Super VLファイル未確認、OSI主張不可、EXO不採用 \cite{B21,B72,B22,B20}`.

No other byte differs: all 7 needspaces (18/18/30/30/22/22/20), all `multicols` segments, all captions, all other cells/rows/cites, typography, columnsep, bibliography, cover — byte-identical to r25. `preview.sty` copied byte-identical (sha256 `f0492fb6…`, same as r22/r25).

## 4. Why historical self-audit falsely passed

- r25 `reader-content-and-bib-invariance-r25.md` claimed "reader bytes preserved / visible words identical all 7" via **C2→V2 print-diff transitivity**: it compared r25 TeX against the r22-lineage TeX (already carrying the shortened cells) instead of against r18 Reader bytes. Diff-of-derivatives cannot detect a defect present in the common ancestor.
- r22–r25 visual QA compared **PDF images to TeX source** (self-consistency), which passes by construction when TeX itself carries the wrong string: the printed `1000万ドル` matches the TeX `1000万ドル`, so image-vs-source checks are blind to Reader divergence.
- The independent audit broke the loop by comparing **r18 Reader JSON bytes → r25 TeX bytes → page PNGs** directly (cell-level, per-table), which is the method r26 now replays fresh for all 7 tables (see `reader-to-tex-all-seven-tables-cell-parity-r26.md`).
- Lesson recorded: `wrapper-only` / `原稿不変` claims are only meaningful relative to a stated baseline; the baseline here was r22-derived TeX, not r18 Reader. Future invariance claims must name the baseline blob and re-anchor to `fc4fd9f2…` on every revision.

## 5. Print closure

- r26 PDF (sha256 `c76f4a6e…`, 21 pp, 508624 bytes): p06 shows the full restored LFM2.5 qualifier incl `（法主体の年商）` with cites; p09 shows `Super VLファイル未確認` with cites. Both tables remain atomic on their pages; 21-page map unchanged; log has 0 warnings/errors.
- Forbidden strings `商用上限1000万ドル` (short form) and `Super VL未開封` occur **zero** times in r26 TeX and in PDF text extraction of p06/p09; restored strings occur exactly where required.
