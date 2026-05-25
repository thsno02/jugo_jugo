# LLM Wiki 循环控制面

这个目录专门管理 LLM Wiki 从 0 到 1 的循环。

当前活跃版本是 V2：brain-mailbox + scoped knowledge card。

循环的产物不是“漂亮的主题结构”，而是一批可读、可审计、可追溯的 scoped knowledge cards。当前阶段仍然不做枢纽页、聚类或主题覆盖，但卡片不再追求机械的过度 atomic；卡片本身必须有知识含量。

## 循环对象

```text
material / exhausted 来源
-> scoped draft card + draft provenance
-> Jieba/Jaccard title similarity top 3
-> comparison provenance 三问
-> draft backlog
-> 融合审计或发布审计
-> 已采纳 scoped knowledge card
```

当前采用 `LOOP_DESIGN_V2.md` 和 `CARD_CONTRACT_V2.md`。旧版 draft-first 控制面已冻结到 `legacy/v2_llm_wiki_loop_20260525/snapshots/draft_first_control_plane/`。

## 主控原则

主控 agent 是控制面决策者，不是具体生产者。

主控 agent 负责：

- 选择下一步循环动作。
- 写出窄任务包或 brain mailbox message。
- 派发、恢复或唤醒 brain / worker。
- 检查状态、交付、comparison provenance 和审计证据。
- 决定采纳、返工、搁置或演化技能。
- 更新 `loop_state.json`、报告和决策记录。

主控 agent 不应该亲自做大段来源挖掘、批量写卡、批量审计、批量采纳或相似候选阅读。只要发生这种情况，就说明 brain、技能、任务包或循环控制面还不够清楚，需要先干预流程。

## 目录说明

- `LOOP_DESIGN_V2.md`：当前新版循环设计。
- `CARD_CONTRACT_V2.md`：当前卡片 metadata、正文、References 和 Footnotes 契约。
- `RUNBOOK.md`：主控 agent 的启动、恢复、派发、审计和干预流程。
- `PRELAUNCH_REQUIREMENTS.md`：正式生产知识卡前必须满足的门禁。
- `CONTEXT_ISOLATION.md`：上下文隔离设计。
- `MAIN_AGENT_ELASTICITY.md`：受限 main-agent 的可用弹性。
- `SUBAGENT_EVOLUTION.md`：预定义 sub-agent 的新增与修改流程。
- `SUBAGENT_LIFECYCLE.md`：sub-agent 生命周期策略。
- `TECH_VALIDATION.md`：Codex / Claude / hook 技术验证路线。
- `SUBAGENT_SCOPE.md`：执行者的行为边界、输入输出约束和终止标记。
- `DRAFT_FIRST_PIPELINE.md`：V2 material-to-draft-to-similarity 的生产管线。
- `brains/`：brain mailbox、wake marker、queue 和最小 hook 协议。
- `loop_state.json`：当前循环状态，供恢复和监控使用。
- `loop_manifest.json`：角色、目录、非目标、门禁和语言规则。
- `system_prompts/`：主控 agent 和各类执行者的稳定 system prompt。
- `task_templates/`：每类执行者的任务包模板。
- `plans/`：给未来 main-agent 的长程执行计划和阶段计划。
- `iterations/`：每一轮循环的任务包、状态、交付和证据。
- `queues/`：待执行动作队列。
- `reports/`：人类可读循环报告。
- `decisions/`：主控 agent 的关键决策记录。
- `reflections/`：out-of-loop 的轨迹、组件和流程反思；不能作为事实来源。
- `logs/`：循环级轻量日志说明。具体来源访问日志优先放在 `data/logs/`。
- `tools/`：机械脚本，负责生成任务包、渲染 dispatch 和检查交付。
- `legacy/`：冻结旧版设计；不能作为当前恢复入口。
- `user_insights/`：发现正式 `user-insights` skill 前的临时 fallback，只保留为历史痕迹。

用户洞察的正式记录位置在仓库顶层 `user-insights/`，由专用 sidecar 写入；loop 控制面只读取其状态和高层输出，不把它当作执行者任务产物。

## 恢复入口

未来任意 agent 恢复时，先读：

1. `loop_state.json`
2. `loop_manifest.json`
3. `LOOP_DESIGN_V2.md`
4. `CARD_CONTRACT_V2.md`
5. `brains/README.md`
6. `RUNBOOK.md`
7. `queues/task_queue.md`
8. `queues/draft_backlog.md`
9. `reports/loop_report.md`
10. `plans/main_agent_long_horizon_execution_plan.md`

不要从聊天记忆恢复循环。
