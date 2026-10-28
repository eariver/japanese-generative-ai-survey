# W43 Sol → Muse Evidence r3 — Patch exact model and primary-source identity + MemT README provenance

Status: `BOUNDED_FACTUAL_PROVENANCE_CORRECTION / NO_STAGE_ADVANCE`
Date: 2026-10-25 JST
Repo: `eariver/japanese-generative-ai-survey`
Branch: existing `weekly/2026-W43-v2-work` ONLY
Sol reviewed r2 work HEAD/Root Tree: `8aeafe90c43e44a96a1b181c0d3b685046e1433d` / `a53b75069b8a72df092c84365822368690f14132`.
Sol ruling (must read IN FULL): `sources/2026-W43/execution/reviews/sol-w43-evidence-r2-factual-provenance-review-20261025.md` (`EDITORIAL_REQUEST_CHANGES`).

**Exact Starting HEAD/Tree for this new execution unit will be sent by Sol after this instruction and index are committed.** Start with read-only 6-way preflight: remote W43 HEAD+root tree exactly dispatch expected; main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6` Tree `a134dc36a407d08ab1de416324229b3955e0325a`; frozen `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. Any mismatch → STOP ZERO WRITES with actual vs expected. No fallback, new/review/repair branch, force push, rebase, reset, Core modifications.

## 1. Trust boundary and immutability

- Production State `CANDIDATES_NORMALIZED` / `stage:evidence-materiality-completeness` (two earlier machine checkpoints passed); Human Architecture/Publication Gates PENDING. Valid accepted Screening r3 `screening/v2/accepted/75dd95db5c40b28cc2d9a665dab8a46294e010096095c2bf92aba36d5ed9817d/screening-accepted.json` and Discovery 51; never rewrite. Thirty-two non-DROP Evidence records include one Grok audit-binder NON_MATERIAL; Frozen Core untouched.
- Preserve accepted r1 Evidence `evidence/v2/accepted/1272d6c1598ab526d89495fd8e00184af1c64d43445fce3ce5a3eecb7b34aa97/`, Views `97586879563080bead28fa7dafdfd17af987ec5ba307df19c2bad9be1c335ddf` AND r2 Evidence `evidence/v2/accepted/3e7fa82772523bdb9303190c64ecd5f9a515e8493261fe6826332b2e94ddb37a/`, Views `c4e0ce931ec176ae56ad0c32483fca599023e2fc8060861b4f1c2771d6f3190c`; NEVER alter these immutable content-addressed directories. Preserve r1 and r2 supplements/raw and r1 history. Snapshot r2 current `materiality-ledger-v2.json` and `profile-completeness-v2.json` into `execution/history/r2/` (actual SHA manifest) before overwriting canonical paths.
- r2 Core machine PASS is genuine per worker report; this r3 corrects **content-level facts and provenance** missing from Core schemas. No broad new source collection, source-list reset, repeat Discovery/Screening or Selection.

## 2. One model error that MUST be repaired

- Exact accepted r2 Patch Card ID `w43-primary-patch-planet-20261021`, result file `task-5d21d93e7679f5441b8a.json`, claim-1 currently says `Calif via GPT-6 Sol`.
- Official **OpenAI** Oct 21 2026 source `https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/` and Japanese official article `https://openai.com/ja-JP/index/coordinated-disclosure-of-critical-vulnerabilities/` both explicitly say **`GPT-5.6 Sol`**. Update to exact publisher wording, preserving that this is a VENDOR_CLAIM about Calif's PHP critical bug finding, NOT independently reproduced and NOT an automatic CVE attribution.
- Search all **new derived** r3 claims/view rationale/editorial notes for wrongly carried `GPT-6 Sol` as the Patch case and fix only this case. Never rewrite original historical r2 Evidence.
- Distinguish *Patch initiative model* vs any other legitimate GPT-6 Sol reference in separate stories; no global blind replace.

## 3. Two exact provenance linkages

### Patch primary publisher binding

- r2 Patch Card `sources[0].url` is `primary:openai.com/index/patch-the-planet`, an **old discovery observation locator**, not the actual official article consumed for claim-1 and the 5-stage framework. It must NOT be misrepresented as an exact source URL for specific claims.
- Use frozen `evidence-authority-supplement-v2.schema.json` to bind an authentic task-scoped first-party source **at exact URL** `https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/`. Try genuine raw HTML fetch; if bot-walled, preserve a bona fide retrieved **rendered markdown/text extraction** with precise fetch/observation time, source URL, original-vs-derived capture class and its **actual saved bytes/SHA256**, with no claim it is publisher-origin HTML or independently reproduces the incident. Check the frozen source_type and task binding rules. If no genuine source artifact can be archived and validated by Core, make exact URL resolution with publisher-section references in new W43 provenance ledger and **STOP BLOCKED if the content claims cannot be truthfully bound**; no homemade Core bypass or fictitious raw bytes.
- In *new* Patch Card, include real source ID for the official article on each factual statement that depends on it. Keep original accepted Discovery and Screening untouched. Citation crosswalk must distinguish original `src-1` screening locator from exact supplementary source and not assert they are the same URL.

### MemT license README binding

