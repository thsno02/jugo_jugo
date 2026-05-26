---
schema: comparison_provenance.v3
draft_card: ../cards/zep-graphiti-three-tier-graph.md
draft_provenance: ../provenance/zep-graphiti-three-tier-graph.md
similarity_result: ../similarity/zep-graphiti-three-tier-graph.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0588
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0.0
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity JSON 中 top 1 的 0.0588 完全来自共享 token `三层`：draft 标题 "Zep/Graphiti 用三层子图..."，候选 "LLM Wiki 的三层架构"。两者都在讲"分三层"的结构，但所指对象天差地别。top 2/3 分数 0.0，纯为占位。

## 2. draft 与候选在哪里不同

- draft 描述 Zep/Graphiti 的**三层时序知识图 $\mathcal{G}=(\mathcal{N},\mathcal{E},\phi)$**：episodic 子图存原始消息、semantic 子图存抽取实体与事实、community 子图存 label-propagation 簇摘要；mechanism 是 agent 记忆建模。来源是 `arxiv-zep`。
- top 1 `llm-wiki-three-layer-architecture` 描述 Karpathy LLM Wiki 的**三层架构**：raw sources / wiki / schema，对象是文档 + markdown + 规则，不是知识图。来源是 `karpathy-gist`。
- 两者都用"三层"作为组织隐喻，但层的物体（图节点子集 vs 文档/markdown/配置文档）、目的（agent memory vs 协作型 wiki）、机制（label propagation / bi-temporal edges vs LLM-maintained markdown）、来源完全不同。

## 3. 下一步的核心依据

(1) 与 (2) 表明这是结构隐喻同名（"三层"）下的不同系统——Graphiti 是 agent 记忆图、LLM Wiki 是文档协作架构。判 `new_card`：draft 应作为独立卡进入 publication_gate。不是 `provenance_delta`，因为 Karpathy 那张三层架构卡的 scope 已严格限定在 "该来源对架构分层" 上，不需要 Zep 证据补充；不是 `revise_before_gate`，draft 已含形式化定义、心理学动机、社区算法选择理由、增量更新边界。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate；可在 `related` 字段加上 v2 `llm-wiki-three-layer-architecture` 作为对比阅读链接（非合并）。

## 5. 备注

"三层"是结构通用词，未来若有第三种"三层 X"出现，预计仍会落入同一 jaccard 桶；建议下一轮在 tokenizer 停用词上加入"三层"以降噪。
