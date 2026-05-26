---
schema: comparison_provenance.v3
draft_card: ../cards/ares-mock-rag-system-evaluation-design.md
draft_provenance: ../provenance/ares-mock-rag-system-evaluation-design.md
similarity_result: ../similarity/ares-mock-rag-system-evaluation-design.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0667
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.0625
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0625
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.07，shared_tokens 是「的」「作为」（汉语虚词 / 结构连词）。draft 标题的实质 token（ARES / mock / RAG / 准确率 / 梯度 / ranking 基准）与 v2 候选（Karpathy LLM-wiki 元描述）无术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 operational_rule 卡，来源 `arxiv-ares`，论述 ARES 论文构造 9 个准确率已知（70/72.5/.../90%，2.5% 间隔）的 mock RAG 系统作为元基准、Kendall's τ 作为客观指标、与 sampled annotations baseline 对比 ARES τ 高 0.08 且仅用 22% 标注量等。属于「RAG 评估器的 meta-benchmark 设计」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述（idea file 抽象、LLM Wiki 作为模式文件、三层架构）。论点轴（评估器自评设计 vs 个人 LLM wiki 模式）、来源、机制完全不同。

## 3. 下一步的核心依据

shared_tokens 全是虚词或结构连词，无语义关联。draft 引文具体到 L541-560 / L562-576 / L819-822，scope 自洽。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `ares-three-judge-rag-evaluation` / `ares-ppi-confidence-bound` 同 source 互引。
