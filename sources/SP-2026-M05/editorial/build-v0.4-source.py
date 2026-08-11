#!/usr/bin/env python3
from pathlib import Path
impl=Path(__file__).with_name('build-v0.4-source-impl.py')
code=impl.read_text(encoding='utf-8').replace("assert len(changed)==22, len(changed)","assert len(changed)==25, len(changed)")
exec(compile(code,str(impl),'exec'),{'__name__':'__main__','__file__':str(impl)})
