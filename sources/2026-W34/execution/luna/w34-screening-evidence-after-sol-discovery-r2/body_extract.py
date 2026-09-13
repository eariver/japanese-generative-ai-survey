#!/usr/bin/env python3
"""Body text extraction + section parsing for evidence consumption."""
from __future__ import annotations
import re, html as ihtml
from pathlib import Path

WS = re.compile(r"\s+")

def html_to_text(data: bytes, limit: int = 60000) -> str:
    t = data.decode("utf-8", errors="replace")
    t = re.sub(r"(?is)<(script|style|noscript|svg|nav|footer|header)\b.*?</\1\s*>", " ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = ihtml.unescape(t)
    t = WS.sub(" ", t).strip()
    return t[:limit]

def split_sentences(text: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])", text)
    return [p.strip() for p in parts if len(p.strip()) > 40]

def score_sent(sent: str, keywords: list[str]) -> int:
    s = sent.lower()
    return sum(1 for k in keywords if k.lower() in s)

def top_sentences(text: str, keywords: list[str], n: int = 6, min_len: int = 60, max_len: int = 600) -> list[str]:
    cands = []
    for s in split_sentences(text):
        if not (min_len <= len(s) <= max_len):
            continue
        sc = score_sent(s, keywords)
        if sc > 0:
            cands.append((sc, s))
    cands.sort(key=lambda x: -x[0])
    out, seen = [], set()
    for _, s in cands:
        key = s[:80].lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(s)
        if len(out) >= n:
            break
    return out

SECTION_HEADS = ["abstract", "introduction", "method", "approach", "experiment", "evaluation",
                 "results", "discussion", "limitation", "conclusion", "related work",
                 "implementation", "setup", "benchmark", "ablation", "reproducibility",
                 "code availability", "data availability", "acknowledg", "references"]

def parse_sections(text: str) -> dict[str, str]:
    """Split arXiv HTML/plain text into coarse sections by numbered headings."""
    lines = text.split("\n")
    # arXiv HTML -> single line; fall back to whole-text buckets
    if len(lines) < 20:
        return {"full": text}
    secs: dict[str, list[str]] = {}
    cur = "front"
    for ln in lines:
        s = ln.strip()
        m = re.match(r"^(\d+(?:\.\d+)*)\s+([A-Z][A-Za-z ,\-/&()]{3,80})$", s)
        if m:
            cur = f"{m.group(1)} {m.group(2)}"
            secs.setdefault(cur, [])
        else:
            secs.setdefault(cur, []).append(s)
    return {k: "\n".join(v) for k, v in secs.items()}

def section_bucket(sections: dict[str, str], wants: list[str]) -> str:
    out = []
    for name, body in sections.items():
        nl = name.lower()
        if any(w in nl for w in wants):
            out.append(body)
    return "\n".join(out)
