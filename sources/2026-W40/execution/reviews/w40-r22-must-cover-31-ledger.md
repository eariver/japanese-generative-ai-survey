# W40 r22 — 31 must-cover semantic coverage ledger

Status: `WORKER_SEMANTIC_AUDIT / ROW_LEVEL_EVIDENCE / R22_DRAFT`
Rule: file-path presence is NOT fulfilment. Every row links exact new Draft block IDs with real quoted exposition plus table/formula kind.

## 01 [P1] (prose) — AUDIT PASS — Sonnet full p

Requirement: `Sonnet 5.5 Sep 28: full price card + safeguard posture + Terminal-Bench 70.6% and GDPval-AA 1844 vendor-reported, attrib…`

- `p1-sonnet-card`: 「Anthropicは9月28日、Claude Sonnet 5.5をリリースした。Claude 5.5ファミリーの2番目のモデルで、窓より前のOpus 5.5（9月22日）を補う位置づけであり、最上位の交代ではない。料金はSonnet 5と同額の公称価格で、入力100万トークンあたり2ドル、出力10ドル、キャッシュ読み…」
- `p1-sonnet-bench`: 「ベンチマークはすべてベンダー計測であり、条件も努力量も異なるため、横断的な優劣表にはしない。Terminal-Bench 4.0で70.6%（Sonnet 5の10.3%から大幅に伸びたとされる）、FrontierCode 1.1 Mainで46.2% Max、CursorBench 4.0で55.5%、GDPval-…」
- Disposition: PASS — Sonnet full price card (2/10/0.20), safeguards, 6 benchmarks with conditions in prose.

## 02 [P1] (prose) — AUDIT PASS — Sol price car

Requirement: `GPT-6.1 Sol Sep 29: verified price card ($2/$10/$0.10) + changelog cross-check + vendor benchmark deltas attributed; Ult…`

- `p1-sol`: 「OpenAIは9月29日、GPT-6.1 Solをリリースした。料金表は変更履歴との突き合わせ済みで、入力100万トークンあたり2ドル、出力10ドル、キャッシュ読み取り0.10ドルとされる。ベンダー側の性能差分は発表者の計測として帰属させる。高速化を示唆するUltrafastのsoon表示は今号の対象に含めない。日付は…」
- Disposition: PASS — Sol price card + changelog cross-check + attributed deltas + Ultrafast exclusion in prose.

## 03 [P1] (prose) — AUDIT PASS — Argon 1M OUTP

Requirement: `Gemini 4 Argon Sep 30: source-precise 1M OUTPUT limit (never input), intro pricing, vendor SOTAs attributed, tester-only…`

- `p1-argon`: 「Googleは9月30日、Gemini 4 Argonを発表した。100万という枠は出力トークンの上限であり（64Kからの拡大とされる）、入力コンテキストの大きさやAPI提供の広がり、展開範囲の広さをこの文言から推し量ってはならない。モデル文書による確認は積み残しである。導入価格は入力2ドル・出力10ドルで95%割引、…」
- Disposition: PASS — Argon 1M OUTPUT precision, intro/post-intro pricing, 5 vendor SOTAs, tester-only in prose.

## 04 [P1] (prose+table) — AUDIT PASS — Day-only date

Requirement: `Day-only dates honored; all benchmark deltas vendor-run with independent reproduction pending.…`

