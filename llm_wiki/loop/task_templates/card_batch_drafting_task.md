# 任务包模板：批量知识卡草稿

- `task_id`:
- `iteration_id`:
- `role`: `card_batch_drafting_worker`
- `main_language`: 中文

## 目标

把任务包列出的多个事实候选批量写成 atomic draft cards。每个候选最多一张卡；每张卡必须有 provenance。

## 允许输入

- 当前任务包。
- `fact_candidate_path`:
- `allowed_candidates`:
- `source_evidence_path`:
- `source_evidence_pointers`:

## 禁止输入

- 父聊天上下文。
- 未列出的来源。
- 已采纳 KB 卡片或 provenance。
- 旧审计报告。
- 枢纽页、聚类页或主题覆盖文档。

## 允许写入

- `llm_wiki/loop/iterations/<iteration_id>/loop_status.md`
- `llm_wiki/loop/iterations/<iteration_id>/loop_delivery.md`
- `llm_wiki/loop/iterations/<iteration_id>/read_log.md`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/draft_cards/`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/provenance/`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/batch_manifest.md`

## 知识卡要求

- 每张卡只表达一个主要事实。
- 标题短，正文可读，不像中间状态。
- 不生成 hub、cluster 或 coverage 文档。
- `References` 必须放在 `Footnotes` 前。
- `Footnotes` 必须是最后一个 section。

## 出处论证要求

每份 provenance 说明：

- 事实从哪里来。
- 来源为什么能支撑它。
- 哪部分是来源明说的。
- 哪部分是整理后的表述。
- 成立范围是什么。
- 当前为什么只能是 `draft`。

## 成功门禁

- `artifacts/batch_manifest.md` 存在，并列出每个候选的结果。
- 每张 drafted 卡都有对应 provenance。
- 所有 drafted 卡都是 `status: draft`。
- 没有新增复杂元数据。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 候选列表与来源证据无法对应。
- 来源证据不足。
- 需要未列出的来源才能支撑事实。
