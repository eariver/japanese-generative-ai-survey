# W41 reader-surface preflight r16 (formal pre-processing + lexical lint, no semantic)

Date: 2026-10-14 JST
Manifest: `sources/2026-W41/publication/v2/reader-manuscript-v2.json` (validated)
Primary: `surveys/weekly/2026-W41/main.tex`
Status: `PREFLIGHT_EDITORIAL_PROOF` (not a formal gate PASS)

## Frozen Core contracts checked (read-only)

- `survey_reader_publication_v2`: authoring + manifest binding + 27/27 identity +
  FINAL_SYNTHESIS/WEEKLY_COMMUNITY_MOVEMENT + fidelity (NOT_APPLICABLE for
  WEEKLY_MAGAZINE) + lexical lint. No semantic PASS required for manifest.
- `survey_reader_surface_gate_v2`: 11 lexical rules (BLOCKING) + formal gate
  requiring persisted independent semantic authority (no synthetic PASS).
- Conclusion: r16 manuscript + lint + local editorial proof allowed pre-review;
  Candidate assembly, semantic/visual PASS, surface-gate PASS, and Human
  decisions require independent authority and are NOT performed here.

## Formal pre-processing validation (no semantic required)

- `validate_manuscript_manifest` (issue `2026-W41`): PASS (27 coverage,
  2 requirements with corrected Section 7/8 locations, SHA/byte_count bound).
- Architecture/approval/Profile identity + SHA binding: PASS.
- Primary is `survey_root/main.tex`: PASS. No duplicate source paths: PASS.

## Lexical lint (independent-semantic-review-free scope)

- `scan_tex_file` on `main.tex` + 10 sections: 0 BLOCKING.
- `scan_bib_file` on `references.bib` (20 entries, fixed titles/dates): 0 BLOCKING.
- Coverage/requirement details (r16): 0 BLOCKING.
- M06 residuals re-scanned (`triage|一次読み|取得済み|text excluded`): none in
  reader body (bib uses bounded announcement language).

## Independent semantic review authority

- NONE EXISTS. No persisted `reader-surface-semantic-review-v2` record for W41r16.
- Nothing used; nothing synthesized. `build_semantic_authority` not invoked.
- Explicit audit matters left for semantic review: supplement S1 adoptability
  (Haiku rows/unit beyond Card), community negative-space analysis adequacy,
  bib title/date bases per `bibliography-audit-r16.md`.

## Formal gate / Human decisions

- `evaluate_reader_surface_gate`: NOT invoked. No gate record written; no PASS.
- No publication-review records written; no PASS. No preview approval, Freeze,
  or Release (all prohibited).

## Editorial proof PDF (distinct from formal Candidate)

- LuaLaTeX + Biber rebuild of exact manifest-bound r16 bytes: SUCCESS (17 pages).
- Output `surveys/weekly/2026-W41/main.pdf` + `main.pdf.sha256` marked
  `UNAPPROVED_EDITORIAL_PROOF` (see pdf-qa-r16); NOT Candidate-bound.
- Layout: tables `[htbp]` + `\Needspace` retained; no claim changes from layout.

(End of file)
