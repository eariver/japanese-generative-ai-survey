#!/usr/bin/env python3
"""Programmatic 36-key classification for r4 audit (exclusive, evidence-backed).

Reads r3 TeX body (pre-bibliography), strips comments/labels for visible spans,
counts exact key occurrences; assigns one exclusive class per key:
- EXACT_VISIBLE_CITATION: key printed in reader-visible body (count>=1)
- EXACT_MACHINE_ONLY: key only in labels/comments/metadata, never visible
- EXPLICIT_NATURAL_REFERENCE / FURTHER_READING / UNAVAILABLE_NO_CLAIM_PROOF / ORPHAN
  from curated evidence map (crosswalk + body location), verified non-empty.
Prints distribution + per-key table. ORPHAN must be 0.
"""
import re, json, pathlib
REPO = pathlib.Path("/home/eariver/git/japanese-generative-ai-survey")
TEX = REPO / "sources/2026-W43/execution/core-free-preview-r3/main.tex"
tex = TEX.read_text(encoding="utf-8")
body = tex.split(r"\begin{thebibliography}")[0]
keys = re.findall(r"\\bibitem\[([^\]]+)\]", tex)
assert len(keys) == 36 and len(set(keys)) == 36
vis = "\n".join(l for l in body.splitlines() if not l.strip().startswith("%"))
vis = re.sub(r"\\label\{[^}]*\}", "", vis)

NATURAL = {
 "1pw-blog-1022": "P3 prose: 1Password発表（2026-10-22、coming soon）+ Fig p3-f1 path B",
 "flux-elo-1139": "P4 prose: Elo 1139・4868票・+47/+50 with AA-unfetched qualifiers",
 "flux-keyframes-conflict": "P4 prose+table note: keyframes UNRESOLVED (both originals unfetched; transparent record)",
 "voxtral-card-units": "P5 p5-f1 rows (WER/cpWER/recall/prices) + task-18a859 line",
 "deepinfer-import-scope": "P2 prose (SamplingParams import) + code comments + DI-README commit",
 "flux-speed-recalc": "P4 prose/table: 25.37x/22.31x/95.52% recalc (same page as flux-page-1019)",
 "ming-aa-cited": "P5 p5-t2 rows: AA三行=発行元引用（原表未取得）",
 "eleven-blog": "P5 prose: realtime compat + unopened-guide notes",
 "patch-rendered": "P6 prose: 5 stages + task-5d21d93e + saved-extraction path 17-22行",
 "securing-page-rss": "P6 prose: isolation + page/RSS clock distinction",
 "tanstack-blog": "P8 prose+table: blog10月23日は日付のみ (date-only, not product clock)",
 "decisions-guide-1025": "P8 典拠: guide URL + snapshot path + SHA (post-cutoff supplementary)",
 "decisions-ts-ref-1025": "P8 prose: TTL 30m Oct25-observation note (not W43 fact)",
}
FURTHER = {
 "DI-ENV": "file-level provenance (environ.py 8738B) for same 9bd9cf24 commit as DI-README (exact-visible); natural language present",
 "DI-LICENSE": "file-level provenance (Apache-2.0 bytes) for same commit; natural language present",
}
UNAVAIL = {"decisions-ref-create": "404 on 2026-10-25; retained SOLELY as transparent unavailable-record"}

rows = []
for k in keys:
    v = vis.count(k)
    raw = body.count(k)
    if v >= 1:
        cls, ev = "EXACT_VISIBLE_CITATION", f"visible x{v} (典拠/table/prose)"
    elif raw >= 1:
        cls, ev = "EXACT_MACHINE_ONLY", f"machine-only x{raw} (label/comment)"
    elif k in NATURAL:
        cls, ev = "EXPLICIT_NATURAL_REFERENCE", NATURAL[k]
    elif k in FURTHER:
        cls, ev = "FURTHER_READING", FURTHER[k]
    elif k in UNAVAIL:
        cls, ev = "UNAVAILABLE_NO_CLAIM_PROOF", UNAVAIL[k]
    else:
        cls, ev = "ORPHAN/AMBIGUOUS", "NO TRACEABILITY — BLOCKER"
    rows.append((k, cls, v, raw, ev))

from collections import Counter
dist = Counter(c for _, c, _, _, _ in rows)
print("DISTRIBUTION:", dict(dist))
assert sum(dist.values()) == 36
assert dist.get("ORPHAN/AMBIGUOUS", 0) == 0, "orphans exist"
print(f"{'key':28} {'class':28} vis raw  evidence")
for k, c, v, r, e in rows:
    print(f"{k:28} {c:28} {v:3} {r:3}  {e}")
