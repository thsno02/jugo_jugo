---
id: retrieval-vs-maintenance
title: 检索与维护的区别
status: accepted
card_type: distinction
tags: [enterprise-wiki, retrieval, maintenance-loop, knowledge-decay]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
justification: ../justification/retrieval-vs-maintenance.md
canonical_concept: retrieval-vs-maintenance
aliases: [检索与维护, retrieval vs maintenance, 搜索层与维护循环]
summary: >-
  retrieval-vs-maintenance（检索与维护 / retrieval vs maintenance / 搜索层与维护循环）
  是企业知识系统的关键区分：大多数企业工具只是检索工具，而 LLM Wiki 的核心贡献是维护循环；
  在陈旧内容上做更好的检索只是更快地返回错误答案
related:
  - maintenance-cost-zero
  - lint-operation
  - llm-wiki-pattern
---

大多数企业知识工具（Glean、Notion AI、Confluence 搜索）本质上是**检索工具**——它们让已有内容更容易被找到，但不解决内容本身是否仍然正确的问题[^src-1]。

这一区分的核心论断是：**在陈旧知识库上的语义搜索引擎，会自信地返回来自过时文档的答案**。更好的检索叠加在糟糕的上下文之上，只是比慢速检索更快地产出错误答案[^src-2]。

个人知识管理社区早已认识到这一点。Karpathy LLM Wiki 之所以有趣，**不在于搜索层，而在于维护循环**：知识图谱保持准确，是因为 LLM 在持续做巡检、起草和调和的工作。没有这个循环，更聪明的搜索只是对可能已经不正确的笔记做更好的查询[^src-3]。

在企业层面，同样的逻辑成立，但维护问题更难——因为没有人像 Karpathy 维护自己的 vault 那样拥有对整体策展的所有权[^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Why retrieval tools don't solve this" 段 -- "Most enterprise knowledge tools on the market are retrieval tools. They make it easier to find what's been captured. Glean, Notion AI, and Confluence search all work this way."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Why retrieval tools don't solve this" 段 -- "Better retrieval over bad context delivers wrong answers more quickly than slow retrieval over bad context."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Why retrieval tools don't solve this" 段 -- "What makes Karpathy's LLM Wiki interesting is the maintenance loop, not the search layer. The graph stays accurate because the LLM is doing the linting, drafting, and reconciliation work continuously."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Why retrieval tools don't solve this" 段 -- "the maintenance problem is harder because nobody owns the curation the way Karpathy owns his vault."
