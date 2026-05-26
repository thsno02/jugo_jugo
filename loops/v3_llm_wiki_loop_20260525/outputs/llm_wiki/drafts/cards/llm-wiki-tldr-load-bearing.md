---
id: llm-wiki-tldr-load-bearing
title: TL;DR 强制规则比 index 更省 context window——load-bearing 设计
status: draft
card_type: operational_rule
tags: [#karpathy-llm-wiki, #tldr, #context-window, #operational-rule]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
provenance_card: ../provenance/llm-wiki-tldr-load-bearing.md
aliases: [TL;DR enforcement, 50-char TL;DR, context window saving]
related: [karpathy-llm-wiki-three-layers, llm-wiki-schema-is-most-important, llm-wiki-contradictions-are-assets, llm-wiki-rohit-v2-improvements, robin-cartier-scale-ceiling]
---

## 主张

Jim Liu 在 6 个月 35 页的实战观察：

> "TL;DR enforcement saves your context window more than the index does. Every page in my wiki has a ≤50-character TL;DR at the top. When I ask Claude 'what did I decide about RAG vs LLM wiki?', it can scan 35 TL;DRs in a single read instead of trying to compress 35 full pages."
> —— `text.txt:38`

Karpathy gist 提到过"TL;DR on top"的想法，但只是一笔带过；Jim 给它一个准确定位：**load-bearing**（承重，结构上不可缺）。

## 为什么 TL;DR 比 index 更省 context

| 工具 | 用什么辅助 query | context 占用 |
|---|---|---|
| `index.md` | 主题 → 页路径的导航地图 | 一份 index 本身就要全文读，且只告诉你"有这个页"，不告诉你"页说了什么" |
| TL;DR 集合 | 每页 ≤50 字符的核心结论 | 35 页 × 50 字 ≈ 1.75K 字符，远小于 35 页全文，且 query 时**直接是答案候选** |

index 解决 **发现** 问题（有哪些页）；TL;DR 解决 **筛选 + 召回** 问题（哪页相关 + 它说的什么）。query 阶段后者承担更多负载，所以"省 context"上 TL;DR 比 index 更显著。

## 字符上限的工程意义

≤50 字符不是审美选择，是 **强制函数**：

- 写得超过 50 字符就放不进 TL;DR 区 → 作者被迫提炼。
- 50 字符大致是一行宽，scan 时不需要换行 / 不需要分页 → 35 页一屏可见。
- LLM 在 1 次 Read 中拿到 35 个"可执行的回答候选"，可以马上决定**继续读哪几页全文**而不是把所有页都拉进上下文。

## 操作含义

- **schema.md 必须把"TL;DR ≤ N 字符"列为强制字段**，否则作者会随手写两段总结，TL;DR 失去 scan 价值。
- **TL;DR 是结论性陈述，不是页标题的复述**——否则等于浪费一行。
- TL;DR 必须随页内容更新同步更新；否则会产生与正文不一致的"虚假答案"。
- 在 lint 时应额外检查：TL;DR 缺失 / 超长 / 与页正文不同步。

## 边界

- 这个规则在 35 页量级下显著有效；千页规模下 TL;DR 集合可能也开始过大，需要分层（先 category 摘要、再页 TL;DR）。
- TL;DR 是"页的最简表达"，对那些只能用图 / 表 / 公式表达的页不适用；强制 50 字符会失真。
- 字符上限可调，但**必须存在**——没有上限的 TL;DR 退化为"另一个 summary 段"。

## References

- 主张：`data/raw/webpage/openaitoolshub-six-months/text.txt:38`。
- Karpathy gist 提及 TL;DR 但不强调：`text.txt:38`。

## Footnotes

- 原文主张：`text.txt:38` —— "TL;DR enforcement saves your context window more than the index does. Every page in my wiki has a ≤50-character TL;DR at the top. When I ask Claude 'what did I decide about RAG vs LLM wiki?', it can scan 35 TL;DRs in a single read instead of trying to compress 35 full pages. Karpathy's gist mentions the TL;DR-on-top idea once; in practice it's load-bearing."
- Jim 的页结构定位：`text.txt:36`（35 页 + 80 raw input + log.md + schema.md）。
