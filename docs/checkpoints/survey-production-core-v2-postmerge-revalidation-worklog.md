# Survey Production Core v2 — Post-merge W33/SP001 revalidation worklog

Status: `REAL-PRODUCTION REVALIDATION PARTIALLY EXERCISED / CANONICAL CLI EXECUTION BLOCKED BY OPERATOR RUNTIME`

Established: 2026-08-23 JST

Integrated Core baseline: `2cb52dc293484a5c2ddd3caf9c909f18f4699c49`

Validation editions:

- Weekly: `weekly/2026-W33-v2-work`
- Thematic/LONGFORM regression: `special/SP001-v2-work`

Historical failed pre-redesign editions remain archived separately and are not acceptance evidence for this run.

## Purpose

This file is the cross-edition resume and feedback record for the **post-merge clean production revalidation** required after the Core v2 redesign.

It is not a Production State, Human Gate record, or substitute for edition-local canonical artifacts. Its purpose is to preserve what the W33/SP001 trial actually exercised, what remains unexecuted, and which findings should be considered for future Core/operator-flow maintenance.

Edition-local resume authorities:

- W33: `weekly/2026-W33-v2-work` / `sources/2026-W33/postmerge-validation-status.md`
- SP001: `special/SP001-v2-work` / `sources/SP001/postmerge-validation-status.md`

## Current overall position

The redesigned Core was merged after exact-head CI and fixed-head review. Clean W33 and SP001 work branches were reset to that integrated baseline while preserving the failed pre-redesign branches as archives.

The revalidation has exercised substantial **real operator work**, but has not completed the canonical lifecycle:

### W33 exercised successfully

- current Weekly time-window resolution;
- self-contained `grok-task.md` creation and Human-mediated Drive handoff;
- Grok execution against the exact task path;
- result return into the exact Drive run folder;
- exact result-byte retrieval and repository Raw import;
- X/community disposition discipline;
- ChatGPT primary-source follow-up;
- fresh editorial Architecture preparation.

W33 is currently blocked before canonical Profile/State/X-manifest/Discovery lifecycle execution.

### SP001 exercised successfully

- current backlog/scope authority lookup and clean scope materialization;
- Thematic X applicability reasoning (`NOT_REQUIRED` prepared);
- broad primary-source intake across DeepSeek/Qwen/GLM/Kimi and supporting families;
- explicit licensing/open-weight/runtime-distribution boundaries;
- complete seven-obligation editorial coverage plan;
- fresh six-package Architecture preparation.

SP001 is currently blocked before canonical Profile/State/Discovery lifecycle execution.

Neither edition may be counted as a post-integration production PASS until the integrated Core validators actually advance authoritative State to `ARCHITECTURE_ESTABLISHED` and stop at pending `ARCHITECTURE_REVIEW` without shared-Core repair.

## Revalidation finding RVF-001 — Human-mediated Grok/Drive transport works in real operation

Status: `CONFIRMED BY W33`

The redesigned single-task-file shape worked as intended:

```text
ChatGPT prepares exact Drive grok-task.md
-> Human gives Grok only that path/reference
-> Grok reads the exact task
-> Grok writes the result into the instructed run folder
-> ChatGPT retrieves exact result bytes
-> ChatGPT imports Raw and continues research
```

This validates the operational direction of PFB-001/PFB-002. No Grok connector is required for the normal boundary.

W33 exact task:

`Grok_X_SourseIntake/Weekly/2026-W33/weekly-x-2026-W33-postmerge-r1/grok-task.md`

Returned Raw repository authority:

`sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/raw/grok-x-result.md`

Raw SHA-256: `93fe6b8c2eeea4e3186868f79927108edacebc26d8ff23f1bcc38ac1080e1f06`

## Revalidation finding RVF-002 — X/community versus technical Evidence boundary works editorially

Status: `CONFIRMED EDITORIALLY / CANONICAL MANIFEST VALIDATION STILL PENDING`

The W33 Grok result contained a mixture of official announcements, hands-on tests, pricing narratives, benchmark commentary, local-inference reports and rumors. ChatGPT was able to treat this as **observation/discovery signal**, then re-verify material claims against first-party sources rather than promoting X assertions directly into technical Evidence.

This division should remain a Core/operator invariant:

- Grok/X answers what is salient, tested, discussed, disputed or practically constrained in the community;
- primary/authoritative sources establish technical facts;
- unsupported X details remain community observation or HOLD.

## Revalidation finding RVF-003 — fresh X can materially change Weekly Architecture

