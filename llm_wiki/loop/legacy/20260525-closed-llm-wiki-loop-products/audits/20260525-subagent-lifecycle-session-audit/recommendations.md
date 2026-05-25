# sub-agent 创建与管理规范

`status`: `AUDIT_DONE`

## 1. 创建标准

只有同时满足以下条件，才创建 sub-agent：

- 任务有独立判断、上下文隔离或完整 fork context 的真实价值。
- 可以写清楚 `role`、`allowed_inputs`、`forbidden_inputs`、`allowed_writes`、`success_gate`。
- 产物能从磁盘恢复，而不是只存在聊天里。
- 完成后能明确判断 `done`、`blocked` 或 `stale`。
- main-agent 不需要在 worker 运行时继续修改同一写入范围。

以下情况默认不要开 sub-agent：

- 只运行确定性脚本。
- 只做 JSON / scope / delivery 校验。
- 只补 report 链接、状态字段或目录说明。
- 任务包还无法说明允许输入和允许写入。
- 当前工作区有另一个 active worker 正在写同一目录。

## 2. 生命周期类型

### resident

适合：

- `main_agent`
- 明确只读的 monitor

规则：

- resident 不能写生产 KB。
- resident 必须只读低噪声控制面。
- resident 必须有 `heartbeat/status` 文件。

### short_lived

适合：

- git push worker
- skill evolution worker
- 围绕同一失败簇连续工作的 repair worker
- user-insights sidecar 的一次 record/organize 周期

规则：

- 必须有 scope 和结束条件。
- 如果连续接收新任务，必须写一条 lifecycle decision，把 `disposable` 转为 `short_lived`。
- 不能隐式变成常驻。

### disposable

适合：

- source mining worker
- card drafting worker
- card audit worker
- card adoption worker
- independent evaluator

规则：

- 一次只处理一个任务包。
- 完成后关闭。
- 不复用上下文做下一张卡或下一次审计。

## 3. lifecycle registry

建议新增：

```text
llm_wiki/loop/logs/subagent_lifecycle.jsonl
```

每次创建写一行：

```json
{
  "event": "spawned",
  "agent_id": "019e...",
  "nickname": "optional",
  "parent_thread_id": "019e...",
  "role": "card_drafting_worker",
  "lifecycle_type": "disposable",
  "fork_context": false,
  "task_path": "llm_wiki/loop/iterations/.../task.md",
  "allowed_write_root": "llm_wiki/loop/iterations/...",
  "spawn_reason": "draft exactly one fact candidate",
  "started_at": "2026-05-25T..."
}
```

完成后追加：

```json
{
  "event": "completed",
  "agent_id": "019e...",
  "result": "LOOP_DONE",
  "delivery_path": "llm_wiki/loop/iterations/.../loop_delivery.md",
  "artifacts": ["..."],
  "done_at": "2026-05-25T..."
}
```

关闭后追加：

```json
{
  "event": "closed",
  "agent_id": "019e...",
  "close_reason": "disposable task completed and inspected",
  "closed_at": "2026-05-25T...",
  "gui_state_checked": "unknown | not_visible | still_visible",
  "reuse_allowed": false
}
```

如果当前 agent 所在环境没有 close API，或调用后无法验证 GUI 最终状态，也要写：

```json
{
  "event": "close_unverified",
  "agent_id": "019e...",
  "reason": "close API missing or GUI close state unreadable",
  "next_human_action": "clear completed active subagent in GUI if still visible"
}
```

当前主控验收确认存在 `close_agent`，因此优先写 `closed`；如果 GUI active 面板仍不可读，则 `gui_state_checked` 填 `unknown`。

## 4. close criteria

disposable worker 的关闭条件：

- `loop_status.md` 存在。
- `loop_delivery.md` 存在并包含 `LOOP_DONE` 或 `LOOP_BLOCKED`。
- `read_log.md` 存在。
- 任务包指定 artifact 存在，或阻塞原因明确。
- `inspect_delivery.py` 通过，或失败被写为 repair/evolution 证据。
- lifecycle registry 记录 `completed` 和 `closed` / `close_unverified`。

不能因为 worker 失败就继续让同一个 worker 自我修复。失败后应新开 repair/evolution/audit 任务，或由 main-agent 做控制面最小修复。

