# 上下文隔离审计任务

`status`: `LOOP_DONE`
`decision`: `context_isolation_issues_found`

## 目标

审计旧版 LLM Wiki 循环中主控 agent 与执行者的上下文隔离、输入输出边界、上下文泄漏风险，以及是否存在越权执行。

## 隔离规则

- 只使用文件系统中可见的一手材料：执行者的 `task.md`、`loop_status.md`、`loop_delivery.md`、控制面状态、action queue、standing status，以及必要的低层 trace。
- 不读取已有结论型报告作为判断来源，包括 `audit_report.md`、`skill_eval_report.md`、`process_findings.md`、`final_delivery_report.md`、`goal_satisfaction_audit.md`、`kb_initialization_demo_report.md`、`final_qa_report.md`。
- 不派生新的 sub-agent；本审计只做边界检查，不再制造新的执行链。
- 不把当前聊天里的结论当作证据；只把磁盘文件里的记录当作证据。

## 主要输入

- `legacy/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/control/`
- `legacy/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/runs/*/{task.md,loop_status.md,loop_delivery.md,next_task_packet.md,validation_trace.md}`
- `legacy/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/skills/*`

## 输出

- `context_isolation_audit.md`
- `io_boundary_findings.md`
- `recommendations_for_atomic_loop.md`
- `loop_status.md`
- `loop_delivery.md`

