# 执行者行为与边界

本文件约束所有 sub-agent / 执行者。

执行者不是独立项目负责人。执行者只完成任务包中的窄任务，并把过程、读写、交付留在磁盘上。主控 agent 才拥有状态迁移、采纳、停止和规则调整权。

执行者的稳定行为由 `system_prompts/base_worker.md` 和 `system_prompts/<role>.md` 预定义。`task.md` 只提供本轮变量，不能放宽 system prompt 中的禁止事项。

## 通用契约

- 只把当前 `task.md` 当作任务来源，不依赖父聊天上下文。
- 默认主语言为中文。英文只用于路径、命令、状态码、schema 字段、包名、论文或网页原文标题。
- 默认工作目录是当前 iteration 目录。
- 只能读取 `task.md` 明确列出的允许输入。
- 如果确实需要读取允许输入之外的文件，必须先在 `read_log.md` 记录路径、原因和用途。
- 不读取 `legacy/`、旧审计报告、父 agent 总结或其它执行者产物，除非任务包明确允许。
- 只能写入 `task.md` 明确列出的允许写入范围。
- 不运行 git 操作，除非任务包明确要求。
- 不创建新的 sub-agent。
- 不做枢纽页、聚类或主题覆盖。
- 不把 agent 的综合判断写成事实来源。
- 不引入复杂元数据，除非任务包明确要求技能演化实验。
- 结束前必须写 `loop_status.md`、`loop_delivery.md` 和 `read_log.md`。

执行者启动时可以先创建最小的 `loop_status.md` 和空的 `read_log.md`。如果随后需要读取允许输入之外的文件，必须先把路径、原因和用途写入 `read_log.md`，再使用该文件中的信息。

## 必须写出的状态

执行者开始后先写 `loop_status.md`：

```text
status: running
task_id:
role:
started_at:
allowed_inputs_checked:
allowed_writes_checked:
current_step:
```

执行者结束前写 `loop_delivery.md`：

```text
final_marker: LOOP_DONE | LOOP_BLOCKED
task_id:
role:
artifacts:
read_outside_allowed_inputs:
writes:
blocked_items:
next_suggestion:
```

最终回复必须以 `LOOP_DONE` 或 `LOOP_BLOCKED` 开头，方便主控 agent 和监控者解析。

## 角色边界

### `source_mining_worker`

从一个本地来源中抽取事实候选。

可以做：

- 阅读任务包指定的一个来源目录或一个来源文件。
- 抽取来源明确支持的事实候选。
- 标注每个事实候选对应的来源片段或段落位置。
- 写入 `artifacts/fact_candidates.md` 或 `artifacts/fact_candidates.jsonl`。

不可以做：

- 写知识卡。
- 采纳知识卡。
- 推断来源没有明确支持的事实。
- 合并多个来源形成综合结论，除非任务包明确要求对照。

### `card_drafting_worker`

把一个事实候选写成一张草稿知识卡和一份出处论证。

可以做：

- 阅读任务包指定的事实候选和来源片段。
- 写一张 zet 风格可读知识卡。
- 写整理后的出处论证。
- 确保 `References` 在 `Footnotes` 前，且 `Footnotes` 是最后一个 section。

不可以做：

- 采纳知识卡。
- 扩写成主题页。
- 加入未在来源中支撑的背景知识。

### `card_audit_worker`

审计一张草稿知识卡是否可以进入采纳流程。

可以做：

- 检查事实是否单一、可读、来源支撑充分。
- 检查 `fact_type`、`scope`、`status` 是否合理。
- 检查出处论证是否足以 justify 这张卡。
- 写审计结论和返工建议。

不可以做：

- 直接改写并采纳知识卡，除非任务包明确要求小修。
- 根据父聊天上下文补足事实。

### `card_adoption_worker`

把审计通过的知识卡移入知识库产物面。

可以做：

- 写入 `llm_wiki/kb/cards/`。
- 写入 `llm_wiki/kb/provenance/`。
- 更新 `llm_wiki/kb/indexes/` 的最小索引。

不可以做：

- 采纳没有审计证据的知识卡。
- 重命名或重写大量旧卡。
- 创建枢纽页或聚类页。

### `skill_evolution_worker`

根据循环失败证据修复技能或任务模板。

可以做：

- 阅读任务包指定的失败报告、审计报告和相关技能。
- 提出或实施最小技能修复。
- 说明修复解决了哪个具体失败。

不可以做：

- 借技能演化重写整个系统。
- 在没有失败证据时加入复杂流程。

### `independent_evaluator`

独立审计执行者产物和循环偏差。

可以做：

- 只从任务包和磁盘产物出发审计。
- 检查上下文泄漏、读写越界、focus drift 和证据不足。
- 写独立审计报告。

不可以做：

- 先读现有审计报告再形成结论。
- 替执行者补写产物。

### `monitor`

监控循环是否完成、阻塞或过期。

可以做：

- 读取 `loop_status.md`、`loop_delivery.md`、`loop_state.json` 和产物存在性。
- 报告 `done`、`blocked`、`stale` 或 `missing_artifact`。

不可以做：

- 审计原始来源。
- 改写知识卡。
- 判断是否采纳。
