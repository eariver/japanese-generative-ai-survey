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
- Full Core contract (`test_survey_*_v2.py`, all 51 modules, per-module chunks with `TMPDIR` on home disk because `/tmp` tmpfs pressure stalled git-heavy tests): **318 tests, 0 failures, 6 intentional skips**.
  - chunk_00: 38 OK; chunk_01: 70 OK; chunk_02: 52 OK (6 skipped); chunk_03: 55 OK (human_gate 5, interactive 5, operator_invalidation 24, operator_workflow 5, orchestrator_provenance 1, orchestrator_v2 + pdf_inspection 15); chunk_04: 71 OK; chunk_05: 32 OK.
  - The 6 skips are explicit legacy-Handoff audit/compatibility skips (`test_survey_handoff_request_v2`, `test_survey_handoff_v2`), pre-existing and unrelated.
  - `python3 -m compileall -q scripts tests`: OK; one pre-existing `SyntaxWarning` in untouched `scripts/normalize_special_legacy_partial_enums.py` (invalid escape `\_`), present on reviewed main, unrelated.
  - `test_survey_human_gate_v2` / `test_survey_operator_invalidation_v2` are slow here (git-subprocess-heavy; 38 s and 149 s single-module runs) but green; neither imports the repaired module (verified by grep: no `weekly_semantic_publication` in their import chains), so no causal link to this repair is possible.
  - No test file other than `tests/test_survey_semantic_publication_v2.py` was modified; no failures concealed.

## 15. Disposable W34 reproduction (read-only fixture, no remote W34 writes) — DONE

Fixture: local detached worktree `/tmp/opencode/w34-repro` at W34 HEAD `c1703f77...` (local git metadata only; never committed, never pushed). Candidate renderer temporarily copied over the worktree's byte-identical pre-fix file (SHA `e7de616a...` verified before overwrite). Disposable driver `/tmp/opencode/w34-bib-regen-driver.py` (outside any repo, not committed).

Pre-existing boundary finding (no edition-local repair performed): renderer `main()` / `_records_from_authorities()` cannot run end-to-end on the W34 tree because `sources/2026-W34/discovery/discovery-accepted-v2.json` uses the root `w34-gapfill-*` namespace (369 rows) while Matrix (409 rows), Evidence acceptance, Ledger, Draft packages and synthesis spec all use the effective `w34-event-*` namespace. The failing function is byte-identical pre/post fix and the failure precedes any `_bib_text` call, so this predates the repair and is unrelated to the note-leak defect. W34 tree also contains no `validated-source-manifest.json` / `interactive-semantic-publication-input.json` (artifacts were authored via the drafting-agent flow, not this renderer). Recorded for Sol (section 19); not repaired here per scope/STOP rules.

Repair-boundary verification (existing validated inputs only): 7 architecture-ordered packages -> spec deck/block dids, deduped -> **41 cited dids**; Evidence/Materiality/HOLD-bar cross-checks PASS for all 41 against Evidence acceptance `8437905d...`, Matrix and Ledger; regenerated keys == committed bib keys **41/41 in order**; `urldate 2026-08-21` consistent; byte delta (327 -> 286 lines) = exactly 41 `note` lines removed (40x VERIFIED/MATERIAL + 1x PARTIAL/MATERIAL on `w2026w34w34eventc055` CoSnitch, authority-consistent) + 41 `urldate` comma normalizations, nothing else changed; leak check (prescribed pattern via `grep -P`, `rg` unavailable) **0 matches** vs baseline 41; stdlib BibTeX check (41 `@online`, unique keys, fields exactly `[title, author, url, urldate]`, braces balanced); 7 package dirs untouched; no lifecycle/Human advancement, no Candidate creation.

PDF build: **environmentally impossible here** (no latexmk/lualatex/biber, no docker; CI uses texlive 2026 action). Delta-safety: only the optional biblatex `note` field removed from a CI-green bib (run `34669447838`, 12 pages); field removal cannot introduce undefined references, missing characters, or overfull boxes. Exact PDF rebuild deferred to CI on the pushed branch / Sol review.

Plan: local disposable clone/worktree of W34 HEAD `c1703f77...` (SUPERSEDED by the DONE record above; the canonical full-`main()` regeneration proved impossible for the pre-existing Discovery-namespace reason documented there, so verification was performed on the exact repair boundary instead, with no edition-local repair and no invented production commands).

## 16. Sidecar reproduction (Publication Boundary Validator) — DONE (plan line retained below for audit)

