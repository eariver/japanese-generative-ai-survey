from __future__ import annotations

from pathlib import Path
import re

path = Path('surveys/special/SP001/main.tex')
text = path.read_text(encoding='utf-8')

# This temporary script is only valid against the pre-r3 reader source.
if r'\begin{multicols}{2}' in text or 'Source-backed Technical Notes / DeepSeek' in text:
    raise SystemExit('r3 reader source appears already transformed; refusing a second application')

if r'\usepackage{multicol}' not in text:
    needle = r'\usepackage{array}' + '\n'
    if needle not in text:
        raise SystemExit('array package anchor not found')
    text = text.replace(needle, needle + r'\usepackage{multicol}' + '\n', 1)

layout_setup = r'''\setlength{\columnsep}{1.45em}
\setlength{\multicolsep}{0.65em}
'''
if layout_setup.strip() not in text:
    needle = r'\addbibresource{references.bib}' + '\n'
    if needle not in text:
        raise SystemExit('bibliography anchor not found')
    text = text.replace(needle, needle + '\n' + layout_setup, 1)

# Remove known production-facing vocabulary while preserving the public claim.
reader_replacements = {
    'SP001のEvidenceから導ける結論は': '本巻で確認した一次資料から導ける結論は',
    '前5節で確立したevidence-bound claimだけを再構成する': '前5節で一次資料に結び付けて確認した内容だけを再構成する',
    '各familyのaccepted Evidenceから': '各familyについて確認した一次資料から',
    'accepted Evidence': '確認済みの一次資料',
    'verification target': '確認事項',
    'SP001でdistributionを競争力の一部として扱う': '本巻でdistributionを競争力の一部として扱う',
    r'\subsection*{Evidence boundary}': r'\subsection*{確認範囲と主張境界}',
}
for old, new in reader_replacements.items():
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
\setlength{\tabcolsep}{3pt}
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.12\textwidth}>{\raggedright\arraybackslash}p{0.23\textwidth}>{\raggedright\arraybackslash}p{0.31\textwidth}>{\raggedright\arraybackslash}X@{}}
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
\setlength{\tabcolsep}{4pt}
\begin{tabularx}{\textwidth}{@{}>{\raggedright\arraybackslash}p{0.12\textwidth}>{\raggedright\arraybackslash}p{0.43\textwidth}>{\raggedright\arraybackslash}X@{}}
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
\setlength{\tabcolsep}{6pt}

