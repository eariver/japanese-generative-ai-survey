# Japanese Technical Terminology Overtranslation Seed Corpus — W39 Additions

Status: `GENERIC QA SEED SUPPLEMENT / READ-ONLY AUTHORITY / NO AUTO-REWRITE`
Date: `2026-09-28`
Scope: Weekly + Special (generic, reusable)
Parent authority: `docs/editorial/ja-technical-terminology-overtranslation-seed.md`
Tracking: Issue #501 / Issue #534 / `CV2-DM-006`
W39 source edition: `2026-W39`
W39 reviewed publication authority: `bb6eacabc86e21da77a91d46d4daa2419be5c988`

## 0. Purpose and invariant

This supplement records reader-facing overtranslation patterns independently identified by Sol during the 2026-W39 Publication Preview review.

It extends, but does not replace, `ja-technical-terminology-overtranslation-seed.md`.

The combined authority for future review is therefore:

1. `docs/editorial/ja-technical-terminology-overtranslation-seed.md`
2. `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-additions.md`

The parent invariant remains unchanged:

> The defect is forced, non-standard, metaphorical, or identity-destroying translation that makes a technically literate Japanese reader reconstruct the English/source technical term.

This is **not** an automatic replacement dictionary. Every occurrence must be adjudicated in source/entity/context. `auto-rewrite allowed` is always `false`.

For every future Weekly/Special reader-surface pass, the reviewer MUST search the complete combined corpus, including terms that do not appear in the current edition, and record either `REPLACE` or `RETAIN_WITH_CONTEXT_REASON` for every hit.

## 1. W39 reader surfaces inspected

The following exact r1 reader-facing surfaces were independently read:

- `surveys/weekly/2026-W39/main.tex`
- `surveys/weekly/2026-W39/sections/00-frontmatter.tex`
- `surveys/weekly/2026-W39/sections/10-cost-frontier.tex`
- `surveys/weekly/2026-W39/sections/20-frontier-challenger.tex`
- `surveys/weekly/2026-W39/sections/30-agent-operations.tex`
- `surveys/weekly/2026-W39/sections/40-coding-models.tex`
- `surveys/weekly/2026-W39/sections/50-local-inference.tex`
- `surveys/weekly/2026-W39/sections/60-science-eval.tex`
- `surveys/weekly/2026-W39/sections/70-memory-privacy.tex`
- `surveys/weekly/2026-W39/sections/80-week-in-review.tex`
- `surveys/weekly/2026-W39/sections/99-source-notes.tex`

## 2. Existing parent-seed families re-observed in W39

These are already generic defects in the parent seed and are explicitly re-observed in W39. Their parent-seed preferred wording remains authoritative unless source context requires a more precise term.

| observed exact search form | canonical concept | preferred direction | classification | W39 notes |
|---|---|---|---|---|
| `模型票` | model card | `モデルカード` / `Model Card` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | Grok 4.7 and source-notes |
| `模型` where ML model is meant | model | `モデル` | `PROHIBITED_HIGH_CONFIDENCE` in ML context | parent seed already covers family |
| `基準測定`-family generic benchmark wording; W39 adds `物差し` family below | benchmark/evaluation | preserve `ベンチマーク` / named metric | `REVIEW_REQUIRED` | W39 broadens the problem into metaphorical wording |

## 3. W39 new seed families

### 3.1 code / model / agent identity

