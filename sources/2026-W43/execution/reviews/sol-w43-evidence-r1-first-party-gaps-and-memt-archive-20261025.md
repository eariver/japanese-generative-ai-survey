# W43 Sol independent Evidence r1 audit — machine PASS, editorial REQUEST_CHANGES before Stage

Status: `SOL_EVIDENCE_R1_REVIEW / CORE_MACHINE_PASS_REPORTED / EDITORIAL_REQUEST_CHANGES / NO_STAGE_ADVANCE`
Date: 2026-10-25 JST
Repository: `eariver/japanese-generative-ai-survey`
Reviewed W43 HEAD/Root Tree: `1aba42fc0a03a9035268e18b695ccc4f758d7116` / `173ed0d433fa148119215abf0c84fd758ba9ff6c`
Exact parent/start: `f8c7a41f8829fb6990163073090b414d84075101` (normal FF)
Reviewed main HEAD/Tree: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`
Frozen Core v2 HEAD/Tree: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

## Reviewed authority

- Worker r1 handoff `execution/SOL_EVIDENCE_MATERIALITY_COMPLETENESS_REVIEW_HANDOFF-r1.md`, session `execution/sessions/muse-w43-evidence-authority-r1-20261025.md`, depth ledger `execution/source-intake/w43-evidence-source-depth-r1.md`, 32-record `execution/compat/evidence-source-class-projection/interactive-evidence-r1.json`, 7-ID projection ledger, exact two PRIMARY_PAPER supplemental PDFs (Oracle and AM-Bench), all Core accepted Evidence/Views, materiality and completeness.
- Accepted Evidence `evidence/v2/accepted/1272d6c1598ab526d89495fd8e00184af1c64d43445fce3ce5a3eecb7b34aa97/evidence-accepted.json` has **32** results: PARTIAL 28, NEEDS_MORE 4; 32 corresponding Views `evidence/v2/views/accepted/97586879563080bead28fa7dafdfd17af987ec5ba307df19c2bad9be1c335ddf/edition-views-accepted.json` have MATERIAL 17 / CONTEXT 10 / NON_MATERIAL 1 (Grok binder) / HOLD 4.
- Materiality `materiality-ledger-v2.json` 51 disposition rows (17 MATERIAL / 10 CONTEXT / 4 HOLD / 1 NON_MATERIAL / 19 EXCLUDED); Completeness `profile-completeness-v2.json` overall LIMITED, current relevance LIMITATION, technical significance LIMITATION, carry-over SATISFIED. All 12 W42 carry IDs accounted.
- Core hashes: Evidence acceptance SHA256 `2c3ccb1f36cbda3a071e9b7640ef976d7469f89283d1c8ad1406fa2dba30f15f`; Views acceptance `94797fb341b83f696d9796b4183edb505d48bf5ed674eac685b2cbc3b26c7929`; materiality ledger `3c36ed7ab3f4b7328e2c76839437b2cd0021fd80bed51a61bbe9397f831ef4c9`. Worker reports native frozen Core checks and agent-first Stage precheck PASS plus negative tamper checks PASS. Sol independently read back and compared structural Core authorities / materialized Card examples but did **not** independently run the worker CLI; structural PASS ≠ technical-content acceptance.
- Seven non-DROP records use unsupported legacy Evidence source types; worker derived-only projection `execution/compat/evidence-source-class-projection/projection-ledger.json` 7 projected / 25 passthrough, with explicit identity/hash; original Discovery and Screening unchanged. Source-class incompatibility is known Issue #569/CV2-DM-016, agent-first State admission Issue #568/CV2-DM-023; frozen Core is unchanged. No Git mutations outside W43 edition-local were reported; actual 145-file changed commit is W43-only.
- Source-depth honest limitations: existing (r2/r4) rendered page reads mostly reused and not byte-archived; in r1 only AM-Bench v2 PDF (2,379,235 B) and Oracle evaluation v2 PDF (261,750 B) were newly collected as PRIMARY_PAPER supplement; no independent model/benchmark reproduction. The six or more large-scope engineering claims need later author/publisher vs independent distinction and actual source evidence.

## Human decision

**NONE / NOT_APPLICABLE.** Sol Evidence source-quality editorial review is not Human Architecture Review or Publication Preview. Both actual Human Gates remain pending. **Do NOT advance to EVIDENCE_REVIEWED now.** Decision: `EDITORIAL_REQUEST_CHANGES` despite true machine-validated r1 artifacts. Old accepted r1 stays immutable as evidence of actual first-pass work.

## Requested changes

### CR-01 — Four HOLD/NEEDS_MORE rows have available in-window FIRST-PARTY bodies, and r1 did not inspect them

Worker r1 marked all four INSPECT rows NEEDS_MORE/HOLD and says official pages were not fetched/consumed. Sol independently found authoritative public publisher bodies. This is not an unavoidable information gap; the existing r1 contract explicitly requested first-party source collection where available.

1. `w43-primary-decisions-api-20261022` **official Oct 22 GA**, not simply RSS-title availability: `https://openai.com/index/decisions-api/` and `https://developers.openai.com/api/docs/changelog`. Official description: Luna-based `v1/decisions`, three bounded answer types (predicate/choice/score), text/image/JSON, up to 400 questions, caching, GPT-Live integration, 10x latency claim vs Responses API (vendor-claimed), publisher price $0.10 / $0.01 cached per 1M input tokens. Need exact GA vs Oct6 beta distinction and no false independent latency confirmation. Publisher content corroborated by `https://openai.com/ja-JP/index/decisions-api/`.
2. `w43-primary-patch-planet-20261021` official Oct21 case: `https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/`. Original Evidence says page-body unfetched, no CVE or process. Official publisher documents critical PHP vulnerability coordination with maintainers, Wiz and Cloudflare, disclosure/mitigation. Check exact disclosed CVE identifiers, timeline, security boundary and disclosure source rather than manufacturing them. Distinguish this from separate Oct23 frontier-training containment and unrelated W42 unverified allegation.
3. `w43-primary-openai-cloud-20261021` official Google Cloud Oct21: `https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers`; official OpenAI news `https://openai.com/ja-JP/news/` links Oct21 Google Cloud availability. Google describes OpenAI models in Model Garden with governance/enterprise distribution. Verify actual SKU/product availability, routing, region/data controls separately.
4. `w43-primary-automode-20261021` official Anthropic article `https://claude.com/resources/articles/auto-mode-default-in-claude-code`, published Aug7 **OUT** but with clearly stamped **Oct22 in-window update** saying auto mode default rollout **next week** for new sessions in most Claude apps (Pro/Max/Team), risk classifier and Enterprise notices. Distinguish original historical product publication from Oct22 update and FUTURE rollout; verify any Oct21 distinct X first-party event rather than re-date Aug7 article. Do NOT infer rollout is already complete within W43.
   