- `p1-sonnet-card`: 「Anthropicは9月28日、Claude Sonnet 5.5をリリースした。Claude 5.5ファミリーの2番目のモデルで、窓より前のOpus 5.5（9月22日）を補う位置づけであり、最上位の交代ではない。料金はSonnet 5と同額の公称価格で、入力100万トークンあたり2ドル、出力10ドル、キャッシュ読み…」
- `p1-sonnet-bench`: 「ベンチマークはすべてベンダー計測であり、条件も努力量も異なるため、横断的な優劣表にはしない。Terminal-Bench 4.0で70.6%（Sonnet 5の10.3%から大幅に伸びたとされる）、FrontierCode 1.1 Mainで46.2% Max、CursorBench 4.0で55.5%、GDPval-…」
- `p1-sol`: 「OpenAIは9月29日、GPT-6.1 Solをリリースした。料金表は変更履歴との突き合わせ済みで、入力100万トークンあたり2ドル、出力10ドル、キャッシュ読み取り0.10ドルとされる。ベンダー側の性能差分は発表者の計測として帰属させる。高速化を示唆するUltrafastのsoon表示は今号の対象に含めない。日付は…」
- `p1-argon`: 「Googleは9月30日、Gemini 4 Argonを発表した。100万という枠は出力トークンの上限であり（64Kからの拡大とされる）、入力コンテキストの大きさやAPI提供の広がり、展開範囲の広さをこの文言から推し量ってはならない。モデル文書による確認は積み残しである。導入価格は入力2ドル・出力10ドルで95%割引、…」
- `p1-table`: 「表: 3モデルの料金・提供・計測の切り分け | Sonnet 5.5: 料金2/10/0.20ドル、提供1M context・128K出力・3クラウド、計測TB 70.6%・GDPval-AA 1844（ベンダー） | GPT-6.1 Sol: 料金2/10/0.10ドル、提供API・変更履歴突き合わせ済み、計測ベンダ…」
- Disposition: PASS — Day-only dates + vendor-run attribution in prose; P1 comparison table lays out 3-model split.

## 05 [P2] (prose+table) — AUDIT PASS — 27B vs 35B-A3

Requirement: `Holo4 Sep 28: 27B vs 35B-A3B split kept; OSWorld 85.2%/80.8% and OSWorld2 61.7%/30.9% publisher-run; private-set eval pe…`

- `p2-holo`: 「H Companyは9月28日、エージェント向けモデルHolo4の2機種をリリースした。27Bの高密モデルと35B-A3BのMixture-of-Expertsモデルは名称が似ていても別物として扱う。高密モデルは研究・非商用ライセンス、MoEモデルはApache-2.0であり、この切り分けを取り違えると利用可否の判断が…」
- `p2-table`: 「表: Holo4とELYZAの切り分け | Holo4: 27B高密（研究・非商用）と35B-A3B MoE（Apache-2.0）、OSWorld 85.2/80.8・OSWorld2 61.7/30.9（発表者計測、私的セット積み残し） | ELYZA: 33B（61.69/日本語62.18、SHA特定）とMoE（…」
- Disposition: PASS — 27B vs 35B-A3B split + licenses + OSWorld/OSWorld2 with private-set caveat in prose + Holo4/ELYZA comparison table.

## 06 [P2] (prose) — AUDIT PASS — Pinned SHAs (

Requirement: `ELYZA Oct 2 eligible: pinned SHAs + Apache-2.0 + 33B 61.69/JA62.18 and MoE 58.46/JA59.61 with JA-localized method and co…`

- `p2-elyza`: 「ELYZAは10月2日、Thinking LLM-jp-4の2機種を公開した。33Bモデルが61.69、日本語62.18、MoEモデルが58.46、日本語59.61で、日本語に寄せた手法と完全な表をそろえ、発表者の計測として分母つきで載せる。重みはコミットSHAで特定し（33Bは6ca556b2…、MoEは5260ec…」
- Disposition: PASS — Pinned SHAs (both), Apache-2.0, 4 scores with JA method + complete tables in prose.

## 07 [P2] (prose) — AUDIT PASS — Trajectory vi

Requirement: `Trajectory viewer + HF dataset links noted as replay-not-executed; Holo4 Nano kept as sub-model, not separate event.…`

- `p2-elyza`: 「ELYZAは10月2日、Thinking LLM-jp-4の2機種を公開した。33Bモデルが61.69、日本語62.18、MoEモデルが58.46、日本語59.61で、日本語に寄せた手法と完全な表をそろえ、発表者の計測として分母つきで載せる。重みはコミットSHAで特定し（33Bは6ca556b2…、MoEは5260ec…」
- `p2-method`: 「読み分けの要点は、汎用エージェント用途のHolo4と日本語特化のELYZAという方法の違いにある。Holo4はOSWorld系の汎用操作ベンチマーク、ELYZAは日本語を含む言語別スコアで測られており、物差しが違うため単純な横並びの優劣にはしない。手法・分母・ライセンス・重みの特定可能性をそろえた比較表を添える。…」
- Disposition: PASS — Trajectory viewer replay-not-executed + Nano sub-model note + method-difference prose.

## 08 [P3] (prose) — AUDIT PASS — systemone int

Requirement: `Ollama v0.35 Sep 29: /v1/systemone interface + Nimble 9B + Tev1 4B/0.8B; 91ms single-example illustrative, not universal…`

