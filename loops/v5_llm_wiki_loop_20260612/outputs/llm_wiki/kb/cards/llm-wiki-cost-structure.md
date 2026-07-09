---
id: llm-wiki-cost-structure
title: LLM Wiki 成本结构
status: accepted
card_type: quantitative-claim
tags:
- llm-wiki
- cost
- open-source
- claude-api
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- anthemcreation-en-guide
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-cost-structure.md
canonical_concept: llm-wiki-cost-structure
aliases:
- wiki cost
- zero cost
- cost structure
summary: LLM wiki 成本结构 cost-structure：开源 LLM (Llama 3) + Obsidian 完全免费；Claude API 每篇文档约 0.01-0.10 欧元；100 篇文档规模总计不到 10 欧元，维护成本低（增量 ingestion）。个人使用几乎零成本。
related:
- llm-wiki-setup-procedure
- llm-wiki-scale-limitations
---

材料提供了 LLM wiki 的具体成本数据 [^src-1]：

| 配置 | 搭建成本 | 维护成本 |
|------|---------|---------|
| Obsidian + 开源 LLM (Llama 3) | 免费 | 0 欧元/月 |
| Obsidian + Claude API | 免费 | 约 0.01-0.10 欧元/篇文档 |
| 100 篇文档 wiki (Claude) | 不到 10 欧元 | 低（增量 ingestion） |

核心结论：个人使用场景下成本几乎为零，开源 LLM 方案无任何经常性费用 [^card-1]。

[^src-1]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- "Real costs of the system" -- "Obsidian + open-source LLM (Llama 3) | Free | 0 €/month"
[^card-1]: 参见 [[llm-wiki-setup-procedure]] 关于使用开源 LLM vs Claude API 的工具选择
