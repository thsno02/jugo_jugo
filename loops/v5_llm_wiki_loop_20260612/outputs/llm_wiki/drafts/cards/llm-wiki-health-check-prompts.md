---
id: llm-wiki-health-check-prompts
title: LLM Wiki 健康检查提示词自愈机制
status: draft
card_type: mechanism
tags: [llm-wiki, self-healing, freshness, maintenance, health-check]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [atlan-llm-wiki-vs-rag-dynamic-20260524]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-health-check-prompts.md
canonical_concept: llm-wiki-health-check-prompts
aliases: [health check prompts, LLM health check, 健康检查提示词, self-healing mechanism]
summary: >-
  LLM wiki health check prompts 是 wiki 方案的自愈机制：周期性 LLM pass 扫描 wiki 文章，识别过时(outdated)、不完整(incomplete)或自相矛盾(contradictory)条目并标记待更新。前提条件：知识稳定、curator 主动定期执行。关键局限：不能自动传播上游变更，不适合无人干预即变化的数据。
related: [llm-wiki-three-folder-architecture]
---

LLM wiki 的健康检查提示词(health check prompts)为知识库增加了自愈机制：周期性 LLM pass 扫描 wiki 文章，识别过时、不完整或自相矛盾的条目并标记待更新。[^src-1]

该机制使 wiki 成为"主动维护"(actively maintained)而非静态的知识库——这是与传统文档站的有意义区别。[^src-2]

**运作前提**：
- 知识本身相对稳定
- Curator 主动定期执行健康检查

**关键局限**：
- 不能自动传播来自上游源的变更
- 不适合无人干预即发生变化的数据
- 企业场景需要 active metadata propagation（管道运行时自动推送变更），而非手动触发 [^src-3] [^card-1]

[^src-1]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is an LLM wiki?" P24 -- "LLM health check prompts add a self-healing mechanism: periodic passes scan wiki articles for outdated, incomplete, or contradictory entries and flag them for update."
[^src-2]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is an LLM wiki?" P25 -- "This makes the wiki actively maintained rather than static, which is a meaningful distinction from a traditional documentation site."
[^src-3]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "FAQs" P96 -- "It does not propagate changes automatically from upstream sources - making it unsuitable for data that changes without human intervention."
[^card-1]: 参见 [[llm-wiki-three-folder-architecture]] — 健康检查是三文件夹架构的维护组件
