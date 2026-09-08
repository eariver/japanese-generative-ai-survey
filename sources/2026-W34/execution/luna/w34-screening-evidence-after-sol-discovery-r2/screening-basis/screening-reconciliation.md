# W34 Fresh Screening Reconciliation (Muse Spark 1.3, EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION)

- Derived Screening basis: 439 records (110 prior +329 new), accounting for all 369 accepted Discovery roots.
- Prior 105 events: freshly reviewed, retaining prior Sol decisions (KEEP 45 / MAYBE 19 / INSPECT 16 / DROP 25 for 105 events) with substantive justification, not by prior validation reuse.
  - Chronology refinements retained: W34-C001 (GLM-5.3) and W34-C039 (Qwen3.8) remain KEEP with provider/service refinement noted; W34-C072 remains DROP for Runway post-cutoff while new W34-GAP-ALIBABA-WAN30 (in-window Model Studio wan3.0-video-prime) is separately KEEP (split identity).
  - 5 coverage passthrough (github releases) retained as DROP (not new events).
- 15 prior refresh leads: 7 official (kimi-cli KEEP, replit-gpt56-luna KEEP, defenders-window KEEP, cohere MAYBE, 3 apple MAYBE) +8 arxiv (k-bench KEEP, 7 others MAYBE).
- Alibaba split/refinement: W34-C001/C039 refinements retained; new Wan split KEEP; Kimi K3 new KEEP.
- New AWS AgentCore Memory JSON event: KEEP (distinct Aug 20 capability).
- New arXiv shortlist identities: 311 triage (KEEP 21 score>=14 / MAYBE 106 score 11-13 / INSPECT 184 score 9-10) +8 refresh arxiv (1 KEEP +7 MAYBE). No paper-DROP, no count optimization; DROP 0 new (all IN_WINDOW, no clear duplicates/off-profile/chronology-ineligible among new).
- Duplicate/merged: 3 arxiv duplicates (21265,21614,23611) merged into refresh identities, single children via refresh parents; 8 official fallback observations merged into prior events via parent union (C001,C039,C010,C034,C099,C100,C101 +1 prewindow), no separate duplicate children.
- Chronology-boundary: 12 pre-window /4 post-cutoff /105 unresolved retained in prior decisions; new all IN_WINDOW; C072 post-cutoff DROP preserved, Wan in-window split KEEP.
- Total fresh: {'KEEP': 73, 'INSPECT': 200, 'MAYBE': 136, 'DROP': 30} / 439. Non-DROP 409 require Evidence.
