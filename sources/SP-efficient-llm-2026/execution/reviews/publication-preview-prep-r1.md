# Publication Preview prep r1 — SP-efficient-llm-2026

Status: `RELEASE_CANDIDATE / HUMAN PUBLICATION PREVIEW PENDING`
Date: `2026-09-22`
Author role: Muse (Luna/Work execution role). Operator package for Sol review and
Human Preview. NOT Human-approved. No Freeze/Release performed.

Working title: **Efficient Intelligence — LLMを速く、軽く、安くする技術史**

## 1. Exact ending authority (uncommitted working tree at prep time)

- Branch: `special/efficient-llm-2026-work`
- HEAD at prep: `b0f1f539e020db5695858595723d9745905a544d`
- Remote HEAD verified equal before prep (final push below re-verifies).
- Reviewed main guard: `175b327f6126e2f0759861067852105ee5a290aa` (untouched throughout).

## 2. Publication Candidate

- Path: `sources/SP-efficient-llm-2026/publication/v2/publication-candidate-v2.json`
- SHA-256: `76191e9b5f24d6950ce3e80a4f3e19cf79dc4dfc2dee5529488bce23956f787e`
- Status: `READY_FOR_PUBLICATION_PREVIEW`
- Candidate SHA (inner): `0499da130ceb286f`

## 3. Reader source and PDF (exact Candidate-bound bytes)

- `surveys/special/efficient-llm-2026/main.tex`
  SHA-256: `b09ab3516afaadb5e0f64e21515d2e71dd43cbb926c657e40d48b939dc54b44c` (293,423 bytes)
- `surveys/special/efficient-llm-2026/main.pdf`
  SHA-256: `bc6e280c668a4a17ff98dae58fc574cdce701cce9dd8926eb8b1138e82a46e0b`
  Bytes: `850455`
  Pages: `66`
  Build: CI `Build Special survey PDF` run `35773857901` on HEAD `b0f1f539e`,
  zero blocking findings, artifact digest matches committed bytes.
- `surveys/special/efficient-llm-2026/references.bib`
  SHA-256: `9c0edead748c24beea8fd9a2e97982d7e6dd7b0086ab0b30906286e09f8478d2` (110 entries, all cited keys resolve)

## 4. QA authority SHAs

- Reader manuscript: `f99c3b9353e978aec009871875a0df77d30b7be387b2c90ede15ac44aacbd693`
- Quality regression bundle (4 DETERMINISTIC PASS): `08c0e35848b93e8e27ae6937ea255278dbe7600eec96dc32af6f295eed1f0f18d`
- Semantic editorial review (9 checks PASS): `c60513eb08a27d8339909dea75d48ea1ddcd6dfe439106a26c8d29465d10c10f`
- Visual review (5 checks PASS, exact PDF): `c4ae1c38c09477dfd003336cf820f9e23267c864861b8292f669a65257d6a222`
- Reader-surface gate: `417e49ac28b9e1c8babeac181fb541618a8f23935e61533ac79e5d21bce678a5`
- Surface semantic review: bound to `main.tex` exact bytes.

## 5. Architecture approval (unchanged, active)

- Review: r1 `APPROVED` by Human Owner, reviewed commit `25dac3b189c39491f2e14d613b4a77f104086b17`
- Approval record: `5289b68e49260a2ecc7aad48ab11a1b12b3a56640905b4d822c885be658d8f68`
- Review record r1: `9988d7118c8040b956a96581b1c21cde88418dbd90961db40261c262d2660395`
- Review index: `b51e7e4371687bde172f0df4606e2b62c53d51f669ef59a16ef9f9ddc5f884d0`
- Architecture bytes unmutated since approval.

## 6. Article map (section / page ranges from exact PDF TOC)

- §1 「効率」とは何を減らすことなのか: pp.6–9
- §2 ScalingからConditional Computeへ: pp.10–13
- §3 AttentionとMemoryを減らす: pp.14–18
- §4 Bitを減らし、巨大モデルを手元で動かす: pp.19–24
- §5 1 tokenずつ待たない: pp.25–28
- §6 Servingで消える無駄: pp.29–33
- §7 「大きなモデルを毎回呼ぶ」必要はあるか: pp.34–38
- §8 2026年の実装点: pp.39–45
- §9 数字をどう読むか: pp.46–49
- §10 結び──層として読む効率: pp.50–52
- Appendix (technical notes, boundary index, glossary): pp.53–59
- References (110 entries): pp.60–66
- Citations: 110 keys, all resolve; no undefined references (CI verified).
- Architecture packages: all 9 present in drafting order plus closing synthesis.
- Page target: 66 pages vs target 76 / max 96 / soft min ~64. Within soft band;
  below-target density consciously reviewed in LONGFORM_TECHNICAL_DEPTH
  (page-plan:66/76, density-review:below-target-substantive). No padding.

## 7. Known residual limitations (retained, not hidden)

- Jev independent reproduction thin; public calibration protocol unresolved.
- GLM D128 abstract-scope; vendor ratios vendor-measured and quarantined.
- Kimi independent reproduction limited; AIPerf standalone product unresolved.
- D157 routing fragility summary-scope; SWE-bench-Pro section-level outstanding.
- Some capstone per-figure pins unresolved; some repo/doc/spec bodies captured but unconsumed.
- Wrong canonical Discovery locator history repaired through Supplement, not rewritten.
- X observations configuration-bound (supporting role only).
- 21 minor layout log notes (9–10pt overfulls in appendix tables, visually clean);
  glossary reflowed into breakable fixed-column tables.

## 8. Gate readiness

- Lifecycle: `RELEASE_CANDIDATE`, next `PUBLICATION_PREVIEW`, terminal `HUMAN_GATE_REACHED`.
- Publication Preview: `pending`, provenance `null` (no approval recorded).
- Freeze: `pending`. Release: `pending`. No freeze record, no release manifest.
- Shared Core v2: unchanged (scripts/schemas/config/workflows/docs untouched).
- CV2-DM-016: OPEN (edition-local workaround, unchanged).
- CV2-DM-017: OPEN (unchanged).
- No new generic Core defect encountered during drafting/validation
  (edition-local layout repairs only; no new CV2-DM-xxx).

## 9. Review routing

- Sol: full Architecture→Draft→Validation→Candidate chain with exact SHAs above.
- Human: exact PDF bytes at `surveys/special/efficient-llm-2026/main.pdf`
  (`bc6e280c668a4a17ff98dae58fc574cdce701cce9dd8926eb8b1138e82a46e0b`, 66 pages).
