# Survey Production Core v2 — Edition Execution Record Policy

Status: `INTEGRATED BASE + OPERATOR BRIDGE/HUMAN-GATE MAINTENANCE CANDIDATE / DIRECT-LOCAL REVIEW PROVENANCE SYNCHRONIZED / REAUDIT PENDING`  
Established: 2026-08-23 JST  
Human-Gate update: 2026-08-24 JST  
Working branch: `maintenance/core-v2-operator-execution-bridge`  
Related redesign: `docs/survey-production-core-v2-redesign-plan-after-w33-sp001.md`

## 1. Purpose

Every Weekly/Special production task is normally executed in its own ChatGPT conversation. The repository therefore needs a stable edition-local record that allows a later session or Core-maintenance review to reconstruct what actually happened without reading chat history or inferring behavior from commits alone.

Machine lifecycle/state artifacts remain authoritative for machine state. Execution records are human-readable operational provenance and must not duplicate every machine field.

The Human Gate round-trip maintenance adds a machine-readable review history under `{source_root}/gates/`; the Markdown review records in `execution/reviews/` summarize and point to that authority rather than replacing it.

## 2. Canonical location

Store edition execution records under the **Profile-declared source root**, not in global `docs/checkpoints/`.

```text
{source_root}/execution/
  index.md
  sessions/
    <session-id>.md
  reviews/
    architecture-r1.md
    architecture-r2.md
    publication-r1.md
    publication-r2.md
  defects/
    <defect-id>.md
```

When the reviewed operator execution bridge is used, two optional transport/provenance directories may additionally exist:

```text
  requests/
    <request-id>.json
  bridge-runs/
    <request-id>/
      ... deterministic result / receipt authority ...
```

Machine Human-review authority is separate from this human-readable execution tree:

```text
{source_root}/gates/reviews/architecture-rN.json
{source_root}/gates/reviews/publication-rN.json
{source_root}/gates/review-index.json
```

`execution/reviews/*.md` are concise operational summaries. `gates/reviews/*.json` plus `gates/review-index.json` are the exact machine provenance for reviewed State/artifact hashes, revision number, decision, reviewed commit and approval/revision consequence.

`requests/` and `bridge-runs/` are not a second lifecycle state machine. Direct-local CLI execution does not need them.

## 3. Deterministic helper boundary

`scripts/survey_execution_record_v2.py` implements only the structural base of this policy. It may create/validate the base `execution/` tree and first session/index skeleton. It does not create Human decisions or change Production State.

`scripts/survey_human_gate_v2.py` owns the deterministic machine review records for the two normal Human Gates. It may record an already explicit Human `APPROVED` or `REQUEST_CHANGES` decision, validate contiguous revision identity, and apply the allowed deterministic State/checkpoint consequence. It must not infer the Human decision, requested changes or regeneration boundary.

Before either direct-local or bridge-backed Human Gate recording, the canonical Human Gate helper must prove that `reviewed_repository_commit_sha` names a real Git commit whose tree contains the exact current reviewed Production State and every Gate-input artifact byte recorded in the review authority. Publication Preview includes the exact Candidate-bound PDF in that proof. A syntactically valid SHA, an uncommitted working-tree view, or a commit containing different/missing review bytes is not sufficient provenance.

The operator bridge may invoke either helper when direct exact local CLI is unavailable, subject to its immutable request and reviewed-main controls. Connector-safe execution adds a transport proof that the reviewed commit is exactly the immutable request-only commit parent. Direct-local execution has no request-parent wrapper, so the canonical Human Gate helper's commit-existence/tree-byte verification is the fail-closed reviewed-commit authority.

## 4. `index.md` — one current run index per edition

`index.md` is the first human-readable navigation file a new ChatGPT session should read after `production-state.json`. It is a compact current-state navigation document, not a diary.

Required content includes:

