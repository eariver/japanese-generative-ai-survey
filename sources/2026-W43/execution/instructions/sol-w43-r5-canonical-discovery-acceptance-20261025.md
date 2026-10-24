# W43 Sol → Muse r5 — two provenance fixes and canonical Discovery Acceptance, no stage advancement

Status: `BOUNDED_FINAL_DISCOVERY_AUTHORITY_MATERIALIZATION / STOP_BEFORE_BRIDGE`
Date: 2026-10-25 JST
Repository: `eariver/japanese-generative-ai-survey`
Existing branch ONLY: `weekly/2026-W43-v2-work`
Sol ruling: `sources/2026-W43/execution/reviews/sol-w43-discovery-completeness-review-r4-20261025.md` (substantive Discovery coverage PASS_WITH_LIMITATIONS).
Reviewed Muse r4 HEAD/Root Tree: `59798654f24f5c096f06bcd816b7cb06c80ff8d5` / `e21e7ae8850ef901a2515d367c09082c6c578ffe`.
Read-only reviewed main HEAD/Tree: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen Core HEAD/Tree: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

**Exact Starting HEAD and Tree are the final remote Git values provided by Sol AFTER writing this contract + execution index.** Verify remote work branch + root tree, remote main HEAD+tree and Frozen Core HEAD+tree read-only before ANY writes. If any mismatch: STOP, ZERO WRITES, report expected and actual. No fallback/new/repair/review branches, reset/rebase/force/history rewrite.

## 1. Exact mission and bounds

Muse r4 passed substantive Sol editorial Discovery completeness. Grok/X original is genuinely imported, canonical `x-source-intake-v2.json` records `PARTIAL` Grok observation with `status=COMPLETE` (registration complete). 51 r4 records / 46 event families and the Flint primary source have already been checked. Do not repeat broad collection, screening or data synthesis.

Do just:
1. Correct the **two precise metadata/reference defects** below without rewriting r1-r4 immutable proposals/archives.
2. Materialize the **canonical** final Discovery JSONL and accepted Discovery authority using frozen scripts.
3. Validate and stop at Sol readback BEFORE trusted stage advancement.

## 2. Required corrections

### CR-01 Grok sensor provenance source_type
- r4 `w43-r4-grok-x-ledger-20261024` was recorded as `source.source_type="PRIMARY_OFFICIAL"`, but its actual publisher is a Grok X observation sensor, not an official primary technical source. Other fields already say `collector_id="grok-x-import"`, `authority_class="X_OBSERVATION"`.
- In r5 active proposal change **only** `source.source_type` for that ID to `X_OBSERVATION`. Retain exact `weekly-x-2026-W43.md` raw path, 13425 bytes/SHA256, manifest discovery bindings, collector, genuine observation date. If distinguishing `temporal`, mark it explicitly as an after-cutoff X observation ABOUT the W43 window, not an Oct 24 technical publication.
- Do not change `w43-r4-flint-20261021` from PRIMARY_OFFICIAL because it is genuinely bound to official Recursive/HF sources; retain its additional Grok Raw linkage.
- Do not count Grok sensor ledger as a model launch in thematic Selection; it is one audit/observation record.

### CR-02 Exact X post ID erratum
- Grok Raw exact second pinned URL: `https://x.com/lm_zheng/status/2110889410615234942`.
- r4 crosswalk `collectors/primary/runs/20261024T133000Z-muse-r4/notes/r4-note-03-grok-crosswalk.md` incorrectly claimed `2110889415895234942`.
- Preserve both source documents unchanged (audit history); create a scoped `sources/2026-W43/execution/source-intake/w43-grok-x-post-id-errata-r5.md` with exact Raw citation, before/after ID, lack of independent verification of linked post beyond Grok sensor, no new weights-release claim, and no fabrication of X timestamp.
- Current Kimi official post ID `2113680701770068067` remains correct; Meta Muse Spark initial weights Oct 15 OUT.
- If active JSONL repeats the erroneous second X ID, fix it. Never mutate original Grok Raw.

## 3. Canonical acceptance generation, identity and integrity

- Create a standalone historical `sources/2026-W43/discovery/discovery-v2-proposal-r5.jsonl` by copying r4 51 rows and applying exactly the one `source_type` correction (and, only if necessary, the above observational temporality clarification). Other 50 rows must remain semantically and byte-identically the same; no extra candidates or deletions.
- Copy final approved r5 JSONL to canonical `sources/2026-W43/discovery/discovery-v2.jsonl` (as W42 practice), preserving all 51 IDs.
- Generate **ONLY through frozen canonical Core v2** `scripts.survey_discovery_v2.build_acceptance(repo_root, discovery_path, manifest_path, "2026-W43", output_path)` and `validate_acceptance` for `sources/2026-W43/discovery/discovery-accepted-v2.json`. No manual JSON forging, copying earlier sandbox result or altering graph hash by hand.
- X manifest `sources/2026-W43/external/x/x-source-intake-v2.json` already COMPLETE; do NOT run record-result again and do NOT overwrite it. Validate require_complete against manifest; both `discovery_ids` (Flint + X ledger) must bind the exact Grok Raw path in `raw_refs` of generated accepted records.
- Confirm profile/state still match (State `ISSUE_INITIALIZED`, next `stage:discovery`, all Human Gates pending). Run execution-record validator (r1/r2 Sol documents already repaired for five headings), active schema, exact graph, source hashes, X integration, `validate_acceptance` and changed-file safeguards.
- If any validator fails, stop honestly (BLOCKED) and preserve diagnostics. No edition-local fake PASS, no edits to frozen Core.

## 4. Output and bounded stop

Artifacts:
- `sources/2026-W43/discovery/discovery-v2-proposal-r5.jsonl`
- `sources/2026-W43/discovery/discovery-v2.jsonl` (canonical)
- `sources/2026-W43/discovery/discovery-accepted-v2.json` (canonical Core output)
- `sources/2026-W43/execution/source-intake/w43-grok-x-post-id-errata-r5.md`
- `sources/2026-W43/execution/sessions/muse-w43-discovery-acceptance-r5-20261025.md`, Sol handoff + index update, machine stdout/report excerpts and exact artifact SHA256/bytes.

All prior proposal r1-r4, Grok Raw, r4 Flint raw/notes, earlier Sol reviews, W42, `AGENTS.md`, protected shared `scripts/`, `schemas/`, `config/`, `.github/`, `tests/`, and frozen Core unchanged. No new branch/force push/reset/rebase. Non-force push exact work branch and remote HEAD/Root Tree readback.

**DO NOT create an operator `ADVANCE_STAGE` request, post Issue #448 command, run Screening/Evidence/Selection/Architecture, or hand-author a Stage Checkpoint/Production State.** The trusted operator will advance `ISSUE_INITIALIZED`→`DISCOVERY_COLLECTED` only AFTER Sol review of your exact accepted bytes.

Stop token: `SOL_CANONICAL_DISCOVERY_ACCEPTANCE_READY_R5`. Return exact remote Final HEAD+Tree, graph SHA256, 51-record count, X manifest status, original Raw SHA, all validation return codes, blockers and the planned operator artifact path.
