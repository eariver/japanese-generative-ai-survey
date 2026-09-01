#!/usr/bin/env python3
"""Fill Special Japanese Technical Notes only from reviewed source-bound overrides.

Missing reader-facing summaries are an editorial error. This path deliberately has
no generic fallback: if an Evidence claim, limitation, or event fact has not been
reviewed, the revision must stop before publication-facing TeX is generated.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

# This helper is also invoked directly by a generated git pre-commit hook. In that
# mode Python's import root is ``scripts/`` rather than the control checkout root.
# Add the repository/control root deterministically before importing the package.
_control_root = Path(__file__).resolve().parents[1]
if str(_control_root) not in sys.path:
    sys.path.insert(0, str(_control_root))

from scripts import special_reader_notes_ja as notes


def load_json(path: Path) -> dict[str, Any]:
    value=json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(value,dict):
        raise ValueError(f'{path}: expected object')
    return value


def run(repo_root: Path, issue_id: str, summary_path: Path, overrides_dir: Path) -> dict[str, Any]:
    repo_root=repo_root.resolve()
    summary_path=(repo_root/summary_path).resolve() if not summary_path.is_absolute() else summary_path.resolve()
    overrides_dir=(repo_root/overrides_dir).resolve() if not overrides_dir.is_absolute() else overrides_dir.resolve()
    doc=load_json(summary_path)
    if doc.get('issue_id') != issue_id:
        raise ValueError('summary issue mismatch')

    index: dict[tuple[str,str,str],dict[str,Any]]={}
    artifact_by_task: dict[str,str]={}
    for record in doc.get('records') or []:
        task=record['evidence_task_id']; artifact_by_task[task]=record['artifact_name']
        for key,kind in (('claims','claim'),('limitations','limitation'),('event_facts','event')):
            for item in record.get(key) or []:
                index[(task,kind,item['item_id'])]=item

    applied=0
    if overrides_dir.is_dir():
        for path in sorted(overrides_dir.glob('part-*.json')):
            part=load_json(path)
            if part.get('issue_id') != issue_id:
                raise ValueError(f'{path}: issue mismatch')
            for tr in part.get('translations') or []:
                key=(tr.get('evidence_task_id'),tr.get('kind'),tr.get('item_id'))
                item=index.get(key)
                if item is None:
                    raise ValueError(f'{path}: unknown translation target {key}')
                if tr.get('source_text_sha256') != item.get('source_text_sha256'):
                    raise ValueError(f'{path}: source hash mismatch for {key}')
                text=tr.get('text_ja')
                if not isinstance(text,str) or not text.strip():
                    raise ValueError(f'{path}: empty Japanese translation for {key}')
                item['text_ja']=text.strip(); applied+=1

    missing=[]
    for (task,kind,item_id), item in index.items():
        if not str(item.get('text_ja') or '').strip():
            missing.append({
                'evidence_task_id':task,
                'artifact_name':artifact_by_task.get(task,task),
                'kind':kind,
                'item_id':item_id,
                'evidence_class':item.get('evidence_class',''),
            })
    if missing:
        preview=', '.join(f"{m['artifact_name']}:{m['kind']}:{m['item_id']}" for m in missing[:8])
        suffix='' if len(missing) <= 8 else f' (+{len(missing)-8} more)'
        raise ValueError(
            f'missing reviewed Japanese Technical Notes summaries: {len(missing)} item(s): {preview}{suffix}'
        )

    doc['status']='READY'
    notes.verify_source_text(repo_root,issue_id,doc)
    errors=notes.validate_summary(doc)
    if errors:
        raise ValueError(f'reader notes validation failed: {errors}')
    notes.write_json(summary_path,doc)
    return {
        'schema_version':'1.0','issue_id':issue_id,'status':'READY',
        'translation_override_count':applied,'fallback_count':0,'item_count':len(index),
        'missing_summary_policy':'fail-closed',
    }


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo-root',default='.')
    p.add_argument('--issue-id',required=True)
    p.add_argument('--summary',required=True)
    p.add_argument('--overrides-dir',required=True)
    a=p.parse_args()
    report=run(Path(a.repo_root),a.issue_id,Path(a.summary),Path(a.overrides_dir))
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
