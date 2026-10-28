# W43 r3 source crosswalk (edition-local, UNVALIDATED)

Status: `EDITION_LOCAL_EDITORIAL_BYPASS / UNVALIDATED`. Citation keys used in r3 preview tables/figures/code and ledger `table_rows[]`.
`archive` = byte-archived primary in repo (`—` = no archived bytes; claim rests on accepted Evidence/screening record).
Clock precision: exact UTC / day-only / FUTURE / version-pin. No URL invented; absent = SOURCE_NOT_VERIFIED.

| key | best primary URL | archive path in repo | clock | evidence task | class |
|---|---|---|---|---|---|
| KIMI-X | https://x.com/Kimi_Moonshot/status/2113680701770068067 | collectors/.../muse-r2/raw/x-kimi-k31pro-2113680701770068067-20261024T115000Z.html | 2026-10-23T17:15:24Z exact | task-98f3617da0de43652fcd | FIRST_PARTY (X HTML raw) |
| KIMI-BLOG | https://www.kimi.ai/blog/kimi-k3-1-pro | collectors/.../muse-r3-evidence/raw/kimi-k3-1-pro-blog.html | day-only 2026-10-23 | task-98f3617da0de43652fcd | FIRST_PARTY_METADATA |
| FLINT-CARD | https://huggingface.co/RecursiveSI/flint | collectors/.../muse-r3-evidence/raw/flint-card-README.md | 2026-10-21 | task-4cea29268a1329179dac | FIRST_PARTY (card bytes: 2.5B/2.2B/262144/Apache-2.0) |
| FLINT-ART | https://recursive.com/updates/introducing-recursive-flint | collectors/.../muse-r4/raw/recursive-flint-announce-20261024T132900Z.html | 2026-10-21 | task-4cea29268a1329179dac | FIRST_PARTY (512k対応/256k推奨の原文) |
| NEMO-CARD | https://huggingface.co/nvidia/Nemotron-3.5-Bolt-E4B-4GB | collectors/.../muse-r3-evidence/raw/nemotron-card-README.md | 2026-10-23 | task-8f140062cf7044ea898a | FIRST_PARTY (8B/4B/64K/OpenMDW-1.1) |
| NEMO-COMMITS | https://huggingface.co/api/models/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB/commits/main | collectors/.../muse-r4-postcutoff/raw/nemotron-hf-commits-20261023.json | 15:12–19:03Z | task-8f140062cf7044ea898a | FIRST_PARTY_METADATA |
| DI-README | https://github.com/deepseek-ai/DeepInfer/blob/main/README.md | collectors/.../muse-r3-evidence/raw/deepinfer-readme-9bd9cf24.md | pin 9bd9cf24 | task-409f6833c40c6428a43e | FIRST_PARTY (README 24-28行: env名・seq_seed) |
| DI-ENV | https://github.com/deepseek-ai/DeepInfer/blob/main/deepinfer/environ.py | collectors/.../muse-r3-evidence/raw/deepinfer-environ-9bd9cf24.py | pin 9bd9cf24 (8738B) | task-409f6833c40c6428a43e | FIRST_PARTY (129-132・197行) |
| DI-LICENSE | https://github.com/deepseek-ai/DeepInfer/blob/main/LICENSE | collectors/.../muse-r3-evidence/raw/deepinfer-LICENSE-9bd9cf24 | pin 9bd9cf24 | task-409f6833c40c6428a43e | FIRST_PARTY (Apache-2.0) |
| MEMT-README | https://github.com/MemTensor/MemT-1.0/blob/main/README.md | collectors/.../muse-r3-evidence/raw/memt-readme-e75c13d.md | 2026-10-20 | task-b09782ca929b9fa55af1 | FIRST_PARTY (208-219行: CC BY-NC-SA 4.0 / PolyForm NC 1.0.0 / MIT / weights除外) |
| duet-blog-1021 | https://claude.com/resources/articles/claude-duet | — | day-only 2026-10-21 | task-3670fe4328b9fa322a0b | DERIVED_ONLY (body unconsumed residual) |
| 1pw-blog-1022 | https://1password.com/blog/1password-for-ai-agents | — | 2026-10-22 | task-673368bcdc8bcd59d611 | FIRST_PARTY (coming-soon) |
| automode-art-1022 | https://claude.com/resources/articles/auto-mode-default-in-claude-code | — | 2026-10-22 IN / 8-7 OUT / 翌週FUTURE | task-ac27404fe35327b74df9 | FIRST_PARTY |
| flux-page-1019 | https://fal.ai/models/blackforestlabs/flux-3-max/text-to-video | collectors/.../muse-r3-evidence/raw/fal-flux-3-max-model.html + fal-flux-3-max-blog.html | 2026-10-19 | task-02df2773fd2e9fdb1cd5 | FIRST_PARTY_METADATA + VENDOR_BENCH (数値は再計算VERIFIED) |
| flux-elo-1139 | https://fal.ai/models/blackforestlabs/flux-3-max/text-to-video | same as above | snapshot差 (+47/+50、1089導出値) | task-02df2773fd2e9fdb1cd5 | DERIVED_ONLY (AA原表未取得) |
| flux-keyframes-conflict | — (PRNewswire PR原文・Oct18 FAQ原文ともに未取得) | — | UNRESOLVED | task-02df2773fd2e9fdb1cd5 | UNRESOLVED (FAQ由来とされる未照合記述) |
| flux-speed-recalc | https://fal.ai/models/blackforestlabs/flux-3-max/text-to-video | same as flux-page-1019 | Oct19 PR / blog | task-02df2773fd2e9fdb1cd5 | VERIFIED_DIRECT (独立再計算) |
| voxtral-announce | https://mistral.ai/news/voxtral-3 | — | day-only 2026-10-20 | task-18a859ebb1ef50040078 | FIRST_PARTY (TTS言語数未解決) |
| ming-readme-license | https://github.com/inclusionAI/Ming-3.0-tts | collectors/.../muse-r3-evidence/raw/ming-readme-028c1ea.md + ming-LICENSE-028c1ea | repo-IN 2026-10-19 | task-4aa7ba129fdeec8b2555 | FIRST_PARTY (MITバイト確認) |
| ming-aa-cited | https://github.com/inclusionAI/Ming-3.0-tts | — | — | task-4aa7ba129fdeec8b2555 | DERIVED_ONLY (AA原表未取得) |
| eleven-blog | https://elevenlabs.io/blog/realtime | — | day-only 2026-10-20 | task-4514088790849f9ca699 | FIRST_PARTY (指南未開封) |
| patch-rendered | https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/ | collectors/.../muse-r3-evidence/raw/openai-patch-planet-rendered-20261025.md | day-only 2026-10-21 RENDERED_TEXT | task-5d21d93e7679f5441b8a | FIRST_PARTY (bot-wall・原本未閲覧) |
| securing-page-rss | https://openai.com/index/securing-our-frontier-model-training-environment/ | — | page day-only / RSS 10:00Z secondary | task-eb7312062a02d1c37826 | FIRST_PARTY_METADATA |
| bio-page | https://openai.com/index/scaling-ai-research-for-complex-biological-data/ | — | day-only 2026-10-21 | task-6c420e98c87871e4a2a0 | FIRST_PARTY (班内・wet-lab未) |
| lowres-page | https://openai.com/index/low-resource-programming-languages/ | — | day-only 2026-10-19 | task-160489b77720f40bd1e1 | FIRST_PARTY (ベンダー測定・hidden保持) |
| decisions-page | https://openai.com/index/decisions-api | collectors/.../muse-r2-evidence/raw/openai-api-changelog.html (changelog bytes) | day-only 2026-10-22 | task-d278dfe78685d601d67a | FIRST_PARTY (endpoint/field/TTL未検証→例はILLUSTRATIVE) |
| tanstack-gh | https://api.github.com/repos/TanStack/ai/releases/tags/%40tanstack%2Fai%401.0.0 | collectors/.../muse-r4-postcutoff/raw/tanstack-ai-release-1.0.0.json | 2026-10-22T15:18:14Z exact | task-20a36d83656e2a4bc1b4 | FIRST_PARTY (npm 15:21:49Zで裏づけ) |
| tanstack-blog | — (URL未取得。本文書では日付のみ2026-10-23の存在として扱い製品時刻に読まない) | — | day-only 2026-10-23 | task-20a36d83656e2a4bc1b4 | FIRST_PARTY_METADATA (UNRESOLVED分離) |
| deepseek-1017 | https://api-docs.deepseek.com/news/news261017 | — | day-only 2026-10-17 | task-d5bceca2dab4af9d685b | FIRST_PARTY (SHA未取得・課金未試験) |
| recap | — (P1–P8横断の編集合成) | — | — | — | DERIVED_ONLY / LIMITED (新規数値なし) |

Preserved raw vs derived rule: `archive`列に経路があるものだけを一次バイト典拠として引用し、それ以外は受理Evidence・screening記録の範囲で `SOURCE_REPORTED / DERIVED_ONLY / LIMITED / UNRESOLVED` とする。`VERIFIED_DIRECT` は独立再計算（FLUX算術・時刻突合）に限定する。
