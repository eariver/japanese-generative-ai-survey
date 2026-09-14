# Human-facing Architecture Review dossier — 2026-W35 r1

Sol-owned review surface for the pending Human Architecture Review. Read this before deciding APPROVED / REQUEST_CHANGES. Machine `READY_FOR_ARCHITECTURE_REVIEW` establishes pipeline readiness only, not research sufficiency.

## 1. Exact review identity

- Edition `2026-W35`, revision r1, Research Profile WEEKLY, Publication Profile WEEKLY_MAGAZINE.
- Reviewed repository commit SHA: `676160e325db35840af1f36b8cac8c3dad54beb4` (updated to the exact pushed W35-branch commit at presentation).
- Lifecycle `ARCHITECTURE_ESTABLISHED`, next action `ARCHITECTURE_REVIEW`, terminal `HUMAN_GATE_REACHED`.
- Canonical window (Core-governed): `[2026-08-21T18:00:00-04:00, 2026-08-28T18:00:00-04:00)` ET; UTC classification `[2026-08-21T22:00:00Z, 2026-08-28T22:00:00Z)`.
- Production Line `production/survey-core-v2 @ 774dd39a` (unchanged); reviewed `main @ 774dd39a`; no Core repairs; W35 never merges to main under current policy.

## 2. Research coverage

- Source Intake: 1 required Grok/X run COMPLETE (r3 Sol-reviewed correction; 35 URLs: 25 ordinary / 0 background / 10 late; ~40+ approximation rejected) + 19 edition-local retrieval Raws + pre-Discovery breadth sweep.
- Discovery: 20 records accepted (1 X-ledger + 19 retrievals). Screening: 19 KEEP / 1 DROP (pre-window Muse Code background, byline-verified 08-06).
- Evidence: 19 cards — 8 VERIFIED (first-party reads) + 11 PARTIAL (relayed claims with exact unresolved targets); 0 NEEDS_MORE/REJECTED. Completeness: 3/3 obligations SATISFIED, overall LIMITED per declared residuals. Carry-over: zero formal inherited obligations (W34 v2 selection scanned: no HOLD_OUT/WATCHLIST/LATE_BREAKING roles; MiniMax thread closed RECHECKED_UNRESOLVED).
- Sol completeness review: NON-BLOCKING. Residual gaps declared: image lane empty, speech-model lane empty, memory/multi-agent no distinct cluster, tracker-only items (Gemini 3.5 Transcribe, Apodex 1.1, Ling 3.0 Flash Fin) without retrievable primaries, MiniMax recheck not re-executed.

## 3. Evidence quality (authority consumption)

- AUTHORITY_CONSUMED: all 8 VERIFIED cards (full-page reads) + all PARTIAL relayed bytes (fully read; PARTIAL reflects missing vendor primaries, not unread content).
- CAPTURED_BUT_UNCONSUMED: none. AUTHORITY_RETRIEVAL_FAILED: z.ai blog/HF cards (secondary + X rows substituted, PARTIAL). AUTHORITY_NOT_FOUND: image/speech-model/MiniMax primaries.
- Self-caught vocabulary defect (custom source_type outside closed Evidence map) repaired edition-locally with full downstream regeneration; classified issue-local, not a Core defect.
- Every relayed figure carries its bound (vendor/author-claim + unresolved target); nothing retrieved is presented as verified by retrieval alone.

## 4. Major candidate/disposition map

- SELECTED 17: GLM-5.3-Flash, Qwen3.8-Flash-Next, Hy4 (P1 primaries) + Granite 4.2, Grok-ledger (P1 supporting); VS Code AHP, Cursor Origin, Copilot-Teams (P2 primaries) + Harness, grith (P2 supporting); Fable 5, GPT-5.6/Kiro (P3 primaries); vLLM v0.28.0, OpenThai 2.0 (P4 primaries); Anthropic auto-alignment, China MIIT, Korea ethics (P5 primaries).
- HOLD 2: Video-IFBench, HUG-VIS (abstract-only, no attached event; watched context).
- DROP 1: Muse Code launch (pre-window background).
- Excluded from candidacy: Nvidia-HF rumor (unconfirmed in-window), video X fragments, tracker-only items, same-week density list (pre-window/tracker context).