| observed exact search form(s) | canonical concept | preferred direction | classification | rationale |
|---|---|---|---|---|
| `符号の新顔` | coding models / coding-model release | `Coding Models` / `コーディングモデル` / `コーディングモデルの新顔` only if stylistically needed | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | `符号` is not the reader-facing term for software code/coding here |
| `符号と知識仕事` | coding and knowledge work | `コーディングと知識労働` / source wording | `PROHIBITED_HIGH_CONFIDENCE` | code identity is lost |
| `符号のFrontierCode` | coding benchmark `FrontierCode` | preserve `FrontierCode` and say `コーディング` where explanation is needed | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | named benchmark must remain identifiable |
| `符号の不通` | Codex outage | `Codexの障害` / `Codexの停止・障害` after source check | `PROHIBITED_HIGH_CONFIDENCE`, `SEMANTIC_COLLISION_RISK` | turns a service outage into “code disconnection” |
| `器` / `二つの器` / `三つの器` / `密・混合の器` / `器の広がり` where ML model/architecture is meant | model / model architecture / supported model family | `モデル`, `アーキテクチャ`, `対応モデル` source-specifically | `PROHIBITED_HIGH_CONFIDENCE` in ML identity contexts | generic vessel metaphor destroys model identity |
| `品` / `影の品` where model/product is meant | model/product/release | preserve product/model name; use `モデル` / `製品` source-specifically | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | generic “item” wording obscures technical entity |
| `土台` / `土台の大きさ` where base model is meant | base model / base-model size | `ベースモデル` / source-supported size wording | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | generic base metaphor obscures the formal concept |
| `家` / `Claude 5.5の家` where model family is meant | model family | `モデルファミリー` / `Claude 5.5ファミリー` | `REVIEW_REQUIRED` | family identity should be explicit |
| `使い手` where AI agent is meant | agent / coding agent | `エージェント` / named agent | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | collides with human user/operator meaning |
| `Claudeの使い手およそ950` | Claude agents / agent instances (source-bound) | source-readback required; preserve `agent` identity | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | likely converts agent count into human-user wording |
| `下働き` where subagent is meant | subagent | `サブエージェント` | `PROHIBITED_HIGH_CONFIDENCE` | servant metaphor destroys component identity |

### 3.2 prompt caching / inference / runtime

| observed exact search form(s) | canonical concept | preferred direction | classification | rationale |
|---|---|---|---|---|
| `待ち受け` / `待ち受け改良` / `待ち受けの改良` | prompt cache / prompt caching | `プロンプトキャッシュ` / `プロンプトキャッシュの改善` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | reads as standby/waiting rather than caching |
| `待ち受けの区切り` | cache breakpoint / cache boundary | source-specific `キャッシュ境界` / `キャッシュの区切り` | `PROHIBITED_HIGH_CONFIDENCE` | cache identity disappears |
| `読みの再利用` | cached-input/cache-read pricing or reuse | source-specific `キャッシュ読み取り` / `キャッシュ済み入力` | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | vague “reuse of reading” wording |
| `使い回す文頭の一致` | reusable/matching prompt prefix | `再利用可能なプロンプトprefix` / `共通prefix` source-specifically | `REVIEW_REQUIRED` | prompt-prefix mechanism becomes opaque |
| `盤面` where dashboard is meant | dashboard | `ダッシュボード` | `PROHIBITED_HIGH_CONFIDENCE` | game-board metaphor |
| `外したわけを説く道具` | cache-miss diagnostics/explanation | `キャッシュミス診断` / source wording | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | diagnostic mechanism is unrecoverable |
| `区切りの置き所` | cache breakpoint/control point | `キャッシュ境界` / source-supported control | `REVIEW_REQUIRED` | vague prose hides mechanism |
| `考えの深さ` where reasoning effort is meant | reasoning effort | `reasoning effort` / `推論effort` / source UI term | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | named configuration dimension should stay identifiable |
| `強い設定` / `普段の設定` / `特盛` / `大盛` / `最大` where benchmark effort level is meant | effort level / reasoning effort setting | preserve source effort labels (`high`, `max`, etc.) with Japanese gloss if needed | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | culinary/ordinary adjectives destroy evaluation condition identity |
| `速い走り` | fast mode | `Fast mode` / `高速モード` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | product/runtime mode becomes metaphor |
| `給仕` / `OpenAI互換の給仕` | serving / inference server | `serving` / `推論サーバー` / `OpenAI互換API serving` | `PROHIBITED_HIGH_CONFIDENCE`, `SEMANTIC_COLLISION_RISK` | waiter/service metaphor for model serving |
| `核（ggml）` / `核の持ち込み` where kernel is meant | compute kernel / kernel porting | `kernel（カーネル）` / `カーネル移植` | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | generic “core” loses runtime component identity |
| `kernelsの包み` | kernel wrapper/package | source-specific `kernel wrapper` / `kernelsパッケージ` | `REVIEW_REQUIRED` | opaque container metaphor |
| `作る輪（generate）` | generation loop | `generation loop` / `生成ループ` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | loop identity literalized |
| `仮面の除去` | mask removal / attention-mask removal (source-bound) | retain source-specific `mask` term (`マスク除去` etc.) | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | ordinary mask metaphor loses code mechanism |
| `止め目の後倒し` | stop/EOS-check deferral (source-bound) | source-readback required; preserve `stop`/`EOS` identity | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | mechanism cannot be reconstructed reliably |
| `詰めた道` / `詰めた束ね` | optimized path / optimized batching | `最適化パス` / `最適化されたバッチ処理` source-specifically | `PROHIBITED_HIGH_CONFIDENCE` | compression metaphor obscures implementation detail |
| `他様式` | other modalities | `他モダリティ` / `画像・音声などのモダリティ` | `REVIEW_REQUIRED` | established multimodal terminology should be used |
| `像・音` where vision/audio modalities are meant | vision/image and audio modalities | `画像・音声` / `vision/audio` | `REVIEW_REQUIRED` | compressed literary wording |

