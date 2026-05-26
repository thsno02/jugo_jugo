---
schema: comparison_provenance.v3
draft_card: ../cards/poisonedrag-baselines-isolate-two-conditions.md
draft_provenance: ../provenance/poisonedrag-baselines-isolate-two-conditions.md
similarity_result: ../similarity/poisonedrag-baselines-isolate-two-conditions.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0833
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0769
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0667
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 分数都低于 0.09，shared_tokens 仅为「的」。draft 标题包含 PoisonedRAG / 基线 / 条件 / 丢 等术语，与 v2 候选（Karpathy LLM-wiki 元描述）没有任何术语级 token 重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 distinction 卡，来源 `arxiv-poisonedrag`，论述 PoisonedRAG 论文 Table 7 里五个基线（Naive Attack / Corpus Poisoning / GCG / Disinformation / Prompt Injection）分别「丢」掉 retrieval-side 或 generation-side 哪一个条件，并把消融结果（ASR / F1）对应到机制理解上。属于「RAG 攻击实验设计 / 消融论证」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述（idea file 抽象、三层架构、schema 配置）。论点轴（攻击实验 vs 知识库模式）、来源（学术论文 vs 个人帖 / gist）、读者（安全研究者 vs 个人知识管理者）完全不同。v2 候选 scope 严格限于 Karpathy 来源，无法承载 RAG 攻击实验数据。

## 3. 下一步的核心依据

shared_tokens 全是「的」，无语义重叠。draft 证据完整（行号 L1221-1244 / L1321-1360 / L110-151 全部到位），scope 自洽，不需要 revise。无任何 v2 卡可 merge 或 provenance_delta。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate。

## 5. 备注

- draft 与 sibling 卡 `poisonedrag-retrieval-generation-two-conditions` 关系紧密（前者用消融证后者用定义），但属于同 source 的内部互引，与 v2 KB 无关。
