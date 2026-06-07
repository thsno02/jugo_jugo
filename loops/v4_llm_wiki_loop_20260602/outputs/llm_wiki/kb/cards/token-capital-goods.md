---
id: token-capital-goods
title: Token 资本品重分类
status: accepted
card_type: concept
tags: [token-economics, capital-goods, consumables, sfas-86, accounting]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-knowledge-compounding]
justification: ../justification/token-capital-goods.md
canonical_concept: token-capital-goods
aliases: [Token资本品, tokens as capital goods, 消耗品vs资本品, token reclassification, SFAS 86 类比]
summary: >-
  token-capital-goods（Token资本品 / tokens as capital goods / SFAS 86 类比）是 Wen & Ku (2026)
  的核心理论贡献：产生持久化可查询制品的 LLM token 应从消耗品重分类为资本品，具备持久产品、
  复利回报、跨模型可继承、负折旧四个资本品属性，类比会计准则 SFAS 86 对软件开发成本的处理
related: [capitalized-latency, knowledge-compounding, supply-demand-token-dividend]
---

Wen & Ku (2026) 的核心理论贡献是提出：在动态 Agentic ROI 框架下，一部分 LLM token 应从**消耗品（consumables）重分类为资本品（capital goods）**[^src-1]。

**重分类不声称什么**：它不声称资本化的 token 比无状态检索的 token 更便宜。实证结果表明相反——Compounding 方案在原始 token 计量下从未胜过 Chunk-RAG。重分类声称的是：**原始 token 计量本身就是错误的分析单元**，正如月度总支出不适合用于比较按揭和租房的经济状况——按揭支出可能永远高于房租，但经济地位从第一个月起就已分化，因为一方在消费服务，另一方在积累资产[^src-2]。

**资本品的四个定义性属性**[^src-3]：

1. **持久产品（persistent product）**——INGEST 和回写操作产生的综合页面和实体记录具有独立于即时问答流价值的存量价值
2. **复利回报（compound returns）**——积累的 wiki 降低了覆盖区域内未来任务的边际成本，使 H(t) 的凹饱和成为数学必然
3. **跨模型代继承性（heritability across model generations）**——wiki 文件以纯 Markdown 存储，无模型依赖，可被后继模型重新 INGEST
4. **负折旧（negative discounting）**——与物理资本不同，知识 wiki 随新条目的添加和既有条目的精炼而增值

**SFAS 86 类比**：1985 年以前，美国所有软件开发成本在发生期间均作为费用处理。FASB 第 86 号准则确立：在"技术可行性"之后发生的成本应资本化而非费用化。本文对 LLM token 的主张结构上完全相同——当前普遍作为期间成本处理的支出类别，在某些配置下实际产生了经济寿命远超支出期间的持久资产[^src-4]。

无状态 token（Chunk-RAG、Long-Context）不具备以上四个属性中的任何一个——其价值在生成时刻实现并立即被丢弃[^src-5]。

供需双重红利理论将 token 资本品重分类置于更大的经济图景中——NVIDIA 供给侧降低 token 生产成本，需求侧资本化提升每个 token 的持久价值，两者结合产生双重红利[^card-1]。资本品重分类不仅适用于 token，也可推广到延迟维度——Compounding 的 81 秒中 15.3 秒属于资本化延迟而非用户等待时间[^card-2]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4 P9 -- "under the dynamic Agentic ROI framework, a subset of LLM tokens should be reclassified from consumables to capital goods"
[^src-2]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4 P9 -- "raw token accounting is the wrong unit of analysis for systems that produce persistent knowledge artifacts, in the same way that gross monthly expenditure is the wrong unit of analysis for a household making mortgage payments rather than paying rent"
[^src-3]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4 P9-10 -- "capitalized tokens display the four defining properties of capital goods: (i) persistent product... (ii) compound returns... (iii) heritability across model generations... (iv) negative discounting"
[^src-4]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4 P10 -- "Prior to 1985, all U.S. software development costs were expensed in the period in which they were incurred. The Financial Accounting Standards Board's Statement 86 changed this"
[^src-5]: `data/raw/arxiv/arxiv-knowledge-compounding/source.pdf` -- Section 3.4 P10 -- "Stateless tokens (Chunk-RAG, Long-Context) display none of these properties; their value is realized at the moment of generation and discarded immediately afterward"
[^card-1]: [Token 供需双重红利](supply-demand-token-dividend.md) -- 本卡建立 token 从消耗品到资本品的理论重分类，该卡将这一需求侧优化与 NVIDIA 供给侧优化组合为双重红利
[^card-2]: [资本化延迟与瞬时延迟](capitalized-latency.md) -- 本卡在 token 维度建立资本品重分类，该卡将同一框架推广到延迟维度（81 秒中 15.3 秒为资本化延迟）
