---
id: llm-wiki-cost-profile
title: LLM Wiki 成本画像
status: draft
card_type: cost_analysis
tags: [llm-wiki, cost, obsidian, claude-api, llama, open-source-llm]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [anthemcreation-fr-guide]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-cost-profile.md
canonical_concept: llm-wiki-cost-profile
aliases: [LLM wiki cost, coûts réels du système, LLM wiki 成本]
summary: >-
  LLM wiki 成本数据（2026 年 4 月）：Obsidian + 开源 LLM（Llama 3）= 零成本；Obsidian + Claude API = 每文档 0.01-0.10 EUR；100 文档 wiki（Claude）初始不到 10 EUR，后续增量维护成本低。个人使用成本"准零"。
related: [llm-wiki-vs-rag-boundary]
---

材料给出三种配置下的具体成本数据 [^src-1]：

| 配置 | 搭建成本 | 维护成本 |
|------|----------|----------|
| Obsidian + 开源 LLM（Llama 3） | 免费 | 0 EUR/月 |
| Obsidian + Claude API | 免费 | 约 0.01-0.10 EUR/文档 |
| 100 文档 wiki（Claude） | < 10 EUR | 低（增量 ingestion） |

成本结构特征：
- 搭建阶段几乎无成本（工具免费，5 分钟配置）
- 运行成本与文档量线性相关但单价极低
- 开源 LLM 路线可实现完全零成本和全私有 [^src-2]

[^src-1]: `data/raw/webpage/anthemcreation-fr-guide/markdown.md` -- "Coûts réels du système" P38-41 -- 成本表格
[^src-2]: `data/raw/webpage/anthemcreation-fr-guide/markdown.md` -- "Extensions et évolutions" P57 -- "Des LLMs locaux optimisés (type Llama) rendant le système zéro coût et entièrement privé"
