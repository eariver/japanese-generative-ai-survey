# J-GAS W42 — Human Owner Issue #570 limited Publication Preview REQUEST_CHANGES authority

Date: 2026-10-20 JST (Owner exact click time not asserted)
Authority: `HUMAN_OWNER_ISSUE570_LIMITED_REQUEST_CHANGES / W42_R32_INTEGRATED_CORRECTION_TO_PREVIEW / NO_APPROVAL_FREEZE_RELEASE`
Repository: `eariver/japanese-generative-ai-survey`
Existing branch: `weekly/2026-W42-v2-work`
Pre-dispatch fixed reviewed W42 r31 HEAD `734b0d08b00e2bfce8219c598eca3e897675066f`, root Tree `505601acdb9d5d58bef55c9a01d8060876f55008`

## Human request and scope

Human Owner said, verbatim:
> 限定修正Issue #570に対応してください。

The Human-created [W42][Publication Preview] GitHub Issue #570 (`https://github.com/eariver/japanese-generative-ai-survey/issues/570`), status `open` at authorization, labels itself `LIMITED REQUEST_CHANGES`, identifies the precise immutable r31 PDF/TeX as review basis, identifies exactly two content loci (TeX L64 body and L105 Table 1 Argon row), gives source and acceptance criteria, and expressly says Human Preview approval/Freeze/Release remain pending.

**Joint interpretation:** The Owner's explicit issue-handling request plus Owner-authored `LIMITED REQUEST_CHANGES` authorizes **a new official `PUBLICATION_PREVIEW / REQUEST_CHANGES` decision** (anticipated review revision r2, derive from live review index), with regeneration boundary **`DRAFT_COMPLETE`**, and a single controlled Muse r32 correction, exact-byte PDF/regenerated formal authorities, new Candidate, and workflow-admitted Stage progress to the next pending Human Preview. This is NOT a Publication Preview approval, nor a waiver of mandatory trust-boundary and independent evidence requirements.

No Human micro-approval is needed for deterministic substeps within this narrow contract. If the Owner's Issue constraints cannot be fulfilled without extra publication text/bibliography scope, stop and report instead of expanding authority.

## Content scope and accepted technical facts

ONLY two reader-facing locations: `surveys/weekly/2026-W42/main.tex` Section 1 Argon body (old line 64) and Table 1 Argon row (old line 105). Other changes allowed only for non-reader-facing provenance/comment lines, source/PDF/Reader/QA/Candidate/generated receipts/checkpoints as actually required by native Core, and possibly tiny mechanical formatting that does not change other prose.

Google first-party references checked by Sol as of 2026-10-20 JST:
- `https://ai.google.dev/gemini-api/docs/models/gemini-4-argon` — unified **1,048,576** input/output token context, normal default synchronous limit **65,536**, long decode up to bounded remaining context.
- `https://ai.google.dev/gemini-api/docs/tokens` — input, thinking, output share same 1,048,576; input/context consumption reduces remaining generation budget.
- `https://ai.google.dev/gemini-api/docs/long-decode` — Interactions API `background:true` + `max_output_tokens>65536` enables hop continuation; `background:false` ≤65,536.
- `https://ai.google.dev/gemini-api/docs/generate-content/long-decode` — GenerateContent per-hop normally ≤65,536 (direct non-streaming REST ≤32,768), client/SDK continuation required; function calls also contribute to unified window. Model-ID-only switch does NOT enable long decode.
- `https://ai.google.dev/gemini-api/docs/latest-model` — official unified-context and pricing examples consistent with baseline.

Keep the distinction: the **unified 1M is not the default single-output allowance**; long decode can produce much more than 65,536 using explicit supported API/SDK orchestration and only within the context remaining after input, thinking and function call history. The `65,536` normal hop ceiling and `32,768` direct non-streaming REST ceiling differ by API transport. Do not portray thinking as an independent separate budget.

Preserve prior r31 price dates and amounts, Minecraft and Wonder article, P1 package and all other sections/table cells, approved Architecture r1, frozen Core v2, prior r29–r31 audit material and history. Do not perform independent 21-page re-audit or arbitrary 28-page padding. No general wording/citation refresh.

## Production safety/stop

The reviewed W42 r31 State at issue opening: `RELEASE_CANDIDATE / HUMAN_GATE_REACHED`, `human_gates.publication_preview=pending`, prior formal Publication Preview review **r1=REQUEST_CHANGES**. The r32 Gate operation is a NEW revision and must not rewrite r1.

Transport is reviewed-main-first-party `.github/workflows/survey-production-v2-operator-bridge.yml` via authenticated issue #448 `/survey-core-execute <request-commit>` or equally verified official permitted workflow trigger. Every request must be its own **request-only HEAD commit**, with actual GitHub Actions `operator-preflight` and `operator-execute` success, bot receipt and read-back. No local CLI bridge substitution, fake run IDs, manual State edit, reset, rebase, force, new branch, main/Core change, preview approval, freeze or release.

Execution contract: `sources/2026-W42/execution/instructions/2026-10-20_muse-w42-r32-issue570-unified-context-bounded-repair-to-preview.md`.

Approved eventual stop: `SOL_W42_R32_ISSUE570_CORRECTED_PREVIEW_READY / RELEASE_CANDIDATE / HUMAN_PREVIEW_PENDING / CORE_V2_FROZEN / NO_FREEZE_NO_RELEASE`.
