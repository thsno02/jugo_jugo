# read_log

- path: `llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/task.md`
  - reason: 当前修复任务包。
  - use: 确认失败证据、允许输入、允许写入、修复范围和验证要求。
- path: `llm_wiki/loop/decisions/20260525-0641-card-audit-pass-candidate-1-with-task-path-risk.md`
  - reason: 任务指定失败证据。
  - use: 确认 audit task 的错误 `fact_candidate_path` 与 repair 触发理由。
- path: `llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/task.md`
  - reason: 任务指定 bad task。
  - use: 作为负向验证样例，确认修复后会报告 `missing_input_path`。
- path: `llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file/task.md`
  - reason: 任务指定 valid task。
  - use: 作为正向验证样例，确认修复不误伤已有有效任务包。
- path: `llm_wiki/loop/tools/validate_scope.py`
  - reason: 任务指定待修复工具。
  - use: 增加 `## 允许输入` 区本地路径存在性检查。
