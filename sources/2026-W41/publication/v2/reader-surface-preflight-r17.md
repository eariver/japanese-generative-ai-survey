# W41 reader-surface preflight r17 (formal pre-processing + lexical lint, no semantic)

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

## Formal pre-processing validation (no semantic required)

- `validate_manuscript_manifest` (issue `2026-W41`): PASS (27 coverage,
  2 requirements with Section 7/8 locations, SHA/byte_count bound).
- Architecture/approval/Profile identity + SHA binding: PASS.
- Primary is `survey_root/main.tex`: PASS. No duplicate source paths: PASS.

## Lexical lint (independent-semantic-review-free scope)

- `scan_tex_file` on `main.tex` + 10 sections: 0 BLOCKING (r17 comment carries
  no prohibited vocabulary; `$\le$` math is masked as structural).
- `scan_bib_file` on `references.bib` (20 entries): 0 BLOCKING.
- Coverage/requirement details (r17): 0 BLOCKING.

## Independent semantic review authority

- NONE EXISTS. Nothing used; nothing synthesized.
- Explicit audit matters left: S17-1 prompt-length/5m-1h adoptability, S17-2
  Gemini new-source authority, community analysis adequacy, bib bases per
  `bibliography-audit-r17.md`.

## Formal gate / Human decisions

- `evaluate_reader_surface_gate`: NOT invoked. No gate record; no PASS.
- No publication-review records; no PASS. No preview approval, Freeze, Release.

## Editorial proof PDF (distinct from formal Candidate)

- LuaLaTeX + Biber rebuild of exact manifest-bound r17 bytes: SUCCESS (17 pages).
- `main.pdf` + `main.pdf.sha256` marked `UNAPPROVED_EDITORIAL_PROOF`
  (see pdf-qa-r17); NOT Candidate-bound. No claim changes from layout.

(End of file)
