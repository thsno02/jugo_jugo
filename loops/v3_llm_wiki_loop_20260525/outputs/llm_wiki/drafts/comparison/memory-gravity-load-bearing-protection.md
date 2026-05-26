---
schema: comparison_provenance.v3
draft_card: ../cards/memory-gravity-load-bearing-protection.md
draft_provenance: ../provenance/memory-gravity-load-bearing-protection.md
similarity_result: ../similarity/memory-gravity-load-bearing-protection.json
existing_cards:
  - card_id: rag-document-qa-does-not-accumulate-synthesized-knowledge
    card_path: llm_wiki/kb/cards/rag-document-qa-does-not-accumulate-synthesized-knowledge.md
    score: 0.0526
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

similarity 中 top 1 的 0.0526 来自共享 token `知识`：draft "...保护**知识**基础..."，候选 "RAG 式文档问答不积累综合**知识**"。top 2/3 分数 0.0 占位。

## 2. draft 与候选在哪里不同

- draft 描述 Miteski (2026) 的 **memory gravity 机制**：base/effective gravity 定义、四条 MUST 性质（中心性单调、碎片化单调、次线性增长、有界归一）、三力分立（gravity/utility/AUDIT）、时间衰减但结构不衰减的设计、与 PageRank/h-index 的前瞻性差异（F(i)），以及"已成承重的错误条目"失效模式由 AUDIT 兜底。来源 `arxiv-memory-as-metabolism`。
- top 1 `rag-document-qa-does-not-accumulate-synthesized-knowledge`：Karpathy gist 中 RAG 不积累综合知识的对比性描述。两者都谈"知识"，但 candidate 关注 KB 是否积累（描述层），draft 关注积累后**已成承重的条目如何保护**（机制层 + safety property）。完全不同的论点轴。
- top 2/3 是 idea file 卡，与 memory gravity 无关。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `知识` 同形，主题层零交集。判 `new_card`：直接走 publication_gate。draft 含完整公式定义、四条 MUST、failure mode 与 AUDIT 兜底关系，发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

无；典型 token 同形误中。