- `p3-ollama`: 「Ollamaは9月29日、v0.35で判断支援モデル向けのインターフェースを開けた。/v1/systemoneというAPIに、Nimble 9BとTev1の4B・0.8Bモデルが並ぶ。ブログ本文は通読済みの範囲の話である。91ミリ秒という数値は単一事例の例示であって、普遍的な性能ではない。ここは新しいモデルの登場ではな…」
- Disposition: PASS — systemone interface + Nimble/Tev1 + 91ms illustrative-only + registry/API limits in prose.

## 09 [P3] (prose) — AUDIT PASS — Oct1 timestam

Requirement: `Clef Oct 1 15:34:02Z: Apache-2.0 weights + 64K ctx + vision + $0.24/$0.09; Jev-Index vendor-hosted lead + latencies vend…`

- `p3-clef`: 「Cloudflareは10月1日15時34分02秒（UTC）にClefをリリースした。重みはApache-2.0ライセンスで公開され、Jev API、6万4千トークンのコンテキストと画像入力、入力0.24ドル・出力0.09ドルの料金が並ぶ。入力は意思決定タスクの記述と画像、出力は判断結果と根拠という構成である。Jev …」
- Disposition: PASS — Oct1 timestamp + Apache-2.0 + 64K/vision + prices + Jev vendor-hosted caveat + no-merge in prose.

## 10 [P3] (prose) — AUDIT PASS — Qwen3.5-2B + 

Requirement: `Strands Decider 2B Oct 1: Qwen3.5-2B + pointer head + r16 LoRA; JevBench/latency attributed; Apache-2.0 triple-confirmed…`

- `p3-strands`: 「Strandsは10月1日、Decider 2Bをリリースした。Qwen3.5-2Bベースにpointer headとr16 LoRAを添えた構成で、ベンダー帰属つきのJevBench結果とレイテンシ、Apache-2.0ライセンスの三重確認が示される。重み配布ページの版はv19で固定する。先頭表示が古い版の様相を見せ…」
- Disposition: PASS — Qwen3.5-2B + pointer head + r16 LoRA + attributed JevBench + triple Apache-2.0 + v19 pin in prose.

## 11 [P4] (prose) — AUDIT PASS — WHAT-shipped 

Requirement: `Agents API computer use: changelog states WHAT shipped (approvals/sign-in handling); computer-use guide docs unopened; n…`

- `p4-agents`: 「OpenAIのAgents APIに、ホスト型ブラウザーでのコンピューター操作機能が加わった。アプリケーション側で承認処理とサインインを扱いながら操作するもので、APIとCodex、WorkのPro500やEnterpriseプランとの組み合わせで提供される。変更履歴の逐語が根拠であり、利用方法は読み取れるが、ここから…」
- Disposition: PASS — WHAT-shipped changelog scope + approvals/sign-in + guide-docs-unopened + no-safety-inference in prose.

## 12 [P4] (prose) — AUDIT PASS — Cloud/browser

Requirement: `dots: cloud computer/browser + 4000+ plugins + read-only proactivity + auto-review; Pro/Biz-Premium + Enterprise/Edu bet…`

- `p4-dots`: 「dotsは、Astraの技術を土台とする常駐型エージェントという位置づけである。クラウド上のコンピューターとブラウザー、4000超のプラグイン、読み取り専用の先回り動作、自動レビューが並ぶ。ProやBiz-PremiumとEnterprise・Eduのベータ提供の組み合わせも示される。製品説明の範囲として読み、測定され…」
- Disposition: PASS — Cloud/browser + 4000+ plugins + read-only proactivity + tiers/beta bounds in prose.

## 13 [P4] (prose) — AUDIT PASS — Bundle-as-spi

Requirement: `DevDay hub: Ultrafast tier + Decisions preview + Agents computer use + Codex family + plugins/Space/Pro500/Marketplace a…`

- `p4-hub`: 「DevDayの発表の束ねは、30番目の見出しにはしない。Ultrafastプラン、Decisionsプレビュー、エージェントのコンピューター操作、Codexファミリー、プラグインやSpaceやPro500やマーケットプレイスが一束になった目録であり、支えとして小さく載せる。見出しに立てれば製品カタログの羅列になるだけで…」
- Disposition: PASS — Bundle-as-spine (never headline) treatment in prose.

