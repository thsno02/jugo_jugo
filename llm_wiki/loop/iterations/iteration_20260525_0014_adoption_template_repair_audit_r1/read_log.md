# read_log

## 工具性检查

- path: `llm_wiki/loop/iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/`
  - reason: 启动前确认允许写入目录存在。
  - use: 仅用于落盘准备，不作为审计证据。
- path: `llm_wiki/loop/iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/loop_status.md`
  - reason: 确认本轮状态文件是否已存在。
  - use: 避免初始化时误覆盖已有产物。
- path: `llm_wiki/loop/iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/read_log.md`
  - reason: 确认本轮读日志是否已存在。
  - use: 避免初始化时误覆盖已有产物。
- path: `llm_wiki/loop/iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/loop_delivery.md`
  - reason: 确认本轮交付文件是否已存在。
  - use: 避免初始化时误覆盖已有产物。
- path: `llm_wiki/loop/iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/artifacts/independent_audit.md`
  - reason: 确认本轮审计报告是否已存在。
  - use: 避免初始化时误覆盖已有产物。

## 任务包允许输入

- path: `llm_wiki/loop/iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/task.md`
  - reason: 当前独立审计任务包。
  - use: 确认允许输入、禁止输入、允许写入、审计问题和结论格式。
- path: `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/task.md`
  - reason: 目标执行者任务包。
  - use: 确认目标任务允许输入、禁止输入、允许写入和成功门禁。
- path: `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/loop_status.md`
  - reason: 目标执行者状态产物。
  - use: 检查目标任务状态和是否可恢复。
- path: `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/loop_delivery.md`
  - reason: 目标执行者交付产物。
  - use: 检查目标任务结果、门禁声明和是否越权决策。
- path: `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/read_log.md`
  - reason: 目标执行者读日志。
  - use: 对照目标任务允许输入，检查是否存在外部读取或未记录读取迹象。
- path: `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/artifacts/template_repair_report.md`
  - reason: 目标执行者修复报告。
  - use: 检查修复证据、改动范围、剩余风险和是否 focus drift。
- path: `llm_wiki/loop/task_templates/card_adoption_task.md`
  - reason: 目标执行者修改后的任务模板。
  - use: 检查模板修复是否局限于目标 KB 路径读取边界。

## 支持证据

- path: `llm_wiki/loop/iterations/iteration_20260525_0008_card_adoption_raw_sources_truth/read_log.md`
  - reason: 当前任务包列出的支持证据，且目标执行者读日志声明使用过。
  - use: 验证失败证据是否支持本次模板修复。
- path: `llm_wiki/loop/iterations/iteration_20260525_0011_card_adoption_architecture_layers/read_log.md`
  - reason: 当前任务包列出的支持证据，且目标执行者读日志声明使用过。
  - use: 验证失败证据是否支持本次模板修复。
