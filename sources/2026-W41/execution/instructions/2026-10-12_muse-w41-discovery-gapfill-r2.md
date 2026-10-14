# J-GAS W41 — Muse r2 bounded Discovery Gap-Fill, Sol re-review

Status: `EXECUTION_AUTHORITY / SOL_DISCOVERY_REVISION_REQUIRED / BOUNDED_SOURCE_INTAKE_ONLY / CORE_V2_IMMUTABLE`
Date: 2026-10-12 JST

Repository: `eariver/japanese-generative-ai-survey`
Existing branch only: `weekly/2026-W41-v2-work`

## 0. Exact preconditions

Invocation supplies HEAD and Tree for this instruction commit. Read-only verify:
- current remote W41 branch HEAD/Tree == invocation exact values;
- this instruction commit's parent is Sol Review r1 commit `e3a8547b302883bef4187798e2047eb789000a4f`, parent Tree `0b42fff823ecfe78a8e487ae908f8dc316956b02`;
- reviewed main HEAD `83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8`, Tree `31c0adc5b57761e5073d100554279a8adc5a18f4`;
- production/survey-core-v2 HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- W41 State `ISSUE_INITIALIZED`, next `stage:discovery`, Human gates pending;
- no unowned dirty edits, unauthorized shared Core/W40 changes.

Mismatch -> ZERO WRITES / STOP. No new/review/repair branch, reset, rebase, force push, history rewrites, Core changes or semantic-policy overrides.

## 1. Governing Sol Review

Read `sources/2026-W41/execution/reviews/sol-w41-discovery-completeness-r1-20261012.md` in full. Verdict: `REVISION_REQUIRED / DISCOVERY_ACCEPTANCE_HOLD`. The review **is the full SC-D01/02/03 scoped obligation register**. Read existing W41 r1 raw notes/proposal and W40 final carry-over first.

## 2. Bounded research

A. Independently retrieve and bind **all** the following original issuer event sources, no silent exclusions:
- Liquid AI d1-3B/d1-omni-600M `https://www.liquid.ai/blog/d1-open`, October 7;
- AWS Nova 2.5 Sonic `https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-nova-2.5-Sonic/`, October 5, plus service card;
- Aleph Alpha Kolibri `https://aleph-alpha.com/en/blog/kolibri-has-landed-a-sovereign-open-weight-model/`, October 3;
- Google EmbeddingGemma 2 `https://ai.google.dev/gemma/docs/releases`, October 6;
- Perplexity pplx-decider-v1.1-27b and pplx-embed-v2-late `https://community.perplexity.ai/c/announcements/9`, October 6/7 (resolve per-post permalink and issuer model card/weight repo);
- existing Decisions API beta Oct 6 `https://developers.openai.com/api/docs/changelog`: amend the existing row's first-party basis, **do not duplicate**.

B. Cutoff-sensitive further candidates: Microsoft-Decision-1 `https://commandline.microsoft.com/microsoft-decision-1-model-foundry/`; Cloudflare Clef-omni `https://blog.cloudflare.com/clef-faster-cheaper-multimodal/`; Tencent `https://huggingface.co/tencent/Youtu-Parsing-Omni`. For Oct 9 items, demand verifiable **pre-2026-10-09T22:00:00Z** event timestamp; day-only -> TIME_UNRESOLVED, not ordinary-positive.

C. For all sources, preserve original first-party URL, retrievable original/bounded verbatim source evidence, retrieval timestamp, immutable file/hash where available, publication time basis, downloaded model-weight/repo status, publisher vs independent benchmarking labels. Avoid carrying over unsupported claims or pretending page URL alone proves original Raw bytes. Commit under edition-local W41.

D. Redo quiet-lane and negative-space sweep of image/video/audio generation, local/edge/quantization/serving, retrieval/embedding, open-weight model releases; do not invent other candidates, but do not declare quiet when directly contradicted by Liquid/AWS/Aleph Alpha/Google/Perplexity. Do not downgrade their importance merely to preserve 20-row r1 count. Existing W40 HOLD remain only if no new W41 event evidence; issue #562 untouched.

E. Resolve prior r1 unpins where readily available within this bounded pass: Ironclad first-party article full-body; Gemini agent official rollout page; Mistral/Reflection model weight availability; llama.cpp supposed v0.6.0 tag existence; check both exact version/date and downloadability. Be explicit about unresolved source and avoid fabricated model version/release claim.

## 3. Required X/Grok lane

Sol has **placed and independently read back** the W41 task (previously missing) in the expected Drive folder:
- `Grok_X_SourseIntake/Weekly/2026-W41/weekly-x-2026-W41/grok-task.md`
- https://docs.google.com/document/d/1GFwHEgOE9gW9UXwp3M926SPnZ77rQ3bD9uGvlFi4LsE/edit?usp=drivesdk
- Folder: https://drive.google.com/drive/folders/1Mbg4icJLKg7GkfP7c1J5Sdz9Ob89ErxS

The native Doc stores repository task text but is not byte-identical Markdown. **File placement is NOT a Grok run or result.** If operator has no Grok access, maintain `AWAITING_GROK`. If Grok returns `grok-x-result.md`, ingest raw unchanged, hash, reconcile exact linked status URLs vs self-report, verify timestamps against W41 window, then update manifest through lawful edition-local procedure. Never assert PASS from task upload or indirect web result. No independent X value -> stop and report unfulfilled dependency.

## 4. Outputs and limits

Create fresh `r2`:
- primary corpus raw/excerpts + run ledger + exact time evidence;
- W41 Discovery proposal JSONL (schema validate), not canonical/accepted;
- materiality-neutral candidate explanations and original links (no premature Selection);
- updated timing matrix, carry-over and complete coverage-by-lane including explicit nonquiet corrections;
- proposed changed/added IDs crosswalk r1->r2;
- X receipt/reconciliation or honest AWAITING status;
- `SOL_DISCOVERY_COMPLETENESS_REVIEW_HANDOFF-r2.md` and session log.

Maintain `ISSUE_INITIALIZED / stage:discovery` throughout. **Do not** accept Discovery, write Human decisions, run Screening/Evidence/Selection/Architecture, or generate Draft/PDF. Stop at fresh Sol Discovery Completeness Review with normal commits/non-force push.

Report exact final HEAD/Tree, primary issuer counts, source evidence classes (actual Raw vs note), new r2 Discovery candidate count, statuses by date confidence, X coverage, missing/blocked items, unchanged main/Core/W40, and all changed paths.
