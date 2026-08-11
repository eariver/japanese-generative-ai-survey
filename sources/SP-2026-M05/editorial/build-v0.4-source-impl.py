#!/usr/bin/env python3
from __future__ import annotations
import copy, hashlib, json, pathlib, re, shutil

root=pathlib.Path('.')
issue='SP-2026-M05'; slug='2026-M05'
state_path=root/'sources'/issue/'pipeline-state.json'; state=json.load(open(state_path,encoding='utf-8'))
assert state['lifecycle_state']=='VALIDATED_DRAFT'
assert state['gates']['latex_build']=='pending' and state['gates']['visual_review']=='pending' and state['gates']['freeze']=='pending'
cur=state['provenance']['validated_issue_source']; assert cur['source_version']=='v0.3'
cur_manifest=root/cur['path']; assert hashlib.sha256(cur_manifest.read_bytes()).hexdigest()==cur['sha256']
old=json.load(open(cur_manifest,encoding='utf-8')); srcdir=cur_manifest.parent
out=root/'surveys/special'/slug/'revisions/v0.4'; assert not out.exists(); shutil.copytree(srcdir,out)
for name in ['main.pdf','main.log','main.aux','main.bcf','main.run.xml','main.bbl','main.blg','main.fdb_latexmk','main.fls','main.out','main.toc']:
    (out/name).unlink(missing_ok=True)

front=out/'sections/00-frontmatter.tex'; ft=front.read_text(encoding='utf-8')
old_scope='本号は2026年7月を後日確認可能になった一次情報も用いて再構成するRetrospective Specialである。'
assert old_scope in ft
ft=ft.replace(old_scope,'本号は2026年5月を後日確認可能になった一次情報も用いて再構成するRetrospective Specialである。')
chronology=r'''
\medskip
\subsection*{May chronology — 選択済みEvidenceで見る5月}
\addcontentsline{toc}{subsection}{May chronology}
\begingroup
\small
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.08}
\begin{tabularx}{\linewidth}{@{}p{0.12\linewidth}X@{}}
\toprule
日付 & 本号で追う動き \\
\midrule
5月5日 & GPT-5.5 Instant更新。default experienceの更新としてfrontier modelが現れる。\autocite{src-01a8b52eee81} \\
5月7日 & Realtime voice向け新モデル。modelと低遅延配信を一体で読む必要が強まる。\autocite{src-24a3c172de48} \\
5月8日 & Running Codex safely。sandbox・approval・network policyがagent運用のcontrol planeとして明示される。\autocite{src-66be12207714} \\
5月13日 & Codex on Windowsのsandbox設計。host OS固有のisolationが実装課題になる。\autocite{src-4a3442a5ca8c} \\
5月15日 & vLLM v0.21.0。May release seriesの中でserving stackが継続更新される。\autocite{src-80b8d67933c0} \\
5月20日 & OpenAIが離散幾何の予想を反証したmodel事例を公表。benchmark外のcapability評価が論点になる。\autocite{src-1c93d6c1c725} \\
5月28日 & AnthropicがClaude Opus 4.8を公表。coding・agentic／long-running work向けの更新として位置付ける。\autocite{src-f6aa679babd7} \\
5月29日 & FlashInfer v0.6.12とthird-party evaluation playbook。runtime最適化と評価方法が同じ月末に前景化する。\autocite{src-74a7052acd7a,src-8c84b8422093} \\
\bottomrule
\end{tabularx}
\endgroup
\smallskip
\noindent{\footnotesize\color{SurveyMuted}日付は本号の選択済み一次資料で日単位に確認できたEventのみを掲載する。月精度のindex項目は日付を補完していない。}
'''
assert '\\tableofcontents' in ft
ft=ft.replace('\\tableofcontents','\\tableofcontents\n'+chronology,1)
front.write_text(ft,encoding='utf-8')

main=out/'main.tex'; mt=main.read_text(encoding='utf-8')
pattern=re.compile(r'\\clearpage\n(\\section\{)')
counter={'n':0}
def repl(m):
    counter['n']+=1
    return m.group(0) if counter['n']==1 else r'\Needspace{0.42\textheight}'+'\n'+r'\bigskip'+'\n'+m.group(1)
