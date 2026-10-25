# W43 Sol adjudication of independent Evidence r3 re-audit — HOLD at trusted Screening boundary

Status: `REQUEST_CHANGES / BLOCKED_REQUIRES_UPSTREAM_AUTHORITY_DECISION / NO_ADVANCE_STAGE`
Date: 2026-10-25 JST
Issue: `2026-W43`; branch: `weekly/2026-W43-v2-work`

## Authority and independent result

- Source: user's `20261025152137_SolReview.md`, raw 18,836B SHA256 `310d28ca5b677f6403886525d46863cffa38126ed371c9e82cf5aeb812102f90`, recorded as a text-normalized (non-byte-identical) copy at `execution/audits/independent-sol-w43-evidence-r3-reaudit-result-20261025.md`.
- Independent reviewer used read-only exact W43 HEAD `dee2d3e8e18ad8eb1d01ac5b9d1c99d256c329a0`, Root Tree `5defa56f58597473338847bc7f0fd16ad4b2f17d`, reviewed main `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a`, Frozen Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- Old audit W43-IA-001..015: **10 PASS / 5 LIMITED / 0 FAIL**; technical errors corrected or explicitly constrained; 32 r3 Cards/Views, 51 Materiality rows, supplement-r3 21 task-scoped rows, projection 7/25. Full archived byte SHA and independent Core CLI NOT executed by independent reviewer; no bench reproduction. Canonical State `CANDIDATES_NORMALIZED`, next `stage:evidence-materiality-completeness`; Evidence and Human Gates pending.
- Final independent disposition **REQUEST_CHANGES / NO EVIDENCE_REVIEWED ADVANCE**, driven by **NEW P1 IA-016** exact cutoff and upstream authority conflict; additional P2 IA-017/018/epoch timestamps.
- 32 records: 20 MATERIAL, 11 CONTEXT, 1 NON_MATERIAL (Grok). 19 DROP excluded. 12 W42 carries accounted 11 excluded/1 CONTEXT. NONE is a Human Architecture/Publication approval; no Selection.

## W43-IA-016 — factual decision

W43 UTC window `[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)`, exclusive end. GitHub official Metrics Changelog `https://github.blog/changelog/2026-10-23-usage-metrics-api-adds-usage-from-tools-like-opencode/`, archived native HTML `collectors/primary/runs/20261025T044100Z-muse-r3-evidence/raw/github-metrics-20261023.html`, JSON-LD `2026-10-23T16:42:03-07:00` == **2026-10-23T23:42:03Z**, confirmed not a dateModified (`23:43:37Z`), secondary first seen `23:53Z`. Verified published event **1h42m03s AFTER exclusive W43 cutoff**. No independently established *other* pre-cutoff first-party API activation/publication. Accepted Discovery source `published_at 2026-10-23`, rationale `Fresh in-window lead`, Screening `MAYBE`, Card exact clock while View `MAIN_EVENT / CONTEXT`: **authority-level contradiction**.

**Sol disposition:** Article publication is **OUT** unless a separate authenticated pre-22:00Z in-window event is proved. Do NOT hide the issue by merely switching View to NON_MATERIAL while retaining false accepted Screening premise. W43 Metrics must not become in-window story. Before any Stage advance decide canonical upstream invalidation via reviewed Core procedure or present a verified equivalent forward authority model; any forward-only derivative alias is not automatically sufficient.

## Adjacent timing risks requiring a bounded clock sweep

- `w43-primary-github-teams-20261023`, `w43-primary-nemotron-e4b-20261023`, `w43-primary-tanstack-20261023`: only day-precision published marker currently grounded, **UNRESOLVED**, cannot infer IN from midnight normalization. Seek exact publisher JSON-LD/meta, GitHub RSS feed/Git tags/commits, HF LFS/commit timestamp or official release event. Account for publication versus revision and metadata modification.
- `w43-r2-openai-securing-20261023`: day-precision primary, external feed ~10:00Z supports IN but is not exact primary-clock proof.
- Kimi original vendor X `2026-10-23T17:15:24Z` **IN**; Kimi blog date-only is not `T00:00Z` actual clock; weights Nov 4 FUTURE. W43 membership can rely on authenticated X announcement, not hallucinated blog posting time.
- `w43-support-vercel-ollama-20261017` reporting dates inconsistent in independent report (10/23 Card vs 10/17 ID); confirm actual source/version and whether it has sufficient primary timestamp, do not silently redate.
- The r3 supplement stores **nine** fabricated-looking `T00:00:00Z` normalized date-only events (Auto mode, Decisions, FLUX ×2, Kimi blog, Nemotron, Patch, Flint ×2). Investigate Core schema requirements; distinguish `DATE_ONLY_NORMALIZED_NOT_ACTUAL_CLOCK` from real release time, correct derived metadata *only through Core-valid accepted authority* after upstream route is decided.

