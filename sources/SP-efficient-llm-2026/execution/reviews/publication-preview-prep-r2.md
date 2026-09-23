# Publication Preview prep r2 — SP-efficient-llm-2026

Status: `RELEASE_CANDIDATE / HUMAN PUBLICATION PREVIEW R2 PENDING`
Date: `2026-09-23`
Author role: Muse Spark (worker/execution review). Operator package for Sol review and
Human Preview r2. NOT Human-approved. No Freeze/Release performed.
Revision chain: r1 `bc6e280c668a4a17ff98dae58fc574cdce701cce9dd8926eb8b1138e82a46e0b` (REQUEST_CHANGES) -> r2 `8a9a721ac35b2e5baa2e20162b5a6ba4ae63945d512d985484aeae56073a23c1` (pending Sol review).

Working title: **Efficient Intelligence — LLMを速く、軽く、安くする技術史**

Human REQUEST_CHANGES r1 (reviewed commit `1266a5f02d5f056d634bd26649ebc67e61c6beee`, reviewed 2026-09-23T08:39:00+09:00 by Human Owner):
`かなりいいですが、加えてIssue 520と521を対応して欲しいです。` plus Sol citation-policy wording correction.
Record: `sources/SP-efficient-llm-2026/gates/reviews/publication-r1.json` (`996f0b582c1c07a99ee4687ba1bdb8d5b3e2fb35790869bcb8df5d959152e568`).
Boundary: `VALIDATED_DRAFT`. Architecture approval remains active.

## 1. Exact ending authority

- Branch: `special/efficient-llm-2026-work`
- Reviewed main guard: `175b327f6126e2f0759861067852105ee5a290aa` (untouched throughout)
- r1 rejected PDF SHA: `bc6e280c668a4a17ff98dae58fc574cdce701cce9dd8926eb8b1138e82a46e0b` (66pp, 850455 bytes)
- r2 PDF SHA: `8a9a721ac35b2e5baa2e20162b5a6ba4ae63945d512d985484aeae56073a23c1`
- r2 PDF bytes: `850785`, pages: `66` (unchanged count, no forced pagination)
- r2 source `main.tex` SHA: `87bcb707e13cfde7e3d589271415b66e42385d4c7359f3bb492e9adf2d09fabe` (293777 bytes; r1 was `b09ab351…` 293423 bytes)
- Build: CI `Build Special survey PDF` run `35801995228` on HEAD `34244ff04ef3b9bc733e73b4f053a300061d2be7`, zero blocking findings, artifact digest matches committed bytes
- `references.bib` SHA: `9c0edead748c24beea8fd9a2e97982d7e6dd7b0086ab0b30906286e09f8478d2` (110 entries, unchanged, all cited keys resolve)

## 2. Publication Candidate r2

- Path: `sources/SP-efficient-llm-2026/publication/v2/publication-candidate-v2.json`
- File SHA-256: `adf22516235c5a5db2a89f9a3facd6d5af559eac0ad564d373fd1b1a7a5e9638`
- Status: `READY_FOR_PUBLICATION_PREVIEW`
- Candidate SHA (inner): `6b9fd9059fc068674e63ec1f7e987fa1c2a9e7f4e008f96033909b463bcb62c4` (r1 inner was `0499da130ceb286f…`)
- Binds exact r2 manuscript/source/PDF/bundle/semantic/visual bytes (see §4)

## 3. Exact changed reader-facing lines (`surveys/special/efficient-llm-2026/main.tex`)

Three bounded repairs only; no Draft/Architecture/Evidence/Selection rollback; no unrelated layout redesign.

### A. Issue #521 — DeepSeek V4.1 Flash active-parameter wording (correctness, publication-boundary preserving)

Old (r1):
`一つ目の実装点は、数百B級の総量に対して作動量を一桁B級前後に抑える疎活性化を土台に、注意と記憶の保持を同時に圧縮する設計である\autocite{v41report}。`

New (r2):
`一つ目の実装点は、552Bの総量に対して、入力では8B、出力では16Bを作動させる非対称な構成を土台に、注意と記憶の保持を同時に圧縮する設計である\autocite{v41report}\autocite{v41card}。この入出力の非対称は文書化されたCausal Encoder--Decoder設計の一部であり、汎用的な疎活性化のみによるものではない。`

- Preserves asymmetry explicitly; does not describe both phases as 一桁B級前後
- Does not imply split caused solely by generic sparse MoE
- Bound to already-accepted first-party DeepSeek authorities `v41report` + `v41card` (both contain 552B/8B/16B per Evidence `dba89409…`)
- No benchmarks, no ranking, DeepSeek-only (Qwen/Kimi/GLM untouched except trivial reflow)

Comparison table (Section 8, `比較の軸` row `総量と作動量`):
Old DeepSeek cell: `数百B級と一桁B級前後`
New DeepSeek cell: `総量552B / 入力8B・出力16B`
Full r2 row: `総量と作動量 & 総量552B / 入力8B・出力16B & 百B級強と一桁B級前後 & 線形系・数百B級と数十B級前後 \\`
Qwen/Kimi/GLM cells byte-identical except layout reflow.

