---
id: use-case-domains
title: 应用领域
status: accepted
card_type: example_pattern
tags: [llm-wiki, use-cases, applications]
created_time: 2026-06-05T00:00:00+08:00
edited_time: 2026-06-05T00:00:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/use-case-domains.md
canonical_concept: use-case-domains
aliases: [应用领域, use cases, 使用场景, application domains]
summary: >-
  use-case-domains（应用领域 / use cases / 使用场景 / application domains）列举 LLM Wiki
  的五类应用：个人成长、研究深耕、书籍阅读（类似 fan wiki）、团队/业务内部 wiki、
  以及竞争分析/尽职调查/旅行规划等知识积累场景，模式统一适用
related: [llm-wiki-pattern]
---

LLM Wiki 模式适用于多种知识积累场景[^card-1]，材料列举了五类应用领域：

1. **个人**——追踪目标、健康、心理、自我提升，归档日记、文章、播客笔记，逐步构建结构化自画像[^src-1]
2. **研究**——在数周或数月内深入一个主题，阅读论文/文章/报告，增量构建带演化论点的综合 wiki[^src-1]
3. **书籍阅读**——逐章归档，为角色、主题、情节线索建页面并记录关联。类比 Tolkien Gateway 等 fan wiki——数千互链页面覆盖角色、地点、事件[^src-2]
4. **业务/团队**——由 LLM 维护的内部 wiki，输入源包括 Slack 对话、会议记录、项目文档、客户通话。可能有人类在环审核更新[^src-3]
5. **其他**——竞争分析、尽职调查、旅行规划、课程笔记、兴趣深入——「任何需要长期积累知识并使其有组织而非分散的场景」[^src-4]

材料将这些应用作为同一模式的不同实例呈现，未建议不同场景需要不同的实现方式。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P6 -- "Personal: tracking your own goals... Research: going deep on a topic over weeks or months"
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P6 -- "Think of fan wikis like Tolkien Gateway — thousands of interlinked pages"
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P6 -- "Business/team: an internal wiki maintained by LLMs... Possibly with humans in the loop reviewing updates"
[^src-4]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P6 -- "anything where you're accumulating knowledge over time and want it organized rather than scattered"
[^card-1]: [LLM Wiki 模式](llm-wiki-pattern.md) -- 本卡列举的应用领域均是该模式的实例
