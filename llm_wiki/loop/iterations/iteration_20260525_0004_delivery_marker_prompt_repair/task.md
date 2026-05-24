# 明确修复任务：worker 交付 marker 规则

- `task_id`: `task_20260525_0005_delivery_marker_prompt_repair`
- `iteration_id`: `iteration_20260525_0004_delivery_marker_prompt_repair`
- `role`: `main_agent_control_plane_repair`
- `main_language`: 中文

## 目标

根据一次具体失败证据，对 worker 基础 prompt 做最小修复，使后续执行者知道 `loop_delivery.md` 本身必须包含 `LOOP_DONE` 或 `LOOP_BLOCKED` 标记。

## 失败证据

- `inspect_delivery.py iteration_20260525_0003_card_drafting_raw_sources_truth` 返回 `delivery_inspection: fail`。
- 失败原因为 `missing: LOOP_DONE_or_LOOP_BLOCKED`。
- 目标 iteration 的 `loop_delivery.md` 存在，但只写了 `status: done`，没有写入检查器要求的 marker。
- 执行者最终回复以 `LOOP_DONE` 开头，但磁盘交付文件不满足可恢复检查。

## 允许输入

- 当前任务包。
- `llm_wiki/loop/tools/inspect_delivery.py`
- `llm_wiki/loop/system_prompts/base_worker.md`
- `llm_wiki/loop/iterations/iteration_20260525_0003_card_drafting_raw_sources_truth/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0003_card_drafting_raw_sources_truth/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0003_card_drafting_raw_sources_truth/read_log.md`

## 禁止输入

- 父聊天上下文中的事实内容。
- `legacy/`。
- `user-insights/`。
- 未列出的来源正文。

## 允许写入

- `llm_wiki/loop/system_prompts/base_worker.md`
- `llm_wiki/loop/iterations/iteration_20260525_0004_delivery_marker_prompt_repair/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0004_delivery_marker_prompt_repair/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0004_delivery_marker_prompt_repair/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0004_delivery_marker_prompt_repair/artifacts/prompt_repair_report.md`

## 成功门禁

- 只修改 `base_worker.md` 中与交付 marker 有关的规则。
- 不修改知识卡正文、provenance 或来源证据。
- 修复报告说明失败证据、改动内容和剩余风险。
- 本 iteration 的 `loop_delivery.md` 必须包含 `LOOP_DONE` 或 `LOOP_BLOCKED`。

## 阻塞条件

- 需要改变 KB schema、card schema 或角色体系。
- 需要重写 worker 产物才能证明修复有效。
