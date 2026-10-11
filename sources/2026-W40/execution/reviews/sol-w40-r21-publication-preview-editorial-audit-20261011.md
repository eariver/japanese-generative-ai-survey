# Sol W40 r21 — Publication Preview substantive editorial audit

Status: `CONTENT_REVISION_REQUIRED / PUBLICATION_PREVIEW_APPROVAL_HOLD / NO_HUMAN_GATE_DECISION`
Date: 2026-10-11 JST
Repo: `eariver/japanese-generative-ai-survey`
Exact Muse r21 reviewed HEAD: `832808af95df29547d7050452fdac7bb3df80f2e`, Tree `fbedf5e070a6816e83affe429dbaa8454c544873`
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`.

## 1. Valid official pipeline, but invalid substantive editorial readiness

- Remote W40 is seven normal fast-forward commits from Sol r21 instruction `8695430b4cf16a869bffc5e4333e42073a802fec`. Official Architecture approval r1 is present, reviewed_by Human Owner, reviewed canonical Muse r20 `3711d777f8c447d25c6e0bfb3212450974afe8ab`; Architecture Gate approved with SHA-bound provenance.
- State is `RELEASE_CANDIDATE / PUBLICATION_PREVIEW / HUMAN_GATE_REACHED`, Draft and Validation checkpoints passed, Preview pending/provenance null, Freeze/Release pending. Publication Candidate says `READY_FOR_PUBLICATION_PREVIEW`; Quality Bundle reports 3/3 PASS, semantic report 11/11, visual review 2/2, 28/28 bibliography citations claimed. These are genuine recorded machine/worker reports, **not a substitute for editorial reading**.
- The candidate PDF `surveys/weekly/2026-W40/main.pdf` is a valid GitHub-held PDF. Sol read the complete PDF from the repo via the GitHub connector as base64, decoded the original bytes, and independently recalculated SHA-256 `f93d15f838cddf9489cc7ed6e73f3eb2cbe551044ac84a45cc41441fabf202ab`; actual PDF byte length **369,980**, and candidate/pdf-preflight both bind that correct length, with 12-page count recorded. Sol independently reviewed ALL nine body TeX files and all nine draft-result.json blocks. **Sol could NOT mount/render the PDF locally or visually inspect every rendered page**; the PDF cannot be certified for visual layout by Sol, and Muse's 12-page visual claim has not been independently rechecked.
- PDF permalink: `https://github.com/eariver/japanese-generative-ai-survey/blob/832808af95df29547d7050452fdac7bb3df80f2e/surveys/weekly/2026-W40/main.pdf`. Visual review and content quality are separate decision axes. No Human Publication Preview decision has been given or recorded.

## 2. Substantive content defect — BLOCKER

Full-text evidence: `surveys/weekly/2026-W40/sections/{10-frontier-models,20-open-reasoning,30-decision-inference,40-devday-surface,50-safety-provenance,60-training-systems,65-eval-infra,70-multimodal-serving,80-enterprise-digest}.tex`.

The **nine substantive TeX sections combined contain only ~9,598 UTF-16 JavaScript string characters including TeX commands/markup, of which ~5,170 are CJK/Hiragana/Katakana matched characters**. There are **zero `tabular` / `tabularx` / `longtable` comparative tables in these nine content sections** and **one display equation (ContextLM Eq.5)**. This is not a page-number quota; it is directly inspectable underdevelopment across 28 selected items.

- P1 (998 raw TeX characters, 3 model paragraphs): the architectural requirement `Sonnet 5.5 full price card` and `Gemini 4 Argon intro pricing` is **not fulfilled in visible main section**. Only GPT-6.1 Sol's $2/$10/$0.10 prices are stated. No comparative price/availability table.
- P2 (817 characters, 2 model paragraphs): the approved Holo4/ELYZA **comparison table** and fully explicit benchmark denominators are not actually laid out as a table; the prose merely **promises** `Holo4の汎用とELYZAの和特化を比べる表は、条件の違いを注記つきで添える`, yet no table exists. Holo4/ELYZA license statements appear; no explicit table.
- P5 (1,116 characters): five independent safety/provenance domains become 4 short paragraphs and no meaningful five-subsection implementation detail. The approved architecture expected distinct evaluations/threat/scope boundaries.
- P6a (1,680 characters, around 1,001 Japanese script characters): P6a is explicitly the deep-technical lead, but Eq.3 and Eq.6 are essentially verbal sketches; only Eq.5 is actually displayed, no explanatory diagram/table for contrasting baselines or 47B/1.2T/2.38T. Key numeric and methodological distinctions are included in compressed numeric strings, not substantively explained; original Eq.5 verified status appears preserved.
- P6b (1,403 characters): correct OpenTTS TTFA conditions and repo timing appear, but AgentPerf serving objective, roofline, and RL Hub pins are terse and do not provide worked method interpretation or protocol/comparator table.
- P7 (1,219 characters): FLUX 3 lists four prices without mapping them to image resolution, despite the approved `per-resolution pricing` requirement.