Status: `CONFIRMED BY W33`

The post-merge W33 X observation surfaced a concentrated Aug. 12–14 frontier/open-model release wave. Primary-source follow-up confirmed that Grok 4.6, Qwen3.8, Gemini 3.7 Flash and GLM-5.3 were all materially in-window.

This changed the editorial interpretation from an older three-feature-centered shape toward a broader system-level week involving:

- model release velocity;
- agentic/coding evaluation;
- local/open-weight deployment;
- serving/runtime co-evolution;
- governed high-risk capability;
- cost/pricing pressure.

Therefore Weekly X intake is not merely a decorative community section; it can change package selection and issue synthesis while still remaining outside technical fact authority.

## Revalidation finding RVF-004 — Thematic X applicability can legitimately be NOT_REQUIRED

Status: `CONFIRMED EDITORIALLY BY SP001 / CANONICAL RECORD PENDING`

For SP001, the technical-history question can be closed through technical reports, official repositories/model cards, API/distribution documentation and license/model artifacts. X is unlikely to change the core technical lineage/strategy Architecture enough to justify mandatory Grok transport.

This supports the current policy distinction:

- Weekly: X required by Profile;
- Thematic/Retrospective: ChatGPT decides applicability with rationale;
- Foundations-guided Thematic: dedicated category when X is materially useful.

The remaining requirement is to prove the `NOT_REQUIRED` decision through the canonical X manifest/profile path once CLI execution is available.

## Revalidation finding RVF-005 — operator runtime bridge is now the blocking production dependency

Status: `NEW / UNRESOLVED`

The redesign intentionally removed research/editorial lifecycle mutation from GitHub Actions. That responsibility correctly returned to ChatGPT + local deterministic Core scripts.

However, the current ChatGPT runtime has the following split capability:

- GitHub connector can read/write files and inspect commits, trees, blobs and Actions;
- the local shell/container is not backed by a mounted checkout of the connected repository;
- the local container cannot directly fetch the repository from GitHub network access;
- connector-returned repository bytes cannot currently be bridged into the shell as a working tree;
- retained Actions intentionally do not provide a research/editorial lifecycle runner.

Result: ChatGPT can perform research and repository mutation through the connector, but cannot legally execute the canonical local Core CLI over the edition branch.

Classification for these trials: `TRANSIENT_EXECUTION / OPERATOR-RUNTIME CAPABILITY`, not yet a shared-Core defect.

### Flow implication

The redesigned architecture needs an **operator execution path**, but that does not imply restoring Actions as a production authoring worker.

Future maintenance should evaluate a minimal, generic bridge such as one of these categories:

1. a supported repository checkout/mount available to the ChatGPT execution runtime;
2. a connector operation that materializes an exact branch/commit into the local execution filesystem;
3. another reviewed deterministic remote-execution bridge that runs the existing canonical CLI without adding editorial/reasoning responsibility to Actions.

The solution must preserve:

- exact commit/branch identity;
- local Core script authority;
- no hidden authoring logic in CI;
- no edition-specific temporary workflow;
- reproducible output/provenance;
- fail-closed handling of shared-Core defects.

This should become a Core/operator-platform maintenance item before PFB-013 can be closed as real-production PASS.

## Revalidation finding RVF-006 — do not fabricate machine acceptance when execution is unavailable

Status: `CONFIRMED OPERATIONAL RULE`

During both editions, sufficient information existed to manually compose plausible `production-profile.json`, `production-state.json`, X manifests and downstream artifacts. Doing so would have made the trial appear successful while bypassing the exact validators being tested.

Therefore the revalidation deliberately stopped at the execution boundary.

Future production sessions should retain this rule:

> If the canonical machine path cannot be executed, preserve preparation and provenance, classify the blocker, and stop short of machine acceptance rather than manually imitating validator output.

## Revalidation finding RVF-007 — edition-local resume records remain useful even before canonical execution records exist

Status: `CONFIRMED / TEMPORARY COMPATIBILITY PRACTICE`

The redesigned Core defines canonical execution records under:

```text
sources/<issue>/execution/
  index.md
  sessions/
  reviews/
  defects/
```

Because canonical Profile/State initialization could not run, those records have not yet been legally bootstrapped for the clean editions. To avoid losing resume state, each branch now has an explicit human-readable checkpoint:

- W33: `sources/2026-W33/postmerge-validation-status.md`
- SP001: `sources/SP001/postmerge-validation-status.md`

