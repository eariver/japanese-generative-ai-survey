# J-GAS W41 — Muse r2c Pre-PDF Daily X Source Reconciliation

Status: `EXECUTION_AUTHORITY / BOUNDED_DISCOVERY_PROPOSAL_ONLY / CORE_V2_IMMUTABLE / NO_HUMAN_GATE`
Date: 2026-10-12 JST
Repository: `eariver/japanese-generative-ai-survey`
Existing work branch only: `weekly/2026-W41-v2-work`

## 1. Exact startup gate

Invoker must supply **exact Starting HEAD and Expected Starting Tree** of this instruction commit. Read-only verify:
- W41 remote HEAD and tree == values supplied by Sol;
- this instruction commit parent == `79fc6b8d83afb997ad0f6abf0c0cb96103b413c9` (Sol DailyX source audit);
- remote main HEAD == `83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8`, Tree == `31c0adc5b57761e5073d100554279a8adc5a18f4`;
- `production/survey-core-v2` remote HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- W41 canonical State == `ISSUE_INITIALIZED / stage:discovery`, both Human gates pending;
- latest r2 Discovery is still `PROPOSED_NOT_ACCEPTED`, no competing worker edits or dirty unowned local work.

Any mismatch: ZERO WRITES and report actual values. No new, repair, or fallback branch; no force/reset/rebase/rewrite. Never edit frozen W40 or Core v2.

## 2. Exact original and authority

Sol found and independently reviewed **seven pre-PDF Daily X original Markdown files**. All are already committed, so **do not re-import, re-render, normalize, or overwrite originals**.

Read in order:
1. `sources/2026-W41/execution/source-intake/w41-dailyx-original-markdown-intake-audit-r0-20261012.md` (Sol source review, link/size/time index);
2. `sources/2026-W41/external/daily-x/raw/2026-10-04_0700.md` through `2026-10-10_0700.md`;
3. `sources/2026-W41/external/x/weekly-x-2026-W41/raw/weekly-x-2026-W41-grok-result.md` + Sol Grok UTC audit;
4. `sources/2026-W41/discovery/discovery-v2-proposal-r2.jsonl`, existing crosswalk/completeness/handoff;
5. Read-only Core schema, profile, materiality and date policies.

The seven 07:00 JST observation windows concatenate to exact W41 UTC half-open interval `[2026-10-02T22:00Z,2026-10-09T22:00Z)`. They contain 92 reporting topics and 239 distinct **cited X status IDs** (238 time-in-window, 1 pre-window context). This is a source inventory, not 92 guaranteed unique events nor 239 verified claims.

A separate 14-status weekly Grok result overlaps DailyX on only 9 status IDs; 2 weekly Grok posts fall after W41 cutoff. Respect the preexisting Sol post-cutoff correction.

No `YYYY-MM-DD_0900.md` was found for any of these seven dates. The DailyX policy calls for 09:00 independent searches; do not say they ran or claim W41 X coverage exhaustive.

## 3. Required bounded work

A. Build a complete source-to-candidate crosswalk of **all 92 DailyX topics**, keyed by report date, report section, raw Markdown file, post URL/ID, raw topic importance/confidence label, official/secondary/poster claim boundary, and original event-clock vs post-clock. Deduplicate identical underlying events across separate days and the weekly Grok 14; preserve independent counter-evidence, experiments or regressions as separate observations when technically meaningful. Mark genuine time-outside-window references correctly.

B. For each topic, assign an explicit reasoned triage `EXISTING_R2_DISCOVERY / NEW_PROPOSED_DISCOVERY / CONTEXT / NOT_MATERIAL / CARRY_OVER / PRE_WINDOW / POST_WINDOW / UNVERIFIED_HOLD`. Missing original X post/authorship or primary source -> no promotion to VERIFIED, but do not silently omit unverified topic from reconciliation.

C. Independently inspect official originals for potentially significant **missing** lines (not automatic article selections):
- OpenAI `textGrain` text provenance / watermark (Oct 6 DailyX), including release/scope/algorithm claims/limitations and date;
- Google SynthID public verification portal (Oct 8 DailyX), date and supported media types vs previously known SynthID background;
- StepFun Step 5 Preview (Oct 9 DailyX), model vs provider preview, free availability periods, actual benchmarks and licensing;
- Cline Ling 3.1 Flash, local-engine Magnitude and MiniMax H3 local video demo (Oct 4), separate new model releases from wrappers/community demonstrations;
- ElevenLabs synthetic-speech detection / protocol workgroup, Nace Drex/NDI, independent Beam evaluations, new inference-serving/agent benchmark methodology; bounded technical priority only after issuer/primary checks;
- Recheck DailyX-origin threads for missing Japanese-language/research/audio content and **false quiet** classifications.

D. Maintain existing r2 primary-source results, Mistral 49B vs 52B *source-version disagreement*, and time-boundary caveats; verify any contradicting Daily X claims rather than silently overriding them. Preserve W40 carry-over HOLD disposition pending proper new evidence. Do not convert old Oct2 W40 article into W41-new event.

E. Regenerate only edition-local W41 **proposed** Discovery r2c plus timing/claim/coverage/count matrices and a `SOL_DISCOVERY_COMPLETENESS_REVIEW_HANDOFF-r2c.md`. Include a transparent before/after comparison (r2 29 rows -> r2c rows), exactly which new sources entered and which remained rejected or held. Keep reader-facing draft and Architecture untouched.

## 4. Terminal stop and validation

- W41 State stays **`ISSUE_INITIALIZED / stage:discovery`**.
- Discovery Acceptance, Screening, Evidence, Selection, Architecture and PDF generation are **not authorized** by this instruction. Return to Sol for an independent Discovery Completeness Review of combined issuer + weekly Grok + DailyX sources.
- No modification to `external/daily-x/raw/`, `external/x/.../raw/`, shared Core, W40, main or unrelated editions.
- If an actual schema incompatibility prevents proposal validation, stop with exact details rather than changing Core.
- Normal edition-local commit(s) and non-force push to existing branch only.
- Report exact final HEAD/Tree, raw untouched, all changed paths, 92-topic crosswalk counts, post/event dedup, missing required 09:00 observations, first-party verification status, new/held candidates and final Sol review target.
