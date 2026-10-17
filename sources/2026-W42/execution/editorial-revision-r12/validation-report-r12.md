# W42 r12 validation report (frozen validators + invariants + TeX proof)

Date: 2026-10-18 JST. No Core/shared-root/main change. No canonical overwrite. No stage transition.

## Frozen CLI validations (all PASS, real receipts)

- `survey_drafting_v2_base.py draft-check` (canonical package × r12 proposal): P1–P7 all `{"passed": true, "errors": []}` (schema, identity, stable refs, attribution, must-cover, boundaries).
- Proposal SHAs (v12.0, REVISED): P1 `4fbe46d4…`, P2 `4202538d…`, P3 `f6922662…`, P4 `c0489707…`, P5 `d759fe99…`, P6 `70c11a11…`, P7 `a270abff…`; 7 tables, 7 notes.
- `synthesis-input` built via frozen CLI from the 7 proposal pairs; proposed synthesis result written; `synthesis-check` `passed: true`.
- `validate_agent_state`: PASS (checked at bridge time; State untouched since).

## F01/F02 gate status

- F01 RESOLVED: LFM terms = publisher operative terms (no full-file claim); Beam = no custom badge BUT full Apache 2.0 conditions preserved; tables/notes aligned; artifact-scope qualifiers added. Programmatic scan for banned phrasings (`表示義務なし`, `条文全文が確認できる`, `何でもできる`, `OSI承認は本号`) returns zero.
- F02 RESOLVED: `narrowed_source_urls` 100% external http(s) (zero non-http rows of 106); bundle-sourced refs dropped from all proposal blocks (4 claims); q5-08 converted to editorial framing; Nipah sentence converted to explicit non-use stance; one accepted-context annotation split into URL + `accepted_context_notes` (accepted bytes untouched).

## Reader preview fidelity

- `reader-preview-r12.PROPOSED.json`: 92 paragraphs / 21,281 body chars / 7 tables / 7 notes; zero CLAIM_BOUNDARY; zero machine-trace/Hangul/simplified ghosts; single documented named-term exception (`SRFT`).
- TeX body = exact preview block copies (same generator objects); `block-diff-r11-r12.json` maps r11→r12.

## Canonical invariants (all preserved)

- `production-state.json`: DRAFT_COMPLETE, architecture approved, publication pending (SHA unchanged).
- Draft checkpoint `ARCHITECTURE_ESTABLISHED.json`, approval, review index, r1 record/snapshot: unchanged.
- Canonical Draft Results/Packages/Synthesis (v10.0): SHAs unchanged (read-only inputs).
- Accepted Evidence/Views/Materiality/Selection/Architecture: untouched. No TeX in canonical paths; Publication Preview not started.

## TeX/PDF proof (non-canonical, edition-local only)

- `execution/preview-r12/main.tex` (552→471 lines) + `preview.sty` (documented biblatex deviation) → `main.pdf` 16 pages, 419,471 bytes, LuaLaTeX/TexLive2026.
- Log clean (0 overfull/underfull/missing-char/warning). All 16 pages rendered + visually inspected (see build manifest). No padding; final page intentionally partial and flagged.
