# 2026-W32 Editorial Polish v0.1

Status: editorial polish applied; full-issue rebuild pending CI/local source-tree availability  
Date: 2026-08-10

## Purpose

This pass changes presentation and readability only. It does not alter candidate selection, evidence classification, chronology, or claim authority.

## Cover

The cover now supports issue-specific editorial framing through reusable template metadata.

W32 headline:

> **モデルの外側へ**

Deck:

> Astraは研究成果を検査可能なartifactへ、MiniMax H3はlocal / serving ecosystemへ、Safetyはharness・serving・policyへ。W32は、生成AIの評価軸がmodel単体からsystem全体へ広がった週だった。

Anchor stories:
- Astra
- MiniMax H3
- Safety beyond the model

The headline was derived from the completed body rather than used to drive candidate selection.

## Cover typography validation

A standalone cover smoke test was built with LuaLaTeX after the template changes.

Validated:
- A4 output;
- no TeX error;
- issue headline/deck/anchors render correctly;
- the previous awkward `Sur-vey` title break was removed by reducing the generic cover title size;
- the anchor line was shortened to prevent an isolated trailing word;
- metadata columns were widened/rebalanced.

The smoke test does not replace the full-issue build gate.

## Front matter

`This Week in AI` was polished so each item states a clearer technical proposition:

1. scientific reasoning: score -> inspectable artifact;
2. open/local AI: post-release ecosystem matters;
3. safety: boundary extends beyond the checkpoint;
4. agents: competition extends to product/harness/evaluation;
5. memory: persistent state and exact retrieval should be separated.

No new evidence was introduced.

## Body prose

Targeted edits were applied where Japanese readability was weaker than the rest of the issue.

### Agent & Coding
- title changed to emphasize the three layers outside the model;
- sentence structure made more Japanese-first while retaining source terminology;
- `governance question` -> `governanceの問い`;
- evaluation language made more direct;
- no chronology or source claim changed.

### X Community Watch
- clarified that technical fact confirmation remains with primary sources;
- normalized spacing/technical phrasing;
- retained the distinction between social observation and capability evidence.

### Source Notes
- clarified that four evidence-display classes are intentionally distinct;
- made the legend more readable without changing evidence policy.

## Template / future-issue improvement

A reusable `\surveycoverstory{headline}{deck}{anchors}` interface was added to `jgaisurvey.sty`.

This avoids hard-coding W32 copy inside the common style while allowing future issues to choose their cover only after article construction.

## Editorial Style Guide

`docs/editorial-style-guide.md` was created from lessons learned in the first complete issue.

It formalizes:
- Japanese/English technical register;
- article structure;
- informative heading style;
- cover/frontmatter timing;
- chronology vs trend chronology;
- vendor/author/community/editorial claim classes;
- benchmark comparison boundaries;
- open-weight/local-AI wording;
- security/threat-model wording;
- paper/simulation treatment;
- X Community Watch purpose;
- Late Breaking behavior;
- page-budget policy;
- final editorial gate.

## Build visibility

The current GitHub connector returns no combined status entries for the latest push and does not provide a push-run listing in this workflow. The runtime also cannot clone the public repository because outbound DNS is unavailable.

Therefore:
- the reusable cover change has been independently LuaLaTeX smoke-tested and visually inspected;
- the previously validated full v0.1 PDF remains the last complete local build;
- a full v0.2 issue rebuild remains an operational follow-up once the complete source tree is available locally or the GitHub Actions run can be addressed by run ID.

## Gate

The W32 content is now suitable for a final full-PDF rebuild and visual diff. No evidence recollection or candidate reselection is required for this editorial pass.
