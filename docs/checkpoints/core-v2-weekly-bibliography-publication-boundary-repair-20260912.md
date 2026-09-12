# Core v2 Weekly bibliography publication-boundary repair — canonical worklog

Maintenance branch: `fix/core-v2-weekly-bibliography-publication-boundary-20260912`
Authority: `EXECUTION_AUTHORITY / SHARED_CORE_MAINTENANCE / WEEKLY_BIBLIOGRAPHY_PUBLICATION_BOUNDARY_REPAIR` (2026-09-12 JST)
Reviewed main SHA: `005e59841272464307386abfc11f5b09228f0814`
Reviewed main tree: `25f65fa91abdb2d5fe601e4a66d3b38a585060d8`
W34 read-only fixture branch: `weekly/2026-W34-v2-work`
W34 HEAD: `c1703f772837317b81735cd4cc851c715fff1a3b`
W34 tree: `46baf8cf9f086f0842b3af22f37cef2707d5b563`
Role note: session runs as maintenance execution (Luna/Work equivalent); Sol review is a separate required step, not claimed here.

## 1. Defect authority

- W34 Publication Boundary sidecar (read-only, non-authoritative second opinion):
  - `sources/2026-W34/execution/luna/w34-post-architecture-drafting-sidecars/publication-boundary-scan-w34-report.md` (W34 HEAD `c1703f77...`)
  - `sources/2026-W34/execution/luna/w34-post-architecture-drafting-sidecars/publication-boundary-scan-w34.json`
  - `sources/2026-W34/execution/luna/w34-post-architecture-drafting-sidecars/feedback-publication-boundary-redteam.md`
- Tool: `eariver/publication-boundary-redteam@7b9de2105c690daaafa6698c1791d51ca84a92c0`, Weekly profile, exit 1, aggregate `FAIL`.
- Counts: 11 targets (9 PASS / 1 NEEDS_REVIEW / 1 FAIL); 165 findings = 164 HARD_FAIL + 1 REVIEW_REQUIRED.
- The 164 HARD_FAIL are `references.bib`-only: 41 entries x 4 rules each:
  - `RULE-BIB-INTERNAL-TAG-LEAK`
  - `RULE-TERM-CORE-EVIDENCE-NOTE`
  - `RULE-TERM-CORE-V2`
  - `RULE-TERM-MATERIALITY-FIELD`
  - all on `note = {Core v2 Evidence: VERIFIED; materiality: MATERIAL}` lines.
- The 1 REVIEW_REQUIRED is `sections/20-agent-workflows.tex` / `RULE-BOUNDARY-MISSING-EXPECTED-FRAMING` (Mistral-reported framing; out of scope, prose must not be touched for it).
- W34 `surveys/weekly/2026-W34/references.bib` (W34 fixture): 41 `@online` entries, 41 `Core v2 Evidence` note lines (verified via `git show` + `grep -c`).
- Defect class per W34 report: systematic shared-Core Weekly renderer defect, not W34 body defect; must be repaired on shared Core, not on the W34 branch.

## 2. Exact starting SHA/tree (maintenance branch creation)

- Created `fix/core-v2-weekly-bibliography-publication-boundary-20260912` from exact reviewed main `005e59841272464307386abfc11f5b09228f0814`.
- Post-creation verification: `HEAD == 005e5984...`, `HEAD^{tree} == 25f65fa9...`, `git diff origin/main...HEAD` empty.
- Remote maintenance branch confirmed absent before creation (`git ls-remote` empty).

## 3. Mandatory initial guards (pre-write, read-only; re-verified after session resume)

1. remote `main` HEAD `== 005e59841272464307386abfc11f5b09228f0814` — PASS (`git ls-remote origin main`).
2. remote `main` tree `== 25f65fa91abdb2d5fe601e4a66d3b38a585060d8` — PASS (`git rev-parse <sha>^{tree}` after fetch; `origin/main` rev-parse matches).
3. remote `weekly/2026-W34-v2-work` HEAD `== c1703f772837317b81735cd4cc851c715fff1a3b` — PASS.
4. remote W34 tree `== 46baf8cf9f086f0842b3af22f37cef2707d5b563` — PASS.
5. remote maintenance branch absent — PASS (empty `git ls-remote`; local branch also absent before creation).
- No repository/GitHub writes occurred before all five guards passed.
- After session interruption/resume: re-verified all five guards (same PASS results), confirmed still on the maintenance branch at `005e5984...` with clean status (only removed untracked `__pycache__`), remote maintenance branch still absent (no push yet).

