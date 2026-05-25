# 任务包模板：独立审计

- `task_id`: `task_20260525_0040_validate_scope_path_check_repair_audit`
- `iteration_id`: `iteration_20260525_0039_validate_scope_path_check_repair_audit`
- `role`: `independent_evaluator`
- `main_language`: 中文

## 目标

独立审计 `validate_scope.py` 路径检查修复是否对应失败证据、范围最小、验证充分，并确认该修复没有扩大知识卡生产 scope。

## 允许输入

- 当前任务包。
- `target_task_path`: `llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/task.md`
- `target_status_path`: `llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/loop_status.md`
- `target_delivery_path`: `llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/loop_delivery.md`
- `target_read_log_path`: `llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/read_log.md`
- `target_artifacts`: `llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/artifacts/tooling_repair_report.md`
- `target_tool_path`: `llm_wiki/loop/tools/validate_scope.py`
- `failure_decision_path`: `llm_wiki/loop/decisions/20260525-0641-card-audit-pass-candidate-1-with-task-path-risk.md`
- `bad_task_path`: `llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/task.md`
- `valid_task_path`: `llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file/task.md`

## 禁止输入

- 父聊天上下文。
- 已有同主题审计报告。
- 未列出的来源材料。
- 执行者没有使用过的额外证据。
- `legacy/`。
- `user-insights/`。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0039_validate_scope_path_check_repair_audit/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0039_validate_scope_path_check_repair_audit/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0039_validate_scope_path_check_repair_audit/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0039_validate_scope_path_check_repair_audit/artifacts/independent_audit.md`

## 审计问题

- 执行者是否只使用了任务包允许的输入？
- 是否存在读取外部文件但未记录的情况？
- 是否写入了允许范围之外的文件？
- 输出是否可以仅凭磁盘产物恢复？
- 是否从原子事实卡漂移到枢纽页、聚类或主题覆盖？
- 是否出现英文主语言漂移？
- 是否遗漏 `loop_status.md`、`loop_delivery.md` 或 `read_log.md`？
- 执行者是否承担了主控 agent 才有的采纳或停止决策？
- 修复是否只针对 `fact_candidate_path` 不存在但校验通过这一失败证据？
- 修复是否避免检查 adoption 目标卡片/目标 provenance 这类采纳前可能不存在的路径？

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
