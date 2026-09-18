# W37 Publication Preview r2 — independent Sol review

Status: `SOL_INDEPENDENT_REVIEW / REQUEST_CHANGES`

Date: `2026-09-19 JST`

Issue: `2026-W37`

Reviewed production authority:

- production commit: `74400d716e703c12efee97707ff0ee97d47f98a8`
- presentation branch HEAD before Sol audit additions: `ab9f15dcadd120a0d4e72d5c9e4f537980686641`
- presentation tree: `59c580c1941459c13a219e551950e618c1e5c0a0`

Exact PDF:

- path: `surveys/weekly/2026-W37/main.pdf`
- SHA-256: `c2298653e959388f359c5dadf0121e28684950343e874c2305179b4c0aa5f4fe`
- bytes: `309850`
- pages: `11`
- CI artifact: `10558181589`

Human Publication Preview r2 decision remains:

`PENDING`

This is an independent Sol review, not a Human decision.

## 1. Canonical Human revision path — PASS

Confirmed:

- Human Publication Preview r1 is canonically recorded as:
  - gate: `PUBLICATION_PREVIEW`
  - revision: `1`
  - decision: `REQUEST_CHANGES`
  - reviewed production commit: `8057a468897f67d3a11bd9287f6f56f0485877ce`
  - regeneration boundary: `ARCHITECTURE_ESTABLISHED`
- Human Architecture approval remains:
  - `APPROVED`
  - Architecture SHA `81e87a64c2418c71340ee8cc1dec28267a55055d2c02d7dbb06e33623efdfcfb`
- current lifecycle:
  - `RELEASE_CANDIDATE`
  - next action `PUBLICATION_PREVIEW`
  - terminal `HUMAN_GATE_REACHED`
  - Publication Preview r2 decision `PENDING`
- no Freeze / Release;
- main unchanged;
- Production Line unchanged;
- shared-Core changed paths in the r2 run: `0`.

The no-Core canonical revision route worked as intended.

## 2. Issue #501 natural technical Japanese — PASS

The r1 forced technical calques are materially repaired.

Independent reader-facing source scan confirms zero technical-use occurrences of the previously flagged substitutions:

- `模型`
- `符号`
- `道具立て`
- `代理人`
- `砂場`
- `給仕`
- `引擎`
- `許し`
- `札の...`
- `訳し`
- `混合専門家`
- `検出子`

The r2 surface uses established technical terminology such as:

- モデル / 言語モデル / テキストモデル
- コード / コーディング
- トークン
- エージェント
- エージェントハーネス
- サンドボックス
- サービング / 推論基盤
- エンジン
- ライセンス
- モデルカード
- 翻訳
- MoE / Mixture-of-Experts
- 評価用モデル
- IOC / 侵害指標

Independent reread finds the W37 r2 body substantially more natural and technically legible than r1.

Issue #501 remains open only for generic Core/QA hardening; the W37 r2 artifact-specific language defect is repaired.

## 3. Issue #506 reviewer provenance — PASS

Current Worker review artifacts correctly identify:

`Worker/Agent (Muse Spark)`

Confirmed for:

- Draft language QA;
- reader-surface semantic review;
- semantic/editorial review;
- visual review.

No current r2 Worker review self-identifies as ChatGPT, Sol, or Human.

The r2 dossier explicitly states that it is not an independent Sol review and not a Human decision.

Issue #506 remains open for generic enforcement; W37 r2 artifact-level provenance is repaired.

## 4. Exact PDF / visual review — PASS

Sol independently downloaded the exact CI artifact and verified:

- SHA-256: `c2298653e959388f359c5dadf0121e28684950343e874c2305179b4c0aa5f4fe`
- bytes: `309850`
- pages: `11`
- A4
- unencrypted
- PDF creation metadata: `2026-09-18T16:44:20Z`
- all 11 pages render successfully.

Visual inspection found:

- no clipping;
- no overlap;
- no broken Japanese glyphs;
- no black-square rendering;
- stable cover/contents/body/bibliography layout.

Page 8 is relatively sparse, but not a blocking layout defect.

## 5. Citation / X public auditability — PASS

Independent source scan confirms:

- unique cited keys: `19`
- bibliography records: `19`
- missing keys: `0`
- unused records: `0`
- direct X status URLs: `8`
- internal GitHub blob URLs: `0`
- internal repository paths in reader prose: `0`.

Independent Snowflake reconstruction confirms all 8 cited X posts are inside the ordinary W37 window.

X remains community/context evidence only and does not establish technical specifications, benchmarks, pricing, licenses, release timing, or architecture.

## 6. Architecture / evidence boundary carry-through — PASS

The r2 reader surface preserves the approved W37 Architecture:

