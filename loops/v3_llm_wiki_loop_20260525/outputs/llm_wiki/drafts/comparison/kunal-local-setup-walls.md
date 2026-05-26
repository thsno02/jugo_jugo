---
schema: comparison_provenance.v3
draft_card: ../cards/kunal-local-setup-walls.md
draft_provenance: ../provenance/kunal-local-setup-walls.md
similarity_result: ../similarity/kunal-local-setup-walls.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1176
  - card_id: rag-document-qa-does-not-accumulate-synthesized-knowledge
    card_path: llm_wiki/kb/cards/rag-document-qa-does-not-accumulate-synthesized-knowledge.md
    score: 0.1111
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0667
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- 候选 #1 共享 `文档`、`的`：draft 标题里"文档预处理"撞 v2 "配置文档"。机械撞分。
- 候选 #2 共享 `rag`、`文档`：draft 标题里"本地 RAG"撞 v2 "RAG 式文档问答"——这是本批中**比较接近真共享**的低分撞，两边都谈到 RAG，但论点完全不同（见下）。
- 候选 #3 共享 `的`，纯虚词撞分。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-schema-configuration-document`：仅讲 Karpathy gist 的 schema 配置文档。和"本地 LLM 部署的三个工程障碍"无任何关系。
- 候选 #2 `rag-document-qa-does-not-accumulate-synthesized-knowledge`：讲 Karpathy gist 中"RAG 式文档问答不积累综合知识"这一**性质论断**。draft 是"本地 RAG 自建的三堵墙"（macOS Clang 不支持 OpenMP / 缺 document loader / CPU 推理太慢）——一组**操作守则**，来源是 Kunal 实战经验。两者都提"RAG"但一个谈知识系统性质、一个谈本地部署工程难题，没有论点轴重叠。
- 候选 #3：完全无关。
- draft 的来源是 `kunal-local-knowledge-base/text.txt` L95–129，记录 Kunal 两周实战中的三堵墙与改进路径展望。v2 KB 中没有任何"本地 LLM 工程实战 / 部署摩擦"卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无本地部署系列卡。
- 不是 `provenance_delta`：候选 #2 虽然也提 "RAG"，但论点是 wiki 模式 vs RAG 的性质对比，无法接收 draft 的工程障碍清单作为引证。
- 不是 `duplicate_skip`：无覆盖。
- 不是 `revise_before_gate`：draft 已有三堵墙完整引文、修复路径、Kunal 的总体定性、边界自检；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控可考察"它解释了为什么纯本地 RAG 直到 2026 年还没真正普及"那一句是否过度引申（90% 数字是 draft 解读，不在 Kunal 原文中）。

## 5. 备注

- 与同源 `kunal-llm-c-rag-misinterpretation` 形成"Kunal 的术语误读 vs Kunal 的实战价值"对照卡组。
- 候选 #2 的低分撞是本批少见的"两张 RAG 卡机械撞分但论点轴正交"案例：一个是 wiki 性质论断、另一个是本地工程清单。
