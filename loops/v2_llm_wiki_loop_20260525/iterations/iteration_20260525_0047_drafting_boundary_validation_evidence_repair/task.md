# 候选块读取边界修复 validation evidence correction

- `task_id`: `task_20260525_0048_drafting_boundary_validation_evidence_repair`
- `iteration_id`: `iteration_20260525_0047_drafting_boundary_validation_evidence_repair`
- `role`: `prompt_repair_validation_evidence`
- `main_language`: 中文

## 目标

根据 `independent_evaluator` 的 concern，补写候选块读取边界 prompt/template repair 的实际 validation result evidence，使修复任务的成功门禁可从磁盘恢复。

## 允许输入

- 当前任务包。
- `audit_concern_report`: `llm_wiki/loop/iterations/iteration_20260525_0046_drafting_candidate_boundary_repair_audit/artifacts/independent_audit.md`
- `audit_concern_decision`: `llm_wiki/loop/decisions/20260525-0747-drafting-boundary-repair-audit-concern.md`
- `target_repair_task`: `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/task.md`
- `target_repair_delivery`: `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/loop_delivery.md`
- `target_repair_report`: `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/artifacts/prompt_repair_report.md`

## 禁止输入

- 父聊天上下文。
- `data/` 来源正文。
- `user-insights/`。
- `legacy/`。
- 与该 validation evidence concern 无关的旧审计报告。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/artifacts/prompt_repair_report.md`
- `llm_wiki/loop/iterations/iteration_20260525_0047_drafting_boundary_validation_evidence_repair/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0047_drafting_boundary_validation_evidence_repair/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0047_drafting_boundary_validation_evidence_repair/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0047_drafting_boundary_validation_evidence_repair/artifacts/validation_evidence_report.md`

## 修复原则

- 只补写实际 validation result evidence。
- 不改 `card_drafting_worker.md` 或 `card_drafting_task.md` 的修复内容。
- 不修改候选 6 草稿卡或 provenance。
- 不读取 `data/` 来源正文。
- 不引入 hub、cluster、topic coverage 或复杂 metadata。

## 成功门禁

- 记录 `validate_scope.py` 的实际命令和输出。
- 记录 `inspect_delivery.py` 的实际命令和输出。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 和 `artifacts/validation_evidence_report.md` 都存在。
- 后续重新派发 `independent_evaluator` 审计该 correction。

## 阻塞条件

- `validate_scope.py` 不通过。
- `inspect_delivery.py` 不通过。
- 需要改动 prompt/template 正文才能关闭 concern。
- 需要人类决定是否重做候选 6 drafting。
