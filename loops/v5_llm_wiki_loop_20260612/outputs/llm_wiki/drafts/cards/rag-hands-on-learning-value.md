---
id: rag-hands-on-learning-value
title: 从零构建 RAG 的学习价值超越教程
status: draft
card_type: practitioner-insight
tags: [learning-by-building, rag, hands-on, borrowed-understanding, teaching-tool]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [kunal-local-knowledge-base]
evidence_basis: practitioner_report
justification: ../justification/rag-hands-on-learning-value.md
canonical_concept: rag-learning-by-building
aliases: [learning by building RAG, borrowed understanding, 从零构建 RAG, 动手学习价值]
summary: >-
  据作者主张，从零走一遍 RAG 全管线（chunking→embedding→retrieval→generation）比任何教程或课程教得更多。未亲手构建过 RAG 系统的 AI 工程师是在"operating on borrowed understanding"。llm.c 的真正价值不在答案质量而在构建过程的学习收获。
related: []
---

作者提出一个强观点：对于从事 AI 相关工作的工程师，如果没有从零构建过 RAG 系统，那就是在"operating on borrowed understanding"（依赖借来的理解）。[^src-1]

其论据为实践体验对比——"Going through the RAG pipeline from scratch — chunking, embedding, retrieval, generation — taught me more about how these systems work than any tutorial or course I've taken."[^src-2]

这与对 llm.c 整体评价一致：该项目的真正价值不在于答案质量（作者承认不如 Claude/GPT-4），而在于透过构建获得对每一层架构的深入理解。作者将其定性为"a teaching tool that happens to be useful"，并观察到社区在此基础上进行的探索（更好 tokenizer、不同 embedding 方案、Apple Silicon 优化）正是"eventually produces real breakthroughs"的开源能量。[^src-3]

[^card-1]: 与 [karpathy-llmc-minimalism-philosophy] 关联——极简设计哲学的目的之一正是教育价值。
[^card-2]: 与 [local-rag-three-stage-pipeline] 关联——"从零走一遍"指的正是该三阶段管线。

[^src-1]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "My Honest Assessment After Two Weeks" P42 -- "if you're an engineer working with AI and you haven't built a RAG system from the ground up, you're operating on borrowed understanding. Full stop."
[^src-2]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "My Honest Assessment After Two Weeks" P42 -- "Going through the RAG pipeline from scratch...taught me more about how these systems work than any tutorial or course"
[^src-3]: data/raw/webpage/kunal-local-knowledge-base/markdown.md -- "My Honest Assessment After Two Weeks" P43 -- "the community building on top of it...is exactly the kind of open-source energy that eventually produces real breakthroughs"
