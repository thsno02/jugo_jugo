---
id: attention-dilution-crossover
title: 注意力稀释与文档数交叉点
status: draft
card_type: 实验发现
tags: [attention-dilution, lost-in-the-middle, scalability, full-context-inference]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
evidence_basis: experimental_paper
justification: ../justification/attention-dilution-crossover.md
canonical_concept: attention-dilution-crossover
aliases: [attention dilution, scalability gap, document-count crossover, lost in the middle, 注意力稀释, 文档数交叉]
summary: >-
  Full-context KV cache 推理在 30 文档/67K tokens(70% 窗口填充)时优于 RAG(4.38 vs 4.08), 但在 80 文档/55-95K tokens(57-99% 填充)时因注意力稀释劣于 RAG(3.47 vs 3.64)。RAG 在 15 个主题中 13 个胜出。机制为 lost in the middle: FC 产生 17% score-1(vs Policygenius 1.2%), 557 个案例中 FC 评分 1 但 RAG>=4——模型有全部文档但无法定位相关段落。交叉点在 30-80 文档之间。
related: []
---

注意力稀释（attention dilution）导致 full-context KV cache 推理存在一个文档数交叉点（document-count crossover）：超过该阈值后 FC 质量劣于 RAG。[^src-1]

**交叉实验证据**：

| 条件 | 文档数 | Token 数 | 窗口填充 | FC 质量 | RAG 质量 | 差值 |
|------|--------|----------|----------|---------|----------|------|
| Policygenius (curated) | 30 | 67K | 70% | 4.38 | 4.08 | +0.30 |
| RepLiQA (raw) | 80/topic | 55-95K | 57-99% | 3.47 | 3.64 | -0.17 |

在 RepLiQA 上，RAG 在 15 个 FC 主题中 13 个胜出，剩余 2 个持平。Full-context 未在任何主题上获胜。[^src-2]

**机制——lost in the middle**：FC 产生 17.0% score-1 回答（vs Policygenius 上 1.2%）。交叉参照逐问题评分发现 557 个案例中 FC 评分 1 但 RAG 评分 >=4：模型拥有全部 80 篇文档但无法定位相关段落；检索器成功将范围缩小到约 2K tokens 使模型成功。[^src-3]

**关键含义**：编译质量（而非仅上下文长度）决定 FC 推理的可行性。这强化了 LLM Wiki 论点——需要高质量编译而非简单堆叠原始文档。

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "The Scalability Gap / Results" P655-670 -- "RAG consistently outperforms full-context...a complete reversal"
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "The Scalability Gap / Results" P666-670 -- "RAG wins on 13 of 15 topics"
[^src-3]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "The Scalability Gap / Results" P673-683 -- "557 cases...where FC scored 1 but RAG scored >=4"

[^card-4]: 为 [[compilation-gap]] 提供动机：规模增大后需要编译，但盲编译失败
[^card-5]: [[llm-wiki-pattern]] 的有效性条件之一
