# 决策：候选 8 drafting revision 可进入审计

- `time`: `2026-05-25T03:01:31+08:00`
- `iteration`: `iteration_20260525_0006_card_drafting_raw_sources_truth_r1`
- `task_id`: `task_20260525_0007_card_drafting_candidate_8_r1`
- `decision`: `ready_for_card_audit`

## 证据

- `inspect_delivery.py iteration_20260525_0006_card_drafting_raw_sources_truth_r1` 返回 `delivery_inspection: pass`。
- `loop_delivery.md` 文件内包含 `LOOP_DONE`，验证了 delivery marker prompt 修复在后续 worker 中生效。
- `read_log.md` 记录未读取上一轮失败 drafting 产物、旧审计报告、`legacy/` 或其它来源。
- `draft_card.md` 保持 `status: draft`，且 `References` 在 `Footnotes` 前，`Footnotes` 是最后一个 section。
- `provenance.md` 明确说明事实来源、支撑关系、明说内容、整理表述、成立范围和 draft 原因。
- drafting revision worker 完成后已关闭；本轮没有保留无用途的 sub-agent。

## 生命周期说明

当前关闭该 drafting worker 是因为它的职责已经结束，且下一步审计必须独立。后续如果出现反复读取同一大来源或同一数据域的任务，可以创建明确职责的 alive sub-agent 来降低重复 IO 和上下文消耗；但该策略需要写入任务包或决策，不能隐式复用上下文。

## 下一步

创建 `card_audit_worker` 任务包，审计本轮 `draft_card.md` 和 `provenance.md` 是否可进入采纳流程。主控 agent 不亲自审计或采纳。
