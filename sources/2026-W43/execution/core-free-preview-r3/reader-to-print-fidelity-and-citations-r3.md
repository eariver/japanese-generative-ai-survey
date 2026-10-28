# W43 r3 reader-to-print fidelity and citations

Source r3.5 `6f07cb49…` → r3 projection `63ad2617…` → r3 TeX `bb0e7e1d…` → PDF `d0fa8b56…` 483305B 22p.
r2→r3 body delta = 4 hunks only (title r3, POST restore, dup cleanup, TanStack 典拠 line). All else identical to r2.

## F-R3-01 POST restore (verified in print)

- Source L473 `` `POST /v1/decisions` `` → r3 projection code span preserved → TeX `\texttt{POST /v1/decisions}` → PDF p-18 `読み方：POST /v1/decisions に…` (300dpi confirmed).
- r1/r2 loss (`（保存済み一次資料…）`) eliminated. Validator P-API-route PASS; N-API-deleted correctly FAILs mutant.

## F-R3-02 URL hygiene (verified in print)

- Body URL now `\url{https://developers.openai.com/api/docs/guides/decisions}` + `（観測2026-10-25、snapshot…）` as text (PDF p-18 confirms blue link ends before `（`).
- TeX scan: 34 http `\url`, 0 with JP punctuation (validator P-url-hygiene PASS; N-malformed-url detects injection).
- SHA hex rendered as `\nolinkurl` (breakable, no false hyperlink); 0 Overfull final.

## Body parity otherwise

- 20 headers / 80 rows (78+2) / 3 figs / 29 claim literals / 5 recap paras identical (validator P-* PASS; allowlist classes TITLE/TOKEN/PATH/DUP documented).
- TanStack 典拠 line added to p8-f2 (no ｜, row count unaffected); GH≠npm separation now exact-key traceable in print.

## Citations

- 36 bibitems complete sentences (r2 fix carried over, unchanged in r3). Tiers 5/24/0 preserved. Exact-vs-natural audit in `source-key-audit-r3.md` (18/15/2/1/0): material TanStack now exact-in-print; others traceable via explicit natural language + crosswalk without invented cites.
