# r6 license corpus — full operative terms consumed 2026-10-17

Run: `20261017T100000Z-muse-r6`. All URLs + access method + date logged; claim kind tagged.

## 1. FLUX Kommunity License v1.0 — FULL TEXT CONSUMED (HF repo LICENSE.md via resolve URL)
- URL: https://huggingface.co/black-forest-labs/flux-3-image-klein/resolve/main/LICENSE.md
- [PRIMARY-LICENSE] Non-commercial + Qualifying User (<$5M gross annualized revenue, affiliates incl.) commercial OUTPUT use only; production use solely to generate Outputs as Qualifying User; separate commercial license otherwise (bfl.ai/licensing).
- [PRIMARY-LICENSE] Derivative INCLUDES distillation/synthetic-data training of other models (§1a) — training competitors on Outputs is licensed-restricted.
- [PRIMARY-LICENSE] Restrictions: no military/surveillance/biometrics; no unlawful/CSAM; GDPR/EU-AI-Act/privacy compliance; NO improving similar AI models with Outputs (§4b); export controls; attribution notice required; unilateral termination + patent retaliation (§8c); indemnification; HIGH-RISK USE disclaimer.
- [PRIMARY-LICENSE] Third-party/FOSS components may be inside (§9) — "open-source components" exist under separate terms; the MODEL license is NOT OSI open-source.
- Repo created 2026-10-13T10:58:40Z (IN clock); 46,123 downloads; gated:auto; BF16/FP8/NVFP4 + upsampler + ComfyUI pack.

## 2. Beam Apache 2.0 — FULL TEXT CONSUMED (repo LICENSE via resolve URL)
- URL: https://huggingface.co/reflection/Beam-1.0-501B-A23B/resolve/main/LICENSE
- [PRIMARY-LICENSE] Standard Apache 2.0 §§1–9: perpetual/royalty-free use/modify/distribute/sublicense; patent grant + retaliation; NOTICE retention; NO output restriction; NO revenue cap; NO display-attribution duty; trademark withheld; AS-IS.
- Contrast for readers: Beam = only OSI-style permissive license among W42 large open-weight releases.
- Repo created 2026-10-07T19:52:01Z (pre-window creation; RELEASE Oct 16 IN); 188 shards; 1,148 downloads; chat template (Harmony-XML, effort 8–512).

## 3. Muse Model License — OPERATIVE TERMS VERIFIED (HF model page + AMD mirror commit + 3 explainers)
- URLs: https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B (LICENSE section); AMD mirror commit 12d1fb2 (full license text mirror).
- [PRIMARY-LICENSE] Broad grant incl. distill/merge/sell; §2 "Built with Muse Spark Open" display duty (UI/docs/site/settings); Derivatives incl. output-improved models; copyright/license/Usage-Policy retention.
- [PRIMARY-LICENSE] §3 MaaS-only $20M aggregate-gross-revenue separate-agreement trigger; internal/research/non-MaaS commercial + feature-embedding EXEMPT; no MAU cap. NOT OSI-approved (Meta: "limited commercial terms").
- Gap: license file read via page/mirror excerpts, not a single canonical LICENSE.md fetch — operative clauses triple-corroborated; full-file byte capture pending.

## 4. OpenMDW-1.1 — OPERATIVE TERMS VERIFIED (openmdw.ai + Nemotron LICENSE file + LF adoption)
- URLs: https://openmdw.ai/license/1-1/; https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16/blob/main/LICENSE ("Add OpenMDW-1.1 LICENSE"); LF press 2026-05-28 (Cosmos/GR00T/Ising/Nemotron adoption).
- [PRIMARY-LICENSE] Model Materials (models + artifacts); no-restriction dealing under copyright/patent/database/trade-secret; NO output obligations; retain agreement + notices; user-side rights-clearing + due diligence; AS-IS; no liability.
- Gap: Super VL repo's own LICENSE file not individually opened (Lightning sibling confirmed; Super VL card states OpenMDW-1.1).

## 5. LFM Open License v1.0 — OPERATIVE TERMS VERIFIED (liquid.ai page + 1.2B repo LICENSE)
- URLs: https://www.liquid.ai/lfm-license (summary/FAQ/full text + Apache diff); https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct/raw/main/LICENSE.
- [PRIMARY-LICENSE] Apache-based + §5 commercial-use condition: free commercial use ENDS at $10M annual revenue (contact sales@liquid.ai beyond); research/non-commercial unaffected; hosting-platform distribution permitted (§4); auto-termination on breach (§11).
- Attribution: LFM Open License v1.0 is the FAMILY license (1.2B card: license:other/lfm1.0); 24B-A2B page points to "our model license" — family attribution with 24B-file confirmation gap noted.

## 6. Granite Apache 2.0 — TAG-VERIFIED (HF API cardData license:apache-2.0; NO license file in repo siblings)
- API: license tag apache-2.0; repo created 2026-10-14T21:38:09Z (IN clock); 567 downloads; siblings list has NO LICENSE file → Apache status = metadata-tag claim, text file absent. Logged limitation (contrast Beam's full file).

## 7. MiniCPM-V 4.7 Apache 2.0 — TAG-VERIFIED (HF API license:apache-2.0; NO license file in siblings)
- API: license tag apache-2.0; repo created 2026-10-07T07:07:30Z (pre-window creation; RELEASE Oct 12 IN); 36,252 downloads/866 likes; 35.2B params. Same tag-only limitation as Granite.

## Reader comparison (licenses, NOT marketing titles)
| Release | Weights live | License (evidence) | OSI open-source? | Commercial gate |
|---|---|---|---|---|
| Beam 501B | HF 188 shards | Apache 2.0 FULL TEXT | Yes (license is) | None |
| Granite 4.1 8B/30B | HF live | Apache 2.0 TAG-ONLY | Tag claims so; file absent | None claimed |
| MiniCPM-V 4.7 | HF live | Apache 2.0 TAG-ONLY | Tag claims so; file absent | None claimed |
| LFM2.5-24B | HF (vendor) | LFM Open 1.0 FULL TERMS | No (revenue cap) | $10M revenue cap |
| Spark Open 816B | HF + gardens | Muse Model License OPERATIVE | No (MaaS gate + attribution) | $20M MaaS-only gate |
| FLUX 3 Klein | HF live | Kommunity FULL TEXT | No | Non-commercial + <$5M output-only |
| Nemotron 3.5 | HF/NIM | OpenMDW-1.1 OPERATIVE | Permissive (LF framework) | None (user clears rights) |
| Glimpse | NOT open (API/chat) | Proprietary service | n/a | n/a |
| GLM-Legal | NO weights (API-gated) | Unpublished rate card | n/a | Application-only |
