# W43 Core-free preview r1 — build commands and limitations

Status: `EDITION_LOCAL / UNVALIDATED / PDF_PROOF_ONLY`.
Starting HEAD/Tree: `fa4235…` / `bf5582b2…` (remote-verified, ff-only from `bc6b1c…`).

## Exact commands (exit codes)

- `python3 sources/2026-W43/execution/editorial-bypass/w43-r3-5-strict-semantic-claim-join-check.py` → exit 0, `EDITION_LOCAL_ROW_JOIN_PASS`, 24/24 negatives, T1 20 headers PASS, T2 80 bijection PASS, C 29 semantic PASS, T5 anchors PASS.
- `lualatex --interaction=nonstopmode -output-directory=sources/2026-W43/execution/core-free-preview-r1 sources/2026-W43/execution/core-free-preview-r1/main.tex` (run 1) → exit 0, 22 pages, 0 Illegal/Errors; 1 Overfull (68pt, URL+SHA line) fixed in v2.
- Same `lualatex` (run 2, TOC stable) → exit 0, 22 pages, 0 Illegal, 0 Overfull, 0 Errors.
- After metadata detokenize fix (underscores preserved), two more runs → exit 0, 22 pages, 480229 bytes, 0 warnings.
- `pdftoppm -png -r 150 …/main.pdf …/pages/p` → exit 0, 22 PNGs `p-01.png`..`p-22.png`.
- Python PIL 12.1.1 contact sheets (batches 8/8/6) → exit 0, 3 sheets.
- `pdfinfo …/main.pdf` → Title `Japanese Generative AI Technical Survey – 2026-W43`, Subject/Keywords `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF`, Creator LuaLaTeX, Producer LuaTeX-1.24.0, Pages 22, A4, 1.7.

Compiler: LuaHBTeX 1.24.0 (TeX Live 2026), format lualatex 2026.10.8, jlreq 10pt single-column, geometry 18mm, HaranoAji fonts, Noto CJK JP available.

## Build warnings

Final `main.log`: 0 Illegal unit, 0 Overfull, 0 Errors. Early v1 had 4× Illegal (figure `\\[..]` → fixed to `\par`) and 1× Overfull 68pt (bare URL + hex SHA → fixed via URL trimming + hex `\url`). Fixed errors recorded in QA; final build clean.

## Honest limitations (not erased)

- Source intake not re-fetched; no independent benchmark rerun; 65-page MemT equations/ablation not fully read; wet-lab unconfirmed; red-team vendor-described.
- `1.86x` stays `SOURCE_UNVERIFIED` (paper-derived AUTHOR_CLAIM, no saved README line); `66x` is storage-capacity only.
- Patch stage4 preparation vs stage5 post-patch guidance; Daybreak/checker outside; CVE unidentified ≠ absent.
- FLUX FAQ `Two at launch` stays UNRESOLVED (source/version/time unidentified); `+47/+50` not unified; `26.5x/96.2%` not cited as true.
- Voxtral TTS language counts unresolved; AA originals unfetched; 11-language sample ≠ coverage.
- Decisions example is official guide illustrative excerpt, NOT_RUN; TTL 30m is Oct25 observation, not W43 fact.
- TanStack GH `15:18:14Z` vs npm `15:21:49Z` kept separate; npm body `RAW_NOT_ARCHIVED`; blog day-only not product clock; Metrics OUT, Grok NEVER_STORY (rendered as 当週の対象外).
- DeepSeek MIT vendor-declared; artifact LICENSE bytes/SHA not retrieved; local execution none.
- 22 pages honest (cover 1, TOC 1, body 18, bib 2) vs Architecture approx target 38/max 44/estimate ~37. Consistent with W42 final 21 pages. Architecture page_plan itself says target is estimate not guarantee and forbids padding. No padding applied. Sol adjudicates volume.

## What was NOT done

No `scripts/`, `schemas/`, `config/`, `.github/`, main, Frozen Core, Production State, Architecture, Selection, Evidence, Human Gates edits. No new branch, no Stage, no Freeze/Release, no force, no PR/merge. `.aux/.toc/.out` excluded from git; only `main.log` kept.
