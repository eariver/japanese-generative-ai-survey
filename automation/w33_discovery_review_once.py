#!/usr/bin/env python3
from __future__ import annotations
import json,re
from pathlib import Path

ROOT=Path('.').resolve(); ISSUE='2026-W33'
SEED=ROOT/f'sources/{ISSUE}/source-intake-v2/fresh-non-x-screening-seed/screening-index.jsonl'
OUT=ROOT/f'sources/{ISSUE}/source-intake-v2/fresh-discovery-review.json'
MD=ROOT/f'sources/{ISSUE}/source-intake-v2/fresh-discovery-review.md'

LANES={
'A':['reasoning','foundation model','language model','llm','mixture of experts','moe','long context'],
'B':['agent','coding','code generation','computer use','tool use','swe','terminal','browser'],
'C':['multimodal','vision-language','vision language','vlm','image understanding','video understanding'],
'D':['image generation','text-to-image','image editing','diffusion','flow matching','image synthesis'],
'E':['video generation','text-to-video','image-to-video','video editing','video synthesis','world model'],
'F':['speech','audio','music','text-to-speech','tts','voice','sound generation'],
'G':['open weight','open-weight','quantization','quantized','gguf','local inference','consumer gpu'],
'H':['inference','serving','throughput','latency','kernel','speculative decoding','kv cache','cuda','distributed'],
'I':['memory','retrieval','rag','multi-agent','multi agent','context engineering'],
'J':['benchmark','evaluation','eval','leaderboard','judge model'],
'K':['safety','security','cyber','jailbreak','alignment','red team','vulnerability'],
'L':['robotics','3d generation','simulation','emerging','scientific discovery'],
}

STOP={'the','and','for','with','from','using','via','towards','toward','based','model','models','learning','large','language','ai','a','an','of','to','in','on','is','are','we','by'}

def compact(r):
 return {'screening_id':r.get('screening_id'),'source_type':r.get('source_type'),'collector_id':r.get('collector_id'),'collector_run_id':r.get('collector_run_id'),'observed_at':r.get('observed_at'),'published_at':r.get('published_at'),'title':r.get('title'),'locator':r.get('locator'),'raw_paths':r.get('raw_paths'),'summary_excerpt':(r.get('summary_text') or '')[:700],'metadata':r.get('metadata') or {}}

def score(text,terms):
 low=text.lower(); s=0
 for t in terms:
  n=low.count(t); s+=min(n,3)*(5 if ' ' in t else 2)
 return s

def main():
 rows=[json.loads(x) for x in SEED.read_text(encoding='utf-8').splitlines() if x.strip()]
 nonpaper=[compact(r) for r in rows if r.get('source_type')!='paper']
 papers=[r for r in rows if r.get('source_type')=='paper']
 top={}
 for lane,terms in LANES.items():
  scored=[]
  for r in papers:
   text=f"{r.get('title','')} {r.get('summary_text','')}"
   s=score(text,terms)
   # reward dense title signal rather than only abstract repetition
   s+=2*score(r.get('title',''),terms)
   if s: scored.append((s,r))
  scored.sort(key=lambda z:(-z[0],str(z[1].get('published_at') or ''),str(z[1].get('screening_id'))))
  top[lane]=[{**compact(r),'lane_score':s} for s,r in scored[:18]]
 # generic novelty titles: favor papers whose title contains concrete systems/model/eval terms and avoid obvious broad surveys
 generic_terms=['agent','reasoning','multimodal','video','image','audio','speech','inference','serving','memory','retrieval','benchmark','evaluation','safety','security','quantization','diffusion','tool','code','coding']
 generic=[]
 for r in papers:
  t=r.get('title',''); s=score(t,generic_terms)
  if s and not re.search(r'\b(survey|review|overview)\b',t,re.I): generic.append((s,r))
 generic.sort(key=lambda z:(-z[0],str(z[1].get('published_at') or ''),str(z[1].get('screening_id'))))
 payload={'schema_version':'1.0','issue_id':ISSUE,'record_count':len(rows),'nonpaper_count':len(nonpaper),'paper_count':len(papers),'legacy_w33_source_intake_used':False,'all_nonpaper':nonpaper,'paper_top_by_lane':top,'paper_generic_top':[{**compact(r),'score':s} for s,r in generic[:60]],'notes':['Discovery review aid only; not Screening authority.','Every row derives from the fresh W33 v2 seed.','Paper ranking is deterministic lexical prioritization for ChatGPT semantic review.']}
 OUT.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 lines=[f'# {ISSUE} fresh Discovery review', '',f'- fresh records: {len(rows)}',f'- non-paper: {len(nonpaper)}',f'- papers: {len(papers)}','- legacy W33 intake used: **no**','', '## Non-paper candidates']
 for r in nonpaper:
  lines += [f"- **{r['title']}** | {r['source_type']} | {r.get('published_at')} | {r['screening_id']}",f"  - {r['locator']}",f"  - {r['summary_excerpt'][:350].replace(chr(10),' ')}"]
 for lane,items in top.items():
  lines += ['',f'## Paper lane {lane}']
  for r in items: lines += [f"- [{r['lane_score']}] **{r['title']}** | {r.get('published_at')} | {r['screening_id']}",f"  - {r['locator']}",f"  - {r['summary_excerpt'][:320].replace(chr(10),' ')}"]
 MD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
 print(json.dumps({'records':len(rows),'nonpaper':len(nonpaper),'papers':len(papers),'out':str(OUT.relative_to(ROOT))},indent=2))
if __name__=='__main__': main()