## 5. Negative-space / omission review

- Image generation/editing: no in-window material candidate found in X or sweep — quiet-or-gap undetermined, declared.
- Speech/audio models: same; HUG-VIS voice-cloning task is the only speech-adjacent evidence.
- Nvidia-HF: post-window confirmation (Sept 10) exists but is out of scope; in-window exclusion is correct chronology discipline.
- Unselected evidence inspected: HOLD abstracts + DROP background re-checked against primaries; no systematic consumption defect found.

## 6. Editorial thesis

In 2026-W35 open-weight efficiency turned architectural — sub-5%-activation MoEs with offloadable memory shipped under MIT and permissive licenses — while the agent coding plane reorganized around portable sessions, agent-native forges, and deterministic guardrails; flagship claims and governance moves are held inside explicit evidence bounds.

## 7. Architecture packages

- P1 `w35-open-efficient-turn` (order 1): primaries GLM/Qwen/Hy4; supporting Grok-ledger + Granite 4.2. The week's defining cluster.
- P2 `w35-agent-coding-plane` (order 2): primaries AHP/Origin/Copilot-Teams; supporting Harness + grith. Session/forge/context/review/security reorganization with trust questions explicit.
- P3 `w35-flagship-receipts` (order 3): primaries Fable 5 + GPT-5.6/Kiro. Proprietary claims with slice-honest bounds.
- P4 `w35-infra-regional` (order 4): primaries vLLM + OpenThai 2.0. First-party-grounded infrastructure and regional open progress.
- P5 `w35-safety-governance` (order 5): primaries auto-alignment + China + Korea. Evidence-vs-governance contrast without equivalence.

## 8. Page/section allocation

Deferred to drafting (noted in page_plan). No optional-section omission decided. Paper Watch–style treatment of the two HOLD papers is a drafting decision, not yet taken.

## 9. Counterfactual alternatives

- Flagship-first ordering (Fable-led): rejected — flagship claims are the least-verified (PARTIAL, primaries missing); leading with them would mislead.
- Sparse issue (open-cluster only, ~3 packages): rejected — would discard independently sourced agent-plane and governance evidence to manufacture focus.
- Granite-as-P2-primary: rejected — its agent-training story serves P1's open breadth better than P2's protocol narrative.

## 10. Known limitations and risks

- P1's three anchors are PARTIAL (secondaries); drafting must inherit must-cover bounds or the issue overclaims.
- Thin image/audio lanes are real residual gaps.
- All vendor figures publisher-only; benchmark slices (GDPval vs AnalystAgent) must survive into prose.
- MiniMax recheck not re-executed; tracker-only items excluded without primaries.

## 11. Sol review finding

Blocking: 0. Non-blocking: 3 (coverage residuals; P1 PARTIAL weight; page allocation pending). No compression audit triggered (SELECTED=17). No Core defect. Recommendation: proceed to Human decision; do not auto-advance.

## 12. Human decision options (only now)

- `APPROVED` — record against the exact reviewed commit; continue to drafting (not in this run; this run STOPS at the pending Gate).
- `REQUEST_CHANGES` — supply requested changes + one allowed pre-Architecture regeneration boundary (ISSUE_INITIALIZED / DISCOVERY_COLLECTED / CANDIDATES_NORMALIZED / EVIDENCE_REVIEWED / SELECTION_COMPLETE); Core records rN and invalidates only affected downstream authority.

---

## Reviewed authority

Same as §1 above; canonical machine shell: `execution/reviews/architecture-r1.md` (reviewed commit recorded there at presentation).

## Human decision

`PENDING` — none recorded. Valid: `APPROVED` / `REQUEST_CHANGES` only.

## Requested changes

None (no review performed yet).

## Regeneration boundary

None selected (no review performed yet).

## Shared-Core implication

None. No Core defect; no repair branch or PR; `main` unmerged by design.