mt=pattern.sub(repl,mt); assert counter['n']==6, counter
mt=mt.replace(r'\clearpage'+'\n'+r'\input{final-synthesis/70-retrospective-synthesis}',r'\Needspace{0.40\textheight}'+'\n'+r'\bigskip'+'\n'+r'\input{final-synthesis/70-retrospective-synthesis}',1)
mt=mt.replace(r'\clearpage'+'\n'+r'\printbibliography[title={References / Source Notes}]',r'\bigskip'+'\n'+r'\printbibliography[title={References / Source Notes}]',1)
main.write_text(mt,encoding='utf-8')

replacements={
 'frontier-models-may.tex':{
  'GPT-5.5 Instant: smarter, clearer, and more personalized':'GPT-5.5 Instant — default experienceの更新',
  'Anthropic May 2026 technical releases':'Anthropic — Claude Opus 4.8とMay releases',
  'Gemini API May 2026 lifecycle':'Gemini API — May lifecycle',
  'Google DeepMind May 2026 releases':'Google DeepMind — May releases',
  'Advancing voice intelligence with new models in the API':'OpenAI Voice API — new realtime models',
  'Alibaba Model Studio May 2026 model lifecycle':'Alibaba Model Studio — May lifecycle',
  'How OpenAI delivers low-latency voice AI at scale':'OpenAI Voice — low-latency serving'},
 'agents-runtime-may.tex':{
  'Building a safe, effective sandbox to enable Codex on Windows':'Codex on Windows — sandbox設計',
  'Kimi Code CLI May 2026 lifecycle':'Kimi Code CLI — May lifecycle',
  'Mistral May 2026 technical releases':'Mistral — MCP・workflow・remote agents',
  'Agentic AI Workload Characteristics':'Agentic Workloads — repeated callsと成長するcontext'},
 'inference-serving-may.tex':{
  'vllm-project/vllm May 2026 release series':'vLLM — May release series',
  'sgl-project/sglang May 2026 release series':'SGLang — May release series',
  'Release v0.6.12':'FlashInfer v0.6.12',
  'Adaptive KV Cache Reuse for Fast Long-Context LLM Serving':'CacheTune — adaptive KV cache reuse',
  'ReMoE: Boosting Expert Reuse through Router Fine-Tuning in Memory-Constrained MoE LLM Inference':'ReMoE — memory-constrained MoEのexpert reuse'},
 'agent-safety-security-may.tex':{
  'From Prompt Injection to Persistent Control: Defending Agentic Harness Against Trojan Backdoors':'ClawTrojan — prompt injectionからpersistent controlへ',
  'Hijacking Agent Memory: Stealthy Trojan Attacks Through Conversational Interaction':'MemPoison — conversational memory poisoning',
  'Relevance as a Vulnerability: How Web Retrieval Degrades Safety Alignment in LLM Agents':'Retrieval Relevance — safety alignmentとのずれ',
  'Send a SCOUT First: Pre-hoc Reasoning for Adaptive Detector Allocation in Prompt-Injection Defense':'SCOUT — adaptive detector allocation'},
 'capability-evaluation-may.tex':{
  'An OpenAI model has disproved a central conjecture in discrete geometry':'Discrete geometry — benchmark外の研究成果',
  'A shared playbook for trustworthy third party evaluations':'Third-party evaluation — trustworthy evaluation playbook'},
 'paper-watch-may.tex':{
  'AgenticVBench: Can AI Agents Complete Real-World Post-Production Tasks?':'AgenticVBench — real-world post-production評価',
  'Identifying and Mitigating Systemic Measurement Bias in Production LLM Inference Benchmarks':'Measurement Bias — production inference benchmark',
  'Representation Forcing for Bottleneck-Free Unified Multimodal Models':'Representation Forcing — unified multimodal'}
}
changed=[]
for fn,mapping in replacements.items():
    p=out/'layout-bodies'/fn; text=p.read_text(encoding='utf-8')
    for before,after in mapping.items():
        needle='\\subsection{'+before+'}'
        assert needle in text, (fn,before)
        text=text.replace(needle,'\\subsection{'+after+'}',1); changed.append((fn,before,after))
    if fn=='paper-watch-may.tex':
        text=text.replace('AgenticVBench、production inference benchmarkのmeasurement bias、Representation Forcing。','AgenticVBench、推論benchmarkの測定bias、Representation Forcing。',1)
    p.write_text(text,encoding='utf-8')