### 3.3 agent operations / software delivery

| observed exact search form(s) | canonical concept | preferred direction | classification | rationale |
|---|---|---|---|---|
| `働かせ方の運び` / `Claude Codeの運び` / `運ばれる仕事` | agent operations / runtime behavior / workflow | `エージェント運用`, `Claude Codeの動作`, `ワークフロー` source-specifically | `REVIEW_REQUIRED` | generic “transport” metaphor for operations |
| `使い倒し` / `使い倒しの道具立て` | agent tooling / persistent-agent operation | `エージェント運用のツール群` / source-specific tooling | `REVIEW_REQUIRED` | colloquial wording replaces a technical operational concept |
| `ハーネスの締め` | harness efficiency/optimization | `ハーネス最適化` / `エージェントハーネスの効率化` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | tightening metaphor hides optimization meaning |
| `仕立て` / `他の仕立て` / `内の仕立て` / `仕立て依存` where harness/configuration is meant | harness / configuration / setup | `ハーネス`, `構成`, `設定` source-specifically | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | one metaphor collapses distinct technical concepts |
| `仕組みの指示文` | system prompt | `システムプロンプト` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | formal prompt role becomes generic prose |
| `道具の説明` where tool descriptions/schema are meant | tool descriptions / tool schemas | `ツール説明` / `ツールスキーマ` source-specifically | `REVIEW_REQUIRED` | technical tool metadata should remain explicit |
| `冷えた外し` | cold cache miss | `cold cache miss` / `コールドキャッシュミス` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | coined phrase is not recognizable technical Japanese |
| `使い分けの促し` | delegation/subagent prompt (source-bound) | source-readback required; preserve `prompt` / delegation identity | `REVIEW_REQUIRED` | “encouragement” wording obscures prompt behavior |
| `試しの速い代理としての評価` | proxy evaluation | `proxy evaluation（代理評価）` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | benchmark/eval concept becomes opaque |
| `利用の実分布` | production/real usage distribution | `実運用の利用分布` / `production usage distribution` | `REVIEW_REQUIRED` | compressed statistical phrase |
| `Cursorの庭` | Cursor production environment / Cursor-specific deployment | `Cursorの実運用環境` / source-specific scope | `PROHIBITED_HIGH_CONFIDENCE` | garden metaphor obscures scope boundary |
| `出荷の番人` / `二つの番人` / `番人たち` | Rollouts / Security Reviewer / post-PR agents | preserve product names; `デプロイ監視` / `セキュリティレビュー` as explanation | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | named products dissolved into “guards” |
| `出荷の仕上げ` / `出荷の見守り` | ship ops / deployment monitoring | `デプロイ工程` / `リリース運用` / `デプロイ監視` | `REVIEW_REQUIRED` | manufacturing metaphor for software delivery |
| `引き継ぎ（PR）` | pull request | `Pull Request（PR）` | `PROHIBITED_HIGH_CONFIDENCE`, `SEMANTIC_COLLISION_RISK` | `引き継ぎ` is not PR |
| `崩れ` where regression is meant | regression | `回帰不具合` / `regression` / `デグレード` source-specifically | `REVIEW_REQUIRED` | vague ordinary noun |
| `戻し案` / `巻き戻し` where rollback is meant | rollback suggestion / rollback | `ロールバック案` / `ロールバック` | `REVIEW_REQUIRED` | preserve deployment identity |
| `自ら統合` where merge is meant | merge | `マージ` | `REVIEW_REQUIRED` | source-control operation should remain canonical |
| `傷の道筋` | exploit/vulnerability path | `攻撃経路` / `脆弱性の悪用経路` source-specifically | `PROHIBITED_HIGH_CONFIDENCE` | injury metaphor hides security meaning |
| `直し案` where remediation/fix is meant | fix/remediation suggestion | `修正案` / `remediation` source-specifically | `REVIEW_REQUIRED` | colloquial compression |
| `旗の上げ下げ` / `旗上げ` | feature flags | `feature flag（機能フラグ）` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | flag-control identity is lost |
| `列車の運び` | release train | `release train` / `リリーストレイン` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | proper delivery term literalized |
| `春先の公開の番人の型` | open-source security-agent templates | `公開されたセキュリティエージェントのテンプレート` | `PROHIBITED_HIGH_CONFIDENCE` | nearly unrecoverable from Japanese surface |
| `各段` / `上位の段` / `TeamsとEnterpriseの段` | plans / tiers | `プラン` / `上位プラン` / `Teams/Enterpriseプラン` | `REVIEW_REQUIRED` | stair-step metaphor for product tiers |
| `試しの分が10日` | trial period | `10日間のトライアル` | `REVIEW_REQUIRED` | reader-facing product condition should be explicit |
| `運び屋` where provider/partner/channel is meant | provider / partner / platform | `プロバイダー`, `パートナー`, `提供チャネル` source-specifically | `PROHIBITED_HIGH_CONFIDENCE` | carrier metaphor destroys channel identity |

