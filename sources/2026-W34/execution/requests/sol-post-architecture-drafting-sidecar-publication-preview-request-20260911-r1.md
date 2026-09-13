# W34 Sol execution request — Human Architecture approval through Publication Preview readiness

Status: `EXECUTION_AUTHORITY / HUMAN_ARCHITECTURE_R3_APPROVED / DRAFTING_AND_READ_ONLY_SIDECAR_PILOT / STOP_BEFORE_PUBLICATION_PREVIEW_HUMAN_DECISION`

Date: `2026-09-11 JST`

## 1. Mission

Continue the existing W34 production branch only after canonically recording the Human Architecture Review r3 approval.

Normal successful path:

```text
ARCHITECTURE_ESTABLISHED / Human Architecture Review pending
-> record exact Human APPROVED r3
-> Drafting + Profile Synthesis
-> DRAFT_COMPLETE
-> reader/publication validation + PDF
-> VALIDATED_DRAFT
-> Publication Boundary Validator read-only sidecar
-> Publication Candidate
-> RELEASE_CANDIDATE
-> Authority Auditor read-only production sidecar
-> SOL_PUBLICATION_PREVIEW_REVIEW_READY
-> STOP
```

Do not make the Publication Preview Human decision.

## 2. Human Architecture approval authority

The Human explicitly approved the exact Architecture surface reviewed at repository commit:

`498e45b5648f418e346e1a171dc588494dacf716`

Tree:

`dd9b8957600a2cd73eff62c33e215a3b6783c670`

Human decision reference:

`sources/2026-W34/execution/reviews/w34-human-architecture-review-decision-20260911-r3.md`

Human identity:

`EaRiver`

Human reviewed_at:

`2026-09-11T11:06:00Z`

Expected Architecture Review revision:

`3`

Architecture approval must be recorded only through the canonical Core v2 Human Gate round-trip script. Do not hand-author the approval/state/index records.

Required canonical invocation semantics:

```bash
python scripts/survey_human_gate_v2.py \
  record-architecture-approval \
  --state sources/2026-W34/production-state.json \
  --expected-revision 3 \
  --reviewed-by EaRiver \
  --reviewed-at 2026-09-11T11:06:00Z \
  --review-reference sources/2026-W34/execution/reviews/w34-human-architecture-review-decision-20260911-r3.md \
  --reviewed-commit-sha 498e45b5648f418e346e1a171dc588494dacf716
```

If the current Core CLI differs syntactically, inspect the reviewed script and use the semantically equivalent canonical command. Do not emulate it manually.

After approval recording, verify at minimum:

- `sources/2026-W34/gates/architecture-approval.json` exists and binds the approved exact Architecture bytes;
- `sources/2026-W34/gates/reviews/approvals/architecture-r3.json` exists;
- `sources/2026-W34/gates/reviews/architecture-r3.json` is `APPROVED` and binds reviewed commit `498e45b5...`;
- `sources/2026-W34/gates/review-index.json` contains contiguous Architecture revisions r1/r2/r3;
- Production State records Architecture Review approved with canonical provenance;
- no Publication Preview approval is created.

Commit and non-force push this Human Gate transition as a distinct checkpoint before Drafting. Fresh remote read-back is mandatory.

## 3. Approved Architecture is immutable during Drafting

Canonical Architecture:

`sources/2026-W34/architecture-v2.json`

Approved editorial model:

- thesis: `agent executionのproductionization`
- 6 substantive packages + final `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW`
- 41 selected candidates retained exactly through approved Architecture
- target pages = 20
- max pages = 26

Packages:

1. `w34-agent-control-plane`
2. `w34-collaborative-agent-workflows-retrieval`
3. `w34-safety-security-governance`
4. `w34-model-economics-distribution`
5. `w34-creative-multimodal-production`
6. `w34-ecosystem-infrastructure-economics`
7. `w34-week-in-review`

Do not change:

- Discovery
- Screening
- Evidence
- Evidence Authority Supplement
- Edition Views
- Materiality
- Completeness
- Candidate Matrix
- Selection
- Architecture
- package ordering
- candidate placement
- page plan
- thesis

