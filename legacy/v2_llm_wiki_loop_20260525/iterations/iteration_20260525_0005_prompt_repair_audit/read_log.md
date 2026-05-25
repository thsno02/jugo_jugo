# read_log

| path | reason | use |
|---|---|---|
| /Users/lw/.codex/skills/agent-loop-runner/SKILL.md | 会话开发者指令要求在 loop 审计任务中使用该 skill | 仅用于执行流程约束，不作为目标执行者审计证据 |
| llm_wiki/loop/iterations/iteration_20260525_0005_prompt_repair_audit/task.md | 当前审计任务包 | 确认允许输入、允许写入、审计问题、结论格式和阻塞条件 |
| llm_wiki/loop/iterations/iteration_20260525_0004_delivery_marker_prompt_repair/task.md | 目标任务包 | 确认目标执行者的任务目标、允许输入、禁止输入、允许写入和成功门禁 |
| llm_wiki/loop/iterations/iteration_20260525_0004_delivery_marker_prompt_repair/loop_status.md | 目标状态文件 | 检查目标任务状态、结果 marker 和修复范围声明 |
| llm_wiki/loop/iterations/iteration_20260525_0004_delivery_marker_prompt_repair/loop_delivery.md | 目标交付文件 | 检查目标交付是否包含 `LOOP_DONE`、是否声明实际修复与后续事项 |
| llm_wiki/loop/iterations/iteration_20260525_0004_delivery_marker_prompt_repair/read_log.md | 目标读日志 | 检查目标执行者声明读取是否与目标任务包允许输入一致 |
| llm_wiki/loop/iterations/iteration_20260525_0004_delivery_marker_prompt_repair/artifacts/prompt_repair_report.md | 目标修复报告 | 检查失败证据、改动内容、最小修改声明和剩余风险 |
| llm_wiki/loop/system_prompts/base_worker.md | 目标允许写入产物之一 | 检查 marker 规则是否存在，以及是否保留输入、写入、语言和内容边界 |
| llm_wiki/loop/tools/inspect_delivery.py | 目标允许输入与检查器 | 检查 delivery marker 的标准验收逻辑，并运行检查器验证目标 iteration |
