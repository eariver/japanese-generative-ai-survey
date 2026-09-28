# Japanese technical terminology overtranslation seed — W39 r3 residual additions

Status: `GENERIC_QA_SUPPLEMENT / READ_ONLY_SEED / NO_AUTO_REWRITE`

Purpose: successor supplement to the generic Japanese reader-surface QA corpus after independent Sol review of the exact W39 Publication Preview r3 reader bytes.

This file is **not** a blind replacement dictionary. Every hit must be adjudicated in context as `REPLACE`, `RETAIN_WITH_CONTEXT_REASON`, or `ZERO_HIT_CHECKED`.

Use together with:

- `docs/editorial/ja-technical-terminology-overtranslation-seed.md`
- `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-additions.md`
- `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-r2-residual-additions.md`

## W39 r3 residual forms observed in exact final reader bytes

| Search / observed form | Why it needs review | Preferred technical-Japanese direction |
|---|---|---|
| `今号の物語に入れない` | Literary metaphor in a temporal-boundary statement; the publication rule is ordinary inclusion/exclusion, not a narrative identity. | `今号の通常集計には含めない` / equivalent explicit boundary wording |
| `遺伝子操作への用立て` | Archaic/indirect wording obscures the intended concept of application or applicability. | `遺伝子操作への応用可能性` or source-bounded equivalent |
| `スコア比較は本号では真としない` | `真とする` is semantically unnatural for benchmark-score comparison and can be misread as a truth-value claim. | State exactly what is not judged: score validity, cross-model superiority, or independent reproducibility, according to source context |
| `ベンチマークのスコア比較は真としない` | Same defect in claim-boundary wording. | Explicit technical scope statement, not truth-value language |
| `高速モードは2.5倍の速さで倍の値` | Colloquial/ambiguous pricing expression; `値` does not clearly identify price. | `2.5倍の速度で、料金は2倍` or source-faithful equivalent |
| `トークン代を7%ほど軽くした` | Colloquial metaphor for measured token-cost reduction. | `トークンコストを約7%削減した` when supported by the source |
| `ベンチマークの深追いは本号ではしない` | Conversational expression where a scope limitation should be explicit. | `詳細なベンチマーク分析は本号の対象外` / equivalent |
| `測られた数値の出所` | Awkward passive nominalization. | `測定値の出所` / `測定条件と出所` |
| `値札` | Metaphorical substitute for price/pricing. May be acceptable in deliberate editorial prose, but must not replace an exact pricing concept where technical precision matters. | Prefer `料金` / `価格` / `料金表`; retain only with an explicit editorial-context reason |
| `目配り` | Figurative wording used for feature-flag/release operations. | Prefer the actual operational concept (`対応`, `監視`, `実装`, `運用`) according to context |
| `手ほどき` | Old-fashioned metaphor when the source means tutorial/walkthrough. | Prefer `手順`, `チュートリアル`, `実演`, `解説` where technically appropriate |
| `素性` | Colloquial wording for model identity/provenance. | Prefer `正体`, `モデルの特定`, `由来`, `identity`-appropriate wording according to evidence |
| `脇を固めた` | Figurative synthesis wording; may obscure the relationship among supporting topics. | Prefer explicit relation (`補完した`, `周辺領域でも進展した`) if retained meaning is technical |
| `動向をうたう言い回し` | Indirect/metalinguistic expression in an evidence boundary. | Prefer `動向を主張しない` / `momentumを示す根拠には使わない` as context requires |

## Required handling

1. Search the **union of all terminology seed/supplement files**, not only the newest additions.
2. Search all exact final reader-facing sources that feed the PDF.
3. Do not auto-replace.
4. For every hit, inspect the sentence and accepted evidence/source before deciding.
5. If the phrase is deliberately editorial and does not obscure technical identity or evidence scope, `RETAIN_WITH_CONTEXT_REASON` is allowed.
6. After all corpus hits are adjudicated, perform a fresh seed-external read of the **exact final TeX bytes**, not an intermediate draft.
7. A final QA report must not claim a metaphor/awkward form was removed if it is still present in the final reader bytes.
