# W43 Evidence r3 source-claim crosswalk (statement → source → bytes)

Status: `EDITION_LOCAL_PROVENANCE / R3_INTEGRATED`
Date: 2026-10-25. Supplement r3 `evidence-authority-supplement-r3.json` (21 sources: 6 retained + 15 new). All raw under `sources/2026-W43`. Fused Discovery locators immutable; r3 splits via supplements.

## Supplement IDs (new)

- Flint article `supplement-src-d2d2f48e181fb4dd` → `https://recursive.com/updates/introducing-recursive-flint` → `runs/20261024T133000Z-muse-r4/raw/recursive-flint-announce-20261024T132900Z.html` 366583B `ce42b796…`
- Flint card `supplement-src-e1fe975d225aaa88` → `https://huggingface.co/RecursiveSI/flint` → `runs/20261025T044100Z-muse-r3-evidence/raw/flint-card-README.md` 6250B `43244381…`
- DeepInfer environ `supplement-src-e20f1cffc1444d3a` → `.../DeepInfer/blob/main/deepinfer/environ.py` → `deepinfer-environ-9bd9cf24.py` 8738B `fe2c5319…` commit `9bd9cf24…` Oct21
- DeepInfer README `supplement-src-d0805b13331ce793` → `.../blob/main/README.md` → `deepinfer-readme-9bd9cf24.md` 4660B `b5562415…`
- DeepInfer LICENSE `supplement-src-d818147e4521ac7a` → `.../blob/main/LICENSE` → `deepinfer-LICENSE-9bd9cf24` 11357B `c71d239d…` Apache-2.0
- GitHub metrics `supplement-src-1a8d33ae41ab22ad` → `github.blog/changelog/2026-10-23-...` → `github-metrics-20261023.html` 107700B `be7faba3…` datePublished `2026-10-23T23:42:03Z`
- FLUX model `supplement-src-1ae0efcded48b6e4` → `https://fal.ai/flux-3-max` → `fal-flux-3-max-model.html` 326207B `9e8ddfd6…`
- FLUX blog `supplement-src-32e30026645a68d3` → `https://fal.ai/blog/introducing-flux-3-max-by-fal` → `fal-flux-3-max-blog.html` 225919B `50ac7df9…`
- Patch rendered `supplement-src-fe148ca1b75a67dd` → `https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/` → `openai-patch-planet-rendered-20261025.md` 3210B `f70ef5b3…` RENDERED_TEXT (curl 9946B spinner only)
- MemT README `supplement-src-baee90a6382ccdbd` → `https://github.com/MemTensor/MemT-1.0/blob/main/README.md` → `memt-readme-e75c13d.md` 10170B `5d576f44…` commit `e75c13d0…` Oct20
- Kimi blog `supplement-src-041ec6c5600beb4d` → `https://www.kimi.ai/blog/kimi-k3-1-pro` → `kimi-k3-1-pro-blog.html` 390347B `86cc8bbe…`
- Nemotron card `supplement-src-9e10348cb212038f` → `https://huggingface.co/nvidia/Nemotron-3.5-Bolt-E4B-4GB` → `nemotron-card-README.md` 59009B `8a06cc67…` OpenMDW-1.1
- Ming README `supplement-src-1d329e6cfb492783` → `.../Ming-3.0-tts/blob/main/README.md` → `ming-readme-028c1ea.md` 74543B `6931f3bd…` commit `028c1ea…` Oct21
- Ming LICENSE `supplement-src-5bb55c72ae60d4a2` → `.../blob/main/LICENSE` → `ming-LICENSE-028c1ea` 1067B `2872f191…` MIT
- Kohaku LICENSE `supplement-src-b751c2c90f23c12a` → `.../KohakuMossTrainer/blob/main/LICENSE` → `kohaku-LICENSE-da5dd97e` 12141B `2e63789e…` commit `da5dd97e…` Oct20

## Retained 6 (GCP corrected)

- Oracle `supplement-src-0226e32d4252d42c` 261750B `8d8ef345…`, AM-Bench `supplement-src-b06a31536a4f162a` 2379235B `fc3b7f96…`, Auto-mode `supplement-src-6f18c05b01b43f45` 599884B `8ed45487…`, Decisions `supplement-src-2a49a7d4f6f2ae5a` 553250B `ea48630a…`, GCP `supplement-src-ea58a61c3678ad4a` 224991B `d77a6291…` (published_at NULL r3; JSON-LD 2026-10-21 vs displayed Oct22 vs first_published 2026-10-22T04:10; preview + coming-soon), MemT paper `supplement-src-927931f4a303eaa6` 7096280B `959206da…`.

## Claim bindings (P1 excerpts)

- GCP claim-1 → src-1 + GCP supplement; datePublished vs displayed; preview + coming-soon.
- Flint claim-1/2 → src-1 + article + card; 512K/256K vs 262144; 125+/150+ with 128K-avg/prefill-excluded/M4 Pro/RTX Spark.
- DeepInfer claim-2 → src-1 + environ + README + LICENSE; DEEPINFER_ENABLE_MTP_VARLEN + DEEPINFER_USE_NEXTN_DECODE default5/0-disable at 9bd9cf24.
- GitHub claim-1/2 → src-1 + changelog; user_selected/auto/product_selected/other/unknown; request_count=model requests not prompts; enterprise/org/user scopes; best-effort integration ID.
- FLUX claim-2/3 → src-1 + model + blog; 10.95/277.80=25.37x vs 12.45/277.80=22.31x; page 22x correct; blog 26.5x/96.2% inconsistent; Elo1139 vendor-cited AA unfetched.
- Patch claim-1/2 → src-1 + rendered; GPT-5.6 Sol; 5-stage; Wiz/Cloudflare; $1B; checker skill; zero CVE; vendor disclosure.
- MemT claim-2/3 + verification → src-1 + paper + README; paper CC BY-NC-SA4.0 vs software PolyForm1.0.0 vs MIT third-party vs excluded weights/data; paper has no license terms.
- Bio/lowresource/Ming Views → materiality_rationale rewritten to team protocol / blinded preference / publisher-cited AA; independent repro ZERO.

Fused Discovery src-1 URLs (Kimi X+blog, Flint blog+HF) immutable; r3 Cards bind ≥2 sources via supplements for split provenance. No new fused single-source URL created in supplements.