## 14 [P5] (prose) — AUDIT PASS — Team-blog + v

Requirement: `ProvenanceGuard W40 team-blog event + pre-window paper v1/v2 ONLY (v2 Jul 26, four authors): routing+NLI+attribution+all…`

- `p5-guard`: 「ProvenanceGuardは、今週のチームブログ記事に載った出来事と、対象期間より前の4著者の論文（v1と7月26日のv2）だけで読む。v3の有無については何も言わない。ルーティングと自然言語推論、帰属づけと許可・遮断、RARRという構成で、281件の追跡のうち138件と139件を検出し、F1スコアで0.802と0…」
- `p5-guard-limits`: 「測定値の読み方に注意が要る。281件という母数、F1の2条件、複数情報源の3条件は、それぞれ別の実験設定の数値であり、一つの優劣に畳んではならない。図表はテキストの仮置きとして読み、5.4節以降や付録の範囲を超えた部分は未読である。コードやポスター、リポジトリの変更提案は開いていない。来歴評価という機能に限った読みとす…」
- Disposition: PASS — Team-blog + v1/v2-only + routing/NLI/attribution/allow-block/RARR + 281/138/139/F1/multi-source + separate-settings warning in prose.

## 15 [P5] (prose) — AUDIT PASS — OpenShell bro

Requirement: `Open Agent Safety Sep 28: OpenShell OSS runtime (broadly available) + Sentry BlueField-4 reference (ms quarantine, DOCA)…`

- `p5-opsafety`: 「NVIDIAのOpen Agent Safety Platformは、公開されたエージェント見守りのリファレンスアーキテクチャである。OpenShellのOSSランタイムは広く提供され、SentryのBlueField-4リファレンス構成はミリ秒単位の隔離とDOCAによる計測を添える。Vera向けに最適化し、ArmやI…」
- Disposition: PASS — OpenShell broad availability + Sentry reference (ms quarantine, DOCA) + Vera/Arm/Intel + reference-only caveat in prose.

## 16 [P5] (prose) — AUDIT PASS — 3-target lab 

Requirement: `SynthID Bio: protein watermarking preserving lab-tested function on 3 targets; Nature paper Sep 30 (X Oct 1 momentum onl…`

- `p5-bio`: 「SynthID Bioは、タンパク質に電子透かしを埋め込み、実験室試験で機能を保ったという報告である。3つの標的で確かめ、9月30日のNature論文が根拠で、10月1日のX投稿は関心の広がりを示すにすぎない。コードもデータも重みも公開された。バイオセキュリティ層の話題として読む。…」
- Disposition: PASS — 3-target lab function + Nature Sep30 (X momentum only) + code/data/weights releases in prose.

## 17 [P5] (prose) — AUDIT PASS — Guidance-vs-d

Requirement: `Safety cases: aspirational frontier-RL training guidelines (alignment/containment/monitoring + ops + incident); guidance…`

- `p5-cases-oauth`: 「残る2件は小さく添える。最前線モデルの学習向け安全事例集は、アライメントと封じ込めと監視に運用と事後対応を添えた指針文書であり、実証の報告ではない。Workers OAuth Provider v1は、分割されたAPIと2026年7月28日のMCP認証、段階的スコープ引き上げの仕様の話題で、仕様への準拠と脅威への耐性は…」
- Disposition: PASS — Guidance-vs-demonstration distinction for safety cases in prose.

## 18 [P5] (prose) — AUDIT PASS — Split API + M

Requirement: `OAuth Provider v1: split API + MCP 2026-07-28 auth + step-up scope; spec adherence is not threat resistance.…`

- `p5-cases-oauth`: 「残る2件は小さく添える。最前線モデルの学習向け安全事例集は、アライメントと封じ込めと監視に運用と事後対応を添えた指針文書であり、実証の報告ではない。Workers OAuth Provider v1は、分割されたAPIと2026年7月28日のMCP認証、段階的スコープ引き上げの仕様の話題で、仕様への準拠と脅威への耐性は…」
- Disposition: PASS — Split API + MCP 2026-07-28 + step-up scope + spec-vs-resistance distinction in prose.

## 19 [P6a] (prose+table) — AUDIT PASS — Editable file

Requirement: `ContextLM: Bash-synced editable file; Eq.3 prefix-reuse FLOPs (FLOPs_prefill(unmatched context suffix) + FLOPs_decode(ge…`

