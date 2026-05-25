# 任务包模板：批量知识卡采纳

- `task_id`:
- `iteration_id`:
- `role`: `card_batch_adoption_worker`
- `main_language`: 中文

## 目标

把审计通过的一组草稿知识卡采纳到 `llm_wiki/kb/`。采纳只做文件移动、轻量整理和最小索引更新，不做扩写。

## 允许输入

- 当前任务包。
- `draft_card_paths`:
- `provenance_paths`:
- `batch_audit_report_path`:
- `target_index_path`: `llm_wiki/kb/indexes/cards.md`，仅用于保留既有最小索引内容并做增量更新。
- `target_card_paths`: 仅用于存在性和覆盖冲突检查。
- `target_provenance_paths`: 仅用于存在性和覆盖冲突检查。

## 禁止输入

- 父聊天上下文。
- 没有通过审计的知识卡。
- 未列出的来源。
- 旧版 `legacy/` 知识库。
- 枢纽页、聚类页或主题覆盖文档。

## 允许写入

- `llm_wiki/kb/cards/`
- `llm_wiki/kb/provenance/`
- `llm_wiki/kb/indexes/cards.md`
- `llm_wiki/loop/iterations/<iteration_id>/loop_status.md`
- `llm_wiki/loop/iterations/<iteration_id>/loop_delivery.md`
- `llm_wiki/loop/iterations/<iteration_id>/read_log.md`

## 成功门禁

- 每张采纳卡落在 `llm_wiki/kb/cards/`。
- 每份 provenance 落在 `llm_wiki/kb/provenance/`。
- 最小索引包含卡片标题、路径、状态和来源。
- 冲突或非 pass 卡被清楚记录，未静默覆盖。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 批量审计报告缺失。
- 没有任何 `audit_result: pass` 的卡。
- 所有 pass 卡都会覆盖已有不同内容。