No fresh research is authorized merely to improve prose. Use accepted Evidence and approved Architecture boundaries. If Drafting reveals a genuine source/evidence contradiction that cannot be written safely, stop and return it to Sol rather than broadening research autonomously.

## 4. Drafting requirements

Run the canonical Core v2 Drafting / Profile Synthesis path to `DRAFT_COMPLETE`.

Draft in Japanese for reader-facing publication.

Required editorial behavior:

- do not convert PRIMARY/SUPPORTING into article-count quota;
- preserve all source-specific limitations from Evidence/Architecture where they matter to claims;
- vendor performance/safety/economic claims remain attributed;
- do not use internal statuses, pipeline terminology, Sol/Muse review language, HOLD/SELECTED labels, execution paths, hashes, or rebuttal prose in reader-facing text;
- do not backdate post-cutoff/re-dated sources;
- Grok Bot Aug 21/Aug 26 chronology boundary must survive;
- OpenAI API regional processing belongs to Model Economics & Distribution, not retrieval/tool orchestration;
- final `w34-week-in-review` is cross-package synthesis and must not invent new factual claims outside accepted Evidence;
- selected supporting candidates with PARTIAL Evidence remain bounded and must not be silently upgraded to VERIFIED-style prose.

Use the current reviewed Core's canonical Draft Package validation. Do not bypass validation because the final synthesis package has no direct Architecture destination; current Core explicitly supports one final cross-package synthesis package.

After reaching `DRAFT_COMPLETE`, commit, non-force push, and fresh remote read-back before proceeding.

## 5. Reader/publication validation

Proceed through the canonical `DRAFT_COMPLETE -> VALIDATED_DRAFT` stage.

Expected canonical reader/publication artifacts include the current Core equivalents of:

- reader manuscript
- `surveys/weekly/2026-W34/main.tex`
- `surveys/weekly/2026-W34/main.pdf`
- quality regression bundle
- semantic editorial review
- visual review

The rendered publication must remain within the approved Architecture's target/max-page policy unless Core validation itself permits a bounded reason. Do not silently drop approved content to force page count.

If canonical semantic/visual/quality validation fails, stop and report the exact failure. Do not proceed to sidecar or Publication Candidate on an invalid draft.

After `VALIDATED_DRAFT`, commit, non-force push, and fresh remote read-back.

## 6. Read-only sidecar pilot A — Publication Boundary Validator

Pinned tool authority:

Repository:

`eariver/publication-boundary-redteam`

Exact tool SHA:

`7b9de2105c690daaafa6698c1791d51ca84a92c0`

This is a read-only second opinion, not Survey Production Core authority.

Use a temporary checkout outside the Survey repository. Verify tool HEAD == exact pinned SHA before use. Do not commit or push to the tool repository.

Run the validator against the actual W34 reader-facing TeX after `VALIDATED_DRAFT`, using the Weekly profile and JSON output, semantically equivalent to:

```bash
publication-boundary-scan surveys/weekly/2026-W34/main.tex --profile weekly --format json
```

Store the resulting non-authoritative report under:

`sources/2026-W34/execution/luna/w34-post-architecture-drafting-sidecars/`

The report must record:

- pinned tool SHA
- scanned W34 source SHA-256
- tool exit status
- aggregate status (`PASS`, `NEEDS_REVIEW`, or `FAIL`)
- HARD_FAIL / REVIEW_REQUIRED / INFO counts
- exact findings

Handling:

- `PASS`: continue.
- `NEEDS_REVIEW`: stop before Publication Candidate and return to Sol for semantic review.
- `FAIL` or any HARD_FAIL: stop before Publication Candidate and return to Sol.

Do not auto-edit reader-facing text in response to sidecar findings unless Sol later authorizes a bounded correction.

## 7. Mandatory feedback after sidecar A

Immediately after first real W34 use of Publication Boundary Validator, create:

`sources/2026-W34/execution/luna/w34-post-architecture-drafting-sidecars/feedback-publication-boundary-redteam.md`

This feedback is for the tool author and must include:

- exact tool SHA
- exact W34 artifact tested
- installation/CLI usability
- execution time/resource behavior observed if available
- useful findings
- false positives / false negatives suspected
- confusing output or missing context
- whether the PASS/NEEDS_REVIEW/FAIL model is operationally useful
- recommended tool improvements
- whether the tool should remain non-authoritative sidecar or appears ready for tighter integration

