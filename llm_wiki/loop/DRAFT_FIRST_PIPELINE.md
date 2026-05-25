# Material Draft First Pipeline V2

本流程是 `LOOP_DESIGN_V2.md` 的生产管线细化。目标不是把知识拆到最低粒度，而是先把 material 变成有信息量的 scoped draft cards，再用轻量 similarity 把审计成本放到最需要的位置。

## 核心顺序

```text
material / exhausted 来源
-> scoped draft card + draft provenance
-> title similarity top 3
-> comparison provenance 三问
-> draft backlog
-> publication audit 或 fusion audit
-> public adoption / provenance delta adoption
```

## 阶段定义

1. `material_to_draft`
   - 对一个已完成 source mining 或 exhausted 的来源，按候选列表批量生成 scoped draft cards 和 draft provenance。
   - 每张卡必须遵守 `CARD_CONTRACT_V2.md` 的 metadata。
   - 正文不使用强模板，但必须有知识含量，不能只是标题的 restatement 或 paraphrase。
   - 草稿只保留 `status: draft`，不进入 `llm_wiki/kb/cards/`。

2. `similarity_top3`
   - 读取 draft title 和 `llm_wiki/kb/indexes/cards.md`。
   - 用 Jieba 对标题分词，计算 Jaccard set similarity。
   - 每张 draft 只列出 top 3 accepted cards。
   - 相似度是候选选择机制，不是事实审计。

3. `comparison_provenance`
   - 只阅读 top 3 对应的 accepted A 卡和必要 provenance。
   - 对每个影响决策的 draft/A 组合回答三问：
     - 为什么认为 draft card 和 A 卡有共同点？
     - draft card 和 A 卡的不同在哪里？
     - 进行下一步操作的核心依据是什么？
   - 三问写入独立 comparison provenance；如果后续融合或增量采纳通过，必须链接回 A 卡 provenance。
   - 输出分类：`new_card`、`merge_candidate`、`provenance_delta`、`duplicate_skip`、`revise_before_gate`。

4. `draft_backlog`
   - `llm_wiki/loop/queues/draft_backlog.md` 是非公开草稿的恢复入口。
   - backlog 记录草稿路径、provenance 路径、similarity top3、comparison provenance、audit 状态和 adoption 状态。

5. `audit_publication`
   - `new_card` 进入最终 publication audit。
   - `merge_candidate` 和 `provenance_delta` 必须先审计 comparison provenance、融合依据和 A 卡链接方式。
   - `duplicate_skip` 保留 comparison provenance，但不写入公开 KB。
   - 只有 `audit_result: pass` 或 `fusion_audit_result: pass` 的动作可以进入采纳。

## 提速点

- production brain 可以先批量把 material 变成 draft，不读取 KB。
- similarity brain 只做 title-index top3，避免每张 draft 全库阅读。
- 只有 top3 需要 comparison provenance。
- new card audit 和 fusion audit 分流，避免所有 draft 都进入最高复杂度审计。
- provenance 增量链接，不重写已接受卡的事实边界。

## 安全边界

- draft backlog 不是公开 KB。
- 不因追求吞吐而生成无 provenance 或低信息量草稿。
- 不把 similarity 输出当成事实审计结论。
- 不把融合、增量 provenance 或 duplicate skip 决策留在聊天里；必须落成可链接的 provenance artifact。
- 不在没有 fusion audit 的情况下修改或链接 accepted A 卡。
- 不做枢纽页、聚类页或主题覆盖。
- 如果 batch 中某张卡触发 revise/reject/read-boundary failure，只拆出该卡处理，不拖慢整批其它草稿。
