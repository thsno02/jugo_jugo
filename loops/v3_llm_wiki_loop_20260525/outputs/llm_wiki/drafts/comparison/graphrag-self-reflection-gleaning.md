---
schema: comparison_provenance.v3
draft_card: ../cards/graphrag-self-reflection-gleaning.md
draft_provenance: ../provenance/graphrag-self-reflection-gleaning.md
similarity_result: ../similarity/graphrag-self-reflection-gleaning.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0667
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0625
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0556
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.07，shared_tokens 仅为「的」。draft 标题的实质 token（GraphRAG / self-reflection / gleaning / 大 chunk / 实体召回 / 损失）与 v2 候选（Karpathy LLM-wiki 元描述）无术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 operational_rule 卡，来源 `arxiv-graphrag`，论述 GraphRAG 的多轮 self-reflection gleaning 循环：用 logit bias = 100 强制 yes/no、追加 prompt「MANY entities were missed」、最多 3 轮把实体召回提升到 3 倍；并给出 HotPotQA × gpt-4-turbo × 600/1200/2400 chunk × 0-3 轮的实体数表，含 chunk size 与 gleaning 的折衷分析。属于「实体抽取召回 prompt 工程」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述。论点轴（gleaning prompt engineering vs 个人 LLM wiki 模式）、来源、机制完全不同。

## 3. 下一步的核心依据

shared_tokens 全是「的」，无语义关联。draft 引文具体到 L60-77 / L1441-1487 / L769-774，scope 自洽。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `graphrag-global-sensemaking-pipeline` / `graphrag-leiden-community-hierarchy` 同 source 互引。