## 4. Mandatory read-first (completed before code edit)

Current main (= maintenance branch start):

- `scripts/survey_weekly_semantic_publication_v2.py`
  - `_bib_text()` (lines 62-77): builds `@online` entry with `title`, `author`, `url`, `urldate`, plus `note = {Core v2 Evidence: <status>; materiality: <materiality>}` from `record["status"]` / `record["materiality"]`.
  - `_records_from_authorities()` (lines 163-258): Evidence-acceptance / Candidate-Matrix / Materiality-Ledger / accepted-Discovery cross-validation producing `records[did] = {entity: {canonical_name, canonical_url, organization: None}, status, materiality}` plus an `authority` binding dict. Must be preserved unchanged.
  - Bibliography / cite-key generation (`main()`, lines 476-481): `bib_key_by_did = {"w" + issue_id... + did...}`, `bib = "\n\n".join(_bib_text(...) for did in cited)`. Cite-key formula, ordering (`cited` order), and identity must be preserved.
- `tests/test_survey_semantic_publication_v2.py` (140 lines): existing `_window`, `_closing_summary`, `_validate_input`, and semantic-quality finalizer tests; no bibliography publication-boundary test yet.

W34 fixture (read-only via `git show c1703f77...:...`, no checkout, no writes):

- Sidecar report / JSON / feedback (see section 1).
- `surveys/weekly/2026-W34/references.bib`: head shows every entry ending with the leaking `note`; counts 41/41.
- `sources/2026-W34/production-state.json`: `lifecycle_state VALIDATED_DRAFT`, `next_action stage:publication-candidate`, architecture approved / preview pending; not to be advanced by this maintenance.
- Canonical production commands: W34 execution tree contains no `survey_weekly_semantic_publication` grep hits under `sources/2026-W34/execution`; the renderer invocation lives in the shared-Core canonical path (`scripts/survey_weekly_semantic_publication_v2.py main()` with `--repo-root/--state/--input`). No new analogous command will be invented; disposable W34 reproduction will reuse the existing validated-inputs regeneration pattern already exercised on W34 (`f6094a8f` TeX assembly, `e67de427` validation + PDF).

## 5. Exact defect reproduction (maintenance branch, pre-fix)

In-memory reproducer (no file writes) on maintenance HEAD `005e5984...`:

```python
from scripts.survey_weekly_semantic_publication_v2 import _bib_text
rec = {"entity": {"canonical_name": "Repro Title", "canonical_url": "https://example.com/x", "organization": "ExampleOrg"}, "status": "VERIFIED", "materiality": "MATERIAL"}
print(_bib_text("w2026w34testkey001", rec, "2026-08-21"))
```

Output (verbatim):

```bibtex
@online{w2026w34testkey001,
  title = {{Repro Title}},
  author = {{ExampleOrg}},
  url = {https://example.com/x},
  urldate = {2026-08-21},
  note = {Core v2 Evidence: VERIFIED; materiality: MATERIAL}
}
```

Substring checks (all `True`, i.e. leaking): `Core v2`, `Evidence:`, `VERIFIED`, `materiality`, `MATERIAL`, `note =`.
Matches the W34 artifact shape exactly (`note = {Core v2 Evidence: VERIFIED; materiality: MATERIAL}` on all 41 entries).

## 6. Root cause

`_bib_text()` in `scripts/survey_weekly_semantic_publication_v2.py` serializes the internal authority fields `record["status"]` (Evidence status) and `record["materiality"]` (Materiality disposition) directly into the reader-facing BibTeX `note` field with the literal internal framing `Core v2 Evidence: ...; materiality: ...`. Every cited record carries these fields (populated by `_records_from_authorities()` from Evidence acceptance + Materiality ledger), so every bibliography entry leaks internal lifecycle/state labels to readers. The validator's 4-rules x 41-entries = 164 HARD_FAIL is the mechanical consequence. Repository-internal provenance (manifests/ledgers/audit, `validated-source-manifest.json`, `subject-entity-property-binding.json`) is unaffected and stays; only the reader-facing serialization boundary is defective.