Do actual new source accesses (not merely copy this review), record exact official URL, actual document timestamp/access time, publisher, content capture depth, claim-to-source maps and archival bytes+SHA where obtainable (no fabricated raw). Record an explicit chronology and event-identity ledger. Re-evaluate four row Evidence statuses and View/Materiality **on observed content**, no quota or forced MATERIAL promotion. Also compare these with 17 original MATERIALs: where a previously held release has higher technical significance than context-only events, discuss editorial implications and overlaps. Full Stage authority must be newly generated and validated.

### CR-02 — MemT report falsely described as archived (source identity/data-integrity error)

Accepted Card for `w43-r2-memt-20261019` (task `evidence:2026-W43:8c735edcfc5e51f3`; result file `task-b09782ca929b9fa55af1.json`) verification target `tech-report-pdf` says **`PDF archived (2.38MB); abs plus intro consumed; full body unread.`**. Its claim-2 context also says `PDF abs+intro consumed`. BUT r1 Git commit archived only two PDFs: **2,379,235B AM-Bench v2** and **261,750B Oracle v2**. The supplement has precisely those two sources, **not MemT**. The 2.38MB figure belongs to AM-Bench, so the MemT archive assertion is false/conflated. Correct the interactive source and generated Card only in NEW r2 authority; preserve original r1. Either actually fetch/archive the **real MemT PDF** and its own SHA, consume relevant mechanism/results sections, or change verification to accurately say paper abstract + repository README (and any actually documented nonarchived read) without claiming PDF bytes exist. In either case, evidence strength, claims and materiality must reflect actual source consumption. Inspect for similar cross-topic source/byte-count conflations elsewhere.

### CR-03 — Review Materiality and Completeness after source remediation

All 17 KEEP became MATERIAL, all 10 research MAYBE became CONTEXT, and all four INSPECT became HOLD in r1. These dispositions are not automatically wrong, but Core acceptance cannot substitute for **independent editorial per-record significance**. Four accessible official body gaps materially undermine the current HOLD conclusions. Reassess positive/negative materiality with separate technical contribution, proof quality, in-window novelty and overlap. Correct per-item profiles and completeness obligations; don't blanket-upgrade `LIMITED` to SATISFIED. Preserve the Grok sensor binder as non-story NON_MATERIAL and 19 excluded original DROP as excluded.

## Regeneration boundary

**Bounded W43 Evidence/Materiality/Completeness r2 source-authority deepening and rebuild ONLY**. No changes to shared/frozen Core, main, W42, accepted Discovery, corrected r3 Screening, X Raw, prior accepted r1 Evidence/Views, production State/checkpoints or Human Gates. Use new exact first-party supplementary authority with task-bounded provenance, reviewed derived-only source class mapping and frozen agent-first `survey_agent_tool_v2`. New content-addressed Evidence/Views accepted paths and dependent materiality/completeness will necessarily get new hashes. Run genuine frozen Core validation, negative tamper/fake source tests and Stage precheck in scratch. If missing evidence, use PARTIAL/NEEDS_MORE and explain honestly rather than forge completeness.

Stop `SOL_EVIDENCE_MATERIALITY_COMPLETENESS_REVIEW_READY_R2`; do **NOT** ADVANCE_STAGE, create operator request, run Selection, Architecture, manuscript/PDF, or Human approval. Sol will independently inspect source-body crosswalk, new Card content, 32-to-32 effects, and source handling before authorizing bridge.

## Shared-Core implication

**No newly diagnosed Core defect**. Existing native agent-first adapter works, derived source-class compatibility remains tracked in Issues #568/#569, frozen Core unchanged. The two substantive defects are edition-local: accessible first-party bodies not consumed, and an incorrect MemT PDF archival claim. Do not report old legacy verifier repaired.
