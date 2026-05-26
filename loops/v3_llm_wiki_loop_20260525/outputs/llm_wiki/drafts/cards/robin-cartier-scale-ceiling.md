---
id: robin-cartier-scale-ceiling
title: Karpathy 风 LLM Wiki 的实战上限：约 200 页 / 100K tokens 后必须降级到子 wiki 或 RAG
status: draft
card_type: operational_rule
tags: [#llm-wiki, #scale-limit, #robin-cartier, #deduplication, #temporal-signal]
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
source_ids: [robin-cartier-llm-knowledge-bases]
provenance_card: ../provenance/robin-cartier-scale-ceiling.md
aliases: [LLM wiki scaling, 200 page ceiling, dedup fragility, temporal weakness]
related: [karpathy-gist-bookkeeping-burden, robin-cartier-schema-as-product-doc]
---

Robin Cartier 作为实践者给 Karpathy 模式做了"实战裁决"，给出**四条具体的缩放局限**，每一条都是规划 LLM Wiki 工程时必须事先承认的工程约束：

1. **规模上限约 200 页 / 100K tokens**——这是 index + 页内容总和能塞进 LLM 上下文窗口的实际门槛。一旦超过，LLM 就不能在单次推理里"看到全索引"，必须切子 wiki 或引入检索层。这条规则直接决定了什么领域用 wiki，什么用 RAG。
2. **去重在规模放大时变得脆弱**——LLM 自身的去重判断没有确定性保障，"the wiki will accumulate near-duplicate pages over time"。换言之，没有显式去重守卫（embedding 相似度阈值 + 规则化合并流程）的话，wiki 会**慢慢长出近似重复页面**，并且这种漂移很难一次性补救。
3. **时间信号过弱**——单一"last updated"字段无法表达"首次见到 / 最近见到"这种关系型存储能轻松提供的趋势追踪能力。如果你需要"哪些事实在多少时间内被多源印证"这种时间趋势分析，wiki 模式不适合。
4. **天然单用户**——没有访问控制、没有 merge conflict 解决机制、没有 audit trail（除了 log 文件）。多人写就要么解决治理问题，要么改用别的形态。

**实操含义（Robin 自己给的选择矩阵）**：

| 场景 | 适合的模式 |
|------|------------|
| 个人 second brain / 研究 / 学习 | LLM wiki（Karpathy 模式） |
| 操作自动化、趋势追踪、流水线投喂的知识 | 结构化关系型知识库 |
| 企业级、百万级文档 | RAG（或混合） |

强项侧也写清楚了：
- **可靠性**——LLM 直接读 index，没有检索 miss；
- **零基础设施**——没有 embedding 模型、没有向量库、没有分块流水线；
- **可读性极佳**——人和 LLM 看的是同一份 markdown；
- **git 版本控制天然成立**。

边界与误用：
- "200 页"是经验值，受底层模型上下文窗口直接影响，未来模型上下文涨了上限会涨；
- "无 RAG infrastructure"也是双刃剑——小规模优势在大规模会变成缺陷；
- 把这套局限当成"反对 wiki 模式"是误用——真正含义是**选择合适的工具到合适的规模**。

## References

Robin Cartier, "Karpathy's LLM Knowledge Base: A Practitioner's Verdict" (2026-04-08)，在 robin-cartier-llm-knowledge-bases 页面 "Strengths and limits" + "When to use it vs alternatives" 两节给出。

- 源路径：`data/raw/webpage/robin-cartier-llm-knowledge-bases/text.txt`（行 39–47 四条局限；行 49–58 选择矩阵；行 35–37 强项侧）。

## Footnotes

- 200 页规则原文（行 41）："Scale ceiling around ~200 pages / ~100K tokens of index + content. Beyond that, the LLM can't hold the index in context and you need sub-wikis or a retrieval layer."
- 去重脆弱原文（行 43）："Deduplication is LLM-dependent and fragile at scale — without a deterministic guard, the wiki will accumulate near-duplicate pages over time."
- 时间信号弱原文（行 45）："Temporal signal is weak: a single 'last updated' field loses the trend-tracking capability a relational store would give you (first_seen / last_seen)."
- 单用户原文（行 47）："Single-user by default: no access control, no merge conflicts, no audit trail beyond the log file."
- 选择矩阵原文（行 49–57）：表格内容逐行复述。
