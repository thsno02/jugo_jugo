# 显式修复任务：validate_scope 输入路径检查

- `task_id`: `task_20260525_0039_validate_scope_path_check_repair`
- `iteration_id`: `iteration_20260525_0038_validate_scope_path_check_repair`
- `role`: `tooling_repair`
- `main_language`: 中文

## 目标

根据候选 1 audit 暴露的失败证据，最小修复 `validate_scope.py`：当任务包 `## 允许输入` 区列出必须可读的本地路径且该路径不存在时，scope validation 必须失败。

## 失败证据

- `llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/task.md` 中 `fact_candidate_path` 指向不存在的 `llm_wiki/loop/iterations/iteration_20260525_0001_source_mining_karpathy_gist/artifacts/fact_candidates.md`。
- `llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/read_log.md` 记录该路径读取失败。
- `validate_scope.py` 在派发前仍返回 `scope_validation: pass`。

## 允许输入

- 当前任务包。
- `failure_decision_path`: `llm_wiki/loop/decisions/20260525-0641-card-audit-pass-candidate-1-with-task-path-risk.md`
- `bad_task_path`: `llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/task.md`
- `valid_task_path`: `llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file/task.md`
- `tool_path`: `llm_wiki/loop/tools/validate_scope.py`

## 禁止输入

- 父聊天上下文。
- `legacy/`。
- `user-insights/`，本任务不需要人类 recall。
- 与本次路径校验失败无关的旧审计报告。

## 允许写入

- `llm_wiki/loop/tools/validate_scope.py`
- `llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/artifacts/tooling_repair_report.md`

## 修复范围

- 只增加 `## 允许输入` 区本地路径存在性检查。
- 不改变 role/template/schema。
- 不要求 `target_card_path` 和 `target_provenance_path` 预先存在，因为 adoption 任务会用它们做存在性和覆盖冲突检查。
- 不检查 `## 允许写入` 区路径是否存在。

## 验证要求

- 负向检查：`python3 llm_wiki/loop/tools/validate_scope.py llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/task.md` 必须失败，并指出 missing input path。
- 正向检查：`python3 llm_wiki/loop/tools/validate_scope.py llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file/task.md` 必须通过。
- `python3 -m py_compile llm_wiki/loop/tools/validate_scope.py` 必须通过。

## 成功门禁

- 修复报告说明改了什么、失败证据是什么、验证结果是什么、剩余风险是什么。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。
- `loop_delivery.md` 必须包含 `LOOP_DONE` 或 `LOOP_BLOCKED`。

## 阻塞条件

- 无法在不扩大 schema/role/template 的情况下修复。
- 修复会让既有有效任务包错误失败。
