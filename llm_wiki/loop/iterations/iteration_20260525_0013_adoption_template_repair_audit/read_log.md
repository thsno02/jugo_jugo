## 额外流程指令读取

- 路径：`/Users/lw/.codex/skills/agent-loop-runner/SKILL.md`
  - 原因：当前任务明确属于 loop 执行/审计工作流，外层工具规则要求使用该技能。
  - 用途：仅用于确认执行流程约束，不作为目标任务审计证据。

## 任务允许输入读取

- 路径：`llm_wiki/loop/iterations/iteration_20260525_0013_adoption_template_repair_audit/task.md`
  - 原因：当前审计任务包。
  - 用途：确认允许输入、允许写入、审计问题、成功门禁和阻塞条件。
- 路径：`llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/task.md`
  - 原因：目标执行者任务包。
  - 用途：确认目标执行者的边界与交付要求。
- 路径：`llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/loop_status.md`
  - 原因：目标执行者状态产物。
  - 用途：检查状态是否存在且可恢复。
- 路径：`llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/loop_delivery.md`
  - 原因：目标执行者交付产物。
  - 用途：检查完成标记、输出摘要与恢复性。
- 路径：`llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/read_log.md`
  - 原因：目标执行者读日志。
  - 用途：核对实际读取与任务允许输入是否一致。
- 路径：`llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/artifacts/template_repair_report.md`
  - 原因：目标执行者报告产物。
  - 用途：审计证据链、focus、语言和是否越权决策。
- 路径：`llm_wiki/loop/task_templates/card_adoption_task.md`
  - 原因：目标执行者修改的任务模板产物。
  - 用途：审计写入结果是否符合目标边界。
- 路径：`llm_wiki/loop/reflections/20260525-small-batch-adoption-template-reflection.md`
  - 原因：目标执行者修改的反思产物。
  - 用途：审计是否存在越权采纳或停止决策。
- 路径：`llm_wiki/loop/iterations/iteration_20260525_0008_card_adoption_raw_sources_truth/read_log.md`
  - 原因：目标任务允许的参考读日志产物。
  - 用途：审计模板修复是否基于目标执行者使用过的证据范围。
- 路径：`llm_wiki/loop/iterations/iteration_20260525_0011_card_adoption_architecture_layers/read_log.md`
  - 原因：目标任务允许的参考读日志产物。
  - 用途：审计模板修复是否基于目标执行者使用过的证据范围。

