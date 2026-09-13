# Core v2 Bibliography Access Provenance Repair — Canonical Worklog

Maintenance branch: `fix/core-v2-bibliography-access-provenance-20260913`
Authority: `EXECUTION_AUTHORITY / SHARED_CORE_DEFECT_CONFIRMED_BY_W34_ISSUE_491 / WEEKLY_AND_SPECIAL_BIBLIOGRAPHY_ACCESS_PROVENANCE_REPAIR / STOP_AT_HUMAN_FULL_CANDIDATE_REVIEW` (2026-09-13 JST)
Reviewed main SHA: `79a0ddea948af18ef02ec63184e67f99ad7f8e09`
Reviewed main tree: `5534594bfc172044a7b8bbd685f0c9fef016e78b`
W34 read-only fixture branch: `weekly/2026-W34-v2-work`
W34 HEAD: `6f68fd09955302fd87e5ec0ce77ff06ccaec8448`
W34 tree: `0d7b504729ff62c92a223cf4ffb2fe63ced874f0`

---

## 1. Defect Authority & Context

- **Issue Reference**: Confirmed by W34 Issue #491.
- **Defect Description**:
  Current publication generators (`scripts/survey_weekly_semantic_publication_v2.py` and `scripts/run_semantic_publication_v2_interactive_base.py`) serialized edition temporal cutoffs (`display_date` / rolling window cutoff / retrospective `as_of`) into BibTeX `urldate`, instead of the actual canonical retrieval/access date (`accessed_at`) of each cited source.
  This caused reader-facing `visited on` dates in the compiled PDF bibliography to misrepresent source access provenance (e.g. indicating an article was visited on the edition cutoff date rather than the date it was actually retrieved by researchers).
- **Scope**:
  - Affects both Weekly (`WEEKLY_MAGAZINE`) and Special (`LONGFORM_SPECIAL`) publication paths.
  - W34 production artifacts remain read-only fixtures and are not modified in this maintenance branch.

---

## 2. Start Guards Verification

All start guards were verified prior to write operations:
1. Reviewed `main` HEAD: `79a0ddea948af18ef02ec63184e67f99ad7f8e09` — PASS (`git rev-parse HEAD`).
2. Expected `main` tree: `5534594bfc172044a7b8bbd685f0c9fef016e78b` — PASS (`git rev-parse HEAD^{tree}`).
3. Remote W34 fixture HEAD: `6f68fd09955302fd87e5ec0ce77ff06ccaec8448` — PASS (`git ls-remote origin weekly/2026-W34-v2-work`).
4. Remote W34 fixture tree: `0d7b504729ff62c92a223cf4ffb2fe63ced874f0` — PASS (`git rev-parse 6f68fd09955302fd87e5ec0ce77ff06ccaec8448^{tree}`).
5. Maintenance branch absent from remote before push — PASS (`git ls-remote origin fix/core-v2-bibliography-access-provenance-20260913` empty).

---

## 3. Root Cause Analysis

- **Weekly Publication Path** (`scripts/survey_weekly_semantic_publication_v2.py`):
  `_window(profile)` computed `(display_date, boundary, display_date)` where the third tuple item was used as a single `urldate` for all cited entries in the bibliography (`bib = "\n\n".join(_bib_text(..., urldate) for did in cited)`).
  This collapsed every cited bibliography entry's `urldate` to the rolling window cutoff wall-time.
- **Special Publication Path** (`scripts/run_semantic_publication_v2_interactive_base.py`):
  `urldate` was derived as `profile["research_scope"]["temporal_policy"]["as_of"][:10]` and passed identically to all entries (`bib = "\n\n".join(_bib_text(..., urldate) for d in cited)`).
  This collapsed every cited bibliography entry's `urldate` to the retrospective `as_of` date.
- **Ground Truth Evidence Invariant**:
  In accepted Evidence cards (`results/*.json`) and interactive evidence payloads, each source entry explicitly records its own canonical `accessed_at` timestamp (ISO-8601 instant, e.g. `2026-09-08T14:52:53Z` or `2026-08-24T17:24:00Z`).
  The publication generators discarded this granular provenance in favor of the edition-wide cutoff.

---

## 4. Architecture & Implementation

