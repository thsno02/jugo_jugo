# 任务包模板：知识卡融合审计

- `task_id`:
- `iteration_id`:
- `role`: `card_fusion_audit_worker`
- `main_language`: 中文

## 目标

审计 draft card 与 accepted A 卡之间的融合或 provenance 增量决策。审计重点是三问 provenance 是否成立，以及是否可以把该 provenance 链接回 A 卡 provenance。

## 允许输入

- 当前任务包。
- `draft_card_path`:
- `draft_provenance_path`:
- `comparison_provenance_path`:
- `accepted_card_a_path`:
- `accepted_card_a_provenance_path`:
- `source_evidence_path`:

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
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/fusion_audit_report.md`

## 审计问题

- comparison provenance 是否明确回答三问？
- commonality 是否真的说明 draft card 与 A 卡的共同点？
- difference 是否保留了两张卡的差异，而不是把差异抹平？
- next_action_basis 是否足以支撑 `merge_candidate` 或 `provenance_delta`？
- 拟写入 A 卡 provenance 的链接是否准确、最小、可追踪？
- 是否避免修改 A 卡事实边界，除非任务包明确要求并有来源支撑？

## 成功门禁

- 审计结论明确。
- `merge_candidate` 或 `provenance_delta` 的下一步被批准、要求修订或拒绝。
- 不直接修改 accepted A 卡或 A 卡 provenance。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 缺少 draft card。
- 缺少 comparison provenance。
- 缺少 accepted A 卡或 A 卡 provenance。
- 来源证据无法对应。
