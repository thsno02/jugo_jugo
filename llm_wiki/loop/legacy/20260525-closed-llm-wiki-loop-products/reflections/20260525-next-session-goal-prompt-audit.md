# 下一次 chat-session goal prompt 审计

日期：2026-05-25

审计对象：

- `llm_wiki/loop/plans/next_session_goal_prompt.md`

## 审计标准

- 是否能复制到新 chat-session 后直接开始执行。
- 是否明确要求创建 goal，而不是只讨论计划。
- 是否约束 main-agent 先读恢复入口。
- 是否保持核心目标为知识卡生产，而不是 hub、cluster、topic coverage。
- 是否明确没有预设 card topic，card 由 agent 从来源中 bottom-up 自主探索。
- 是否防止 main-agent 亲自执行 worker 的生产任务。
- 是否覆盖 KB 生产、skill/prompt/template/tool 演化、文件系统管理、out-of-loop 反思和无人值守自治。
- 是否包含网络限制、语言规则、user-insights 边界和停止逻辑。

## 证据

- Prompt 明确写了“请在 ... 开启一个新的 goal，并进入 long-horizon autonomous loop”。
- Prompt 明确写了“请现在开始...不要只给计划”。
- Prompt 的恢复入口只列出 loop state、manifest、runbook、queue、report 和 long-horizon plan。
- Prompt 明确写了“loop 的核心是生产知识卡片，不是聚合知识 hub”。
- Prompt 明确写了“没有预设 card topic；card 的生产由 agent 从本地来源中 bottom-up 自主探索事实候选”。
- Prompt 禁止 main-agent 亲自大段阅读来源、写卡、写 provenance、审计采纳或绕过 task packet。
- Prompt 覆盖 source mining -> drafting -> audit -> adoption 的生产链路。
- Prompt 覆盖失败证据触发的 skills、system prompts、task templates、tools 和控制面演化。
- Prompt 覆盖 reflection 文档、文件系统职责、网络限制、中文主语言、References / Footnotes 顺序、无人值守和停止条件。

## 假设

- H1：新 main-agent 可以用该 prompt 直接进入 loop，而不会只输出计划。
- H2：该 prompt 不会诱导新 main-agent 预设 card topic 或做 hub 聚合。
- H3：该 prompt 给了 main-agent 足够弹性，但不会让它变成执行者。
- H4：该 prompt 的自治要求不会越过人类 checkpoint。

## 验证

- H1 成立。Prompt 最后一行要求立刻创建 goal、读取恢复入口、确认状态并创建/派发第一轮 source_mining_worker。
- H2 成立。Prompt 多处明确非目标为 hub、cluster、topic coverage，并说明无预设 card topic。
- H3 成立。Prompt 允许 main-agent 做状态迁移、任务包、派发、验收、决策和反思；禁止它执行来源挖掘、写卡、审计和采纳。
- H4 成立。Prompt 要求扩大 scope、进入 hub/cluster/topic、改变 schema、批量采纳、git push、外部同步或不可逆操作时停止并记录 human checkpoint。

## 结论

```text
audit_result: pass
```

该 prompt 可以交付给用户。
