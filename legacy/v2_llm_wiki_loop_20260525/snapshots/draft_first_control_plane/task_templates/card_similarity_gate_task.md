# 任务包模板：知识卡相似门

- `task_id`:
- `iteration_id`:
- `role`: `card_similarity_gate_worker`
- `main_language`: 中文

## 目标

判断一组草稿卡与现有 KB 卡片之间的知识身份关系。相似门只做新卡/融合/重复/增量 provenance 判断，不做事实审计。

## 允许输入

- 当前任务包。
- `draft_batch_manifest_path`:
- `draft_card_paths`:
- `draft_provenance_paths`:
- `target_index_path`: `llm_wiki/kb/indexes/cards.md`
- `similar_existing_card_paths`:
- `draft_backlog_path`: `llm_wiki/loop/queues/draft_backlog.md`

## 禁止输入

- 父聊天上下文。
- 未列出的来源。
- 未列出的 KB 卡片。
- 旧审计报告。
- 枢纽页、聚类页或主题覆盖文档。

## 允许写入

- `llm_wiki/loop/iterations/<iteration_id>/loop_status.md`
- `llm_wiki/loop/iterations/<iteration_id>/loop_delivery.md`
- `llm_wiki/loop/iterations/<iteration_id>/read_log.md`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/similarity_gate.md`

## 成功门禁

- 每张草稿卡都有一个明确分类。
- 每个 `merge_candidate`、`provenance_delta` 或 `duplicate_skip` 都指出对应 existing card。
- 没有把相似门结论写成事实审计结论。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 草稿清单缺失。
- KB 索引缺失。
- 任务包没有列出需要对照的相似卡路径。