Do not modify the sidecar tool repository.

## 8. Publication Candidate

Only if canonical validation and Publication Boundary Validator sidecar are acceptable (`PASS`), run the canonical `VALIDATED_DRAFT -> RELEASE_CANDIDATE` Publication Candidate stage.

Do not create Human approval.

Commit, non-force push, and fresh remote read-back.

## 9. Read-only sidecar pilot B — Core v2 Authority Auditor

Pinned tool authority:

Repository:

`eariver/survey-core-v2-authority-auditor`

Exact tool SHA:

`c5f09d463b21c914d9c59b34597858f6182fc244`

This pinned version contains the W34 read-only production adapter.

Use a temporary checkout outside the Survey repository. Verify tool HEAD == exact pinned SHA before use. Do not commit or push to the tool repository.

Run against the actual Survey checkout only after Publication Candidate / `RELEASE_CANDIDATE` exists, semantically equivalent to:

```bash
python -m core_v2_authority_auditor.cli audit-production \
  --survey-repo /path/to/japanese-generative-ai-survey-checkout \
  --issue-id 2026-W34 \
  --json /tmp/w34-authority-audit.json \
  --markdown /tmp/w34-authority-audit.md
```

Copy/store the resulting non-authoritative reports under:

`sources/2026-W34/execution/luna/w34-post-architecture-drafting-sidecars/`

Record:

- pinned auditor SHA
- surveyed W34 remote HEAD/tree
- Production State SHA-256
- Publication Candidate SHA-256
- auditor exit status
- overall PASS/FAIL
- invariant findings
- explicit reminder that PARTIAL invariants remain non-authoritative limitations

Handling:

- PASS: continue to final Sol handoff.
- FAIL / ambiguous blocking finding: do not invent a repair. Stop at current `RELEASE_CANDIDATE` and return exact findings to Sol.

## 10. Mandatory feedback after sidecar B

Create:

`sources/2026-W34/execution/luna/w34-post-architecture-drafting-sidecars/feedback-survey-core-v2-authority-auditor.md`

Include:

- exact tool SHA
- exact W34 production surface audited
- setup/CLI usability
- runtime/resource behavior
- useful invariants/findings
- false positives / missing invariants suspected
- usefulness of W34 production adapter
- clarity of FULL/PARTIAL/non-authoritative boundaries
- recommended improvements
- whether the tool should remain read-only sidecar or appears suitable for tighter future integration

Do not modify the auditor repository.

## 11. 8GB RAM environment safety

OpenCode runtime is Ubuntu with 8GB RAM.

Use sequential execution. Do not hold large PDF/body/JSON corpora concurrently.

Before memory-heavy phases, lightweight `free -h` observation is allowed.

Do not modify OS/swap/system settings with sudo.

Prefer durable commits at the phase boundaries specified above so an OpenCode/OOM interruption loses minimal work.

## 12. Write and branch discipline

- existing branch only;
- no new/fallback/repair/review branch;
- no force push;
- no rebase/reset/history rewrite;
- normal forward commits only;
- recheck remote parent immediately before every write;
- fresh remote read-back after every push;
- no shared-Core edits during W34 production;
- if a shared-Core defect is encountered, record it edition-locally and stop.

## 13. Execution identity

Record:

`Execution agent: Muse Spark 1.3`

`Execution mode: EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION`

## 14. Successful terminal state

Successful terminal state for this request is:

- Architecture Human Gate = approved with revision 3 exact provenance
- Draft = passed
- Validation = passed
- lifecycle = `RELEASE_CANDIDATE`
- Publication Preview = pending
- freeze/release = pending
- Publication Boundary Validator sidecar completed and acceptable
- Authority Auditor sidecar completed and acceptable
- both feedback Markdown files created
- no Publication Preview Human decision generated

Required terminal marker:

`SOL_PUBLICATION_PREVIEW_REVIEW_READY`

At that marker, STOP.

Sol will independently review the actual reader-facing publication, PDF, semantic/visual reviews, Publication Candidate, sidecar reports, and feedback before presenting the Publication Preview Human Gate.
