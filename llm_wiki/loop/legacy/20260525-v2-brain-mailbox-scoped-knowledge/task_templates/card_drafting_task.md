# 任务包模板：知识卡草稿

- `task_id`:
- `iteration_id`:
- `role`: `card_drafting_worker`
- `main_language`: 中文

## 目标

把一个事实候选写成一张 zet 风格 scoped draft knowledge card，并写一份整理后的出处论证。

## 允许输入

- 当前任务包。
- `fact_candidate_path`: 仅限任务指定的单个候选块。
- `source_evidence_path`:

## 候选读取边界

- 读取 `fact_candidates.md` 时，只读取当前任务指定的候选块。
- 不把带上下文的关键词检索结果当作候选证据。
- 如果工具输出暴露相邻候选字段，必须改用精确候选块读取；相邻候选内容不得进入知识卡、provenance 或审计证据，并要写入 `read_log.md`。

## 禁止输入

- 父聊天上下文。
- 未列出的来源。
- 旧审计报告。
- 其它主题页或枢纽页。
- 相邻事实候选的字段、标题或表述。

## 允许写入

- `llm_wiki/loop/iterations/<iteration_id>/loop_status.md`
- `llm_wiki/loop/iterations/<iteration_id>/loop_delivery.md`
- `llm_wiki/loop/iterations/<iteration_id>/read_log.md`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/draft_card.md`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/provenance.md`

## 知识卡要求

知识卡应该是结果，不是流程日志。

必须包含 `CARD_CONTRACT_V2.md` 的固定 metadata：

- `id`
- `title`
- `status: draft`
- `card_type`
- `tags`
- `created_time`
- `edited_time`
- `edited_entity`
- `source_ids`
- `provenance_card`
- `aliases`
- `related`

写作要求：

- 标题短。
- 正文只围绕一个主要知识范围。
- 正文必须提供知识信息，不能只是标题 restatement 或 paraphrase。
- 可以说明机制、边界、对比或 operational definition，但不能扩写成主题页。
- `References` 必须放在 `Footnotes` 前。
- `Footnotes` 必须是最后一个 section。

## 出处论证要求

出处论证说明这张卡为什么可以暂时被当作事实：

- 事实从哪里来。
- 来源为什么能支撑它。
- 哪部分是来源明说的。
- 哪部分是整理后的表述。
- 成立范围是什么。
- 当前为什么只能是 `draft`。

## 成功门禁

- 只生成一张知识卡。
- 知识卡可读，不像中间状态。
- 知识卡正文有信息量，不是标题改写。
- 出处论证可读，不是流水日志。
- metadata 完整，`edited_entity` 区分 `llm` / `human` / `llm+human`。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 事实候选不够清楚。
- 来源证据不足。
- 需要额外来源才能支撑事实。
