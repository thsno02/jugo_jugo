---
schema: comparison_provenance.v3
draft_card: ../cards/ares-synthetic-data-pipeline.md
draft_provenance: ../provenance/ares-synthetic-data-pipeline.md
similarity_result: ../similarity/ares-synthetic-data-pipeline.json
existing_cards:
  - card_id: llm-wiki-persistent-wiki-alternative-mode
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md
    score: 0.0667
  - card_id: llm-wiki-query-answer-writeback
    card_path: llm_wiki/kb/cards/llm-wiki-query-answer-writeback.md
    score: 0.0625
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都极低（≤ 0.067），其中 top 3 的分数为 0。shared_tokens 仅为「替代」（top 1：draft 写「替代人工标注」vs v2 写「持久 wiki 替代模式」）与「query」（top 2：draft 用 query-answer 合成 vs v2 描述 Query 操作回写）。词形同但语义截然不同。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 mechanism 卡，来源 `arxiv-ares`，论述 ARES 用 FLAN-T5-XXL + few-shot 生成 in-domain 合成 query/answer 训练 DeBERTa-v3-Large 小判官，涵盖 weak/strong negative 两种采样策略与 fine-tune 超参，并给出数据效率与硬件门槛边界。属于「RAG 评估器训练数据合成」论点轴。

三张 v2 候选：top 1 描述 Karpathy LLM 持久 wiki 模式、top 2 描述 query 操作把好答案回写 wiki、top 3 是 idea file 抽象性。论点轴（合成数据训练小判官 vs 个人 LLM wiki 内的 query 写回）、来源（学术评估论文 vs Karpathy gist）、机制（FLAN-T5 + DeBERTa fine-tune vs LLM 写 markdown）完全不同。

## 3. 下一步的核心依据

shared_tokens 是「替代」「query」两个同形不同义的词，无语义关联。draft 引文具体到 L698-721 / L298-303 / L666-678，scope 自洽。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `ares-three-judge-rag-evaluation` / `ares-ppi-confidence-bound` 同 source 互引。