- Pinned tool `eariver/publication-boundary-redteam` freshly cloned outside the Survey repo at `/tmp/opencode/pb-redteam`; HEAD `== 7b9de2105c690daaafa6698c1791d51ca84a92c0` (clean status).
- Scan inputs `/tmp/opencode/w34-validator-input/surveys/weekly/2026-W34/`: unchanged W34 `main.tex` + `sections/*.tex`, regenerated `references.bib` (SHA `1d3fecf3...`).
- Command (pilot-equivalent): `PYTHONPATH=<redteam>/src python3 -m publication_boundary.cli main.tex sections/*.tex references.bib --profile weekly --format json`.
- Result: aggregate `NEEDS_REVIEW` (exit 1), 11 targets (10 PASS / 1 NEEDS_REVIEW / 0 FAIL), 1 finding total (0 HARD_FAIL).
  - `references.bib` = **PASS**, 0 findings: `RULE-BIB-INTERNAL-TAG-LEAK` 0, `RULE-TERM-CORE-EVIDENCE-NOTE` 0, `RULE-TERM-CORE-V2` 0, `RULE-TERM-MATERIALITY-FIELD` 0. All four acceptance conditions met.
  - Before/after: `FAIL` 164 HARD_FAIL + 1 REVIEW_REQUIRED (165 findings) -> `NEEDS_REVIEW` 0 HARD_FAIL + 1 REVIEW_REQUIRED (1 finding).
  - Residual: the known `sections/20-agent-workflows.tex` `RULE-BOUNDARY-MISSING-EXPECTED-FRAMING` REVIEW_REQUIRED persists by design (Mistral-reported prose; publication text untouched per non-goals). Its presence is not repair failure.
- Raw output retained at `/tmp/opencode/w34-validator-output.json` (disposable, outside repo).

Plan: disposable checkout of `eariver/publication-boundary-redteam@7b9de2105c690daaafa6698c1791d51ca84a92c0` outside the Survey repo; scan disposable regenerated `main.tex`, `sections/*.tex`, `references.bib` as in pilot. Acceptance: `references.bib` PASS, bibliography HARD_FAIL 0, `RULE-BIB-INTERNAL-TAG-LEAK` 0, `RULE-TERM-CORE-EVIDENCE-NOTE` 0, `RULE-TERM-CORE-V2` 0, `RULE-TERM-MATERIALITY-FIELD` 0. Known `sections/20-agent-workflows.tex` `RULE-BOUNDARY-MISSING-EXPECTED-FRAMING` REVIEW_REQUIRED (Mistral-reported prose) is out of scope and must remain untouched; its presence is not repair failure.

## 17. Exact-head CI

- Local exact-head equivalent at candidate HEAD: full Core contract `test_survey_*_v2.py` (318 tests, 0 failures, 6 intentional legacy skips) + `compileall` OK — see section 14.
- Remote CI (`survey-production-v2-ci.yml`, `pipeline-contract-tests.yml`, weekly build) runs on push of the maintenance branch; status to be recorded after push (read-back step). No candidate mutation after CI green except the worklog finalization commits recorded in section 18; if any further change becomes necessary, CI must be re-run.

## 18. Candidate commit SHA/tree

- Code freeze candidate (pushed, remote read-back match confirmed):
  - commit `66cb9fc4e26be37b0d99113988cc065fd07e0438`
  - tree `72e9cfb7ab522a779d15ccb519397d7e8f1e9a85`
  - parent `e4eddfbde3eb409bb758157e2abf16d5e0ebe0d2` (fix commit; grandparent = reviewed main `005e5984...`)
  - changed paths vs reviewed main (exactly the 3 allowed): `scripts/survey_weekly_semantic_publication_v2.py`, `tests/test_survey_semantic_publication_v2.py`, `docs/checkpoints/core-v2-weekly-bibliography-publication-boundary-repair-20260912.md`
  - remote read-back: `git ls-remote` returns `66cb9fc4...` for the maintenance branch — match.
- This section itself is finalized in a worklog-only closeout commit on top (no code/test changes after the freeze above); final HEAD + remote read-back recorded in section 20 return data. Remote CI re-runs on each push; worklog-only delta does not affect contract verdicts (section 14 ran at the frozen code bytes).

## 19. Residual limitations

1. `sections/20-agent-workflows.tex` `RULE-BOUNDARY-MISSING-EXPECTED-FRAMING` REVIEW_REQUIRED persists by design (section 16); validator remains a non-authoritative second opinion.
2. Local PDF rebuild impossible (no TeX toolchain); exact-PDF verification deferred to branch CI / Sol review (section 15 delta-safety argument).
3. Pre-existing observation for Sol (out of scope, not repaired): `_records_from_authorities()` joins the Candidate Matrix against root-namespace `discovery-accepted-v2.json`, but W34's Matrix uses the effective `w34-event-*` namespace (DERIVED_EXPANSION), so full renderer `main()` cannot run on the W34 tree. Any future end-to-end use of this renderer on expansion-basis editions needs a reviewed Core decision on effective-basis resolution in the publication path — separate maintenance, not this repair.
4. Environment substitutions recorded, none affecting verdicts: `pytest` -> repo-contract `unittest`; `rg` -> `grep -P` (identical PCRE); `TMPDIR` on home disk for git-heavy tests (`/tmp` tmpfs pressure).

