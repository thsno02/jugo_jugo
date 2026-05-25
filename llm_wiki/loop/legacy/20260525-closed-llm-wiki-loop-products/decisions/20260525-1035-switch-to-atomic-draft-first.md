# 切换到 Atomic Draft First

- `timestamp`: `2026-05-25T10:35:24+08:00`
- `decision`: `switch_to_atomic_draft_first`
- `trigger`: 用户指出 7 小时只产出 15 张 accepted card，吞吐明显过低。

## 判断

用户提出的流程能提升效率：先从 exhausted 或已完成 source mining 的来源中批量生成 atomic draft cards，再做相似门和后置 audit/publication。

当前慢点不是单张卡写作本身，而是每张卡都串行经历 drafting、audit、adoption、状态更新、报告更新、decision、commit/push 和 sub-agent 生命周期管理。这个流程对可恢复性很好，但对吞吐不友好。

## 新规则

- 先批量 drafting：每个候选最多生成一张 `status: draft` 的 atomic card 和 provenance。
- 草稿进入 `queues/draft_backlog.md`，不直接进入公开 KB。
- publication 前做相似门，分类为 `new_atomic_card`、`merge_candidate`、`provenance_delta`、`duplicate_skip` 或 `revise_before_gate`。
- `new_atomic_card` 不需要融合审计，但仍需要最终发布审计。
- `merge_candidate` 和 `provenance_delta` 必须审计融合或增量 provenance。
- audit/adoption 改为 batch 推进；单卡失败只拆出该卡。

## 首批约束

首批 batch 限制在 6 个候选以内，来源限定为 `karpathy-x-launch-post` 已完成 source mining 的剩余高价值候选。candidate 11 已产出 draft，登记到 draft backlog，后置进入 publication 批次。

## 风险

新流程本身尚未经过独立审计。为降低风险，首批只改生产顺序，不放宽事实来源、provenance、draft/accepted 状态边界，也不取消最终 publication audit。
