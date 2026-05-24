# read_log

- path: `llm_wiki/loop/iterations/iteration_20260525_0004_delivery_marker_prompt_repair/task.md`
  - reason: 当前明确修复任务。
  - use: 确认失败证据、允许输入、允许写入和成功门禁。
- path: `llm_wiki/loop/tools/inspect_delivery.py`
  - reason: 失败检查器。
  - use: 确认检查器在 `loop_delivery.md` 中查找 `LOOP_DONE` 或 `LOOP_BLOCKED`。
- path: `llm_wiki/loop/system_prompts/base_worker.md`
  - reason: 本次允许修复的 worker 基础 prompt。
  - use: 添加交付文件 marker 要求。
- path: `llm_wiki/loop/iterations/iteration_20260525_0003_card_drafting_raw_sources_truth/loop_delivery.md`
  - reason: 失败证据。
  - use: 确认该文件存在但缺少 `LOOP_DONE` 或 `LOOP_BLOCKED`。
- path: `llm_wiki/loop/iterations/iteration_20260525_0003_card_drafting_raw_sources_truth/loop_status.md`
  - reason: 失败上下文。
  - use: 确认目标 iteration 状态文件存在。
- path: `llm_wiki/loop/iterations/iteration_20260525_0003_card_drafting_raw_sources_truth/read_log.md`
  - reason: 失败上下文。
  - use: 确认目标 iteration 有读日志，问题集中在交付 marker。
