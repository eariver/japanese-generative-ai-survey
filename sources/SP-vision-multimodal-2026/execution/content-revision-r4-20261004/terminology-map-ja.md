# Terminology map (edition-local, content-revision-r4-20261004)

Re-audit of `bounded-revision-112-20261004/terminology-map-ja.md`, extended per supplied
fresh independent content review §15. Applies to all 16 draft-result prose + profile synthesis.
Preferred terms replace avoided forms; supplement with explanation at first use where the
concept is introduced. Proper technical nouns in English are kept.

| Avoid | Preferred | Note |
|---|---|---|
| 箱 | バウンディングボックス | 初出で bounding box の略と補足可（前回より継続） |
| 框 | バウンディングボックス | P05の注釈・検出・領域指定の框を全置換（8件） |
| 後始末 | NMS / 後処理 | 前回より継続 |
| 界面 | インターフェース | 前回より継続 |
| 模型 | モデル | model は原則「モデル」（122件置換） |
| 記号量 | トークン数 / トークン予算 | 前回より継続 |
| 仮面 | マスク | 前回より継続 |
| 多方式 | マルチモーダル | 前回より継続 |
| こま | フレーム | frame→フレーム（前回残存なし、今回0件） |
| 名札 | ラベル | 前回より継続 |
| 接近可能性木 | アクセシビリティツリー | 前回より継続 |
| 檔案系統 | ファイルシステム | 残存0を確認 |
| 文書物体模型 | DOM（Document Object Model） | 残存0を確認；英語正式名は置換保護 |
| 物差し | 指標 / 評価軸 / 評価条件 | 残存0を確認 |
| 接地 | グラウンディング | 54件置換（P09×9、P12×8、P15×3、P07A×2他）；初出で位置の対応づけ等の説明を添える |
| 投票型 | POPEの質問方式／初出は反復的な二値質問によるobject probing（polling-based query） | P10×3・P15×4を全置換；ensemble投票との誤読を回避 |
| 定石 | 手順／段取り | 過剰一般化を避け2件除去 |
| 言う側 / できる側 / 言える側 | 言語側 / 行動側 | P13×14＋合成×4を全置換 |
| 通貨の確認 | 鮮度の確認 | P12-b7の生成誤りを修正 |
| 通貨的 | 時間的 | P09-b10の通貨的な新しさ→時間的な新しさ |
| 意味を言い当てる | 潜在表現を予測する | P14-b3の曖昧表現をtechnical meaningへ（3件） |
| 復号器 | デコーダ | decoderは「デコーダ」（9件） |
| 符号化器 | エンコーダ | encoderは「エンコーダ」（13件） |
| 伍する | 匹敵する | 古語化を修正（P09×2） |
| 情報を落とさず | 空間情報をチャネル方向へ再配置する／単純な縮小とは異なる形で高解像度情報を保持する | P09-b2のpixel-unshuffle断定を限定表現へ |
| token / encoder / decoder / markup / suite / pair / dataset / benchmark / mask / interface | トークン / エンコーダ / デコーダ / マークアップ / スイート / ペア / データセット / ベンチマーク / マスク / インターフェース | 無秩序な英語混在を整理（計224件）；DOM正式名・accessibility tree説明は保護 |
| code / data / leaderboard | コード / データ / リーダーボード | 公開文脈の無秩序な混在を整理（29件） |
| supermacy (typo) | 単一方式の優越性 / 万能性 | 前回より継続、残存0 |

Application gaps fixed this run (all 16 packages + synthesis residual scan clean):
接地0、投票型0、框0、檔案系統0、文書物体模型0、言う側/できる側0、通貨の確認0、定石0、伍する0、raw-EN generic tokens 0。