- Financial Services on Astra remains distinct from GPT-Live-1 and Agents API;
- GPT-Live-1 remains a separate voice layer;
- Agents API remains a separate harness;
- DeepSeek ahead-of-Pro comparison remains vendor-attributed;
- Sep 14 routing remains future/post-window;
- Fusion timestamp remains `2026-09-11T17:00:00Z`;
- Fusion 39% remains a maximum, not uniform;
- MiniCPM/North/Ling remain card/vendor bounded;
- North judge/license boundaries remain visible;
- Threat cases remain vendor investigations;
- resignation discourse is not Architecture-bearing;
- GLM rumor remains excluded.

No upstream research or Architecture revision is required.

## 7. BLOCKING — Issue #434 semantic Publication Boundary false negative

The r2 surface still contains internal retrieval/production-process narration.

Reader-facing examples:

### DeepSeek section

`surveys/weekly/2026-W37/sections/40-efficient-flagship.tex`

contains:

> ベンチマーク表や図の詳細は取得の打ち切りでたどり切れておらず

This wording exposes the internal collection/retrieval stopping condition rather than the reader-relevant verification boundary.

The same wording is present in canonical Draft r2, so this is not only a TeX transformation problem.

### Sources & Limitations

`surveys/weekly/2026-W37/sections/99-source-notes.tex`

contains:

> 全文PDFやIOC、ベンチマーク手法の詳細、図表の値は参照の打ち切りで取り切れていない

Again, this narrates production process rather than publication-facing scope.

Current Worker semantic/editorial review says there is “no retrieval-process narration”, so the current semantic review produced a false negative.

Issue #434 has been reopened with W37 evidence.

### Required repair

Express only the reader-relevant limitation.

Examples of acceptable semantic direction:

- instead of “取得の打ち切りでたどり切れておらず”:
  - “本号ではベンチマーク表・図の詳細な検証までは行っていない”
  - or another natural equivalent that does not imply the source itself lacks those details;
- instead of “参照の打ち切りで取り切れていない”:
  - “本号では全文PDFやIOC、ベンチマーク手法・図表の詳細までは扱わない”
  - or equivalent.

Do not falsely say “資料に存在しない” when the real boundary is non-consumption.

Also re-read all reader-facing Draft/TeX for equivalent process narration, including variants such as:

- retrieval/取得を途中で止めた;
- 参照を打ち切った;
- budget/tool/time limits;
- internal source-consumption mechanics.

Transparent reader-facing verification scope is allowed; internal production mechanics are not.

## 8. Execution timestamp provenance defect — CORRECTED APPEND-ONLY, NONBLOCKING FOR PDF

Independent audit found future-dated execution/Human-Gate timestamps.

Generic tracking:

Issue #507.

W37 edition-local correction ledger:

`sources/2026-W37/execution/provenance/w37-execution-time-correction-20260919.md`

The ledger:

- preserves original historical bytes;
- marks future-dated values invalid as actual wall-clock times;
- does not invent replacement seconds;
- uses Git commit timestamps and valid Human authority only as ordering evidence;
- records that the exact historical wall-clock second is not recoverable where absent.

This defect does not alter publication content or PDF bytes and therefore does not independently require Draft/PDF regeneration.

However any next Human decision or Worker review must use actual timezone-aware current wall time and must not be future-dated.

## 9. W37 r2 Human-review readiness

Content readiness:

- Japanese technical language: PASS
- visual/PDF: PASS
- citations/X auditability: PASS
- vendor attribution: PASS
- temporal boundaries: PASS
- reviewer identity: PASS
- Architecture fidelity: PASS

Blocking reader-boundary finding remains:

- production/retrieval “打ち切り” narration (#434).

Therefore r2 is not yet suitable for Human approval as-is.

## 10. Required regeneration boundary

Because the DeepSeek process wording exists in canonical Draft r2:

`ARCHITECTURE_ESTABLISHED`

is the safe canonical boundary.

Preserve unchanged:

- Grok/X;
- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- approved Architecture;
- Human Architecture approval.

Regenerate only:

`Draft -> reader surface -> PDF -> QA -> Publication Candidate -> fresh Publication Preview r3`

No fresh research is required.

The language rewrite should be narrowly bounded to publication-process narration and should preserve all successful r2 natural-language repairs.

## 11. Sol verdict

`REQUEST_CHANGES`

Blocking finding:

1. Issue #434 semantic Publication Boundary leak: internal retrieval/production stopping narration remains in reader-facing Draft/TeX.

Nonblocking but audit-significant finding:

2. Issue #507 future-dated/timezone-mislabeled execution timestamps, now transparently covered by an append-only W37 correction ledger.

Human Publication Preview r2 decision remains:

`PENDING`

Do not record a Human r2 decision merely because Sol requested changes.

Normal next endpoint after Human accepts this revision request:

`RELEASE_CANDIDATE / fresh Publication Preview r3 PENDING`.