**The Draft itself is too short**, not merely a TeX transform bug: the nine canonical `draft/v2/packages/{P1...P8}/draft-result.json` together have only 38 blocks, including 9 `CLAIM_BOUNDARY` blocks (29 normal prose blocks). The Japanese article prose is largely transferred from those `PARAGRAPH` blocks into TeX with citations/TeX commands. Therefore correction must begin at **Draft-authoring**, not only TeX formatting.

## 3. Terminology/natural Japanese defect — BLOCKER

The actual Japanese contains repeated nontechnical, opaque and over-literary neologisms. This contradicts active `docs/editorial-style-guide.md §1, §3` (natural technical Japanese, preserve exact English source terminology) and the Owner's explicit no-over-Hanji/no-overtranslation preference.

Verified examples from published body:
- `Ollamaの口、Clefの重み、Deciderの頭` for interface/model/pointer-head → say `推論API／モデル重み／pointer head`.
- `市庭の消息` for enterprise/industry news → `企業・業界動向`.
- `文脈を綴じとして編む`, `Bashで擦り合わせた綴じの品` for ContextLM skill file/context representation → `編集可能なコンテキストファイル`, `Bashと同期する状態/文書` where supported.
- `絵の目` for image/multimodal input, `声の品` for TTS model, `写しの到着` for eval scripts, `模型` for models, `手習い` for tutorials, `技持ち` for experts, `売り手の催しの計り` for vendor-reported demo measurement, `団子記事` for a team/blog article, `協定時` for UTC. These impede technical traceability and naturalness and require **systematic terminology audit** across Draft/TeX/frontmatter/Week in Review/Source Notes, not mere local search-and-replace without source semantics.
- A concrete chronology slip: P3 kicker/deck says `三つの10月1日を混ぜない` but the Ollama paragraph dates the first item **September 29**. Clarify correct chronology; preserve approved source date.

Use standard technical English when precise: model, benchmark, token, context, weights, inference/serving, API, pointer head, MoE, expert routing, evaluation script, SFT/RL, latency, FLOPs. Explain genuine terms in natural Japanese, not lexical calques.

## 4. Metadata/documentation discrepancy — MINOR

The session/handoff narrative and the `quality-regression-bundle-v2.json` PDF_PREFLIGHT evidence sentence claim PDF **370,741 bytes**, but the actual GitHub PDF decoded byte length **369,980**; both `publication-candidate-v2.json` and `publication/v2/deterministic/pdf-preflight.json` correctly bind **369,980**, and PDF SHA matches the canonical `f93d15...`. Thus the canonical PDF authority/hash is correct; the 370,741 prose assertion is stale/misleading and needs correction on regeneration, not a Core hotfix.

## 5. Disposition and governance

`CONTENT_REVISION_REQUIRED / HOLD_HUMAN_PUBLICATION_PREVIEW_APPROVAL` recommended. No request to waive the official machine QA or invalidate existing Authority manually; no Human `REQUEST_CHANGES` or `APPROVED` has been recorded in this audit.

**Important frozen Core governance:** `config/survey-production-v2.json` sets `operator_pending_gate_invalidation_boundaries.PUBLICATION_PREVIEW=[]`, and `scripts/survey_human_gate_v2.py::invalidate_pending_gate` rejects the operation across an approved Architecture Gate or with nonempty Human review history. Thus operator pending-Gate invalidation, used during *pre-approval Architecture* repairs, is **NOT LEGAL at this Publication Preview**.

A new Japanese Draft requires a separate explicit Human Owner `PUBLICATION_PREVIEW / REQUEST_CHANGES` decision, using `scripts/survey_human_gate_v2.py request-publication-preview-revision` with `regeneration_boundary=ARCHITECTURE_ESTABLISHED` (allowed in Human revision config and preserves Architecture approval), `reviewed_by=Human Owner`, revision 1 if no Publication Preview reviews exist, exact reviewed Candidate commit/Gate bytes, and the recorded requested-changes contract. Do not infer the Owner's Human decision merely from Sol's review. If the Owner authorizes this later, stage-specific Draft/reader source revisions must respect existing singleton/core checkpoint ownership; any actual Core limitation must STOP without workaround.

Once Human REQUEST_CHANGES is explicitly provided, use the proposed (currently NOT EXECUTABLE) `execution/instructions/2026-10-11_muse-w40-r22-proposed-post-human-preview-revision.md`.

Preview Approval readiness: **FAIL due to substantive editorial content and unnatural Japanese**; Stage/Git integrity is otherwise structurally PASS on checked evidence. No Freeze, Release or publication changes authorized.
