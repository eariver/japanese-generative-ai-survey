# W41 reader-surface preflight (formal pre-processing + lexical lint, no semantic)

Date: 2026-10-14 JST
Manifest: `sources/2026-W41/publication/v2/reader-manuscript-v2.json` (validated, rebuilt after layout fix)
Primary: `surveys/weekly/2026-W41/main.tex`
Status: `PREFLIGHT_EDITORIAL_PROOF` (not a formal gate PASS)

## Frozen Core contracts checked (read-only, `774dd39a`)

- `scripts/survey_reader_publication_v2.py`: ChatGPT authors reader source directly;
  `build_manuscript_manifest` binds exact bytes + Architecture/approval/Profile,
  enforces 27/27 coverage identity + `FINAL_SYNTHESIS`/`WEEKLY_COMMUNITY_MOVEMENT`,
  runs fidelity (NOT_APPLICABLE for WEEKLY_MAGAZINE) + lexical lint.
  No semantic PASS required for manifest.
- `scripts/survey_reader_surface_gate_v2.py`: lexical lint (11 rules, BLOCKING)
  scans TeX/bib/coverage details; formal `evaluate_reader_surface_gate` requires
  independently validated persisted semantic authority (`READER_PIPELINE_INDEPENDENCE`,
  digest + surface-SHA bound, no synthetic PASS).
- Conclusion: manuscript + lexical lint + local LuaLaTeX editorial proof are allowed
  before formal review; formal Candidate assembly, semantic/visual review records,
  surface-gate PASS, and Human decisions require independent authority and are NOT
  performed here.

## Formal pre-processing validation (no semantic required)

- `validate_manuscript_manifest` (issue `2026-W41`): PASS (27 coverage, 2 requirements,
  SHA/byte_count bound, rebuilt after layout fix to exact current TeX bytes).
- Architecture/approval/Profile identity + SHA binding: PASS.
- Primary must be `survey_root/main.tex`: PASS.
- No duplicate source paths: PASS.

## Lexical lint (independent-semantic-review-free scope)

- `scan_tex_file` on `main.tex` + 10 section files: 0 BLOCKING (11/11 files).
- `scan_bib_file` on `references.bib`: 0 BLOCKING.
- Coverage/requirement details: 0 BLOCKING (pre-checked before manifest build).
- Masks applied for `%` comments + `\label`/`\cite`/`\Needspace`/`\input` etc.
  (citation keys and cross-ref labels do not trigger).
- W40-precedent public-ledger bare filename retained (no `sources/`/`surveys/` prefix).

## Independent semantic review authority

- NONE EXISTS. No `reader-surface-semantic-review-v2` record on disk for W41.
- No SHA/target to match; nothing used. No synthetic PASS generated.
- `build_semantic_authority` without persisted review would raise; not invoked.

## Formal gate / Human decisions

- `evaluate_reader_surface_gate`: NOT invoked (would fail closed without semantic authority).
- No `reader-surface-gate-v2.json` written; no PASS recorded.
- No publication-review `SEMANTIC_EDITORIAL`/`VISUAL` records written; no PASS recorded.
- No `RECORD_PUBLICATION_PREVIEW_APPROVAL`, no Freeze/Release/merge (all prohibited by mission).

## Editorial proof PDF (distinct from formal Candidate)

- LuaLaTeX + Biber build of exact manifest-bound TeX bytes: SUCCESS (17 pages).
- Output `surveys/weekly/2026-W41/main.pdf` + `main.pdf.sha256` marked
  `UNAPPROVED_EDITORIAL_PROOF` (see QA record); NOT a Candidate-bound reviewed PDF.
- Layout fixes in same run (meaning unchanged, manifest rebuilt + revalidated):
  tables `[h]`→`[htbp]`, `\Needspace{10\baselineskip}` before final subsection
  (W40 precedent). No semantic re-review triggered by layout (no wording changed
  except recorded P1/t1 cross-ref naturalization, already covered).

(End of file)
