# W40 r11 host-timestamp ledger — HF-hosted first-party announcements (staged, NOT canonical)

Status: STAGED_R11 / NOT_ACCEPTED / NO_CANONICAL_MUTATION
Work branch: weekly/2026-W40-v2-work
Starting SHA/Tree: e45a845db406392191a819f5a99b0c68bc36d97c / f045911d565c8e7b9243a65af1ee72df0b763d89
Reviewed main: afdb3df3faa20af3bb5798be429bba8dbd2100b1
W40 exclusive window (half-open UTC): [2026-09-25T22:00:00Z, 2026-10-02T22:00:00Z)
Cutoff: 2026-10-02T22:00:00Z
Retrieval date (this run): 2026-10-10Z (UTC; JST 2026-10-10)
Method: direct original-host HTTPS read (curl/urllib + WebFetch HTML), JSON-LD extraction,
canonical-link check, org/author page existence check, HF API model/dataset verification.
Secondary crawler (wesearch.press) is corroboration ONLY, never publisher authority.

## 1. AstaBrief — https://huggingface.co/blog/allenai/astabrief

- Exact URI (canonical): https://huggingface.co/blog/allenai/astabrief
- Canonical link verified: <link rel="canonical" href="https://huggingface.co/blog/allenai/astabrief"> present.
- Org path: /blog/allenai/ → Hugging Face organization `allenai` (org page exists;
  title `allenai (Ai2)`).
- Author (JSON-LD author/creator): Person `Kyle Wiggers`, url https://huggingface.co/Ai2Comms.
  User page exists (title `Ai2Comms (Kyle Wiggers)`). Sol r10 already verified
  Ai2Comms = Ai2 communications account; article prose is first-person Ai2
  ("We built AstaBrief 8B…", "We wanted to help scientists…", "we're also open-sourcing it…").
- JSON-LD (original host bytes, re-read 2026-10-10Z):
  - @type: SocialMediaPosting; headline: "Open-sourcing AstaBrief, the fast report-generation model in Asta"
  - datePublished: 2026-10-02T15:19:50.340Z
  - dateCreated: 2026-10-02T15:19:50.340Z
  - dateModified: 2026-10-02T15:22:07.584Z
  - publisher: Organization Hugging Face (platform operator, NOT the issuer).
- Raw capture (this run, urllib): 169,199 bytes;
  SHA-256: d440b90083303f3d6a4b5906369f312039098996553bf6a91e369c0599e9ea9e.
  (Byte length/SHA are transport-framing-sensitive; JSON-LD strings above are the authority.)
- In-window verdict: 15:19:50.340Z < 22:00:00Z ⇒ IN-WINDOW article event CONFIRMED
  (margin ≈ 6h40m). dateModified also in-window.
- Corporate-domain counterpart (distinguish, do NOT conflate):
  - https://allenai.org/blog/astabrief exists (first-person Ai2 original).
  - Ai2 RSS pubDate: 2026-10-02T00:00:00-08:00 = DAY-ONLY midnight default (same for all
    Ai2 items; r10 control stands). Page head carries no timestamp meta.
  - allenai.org HTML (1,202,185 bytes; SHA-256
    1548def7420b7a27ccc23e69ca4da2d85af76c353299592884820838099dbfa1) contains CMS
    asset names `2026-10-02t15-18-13-…` (≈90s before HF datePublished) — same-day
    corroboration only, NOT a standalone-domain publication clock.
  - Conclusion: HF hosting clock proves THE HF-HOSTED ISSUER ARTICLE event; it does NOT
    prove the allenai.org page hour or the first weight-file availability instant.
- Artifact/file availability (distinguish from article event):
  - HF API `allenai/AstaBrief_8B`: createdAt 2026-02-09T17:13:01Z (pre-window),
    lastModified 2026-10-03T18:55:16Z (post-cutoff modification; NOT the article event).
    license tag apache-2.0; base Qwen3-8B lineage via SFT checkpoint.
  - `allenai/AstaBrief_8B_SFT`: createdAt 2026-09-10T23:36:30Z; apache-2.0.
  - Datasets `allenai/AstaBrief_SFT_Mix` (39.5k; lastModified 2026-09-29T21:49:00Z,
    license cc-by-nc-4.0) and `allenai/AstaBrief_DPO_Mix` (6.6k; lastModified
    2026-09-29T21:58:58Z) predate the article; training-data release accompanies the
    Oct 2 announcement but files themselves are NOT Oct 2 creations.
  - Article-declared technical facts (publisher-attributed, NOT independently reproduced):
    Qwen3-8B base; SFT 47K + DPO ~6K from real Asta/ScholarQA queries (to June 2025);
    one-pass report pipeline; Fast mode 51.1s vs Thinking 178.5s (≈3.5×);
    2025-era comparison baselines (Claude 3.5/3.7, o3/o4-mini, GPT-4.1, DeepSeek-V3/R1);
    evaluation NOT rerun against current frontier (article states this explicitly).
