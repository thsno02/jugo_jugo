# 任务包模板：知识卡融合采纳

- `task_id`:
- `iteration_id`:
- `role`: `card_fusion_adoption_worker`
- `main_language`: 中文

## 目标

在融合审计通过后，把 comparison provenance 或 provenance delta 链接回 accepted A 卡 provenance。默认不改 A 卡正文。

## 允许输入

- 当前任务包。
- `draft_card_path`:
- `draft_provenance_path`:
- `comparison_provenance_path`:
- `fusion_audit_report_path`:
- `accepted_card_a_path`: 仅在任务包明确授权时可做最小正文改动。
- `accepted_card_a_provenance_path`:

## 禁止输入

- 父聊天上下文。
- 没有 `fusion_audit_result: pass` 的融合决策。
- 未列出的来源。
- 未列出的 KB 卡片。
- 旧版 `legacy/` 知识库。

## 允许写入

- `accepted_card_a_provenance_path`
- `accepted_card_a_path`，仅限任务包明确授权并且 fusion audit 批准的最小正文改动。
- `llm_wiki/loop/iterations/<iteration_id>/loop_status.md`
- `llm_wiki/loop/iterations/<iteration_id>/loop_delivery.md`
- `llm_wiki/loop/iterations/<iteration_id>/read_log.md`

## 成功门禁

- A 卡 provenance 增加了指向 comparison provenance 和 fusion audit report 的链接。
- 更新内容回答或链接到三问 provenance。
- 如修改 A 卡正文，保留固定 metadata 并更新 `edited_time` / `edited_entity`。
- 未静默覆盖 A 卡原有 provenance。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- fusion audit 未通过。
- A 卡 provenance 缺失。
- 目标文件内容冲突，无法最小更新。
