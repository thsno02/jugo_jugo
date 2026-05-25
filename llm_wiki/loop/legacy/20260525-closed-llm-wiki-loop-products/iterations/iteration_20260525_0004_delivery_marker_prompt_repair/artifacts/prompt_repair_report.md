# prompt 修复报告：交付文件 marker

## 失败证据

`inspect_delivery.py iteration_20260525_0003_card_drafting_raw_sources_truth` 返回失败，原因是 `loop_delivery.md` 中缺少 `LOOP_DONE` 或 `LOOP_BLOCKED`。该 iteration 的执行者最终回复包含 `LOOP_DONE`，但磁盘交付文件只写了 `status: done`，导致恢复者无法仅凭标准检查器验收该轮。

## 修改内容

修改 `llm_wiki/loop/system_prompts/base_worker.md` 的状态规则，把结束前必须写的 `loop_delivery.md` 明确改为：`loop_delivery.md` 文件中也必须写入 `LOOP_DONE` 或 `LOOP_BLOCKED`。

## 为什么是最小修改

失败来自 prompt 与检查器之间的契约不一致：检查器检查磁盘交付文件，prompt 只明确要求最终回复带 marker。修复只补齐这条交付契约，没有改变 worker 的输入权限、写入权限、事实来源规则、KB schema 或知识卡格式。

## 剩余风险

已经失败的 `iteration_20260525_0003_card_drafting_raw_sources_truth` 不应由主控 agent 手工改写。后续需要重新派发一个 drafting revision，确认新 prompt 下的 worker 交付能通过 `inspect_delivery.py`，再进入 card audit。
