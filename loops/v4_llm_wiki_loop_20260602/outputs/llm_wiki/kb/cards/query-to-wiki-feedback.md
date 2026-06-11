---
id: query-to-wiki-feedback
title: 查询到 Wiki 的反馈回路
status: accepted
card_type: mechanism
tags: [llm-wiki, feedback-loop, query, knowledge-growth, dedup]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
justification: ../justification/query-to-wiki-feedback.md
canonical_concept: query-to-wiki-feedback
aliases: [查询反馈, Query-to-Wiki Feedback, 对话回写, conversation-to-wiki, 查询结果反哺 Wiki]
summary: >-
  query-to-wiki-feedback（查询反馈 / Query-to-Wiki Feedback / 对话回写）
  是 LLM Wiki 插件中将有价值的查询对话保存回 Wiki 的机制：对话内容经实体/概念提取后写入 wiki，
  保存前执行语义去重防止重复，哈希追踪防止未变对话被重复评估
related: [alias-cross-language-dedup, full-context-anti-rag, obsidian-karpathy-wiki-plugin]
---

Karpathy LLM Wiki 插件实现了**查询到 Wiki 的反馈回路**（Query-to-Wiki Feedback），允许用户将有价值的查询对话保存回 Wiki 知识库[^src-1]。

**流程机制**：
1. 用户通过会话式查询（Query wiki）获得流式回答，回答带有 [[wiki-links]] 引用[^src-2]
2. 用户判断对话有价值后，触发保存操作
3. 系统对对话内容执行**实体/概念提取**——与从源文档摄入相同的提取逻辑
4. 保存前执行**语义去重**——防止对话中产生的实体/概念与 Wiki 中已存在的页面重复[^src-1]
5. **哈希追踪**机制防止未发生变化的对话被重复评估[^src-3]

**知识增长模式**：这一机制将 Wiki 从「只读知识库」转变为「对话驱动的知识增长系统」。传统流程是单向的（源文档 -> 摄入 -> Wiki -> 查询 -> 回答），而该反馈回路构成了闭环：查询过程中产生的推理结果和综合知识被回写进 Wiki，成为后续查询的上下文[^src-1]。

**去重保障**的必要性：查询回答中 LLM 可能用不同措辞重述 Wiki 中已有知识，如果不经语义去重直接写入会导致冗余页面增长。哈希追踪则解决了用户可能多次对同一对话执行保存的幂等性问题[^src-3]。

该机制与全上下文反 RAG 架构[^card-1]形成配合——因为查询时 LLM 看到了完整 Wiki 上下文，其回答中包含的综合推理是跨多页面的推理结果，这些综合知识值得回写形成新的知识节点。别名去重系统[^card-2]在保存前的语义去重中发挥作用。

## Footnotes

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` L95 -- "Query-to-Wiki Feedback — Save valuable conversations to Wiki with entity/concept extraction, semantic dedup before save"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` L94 -- "Conversational Query — ChatGPT-style dialog with streaming Markdown and [[wiki-links]], multi-turn history"
[^src-3]: `data/raw/webpage/obsidian-community-plugin/markdown.md` L96 -- "Duplicate Save Prevention — Hash tracking prevents re-evaluation of unchanged conversations"
[^card-1]: [全上下文反 RAG 架构选择](full-context-anti-rag.md) -- 本卡描述查询结果回写 Wiki 的反馈机制，该卡论证全上下文查询产生的综合推理因跨页面推理而具有独立保存价值
[^card-2]: [别名系统与跨语言去重](alias-cross-language-dedup.md) -- 本卡在对话保存前依赖语义去重防止冗余，该卡详述去重所依赖的别名匹配与两层语义检测机制
