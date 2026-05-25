# 任务包模板：技能演化

- `task_id`:
- `iteration_id`:
- `role`: `skill_evolution_worker`
- `main_language`: 中文

## 目标

根据循环失败证据，对技能或任务模板做最小修复。技能演化必须服务于当前 scoped knowledge card 循环，不服务于枢纽页、聚类或主题覆盖。

## 允许输入

- 当前任务包。
- `failure_evidence_path`:
- `skill_path`:
- 可选 `task_template_path`:

## 禁止输入

- 父聊天上下文。
- 与本次失败无关的旧审计报告。
- 未列出的技能文件。

## 允许写入

- `llm_wiki/skills/<skill_name>/SKILL.md`
- `llm_wiki/loop/task_templates/<template_name>.md`
- `llm_wiki/loop/iterations/<iteration_id>/loop_status.md`
- `llm_wiki/loop/iterations/<iteration_id>/loop_delivery.md`
- `llm_wiki/loop/iterations/<iteration_id>/read_log.md`
- `llm_wiki/loop/iterations/<iteration_id>/artifacts/skill_change_report.md`

## 修复原则

- 只修复证据中出现的问题。
- 优先删掉多余步骤，而不是增加复杂流程。
- 保持中文主语言。
- 保持 scoped knowledge card 为当前唯一生产目标。
- 不新增枢纽页、聚类或主题覆盖流程。

## 成功门禁

- 每个改动都能追溯到一个失败证据。
- 技能文件仍能通过技能校验。
- 修复报告说明改了什么、为什么改、剩余风险是什么。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 缺少失败证据。
- 需要人类在设计层面取舍。
- 修复会影响多个技能但任务包只授权一个技能。