- `p6a-clm-file`: 「ContextLMは、コンテキストをBashと同期する編集可能なファイルとして扱う。接頭辞再利用の計算量をFLOPsという物差しで測る。式3の定義は、最初の不一致以降のトークンの再プリフィル計算量と新規生成トークンのデコード計算量の合計であり、壁時間でもキャッシュヒット率でもない。一致した接頭辞部分は課金されないという…」
- `p6a-clm-nums`: 「数値の土台は混ぜない。BCPは59.4%で相対11.4%の改善、向かう先はCodex流要約という最強のベースラインである。接頭辞再利用の削減は同ベースラインに21.5%、MEM1に28.9%で、両者は統合しない。TB2.1は同等精度で7割の計算量、TBLiteは73.7対67.0で9割1分の計算量で、土台は同じCode…」
- `p6a-clm-table`: 「表: ContextLMの主要数値と土台の切り分け | BCP 59.4%（相対+11.4%）対Codex流要約 | FLOPs削減21.5%対同左・28.9%対MEM1（統合しない） | TB2.1同等精度・計算量70%対Codex流 | TBLite 73.7/67.0・計算量91%対Codex流 | EdgeBe…」
- Disposition: PASS — Editable file + Eq.3 definition + BCP/EdgeBench/swarm/RL with distinct baselines in prose + metrics table.

## 20 [P6a] (prose+equation) — AUDIT PASS — Eq.5 VERIFIED

Requirement: `ContextLM Eq.5 vs Eq.6: skill-evolution Eq.5 loop (fixed model weights; train/dev/held-out split with single held-out ev…`

- `p6a-clm-eq56`: 「式5はスキル進化ループの記述である。モデルの重みは固定したまま、スキル文書 s を最適化し、学習用・開発用・ホールドアウトの3分割で運用し、ホールドアウトでは一度だけ評価する。持ち越し精度の改善は最大で35.9ポイントと置かれる。式の本体は次の最適化目的であり、コンテキスト内に技を置く流儀である。式6は別の強化学習であ…」
- `p6a-clm-eqs`: 「式の置き場をここに固める。接頭辞再利用の定義は \(\mathrm{FLOPs}_{\mathrm{prefix-reuse}} = \mathrm{FLOPs}_{\mathrm{prefill}} + \mathrm{FLOPs}_{\mathrm{decode}}\) であり、課金対象の明示である。スキル最適化の…」
- Disposition: PASS — Eq.5 VERIFIED loop (fixed weights, 3-split, 35.9pt) vs Eq.6 RL updates (<2-success efficiency-0-only); Eq.4 unchanged; display equations for Eq.3/Eq.5-objective/efficiency term.

## 21 [P6a] (prose) — AUDIT PASS — DDP + GPU rou

Requirement: `Olmo-core 3: DDP resident experts with GPU-resident expert routing/dispatch as the Olmo MoE technical mechanism (reorder…`

- `p6a-olmo`: 「Olmo-core 3は、専門家混合モデルの分散学習基盤である。DDPに専門家を常駐させ、GPU上でexpert routingを決めて並べ替えの余分を抑え、grouped-GEMMとMXFP8で固める。MXFP8の効果はB300 4枚の均一負荷という統制された構成での話で、エンドツーエンドの学習スループットが21%伸…」
- `p6a-olmo-scale`: 「測定の置き場は3つに分ける。47Bは実測値、1.2Tはルーティング条件（能動58.36B・512 GPU・最大858TFLOP/s/GPU、ランダムルーティング下のシステム測定であり、モデル品質の主張ではない）、2.38Tは短時間の容量試験である。3つを一つの規模に束ねてはならない。うまくいかなかった実験も載せる。ルー…」
- Disposition: PASS — DDP + GPU routing/dispatch + grouped-GEMM + MXFP8 B300x4 (+21%, 103->95GiB) + 8->128/2.7x + 47B/1.2T/2.38T separation + negatives + report-body gap in prose.

## 22 [P6b] (prose) — AUDIT PASS — Single-user r

Requirement: `AgentPerf: Spark/5090/Halo/M5Pro single-user trajectory replays; 14 all-speculative configs; publisher-measured; serving…`

