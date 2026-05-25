# 主控验收记录

`status`: `ACCEPTED_WITH_FACTUAL_CORRECTION`

## 验收结论

本审计 folder 满足用户要求：它以 fork sub-agent 方式完成，覆盖 sub-agent 泛滥原因、必要与不必要的 agent、生命周期缺口、GUI active 风险、main-agent / sub-agent 协作卡点、做得好的地方和未来 create/manage 规范。

核心结论可接受：旧 loop 的主要问题不是单个 worker 失控，而是把“保持 main-agent 上下文干净”过度实现成“每个小步骤都开 sub-agent”，且缺少生命周期 registry。

## 事实修正

验收时主控 agent 通过工具发现当前环境存在 `multi_agent_v1.close_agent`，可以关闭已知 agent id 并返回关闭前状态。因此需要修正“close API 未暴露”的说法。

修正后的判断是：

- 有关闭工具。
- 缺少统一 lifecycle registry。
- 缺少直接读取 GUI active 面板最终状态的机制。
- `LOOP_DONE` 仍不能等同于 `closed`。

## 本轮关闭动作

主控 agent 已对以下已完成且不需复用的 agent 调用 `close_agent`：

| agent id | nickname | close 依据 |
|---|---|---|
| `019e5b5f-befe-78e0-aa64-e388f5bcbba9` | `Heisenberg` | 生命周期审计已 `AUDIT_DONE` |
| `019e5b0d-4627-7f43-9929-2d558e09ee1b` | `Volta` | hooks / sub-agent 可行性调查已完成 |
| `019e56da-9b85-7822-8c24-433753dc51d2` | unknown | pre-loop skill coverage 审计已 `LOOP_DONE` |

GUI 面板最终是否仍显示这些 agent，当前无法从文件系统或工具返回值中直接证明，因此仍应由未来 registry 记录 `gui_state_checked: unknown | not_visible | still_visible`。

## 后续最小动作

下一轮不需要重构生产 loop，优先补两个控制面小件：

1. 新增 `llm_wiki/loop/logs/subagent_lifecycle.jsonl`。
2. 在 dispatch / wait / close 的主控流程中写入 `spawned`、`completed`、`closed` 或 `close_unverified` 事件。
