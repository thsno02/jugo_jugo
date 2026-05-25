# Brain mailbox smoke test

`status`: `PASS`
`tested_time`: `2026-05-25T15:35:00+08:00`

## 目的

验证最小 brain mailbox 机制是否可实践：audit brain 可以通过 outbox 发送消息，hook/router 可以投递到 production inbox，production brain 可以 claim/complete，并把 response route 回 audit。

## 执行链路

1. `audit -> production`
   - message_id: `msg_smoke_audit_to_production_20260525_1532`
   - type: `revision_request`
   - artifact_ref: `llm_wiki/loop/audits/20260525-control-plane-subagent-task-audit/task_flow_audit.md`

2. `brainctl hook --event smoke_send`
   - routed: `msg_smoke_audit_to_production_20260525_1532`
   - wake_required: `production`

3. `production` claim / complete
   - claimed_by: `smoke-production-brain`
   - response_type: `revision_response`
   - response_message_id: `msg_smoke_production_to_audit_20260525_1532`

4. `brainctl hook --event smoke_response`
   - routed: `msg_smoke_production_to_audit_20260525_1532`
   - wake_required: `audit`

5. `audit` claim / complete
   - claimed_by: `smoke-audit-brain`
   - response: smoke response received

6. `brainctl reconcile`
   - reconciled both source outbox messages to `resolved`.

## 结果

`brainctl status` 最终显示：

```json
{
  "audit": {"inbox_open": 0, "outbox_open": 0, "outbox_routed": 0, "state": "idle", "wake_required": false},
  "ops": {"inbox_open": 0, "outbox_open": 0, "outbox_routed": 0, "state": "idle", "wake_required": false},
  "production": {"inbox_open": 0, "outbox_open": 0, "outbox_routed": 0, "state": "idle", "wake_required": false},
  "similarity": {"inbox_open": 0, "outbox_open": 0, "outbox_routed": 0, "state": "idle", "wake_required": false}
}
```

## 实验发现

- mailbox + router + wake marker 是可实践的。
- hook 不需要做重活，只需调用 `brainctl hook`。
- repo-local shell hook `llm_wiki/loop/hooks/brain-mailbox-hook.sh` 可以调用，并在无消息时保持所有 brain idle。
- brain agent 可以是 event-driven：醒来读取 inbox，claim 一条消息，处理后 complete，再退出。
- 初版 `complete` 没有同步 source outbox 的 resolved 状态；实验中补充了 `reconcile`，并让后续 complete 自动更新源 outbox。

## 限制

- 这不是完整 scheduler；它不会自动调用 `spawn_agent`。
- 当前 wake marker 需要 main-agent 或未来 ops brain 读取后再唤醒目标 brain。
- 未测试真实 Codex hook 全局安装，只测试了 repo-local hook-friendly command。
