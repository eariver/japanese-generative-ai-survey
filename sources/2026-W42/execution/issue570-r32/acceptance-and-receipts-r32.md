# W42 r32 Issue #570 — old/new manifest, acceptance matrix, receipts index

## Old → new (r31 → r32)

| Artifact | r31 (history) | r32 (current) |
|---|---|---|
| TeX | `008b6a27…` 97154 B | `e6d53d5a…` 97647 B (+493: L64 body + T1 cell + header provenance) |
| PDF | `02638611…` 505327 B, 21 pp | `827a93d8…` 505694 B, 21 pp (+367) |
| Reader file | r31 SHA (history) | rebuilt, primary binds new TeX |
| preview.sty | `f0492fb6…` unchanged | same bytes |

TeX delta (reader-facing): exactly L65 body sentence + L106 T1 Argon cell (plus `% r32` provenance comment, not typeset). Prices (2/10 → 4/20 11/30), dates (Oct 13 GA), examples (Chrome/Minecraft/Copilot), citations, P2–P7, T2–T7, bibliography (90 keys) byte-identical.

## Issue #570 Acceptance Criteria — results

- [x] Argon 1,048,576 as unified shared context frame, no unconditional-1M-output misreading. Body states shared frame + hop caps + budget reduction; table cell states shared frame + continuation condition.
- [x] Ordinary single-generation cap vs long-decode conditions distinguished in body (65,536; 32,768 REST; API/SDK long decode; remaining budget). Thinking rendered as co-tenant, not independent budget; 最大 (maximum) wording, no guaranteed-answer implication.
- [x] Table T1 Argon row consistent with body (compact unified-frame phrase, same numbers/conditions).
- [x] Existing prices/dates/evaluations/sources/numbers/other sections preserved (verified: P2–P7 identical, T2–T7 identical, bib 90 identical, cites same order, 28/28 selection intact).
- [x] Rebuilt PDF target + neighbor pages checked (worker viewed p02/p03/p04/p05; delta reviewer verified T1 placement + full page map by extraction): no header orphan, no table split, no clipped cells, no glyph loss, no unexpected blanks, page count 21 unchanged.
- [x] New exact reader-facing artifacts generated for formal Publication Preview. Human approval / Freeze / Release NOT performed (stopped at RELEASE_CANDIDATE pending).

## Receipts index (trusted GitHub Actions)

- Gate r2 revision: request-only commit + run + bot commit (see session for SHAs/URLs).
- Re-advance 1 (DRAFT_COMPLETE → VALIDATED_DRAFT): request-only + run + receipt + checkpoint.
- Re-advance 2 (VALIDATED_DRAFT → RELEASE_CANDIDATE): request-only (candidate only) + run + receipt + checkpoint.
- All preflights: operator-preflight + operator-execute success; remote read-back verified; no local CLI substitution.

## Residual limits

- Route A whitespace (accepted); Vals live-page drift beyond Oct-12 snapshot; ASPIRE README month-granularity; OpenAI-compat long decode unclaimed (no official passage found; TeX claims nothing).
