# Defect record — W36 r2 regeneration blocked by frozen-Core reader-surface suppression plumbing

- Date: `2026-09-17` (UTC run; JST wall clock 2026-09-17/18)
- Branch: `weekly/2026-W36-v2-work`
- State at block: `DRAFT_COMPLETE` / `stage:reader-publication-validation`
- Classification: `BLOCKING_SHARED_CORE_DEFECT` (edition-local repair complete; canonical regeneration cannot advance without Core change)
- Related: #434 (Publication Boundary gate family), #502 (community citation auditability), W36 Publication Preview r1 `REQUEST_CHANGES` (`sources/2026-W36/gates/reviews/publication-r1.json`, boundary `DRAFT_COMPLETE`)

## 1. Exact blocker

The mandated #502 immutable bibliography URL

```text
https://github.com/eariver/japanese-generative-ai-survey/blob/188f5acc0cfd97885e3b110b565a57d31e13ff3c/surveys/weekly/2026-W36/community-observation.md
```

in `surveys/weekly/2026-W36/references.bib` (`w36community`, line 35) trips exactly one BLOCKING finding in the frozen Core gate:

```text
[RSG-LEX-INTERNAL-PATHS] surveys/weekly/2026-W36/community-observation.md — Leaks repository internal surveys/ path into reader prose or URLs
```

The matched span is a substring of a public `https://github.com/.../blob/<full-SHA>/...` permalink — the very URL form the execution request mandates. The rule hint itself says "Use public web URLs"; the regex cannot distinguish a public permalink from a live internal path reference. This is a gate false positive on the required citation, distinct from the #434 false negative (gate PASSED r1 despite HOLD/PARTIAL leakage).

## 2. Why the designed remedy cannot take effect without Core modification

Core documents "a narrow, audited suppression mechanism" (`scripts/survey_reader_surface_gate_v2.py` module docstring) and auto-loads an edition file from `{source_root}/publication/v2/reader-surface-suppressions-v2.json` in `survey_reader_publication_v2._validate_manifest_semantics` and `build_reader_surface_gate`. That plumbing is broken in the frozen Core:

1. File loads go through `core.load_json`, which raises `ValueError: expected JSON object` for a JSON array file (the CLI help text itself says "Path to suppressions JSON array" — doc/code mismatch).
2. A JSON object file (e.g. `{"suppressions": [...]}`) loads but is consumed via `list(suppressions or [])`, which yields dict keys (`["suppressions"]`); `_is_suppressed` skips non-dict entries, so the suppression is silently inert. No code unwraps the `"suppressions"` key (verified by search).
3. Suppression works only when passed as a Python list directly to `build_manuscript_manifest(..., suppressions=[...])` and `evaluate_reader_surface_gate(..., suppressions=[...])` — the only shapes Core's own test (`tests/test_survey_reader_surface_gate_v2.py::test_narrow_allowlist_suppression_allows_pass`) exercises.
4. `build_review_record`, `validate_review_record`, and `validate_manuscript_manifest` callers inside the canonical path (`survey_stage_validation_v2.py` DRAFT_COMPLETE branch, `survey_agent_control_v2.py advance-stage`) expose no suppression passthrough, so canonical stage validation fails deterministically:

```text
ValueError: Pre-Publication Reader-Surface Gate FAILED: 1 blocking finding(s) detected:
[1] RSG-LEX-INTERNAL-PATHS at surveys/weekly/2026-W36/references.bib (Line 35, entry:w36community)
```

Empirically verified this run: direct-API suppression yields `SUPPRESSED/SUPPRESSED` with 0 unresolved blocking, and `evaluate_reader_surface_gate` returns `PASSED` (gate record `reader-surface-gate-v2.json` valid per `validate-gate`); the canonical `build_review_record` on identical bytes fails on the internal re-scan.

## 3. Ruled-out alternatives (no silent narrowing, no gate evasion)

- Dropping or weakening the blob URL: violates explicit Human requirement (#502 + execution request §9/§12, exact mandated form). Forbidden narrowing.
- Moving the manifest to a non-`surveys/` path: the execution request fixes the exact path/URL form; any repo permalink still matches `sources/`/`surveys/` patterns.
- Splitting/encoding the URL across lines or percent-encoding to dodge the regex: gate evasion, dishonest. Rejected.
- Hand-assembling review records around the builder: downstream canonical stage validation re-runs the same failing scan; `advance-stage` cannot pass. Bypassing stage validation is out of bounds.
- Modifying `scripts/`, `config/`, `schemas/`: prohibited by the execution contract (shared-Core freeze).

## 4. Completed edition-local work (committed, pushed)

- r1 `REQUEST_CHANGES` recorded canonically (`gates/reviews/publication-r1.json`, reviewed `c4ab0455`, boundary `DRAFT_COMPLETE`); Architecture r2 `APPROVED` preserved.
- `surveys/weekly/2026-W36/community-observation.md` created with exact 15 accepted X URLs (byte-identical to accepted ledger), committed alone as `188f5acc0cfd97885e3b110b565a57d31e13ff3c`, pushed; history preserved (no squash).
- Full reader-facing repair committed as `7a92004d5` (#434 boundary rewrite, #500 GLM boundary/no-same-week, #501 natural technical Japanese, #502 bib URL): all representative phrases verified absent; lexical `scan-file` PASS on all 10 TeX files.
- CI `build-weekly-survey` run `35229849238` success; new PDF pinned (`surveys/weekly/2026-W36/main.pdf`, 12 pages, 359906 bytes, SHA-256 `abbbe4eb48427ccaeb7cf65026f737cc9836a7393f24efb192e96fc02ac703f6`); PDF text extraction clean (no defect tokens, all sections present).
- Rebuilt and verified: `reader-manuscript-v2.json` (20/20 coverage, direct-API suppression), 3 deterministic checks + `quality-regression-bundle-v2.json`, `reader-surface-input-v2.json`, persisted `reader-surface-semantic-review-v2.json` (validated PASS), `reader-surface-gate-v2.json` (`PASSED`, 1 audited SUPPRESSED finding, `validate-gate` PASS).
- Edition-local audited suppression file `sources/2026-W36/publication/v2/reader-surface-suppressions-v2.json` (object shape; loads cleanly; inert through canonical builders per §2 — kept as audit record, not as a working bypass).

## 5. Not built (blocked)

- `semantic-editorial-review-v2.json`, `visual-review-v2.json` (review rows authored; canonical binder refuses to write).
- `publication-candidate-v2.json`, DRAFT_COMPLETE stage validation/advance, Preview r2 shell/dossier.

## 6. Resume guidance (after reviewed Core repair)

A reviewed Core fix should (a) make file-based suppressions effective (or thread suppressions through review builders/validators), and (b) add a regression test for a public permalink exemption. After repair, resume on this branch from `DRAFT_COMPLETE`: stage-validate, advance to `VALIDATED_DRAFT`, build candidate, advance to `RELEASE_CANDIDATE`, create Preview r2 shell (`PENDING`), STOP. Reused r2 bytes (manuscript/deterministics/bundle/surface/semantic-review/gate) remain valid provided TeX/Bib/PDF bytes are untouched; re-verify SHAs before use.

## 7. Shared-Core change accounting for this run

- Shared-Core changed paths: `0` (`.github/`, `config/`, `schemas/`, `scripts/`, `templates/`, `tests/`, `main`, `production/survey-core-v2` all untouched).
- No Grok/X intake, Discovery, Screening, Evidence, Materiality, Completeness, Selection, Architecture, approval, or Draft authority was altered (Draft freeze re-verified byte-identical).