Semantic checks (worker/execution review PASS):
- No DeepSeek V4.1 summary remains characterizing whole active range as merely 一桁B級前後 (remaining 一桁B級前後 is Qwen-only, lines for Qwen prose + table Qwen cell)
- Prose and table agree (552B / 8B input / 16B output)
- Numbers clearly bound to DeepSeek V4.1-Flash with v41report+v41card
- Prefill/input and decode/output distinction consistent (input 8B, output 16B not reversed; P1 プリフィル/デコード mapping preserved)
- No vendor benchmark ranking added

### B. Issue #520 — p.56 glossary first-table layout (layout-only)

File: `surveys/special/efficient-llm-2026/main.tex`, glossary head.

Old:
```
\subsection*{用語集}
本巻で使う技術用語の定義を集めたものである。節をまたいで同じ言葉が同じ意味で使われていることを確かめるために置いた。
\begin{tabular}{@{}p{0.18\textwidth}p{0.75\textwidth}@{}}
```

New:
```
\subsection*{用語集}
本巻で使う技術用語の定義を集めたものである。節をまたいで同じ言葉が同じ意味で使われていることを確かめるために置いた。\par
\noindent
\begin{tabular}{@{}p{0.18\textwidth}p{0.75\textwidth}@{}}
```

- Minimum layout-only correction; no glossary content rewritten; no unrelated page redesign; no appendix redesign
- r1 log had ~70pt Overfull hbox for this table with VISUAL PASS (defect); r2 log has no ≥20pt overfull (see §5)

### C. Sol citation-policy wording correction (reader-facing frontmatter)

Old (`記号と表記の約束` tail):
`引用は一次資料・公式文書・実装記録・公開手順書に限定し、受容記録は配置依存の観察として扱う。`

New:
`技術的事実を確定する典拠は一次資料・公式文書・実装記録・公開手順書を基本とし、受容記録やコミュニティ資料を引用する場合は配置依存の観察・再現の手がかりに限定し、技術的事実の根拠には用いない。`

- Clarifies technical-fact authority vs community/reception as observation/reproduction leads only
- `引用の約束` subsection unchanged and now semantically consistent (already states reception as observation, not technical-fact grounds)
- Does not broaden community evidence authority

## 4. QA authority SHAs (all fresh r2; r1 records retained as rejected history, not reused)

- Reader manuscript: `cf7aca20714a23ba0b909fb62d79fe644c5e1fbc0d68ebc16b883d0a408f416e` (9657 bytes; r1 was `f99c3b93…`)
- Quality regression bundle (4 DETERMINISTIC PASS): `a3f1b649732571dcfe5d713b28352c20f0edee0f90f6b7874ffc2b049130c0a9` (r1 was `08c0e358…`)
- Deterministic: `identifier-preservation`, `pdf-preflight` (CI 35801995228, 66pp, 0 blocking, 18 layout), `subject-entity-property-binding` (110/110 keys), `empty-wrapper-suppression` (10/10 sections non-empty)
- Semantic editorial review (9 checks PASS, worker/execution review): `6f5e7ff106066fe59ea08ec51d4ea7ccec9574deef327cd78505db023d446c5a` (r1 was `c60513eb…`)
- Visual review (5 checks PASS, worker/execution review, full 66pp render): `fae79e6739beb225e6c810bf9de2943729853a1b37e792ddc651765425b70487` (r1 was `c4ae1c38…`)
- Reader-surface gate: `d5c95b52ca6b0a3e3058ec0b9e17d4aba7563f65ad7ca8822ee9457869bee01e`
- Surface semantic review: bound to r2 `main.tex` exact bytes, worker/execution review PASS
- Reviewer authority truthful: all r2 semantic/visual judgments recorded by Muse Spark as worker/execution review; NOT Sol, NOT Human. Sol will independently review r2 afterward.

## 5. Layout guard and visual results

Edition-local guard: `sources/SP-efficient-llm-2026/execution/validation/overfull_hbox_guard.py` + `overfull-guard-r2.json`.
Policy: ≥20pt BLOCK, 10–20pt REVIEW_REQUIRED, <10pt RECORD. r2 acceptance requires MAX <20pt with explicit disposition for every 10–20pt.

- r1 max: ~70pt (p.56 glossary, BLOCK-level but passed as VISUAL PASS — defect leading to CV2-DM-018)
- r2 max: `10.0pt` (PASS, <20pt BLOCK threshold)
- r2 counts: total 18, BLOCK 0, REVIEW_REQUIRED 12 (all exactly 10.0pt at TeX lines 1204–1280, full-width tabularx tables), RECORD 6 (8.99994pt at lines 1159–1190)
- 10–20pt disposition (rendered visual): all 12 correspond to full-width appendix/capstone tabularx tables; full-PDF render shows all within margins, no clipping, no overlap; glossary pp.56–58 within bounds; disposition recorded in visual review `TECHNICAL_NOTES_TAIL_NEEDSPACE` and here
- Page count: `66` before and after (no forced pagination; legitimate reflow would have been fully reviewed, but count unchanged)
- PDF bytes: r1 850455 → r2 850785 (+330 bytes from bounded wording + layout fix)

