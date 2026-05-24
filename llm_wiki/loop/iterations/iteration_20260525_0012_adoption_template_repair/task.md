# 明确修复任务：adoption 目标路径读取边界

- `task_id`: `task_20260525_0013_adoption_template_repair`
- `iteration_id`: `iteration_20260525_0012_adoption_template_repair`
- `role`: `main_agent_control_plane_repair`
- `main_language`: 中文

## 目标

根据两次 adoption worker 的重复 read_log 证据，对 `card_adoption_task.md` 做最小修复：显式允许读取目标 KB 卡片、目标 provenance 和索引文件，用于存在性检查、覆盖冲突检查和保留索引内容。

## 失败证据

- `llm_wiki/loop/iterations/iteration_20260525_0008_card_adoption_raw_sources_truth/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0011_card_adoption_architecture_layers/read_log.md`
- 两者都把目标 KB 卡片、目标 provenance 和 `llm_wiki/kb/indexes/cards.md` 记录为额外读取。

## 允许输入

- 当前任务包。
- `llm_wiki/loop/task_templates/card_adoption_task.md`
- `llm_wiki/loop/iterations/iteration_20260525_0008_card_adoption_raw_sources_truth/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0011_card_adoption_architecture_layers/read_log.md`

## 禁止输入

- 父聊天上下文中的事实内容。
- `legacy/`。
- `user-insights/`。
- 未列出的来源正文。

## 允许写入

- `llm_wiki/loop/task_templates/card_adoption_task.md`
- `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/artifacts/template_repair_report.md`

## 成功门禁

- 只修改 `card_adoption_task.md` 中与目标 KB 路径读取有关的边界说明。
- 不扩大 adoption worker 到 hub、cluster、topic coverage 或批量采纳。
- 修复报告说明失败证据、改动内容和剩余风险。
- 本 iteration 的 `loop_delivery.md` 包含 `LOOP_DONE` 或 `LOOP_BLOCKED`。

## 阻塞条件

- 需要改变 KB schema、card schema 或角色体系。
- 修复需要改动多个 role prompt 才能成立。
