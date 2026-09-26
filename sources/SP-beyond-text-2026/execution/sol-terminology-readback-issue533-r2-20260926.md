# Sol terminology readback — Issue #533 r2

Status: `REQUEST_CHANGES / ONE_READER_TERM_PLUS_LEDGER_VIEW_SYNC`

Date: 2026-09-26 JST

Reviewed branch state:
- `special/beyond-text-2026-work`
- HEAD `4fd1080731e316eda9fad380ecf1ab99ed52e256`
- tree `f3d2bb8a23028768128cb91820ca36c7505d1182`
- main guard `0bbb02b3c5963403860897daec2feaf61e82589a` / `e4ddde5ed5059d303b818f54e27204369b256bcb`

## What passed

The bounded AnyGPT cleanup correctly normalized the three explicitly targeted BT-D096 phrases to the source-bound AnyGPT base-model / zero-shot wording. The canonical JSON ledger was also updated from `ESCALATE` to `REPLACE` for `ゼロショット素体`, with `2 -> 0`. Reported semantic invariants remain acceptable: citations, numbers/units, section structure, 139/139 coverage, Evidence boundaries, vendor/closed-system boundaries, and bibliography authority were preserved. Production state remains `RELEASE_CANDIDATE` with Publication Preview pending and Freeze/Release unentered.

## Blocking residual A — reader-facing `素体` still remains

The exact active `main.tex` still contains:

`...記録locatorの転記欠陥は正規二四〇二・一二二二六側本文で消費した旨を添え、素体値の比較は条件固定の差として読む。...`

This contradicts the session report statement that `素体` is fully gone from reader prose. The same source-bound subject has already been resolved as the AnyGPT base model evaluated in a zero-shot setting, so `素体値` is no longer acceptable reader-facing terminology.

Required correction direction:

`ベースモデルのゼロショット結果の比較は条件固定の差として読む。`

Equivalent natural wording is acceptable only if it preserves exactly the same subject and boundary. Do not alter surrounding numbers, comparisons, citations, or the condition-bound caveat.

## Blocking residual B — Markdown ledger view is stale

Canonical JSON ledger now records:
- decision `REPLACE`
- final term `ベースモデルのゼロショット評価/設定/結果 ...`
- `after_count: 0`

but `terminology-decision-ledger.md` still says:
- `ESCALATE: 1`
- `ゼロショット素体 | 2 | 2 | ESCALATED...`
- `Additional candidates: all REPLACE except ゼロショット素体 ESCALATE.`

The Markdown view must be synchronized with the canonical JSON ledger. No other ledger decision may change.

## Disposition

`REQUEST_CHANGES / ONE_READER_TERM_PLUS_LEDGER_VIEW_SYNC`

This is not a new research or terminology campaign. Only:
1. replace the one remaining reader-facing `素体値` phrase with source-bound AnyGPT base-model zero-shot wording;
2. synchronize `terminology-decision-ledger.md` with the already-correct JSON ledger;
3. rebuild/revalidate the exact Publication Preview and prove semantic invariants;
4. stop again at Publication Preview pending.

All Issue #529 depth changes and all other Issue #533 terminology changes are accepted and frozen. Freeze / Release remain unauthorized.