- issue / edition ID;
- Research Profile and Publication Profile;
- canonical work branch and Profile-declared source root;
- source-of-truth reviewed `main` commit SHA used to start the run;
- run start date/time;
- requested Human Gate / requested end state;
- current lifecycle and stop reason as convenience pointers from canonical State;
- Human Gate status and relevant Issue/PR pointers;
- latest machine Human-review revision pointer when a gate has been reviewed;
- current accepted/rejected Publication Candidate and PDF identity when applicable;
- Grok/X applicability, latest Drive task-file path and result disposition when applicable;
- execution mode (`DIRECT_LOCAL_CLI` or bridge when material to provenance);
- known edition-local deviations;
- known shared-Core defects;
- session logs in chronological order;
- final disposition: `IN_PROGRESS`, `HUMAN_GATE`, `BLOCKED_CORE_DEFECT`, `TERMINATED_VALIDATION`, or `COMPLETE`.

### Freshness rule

Update `index.md` whenever:

- lifecycle crosses a Human Gate boundary;
- a Human Gate receives `REQUEST_CHANGES` or `APPROVED`;
- the current Human-review revision changes;
- a shared-Core defect changes the ability to continue;
- a new Publication Candidate becomes the Human review target;
- the run is terminated or completed.

Routine `REQUEST_CHANGES` must not be described as an Exception/rejection merely because an older State enum used the word `rejected`.

## 5. `sessions/<session-id>.md` — actions actually performed

Create one session log per ChatGPT production conversation, or per materially separate continuation if one conversation is intentionally split into distinct execution phases.

Recommended ID:

```text
YYYY-MM-DDTHHMM-JST-<short-purpose>.md
```

Required sections are:

### Starting authority

Record branch head, Production State path/SHA, reviewed Core/main SHA, session objective/requested stop and prior execution pointer.

### Actions actually performed

Group by meaningful stage rather than tool call. Record material work, useful counts, important judgments, canonical artifact paths, and commit/PR/run identity only when it materially identifies resulting state.

### External handoff

When Grok/X is used, record only exact Drive task/result references, imported Raw path, result hash/byte count or manifest identity, and editorial disposition. Do not duplicate task/result bodies.

### Deterministic execution transport

When the operator bridge is used, record only request/receipt identity needed to reconstruct execution:

- request id/path and exact request commit;
- bridge-run receipt/result path;
- resulting Production State path/SHA or lifecycle edge;
- Human Gate review record/index path when the request recorded a Human decision;
- workflow/run pointer if useful for failure diagnosis.

For a Human Gate decision in either execution mode, record/preserve the exact `reviewed_repository_commit_sha` that was validated against the reviewed State/Gate-input bytes. In bridge mode the request/event commit is separate execution provenance and must not be substituted for the reviewed parent commit.

Do not duplicate request/result bodies in session Markdown.

### Deviations / failures

Record only run-affecting failures and classify each as `EDITION_LOCAL`, `TRANSIENT_EXECUTION`, or `SHARED_CORE_DEFECT`.

### End state

Record lifecycle/Human Gate status, exact candidate/PDF identity if applicable, current Human-review revision, next action and why the session ended.

## 6. Recording granularity

The record must be sufficient to answer:

1. What did ChatGPT actually do?
2. What material decisions were made and why?
3. Which exact artifacts became authoritative?
4. Where did Human/Grok interaction occur?
5. Which deterministic execution substrate was used when relevant?
6. Which machine Human-review record binds the latest Human Gate decision?
7. Did the production session encounter or modify shared Core?
8. Why did the session stop?

It must not be a transcript or chain-of-thought log.

A normal stage usually needs 3–10 concise bullets. Do not routinely list every connector invocation, workflow poll, successful command, file opened, repetitive PASS output, full Issue body, or full external-source content.

## 7. `reviews/` — compact Human Gate revision history

Every Human Gate review gets one short Markdown record even if detailed feedback lives in a GitHub Issue.

Required headings are:

