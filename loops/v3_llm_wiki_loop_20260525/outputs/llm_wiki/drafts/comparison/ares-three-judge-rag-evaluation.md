---
schema: comparison_provenance.v3
draft_card: ../cards/ares-three-judge-rag-evaluation.md
draft_provenance: ../provenance/ares-three-judge-rag-evaluation.md
similarity_result: ../similarity/ares-three-judge-rag-evaluation.json
existing_cards:
  - card_id: rag-document-qa-does-not-accumulate-synthesized-knowledge
    card_path: llm_wiki/kb/cards/rag-document-qa-does-not-accumulate-synthesized-knowledge.md
    score: 0.0667
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0.0
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选中 top 2 / top 3 jaccard 直接为 0，top 1 也仅 0.067，shared_tokens 仅为「rag」一词。Top 1 `rag-document-qa-does-not-accumulate-synthesized-knowledge` 是 Karpathy gist 对 RAG 式文档问答的概括描述——与 draft 一样提到「RAG」这个三字词，但论点完全不同。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 mechanism 卡，来源 `arxiv-ares`，论述 ARES 把 RAG 评估拆成三个独立的 DeBERTa-v3-Large 判官（Context Relevance / Answer Faithfulness / Answer Relevance），各对应 RAG 管线的一段失败模式，三判官不共享参数，并讨论领域漂移时 Kendall's τ 下降到 0.28-0.38 的边界。属于「RAG 评估器架构」论点轴。

Top 1 `rag-document-qa-does-not-accumulate-synthesized-knowledge`：Karpathy 描述「上传文件 → 查询时检索片段 → 生成答案」的 RAG 式体验「不会跨问题积累综合知识」。论点是「RAG 体验描述的局限性主张」，scope 限于 Karpathy 原文。它与 draft 都谈 RAG，但是「问题描述层 vs 评估器架构层」的关系——一个说 RAG 体验有什么不足，一个说怎么评估 RAG 系统。机制（无 vs 三独立 fine-tuned 判官）、来源（Karpathy gist vs ARES 论文）、读者（个人知识管理者 vs RAG 评估器使用者）都不同。

Top 2 / 3 jaccard = 0，明显无关。

## 3. 下一步的核心依据

shared_tokens 是「rag」一词的字面命中（语义飘移）。v2 top 1 卡的 scope 严格限于 Karpathy 原文对 RAG 体验的高层描述，无法承载 ARES 的评估器架构。draft 引文具体到 L730-739 / L621-626 / L207-212，scope 自洽。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `ares-synthetic-data-pipeline` / `ares-mock-rag-system-evaluation-design` / `ares-ppi-confidence-bound` 同 source 互引。

## 5. 备注

- 「RAG」是高频 token，跨论文 / 跨 source 命中频繁，但语义在「体验描述 vs 评估器架构 vs 攻击对象」之间高度发散，typical jaccard 噪声场景。
