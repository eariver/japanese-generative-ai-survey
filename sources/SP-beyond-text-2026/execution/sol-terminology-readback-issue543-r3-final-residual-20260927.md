# TS-002 Issue #543 — Sol terminology readback r3 final residual

Date: 2026-09-27 JST  
Status: `REQUEST_CHANGES / FINAL_RESIDUAL_MAP_READY / HUMAN_R9_REQUIRED`

## 1. Scope

This review evaluates the Human Publication Preview r8 execution for TS-002 Issue #543 after Muse applied the Sol r2 authoritative terminology map.

This is an edition-local terminology review only. Shared Survey Production Core v2 remains frozen and immutable.

## 2. Reviewed r8 state

Reviewed worker HEAD:

`4c82ffd7fe716ca20a3603cb749db2ba86df8a68`

Reviewed worker tree:

`44f9c0f529c05b0845f721c5dceb4ed8e223511d`

r8 candidate:

- pages: `77`
- PDF SHA-256: `e98f769e7dfb0bfa08f218281747b8fa1973e56f0d28e98a8a50f561ad957464`
- Candidate SHA-256: `9d6cd7dd262ab55bd57eb71048f68c2ccc41cdf90b9bb9be01f9b426be0c0efa`
- lifecycle: `RELEASE_CANDIDATE`
- publication preview: `pending`
- terminal reason: `HUMAN_GATE_REACHED`
- freeze: pending
- release: pending

## 3. r8 execution compliance

PASS:

- Human r8 `REQUEST_CHANGES` was used as the publication-local regeneration authority.
- The existing Frozen Core v2 transition mechanism was used; no Core repair or extension was introduced.
- Repository writes remained inside the TS-002 edition-local allowlist.
- The r2 Sol map was applied rather than reinterpreted.
- Muse did not invent resolutions for unmapped or uncertain reader-facing terms.
- Muse returned twelve uncertain occurrences to Sol as `CANDIDATE_FOR_SOL_REVIEW / NO_MUSE_DECISION`.
- The edition returned to `RELEASE_CANDIDATE / PUBLICATION_PREVIEW pending` without synthesizing Human approval, Freeze, or Release.

The worker behavior on unresolved candidates is specifically accepted as correct executor behavior.

## 4. Why Issue #543 is not yet complete

Sol independently re-read the r8 manuscript after worker completion instead of treating the Muse candidate list as the closure set.

That readback found two classes of residuals:

1. the twelve candidates correctly returned by Muse;
2. additional seed-independent reader-facing terminology and metric-identity residuals not present in the Muse candidate file.

Representative additional residuals included:

- residual `端末間` for End-to-End;
- CosyVoice 2 `区画因果Flow Matching` instead of chunk-aware causal Flow Matching;
- Moshi/Mimi `神経符号` / `RVQ神経符号` and split-RVQ literalization;
- codec `帳` terminology;
- `浮動32`;
- `画素再帰網`;
- generic `〜網` in unambiguous network/model contexts;
- Video Diffusion Models `連合学習` for joint training;
- Imagen Video `振動誘導` and unnamed CLIP Score values;
- unnamed Video Diffusion / Make-A-Video metrics;
- ML text-modality literalizations such as `文章画像` / `文章動画` / `文章音響` / `文章音楽`;
- AudioLDM CLAP/mixup/editing literalizations;
- product-surface `joint化`;
- Ray `首尾keyframe`;
- reception prose `制作者管` and duplicated `への言及への言及`;
- synthesis `frame`, `RVQ神経符号`, and other literal remnants.

These findings mean r8 is a valid regenerated candidate but is not the terminology-final candidate required to close Issue #543.

## 5. Sol source adjudication completed

Sol has now resolved the returned candidates and the independently discovered residuals against already accepted / consumed authority.

The resulting normative map is:

`sources/SP-beyond-text-2026/execution/terminology-issue543/sol-authoritative-terminology-map-r3-final-residual-20260927.md`

Its status is:

`AUTHORITATIVE / SOL_EDITORIAL_DECISION / FINAL_RESIDUAL / APPLY_WITHOUT_REINTERPRETATION`

The map fixes, among other items:

- VALL-E 2 Grouped Code Modeling / Repetition Aware Sampling terminology;
- AudioLDM FD / IS / KL / FAD / OVL identities for existing manuscript values;
- Stable Audio Open FD_openl3 / KL_passt / CLAP score identities;
- MuSTANGO FD / KL / PCM identities;
- Video Diffusion Models FID / IS / FVD and joint-training terminology;
- Imagen Video oscillating guidance / CLIP Score / Sampling Time terminology;
- Make-A-Video CLIP-FID / CLIPSIM / FVD / IS identities;
- CosyVoice 2 chunk-aware causal Flow Matching;
- Moshi/Mimi split RVQ and neural-codec terminology;
- PixelRNN/PixelCNN, codec codebook, End-to-End, ML text-modality, Ray keyframe, reception, and synthesis residuals.

No further editorial judgment is delegated to Muse for these decisions.

## 6. Citation exceptions

Two citation changes are explicitly authorized by Sol and only these two:

1. `SOL-CIT-001`: DAC Balanced data sampling -> `btd008`, while the EnCodec boundary remains `btd007`.
2. `SOL-CIT-002`: the front-matter Wan2.2 open-weight lineage boundary is rewritten to the already established wording and locally bound to `btd124`.

Any additional citation addition/removal/rebinding remains stop-and-report.

## 7. Frozen Core v2 invariant

Core v2 must remain unchanged.

Current frozen identities remain:

- Core implementation SHA: `95c03bf5285cb4b2c1103a14c460574183a8cb93`
- pipeline contract SHA-256: `ee89796245c22072cec98f34931180214a4928c24f399280793cd6420a4c8e71`
- quality contract SHA-256: `b5b955d524fb438c0f1b2c9490bea1da2083e79028d67a55ca424bbfc20f2958`
- research profile SHA-256: `0f575e6d97caec72b2bf8b7f6b78a562d97ca67b2071193417b968ba3d73e6e8`
- publication profile SHA-256: `a6859559dd1b9d42ab8fb4402b74b7bdd8611dbe65c8e02a7b022b545c20f4eb`

If the next repair cannot execute through the already frozen Core mechanism, it must stop rather than modify Core.

## 8. Gate disposition

The current r8 state is already `RELEASE_CANDIDATE / PUBLICATION_PREVIEW pending`.

Frozen Core v2 has no legal path back to the publication-local repair boundary under the already consumed r8 revision.

Therefore:

`REQUEST_CHANGES / FINAL_RESIDUAL_MAP_READY / HUMAN_R9_REQUIRED`

No r9 Human decision is created by this review.

The next action requires explicit Human Owner authorization of the next Publication Preview revision as `REQUEST_CHANGES`, with regeneration boundary `DRAFT_COMPLETE`, solely to apply the finalized Sol r2+r3 terminology maps.

After such authority exists, Muse may only apply the maps, synchronize ledgers, run invariants/build/rendered-text/visual QA, regenerate the candidate, and stop at Publication Preview. Core v2 modification, Freeze, Release, merge, or autonomous new editorial decisions remain prohibited.
