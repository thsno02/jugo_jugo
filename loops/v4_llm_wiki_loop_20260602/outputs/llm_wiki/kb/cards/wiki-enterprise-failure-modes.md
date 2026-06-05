---
id: wiki-enterprise-failure-modes
title: Wiki 企业级三大失效模式
status: accepted
card_type: distinction
tags: [llm-wiki, enterprise, scale, limitations, concurrency, access-control]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [atlan-llm-wiki-vs-rag-dynamic-20260524]
justification: ../justification/wiki-enterprise-failure-modes.md
canonical_concept: wiki-enterprise-failure-modes
aliases: [wiki企业失效模式, wiki enterprise limitations, wiki规模上限]
summary: >-
  wiki-enterprise-failure-modes（wiki企业失效模式 / wiki enterprise limitations / wiki规模上限）
  LLM wiki 在企业规模下有三大失效模式：索引溢出（50K-100K token 上限）、无原生 RBAC、
  并发写入冲突——这些不是 bug 而是设计假设的必然后果
related: []
---

LLM wiki 在企业规模下面临**三个核心限制**，它们不是 bug，而是设计假设（面向个人研究者）的必然后果[^src-1]。

**1. 索引溢出（Scale）**——index.md 必须装入上下文窗口，将实际可承载的知识量限制在 50,000-100,000 token 左右。超过此阈值，索引无法装入上下文，无论存储格式如何，都必须引入检索层[^src-2]。文章将规模称为"不是附带说明，而是整个框架"[^src-3]。

**2. 无访问控制（Access Control）**——markdown 文件夹没有原生的角色权限机制。任何拥有文件系统访问权限的 agent 都可以读取任何内容，无法实现 policy-level RBAC（例如 FinanceAgent 不应访问 HR 数据）[^src-4]。

**3. 并发写入冲突（Concurrency）**——多个同时操作的 agent 或用户更新同一个 markdown wiki 会产生竞态条件、写入冲突，甚至数据损坏，因为没有事务型数据库支持[^src-5]。Karpathy 本人明确将其方法定位于个人研究者——"bypasses RAG"的媒体框架误读了他的声明意图[^src-6]。

一个具体场景说明了三者如何同时发作：一位金融科技数据工程师有约 80 份监管笔记，wiki 方式可以运作良好；但当同一公司需要 200 名分析师跨 5 个系统查询 50,000 份文档并需要角色权限时，wiki 立即在索引溢出、访问控制和并发写入三个维度上崩溃[^src-7]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L436-437 -- "Three core limitations constrain the approach at enterprise scale... the limitations are not bugs, they are consequences of the design assumptions."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L281 -- "The 50,000-100,000 token threshold is where the wiki approach stops working reliably: beyond that, the index cannot fit in context"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L281 -- "Scale is not a minor caveat. It is the entire frame."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L436 -- "access control: markdown folders have no native role-based permissions, meaning any agent with file access can read any content"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L357 -- "multiple simultaneous agents updating a markdown wiki create race conditions, write conflicts, and potential for data corruption without transactional database support"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L357 -- "Karpathy himself scoped the approach explicitly to individual researchers - the 'bypasses RAG' framing misrepresents his stated intent."
[^src-7]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L359 -- "the LLM wiki breaks down immediately: index overflow, no access control layer, and write conflicts across simultaneous users"
