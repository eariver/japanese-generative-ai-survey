# Japanese Technical Terminology Overtranslation Seed Corpus — W39 r2 Residual Additions

Status: `GENERIC QA SEED SUPPLEMENT / READ-ONLY AUTHORITY / NO AUTO-REWRITE`
Date: `2026-09-28`
Scope: Weekly + Special (generic, reusable)
Parent authorities:
- `docs/editorial/ja-technical-terminology-overtranslation-seed.md`
- `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-additions.md`
Tracking: Issue #501 / Issue #534 / `CV2-DM-006`
W39 source edition: `2026-W39`
Residual review basis: Publication Preview r2 reader surface at reviewed commit `d95a811abd014ad4476d8f305b792920aa6e87fe`
Reviewer: Sol independent read-back

## 0. Purpose

This supplement records residual reader-facing wording that remained after the first W39 full-corpus repair. It is part of the generic search authority for future Weekly/Special review.

Future terminology review MUST use the union of all three files:

1. `ja-technical-terminology-overtranslation-seed.md`
2. `ja-technical-terminology-overtranslation-seed-w39-additions.md`
3. `ja-technical-terminology-overtranslation-seed-w39-r2-residual-additions.md`

As with the parent corpus, this is not an automatic substitution dictionary. Every hit requires source/entity/context adjudication.

## 1. High-confidence residuals requiring review/replacement

| observed exact search form(s) | canonical concept | preferred direction | classification | context / rationale |
|---|---|---|---|---|
| `卓上版` | desktop app / desktop surface | source-readback, then `デスクトップアプリ` / `デスクトップ版` / exact product surface | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | product delivery surface is obscured by literal `desktop -> 卓上` wording |
| `腕前のベンチマーク結果` / technical-performance senseの`腕前` | model capability / benchmark performance | `性能ベンチマーク` / `ベンチマーク結果` / source-specific capability wording | `REVIEW_REQUIRED` | ability metaphor is not precise technical evaluation wording |
| `貯めて使える制限の戻し` | usage-limit / quota rollover | source-readback required; use exact `利用上限の繰り越し` / `quota rollover` semantics supported by source | `PROHIBITED_HIGH_CONFIDENCE` | reader must reverse-engineer the source feature |
| `発表側の手つき` | vendor-reported evaluation conditions / methodology | `発表側の評価条件` / `ベンダー側の評価方法` | `PROHIBITED_HIGH_CONFIDENCE` | literary hand-motion metaphor in benchmark methodology |
| `近来で最良` | vendor claim of best/recent-best behavior | source-readback and preserve exact comparison population/time scope | `REVIEW_REQUIRED` | vague chronology and population |
| `悪い使い道` | misuse / abuse | `悪用` / `misuse` source-specifically | `REVIEW_REQUIRED` | colloquial phrase weakens safety concept identity |
| `Claude Codeの動作も動いた` | Claude Code behavior/update changed | rewrite sentence naturally, e.g. `Claude Codeにも動作変更があった` if source supports | `PROHIBITED_HIGH_CONFIDENCE` | tautological publication prose |
| `公式の場` / `公式の場の示し` | official announcement / official channel / primary source | `公式発表` / exact official channel | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | vague “place” wording hides source authority |
| `大勢の利用での試し（A/B）` | large-scale A/B test / production A/B test | `大規模A/Bテスト` / exact source scope | `PROHIBITED_HIGH_CONFIDENCE` | non-standard experiment wording |
| `使る` | `使う` | `使う` | `PROHIBITED_HIGH_CONFIDENCE`, `TYPO` | clear orthographic error in r2 reader surface |
| `読みの行番号` | read-tool / file-read line-number tokens or line-number output | source-readback; preserve tool identity and say `readツールの行番号` / equivalent | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | generic “reading” hides tool behavior |
| software/cloud contextの`出荷済み` | shipped / released / available feature | `リリース済み` / `提供済み` / source-specific availability state | `REVIEW_REQUIRED` | physical shipping metaphor may misstate software availability |
| `学びの長さ` | training duration / RL horizon / training length | source-readback then `学習期間` / `強化学習の長さ` / exact concept | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | generic “learning” wording loses training concept |
| `扱える投稿` | usable/relevant/eligible source-intake post | `採用可能な投稿` / `該当する投稿` / exact evidence criterion | `REVIEW_REQUIRED` | vague editorial criterion in reader-facing prose |
| `三つのモデルで寄せた` | speed comparison / near-parity measurement | source-readback; state exactly what the comparison showed | `PROHIBITED_HIGH_CONFIDENCE` | verb does not identify measured relation |
| benchmark/evaluation contextの`測り` | measurement / benchmark / evaluation | `測定` / `計測` / `ベンチマーク` | `PROHIBITED_HIGH_CONFIDENCE` in technical evaluation context | recurring metaphor remained after `物差し` repair |
| `速さの薦め` | performance recommendation | `速度重視なら…を推奨` / exact source recommendation | `REVIEW_REQUIRED` | noun phrase is non-standard and ambiguous |
| correctness/evaluation contextの`量らない` | not independently verify / not assess | `検証しない` / `評価しない` source-specifically | `REVIEW_REQUIRED` | measurement verb obscures epistemic boundary |
| `スコアの比べ` | score comparison | `スコア比較` | `REVIEW_REQUIRED` | non-standard benchmark wording |
| `プレプリントの記録だけで立つ` | evidence limited to preprint / abstract | `根拠はプレプリント（要旨）に限られる` / exact consumption depth | `PROHIBITED_HIGH_CONFIDENCE` | literary metaphor obscures evidence depth |
| `四組織による作` | collaboration by four organizations | `4組織による共同開発` / source-supported relationship | `PROHIBITED_HIGH_CONFIDENCE` | generic `作` obscures collaboration identity |
| source-claim contextの`書きぶり` | wording of announcement / source statement | `発表では…とされる` / `発表内容は…` | `REVIEW_REQUIRED` | r2 dossier says this residual was repaired, but final r2 TeX still contains it |
| community/evidence contextの`場の声` | public reaction / community posts | `公開投稿での反応` / `コミュニティの反応` | `REVIEW_REQUIRED` | source surface is obscured |
| validation contextの`他所の確かめ` | independent verification | `独立検証` | `PROHIBITED_HIGH_CONFIDENCE` | colloquial phrase for a formal evidence boundary |
| `請求の実相` | actual billing / observed charge | `実際の請求額` / `請求実績` | `REVIEW_REQUIRED` | literary wording for billing evidence |
| benchmark-setting contextの`力の入れ方` | reasoning effort / effort setting / harness setting | preserve exact setting (`reasoning effort`, `xhigh`, `max`, etc.) | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | r2 dossier explicitly retained this as an ordinary word, but in benchmark context it encodes a technical evaluation setting |

