# Muse forward-only post-cutoff proof r4 (STEP A rehearsal + STEP B canonical)

Status: `NATIVE_CORE_PROOF_PASS / NO_CORE_CHANGE / NO_STAGE_ADVANCE`
Date: 2026-10-25. Pinned start `e2fa8e935…` (`ae78cc2e…`). Ruling: Sol forward-only correction (Metrics MAYBE provisional → POST_CUTOFF/NON_MATERIAL) is testable; no rewind/invalidation.

## Reviewed authority

- Sol ruling `sol-w43-frozen-core-forward-only-evidence-correction-ruling-20261025.md` (MAYBE provisional, POST_CUTOFF/NON_MATERIAL + ledger MAYBE→NON_MATERIAL lawful; Grok precedent; no Screening rewrite).
- Clock audit `w43-cutoff-oct23-event-clock-audit-r1-20261025.md` + handoff `SOL_W43_UPSTREAM_AUTHORITY_DECISION_HANDOFF-r1.md` (Metrics 23:42:03Z OUT; Teams 21:29:58Z IN; Kimi X IN; Nemotron commits IN; TanStack product IN/blog UNRESOLVED; Securing RSS caveat; Vercel split; nine DATE_ONLY).
- R3 acceptances `dbc27cd8…`/`7a812053…`, Screening 51 MAYBE (Metrics low), Discovery day-precision IN premise, State `CANDIDATES_NORMALIZED`, Gates pending.

## Human decision

- NONE. No Human Gate requested, recorded, or inferred. No `ADVANCE_STAGE`, invalidation, revision, Selection, Architecture, Draft, PDF.

## Requested changes

- None executed beyond the bounded r4 correction contract: Metrics POST_CUTOFF/NON_MATERIAL with supersession; Oct23 clock/citation precision; IA-017 crosswalk; IA-018 19/13 erratum. No broad re-research, no 31-record churn, no count targeting.

## Regeneration boundary

- No upstream rewrite. Forward-only r4: new content-addressed Evidence/Views + versioned supplement-r4/compat-r4/interactive-r4 + snapshotted-then-regenerated canonical ledger/completeness. r1/r2/r3, Discovery/Screening, State/Checkpoints, Core/main/Gates immutable.

## Shared-Core implication

- Design A (rewind/invalidation) NOT_SUPPORTED (forward-only +1, no INVALIDATE_STAGE, pending-gate only, W43 not at gate). Design B (downstream label alone) insufficient without explicit supersession/provenance (schema would PASS unacknowledged MAIN_EVENT — demonstrated gap). Design C (separate Core maintenance) contingency only, NOT executed. No Core edits; W34 candidate not reused as edition patch.

## STEP A isolated rehearsal (no canonical writes)

- Worktree `/home/eariver/git/w43-r4-check` detached at `e2fa8e935…` (full checkout, clean except untracked tmp). Same frozen code/data/State as canonical.
- Trial input `/tmp/interactive-r4-trial.json` (runner `2026-10-25T05:00:00Z`): Metrics PARTIAL + NON_MATERIAL/POST_CUTOFF with supersession (provisional IN → verified 23:42:03Z OUT +1h42m03s, no pre-22Z event); Teams 21:29:58Z IN note; Kimi X 17:15:24Z IN/blog DATE_ONLY; Nemotron 07:00Z + 15:12–19:03Z IN; TanStack product Oct22 IN/blog UNRESOLVED; Securing RSS 10:00Z caveat; Vercel/Ollama Oct17+Oct23 split.
- Frozen chain (unchanged native adapter, impl `e2fa8e935…`): interactive 32 VALID → 32 Cards → accept `fca3db52…` (worktree tmp) → 32 Views → accept `725384f3…` → ledger 51 (MATERIAL 20 / CONTEXT 10 / NON_MATERIAL 2 / EXCLUDED 19) → completeness LIMITED. Commands: worktree `tmp-run-stepA.py` (exit 0), stage precheck CLI (exit 0, `CANDIDATES_NORMALIZED→EVIDENCE_REVIEWED`, State SHA `f356b238…` unchanged).
- `validate_edition_view` permits PARTIAL + NON_MATERIAL/POST_CUTOFF (only REJECTED→NON_MATERIAL / NEEDS_MORE→HOLD constrained; Grok MAYBE→NON_MATERIAL precedent). `build_materiality_ledger` yields Metrics MAYBE/NON_MATERIAL without touching Screening. `validate_stage` `_evidence_basis` revalidates exact Screening SHA + chain (old `Fresh in-window lead` NOT reasserted as fact).
- Negatives: unacknowledged MAIN_EVENT Metrics → Core schema PASS (empty errors) = schema-only gap DEMONSTRATED (semantic supersession required, provided); tampered supplement byte_count → FAIL_CLOSED; lost task → FAIL_CLOSED; forged acceptance SHA → FAIL_CLOSED (`accepted Evidence result changed`). Worktree tracked files unchanged (only untracked tmp); canonical repo untouched (verified `git status` clean except later STEP B).
- Epistemic chain: Card/View cite 23:42:03Z + supersession + W44-pointer-only; ledger keeps MAYBE provenance + NON_MATERIAL disposition; Selection shortlist must exclude Metrics (documented in View rationale).

## STEP B canonical result (same inputs + supplement-r4, frozen Core)

- Supplement-r4 25 (21 retained with 9 midnights + GCP/paper already-null → NULL/DATE_ONLY_PRECISION, 0 `T00:00Z`; + Teams 21:29:58Z / Nemotron commits 15:12:12Z / TanStack release 15:18:14Z Oct22 / Securing RSS 10:00Z, all byte-bound). Compat-r4 SHA `8c5bebb5…` (7 projected/25 passthrough). Interactive-r4 32 VALID (runner `2026-10-25T05:00:00Z`; 19 multi-source bindings).
- Acceptances: Evidence `fb6e5900b09ee77453aeaaf904d76fb56091fc977d61f82e4154e6f3787cf72b` (`7b732c15…`, 32 PARTIAL); Views `482a084e172d20450afe45c84933f69a0074a8244f823ae8b2589279d7d3858e` (`00e24555…`, 20/10/2); ledger `31929cf5…`→new SHA (51: 20/19/10/2); completeness LIMITED. r3→r4 interactive: 7 substantive (Metrics/Teams/Kimi/Nemotron/TanStack/Securing/Vercel) + 25 identical; all 32 accepted SHAs differ (package/basis regen, not 32 claim edits).
- Stage precheck canonical CLI exit 0 (`/tmp/w43-r4-stage-precheck.json`, impl `e2fa8e935…`, State unchanged). State still `CANDIDATES_NORMALIZED`, Gates pending. No ADVANCE/operator/Human/Core/bridge/selection/prose/build.

## Frozen validators used

`validate_evidence_authority_supplement` (r4 25 PASS), compat `validate_evidence_package_basis` PASS, `validate_interactive_input` 32 PASS, `validate_evidence_card` 32 PASS, `accept_evidence_results` + `validate_evidence_acceptance` PASS, `validate_edition_view` 32 PASS, `accept_edition_views` + `validate_edition_views_acceptance` PASS, `build_materiality_ledger` + `validate_materiality_ledger` PASS, `validate_profile_completeness` + schema PASS, `survey_stage_validation_v2` CLI PASS, `survey_execution_record_v2 validate` (pre-existing Sol gaps only). Adapter: frozen native (no unit change). Core PASS = schema/integrity only; factual closure (clocks, supersession, citations) is editorial proof above.
