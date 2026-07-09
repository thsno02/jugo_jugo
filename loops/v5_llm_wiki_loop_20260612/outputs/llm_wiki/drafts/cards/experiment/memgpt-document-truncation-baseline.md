---
id: memgpt-document-truncation-baseline
title: 文档截断策略的性能退化
status: draft
card_type: empirical-result
tags: [memgpt, document-truncation, baseline, context-overflow, performance-degradation]
created_time: 2026-06-12T10:31:00+08:00
edited_time: 2026-06-12T10:31:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-document-truncation-baseline.md
canonical_concept: document-truncation-degradation
aliases: [文档截断退化, document truncation, baseline context overflow strategy]
summary: >-
  MemGPT document-truncation-degradation 实验中 fixed-context baseline 为处理超量文档采用截断策略（缩短文档以塞入更多条目），但截断增加了关键片段被省略的概率，性能随文档数增加而下降。
related: [memgpt-document-qa-pagination, memgpt-lost-in-middle-motivation]
---

论文为评估 fixed-context baseline 在超出默认上下文长度时的表现，采用 document truncation 策略——截断每个文档片段使更多文档能塞入有限上下文：

**策略描述**：当 top-K 文档总 token 数超出模型上下文窗口时，等比例截断每个文档段以在同等空间内放入更多条目。[^src-1]

**观察结果**：Document truncation 导致性能下降，因为截断增加了 gold document 中关键片段（回答问题所需的具体段落）被省略的概率。随着 K 增大（需要更激进的截断），性能退化更明显。[^src-1]

**与 MemGPT 的对比**：MemGPT 不需要截断——每次检索返回完整（分页）文档片段，通过多次检索获取更多信息。因此 MemGPT 的性能不随可用文档数增加而下降。[^src-1]

然而，这一比较的公平性有前提：truncation 是一种简单 baseline 策略，更智能的压缩方法（如 selective summarization、关键句提取）可能缓解信息损失。论文未探索这些替代方案，使得 MemGPT 相对于最优 baseline 的优势尚不确定。[^src-1]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Multi-document QA -- "document truncation reduces accuracy as documents shrink as the chance of the relevant snippet (in the gold document) being omitted grows"
[^card-1]: -> memgpt-document-qa-pagination -- 本卡描述 baseline 的截断策略及其退化，该卡描述 MemGPT 的迭代检索替代方案
