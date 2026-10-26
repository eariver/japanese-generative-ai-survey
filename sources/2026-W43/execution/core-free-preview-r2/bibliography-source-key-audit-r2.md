# W43 bibliography source-key audit r2 (36 keys, no truncation)

Reader 典拠 keys -> printed TeX `bibitem` -> exact URL/archive/tier/clock/wording. No duplicates/unused/missing. r1 blind 60-char cuts (`速度で]`, `Small/Re]`, `=IMP]`, `upstream validat]`, `別ソ]`, `no post-cutoff]`) all fixed to complete sentences.

| key | URL / absent | archive / tier | clock | printed tier + note (complete) |
|---|---|---|---|---|
| KIMI-X | https://x.com/Kimi_Moonshot/status/2113680701770068067 | X HTML raw / FIRST_PARTY | 2026-10-23T17:15:24Z exact | X原文秒確定。API証拠。重み証拠ではない。 |
| KIMI-BLOG | https://www.kimi.ai/blog/kimi-k3-1-pro | FIRST_PARTY_METADATA | 日付のみ | 日付粒度のみ。2.8T根拠にしない。 |
| FLINT-CARD | https://huggingface.co/RecursiveSI/flint | card bytes / FIRST_PARTY | 2026-10-21 | 39.8B/2.5B/262144/Apache-2.0明記。 |
| FLINT-ART | https://recursive.com/updates/introducing-recursive-flint | HTML raw / FIRST_PARTY | 2026-10-21 | 512k対応・256k推奨の原文。 |
| NEMO-CARD | https://huggingface.co/nvidia/Nemotron-3.5-Bolt-E4B-4GB | FIRST_PARTY | 2026-10-23 | 8B/4B/64K/OpenMDW-1.1。等価比較禁止。 |
| NEMO-COMMITS | …/commits/main | FIRST_PARTY_METADATA | 15:12-19:03Z | 配布時刻のみ。SHA再ハッシュなし。 |
| DI-README | …/DeepInfer/README.md | pin 9bd9cf24 / FIRST_PARTY | 固定版 | 環境変数・seq_seed明記。 |
| DI-ENV | …/environ.py | 8738B / FIRST_PARTY | 固定版 | 設定明記。未実行。 |
| DI-LICENSE | …/LICENSE | FIRST_PARTY | 固定版 | Apache-2.0。範囲未審査。 |
| MEMT-README | …/MemT-1.0/README.md | saved / FIRST_PARTY | 2026-10-20 | 24行=保存容量66x・速度ではない。55行=方式内。208-219行=権利分離。1.86x未検証。 |
| duet-blog-1021 | https://claude.com/…/claude-duet | DERIVED_ONLY | 日付のみ | 未消費残差。独立確認なし。 |
| 1pw-blog-1022 | https://1password.com/… | FIRST_PARTY | 2026-10-22 | 提供予定。liveと書かない。 |
| automode-art-1022 | https://claude.com/…/auto-mode… | FIRST_PARTY | 10-22 IN/8-7 OUT/翌週 | 翌週は将来予定。 |
| flux-page-1019 | …/flux-3-max/text-to-video | FIRST_PARTY_METADATA+VENDOR | 2026-10-19 | 再計算検証済み・独立測定ではない。 |
| flux-elo-1139 | same | DERIVED_ONLY | snapshot差 | AA原表未取得。単一値に統一しない。 |
| flux-keyframes-conflict | absent | UNRESOLVED | 未解決 | PR・FAQ原文未取得。確定矛盾としない。 |
| voxtral-card-units | https://mistral.ai/news/voxtral-3 | VENDOR_BENCH | 日付のみ | 内訳=比較未確認。単価=単位未確認。確認分離記。AA未取得。 |
| deepinfer-import-scope | …/README.md | FIRST_PARTY partial | 固定版 | env確認。import経路未確認。例は未実行。 |
| flux-speed-recalc | …/text-to-video | VERIFIED_DIRECT | Oct19 PR/blog | 25.37/22.31/95.52%再計算。26.5x不整合。 |
| voxtral-announce | https://mistral.ai/news/voxtral-3 | FIRST_PARTY | 日付のみ | TTS数未解決。単一値禁止。 |
| ming-readme-license | https://github.com/inclusionAI/Ming-3.0-tts | FIRST_PARTY saved | 2026-10-19 | MITバイト確認。AA原表未取得。 |
| ming-aa-cited | same repo | DERIVED_ONLY | — | 原表未取得。順位を検証済みにしない。 |
| eleven-blog | https://elevenlabs.io/blog/realtime | FIRST_PARTY | 日付のみ | 指南未開封。AAはblog経由。 |
| patch-rendered | …/coordinated-disclosure… | RENDERED_TEXT / FIRST_PARTY | 日付のみ | 描画抽出のみ。5段階完全。工程外明記。CVE≠不存在証明。 |
| securing-page-rss | …/securing… | FIRST_PARTY_METADATA | 頁日付/RSS二次 | RSSは頁証明ではない。 |
| bio-page | …/biological-data | FIRST_PARTY | 日付のみ | 班内・wet-lab未。独立再現なし。 |
| lowres-page | …/low-resource… | FIRST_PARTY | 日付のみ | 公開≠再現。外部一般化なし。 |
| decisions-page | …/decisions-api | FIRST_PARTY | 日付のみ | 例は例示転載。NOT_RUN。 |
| tanstack-gh | …/releases/tags/… | GH JSON / FIRST_PARTY | 15:18:14Z exact | GH時刻のみ証明。npm証明にならない。別典拠突合。 |
| tanstack-npm | https://registry.npmjs.org/@tanstack%2Fai | RAW_NOT_ARCHIVED | 15:21:49.491Z exact | 原本未取得。限定版URL。GHが証明と書かない。 |
| tanstack-blog | absent | FIRST_PARTY_METADATA | 日付のみ | URL未取得。製品時刻に読まない。分離。 |
| deepseek-1017 | …/news261017 | FIRST_PARTY | 日付のみ | SHA未取得・実行なし。MITは公表。 |
| recap | absent | DERIVED/LIMITED | 新規なし | 横断合成。新規主張なし。 |
| decisions-guide-1025 | …/guides/decisions | Oct25 bytes / FIRST_PARTY | 締切後補足 | Oct25観測。W43事実に昇格させない。 |
| decisions-ts-ref-1025 | …/methods/create | FIRST_PARTY | 締切後読取 | TTLは観測詳細。W43事実としない。 |
| decisions-ref-create | …/resources/…/create | UNAVAILABLE (404) | 2026-10-25 | 典拠に用いない。 |

Audit: 36/36 present, 0 duplicates, 0 unused (all keys appear in reader 典拠 notes or body), 0 missing vs crosswalk (37th crosswalk row is header, not key). URLs clickable in PDF (xurl breaks, 0 overfull). No `速度で]`-type fragments remain (`grep` clean except legitimate body `validate+fix`).
