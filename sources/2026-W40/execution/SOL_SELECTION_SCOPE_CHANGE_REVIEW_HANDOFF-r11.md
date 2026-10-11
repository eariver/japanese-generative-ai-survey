# SOL_SELECTION_SCOPE_CHANGE_REVIEW_HANDOFF-r11 (Muse bounded r11 → Sol)

Status: SOL_SELECTION_SCOPE_CHANGE_REVIEW_REQUIRED (proposed terminal; Sol adjudicates)
Work branch: weekly/2026-W40-v2-work
Starting SHA/Tree: e45a845db406392191a819f5a99b0c68bc36d97c / f045911d565c8e7b9243a65af1ee72df0b763d89
Reviewed main: afdb3df3faa20af3bb5798be429bba8dbd2100b1
Production State: EVIDENCE_REVIEWED (unchanged); next stage:selection;
Selection/Architecture pending; Human Gates pending.
Sol adjudication in: execution/reviews/sol-w40-selection-r10-scope-adjudication-20261010.md
R11 contract: execution/instructions/2026-10-10_muse-w40-hf-publication-timing-and-core-reentry-r11.md
R11 outputs (all staged W40-local, NO canonical mutation):
- execution/host-timestamp-ledger-r11.md (original JSON-LD, SHAs, artifact distinctions)
- execution/selection/selection-counterfactual-r11.md (Plan A vs Plan B, P6a/P6b kept)
- execution/core-reentry-feasibility-r11.md (CORE_REENTRY_CONTRACT_GAP + minimal fix)
- execution/sessions/muse-w40-r11-20261010.md (run log)

## 1. Start-Guard note (read-only verification + one FF alignment)

- Remote branch HEAD (ls-remote): e45a845db406392191a819f5a99b0c68bc36d97c — MATCHES expected.
- Remote Tree (rev-parse e45a845^{tree}): f045911d565c8e7b9243a65af1ee72df0b763d89 — MATCHES.
- Remote main HEAD (ls-remote): afdb3df3faa20af3bb5798be429bba8dbd2100b1 — MATCHES.
- Ancestry: reviewed-main afdb3df IS ancestor of e45a845; e45a845 parent = 4dd18ff
  (Muse r10) — descended as required.