### 3.4 benchmark / evaluation / evidence language

| observed exact search form(s) | canonical concept | preferred direction | classification | rationale |
|---|---|---|---|---|
| `物差し` / `腕前の物差し` / `確かめの物差し` / `使い手の記憶の物差し` / `心の寄り添いの物差し` | benchmark / evaluation / metric | preserve benchmark/dataset name; use `ベンチマーク`, `評価`, `指標` source-specifically | `PROHIBITED_HIGH_CONFIDENCE` when replacing named benchmark identity, otherwise `REVIEW_REQUIRED` | broad metaphor repeatedly replaces technical evaluation vocabulary |
| `物差しの読み` / `物差しの優劣` / `物差しの点比べ` / `点の比べ` | benchmark interpretation / score comparison | `ベンチマーク結果`, `スコア比較`, `評価結果` | `REVIEW_REQUIRED` | hides what is actually being compared |
| `端末仕事` | terminal tasks / Terminal-Bench tasks | preserve `Terminal-Bench`; explanation `端末操作タスク` if needed | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | benchmark identity becomes generic work |
| `一仕事` / `一仕事あたり` where task/cost-per-task is meant | task / cost per task | `タスク` / `タスク当たりコスト` | `REVIEW_REQUIRED` | technical unit should be explicit |
| `力比べ` | benchmark comparison / capability comparison | `ベンチマーク比較` / `性能比較` source-specifically | `REVIEW_REQUIRED` | colloquial contest metaphor |
| `外の目` | external evaluator / third-party evaluation | `外部評価機関` / `第三者評価` | `REVIEW_REQUIRED` | actor identity becomes vague |
| `頂` / `Astraの頂` where max/best benchmark setting or score is meant | max setting / top score (source-bound) | source-readback required; preserve exact setting/score semantics | `REVIEW_REQUIRED` | “summit” metaphor hides evaluation condition |
| `寄せの速さ` | performance proximity / benchmark parity | `性能差`, `速度比較`, `近似性能` source-specifically | `REVIEW_REQUIRED` | vague metaphor |
| `証し` where evidence is meant | evidence | `根拠` / `証拠` / `エビデンス` according to register | `REVIEW_REQUIRED` | literary phrasing can obscure evidence status |
| `採点の手` | grader / evaluator model | `grader（採点モデル）` / `評価モデル` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | benchmark methodology identity lost |
| `自家の品で自家の物差しを採点する巡り` | grader circularity / model-as-judge circularity | `同一系列モデルをgraderに使う循環性` / source-supported wording | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | a key methodological limitation becomes a riddle |
| `目盛りの規準` | scoring rubric / rating rubric | `評価rubric（採点基準）` / `評価基準` | `REVIEW_REQUIRED` | metric construction should remain explicit |
| `景気` / `窓内の景気` where community momentum is meant | community momentum / observed activity | `コミュニティ上の反応`, `投稿動向`, `momentum` only if properly bounded | `PROHIBITED_HIGH_CONFIDENCE`, `SEMANTIC_COLLISION_RISK` | economic “business climate” sense collides with social momentum |
| `引き上げ` where evidence elevation/promotion is meant | elevate/promote evidence status | reader-facing prose should state the actual boundary (`技術的根拠には使わない` etc.), not internal “elevation” metaphor | `REVIEW_REQUIRED` | internal editorial concept leaks into reader prose |