## 20. Sol review readiness

`READY_FOR_SOL_FIXED_HEAD_REVIEW` (to be confirmed with final SHA/tree in section 18 after push + read-back). No merges, no W34/main writes beyond the maintenance branch, no Human decisions generated, no Publication Candidate created.

## 21. Pre-freeze authority reconciliation (Sol `PREFREEZE_REPAIR_REQUIRED_CURRENT_CORE_AUTHORITY_SYNC`)

Sol accepted the bibliography implementation direction/scope but blocked freeze: `docs/survey-production-core-v2-authority.md` and `docs/checkpoints/survey-production-core-v2-worklog.md` still named stale current `main`/branch/PR (`d54f9c7b...`, 20260907 governance branch, PR #484 / `2adcffdc...`, 20260905 branch).

Bounded repair on this same branch, bibliography code/tests byte-identical (verified pre-commit):
- `docs/survey-production-core-v2-authority.md`: current `main@005e5984...` / tree `25f65fa9...`; PRs #484–487 as merged history; current branch + draft PR #488; pre-freeze (not frozen, no PASS, no approval) state; W34 read-only `c1703f77...`, no Candidate created.
- `docs/checkpoints/survey-production-core-v2-worklog.md`: same synchronization (status/branch/PRs/main/W34/no-Candidate); prior SHAs retained as historical evidence.
- Other docs inspected: dated `docs/checkpoints/2026-09-0*` records are historical execution evidence (preserved); `docs/survey-production-core-v2-improvement-plan.md` and `docs/survey-production-core-v2-production-feedback-backlog.md` carry stale program/track headers of the same textual class, but synchronizing them to bibliography-repair authority would misattribute program ownership — left for Sol disposition, explicitly not rewritten here.
- This section is the bounded reconciliation checkpoint. Fresh exact-head/PR-merge-context CI required for the replacement candidate; `8bb3f42a...` runs are diagnostic/historical after mutation. No freeze, no seven-point audit, no Human approval request, no merge in this task.

## 22. Active authority-chain reconciliation (Sol `PREFREEZE_REPAIR_REQUIRED_ACTIVE_AUTHORITY_CHAIN_SYNC`)

First synchronization was incomplete: Sol re-review of `fb257a11...` (CI green: `34682551155` / `34682551160` SUCCESS) found the authority index + worklog correct, but two further precedence-chain documents still carried false current-facing state.

Bounded repair on this same branch, bibliography code/test byte-identical (`8de06a60...` / `4dcddb0c...`, verified pre-commit):
- `docs/survey-production-core-v2-improvement-plan.md`: current-facing header synchronized to `main@005e5984...` / tree `25f65fa9...`, current branch, draft PR #488, PRE-AUDIT CANDIDATE / PRE-FREEZE with no PASS, no approval, not merged, W34 read-only with no Candidate; §14 rollout boundary now names PRs #310/#452/#483–#487 historical and PR #488 as the open review surface. Program body narrative and historical repair-phase references preserved; the plan was not rewritten into a bibliography design document.
- `docs/survey-production-core-v2-session-bootstrap.md`: status synchronized to `CANONICAL POST-INTEGRATION AGENT-FIRST SESSION BOOTSTRAP / SOL-LUNA REVIEW GOVERNANCE INTEGRATED` (governance integrated via PR #485, no longer REVIEW PENDING). Document kept generic across Weekly/Retrospective/Thematic/guided Special work; no bibliography-specific semantics added.
- Sweep of the remaining precedence/map chain: governance (two Human Gates, unchanged), final-audit rule / checklist / x-source-intake (no current branch/main/PR claims), agent-first re-audit `Working branch` (dated 2026-08-22 execution context, not a current-branch claim — preserved), foundations memo (no current claims), dated checkpoints (historical evidence — preserved), production-feedback backlog (not in precedence/map; historical track — preserved per Sol). No additional path changed.
- Fresh exact-head/PR-merge-context CI required for the replacement candidate; `fb257a11...` runs become diagnostic/historical after mutation. No freeze, no seven-point audit, no Human approval request, no Human decision, no merge in this task. No seven-point PASS claimed.
