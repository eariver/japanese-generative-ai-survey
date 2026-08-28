from __future__ import annotations

from pathlib import Path
import re

path = Path('surveys/special/SP001/main.tex')
text = path.read_text(encoding='utf-8')

if r'\usepackage{multicol}' not in text:
    text = text.replace(r'\usepackage{array}' + '\n', r'\usepackage{array}' + '\n' + r'\usepackage{multicol}' + '\n')

layout_setup = r'''\setlength{\columnsep}{1.45em}
\setlength{\multicolsep}{0.65em}
'''
if layout_setup.strip() not in text:
    text = text.replace(r'\addbibresource{references.bib}' + '\n', r'\addbibresource{references.bib}' + '\n\n' + layout_setup)

# Remove production-facing vocabulary while preserving the reader-facing claim.
replacements = {
    'accepted Evidenceでは': '一次資料で確認できる範囲では',
    'accepted Evidenceで': '確認済みの一次資料で',
    'accepted Evidenceに': '確認済みの一次資料に',
    'accepted Evidenceは': '確認済みの一次資料は',
    'accepted Evidenceを': '確認済みの一次資料を',
    '各familyのaccepted Evidenceから': '各familyについて確認した一次資料から',
    'SP001のEvidenceから導ける結論は': '本巻で確認した一次資料から導ける結論は',
    '前5節で確立したevidence-bound claimだけを再構成する': '前5節で一次資料に結び付けて確認した内容だけを再構成する',
}
for old, new in replacements.items():
    text = text.replace(old, new)

plural_notes = r'''
\Needspace{15\baselineskip}
\subsection*{Source-backed verification / 前史のanchor}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.17\textwidth}>{\raggedright\arraybackslash}p{0.38\textwidth}>{\raggedright\arraybackslash}X@{}}
\toprule
Artifact & 一次資料で確認するtechnical point & 読解上の境界 \\
\midrule
GLM-130B & 2022年のlarge bilingual pre-trained modelとしてchronologyを固定する。 & 後年のsparse attentionやRL infrastructureへの直接継承までは推定しない。 \\
Baichuan 2 & 2023年時点ですでに複数のopen large-model branchが存在したことを示す。 & 2026年の主要familyの性能やlicenseを代理させない。 \\
DeepSeek LLM & 7B/67B、約2T-token中英pretraining、scaling-law、SFT/DPOをfoundation baselineとして置く。 & 後のV2/R1の設計をこの段階へ遡及させない。 \\
Qwen2 & dense/MoEのmodel breadthとhub distribution、quantization、fine-tuning、deploymentを同じfamily surfaceとして確認する。 & family labelを単一architectureや単一licenseへ縮約しない。 \\
\bottomrule
\end{tabularx}
\normalsize
\autocite{glm130b,baichuan2,deepseekllm,qwen2}
'''

deepseek_notes = r'''
\Needspace{17\baselineskip}
\subsection*{Source-backed Technical Notes / DeepSeek}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.16\textwidth}>{\raggedright\arraybackslash}p{0.43\textwidth}>{\raggedright\arraybackslash}X@{}}
\toprule
Artifact & Technical point & Boundary / limitation \\
\midrule
DeepSeek LLM & 7B/67B、約2T-tokenの中国語・英語pretraining、scaling-law、SFT/DPOをfoundation baselineとして確認する。 & 後のefficiency architectureやRL reasoningを最初から内包したfamilyとは扱わない。 \\
DeepSeek-V2 & 236B total / 21B activated、128K context、MLA、DeepSeekMoE。capacityとactive computation、attention/serving costを別軸として読む。 & total/active parameterを他familyの異なるaccountingへそのまま正規化しない。 \\
DeepSeek-R1 & R1-Zeroのpreliminary SFTなしlarge-scale RLと、最終R1のcold-start + multi-stage sequenceを分けて確認する。 & primary weightsとdistilled derivativesのlicense authorityを混同しない。 \\
DeepSeek V4 & 1M context、sparse/token-compression、thinking/non-thinking、agentic coding、API/deploymentをsystem endpointとして確認する。 & checkpoint-specific license、benchmark comparability、current detailはartifact-localのまま残す。 \\
\bottomrule
\end{tabularx}
\normalsize
\autocite{deepseekllm,deepseekv2,deepseekr1,deepseekv4}
'''