### 3.5 safety / safeguards / product behavior

| observed exact search form(s) | canonical concept | preferred direction | classification | rationale |
|---|---|---|---|---|
| `守り` / `守りの仕組み` / `守りの構え` / `守りが働いた箇所` | safeguards / safety mechanisms / safeguard-triggered cases | `安全対策`, `safeguard`, `安全機構` source-specifically | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | generic defense metaphor collapses distinct mechanisms |
| `振る舞いの自動点検` | automated behavioral evaluation/audit | `自動的な挙動評価` / source-specific audit name | `REVIEW_REQUIRED` | “inspection” wording hides evaluation type |
| `囲いを越えようとする振る舞い` | source-specific sandbox escape / boundary-violation behavior | source-readback required; preserve the formal safety behavior term | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | exact safety category cannot be inferred reliably from metaphor |
| `悪い使い道` | misuse / harmful-use category | `悪用` / `misuse` source-specifically | `REVIEW_REQUIRED` | safety taxonomy should remain explicit |
| `生物の仕事` | biology tasks / bio tasks | `生物学タスク` / source category | `REVIEW_REQUIRED` | ordinary wording obscures safety domain |
| `点検されていると疑う素振り` | evaluation awareness / eval awareness | `評価されていることを認識する傾向` / `eval awareness` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | named limitation becomes anthropomorphic prose |
| `作り手の試し言葉` / `試し言葉` | early-tester quotes / testimonials | `テスターのコメント`, `テスター証言`, `early-tester quote` with attribution | `PROHIBITED_HIGH_CONFIDENCE` | testimonial boundary becomes opaque |
| `切れ目を探して始末をつける` | graceful stop / graceful stopping | `graceful stop（安全な中断）` / source product wording | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | formal behavior is hidden in idiom |
| `週の枠から少し分けて後始末` | reserved quota / grace allocation (source-bound) | source-readback required; state exact quota/reserve behavior | `PROHIBITED_HIGH_CONFIDENCE` | usage-limit mechanism unrecoverable |
| `手厚い段差` | plan-specific quota/limit differences | state exact plan/tier differences | `PROHIBITED_HIGH_CONFIDENCE` | vague metaphor for entitlement differences |

### 3.6 science / benchmark methodology

