---
schema: comparison_provenance.v3
draft_card: ../cards/poisonedrag-retrieval-generation-two-conditions.md
draft_provenance: ../provenance/poisonedrag-retrieval-generation-two-conditions.md
similarity_result: ../similarity/poisonedrag-retrieval-generation-two-conditions.json
existing_cards:
  - card_id: llm-wiki-wiki-layer-generated-markdown-directory
    card_path: llm_wiki/kb/cards/llm-wiki-wiki-layer-generated-markdown-directory.md
    score: 0.0667
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0.0
---

## 1. draft 与候选为什么看起来相关

Top 2 / Top 3 的分数为 0.0，即没有任何 token 共享，被纳入 top 3 仅是因为没有更高分候选。Top 1 `llm-wiki-wiki-layer-generated-markdown-directory` 的 0.0667 共享 token 大概是"生成"或"文档"这类通用动词/名词，与"恶意文本 / retriever / 攻击者目标"无任何主题关系。

## 2. draft 与候选在哪里不同

draft 是 PoisonedRAG（Zou 等）的核心机制总结：把恶意文本 P 拆成 retrieval condition + generation condition 两个**必要条件**，并通过 `P = S ⊕ I` 的两段拆分由不同 LLM 操作分别满足；包含 NQ ASR 0.97、parametric bias 失败案例、Table 9 top-k 内恶意数 → ASR 函数等具体证据。

v2 候选都是 Karpathy 概念层卡片：top 1 描述 wiki 层是 LLM 生成的 markdown 目录角色；top 2 描述 idea file 的抽象性；top 3 描述 idea file 的分享逻辑。没有任何 v2 卡讨论攻击、RAG 安全、检索投毒、对抗优化。

## 3. 下一步的核心依据

由于 top 2 / top 3 score = 0 且 top 1 也仅 0.067，可断定 v2 中没有任何 PoisonedRAG 相关卡。draft 论点完整（两条件 + 拆分 + 实测数字 + 边界），无 revise 必要。结论为 `new_card`。

不选 `duplicate_skip`：v2 完全没有覆盖该主题。
不选 `provenance_delta`：没有 v2 卡 body 需要被补充。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进 publication_gate；与同 batch 的 `poisonedrag-survives-advanced-rag-and-agents`、`tkpa-graph-guided-targeted-poisoning`、`ukpa-coreference-disruption` 等卡形成 RAG-poisoning 簇。

## 5. 备注

Top 2 / Top 3 = 0.0 是 jaccard 在 v2 卡片基数（15 张）极小时的常见现象——空 token 共享下仍要凑满 top 3，候选无意义。
