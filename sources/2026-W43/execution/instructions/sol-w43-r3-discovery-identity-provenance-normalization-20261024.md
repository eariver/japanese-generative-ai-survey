# W43 Sol → Muse r3 — LIMITED Discovery canonical-record reconciliation

Status: `LIMITED_REQUEST_CHANGES / PROVENANCE_AND_DEDUP_ONLY / NO_STAGE_ADVANCEMENT`
Date: 2026-10-24 JST
Repo: `eariver/japanese-generative-ai-survey`
Branch: `weekly/2026-W43-v2-work`
Authority: `sources/2026-W43/execution/reviews/sol-w43-discovery-completeness-review-r2-20261024.md`.
Muse r2 reviewed HEAD/Tree: `ab69aed74c1c6418ece2842796830134d63fbc30` / `dda0b894194a6ee27cebc11dea458cc7bc167e3d`.
Reviewed `main` HEAD/Tree: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen Core branch HEAD/Tree: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

**Exact Starting HEAD and Tree for this r3 contract will be the live remote post-contract commit/Root Tree supplied by Sol separately.** Verify current remote `weekly/2026-W43-v2-work`, `main`, Frozen Core fully match those 6 expected values read-only. Mismatch => **ZERO WRITES** and report expected/actual. No fallback/repair/review branch, resets, rebase, force push, history rewrite.

## 1. Scope: one correction pass, no new thematic research

Read Sol r2 verdict in full. r2 editorial **technical/source coverage is substantially adequate for a provisional Discovery candidate pool**, pending Grok/X and stronger Evidence later. Do NOT repeat broad Source Intake, model news search, full article analysis, raw GitHub commits or Core internals research.

Scope ONLY:
A. Active canonical r3 Discovery proposal data consistency, event deduplication, corrected dates/source bindings.
B. r1/r2 exact provenance integrity / impossible collection clock remediation with transparent errata (no fake time).
C. A concise r3 Sol review handoff, ledger and machine schema/graph checks.

`sources/2026-W43/discovery/discovery-v2-proposal-r1.jsonl`, `...-r2.jsonl`, and all historical r1/r2 bundles/receipts are immutable. No modification/deletion to historic proposals to hide errors.

## 2. Required corrections, acceptance assertions

- r2 appended a separate Kimi corrected record while leaving r1 original at 21:15Z; normalize one **announcement/API event** at official UTC `2026-10-23T17:15:24Z` (13:15:24 EDT) with raw X locator 19-digit ID and weight availability still FUTURE. No two active rows representing same event.
- AM-Bench v1 (`2026-10-16T21:46:19Z`) OUT; v2 (`2026-10-20T15:40:19Z`) IN only as **revision**, pending substantive delta. No active contradictory "time unknown" family row. OR-License v1 `2026-10-16T18:13:25Z` OUT; no duplicate contradictory "unknown" row.
- DeepInfer original repo Oct 16 OUT vs Oct 20 distribution/announcement IN; MOSS code/weights Oct 16 OUT vs trainer Oct 18 / report-announcement Oct 19 / API Oct 20 IN are genuinely distinct event identities. Preserve separate events with explicit family links. Model original and announcement are NOT the same technical release.
- Nemotron E4B **64K** context from the checked original page, not 1M for a different model. Discovery active authority links must reference actually consumed r2 bodies (note-level) and related source provenance; avoid claiming original HTML bytes for render notes.
- Preserve stable IDs where it does not misrepresent identity; provide a complete `51 old r2 IDs -> active r3 ID, merged/retained/excluded` map with rationale. If a row remains as background or out-of-window, mark it explicitly (not in-window news) and show why it is distinct. All active IDs unique and semantic event-family dedup assertion PASS with supporting mapping.
- Every active row must contain non-contradictory `source.published_at` and event type / revision / cutoff treatment (schema permits null but avoid unnecessary null where verified exact UTC exists). Preserve publisher vs independent measurement distinction.

## 3. Provenance/time correction

- r1 GitHub commit `57afcd292d946078ae03900bd242b6f0b4f7de60` authored/committed `2026-10-24T11:20:22Z`, while source `observed_at` uniform `2026-10-24T12:00:00Z`. This is impossible for already-committed r1 content. Review actual available capture/session logs. Never invent a time or substitute commit time as if observation happened then. If true source read timestamps cannot be reconstructed, mark those historical observation clocks INVALID and reobserve relevant canonical sources **now** using truthful actual UTC. In the r3 proposal bind new r3 observations and unchanged historical claims/source artifacts with an explicit errata bridge. Do not alter r1 bytes.
- r2 commit `ab69aed74c1c6418ece2842796830134d63fbc30` committed `2026-10-24T11:56:58Z`, but its collector label/path `20261024T133000Z-muse-r2` misleadingly encodes a time later than commit by 1h33m02s. Its `observed_at=11:50Z` can be legitimate if supported. Keep immutable r2 path but record run_id as **OPAQUE/MISNAMED**, not a real timestamp. Use real measured current UTC in all newly written r3 paths/metadata.
- Five GitHub repo "raw metadata" JSON files appear to contain a selective field projection (six short keys), not complete returned API-body bytes. Verify recording method. Unless raw unmodified response body can be proven, reclassify them `DERIVED_GITHUB_API_FIELD_PROJECTION` in new records, leaving byte hashes valid for the local projection, not claiming original API exact-byte capture.
- Kimi X HTML may still be reported as actual raw captured source if its HTTP bytes and embedded timestamp validated; do not conflate X HTML capture and Grok result.
- Emit a machine-readable or human-readable `w43-provenance-time-errata-r3` with observed-at status for each legacy batch, original vs corrected interpretation, source of proof, and impact on canonical active proposal.

## 4. Stage/X/Git prohibitions

- `x-source-intake-v2.json` remains `AWAITING_GROK` until real Grok original result is captured and Sol imports/validates. Google Drive currently has a **task** at https://docs.google.com/document/d/1BubHtxps3Lg711pDJKfoNwe8AyeND7miT9hMQwSnsjw/edit, not a result.
- No trusted `ADVANCE_STAGE` request in r3. Keep `ISSUE_INITIALIZED` / `stage:discovery`, no accepted Discovery claim. No Screening/Evidence/Selection/Architecture, Human Gate, PDF or Release.
- No shared Core files, workflows, tests, `AGENTS.md`, W42 state/release/Issue #570 edits. Edition-local normal commits + non-force push only, exact remote readbacks.
- Verify r3 proposal schema **and** Core graph provenance validation and source paths; present candidate-family duplication audit, temporal reconciliation and actual git parent chain. Tool PASS alone is not semantic PASS.

## 5. Output and stop

Create `discovery-v2-proposal-r3.jsonl`, `execution/source-intake/w43-discovery-identity-reconciliation-r3.md`, `execution/source-intake/w43-provenance-time-errata-r3.md`, bounded session record, Sol handoff and index update, with source byte hashes where appropriate. Avoid overwriting r1/r2 artifacts.

Report original 51 records, retained/merged/excluded records and **canonical active event-family count**; what was corrected and what is still conditional. Stop at `SOL_DISCOVERY_COMPLETENESS_REVIEW_READY_R3` and give exact Final remote HEAD/Root Tree.

If a missing real observation timestamp cannot be reconstructed and honest rebinding is not feasible, stop `BLOCKED_PROVENANCE` rather than backdating/forging metadata.
