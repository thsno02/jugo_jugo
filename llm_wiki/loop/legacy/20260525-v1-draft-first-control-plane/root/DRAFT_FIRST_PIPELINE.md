# Atomic Draft First 流程

本流程用于修正单卡串行生产过慢的问题。目标是先把来源材料转成可追踪的原子草稿卡，再把融合、审计和公开发布放到后置批处理。

## 核心顺序

```text
已挖掘来源 / exhausted 来源
-> 批量 atomic draft
-> 相似卡门禁
-> draft backlog
-> 批量 audit
-> public adoption
```

## 阶段定义

1. `batch_atomic_draft`
   - 对一个已完成 source mining 的来源，按候选列表批量生成草稿卡和草稿 provenance。
   - 每个候选最多产出一张原子卡；不清楚的候选写入 `batch_manifest.md` 的 skip/block 记录。
   - 草稿只保留 `status: draft`，不进入 `llm_wiki/kb/cards/`。

2. `similarity_gate`
   - 读取草稿卡、`llm_wiki/kb/indexes/cards.md` 和任务包指定的相似 accepted card。
   - 只判断知识身份关系，不做事实审计。
   - 输出分类：`new_atomic_card`、`merge_candidate`、`provenance_delta`、`duplicate_skip`、`revise_before_gate`。

3. `draft_backlog`
   - `llm_wiki/loop/queues/draft_backlog.md` 是非公开草稿的恢复入口。
   - backlog 记录草稿路径、provenance 路径、来源候选、相似门结果、audit 状态和 adoption 状态。

4. `audit_publication`
   - `new_atomic_card` 可以跳过融合审计，但不能跳过最终发布审计。
   - `merge_candidate` 和 `provenance_delta` 必须先审计融合或增量 provenance，再进入公开发布。
   - 只有 `audit_result: pass` 的卡可以进入 `llm_wiki/kb/`。

## 提速点

- 批量 drafting 摊薄 worker 启动、状态更新、commit 和 push 成本。
- 相似门只做身份判断，不把事实审计提前到每张 draft。
- audit/publication 后移到较稳定的 draft backlog 上，减少“写一张、审一张、发一张”的切换损耗。
- provenance 以增量方式处理：新来源只补充它能支撑的事实，不重写已接受卡的事实边界。

## 安全边界

- draft backlog 不是公开 KB。
- 不因追求吞吐而生成无 provenance 的草稿。
- 不把相似门输出当成事实审计结论。
- 不做枢纽页、聚类页或主题覆盖。
- 如果 batch 中某张卡触发 revise/reject/read-boundary failure，只拆出该卡处理，不拖慢整批其它草稿。
