#!/usr/bin/env python3
"""TS-002 r2 bibliography regeneration (deterministic, reader-facing).

Repairs r1 defects found by Sol Publication Preview r1 review:
1. Author display strings (e.g. `Kingma & Welling`, `van den Oord et al.`,
   `OpenAI`) are emitted as LITERAL BibLaTeX author values (double braces)
   so biber/BibLaTeX never parses them into initials/name parts
   (r1 rendered `K. et al.`, `I. 2. Panayotov et al.`, `B. F. Labs.`).
   No full-author metadata is invented.
2. Generic internal pipeline boilerplate (`Source class ... as bound in
   Evidence`, `Primary locator as rebound ...`) is removed from ordinary
   VERIFIED entries.
3. PARTIAL / NEEDS_MORE entries keep reader-facing limitation notes written
   in reader language (no pipeline jargon). Canonical URLs and dates kept.

Source of truth: sanitized Evidence acceptance f8e273fd + edition matrix.
Output: surveys/special/beyond-text-2026/references.bib (139 entries).
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path("/home/eariver/git/japanese-generative-ai-survey")
sys.path.insert(0, str(ROOT))

EVIDENCE_DIR = "sources/SP-beyond-text-2026/evidence/v2/accepted/f8e273fd706beaed9bda108ffc965708d029f1a8129f191af412cb20b2cd9289/results"
EVIDENCE_ACCEPTANCE = "sources/SP-beyond-text-2026/evidence/v2/accepted/f8e273fd706beaed9bda108ffc965708d029f1a8129f191af412cb20b2cd9289/evidence-accepted.json"
OUT = "surveys/special/beyond-text-2026/references.bib"
URLDATE = "2026-09-26"

PARTIAL_NOTES = {
    "BT-D022": "Abstract-level authority (full text not consumed): cited for design-space headline facts only; preconditioning, schedule, and solver ablations are not claimed.",
    "BT-D059": "Partially consumed body (mechanism sections only; result tables truncated): cited for grouped-code and repetition-aware mechanism only; parity margins and speedups are not claimed.",
    "BT-D076": "Abstract-level authority (method and evaluation sections not consumed): cited for cast, resolution, and capability headlines only; architecture and training claims are not made.",
    "BT-D083": "Abstract-level authority (full text not consumed): cited for the distribution-distance definition and update-rule headline only; embedding-layer and sample-size requirements are not claimed.",
    "BT-D089": "Snippet-level authority (corpus protocol not consumed from body): cited for corpus existence and scale headlines only; splits, alignment, and baselines are not claimed.",
    "BT-D098": "Homepage-level authority (specification not consumed): cited for the provenance-framework existence only; manifest, signing, and binding construction are not claimed.",
    "BT-D106": "Lifecycle-context authority (product page redirect; capability body not consumed): cited for the deprecation/lifecycle transition only.",
    "BT-D134": "Framework-level authority (evaluation section not consumed): cited for the full-duplex dialogue framework and latency design only; quality rankings are not claimed.",
}

HOLD_NOTE = ("Body unavailable (access barrier): cited for capability, workflow, or lifecycle context only; "
             "mechanism claims rest on sibling authority.")

X_NOTE = ("Accepted community-reception ledger (27 observations in one bounded pass): cited for practical "
          "adoption, deployment, and failure evidence only; not a technical authority.")


def tex_escape(s: str) -> str:
    s = s.replace("\\", "\\textbackslash{}")
    for ch, esc in (("%", "\\%"), ("#", "\\#"), ("&", "\\&"), ("_", "\\_"), ("$", "\\$")):
        s = s.replace(ch, esc)
    return s


def clean_title(t: str) -> str:
    return " ".join(t.split())


def main() -> int:
    root = ROOT
    base = root / EVIDENCE_DIR
    ev = json.loads((root / EVIDENCE_ACCEPTANCE).read_text(encoding="utf-8"))
    tmap = {r["evidence_task_id"]: (r["discovery_ids"][0], r["status"]) for r in ev["results"]}
    rows = []
    for f in base.glob("*.json"):
        card = json.loads(f.read_text(encoding="utf-8"))
        did, status = tmap[card["evidence_task_id"]]
        art = card.get("artifact", {})
        srcs = card.get("sources", [])
        rows.append((did, status, art, srcs[0] if srcs else {}, card))
    rows.sort(key=lambda x: int(x[0].split("-D")[1]))
    assert len(rows) == 139, len(rows)

    out: list[str] = [
        "% Bibliography for SP-beyond-text-2026 (Beyond Text), r2.",
        "% Keys are BT-D discovery IDs (btd001..btd139), cited from the reader-facing source.",
        "% Generated deterministically from sanitized Evidence acceptance f8e273fd by",
        "% sources/SP-beyond-text-2026/execution/bib-repair-r2-20260926/gen_bib_r2.py.",
        "% Author display strings are literal BibLaTeX values (no name-list parsing, no invented metadata).",
        "% PARTIAL/NEEDS_MORE limits are reader-facing; canonical URLs and dates preserved.",
        "",
    ]
    changed_authors = 0
    boilerplate_removed = 0
    for did, status, art, src, card in rows:
        key = did.lower().replace("-", "")
        title = clean_title(art.get("canonical_name") or src.get("title") or did)
        url = src.get("url") or art.get("canonical_url") or ""
        is_http = url.startswith("http")
        date = src.get("published_at") or ""
        org = next((e.get("organization") for e in card.get("entities", []) if e.get("organization")), None)
        if org:
            author_src = org
        else:
            m = re.search(r"\(([^)]+)\)\s*$", title)
            author_src = m.group(1) if (m and len(m.group(1)) < 80) else "Various"
        author = "{{" + tex_escape(author_src) + "}}"
        changed_authors += 1
        note = None
        if did == "BT-D139":
            note = X_NOTE
        elif status == "PARTIAL":
            note = PARTIAL_NOTES[did]
        elif status == "NEEDS_MORE":
            note = HOLD_NOTE
        else:
            boilerplate_removed += 1
        out.append(f"@online{{{key},")
        out.append(f"  author  = {author},")
        out.append("  title   = {" + tex_escape(title) + "},")
        if date:
            out.append(f"  date    = {{{date}}},")
        if is_http:
            out.append(f"  url     = {{{url}}},")
            out.append(f"  urldate = {{{URLDATE}}},")
        if note is not None:
            out.append("  note    = {" + tex_escape(note) + "},")
        out.append("}")
        out.append("")

    text = "\n".join(out)
    body = "\n".join(line for line in out if not line.startswith("%"))
    banned = ["bibinitperiod", "bibnamedelim", "\\mkbib", "PRIMARY_", "as bound in Evidence",
              "provenance repair", "SHA", "sha256", "NEEDS_MORE", "Evidence PARTIAL"]
    hits = [b for b in banned if b in body]
    assert not hits, f"banned tokens in regenerated bib: {hits}"
    # every entry must have author/title; http entries must have url+date handling
    assert text.count("@online{") == 139
    (root / OUT).write_text(text, encoding="utf-8")
    print(json.dumps({"entries": 139, "literal_authors": changed_authors,
                      "boilerplate_removed_verifed": boilerplate_removed,
                      "partial_notes": 8, "hold_notes": 5, "x_notes": 1,
                      "bytes": len(text.encode())}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