Visual QA (worker/execution review, full render — not sampled):
- p.1: title/abstract/metadata clean, no overflow
- pp.4–5 TOC: 10 sections + subsections with page numbers, hierarchy intact
- pp.39–45 capstone (§8): DeepSeek r2 wording + comparison table render clean, no clipping, no ranking, boundary boxes intact
- pp.46–49 measurement (§9): tables/boxes clean
- pp.53–59 appendix/glossary: all tables within margins; p.56 first glossary table entirely within text/page bounds, right-edge clipping 0, no cropped glyphs, no orphan header; p.57 and p.58 glossary tables correct, no regression
- pp.60–66 references: 110 entries, one-column layout, no overflow, no broken URLs
- Full 66pp: no overlap, no blank page (min chars 655 on p.1; glossary 681–986; refs 966–4022), no page hole, no header/footer corruption, no bibliography regression
- Render method: `pdftoppm` 100–150dpi for key pages + `pypdf` text-length audit for all 66; CI log blocking 0

## 6. Publication-surface revalidation (frozen-Core canonical mechanism)

- Prior checkpoint: `sources/SP-efficient-llm-2026/orchestration/v2/checkpoints/DRAFT_COMPLETE.json` (`9d795a31…`, byte-identical, never rewritten)
- Revalidation record: `sources/SP-efficient-llm-2026/publication/v2/publication-surface-revalidation-r1.json` (`380cedca0381c075e03fe3508eb349483e2e628a0f3729a2b08cc4a91b4311ac`)
- Reason class: `REVIEWED_CORE_CHANGE` (only enum in frozen Core; reason text explicitly records Human REQUEST_CHANGES Issues #520/#521 + citation repair; shared Core implementation unchanged)
- Superseded (7/7 publication surface, prior→new): validated-source `b09ab351…→87bcb707…`, publication-pdf `bc6e280c…→8a9a721a…`, reader-manuscript `f99c3b93…→cf7aca20…`, quality-bundle `08c0e358…→a3f1b649…`, semantic `c60513eb…→6f5e7ff1…`, visual `c4ae1c38…→fae79e67…`, surface-gate `417e49ac…→d5c95b52…`
- Preserved upstream: all Draft/Architecture/Evidence/SelectionCheckpoint bytes byte-identical (verified by `_verify_preserved_provenance`; state VALID)
- Binds: new PDF (66pp 8a9a721a), fresh semantic, fresh visual, fresh quality bundle
- Executor: `Muse Spark (worker/execution review)`, recorded `2026-09-23T00:40:00Z`
- State now `VALIDATED_DRAFT + revalidation provenance` → advanced to `RELEASE_CANDIDATE` via `stage:publication-candidate` (checkpoint `VALIDATED_DRAFT.json` recreated with r2 candidate; `DRAFT_COMPLETE.json` untouched)

## 7. Architecture approval (unchanged, active)

- Review: r1 `APPROVED` by Human Owner, reviewed commit `25dac3b189c39491f2e14d613b4a77f104086b17`
- Approval record: `5289b68e49260a2ecc7aad48ab11a1b12b3a56640905b4d822c885be658d8f68` (byte-identical)
- Review record r1: `9988d7118c8040b956a96581b1c21cde88418dbd90961db40261c262d2660395`
- Architecture bytes unmutated since approval; `human_gates.architecture_review == approved` with intact provenance

## 8. Gate readiness

- Lifecycle: `RELEASE_CANDIDATE`, next `PUBLICATION_PREVIEW`, terminal `HUMAN_GATE_REACHED`
- Publication Preview: `pending`, provenance `null` (r1 REQUEST_CHANGES recorded as `publication-r1.json`; no approval recorded)
- Freeze: `pending`. Release: `pending`. No freeze record, no release manifest. Freeze/Release prohibited until Human approves r2.
- Shared Core v2: unchanged (scripts/schemas/config/workflows untouched; verified via `git status` + deferred-maintenance isolation below)
- CV2-DM-016: OPEN. CV2-DM-017: OPEN. New #520 QA debt: OPEN as CV2-DM-018 (docs-only, isolated branch/PR, not production branch)
- Issue #521 is EDITION_LOCAL / PUBLICATION_CORRECTNESS, not a Core defect (no CV2-DM entry)

## 9. Review routing

- Sol: full r1→r2 chain with exact SHAs above (r1 rejected bytes + r1 review + r2 revalidation + r2 candidate + r2 QA + overfull guard + visual renders). Issues #520/#521 remain OPEN for Sol to close after independent r2 acceptance.
- Human: exact r2 PDF bytes at `surveys/special/efficient-llm-2026/main.pdf` (`8a9a721ac35b2e5baa2e20162b5a6ba4ae63945d512d985484aeae56073a23c1`, 66 pages) pending Publication Preview r2 decision.