assert len(changed)==22, len(changed)

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
marker=root/'sources'/issue/'editorial/layout-revision-v0.4.json'; marker.parent.mkdir(parents=True,exist_ok=True)
marker_data={
 'schema_version':'1.0','issue_id':issue,'revision':'v0.4','from_source_version':'v0.3',
 'constraints':{'new_external_evidence_allowed':False,'selected_evidence_only':True,'reader_content_changed':True},
 'changes':['Correct retrospective scope month from July to May.','Add a reader-facing May chronology using only already-selected Evidence with day-level confirmed Events.','Replace forced later chapter/reference page breaks with adaptive spacing.','Shorten reader-facing two-column subsection headings; formal artifact titles remain in Technical Notes.','Do not add final-synthesis subsection Needspace guards.'],
 'qa_targets':['remove structural blank tails at chapter transitions','retain first Feature on a fresh page','eliminate Underfull hbox warnings from long English headings','keep visual_review and freeze pending']}
marker.write_text(json.dumps(marker_data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

new=copy.deepcopy(old); new['source_version']='v0.4'; new['status']='VALIDATED_BALANCED_ADAPTIVE_CHRONOLOGY_REVISION'
new['derivation']='Reader-facing revision of v0.3 using only already-selected Evidence: correct May scope wording, add a compact selected-Evidence May chronology, shorten display headings, and relax later chapter/reference page breaks. Accepted Evidence set and formal Technical Notes artifact titles are unchanged.'
new['basis']=copy.deepcopy(old.get('basis') or {}); new['basis']['previous_source_manifest_path']=cur['path']; new['basis']['previous_source_manifest_sha256']=cur['sha256']
new['layout']=copy.deepcopy(old.get('layout') or {}); new['layout']['chapter_start_policy']='first Feature on new page; later chapters Needspace(0.42 textheight)'; new['layout']['final_synthesis_start_policy']='Needspace(0.40 textheight)'; new['layout']['references_start_policy']='continue after final synthesis without forced clearpage'
new['layout_revision']={'from_source_version':'v0.3','reader_content_changed':True,'new_external_evidence':False,'selected_evidence_only':True,'adaptive_chapter_starts':True,'may_chronology_added':True,'scope_month_corrected':True,'short_display_headings':True,'final_synthesis_subsection_needspace_baselines':0}
new['main_tex']={'path':'main.tex','sha256':sha(main)}; new['frontmatter']={'path':'sections/00-frontmatter.tex','sha256':sha(front)}
for item in new.get('article_layout_bodies',[]):
    p=out/item['path']; item['sha256']=sha(p); item['v0_4_display_heading_revision']=True
manifest=out/'source-manifest.json'; manifest.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); msha=sha(manifest)
state.setdefault('provenance_history',{}).setdefault('validated_issue_source',[]).append(copy.deepcopy(cur))
state['provenance']['validated_issue_source']={'path':manifest.relative_to(root).as_posix(),'sha256':msha,'source_version':'v0.4','layout_mode':'balanced-multicol-adaptive-spacing-with-may-chronology','layout_revision_path':marker.relative_to(root).as_posix(),'layout_revision_sha256':sha(marker)}
state['provenance']['reader_layout_revision']={'source_version':'v0.4','layout_revision_path':marker.relative_to(root).as_posix(),'layout_revision_sha256':sha(marker),'reason':'Pre-Human render QA: fix May scope typo, fill TOC tail with selected-Evidence chronology, remove forced chapter whitespace, and shorten pathological two-column headings.'}
state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'source_manifest':manifest.as_posix(),'source_manifest_sha256':msha,'heading_changes':len(changed)},ensure_ascii=False))
