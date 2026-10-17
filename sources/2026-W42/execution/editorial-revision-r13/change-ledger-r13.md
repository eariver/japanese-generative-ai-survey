# W42 r13 change ledger (external audit M01–M06 / m01–m05 closure + Unit B depth)

Status: `EDITION_LOCAL / PROPOSAL_LEDGER`
Date: 2026-10-18 JST. Old: r12 v12.0 (92 paras / 21,281 body chars). New: r13 v13.0 (103 paras / 22,315 body chars; **paragraph-only 103 / 19,193** vs r12 auditor count 82 / 17,004 → **+21 paras / +2,189 paragraph chars** of source-backed depth, no padding).

## M01 Nemotron MTP acceptance unit — RESOLVED (with explicit unconfirmed remainder)
- Before: r12 `MTPによる受理率4.287→4.718`.
- After: `MTPによる平均受理長4.287→4.718トークン` + mechanism sentence (internal drafter proposes several tokens; main model verifies in one forward pass; accepting several at once reduces verification steps) + explicit `復号条件・ドラフト長の詳細は本号の保持資料では未確認であり、断定的な条件づけはしない`.
- Evidence: live NVIDIA developer blog (sidecar S1: MTP/LiLiCorr/QAD/context-reuse/Dynamo sections read 2026-10-18); accepted card claim "MTP boosting 4.287→4.718 acceptance" + in-repo 79pp excerpt. Blog does NOT state greedy/draft-7 — those qualifiers are NOT used (hard gate honored).
- Swept all 7 chapters + tables for `受理率` (zero remaining).

## M02 wet-lab denominator — RESOLVED
- Before: r12 `q6-10` implied 8 clones explain the 42.1% rate; `q6-02` bundled trajectory + titrations.
- After: `q6-02` keeps the screening trajectory (thrombin 0/167→54/208→131/311 etc.); new `q6-10` states the 8-clone titration is a **separate confirmation stage, not the denominator** (`分母と確認工程を混同してはならない`). No linkage invented beyond the accepted card.
- MSA-omission artifact + G4 collapse/recovery kept with caveats; FAP single-target/nM/8.6x framed as scope + safety conditions (sidecar S1 wetlab blog excerpt, derived-note caveat retained).

## M03 word-count methodology — ANSWERED (not gamed)
- r13 reports BOTH: paragraph-only 19,193 chars (auditor-comparable) AND body-with-tables/notes 22,315 chars, labeled separately; per-chapter splits published. No quota claimed; density proof is the TeX PDF itself (19 pages).

## M04 citable bibliography — RESOLVED
- TeX now carries inline `\cite{B01}…` per paragraph/table/note + `thebibliography` with 59 unique keys, each with source-class tag ([一次・発行者]/[論文]/[独立評価]/[二次・参考]). Chapter source boxes split primary vs secondary. Block→key crosswalk in ledger; no EXO scores, no AA ranks; MarkTechPost/OpenRouter/HF-API/X labeled secondary, never primary.

## M05 independent visual QA delivery — RESOLVED (as far as this transport allows)
- Committed: `main.tex` + `preview.sty` + 3-run-stable `main.pdf` (19 pp) + full `main.log` + 19 page PNGs @150dpi + 2 contact sheets + `review-pages-r13.md` (renderable index, per-page density/cite/table checklist, file hashes, retrieval routes).
- Honest limitation recorded: remote fetch cannot be self-certified; auditor text-API failure mode remains possible → documented `PDF_INDEPENDENT_VISUAL_QA_BLOCKED` fallback with exact handoff. Muse self-QA is NOT claimed as independent PASS.

## M06 timestamp provenance — CORRECTED (notice, no rewrite)
- `r12-timestamp-provenance-correction-r13.md`: r12 `generated_at` 03:00/04:00Z vs true generation ~17:42Z Oct 17 (file mtimes + JST commits) = JST-wall-clock mislabeled `Z` (~9–10h ahead). Most probable mechanism stated with evidence; no fabrication alleged; r12 bytes untouched.
- r13 stamps use verified executor UTC (`date -u`, recorded in validation report).

## m01–m05 minors — all RESOLVED
- m01: `分母の practice` → `分母つき開示` (2 sites).
- m02: `上限（呼び出し100回・30分・100万）` → `上限（呼び出し100回・30分・文脈100万トークン）` with paper §3.4 (100-call/30-min/1M-token-window caps) cited in sidecar S2.
- m03: `6名の常駐` → `6名が従業員相当のアクセス権を付与されて参画` (+ table/note `成果ゼロ`→`評価結果未公表` kept from r12).
- m04: removed 6 duplicated blocks (Argon pricing r1-15 merged into pricing para; Maia N2P r2-13; Scion WAL/API r4-16/r4-17; Rosalind areas r6-12; VLA r7-11); space redirected to causal mechanisms (Unit B).
- m05: `成果ゼロ`→`評価結果未公表`, `記事の作法`→factual closings (r3-13, r6-15); `三層モデル`→`三段階のアクセス条件` (METR program, distinct from P5 四局面).
- D closings rewritten (r2-17, r5-15/16, r7-15); P3 heading already distinct.

## Unit B depth (all source-backed, sidecars S1/S2 or accepted cards)
- P1: Minecraft failure-history reading (single trial, 605 deaths, structured-only) [ARGON].
- P2: per-bench temperature practice [LFM]; HBM-vs-context relationship [MAIA].
- P3: LiLiCorr / QAD / context-reuse / Dynamo+600TPS / MOPD-teachers (5, from S1 live blog).
- P4: Codex survivorship/transfer caveats [CODEX]; HydraFusion Max tiering [HYDRA].
- P5: investigation-actor layering [UNINT] (Anthropic self / operator partial / White House response).
- P6: FAP scope+safety [WETLAB]; 4-config comparison ($0.199 vs $0.167, +10.5pp/3¢) [EARTH]; tool contribution (3→52→63, searches, EE%) [EARTH]; golden-workflow construction + 4 unreconciled [EARTH]; saturation warning [EARTH].
- P7: OpenRouter existence-vs-spec separation [GLIMPSE].

## Coverage / dispositions (validator-enforced, 7/7 PASS)
- must_cover mapped to explaining blocks only; boundaries EXPLICITLY_STATED with preserved rationale; frozen `draft-check` 7/7 PASS; `synthesis-check` PASS on pair-built input. Status v13.0 REVISED, PROPOSED/NOT_CANONICAL.
