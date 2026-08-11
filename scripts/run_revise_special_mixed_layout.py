#!/usr/bin/env python3
"""Execute mixed-layout Special revision with reader-facing text normalization.

Editorial synthesis artifacts may retain review-context wording for provenance. This
runner removes only known internal-review references before rendering, then delegates
all validation, Evidence binding, source copying, and state transitions to the
canonical mixed-layout revision builder.
"""

from __future__ import annotations

import re

from scripts import revise_special_mixed_layout as revision


def reader_normalize(text: str) -> str:
    text = text.replace("本Evidence set", "本号で確認した一次資料群")
    text = re.sub(r"Issue #\d+の反省を踏まえ、", "", text)
    return text


_original_render = revision.render_synthesis


def normalized_render(theme, package, bib_map):
    normalized = dict(theme)
    normalized["title"] = reader_normalize(str(theme.get("title") or ""))
    normalized["intro"] = reader_normalize(str(theme.get("intro") or ""))
    rows = []
    for row in theme.get("rows") or []:
        item = dict(row)
        item["dimension"] = reader_normalize(str(row.get("dimension") or ""))
        item["observation"] = reader_normalize(str(row.get("observation") or ""))
        rows.append(item)
    normalized["rows"] = rows
    return _original_render(normalized, package, bib_map)


revision.render_synthesis = normalized_render


if __name__ == "__main__":
    raise SystemExit(revision.main())