| observed exact search form(s) | canonical concept | preferred direction | classification | rationale |
|---|---|---|---|---|
| `生き物の研究所` | biology lab / life-science lab | `生物学研究施設` / `biology lab` source-specifically | `PROHIBITED_HIGH_CONFIDENCE` | infantilizing/non-technical wording |
| `湾岸の濡れ場` | Bay Area wet lab | `ベイエリアのwet lab（実験室）` | `PROHIBITED_HIGH_CONFIDENCE`, `SEMANTIC_COLLISION_RISK` | `濡れ場` has an unrelated common Japanese meaning |
| `濡れ仕事` | wet-lab work | `wet-lab実験` / `実験作業` | `PROHIBITED_HIGH_CONFIDENCE`, `SEMANTIC_COLLISION_RISK` | same collision |
| `DNAの海` | DNA sequence space/database/search space (source-bound) | source-readback required; `DNA配列データ` / `配列探索空間` | `REVIEW_REQUIRED` | metaphor obscures what was searched |
| `逆転写酵素の変わり種` | unusual/novel reverse transcriptase | `新規／特殊な逆転写酵素` source-specifically | `REVIEW_REQUIRED` | informal wording for scientific claim |
| `繰り返しの列` | repeat array / repeated sequence (source-bound) | preserve source biological term (`反復配列` etc.) | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | scientific structure should use established terminology |
| `列と添えの種` | array + adjacent gene(s), source-bound | source-readback required; use established biology terms | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | meaning is not recoverable |
| `列が短いRNAとして読まれる` | array transcribed into short RNA (source-bound) | `短いRNAへ転写される` / exact source wording | `REVIEW_REQUIRED` | “read” metaphor for transcription |
| `探し回りが使い手の領分` | agentic search / agent-controlled search | `探索はエージェントが担当` / source boundary | `PROHIBITED_HIGH_CONFIDENCE` | autonomy boundary must be technically explicit |
| `心の寄り添いの物差し` | MentalHealthBench | preserve `MentalHealthBench`; explain as mental-health response benchmark | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | benchmark identity dissolved into sentimental prose |
| `免許持ち` | licensed clinicians/professionals | `有資格の臨床家` / `免許を持つ専門家` source-specifically | `PROHIBITED_HIGH_CONFIDENCE` | colloquial wording degrades professional identity |
| `分科` | clinical specialties / disciplines | `専門分野` / `診療科` source-specifically | `REVIEW_REQUIRED` | vague/archaic wording |
| `作り話のやり取り` | synthetic conversations/scenarios | `合成会話`, `synthetic conversation`, `想定会話` source-specifically | `PROHIBITED_HIGH_CONFIDENCE` | “fabricated story” wording changes methodology tone |
| `一つの返し` | response | `応答` / `モデル応答` | `REVIEW_REQUIRED` | colloquial wording in benchmark construction |
| `使い手の記憶の物差し` | agent-memory benchmark | preserve `DolphinBench`; `エージェント記憶ベンチマーク` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | dataset/benchmark identity lost |
| `知識仕事の三つの顔` | three knowledge-work personas/roles | source-readback required; `3種類の知識労働persona/役割` | `PROHIBITED_HIGH_CONFIDENCE` | exact benchmark setup becomes opaque |
| `来歴` where long context/history is meant | interaction history / long-term history/context | `履歴`, `会話履歴`, `長期コンテキスト` source-specifically | `REVIEW_REQUIRED` | ordinary biography/history word may misstate benchmark input |
| `題` / `200題` where tasks/questions are meant | benchmark tasks/questions | `タスク`, `設問` source-specifically | `REVIEW_REQUIRED` | benchmark unit should be explicit |
| `表紙` / `6枚の草稿の表紙` / `表紙読み` where arXiv abstract is meant | arXiv abstract / abstract-only consumption | `arXiv abstract（要旨）のみ` / `要旨のみ確認` | `PROHIBITED_HIGH_CONFIDENCE`, `SEMANTIC_COLLISION_RISK` | abstract is not a cover page |
| `土台の数` where baselines are meant | baselines / baseline count | `ベースライン` / `比較対象` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | collides with base-model wording |
| `草稿の権威` | paper/preprint authority | `論文／プレプリントを根拠とする` with exact evidence boundary | `REVIEW_REQUIRED` | abstract editorial metaphor |

