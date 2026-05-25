# LLM Wiki 循环运行手册

本手册约束主控 agent。执行者的边界见 `SUBAGENT_SCOPE.md`。

## 启动前检查

主控 agent 每次启动或恢复循环时，只先读这些文件：

- `llm_wiki/README.md`
- `llm_wiki/loop/README.md`
- `llm_wiki/loop/PRELAUNCH_REQUIREMENTS.md`
- `llm_wiki/loop/loop_state.json`
- `llm_wiki/loop/loop_manifest.json`
- `llm_wiki/loop/queues/task_queue.md`
- `llm_wiki/loop/reports/loop_report.md`
- `llm_wiki/loop/plans/main_agent_long_horizon_execution_plan.md`

如果需要选择来源，再读 `data/manifests/acquired_sources_index.md` 或 `data/manifests/sources.jsonl`。不要先读旧版 `legacy/` 报告来决定当前循环，除非任务明确要求历史审计。

如果 `queues/task_queue.md` 或 `reports/loop_report.md` 缺失、过期或与 `loop_state.json` 矛盾，以 `loop_state.json` 为准，先修复控制面，再派发执行者。

## 单轮主控循环

1. 读取当前状态和队列，确认只推进一个最小动作。
2. 选择执行角色，并读取对应 `system_prompts/<role>.md`。
3. 从 `task_templates/` 复制对应模板，生成新的 `iterations/<iteration_id>/task.md`。
4. 在任务包中写清楚允许输入、禁止输入、允许写入、成功门禁、阻塞条件和最终输出格式。
5. 确认任务包没有放宽 system prompt；任务包只能收窄角色边界，不能扩大权限。
6. 如果是来源挖掘任务，只选择一个具体本地来源，不按主题覆盖、聚类或枢纽页规划来选源。
7. 派发给对应执行者，或在没有可用执行者时只做控制面维护，不亲自展开具体挖掘。
8. 执行者必须先写 `loop_status.md`，结束前写 `loop_delivery.md` 和 `read_log.md`。
9. 主控 agent 只检查任务包、状态、交付、读日志和产物，不替执行者补写核心内容。
10. 根据门禁决定 `accept`、`revise`、`reject`、`skill_evolution` 或 `defer`。
11. 更新 `loop_state.json`、`reports/loop_report.md`，必要时写入 `decisions/`。

如果当前任务是长程恢复或无人值守继续执行，先对照 `plans/main_agent_long_horizon_execution_plan.md`，确认本轮动作属于生产、演化、反思或运维中的哪一条链路。不要在同一轮里混改生产产物和大组件设计。

## Atomic Draft First 模式

当 `loop_state.json.status` 是 `ATOMIC_DRAFT_FIRST_READY` 或 `ATOMIC_DRAFT_BATCH_IN_PROGRESS` 时，主控 agent 优先使用 `DRAFT_FIRST_PIPELINE.md`：

1. 对一个已完成 source mining 的来源，批量生成 atomic draft cards 和 provenance。
2. 把草稿登记到 `queues/draft_backlog.md`。
3. 用 `card_similarity_gate_worker` 判断 `new_atomic_card`、`merge_candidate`、`provenance_delta`、`duplicate_skip` 或 `revise_before_gate`。
4. `new_atomic_card` 可以跳过融合审计，但最终公开发布前仍需 audit。
5. `merge_candidate` 和 `provenance_delta` 必须先审计融合或增量 provenance。
6. audit/publication 按 batch 推进；单卡 revise/reject/read-boundary failure 只拆出该卡，不阻塞整批。

这个模式替代“写一张、审一张、采纳一张”的默认节奏。它仍然禁止无 provenance 草稿、无审计公开发布和把 draft 当 accepted。

## 提示词组合方式（prompt）

派发执行者时，主控 agent 使用：

```text
system prompt = system_prompts/base_worker.md + system_prompts/<role>.md
task input = iterations/<iteration_id>/task.md
```

主控 agent 自身使用 `system_prompts/main_agent.md` 作为恢复和自治时的稳定约束。

