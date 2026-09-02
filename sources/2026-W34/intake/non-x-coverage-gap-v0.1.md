# 2026-W34 non-X coverage and gap audit

Observed: 2026-09-02T12:26:00Z  
Window: 2026-08-14T18:00:00-04:00 → 2026-08-21T18:00:00-04:00  
Profile: WEEKLY + WEEKLY_MAGAZINE

This is an intake-readiness record. Leads remain unscreened and are not Evidence, Selection, or publication material.

## Collector status

| Surface | Configured scope | Result | Raw status |
|---|---:|---|---|
| arXiv API | 6 category queries | canonical run blocked in this execution surface; 6 manual page locators recorded | 0 |
| GitHub Releases | 7 repositories | canonical bounded API run succeeded; 5 release matches | 7 immutable JSON responses |
| Official pages | 22 configured pages | canonical run blocked in this execution surface; 16 manual subpage locators recorded | 0 |

## Coverage

| Lane | Seed | Key leads | Gap / next check |
|---|---|---|---|
| model/reasoning | SEED_PRESENT | lead:openai-api-regional-processing, lead:google-gemini-3-7-flash, lead:zai-glm-5-3, lead:qwen3-8-27b | Google Gemini 3.7 is pre-window; in-window vendor/model leads still need canonical page capture and screening. |
| agents/coding | SEED_PRESENT | lead:mistral-agentic-search, lead:deepseek-v4-flash-vision-exp, lead:zai-glm-5-3, lead:arxiv-lapf, lead:arxiv-scienceflow | No current Discovery records may be created until canonical collector gaps and Grok/X are resolved. |
| multimodal | SEED_PRESENT | lead:deepseek-v4-flash-vision-exp, lead:qwen3-8-27b, lead:arxiv-egogazelite, lead:arxiv-embodied-security | Raw arXiv and official HTML snapshots are missing in this run. |
| image | PARTIAL | lead:xai-api-changelog, lead:qwen3-8-27b | No image-first in-window release was canonically captured; targeted official page scan remains required. |
| video | PARTIAL | lead:runway-changelog, lead:minimax-h3, lead:google-omni-1-1-flash | Available prominent leads are pre-window or post-cutoff; no in-window video release is established. |
| audio/music | SEED_PRESENT | lead:stability-stable-audio, lead:minimax-music-3, lead:google-transcribe | Stable Audio is in-window; MiniMax and Google entries are boundary/post-cutoff and must remain dated. |
| open-weight/local AI | SEED_PRESENT | lead:qwen3-8-27b, lead:zai-glm-5-3, lead:minimax-h3, lead:minimax-music-3 | Model card/license/weight availability details remain unverified for Evidence. |
| serving/systems | CANONICAL_SEED_PRESENT | lead:openai-api-regional-processing, lead:qwen3-8-27b, lead:arxiv-egogazelite | GitHub release Raw is complete; Transformers/FlashInfer matches are still only unscreened leads. |
| memory/retrieval | SEED_PRESENT | lead:mistral-agentic-search, lead:aws-vector-solutions, lead:arxiv-scienceflow | Implementation posts need technical scope checks and must be separated from model-release claims. |
| evaluation | PARTIAL | lead:mistral-agentic-search, lead:deepseek-v4-flash-vision-exp, lead:arxiv-corun, lead:arxiv-embodied-security | Benchmark figures are not imported into Evidence; primary snapshots and evaluation methodology checks remain. |
| safety/security | SEED_PRESENT | lead:zai-glm-5-3, lead:arxiv-agent-inheritance, lead:arxiv-embodied-security | Speculative and research leads are deliberately not treated as operational facts. |
| other emerging technology | SEED_PRESENT | lead:openai-chatgpt-release-notes, lead:openai-api-regional-processing, lead:nvidia-ai-ecosystem, lead:arxiv-agent-inheritance | Keep product/ecosystem context separate from technical Evidence and await full canonical intake. |

## Chronology guards

- Gemini 3.7 Flash (Aug 13), ScienceFlow (Aug 14 14:54 UTC), CoRun (Aug 14 15:17 UTC), MiniMax Music 3.0 (Aug 13), and MiniMax H3 (Aug 3) remain pre-window.
- Google Gemini Omni 1.1 Flash (Aug 27), Gemini 3.5 Transcribe (Aug 26), and Runway Wan 3.0 (Aug 24) remain post-cutoff.
- SGLang v0.5.18 was created Aug 21 but published Aug 22; the collector classifies it by published_at and excludes it from W34.

## Carry-over

The sole derived W33 HOLD_OUT obligation is MiniMax candidate:2026-W33:986cf7db00a0202e. Official listings were rechecked; the item remains RECHECKED_UNRESOLVED with no current-week promotion.

## Blocking conditions

- Weekly Grok/X is REQUIRED_BY_PROFILE; no task/result has been prepared or imported in this run. Discovery acceptance is therefore blocked.
- The canonical arXiv and official-page exact-byte collectors need a retry in an HTTPS-enabled execution surface. Manual web observations do not satisfy the Raw contract.
- Screening, Evidence, Selection, Architecture, drafting and publication remain outside this task boundary.