- r2 MemT Card `w43-r2-memt-20261019` cites only `src-1` arXiv and `supplement-src-927931f4a303eaa6` (real MemT 7,096,280 B paper PDF) while claiming `CC BY-NC-SA / PolyForm Noncommercial` terms are ONLY in repository README, NOT the paper itself. This is **missing claim-level authority**.
- Identify actual authoritative MemT upstream repository README from the previously consumed r1/r2 sources; fetch and save authentic README bytes/URL/sha/actual commit/ref or access datetime, bind via exact existing frozen Core supplement API as a task-scoped `PRIMARY_REPOSITORY` (or correct supported class), without assigning paper the license provenance. Validate precise paper/repo/code/weight/dataset licensing distinctions from actual text. If no authentic current README, delete or downgrade unsupported license assertions and leave verification `UNRESOLVED`; never fabricate a license.
- Keep actual MemT PDF archive and architecture/benchmark textual author claims. Correct ambiguous r2 `tech-report-pdf` finding (says PDF's 'license sections' consumed although the PDF contains no license) with precise evidence: paper sections checked and no license statements found, README is separate.

## 4. Documentary errata (historical r2 files unchanged)

- Actual starting work parent `6a3898771038d64fc2cd6a911c4445177d43a8e2` has true Root Tree `b8e1a207edb3cc82927284241e486ce468360642`; r2 worker session/handoff mistakenly wrote `b8e1a207edb3cc92827284241e486ce4683612`. W43 r2 git parent and remote preflight HEAD were correct; r3 erratum must state exact old vs actual Tree and no claim of a different history.
- Actual `external/evidence-supplement/evidence-authority-supplement-r2.json` has **6** `sources` entries (2 carried r1 paper + 4 newly added: Anthropic article, OpenAI API changelog, Google Cloud HTML, MemT PDF), NOT 8 asserted by worker handoff. Explain this count only in errata; do not tamper frozen r2 supplement.
- `VERIFIED` target statuses mean publisher text or raw was read, not independently reproduced benchmark/capability. No independent reproduction claimed.

## 5. Core regenerated outputs, assessment, and stop

1. Revalidate true agent-first State, exact r2 accepted Evidence/Views/Materiality/Completeness, 32 IDs (PARTIAL 32), 7-ID derived-only source-class projection, X `COMPLETE` registration/`PARTIAL` sensor. Frozen Core adapter `scripts/survey_agent_tool_v2.py` unchanged; Issues #568/#569 remain OPEN.
2. New **r3** source supplement and derived Evidence package with actual new first-party source binding(s). Keep existing six supplement entries identical unless schema forces a truthful versioned update, add Patch and MemT README if authentic. Map added source IDs only to their owning Evidence task. Preserve all other source binding and hashes with recorded diff.
3. New **r3** interactive input: the 27 unaffected r2 records **semantically identical**, and original four first-party gap repairs preserved. Change ONLY Patch case source/claim and MemT repo/license/provenance; no invented fresh metrics. Use accurate proof and materiality reasoning for these two; preserve 20 MATERIAL/11 CONTEXT/1 NON_MATERIAL as starting point unless real new source fact justifies change. Core accepted run will have different task/Card/View hashes; distinguish those mechanical differences from content changes.
4. Rebuild using frozen first-party `survey_agent_tool_v2.current_stage_basis_override` and W43/W42-reviewed **edition-local 7-ID projection**. Generate **32 canonical Evidence Cards + 32 Edition Views**, new content-addressed accepted paths, 51-row Materiality ledger, Completeness (may remain `LIMITED`). Original r2 accepted folders immutable. Run actual frozen Core `validate_acceptance` + `survey_stage_validation_v2` scratch precheck `CANDIDATES_NORMALIZED`→`EVIDENCE_REVIEWED`; agent-first State before/after, original source SHA/bytes and negative source-binding and tamper tests; validate execution-record format. Report actual stdout/error codes, no claim that legacy direct helper is fixed.
5. Create factual correction ledger: source evidence section+URL for `GPT-5.6 Sol`, prior `GPT-6 Sol` error and precise before/after; exact Patch claimed `src-1` vs actual source-binding resolution; README license strings with own source_id and no paper assertion; 6-vs-8 and Starting Tree transcription errata. Include 32-row r2→r3 semantic diff accounting (original 30 other than Patch/MemT remain identical), exact r2/r3 accepted SHA256, Materiality/Completeness and actual residual limitations.
6. Update W43 `execution/index.md`, new session `execution/sessions/muse-w43-evidence-authority-r3-20261025.md`, handoff `execution/SOL_EVIDENCE_MATERIALITY_COMPLETENESS_REVIEW_HANDOFF-r3.md`, normal commit and non-force push same existing work branch, remote HEAD/Root Tree readback.
7. Strict stop `SOL_EVIDENCE_MATERIALITY_COMPLETENESS_REVIEW_READY_R3`; if true source binder / Core accept fails, `BLOCKED` with exact diagnostics and NO fake PASS. **Do not** `ADVANCE_STAGE`, create Issue #448 comment, begin Selection/Architecture/Draft, or modify Human Gates. Frozen Core, main, W42, X Grok Original, canonical Discovery/Screening, Production State and machine Checkpoints unchanged. Sol will independently review before trusted Stage transition.