qwen_notes = r'''
\Needspace{15\baselineskip}
\subsection*{Source-backed Technical Notes / Qwen}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.16\textwidth}>{\raggedright\arraybackslash}p{0.43\textwidth}>{\raggedright\arraybackslash}X@{}}
\toprule
Artifact & Technical point & Boundary / limitation \\
\midrule
Qwen2 & dense/MoEを含むmodel range、multilingual/coding/math/reasoning、Hugging Face/ModelScope distributionを確認する。 & family labelを一つのparameter countやarchitectureへ縮約しない。 \\
Qwen2 engineering surface & quantization、fine-tuning、deployment resourceがfirst-party technical surfaceに含まれ、weight取得後のdeveloper pathを形成する。 & resourceの存在だけから特定hardware上のcost/performance advantageを推定しない。 \\
Qwen3.8 & 2026年のofficial repositoryでagent/coding/research positioningとHugging Face/ModelScope distributionを確認する。 & Qwen2からのchronologyを特定mechanismの直接継承とはみなさない。 \\
License / performance & repositoryとcheckpoint-specific weight/model licenseを分離し、performanceはsource-local条件に止める。 & repository metadataから全checkpointの再配布・商用利用条件を一括推定しない。 \\
\bottomrule
\end{tabularx}
\normalsize
\autocite{qwen2,qwen38}
'''

glm_notes = r'''
\Needspace{16\baselineskip}
\subsection*{Source-backed Technical Notes / GLM}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.16\textwidth}>{\raggedright\arraybackslash}p{0.43\textwidth}>{\raggedright\arraybackslash}X@{}}
\toprule
Artifact & Technical point & Boundary / limitation \\
\midrule
GLM-130B & 2022年のlarge bilingual pre-trained modelをfamily chronologyのanchorとして確認する。 & GLM-5のsparse mechanismやRL infrastructureへの直接的mechanism ancestryは主張しない。 \\
GLM-5 scale & 744B total / 40B active、28.5T tokensをsource-local specificationとして扱う。 & token countやparameter accountingを他familyとの単純efficiency rankingへ変換しない。 \\
GLM-5 systems & sparse-attention provenance wording、asynchronous RL infrastructure、long-horizon agentic engineeringを同じ2026 endpointで確認する。 & 類似mechanismの存在からorganizational lineageを推定しない。 \\
Local serving & 複数のlocal-serving recipeがtechnical materialへ含まれることをdeployment surfaceとして扱う。 & 未検証hardware上のcost superiorityやrepository/model license条件を補完しない。 \\
\bottomrule
\end{tabularx}
\normalsize
\autocite{glm130b,glm5}
'''

kimi_notes = r'''
\Needspace{16\baselineskip}
\subsection*{Source-backed Technical Notes / Kimi}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.16\textwidth}>{\raggedright\arraybackslash}p{0.43\textwidth}>{\raggedright\arraybackslash}X@{}}
\toprule
Artifact & Technical point & Boundary / limitation \\
\midrule
Kimi k1.5 & long-context multimodal reasoningとRL methodをfamily内のbridgeとして確認する。 & 後続K3の個別mechanismをk1.5由来と遡及的に決めない。 \\
Kimi K3 scale & 2.8T open-weight native multimodal model、sparse MoEを同じrelease lineで確認する。 & total scaleとsparse routingが示すactive computationを同じ尺度にしない。 \\
Kimi K3 system & 1M context、efficient-attention/residual mechanism、long-horizon coding/agentic focusをsystem propertyとして読む。 & DeepSeek V4との「1M」一致から同一mechanismや技術系譜を推定しない。 \\
License / benchmark & 技術仕様を記述する一次資料と、checkpoint固有の利用条件・性能条件を別authorityとして扱う。 & open-weightという配布形態から商用利用やcross-family benchmark comparabilityを自動推定しない。 \\
\bottomrule
\end{tabularx}
\normalsize
\autocite{kimik15,kimik3}
'''

