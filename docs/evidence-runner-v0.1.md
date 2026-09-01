# Evidence Runner v0.1

Status: implemented provider-agnostic contract. W32 was used only as replay/smoke evidence; the frozen W32 editorial selection is unchanged.

## Purpose

Evidence Runner sits between broad source screening and final Candidate Selection.

It is designed to prevent three failure modes observed during the first issue:

1. screening hypotheses becoming facts without primary verification;
2. project/vendor/paper benchmark claims being laundered into independent facts;
3. high-frequency release streams becoming many duplicate candidate stories.

## Pipeline

```text
Source Intake
  ↓
screening-index.jsonl
  ↓
batches/batch-NNN.jsonl
  ↓
LLM Screening Result
  ↓ validate exact IDs + batch/prompt SHA
screening-reviewed.jsonl
  ├─ DROP
  └─ verification-queue.jsonl
       ↓
Evidence Task Builder
       ↓
tasks/<task-id>.json
       ↓ primary-source verification
Evidence Run JSON
       ↓ validate task/prompt SHA + references + target coverage
Evidence Merge
       ├─ candidate-ready.jsonl
       ├─ evidence-hold.jsonl
       └─ evidence-rejected.jsonl
             ↓
Candidate Record Materializer
             ↓
<one pre-selection candidate Markdown per Evidence Run>
             ↓
Human Candidate Selection Gate
```

## Screening stage

Screening is triage, not verification.

Decisions:

- `KEEP`
- `MAYBE`
- `DROP`
- `INSPECT`

A batch result is invalid unless every input `screening_id` appears exactly once and the exact input-batch SHA-256 and prompt SHA-256 match.

Partial progress is allowed. `merge_screening_results.py` can merge any completed subset; `--require-complete` is used before declaring screening complete.

## Evidence Task stage

Evidence Tasks are deterministic work orders, not claims.

Task types:

- `VERIFY_ITEM`
- `VERIFY_SERIES`
- `INSPECT_INDEX`

An LLM `duplicate_group` is only a grouping hypothesis. It always carries `requires_confirmation=true`.

When only one member of such a group has been screened so far, it remains `VERIFY_ITEM`; a one-item `VERIFY_SERIES` is not created. Once two or more retained items share the group, they can become one `VERIFY_SERIES` task.

Each Evidence Task is written as its own JSON file under `tasks/`, and its SHA-256 is recorded in the Evidence Task manifest. The Evidence Runner therefore has one exact immutable logical input.

## Evidence classes

Evidence Cards distinguish:

- `PRIMARY_FACT` — directly checkable existence/date/artifact/API/repository fact;
- `VENDOR_CLAIM` — vendor-reported capability/performance/comparison;
- `PROJECT_CLAIM` — OSS project/maintainer/contributor-reported measurement, compatibility or comparison;
- `AUTHOR_CLAIM` — paper-author result/interpretation;
- `SOCIAL_OBSERVATION` — social/community observation or demonstration;
- `INFERENCE` — explicit synthesis from cited evidence.

A primary source does not automatically make every statement in it a `PRIMARY_FACT`.

## Evidence Card content

An Evidence Card contains:

- grouping resolution;
- artifact identity;
- Artifact/Event temporal fields;
- primary/social/secondary sources;
- claims with evidence classes;
- metrics with benchmark/setup context;
- limitations and boundaries;
- every original verification target and its resolution;
- unresolved questions / contradictions;
- an Evidence Runner recommendation.

Recommendations are:

- `CANDIDATE`
- `HOLD`
- `INSPECT_MORE`
- `REJECT`

This is a recommendation only. It is not Candidate Selection.

## Evidence Run provenance

The outer Evidence Run records:

- exact Evidence Task SHA-256;
- exact verification prompt SHA-256;
- provider/model/invocation;
- generation time and optional run reference;
- the Evidence Card.

`validate_evidence_run.py` additionally checks all source-ID references and requires every Evidence Task verification target to be addressed.

## Resumable merge

`merge_evidence_runs.py` accepts a partial set of valid Evidence Runs by default.

It emits:

- `evidence-reviewed.jsonl`
- `candidate-ready.jsonl`
- `evidence-hold.jsonl`
- `evidence-rejected.jsonl`
- `evidence-progress.json`

Any invalid Evidence Run blocks the merge even in partial mode. Missing runs are allowed only when `--require-complete` is absent.

## Candidate Record materialization

`materialize_candidate_records.py` converts only `recommendation=CANDIDATE` records into deterministic Markdown files.

It refuses:

- non-CANDIDATE input;
- `REJECTED` / `NEEDS_MORE` Evidence status;
- `grouping_resolution.split_recommended=true`.

Separate Evidence Runs are never automatically merged solely because their canonical names or URLs match.

The resulting record is explicitly `pre-selection-candidate` and states that candidate-ready does not mean selected.

## Provider boundary

The contracts do not depend on a particular inference service.

Interactive ChatGPT can currently produce screening/Evidence outputs manually against these contracts. A future API runner may be added without changing the editorial semantics, provided it emits the same schemas and provenance fields.

No production inference adapter is required for the deterministic pipeline, validators, merges, or Candidate Record generation.

## W32 smoke evidence

The real W32 replay demonstrated:

- 1,037 normalized source records split into 39 bounded batches;
- complete screening-result validation on sampled batches;
- high-frequency llama.cpp DeepSeek V4 releases grouped into one primary-source Evidence investigation;
- separation of implementation facts from project-reported performance measurements;
- preservation of unresolved backend/performance questions.

See `docs/evidence-runner-smoke-v0.1.md` for the primary-source smoke record.
