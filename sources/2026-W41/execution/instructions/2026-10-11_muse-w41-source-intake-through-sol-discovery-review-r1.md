# Muse W41 r1 — Primary Source Intake + X/Grok through Sol Discovery Completeness Review

Status: `EXECUTION_AUTHORITY / EDITION_LOCAL / NO_CORE_CHANGE / STOP_BEFORE_DISCOVERY_ACCEPTANCE`
Date: 2026-10-11 JST
Repo: `eariver/japanese-generative-ai-survey`
**Existing canonical branch:** `weekly/2026-W41-v2-work`

## 0. Exact startup gate

Invoker must supply exact remote Starting HEAD and Tree (the commit containing this instruction) from Sol handoff. Before writing, read-only check:
- remote `weekly/2026-W41-v2-work` HEAD == Invoker Exact Starting SHA;
- branch tree == Invoker Expected Tree;
- current instruction file is reachable from the Sol reconnaissance commit `e12d23c0df4df00f20a62b05f83fd0b0ca1ff374` by edition-local documentation commits only; confirm the exact parent chain read-only;
- remote `main` HEAD == `83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8`, tree == `31c0adc5b57761e5073d100554279a8adc5a18f4`;
- `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20` (verify actual, do not infer tree);
- W41 canonical State `ISSUE_INITIALIZED`, next `stage:discovery`, both Human Gates pending;
- W41 Profile `WEEKLY/WEEKLY_MAGAZINE`, exact temporal bounds below, issue root and branch correct;
- no unowned local edits, unreviewed main/Core/config drift, or conflicting canonical W41 work.

Any mismatch -> **ZERO WRITES**, report actual/expected. Never create a new/fallback/review/repair branch, force/reset/rebase/rewrite or modify shared Core.

## 1. Exact scope

Window = `[2026-10-02T18:00:00-04:00, 2026-10-09T18:00:00-04:00)`, New York EDT; UTC `[2026-10-02T22:00:00Z, 2026-10-09T22:00:00Z)`.

Canonical W41 initialization ALREADY succeeded via Core v2 operator bridge (run `38148215996`, request `5fae0ad4432a2f3c74657e02c6bdcb786b53dc44`), and a corresponding Core-created Profile, State, index and session exist. **Do not initialize again.**

Read:
1. This instruction.
2. `sources/2026-W41/production-profile.json` / `production-state.json` / `execution/index.md`;
3. `sources/2026-W41/execution/source-intake/w41-sol-first-party-scout-r0-20261011.md` (leads, NOT accepted Discovery);
4. W40 final `sources/2026-W40/candidate-selection-v2.json`, architecture, `profile-completeness-v2.json`, and W40 release outcomes;
5. Core v2 read-only Source Intake/Discovery contracts, schemas and code; `config/source-intake.json` and `config/survey-production-v2.json`; W40 previous receipt/completeness audit as reference.
6. Official X/Grok profile instructions and current Daily X entries available to the operator.

## 2. Mission r1

Perform broad-but-auditable W41 Source Intake, technical triage, and make a full Discovery completeness **proposal** for Sol review. This is not an editorial Architecture decision and must not bypass accepted upstream authority.

A. Collect issuers' original source pages, version-pinned release notes/model/system cards, papers and exact linked repos where feasible; store original/faithfully bounded Raw with URLs, timestamps, retrieval timestamp, source type and any immutable hashes under W41 edition paths. Keep claims from marketing and independently verified claims separate. Track exact release versus future promised availability. Explicitly disclose inaccessible source bytes (do not invent them).

B. Investigate all first-party r0 leads (GPT-6/Intelligent UI, Haiku 5.5, Mistral Large 4, Reflection Beam, Decisions beta, Ultrafast, mathematics, Ironclad, Anthropic cyber policy/mission, Gemini work agent, llama.cpp v0.6.0, Oct9 model behavior report) **as candidates only**, not mandated selections. Reconcile Mistral Large 4 active-parameter documentation 49B versus 52B with source-version pins before repeating either numerically. Locate model-weight/license truth rather than equating `open-weight` intention with actual downloadable bytes.