- `p6b-agentperf`: 「AA-AgentPerf-Localは、手元で実行するオープンな再実行ベンチマークである。実軌跡をSparkや5090やHaloやM5Proでなぞり直す。実行構成は14通りすべてが仮説的と明記され、発表者の計測として置く。サービングの話に限る品であり、エージェントの賢さの話ではない。帯域制約ルーフラインとの比較は理論上…」
- Disposition: PASS — Single-user replays + 14 speculative + serving-only + theoretical roofline + single-vs-production split in prose.

## 23 [P6b] (prose) — AUDIT PASS — WER/CER/RTFx/

Requirement: `OpenTTS: macro-average English WER + multilingual CER + RTFx (batched offline, H200) + TTFA objective protocol (50 Engli…`

- `p6b-opentts`: 「Open TTS Leaderboardは、多言語・声 cloning の客観評価基盤であり、新しい音声モデルではない。英語の巨視的平均の単語誤り率、多言語の文字誤り率、RTFx（バッチ化オフライン推論、H200）とTTFAとSIMを、Seed-TTSとCV3の上で測る。TTFA手順は一句ごとに検証済みで、同じ英語50…」
- `p6b-opentts-time`: 「到着時期の切り分けは欠かさない。場と物差しの本体は今週にあるが、評価スクリプトは9月30日の記事では「まもなく公開」という未来形である。リポジトリの初の評価スクリプトの固まりは10月7日14時53分41秒（UTC）と確認した。対象期間の締め切り（10月2日22時UTC）の時点ではリポジトリにスクリプトはなく、9月15日…」
- Disposition: PASS — WER/CER/RTFx/TTFA/SIM + 50-prompt/batch1/3-warmup/median/H200 protocol + Sep30-future vs Oct7-commit chronology in prose.

## 24 [P6b] (prose) — AUDIT PASS — Filter + 4 ta

Requirement: `RL-Env Hub Sep 28: rl-environment filter + 4 framework tags (harbor/verifiers/openenv/nemo-gym) + per-framework snippets…`

- `p6b-rlhub`: 「RL Environments Hubは、強化学習環境のタスクセット目録である。rl-environmentフィルターと4つのフレームワークタグ（harbor・verifiers・openenv・nemo-gym）、枠ごとの実行例が並ぶ。タスクセットのデータと実行時・報酬の切り分けを保ち、新しいリポジトリ型はなく、タグ…」
- Disposition: PASS — Filter + 4 tags + snippets + data-vs-runtime split + tag-compatibility + pin-does-not-pin-taskset + missing inputs in prose.

## 25 [P7] (prose+table) — AUDIT PASS — BBox + per-bo

Requirement: `FLUX 3 Oct 1: BBox layout + per-box multi-step edits; $0.041/0.048/0.100/0.607 per resolution + 50%-off Oct 1 15:00 UTC-…`

- `p7-flux`: 「Black Forest Labsは10月1日、FLUX 3の画像SKUを出した。絵の勘所は0から1000のグリッドで置くバウンディングボックスで、全体の説明文と箱ごとの指示例、箱単位の多段階編集という運びである。7月23日のマルチモーダル基盤発表（早期アクセス、映像優先、画像は後数週）は別の出来事であり、混ぜない。X…」
- `p7-flux-table`: 「表: FLUX 3の解像度別料金（10月1日リリースノート、計算機の既定は1k） | 768正方形 0.041ドル | 1k 0.048ドル | 2k 0.100ドル | 4k 0.607ドル。開始特価は10月1日15時UTCから8日まで半額（見出し帯から確認、開示済み）。料金は発表時点の文書の内容である。…」
- Disposition: PASS — BBox + per-box edits + 4 prices mapped to 768sq/1k/2k/4k + promo window + Jul23 separation in prose + price table.

## 26 [P7] (prose) — AUDIT PASS — Skill + EVS m

Requirement: `VSS 3.3: Build Vision Agent skill (<30min demo on 2x RTX PRO 6000) + Adaptive EVS vendor-demo 17%/+46%/-80% on stated co…`