- Workspace was 1 commit behind (local 4dd18ff / tree 4ef46ebe…, origin tracking stale)
  due to the interrupted pre-run; per outer instruction ("Start Guardは無視して状況を
  確認して続行") verified remote first (ZERO WRITES), then `fetch + merge --ff-only`
  to the exact Starting SHA/Tree (no reset/rebase/force/new-branch; untracked
  scripts/__pycache__/ untouched). Post-alignment HEAD/Tree == expected.

## 2. Primary-source verdicts (HF official org articles; details in ledger)

- AstaBrief (https://huggingface.co/blog/allenai/astabrief): org `allenai` + author
  Ai2Comms/Kyle Wiggers + first-person Ai2 prose VERIFIED; JSON-LD datePublished =
  dateCreated = 2026-10-02T15:19:50.340Z (modified 15:22:07.584Z); canonical link OK;
  raw 169,199B, SHA-256 d440b900…. IN-WINDOW (≈6h40m margin). Article event proven;
  allenai.org hour NOT proven (RSS day-only; CMS asset names corroboration only);
  weight/dataset instants DISTINGUISHED (8B created Feb 9; SFT Sep 10; SFT/DPO mixes
  lastModified Sep 29; licenses apache-2.0 weights / cc-by-nc-4.0 data; 2025-era
  baselines; eval-not-rerun caveat).
- AutoSynthData (https://huggingface.co/blog/ServiceNow-AI/autosynthdata): org
  `ServiceNow-AI` + 4 ServiceNow-AI-badged authors + first-person CoreAI prose
  VERIFIED; JSON-LD datePublished = dateCreated = 2026-10-02T04:01:31.290Z
  (modified 04:05:48.837Z); canonical link OK; raw 210,484B, SHA-256 d84a35e6….
  IN-WINDOW (≈18h margin). METHOD ANNOUNCEMENT proven; standalone code/weights/
  dataset release ABSENT (no public AutoSynthData model/dataset/pipeline code);
  EnterpriseOps Gym (Feb 28/Apr 30, apache-2.0, arXiv:2603.13594) DISTINGUISHED as
  background; Hybrid +7.2pp/35% and ITSM 18.77%→27.18% are publisher-measured,
  Gym-scoped, SFT-only; target/multiply + sample/batch + positive/negative gates
  and limits preserved.
- Old TIME_UNRESOLVED HOLD justification for the ARTICLE-EVENT question is SUPERSEDED
  for both. No MATERIAL/SELECTED formal change made (per contract).

## 3. Materiality + article-allocation judgment (for Sol; not an acceptance)

- Both are MATERIAL in-window candidates: AstaBrief = only open-weights cited-report
  model+data release with grounding lessons; AutoSynthData = only
  environment-validated synthetic-curriculum method with explicit verifier gates.
- Allocation: AstaBrief → P6a (training-methods-and-systems) as third PRIMARY;
  AutoSynthData → P6a as fourth PRIMARY (methods); P6b UNCHANGED; P6a/P6b depth kept;
  P1–P5/P7/P8 unchanged. Full A-vs-B comparison in counterfactual file.
  Recommendation: Plan B (30 SELECTED = 22 PRIMARY / 8 SUPPORTING) IF Sol authorizes
  lawful re-entry; else Plan A only with rewritten scope-based HOLD rationales.

## 4. Core re-entry route (for Sol; not executed)

- NO lawful frozen-Core post-EVIDENCE_REVIEWED upstream-amendment path exists:
  transition_state is forward-only; invalidate_pending_gate has no pending Gate at
  EVIDENCE_REVIEWED (gate_at_state maps only ARCHITECTURE_ESTABLISHED/RELEASE_CANDIDATE;
  terminal null; architecture pending). ⇒ CORE_REENTRY_CONTRACT_GAP (confirmed).
- Minimal fix + exact allowlisted regeneration plan (2 Discovery / 2 Screening /
  2 Evidence+Cards / 2 Views / 2 Ledger rows / Completeness re-validation / Matrix +
  Selection rebuild; same-state supersession with old-SHA lineage, no rewind) in
  core-reentry-feasibility-r11.md. Shared Core NOT touched here.

## 5. Unresolved doubts / carryovers (unchanged scope)

- HF byte SHAs are framing-sensitive; JSON-LD strings are the authority (both
  re-read twice: WebFetch + urllib, identical).
- AstaBrief model lastModified Oct 3 (post-cutoff) reflects post-article repo activity,
  not the article event; do not cite as release proof.
- AutoSynthData teacher-model naming in article (Qwen3.8-27B) is taken verbatim;
  no external model-registry proof attempted (out of r11 scope).
- Cloudflare Web Search API + Pi Durable Harness remain UNADMITTED (per contract,
  not broadened here).
- No Selection Acceptance, SELECTION_COMPLETE, Architecture, Human Gate, draft, or
  publication performed. No canonical accepted mutation (verified by diff allowlist).

## 6. Commit / push / readback (filled at close)

- Parent/diff allowlist: parent e45a845…; diff = 5 NEW W40-local execution files only
  (this handoff + ledger + counterfactual + feasibility + session log); NO
  production-state/discovery/screening/evidence/views/ledger/completeness/config/
  scripts/main/other-edition changes.
- Content commit: b806316402e7fac53381a16910464fcfba0a4bc0
  (Tree e6433962d0e13d039a7e5c0eca25292e3b223705; parent e45a845…).
  Push is nonforce `git push origin weekly/2026-W40-v2-work`; remote readback
  confirmed at b806316… before close-out fill (final HEAD after fill-commit: see report).
- Terminal proposed: SOL_SELECTION_SCOPE_CHANGE_REVIEW_REQUIRED. (SEMANTIC_READY
  criteria NOT met: both items are eligible + material; BLOCKED criteria NOT met:
  original clocks were readable.)
