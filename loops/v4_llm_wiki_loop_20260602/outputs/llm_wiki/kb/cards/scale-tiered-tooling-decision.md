---
id: scale-tiered-tooling-decision
title: 规模分层工具决策框架
status: accepted
card_type: distinction
tags: [llm-wiki, scale, tooling, decision-framework, infrastructure]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
justification: ../justification/scale-tiered-tooling-decision.md
canonical_concept: scale-tiered-tooling-decision
aliases: [规模分层决策, scale-tiered tooling, 工具选择阈值, infrastructure decision points, 渐进式基础设施]
summary: >-
  scale-tiered-tooling-decision（规模分层决策 / scale-tiered tooling / 工具选择阈值 /
  infrastructure decision points / 渐进式基础设施）是基于实践的 LLM Wiki 工具选择框架：
  <100 页用 grep（5min/day），100-500 页加 lifecycle 字段（10min/day），1000+ 页用
  Postgres+Dream-Cycle（cron-driven，~0）；在临界点前跳过重型基础设施
related: [llm-wiki-scale-boundary, complexity-collapse-threshold, wiki-compounding-artifact]
---

六个月的三套方案对比实践产生了一个**具体的规模分层工具决策框架**[^src-1]：

| 页面规模 | 推荐方案 | 存储 | 搜索 | 巡检 | 维护成本 |
|---|---|---|---|---|---|
| <100 页 | Karpathy v1 | Markdown | grep | 手动 | ~5 min/day |
| 100-500 页 | Rohit v2 | Markdown + lifecycle 字段 | grep + typed graph | 质量控制协议 | ~10 min/day |
| 1,000+ 页 | GBrain (Garry Tan) | Postgres + pgvector + markdown | Hybrid (BM25 + vec + graph) | 每夜 Dream Cycle cron | ~0（cron 驱动） |

核心决策原则是：**在页面数达到临界点之前，跳过重型基础设施**[^src-2]。具体而言：

- 35 页时 `grep -r "keyword" wiki/` 返回耗时 <50ms[^src-3]
- GBrain 是为 14,700+ 文件、每夜 cron 合并设计的[^src-4]
- 作者在 35 页规模下选择了 Rohit v2 子集（lifecycle 字段 + originals/ 文件夹）但跳过了 Hybrid search 和 Postgres[^src-5]
- 明确设定了升级触发点：「当页面数跨过 ~500 且 grep 开始变慢时，我会切换」[^src-6]

这一框架与 `llm-wiki-scale-boundary` 的区别在于：后者从法语社区源得出理论性的规模边界（10 至数百篇文档），本卡提供了从**同一实践者运行三个方案变体**得出的具体操作阈值和维护时间数据[^card-1]。与 `complexity-collapse-threshold` 也不同：后者描述认知层面的不可管理性，本卡描述的是**实用工具选择**的分层逻辑[^card-2]。

## Footnotes

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L47-54 -- 完整比较表：Dimension | Karpathy v1 | Rohit v2 | GBrain (Garry Tan) | What I Actually Run
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L7 -- "Skip the Postgres + Dream Cycle stuff (GBrain) until your wiki crosses ~500 pages. At 35, plain markdown + grep is faster."
[^src-3]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L42 -- "At 35 pages, grep -r 'keyword' wiki/ returns in 40ms."
[^src-4]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L43 -- "GBrain's Postgres + Dream Cycle. Garry Tan's GBrain stack deploys at 14,700+ files with nightly cron consolidation."
[^src-5]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L42-44 -- "Hybrid search (BM25 + vector + graph). The Rohit v2 essay recommends it. At 35 pages... I'll revisit at 500 pages."
[^src-6]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L90 -- "I'll switch when my page count crosses ~500 and grep starts feeling slow. Currently it returns in <50ms."
[^card-1]: [LLM Wiki 的适用规模边界](llm-wiki-scale-boundary.md) -- 该卡从法语社区来源得出理论性规模边界（10 至数百篇），本卡从同一实践者对比三个方案变体得出具体操作阈值和维护时间数据，两卡分别提供理论性与实证性的规模边界视角
[^card-2]: [复杂度崩溃阈值](complexity-collapse-threshold.md) -- 该卡描述超出规模后的认知崩溃机制，本卡描述如何在崩溃之前通过分层工具选择避免问题——前者是「为什么会崩」，后者是「怎么不崩」
