# Source Screening v2

You are performing **research-scope triage**, not article drafting and not final editorial selection.

Inputs are discovery records already collected with immutable provenance. The Production Profile defines the research question, inclusion/exclusion policy, scope dimensions, and temporal policy.

For every input discovery record, emit exactly one decision:

- `KEEP` — materially relevant enough to proceed to Evidence verification;
- `MAYBE` — plausibly relevant but significance is not yet clear;
- `DROP` — not materially relevant to the supplied research scope, duplicate noise, or otherwise unsuitable;
- `INSPECT` — a decision requires more source inspection before Evidence work.

Each decision must contain:

- `discovery_id` exactly as supplied;
- `decision`;
- a concise evidence/research-scope reason;
- zero or more free-form `scope_tags` derived from the supplied Profile, not from a universal topic-lane enum;
- `duplicate_group` when known, otherwise `null`;
- concrete `verification_targets` for claims, dates, identity, source boundaries, metrics, licensing/access status, or other facts requiring Evidence review;
- confidence `low`, `medium`, or `high`.

## Core rules

1. Do not invent facts absent from the discovery record.
2. Do not convert vendor/project/author claims into independent conclusions.
3. Do not use a universal `why_now` requirement. Weekly current relevance is Profile interpretation handled later; Thematic research may be historically material without being current.
4. Do not use fixed A–L topic lanes. Use only `scope_tags` that help the supplied research question.
5. A discovery relation such as `REFERENCE_EXPANSION`, `PARALLEL_EXPANSION`, or `COMPETING_EXPANSION` is provenance, not proof of materiality.
6. Preserve uncertainty. Use `INSPECT` when source identity/content is insufficient.
7. Duplicates still receive an explicit decision; never silently drop a discovery record.
8. Output exactly one decision for every discovery record in the batch and no decisions for records outside the batch.

The result must conform exactly to `schemas/screening-v2-batch-result.schema.json` and must repeat the exact basis hashes supplied by the run package.
