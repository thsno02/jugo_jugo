# planner task

run_dir:: .llmwiki/runs/<run_id>
main_language:: zh-CN
status:: frontier_gated

## 职责

从 `.llmwiki/control/knowledge_frontier.yaml` 中选择一个 `ready_to_build` candidate，写 `planner_report.md`、`evidence_scope.yaml` 和 `next_task_packet.md`。

如果没有 `ready_to_build` candidate，则不要写 generator packet；改写 source mining 或 frontier repair task。

Main/controller 只创建或审查本 task packet、读取你的 summary/status/gate/delivery、决定是否采用。你是 worker/executor，必须在 delivery 中写明 executor_role、task_packet、allowed_inputs、outputs_written 和 `LOOP_DONE` / `LOOP_BLOCKED`。

## 必读

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/control/knowledge_frontier.yaml`
- 本轮或前序 `source_scope.md`
- 本轮或前序 `source_mining.md`
- 本轮或前序 `candidate_frontier_delta.yaml`

## 安全边界

你不是 repo 里唯一的执行者。不要 revert、overwrite 或清理无关文件。任何超出 scoped inputs 的读取都应记录理由。

Planner output 不能仅凭 `topic_plan.md`、`topic_node_backlog.yaml` 或默认候选直接授权 card generation。

如果输入来自 controller drift sample，必须先要求 worker source-mining review/rerun 已完成，不得直接规划 generation。