## 2. Additional context-sensitive residuals

These are not blanket-prohibited. Search all occurrences and retain only where ordinary Japanese remains semantically exact.

| observed | review direction |
|---|---|
| `先代` in model comparisons | prefer explicit predecessor/model identity where ambiguity remains |
| `長い仕事` in agent benchmark context | review whether source means long-running task / long-horizon task; use exact term where material |
| `作り手` in vendor-evaluation context | prefer `開発元` / `ベンダー` when attribution identity matters |
| `書き手` in technical recommendation context | prefer `著者` / `Hugging Face` where source identity matters |
| `各所に出る` / `クラウド各社に出る` | prefer `提供される` / `利用可能になる` for availability claims |
| `使える日の目処` | prefer `提供時期` / `利用開始時期` |
| `次の一手` in evaluation/survey semantics | preserve only if it truly means an ordinary next action; otherwise source-bound `next step` wording |
| `調子` in response-quality context | preserve only if ordinary tone is truly intended; otherwise `応答のトーン` / source concept |

## 3. r2 audit inconsistency to prevent

The r2 worker dossier states that seed-external residual scan repaired `書きぶり`, but the reviewed r2 reader surface still contains:

`ただし書きぶりは「これからできる」の構想であり...`

Therefore future completion claims MUST be checked against post-edit final TeX bytes, not only the occurrence ledger or an intermediate scan result.

For every claimed repaired residual:

- search the final canonical reader source after all regeneration;
- record zero remaining defective-context hits;
- if the same form remains in a contextually valid sense, record that exact occurrence and reason;
- do not write broad statements such as “all defective forms removed” when any listed form remains without per-context reconciliation.

## 4. Acceptance criterion for W39 follow-up

A W39 follow-up terminology pass is complete only when:

1. the union of all three terminology files is searched;
2. every hit is `REPLACE` or `RETAIN_WITH_CONTEXT_REASON`;
3. every form with no hit is recorded as checked;
4. the residual forms in §1 are absent from defective reader contexts;
5. the typo `使る` is zero;
6. a fresh seed-external read of the final TeX finds no additional identity-destroying or machine-literal wording;
7. the completion report is cross-checked against the exact final TeX/PDF bytes.