## 5. monitor cadence

长任务可使用 monitor，但 monitor 必须低噪声：

- 每 5-10 分钟只读 `loop_status.md`、`loop_delivery.md` 和 expected artifact existence。
- 不读原始来源。
- 不写生产 artifact。
- 不催促 worker 改内容。
- 只报告 `running`、`done`、`blocked`、`stale`。

如果 worker 超过预期时长：

- 第一次：monitor 记录 stale risk。
- 第二次：main-agent 检查 status。
- 第三次：标记 `human_checkpoint_required` 或创建 replacement worker，但不得让两个 worker 写同一输出路径。

## 6. fork_context 使用规则

默认：

```text
fork_context: false
```

适用于：

- source mining
- card drafting
- card audit
- card adoption
- independent evaluator
- prompt/tool repair audit

允许 `fork_context: true` 的情况：

- user-insights 需要记录会话洞察。
- lifecycle / focus drift / context isolation 审计需要调查父聊天。
- 用户明确要求 fork 完整会话上下文。

使用 `fork_context: true` 时必须写偏差控制：

- 先列磁盘证据。
- 再提出假设。
- 再用 session metadata、任务包、交付文件验证。
- 无法验证的 GUI 状态标 `unknown`。

## 7. push worker 规则

git push worker 只能在以下条件下创建：

- 用户明确要求。
- 当前生产 loop 已暂停，或有明确 push window。
- 白名单路径已经写清。
- push worker 不编辑文件。
- push worker 不使用 `git add .`。
- push worker 不 force push。
- push rejected 时停止，不 rebase/merge。

如果 push 期间出现新的未提交变化：

- 若路径不在白名单，停止并报告。
- 不扩大范围，除非用户明确更新白名单。
- 如果新增变化来自正在跑的 loop，优先暂停 push，而不是追着生产 loop commit。

推荐流程：

```text
main-agent 写 push_window decision
-> 暂停生产 worker 或等待当前 worker 完成
-> git worker 分批 push
-> 确认 status
-> 关闭 git worker
-> 恢复生产 loop
```

## 8. 什么时候必须开

- main-agent 将要亲自读来源抽事实。
- main-agent 将要亲自写知识卡或 provenance。
- main-agent 将要亲自审计自己刚产出的卡。
- 需要独立检查 context leak、focus drift 或 lifecycle 问题。
- 需要 user-insights 记录完整会话洞察。
- 需要把同一个失败簇交给独立 repair/evolution worker。

## 9. 什么时候不要开

- 只是修一个 Markdown link。
- 只是更新 `loop_state.json` 的状态字段。
- 只是跑 `validate_scope.py` 或 `inspect_delivery.py`。
- 只是把已知审计结果写进 report。
- 任务目标、输入、输出或结束条件还不清楚。
- 另一个 worker 正在写同一 iteration。

## 10. GUI active 清理 checklist

每个 main-agent 回合结束前检查：

- `subagent_lifecycle.jsonl` 中是否有 `spawned` 但无 `completed` 的 agent。
- 是否有 `completed` 但无 `closed` / `close_unverified` 的 agent。
- 环境上下文里是否仍显示已完成 agent。
- `loop_report.md` 中是否记录“完成且不需复用的 worker 已关闭”。
- 如果 GUI 仍显示 active，但工具无法关闭，是否写了 `human_gui_cleanup_required`。

推荐在 `loop_state.json` 加轻量字段：

```json
{
  "active_subagents": [],
  "completed_subagents_pending_gui_cleanup": [
    "019e56da-...",
    "019e5b0d-..."
  ]
}
```

## 11. 最小落地动作

下一次主控 agent 可以不改生产链路，只补两个控制面小件：

1. 新增 `llm_wiki/loop/logs/subagent_lifecycle.jsonl`。
2. 修改 `render_dispatch.py` 或 main-agent runbook：每次 dispatch 后必须登记 spawn；每次收到 notification 后必须登记 completed；每次关闭或无法验证关闭后必须登记 closed / close_unverified。

这两个动作能把 GUI active 从“聊天里感觉很多”变成“文件系统可审计的生命周期状态”。
