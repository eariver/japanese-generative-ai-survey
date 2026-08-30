# 2026-W33 Sol review — five-carry-over Discovery authority repair r1

Decision: `ACCEPT / FIVE_CARRYOVER_SOURCE_AUTHORITY_REPAIRED / HANDOFF_ORIGIN_TYPO_CORRECTED / APPROVED_FOR_DISCOVERY_ADVANCEMENT`

Issue: `2026-W33`  
Branch: `weekly/2026-W33-v2-work`  
Luna starting SHA: `457c75a923a459f31733e8cb4a1b8c5d159f39a7`  
Canonical repair commit: `b7df5119bf1e6622fca30f6fbfc85113ecb17583`  
Luna ending SHA: `41bbee74dc14b99369afbeeffaa4f2e84397ba7a`

## Review conclusion

The bounded Discovery authority repair is accepted.

The repaired Discovery basis now provides fresh first-party authority for exactly the five active W32 carry-over obligations while preserving the 41-record Discovery identity set and all non-target Discovery objects.

No lifecycle advancement is authorized by this review itself. The next authorized action is a separate deterministic `ISSUE_INITIALIZED -> DISCOVERY_COLLECTED` advancement using a newly regenerated Discovery acceptance bound to the repaired Discovery bytes.

## Change-boundary verification

The Luna range is two fast-forward commits from the supplied Starting SHA.

Repair commit `b7df5119bf1e6622fca30f6fbfc85113ecb17583` changes only:

- `sources/2026-W33/discovery/discovery-v2.jsonl`;
- ten Raw captures under `sources/2026-W33/collectors/sol-approved-carryover-repair/runs/w33-five-carryover-r1/raw/`.

Bookkeeping commit `41bbee74dc14b99369afbeeffaa4f2e84397ba7a` adds only:

- `sources/2026-W33/execution/sessions/w33-luna-discovery-carryover-repair-20260830-r1.md`.

No non-allowlisted path changed.

The remote work branch was read back at `41bbee74dc14b99369afbeeffaa4f2e84397ba7a`.

## Discovery invariants

Verified from the Luna session and direct repository inspection:

- starting Discovery SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`;
- repaired Discovery SHA-256: `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`;
- record count remains exactly `41`;
- the exact 41-ID set is unchanged;
- all 36 non-target parsed Discovery objects are unchanged;
- `base-official-index-minimax-news` is unchanged;
- X Source Intake SHA-256 remains `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6` and remained valid/COMPLETE;
- temporary current-Core Discovery acceptance build/validation passed;
- no Discovery acceptance/checkpoint was committed by Luna;
- Production State remained byte-identical at SHA-256 `0f5b14d6f8afc85605fc621b88e9c4005f70e13e7dbc727f68dae2cc5ca4d56c` with `ISSUE_INITIALIZED / stage:discovery`.

## Five repaired records

### `carry-w32-claude-retirement`

Accepted first-party authority:

- Anthropic model-deprecation documentation.

Accepted finding:

- `claude-opus-4-1-20250805` retirement is established for 2026-08-05;
- affected API developers were notified / deprecation was announced on 2026-06-05;
- Anthropic lists Claude Opus 4.8 as the recommended replacement;
- partner-operated platform schedules are explicitly not inferred.

The Discovery record stores `published_at = 2026-06-05` and `metadata.event_date = 2026-08-05`. This is accepted because the record explicitly distinguishes deprecation/notification chronology from the retirement event, and Screening receives the full Discovery object rather than mechanically deriving chronology from `published_at` alone. Downstream Evidence must preserve the retirement event date explicitly.

### `carry-w32-copilot-cloud-agent`

Accepted first-party authority:

- GitHub changelog entries dated 2026-08-03 for cloud-agent reasoning-level control and comment-triggered automations.

Accepted finding:

- a concrete August cloud-agent update is established;
- it is narrower than the old under-specified shorthand;
- older June/July functionality is not aggregated into an August launch claim;
- plan and administrator-policy limits remain attached.

### `carry-w32-kimi-k3-copilot`

Accepted first-party authority:

- GitHub changelog dated 2026-08-06.

Accepted finding:

- Kimi K3 availability in GitHub Copilot is established;
- gradual rollout and the documented pause/resumption remain explicit;
- Business/Enterprise policy requirements remain explicit;
- no unrelated benchmark/model-performance claim was imported.

### `carry-w32-openai-gpt56-update`

Accepted first-party authority:

- OpenAI ChatGPT product update;
- OpenAI Deployment Safety Hub August update.

Accepted finding:

- a distinct 2026-08-06 GPT-5.6 Sol/Luna ChatGPT update is established;
- this is not rewritten as the original GPT-5.6 launch;
- Work/Codex model-version non-change remains explicit;
- product and safety-evaluation claims remain OpenAI-attributed.

### `carry-w32-repowise`

Accepted first-party authority:

- Repowise project repository;
- `repowise-bench` repository;
- Flask v3 benchmark report;
- reproduction instructions.

Accepted finding:

- project/tool identity and benchmark methodology are established;
- reported work-reduction results remain project-reported;
- retrieval/work reduction is not generalized to task success;
- small sample sizes, judge noise, caching sensitivity, scope, and credential requirements remain attached;
- no independent reproduction is claimed.

## Handoff specification defect

The Sol handoff `w33-discovery-carryover-repair-luna-r1.md` incorrectly stated in section 4 that the five target records should preserve `provenance.origin = CARRY_OVER`.

The actual Starting Discovery authority at `457c75a923a459f31733e8cb4a1b8c5d159f39a7` shows all five target records with:

- `provenance.origin = GAP_FILL`;
- `research_pass = 1`;
- empty `parent_refs`;
- `weekly:carry-over` in `obligation_ids`.

Luna correctly preserved the actual Starting authority rather than silently mutating the provenance graph to satisfy the erroneous textual constant. This is a Sol handoff typo, not a worker defect.

Authoritative interpretation for subsequent W33 revision work:

> preserve the actual repaired Discovery provenance as `GAP_FILL` for these five records unless a separate reviewed migration explicitly changes the graph.

No provenance repair is required.

## Stale acceptance status

The existing file:

`sources/2026-W33/discovery/discovery-accepted-v2.json`

is historical/stale relative to the repaired Discovery bytes. It still binds the pre-repair Discovery SHA-256 `632ba233...`.

It must therefore **not** be reused for the new Discovery checkpoint.

The next deterministic advancement must regenerate/replace this canonical acceptance from:

- repaired Discovery SHA-256 `6e6590b5b8153ccc8590c3230ed3b7605c0a9805b636081babc3247f0442bfbd`;
- unchanged X Source Intake SHA-256 `4e90919e54f2f32b2e010fed57b23d94799a88fe2330e9ee8a090c54953905f6`.

## Carry-forward constraints

Subsequent Screening/Evidence/Completeness must actually dispose the five `weekly:carry-over` obligations from this repaired first-party basis. They must not mechanically inherit the old HOLD/NEEDS_MORE outcomes.

Architecture regeneration later in the revision remains subject to the Owner's r2 requirements, including:

- explicit mandatory `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` chapter;
- preserve the previously accepted six substantive packages, 28-candidate placement strategy, 18-page target / 24-page hard cap, and Agent Reliability comparative-synthesis constraint unless newly accepted downstream evidence justifies a change.

## Next authorized transition

Exactly:

`ISSUE_INITIALIZED -> DISCOVERY_COLLECTED`

using a newly regenerated Discovery acceptance and the canonical operator bridge.

Do not begin Screening in the same deterministic advancement task.