- `Reviewed authority`
- `Human decision`
- `Requested changes`
- `Regeneration boundary`
- `Shared-Core implication`

For revision `rN`, the Markdown must point to the exact machine record:

```text
Architecture: {source_root}/gates/reviews/architecture-rN.json
Publication:  {source_root}/gates/reviews/publication-rN.json
Index:        {source_root}/gates/review-index.json
```

Record gate, revision, reviewed candidate identity, Human decision, detailed feedback pointer, concise defect families, earliest Human-supplied regeneration boundary and whether shared Core is implicated. Do not duplicate the full Human feedback body.

Decision vocabulary for normal gates is:

- `APPROVED`
- `REQUEST_CHANGES`

A genuine Owner-level Exception is recorded separately; do not encode routine corrections as a normal-gate `REJECTED` shortcut.

### Revision history rule

Machine review revisions are contiguous independently for Architecture and Publication Preview. The Markdown filename revision must match the corresponding machine JSON revision.

After `REQUEST_CHANGES`, old canonical artifact paths may later contain regenerated bytes. Historical review identity remains exact through the machine review record's SHA-256 fields and `reviewed_repository_commit_sha`. The reviewed commit is reconstructable authority only because Core has verified that the named commit exists and contains those exact reviewed bytes. In bridge mode Actions additionally proves it is the request-only parent. Current authority comes from Production State/checkpoint/gate provenance, not from an old review Markdown.

## 8. `defects/` — shared-Core observations from production

A Production session may observe but must not repair a shared-Core defect.

Required headings are:

- `Observation`
- `Reproduction boundary`
- `Impact`
- `Safe edition-local workaround`
- `Core-maintenance pointer`
- `Production disposition`

Record symptom, affected edition/profile, reproducing artifact/boundary, correctness/quality/autonomy impact, safe workaround availability, maintenance pointer, and `CONTINUE_WITH_SAFE_LOCAL_WORKAROUND` or `BLOCKED/TERMINATED` disposition.

Do not put proposed generic implementation patches in the edition record.

## 9. Relationship to machine artifacts

Keep machine-oriented artifacts under Profile/canonical paths and point to them from execution records:

```text
{source_root}/production-state.json
{source_root}/orchestration/...     # lifecycle / Stage Checkpoints / validator artifacts
{source_root}/gates/...             # approvals + exact Human Gate revision authority
{source_root}/execution/...         # human-readable continuity + optional bridge provenance
{source_root}/publication/...       # publication/candidate artifacts where Profile places them
```

`execution/` is not a second state machine. Bridge requests/receipts and review Markdown do not outrank canonical Production State or machine Human-review authority.

## 10. Session bootstrap

Every new edition production conversation reads, in this order:

1. current reviewed `main` Core authority / session bootstrap;
2. `{source_root}/production-state.json` if the run exists;
3. `{source_root}/execution/index.md` if the run exists;
4. latest machine Human-review index/record referenced by the execution record when a Human Gate has already been reviewed;
5. latest referenced session/review/defect/bridge receipt needed to continue.

For a new run, initialize the execution record after canonical Profile/State initialization. For an existing run, do not rerun `init`; create/update the next session record and list it in `index.md`.

## 11. Session close

Before a production conversation ends for any reason other than abrupt tool/session failure, it must:

1. update/create its session log;
2. update `execution/index.md` when current-state navigation changed;
3. ensure Human Gate/review/defect pointers are present;
4. ensure any Human review Markdown points to the exact rN machine record;
5. record exact next action/stop reason;
6. run structural execution-record validation;
7. commit the record on the edition work branch.

This logging is internal production work and never requires routine approval.

## 12. Migration / compatibility

Existing W33 and SP001 pre-policy logs remain historical evidence and are not rewritten merely to match the new layout.

Clean validation runs initialize `{source_root}/execution/` once canonical Profile/State exists. Temporary human-readable resume files created before canonical initialization remain migration evidence only and should point forward to canonical execution records after restart.
