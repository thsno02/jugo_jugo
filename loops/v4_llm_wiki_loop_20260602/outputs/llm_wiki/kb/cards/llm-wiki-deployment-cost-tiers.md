---
id: llm-wiki-deployment-cost-tiers
title: LLM Wiki 部署成本三档
status: accepted
card_type: source_claim
tags: [llm-wiki, cost, deployment, open-source, claude-api, llama]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [anthemcreation-en-guide]
justification: ../justification/llm-wiki-deployment-cost-tiers.md
canonical_concept: llm-wiki-deployment-cost-tiers
aliases: [部署成本三档, deployment cost tiers, 零成本配置, real costs]
summary: >-
  llm-wiki-deployment-cost-tiers（部署成本三档 / deployment cost tiers / 零成本配置）是该来源给出的
  LLM Wiki 部署成本结构化数据：三种配置从完全免费（Obsidian + Llama 3）到极低成本（Claude API
  每文档 0.01-0.10 欧元），100 文档 wiki 总搭建成本低于 10 欧元
related: [compounding-cost-honesty, full-stack-locality, llm-wiki-scale-boundary, maintenance-cost-zero]
---

该来源以结构化表格呈现了 LLM Wiki 三种部署配置的实际成本[^src-1]：

| 配置 | 搭建成本 | 维护成本 |
|---|---|---|
| Obsidian + 开源 LLM（Llama 3） | 免费 | 0 欧元/月 |
| Obsidian + Claude API | 免费 | 每摄入文档约 0.01 至 0.10 欧元 |
| 100 文档 wiki（Claude） | 低于 10 欧元 | 低（增量摄入） |

这一数据的意义在于：它将个人使用场景定性为**成本几乎为零**[^src-2]。开源 LLM 路线可以实现**零经常性成本且完全私有**[^src-3]，而 Claude API 路线的 100 文档总成本低于 10 欧元——远低于任何向量数据库或托管 RAG 服务的月费。

这一部署层面的成本分析与学术层面的 token 消耗分析构成互补视角：Wen & Ku (2026) 证明 Compounding 方案在绝对 token 消耗上永远高于 Chunk-RAG[^card-1]，但本卡显示从终端用户的实际支出角度，这种 token 开销折算为极低的现金成本。全栈本地配置（Llama 3 路线）进一步消除了隐私顾虑，这与全栈本地性概念直接呼应[^card-2]。

## Footnotes

[^card-1]: [复利方案在原始 token 成本上从不胜出](compounding-cost-honesty.md) -- 本卡展示部署层面的实际现金成本（0-10 欧元），该卡从 token 消耗角度证明 Compounding 永远不低于 Chunk-RAG；两者从不同抽象层解释成本：用户体验层 vs 计算资源层
[^card-2]: [全栈本地性](full-stack-locality.md) -- 本卡的 Llama 3 零成本配置是全栈本地性的经济学补充——不仅数据和计算均在本地，而且经济成本归零

[^src-1]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- L40-44 -- "| Obsidian + open-source LLM (Llama 3) | Free | 0 €/month | | Obsidian + Claude API | Free | ~0.01 to 0.10 € per ingested doc | | Wiki of 100 documents (Claude) | Less than 10 € | Low (incremental ingestions) |"
[^src-2]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- L7 -- "The cost is almost zero for personal use, with open-source LLMs for no recurring cost."
[^src-3]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- L59 -- "Optimized local LLMs (like Llama) making the system zero-cost and fully private"