二つの表は順位表ではない。上段は各familyで第一級になった設計問題を、下段はmodel artifactを利用可能にするdistribution/runtimeと公開境界を分離している。parameter accounting、context evaluation、benchmark harnessが異なるため、数値を一つの横断scoreへ正規化しない。
'''

# Replace the previous over-dense five-column comparison table.
comparison_start = text.find(r'\subsection{Cross-family structured comparison}')
comparison_end_phrase = 'parameter accounting、context evaluation、benchmark harnessが異なるため、数値の横断正規化は行わない。'
if comparison_start < 0:
    raise SystemExit('comparison start not found')
comparison_end = text.find(comparison_end_phrase, comparison_start)
if comparison_end < 0:
    raise SystemExit('comparison terminator not found')
comparison_end += len(comparison_end_phrase)
text = text[:comparison_start] + comparison + text[comparison_end:]


def after_label(label: str, insertion: str) -> None:
    global text
    anchor = r'\label{' + label + '}'
    pos = text.find(anchor)
    if pos < 0:
        raise SystemExit(f'label not found: {label}')
    pos += len(anchor)
    text = text[:pos] + '\n\n' + insertion + text[pos:].lstrip('\n')


def next_section_after(offset: int) -> int:
    m = re.search(r'(?m)^\\section\{', text[offset:])
    if not m:
        raise SystemExit('next section not found')
    return offset + m.start()


def wrap_whole_section(label: str, notes: str) -> None:
    global text
    anchor = r'\label{' + label + '}'
    label_pos = text.find(anchor)
    if label_pos < 0:
        raise SystemExit(f'label not found: {label}')
    after = label_pos + len(anchor)
    text = text[:after] + '\n\n' + r'\begin{multicols}{2}' + '\n' + r'\raggedcolumns' + text[after:].lstrip('\n')
    after = text.find(anchor) + len(anchor)
    section_pos = next_section_after(after)
    text = text[:section_pos] + r'\end{multicols}' + '\n\n' + notes.strip() + '\n\n' + text[section_pos:]


# Section 1: two-column framing, full-width chronology, then two-column analysis.
plural_anchor = r'\label{sec:plural}'
plural_pos = text.find(plural_anchor)
if plural_pos < 0:
    raise SystemExit('plural label not found')
after = plural_pos + len(plural_anchor)
text = text[:after] + '\n\n' + r'\begin{multicols}{2}' + '\n' + r'\raggedcolumns' + text[after:].lstrip('\n')
chronology = r'\subsection{Source-specific chronology: 2022--2024}'
chron_pos = text.find(chronology, after)
if chron_pos < 0:
    raise SystemExit('chronology subsection not found')
text = text[:chron_pos] + r'\end{multicols}' + '\n\n' + text[chron_pos:]
center_end = text.find(r'\end{center}', chron_pos)
if center_end < 0:
    raise SystemExit('chronology table end not found')
autocite = r'\autocite{glm130b,baichuan2,deepseekllm,qwen2}'
cite_pos = text.find(autocite, center_end)
if cite_pos < 0:
    raise SystemExit('chronology citation not found')
cite_end = cite_pos + len(autocite)
text = text[:cite_end] + '\n\n' + r'\begin{multicols}{2}' + '\n' + r'\raggedcolumns' + text[cite_end:].lstrip('\n')
# Close Section 1 immediately before Section 2 and add full-width verification layer.
plural_after = text.find(plural_anchor) + len(plural_anchor)
sec2 = next_section_after(plural_after)
text = text[:sec2] + r'\end{multicols}' + '\n\n' + plural_notes.strip() + '\n\n' + text[sec2:]

# Sections 2–5: full-width chapter heading, balanced local two-column narrative,
# then a full-width source-backed verification layer before the next chapter.
wrap_whole_section('sec:deepseek', deepseek_notes)
wrap_whole_section('sec:qwen', qwen_notes)
wrap_whole_section('sec:glm', glm_notes)
wrap_whole_section('sec:kimi', kimi_notes)

# Publication-boundary fail-closed scan on reader-facing source.
for forbidden in [
    'accepted Evidence',
    '本 package',
    '一次資料として昇格させない',
    'coverage を広げる',
    'Core v2 Evidence:',
    'materiality:',
]:
    if forbidden in text:
        raise SystemExit(f'forbidden reader-facing production vocabulary remains: {forbidden}')
if re.search(r'(?<![A-Za-z])D0\d{2}(?![A-Za-z0-9])', text):
    raise SystemExit('internal Dxxx Evidence identifier remains in reader source')

begins = text.count(r'\begin{multicols}{2}')
ends = text.count(r'\end{multicols}')
if begins != 6 or ends != 6:
    raise SystemExit(f'expected exactly 6 balanced multicols flows, got begin={begins}, end={ends}')

for required in [
    'Source-backed verification / 前史のanchor',
    'Source-backed Technical Notes / DeepSeek',
    'Source-backed Technical Notes / Qwen',
    'Source-backed Technical Notes / GLM',
    'Source-backed Technical Notes / Kimi',
    '設計とpost-trainingの比較',
    'Distribution / servingと公開境界',
    r'\section{最終総括: 2026年のfrontierで収束したもの、残った差}',
]:
    if required not in text:
        raise SystemExit(f'missing r3 reader surface: {required}')

path.write_text(text, encoding='utf-8')
print('patched', path)
print('multicols flows:', begins)
print('reader bytes:', len(text.encode('utf-8')))
