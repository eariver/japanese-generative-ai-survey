# TS-003 Sol Draft Review r2

Status: `SOL_DRAFT_REVIEW_R2 / REQUEST_CHANGES / TERMINOLOGY_AND_READER_SURFACE_REPAIR`

Date: `2026-10-02 JST`

Issue: `SP-vision-multimodal-2026`

Reviewed Draft r2 authority commit:

`4a553c33385cb245d7239c116812999560165188`

Reviewed tree:

`f1f6fdf5582d30d03a280aea00e872dcf026a30f`

Decision:

`REQUEST_CHANGES`

Draft r2 is materially better than r1: systemic exact-sentence repetition was removed, the original `網` substitution disappeared, raw English CLAIM_BOUNDARY leakage was repaired, and lifecycle/upstream authority remained intact. However, the edition-local binding Japanese terminology policy is still violated in multiple reader-facing locations, and several r1-style metaphorical substitutions remain. Publication validation must not start yet.

## 1. What passed

- Startup guards matched the authorized r2 launch state.
- Work branch advanced by one normal child commit from `55dc1543247b585409bedd0abfc85de11a35dd77`.
- main remained `d6381568cc897a47d6de992189e20339350342b7` / tree `83ce3a216d852a1c32d0138f9c56fadefa800666`.
- Frozen Core remained `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- Discovery / Screening / Evidence / Materiality / Completeness / Selection / Architecture r2 / Human Architecture approval were not changed.
- Lifecycle remains `DRAFT_COMPLETE`; Publication Preview remains pending; validation/freeze/release remain pending.
- All 16 canonical Draft Results are `draft_version=r2`, `status=REVISED`.
- Exact duplicate reader-facing sentence scan independently confirms zero duplicates in all packages.
- The r1 substitution `網` is absent from the r2 canonical reader surface.
- Internal workflow identifiers such as VM-D / G01-G06 / PARTIAL / stage labels are not leaking into ordinary prose.
- CLAIM_BOUNDARY blocks are now concise Japanese rather than raw English Architecture strings.
- P07B remains mechanism-grouped rather than reverting to a paper catalogue.
- P09 keeps attribution around paper-internal comparisons and does not become a cross-task authored leaderboard.
- P15 is substantially shorter and denser than r1; deletion of filler was appropriate and should not be reversed merely to recover character count.

These passes do not override the blocking findings below.

## 2. Blocking finding F1 — binding terminology-map violations remain

The edition-local terminology map is explicitly mandatory and says:

- `multimodal -> マルチモーダル`, avoid `多様式 / 多模式`;
- `deployment -> デプロイ` (plain `配備` may exist in Japanese, but the volume is to standardize on デプロイ);
- `post-training -> ポストトレーニング`, avoid `事後学習`;
- `hallucination -> ハルシネーション`, avoid `幻覚`;
- `segmentation -> セグメンテーション` as the load-bearing technical term;
- established technical terms should not be replaced by improvised Japanese merely to sound natural.

Independent Sol scan of the canonical r2 results found, among others:

- `多様式`: 4 occurrences (P09 x3, P11 x1);
- `事後学習`: 1 occurrence (P09);
- `幻覚`: 3 occurrences (P15);
- segmentation-specific prose replaced by `切り分け / 塗り分け` in P01/P03;
- boundary prose still uses `配備` where the edition map standardizes on `デプロイ`.

This is a direct failure of the binding edition-local terminology contract, not a stylistic preference.

Required repair: restore the terminology map forms wherever the term is technical/load-bearing. Ordinary Japanese uses of words such as `切り分ける` may remain when they literally mean “separate/distinguish”, but must not substitute for `segmentation`.

## 3. Blocking finding F2 — teacher/student terminology is still over-domesticated

The r1 review specifically called out the ViLD wording and required established teacher/student terminology. The handoff policy states that `teacher/student` should be rendered as `教師モデル / 生徒モデル` where needed.

Canonical r2 still contains:

- `教員`: 19 occurrences (P06 x4, P07B x15);
- `生徒`: 3 occurrences (P07B x3).

The r1-problematic construction remains essentially intact:

`CLIP・ALIGNの教員を二段の生徒に蒸留する。`

Other examples include `教員モデル`, `教員役`, `教員の質`, `領域の生徒`.

This is exactly the failure mode the repair was intended to remove. Use `教師モデル`, `生徒モデル`, `teacher signal / 教師信号`, or a direct description of the distillation relation as context requires. Do not personify model roles as school personnel.

## 4. Blocking finding F3 — technical terms are still replaced by nonstandard Japanese

Several reader-facing sentences use `符号` to mean source code/software code, e.g.:

- P08: `符号とモデルとデータは公開された。`
- P09: `三つの部品の積み重ねは符号の上で確かめられる`
- P09: `符号はApache 2.0で公開が確認され`
- P10/P11: `符号は公開された`, `符号とデータは公開された`

Here `符号` is not an established reader-facing rendering of repository/source code. Use `コード`, `ソースコード`, `推論コード`, `学習コード` as appropriate.

Note that genuine uses such as character encoding or positional/time encoding are not the target. The repair must be semantic, not a blind string replacement.

Other residual examples include:

- P06/P09: `受け口` as a substitute for interface/input side;
- P06: `難しい当て戻し` for masked reconstruction;
- P07A: `袋詰め` for image-text/global representation behavior.

These should be replaced by the actual technical concept or a straightforward explanation.

## 5. Blocking finding F4 — r1-style metaphorical editorial prose remains

The volume is no longer dominated by r1 rhetoric, but several sections still contain nontechnical metaphor chains that obscure rather than explain.

Representative examples:

- P07A: `袋詰めの限界`, `袋にまとめて照らす`, `受け皿`;
- P07B: `指示表現の契約の家はRefCOCO`;
- P07B closing synthesis: `語彙の足し`, `遅い渡し`, `固い混ぜ`, `規模の回し`, `レア側の埋め`;
- P10: `投票は幻のふるい`;
- P14/P15: `錨` used repeatedly as an editorial organizing metaphor;
- P15: `投票の素描`, `二言語の輪切り`, `配りの極`.

These are not required technical terms and recreate the r1 `OVER_DOMESTICATION / METAPHORICAL_TERMINOLOGY_SUBSTITUTION` failure in a smaller but still material form.

Draft r3 should use direct technical statements. A metaphor is acceptable only when it genuinely clarifies a concept and does not replace the concept itself. Editorial connective tissue should not be metaphor-driven.

## 6. Blocking finding F5 — Language QA r2 overstates closure

`execution/language-qa-ja-draft-r2.md` states:

- `F1-F5_CLOSED`;
- r1 failure lexicon total `528 -> 0`;
- no material terminology residue.

Independent Sol scan disagrees.

Even within the earlier r1-style lexicon:

- `受け口`: 2 reader-facing PARAGRAPH occurrences remain;
- `物差し`: 3 reader-facing CLAIM_BOUNDARY occurrences remain.

More importantly, the QA did not catch the binding terminology-map violations listed above (`多様式`, `教員/生徒`, `事後学習`, `幻覚`, segmentation paraphrases, code -> `符号`).

Therefore the QA process itself needs repair. Regex counts for a selected r1 lexicon are insufficient. Draft r3 QA must explicitly validate the binding terminology map and perform a manual full-volume read for semantically equivalent substitutions.

## 7. Non-blocking observations

### N1 — Volume reduction

The reduction from roughly 90.3k to 52.2k characters is not itself a defect. r1 contained extensive duplication and padding. Do not restore length by paraphrase.

Actual page count remains a later materialization concern. If a package becomes technically shallow, deepen it only with already-bound Evidence and approved Architecture coverage.

### N2 — P09 comparisons

The same-source/same-protocol comparisons may remain when:

- explicitly attributed;
- version/config/protocol bound;
- materially relevant to the technical argument;
- not reused as a general cross-task ranking.

No new Evidence research is requested.

### N3 — lifecycle limitation

The Worker correctly did not fake a rollback or advance to reader-publication validation. Keep `DRAFT_COMPLETE` until fresh Sol review passes.

## 8. Required Draft r3 repair boundary

This remains a bounded Draft-only editorial repair.

Immutable:

- Discovery;
- Screening;
- Evidence r1-r5 and active Evidence/Views;
- Materiality;
- Completeness;
- Candidate Matrix / Selection;
- Architecture r2;
- Human Architecture r2 APPROVED record;
- all Draft Packages;
- source set;
- G01-G06;
- five PARTIAL limitations;
- main;
- Frozen Core.

Do not perform new research.

Revise only reader-facing Draft Results / synthesis / terminology QA artifacts as needed.

Draft r1 and r2 remain immutable Git history.

## 9. Draft r3 acceptance criteria

Before returning to Sol:

1. `網` remains absent as a neural-network substitute.
2. `multimodal` uses `マルチモーダル`, not `多様式 / 多模式`.
3. teacher/student roles use `教師モデル / 生徒モデル` or an equally standard explicit technical form; no recurrent `教員 / 生徒` personification.
4. `post-training` uses `ポストトレーニング` where that is the technical concept.
5. `hallucination` uses `ハルシネーション` where that is the technical concept.
6. segmentation-specific uses retain `セグメンテーション`; generic editorial `切り分け` is allowed only when it means actual separation/distinction.
7. source/software code uses `コード`, not `符号`; encoding-related `符号化` may remain where technically correct.
8. `受け口`, `袋詰め`, `契約の家`, `語彙の足し`, `遅い渡し`, `固い混ぜ`, `レア側の埋め`, `投票の素描`, `二言語の輪切り`, `配りの極` and similar metaphorical substitutes are removed or rewritten directly.
9. terminology-map avoid forms are scanned across headline/deck/all reader blocks, including CLAIM_BOUNDARY.
10. manual full-text review confirms that a removed bad term was not replaced with a new improvised synonym.
11. exact-sentence duplicate count remains zero; do not re-pad.
12. Evidence refs, attribution, boundary dispositions and G01-G06/PARTIAL semantics remain intact.
13. no reader-publication validation / Publication Preview / Freeze / Release.

## 10. State boundary

Current `DRAFT_COMPLETE` remains valid.

Terminal target:

`TS-003 DRAFT_R2_SOL_REVIEW_REQUEST_CHANGES`

`TS-003 DRAFT_R3_TERMINOLOGY_READER_SURFACE_REPAIR_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW_R3`

`NO_READER_PUBLICATION_VALIDATION`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`
