# 任务包模板：独立审计

- `task_id`:
- `iteration_id`:
- `role`: `independent_evaluator`
- `main_language`: 中文

## 目标

独立审计一个执行者任务是否存在上下文泄漏、读写越界、focus drift、证据不足或输出不可恢复的问题。

## 允许输入

- 当前任务包。
- `target_task_path`:
- `target_status_path`:
- `target_delivery_path`:
- `target_read_log_path`:
- `target_artifacts`:

## 禁止输入

- 父聊天上下文。
- 已有同主题审计报告。
- 未列出的来源材料。
- 执行者没有使用过的额外证据。

## 允许写入

- `llm_wiki/loop/iterations/<iteration_id>/loop_status.md`
- `llm_wiki/loop/iterations/<iteration_id>/loop_delivery.md`
- `llm_wiki/loop/iterations/<iteration_id>/read_log.md`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/independent_audit.md`

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
