# W34 Luna/Work instruction — Evidence through Architecture Review

Status: `EXECUTION_AUTHORITY / BOUNDED_AT_HUMAN_ARCHITECTURE_REVIEW`

Date: 2026-09-05 JST

## 1. Mission

Continue `2026-W34` from the current accepted Screening boundary through the normal Survey Production Core v2 research/architecture loop and stop only at the first normal Human Gate:

```text
CANDIDATES_NORMALIZED
-> Evidence verification
-> materiality / completeness closure
-> Selection
-> Architecture
-> exact stage validation/checkpoints
-> durable Human-review surface
-> ARCHITECTURE_REVIEW pending
```

Do not draft reader-facing publication text and do not execute the external publication sidecars in this task.

The Exact Starting SHA is supplied by the invoking prompt and is authoritative for the start guard. Do not use a stale SHA embedded in older handoffs as a replacement start guard.

## 2. Repository authority

Repository:

`eariver/japanese-generative-ai-survey`

Canonical work branch:

`weekly/2026-W34-v2-work`

Reviewed shared Core authority:

`main@a9f121f0d65591f52b53515712d7c0bae573b2ef`

During edition production, shared Core roots remain read-only exactly as required by `AGENTS.md`:

```text
AGENTS.md
config/
schemas/
scripts/
.github/workflows/
docs/survey-production-core-v2-*.md
```

If a new shared-Core defect is discovered, record it under the W34 execution tree and stop the affected formal production run; do not repair shared Core in this edition branch.

## 3. Mandatory read order

Before substantive work, read current branch versions of:

1. `AGENTS.md`
2. `docs/survey-production-core-v2-session-bootstrap.md`
3. applicable Weekly Profile / X intake / execution-record policy documents referenced by bootstrap
4. `sources/2026-W34/production-profile.json`
5. `sources/2026-W34/production-state.json`
6. `sources/2026-W34/execution/index.md`
7. `sources/2026-W34/execution/luna/w34-post-483-core-sync-screening-recovery-r1/sol-screening-handoff-v0.1.md`
8. `sources/2026-W34/execution/luna/w34-post-483-core-sync-screening-recovery-r1/validation-v0.1.json`
9. `sources/2026-W34/execution/findings/sol-external-sidecar-qa-pilot-plan-20260905-r1.md`
10. `sources/2026-W34/execution/reviews/sol-authority-auditor-production-adapter-review-20260905-r1.md`

Repository state outranks chat history.

## 4. Accepted Screening boundary

The accepted root Discovery remains immutable:

- path: `sources/2026-W34/discovery/discovery-v2.jsonl`
- records: 40
- SHA-256: `8a176af94ccd245a7651a7a292d001cff9cef355b1320f4a73278ee9f2e5216c`

Current effective derived Screening basis:

