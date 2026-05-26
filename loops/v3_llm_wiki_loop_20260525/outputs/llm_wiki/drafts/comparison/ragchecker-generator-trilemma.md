---
schema: comparison_provenance.v3
draft_card: ../cards/ragchecker-generator-trilemma.md
draft_provenance: ../provenance/ragchecker-generator-trilemma.md
similarity_result: ../similarity/ragchecker-generator-trilemma.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0769
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0714
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0625
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.08，shared_tokens 仅为「的」。draft 标题的实质 token 是 RAG / faithfulness / context utilization / noise sensitivity / 三难 / 生成器，与 v2 候选（Karpathy LLM-wiki 元描述）无任何术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 distinction 卡，来源 `arxiv-ragchecker`，论述 RAGChecker 把生成器维度拆成 5 个 claim-级指标，其中 faithfulness / context utilization / noise sensitivity 三个互相牵制构成「三难」，并给出 prompt 实验数字与 GPT-4 vs Llama3-70B 的差异验证。属于「RAG 评估指标设计」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述（idea file 抽象、wiki 三层、schema 配置）。论点轴、来源类型、机制（RAG 指标拆解 + entailment 评估 vs 个人 LLM wiki 模式）完全不同。

## 3. 下一步的核心依据

shared_tokens 全是助词「的」，无语义关联。v2 候选 scope 限于 Karpathy 来源，无法承载 RAGChecker 论文的指标定义与实验数字。draft 引文具体到 L437-448 / L820-822 / L830 / L800-805 / L892-908，scope 自洽。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `ragchecker-tuning-knobs-saturate` / `ragchecker-claim-entailment-decomposition` 在 source 内互引。