## 7. Repair design (preferred minimal repair per instruction)

- In `_bib_text()`: stop serializing `status` and `materiality`; remove the internal-metadata-only `note` field entirely.
- No reader-facing substitute `note` is introduced.
- Preserved exactly: BibTeX entry type (`@online`), cite key, source title, URL, `urldate`, existing author/organization rendering (`organization or "Unknown"`, brace escaping), source ordering, citation identity, `_records_from_authorities()` Evidence/Materiality authority validation, repository-internal provenance (manifests/ledgers/audit data still record `status`/`materiality`).
- Passing internal metadata *into* the renderer remains allowed; only serializing it to reader-facing BibTeX is removed.
- Not a regex post-filter on forbidden phrases: the `note` construction and its `status`/`materiality` reads are deleted at the source template.
- WEEKLY_MAGAZINE-only change; no Special/THEMATIC renderer touched.

## 8. Scope

Planned changed paths (max 3):

1. `scripts/survey_weekly_semantic_publication_v2.py` — `_bib_text()` minimal repair only.
2. `tests/test_survey_semantic_publication_v2.py` — bibliography publication-boundary regression test only.
3. `docs/checkpoints/core-v2-weekly-bibliography-publication-boundary-repair-20260912.md` — this canonical worklog (this file).

## 9. Explicit non-goals (will not do)

- No hand-edit of W34 `references.bib`; no W34 body changes; no Mistral prose changes.
- No Publication Boundary Validator changes.
- No Materiality/Evidence/Selection semantics changes.
- No source-identity or cite-key generation changes.
- No general bibliography title/URL/date/author policy revision; no `"Unknown"` author behavior change.
- No speculative Special-renderer changes.
- No regex special-case filter on forbidden phrases.
- No lifecycle/Human Gate advancement; no Publication Candidate creation; no Human approval generation; no merges (to `main` or W34); no PR merges.

## 10. Planned tests

- New regression in `tests/test_survey_semantic_publication_v2.py`: fixture record with `status = "VERIFIED"`, `materiality = "MATERIAL"` through `_bib_text()`; positive assertions (title, URL, urldate, cite key, `@online` structure remain) and negative assertions (`Core v2`, `Evidence:`, `VERIFIED`, `materiality`, `MATERIAL` absent). Proves leak-freedom for records carrying internal metadata, not a string-substitution check.
- Focused: `pytest -q tests/test_survey_semantic_publication_v2.py`.
- Broader: repository normal Core test contract / CI (exact command recorded at runtime).
- Unrelated pre-existing failures, if any, recorded without concealment.

## 11. Implementation result

- `scripts/survey_weekly_semantic_publication_v2.py` `_bib_text()`: deleted the `status`/`materiality` reads and the entire `note = {Core v2 Evidence: ...; materiality: ...}` line. `urldate` is now the final field (no trailing comma). Added a 2-line boundary comment stating internal Evidence/materiality authority stays in manifests/ledgers and must never serialize into BibTeX. No other renderer code touched: `_records_from_authorities()`, cite-key formula, ordering, `@online` type, title/URL/urldate/author rendering all byte-identical in behavior.
- `tests/test_survey_semantic_publication_v2.py`: added `test_bib_text_omits_internal_evidence_materiality` to `WeeklySemanticPublicationTests`. Fixture record carries `status = "VERIFIED"` + `materiality = "MATERIAL"` through `_bib_text()`; positive assertions (cite key, title, URL, urldate, `@online{key,` structure) and negative assertions (`Core v2`, `Evidence:`, `VERIFIED`, `materiality`, `MATERIAL` absent).
- Post-fix reproducer (same input as section 5) now emits:

```bibtex
@online{w2026w34testkey001,
  title = {{Repro Title}},
  author = {{ExampleOrg}},
  url = {https://example.com/x},
  urldate = {2026-08-21}
}
```