- Secondary corroboration (non-authority):
  https://wesearch.press/s/open-sourcing-astabrief-the-fast-report-generation-model-in-e81b1dea
  (15:19:50Z posting; observed 16:25:50Z) — matches host clock; does NOT substitute host.

## 2. AutoSynthData — https://huggingface.co/blog/ServiceNow-AI/autosynthdata

- Exact URI (canonical): https://huggingface.co/blog/ServiceNow-AI/autosynthdata
- Canonical link verified: <link rel="canonical"
  href="https://huggingface.co/blog/ServiceNow-AI/autosynthdata"> present.
- Org path: /blog/ServiceNow-AI/ → Hugging Face organization `ServiceNow-AI`
  (org page exists; title `ServiceNow-AI (ServiceNow-AI)`).
- Authors (JSON-LD author/creator, 4 persons): Esakkivel Esakkiraja
  (https://huggingface.co/esakkivel), Shruthan Radhakrishna, Denis Akhiyarov,
  Sagar Davasam — each author line carries a `Follow / ServiceNow-AI` badge in page
  body (re-read 2026-10-10Z). Article prose is first-person ServiceNow CoreAI
  ("At ServiceNow CoreAI, we built AutoSynthData…", "We illustrate the pipeline with
  EnterpriseOps Gym…").
- JSON-LD (original host bytes, re-read 2026-10-10Z):
  - headline: "AutoSynthData: Generating Training Data for Enterprise Agents"
  - datePublished: 2026-10-02T04:01:31.290Z
  - dateCreated: 2026-10-02T04:01:31.290Z
  - dateModified: 2026-10-02T04:05:48.837Z
  - publisher: Organization Hugging Face (platform operator, NOT the issuer).
- Raw capture (this run, urllib): 210,484 bytes;
  SHA-256: d84a35e69695bc5b8bc531871d4c7d9a2082037eb2f89eaa32f8dd006ab56a44.
  (Same framing caveat as above.)
- In-window verdict: 04:01:31.290Z < 22:00:00Z ⇒ IN-WINDOW article event CONFIRMED
  (margin ≈ 18h). dateModified also in-window.
- Method-vs-artifact distinction (critical):
  - No standalone `ServiceNow-AI/AutoSynthData` model (HF API → 401/Unauthorized =
    nonexistent-or-private; NOT a public release) and no `autosynthdata` dataset under
    ServiceNow-AI (API search → empty). No public AutoSynthData pipeline code found
    (consistent with r4 AUTHORITY_RETRIEVAL_FAILED; site searches negative then and now).
  - What the article DOES announce: a methodology (target-model failures + teacher
    successes → capability cards → target/multiply generation → sample/batch gates →
    moving-frontier curriculum) DEMONSTRATED on the separately released
    EnterpriseOps Gym dataset.
  - EnterpriseOps Gym is a DIFFERENT artifact: dataset `ServiceNow-AI/EnterpriseOps-Gym`
    (createdAt 2026-02-28T21:11:46Z; lastModified 2026-04-30T15:27:14Z;
    license apache-2.0; paper arXiv:2603.13594 Malay et al. 2026). It is background
    infrastructure for the experiment, NOT the AutoSynthData release.
  - Article-declared results (publisher-measured, environment-scoped, NOT reproduced):
    Hybrid (Gemma-4-26B-A4B-it target, Qwen3.8-27B teacher): synthetic SFT +7.2pp mean
    Pass@1 (35% relative), verifier 63.01%→68.55%, closes 59% of target–reference gap;
    ITSM (same target, DeepSeek-V4.1-Flash teacher; 1,994 samples / 66h):
    18.77%→27.18% mean Pass@1. Generator never saw original eval prompts/entities/
    trajectories/verifiers (capability-card sanitization claimed).
  - Gates/limits to preserve in any future canonical text: task feasibility requirement;
    target-phase (parallel vetted core set) vs multiply-phase (variants of accepted
    targets only, no second-generation seeding); positive gate (reference must solve),
    negative gate (mutated outcomes must fail), bounded critic repair; SFT-only evidence
    (no RL result); single-benchmark-family scope (EnterpriseOps Gym Hybrid+ITSM only).
- Secondary corroboration (non-authority):
  https://wesearch.press/s/autosynthdata-generating-training-data-for-enterprise-agents-56c490db
  (04:05:43Z capture) — matches host clock; does NOT substitute host.

## 3. Common interpretation rule applied

- A first-person issuer-authored article on a verified organizational HF account counts as
  a potential FIRST-PARTY TECHNICAL ANNOUNCEMENT with the hosting platform's original
  publication clock as the event clock for THAT article. It does NOT transfer its clock
  to a corporate-domain page, weight files, datasets, or code repos.
- Publisher field `Hugging Face` in JSON-LD identifies the platform operator, not the
  issuer; issuer identity comes from org path + author account + first-person prose,
  all verified above.
- Old HOLD justification "TIME_UNRESOLVED" (day-only everywhere) is SUPERSEDED for the
  article-event question by the two in-window host clocks. Upstream HOLD rows remain
  canonically unchanged in this unit (no canonical mutation); the scope decision is for
  Sol.
