# Survey Production Core v2 — Redesign implementation worklog

Status: `IMPLEMENTATION SUBSTANTIALLY COMPLETE / REGRESSION REPAIR + FIXED-HEAD AUDIT PENDING`  
Started: 2026-08-23 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft PR: `#446`  
Authority: `docs/survey-production-core-v2-redesign-authority.md`  
Design audit: `docs/survey-production-core-v2-redesign-preimplementation-audit.md`

## Purpose

This log records the actual Core v2 redesign implementation work performed after the W33/SP001 production-validation failure and the subsequent pre-implementation design audit.

It is an implementation worklog, not production-edition provenance. W33/SP001 remain failed production-validation evidence and must not be rewritten to look like successful runs.

## Operating rules

- Follow the audited redesign authority and Actions responsibility policy.
- Keep shared Core, Research Profile, Publication Profile, and edition/series authority orthogonal.
- Do not overfit implementation to W33/SP001 topic structure.
- GitHub Actions may remain only for clearly advantageous deterministic/reproducible/security-sensitive work; authoring/editorial reasoning belongs to ChatGPT.
- Preserve exact provenance, Human Gates, Publication Candidate byte identity, Freeze/Release integrity, and historical Evidence rigor.
- Record material implementation decisions, changed responsibility boundaries, regression coverage, and validation results here. Do not record every tool call.

## Planned implementation workstreams

1. Responsibility / orchestration simplification
2. Reader-facing Publication Boundary
3. Editorial / semantic / visual QA separation
4. Publication Candidate atomic revision/finalization
5. Edition execution-record bootstrap support
6. Grok single-task-file / Drive-path handoff cleanup
7. Regression + cross-profile compatibility validation
8. Fixed-head final audit

## 2026-08-23 — implementation start

### Starting state

- W33 and SP001 real-production validation are treated as failed Core v2 acceptance evidence.
- Pre-implementation redesign audit completed and design-level inconsistencies were corrected before implementation.
- Normal Human Gates remain `ARCHITECTURE_REVIEW` and `PUBLICATION_PREVIEW`.
- `refactor/survey-production-core-v2` remains the canonical redesign branch.

### Runtime synchronization before code changes

The canonical redesign branch initially still represented the pre-pilot Core snapshot plus redesign documentation, while current `main` had accumulated 111 commits during W33/SP001 production. Those commits contained the exact runtime paths that failed in real production, including interactive Drafting/Synthesis, Selection/Architecture, semantic-publication/quality, work-branch control, Weekly publication rendering, LONGFORM renderer/style repairs and related tests.

Redesigning only the older snapshot would therefore have produced a false repair target.

The branch histories were reconciled explicitly:

- prior redesign head: `e4794648589d32bbffbaafa29fdb58e26b86f55e`;
- current production `main`: `198c69703dba7b4f2f7b1d914d88f72bf7d7d887`;
- merge base: `a009ad28c2c2ed61ab90022a93b23eb053cadb3b`;
- an explicit merge tree adopted current `main` runtime wholesale and overlaid only the audited redesign authority/plan/policy/worklog files;
- canonical redesign merge commit: `5812c5761ed5e94bda503bf522dba96299255250`.

This makes the failed real-production runtime the implementation baseline while preserving the redesign history as the other merge parent.

PR #445 records the synchronization operation. It is not an edition-production execution trigger.

### Initial workflow inventory observation

The synchronized `.github/workflows/` tree confirmed extensive production mutation in Actions: `prepare-*`, `apply-*`, `revise-*`, interactive Drafting/Evidence/Selection/Semantic Publication/Semantic Quality, work-branch state control and cadence-specific layout/pagination repair workflows.

The redesign therefore established the rule that Actions is a deterministic executor/verifier rather than a research/editorial/publication-authoring agent.

### Initial Publication Boundary observation

The synchronized W33 renderer directly demonstrated the #433/#434 defect by carrying internal Evidence/materiality/profile-synthesis vocabulary into reader-facing output and treating internal Draft bytes as publication authority. LONGFORM publication similarly depended on a workflow-owned structured revision path.

Those failure modes became concrete regressions for the redesigned reader-facing boundary.

## 2026-08-23 — reader-facing Publication Boundary implemented

The publication path was redesigned around an explicit reader-facing manuscript/source boundary.

Implemented properties:

- Draft/Profile artifacts no longer act as a fallback publication source.
- Reader Manuscript is explicit publication input authority.
- Semantic/editorial review binds exact reader source bytes before Publication Preview.
- Visual review binds the exact rendered PDF before Publication Preview.
- Quality Regression Bundle owns deterministic QA only; agent semantic/visual PASS rows cannot impersonate deterministic results.
- Publication Candidate atomically binds Reader Manuscript, source, exact repository-resident PDF, deterministic QA, semantic/editorial review and visual review.
- Candidate becomes `READY_FOR_PUBLICATION_PREVIEW` only after those authorities agree.
- PDF/source byte change invalidates downstream Candidate/Preview/Freeze identity.
- Weekly, Retrospective Period, Thematic and LONGFORM_SPECIAL semantics remain Profile-owned rather than being flattened into one edition-specific schema.

The design intentionally keeps Human Publication Preview as review of exact candidate bytes, not another workflow-authored semantic gate.

## 2026-08-23 — Production/Core responsibility boundary implemented

`AGENTS.md` and `docs/survey-production-core-v2-session-bootstrap.md` now distinguish edition production from shared-Core maintenance.

