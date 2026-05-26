---
schema: comparison_provenance.v3
draft_card: ../cards/memgpt-main-vs-external-context.md
draft_provenance: ../provenance/memgpt-main-vs-external-context.md
similarity_result: ../similarity/memgpt-main-vs-external-context.json
existing_cards:
  - card_id: llm-wiki-wiki-layer-generated-markdown-directory
    card_path: llm_wiki/kb/cards/llm-wiki-wiki-layer-generated-markdown-directory.md
    score: 0.087
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0476
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0455
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选 jaccard 分数都低于 0.09，shared_tokens 是「和」「由」「的」这类汉语虚词。Top 1 0.087 的命中只因 draft 标题里有「角色和写规则」「由 ... 组成」，与候选「Wiki 层由 LLM 生成和维护」共享「由」「和」两个常用连接词。Top 2/3 的「的」属于汉语最普通的助词。整体属于 jaccard 误中。

## 2. draft 与候选在哪里不同

draft 是 MemGPT 论文 §2 的机制卡：把 main context（system instructions / working context / FIFO queue）与 external context（recall storage / archival storage）这五个具名分区的角色、写规则、可见性、典型误用都展开讲，引文具体到行号。它属于 agent memory architecture 这一论点轴，来源是 `arxiv-memgpt`。

候选三张：top 1 描述 Karpathy LLM-wiki 中「wiki 层是 LLM 生成 / 维护的 markdown 目录」；top 2 描述 idea file 的抽象性；top 3 描述 LLM-wiki 的「原始来源 / wiki / schema」三层架构。这三张的「层 / 架构 / 分层」属于 wiki 文档组织层，与 MemGPT 的 prompt-token 内存分层没有任何机制重叠：分层对象（人读 wiki 文件 vs LLM prompt 内的内存区）、写主体、可见性约束、出处都不同。

## 3. 下一步的核心依据

shared_tokens 全是虚词 → 关联是 token 噪声，不是语义。论点轴、来源体（arxiv vs Karpathy gist）、scope 限定都互不相容；不存在能 merge 或 provenance_delta 的 v2 卡。draft 本身证据完整（行号到位）且 scope 自洽，不需要 revise。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate。

## 5. 备注

- 「分层 / 架构」是 v2 与 v3 都会用到的高频词，但语义指向完全不同（文档组织层 vs prompt 内存区），未来或可在 tokenizer 前对这种「同形不同义」做术语命名空间区分。