comparison = r'''\subsection{Cross-family structured comparison}
\subsubsection*{設計とpost-trainingの比較}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.13\textwidth}>{\raggedright\arraybackslash}p{0.24\textwidth}>{\raggedright\arraybackslash}p{0.31\textwidth}>{\raggedright\arraybackslash}X@{}}
\toprule
Family & 強い転換点 & Architecture / compute & Post-training / behavior \\
\midrule
DeepSeek & LLM $\rightarrow$ V2 $\rightarrow$ R1 $\rightarrow$ V4 & V2のMoE/MLA/DeepSeekMoE、236B total / 21B active。V4ではsparse/token-compressionへ展開。 & R1-Zeroのlarge-scale RL、R1のcold-start + multi-stage。V4ではthinking/non-thinkingとagentic codingへ接続。 \\
Qwen & Qwen2 $\rightarrow$ Qwen3.8 & dense/MoEを含むmodel breadthを、単一checkpointではなくfamily設計として維持。 & coding/math/reasoningを広いfamily surfaceとして扱い、2026にはagent/coding/research lineを前面化。 \\
GLM & GLM-130B $\rightarrow$ GLM-5 & 744B total / 40B active、sparse attention。 & asynchronous RL infrastructureとlong-horizon agentic engineeringをsystems endpointへ統合。 \\
Kimi & k1.5 $\rightarrow$ K3 & K3は2.8T、sparse MoE、efficient-attention/residual、1M context。 & k1.5のmultimodal reasoning/RLから、K3のlong-horizon coding/agentic focusへ展開。 \\
\bottomrule
\end{tabularx}
\normalsize

\subsubsection*{Distribution / servingと公開境界}
\small
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.13\textwidth}>{\raggedright\arraybackslash}p{0.43\textwidth}>{\raggedright\arraybackslash}X@{}}
\toprule
Family & Distribution / serving & License / comparison boundary \\
\midrule
DeepSeek & V4ではagentic codingをAPI/deploymentへ接続し、context・推論mode・tool-oriented workloadを同じ運用surfaceへ束ねる。 & checkpoint licenseとbenchmark comparabilityはartifact-local。R1 primary weightsとdistilled derivativesも分ける。 \\
Qwen & Hugging Face/ModelScope、quantization、fine-tuning、deploymentをdeveloper pathとして継続し、Qwen3.8ではagent/coding/research用途へ接続。 & repository licenseと各checkpointのweight/model licenseを同一視しない。 \\
GLM & GLM-5は複数local-serving recipeをtechnical materialへ含め、post-trainingとdeploymentを同じsystems engineeringへ入れる。 & repository/model licenseは未解決境界。hardware間のcost superiorityは未検証。 \\
Kimi & open-weight native multimodal releaseとして、1M contextをlong-horizon coding/agentic workloadへ接続する。 & checkpoint固有licenseとsource-local benchmark条件を、open-weightという語だけで補完しない。 \\
\bottomrule
\end{tabularx}
\normalsize

二つの表は順位表ではない。上段は各familyで第一級になった設計問題を、下段はmodel artifactを利用可能にするdistribution/runtimeと公開境界を分離している。parameter accounting、context evaluation、benchmark harnessが異なるため、数値を一つの横断scoreへ正規化しない。
'''