### 3.7 privacy / security architecture

| observed exact search form(s) | canonical concept | preferred direction | classification | rationale |
|---|---|---|---|---|
| `私的計算` when the named system is meant | Private AI Compute | preserve `Private AI Compute`; Japanese gloss may follow | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | proper architecture name should not be dissolved |
| `私的記憶` | privacy-preserving/server-side memory | `プライバシー保護されたサーバー側メモリ` / source wording | `REVIEW_REQUIRED` | vague phrase can imply “personal memory” instead of privacy architecture |
| `覚える雲` | server-side/cloud memory | `サーバー側メモリ` / `クラウド側メモリ` source-specifically | `PROHIBITED_HIGH_CONFIDENCE` | poetic metaphor for architecture |
| `越し方の記憶` | cross-session/persistent memory | `セッションをまたぐ永続メモリ` / source-specific persistent memory | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | mechanism unrecoverable |
| `雲の隔離の座` | cloud enclave / secure enclave | `secure enclave（セキュアエンクレーブ）` / source formal term | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | enclave identity destroyed |
| `用を足す` / `用を足すたびに忘れる` | process/compute; stateless per-request behavior (source-bound) | state exact processing/stateless behavior | `PROHIBITED_HIGH_CONFIDENCE` | colloquial idiom is semantically hazardous |
| `包み直す` | re-encrypt / re-wrap encrypted data | `再暗号化` / source-specific cryptographic operation | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | encryption identity lost |
| `使った道具の正しさ` | attestation / verifiable software identity (source-bound) | preserve `attestation` / `software verification` / exact source term | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | security mechanism becomes vague |
| `公開の記録` | transparency log / public log (source-bound) | `transparency log（透明性ログ）` / exact source term | `REVIEW_REQUIRED`, `CANONICAL_IDENTITY_RISK` | formal security mechanism may be hidden |
| `端末・中核・雲の四つの組` | named four-team/component collaboration (source-bound) | source-readback required; enumerate actual teams/components | `PROHIBITED_HIGH_CONFIDENCE` | current phrase is internally inconsistent and opaque |
| `跨いで覚える道` | persistent cross-session memory | `セッションをまたぐ永続メモリ` | `PROHIBITED_HIGH_CONFIDENCE` | mechanism expressed as metaphor |
| `技の書` | technical brief | `technical brief（技術資料）` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | document identity is lost |
| `守りの性質` | security properties | `セキュリティ特性` / `security properties` | `REVIEW_REQUIRED` | formal security term should be explicit |

### 3.8 temporal / release / community boundary language

| observed exact search form(s) | canonical concept | preferred direction | classification | rationale |
|---|---|---|---|---|
| `影の登場` / `影の品` / `影の正体` | stealth model / unidentified model | `stealth model`, `未特定モデル`, `Pixel Canary` source-specifically | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | “shadow” metaphor obscures release identity |
| `不通の知らせ` | outage notice | `障害報告` / `outage notice` | `REVIEW_REQUIRED` | operational incident should be explicit |
| `持ち込み` where carry-in is meant | carry-in / carry-over | `前号からの持ち越し` / `carry-over` | `REVIEW_REQUIRED` | ingestion metaphor for editorial temporal category |
| `送り` / `次号への送り` | carry-over to next issue | `次号へ持ち越す` / `次号で再検証する` | `REVIEW_REQUIRED` | vague editorial shorthand |
| `窓` / `窓を過ぎた` where formal edition time window is meant | edition window / post-window | `対象期間`, `締切後`, `期間外` where reader-facing | `REVIEW_REQUIRED` | internal window jargon may be okay only if explicitly defined |
| `窓過ぎの二次書き` / `窓を過ぎた翌日の二次書き` | post-window secondary report | `対象期間後の二次資料` | `PROHIBITED_HIGH_CONFIDENCE` | unnatural coined phrase |
| `古い呼び名の求め` / `古い呼び名の回し先` | legacy alias requests / routing | `旧モデル名へのAPIリクエスト` / `旧aliasのルーティング先` | `PROHIBITED_HIGH_CONFIDENCE`, `CANONICAL_IDENTITY_RISK` | API routing behavior becomes opaque |
| `求め` where API request is meant | request | `リクエスト` | `REVIEW_REQUIRED` | ordinary request noun can hide protocol/API unit |
| `切り替わりの正確な刻` | exact cutover instant/timestamp | `正確な切替時刻` / `cutover時刻` | `REVIEW_REQUIRED` | literary timestamp wording |
| `紙` / `紙面` where a web doc/page is meant | documentation page / pricing page / release page | `公式ページ`, `料金表`, `ドキュメント` source-specifically | `REVIEW_REQUIRED` | physical-paper metaphor can misdescribe web authority |

