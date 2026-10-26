# W43 Core-free PDF Preview r1 — independent visual review request (PROPOSED, not a PASS)

To: Independent Sol (visual/semantic). From: Muse Worker. Date: 2026-10-26.
Status: `MUSE_W43_CORE_FREE_PDF_PREVIEW_R1_READY_FOR_SOL_VISUAL_REVIEW` (worker claim only).

## Fixed inputs for review (hash-pinned)

- Reader `6f07cb494938f0ea9db7f41b32fdd46f22ac0549bd7846b130f00b1cc5da46d6`, ledger `6fd9d6fe…`, manifest `85d94d74…` (exact bytes verified before print).
- Projection `e1a49da9…` (72862B), diff (title + 19 operator-token classes + internal-path neutralization, auditable via `diff -u`).
- TeX `0d8a8a09…` (897 lines, 20 tables / 3 figures / 36 bibitems), sty `28a663bc…`.
- PDF `fd88cb7c…` (480229B, 22 pages, A4, LuaLaTeX 1.24.0, Subject/Keywords `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF`, 0 warnings).
- Pages `p-01.png`..`p-22.png` (150dpi) + `contact-sheet-01..03.png` (see manifest for per-file SHA256 at commit time; verify after push via commit-pinned URLs).

## Scope (visual + print-fidelity only)

- Verify every PDF page image vs TeX vs projection vs r3.5 reader: table width/clipping, fonts/glyphs, floats/captions, code/URLs, near-empty/overfull, source notes, order, bibliography, P8→recap continuity, cross-page breaks.
- Verify 20/80/29 parity, 5-para recap after P8 (not P9), 19 placements, authority tiers (5 RAW / 24 QUALIFIED), and that no substantive claim/value/unit/comparator/provenance was altered in print projection.
- Confirm 22-page honest density (cover 1, TOC 1, body 18, bib 2) vs Architecture approx 38/max 44/estimate ~37 is acceptable without padding (W42 final 21 pages precedent; Architecture notes target is estimate not guarantee).

## Risks / open limitations (do NOT promote)

- Independent Sol did not run Python negatives itself; `claim_id/source_class` map not exhaustive; some raw snapshots unavailable; no reproduced benchmarks.
- COBOL 40%+ accepted-derived (ARCHIVE_UNAVAILABLE); npm body RAW_NOT_ARCHIVED; 1.86x SOURCE_UNVERIFIED; FLUX FAQ UNRESOLVED; Voxtral TTS unresolved; Decisions example NOT_RUN; DeepSeek MIT vendor-declared SHA unseen.
- Volume: honest 22 pages is 16 short of 38 target. Worker did NOT pad; Sol adjudicates whether VOLUME_OR_LAYOUT_REVIEW_REQUIRED or accept with W42 precedent.

## Explicit non-claims

No independent PASS, no Human Gate, no publication receipt, no Freeze/Release, no Stage advance is claimed or requested here. A separate independent semantic/visual PASS and explicit Human PDF approval are future decisions.

Please return independent findings as `2026…_SolReview.md` (or equivalent) with PASS_WITH_LIMITATIONS / REQUEST_CHANGES and exact HEAD/Tree verdict.
