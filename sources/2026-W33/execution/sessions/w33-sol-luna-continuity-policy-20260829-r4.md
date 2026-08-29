# Survey Production session — w33-sol-luna-continuity-policy-20260829-r4

Issue: `2026-W33`  
Recorded: `2026-08-29 JST`

## Starting authority

- Work branch: `weekly/2026-W33-v2-work`
- Verified branch head before this record: `78ad4289deac13c22f67d3ec8c7c0f68a55af6eb`
- Current lifecycle: `ISSUE_INITIALIZED`
- Current next machine action: `stage:discovery`
- Active Luna task: `sources/2026-W33/execution/handoffs/w33-discovery-rebuild-luna-r1.md`

## Actions actually performed

- Recorded the Human-specified continuity policy for Work/GPT-5.6 Luna.
- The Luna side is to use one continuing Work chat session for the remainder of this production flow, including successive bounded task handoffs from Sol.
- A new Luna chat session is expected only if the current Work chat reaches its session/context limit or otherwise cannot continue.
- Repository handoff files, execution records, exact branch/commit SHAs, and task-specific write boundaries remain authoritative even when the same Luna chat carries conversational continuity.
- Sol continues to issue bounded task specifications and independently reviews Luna worker commits before semantic acceptance or lifecycle advancement.

## External handoff

- The first Luna task remains `handoffs/w33-discovery-rebuild-luna-r1.md` starting from `78ad4289deac13c22f67d3ec8c7c0f68a55af6eb`.
- After Luna returns that candidate commit, subsequent Luna work should normally be sent into the same Work chat session rather than opening a fresh session.
- Each subsequent Luna task must still state the exact repository start SHA and task authority path so repository continuity does not depend on chat memory.

## Deterministic execution transport

- No operator request or stage advancement was executed in this record.
- `production-state.json` remains unchanged.

## Deviations / failures

- None.

## End state

- Luna conversational continuity policy: `SAME_WORK_CHAT_BY_DEFAULT`.
- New Luna chat exception: only when the continuing Work chat cannot be continued, including session/context limit.
- Repository crash-recovery policy remains unchanged: recover from `sources/2026-W33/execution/index.md`, Production State, latest session record, and active handoff.
