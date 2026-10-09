# Sol Decision Record — TS-003 Reader R02/R04/R05 Bounded Repair

- Decision authority: Sol editorial coordinator
- Decision: `READER_PUBLICATION_REVISION_REQUIRED`
- Blocking scope: R02 / R04 / R05 (R01, R03 PASS)
- Repair scope: reader-only, 9 occurrences, 7 lines
- Technical authority: preserved (Architecture r9, Evidence 124, Draft `fresh-124-r9`)
- Core v2: frozen, no changes permitted
- Canonical publication replacement: not authorized
- Publication Candidate: HOLD

This is an edition-local Sol editorial execution record. **It is not a Human
Gate Approval.** The existing Human Architecture r9 approval record
(`sources/SP-vision-multimodal-2026/gates/architecture-approval.json`,
`APPROVED` 2026-10-09 JST) is preserved unchanged.

## Blocking findings and authorized corrections

### R05 — P01: `残差 reformulation` ×2

- L59 deck: `残差 reformulation が超深度の最適化を切り開いた`
  → `残差としての再定式化が超深度の最適化を切り開いた`
- L64 body: `学ぶ残差 reformulation へ切り替えた`
  → `学ぶ残差としての再定式化へ切り替えた`
- Meaning preserved: ResNet residual mapping (H(x)/F(x) = H(x)−x) and the
  optimization-framed diagnosis are unchanged; only the loanword mix is
  naturalized (the pre-`が`/pre-`へ` inter-word space is dropped as required
  by Japanese orthography).

### R02 — P04: `exhibits` ×3 (context-natural Japanese)

- Zero-shot depth-transfer evaluation case (L127):
  `頑健さ測定の exhibits として示されている`
  → `頑健さ測定の評価事例として示されている`
- OpenPose technical comparison case (L128):
  `対応づけ自体の表現化を示す exhibits である`
  → `対応づけ自体の表現化を示す技術的な比較例である`
- DUSt3R downstream-relevance editorial comparison case (L131):
  `後の融合や身体系への受け渡し exhibits になる`
  → `後の融合や身体系への受け渡しを考える編集上の比較例になる`

### R02 — P04: `cap` ×3 (natural scope-limiting wording)

- L127 + L132 (identical sentence ×2):
  `後継の追加は新しい契約を生まないものとして cap の外に置く。`
  → `後継の追加は新しい契約を生まないものとして本節の対象外に置く。`
- L128: `三次元持ち上げは cap により扱わず`
  → `三次元持ち上げは本節の対象外として扱わず`
- The wording matches the pre-existing canonical scope-limiting idiom
  (`本節の対象外とする`, P11). DUSt3R downstream linkage remains
  Survey/editorial synthesis: the explicit disclaimer sentence in L132
  (`資料が直接の因果継承を支えるものではなく、本サーベイの編集上の比較判断`)
  is preserved byte-identically.

### R04 — P07B: `IDは受入時に修正済みである。` ×1 (deletion)

- L215: trailing internal-process sentence deleted; the preceding `。` and
  `\autocite{vmd046}` are retained. Detic mechanism, evaluation values
  (LVIS 2.4/8.3/41.7 mAP, 21K generalization), source attribution, and the
  stated limitation are unchanged.

## Non-goals enforced

- Shared Core v2 untouched (`scripts/`, `schemas/`, `config/`, workflows,
  Core docs). No patch, schema extension, or revalidation-reason reuse.
- `REVIEWED_CORE_CHANGE` reason transfer: prohibited, not used.
- `RELEASE_CANDIDATE` progression as a bypass for the Human Gate: prohibited,
  not started.
- Canonical publication surface untouched: `surveys/special/vision-multimodal-2026/`
  bytes are read-only inputs; repaired outputs live only in
  `sources/SP-vision-multimodal-2026/execution/reader-r02-r04-r05-repair-20261009/`.

## Deferred Core dependency (implementation out of scope)

Promoting this staged repair into formal publication authority requires a
future Core v2 blanket repair that gives reader editorial revalidation a
formal contract (post-validation revalidation reason for editorial
corrections). The mechanism is not designed here; this dependency is recorded
only.

## Terminal boundary

`R02_R04_R05_STAGED_REPAIR_COMPLETE` / `CANONICAL_AUTHORITY_PRESERVED` /
`CORE_V2_UNCHANGED` / `PUBLICATION_CANDIDATE_HOLD`. STOP.
