# 任务包模板：知识卡草稿

- `task_id`:
- `iteration_id`:
- `role`: `card_drafting_worker`
- `main_language`: 中文

## 目标

把一个事实候选写成一张 zet 风格原子事实知识卡，并写一份整理后的出处论证。

## 允许输入

- 当前任务包。
- `fact_candidate_path`:
- `source_evidence_path`:

## 禁止输入

- 父聊天上下文。
- 未列出的来源。
- 旧审计报告。
- 其它主题页或枢纽页。

## 允许写入

- `llm_wiki/loop/iterations/<iteration_id>/loop_status.md`
- `llm_wiki/loop/iterations/<iteration_id>/loop_delivery.md`
- `llm_wiki/loop/iterations/<iteration_id>/read_log.md`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/draft_card.md`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/provenance.md`

## 知识卡要求

知识卡应该是结果，不是流程日志。

必须包含极简契约：

- `statement`
- `fact_type`
- `support`
- `scope`
- `status: draft`

写作要求：

- 标题短。
- 正文只围绕一个主要事实。
- 可以有简短解释，但不能扩写成主题页。
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
- 出处论证可读，不是流水日志。
- 没有新增复杂元数据。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 事实候选不够清楚。
- 来源证据不足。
- 需要额外来源才能支撑事实。
