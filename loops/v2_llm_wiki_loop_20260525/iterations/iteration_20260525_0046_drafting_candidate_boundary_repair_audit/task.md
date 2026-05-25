# 任务包模板：独立审计

- `task_id`: `task_20260525_0047_drafting_candidate_boundary_repair_audit`
- `iteration_id`: `iteration_20260525_0046_drafting_candidate_boundary_repair_audit`
- `role`: `independent_evaluator`
- `main_language`: 中文

## 目标

独立审计一个执行者任务是否存在上下文泄漏、读写越界、focus drift、证据不足或输出不可恢复的问题。

## 允许输入

- 当前任务包。
- `target_task_path`: `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/task.md`
- `target_status_path`: `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/loop_status.md`
- `target_delivery_path`: `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/loop_delivery.md`
- `target_read_log_path`: `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/read_log.md`
- `target_artifacts`: `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/artifacts/prompt_repair_report.md`
- `changed_system_prompt`: `llm_wiki/loop/system_prompts/card_drafting_worker.md`
- `changed_task_template`: `llm_wiki/loop/task_templates/card_drafting_task.md`
- `failure_evidence_read_log`: `llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases/read_log.md`
- `failure_decision`: `llm_wiki/loop/decisions/20260525-0733-card-drafting-candidate-6-requires-boundary-repair.md`
- `failure_reflection`: `llm_wiki/loop/reflections/20260525-read-boundary-noise-reflection.md`

## 禁止输入

- 父聊天上下文。
- 已有同主题审计报告。
- 未列出的来源材料。
- 执行者没有使用过的额外证据。
- `data/` 来源正文。
- `user-insights/`。
- `legacy/`。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0046_drafting_candidate_boundary_repair_audit/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0046_drafting_candidate_boundary_repair_audit/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0046_drafting_candidate_boundary_repair_audit/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0046_drafting_candidate_boundary_repair_audit/artifacts/independent_audit.md`

## 审计问题

- 执行者是否只使用了任务包允许的输入？
- 是否存在读取外部文件但未记录的情况？
- 是否写入了允许范围之外的文件？
- 输出是否可以仅凭磁盘产物恢复？
- 是否从原子事实卡漂移到枢纽页、聚类或主题覆盖？
- 是否出现英文主语言漂移？
- 是否遗漏 `loop_status.md`、`loop_delivery.md` 或 `read_log.md`？
- 执行者是否承担了主控 agent 才有的采纳或停止决策？
- 修复是否只对应候选 6 `read_log.md` 中的相邻候选字段暴露失败证据？
- 修改范围是否保持最小，没有改变知识卡 schema、审计/采纳链路或引入 hub/cluster/topic coverage？
- 生命周期判断是否合理：本次是否确实不需要 alive sub-agent 常驻？

## 结论格式

```text
audit_result: pass | concern | fail
evidence:
hypotheses:
validated_findings:
required_changes:
```

## 成功门禁

- 先列证据，再给假设，再验证假设。
- 不引用父聊天上下文。
- 不替执行者补写产物。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 目标任务包、状态、交付或读日志缺失，无法独立还原执行边界。
- 允许输入列表为空或与实际审计目标不一致。
- 发现必须读取未授权材料才能判断结论。
- 需要写入允许范围之外的文件才能完成审计。