- `p7-vss`: 「NVIDIAのVSS Blueprint 3.3は9月29日のリファレンスアーキテクチャである。Build Vision Agentスキル（vss-build-vision-ai）とAdaptive EVS（コサイン類似度のパッチ枝刈りとイベントバッチ処理）を添え、VLMとRAGとMCPの映像ワークフローを扱う。ボトリ…」
- `p7-vss-time`: 「時系列の正しさが要る。NVIDIAは10月1日9時00分PDT（UTCで同日16時）のライブ配信を9月29日に事前告知しており、この日時は対象期間の締め切り（10月2日22時UTC）より前、すなわち期間内である。告知するのは配信予定であって、配信の実施内容や追加成果を独立検証したものではない。従来の下流分類にあった対象…」
- Disposition: PASS — Skill + EVS metrics (latency 1021->844ms, streams 13->19, summary halving, -80% tokens) + vendor-config variance + reference-only + IN-WINDOW Oct1 9am PDT scheduling correction (delivery unverified) in prose.

## 27 [P7] (prose) — AUDIT PASS — 133.7h + 55.0

Requirement: `Nemotron ASR: Najdi/Hijazi via NeMo (133.7h; WER 55.05%->29.96%; English retained; 24-layer depth study; beam-8 +800ms; …`

- `p7-asr`: 「Nemotronのサウジアラビア方言適応は、チュートリアル範囲の報告である。NeMoの手でNajdiとHijaziを133.7時間、単語誤り率は55.05%から29.96%へ、英語は維持し、24層の深さの検討やビーム8・800ミリ秒の追加、8話者までの話者分離の拡張も添う。評価はSADAとFLEURSの分割ごとの話であ…」
- Disposition: PASS — 133.7h + 55.05->29.96 + English retained + 24-layer + beam-8/800ms + diarization + SADA/FLEURS split scope in prose.

## 28 [P7] (prose) — AUDIT PASS — ATOF/ATIF/OTe

Requirement: `Relay: ATOF/ATIF/OTel-Phoenix tracing + Hermes tutorial (VALUE=42, COLT 2026) + ToolPerf 108-run case study; companion r…`

- `p7-relay-ross`: 「脇の2件は小さく添える。NeMo Relayは、ATOFとATIFとOTel-Phoenixによる計装にHermesチュートリアル（VALUE=42、COLT 2026）とToolPerfの108走の事例を添えたもので、道具立ての話であり、信頼性の証拠ではない。実網での実行は試しであって順位ではない。Rossは、MCP…」
- Disposition: PASS — ATOF/ATIF/OTel-Phoenix + Hermes + ToolPerf108 + instrumentation-not-proof + unopened companions in prose.

## 29 [P7] (prose) — AUDIT PASS — MCP/KB/skills

Requirement: `Ross: MCP/KB/skills/examples + Vivado/Vitis/ROCm + client-agnostic + available-now + monthly cadence; acceleration UNMEA…`

- `p7-relay-ross`: 「脇の2件は小さく添える。NeMo Relayは、ATOFとATIFとOTel-Phoenixによる計装にHermesチュートリアル（VALUE=42、COLT 2026）とToolPerfの108走の事例を添えたもので、道具立ての話であり、信頼性の証拠ではない。実網での実行は試しであって順位ではない。Rossは、MCP…」
- Disposition: PASS — MCP/KB/skills + Vivado/Vitis/ROCm + available-now/monthly + UNMEASURED + embedded-only in prose.

## 30 [P8] (prose) — AUDIT PASS — DEFINITIVE AG

Requirement: `World Labs: DEFINITIVE AGREEMENT (not close) with spatial-model rationale; valuation unvalidated; corporate event, not m…`

- `p8-deals`: 「AMDとWorld Labsは、買収の確定契約を結んだという発表である。完了の報告ではなく、空間モデルという筋書きが添えられる。評価額の話は検証していない。モデルの新登場として読んではならない。企業・業界の出来事として短く載せる。…」
- Disposition: PASS — DEFINITIVE AGREEMENT (not close) + spatial rationale + valuation unvalidated + corporate-only in prose.

## 31 [P8] (prose) — AUDIT PASS — Hybrid defaul

Requirement: `AI Search: hybrid-retrieval default + Workers AI included + multimodal/image search + scanned-PDF OCR (10MiB/4MiB) + bil…`

- `p8-terms`: 「CloudflareのAI Searchは、提供条件の文書である。ハイブリッド検索が既定で、Workers AIが含まれ、マルチモーダルと画像検索、走査PDFのOCR（10MiBと4MiB）、11月1日の課金が並ぶ。ベンチマークの話題ではなく、提供の約束として読む。…」
- Disposition: PASS — Hybrid default + Workers AI + multimodal/OCR bounds + Nov1 billing + terms-not-benchmark in prose.