## W43-IA-017 and 018

- **IA-017 P2**: Kimi and Flint r3 Cards still carry immutable fused Discovery `src-1.url` (`url1 + url2`) and include `src-1` in every claim despite valid split supplements. Need edition-local exact `statement_id -> specific supplement source_id + URL + observed excerpt` and suppress fused locator from reader-visible citations. Do not change accepted Discovery in place. If Core requires original src-1, it can be retained as *discovery provenance* not sole claim proof.
- **IA-018 P2**: independently verified `interactive-evidence-r2.json` -> `r3.json` changes: **19 substantive field changes, 13 materiality-rationale-only**; 32 accepted Card sha changes include Core basis recalculation, NOT 32 independently corrected scientific claims. Muse closure `20/12` is inaccurate for semantic inputs. Append erratum, never rewrite old files.
- Existing 5 LIMITED items (GCP date conflict, fused refs, v1-v2 deltas, Duet/1Password live integration, license/weights and OSI) do not become P1 without new conflicting facts; keep honest `LIMITED` statuses.

## Frozen Core capability investigation, important boundary

Sol read frozen code at pinned current main/edition (unchanged):
- `scripts/survey_production_v2.py::transition_state()`: **only exactly one forward step** (`target_index != current_index+1` raises `non-monotonic transition refused`). No generic backward move.
- `scripts/survey_core_execution_bridge_v2.py::execute_request()`: operation kinds only initialization, `ADVANCE_STAGE` and 4 Human Gate operations; **no operator `INVALIDATE_STAGE`** bridge kind exists.
- `scripts/survey_human_gate_v2.py::invalidate_pending_gate()`: requires current State at a pending **Architecture Review or Publication Preview Human Gate** (`_current_pending_gate`), and at Architecture also machine checkpoint `architecture=passed`; W43 is **not at either gate** (`CANDIDATES_NORMALIZED`, architecture pending). This operator-only pending-gate rewind is **not applicable** at W43 present lifecycle, so do NOT reuse it to circumvent Stage security.
- `REQUEST_ARCHITECTURE_REVISION` / `REQUEST_PUBLICATION_PREVIEW_REVISION` require real Human decision at their matching Gate; user has made neither. Creating an artificial Human Gate decision is prohibited.
- Ordinary frozen Core offers **no demonstrated authorized automatic backward transition from currently trusted `CANDIDATES_NORMALIZED` to `DISCOVERY_COLLECTED`**. Any proposal requiring new frozen Core behavior belongs to separately reviewed Core maintenance, not to edition-local Weekly code changes. No branch reset, force push, State JSON rewrite, canonical acceptance overwrite or manual checkpoint deletion.
- Consequence: a purported "rerun Screening from DISCOVERY_COLLECTED" as if current State were still DISCOVERY_COLLECTED is **NOT AUTHORIZED**; an explicit operator/Human-authority design decision is needed.

## Editorial decision and next bounded task

**Do not modify machine State, checkpoint, accepted Discovery/Screening or acceptance r3. Do NOT initiate Issue #448 Bridge. No Stage advancement.** To avoid introducing a Core override before confirming the need, first mandate a narrowly bounded **read-only chronology and forward-only authority feasibility investigation**, preserving exact source time stamps and report provenance. A Muse execution unit may write **only new W43 edition-local research/authority-diagnostic Markdown** documenting first-party Oct23 timestamps, safe alternatives, and specific Core api/schema grounds; no Core/State/checkpoints/accepted bytes. Stop for Sol review of the options and any necessary genuine operator consent.

Next authorization requires one of:
A. **Separate authenticated W43 in-window source event** for Metrics, semantically genuinely same release, with source identity and exact datetime; document whether it can cure screening rationale under immutable accepted authority.
B. If Metrics has only OUT event, **proven Core-compatible explicit authority restoration path** endorsed by exact State/Schema constraints, with correct historical preservation and machine provenance (possibly separate Core maintenance reviewed and integrated before work resumes).
C. If no supported restoration path under frozen Core, remain **BLOCKED** and do not manufacture a "derived-only PASS". It may be more appropriate to carry the item to following issue, but this alone does not repair already accepted false in-window Discovery/Screening provenance.

Use independent Sol post-investigation to authorize one actual canonical remediation contract. No more routine Evidence Card r4 regenerated on unchecked authority.
