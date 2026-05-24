# 任务包：前置门禁独立审计

- `task_id`: `task_20260525_0001_prelaunch_validation`
- `iteration_id`: `iteration_20260525_0001_prelaunch_validation`
- `role`: `independent_evaluator`
- `main_language`: 中文

## 目标

独立审计当前 loop 前置控制面是否足以进入第一轮 `source_mining_worker`。重点检查上下文隔离、受限 main-agent 弹性、预定义 sub-agent 演化、生命周期、技术验证和 user-insights 记录是否形成可执行门禁。

## 允许输入

- 当前任务包。
- `llm_wiki/loop/PRELAUNCH_REQUIREMENTS.md`
- `llm_wiki/loop/CONTEXT_ISOLATION.md`
- `llm_wiki/loop/MAIN_AGENT_ELASTICITY.md`
- `llm_wiki/loop/SUBAGENT_EVOLUTION.md`
- `llm_wiki/loop/SUBAGENT_LIFECYCLE.md`
- `llm_wiki/loop/TECH_VALIDATION.md`
- `llm_wiki/loop/RUNBOOK.md`
- `llm_wiki/loop/SUBAGENT_SCOPE.md`
- `llm_wiki/loop/loop_state.json`
- `llm_wiki/loop/loop_manifest.json`
- `llm_wiki/loop/queues/task_queue.md`
- `llm_wiki/loop/reports/loop_report.md`
- `llm_wiki/loop/tools/README.md`
- `llm_wiki/loop/tools/create_task.py`
- `llm_wiki/loop/tools/render_dispatch.py`
- `llm_wiki/loop/tools/validate_scope.py`
- `llm_wiki/loop/tools/inspect_delivery.py`
- `llm_wiki/loop/iterations/iteration_0000_bootstrap/artifacts/codex_hooks_feasibility_smoke.md`
- `llm_wiki/loop/iterations/iteration_0000_bootstrap/artifacts/cli_capability_probe.md`
- `user-insights/` 下本次 sidecar 已写入的文件；如果目录不存在或内容不完整，记录为证据。

## 禁止输入

- 父聊天上下文。
- 已有同主题审计报告。
- 未列出的来源材料。
- `llm_wiki/legacy/`。
- `llm_wiki/loop/user_insights/`，除非只用于确认它是 pre-skill fallback；不得把它当成正式 user-insights 输出。
- `data/` 中的来源内容。
- 任何知识卡草稿、主题页、hub 或 cluster 产物。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0001_prelaunch_validation/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0001_prelaunch_validation/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0001_prelaunch_validation/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0001_prelaunch_validation/artifacts/independent_audit.md`

## 审计问题

- 前置门禁是否覆盖用户要求的上下文隔离、main-agent 受限弹性、sub-agent 可演化机制和生命周期。
- 是否仍要求 main-agent 临场写大段 prompt，或者能通过稳定 prompt、任务包和机械脚本减少临场发挥。
- `TECH_VALIDATION.md` 是否清楚记录 hooks、Codex CLI、Claude CLI 的已验证事实、未验证项、风险和替代路线。
- `user-insights/` 是否已经由专用 sidecar 写入，并且没有继续使用旧 fallback 目录作为 canonical target。
- 当前队列是否在前置门禁通过前阻止 source mining。
- 文档主语言是否保持中文，英文是否只出现在路径、命令、schema 字段、状态码或固定名词中。
- 是否出现 focus drift：把当前阶段从“前置控制面 + 原子事实卡基础”带到 hub、cluster、topic coverage 或复杂 metadata。
- 这些文档是否足以让未来 agent 不依赖父聊天上下文恢复 loop。

## 结论格式

```text
audit_result: pass | concern | fail
evidence:
hypotheses:
validated_findings:
required_changes:
```

## 成功门禁

- 先列证据，再给假设，再验证假设。
- 不引用父聊天上下文。
- 不替主控 agent 补写控制文档。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。
- `artifacts/independent_audit.md` 给出 `pass`、`concern` 或 `fail`。

## 阻塞条件

- 允许输入中的关键文件缺失，导致无法判断前置门禁。
- 发现必须读取未授权材料才能判断结论。
- 需要写入允许范围之外的文件才能完成审计。
