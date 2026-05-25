# 循环日志

这里放循环级轻量日志说明。

当前约定：

- 来源获取和访问失败优先记录在 `data/logs/`。
- 每个执行者的额外读取记录在对应 iteration 的 `read_log.md`。
- 主控 agent 的关键决策记录在 `llm_wiki/loop/decisions/`。
- brain mailbox 路由事件记录在 `brain_message_bus.jsonl`。
- sub-agent / brain 实验生命周期事件记录在 `subagent_lifecycle.jsonl`。

不要把大量原始来源内容复制到这里。