leak checks all `False`; preservation checks all `True`.

## 12. Actual changed paths

1. `scripts/survey_weekly_semantic_publication_v2.py` (`_bib_text()` only)
2. `tests/test_survey_semantic_publication_v2.py` (one regression test only)
3. `docs/checkpoints/core-v2-weekly-bibliography-publication-boundary-repair-20260912.md` (this file)

No other paths touched. `git status` shows only these (plus transient `__pycache__`, removed before commit).

## 13. Intermediate failures

- `pytest -q tests/test_survey_semantic_publication_v2.py` (as prescribed) not runnable here: `pytest` is not installed in this environment (`No module named pytest`). Used the repository CI contract instead: `python3 -m unittest tests.test_survey_semantic_publication_v2 -v` (CI runs `python -m unittest discover -s tests -p 'test_survey_*_v2.py' -v`). Recorded as environment fact, not a code failure.
- Full `test_survey_*_v2.py` discover did not complete inside a single 300 s tool window (no output captured; suite is ~150 modules including slow bridge/retry tests). Switched to (a) a targeted relevant subset immediately (section 14) and (b) chunked full-contract runs with per-chunk timeouts so every result is captured incrementally. No failure concealed; chunk log below.

## 14. Unit/regression test results

- Focused: `python3 -m unittest tests.test_survey_semantic_publication_v2 -v` — 5/5 OK (4 pre-existing + 1 new `test_bib_text_omits_internal_evidence_materiality`).
- Relevant subset: `test_survey_semantic_publication_v2 + test_survey_publication_v2 + test_merge_generated_bibliography + test_survey_reader_fidelity_v2 + test_weekly_pipeline` — 38/38 OK in 6.6 s.
- Full Core contract (`test_survey_*_v2.py` discover): chunked run results below (PENDING at time of writing; to be filled).

## 15. Disposable W34 reproduction (to be filled; read-only fixture, no remote W34 writes)

Plan: local disposable clone/worktree of W34 HEAD `c1703f77...`; temporarily apply maintenance candidate renderer change; regenerate publication artifacts from existing validated inputs via canonical commands; verify: bibliography entries = 41, citation identity = 41, cite keys unchanged, internal Evidence/materiality leakage = 0 (`rg -n 'Core v2|Evidence: (VERIFIED|PARTIAL)|materiality: (MATERIAL|CONTEXT)|SELECTED|HOLD' surveys/weekly/2026-W34` reader-facing matches attributable to repair = 0; audit/provenance-internal occurrences out of scope), PDF build PASS, canonical validation PASS, package identity remains 7, no lifecycle/Human advancement, no Candidate creation.

## 16. Sidecar reproduction (Publication Boundary Validator; to be filled)

Plan: disposable checkout of `eariver/publication-boundary-redteam@7b9de2105c690daaafa6698c1791d51ca84a92c0` outside the Survey repo; scan disposable regenerated `main.tex`, `sections/*.tex`, `references.bib` as in pilot. Acceptance: `references.bib` PASS, bibliography HARD_FAIL 0, `RULE-BIB-INTERNAL-TAG-LEAK` 0, `RULE-TERM-CORE-EVIDENCE-NOTE` 0, `RULE-TERM-CORE-V2` 0, `RULE-TERM-MATERIALITY-FIELD` 0. Known `sections/20-agent-workflows.tex` `RULE-BOUNDARY-MISSING-EXPECTED-FRAMING` REVIEW_REQUIRED (Mistral-reported prose) is out of scope and must remain untouched; its presence is not repair failure.

## 17. Exact-head CI (to be filled)

PENDING.

## 18. Candidate commit SHA/tree (to be filled)

PENDING.

## 19. Residual limitations (to be filled)

PENDING (anticipated: section-20 REVIEW_REQUIRED persists by design; validator stays non-authoritative).

## 20. Sol review readiness

PENDING. Final state target: `READY_FOR_SOL_FIXED_HEAD_REVIEW` with no merges, no W34/main writes beyond the maintenance branch, no Human decisions generated.
