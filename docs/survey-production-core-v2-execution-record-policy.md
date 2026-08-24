# Survey Production Core v2 — Edition Execution Record Policy

Status: `OPERATOR/HUMAN-GATE FOLLOW-UP REVIEW REPAIR / REAUDIT PENDING`  
Established: 2026-08-23 JST  
Updated: 2026-08-24 JST

## 1. Purpose

Every edition must be resumable from repository state without prior chat history. Machine lifecycle/state artifacts remain authoritative for machine state; `execution/` is concise human-readable operational provenance.

Human Gate round-trip authority is machine-readable under `{source_root}/gates/` and is summarized, not duplicated, under `execution/reviews/`.

## 2. Canonical layout

```text
{source_root}/execution/
  index.md
  sessions/<session-id>.md
  reviews/architecture-rN.md
  reviews/publication-rN.md
  defects/<defect-id>.md
  requests/<request-id>.json            # connector-safe bridge only
  bridge-runs/<request-id>/...          # connector-safe bridge only

{source_root}/gates/
  architecture-approval.json             # current active canonical approval
  publication-preview-approval.json      # current active canonical approval
  review-index.json
  reviews/architecture-rN.json
  reviews/publication-rN.json
  reviews/approvals/architecture-rN.json # immutable approval snapshot
  reviews/approvals/publication-rN.json  # immutable approval snapshot
```

The review index + rN JSON records + immutable approval snapshots are the durable Human-review history. Current Production State and current canonical approvals determine active authority.

## 3. Human review surface must be durable

Before presenting either normal Human Gate:

1. commit the exact current Production State and every configured Gate input;
2. push/retain that commit on the Profile-bound canonical work branch;
3. record that exact SHA as `reviewed_repository_commit_sha`;
4. present only those committed bytes to the Human.

Canonical `survey_human_gate_v2` must reject a reviewed commit unless it:

- exists;
- remains reachable from canonical `work_branch` (`origin/<work_branch>` when an origin exists; otherwise the local branch);
- contains the exact current reviewed State/Gate-input bytes;
- for Publication Preview, also contains the exact Candidate-bound PDF bytes.

A dangling `commit-tree` object, uncommitted working tree, different branch commit, missing path, or same-path/different-byte commit is not acceptable review provenance.

Connector-safe bridge mode adds the invariant that this durable reviewed commit equals the immutable request-only commit parent. The later request/event commit is separate execution provenance.

## 4. Review decisions and approval snapshots

Normal Gate decisions are:

- `APPROVED`
- `REQUEST_CHANGES`

Every APPROVED decision creates an immutable approval snapshot under `gates/reviews/approvals/<gate>-rN.json`. The rN review record points to that snapshot rather than relying on a canonical approval filename that may later be superseded.

This distinction is essential:

- **current canonical approval** = active State-machine authority;
- **immutable rN approval snapshot** = historical decision evidence.

Old historical review evidence must remain reconstructable even when a later dependency correction reopens Architecture.

## 5. Architecture review revision

Architecture `REQUEST_CHANGES` may return to an allowed pre-Architecture boundary. Record:

- exact reviewed repository commit;
- exact reviewed State/Gate hashes;
- requested changes;
- Human-selected regeneration boundary;
- rN machine review record + index update.

Then invalidate only downstream active authority and resume automatically to Architecture Review rN+1.

## 6. Publication Preview revision

Publication Preview feedback may be publication-local or upstream.

### Publication-local

If regeneration starts at `ARCHITECTURE_ESTABLISHED` or later, the approved Architecture remains active. Invalidate affected drafting/validation/candidate authority and return to Publication Preview rN+1.

### Upstream / cross-gate

If the Human selects a boundary before `ARCHITECTURE_ESTABLISHED` because Publication review exposed an Evidence/Selection/Architecture defect:

1. record Publication `REQUEST_CHANGES` rN against exact reviewed Candidate/PDF bytes;
2. preserve prior Architecture rN review record and immutable approval snapshot;
3. verify current canonical Architecture approval matches State provenance;
4. supersede/remove only that active canonical Architecture approval;
5. set Architecture Review back to pending and clear active Architecture provenance;
6. invalidate checkpoints downstream of the selected boundary;
7. resume through normal research/Selection/Architecture work;
8. stop again at Architecture Review rN+1 before any new Draft/Publication continuation.

This is routine dependency-aware correction, not an Owner Exception Gate.

## 7. `index.md`

`execution/index.md` is the first human-readable navigation file after Production State. Record only current navigation and material provenance:

- issue/Profile/source root/work branch;
- reviewed main baseline;
- current lifecycle/stop reason;
- requested end Gate;
- latest Human-review rN pointers;
- exact reviewed commit for any currently presented/recorded Gate;
- current Candidate/PDF identity when applicable;
- X/Grok task/result disposition;
- execution mode;
- shared-Core defect pointers;
- session list;
- final disposition.

Update it when a Gate decision/revision changes, Architecture is reopened, Candidate changes, a shared-Core blocker appears, or the run terminates/completes.

## 8. `sessions/`

A session record should contain concise sections for:

- Starting authority
- Actions actually performed
- External handoff
- Deterministic execution transport
- Deviations / failures
- End state

When bridge transport is used, record request id/path + request commit, trusted workflow/run pointer when useful, bridge receipt, resulting State, and Human review authority if applicable. Do not duplicate request/result bodies.

When a Human Gate is involved, preserve the Human-reviewed commit separately from request/event execution commit.

## 9. `execution/reviews/`

Each Human Gate revision gets one concise Markdown summary with headings:

- `Reviewed authority`
- `Human decision`
- `Requested changes`
- `Regeneration boundary`
- `Shared-Core implication`

Point to the exact machine rN JSON and review index. For APPROVED rows also point to the immutable approval snapshot.

A Publication cross-gate revision must explicitly note that active Architecture authority was reopened/superseded and identify the new required Architecture revision.

## 10. Shared-Core defects

Production may observe but not repair shared Core. Record symptom/reproduction/impact/workaround/maintenance pointer and either continue with a semantically safe edition-local workaround or stop as `BLOCKED_CORE_DEFECT`.

Core maintenance remains separate from production evidence.

## 11. Trusted operator execution provenance

The work-branch operator workflow is a read-only signal only. Trusted request admission/execution is owned by default-branch `pipeline-contract-tests.yml` through `workflow_run`.

A session record may therefore distinguish:

```text
Human-reviewed edition commit
request-only work-branch commit
read-only signal workflow run
trusted default-branch preflight/executor run
bot output commit
```

Do not collapse those identities.

## 12. Session close

Before a normal conversation ends, ensure:

- session log exists;
- `index.md` current navigation is correct;
- Human rN/current approval pointers are correct;
- any cross-gate reopen is visible;
- exact next action/stop reason is recorded;
- structural execution-record validation passes;
- records are committed to the edition work branch.

This logging is internal work and does not require routine Human confirmation.