# Add local balanced two-column flows for normal narrative, keeping headings/tables/notes full-width.
plural_label = r'\label{sec:plural}'
if plural_label + '\n\n\\begin{multicols}{2}' not in text:
    text = text.replace(plural_label + '\n\n', plural_label + '\n\n\\begin{multicols}{2}\n\\raggedcolumns\n', 1)
    text = text.replace(r'\subsection{Source-specific chronology: 2022--2024}', r'\end{multicols}' + '\n\n' + r'\subsection{Source-specific chronology: 2022--2024}', 1)
    marker = r'\autocite{glm130b,baichuan2,deepseekllm,qwen2}' + '\n\n' + 'この表は「祖先表」ではない。'
    text = text.replace(marker, r'\autocite{glm130b,baichuan2,deepseekllm,qwen2}' + '\n\n' + r'\begin{multicols}{2}' + '\n' + r'\raggedcolumns' + '\n' + 'この表は「祖先表」ではない。', 1)

# Close each family flow before its full-width verification layer and start the next family in two columns.
transitions = [
    (r'\section{DeepSeek: foundationから効率化、reasoning、agentic frontierへ}', plural_notes, 'sec:deepseek'),
    (r'\section{Qwen: model breadthとdistributionを一体化する}', deepseek_notes, 'sec:qwen'),
    (r'\section{GLM: bilingual foundationからagentic systems engineeringへ}', qwen_notes, 'sec:glm'),
    (r'\section{Kimi: long contextとmultimodal reasoningからopen-weight agentへ}', glm_notes, 'sec:kimi'),
    (r'\section{最終総括: 2026年のfrontierで収束したもの、残った差}', kimi_notes, None),
]
for section_marker, notes, next_label in transitions:
    if notes.strip() not in text:
        text = text.replace(section_marker, r'\end{multicols}' + '\n\n' + notes + '\n' + section_marker, 1)
    if next_label:
        label = r'\label{' + next_label + '}'
        if label + '\n\n\\begin{multicols}{2}' not in text:
            text = text.replace(label + '\n\n', label + '\n\n\\begin{multicols}{2}\n\\raggedcolumns\n', 1)

# Split the over-dense cross-family table into two scan-friendly full-width tables.
start = text.find(r'\subsection{Cross-family structured comparison}')
if start != -1:
    end_phrase = 'parameter accounting、context evaluation、benchmark harnessが異なるため、数値の横断正規化は行わない。'
    end = text.find(end_phrase, start)
    if end == -1:
        raise SystemExit('could not locate old comparison table terminator')
    end += len(end_phrase)
    text = text[:start] + comparison + text[end:]

# Reader-facing wording must not expose known production vocabulary.
for forbidden in ['accepted Evidence', '本 package', '一次資料として昇格させない', 'coverage を広げる', 'Core v2 Evidence:', 'materiality:']:
    if forbidden in text:
        raise SystemExit(f'forbidden reader-facing production vocabulary remains: {forbidden}')
if re.search(r'(?<![A-Za-z])D0\d{2}(?![A-Za-z0-9])', text):
    raise SystemExit('internal Dxxx Evidence identifier remains in reader source')

if text.count(r'\begin{multicols}{2}') < 6:
    raise SystemExit(f'expected at least 6 two-column flows, found {text.count(r"\\begin{multicols}{2}")}')
if text.count(r'\begin{multicols}{2}') != text.count(r'\end{multicols}'):
    raise SystemExit('unbalanced multicols environments')
for required in [
    'Source-backed Technical Notes / DeepSeek',
    'Source-backed Technical Notes / Qwen',
    'Source-backed Technical Notes / GLM',
    'Source-backed Technical Notes / Kimi',
    '設計とpost-trainingの比較',
    'Distribution / servingと公開境界',
]:
    if required not in text:
        raise SystemExit(f'missing r3 reader surface: {required}')

path.write_text(text, encoding='utf-8')
print('patched', path)
print('multicols flows:', text.count(r'\begin{multicols}{2}'))