任务包只能提供本轮变量，例如来源路径、候选路径、允许写入目录和成功门禁。任务包不能覆盖 system prompt 中的禁止事项。

## 前置阶段

当 `loop_state.json.status` 是 `PRELAUNCH_IN_PROGRESS` 时，主控 agent 只能推进前置要求：

- 上下文隔离。
- main-agent 弹性。
- sub-agent 演化机制。
- sub-agent 生命周期。
- Codex / Claude / hook 最小技术验证。
- 用户洞察记录。

不能派发 `source_mining_worker` 生产事实候选，直到 `PRELAUNCH_REQUIREMENTS.md` 的门禁被记录为通过。

## 机械工具

主控 agent 优先调用 `tools/`，减少临场 prompt：

- `python3 llm_wiki/loop/tools/create_task.py ...`
- `python3 llm_wiki/loop/tools/render_dispatch.py ...`
- `python3 llm_wiki/loop/tools/validate_scope.py <task.md>`
- `python3 llm_wiki/loop/tools/inspect_delivery.py <iteration_id>`
- `python3 llm_wiki/loop/tools/cli_capability_probe.py --output <path>`

## 当前允许的循环动作

- 从一个本地来源挖掘事实候选。
- 把一个事实候选写成一张草稿知识卡和一份出处论证。
- 把一个已挖掘来源的多个候选批量写成 atomic draft cards 和 provenance。
- 对一组草稿卡做相似门判断。
- 审计一张草稿知识卡。
- 批量审计多张草稿知识卡。
- 采纳一张审计通过的知识卡。
- 批量采纳多张审计通过且无冲突的知识卡。
- 根据失败证据迭代技能或任务模板。
- 独立审计执行者是否越界、泄漏上下文或造成 focus drift。

## 当前禁止的循环动作

- 生成枢纽页。
- 做聚类。
- 做主题覆盖。
- 批量生成没有出处论证的知识卡。
- 把相似门结论当作事实审计结论。
- 把 draft backlog 当作公开 KB。
- 把 agent 的综合判断当作事实来源。
- 为知识卡引入复杂元数据，除非循环失败证据证明必要。
- 让执行者读取父聊天上下文或旧审计报告来补全任务。

## 干预条件

出现以下情况时，主控 agent 停止继续生产知识卡，先修复流程：

- 任务目标从原子事实卡漂移到枢纽页、主题或覆盖率。
- 执行者没有写 `loop_status.md` 或 `loop_delivery.md`。
- 执行者读取了允许输入之外的材料却没有记录原因。
- 执行者写入了允许写入范围之外的文件。
- 知识卡变成中间状态、审计日志或流程记录，而不是可读 zet 风格卡。
- `References` 没有放在 `Footnotes` 之前，或 `Footnotes` 不是最后一个 section。
- 新写的人类可读文档主语言不是中文。

## 长时间自治

人类离开电脑时，循环只能沿着队列中的窄任务继续。

默认策略：

- 优先使用 `data/` 中已有来源。
- 网络 retrieve 只做有限尝试，遇到公司网络限制就记录并搁置。
- 每轮只改变一个变量：来源、事实候选、知识卡、审计或技能修复。
- 不自动推送远端，除非人类明确要求。
- 不把“跑了很多轮”当作成功；成功只来自可读知识卡、出处论证和审计证据。

如果出现重复失败、周期过长、文件系统恢复困难或 main-agent 需要亲自执行具体生产的迹象，暂停生产并写入 `reflections/`。反思必须给出一个下一步动作：继续生产、技能演化、prompt 演化、工具修复、文件系统修复、人类 checkpoint、搁置或停止。

## 停止逻辑

循环没有固定轮数。主控 agent 只有在以下情况下停止：

- 当前队列为空，且没有明显高价值下一步。
- 连续阻塞来自同一个外部条件，且已经记录证据。
- 当前阶段目标已经被证据满足。
- 发现流程本身有偏差，需要先等待人类审计或重设规则。

停止或暂停时，必须更新 `loop_state.json` 和 `reports/loop_report.md`。
