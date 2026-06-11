# read_log

| path | reason | purpose |
| --- | --- | --- |
| ~/.codex/skills/agent-loop-runner/SKILL.md | 任务属于循环执行/审计工作，按运行环境技能规则读取 | 仅用于执行流程约束，不作为审计证据 |
| llm_wiki/loop/iterations/iteration_20260525_0039_validate_scope_path_check_repair_audit/task.md | 当前任务包 | 确认审计目标、允许输入、禁止输入、允许写入和结论格式 |
| llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/task.md | 任务包允许输入 target_task_path | 还原被审计执行者任务边界 |
| llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/loop_status.md | 任务包允许输入 target_status_path | 核查被审计执行者状态与工作范围 |
| llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/loop_delivery.md | 任务包允许输入 target_delivery_path | 核查被审计执行者交付与验证结论 |
| llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/read_log.md | 任务包允许输入 target_read_log_path | 核查被审计执行者读取是否越界或未记录 |
| llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/artifacts/tooling_repair_report.md | 任务包允许输入 target_artifacts | 核查修复证据、范围和验证 |
| llm_wiki/loop/tools/validate_scope.py | 任务包允许输入 target_tool_path | 核查实际工具修复是否最小且未扩大生产 scope |
| llm_wiki/loop/decisions/20260525-0641-card-audit-pass-candidate-1-with-task-path-risk.md | 任务包允许输入 failure_decision_path | 核查失败证据是否为 fact_candidate_path 缺失但校验通过 |
| llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/task.md | 任务包允许输入 bad_task_path | 核查负例路径语义和失败复现目标 |
| llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file/task.md | 任务包允许输入 valid_task_path | 核查正例路径语义和回归验证目标 |

## 验证命令

- `python3 -B llm_wiki/loop/tools/validate_scope.py llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/task.md`
- `python3 -B llm_wiki/loop/tools/validate_scope.py llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file/task.md`
- `python3 -B llm_wiki/loop/tools/validate_scope.py llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/task.md`

以上命令只读取已登记的 `target_tool_path`、`bad_task_path`、`valid_task_path` 和 `target_task_path`。