Edition production may repair edition-local/transient issues autonomously, but shared Core roots are read-only during a production run. A shared defect is recorded under `sources/<issue>/execution/defects/`; a safe edition-local workaround may allow continued production, otherwise the run terminates/blocks rather than debugging Core in-place.

This directly closes the W33/SP001 ambiguity where “autonomous repair” could be interpreted as permission for the edition session to author generic Core changes.

## 2026-08-23 — GitHub Actions production authority removed

Canonical `workflow_control` was reduced so ordinary lifecycle stages are local ChatGPT + deterministic-script operations. `FROZEN -> RELEASED` is the only `WORKFLOW_DISPATCH` stage.

Major workflow reductions:

- `53f73386b86b2cb08ea1d03572787c9352f31205`: removed 11 Core-v2 production-mutation/request/control workflows.
- `1bd3c45b975a0ffea7bd09352624bd18cf4b488f`: removed obsolete focused contract workflows that duplicated tests or asserted retired mutation topology.
- `46818916547d91602fdbf42a293509fa1def49fd`: removed the remaining historical authoring/mutation/layout-repair/gate/release/pipeline workflow topology.

The intended final Actions surface is six workflows only:

1. `pipeline-contract-tests.yml`
2. `survey-production-v2-ci.yml`
3. `build-weekly-survey.yml`
4. `build-special-pdf.yml`
5. `survey-production-v2-export-publication-preview.yml`
6. `survey-production-v2-release.yml`

`tests/test_survey_pilot_bootstrap_v2.py` now treats that six-workflow set as a Core invariant.

## 2026-08-23 — reproducible build and preview transport boundaries simplified

`build-special-pdf.yml` was converted from a write-capable legacy lifecycle workflow into read-only reproducible build verification:

- no `pipeline-state.json` mutation;
- no lifecycle advancement;
- no bot commit/push;
- no editorial page-target/ceiling enforcement;
- build audit reports source/profile/PDF identity, bytes, page count and TeX findings.

Weekly build remains read-only.

Publication Preview export now resolves/validates one exact `publication-candidate-v2.json` and transports the exact Candidate-bound repository PDF. The old `interactive-preview-export.json` request artifact is gone.

Core v2 CI was simplified to compile all `scripts/survey_*_v2.py`, discover all `tests/test_survey_*_v2.py`, parse Core JSON contracts, and run on both the redesign branch and `main`.

## 2026-08-23 — Grok/X handoff simplified

PFB-001/PFB-002 were implemented as one self-contained run task:

```text
Grok_X_SourseIntake/<category>/<edition>/<run-id>/
  grok-task.md
  <result>.md
```

The X manifest now binds:

- exact `drive_task_path`;
- one repository `task` authority and SHA-256;
- result folder/filename;
- imported Raw bytes and downstream disposition.

Separate `grok-instruction.md` / `grok-prompt.md` authorities were removed. The Human passes only the exact Drive `grok-task.md` path/reference. Connector discovery is explicitly outside the expected production architecture.

## 2026-08-23 — edition execution record implemented

Added `scripts/survey_execution_record_v2.py` and `tests/test_survey_execution_record_v2.py`.

The helper owns structure only:

```text
sources/<issue>/execution/
  index.md
  sessions/<session-id>.md
  reviews/
  defects/
```

It initializes the standard tree from exact Profile/State/commit inputs and validates headings, Profile identity, canonical State pointer, and session-index continuity. It does not infer research/editorial content, Human decisions or defect classification and does not mutate Production State.

`docs/survey-production-core-v2-execution-record-policy.md` is now marked implemented in the redesign candidate.

## 2026-08-23 — regression repair during implementation

Implementation CI caught and corrected several redesign-process regressions without restoring obsolete architecture:

- Core contract authority additions initially were absent from sparse checkout; Core CI checkout was made contract-complete.
- old tests expected semantic rows in the deterministic Quality Bundle; tests were updated to the new QA split.
- old bootstrap tests required pilot-only W33/SP001 CLI wording in the live bootstrap; historical validation was separated from current production bootstrap authority.
- a test edit accidentally replaced current Review Finding/Repair Set fixture shape with an old shape; the current schema fixture was restored.
- a Weekly bibliography regression imported `pytest` unnecessarily; converted to standard `unittest`.
- old Special page-budget tests expected Actions to enforce editorial page budgets; they were rewritten to require read-only reporting instead.
- the execution-record helper initially referenced a non-canonical State validator; it was corrected to use `survey_agent_control_v2.validate_agent_state`.

At redesign head `1bd3c45b975a0ffea7bd09352624bd18cf4b488f`, both `Pipeline contract tests` and `Survey Production Core v2 CI` were observed PASS before the final legacy workflow reduction. The post-reduction tree must be revalidated from its later exact head; the earlier PASS is implementation evidence, not final-audit evidence.

## Remaining work before candidate freeze

1. Run full regression after the six-workflow reduction and repair only genuine stale expectations/invariants.
2. Synchronize redesign authority/plan/backlog wording with implemented behavior where still marked proposed/deferred.
3. Inspect the complete PR diff for accidental compatibility or scope regressions.
4. Freeze one candidate head SHA only after all intended candidate changes and CI repair are complete.
5. Run the complete six-point acceptance audit from zero on that exact unchanged SHA.
6. If any audit point requires a tree change, invalidate the audit, repair, freeze a new SHA and rerun all six points.
7. Only after unchanged six-point PASS present that exact candidate SHA for Human full-candidate review of Draft PR #446.
