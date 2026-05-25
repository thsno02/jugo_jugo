# 任务包模板：独立审计

- `task_id`: `task_20260525_0015_adoption_template_repair_audit_r1`
- `iteration_id`: `iteration_20260525_0014_adoption_template_repair_audit_r1`
- `role`: `independent_evaluator`
- `main_language`: 中文

## 目标

独立审计一个执行者任务是否存在上下文泄漏、读写越界、focus drift、证据不足或输出不可恢复的问题。

## 允许输入

- 当前任务包。
- `target_task_path`: `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/task.md`
- `target_status_path`: `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/loop_status.md`
- `target_delivery_path`: `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/loop_delivery.md`
- `target_read_log_path`: `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/read_log.md`
- `target_artifacts`:
  - `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/artifacts/template_repair_report.md`
  - `llm_wiki/loop/task_templates/card_adoption_task.md`

## 支持证据

以下文件只用于理解失败背景，不是目标执行者产物，不用于判断目标执行者写入范围：

- `llm_wiki/loop/reflections/20260525-small-batch-adoption-template-reflection.md`
- `llm_wiki/loop/iterations/iteration_20260525_0008_card_adoption_raw_sources_truth/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0011_card_adoption_architecture_layers/read_log.md`
- `llm_wiki/loop/decisions/20260525-0348-adoption-template-audit-concern-resolution.md`

## 禁止输入

- 父聊天上下文。
- 已有同主题审计报告。
- 未列出的来源材料。
- 执行者没有使用过的额外证据。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/artifacts/independent_audit.md`

## 审计问题

- 执行者是否只使用了任务包允许的输入？
- 是否存在读取外部文件但未记录的情况？
- 是否写入了允许范围之外的文件？
- 输出是否可以仅凭磁盘产物恢复？
- 是否从原子事实卡漂移到枢纽页、聚类或主题覆盖？
- 是否出现英文主语言漂移？
- 是否遗漏 `loop_status.md`、`loop_delivery.md` 或 `read_log.md`？
- 执行者是否承担了主控 agent 才有的采纳或停止决策？

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