### 3.9 reader-facing framing metaphors requiring review

These are not always wrong in ordinary prose, but in W39 they are repeatedly used in headings/decks to replace technical categories. Every occurrence requires a contextual decision rather than automatic replacement.

| observed exact search form(s) | canonical concept | preferred direction | classification |
|---|---|---|---|
| `確かめの道具立て` | evaluation / benchmarks | `評価`, `ベンチマーク`, or a natural descriptive heading | `REVIEW_REQUIRED` |
| `使い倒しの道具立て` | agent tooling / operational tooling | `エージェント運用のツール群` / source-specific heading | `REVIEW_REQUIRED` |
| `働かせ方の運び` | agent operations | `エージェント運用` | `REVIEW_REQUIRED` |
| `覚える雲、鍵は手元に` | privacy-preserving cloud/server memory | preserve intended reader tone only if technical identity is stated plainly in the same heading/deck | `REVIEW_REQUIRED` |
| `安くなる最前線、運ばれる仕事` | lower-cost frontier + agent operations | rewrite only if needed after section-level terminology repair; do not preserve “transported work” if it remains technically vague | `REVIEW_REQUIRED` |

## 4. Required use in future editions

A terminology pass that merely checks words already present in the current edition is insufficient.

For every Publication Preview remediation run:

1. load the **entire parent seed** and this W39 supplement;
2. enumerate every `observed` literal/search form from both files;
3. search all reader-facing source fields and rendered-source files, including terms with zero current hits;
4. for every hit, inspect surrounding sentence/paragraph and accepted source/evidence;
5. choose exactly one decision:
   - `REPLACE`
   - `RETAIN_WITH_CONTEXT_REASON`
6. never blind-replace a substring merely because it appears in the seed;
7. preserve canonical named entities, benchmark identities, metric names, product names, configuration labels, source strength, temporal boundaries, and uncertainty;
8. after the known-seed pass, perform a **seed-external residual scan** looking for newly coined/metaphorical technical wording not yet in either corpus;
9. add any new generalizable residuals back to the generic corpus before declaring terminology closure.

## 5. Required occurrence ledger schema

Every remediation run must preserve an auditable occurrence ledger with at least:

- `seed_source` (`BASE` or `W39_SUPPLEMENT`)
- `observed_form`
- `file`
- `line_or_locator`
- `context_excerpt`
- `canonical_concept`
- `decision` (`REPLACE` / `RETAIN_WITH_CONTEXT_REASON`)
- `replacement_or_retained_form`
- `reason`
- `source_recheck_required`
- `source_recheck_result`
- `post_edit_validation`

Zero-hit search forms must also be recorded as `ZERO_HIT_CHECKED`; this is how future editions prove that the **whole corpus**, not only current known defects, was searched.

## 6. W39 closure condition

W39 terminology remediation is not complete until:

- all reader-facing `.tex` and reader-manuscript fields have been searched against the full combined corpus;
- every hit has a context decision in the occurrence ledger;
- the W39 examples in §§2–3 above are no longer present in defective technical contexts;
- seed-external residual scan returns no unresolved coined/metaphorical technical term;
- semantic/citation/temporal boundaries remain unchanged except for wording clarification;
- regenerated PDF is visually reviewed after terminology repair.
