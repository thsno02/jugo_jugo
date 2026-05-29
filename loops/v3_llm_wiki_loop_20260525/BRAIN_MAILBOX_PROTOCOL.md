# Brain Mailbox Protocol V3

V3 keeps the mailbox idea minimal. The mailbox is a filesystem communication surface, not a full scheduler.

## Runtime Reality

Brain directories are role state, not proof that a live agent exists.

Default Claude Code subagents cannot spawn other subagents through the native Agent tool. However, a subagent can launch an independent headless Claude process through Bash with `claude --permission-mode auto -p "..." --output-format text` when the inner prompt is self-contained.

Therefore a brain must not assume native nested Agent delegation. If a brain needs work delegated, it must either:

- write a visible request to the target mailbox or queue and let the lead/main session invoke the worker; or
- launch a process-level inner Claude session with a self-contained prompt, then record the command, output summary, and artifacts in v3 files.

If Claude Code agent teams are explicitly enabled, production/similarity/audit/ops may run as teammates. In that mode, teammates can communicate, but they still must respect v3 queues and context boundaries.

## Roles

- `production`: reads material tasks and writes draft cards.
- `similarity`: reads draft cards and writes top 3 similarity results plus comparison tasks.
- `audit`: audits fusion, provenance delta, and process drift.
- `ops`: maintains queues, reports, and state consistency.

## Files

Each brain directory may contain:

- `brain_state.json`: current brain status.
- `inbox.jsonl`: messages addressed to the brain.
- `outbox.jsonl`: messages emitted by the brain.
- `queue.jsonl`: actionable jobs for that brain.
- `wake_required.json`: whether the brain needs to be invoked.

## Message Schema

```json
{
  "message_id": "msg-20260525-0001",
  "created_time": "2026-05-25T20:54:47+08:00",
  "from": "main",
  "to": "production",
  "kind": "task_request",
  "subject": "Create draft cards from material batch",
  "payload_path": "queues/material_queue.md",
  "requires_wake": true,
  "status": "open"
}
```

## Wake Rule

Writing to a mailbox does not itself run an agent. A hook, main-agent action, or future automation must read `wake_required.json` and invoke the right brain.

Until that mechanism exists, the mailbox is still useful because it makes handoff state explicit and recoverable.

For process-level nested Claude calls, the mailbox item should include the exact prompt path or command payload path so the inner session can be reproduced.

Recommended command shape:

```bash
claude --permission-mode auto -p "$(cat <prompt_path>)" --output-format text
```

The prompt file must include v3 access boundaries and required output paths.

## Directionality

Brain-to-brain requests are allowed, but they must be visible:

- write to the target brain inbox;
- add a queue item;
- set `wake_required.json`;
- update `outbox.jsonl` for the sender.

Audit findings that affect production should be sent to `brains/production/inbox.jsonl` and summarized in `queues/task_queue.md`.