C. Separate **event timestamp** from URL update and product availability. For any Oct 9 day-only event (e.g., possible Clef-omni or Anthropic unintended-model-actions paper), determine whether the event occurred before 18:00 EDT; unknown -> time HOLD/CONTEXT, not fabricated positive. W40 post-window candidates Oct 6 and Oct 8 are in scope for W41 (new event only if publisher pin confirms).

D. Recheck all W40 HOLD/carry-over obligations with item-specific new W41 evidence:
   1. Pixel Canary (source availability/outage status history)
   2. TBC Video (independent measured technical evidence)
   3. Ai2 AstaBrief 8B
   4. ServiceNow AutoSynthData.
   The last two were original Oct 2 W40 articles held because frozen Core did not offer lawful Evidence supersession (#562), **NOT** because timestamps were unknown. Do not claim them as newly released W41 models without new W41 dated events. Honor deferred Core ownership.

E. Mandatory X/Grok and Daily X:
   - Create issuer/original-status-URL-oriented Grok task for W41 under the analogous `Grok_X_SourseIntake/Weekly/2026-W41/weekly-x-2026-W41` folder if access permits, with repository-source task and exact content/provenance. Do not claim raw Markdown bytes equal a native Google Doc representation.
   - Request verifiable `x.com/.../status/<id>` links with author, UTC time, subject, bounded claim and negative-space reporting. Keep X opinion/reaction distinct from primary model/repo announcements.
   - If Grok cannot be launched or result isn't returned, mark `AWAITING_GROK` and complete lawful independent first-party preparation without falsely passing the X lane. Import returned raw bytes unmodified and reconcile stated post counts vs observed URLs; use Daily X for independent cross-check, with explicit coverage gaps.

F. Comprehensive domain coverage beyond frontier model announcements: open models & local execution; image/video/audio/multimodal; agent/tool protocols and evaluation; inference performance, quantization, GPU serving; learning methods and data; reasoning/science; safety/cyber; Japanese domestic technical work. Dated negative space where no worthy source found; don't create filler candidates.

G. Prepare edition-local Discovery source index and a **proposed, schema-validated (not accepted)** Discovery JSONL, normalizations, timing matrix, carry-over table, completeness report, unresolved-source list, and exact claim-to-source citations. Show both major materiality candidates and why weak sources weren't selected at proposal level. Prevent silent inclusion of vendor metrics as independent results.

## 3. Scope ceiling / stop

- **Do not** canonically accept Discovery or advance State to DISCOVERY_COLLECTED/CANDIDATES_NORMALIZED without Sol assessment of the completed proposed discovery surface.
- Do not start Screening/Evidence/Selection/Architecture or draft an issue PDF in this first unit.
- No new branches, no shared Core/scripts/config/schema/workflow changes, no changes to W40 frozen sources.
- Do not promote HOLD on inference; no invented Human Gate approval; no process metadata in future reader prose.
- Treat entire r0 Sol lead list as provisional; favor primary technical detail and evidence over article count.
- Keep local source snapshots/source evidence and clear mapping to the half-open W41 window, not ever-changing news-page screenshots alone.

Terminal: remote W41 branch with noncanonical first-pass Source Intake/Discovery Proposal + X manifest disposition, **State still ISSUE_INITIALIZED**, a Sol Discovery Completeness Review handoff, normal commits/push (force=false), exact HEAD/Tree and all changed file paths reported. Stop until Sol reviews the package.

## 4. Final report

Final W41 branch SHA/Tree, reviewed main/Core SHA, canonical State identity, primary-source count and date/class confidence, X/Grok raw receipt status and count reconciliation, carried-over item dispositions, completeness coverage by lane, top uncertainty/blockers, location of proposal/review dossier, number and dates of source samples. Be exact: `PROPOSED_NOT_ACCEPTED` must not be misreported as a canonical Discovery PASS.
