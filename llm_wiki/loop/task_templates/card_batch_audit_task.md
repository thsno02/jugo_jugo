# 任务包模板：批量知识卡审计

- `task_id`:
- `iteration_id`:
- `role`: `card_batch_audit_worker`
- `main_language`: 中文

## 目标

逐张审计一组草稿知识卡是否能进入公开采纳流程。审计结论必须基于任务包指定的知识卡、provenance 和来源证据。

## 允许输入

- 当前任务包。
- `draft_card_paths`:
- `provenance_paths`:
- `source_evidence_paths`:
- `similarity_gate_path`:

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
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/batch_audit_report.md`

## 成功门禁

- 每张卡都有明确审计结论。
- 结论只引用任务包允许输入。
- 没有直接采纳知识卡。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 草稿卡缺失。
- provenance 缺失。
- 来源证据缺失。
- 来源证据与知识卡无法对应。
