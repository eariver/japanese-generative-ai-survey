# DELEGATED RETRIEVAL LOG — r4 gap-fill (subagent findings, Muse-recorded)

Method: three parallel bounded retrieval subagents (research-only, no writes) on 2026-10-10Z; findings below are THEIR verbatim-quote reports, recorded here for Sol re-verification via exact URLs. Muse did NOT directly re-fetch these pages; authority = subagent-consumed + Sol-reverifiable URLs. No timestamps/licenses/versions fabricated.

## A. Strands Decider license + v19 pin — PARTIAL (license CONFIRMED; git tag N/A by construction)

- `https://raw.githubusercontent.com/strands-labs/strands-decider/main/pyproject.toml`: `license = "Apache-2.0"`, `license-files = ["LICENSE"]`
- `.../main/LICENSE`: `Apache License / Version 2.0, January 2004` ... `Licensed under the Apache License, Version 2.0`
- Repo page: `This project is licensed under the Apache License 2.0`; Hub `StrandsAgents/strands-decider-2B-hobson-v19`: `License: apache-2.0`; Hub API cardData `license: apache-2.0`
- v19 vs v21 are Hub repos/recipe generations, NOT git tags (GitHub tags API `[]`, releases empty; naming.md: `model/<name>` tag convention). v19 Hub: created 2026-09-30, SHA `bb282d786bc251fd4e3068de3ada9ddbb38127cd`; v21: created 2026-10-05, SHA `2b52a6235c1b8306bbfa30b00b9d4b74b63a39f5` (CHANGELOG: v21 = v19 recipe + paraphrases + Qwen3.5-4B distillation). Head main @ `0ac22a9` (2026-10-09) is v1-era. W40 pins v19 Hub revision `bb282d7`, NOT head.
- Exact license string: `Apache-2.0`.

## B. BFL FLUX 3 Image pricing/availability — CONFIRMED

- `https://docs.bfl.ai/release-notes` (`<Update label="October 1, 2026">` → `## FLUX 3 Image` → `### Pricing`): `768sq $0.041 / 1k $0.048 / 2k $0.100 / 4k $0.607` (same table at `https://docs.bfl.ai/quick_start/pricing` with resolutions)
- `https://bfl.ai/pricing` calculator default: `$0.048 / image` (= 1k tier); launch-offer banner quoted via search index: `Launch offer: 50% off list prices for FLUX 3 Image generations accepted from 1 October 2026 8:00 AM PT (15:00 UTC) until 8 October 2026 8:00 AM PT` (direct fetch JS-gated; method disclosed; corroborated by bfl.ai homepage `50% off until 10/8`, the-decoder 10-02, Runware 10-04)
- `/pricing` carries NO publication timestamp; date labels live on release-notes. Jul 23 foundation (`FLUX 3 ... Early Access ... multimodal foundation model ... early access phase for FLUX 3 Image in the following weeks`) DISTINGUISHED from Oct 1 Image SKU.

## C. DGX Spark 64GB timestamp — CONFIRMED (resolves TIME_UNRESOLVED → ordinary-eligible)

- `https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/` HTML head + JSON-LD: `"datePublished":"2026-10-02T13:00:39+00:00"`, modified `2026-10-05T19:28:28+00:00`; byline `October 2, 2026 by Allen Bourgoyne` (calendar only in visible text)
- 13:00:39Z is ~8h59m BEFORE 22:00Z cutoff → ORDINARY-ELIGIBLE (Discovery record keeps TIME_UNRESOLVED only because acceptance is hash-pinned; Evidence resolves it here; Selection dispositions).
- Same page: 64GB SKU + Sync Cluster Assistant (2-unit clustering, no extra setup) + Oct 23 third-party availability (Acer/ASUS/Dell/Gigabyte/HP/MSI, from $4,999) = FUTURE availability, NOT W40 shipping.

## D. ELYZA LLM-jp-4 Oct 2 — CONFIRMED (upgrades weak/unverified → release facts verified)

- Hub API: `elyza/ELYZA-Thinking-1.0-llm-jp-4-33b` SHA `6ca556b2ddc4642580752b3a1ae2d7e7681106fc`, created `2026-10-02T00:46:49Z`, modified `2026-10-02T10:27:37Z`; `elyza/ELYZA-Thinking-1.0-llm-jp-4-32b-a3b` SHA `5260ecc249f32ef5005ef940c78f41f130d9c468`, created `2026-10-02T00:47:54Z`, modified `2026-10-02T10:25:43Z`
- License: `license:apache-2.0` (tags + cardData) + LICENSE raw `Apache License ... Copyright 2026 ELYZA, Inc.`; README frontmatter `license: apache-2.0, language: ja en, base_model: llm-jp/llm-jp-4-33b-base`; `reasoning model by ELYZA, Inc. ... for Japanese and English language understanding and generation`, mid/post-trained on llm-jp-4 base (upstream bases: 33b-base 2026-08-14, 32b-a3b-base 2026-04-24, both Apache-2.0)
- Remaining: NO eval/benchmark content consumed → PARTIAL+HOLD stands (release facts VERIFIED, performance NOT).

## E. AstaBrief HF card — CONFIRMED (license + eval)

- `https://huggingface.co/allenai/AstaBrief_8B`: `License: apache-2.0`; body: `licensed under Apache 2.0 and is based on Qwen 3-8B`
- Eval (ScholarQA-CS2 test 100Q): `Qwen3-8B 77.3/77.8/90.6/76.2/64.6; AstaBrief-8B-SFT 83.7/85.2/90.4/87.7/71.3; AstaBrief-8B 87/90.2/89/90.5/78.2` (Average/IngredientRecall/AnswerPrecision/CitationPrecision/CitationRecall); second table SQA-Dev/Test + DeepScholarBench + win-rates. Time remains day-only → HOLD stands.

## F. EnterpriseOps-Gym + AutoSynthData release — PARTIAL (dataset CONFIRMED; standalone NOT_FOUND)

- Dataset page + README frontmatter: `license: apache-2.0` (changed Apr 30, commit c8e538e; arXiv paper v1 banner CC BY-NC-SA 4.0 applies to paper, NOT current dataset/code; GitHub `License: Apache-2.0`); public load_dataset, no gating; Viewer configs oracle/plus_10/15/5_tools.
- Blog (Oct 2): pipeline + Hybrid/ITSM figures + `using the released dataset` link; NO separate AutoSynthData GitHub/HF/license string (site: searches negative). AutoSynthData standalone release = NOT_FOUND (methodology lead only).

## G. arXiv confirmations — CONFIRMED ×2

- 2609.37725: `[Submitted on 29 Sep 2026]`, `[v1] Tue, 29 Sep 2026 14:50:08 UTC`; abstract BrowseComp-Plus +11.4%/-21.5% FLOPs etc. verbatim.
- 2609.31140: `[Submitted on 25 Sep 2026]`, `[v1] Fri, 25 Sep 2026 11:31:02 UTC` (BEFORE 22:00Z cutoff); `Accepted at NeurIPS 2026`.

- artifact_class (this file): CLAIM_LEVEL_DERIVED_NOTE__DELEGATED_RETRIEVAL_LOG (Muse-recorded subagent excerpts; Sol re-verifies via URLs; NOT Muse-read bodies)
