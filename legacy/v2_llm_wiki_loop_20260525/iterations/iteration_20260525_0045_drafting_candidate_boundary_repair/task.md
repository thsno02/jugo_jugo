# 候选块读取边界修复任务

- `task_id`: `task_20260525_0046_drafting_candidate_boundary_repair`
- `iteration_id`: `iteration_20260525_0045_drafting_candidate_boundary_repair`
- `role`: `prompt_template_repair`
- `main_language`: 中文

## 目标

根据候选 6 drafting 的失败证据，对 `card_drafting_worker` prompt 和 `card_drafting_task` template 做最小修复：要求后续 drafting worker 读取 `fact_candidates.md` 时只读取任务指定的单个候选块，避免相邻候选字段被检索上下文带出。

## 允许输入

- 当前任务包。
- `failure_evidence_read_log`: `llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases/read_log.md`
- `failure_decision`: `llm_wiki/loop/decisions/20260525-0733-card-drafting-candidate-6-requires-boundary-repair.md`
- `failure_reflection`: `llm_wiki/loop/reflections/20260525-read-boundary-noise-reflection.md`
- `system_prompt_path`: `llm_wiki/loop/system_prompts/card_drafting_worker.md`
- `task_template_path`: `llm_wiki/loop/task_templates/card_drafting_task.md`

## 禁止输入

- 父聊天上下文。
- `data/` 来源正文。
- `user-insights/`。
- `legacy/`。
- 旧审计报告。
- 未列出的技能、prompt 或任务模板。

## 允许写入

- `llm_wiki/loop/system_prompts/card_drafting_worker.md`
- `llm_wiki/loop/task_templates/card_drafting_task.md`
- `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/artifacts/prompt_repair_report.md`

## 修复原则

- 只修复候选块读取边界问题。
- 不改变 atomic fact card schema。
- 不新增 hub、cluster、topic coverage 或复杂 metadata。
- 不重写候选 6 草稿卡正文或 provenance。
- 保持 sub-agent 生命周期策略：本次修复不是大规模来源 I/O，不创建 alive sub-agent。

## 成功门禁

- 修复能追溯到候选 6 `read_log.md` 和复开反思。
- 改动只落在 `card_drafting_worker.md` 和 `card_drafting_task.md` 的候选读取规则。
- `validate_scope.py` 对本任务包返回 `scope_validation: pass`。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 和 `artifacts/prompt_repair_report.md` 都存在。

## 阻塞条件

- 需要改变知识卡 schema。
- 需要重写候选 6 草稿卡。
- 修复需要扩展到多个 worker 角色但本任务未授权。
- 需要人类决定是否改为 hub、cluster 或 topic coverage。