- path: `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
- records: 110
- SHA-256: `9bfc0fc9b63f97cc9568dc53bb06595dd2540b92e843b55b2650abcbcc97aca2`
- accepted-root accounting: 40/40

Current active Screening acceptance is selected only through the passed Screening Stage Checkpoint:

`sources/2026-W34/screening/v2/accepted/5692a79ac20f4376beee02758754a71b771ed78ff30b675d2fa8177af7f65e98/screening-accepted.json`

Decision totals:

- KEEP 45
- MAYBE 19
- INSPECT 16
- DROP 30
- TOTAL 110

Expected non-DROP Evidence task count: `80`.

Historical 105-record Screening acceptance and historical 105-event Sol decision authority remain immutable history. Do not delete, rewrite, or use directory-order/latest heuristics to select authority.

## 5. Evidence verification

Use the current reviewed agent-first Core machinery and the active Screening acceptance to prepare exactly the required non-DROP Evidence work.

Evidence research is substantive research, not mechanical restatement of Discovery claims.

For each non-DROP item:

- verify concrete claim identity, date/chronology, technical/product/research delta, and source authority;
- prefer first-party/official/primary technical authority where available;
- preserve exact source provenance and repository Raw evidence required by current Core;
- distinguish event date from later commentary/availability/distribution dates;
- resolve `INSPECT` uncertainties rather than automatically promoting them;
- treat `MAYBE` as requiring real verification, not presumed materiality;
- keep duplicate/context relationships explicit rather than silently collapsing provenance;
- do not treat a Discovery title/summary as established Evidence.

DailyX, Grok, and ordinary X observations remain Discovery/community signals. They may identify a verification target but are not direct technical Evidence authority unless a separate, legitimately authoritative source is captured under the applicable Core source/evidence contract.

Do not use post-cutoff developments to retroactively create an in-window event. Later sources may be used only when they legitimately verify facts/chronology about the W34 event and the provenance distinction is explicit.

Evidence work may perform bounded search expansion needed to resolve verification targets. Do not broaden into unrelated current-news research.

## 6. Materiality and completeness

After Evidence acceptance, continue autonomously through the configured materiality/completeness stage.

Apply current generic WEEKLY profile authority. Do not create edition-specific machine semantics.

Completeness must address the accepted research obligations and materiality questions, not merely count successful Evidence records. If a material gap remains, perform bounded gap-fill research through the existing Core provenance model and revalidate before closure.

Do not request Human confirmation for normal search refinement, evidence repair, completeness repair, or materiality judgment.

## 7. Selection

Selection is an internal editorial/research stage, not a Human Gate.

Use verified Evidence and materiality/completeness authority to select the reader-significant W34 set. Preserve reasons for inclusion/exclusion, duplicate handling, chronology and authority boundaries, and any retained uncertainty required by Core.

Do not leak internal Selection labels into future reader-facing prose; that publication-boundary check is deferred to post-Architecture drafting.

## 8. Architecture

Build the W34 Architecture using the selected, verified material and current Weekly publication profile.

Architecture should define the reader-facing narrative structure and emphasis without turning internal Evidence/Selection metadata into reader prose.

Run the canonical Architecture validation and create the exact configured Architecture Review inputs, including current review summary and review-attention authority required by Core.

## 9. Durable Human Gate surface

Before stopping:

1. finish every configured Architecture Review input;
2. commit exact current Production State and all Gate inputs;
3. push/retain that commit on `weekly/2026-W34-v2-work`;
4. verify the commit remains the current reachable canonical branch head;
5. use that exact commit as `reviewed_repository_commit_sha`;
6. verify Architecture Review remains `pending` and Publication Preview remains `pending`.

Do not record or infer a Human decision.

The stop condition is the durable review surface, not merely generation of an Architecture file.

## 10. External sidecar tools — explicitly deferred

Do not run either tool in this task:

- Publication Boundary Validator: `eariver/publication-boundary-redteam@7b9de2105c690daaafa6698c1791d51ca84a92c0`
- Authority Auditor production adapter: `eariver/survey-core-v2-authority-auditor@c5f09d463b21c914d9c59b34597858f6182fc244`

They start only after Human Architecture Review approval and reader-facing Drafting begins, as defined by the W34 sidecar pilot plan.

Do not add a lifecycle state, Human Gate, Production State authority, CI workflow, or blocking Core rule for either sidecar.

## 11. Execution records

Maintain edition-local execution records sufficient for a fresh session to resume without chat history. At minimum record:

- starting branch/head and reviewed main SHA;
- Evidence package/task counts and accepted result identity;
- Evidence source/provenance summary and unresolved items;
- materiality/completeness outcomes and any bounded gap-fill;
- Selection result identity/counts;
- Architecture result identity;
- stage/checkpoint validation results;
- exact Human Gate review inputs;
- final `reviewed_repository_commit_sha`;
- confirmation that external sidecars were not executed;
- confirmation that shared Core was not edited;
- any new defects or retained limitations.

Update `sources/2026-W34/execution/index.md` to the actual final state.

## 12. Validation / bounded stop

Use current Core validators at each formal stage. Do not manually edit Production State to simulate progression.

If all routine stages succeed, stop at:

`ARCHITECTURE_REVIEW_READY_FOR_HUMAN`

Expected characteristics at stop:

- Evidence/materiality/completeness/selection/architecture machine checkpoints required by the current Core are passed;
- Architecture Review is pending;
- exact review bytes are committed/pushed on the canonical W34 branch;
- a full 40-hex `reviewed_repository_commit_sha` is reported;
- no drafting, Publication Candidate, Publication Preview, Freeze, Release, or sidecar execution has occurred.

If an actual shared-Core defect is encountered, record it and stop as `NEEDS_SOL_REVIEW` without weakening Core authority.

A genuine unresolved Owner decision may use the normal Exception Gate contract. Routine editorial/research uncertainty is not an Exception Gate.
