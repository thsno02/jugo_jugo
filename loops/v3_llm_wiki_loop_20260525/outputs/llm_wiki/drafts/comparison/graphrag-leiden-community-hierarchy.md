---
schema: comparison_provenance.v3
draft_card: ../cards/graphrag-leiden-community-hierarchy.md
draft_provenance: ../provenance/graphrag-leiden-community-hierarchy.md
similarity_result: ../similarity/graphrag-leiden-community-hierarchy.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0833
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.0769
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0769
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.09，shared_tokens 是「的」「作为」。draft 标题主体由具体术语（GraphRAG、Leiden、社群、分层、摘要、索引）构成，与三张 v2 候选标题（LLM Wiki / idea file / 模式 / 三层架构）没有任何术语级别的重合。Top 2 的「作为」是 draft 「作为全局摘要索引」与候选「LLM Wiki 作为模式文件」共享的连词，属于结构性虚词。整体属于 jaccard 误中。

## 2. draft 与候选在哪里不同

draft 来源 `arxiv-graphrag`（Edge et al. NeurIPS 2024 §3.1.4-3.1.5），论述 GraphRAG 用 Leiden 算法对知识图做递归社群检测，构造 C0–C3 四层 MECE 划分作为「全局摘要索引」，并描述叶/上层社群的递归 token 预算填充规则。属于「retrieval-augmented sensemaking 算法」论点轴。

三张 v2 候选全部是 Karpathy LLM-wiki 的元描述：idea file 抽象性、LLM Wiki 作为「模式文件」（pattern）、LLM Wiki 的三层（原始来源/wiki/schema）架构。它们与 draft 的「图社群检测算法 + token 预算 + map-reduce 全局摘要」在论点轴、来源（学术论文 vs Karpathy 个人帖）、机制（Leiden 算法 vs 人 LLM 分工的 wiki 维护）上完全不同。注意：v2 的「三层架构」与 draft 的「分层 Leiden」共用一个「分层」概念，但前者是 wiki 文档组织层级，后者是图社群层级——同形不同义。

## 3. 下一步的核心依据

共享 token 全是虚词或结构连词，无术语级语义重叠。v2 候选 scope 严格限于 Karpathy 帖文，没有任何可纳入 GraphRAG 实验细节的位置。draft 引文具体到行号，证据完整。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate。

## 5. 备注

- 「分层」在两端语义不同（wiki 文档层 vs 社群算法层），是 token 级噪声的典型例子。