### A. Shared Provenance Helper (`scripts/survey_bibliography_access_provenance_v2.py`)
Created a dedicated module providing:
- `parse_access_date(value: str) -> tuple[str, str]`:
  Validates ISO-8601 instant or date strings using `core.parse_instant` and `datetime.date.fromisoformat`. Returns `(full_timestamp, YYYY-MM-DD)`. Fails closed on invalid or blank timestamps.
- `resolve_source_access_provenance(sources, canonical_url, did, explicit_source_id=None) -> dict[str, Any]`:
  - Enforces URL matching against the canonical bibliography URL.
  - Handles single-source and multi-source cards.
  - Multi-capture / ambiguous provenance rule: if multiple captures share the URL with different access dates, requires unambiguous resolution via `explicit_source_id`, or fails closed.
  - Missing-date rule: if `accessed_at` is missing or blank, fails closed with an actionable error identifying Discovery ID and source.
  - Returns `{"source_id", "source_accessed_at", "urldate", "source"}`.
- `load_evidence_sources(acceptance_path: Path) -> dict[str, dict[str, Any]]`:
  Loads sources mapped by Discovery ID from `evidence-accepted.json` (supporting `results`, card JSON files in `results/<filename>`, embedded `card`/`evidence_card`, and `interactive-evidence.json` source bindings).

### B. Weekly Publication Generator (`scripts/survey_weekly_semantic_publication_v2.py`)
- Updated `_window(profile) -> tuple[str, str]` (removed `urldate` from window return value).
- Updated `_bib_text(key, record, urldate=None)`: accepts per-record `urldate` or derives it from `source_accessed_at`/`accessed_at`; fails closed if missing.
- Updated `_records_from_authorities`: loads evidence sources via `provenance_resolver.load_evidence_sources(acceptance_path)`, resolves access provenance for each cited discovery row, and records `source_accessed_at` and `urldate` in `records[did]`.
- Updated `main()`: passes `records[did]["urldate"]` to `_bib_text` and writes `source_accessed_at` to `quality/subject-entity-property-binding.json`.

### C. Special Publication Generator (`scripts/run_semantic_publication_v2_interactive_base.py`)
- Imported `provenance_resolver`.
- Updated `_bib_text(key, record, urldate=None)`: validates canonical access date; fails closed if missing.
- Updated `main()`: resolves canonical source access provenance for all cited entries; removes `urldate = profile["as_of"][:10]` assignment; passes per-record `urldate` to `_bib_text`; records `source_accessed_at` in `quality/subject-entity-property-binding.json`.

---

## 5. Verification & Regression Coverage

### Mandatory Test Contracts (B1–B9)
Implemented in [`tests/test_survey_bibliography_access_provenance_v2.py`](file:///home/eariver/git/jgas-core-fix/tests/test_survey_bibliography_access_provenance_v2.py):
- **B1**: Weekly publication binds per-source access date, distinct from edition cutoff.
- **B2**: Special publication binds per-source access date, distinct from retrospective `as_of`.
- **B3**: Multiple sources in the same publication retain independent per-source `urldate` values.
- **B4**: Published/event date differs from retrieval/access date; `urldate` binds access date, not event date.
- **B5**: Revised page chronology (c066 class: event Aug 21, page re-dated Aug 26, canonical access Sep 8 -> `urldate` Sep 8).
- **B6**: Missing or blank access timestamp fails closed with actionable error.
- **B7**: Ambiguous access provenance fails closed unless explicitly disambiguated.
- **B8**: Citation keys, URL, title, organization, status, materiality, and citation ordering remain unchanged.
- **B9**: Fixture compatibility:
  - W34 read-only fixture regression verifies all 41 references resolve to canonical access on `2026-09-08` and proves `w34-event-c066` repair (`2026-09-08` vs old `2026-08-21`).
  - SP001 read-only fixture regression verifies all 11 accepted evidence sources resolve to `2026-08-24T17:24:00Z` and `urldate` `2026-08-24`.

### Test Suite Execution
- `python3 -m unittest tests/test_survey_bibliography_access_provenance_v2.py -v`: 14/14 PASS (0.019s).
- `python3 -m unittest discover -s tests -p 'test_survey_*_v2.py'`: 364/364 PASS (skipped=6).
- `python3 -m compileall -q scripts tests`: PASS (0 errors).
- JSON syntax validation for `config/` and `schemas/`: PASS.
