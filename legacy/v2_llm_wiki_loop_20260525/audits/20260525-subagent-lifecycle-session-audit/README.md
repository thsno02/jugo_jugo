# sub-agent 生命周期会话审计

`status`: `AUDIT_DONE`
`audit_scope`: 当前 LLM Wiki chat session、相关 fork sub-agent、本地 session 记录、loop/audit 落盘产物。
`main_language`: 中文

## 入口结论

本次审计认为：sub-agent 泛滥不是因为某一个 worker 失控，而是因为旧 loop 把“保持 main-agent 上下文干净”理解成“几乎所有具体动作都开一个 sub-agent”，同时没有把 `agent_id / role / lifecycle / close_at / gui_state` 做成运行时账本。结果是：每个小阶段都有执行者，`LOOP_DONE` 能证明任务产物完成，却不能证明 GUI thread 已关闭。

当前新版 loop 的方向已经明显改善：`fork_context: false`、任务包、`read_log.md`、`loop_delivery.md` 和完成即关闭的设计都比旧版更好。但 Zeno push worker 和并行 active loop 说明：只要另一个 session 还在写文件，git worker 或审计 worker 就会被新的本地变化反复拖住。好的生命周期管理必须同时管理 agent 和工作区写入节奏。

## 关键判断

- 必要的 sub-agent：来源挖掘、单卡 drafting、独立审计、user-insights sidecar、当前生命周期审计、窄 scope 的 push worker。
- 可避免或应替换的 sub-agent：机械状态同步、纯脚本校验、过细的 per-step skill eval、没有独立判断价值的“补文档/补链接”任务。
- 最大反直觉点：为了保护 main-agent 上下文而频繁开 sub-agent，反而把系统复杂度转移到生命周期、GUI active 状态和多 agent 写入冲突上。
- 未来规则：每个 sub-agent 必须有明确 `create_reason`、`lifecycle_type`、`close_criteria` 和 `post_completion_action`；没有这些字段时，默认不要创建。

## 文件说明

- [subagent_inventory.md](subagent_inventory.md)：可见 sub-agent 清单、必要性、状态和 GUI active 风险。
- [evidence_log.md](evidence_log.md)：按时间线记录证据，包括用户要求、通知、派发/关闭行为和 Zeno push 卡点。
- [lifecycle_audit.md](lifecycle_audit.md)：核心审计报告，包含证据、假设、验证、根因和反直觉发现。
- [recommendations.md](recommendations.md)：未来 create/manage sub-agent 的可执行规范。
- [main_agent_acceptance.md](main_agent_acceptance.md)：主控 agent 的验收记录、事实修正和本轮关闭动作。

## 证据边界

本审计使用三类证据：

- 当前 fork 审计线程可见的聊天上下文。
- 本地 Codex session 元数据，例如当前审计线程 `019e5b5f-befe-78e0-aa64-e388f5bcbba9` 标记为 `thread_source: subagent`、nickname `Heisenberg`。
- 磁盘产物，包括 `llm_wiki/loop/*`、`legacy/audits/*`、`user-insights/*` 和相关 `.codex/sessions/*.jsonl`。

风险控制：fork context 让审计者能看到父聊天叙事，但也可能被父叙事污染。因此核心结论优先依赖磁盘证据和 session metadata；只在无法从磁盘复原 GUI 状态时标注 `unknown`。

## 主控验收补充

主控 agent 验收时确认：当前工具层存在 `multi_agent_v1.close_agent`，可以对已知 agent id 发起关闭并返回关闭前状态。因此“没有 close API”不是最终结论；真正缺口是没有统一 registry 记录 `spawned -> completed -> closed`，也不能直接读取 GUI 面板最终是否仍显示 active。

主控验收期间已对以下已完成且不需复用的 agent 发起关闭：

- `019e5b5f-befe-78e0-aa64-e388f5bcbba9` / Heisenberg
- `019e5b0d-4627-7f43-9929-2d558e09ee1b` / Volta
- `019e56da-9b85-7822-8c24-433753dc51d2`
