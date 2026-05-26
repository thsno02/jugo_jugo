---
schema: comparison_provenance.v3
draft_card: ../cards/ragas-reference-free-rag-evaluation.md
draft_provenance: ../provenance/ragas-reference-free-rag-evaluation.md
similarity_result: ../similarity/ragas-reference-free-rag-evaluation.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0588
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0556
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.05
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity JSON 显示 top 1/2/3 都只共享一个 token —— 汉语助词 `的`。jaccard 0.0588 实质等价于"标题里恰好都用了'的'"。三个候选标题分别是"idea file 的抽象性"、"LLM Wiki 的三层架构"、"Schema 是 LLM Wiki 的配置文档"，与 draft 的"Ragas 框架：无需 ground truth 也能评估 RAG 的三维度自动评测"在主题上完全无交集。

## 2. draft 与候选在哪里不同

- draft 描述 **Ragas RAG 评估框架的整体定位**：三正交指标（Faithfulness/Answer Relevance/Context Relevance）、reference-free、用 gpt-3.5-turbo-16k 当 judge、与 LlamaIndex/LangChain 集成、对应 EMNLP 2023 论文。
- top 1 `idea-file-abstract-vague`：Karpathy 帖文中 idea file 被有意保持抽象的设计观察。
- top 2 `llm-wiki-three-layer-architecture`：Karpathy Wiki 的三层架构（raw sources / wiki / schema）。
- top 3 `llm-wiki-schema-configuration-document`：schema 层作为 LLM 工作流配置文档。
- 三者全部来自 `karpathy-gist`，与 `arxiv-ragas` 论文在来源、论点轴（架构定义 vs 评估指标算法）、机制完全不重叠。

## 3. 下一步的核心依据

(1) 显示分数完全来自语义空洞 token `的`；(2) 表明任何 v2 候选都没有 RAG 评估的内容。因此应判 `new_card`：直接走 publication_gate。不需要 `revise_before_gate`——draft 已含动机、三维度定义、关键设计选择、边界、引文与论文行号。不需要 `provenance_delta`——没有可反向链接进 v2 卡的新证据。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

`的` 这个 token 在中文卡片标题里几乎无差别共享，是低分 jaccard 误中的主要来源，本卡是典型例子。