Once canonical execution-record initialization becomes possible, future edition work should use the standard `execution/` tree and treat these postmerge status files as migration/resume evidence rather than the long-term preferred layout.

## Revalidation finding RVF-008 — old failed edition artifacts must remain visibly non-authoritative

Status: `CONFIRMED`

W33 demonstrates the compatibility case directly: integrated `main` already contains historical `sources/2026-W33/pipeline-state.json` and older Grok material. The redesigned Core declares that legacy state `NON_AUTHORITATIVE_READ_ONLY`.

A clean validation can therefore coexist with historical files only if:

- canonical `production-state.json` is initialized independently;
- legacy bytes are pinned as compatibility evidence only;
- no old Candidate/Architecture/acceptance state is silently adopted.

SP001 takes the stronger clean-start path: failed pre-redesign canonical artifacts were not copied into the new branch.

## PFB-013 status after this trial

Existing acceptance requirement: real cold-start Weekly + SP001/LONGFORM validation after reviewed Core integration.

Current verdict: `PARTIALLY EXERCISED / NOT PASSED`.

Reason:

- W33 and SP001 both exercised real research/editorial operator flows without shared-Core mutation;
- W33 also exercised the actual Human-mediated Grok transport path;
- canonical lifecycle execution could not start because the operator runtime lacked a repository execution bridge.

Therefore PFB-013 must remain open until the same integrated Core can be executed canonically and both editions reach the requested Human Gate without shared-Core repair.

## Resume plan for the validation program

### W33

Read first:

`weekly/2026-W33-v2-work:sources/2026-W33/postmerge-validation-status.md`

Resume at:

```text
canonical Profile/State initialization
-> canonical X manifest generation
-> bind existing imported Grok Raw
-> Discovery
-> Screening
-> Evidence / Materiality / Completeness
-> Candidate Matrix / Selection
-> Architecture
-> ARCHITECTURE_REVIEW
```

Do not rerun Grok unless the exact existing result fails canonical validation.

### SP001

Read first:

`special/SP001-v2-work:sources/SP001/postmerge-validation-status.md`

Resume at:

```text
canonical Profile/State initialization from current scope
-> canonical X NOT_REQUIRED record
-> materialize prepared primary sources as Discovery/Raw
-> Screening
-> Evidence / Materiality / Completeness
-> Candidate Matrix / Selection
-> Architecture
-> ARCHITECTURE_REVIEW
```

Do not copy failed pre-redesign accepted artifacts into the clean run.

## Planned maintenance disposition

Before changing Core, distinguish three classes:

1. **Confirmed existing design behavior** — keep and eventually mark PFB items validated by real production (for example the Grok task-file transport).
2. **Operator/platform capability gap** — solve through a generic execution bridge if possible; do not reintroduce Actions editorial ownership.
3. **Shared-Core semantic defect** — if later discovered during canonical execution, fail the affected validation run, repair Core separately, then restart from a clean boundary.

No shared-Core semantic defect has yet been established by the post-merge W33/SP001 trial.

## Files to use when resuming

| Purpose | Branch | File |
|---|---|---|
| W33 current position / plan | `weekly/2026-W33-v2-work` | `sources/2026-W33/postmerge-validation-status.md` |
| W33 research / Architecture preparation | `weekly/2026-W33-v2-work` | `sources/2026-W33/postmerge-research-intake.md` |
| W33 exact Grok Raw | `weekly/2026-W33-v2-work` | `sources/2026-W33/external/x/weekly-x-2026-W33-postmerge-r1/raw/grok-x-result.md` |
| SP001 current position / plan | `special/SP001-v2-work` | `sources/SP001/postmerge-validation-status.md` |
| SP001 research scope | `special/SP001-v2-work` | `sources/SP001/research-scope-v2.json` |
| SP001 research intake | `special/SP001-v2-work` | `sources/SP001/intake/postmerge-primary-source-intake.md` |
| SP001 Architecture preparation | `special/SP001-v2-work` | `sources/SP001/architecture-preparation.md` |
| Cross-edition post-merge findings / future-flow plan | `main` | `docs/checkpoints/survey-production-core-v2-postmerge-revalidation-worklog.md` |
| Pre-existing production feedback backlog | `main` | `docs/survey-production-core-v2-production-feedback-backlog.md` |
| Redesign implementation history | `main` | `docs/checkpoints/survey-production-core-v2-redesign-worklog.md` |

Repository reality and canonical Production State, once created, outrank this human-readable summary.
